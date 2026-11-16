"""Frontier trend models on the latent ability scale.

A *frontier series* is the set of record-setting releases (running maximum of ECI by
release date). Each candidate trend form is a regression that is linear in its
coefficients given a structural parameter tau (changepoint date), fitted with Student-t
errors by IRLS. Uncertainty comes from three places:

  1. which models exist      - bootstrap over models (resample with replacement)
  2. what their abilities are - one of Epoch's 500 joint posterior draws per replicate;
                                the record set is recomputed for every replicate, so the
                                winner's-curse selection of noisy records is propagated
  3. the fit itself           - multivariate-t draws of the coefficients, and a profile
                                likelihood over tau for the changepoint forms

Two estimands are kept apart:
  level L(T)    the height of the line through record points at date T
                (what a new record-setter released at T is expected to score)
  frontier F(T) the running maximum actually held at T: a step function that sits at or
                below the line, F(T) = max(F(t0), L(T - A) + e), with A the age of the
                standing record. A is drawn from the observed record gaps.
"""
from __future__ import annotations
import numpy as np
from scipy import optimize, special

NU = 4.0            # Student-t degrees of freedom for residuals (fixed; robust to outliers)
S_FLOOR = 0.75      # floor on residual scale, ECI points (assumption: ECI posterior sd at the
                    # frontier is ~1-2 points, so a fitted scale below this is an artefact of small n)
CANDS = ["lin_all", "lin_24", "lin_12", "hinge", "jump", "quad"]


def records(t, y, start=None):
    """Indices (into t-sorted arrays) of running-maximum setters at or after `start`."""
    best, out = -np.inf, []
    for i in range(len(t)):
        if start is not None and t[i] < start:
            continue
        if y[i] > best:
            best = y[i]
            out.append(i)
    return np.asarray(out, int)


def t_irls(X, y, nu=NU, iters=20):
    n, p = X.shape
    w = np.ones(n)
    beta = np.zeros(p)
    s2 = 1.0
    for _ in range(iters):
        XtW = X.T * w
        A = XtW @ X + 1e-8 * np.eye(p)
        beta = np.linalg.solve(A, XtW @ y)
        r = y - X @ beta
        s2 = max(float((w * r * r).sum()) / max(n - p, 1), S_FLOOR ** 2)
        w = (nu + 1.0) / (nu + r * r / s2)
    s = np.sqrt(s2)
    z = (y - X @ beta) / s
    ll = float(np.sum(special.gammaln((nu + 1) / 2) - special.gammaln(nu / 2) - 0.5 * np.log(nu * np.pi)
                      - np.log(s) - (nu + 1) / 2 * np.log1p(z * z / nu)))
    cov = np.linalg.inv((X.T * w) @ X + 1e-8 * np.eye(p))
    return beta, s, cov, ll


def _design(kind, u, tau=None):
    one = np.ones_like(u)
    if kind == "lin":
        return np.column_stack([one, u])
    if kind == "hinge":
        return np.column_stack([one, u, np.maximum(u - tau, 0.0)])
    if kind == "jump":
        return np.column_stack([one, u, (u >= tau).astype(float)])
    if kind == "quad":
        return np.column_stack([one, u, u * u])
    raise ValueError(kind)


