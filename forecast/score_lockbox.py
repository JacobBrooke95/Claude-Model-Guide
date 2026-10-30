"""Turn the backtest pickles into output/backtest.json (what the page shows)."""
import itertools
import json
import sys

import numpy as np
import pandas as pd

from engine import backtest as bt
from engine.data import load_releases

TAG = "v2"
rel = load_releases()
KEY = ["origin", "target", "h", "y", "clim", "ewma"]


def merged(a, *bs):
    A = pd.read_pickle(a)
    for b in bs:
        Bb = pd.read_pickle(b)
        A = A.merge(Bb.drop(columns=[c for c in ("clim", "ewma") if c in Bb]), on=["origin", "target", "h", "y"])
    return A


lock = merged("output/lockbox_scores_v2.pkl", "output/lockbox_scores_v2_ensemble-ensemble50.pkl", "output/lockbox_scores_v2_final.pkl")
tune = merged("output/tuning_full_scores_v2.pkl", "output/tuning_full_scores_v2_ensemble-ensemble50.pkl", "output/tuning_full_scores_v2_final.pkl")
ev = pd.read_pickle("output/event_scores_v2.pkl")
for extra, pre in (("output/event_scores_v2_ensemble.pkl", "ensemble_"), ("output/event_scores_v2_final.pkl", "final_")):
    eve = pd.read_pickle(extra)
    ev = ev.merge(eve[["family", "actual", "kind", "origin"] + [c for c in eve if c.startswith(pre)]],
                  on=["family", "actual", "kind", "origin"], how="left")
allp = pd.concat([tune, lock], ignore_index=True)
MAIN_T = ["opus", "sonnet", "haiku", "frontier", "any"]
models = [c for c in lock.columns if c not in ("origin", "target", "h", "y", "clim", "ewma")]

out = {"tag": TAG, "lockbox_start": str(lock.origin.min().date()), "lockbox_end": str(lock.origin.max().date()),
       "tuning_start": str(tune.origin.min().date()), "tuning_end": str(tune.origin.max().date())}


def n_events(df, tgt):
    ds = bt.target_dates(rel, tgt)
    lo, hi = df.origin.min(), df.origin.max() + pd.Timedelta(days=int(df.h.max()))
    return int(sum(lo <= pd.Timestamp(x) <= hi for x in ds))


def table(df, label):
    rows = []
    d = df[df.target.isin(MAIN_T)]
    for m in models + ["clim"]:
        for h in (7, 30, 90):
            s = d[(d.h == h)].dropna(subset=[m])
            if s.empty:
                continue
            b, c = bt.brier(s[m], s.y), bt.brier(s.clim, s.y)
            rows.append(dict(period=label, model=m, h=h, n=len(s), positives=int(s.y.sum()), brier=b,
                             logloss=bt.logloss(s[m], s.y), bss_vs_clim=1 - b / c))
    # EWMA only exists for opus/sonnet/haiku; compare on that subset
    d3 = df[df.target.isin(["opus", "sonnet", "haiku"])]
    for m in ["v1", "base", "signals", "ensemble", "ensemble50", "final", "ewma", "clim"]:
        if m not in d3:
            continue
        for h in (7, 30, 90):
            s = d3[d3.h == h].dropna(subset=[m, "ewma"])
            rows.append(dict(period=label, model=m + " (O/S/H only)", h=h, n=len(s), positives=int(s.y.sum()),
                             brier=bt.brier(s[m], s.y), logloss=bt.logloss(s[m], s.y),
                             bss_vs_clim=1 - bt.brier(s[m], s.y) / bt.brier(s.clim, s.y)))
    return rows


out["scores"] = table(lock, "lockbox") + table(tune, "tuning") + table(allp, "all")
out["events_in_lockbox"] = {t: n_events(lock, t) for t in MAIN_T}
out["events_in_tuning"] = {t: n_events(tune, t) for t in MAIN_T}

# pairwise tests on the lockbox, pooled main targets
tests = []
for a, b in [("base", "clim"), ("v1", "clim"), ("base", "v1"), ("signals", "base"), ("ensemble", "signals"), ("final", "ensemble"), ("final", "clim"), ("final", "base"), ("full", "signals"), ("comp_major", "base"), ("comp_sota", "base"),
             ("changepoint", "base"), ("cadence_only", "base"), ("wave_only", "base"), ("base_nocal", "base"),
             ("sig_rho35_cap8", "signals"), ("sig_rho70_cap5", "signals"), ("sig_noabsence", "signals")]:
    if a not in lock or b not in lock:
        continue
    for h in (7, 30, 90):
        s = lock[(lock.h == h) & lock.target.isin(MAIN_T)].dropna(subset=[a, b]).sort_values(["target", "origin"])
        mean, ci, nb = bt.block_bootstrap_diff(s, a, b, rel)
        t, p = bt.dm_hac(s, a, b)
        tests.append(dict(a=a, b=b, h=h, n=len(s), brier_diff=mean, ci95=ci, blocks=nb, dm_t=t, dm_p=p))
for period, frame_ in (("lockbox", lock), ("all", allp)):
    d3 = frame_[frame_.target.isin(["opus", "sonnet", "haiku"])]
    for a in ("signals", "ensemble", "final"):
        for h in (7, 30, 90):
            s = d3[d3.h == h].dropna(subset=[a, "ewma"]).sort_values(["target", "origin"])
            mean, ci, nb = bt.block_bootstrap_diff(s, a, "ewma", rel)
            t, p = bt.dm_hac(s, a, "ewma")
            tests.append(dict(a=a, b="ewma", period=period, h=h, n=len(s), brier_diff=mean, ci95=ci, blocks=nb, dm_t=t, dm_p=p))
