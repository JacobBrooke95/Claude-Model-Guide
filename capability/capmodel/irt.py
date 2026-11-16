"""Own two-parameter IRT refit of the public ECI inputs, for leave-future-out vintages.

Model (Epoch's form): performance_mb = sigmoid(alpha_b * (C_m - D_b)).
Estimation: least squares on performance with weak ridge priors (Epoch's current fit is a
joint Bayesian model with a Beta likelihood; this is a simpler estimator and is used
only as a robustness check, never as the headline ability).

A vintage fit at date d uses only models released on or before d and only their scores.
Its raw scale is arbitrary, so it is mapped to ECI units by a robust (Huber) line through
the published ECI of the same models. That alignment borrows today's *units* for past
models; it does not borrow any information about models released after d.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy import optimize, sparse

from .common import RAW, CACHE, yr

MIN_MODELS_PER_BENCH = 4
MIN_BENCH_PER_MODEL = 4


def monotone_align(xs, ys, xnew, nbins=10):
    """Map raw abilities to ECI units: medians of (x, y) in equal-count bins, made
    monotone, linearly interpolated, and linearly extrapolated with the slope of the
    outer two knots."""
    o = np.argsort(xs)
    xs, ys = xs[o], ys[o]
    nb = int(min(nbins, max(2, len(xs) // 6)))
    edges = np.linspace(0, len(xs), nb + 1).astype(int)
    kx = np.array([np.median(xs[a:b]) for a, b in zip(edges[:-1], edges[1:])])
    ky = np.maximum.accumulate(np.array([np.median(ys[a:b]) for a, b in zip(edges[:-1], edges[1:])]))
    kx = kx + np.arange(nb) * 1e-9
    out = np.interp(xnew, kx, ky)
    lo = (ky[1] - ky[0]) / (kx[1] - kx[0])
    hi = (ky[-1] - ky[-2]) / (kx[-1] - kx[-2])
    out = np.where(xnew < kx[0], ky[0] + lo * (xnew - kx[0]), out)
    out = np.where(xnew > kx[-1], ky[-1] + hi * (xnew - kx[-1]), out)
    return out


def load_inputs():
    b = pd.read_csv(RAW / "eci_benchmarks.csv")
    b = b.groupby(["model", "benchmark"], as_index=False).agg(
        p=("performance_0_1", "max"), date=("model_release_date", "first"))
    b["t"] = b.date.map(yr)
    # canonical release dates (the repo's for Claude models), so a model cannot enter a vintage before its canonical date
    from .common import DATA
    m = pd.read_csv(DATA / "models.csv")
    canon = dict(zip(m.model_id, m.release_date.map(yr)))
    b["t"] = [canon.get(mod, t) for mod, t in zip(b.model, b.t)]
    return b


def fit_irt(obs: pd.DataFrame, published: pd.Series):
    """obs: columns model, benchmark, p. Returns Series model -> ability in ECI units."""
    obs = obs.copy()
    while True:   # iterate the minimum-count filters to a fixed point
        nb = obs.groupby("benchmark").model.transform("nunique")
        nm = obs.groupby("model").benchmark.transform("nunique")
        keep = (nb >= MIN_MODELS_PER_BENCH) & (nm >= MIN_BENCH_PER_MODEL)
        if keep.all():
            break
        obs = obs[keep]
    models = sorted(obs.model.unique())
    benches = sorted(obs.benchmark.unique())
    mi = obs.model.map({m: i for i, m in enumerate(models)}).to_numpy()
    bi = obs.benchmark.map({b: i for i, b in enumerate(benches)}).to_numpy()
    p = obs.p.clip(0.0, 1.0).to_numpy()
    M, Bn, N = len(models), len(benches), len(p)
    # start: ability from mean logit, difficulty 0, slope 1 (in logit units)
    lg = np.log((p.clip(0.02, 0.98)) / (1 - p.clip(0.02, 0.98)))
    c0 = pd.Series(lg).groupby(mi).mean().to_numpy()
    d0 = -(pd.Series(lg - c0[mi]).groupby(bi).mean().to_numpy())
    x0 = np.concatenate([c0, d0, np.zeros(Bn)])
    lam_c, lam_a = 0.02, 0.15

    def unpack(x):
        return x[:M], x[M:M + Bn], np.exp(x[M + Bn:])

    def resid(x):
        c, dd, a = unpack(x)
        z = a[bi] * (c[mi] - dd[bi])
        f = 1 / (1 + np.exp(-z))
        return np.concatenate([f - p, lam_c * c, np.zeros(Bn), lam_a * x[M + Bn:]])

    def jac(x):
        c, dd, a = unpack(x)
        z = a[bi] * (c[mi] - dd[bi])
        f = 1 / (1 + np.exp(-z))
        g = f * (1 - f)
        rows = np.arange(N)
        J = sparse.coo_matrix(
            (np.concatenate([g * a[bi], -g * a[bi], g * z]),
             (np.concatenate([rows, rows, rows]), np.concatenate([mi, M + bi, M + Bn + bi]))),
            shape=(N, M + 2 * Bn))
        reg = sparse.diags(np.concatenate([np.full(M, lam_c), np.zeros(Bn), np.full(Bn, lam_a)]))
        return sparse.vstack([J, reg]).tocsr()

    r = optimize.least_squares(resid, x0, jac=jac, method="trf", x_scale="jac", max_nfev=200)
    c = pd.Series(unpack(r.x)[0], index=models)
    # monotone alignment to published ECI units (piecewise-linear through binned medians;
    # the least-squares scale is a curved, monotone function of Epoch's Bayesian scale)
    common = [m for m in models if m in published.index and np.isfinite(published[m])]
    xs, ys = c[common].to_numpy(), published[common].to_numpy()
    out = pd.Series(monotone_align(xs, ys, c.to_numpy()), index=models)
    rmse = float(np.sqrt(np.mean((out[common] - published[common]) ** 2)))
    return out, {"n_models": M, "n_bench": Bn, "n_obs": N, "align_rmse": rmse, "cost": float(r.cost)}


VINTAGE_FILE = "irt_vintages.csv.gz"
DATE_TOL = 2e-4      # years (~0.07 day): dates are keyed rounded to 4 decimals, so 'on or before d' needs a tolerance


def vintage_abilities(dates, published: pd.Series, full=False):
    """Abilities re-estimated at each date from models released on or before it.
    The fit is deterministic. Results are stored in capability/data/irt_vintages.csv.gz
    (committed, and part of the input hash that --check verifies); full=True recomputes
    every vintage, otherwise only missing dates are computed."""
    from .common import DATA
    f = DATA / VINTAGE_FILE
    keys = sorted({round(float(d), 4) for d in dates})
    have = {}
    if f.exists() and not full:
        df = pd.read_csv(f)
        have = {k: g.set_index("model").ability for k, g in df.groupby("date")}
    obs = load_inputs()
    changed = False
    for k in keys:
        if k not in have:
            have[k] = fit_irt(obs[obs.t <= k + DATE_TOL], published)[0].round(3)
            changed = True
    if changed or full or set(have) != set(keys):
        import gzip
        rows = pd.concat([pd.DataFrame({"date": k, "model": have[k].index, "ability": have[k].to_numpy()}) for k in keys])
        with gzip.GzipFile(f, "wb", mtime=0) as fh:
            fh.write(rows.to_csv(index=False).encode())
    return {k: (have[k], {}) for k in keys}
