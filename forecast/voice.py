"""Voice-model forecast: when will Anthropic ship a speech model of its own?

    python3 voice.py [DATE]          # compute, write output/voice_forecast.json, freeze a snapshot, append log rows
    python3 voice.py DATE --print    # compute and print only; writes nothing

This is not the family engine. A first speech model is a first-of-kind event
with no cadence history, so there are no gaps to fit. The model is small on
purpose and every step is printed:

  1. base rate      events per lab-year in a reference class of frontier labs
                    (data/voice_reference_class.csv), shrunk toward Anthropic's
                    own record of zero events
  2. signals        a documented mapping from the open rows of
                    data/voice_signals.csv to hazard multipliers, and, once a
                    first-party "coming weeks" statement exists, the repo's
                    measured 6-18 day lead time
  3. market         a log-odds blend with a prediction-market price where a
                    market has been mapped to a rung (data/voice_params.json,
                    market.map); none exists as of 2026-11-10

Three questions ("rungs", criteria in data/voice_params.json): A any
first-party speech model with external access, B general availability, C
native speech-to-speech. B and C are derived from A.

Records, same conventions as the family forecast (append-only, one per origin):
  output/voice_forecast.json             the live forecast
  history/voice_forecast_<date>.json     frozen snapshot, never edited
  voice_forecast_log.csv                 one row per rung x horizon, never edited
A second run for the same date restores the snapshot and adds no rows. These
files are separate from the family files on purpose: nothing here touches
history/forecast_*.json or forecast_log.csv, and the family scorecard numbers
do not include voice rows.

Resolution lives in data/voice_resolutions.json and is set by hand on the day
a rung resolves (DAILY_RUNBOOK.md, "Voice model").
"""
from __future__ import annotations

import csv
import glob
import json
import math
import os
import re
import shutil
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

from engine.data import holiday_mask                          # noqa: E402
from engine.market import pool                                # noqa: E402
from engine.modifiers import election_mask, thanksgiving_mask  # noqa: E402


