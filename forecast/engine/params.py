"""Release parameters: what the next release in each family is likely to look
like, beyond its date. Each estimate states whether it is fitted (with n) or
rule-based, because n is small and a reader should know which is which.

  generation   renewal on generation gaps (Claude 1→2→3→4→5) → P(next major
               number by date); fitted, n = 4 gaps
  version      step size of the next version number in the family (+0.1,
               +0.5, new major); empirical frequencies since Claude 4, Laplace-
               smoothed, with the generation clock deciding "new major"
  price        P(list price unchanged / cut / raised) at the next release,
               from launches since 2025 (regime after the Opus 4.5 reset)
  co-launch    share of the family's releases that shared a day with another
               family's release
  benchmark    SWE-bench Pro for the next model, Bayesian linear trend on
               logit(score) vs time with a slope pooled across families
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import expit, logit

from .data import d

# SWE-bench Pro (Anthropic-reported, from claude-models.html sweData)
SWE_PRO = {
    "opus": [("2025-11-24", 52.0), ("2026-02-05", 53.4), ("2026-04-16", 64.3), ("2026-05-28", 69.2),
             ("2026-07-24", 79.2), ("2026-09-22", 89.9)],
    "sonnet": [("2026-02-17", 58.1), ("2026-06-30", 63.2), ("2026-09-28", 81.3)],
    "haiku": [("2026-10-07", 64.8)],
    "fable": [("2026-06-09", 80.0), ("2026-09-01", 81.2)],
}

GEN_STARTS = ["2023-03-14", "2023-07-11", "2024-03-04", "2025-05-22", "2026-06-09"]


def generation_clock(asof, horizon_dates):
    """P(generation 6 publicly announced by each date). Log-normal on the four
    gaps between generation debuts, conditioned on none since 2026-06-09."""
    starts = [d(x) for x in GEN_STARTS]
    gaps = np.log([(b - a).days for a, b in zip(starts[:-1], starts[1:])])
    n = len(gaps)
    m, s = gaps.mean(), gaps.std(ddof=1)
    # posterior predictive (unknown mean/var, flat prior) → Student-t on log gap
    scale = s * np.sqrt(1 + 1 / n)
    elapsed = (d(asof) - starts[-1]).days
    S0 = stats.t.sf((np.log(elapsed) - m) / scale, n - 1)
    out = {}
    for dt in horizon_dates:
        g = (d(dt) - starts[-1]).days
        S = stats.t.sf((np.log(g) - m) / scale, n - 1)
        out[str(d(dt).date())] = float(1 - S / S0)
    return out, dict(gaps_days=[int(round(np.exp(x))) for x in gaps], median_gap_days=float(np.exp(m)),
                     elapsed_days=elapsed)


def version_steps(rel, family):
    r = rel[(rel.family == family) & (rel.generation >= 4)].sort_values("date")
    v = r.version.values
    steps = np.round(np.diff(v), 2)
    cats = {"+0.1": 0, "+0.5 or half-step": 0, "new major": 0}
    for a, b, st in zip(v[:-1], v[1:], steps):
        if int(b) > int(a):
            cats["new major"] += 1
        elif abs(st - 0.1) < 1e-6:
            cats["+0.1"] += 1
        else:
            cats["+0.5 or half-step"] += 1
    return cats, list(r.model)


def next_names(rel, family, p_new_major):
    """Combine the family's step frequencies (Laplace-smoothed) with the
    generation clock for the probability that the next model is a new major."""
    r = rel[rel.family == family].sort_values("date")
    if r.empty:
        return {}
    last = float(r.version.iloc[-1])
    cats, _ = version_steps(rel, family)
    minor = {k: v + 1 for k, v in cats.items() if k != "new major"}
    tot = sum(minor.values())
    fam_name = family.capitalize()
    major = int(np.floor(last)) + 1
    names = {f"Claude {fam_name} {major}": p_new_major}
    p_minor = 1 - p_new_major
    n01 = round(last + 0.1, 1)
    if abs(last - round(last)) < 1e-9 or abs((last * 10) % 10 - 5) < 1e-6:
        n05 = round(np.floor(last) + 0.5, 1) if last % 1 < 0.5 else None
    else:
        n05 = round(np.floor(last) + 0.5, 1) if last % 1 < 0.5 else None
    if n05 is None or n05 <= last:
        names[f"Claude {fam_name} {n01:g}"] = p_minor
    else:
        names[f"Claude {fam_name} {n01:g}"] = p_minor * minor["+0.1"] / tot
        names[f"Claude {fam_name} {n05:g}"] = p_minor * minor["+0.5 or half-step"] / tot
    return dict(sorted(names.items(), key=lambda kv: -kv[1]))


def price_change(rel, family, since="2025-01-01"):
    r = rel[(rel.family == family)].sort_values("date")
    r = r[r.price_out.notna()]
    same = cut = rise = 0
    for (_, a), (_, b) in zip(r.iloc[:-1].iterrows(), r.iloc[1:].iterrows()):
        if b.date < d(since):
            continue
        if b.price_out == a.price_out and b.price_in == a.price_in:
            same += 1
        elif b.price_out < a.price_out:
            cut += 1
        else:
            rise += 1
    n = same + cut + rise
    a = 1.0  # Laplace
    tot = n + 3 * a
    last = r.iloc[-1] if len(r) else None
    return dict(n=n, p_same=(same + a) / tot, p_cut=(cut + a) / tot, p_raise=(rise + a) / tot,
                current=(f"${last.price_in:g} / ${last.price_out:g}" if last is not None else None))


def colaunch_rate(rel, family):
    r = rel[rel.family == family]
    days = rel.groupby("date").family.nunique()
    shared = sum(days.get(x, 1) > 1 for x in r.date)
    return dict(n=len(r), shared=int(shared), rate=(shared + 0.5) / (len(r) + 1))


def swe_pro_projection(family, at_date, n_draws=20000, seed=0):
    """Next-model SWE-bench Pro. Each past step within a family gives a rate
    of progress r_i = Δlogit(score) / years between the two models. Rates are
    pooled across families (Student-t predictive for a new r), and the next
    model is projected from the family's latest score:
        logit(next) = logit(last) + r · (years from last model to at_date)
    so the projection can fall below the last score only if r < 0, which
    has not happened yet (n = 8 steps)."""
    rng = np.random.default_rng(seed)
    rates = []
    for f, pts in SWE_PRO.items():
        for (d0, s0), (d1, s1) in zip(pts[:-1], pts[1:]):
            yrs = (d(d1) - d(d0)).days / 365.25
            rates.append((logit(s1 / 100) - logit(s0 / 100)) / yrs)
    rates = np.array(rates)
    n = len(rates)
    m, sd = rates.mean(), rates.std(ddof=1)
    if family not in SWE_PRO:
        return None
    last_d, last = SWE_PRO[family][-1]
    yrs = max((d(at_date) - d(last_d)).days / 365.25, 1 / 52)
    r = m + sd * np.sqrt(1 + 1 / n) * rng.standard_t(n - 1, n_draws)
    sc = 100 * expit(logit(last / 100) + r * yrs)
    return dict(median=float(np.median(sc)), lo80=float(np.percentile(sc, 10)), hi80=float(np.percentile(sc, 90)),
                last=last, rate_logit_per_year_mean=float(m), rate_sd=float(sd), n_steps=int(n))


def apply_named_signals(names: dict, named_versions: list[str], weight=0.85):
    """If grade A/B artifacts name a specific next version (e.g. an Azure row
    `claude-fable-5-5` and a client commit naming 'Fable 5.5'), give that name
    `weight` and rescale the rest. Rule-based, not fitted."""
    if not named_versions:
        return names
    tgt = named_versions[0]
    rest = {k: v for k, v in names.items() if k != tgt}
    z = sum(rest.values()) or 1.0
    out = {tgt: weight}
    out.update({k: (1 - weight) * v / z for k, v in rest.items()})
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))
