"""Assemble one forecast at one origin from the layers.

    cadence (per-family renewal)  ┐
                                  ├─ linear pool (weights in Config) → base pmf per target
    wave (company renewal + mix)  ┘
    → day modifiers (weekday, holiday, competitor)   [hazard scale]
    → signal likelihoods                               [Bayes update, per family]
    → aggregates ("frontier", "any") recomputed so they stay consistent

Targets: opus, sonnet, haiku, fable, mythos, frontier (opus|fable|mythos), any.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict, replace

import numpy as np
import pandas as pd

from .cadence import fit_posterior
from .data import FAMILIES, d, family_history
from .modifiers import apply_hazard, day_multipliers, estimate_gamma
from .signals import SignalModel
from .wave import WaveForecast

TARGETS = FAMILIES + ["frontier", "any"]
_EWMA_CACHE: dict = {}
H = 400


@dataclass
class Config:
    err: str = "weibull"
    trend: str = "changepoint"
    w_wave: float = 0.5           # linear-pool weight on the wave model
    half_life: float | None = None  # recency weighting of past gaps, years (None = equal weight)
    fam_sigma: bool = False       # family-specific dispersion (partially pooled)
    w_ewma: float = 0.0           # linear-pool weight on the repo's EWMA model
    n_seeds: int = 1              # average the cadence posterior over this many MCMC chains
    sig_recent: bool = False      # v3d: clock from the most recent A/B sighting per class
    same_day: bool = False        # v3d live runs: count sightings first seen on the run date
    split_fp: bool = False        # v3d: Anthropic's own surfaces form their own signal class
    weekday: bool = True
    holiday: bool = True
    competitor: str | None = None  # None | "major21" | "sota30"
    signals: bool = False
    rho: float = 0.5
    cap: float = 5.0
    absence: bool = True
    seed: int = 0

    def key(self):
        return tuple(sorted(asdict(self).items()))


def _combine_any(pmfs: list[np.ndarray], tails: list[float]):
    """First-of independent clocks: S_any = Π S_f."""
    S = np.ones(H + 1)
    for p, t in zip(pmfs, tails):
        S *= np.concatenate([[1.0], 1.0 - np.cumsum(p)])
    return S[:-1] - S[1:], float(S[-1])


def _surv(p):
    return np.concatenate([[1.0], 1.0 - np.cumsum(p)])


class FitCache:
    """Expensive fits keyed by (origin, err, trend, seed)."""
    def __init__(self):
        self.cad, self.wave = {}, {}

    def cadence(self, rel, asof, cfg):
        k = (str(d(asof).date()), cfg.err, cfg.trend, cfg.seed, cfg.half_life, cfg.fam_sigma)
        if k not in self.cad:
            self.cad[k] = fit_posterior(rel, asof, err=cfg.err, trend=cfg.trend, seed=cfg.seed, half_life=cfg.half_life,
                                        fam_sigma=cfg.fam_sigma)
        return self.cad[k]

    def wavef(self, rel, asof, cfg):
        k = (str(d(asof).date()), cfg.err, cfg.trend, cfg.seed, cfg.half_life)
        if k not in self.wave:
            self.wave[k] = WaveForecast(rel, asof, err=cfg.err, trend=cfg.trend, seed=cfg.seed, horizon=H,
                                        half_life=cfg.half_life)
        return self.wave[k]


def forecast(rel, comp, sig, asof, cfg: Config, cache: FitCache | None = None, explain=False):
    cache = cache or FitCache()
    asof = d(asof)
    out, info = {}, {}
    cad = cache.cadence(rel, asof, cfg) if cfg.w_wave < 1 else None
    cads = [cad] + [cache.cadence(rel, asof, replace(cfg, seed=cfg.seed + k)) for k in range(1, cfg.n_seeds)] if cad is not None else []
    wav = cache.wavef(rel, asof, cfg) if cfg.w_wave > 0 else None

    # ---- base distributions -------------------------------------------------
    base = {}
    for f in FAMILIES:
        if not family_history(rel, f, asof):
            continue
        parts = []
        if cad is not None and f in cad.cd.families:
            ps = [c.pmf(f, H) for c in cads]
            parts.append((1 - cfg.w_wave, (sum(p for p, _ in ps) / len(ps), sum(t for _, t in ps) / len(ps))))
        if wav is not None:
            parts.append((cfg.w_wave, wav.pmf(f)))
        wsum = sum(w for w, _ in parts)
        pmf = sum(w * p for w, (p, _) in parts) / wsum
        tail = sum(w * t for w, (_, t) in parts) / wsum
        base[f] = (pmf, tail)

    # aggregates: wave model has them natively (co-launch aware); cadence via
    # independence, which overstates P(any) when families co-launch
    def agg(names, key):
        fams = [n for n in names if n in base]
        if not fams:
            return None
        ind = _combine_any([base[n][0] for n in fams], [base[n][1] for n in fams])
        if wav is None:
            return ind
        wp = wav.pmf(key)
        if cad is None:
            return wp
        return ((1 - cfg.w_wave) * ind[0] + cfg.w_wave * wp[0], (1 - cfg.w_wave) * ind[1] + cfg.w_wave * wp[1])

    # fable and mythos move together: treat their union as one clock in aggregates
    fm = None
    if "fable" in base or "mythos" in base:
        cands = [base[k] for k in ("fable", "mythos") if k in base]
        fm = (sum(c[0] for c in cands) / len(cands), sum(c[1] for c in cands) / len(cands))  # one shared clock
    base_fm = dict(base)
    base_fm.pop("fable", None); base_fm.pop("mythos", None)
    if fm is not None:
        base_fm["fable_mythos"] = fm

    def agg2(names, key):
        fams = [n for n in names if n in base_fm]
        ind = _combine_any([base_fm[n][0] for n in fams], [base_fm[n][1] for n in fams])
        if wav is None:
            return ind
        wp = wav.pmf(key)
        if cad is None:
            return wp
        return ((1 - cfg.w_wave) * ind[0] + cfg.w_wave * wp[0], (1 - cfg.w_wave) * ind[1] + cfg.w_wave * wp[1])

    base["frontier"] = agg2(["opus", "fable_mythos"], "frontier")
    base["any"] = agg2(["opus", "sonnet", "haiku", "fable_mythos"], "any")

    # ---- day modifiers ----------------------------------------------------------
    gamma = 0.0
    if cfg.competitor and comp is not None and len(comp) and cad is not None:
        gamma, gsd, ev, ex = estimate_gamma(cad, rel, comp, asof, rule=cfg.competitor)
        info["competitor"] = dict(rule=cfg.competitor, gamma=gamma, sd=gsd, exposed_events=ev, exposed_days=ex)
    mult = day_multipliers(rel, asof, H, comp=comp, gamma=gamma, rule=cfg.competitor or "major21",
                           weekday=cfg.weekday, holiday=cfg.holiday)
    mod = {k: apply_hazard(p, t, mult) for k, (p, t) in base.items() if p is not None}

    # ---- signals ----------------------------------------------------------------
    if cfg.signals and sig is not None and len(sig):
        sm = SignalModel(sig, rel, asof, rho=cfg.rho, cap=cfg.cap, recent=cfg.sig_recent, same_day=cfg.same_day,
                         split_first_party=cfg.split_fp)
        info["signal_params"] = sm.par
        upd = {}
        for f in FAMILIES:
            if f not in mod:
                continue
            last = family_history(rel, f, asof)[-1]
            L, Lt, det = sm.likelihood(f, last, H, use_absence=cfg.absence)
            upd[f] = SignalModel.update(mod[f][0], mod[f][1], L, Lt)
            info.setdefault("signals", {})[f] = det
        # carry the per-family survival changes into the aggregates
        for key, members in (("frontier", ["opus", "fable", "mythos"]), ("any", ["opus", "sonnet", "haiku", "fable", "mythos"])):
            S = _surv(mod[key][0])
            ratio = np.ones(H + 1)
            seen_fm = False
            for f in members:
                if f not in upd:
                    continue
                if f in ("fable", "mythos"):
                    if seen_fm:
                        continue  # one shared clock
                    seen_fm = True
                    # one shared clock: Fable's update stands for both
                    f = "fable" if "fable" in upd else "mythos"
                r = _surv(upd[f][0]) / np.maximum(_surv(mod[f][0]), 1e-12)
                ratio *= np.clip(r, 0, None)
            S2 = np.clip(S * ratio, 0, 1)
            S2 = np.minimum.accumulate(S2)
            upd[key] = (S2[:-1] - S2[1:], float(S2[-1]))
        mod.update(upd)

    # ---- ensemble with the repo's EWMA model (Opus / Sonnet / Haiku) -----------
    # Linear pool. The hierarchical model adapts slowly to a cadence shift; the
    # EWMA adapts fast but was badly miscalibrated in 2024–25. Pooled, they beat
    # both over the full backtest (see README, "v3").
    if cfg.w_ewma > 0:
        from .backtest import ewma_baseline
        from .ewma import ewma_pmf
        ew = _EWMA_CACHE.get(asof) or ewma_baseline(asof)
        _EWMA_CACHE[asof] = ew
        old = dict(mod)
        for f in ("opus", "sonnet", "haiku"):
            e = ewma_pmf(ew.get(f), asof, H)
            if e is None or f not in mod:
                continue
            mod[f] = ((1 - cfg.w_ewma) * mod[f][0] + cfg.w_ewma * e[0], (1 - cfg.w_ewma) * mod[f][1] + cfg.w_ewma * e[1])
        for key, members in (("frontier", ["opus"]), ("any", ["opus", "sonnet", "haiku"])):
            S = _surv(mod[key][0])
            for f in members:
                if f in old:
                    S = S * (_surv(mod[f][0]) / np.maximum(_surv(old[f][0]), 1e-12))
            S = np.minimum.accumulate(np.clip(S, 0, 1))
            mod[key] = (S[:-1] - S[1:], float(S[-1]))
        info["ewma"] = {f: ew.get(f) for f in ("opus", "sonnet", "haiku")}

    for k in TARGETS:
        if k in mod:
            out[k] = mod[k]
    if explain:
        info["cadence"] = cad.params() if cad is not None else None
        info["wave"] = wav.params() if wav is not None else None
        info["day_mult"] = mult
    return out, info


def summarize(pmf, tail, asof, horizons=(7, 14, 30, 60, 90)):
    cdf = np.cumsum(pmf)
    asof = d(asof)
    q = lambda p: (asof + pd.Timedelta(days=int(np.searchsorted(cdf, p)))) if cdf[-1] >= p else None
    s = {f"p{h}": float(cdf[h - 1]) for h in horizons}
    for name, p in (("q10", .1), ("q25", .25), ("median", .5), ("q75", .75), ("q90", .9)):
        v = q(p)
        s[name] = str(v.date()) if v is not None else f">{(asof + pd.Timedelta(days=H)).date()}"
    s["mode"] = str((asof + pd.Timedelta(days=int(np.argmax(pmf)))).date())
    s["tail_beyond_horizon"] = tail
    return s
