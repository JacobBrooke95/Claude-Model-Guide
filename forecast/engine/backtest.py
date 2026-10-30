"""Rolling-origin backtest.

Leakage rules: at origin t the forecaster sees releases dated < t, competitor
releases dated < t, and signals first seen < t whose outcome had resolved by
t. Nothing else.

Two scoring views (both reported, because each flatters a different model):
  * window questions — weekly origins; "does target X ship in [t, t+h)?"
    for h ∈ {7, 30, 90}; Brier, log loss, skill vs climatology. Overlapping
    windows are autocorrelated, so the effective sample is roughly the number
    of release events, not the number of origins; CIs use a block bootstrap
    whose blocks are inter-release intervals.
  * event view — for every release, the predictive distribution of its date
    made the day after the family's previous release and at 60/30/14/7 days
    before it: CRPS (days), PIT, median absolute error.
"""
from __future__ import annotations

import json
import subprocess
from dataclasses import replace

import numpy as np
import pandas as pd

from .data import FAMILIES, d, next_release
from .forecast import Config, FitCache, forecast, H, TARGETS

REPO = __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..")

TARGET_FAMS = {**{f: [f] for f in FAMILIES}, "frontier": ["opus", "fable", "mythos"],
               "any": ["opus", "sonnet", "haiku", "fable", "mythos"]}


def target_dates(rel, target):
    return sorted(rel.loc[rel.family.isin(TARGET_FAMS[target]), "date"].unique())


def outcome(rel, target, origin, h):
    ds = np.array(target_dates(rel, target), dtype="datetime64[D]")
    o = np.datetime64(d(origin).date())
    return int(((ds >= o) & (ds < o + np.timedelta64(h, "D"))).any())


def first_after(rel, target, origin):
    ds = [pd.Timestamp(x) for x in target_dates(rel, target) if pd.Timestamp(x) >= d(origin)]
    return ds[0] if ds else None


def climatology(rel, target, origin, h, start="2024-03-04"):
    """Leak-free empirical P(release in an h-day window): share of past days
    (within the target's own history) whose next-h-day window held a release."""
    ds = [pd.Timestamp(x) for x in target_dates(rel, target) if pd.Timestamp(x) < d(origin)]
    if not ds:
        return np.nan
    lo = max(d(start), ds[0])
    hi = d(origin) - pd.Timedelta(days=h)
    if hi <= lo:
        # too little history: Poisson with the target's rate so far (≥1 event)
        rate = len(ds) / max((d(origin) - d(start)).days, 30)
        return 1 - np.exp(-rate * h)
    days = pd.date_range(lo, hi, freq="D")
    arr = np.array(ds, dtype="datetime64[D]")
    dd = days.values.astype("datetime64[D]")
    nxt = np.searchsorted(arr, dd, side="left")
    ok = nxt < len(arr)
    gap = np.full(len(dd), 10 ** 6)
    gap[ok] = (arr[nxt[ok]] - dd[ok]).astype(int)
    return float(np.mean(gap < h))


def recent_rate(rel, target, origin, h, window=180):
    """Poisson rate from the target's releases in the previous `window` days
    (distinct days), floored at half a release per window."""
    ds = [pd.Timestamp(x) for x in target_dates(rel, target)]
    o = d(origin)
    n = sum(o - pd.Timedelta(days=window) <= x < o for x in ds)
    rate = max(n, 0.5) / window
    return float(1 - np.exp(-rate * h))


def ewma_baseline(origin):
    """The repo's existing model (claude-models.html, via its own CLI)."""
    # predict-releases.js keeps releases dated <= --date, so ask for the day before
    # the origin; otherwise a release on the origin day leaks into the baseline
    day_before = d(origin) - pd.Timedelta(days=1)
    out = subprocess.run(["node", "scripts/predict-releases.js", "--json", "--date", str(day_before.date())],
                         cwd=REPO, capture_output=True, text=True)
    if out.returncode != 0:
        return {}
    js = json.loads(out.stdout)
    res = {}
    for fam in js["forecast"]["families"]:
        res[fam["name"].lower()] = fam
    return res


