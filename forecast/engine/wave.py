"""Layer 1b — the two-level "wave" model.

Per-family renewals treat Opus, Sonnet, Haiku, Fable and Mythos as
independent clocks. They are not: Anthropic co-launches (Claude 3, Claude 4,
Fable+Mythos twice) and staggers (Opus 5.5 → Sonnet 5.5 → Haiku 5.5 over 15
days). The wave model uses every distinct release *day* as one event of a
single company-level renewal process (≈27 events instead of 2–9 per family),
then decides which families ride each wave:

    wave gaps:   same Bayesian renewal as cadence.py, one pseudo-family "wave"
    inclusion:   logit P(family f ships in a wave) = a_f + b·(log days-since-f − log 90)
                 fitted conditionally on the wave being non-empty

Fable and Mythos have only ever shipped together or as a Mythos-only preview,
so they share one inclusion group ("fable_mythos") here; per-family numbers
for both read off that group.

Forward simulation gives each family's next-release distribution, plus the
company-level "any release" and "any frontier release" distributions, with
co-launch dependence built in rather than assumed away.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit

from .cadence import fit_posterior, _trend_z
from .data import d, releases_asof

GROUPS = ["opus", "sonnet", "haiku", "fable_mythos"]
GROUP_OF = {"opus": "opus", "sonnet": "sonnet", "haiku": "haiku", "fable": "fable_mythos", "mythos": "fable_mythos"}


def wave_frame(rel: pd.DataFrame) -> pd.DataFrame:
    r = rel.copy()
    r["family"] = "wave"
    return r.drop_duplicates("date")


def inclusion_data(rel: pd.DataFrame, asof):
    r = releases_asof(rel, asof)
    r = r[r.family != "legacy"].copy()
    r["group"] = r.family.map(GROUP_OF)
    days = sorted(r.date.unique())
    first = r.groupby("group").date.min()
    rows = []  # (wave_idx, group_idx, logds, y)
    for w, day in enumerate(days):
        day = pd.Timestamp(day)
        shipped = set(r.loc[r.date == day, "group"])
        for g_i, g in enumerate(GROUPS):
            if g not in first or first[g] >= day:
                continue  # group not yet in the lineup: its debut is not an inclusion choice
            prev = r[(r.group == g) & (r.date < day)].date.max()
            ds = max((day - prev).days, 1)
            rows.append((w, g_i, np.log(ds) - np.log(90), 1 if g in shipped else 0))
    return np.array(rows, dtype=float).reshape(-1, 4), first


def fit_inclusion(rows):
    """MAP of a_g (per group) and shared slope b, conditional on ≥1 inclusion."""
    G = len(GROUPS)
    if len(rows) == 0:
        return np.full(G, -1.0), 1.0   # no inclusion history yet: the prior means
    w_idx = rows[:, 0].astype(int)
    g_idx = rows[:, 1].astype(int)
    x, y = rows[:, 2], rows[:, 3]
    waves = np.unique(w_idx)

    def nlp(p):
        a, b = p[:G], p[G]
        eta = a[g_idx] + b * x
        lp1 = -np.logaddexp(0, -eta)
        lp0 = -np.logaddexp(0, eta)
        ll = np.sum(y * lp1 + (1 - y) * lp0)
        # condition on the wave being non-empty: subtract log(1 − Π(1−p))
        sum_lp0 = np.bincount(w_idx, weights=lp0, minlength=w_idx.max() + 1)[waves]
        ll -= np.sum(np.log1p(-np.exp(np.minimum(sum_lp0, -1e-9))))
        prior = -0.5 * np.sum(((a + 1.0) / 1.5) ** 2) - 0.5 * ((b - 1.0) / 1.0) ** 2
        return -(ll + prior)

    res = minimize(nlp, np.r_[np.full(G, -1.0), 1.0], method="L-BFGS-B")
    return res.x[:G], res.x[G]


class WaveForecast:
    def __init__(self, rel, asof, err="weibull", trend="changepoint", seed=0, n_sims=4000, horizon=400, half_life=None):
        self.asof = d(asof)
        self.H = horizon
        wf = wave_frame(rel)
        self.post = fit_posterior(wf, asof, err=err, trend=trend, families=["wave"], seed=seed, half_life=half_life)
        rows, first = inclusion_data(rel, asof)
        self.a, self.b = fit_inclusion(rows)
        self.first = first
        rng = np.random.default_rng(seed + 1)
        self._simulate(rel, rng, n_sims)

    def _gap_sampler(self, rng, n, cond_elapsed=None):
        post = self.post
        k = 0
        idx = rng.integers(0, len(post.sigma), n)
        m = post.mu[idx, k] + post.beta[idx] * _trend_z(self.asof, self.asof, post.cd.trend)
        s = post.sigma[idx]
        u = rng.random(n)
        if cond_elapsed is not None:
            # inverse-CDF draw of G | G > c for the Weibull/log-normal error family
            from .cadence import _sf
            lx = (np.log(np.maximum(cond_elapsed, 0.5)) - m) / s
            u = u * _sf(lx, post.err)          # survival target in (0, S(c))
        else:
            u = u * 1.0
        if post.err == "weibull":
            x = np.log(-np.log(np.clip(u, 1e-300, 1)))
        elif post.err == "normal":
            from scipy.stats import norm
            x = norm.isf(u)
        else:
            from scipy.stats import t
            x = t.isf(u, 4)
        return np.exp(m + s * x)

    def _simulate(self, rel, rng, n):
        last_wave = self.post.cd.last["wave"]
        c = (self.asof - last_wave).days
        r = releases_asof(rel, self.asof)
        r = r[r.family != "legacy"].copy()
        r["group"] = r.family.map(GROUP_OF)
        last_g = {g: r.loc[r.group == g, "date"].max() for g in GROUPS}
        ds0 = np.array([(self.asof - last_g[g]).days if pd.notna(last_g[g]) else np.nan for g in GROUPS])

        H = self.H
        first_any = np.full(n, H)
        first_frontier = np.full(n, H)
        first_g = np.full((n, len(GROUPS)), H)
        n_waves = np.zeros(n, dtype=int)
        # day offset (from origin) of the next wave
        t_next = self._gap_sampler(rng, n, cond_elapsed=np.full(n, c)) - c
        t_next = np.floor(np.maximum(t_next, 0)).astype(int)
        alive = np.ones(n, dtype=bool)
        since = np.tile(ds0, (n, 1))  # days since group last shipped, at origin
        for _ in range(40):
            active = alive & (t_next < H)
            if not active.any():
                break
            idx = np.where(active)[0]
            tw = t_next[idx]
            ds = since[idx] + tw[:, None]
            x = np.log(np.maximum(ds, 1)) - np.log(90)
            p = expit(self.a[None, :] + self.b * x)
            p[np.isnan(p)] = 0.0
            inc = rng.random(p.shape) < p
            empty = ~inc.any(axis=1)
            tries = 0
            while empty.any() and tries < 50:   # rejection: a wave ships something
                redraw = rng.random((empty.sum(), p.shape[1])) < p[empty]
                inc[empty] = redraw
                empty = ~inc.any(axis=1)
                tries += 1
            n_waves[idx] += 1
            first_any[idx] = np.minimum(first_any[idx], tw)
            front = inc[:, GROUPS.index("opus")] | inc[:, GROUPS.index("fable_mythos")]
            first_frontier[idx[front]] = np.minimum(first_frontier[idx[front]], tw[front])
            for g in range(len(GROUPS)):
                hit = inc[:, g]
                first_g[idx[hit], g] = np.minimum(first_g[idx[hit], g], tw[hit])
                since[idx[hit], g] = -tw[hit]  # reset: days since = (day − wave day)
            gaps = np.floor(self._gap_sampler(rng, len(idx))).astype(int)
            t_next[idx] = tw + np.maximum(gaps, 1)
        self.first_any, self.first_frontier, self.first_g = first_any, first_frontier, first_g

    @staticmethod
    def _to_pmf(first, H):
        counts = np.bincount(np.minimum(first, H), minlength=H + 1).astype(float)
        counts /= counts.sum()
        return counts[:H], float(counts[H])

    def pmf(self, family: str):
        if family == "any":
            return self._to_pmf(self.first_any, self.H)
        if family == "frontier":
            return self._to_pmf(self.first_frontier, self.H)
        g = GROUPS.index(GROUP_OF[family])
        return self._to_pmf(self.first_g[:, g], self.H)

    def params(self):
        return {"inclusion_a": dict(zip(GROUPS, map(float, self.a))), "inclusion_b": float(self.b),
                "wave_gap": self.post.params()["wave"], "shared": self.post.params()["_shared"]}
