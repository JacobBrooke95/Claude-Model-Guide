"""Family structure: each Claude family's offset from the Anthropic frontier.

offset_i = ECI_i - R(t_i), where R is the reference curve: the posterior-mean piecewise
(hinge) line through Anthropic's record-setting releases, fitted on data before the
origin. Record-setters scatter around R; lower tiers sit below it.

Two predictors of a family's next offset are kept and combined by stacking:
  'mean'  the family's recency-weighted mean offset, partially pooled across families
          (normal-normal empirical Bayes; shrinkage is set by the data);
  'last'  the offset of the family's most recent release (persistence).
A version-type effect (new generation / x.5 / minor), pooled across families and shrunk
toward zero, can be added to both.

Fable and Mythos are one underlying model per Anthropic. Public ECI scores Fable only, so
on the ECI scale Mythos inherits Fable's history and offset.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

from .trend import NU

HALF_LIFE = 1.5     # years; recency weighting of past offsets (assumption; families re-rank over time)
ETA_FLOOR = 1.0     # floor on within-family scatter, ECI points (assumption: ~ECI measurement sd)
TYPE_K0 = 4.0       # shrinkage pseudo-count for version-type effects (assumption)
TYPES = ["gen", "half", "minor"]


def twin_family(f):
    return "fable" if f == "mythos" else f


def offsets_table(claude: pd.DataFrame, ref, t0):
    """ref: callable t -> reference level."""
    h = claude[claude.t < t0].copy()
    h["offset"] = h.eci.to_numpy() - ref(h.t.to_numpy())
    h["w"] = 0.5 ** ((t0 - h.t) / HALF_LIFE)
    return h


def fit_families(h: pd.DataFrame):
    """Return dict with pooled/unpooled family offsets, last offsets, type effects, scatter."""
    fams = sorted(h.family.unique())
    rows = {}
    for f in fams:
        g = h[h.family == f]
        w = g.w.to_numpy()
        m = float(np.average(g.offset, weights=w))
        neff = float(w.sum() ** 2 / (w ** 2).sum())
        v = float(np.average((g.offset - m) ** 2, weights=w)) if len(g) > 1 else np.nan
        rows[f] = dict(n=len(g), n_eff=neff, mean=m, var=v, last=float(g.sort_values("t").offset.iloc[-1]),
                       last_t=float(g.t.max()), last_eci=float(g.sort_values("t").eci.iloc[-1]))
    vs = np.array([r["var"] * r["n"] for r in rows.values() if np.isfinite(r["var"])])
    ns = np.array([r["n"] for r in rows.values() if np.isfinite(r["var"])])
    s2 = max(float(vs.sum() / max(ns.sum() - len(ns), 1)), ETA_FLOOR ** 2) if len(vs) else 4.0
    means = np.array([r["mean"] for r in rows.values()])
    neffs = np.array([r["n_eff"] for r in rows.values()])
    mu = float(np.average(means, weights=neffs))
    tau2 = max(float(np.average((means - mu) ** 2, weights=neffs)) - float(np.mean(s2 / neffs)), 0.25) \
        if len(means) > 1 else 25.0
    for f, r in rows.items():
        prec = r["n_eff"] / s2 + 1 / tau2
        r["pooled"] = float((r["mean"] * r["n_eff"] / s2 + mu / tau2) / prec)
        r["pooled_se"] = float(prec ** -0.5)
        r["shrink"] = float((1 / tau2) / prec)
    # version-type effects on residuals from the pooled family mean
    res = h.offset.to_numpy() - np.array([rows[f]["pooled"] for f in h.family])
    gam = {}
    for ty in TYPES:
        m = (h.version_type == ty).to_numpy()
        w = h.w.to_numpy()[m]
        gam[ty] = float(np.average(res[m], weights=w) * w.sum() / (w.sum() + TYPE_K0)) if m.sum() else 0.0
    return dict(fam=rows, s2=s2, mu=mu, tau2=tau2, type=gam)


def predict_offset(ff, fam, vtype_probs, n, rng, use_type=True, T=None):
    """Samples of the next release's offset under the two predictors -> dict of arrays."""
    f = twin_family(fam)
    r = ff["fam"].get(f)
    eta = np.sqrt(ff["s2"]) * rng.standard_t(NU, n) * np.sqrt((NU - 2) / NU)
    g = np.zeros(n)
    if use_type and vtype_probs:
        tys = list(vtype_probs)
        pick = rng.choice(len(tys), size=n, p=np.array([vtype_probs[k] for k in tys]) / sum(vtype_probs.values()))
        g = np.array([ff["type"].get(t, 0.0) for t in tys])[pick]
    if r is None:   # family with no history: grand mean, wide
        base = ff["mu"] + np.sqrt(ff["tau2"]) * rng.standard_normal(n)
        return {"mean": base + g + eta, "last": base + g + eta}
    mean = r["pooled"] + r["pooled_se"] * rng.standard_normal(n)
    # persistence: the last offset is itself one noisy observation of the family's position
    last = r["last"] + np.zeros(n)
    return {"mean": mean + g + eta, "last": last + g + eta}


def version_type_of_name(name: str, last_gen: int) -> str:
    """Version type implied by a predicted product name, e.g. 'Claude Opus 5.6' -> minor,
    'Claude Opus 6' -> gen, 'Claude Mythos 5.5' -> half."""
    import re
    m = re.search(r"(\d+(?:\.\d+)?)\s*$", name)
    v = float(m.group(1))
    if int(v) > last_gen:
        return "gen"
    return "half" if abs(v * 10 % 10 - 5) < 1e-6 else "minor"


# ----------------------------------------------------------------------------- v2 gain model
GAIN_FLOOR = 0.3        # ECI points: smallest line gain the multiplicative model is applied to
RATIO_SD_FLOOR = 0.25   # floor on the log-sd of (actual step / line gain)


def gain_stats(hist: pd.DataFrame, ref):
    """Historical within-family steps before the origin, as a ratio to the reference line's
    gain over the same interval. Returns (median log ratio, robust log sd, n steps, min step)."""
    lr, steps = [], []
    for _, g in hist.sort_values("t").groupby("family"):
        if len(g) < 2:
            continue
        dy = np.diff(g.eci.to_numpy())
        dl = np.diff(ref(g.t.to_numpy()))
        ok = dy > 0
        lr += list(np.log(dy[ok] / np.maximum(dl[ok], GAIN_FLOOR)))
        steps += list(dy)
    if len(lr) < 5:
        return 0.0, 0.5, len(lr), (min(steps) if steps else None)
    lr = np.asarray(lr)
    c = float(np.median(lr))
    s = max(float(1.4826 * np.median(np.abs(lr - c))), RATIO_SD_FLOOR)
    return c, s, len(lr), float(min(steps))


def predict_step(y_prev, line_gain, c, s, meas_sd, rng, use_ratio=True):
    """Next release = predecessor + a positive gain + measurement noise of the new score.
    gain = max(line gain, floor) * exp(c + s*z): a shifted-lognormal step, so the latent step
    is never negative; the published score can still land below the predecessor through
    measurement noise alone."""
    n = len(line_gain)
    g = np.maximum(line_gain, GAIN_FLOOR)
    if use_ratio:
        g = g * np.exp(c + s * rng.standard_normal(n))
    return y_prev + g + meas_sd * rng.standard_normal(n)
