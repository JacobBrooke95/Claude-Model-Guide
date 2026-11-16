"""The one level process (v2). Both the next-model layer and the 2026-2030 projection
draw from it, so they cannot disagree.

For a frontier series (Anthropic's records, or all labs') as of origin t0:

  L0, recent slope   drawn with equal weight from three recent-trend forms fitted to the
                     record-setters: trailing-12-month line, trailing-24-month line, and
                     the piecewise (hinge) line's last segment. Forms that put weight on
                     all-history slopes are not used: every backtest fold shows them
                     under-predicting.
  pre-break slope    the hinge's first segment (all-history line where no hinge fits).
  path               L(t) = L0 + integral of pace, pace(t) = KAPPA*log10(compute growth)
                     + a0*m(t), with m(t) set by a scenario drawn per path (see SCENARIOS).
  bias term          added by the caller: beta*min(h, 1.5), beta estimated out of sample
                     from this process's own backtest (backtest.machine_folds).

Uncertainty in the fits is a subsample bootstrap: each replicate keeps each model with
probability ~0.63 (the distinct members of a with-replacement resample) and takes one of
Epoch's 500 joint posterior draws; the record set is recomputed per replicate.
"""
from __future__ import annotations
import numpy as np

from .common import wquantile, wsummary, from_yr
from .trend import Ensemble, NU

RECENT = ["lin_12", "lin_24", "hinge"]
SCENARIOS = ["slowdown", "reversion", "hold", "compounding", "explosive"]
DT = 1.0 / 12
T_SD = np.sqrt(NU / (NU - 2))
BIAS_H_CAP = 1.5          # the bias term is not extrapolated beyond the longest backtested horizon

COMPUTE = {   # frontier training compute growth, x/yr, from driver_scenarios_2026_2030.csv (5x/yr before 2027: Epoch trend)
    "low": {2027: 2.5, 2028: 2.0, 2029: 1.5, 2030: 1.5},
    "central": {2027: 5.0, 2028: 4.0, 2029: 3.0, 2030: 2.5},
    "high": {2027: 5.0, 2028: 5.0, 2029: 5.0, 2030: 5.0},
}
KAPPA_MEAN, KAPPA_SD = 9.0, 2.0
HAIRCUT = (0.6, 1.0)
SCENARIO_DEFS = {
    "slowdown": "Below pre-break pace. Training-compute growth follows the 'low' driver path (2.5x, 2x, 1.5x, 1.5x per year "
                "2027-30) and the algorithmic multiplier falls to 0.4-0.9 of its pre-break value within a year.",
    "reversion": "The 2025-26 step-up was one-off. Pace returns within six months to 0.85-1.15x the pre-break slope (centred "
                 "on it, so about half these paths run below pre-break pace), then follows the 'central' compute path down.",
    "hold": "The recent trend holds: the algorithmic multiplier stays where the recent slope puts it; compute follows the "
            "'central' driver path (5x, 4x, 3x, 2.5x).",
    "compounding": "AI R&D feedback: the algorithmic multiplier doubles every 6-12 months until it reaches 4-7.5x, then stays; "
                   "60-100% of the excess over 'hold' is realised; compute on the 'central' or 'high' path.",
    "explosive": "Bounded explosive tail: the multiplier doubles every 3-6 months to a peak of 8-30x, holds 1-2 years, then "
                 "settles at 3-6x; same 60-100% realisation haircut.",
}
WEIGHTS = {   # priors, not estimates; METHODS section 10
    "central":         {"slowdown": 0.12, "reversion": 0.28, "hold": 0.38, "compounding": 0.16, "explosive": 0.06},
    "sceptic":         {"slowdown": 0.25, "reversion": 0.42, "hold": 0.26, "compounding": 0.06, "explosive": 0.01},
    "accelerationist": {"slowdown": 0.00, "reversion": 0.15, "hold": 0.35, "compounding": 0.30, "explosive": 0.20},
}


def compute_growth(path, t):
    y = np.floor(np.asarray(t)).astype(int)
    tab = COMPUTE[path]
    return np.array([5.0 if v < 2027 else tab[int(min(v, 2030))] for v in y])


