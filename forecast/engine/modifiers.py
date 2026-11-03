"""Layer 2 — day-level hazard modifiers and the competitor-pressure test.

All modifiers act multiplicatively on the *daily hazard* (proportional
hazards), never on the pmf directly, so a quiet day pushes probability later
instead of deleting it:

    h'_j = 1 − (1 − h_j) ** m_j

Modifiers:
  weekday      Dirichlet-smoothed profile from releases before the origin
               (Mon/Tue dominate; weekends ≈0; Friday rare)
  holiday      Dec 20 – Jan 4 freeze (no release in 2023–25), US
               Thanksgiving Thu–Fri, and (v3e) US federal election day;
               factor set a priori (0.25), not fitted
  competitor   exp(γ · x_t), x_t = 1 if a competitor shipped a qualifying
               release within the prior `window` days. γ is estimated at
               each origin from data before it, with a N(0, 0.5) prior, and
               the definition of "qualifying" is fixed before looking at
               results (see COMPETITOR_RULES).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

from .cadence import _sf, _trend_z
from .data import d, weekday_profile, holiday_mask, FAMILIES

# Pre-registered definitions (fixed 2026-10-30 before any backtest was run).
COMPETITOR_RULES = {
    "major21": dict(col="is_major", window=21),       # primary
    "sota30": dict(col="took_sota", window=30),        # secondary
}


def thanksgiving_mask(days: pd.DatetimeIndex) -> np.ndarray:
    out = np.zeros(len(days), dtype=bool)
    for i, day in enumerate(days):
        if day.month == 11 and day.weekday() in (3, 4):
            # 4th Thursday of November and the Friday after
            first_thu = 1 + (3 - pd.Timestamp(day.year, 11, 1).weekday()) % 7
            tg = first_thu + 21
            out[i] = day.day in (tg, tg + 1)
    return out


def election_mask(days: pd.DatetimeIndex) -> np.ndarray:
    """US federal general election day: the Tuesday after the first Monday of
    November, even years (2024-11-05, 2026-11-03, 2028-11-07). Added in v3e
    (2026-11-02, Jacob-approved) as a prior, not a fitted effect: the one case
    on record (2024) saw Claude 3.5 Haiku ship the day before, nothing on the day."""
    out = np.zeros(len(days), dtype=bool)
    for i, day in enumerate(days):
        if day.month == 11 and day.year % 2 == 0 and day.weekday() == 1:
            first_mon = 1 + (0 - pd.Timestamp(day.year, 11, 1).weekday()) % 7
            out[i] = day.day == first_mon + 1
    return out


def apply_hazard(pmf: np.ndarray, tail: float, mult: np.ndarray):
    S = 1.0 - np.concatenate([[0.0], np.cumsum(pmf)])  # S[j] = P(T ≥ day j)
    S = np.maximum(S, 1e-15)
    h = np.clip(pmf / S[:-1], 0, 1)
    h2 = 1.0 - (1.0 - h) ** mult
    surv = np.cumprod(1.0 - h2)
    prev = np.concatenate([[1.0], surv[:-1]])
    new = prev * h2
    return new, float(surv[-1])


def competitor_exposure(comp: pd.DataFrame, days: pd.DatetimeIndex, rule="major21") -> np.ndarray:
    if comp is None or comp.empty:
        return np.zeros(len(days))
    r = COMPETITOR_RULES[rule]
    ev = comp.loc[comp[r["col"]] == 1, "date"].values.astype("datetime64[D]")
    if len(ev) == 0:
        return np.zeros(len(days))
    dd = days.values.astype("datetime64[D]")
    # exposed if some event e satisfies 0 < day − e ≤ window
    diff = (dd[:, None] - ev[None, :]).astype(int)
    return ((diff > 0) & (diff <= r["window"])).any(axis=1).astype(float)


def day_multipliers(rel, asof, H, comp=None, gamma=0.0, rule="major21",
                    weekday=True, holiday=True, holiday_factor=0.25):
    days = pd.date_range(d(asof), periods=H, freq="D")
    m = np.ones(H)
    if weekday:
        m *= weekday_profile(rel, asof)[days.weekday]
    if holiday:
        m = np.where(holiday_mask(days) | thanksgiving_mask(days) | election_mask(days), m * holiday_factor, m)
    if gamma and comp is not None:
        # exposure only from competitor releases already public at the origin;
        # future competitor launches are unknown, so their effect is not assumed
        known = comp[comp.date < d(asof)]
        m *= np.exp(gamma * competitor_exposure(known, days, rule))
    return m


def estimate_gamma(cadence_post, rel, comp, asof, rule="major21", start="2024-03-04", n_draws=200, prior_sd=0.5):
    """MAP of the competitor log-hazard ratio from family-days before the origin,
    using the cadence posterior's in-sample daily baseline hazard. Returns
    (gamma, approx_sd, exposed_events, exposed_days)."""
    asof = d(asof)
    days = pd.date_range(d(start), asof - pd.Timedelta(days=1), freq="D")
    if len(days) < 60 or comp is None or comp.empty:
        return 0.0, prior_sd, 0, 0
    x = competitor_exposure(comp[comp.date < asof], days, rule)
    post = cadence_post
    rng = np.random.default_rng(7)
    sel = rng.choice(len(post.sigma), size=min(n_draws, len(post.sigma)), replace=False)
    H_all, Y_all, X_all = [], [], []
    for k, f in enumerate(post.cd.families):
        rd = sorted(rel.loc[(rel.family == f) & (rel.date < asof), "date"].unique())
        if len(rd) < 2:
            continue
        rd = [pd.Timestamp(v) for v in rd]
        rd_arr = np.array(rd, dtype="datetime64[ns]")
        idx = np.searchsorted(rd_arr, days.values, side="left")
        ok = idx >= 1
        prev = rd_arr[np.maximum(idx - 1, 0)]
        c = (days.values - prev).astype("timedelta64[D]").astype(float)
        y = np.isin(days.values.astype("datetime64[D]"), rd_arr.astype("datetime64[D]")).astype(float)
        z = np.array([_trend_z(pd.Timestamp(p), asof, post.cd.trend) if o else 0.0 for p, o in zip(prev, ok)])
        m = post.mu[sel, k][:, None] + post.beta[sel][:, None] * z[None, :]
        s = post.sigma_f[sel, k][:, None]
        lx0 = (np.log(np.maximum(c, 0.5))[None, :] - m) / s
        lx1 = (np.log(np.maximum(c + 1, 0.5))[None, :] - m) / s
        S0, S1 = _sf(lx0, post.err), _sf(lx1, post.err)
        h = np.clip(((S0 - S1) / np.maximum(S0, 1e-12)).mean(axis=0), 1e-6, 0.999)
        # the release day itself counts as the event at age c (c ≥ 1)
        H_all.append(h[ok & (c >= 1)]); Y_all.append(y[ok & (c >= 1)]); X_all.append(x[ok & (c >= 1)])
    if not H_all:
        return 0.0, prior_sd, 0, 0
    h, y, xx = map(np.concatenate, (H_all, Y_all, X_all))

    def nlp(g):
        hh = 1 - (1 - h) ** np.exp(g * xx)
        hh = np.clip(hh, 1e-9, 1 - 1e-9)
        return -(np.sum(y * np.log(hh) + (1 - y) * np.log1p(-hh)) - 0.5 * (g / prior_sd) ** 2)

    res = minimize_scalar(nlp, bounds=(-3, 3), method="bounded")
    g = float(res.x)
    eps = 1e-3
    curv = (nlp(g + eps) - 2 * nlp(g) + nlp(g - eps)) / eps ** 2
    sd = float(1 / np.sqrt(max(curv, 1e-6)))
    return g, sd, int((y * xx).sum()), int(xx.sum())