def _no_nan(o):
    """NaN and infinity are not valid JSON and break browser parsers: write null instead."""
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if isinstance(o, dict):
        return {k: _no_nan(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_no_nan(v) for v in o]
    return o



MODEL_VERSION = "voice-v1"
RUNGS = ["A", "B", "C"]
LOG = "voice_forecast_log.csv"
LOG_COLS = ["as_of", "model_version", "target", "checkpoint", "p_base", "p_model", "p_market", "p_final", "p_low", "p_high",
            "median", "q10", "q90"]
VOICE_Q = re.compile(r"(?i)(anthropic|claude).*\b(voice|audio|speech|speak)|\b(voice|audio|speech)\b.*(anthropic|claude)")
SPEC_STEP_DOWN = {"yes": "partial", "partial": "no", "no": None}


# ---------------------------------------------------------------- inputs
def load_inputs():
    P = json.load(open("data/voice_params.json"))
    ref = pd.read_csv("data/voice_reference_class.csv", keep_default_na=False)
    sig = pd.read_csv("data/voice_signals.csv", keep_default_na=False)
    res = json.load(open("data/voice_resolutions.json")) if os.path.exists("data/voice_resolutions.json") else {}
    return P, ref, sig, res


def base_rates(ref, as_of):
    """Pooled, self and shrunken annual rates from the reference class, as of the origin."""
    asof = pd.Timestamp(as_of)
    events, days, self_days = 0, 0.0, None
    for _, r in ref.iterrows():
        start = pd.Timestamp(r.era_start)
        if r.status == "shipped" and r.first_speech_date and pd.Timestamp(r.first_speech_date) <= asof:
            events += 1
            days += (pd.Timestamp(r.first_speech_date) - start).days
        else:                                   # censored at the origin
            days += max((asof - start).days, 0)
        if r.lab == "Anthropic":
            self_days = max((asof - start).days, 1)
    years = days / 365.25
    pooled = (events + 0.5) / years
    self_rate = 0.5 / (self_days / 365.25) if self_days else pooled
    return dict(n_labs=int(len(ref)), events=int(events), lab_years=round(years, 2), anthropic_years=round((self_days or 0) / 365.25, 2),
                pooled=pooled, self=self_rate, shrunk=math.sqrt(pooled * self_rate))


# ---------------------------------------------------------------- hazard
def _class_best(sig, asof, cls, gw, sw, step_down=False):
    """Best open prep signal of a class at the origin: (weight, most recent sighting date, signal_id)."""
    rows = sig[(sig.stage == "prep") & (sig.status == "open") & (sig.cls == cls) & (pd.to_datetime(sig.first_seen_date) <= asof)]
    best = None
    for _, r in rows.iterrows():
        spec = SPEC_STEP_DOWN.get(r.specific, None) if step_down else r.specific
        w = gw.get(r.source_grade, 0.0) * (sw.get(spec, 0.0) if spec else 0.0)
        if best is None or w > best[0]:
            best = (w, r.signal_id)
    if best is None:
        return None
    last = pd.to_datetime(rows.first_seen_date).max()   # the clock runs from the most recent sighting (as in v3d)
    return best[0], last, best[1]


def hazard_path(P, R, sig, as_of, scenario="central"):
    """Daily hazard over the horizon, and what went into it. scenario: central | low | high | base."""
    asof = pd.Timestamp(as_of)
    H = int(P["horizon_days"])
    days = pd.date_range(asof, periods=H, freq="D")
    S = P["signals"]
    info = {}
    open_ = sig[(sig.status == "open") & (pd.to_datetime(sig.first_seen_date) <= asof)]
    program = open_[(open_.stage == "program") & open_.source_grade.isin(["A", "B"])]
    credited = len(program) > 0 and scenario in ("central", "high")
    lam = R["pooled"] if credited else R["shrunk"]
    info["program"] = dict(credited=bool(credited), signals=list(program.signal_id), multiplier=(R["pooled"] / R["shrunk"] if credited else 1.0))
    mult = np.ones(H)
    info["classes"] = {}
    if scenario != "base":
        pr = S["prep"]
        rho = 1.0 if scenario == "high" else pr["rho"]
        for cls in ("infra", "client", "report", "soft"):
            b = _class_best(sig, asof, cls, pr["grade_weight"], pr["specific_weight"], step_down=(scenario == "low"))
            if not b or b[0] <= 0:
                continue
            w, last, sid = b
            age = (days - last).days.values.astype(float)
            m = pr["cap"] ** (rho * w * 0.5 ** (np.maximum(age, 0) / pr["half_life_days"]))
            mult *= m
            info["classes"][cls] = dict(signal=sid, weight=w, last_seen=str(last.date()), multiplier_today=float(m[0]))
    info["prep_multiplier_today"] = float(mult[0])
    lam_t = lam * mult
    h = 1.0 - np.exp(-lam_t / 365.25)
    low = holiday_mask(days) | thanksgiving_mask(days) | election_mask(days)
    h = np.where(low, 1.0 - (1.0 - h) ** P["calendar"]["factor"], h)
    info["annual_hazard_today"] = float(lam_t[0])
    info["annual_hazard_base"] = float(lam)

    # second clock: a dated first-party statement (none as of 2026-11-10)
    surv_extra = np.ones(H)
    info["dated"] = []
    if scenario != "base":
        for stage in ("dated_weeks", "dated_months"):
            rows = open_[(open_.stage == stage) & (open_.source_grade == "A")]
            if not len(rows):
                continue
            first = pd.to_datetime(rows.first_seen_date).max()
            cfg = S[stage]
            if stage == "dated_weeks":
                lg = np.log(np.array(cfg["lead_days"], dtype=float))
                mu, sd = float(lg.mean()), float(max(lg.std(ddof=1), 0.3))
            else:
                mu, sd = math.log(cfg["median_days"]), float(cfg["sigma"])
            from scipy.stats import norm
            t = (days - first).days.values.astype(float) + 1.0          # lead if the release were on that day
            G = norm.cdf((np.log(np.maximum(t, 1e-9)) - mu) / sd)
            elapsed = max((asof - first).days, 0)
            G0 = norm.cdf((math.log(max(elapsed, 1e-9)) - mu) / sd) if elapsed > 0 else 0.0
            Gc = np.clip((G - G0) / max(1 - G0, 1e-9), 0, 1)             # conditional on not having happened yet
            surv_extra *= 1.0 - cfg["p_hit"] * Gc
            info["dated"].append(dict(stage=stage, since=str(first.date()), median_lead_days=round(math.exp(mu), 1), p_hit=cfg["p_hit"]))
    surv = np.cumprod(1.0 - h) * surv_extra
    cdf = 1.0 - surv
    return days, cdf, info


def ladder(P, R, cdf_a):
    """Rungs B and C from rung A: with a share on the same day, otherwise after an exponential delay."""
    L = P["ladder"]
    pmf = np.diff(np.concatenate([[0.0], cdf_a]))
    n = len(pmf)
    t = np.arange(n, dtype=float)

    def delayed(share_same, mean_days):
        g = np.diff(np.concatenate([[0.0], 1.0 - np.exp(-(t + 1) / mean_days)]))   # delay pmf on days 0..n-1
        conv = np.convolve(pmf, g)[:n]
        return np.cumsum(share_same * pmf + (1 - share_same) * conv)

    cdf_b = delayed(L["B_same_day_share"], float(L["B_delay_mean_days"]))
    follow = R["pooled"] if L["C_follow_rate"] == "pooled" else float(L["C_follow_rate"])
    cdf_c = delayed(L["C_first_share"], 365.25 / follow)
    return cdf_b, cdf_c


def quantile(days, cdf, q):
    i = int(np.searchsorted(cdf, q))
    return str(days[i].date()) if i < len(days) else ">" + str(days[-1].date())


# ---------------------------------------------------------------- markets
def read_markets(P, as_of):
    files = sorted(f for f in glob.glob("data/raw/markets_*.csv") if os.path.basename(f)[8:18] <= as_of)
    out = dict(file=(files[-1] if files else None), mapped=[], candidates=[], near_misses=P["market"].get("near_misses", []),
               last_search=P["market"].get("last_search", ""))
    if not files:
        return out
    mk = pd.read_csv(files[-1])
    used = set()
    for m in P["market"].get("map", []):
        for _, r in mk[mk.platform == m["platform"]].iterrows():
            g = re.search(m["pattern"], str(r.question))
            if not g:
                continue
            try:
                dt = str(pd.Timestamp(g.group(1)).date())
            except Exception:
                continue
            try:
                vol = float(str(r.volume).split()[0].replace(",", ""))
            except Exception:
                vol = 0.0
            liquid = m["platform"] in ("Polymarket", "Kalshi") and "mana" not in str(r.volume) and vol >= P["market"]["liquid_volume_usd"]
            out["mapped"].append(dict(platform=m["platform"], rung=m["rung"], date=dt, question=str(r.question), prob=float(r.prob),
                                      volume=str(r.volume), url=str(r.url), weight=(P["market"]["weight_liquid"] if liquid else P["market"]["weight_thin"])))
            used.add(str(r.question))
    for _, r in mk.iterrows():
        if VOICE_Q.search(str(r.question)) and str(r.question) not in used:
            out["candidates"].append(dict(platform=r.platform, question=str(r.question), prob=float(r.prob), volume=str(r.volume), url=str(r.url)))
    return out


# ---------------------------------------------------------------- forecast
def compute(as_of):
    P, ref, sig, res = load_inputs()
    R = base_rates(ref, as_of)
    asof = pd.Timestamp(as_of)
    paths = {}
    for sc in ("base", "central", "low", "high"):
        days, cdf_a, info = hazard_path(P, R, sig, as_of, sc)
        cdf_b, cdf_c = ladder(P, R, cdf_a)
        if (res.get("A") or {}).get("resolved_date"):
            # Rung A has happened. A rung still open did not resolve with it, so only the delay is left:
            # exponential, hence the same curve from any later origin (documented in voice_params.json, ladder).
            t = np.arange(len(cdf_a), dtype=float) + 1.0
            follow = R["pooled"] if P["ladder"]["C_follow_rate"] == "pooled" else float(P["ladder"]["C_follow_rate"])
            cdf_b = 1.0 - np.exp(-t / float(P["ladder"]["B_delay_mean_days"]))
            cdf_c = 1.0 - np.exp(-t * follow / 365.25)
        paths[sc] = dict(A=cdf_a, B=cdf_b, C=cdf_c, info=info)
    mk = read_markets(P, as_of)

    def at(cdf, date):
        j = (pd.Timestamp(date) - asof).days       # "by DATE" includes DATE
        return float(cdf[j]) if 0 <= j < len(cdf) else None

    out = dict(as_of=as_of, model_version=MODEL_VERSION, generated_by="forecast/voice.py", horizons=P["horizons"], rungs={},
               base_rate=dict(R, method=P["base_rate"]["method"]), hazard=paths["central"]["info"],
               hazard_low=paths["low"]["info"]["annual_hazard_today"], hazard_high=paths["high"]["info"]["annual_hazard_today"])
    for k in RUNGS:
        meta = P["rungs"][k]
        rr = (res.get(k) or {})
        rung = dict(title=meta["title"], short=meta["short"], criteria=meta["criteria"], resolved=bool(rr.get("resolved_date")),
                    resolution=(rr if rr.get("resolved_date") else None), by={})
        c = paths["central"][k]
        for hz in P["horizons"]:
            if pd.Timestamp(hz) < asof:
                continue
            p_sig = at(c, hz)
            lo, hi = sorted([at(paths["low"][k], hz), at(paths["high"][k], hz)])
            m = [x for x in mk["mapped"] if x["rung"] == k and x["date"] == hz]
            p_mkt = m[0]["prob"] if m else None
            p_fin = float(pool(p_sig, p_mkt, m[0]["weight"])) if m else p_sig
            rung["by"][hz] = dict(base=at(paths["base"][k], hz), signals=p_sig, market=p_mkt,
                                  market_weight=(m[0]["weight"] if m else None), final=p_fin, low=min(lo, p_sig), high=max(hi, p_sig))
        rung.update(median=quantile(days, c, 0.5), q10=quantile(days, c, 0.1), q90=quantile(days, c, 0.9),
                    median_low=quantile(days, paths["high"][k], 0.5), median_high=quantile(days, paths["low"][k], 0.5),
                    median_base=quantile(days, paths["base"][k], 0.5))
        # quarter-end points for a reader who wants the curve (after signals, before any market blend)
        qe = [x for x in pd.date_range(asof, periods=17, freq="QE") if (x - asof).days < len(c)]
        rung["curve"] = {str(x.date()): round(at(c, str(x.date())), 4) for x in qe}
        out["rungs"][k] = rung
    out["signals"] = [dict(id=r.signal_id, code=r.signal_code, stage=r.stage, cls=r.cls, first_seen=r.first_seen_date, grade=r.source_grade,
                           specific=r.specific, status=r.status, verified=r.verified, url=r.source_url, headline=r.headline, note=r.note)
                      for _, r in sig.sort_values("first_seen_date", ascending=False).iterrows()]
    out["reference_class"] = [dict(lab=r.lab, era_start=r.era_start, first_speech_date=r.first_speech_date, model=r.first_speech_model,
                                   kind=r.kind, days=((pd.Timestamp(r.first_speech_date) - pd.Timestamp(r.era_start)).days if r.first_speech_date
                                                      else (asof - pd.Timestamp(r.era_start)).days),
                                   status=r.status, url=r.source_url, verified=r.verified) for _, r in ref.iterrows()]
    out["markets"] = mk
    out["criteria"] = dict(does_not_count=P["does_not_count"], already_shipped_note=P["already_shipped_note"], grading_note=P["grading_note"])
    out["assumptions"] = dict(base_rate=P["base_rate"]["status"], program=P["signals"]["program"], prep={k: v for k, v in P["signals"]["prep"].items()},
                              dated_weeks=P["signals"]["dated_weeks"], dated_months=P["signals"]["dated_months"], counter=P["signals"]["counter"],
                              calendar=P["calendar"], ladder=P["ladder"], range=P["range"],
                              market={k: v for k, v in P["market"].items() if k not in ("map", "near_misses", "_map_format", "last_search")})
    out["cases"] = P["cases"]
    return out


def check(out):
    """Sanity checks; returns a list of problems (empty when fine)."""
    bad = []
    for k, r in out["rungs"].items():
        vals = [v[c] for v in r["by"].values() for c in ("base", "signals", "final", "low", "high") if v[c] is not None]
        if any(not (0 <= v <= 1) for v in vals):
            bad.append(f"rung {k}: probability outside [0, 1]")
        for col in ("base", "signals", "final"):
            seq = [v[col] for v in r["by"].values()]
            if any(b < a - 1e-9 for a, b in zip(seq, seq[1:])):
                bad.append(f"rung {k}: {col} not non-decreasing across horizons")
    for hz, a in ({} if out["rungs"]["A"]["resolved"] else out["rungs"]["A"]["by"]).items():
        for k in ("B", "C"):
            if out["rungs"][k]["by"][hz]["signals"] > a["signals"] + 1e-9:
                bad.append(f"rung {k} above rung A at {hz}")
    return bad


def append_log(out):
    new = not os.path.exists(LOG)
    if not new and any(line.startswith(out["as_of"] + "," + out["model_version"] + ",") for line in open(LOG)):
        print(f"{LOG} already has {out['as_of']} {out['model_version']} - not appending")
        return 0
    n = 0
    with open(LOG, "a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(LOG_COLS)
        for k, r in out["rungs"].items():
            if r["resolved"]:
                continue
            for hz, v in r["by"].items():
                w.writerow([out["as_of"], out["model_version"], "voice_" + k, hz, round(v["base"], 4), round(v["signals"], 4),
                            "" if v["market"] is None else round(v["market"], 4), round(v["final"], 4), round(v["low"], 4), round(v["high"], 4),
                            r["median"], r["q10"], r["q90"]])
                n += 1
    return n


def summary(out):
    L = [f"Voice model forecast {out['as_of']} ({out['model_version']})",
         f"  base rate: {out['base_rate']['events']} events in {out['base_rate']['lab_years']} lab-years; pooled {out['base_rate']['pooled']:.2f}/yr, "
         f"Anthropic alone {out['base_rate']['self']:.2f}/yr, shrunken {out['base_rate']['shrunk']:.2f}/yr",
         f"  after signals: {out['hazard']['annual_hazard_today']:.2f}/yr today (program x{out['hazard']['program']['multiplier']:.2f}, "
         f"prep x{out['hazard']['prep_multiplier_today']:.2f}); range {out['hazard_low']:.2f}-{out['hazard_high']:.2f}/yr",
         f"  markets mapped: {len(out['markets']['mapped'])}; unmapped voice-like questions in {out['markets']['file']}: {len(out['markets']['candidates'])}"]
    for c in out["markets"]["candidates"]:
        L.append(f"    candidate (read its rule, then map it in data/voice_params.json or add it to near_misses): {c['platform']}: {c['question']} = {c['prob']:.2f}")
    for k, r in out["rungs"].items():
        if r["resolved"]:
            L.append(f"  {k} {r['short']}: RESOLVED {r['resolution']['resolved_date']}")
            continue
        L.append(f"  {k} {r['short']}: " + ", ".join(f"by {hz} {v['final']:.0%} ({v['low']:.0%}-{v['high']:.0%})" for hz, v in r["by"].items())
                 + f"; median {r['median']}, 80% {r['q10']} to {r['q90']}")
    a = out["rungs"]["A"]
    if not a["resolved"]:
        L.append("  decomposition, rung A: " + "; ".join(
            f"{hz}: base {v['base']:.0%} -> signals {v['signals']:.0%} -> market {'none' if v['market'] is None else format(v['final'], '.0%')}"
            for hz, v in a["by"].items()))
    return "\n".join(L)


def run(as_of):
    """Compute, freeze and log. One forecast per origin; returns (made, out)."""
    os.makedirs("history", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    snap = f"history/voice_forecast_{as_of}.json"
    if os.path.exists(snap):
        shutil.copy(snap, "output/voice_forecast.json")
        print(f"{snap} exists: the voice forecast for this origin is already frozen; not recomputed, no log rows added")
        return False, json.load(open(snap))
    out = compute(as_of)
    bad = check(out)
    if bad:
        raise SystemExit("voice forecast failed its checks, nothing written: " + "; ".join(bad))
    json.dump(_no_nan(json.loads(json.dumps(out, default=float))), open("output/voice_forecast.json", "w"), indent=1, allow_nan=False)
    shutil.copy("output/voice_forecast.json", snap)
    n = append_log(out)
    print(summary(out))
    print(f"wrote output/voice_forecast.json, {snap}; {n} rows appended to {LOG}")
    return True, out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        date = args[0]
    else:
        from datetime import datetime
        from zoneinfo import ZoneInfo
        date = datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d")
    if "--print" in sys.argv:
        o = compute(date)
        print(summary(o))
        print("checks:", check(o) or "ok")
    else:
        run(date)
