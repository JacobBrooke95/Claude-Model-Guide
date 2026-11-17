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
                    measured 6-18 day lead time. A dated first-party statement
                    that names no speech model (signal V9, "more to share
                    later this year") is not run as a release clock outright:
                    the published curve is a mixture, (1 - w) x the forecast
                    without that clock + w x the forecast with it, w =
                    signals.unnamed_statement.unnamed_statement_weight in
                    data/voice_params.json (an owner's judgement). The
                    weighted part lapses after the row's `expires` date.
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

A separate, informational question (data/voice_tracking.json: "any material
voice update by 2026-12-31") is carried next to the rungs, in the snapshot's
`tracking` list and in voice_tracking_log.csv. It never feeds rungs A-C.

    python3 voice.py --selftest      # mixture checks: w = 0 and w = 1 reproduce the reference numbers

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



MODEL_VERSION = "voice-v1.1"      # v1.1 (2026-11-17): half-weight mixture for an unnamed dated statement; EXPERIMENTS.md V7
RUNGS = ["A", "B", "C"]
LOG = "voice_forecast_log.csv"
TRACK_LOG = "voice_tracking_log.csv"
TRACK_COLS = ["as_of", "id", "deadline", "p", "p_low", "p_high", "anchor_date", "basis"]
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


def statement_rows(sig, as_of):
    """Open dated first-party statements that name no speech model (specific 'no', grade A or B).
    Returns (live, lapsed): live rows may run the weighted clock; a row lapses the day after its `expires` date."""
    asof = pd.Timestamp(as_of)
    rows = sig[(sig.status == "open") & sig.stage.isin(["dated_weeks", "dated_months"]) & (sig.specific == "no")
               & sig.source_grade.isin(["A", "B"]) & (pd.to_datetime(sig.first_seen_date) <= asof)]
    exp = rows.expires if "expires" in rows.columns else pd.Series("", index=rows.index)
    gone = exp.map(lambda x: bool(x) and pd.Timestamp(x) < asof)
    return rows[~gone], rows[gone]


def hazard_path(P, R, sig, as_of, scenario="central", statement=False):
    """Daily hazard over the horizon, and what went into it. scenario: central | low | high | base.
    statement=True also runs the dated clock for live statements that name no model (see statement_rows);
    compute() mixes the two paths."""
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
            # a statement that names the model, on a first-party page, always runs; one that names none only when asked
            rows = open_[(open_.stage == stage) & (open_.source_grade == "A") & (open_.specific != "no")]
            if statement:
                live, _ = statement_rows(sig, as_of)
                rows = pd.concat([rows, live[live.stage == stage]])
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


# ---------------------------------------------------------------- tracking question (informational)
def _effective_days(d0, d1, factor):
    """Days from d0 to d1 inclusive, low-hazard days (holiday freeze, Thanksgiving, election day) counted at `factor`."""
    if pd.Timestamp(d1) < pd.Timestamp(d0):
        return 0.0
    days = pd.date_range(d0, d1, freq="D")
    low = holiday_mask(days) | thanksgiving_mask(days) | election_mask(days)
    return float(np.where(low, factor, 1.0).sum())


def tracking(as_of, path="data/voice_tracking.json"):
    """Informational questions next to the rungs (never an input to them). Each has a deadline, criteria, a
    resolution set by hand, and a list of dated judgements ("anchors"). Between judgements the probability
    follows one rule: the latest anchor fixes a constant daily rate over the effective days that were left
    on its date, and each day that passes with nothing shipped leaves fewer days:
        p(d) = 1 - (1 - p_anchor) ** (effective days left on d / effective days left on the anchor date)."""
    if not os.path.exists(path):
        return []
    T = json.load(open(path))
    factor = json.load(open("data/voice_params.json"))["calendar"]["factor"]
    asof, out = pd.Timestamp(as_of), []
    for q in T.get("questions", []):
        res = q.get("resolution") or {}
        anchors = sorted((a for a in q.get("anchors", []) if pd.Timestamp(a["date"]) <= asof), key=lambda a: a["date"])
        item = dict(id=q["id"], question=q["question"], short=q.get("short", q["question"]), deadline=q["deadline"], counts=q.get("counts", []),
                    does_not_count=q.get("does_not_count", []), reason=q.get("reason", {}), label=q.get("label", ""), rule=q.get("rule", ""),
                    resolution=(res if res.get("outcome") else None), days_left=int((pd.Timestamp(q["deadline"]) - asof).days),
                    p=None, p_low=None, p_high=None, anchor=(anchors[-1] if anchors else None), state="open")
        if res.get("outcome") in ("yes", "no"):
            item.update(state="resolved " + res["outcome"], p=(1.0 if res["outcome"] == "yes" else 0.0))
        elif asof > pd.Timestamp(q["deadline"]):
            item.update(state="deadline passed, not resolved by hand yet: grade it No unless something shipped", p=0.0)
        elif anchors:
            a = anchors[-1]
            e0, e1 = _effective_days(a["date"], q["deadline"], factor), _effective_days(as_of, q["deadline"], factor)
            f = (lambda p0: None if p0 is None else float(1.0 - (1.0 - p0) ** (e1 / e0)) if e0 > 0 else 0.0)
            item.update(p=f(a["p"]), p_low=f(a.get("low")), p_high=f(a.get("high")))
        out.append(item)
    return out


def append_tracking_log(out):
    """One row per question per origin, append-only, like the forecast log."""
    have = set()
    if os.path.exists(TRACK_LOG):
        have = {(r["as_of"], r["id"]) for r in csv.DictReader(open(TRACK_LOG))}
    rows = [t for t in out.get("tracking", []) if t["p"] is not None and (out["as_of"], t["id"]) not in have]
    if not rows:
        return 0
    new = not os.path.exists(TRACK_LOG)
    with open(TRACK_LOG, "a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(TRACK_COLS)
        for t in rows:
            w.writerow([out["as_of"], t["id"], t["deadline"], round(t["p"], 4), "" if t["p_low"] is None else round(t["p_low"], 4),
                        "" if t["p_high"] is None else round(t["p_high"], 4), (t["anchor"] or {}).get("date", ""),
                        t["state"] if t["state"] != "open" else "rule from anchor"])
    return len(rows)


# ---------------------------------------------------------------- forecast
def compute(as_of):
    P, ref, sig, res = load_inputs()
    R = base_rates(ref, as_of)
    asof = pd.Timestamp(as_of)
    paths = {}
    live, lapsed = statement_rows(sig, as_of)
    us = P["signals"].get("unnamed_statement", {})
    w = float(us.get("unnamed_statement_weight", 0.0)) if len(live) else 0.0
    if not 0.0 <= w <= 1.0:
        raise SystemExit("unnamed_statement_weight must be between 0 and 1")
    alt = {}
    for sc in ("base", "central", "low", "high"):
        days, cdf_a, info = hazard_path(P, R, sig, as_of, sc)
        if len(live) and sc != "base":
            # mixture of two readings of the statement: no effect, and a promise of a speech model (full clock).
            # Rungs B and C are linear in rung A's curve, so mixing A first is the same as mixing each rung.
            _, cdf_on, info_on = hazard_path(P, R, sig, as_of, sc, statement=True)
            if sc == "central":
                alt = dict(none=dict(zip(RUNGS, (cdf_a,) + ladder(P, R, cdf_a))), full=dict(zip(RUNGS, (cdf_on,) + ladder(P, R, cdf_on))),
                           dated=info_on["dated"])
            cdf_a = (1.0 - w) * cdf_a + w * cdf_on
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
        if alt:     # the two readings the published number is mixed from (central scenario, before any market blend)
            rung["statement_alt"] = dict(
                by={hz: dict(none=at(alt["none"][k], hz), full=at(alt["full"][k], hz)) for hz in rung["by"]},
                median_none=quantile(days, alt["none"][k], 0.5), median_full=quantile(days, alt["full"][k], 0.5))
        out["rungs"][k] = rung
    exp_of = lambda r: (r.expires if "expires" in r.index else "")
    out["statement"] = None
    if len(live):
        r0 = live.sort_values("first_seen_date").iloc[-1]
        out["statement"] = dict(signals=list(live.signal_id), weight=w, since=r0.first_seen_date, expires=exp_of(r0) or None,
                                days_left=((pd.Timestamp(exp_of(r0)) - asof).days if exp_of(r0) else None), url=r0.source_url,
                                clock=alt.get("dated", []), rule=us.get("rule", ""), status=us.get("status", ""))
    out["statement_lapsed"] = [dict(signal=r.signal_id, since=r.first_seen_date, expired=exp_of(r), url=r.source_url) for _, r in lapsed.iterrows()]
    out["tracking"] = tracking(as_of)
    out["signals"] = [dict(id=r.signal_id, code=r.signal_code, stage=r.stage, cls=r.cls, first_seen=r.first_seen_date, grade=r.source_grade,
                           specific=r.specific, status=r.status, verified=r.verified, url=r.source_url, headline=r.headline, note=r.note,
                           expires=(r.expires if "expires" in sig.columns else ""))
                      for _, r in sig.sort_values("first_seen_date", ascending=False).iterrows()]
    out["reference_class"] = [dict(lab=r.lab, era_start=r.era_start, first_speech_date=r.first_speech_date, model=r.first_speech_model,
                                   kind=r.kind, days=((pd.Timestamp(r.first_speech_date) - pd.Timestamp(r.era_start)).days if r.first_speech_date
                                                      else (asof - pd.Timestamp(r.era_start)).days),
                                   status=r.status, url=r.source_url, verified=r.verified) for _, r in ref.iterrows()]
    out["markets"] = mk
    out["criteria"] = dict(does_not_count=P["does_not_count"], already_shipped_note=P["already_shipped_note"], grading_note=P["grading_note"])
    out["assumptions"] = dict(base_rate=P["base_rate"]["status"], program=P["signals"]["program"], prep={k: v for k, v in P["signals"]["prep"].items()},
                              dated_weeks=P["signals"]["dated_weeks"], dated_months=P["signals"]["dated_months"],
                              unnamed_statement=P["signals"].get("unnamed_statement"), counter=P["signals"]["counter"],
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
    st = out.get("statement")
    if st:
        L.append(f"  statement {', '.join(st['signals'])} ({st['since']}, names no model): mixture weight {st['weight']:g}"
                 + (f"; lapses after {st['expires']} ({st['days_left']} days left)" if st["expires"] else ""))
        for k, r in out["rungs"].items():
            if "statement_alt" in r:
                L.append(f"    {k}: " + ", ".join(f"{hz} {v['none']:.0%} | {r['by'][hz]['signals']:.0%} | {v['full']:.0%}" for hz, v in r["statement_alt"]["by"].items())
                         + f"  (no effect | published | full strength); median {r['statement_alt']['median_none']} | {r['median']} | {r['statement_alt']['median_full']}")
    for x in out.get("statement_lapsed", []):
        L.append(f"  !! statement {x['signal']} lapsed after {x['expired']} with no rung resolved: its clock no longer contributes. By hand: set its status to "
                 f"'lapsed' in data/voice_signals.csv and record the undelivered promise in LEARNINGS.md (DAILY_RUNBOOK.md, Voice watch).")
    for t in out.get("tracking", []):
        L.append(f"  tracking (informational, not a rung): {t['short']}: " + (f"{t['p']:.0%}" if t["state"] == "open" else t["state"])
                 + (f" ({t['p_low']:.0%}-{t['p_high']:.0%})" if t["state"] == "open" and t["p_low"] is not None else "")
                 + (f"; {t['days_left']} days left; judgement of {t['anchor']['date']} ({t['anchor']['p']:.0%}) run down by rule" if t["state"] == "open" and t["anchor"] else ""))
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
    nt = append_tracking_log(out)
    print(summary(out))
    print(f"wrote output/voice_forecast.json, {snap}; {n} rows appended to {LOG}, {nt} to {TRACK_LOG}")
    return True, out


def selftest():
    """The mixture's two ends, checked against numbers issued before it existed.
    w = 0: every probability, range and date of the frozen 2026-11-17 snapshot (voice-v1), exactly.
    w = 1: the 'full strength' reading reported on 2026-11-17 for origin 2026-11-18 (rung A 28 / 56 / 67 / 78%)."""
    global load_inputs
    real = load_inputs

    def with_w(w):
        def f():
            P, ref, sig, res = real()
            P["signals"].setdefault("unnamed_statement", {})["unnamed_statement_weight"] = w
            return P, ref, sig, res
        return f
    try:
        load_inputs = with_w(0.0)
        got, ref = compute("2026-11-17"), json.load(open("history/voice_forecast_2026-11-17.json"))
        assert got["statement"] and got["statement"]["weight"] == 0.0, "no live unnamed statement on 2026-11-17: the test would prove nothing"
        for k in RUNGS:
            for hz, v in ref["rungs"][k]["by"].items():
                for c in ("base", "signals", "final", "low", "high"):
                    assert got["rungs"][k]["by"][hz][c] == v[c], f"w=0 differs from the frozen snapshot: {k} {hz} {c}"
            for c in ("median", "q10", "q90", "median_low", "median_high", "median_base"):
                assert got["rungs"][k][c] == ref["rungs"][k][c], f"w=0 differs from the frozen snapshot: {k} {c}"
        load_inputs = with_w(1.0)
        got = compute("2026-11-18")
        want = {"A": [0.2844, 0.5650, 0.6742, 0.7760], "B": [0.2121, 0.4846, 0.6235, 0.7573], "C": [0.1932, 0.3992, 0.4961, 0.6124]}
        for k, ws in want.items():
            for (hz, v), x in zip(got["rungs"][k]["by"].items(), ws):
                assert abs(v["signals"] - x) < 5e-4, f"w=1 differs from the full-strength reference: {k} {hz} {v['signals']:.4f} vs {x}"
        assert got["rungs"]["A"]["median"] == "2027-03-01", got["rungs"]["A"]["median"]
        load_inputs = with_w(0.5)
        mid = compute("2026-11-18")
        for k in RUNGS:
            for hz, v in mid["rungs"][k]["by"].items():
                a = mid["rungs"][k]["statement_alt"]["by"][hz]
                assert abs(v["signals"] - 0.5 * (a["none"] + a["full"])) < 1e-12, "w=0.5 is not the midpoint"
        load_inputs = real
        late = compute("2027-01-01")
        assert late["statement"] is None and late["statement_lapsed"], "the statement did not lapse after its expiry date"
        assert "statement_alt" not in late["rungs"]["A"]
    finally:
        load_inputs = real
    print("voice selftest ok: w=0 equals the frozen 2026-11-17 snapshot; w=1 equals the full-strength reference; w=0.5 is the midpoint; the statement lapses on 2027-01-01")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit(0)
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
