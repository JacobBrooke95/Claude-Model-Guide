"""Layer 1 — hierarchical renewal (cadence) model.

Each family's inter-release gaps are modelled as

    log g_{f,i} = mu_f + beta * z_{f,i} + eps,   eps ~ Normal(0, sigma) or Student-t(nu=4)
    mu_f        = mu0 + tau * eta_f,             eta_f ~ N(0, 1)   (partial pooling)

with z = (interval start − origin) in years, so mu_f is the family's log-gap
"now" and beta is the shared acceleration of the whole lineup. Each family's
open interval (last release → origin, no release yet) enters as a right-
censored observation, which is what lets a long silence push the forecast out
instead of being ignored.

Fitted by adaptive random-walk Metropolis (non-centred). n is tiny (≈25 gaps),
so the priors carry real weight and are stated here in full:

    mu0   ~ N(log 90d, 0.8)     tau  ~ HalfNormal(0.6)
    beta  ~ N(0, 0.4) per year  sigma ~ HalfNormal(0.6)

Output: for each family a posterior predictive daily pmf of the next release
date, conditional on no release between the last one and the origin.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import log_ndtr, ndtr, stdtr, gammaln

from .data import FAMILIES, family_history, d

LOG90 = np.log(90.0)
NU = 4.0


# Error families for the standardized log-gap x = (log g - m) / sigma.
#   normal  -> log-normal gaps (hazard rises then falls: an overdue release
#              looks *less* likely each day — the sensitivity case)
#   t       -> log-t(4): heavier tails, robust to the 444-day Opus gap
#   weibull -> x ~ standard minimum-extreme-value, so g ~ Weibull with
#              shape k = 1/sigma; k > 1 gives a hazard that keeps rising
#              when a release is overdue (the pipeline-delay intuition)
_T_LOGC = float(gammaln((NU + 1) / 2) - gammaln(NU / 2) - 0.5 * np.log(NU * np.pi))
_HALF_LOG_2PI = 0.5 * np.log(2 * np.pi)


def _logsf(x, err):
    if err == "normal":
        return log_ndtr(-x)
    if err == "t":
        return np.log(np.maximum(stdtr(NU, -x), 1e-300))
    return -np.exp(np.minimum(x, 50))


def _logpdf(x, err):
    if err == "normal":
        return -0.5 * x * x - _HALF_LOG_2PI
    if err == "t":
        return _T_LOGC - (NU + 1) / 2 * np.log1p(x * x / NU)
    return x - np.exp(np.minimum(x, 50))


def _sf(x, err):
    if err == "normal":
        return ndtr(-x)
    if err == "t":
        return stdtr(NU, -x)
    return np.exp(-np.exp(np.minimum(x, 50)))


# Calendar-trend options for the log-gap level:
#   linear      -> beta * (interval start − origin) in years
#   changepoint -> beta * years *before* BREAK (0 after it): gaps were longer
#                  before the lineup settled into its 2025+ rhythm, flat since
#   none        -> no trend term (beta pinned at 0)
BREAK = pd.Timestamp("2025-06-01")


def _trend_z(start: pd.Timestamp, asof: pd.Timestamp, trend: str) -> float:
    if trend == "linear":
        return (start - asof).days / 365.25
    if trend == "changepoint":
        return max(0.0, (BREAK - start).days / 365.25)
    return 0.0


class CadenceData:
    """Gaps and censored open intervals for every family as of an origin."""

    def __init__(self, rel: pd.DataFrame, asof, families=FAMILIES, min_events=1, trend="changepoint", half_life=None,
                 fam_sigma=False):
        self.asof = d(asof)
        self.fam_sigma = fam_sigma
        self.trend = trend
        self.half_life = half_life
        self.families = []
        fam_idx, logg, z, cens, wts = [], [], [], [], []
        self.last = {}
        for f in families:
            hist = family_history(rel, f, asof)
            if len(hist) < min_events:
                continue
            k = len(self.families)
            self.families.append(f)
            self.last[f] = hist[-1]
            for a, b in zip(hist[:-1], hist[1:]):
                gap = max((b - a).days, 1)
                fam_idx.append(k); logg.append(np.log(gap)); z.append(_trend_z(a, self.asof, trend)); cens.append(0)
                # recency weight (power prior): a gap that ended `age` years ago counts 0.5**(age/half_life)
                age = (self.asof - b).days / 365.25
                wts.append(1.0 if not half_life else 0.5 ** (age / half_life))
            open_gap = max((self.asof - hist[-1]).days, 1)
            fam_idx.append(k); logg.append(np.log(open_gap)); z.append(_trend_z(hist[-1], self.asof, trend)); cens.append(1)
            wts.append(1.0)
        self.fam_idx = np.array(fam_idx, dtype=int)
        self.logg = np.array(logg)
        self.z = np.array(z)
        self.cens = np.array(cens, dtype=bool)
        self.w = np.array(wts)
        self.F = len(self.families)


SIGMA_SPREAD = 0.35  # sd of log sigma_f around the shared sigma when fam_sigma is on


def log_post(theta, cd: CadenceData, err: str):
    F = cd.F
    mu0, log_tau, beta, log_sigma = theta[:4]
    eta = theta[4:4 + F]
    tau, sigma = np.exp(log_tau), np.exp(log_sigma)
    mu = mu0 + tau * eta
    m = mu[cd.fam_idx] + beta * cd.z
    if cd.fam_sigma:
        zeta = theta[4 + F:4 + 2 * F]
        sig_i = (sigma * np.exp(SIGMA_SPREAD * zeta))[cd.fam_idx]
        extra = -0.5 * np.dot(zeta, zeta)
    else:
        sig_i, extra = sigma, 0.0
    x = (cd.logg - m) / sig_i
    ll = (cd.w * np.where(cd.cens, _logsf(x, err), _logpdf(x, err) - np.log(sig_i))).sum() + extra
    bsd = 0.4 if cd.trend == "linear" else (0.6 if cd.trend == "changepoint" else 1e-3)
    lp = (-0.5 * ((mu0 - LOG90) / 0.8) ** 2
          - 0.5 * (tau / 0.6) ** 2 + log_tau          # half-normal + Jacobian for log-scale
          - 0.5 * (beta / bsd) ** 2
          - 0.5 * (sigma / 0.6) ** 2 + log_sigma
          - 0.5 * np.dot(eta, eta))
    return ll + lp


def fit(cd: CadenceData, err="weibull", n_iter=5000, burn=1500, thin=7, seed=0):
    rng = np.random.default_rng(seed)
    dim = 4 + cd.F * (2 if cd.fam_sigma else 1)
    theta = np.concatenate([[LOG90, np.log(0.3), 0.0, np.log(0.4)], np.zeros(dim - 4)])
    lp = log_post(theta, cd, err)
    scale = np.full(dim, 0.15)
    draws, acc = [], 0
    for it in range(n_iter):
        prop = theta + rng.normal(0, scale)
        lpp = log_post(prop, cd, err)
        if np.log(rng.random()) < lpp - lp:
            theta, lp = prop, lpp
            acc += 1
        # Robbins–Monro step-size adaptation during burn-in only
        if it < burn and it % 100 == 99:
            rate = acc / 100.0
            scale *= np.exp(rate - 0.25)
            acc = 0
        if it >= burn and (it - burn) % thin == 0:
            draws.append(theta.copy())
    return np.array(draws)


class CadencePosterior:
    def __init__(self, cd: CadenceData, draws: np.ndarray, err: str):
        self.cd, self.draws, self.err = cd, draws, err
        F = cd.F
        mu0, tau, beta, sigma = draws[:, 0], np.exp(draws[:, 1]), draws[:, 2], np.exp(draws[:, 3])
        self.mu = mu0[:, None] + tau[:, None] * draws[:, 4:4 + F]
        self.beta, self.sigma = beta, sigma
        if cd.fam_sigma:
            self.sigma_f = sigma[:, None] * np.exp(SIGMA_SPREAD * draws[:, 4 + F:4 + 2 * F])
        else:
            self.sigma_f = np.repeat(sigma[:, None], F, axis=1)

    def params(self):
        out = {f: {"median_gap_now_days": float(np.exp(np.median(self.mu[:, k]))),
                   "sigma": float(np.median(self.sigma_f[:, k]))}
               for k, f in enumerate(self.cd.families)}
        out["_shared"] = {
            "beta_per_year": float(np.median(self.beta)),
            "beta_90ci": [float(x) for x in np.percentile(self.beta, [5, 95])],
            "sigma": float(np.median(self.sigma)),
            "gap_multiplier_per_year": float(np.exp(np.median(self.beta))),
        }
        return out

    def pmf(self, family: str, horizon: int = 400):
        """Daily pmf over origin+0 .. origin+horizon-1 (index 0 = origin day)
        and the remaining survival mass beyond the horizon."""
        k = self.cd.families.index(family)
        last = self.cd.last[family]
        c = (self.cd.asof - last).days  # days already elapsed
        zc = _trend_z(last, self.cd.asof, self.cd.trend)
        m = self.mu[:, k] + self.beta * zc  # (S,)
        s = self.sigma_f[:, k]
        # survival at elapsed day counts c, c+1, ..., c+horizon
        ages = c + np.arange(horizon + 1)
        lx = (np.log(np.maximum(ages, 0.5))[None, :] - m[:, None]) / s[:, None]
        S = _sf(lx, self.err)
        S0 = np.maximum(S[:, :1], 1e-12)
        cond = S / S0                       # P(T > origin+j | T > origin, θ)
        surv = cond.mean(axis=0)            # posterior predictive survival
        pmf = surv[:-1] - surv[1:]
        return pmf, float(surv[-1])


def fit_posterior(rel, asof, err="weibull", trend="changepoint", families=FAMILIES, seed=0, half_life=None,
                  fam_sigma=False, **kw):
    cd = CadenceData(rel, asof, families=families, trend=trend, half_life=half_life, fam_sigma=fam_sigma)
    draws = fit(cd, err=err, seed=seed, **kw)
    return CadencePosterior(cd, draws, err)