def ewma_prob(fam, origin, h):
    """Generous probabilistic reading of the EWMA model: its window treated
    as a central 80% interval of a normal on the release date, truncated to
    dates ≥ origin."""
    from scipy.stats import norm
    if not fam:
        return np.nan
    o = d(origin)
    centre = o if fam["overdue"] else d(fam["predictedDate"])
    sd = max(fam["spreadDays"], 3) / 1.2816
    mu = (centre - o).days
    lo = norm.sf(0, mu, sd)
    if lo <= 1e-9:
        return 1.0
    return float((norm.cdf(h, mu, sd) - norm.cdf(0, mu, sd)) / lo)


def crps_days(pmf, tail, actual_offset):
    cdf = np.cumsum(pmf)
    cdf = np.concatenate([cdf, np.full(100, 1.0)])  # tail mass placed at day H+100
    x = np.arange(len(cdf))
    step = (x >= actual_offset).astype(float)
    return float(np.sum((cdf - step) ** 2))


def weekly_origins(start="2024-06-03", end="2026-10-26"):
    return list(pd.date_range(start, end, freq="7D"))


def event_origins(rel, start="2024-06-01", leads=(60, 30, 14, 7)):
    out = []
    for f in ["opus", "sonnet", "haiku", "fable", "mythos"]:
        ds = target_dates(rel, f)
        for a, b in zip(ds[:-1], ds[1:]):
            a, b = pd.Timestamp(a), pd.Timestamp(b)
            if b < d(start):
                continue
            out.append((f, b, "after_prev", a + pd.Timedelta(days=1)))
            for L in leads:
                o = b - pd.Timedelta(days=L)
                if o > a:
                    out.append((f, b, f"lead{L}", o))
    return out


def run(rel, comp, sig, configs: dict, origins, data_end, horizons=(7, 30, 90), cache=None, with_ewma=True,
        progress=False):
    cache = cache or FitCache()
    rows = []
    ew_cache = {}
    for i, o in enumerate(origins):
        if progress and i % 10 == 0:
            print(f"  origin {i}/{len(origins)} {o.date()}", flush=True)
        fc = {name: forecast(rel, comp, sig, o, cfg, cache)[0] for name, cfg in configs.items()}
        if with_ewma:
            ew_cache[o] = ewma_baseline(o)
        for tgt in TARGETS:
            for h in horizons:
                if o + pd.Timedelta(days=h - 1) > d(data_end):
                    continue
                if tgt not in next(iter(fc.values())):
                    continue
                y = outcome(rel, tgt, o, h)
                row = dict(origin=o, target=tgt, h=h, y=y, clim=climatology(rel, tgt, o, h),
                           rr180=recent_rate(rel, tgt, o, h))
                for name, f in fc.items():
                    if tgt in f:
                        row[name] = float(np.sum(f[tgt][0][:h]))
                if with_ewma and tgt in ("opus", "sonnet", "haiku"):
                    row["ewma"] = ewma_prob(ew_cache[o].get(tgt), o, h)
                rows.append(row)
    return pd.DataFrame(rows), cache


