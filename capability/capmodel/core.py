"""The model as fitted at one origin date: trend ensembles, family offsets, predictors.

Everything in here sees only models released strictly before the origin t0. The same
class is used for the backtest folds and for the live forecast.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

from .trend import Ensemble, CANDS, NU, mixture_sample
from . import families as fam

TREND = CANDS + ["pool_all"]
T_SD = np.sqrt(NU / (NU - 2))


class OriginModel:
    def __init__(self, d, t0, B, rng, abilities=None, need_all=True):
        self.d, self.t0, self.rng = d, float(t0), rng
        self.anth = Ensemble(d.series("anthropic", abilities), t0, B, rng)
        self.all = Ensemble(d.series("all", abilities), t0, B, rng) if need_all else None
        self.claude = d.claude(abilities)
        self.ref = self.anth.fits["hinge"][0].mean if self.anth.ok else (lambda t: np.full(len(np.atleast_1d(t)), np.nan))
        self.hist = fam.offsets_table(self.claude, self.ref, t0)
        self.ff = fam.fit_families(self.hist) if len(self.hist) >= 3 else None
        self.ok = self.anth.ok and (self.all is None or self.all.ok)
        if self.all is not None and self.all.ok and len(self.anth.rt) >= 3:
            # Pooled candidate: Anthropic's record line = all-lab line + a mean-reverting gap.
            #   gap(h) = mu + (g_now - mu) * phi^h,  h = years past the origin
            # g_now: mean residual of Anthropic's last three records against the all-lab trailing-24-month
            # line; mu: mean residual over all its records; phi: yearly persistence from the lag-1
            # autocorrelation of the residual series (default 0.5 with fewer than 6 records).
            g = self.anth.ry - self.all.fits["lin_24"][0].mean(self.anth.rt)
            self.gap_mu = float(g.mean())
            self.gap_now = float(g[-3:].mean())
            self.gap_sd = max(float(g.std(ddof=1)), 1.0)
            phi = 0.5
            if len(g) >= 6:
                r1 = float(np.corrcoef(g[:-1], g[1:])[0, 1])
                dt = float(np.mean(np.diff(self.anth.rt)))
                if np.isfinite(r1) and r1 > 0:
                    phi = float(np.clip(r1 ** (1.0 / max(dt, 0.05)), 0.05, 0.9))
                else:
                    phi = 0.05
            self.gap_phi = phi

    # ---- trend level -----------------------------------------------------------------
    def level(self, cand, T, n, which="anth"):
        """(n, len(T)) draws of the record-line level and (n,) residual scales."""
        T = np.atleast_1d(np.asarray(T, float))
        ens = self.anth if which == "anth" else self.all
        if cand == "pool_all":
            L, S = self.all.sample_level("lin_24", T, n, self.rng)
            ph = self.gap_phi ** np.maximum(T - self.t0, 0.0)[None, :]
            mu = self.gap_mu + self.gap_sd / np.sqrt(len(self.anth.rt)) * self.rng.standard_normal((n, 1))
            gap = mu + (self.gap_now - mu) * ph + self.gap_sd * np.sqrt(1 - ph ** 2) * self.rng.standard_normal((n, 1))
            return L + gap, np.full(n, self.gap_sd * 0.5)
        return ens.sample_level(cand, T, n, self.rng)

    def stacked_level(self, T, n, w, which="anth"):
        """Draws from the weighted mixture of candidates: level (n, len(T)), scale (n,), component id."""
        names = TREND if which == "anth" else CANDS
        w = np.asarray([w.get(c, 0.0) for c in names], float)
        w = w / w.sum()
        k = self.rng.choice(len(names), size=n, p=w)
        T = np.atleast_1d(np.asarray(T, float))
        L = np.empty((n, len(T)))
        S = np.empty(n)
        for j in np.unique(k):
            m = k == j
            L[m], S[m] = self.level(names[j], T, int(m.sum()), which)
        return L, S, k

    def frontier(self, cand, T, n, which="anth"):
        """Draws of the running-max frontier held at date T under one candidate."""
        ens = self.anth if which == "anth" else self.all
        L, S = self.level(cand, [T - 0.25, T], n, which)
        slope = (L[:, 1] - L[:, 0]) / 0.25
        age = np.minimum(ens.sample_age(n, self.rng), max(T - self.t0, 0.0))
        return np.maximum(L[:, 1] - slope * age + S * self.rng.standard_t(NU, n) / T_SD, ens.F0)

    # ---- family prediction -----------------------------------------------------------
    def family_components(self, family, T, vtype_probs, n, w, use_type=True):
        """Ability draws for the next release of `family` at date(s) T (scalar or (n,) array),
        under the two offset predictors. Returns dict name -> (n,) array."""
        T = np.asarray(T, float)
        if T.ndim == 0:
            L, S, _ = self.stacked_level([float(T)], n, w)
            L = L[:, 0]
        else:   # a different date per draw: evaluate on a grid and interpolate per draw
            grid = np.linspace(T.min(), T.max() + 1e-6, 25)
            Lg, S, _ = self.stacked_level(grid, n, w)
            pos = np.clip((T - grid[0]) / (grid[1] - grid[0]), 0, len(grid) - 1 - 1e-9)
            i0 = pos.astype(int)
            fr = pos - i0
            r = np.arange(n)
            L = Lg[r, i0] * (1 - fr) + Lg[r, i0 + 1] * fr
        off = fam.predict_offset(self.ff, family, vtype_probs, n, self.rng, use_type)
        return {k: L + v for k, v in off.items()}, L

    def family_predict(self, family, T, vtype_probs, n, w, alpha, use_type=True):
        comps, L = self.family_components(family, T, vtype_probs, n, w, use_type)
        pick = self.rng.random(n) < alpha
        return np.where(pick, comps["last"], comps["mean"]), comps, L