for h in (7, 30, 90):
    s = allp[(allp.h == h) & allp.target.isin(MAIN_T)].dropna(subset=["ensemble", "clim"]).sort_values(["target", "origin"])
    mean, ci, nb = bt.block_bootstrap_diff(s, "ensemble", "clim", rel)
    t, p = bt.dm_hac(s, "ensemble", "clim")
    tests.append(dict(a="ensemble", b="clim", period="all", h=h, n=len(s), brier_diff=mean, ci95=ci, blocks=nb, dm_t=t, dm_p=p))
out["tests"] = tests

# reliability (lockbox, h = 30, main targets)
out["reliability"] = {}
out["reliability_all"] = {}
for m in ["base", "signals", "final", "clim"]:
    s_ = allp[(allp.h == 30) & allp.target.isin(MAIN_T)]
    out["reliability_all"][m] = bt.reliability(s_[m], s_.y)
for m in ["base", "signals", "final", "clim"]:
    if m in lock:
        s = lock[(lock.h == 30) & lock.target.isin(MAIN_T)]
        out["reliability"][m] = bt.reliability(s[m], s.y)

# per-target lockbox Brier at 30d
out["by_target"] = []
for t in MAIN_T + ["fable", "mythos"]:
    s = lock[(lock.h == 30) & (lock.target == t)]
    if s.empty:
        continue
    r = dict(target=t, n=len(s), positives=int(s.y.sum()))
    for m in ["v1", "base", "signals", "ensemble", "final", "clim", "ewma"]:
        if m in s and s[m].notna().any():
            r[m] = bt.brier(s[m].dropna(), s.y[s[m].notna()])
    out["by_target"].append(r)

# event view
evo = []
for kind in ["after_prev", "lead60", "lead30", "lead14", "lead7"]:
    e = ev[ev.kind == kind]
    lockmask = e.actual >= pd.Timestamp("2025-07-07")
    for period, mask in (("all", np.ones(len(e), bool)), ("lockbox", lockmask.values)):
        ee = e[mask]
        r = dict(kind=kind, period=period, n=len(ee))
        for m in ["v1", "base", "signals", "full", "ensemble", "final", "ewma"]:
            if f"{m}_mederr" in ee and ee[f"{m}_mederr"].notna().any():
                x = ee[f"{m}_mederr"].dropna()
                r[f"{m}_mae"] = float(np.median(np.abs(x)))
                r[f"{m}_bias"] = float(np.median(x))
                r[f"{m}_cov80"] = float(ee[f"{m}_in80"].dropna().mean())
            if f"{m}_crps" in ee:
                r[f"{m}_crps"] = float(ee[f"{m}_crps"].mean())
        evo.append(r)
out["events"] = evo
e = ev[ev.kind == "after_prev"]
out["pit_after_prev"] = {m: [round(float(x), 3) for x in e[f"{m}_pit"].dropna()] for m in ["base", "signals", "ensemble", "final"] if f"{m}_pit" in e}
out["events_total"] = int(len(ev[ev.kind == "after_prev"]))
out["event_rows"] = [
    {k: (str(v.date()) if isinstance(v, pd.Timestamp) else (None if (isinstance(v, float) and np.isnan(v)) else v))
     for k, v in r.items()} for r in ev.to_dict("records")]

# probability of backtest overfitting across the 27 stage-1 configs (CSCV, Bailey et al. 2017)
tun27 = pd.read_pickle("output/tuning_scores.pkl")
cfgs = [c for c in tun27.columns if "|" in c]
t = tun27[tun27.target.isin(MAIN_T)].copy()
t["blk"] = pd.qcut(t.origin.rank(method="dense"), 8, labels=False)
loss = {c: -(t.y * np.log(np.clip(t[c], 1e-4, 1)) + (1 - t.y) * np.log(np.clip(1 - t[c], 1e-4, 1))) for c in cfgs}
M = pd.DataFrame({c: loss[c].groupby(t.blk).mean() for c in cfgs})  # blocks × configs
logits = []
for IS in itertools.combinations(range(8), 4):
    OS = [i for i in range(8) if i not in IS]
    best = M.loc[list(IS)].mean().idxmin()
    rank_os = M.loc[OS].mean().rank(pct=True)[best]  # lower loss = better; rank near 0 is good
    w = 1 - rank_os + 1e-6
    logits.append(np.log(w / (1 - w + 1e-6)))
out["pbo"] = dict(value=float(np.mean(np.array(logits) <= 0)), n_splits=len(logits), n_configs=len(cfgs),
                  note="share of in-sample/out-of-sample splits where the in-sample best config lands in the bottom half out of sample")

json.dump(out, open("output/backtest.json", "w"), indent=1, default=float)

pd.set_option("display.width", 220)
sc = pd.DataFrame(out["scores"])
for per in ("lockbox", "all"):
    print(per); print(sc[sc.period == per].pivot_table(index="model", columns="h", values=["brier", "logloss"]).round(4))
print(pd.DataFrame(tests).round(4).to_string())
print(pd.DataFrame(evo).round(2).to_string())
print("PBO", out["pbo"])
print("events in lockbox", out["events_in_lockbox"])