class LevelProcess:
    def __init__(self, series, t0, B, rng, era_start=2024.15, min_era_records=8):
        """Fitted on record-setters since `era_start` (Claude 3 Opus; Epoch dates the
        reasoning-era break to April 2024) once at least `min_era_records` of them precede
        the origin, so that 'pre-break' means the same era for both series; before that,
        on all history."""
        self.t0, self.rng = float(t0), rng
        cut = series.cut(t0)
        full_start = series.start
        series.start = era_start
        if len(series.cut(t0).published_records()[0]) < min_era_records:
            series.start = full_start
        self.era_start = series.start
        self.ens = Ensemble(series, t0, B, rng, cands=RECENT + ["lin_all"])
        self.ok = self.ens.ok
        if not self.ok:
            return
        s = self.ens.series
        self.rt, self.ry = self.ens.rt, self.ens.ry
        self.F0 = self.ens.F0
        # the standing leader's measurement uncertainty: per posterior draw, the best of the last three record-setters
        _, _, ridx = s.published_records()
        self.F0_draws = s.Y[ridx[-3:]].max(axis=0)
        self.meas_sd = float(np.mean(s.Y[ridx[-5:]].std(axis=1))) if len(ridx) else 1.5
        self.ref = self.ens.fits["hinge"][0].mean                     # descriptive reference line (in-sample)
        self.S = float(np.mean([p[3] for f in self.ens.fits["hinge"][:40] for p in f.parts]))
        # pace variability: sd of 12-month gains of the running maximum, quarterly, before the origin
        tt = np.arange(self.rt[0] + 1.0, t0, 0.25)
        F = lambda t: self.ry[self.rt <= t].max()
        g = np.array([F(t) - F(t - 1.0) for t in tt]) if len(tt) else np.array([])
        self.sigma_w = float(np.clip(g.std(ddof=1), 2.0, 6.0)) if len(g) >= 4 else 3.0

    def draws(self, n):
        """(L0, recent slope, pre-break slope): equal weight over the three recent-trend forms."""
        r = self.rng
        k = r.integers(0, len(RECENT), n)
        L0, b_post = np.empty(n), np.empty(n)
        for j, c in enumerate(RECENT):
            m = k == j
            if m.any():
                L, _ = self.ens.sample_level(c, [self.t0 - 0.25, self.t0], int(m.sum()), r)
                L0[m], b_post[m] = L[:, 1], (L[:, 1] - L[:, 0]) / 0.25
        hinge = [f for f in self.ens.fits["hinge"] if f.kind_eff == "hinge"]
        if hinge:
            per = int(np.ceil(n / len(hinge)))
            b_pre = np.concatenate([f.sample_slopes(per, r)[:, 0] for f in hinge])[:n]
            r.shuffle(b_pre)
        else:
            La, _ = self.ens.sample_level("lin_all", [self.t0 - 1.0, self.t0], n, r)
            b_pre = La[:, 1] - La[:, 0]
        # physically implausible draws are clipped, not discarded (share reported by the pipeline)
        self.clip_share = float(np.mean((b_post < 4) | (b_post > 60) | (b_pre < 4) | (b_pre > 40)))
        b_post, b_pre = np.clip(b_post, 4, 60), np.clip(b_pre, 4, 40)
        # 'pre-break pace' is the earlier, slower pace: where the series shows no step-up (all labs),
        # it coincides with the recent slope, so 'reversion' never means speeding up
        return L0, b_post, np.minimum(b_pre, b_post)

    def paths(self, n, weights, t_end, scn=None, drv=None):
        """Monthly level paths from t0 to t_end under scenarios drawn from `weights`.
        Returns dict(tm, level, pace, scn, b_pre, b_post, L0)."""
        r = self.rng
        tm = np.arange(self.t0, t_end + DT, DT)
        L0, b_post, b_pre = self.draws(n) if drv is None else drv
        if scn is None:
            scn = r.choice(len(SCENARIOS), size=n, p=np.array([weights[s] for s in SCENARIOS]) / sum(weights.values()))
        kappa = np.clip(KAPPA_MEAN + KAPPA_SD * r.standard_normal(n), 4.0, 14.0)
        c5 = kappa * np.log10(5.0)
        a0 = np.maximum(b_pre - c5, 2.0)
        m_post = np.maximum((b_post - c5) / a0, 0.2)
        h = (tm - self.t0)[None, :]
        m = np.repeat(m_post[:, None], len(tm), 1)
        cpath = np.full(n, "central", dtype=object)
        u = lambda a, b: r.uniform(a, b, n)
        i = scn == 0                                               # slowdown
        m_end = np.minimum(u(0.4, 0.9), m_post)
        m[i] = (m_post[:, None] + (m_end - m_post)[:, None] * np.clip(h / 1.0, 0, 1))[i]
        cpath[i] = "low"
        i = scn == 1                                               # reversion
        m_end = np.maximum((u(0.85, 1.15) * b_pre - c5) / a0, 0.2)
        m[i] = (m_post[:, None] + (m_end - m_post)[:, None] * np.clip(h / 0.5, 0, 1))[i]
        phi = u(*HAIRCUT)
        hi_path = r.random(n) < 0.5
        i = scn == 3                                               # compounding
        raw = np.minimum(m_post[:, None] * 2.0 ** (h / u(0.5, 1.0)[:, None]), np.maximum(u(4.0, 7.5), m_post)[:, None])
        m[i] = (m_post[:, None] + phi[:, None] * (raw - m_post[:, None]))[i]
        cpath[i & hi_path] = "high"
        i = scn == 4                                               # explosive
        D = u(0.25, 0.5)
        peak = np.maximum(np.exp(u(np.log(8.0), np.log(30.0))), m_post)
        t_peak = D * np.log2(peak / m_post)
        up = np.minimum(m_post[:, None] * 2.0 ** (h / D[:, None]), peak[:, None])
        fall = np.clip((h - (t_peak + u(1.0, 2.0))[:, None]) / 0.5, 0, 1)
        raw = up + (u(3.0, 6.0)[:, None] - up) * fall
        m[i] = (m_post[:, None] + phi[:, None] * (raw - m_post[:, None]))[i]
        cpath[i & hi_path] = "high"
        cg = np.empty((n, len(tm)))
        for p in ("low", "central", "high"):
            mk = cpath == p
            if mk.any():
                cg[mk] = compute_growth(p, tm)[None, :]
        pace = kappa[:, None] * np.log10(cg) + a0[:, None] * m
        noise = self.sigma_w * np.sqrt(DT) * r.standard_normal((n, len(tm)))
        inc = pace * DT + noise
        level = L0[:, None] + np.cumsum(inc, axis=1) - inc[:, :1]
        return dict(tm=tm, level=level, pace=pace, scn=scn, b_pre=b_pre, b_post=b_post, L0=L0, m_post=m_post)

    def at(self, P, T):
        """Level of each path at time(s) T (scalar, or one per path), linear interpolation."""
        T = np.asarray(T, float)
        pos = np.clip((T - P["tm"][0]) / DT, 0, len(P["tm"]) - 1 - 1e-9)
        if pos.ndim == 0:
            i0 = int(pos)
            fr = float(pos - i0)
            return P["level"][:, i0] * (1 - fr) + P["level"][:, i0 + 1] * fr
        i0 = pos.astype(int)
        fr = pos - i0
        rr = np.arange(P["level"].shape[0])
        return P["level"][rr, i0] * (1 - fr) + P["level"][rr, i0 + 1] * fr

    def frontier_at(self, P, T, beta=0.0):
        """Draws of the running maximum held at T: max(leader's own (uncertain) value,
        line level lagged by the standing record's age + scatter)."""
        n = P["level"].shape[0]
        r = self.rng
        h = max(T - self.t0, 0.0)
        age = np.minimum(self.ens.sample_age(n, r), h)
        Lt = self.at(P, T - age) + beta * np.minimum(np.maximum(T - age - self.t0, 0), BIAS_H_CAP)
        f0 = r.choice(self.F0_draws, n)
        return np.maximum(Lt + self.S * r.standard_t(NU, n) / T_SD, f0)


