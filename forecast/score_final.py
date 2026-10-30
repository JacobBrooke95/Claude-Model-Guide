"""Score the post-review backtest → output/backtest.json (what the page shows).

Primary questions: Opus, Sonnet and Haiku separately (the per-family
questions). "Any" and "frontier" are reported per target only: at 90 days
their outcome is almost always 1, so pooling them would reward any model that
says "high". Significance uses one number per inter-release block (the mean
loss differential within it), so n is the number of blocks, close to the
number of release events.
"""
import itertools
import json

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize

from engine import backtest as bt
from engine.data import load_releases

rel = load_releases()
lock = pd.read_pickle("output/final_lock.pkl")
tune = pd.read_pickle("output/final_tune.pkl")
ev = pd.read_pickle("output/final_events.pkl")
allp = pd.concat([tune, lock], ignore_index=True)
OSH = ["opus", "sonnet", "haiku"]
MODELS = ["clim", "rr180", "ewma", "v1", "base", "signals", "signals_abs", "comp_major", "final"]
LABEL = {"clim": "Climatology (base rate)", "rr180": "Recent rate (last 180 days)", "ewma": "Old EWMA model (site)",
         "v1": "v1: first design, cadence only", "base": "v2: cadence + recency weighting",
         "signals": "v2 + signals", "signals_abs": "v2 + signals with absence term",
         "comp_major": "v2 + competitor pressure", "final": "Final: v2 + signals, 30% EWMA pool"}
PERIODS = {"tuning": tune, "lockbox": lock, "all": allp}
out = {"periods": {k: [str(v.origin.min().date()), str(v.origin.max().date()), int(v.origin.nunique())] for k, v in PERIODS.items()}}


def loss(p, y, kind="brier"):
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return (p - y) ** 2 if kind == "brier" else -(y * np.log(p) + (1 - y) * np.log(1 - p))


rows = []
for per, df in PERIODS.items():
    d = df[df.target.isin(OSH)]
    for m in MODELS:
        for h in (7, 30, 90):
            s = d[d.h == h].dropna(subset=[m])
            rows.append(dict(period=per, model=m, label=LABEL[m], h=h, n=len(s), positives=int(s.y.sum()),
                             brier=float(loss(s[m], s.y).mean()), logloss=float(loss(s[m], s.y, "log").mean()),
                             bss_vs_clim=float(1 - loss(s[m], s.y).mean() / loss(s.clim, s.y).mean())))
out["scores"] = rows

# per target (lockbox and all), 30 and 90 days
pt = []
for per in ("lockbox", "all"):
    df = PERIODS[per]
    for t in ["opus", "sonnet", "haiku", "fable", "mythos", "frontier", "any"]:
        for h in (30, 90):
            s = df[(df.target == t) & (df.h == h)]
            if s.empty:
                continue
            r = dict(period=per, target=t, h=h, n=len(s), positives=int(s.y.sum()))
            for m in MODELS:
                if m in s and s[m].notna().any():
                    ss = s.dropna(subset=[m])
                    r[m] = float(loss(ss[m], ss.y).mean())
            pt.append(r)
out["by_target"] = pt


def block_test(df, a, b, h):
    """Mean Brier difference a − b with one observation per inter-release block."""
    s = df[(df.h == h) & df.target.isin(OSH)].dropna(subset=[a, b]).copy()
    s["diff"] = loss(s[a], s.y) - loss(s[b], s.y)
    s["blk"] = bt.interval_blocks(s, rel)
    g = s.groupby("blk")["diff"].mean()
    n = len(g)
    m, se = g.mean(), g.std(ddof=1) / np.sqrt(n)
    tstat = m / se if se > 0 else np.nan
    p = float(2 * stats.t.sf(abs(tstat), n - 1)) if n > 1 else np.nan
    boot = [g.sample(n, replace=True, random_state=i).mean() for i in range(2000)]
    return dict(a=a, b=b, h=h, brier_diff=float(s["diff"].mean()), block_mean=float(m), blocks=n,
                ci95=[float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))], t=float(tstat), p=p)


tests = []
for per in ("lockbox", "all"):
    for a, b in [("final", "clim"), ("final", "rr180"), ("final", "ewma"), ("base", "clim"), ("base", "rr180"),
                 ("v1", "clim"), ("v1", "ewma"), ("signals", "base"), ("signals_abs", "signals"),
                 ("comp_major", "base"), ("final", "signals")]:
        for h in (7, 30, 90):
            r = block_test(PERIODS[per], a, b, h)
            r["period"] = per
            tests.append(r)
out["tests"] = tests


# calibration by period (O/S/H, all horizons)
def calib(df, m="final"):
    s = df[df.target.isin(OSH)]
    x = np.log(np.clip(s[m], 1e-4, 1 - 1e-4) / (1 - np.clip(s[m], 1e-4, 1 - 1e-4)))
    y = s.y.values
    f = lambda ab: -np.sum(y * -np.logaddexp(0, -(ab[0] + ab[1] * x)) + (1 - y) * -np.logaddexp(0, ab[0] + ab[1] * x))
    a, b = minimize(f, [0, 1]).x
    return dict(intercept=float(a), slope=float(b), mean_p=float(s[m].mean()), freq=float(y.mean()), n=int(len(s)))