def run_events(rel, comp, sig, configs, evs, cache=None, with_ewma=True):
    cache = cache or FitCache()
    rows = []
    for f, actual, kind, o in evs:
        off = (actual - o).days
        row = dict(family=f, actual=actual, kind=kind, origin=o, offset=off)
        for name, cfg in configs.items():
            fc = forecast(rel, None if not cfg.competitor else comp, sig, o, cfg, cache)[0]
            if f not in fc:
                continue
            pmf, tail = fc[f]
            cdf = np.cumsum(pmf)
            row[f"{name}_crps"] = crps_days(pmf, tail, off)
            row[f"{name}_pit"] = float(cdf[off - 1] if off >= 1 else 0) + 0.5 * float(pmf[off]) if off < H else 1.0
            med = int(np.searchsorted(cdf, 0.5)) if cdf[-1] >= 0.5 else H + 50
            row[f"{name}_mederr"] = med - off
            lo, hi = np.searchsorted(cdf, 0.1), np.searchsorted(cdf, 0.9)
            row[f"{name}_in80"] = int(lo <= off <= hi)
        if with_ewma and f in ("opus", "sonnet", "haiku"):
            e = ewma_baseline(o).get(f)
            if e:
                pred = 0 if e["overdue"] else (d(e["predictedDate"]) - o).days
                row["ewma_mederr"] = pred - off
                ws = (d(e["windowStart"]) - o).days
                we = (d(e["windowEnd"]) - o).days
                row["ewma_in80"] = int(ws <= off <= we)
        rows.append(row)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- scoring ----
def brier(p, y):
    return float(np.mean((np.asarray(p) - np.asarray(y)) ** 2))


def logloss(p, y):
    p = np.clip(np.asarray(p), 1e-4, 1 - 1e-4)
    y = np.asarray(y)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def interval_blocks(df, rel):
    """Block id = which inter-release interval (any release) the origin sits in."""
    ds = np.array(sorted(rel.date.unique()), dtype="datetime64[D]")
    o = df.origin.values.astype("datetime64[D]")
    return np.searchsorted(ds, o, side="right")


def block_bootstrap_diff(df, a, b, rel, n=2000, seed=0, metric="brier"):
    """CI for mean(score_a − score_b) resampling inter-release blocks."""
    rng = np.random.default_rng(seed)
    blocks = interval_blocks(df, rel)
    sa = (df[a] - df.y) ** 2 if metric == "brier" else -(df.y * np.log(np.clip(df[a], 1e-4, 1)) + (1 - df.y) * np.log(np.clip(1 - df[a], 1e-4, 1)))
    sb = (df[b] - df.y) ** 2 if metric == "brier" else -(df.y * np.log(np.clip(df[b], 1e-4, 1)) + (1 - df.y) * np.log(np.clip(1 - df[b], 1e-4, 1)))
    diff = (sa - sb).values
    ub = np.unique(blocks)
    idx = {u: np.where(blocks == u)[0] for u in ub}
    stats_ = []
    for _ in range(n):
        pick = rng.choice(ub, size=len(ub), replace=True)
        ii = np.concatenate([idx[u] for u in pick])
        stats_.append(diff[ii].mean())
    return float(diff.mean()), [float(np.percentile(stats_, 2.5)), float(np.percentile(stats_, 97.5))], int(len(ub))


def dm_hac(df, a, b, lag=None):
    """Diebold–Mariano on Brier loss differential with Newey–West variance."""
    from scipy.stats import norm
    dd = ((df[a] - df.y) ** 2 - (df[b] - df.y) ** 2).values
    n = len(dd)
    if n < 10:
        return np.nan, np.nan
    lag = lag or int(np.ceil(df.h.iloc[0] / 7)) + 1
    m = dd.mean()
    e = dd - m
    v = e @ e / n
    for k in range(1, lag + 1):
        w = 1 - k / (lag + 1)
        v += 2 * w * (e[k:] @ e[:-k]) / n
    se = np.sqrt(max(v, 1e-12) / n)
    t = m / se
    return float(t), float(2 * norm.sf(abs(t)))


def reliability(p, y, bins=(0, .05, .15, .3, .5, .7, .85, 1.0001)):
    p, y = np.asarray(p), np.asarray(y)
    out = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (p >= lo) & (p < hi)
        if m.sum():
            out.append(dict(bin=f"{lo:.2f}-{min(hi,1):.2f}", n=int(m.sum()), mean_p=float(p[m].mean()), freq=float(y[m].mean())))
    return out
