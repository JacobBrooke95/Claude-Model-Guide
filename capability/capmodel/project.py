"""Long-range projection, 2026-2030: Monte Carlo over a scenario mixture.

The pace of the Anthropic frontier on the public-ECI scale is decomposed with the driver
tables in data/raw (research note 1):

    pace(t) = KAPPA * log10(compute growth factor in year t) + a0 * m(t)

  KAPPA  ECI points per 10x training compute (~9; research note 1, 'approximate')
  a0     algorithmic contribution at the pre-break pace: a0 = b_pre - KAPPA*log10(5)
         (5x/yr = Epoch's training-compute trend, drivers_compute.csv)
  m(t)   multiplier on algorithmic progress (1 = pre-break). The post-break public slope
         implies m_post = (b_post - KAPPA*log10(5)) / a0.

b_pre, b_post are posterior draws from the hinge fit to Anthropic's public-ECI records.
Scenarios differ only in the compute path and in m(t); nothing else is free-hand.
"""
from __future__ import annotations
import numpy as np

from .common import yr, AS_OF, wquantile, wsummary, from_yr
from .trend import NU

T_NOW = yr(AS_OF)
SCENARIOS = ["slowdown", "reversion", "hold", "compounding", "explosive"]
QUARTERS = [f"{y}-{md}" for y in range(2026, 2031) for md in ("03-31", "06-30", "09-30", "12-31")]
QUARTERS = [qd for qd in QUARTERS if yr(qd) > T_NOW]
TQ = np.array([yr(qd) for qd in QUARTERS])
DT = 1.0 / 12
TM = np.arange(T_NOW, 2031.0 + 1e-9, DT)        # monthly integration grid

COMPUTE = {   # frontier training compute growth, x/yr, from driver_scenarios_2026_2030.csv
    "low": {2026: 5.0, 2027: 2.5, 2028: 2.0, 2029: 1.5, 2030: 1.5},
    "central": {2026: 5.0, 2027: 5.0, 2028: 4.0, 2029: 3.0, 2030: 2.5},
    "high": {2026: 5.0, 2027: 5.0, 2028: 5.0, 2029: 5.0, 2030: 5.0},
}
KAPPA_MEAN, KAPPA_SD = 9.0, 2.0        # ECI per 10x compute (assumption with stated uncertainty)
HAIRCUT = (0.6, 1.0)                   # realised share of scenario-style acceleration (AI 2027 ran at ~60-75%)
FAMILY_DRIFT_SD = 1.5                  # ECI points per sqrt(year): slow re-ranking of family offsets (assumption)

SCENARIO_DEFS = {
    "slowdown": "Compute/supply-limited: training-compute growth falls on the 'low' driver path (2.5x, 2x, 1.5x, 1.5x "
                "per year 2027-30) and algorithmic progress falls back to 0.6-1.0x its pre-break rate within a year.",
    "reversion": "One-time jump: the 2025-26 step up was a level shift. Pace returns within six months to 1.0-1.4x the "
                 "pre-break slope (at 5x/yr compute), then follows the 'central' compute path down.",
    "hold": "New trend holds: algorithmic progress stays at the multiplier implied by the post-break slope; compute "
            "follows the 'central' driver path (5x, 4x, 3x, 2.5x).",
    "compounding": "AI R&D feedback: the algorithmic multiplier doubles every 6-12 months until it reaches 4-7.5x "
                   "(total pace ~3-5x pre-break, as in research note 3), then stays there; 60-100% of the excess over "
                   "'hold' is realised; compute on the 'central' or 'high' path.",
    "explosive": "Bounded explosive tail: the multiplier doubles every 3-6 months to a peak of 8-30x (Forethought's "
                 "'won't be 30X' cap), holds 1-2 years, then settles at 3-6x; same 60-100% realisation haircut.",
}
WEIGHTS = {   # documented priors; see METHODS.md section 8 for the evidence behind each
    "central":         {"slowdown": 0.10, "reversion": 0.27, "hold": 0.38, "compounding": 0.19, "explosive": 0.06},
    "sceptic":         {"slowdown": 0.20, "reversion": 0.45, "hold": 0.28, "compounding": 0.06, "explosive": 0.01},
    "accelerationist": {"slowdown": 0.00, "reversion": 0.15, "hold": 0.35, "compounding": 0.30, "explosive": 0.20},
}


def compute_growth(path, t):
    y = np.clip(np.floor(t).astype(int), 2026, 2030)
    tab = COMPUTE[path]
    return np.array([tab[int(v)] for v in y])