def bias_beta(folds, before=None, min_folds=6):
    """Slope of (actual - predicted median) on horizon through the origin, from folds whose
    target precedes `before`. Returns (beta, n)."""
    use = [f for f in folds if before is None or f["T"] < before]
    if len(use) < min_folds:
        return 0.0, len(use)
    h = np.array([min(f["h"], BIAS_H_CAP) for f in use])
    e = np.array([f["err_raw"] for f in use])
    return float((e * h).sum() / (h * h).sum()), len(use)


def bias_beta_se(folds, rng, nboot=400):
    """Block bootstrap (blocks = half-years of origin) standard error of beta."""
    blocks = {}
    for f in folds:
        blocks.setdefault(int(f["t0"] * 2), []).append(f)
    keys = list(blocks)
    out = []
    for _ in range(nboot):
        pick = [blocks[keys[i]] for i in rng.integers(0, len(keys), len(keys))]
        out.append(bias_beta([f for b in pick for f in b], None, 1)[0])
    return float(np.std(out)), len(keys)


def crossing_date(tm, level, thresh):
    thr = np.asarray(thresh, float)[:, None]
    above = level >= thr
    first = above.argmax(axis=1)
    out = np.full(level.shape[0], np.inf)
    rr = np.arange(level.shape[0])
    j = np.maximum(first, 1)
    l0, l1 = level[rr, j - 1], level[rr, j]
    fr = np.clip((thr[:, 0] - l0) / np.maximum(l1 - l0, 1e-9), 0, 1)
    any_ = above.any(axis=1)
    out[any_] = (tm[j - 1] + fr * DT)[any_]
    out[above[:, 0]] = -np.inf
    return out


def date_summary(tc, w, t_now):
    w = np.asarray(w, float)
    already = float(w[np.isneginf(tc)].sum() / w.sum())
    never = float(w[np.isposinf(tc) | (tc > 2031.0)].sum() / w.sum())
    x = np.where(np.isneginf(tc), t_now - 1e-3, np.where(np.isposinf(tc), 2100.0, tc))
    qs = wquantile(x, w, [0.1, 0.5, 0.9])
    f = lambda v: "already" if v <= t_now else ("after 2030" if v > 2031.0 else from_yr(v).isoformat())
    return dict(median=f(qs[1]), q10=f(qs[0]), q90=f(qs[2]), p_already=round(already, 3), p_by_end_2030=round(1 - never, 3))