class Fit:
    """One fitted candidate on one replicate. Times are in years relative to the origin t0."""

    def __init__(self, kind, t0, u, y):
        self.kind, self.t0, self.n = kind, t0, len(u)
        self.parts = []   # (weight, tau, beta, s, cov)
        if kind in ("hinge", "jump"):
            taus = tau_grid(u)
            if len(taus) == 0:
                kind = self.kind_eff = "lin"
            else:
                lls, fits = [], []
                for tau in taus:
                    b, s, c, ll = t_irls(_design(kind, u, tau), y)
                    lls.append(ll)
                    fits.append((tau, b, s, c))
                lls = np.asarray(lls)
                w = np.exp(lls - lls.max())
                w /= w.sum()
                self.parts = [(w[i],) + fits[i] for i in range(len(taus)) if w[i] > 1e-4]
                self.ll = float(lls.max())
                self.k = 5   # 3 coefficients + scale + tau
        if kind in ("lin", "quad"):
            b, s, c, ll = t_irls(_design(kind, u), y)
            self.parts = [(1.0, None, b, s, c)]
            self.ll = ll
            self.k = len(b) + 1
        self.kind_eff = kind
        self.df = max(self.n - (self.k - 1), 2)
        ws = np.array([p[0] for p in self.parts])
        self._w = ws / ws.sum()

    def bic(self):
        return -2 * self.ll + self.k * np.log(max(self.n, 2))

    def sample(self, tnew, n, rng):
        """n draws of (level at each tnew, residual scale). Shape (n, len(tnew)), (n,)."""
        u = np.atleast_1d(np.asarray(tnew, float)) - self.t0
        idx = rng.choice(len(self.parts), size=n, p=self._w)
        out = np.empty((n, len(u)))
        ss = np.empty(n)
        for j in np.unique(idx):
            _, tau, b, s, c = self.parts[j]
            m = idx == j
            k = int(m.sum())
            L = np.linalg.cholesky(c * s * s + 1e-10 * np.eye(len(b)))
            g = rng.standard_normal((k, len(b))) @ L.T
            g /= np.sqrt(rng.chisquare(self.df, size=k) / self.df)[:, None]
            X = _design(self.kind_eff, u, tau)
            out[m] = (b + g) @ X.T
            ss[m] = s
        return out, ss

    def mean(self, tnew):
        """Posterior-mean line at tnew (weighted over changepoints)."""
        u = np.atleast_1d(np.asarray(tnew, float)) - self.t0
        return sum(w * (_design(self.kind_eff, u, p[1]) @ p[2]) for w, p in zip(self._w, self.parts))

    def sample_slopes(self, n, rng):
        """Draws of (pre slope, post slope, tau) for a hinge fit, with coefficient uncertainty."""
        idx = rng.choice(len(self.parts), size=n, p=self._w)
        out = np.empty((n, 3))
        for j in np.unique(idx):
            _, tau, b, s, c = self.parts[j]
            m = idx == j
            k = int(m.sum())
            L = np.linalg.cholesky(c * s * s + 1e-10 * np.eye(len(b)))
            g = rng.standard_normal((k, len(b))) @ L.T
            g /= np.sqrt(rng.chisquare(self.df, size=k) / self.df)[:, None]
            bb = b + g
            post = bb[:, 1] + (bb[:, 2] if self.kind_eff == "hinge" else 0.0)
            out[m] = np.column_stack([bb[:, 1], post, np.full(k, (tau if tau is not None else np.nan) + self.t0 if tau is not None else np.nan)])
        return out

    def slopes(self):
        """Posterior-mean pre/post slopes (points/yr) and tau (absolute year) where defined."""
        w = self._w
        if self.kind_eff == "hinge":
            pre = sum(wi * p[2][1] for wi, p in zip(w, self.parts))
            post = sum(wi * (p[2][1] + p[2][2]) for wi, p in zip(w, self.parts))
            tau = sum(wi * p[1] for wi, p in zip(w, self.parts)) + self.t0
            return pre, post, tau
        if self.kind_eff == "jump":
            pre = sum(wi * p[2][1] for wi, p in zip(w, self.parts))
            tau = sum(wi * p[1] for wi, p in zip(w, self.parts)) + self.t0
            return pre, pre, tau
        b = self.parts[0][2]
        return b[1], b[1], None


def tau_grid(u, min_after=3, min_before=3, step=1 / 12):
    """Changepoint grid: at least `min_before` points before and `min_after` at/after tau."""
    us = np.sort(u)
    if len(us) < min_before + min_after:
        return np.array([])
    lo, hi = us[min_before - 1] + 1e-6, us[-min_after] - 1e-6
    if hi <= lo:
        return np.array([])
    return np.arange(lo, hi + 1e-9, step)


