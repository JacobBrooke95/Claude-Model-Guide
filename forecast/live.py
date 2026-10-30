"""Live forecast as of a date → output/forecast.json.

    python3 live.py 2026-10-30

Uses the stage-1b configuration (output/tuning_v2_ranking.csv) with the signal
layer on and the 30% EWMA pool. Several posterior seeds are averaged so the published numbers do
not depend on one MCMC chain.
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict, replace

import numpy as np
import pandas as pd

from engine import market as mk
from engine import params as P
from engine.data import FAMILIES, d, family_history, load_competitors, load_releases, load_signals, weekday_profile
from engine.forecast import Config, FitCache, forecast, summarize, H, TARGETS
from engine.signals import SignalModel

AS_OF = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "2026-10-30"
SEEDS = [0]  # n_seeds=4 inside the config averages four chains

rel, comp, sig = load_releases(), load_competitors(), load_signals()
best = pd.read_csv("output/tuning_v2_ranking.csv").config.iloc[0]          # e.g. weibull|changepoint|w0.0|hl0.75
err, trend, w, hl = best.split("|")
BASE = Config(err=err, trend=trend, w_wave=float(w[1:]), half_life=None if hl == "hlNone" else float(hl[2:]))
# final = v2 cadence + signals (no absence term) pooled 70/30 with the repo's EWMA; no competitor term
FULL = replace(BASE, signals=True, absence=False, w_ewma=0.3, n_seeds=4)
MODEL_VERSION = "v3c-post-review"

variants = {"cadence": replace(BASE, n_seeds=4), "with_signals": FULL}
res = {}
info_keep = {}
for name, cfg in variants.items():
    acc = {}
    for s in SEEDS:
        fc, info = forecast(rel, comp, sig, AS_OF, replace(cfg, seed=s), FitCache(), explain=True)
        for k, (p, t) in fc.items():
            a = acc.setdefault(k, [np.zeros(H), 0.0])
            a[0] += p / len(SEEDS); a[1] += t / len(SEEDS)
        if s == 0:
            info_keep[name] = info
    res[name] = acc

asof = d(AS_OF)
days = pd.date_range(asof, periods=H, freq="D")
out = dict(as_of=str(asof.date()), config=dict(stage1=best, **{k: v for k, v in asdict(FULL).items()}),
           targets={}, markets={}, params={}, signals={}, cadence_params=info_keep["cadence"].get("cadence"),
           wave_params=info_keep["cadence"].get("wave"))

# daily cdf for charts (first 180 days)
for name, acc in res.items():
    for k, (p, t) in acc.items():
        tgt = out["targets"].setdefault(k, {})
        tgt[name] = summarize(p, t, asof)
        tgt[name]["cdf180"] = [round(float(x), 4) for x in np.cumsum(p)[:180]]
        tgt[name]["pmf180"] = [round(float(x), 5) for x in p[:180]]
        for label, dt in (("by_nov15", "2026-11-15"), ("by_nov30", "2026-11-30"), ("by_dec31", "2026-12-31"),
                          ("by_jan31", "2027-01-31"), ("by_mar31", "2027-03-31")):
            j = (d(dt) - asof).days
            tgt[name][label] = float(np.cumsum(p)[j]) if j < H else None

# markets: ladder vs model vs blend
mkts = pd.read_csv("data/raw/markets_2026-10-30.csv")
lad = mk.ladders(mkts)
for fam, L in lad.items():
    p = res["with_signals"][fam][0]
    cdf = np.cumsum(p)
    rows = []
    for _, r in L.iterrows():
        j = (r.date - asof).days  # "released by DATE" includes DATE
        if j < 0 or j >= H:
            continue
        pm = float(cdf[j])
        rows.append(dict(date=str(r.date.date()), market_raw=r.raw, market=float(r.prob), model=pm,
                         blend=float(mk.pool(pm, r.prob)), volume=r.volume))
    out["markets"][fam] = rows

# signals visible now, per family
sm = SignalModel(sig, rel, AS_OF, rho=FULL.rho, cap=FULL.cap)
out["signal_class_params"] = sm.par
for f in FAMILIES:
    hist = family_history(rel, f, AS_OF)
    v = sm.visible(f, hist[-1])
    out["signals"][f] = [dict(code=r.signal_code, cls=r.cls, first_seen=str(r.first_seen.date()), grade=r.grade,
                              note=r.note, source=r.source) for _, r in v.iterrows()]
    out["signals"][f + "_detail"] = info_keep["with_signals"].get("signals", {}).get(f)
if "competitor" in info_keep["with_signals"]:
    out["competitor"] = info_keep["with_signals"]["competitor"]

# release parameters
gen, gen_info = P.generation_clock(AS_OF, ["2026-12-31", "2027-03-31", "2027-06-30", "2027-12-31"])
out["params"]["generation6"] = dict(prob_by=gen, **gen_info)
for f in FAMILIES:
    med = out["targets"][f]["with_signals"]["median"]
    at = med if not med.startswith(">") else "2027-06-30"
    # P(next model is a new major) = P(generation clock fires before this family's median date)
    pg, _ = P.generation_clock(AS_OF, [at])
    names = P.next_names(rel, f, list(pg.values())[0])
    if f in ("fable", "mythos"):
        # Azure catalog row `claude-fable-5-5` (10/13) and the T3 commit naming "Fable 5.5" (10/19)
        names = P.apply_named_signals(names, [f"Claude {f.capitalize()} 5.5"])
    out["params"][f] = dict(names=names, price=P.price_change(rel, f), colaunch=P.colaunch_rate(rel, f),
                            swe_bench_pro=P.swe_pro_projection(f, at), median_date_used=at)
wp = weekday_profile(rel, AS_OF)
out["params"]["weekday_share"] = dict(zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], (wp / 7).round(3).tolist()))

out["model_version"] = MODEL_VERSION
json.dump(out, open("output/forecast.json", "w"), indent=1, default=float)

# forward log: append this run's calls so they can be scored when they resolve
import csv, os
logp = "forecast_log.csv"
new = not os.path.exists(logp)
if not new and any(line.startswith(out["as_of"] + "," + MODEL_VERSION + ",") for line in open(logp)):
    print("forecast_log.csv already has", out["as_of"], MODEL_VERSION, "- not appending")
    sys.exit(0)
with open(logp, "a", newline="") as fh:
    wr = csv.writer(fh)
    if new:
        wr.writerow(["as_of", "model_version", "target", "p_by_2026-11-15", "p_by_2026-11-30", "p_by_2026-12-31",
                     "p_by_2027-01-31", "p_by_2027-03-31", "median", "q10", "q90"])
    for k in TARGETS:
        t = out["targets"][k]["with_signals"]
        wr.writerow([out["as_of"], MODEL_VERSION, k] + [round(t[x], 4) if t[x] is not None else "" for x in
                    ("by_nov15", "by_nov30", "by_dec31", "by_jan31", "by_mar31")] + [t["median"], t["q10"], t["q90"]])
for k in TARGETS:
    a = out["targets"][k]["cadence"]; b = out["targets"][k]["with_signals"]
    print(f"{k:9s} cadence p30={a['p30']:.2f} med={a['median']} | +signals p7={b['p7']:.2f} p30={b['p30']:.2f} "
          f"p90={b['p90']:.2f} med={b['median']} 80%=[{b['q10']}, {b['q90']}] by11/30={b['by_nov30']:.2f} by12/31={b['by_dec31']:.2f}")
for fam, rows in out["markets"].items():
    for r in rows:
        if r["date"] in ("2026-11-05", "2026-11-10", "2026-11-19", "2026-11-30", "2026-12-31", "2027-01-31"):
            print(f"  {fam:7s} {r['date']} model={r['model']:.2f} market={r['market']:.2f} blend={r['blend']:.2f}")
