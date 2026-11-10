"""Live forecast as of a date → output/forecast.json.

    python3 live.py 2026-10-30

Uses the stage-1b configuration (output/tuning_v2_ranking.csv) with the signal
layer on and the 30% EWMA pool. Several posterior seeds are averaged so the published numbers do
not depend on one MCMC chain.
"""
from __future__ import annotations

import json
import os
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
# v3d (2026-11-01, Jacob-approved): the signal clock runs from the most recent A/B
# sighting per class, and live runs count sightings first seen on the run date
FULL = replace(BASE, signals=True, absence=False, w_ewma=0.3, n_seeds=4, sig_recent=True, same_day=True)
MODEL_VERSION = "v3e"  # v3d + US election day as a low-hazard day (2026-11-02)

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
# checkpoints: the next six month-ends; C1 is the first at least 10 days out, C2 the one after
MONTH_ENDS = [m for m in pd.date_range(asof, periods=8, freq="ME") if m >= asof][:7]
_far = [m for m in MONTH_ENDS if (m - asof).days >= 10]
CHECKPOINTS = [str(_far[0].date()), str(_far[1].date())]
out = dict(as_of=str(asof.date()), checkpoints=CHECKPOINTS, config=dict(stage1=best, **{k: v for k, v in asdict(FULL).items()}),
           targets={}, markets={}, params={}, signals={}, cadence_params=info_keep["cadence"].get("cadence"),
           wave_params=info_keep["cadence"].get("wave"))

# daily cdf for charts (first 180 days)
for name, acc in res.items():
    for k, (p, t) in acc.items():
        tgt = out["targets"].setdefault(k, {})
        tgt[name] = summarize(p, t, asof)
        tgt[name]["cdf180"] = [round(float(x), 4) for x in np.cumsum(p)[:180]]
        tgt[name]["pmf180"] = [round(float(x), 5) for x in p[:180]]
        cdf = np.cumsum(p)
        tgt[name]["by"] = {str(m.date()): (float(cdf[(m - asof).days]) if (m - asof).days < H else None) for m in MONTH_ENDS}

# markets: ladder vs model vs blend
import glob, os
_mfiles = sorted(f for f in glob.glob("data/raw/markets_*.csv") if os.path.basename(f)[8:18] <= str(asof.date()))
MARKET_FILE = _mfiles[-1]
mkts = pd.read_csv(MARKET_FILE)
# keep only ladders about a model that has not shipped as of the origin
_latest = {f: float(rel[(rel.family == f) & (rel.date < asof)].sort_values("date").version.iloc[-1])
           for f in FAMILIES if len(rel[(rel.family == f) & (rel.date < asof)])}
lad = mk.ladders(mkts, latest=_latest)
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
_q = [m for m in pd.date_range(asof, periods=6, freq="QE")][:5]
gen, gen_info = P.generation_clock(AS_OF, [str(m.date()) for m in _q])
out["params"]["generation6"] = dict(prob_by=gen, **gen_info)
for f in FAMILIES:
    med = out["targets"][f]["with_signals"]["median"]
    at = med if not med.startswith(">") else "2027-06-30"
    # P(next model is a new major) = P(generation clock fires before this family's median date)
    pg, _ = P.generation_clock(AS_OF, [at])
    names = P.next_names(rel, f, list(pg.values())[0])
    # versions named by grade A/B artifacts (maintained by hand in data/named_versions.json;
    # clear an entry once that model ships)
    nv = json.load(open("data/named_versions.json")) if os.path.exists("data/named_versions.json") else {}
    if nv.get(f):
        names = P.apply_named_signals(names, [nv[f]])
    out["params"][f] = dict(names=names, price=P.price_change(rel, f), colaunch=P.colaunch_rate(rel, f),
                            swe_bench_pro=P.swe_pro_projection(f, at), median_date_used=at)
wp = weekday_profile(rel, AS_OF)
out["params"]["weekday_share"] = dict(zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], (wp / 7).round(3).tolist()))

out["model_version"] = MODEL_VERSION
out["market_file"] = MARKET_FILE
# family to feature in the page's "watch" section: the likeliest within 30 days among
# families with live signals (fallback: likeliest overall)
_sig = [f for f in FAMILIES if out["signals"].get(f)]
_pool = _sig or FAMILIES
out["watch"] = max(_pool, key=lambda f: out["targets"][f]["with_signals"]["p30"])
json.dump(out, open("output/forecast.json", "w"), indent=1, default=float)

# forward log (long format): one row per target × checkpoint, with the market
# price where a Polymarket ladder rung exists for that date. Never edited.
import csv
logp = "forecast_log.csv"
new = not os.path.exists(logp)
if not new and any(line.startswith(out["as_of"] + "," + MODEL_VERSION + ",") for line in open(logp)):
    print("forecast_log.csv already has", out["as_of"], MODEL_VERSION, "- not appending")
else:
    with open(logp, "a", newline="") as fh:
        wr = csv.writer(fh)
        if new:
            wr.writerow(["as_of", "model_version", "target", "checkpoint", "p_model", "p_market", "median", "q10", "q90"])
        for k in TARGETS:
            t = out["targets"][k]["with_signals"]
            mrows = {r["date"]: r["market"] for r in out["markets"].get(k, [])}
            for cp, pv in t["by"].items():
                if pv is None:
                    continue
                wr.writerow([out["as_of"], MODEL_VERSION, k, cp, round(pv, 4),
                             round(mrows[cp], 4) if cp in mrows else "", t["median"], t["q10"], t["q90"]])
for k in TARGETS:
    a = out["targets"][k]["cadence"]; b = out["targets"][k]["with_signals"]
    print(f"{k:9s} cadence p30={a['p30']:.2f} med={a['median']} | +signals p7={b['p7']:.2f} p30={b['p30']:.2f} "
          f"p90={b['p90']:.2f} med={b['median']} 80%=[{b['q10']}, {b['q90']}] by {CHECKPOINTS[0]}={b['by'][CHECKPOINTS[0]]:.2f} by {CHECKPOINTS[1]}={b['by'][CHECKPOINTS[1]]:.2f}")
for fam, rows in out["markets"].items():
    for r in rows:
        if r["date"] in CHECKPOINTS:
            print(f"  {fam:7s} {r['date']} model={r['model']:.2f} market={r['market']:.2f} blend={r['blend']:.2f}")