def fit_candidate(name, t, y, t0):
    u = np.asarray(t, float) - t0
    y = np.asarray(y, float)
    if name == "lin_all":
        return Fit("lin", t0, u, y)
    if name in ("lin_24", "lin_12"):
        win = 2.0 if name == "lin_24" else 1.0
        m = u >= -win
        if m.sum() < 4:                # too few records in the window: widen it
            m = u >= -2.0
        if m.sum() < 4:
            m = np.ones_like(u, bool)
        return Fit("lin", t0, u[m], y[m])
    if name == "quad":
        m = u >= -3.0
        if m.sum() < 5:
            m = np.ones_like(u, bool)
        return Fit("quad" if m.sum() >= 5 else "lin", t0, u[m], y[m])
    return Fit(name, t0, u, y)


class Series:
    """All models of a group with release time and the matrix of ability draws."""

    def __init__(self, t, Y, y_pub, names=None, start=None):
        o = np.argsort(t, kind="stable")
        self.t, self.Y, self.y = np.asarray(t, float)[o], np.asarray(Y, float)[o], np.asarray(y_pub, float)[o]
        self.names = None if names is None else list(np.asarray(names)[o])
        self.start = start

    def cut(self, t0):
        m = self.t < t0
        return Series(self.t[m], self.Y[m], self.y[m], None if self.names is None else np.asarray(self.names)[m],
                      self.start)

    def published_records(self):
        idx = records(self.t, self.y, self.start)
        return self.t[idx], self.y[idx], idx

    def replicate(self, rng, resample=True):
        n = len(self.t)
        idx = np.sort(rng.integers(0, n, n)) if resample else np.arange(n)
        idx = np.unique(idx)
        d = rng.integers(0, self.Y.shape[1])
        t, y = self.t[idx], self.Y[idx, d]
        r = records(t, y, self.start)
        return t[r], y[r]


class Ensemble:
    """Fits of every candidate on B replicates of a frontier series, as of origin t0."""

    def __init__(self, series: Series, t0, B, rng, cands=CANDS):
        self.t0, self.cands = t0, list(cands)
        s = series.cut(t0)
        self.series = s
        self.rt, self.ry, _ = s.published_records()
        self.fits = {c: [] for c in cands}
        reps = [(self.rt, self.ry)] + [s.replicate(rng) for _ in range(B)]
        for (t, y) in reps:
            if len(t) < 4:
                continue
            for c in cands:
                self.fits[c].append(fit_candidate(c, t, y, t0))
        self.ok = all(len(v) > 0 for v in self.fits.values())
        self.F0 = float(self.ry[-1]) if len(self.ry) else np.nan
        gaps = np.diff(self.rt)
        self.gaps = gaps[-12:] if len(gaps) else np.array([0.15])   # recent record gaps, years

    def sample_level(self, cand, tnew, n, rng):
        fits = self.fits[cand]
        per = int(np.ceil(n / len(fits)))
        L, S = [], []
        for f in fits:
            a, b = f.sample(tnew, per, rng)
            L.append(a)
            S.append(b)
        L, S = np.concatenate(L)[:n], np.concatenate(S)[:n]
        p = rng.permutation(len(L))
        return L[p], S[p]

    def sample_age(self, n, rng):
        g = rng.choice(self.gaps, size=n, p=self.gaps / self.gaps.sum())   # length-biased
        return g * rng.random(n)

    def sample_frontier(self, cand, T, n, rng):
        """Draws of the running-max frontier value held at date T (scalar)."""
        age = np.minimum(self.sample_age(n, rng), max(T - self.t0, 0.0) + 1e-9)
        fits = self.fits[cand]
        out = np.empty(n)
        which = rng.integers(0, len(fits), n)
        for j in np.unique(which):
            m = which == j
            # evaluate each draw at its own T - age
            Lm, Sm = fits[j].sample(T - age[m], int(m.sum()), rng)
            k = int(m.sum())
            out[m] = Lm[np.arange(k), np.arange(k)]
            out[m] += Sm * rng.standard_t(NU, int(m.sum()))
        return np.maximum(out, self.F0)


def crps_sample(x, y):
    x = np.sort(np.asarray(x, float))
    n = len(x)
    e1 = np.mean(np.abs(x - y))
    e2 = 2.0 * np.sum((2 * np.arange(1, n + 1) - n - 1) * x) / (n * n)   # E|X - X'|
    return float(e1 - 0.5 * e2)


