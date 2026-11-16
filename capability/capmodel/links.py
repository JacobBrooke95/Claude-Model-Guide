"""Benchmark link layer: ability (public ECI) -> observable score.

bounded     p = (score - lo)/(hi - lo) = sigmoid(a * (ability - D))        [Epoch's IRT form]
            noise on the logit scale (Student-t), so predictive draws respect the bounds
elo/linear  score = b0 + b1 * ability + noise
loghorizon  log2(minutes) = b0 + b1 * ability + noise    (1/b1 = ECI points per doubling)

Every link is fitted on all models that have both a public ECI and a score in the stated
configuration. Parameter uncertainty is a bootstrap over models; residual noise is
estimated from the fit and partially pooled across benchmarks of the same kind, because a
10-point fit understates its own scatter.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy import optimize

NU = 4.0
MIN_N = 8            # minimum models with ability + score
MIN_INFORMATIVE = 5  # bounded: minimum points strictly inside (5%, 95%) of the range
POOL_N0 = 10         # pseudo-count for pooling residual scale across benchmarks
T_SD = np.sqrt(NU / (NU - 2))


def _sig(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40, 40)))


def _logit(p):
    p = np.clip(p, 0.005, 0.995)
    return np.log(p / (1 - p))


def _fit_sigmoid(x, p):
    lg = _logit(p)
    A = np.column_stack([np.ones_like(x), x])
    b = np.linalg.lstsq(A, lg, rcond=None)[0]
    a0 = max(b[1], 0.01)
    D0 = -b[0] / a0 if a0 > 0 else np.median(x)
    D0 = float(np.clip(D0, 60, 260))
    try:
        r = optimize.least_squares(lambda q: _sig(q[0] * (x - q[1])) - p, [a0, D0],
                                   bounds=([0.005, 40], [1.0, 300]), max_nfev=60)
        return float(r.x[0]), float(r.x[1])
    except Exception:
        return float(a0), float(D0)


def _fit_line(x, y):
    A = np.column_stack([np.ones_like(x), x])
    b = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(b[0]), float(b[1])


class Link:
    def __init__(self, key, kind, lo, hi, x, y, B, rng, epoch_params=None):
        self.key, self.kind, self.lo, self.hi = key, kind, lo, hi
        self.x, self.y = np.asarray(x, float), np.asarray(y, float)
        self.n = len(self.x)
        self.note = ""
        x, y = self.x, self.y
        if kind == "bounded":
            self.p = np.clip((y - lo) / (hi - lo), 0.0, 1.0)
            self.par = _fit_sigmoid(x, self.p)
            fit_p = _sig(self.par[0] * (x - self.par[1]))
            self.rmse_p = float(np.sqrt(np.mean((fit_p - self.p) ** 2)))
            self.epoch_params, self.rmse_epoch = epoch_params, None
            if epoch_params is not None:
                fe = _sig(epoch_params[0] * (x - epoch_params[1]))
                self.rmse_epoch = float(np.sqrt(np.mean((fe - self.p) ** 2)))
            mid = (fit_p > 0.05) & (fit_p < 0.95) & (self.p > 0.005) & (self.p < 0.995)
            res = (_logit(self.p) - self.par[0] * (x - self.par[1]))[mid]
            self.n_res = int(mid.sum())
        else:
            self.t = np.log2(np.maximum(y, 1e-9)) if kind == "loghorizon" else y
            self.par = _fit_line(x, self.t)
            res = self.t - (self.par[0] + self.par[1] * x)
            self.n_res = len(res)
            self.rmse_p = float(np.sqrt(np.mean(res ** 2)))
        self.s_raw = float(1.4826 * np.median(np.abs(res - np.median(res)))) if len(res) >= 3 else np.nan
        if len(res) >= 3:
            self.s_raw = max(self.s_raw, float(np.sqrt(np.mean(res ** 2))) * 0.7)
        self.s = self.s_raw
        self.boot = []
        for _ in range(B):
            idx = rng.integers(0, self.n, self.n)
            if len(np.unique(idx)) < 4:
                continue
            if kind == "bounded":
                self.boot.append(_fit_sigmoid(x[idx], self.p[idx]))
            else:
                self.boot.append(_fit_line(x[idx], self.t[idx]))
        if not self.boot:
            self.boot = [self.par]
        self.boot = np.asarray(self.boot)

    def mean(self, theta, par=None):
        par = self.par if par is None else par
        theta = np.asarray(theta, float)
        if self.kind == "bounded":
            return self.lo + (self.hi - self.lo) * _sig(par[0] * (theta - par[1]))
        v = par[0] + par[1] * theta
        return 2.0 ** v if self.kind == "loghorizon" else v

    def sample(self, theta, rng, noise=True):
        """Predictive draws of the score for ability draws theta (1-d)."""
        theta = np.asarray(theta, float)
        pi = rng.integers(0, len(self.boot), theta.shape[0])
        a, b = self.boot[pi, 0], self.boot[pi, 1]
        if theta.ndim == 2:
            a, b = a[:, None], b[:, None]
        e = (self.s * rng.standard_t(NU, theta.shape) / T_SD) if noise else 0.0
        if self.kind == "bounded":
            return self.lo + (self.hi - self.lo) * _sig(a * (theta - b) + e)
        v = a + b * theta + e
        return 2.0 ** v if self.kind == "loghorizon" else v

    def ability_at(self, frac):
        """Ability at which the fitted curve reaches `frac` of the ceiling-rescaled range."""
        if self.kind != "bounded":
            return None
        return float(self.par[1] + np.log(frac / (1 - frac)) / self.par[0])

    def describe(self):
        d = dict(benchmark=self.key, kind=self.kind, n=self.n, resid_scale=round(float(self.s), 3),
                 resid_scale_unpooled=None if not np.isfinite(self.s_raw) else round(float(self.s_raw), 3),
                 note=self.note)
        if self.kind == "bounded":
            d.update(slope=round(self.par[0], 4), difficulty=round(self.par[1], 2), rmse_score=round(self.rmse_p * (self.hi - self.lo), 2),
                     eci_50_to_90=round(2.197 / self.par[0], 1),
                     epoch_slope=None if self.epoch_params is None else round(self.epoch_params[0], 4),
                     epoch_difficulty=None if self.epoch_params is None else round(self.epoch_params[1], 2),
                     rmse_score_epoch_params=None if self.rmse_epoch is None else round(self.rmse_epoch * (self.hi - self.lo), 2))
        else:
            d.update(intercept=round(self.par[0], 3), slope=round(self.par[1], 4), rmse_fit=round(self.rmse_p, 3))
            if self.kind == "loghorizon":
                d["eci_per_doubling"] = round(1 / self.par[1], 2)
                bs = 1 / self.boot[:, 1]
                d["eci_per_doubling_ci90"] = [round(float(v), 2) for v in np.quantile(bs, [0.05, 0.95])]
        return d


EPOCH_NAME = {"rli": "Remote Labor Index", "arc_agi_2": "ARC-AGI-2", "gpqa_diamond": "GPQA diamond",
              "frontiermath_t13": "FrontierMath-Tiers-1-3-v2-Private", "terminal_bench_2": "Terminal Bench",
              "osworld": "OSWorld", "metr_h50": "METR Time Horizons"}


def fit_links(bench: pd.DataFrame, meta: pd.DataFrame, abilities: pd.Series, t_cut, B, rng, edi=None):
    """Fit every benchmark that passes the inclusion rule on models released before t_cut.
    Returns (links dict, dropped list of (key, reason))."""
    links, dropped = {}, []
    for m in meta.itertuples():
        b = bench[(bench.benchmark == m.benchmark) & (bench.t < t_cut)]
        b = b[b.model_id.isin(abilities.index)]
        x = abilities.loc[b.model_id].to_numpy()
        y = b.value.to_numpy()
        ok = np.isfinite(x) & np.isfinite(y)
        x, y = x[ok], y[ok]
        if len(x) < MIN_N:
            dropped.append((m.benchmark, f"only {len(x)} models with both a public ECI and a score (minimum {MIN_N})"))
            continue
        if m.kind == "bounded":
            p = (y - m.lo) / (m.hi - m.lo)
            ninf = int(((p > 0.05) & (p < 0.95)).sum())
            if ninf < MIN_INFORMATIVE:
                dropped.append((m.benchmark, f"only {ninf} scores strictly inside 5-95% of the range (minimum {MIN_INFORMATIVE})"))
                continue
        ep = None
        if edi is not None and m.benchmark in EPOCH_NAME and m.kind == "bounded":
            r = edi[edi.benchmark_name == EPOCH_NAME[m.benchmark]]
            if len(r):
                ep = (float(r.estimated_slope_scaled.iloc[0]), float(r.edi.iloc[0]))
        links[m.benchmark] = Link(m.benchmark, m.kind, m.lo, m.hi, x, y, B, rng, ep)
    # pool residual scales within kind
    for kind in ("bounded", "elo", "linear", "loghorizon"):
        ls = [l for l in links.values() if l.kind == kind and np.isfinite(l.s_raw)]
        if kind == "bounded" and ls:
            pool = float(np.median([l.s_raw for l in ls]))
            for l in links.values():
                if l.kind == kind:
                    s0 = l.s_raw if np.isfinite(l.s_raw) else pool
                    l.s = float(np.sqrt((l.n_res * s0 ** 2 + POOL_N0 * pool ** 2) / (l.n_res + POOL_N0)))
        else:
            for l in ls:   # unit-specific scales cannot be pooled; inflate for small n instead
                l.s = float(l.s_raw * np.sqrt((l.n + 2) / max(l.n - 2, 1)))
    return links, dropped