def simulate(scn, n, rng, L0, b_pre, b_post, sigma_w):
    """n monthly paths of the Anthropic record-line level under one scenario.
    Returns level (n, len(TM)), pace (n, len(TM)), and the driver draws."""
    kappa = np.clip(KAPPA_MEAN + KAPPA_SD * rng.standard_normal(n), 4.0, 14.0)
    c5 = kappa * np.log10(5.0)
    a0 = np.maximum(b_pre - c5, 2.0)
    m_post = np.maximum((b_post - c5) / a0, 0.3)
    h = (TM - T_NOW)[None, :]
    if scn == "slowdown":
        cpath = np.array(["low"] * n)
        m_end = rng.uniform(0.6, 1.0, n)
        m = m_post[:, None] + (m_end - m_post)[:, None] * np.clip(h / 1.0, 0, 1)
    elif scn == "reversion":
        cpath = np.array(["central"] * n)
        k = rng.uniform(1.0, 1.4, n)
        m_end = (k * b_pre - c5) / a0
        m = m_post[:, None] + (m_end - m_post)[:, None] * np.clip(h / 0.5, 0, 1)
    elif scn == "hold":
        cpath = np.array(["central"] * n)
        m = np.repeat(m_post[:, None], len(TM), 1)
    elif scn == "compounding":
        cpath = np.where(rng.random(n) < 0.5, "central", "high")
        D = rng.uniform(0.5, 1.0, n)
        cap = np.maximum(rng.uniform(4.0, 7.5, n), m_post)
        raw = np.minimum(m_post[:, None] * 2.0 ** (h / D[:, None]), cap[:, None])
        phi = rng.uniform(*HAIRCUT, n)
        m = m_post[:, None] + phi[:, None] * (raw - m_post[:, None])
    elif scn == "explosive":
        cpath = np.where(rng.random(n) < 0.5, "central", "high")
        D = rng.uniform(0.25, 0.5, n)
        peak = np.maximum(np.exp(rng.uniform(np.log(8.0), np.log(30.0), n)), m_post)
        t_peak = D * np.log2(peak / m_post)                     # years until the peak is reached
        dur = rng.uniform(1.0, 2.0, n)
        settle = rng.uniform(3.0, 6.0, n)
        up = np.minimum(m_post[:, None] * 2.0 ** (h / D[:, None]), peak[:, None])
        fall = np.clip((h - (t_peak + dur)[:, None]) / 0.5, 0, 1)
        raw = up + (settle[:, None] - up) * fall
        phi = rng.uniform(*HAIRCUT, n)
        m = m_post[:, None] + phi[:, None] * (raw - m_post[:, None])
    else:
        raise ValueError(scn)
    cg = np.empty((n, len(TM)))
    for p in ("low", "central", "high"):
        mk = cpath == p
        if mk.any():
            cg[mk] = compute_growth(p, TM)[None, :]
    pace = kappa[:, None] * np.log10(cg) + a0[:, None] * m
    noise = sigma_w * np.sqrt(DT) * rng.standard_normal((n, len(TM)))
    level = L0[:, None] + np.cumsum(pace * DT + noise, axis=1) - (pace[:, :1] * DT + noise[:, :1])
    return level, pace, dict(kappa=kappa, a0=a0, m_post=m_post, m=m)


def at_quarters(x):
    """Interpolate monthly paths (n, len(TM)) to quarter ends (n, len(TQ))."""
    pos = (TQ - TM[0]) / DT
    i0 = np.clip(pos.astype(int), 0, len(TM) - 2)
    fr = pos - i0
    return x[:, i0] * (1 - fr) + x[:, i0 + 1] * fr


def bands(x, w, nd=2):
    """Weighted bands per quarter for x (n, Q)."""
    return [dict(date=QUARTERS[j], **wsummary(x[:, j], w, nd)) for j in range(x.shape[1])]


def crossing_date(level, thresh):
    """First time each monthly path reaches its threshold (linear interpolation);
    -inf if already there at the start, +inf if not reached by the end of the grid."""
    thr = np.asarray(thresh, float)[:, None]
    above = level >= thr
    first = above.argmax(axis=1)
    any_ = above.any(axis=1)
    out = np.full(level.shape[0], np.inf)
    r = np.arange(level.shape[0])
    j = np.maximum(first, 1)
    l0, l1 = level[r, j - 1], level[r, j]
    fr = np.clip((thr[:, 0] - l0) / np.maximum(l1 - l0, 1e-9), 0, 1)
    out[any_] = (TM[j - 1] + fr * DT)[any_]
    out[above[:, 0]] = -np.inf
    return out


def date_summary(tc, w):
    """Summarise crossing times with weights; handles 'already' and 'not by end-2030'."""
    w = np.asarray(w, float)
    already = float(w[np.isneginf(tc)].sum() / w.sum())
    never = float(w[np.isposinf(tc) | (tc > 2031.0)].sum() / w.sum())
    x = np.where(np.isneginf(tc), T_NOW - 1e-3, np.where(np.isposinf(tc), 2100.0, tc))
    qs = wquantile(x, w, [0.1, 0.5, 0.9])
    f = lambda v: "already" if v <= T_NOW else ("after 2030" if v > 2031.0 else from_yr(v).isoformat())
    return dict(median=f(qs[1]), q10=f(qs[0]), q90=f(qs[2]), p_already=round(already, 3), p_by_end_2030=round(1 - never, 3))