def _cross_abs(a, b):
    """E|A - B| for two samples (subsampled for speed)."""
    a = np.asarray(a)[:200]
    b = np.asarray(b)[:200]
    return float(np.mean(np.abs(a[:, None] - b[None, :])))


def stack_crps(sample_sets, ys, floor=0.05):
    """Stacking weights that minimise the mean CRPS of the mixture predictive.

    sample_sets: list over folds of list over K components of sample arrays.
    CRPS of a mixture is quadratic in the weights:
        sum_k w_k E|X_k - y| - 0.5 sum_kl w_k w_l E|X_k - X_l|.
    Every component keeps at least `floor` weight: the folds are few and overlap, and an
    unfloored optimum puts ~all weight on whichever candidate was least biased.
    """
    K = len(sample_sets[0])
    a = np.zeros(K)
    Bm = np.zeros((K, K))
    for comps, y in zip(sample_sets, ys):
        for k in range(K):
            a[k] += np.mean(np.abs(comps[k] - y))
            for l in range(k, K):
                v = _cross_abs(comps[k], comps[l])
                Bm[k, l] += v
                Bm[l, k] = Bm[k, l]
    a /= len(ys)
    Bm /= len(ys)
    f = lambda w: float(w @ a - 0.5 * w @ Bm @ w)
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}]
    best = None
    for w0 in [np.full(K, 1 / K)] + [np.eye(K)[k] * 0.9 + 0.1 / K for k in range(K)]:
        r = optimize.minimize(f, w0, bounds=[(floor, 1)] * K, constraints=cons, method="SLSQP")
        if best is None or r.fun < best.fun:
            best = r
    w = np.clip(best.x, floor, 1)
    w /= w.sum()
    return w, float(best.fun), a


def mixture_sample(comps, w, n, rng):
    """Draw n values from a weighted mixture of sample arrays."""
    k = rng.choice(len(comps), size=n, p=w)
    out = np.empty(n)
    for j in np.unique(k):
        m = k == j
        out[m] = rng.choice(comps[j], size=int(m.sum()))
    return out


def break_analysis(t, y, t0):
    """Fit the four forms to one record series and report BIC weights, slopes and tau.
    Used for the 'was there a break' tables (not for forecasting)."""
    out = {}
    u = np.asarray(t) - t0
    forms = {"linear": Fit("lin", t0, u, y), "hinge": Fit("hinge", t0, u, y),
             "jump": Fit("jump", t0, u, y), "quadratic": Fit("quad", t0, u, y)}
    bics = {k: f.bic() for k, f in forms.items()}
    mn = min(bics.values())
    w = {k: np.exp(-0.5 * (b - mn)) for k, b in bics.items()}
    tot = sum(w.values())
    for k, f in forms.items():
        pre, post, tau = f.slopes()
        out[k] = {"bic": round(bics[k], 2), "bic_weight": round(w[k] / tot, 3), "slope_pre": round(float(pre), 2),
                  "slope_post": round(float(post), 2), "tau": None if tau is None else round(float(tau), 3),
                  "resid_scale": round(float(np.mean([p[3] for p in f.parts])), 2), "n": int(f.n)}
    h = forms["hinge"]
    taus = np.array([p[1] for p in h.parts]) + t0
    ws = h._w
    cs = np.cumsum(ws[np.argsort(taus)])
    ts = np.sort(taus)
    out["hinge"]["tau_q10"] = round(float(ts[np.searchsorted(cs, 0.1)]), 3)
    out["hinge"]["tau_q90"] = round(float(ts[min(np.searchsorted(cs, 0.9), len(ts) - 1)]), 3)
    out["hinge"]["ratio"] = round(float(out["hinge"]["slope_post"] / out["hinge"]["slope_pre"]), 3)
    return out, forms


def envelope(rt, ry, t):
    """Anthropic frontier envelope: linear interpolation between record points, flat
    before the first and after the last. A release's offset is measured against it."""
    return np.interp(np.asarray(t, float), rt, ry)