out["calibration"] = {per: calib(df) for per, df in PERIODS.items()}
out["reliability"] = {per: bt.reliability(df[(df.h == 30) & df.target.isin(OSH)]["final"], df[(df.h == 30) & df.target.isin(OSH)].y)
                      for per, df in (("tuning", tune), ("lockbox", lock))}

# events: valid (after previous release) and diagnostic (counted back from release)
evo = []
for kind in ["after_prev", "lead60", "lead30", "lead14", "lead7"]:
    e = ev[ev.kind == kind]
    r = dict(kind=kind, n=int(len(e)))
    for m in ["v1", "base", "signals", "final", "ewma"]:
        if f"{m}_mederr" in e and e[f"{m}_mederr"].notna().any():
            x = e[f"{m}_mederr"].dropna()
            r[f"{m}_mae"] = float(np.median(np.abs(x)))
            r[f"{m}_bias"] = float(np.median(x))
            r[f"{m}_cov80"] = float(e[f"{m}_in80"].dropna().mean())
        if f"{m}_crps" in e:
            r[f"{m}_crps"] = float(e[f"{m}_crps"].mean())
    evo.append(r)
out["events"] = evo
out["events_total"] = int((ev.kind == "after_prev").sum())
out["pit_after_prev"] = {m: [round(float(v), 3) for v in ev.loc[ev.kind == "after_prev", f"{m}_pit"].dropna()] for m in ["base", "final"]}
out["release_days"] = {per: int(sum(df.origin.min() <= pd.Timestamp(x) <= df.origin.max() + pd.Timedelta(days=90)
                                    for x in rel.date.unique())) for per, df in PERIODS.items()}
out["events_by_family_lockbox"] = {t: int(sum(pd.Timestamp("2025-07-07") <= pd.Timestamp(x) <= pd.Timestamp("2026-10-29")
                                             for x in rel[rel.family == t].date)) for t in OSH + ["fable", "mythos"]}

# PBO across every config scored on all 126 origins (pre- and post-review runs)
frames = []
for tag, (a, b) in {"v2": ("output/tuning_full_scores_v2.pkl", "output/lockbox_scores_v2.pkl"),
                    "ens": ("output/tuning_full_scores_v2_ensemble-ensemble50.pkl", "output/lockbox_scores_v2_ensemble-ensemble50.pkl"),
                    "fin": ("output/tuning_full_scores_v2_final.pkl", "output/lockbox_scores_v2_final.pkl")}.items():
    x = pd.concat([pd.read_pickle(a), pd.read_pickle(b)])
    cols = [c for c in x.columns if c not in ("origin", "target", "h", "y", "clim", "ewma", "rr180")]
    frames.append(x[["origin", "target", "h", "y"] + cols].rename(columns={c: f"{tag}:{c}" for c in cols}))
pf = allp[["origin", "target", "h", "y"] + [m for m in MODELS if m not in ("clim", "rr180", "ewma")]].rename(
    columns={m: f"post:{m}" for m in MODELS})
for f_ in frames:
    pf = pf.merge(f_, on=["origin", "target", "h", "y"], how="inner")
pf = pf[pf.target.isin(OSH)]
cfgs = [c for c in pf.columns if ":" in c]
pf["blk"] = pd.qcut(pf.origin.rank(method="dense"), 10, labels=False)
M = pd.DataFrame({c: loss(pf[c], pf.y, "log").groupby(pf.blk).mean() for c in cfgs})
lg = []
for IS in itertools.combinations(range(10), 5):
    OS = [i for i in range(10) if i not in IS]
    best = M.loc[list(IS)].mean().idxmin()
    r = M.loc[OS].mean().rank(pct=True)[best]
    w = min(max(1 - r, 1e-6), 1 - 1e-6)
    lg.append(np.log(w / (1 - w)))
out["pbo"] = dict(value=float(np.mean(np.array(lg) <= 0)), n_splits=len(lg), n_configs=len(cfgs))
s1 = pd.read_pickle("output/tuning_scores.pkl")
out["configs_tried"] = dict(stage1=27, stage1b=18, lockbox_runs=5, scored_on_lockbox=len(cfgs) + 1, total_distinct=59)

json.dump(out, open("output/backtest.json", "w"), indent=1, default=float)

sc = pd.DataFrame(rows)
pd.set_option("display.width", 220)
print(sc.pivot_table(index="model", columns=["period", "h"], values="brier").round(4).to_string())
print(pd.DataFrame(tests)[["period", "a", "b", "h", "brier_diff", "ci95", "blocks", "p"]].round(4).to_string())
print(json.dumps(out["calibration"], indent=0))
print(pd.DataFrame(evo).round(1).to_string())
print("PBO", out["pbo"])
