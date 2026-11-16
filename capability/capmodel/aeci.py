"""AECI layer: mapping from public ECI to AECI (Nov 6 2026 fit) and refit drift.

Mapping, fitted on Claude models that have both values (Mythos paired with its Fable twin):
  hinge  : AECI = a0 + ECI + c * max(ECI - k, 0) + e     (divergence keeps growing)
  offset : AECI = a0 + ECI + d * 1[ECI > k]      + e     (one-time level shift)
Both reproduce the overlap about equally well; they differ only in extrapolation, and the
projection ties the choice to the scenario (see project.py).

Drift: every system card refits the whole AECI scale. From the drift matrix we take, for
each pair of consecutive card fits, the change in the printed value of every model that
appears in both. The next model's 'own-card' value = its value on the Nov 6 scale + the
drift accumulated over the card refits between now and its card.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

FIT_ORDER = ["opus4.8", "fable5", "opus5", "fable5.1", "opus5.5", "sonnet5.5", "haiku5.5", "fable5.2"]
KGRID = np.arange(145.0, 163.01, 0.5)
OWN_SD = 0.7      # sd of a model's own-card value around the later-refit-consistent value (from 4 cases; see drift table)


def overlap_table(d):
    a = d.aeci("fable5.2")
    a = a[a.value_type.isin(["printed", "figure_read", "anchor_by_definition"])].copy()
    m = d.models.set_index("model_id")
    rows = []
    for r in a.itertuples():
        src = r.model_id
        if not (isinstance(r.eci, float) and np.isfinite(r.eci)):
            src = r.twin if isinstance(r.twin, str) else None
        if src is None or src not in d.draws.index:
            continue
        sd = (r.local_hi - r.local_lo) / 3.92 if np.isfinite(r.local_lo) else (0.0 if r.value_type.startswith("anchor") else 0.15)
        rows.append(dict(model_id=r.model_id, eci_source=src, eci=float(m.loc[src, "eci"]), aeci=float(r.value),
                         aeci_sd=sd, value_type=r.value_type, t=float(m.loc[r.model_id, "t"])))
    return pd.DataFrame(rows).sort_values("eci").reset_index(drop=True)


def _fit(E, A, form):
    best = None
    y = A - E
    for k in KGRID:
        x = np.maximum(E - k, 0.0) if form == "hinge" else (E > k).astype(float)
        if x.sum() == 0 or (x > 0).sum() < 3 or (x == 0).sum() < 3:
            continue
        X = np.column_stack([np.ones_like(E), x])
        b, *_ = np.linalg.lstsq(X, y, rcond=None)
        r = y - X @ b
        sse = float(r @ r)
        if best is None or sse < best[0]:
            best = (sse, k, b)
    sse, k, b = best
    return dict(k=float(k), a0=float(b[0]), c=float(b[1]), sd=float(np.sqrt(sse / max(len(E) - 3, 1))), sse=sse)


class Mapping:
    def __init__(self, d, B, rng):
        self.tab = ov = overlap_table(d)
        E0, A0 = ov.eci.to_numpy(), ov.aeci.to_numpy()
        self.point = {f: _fit(E0, A0, f) for f in ("hinge", "offset")}
        Y = d.draws.loc[ov.eci_source].to_numpy()
        self.draws = {"hinge": [], "offset": []}
        n = len(ov)
        for _ in range(B):
            j = rng.integers(0, Y.shape[1])
            idx = rng.integers(0, n, n)                      # resample overlap models
            E = Y[idx, j]
            A = A0[idx] + ov.aeci_sd.to_numpy()[idx] * rng.standard_normal(n)
            for f in ("hinge", "offset"):
                try:
                    self.draws[f].append(_fit(E, A, f))
                except TypeError:
                    pass
        for f in ("hinge", "offset"):
            p = self.point[f]
            ov["fit_" + f] = self.apply_point(E0, f)
        n_ = len(E0)
        self.bic = {f: n_ * np.log(self.point[f]["sse"] / n_) + 3 * np.log(n_) for f in self.point}

    def apply_point(self, E, form):
        p = self.point[form]
        x = np.maximum(E - p["k"], 0.0) if form == "hinge" else (np.asarray(E) > p["k"]).astype(float)
        return p["a0"] + E + p["c"] * x

    def sample(self, E, form, rng, noise=True, pidx=None):
        """Map ability samples E (array) to AECI with parameter draws and residual noise.
        form may be a string or an array of 0/1 (0 = hinge, 1 = offset) per sample."""
        E = np.asarray(E, float)
        out = np.empty_like(E)
        forms = np.where(np.asarray(form) == "offset", 1, 0) if isinstance(form, str) or np.asarray(form).dtype.kind in "US" \
            else np.asarray(form)
        forms = np.broadcast_to(forms, E.shape[:1]) if E.ndim > 0 else forms
        for code, name in ((0, "hinge"), (1, "offset")):
            m = forms == code
            if not m.any():
                continue
            dr = self.draws[name]
            pi = rng.integers(0, len(dr), int(m.sum())) if pidx is None else pidx[m] % len(dr)
            k = np.array([dr[i]["k"] for i in pi])
            a0 = np.array([dr[i]["a0"] for i in pi])
            c = np.array([dr[i]["c"] for i in pi])
            Em = E[m]
            if Em.ndim == 2:
                k, a0, c = k[:, None], a0[:, None], c[:, None]
            x = np.maximum(Em - k, 0.0) if name == "hinge" else (Em > k).astype(float)
            out[m] = a0 + Em + c * x
        if noise:
            sd = max(self.point["hinge"]["sd"], 0.5)
            out = out + sd * rng.standard_normal(E.shape)
        return out

    def slope_above(self):
        c = np.array([p["c"] for p in self.draws["hinge"]])
        return 1 + c


def drift_table(d):
    a = d.index[(d.index.scale == "aeci") & d.index.fit.isin(FIT_ORDER)].copy()
    piv = a.pivot_table(index="model_id", columns="fit", values="value")[FIT_ORDER]
    own = a[a.own_card == 1].set_index("model_id").fit.to_dict()
    rows = []
    for mid, r in piv.iterrows():
        prev = None
        for f in FIT_ORDER:
            if not np.isfinite(r[f]):
                continue
            if prev is not None:
                rows.append(dict(model_id=mid, fit_from=prev, fit_to=f, n_refits=FIT_ORDER.index(f) - FIT_ORDER.index(prev),
                                 delta=float(r[f] - r[prev]), from_own_card=int(own.get(mid) == prev)))
            prev = f
    return pd.DataFrame(rows), piv


class OwnCard:
    """'AECI as printed in the model's own system card', modelled directly (v2).

    gap_i = own-card AECI_i - public ECI_i (today's Epoch fit; vintage ECI is not available),
    one per card that printed an own value, in card order. The gap is a property of the
    card's fit (it rose from about -4 to about +4 between May and November 2026, with two
    large steps that coincided with basket changes), not of the model's level, so it is
    forecast as a level: the mean of the last three cards' gaps. The predictive sd is the
    larger of the rolling out-of-sample RMSE of that rule and the sd of the last four gaps,
    widened by sqrt(1 + 0.25 (K-1)) for K card refits before the model's own card. Steps are
    not treated as iid and no upward drift is extrapolated. Eight cards: a judgement-heavy
    estimate, not a tested forecast."""

    def __init__(self, d):
        a = d.index[(d.index.scale == "aeci") & (d.index.own_card == 1) & (d.index.value_type == "printed")]
        m = d.models.set_index("model_id")
        rows = []
        for r in a.sort_values("fit_order").itertuples():
            src = r.model_id if np.isfinite(m.loc[r.model_id, "eci"]) else m.loc[r.model_id, "twin"]
            if not isinstance(src, str):
                continue
            rows.append(dict(card=r.fit, model_id=r.model_id, eci_source=src, card_date=m.loc[r.model_id, "release_date"],
                             aeci_own=float(r.value), eci=float(m.loc[src, "eci"]), gap=float(r.value - m.loc[src, "eci"]),
                             n_benchmarks=r.n_benchmarks))
        self.tab = pd.DataFrame(rows)
        g = self.tab.gap.to_numpy()
        self.pred = float(g[-3:].mean())
        bt = []
        for i in range(3, len(g)):
            bt.append(dict(card=self.tab.card.iloc[i], model_id=self.tab.model_id.iloc[i], predicted_gap=round(float(g[i - 3:i].mean()), 2),
                           actual_gap=round(float(g[i]), 2), error=round(float(g[i] - g[i - 3:i].mean()), 2),
                           last_gap_rule_error=round(float(g[i] - g[i - 1]), 2)))
        self.backtest = bt
        e = np.array([b["error"] for b in bt])
        self.rmse = float(np.sqrt(np.mean(e ** 2)))
        self.sd = max(self.rmse, float(g[-4:].std(ddof=1)))
        for b in bt:
            b["inside_80"] = int(abs(b["error"]) <= 1.2816 * self.sd)

    def sample(self, K, rng):
        K = np.minimum(np.asarray(K, float), 8.0)
        return self.pred + self.sd * np.sqrt(1 + 0.25 * (K - 1)) * rng.standard_t(4, K.shape) / np.sqrt(2.0)

    def summary(self):
        e = [b["last_gap_rule_error"] for b in self.backtest]
        return dict(predicted_gap=round(self.pred, 2), sd=round(self.sd, 2), rolling_rmse_mean_of_last_3=round(self.rmse, 2),
                    rolling_rmse_last_gap_rule=round(float(np.sqrt(np.mean(np.square(e)))), 2), n_cards=int(len(self.tab)),
                    n_backtest=len(self.backtest), cov80_in_sample_sd=round(float(np.mean([b["inside_80"] for b in self.backtest])), 2))


class Drift:
    """Empirical model of the per-refit change in printed AECI of frontier models."""

    def __init__(self, d):
        self.rows, self.piv = drift_table(d)
        one = self.rows[self.rows.n_refits == 1]
        # per-transition mean over models (the scale's movement at the top)
        self.trans = one.groupby("fit_to", sort=False).delta.agg(["mean", "count"]).reindex(FIT_ORDER[1:])
        # the two-refit rows (Mythos Preview fable5->opus5.5; Mythos 5.1 has none) are split evenly only
        # if a transition has no single-refit observation
        self.steps = self.trans["mean"].dropna().to_numpy()
        dev = one.delta - one.fit_to.map(self.trans["mean"])
        self.within_sd = float(np.sqrt(np.mean(dev ** 2))) if len(dev) > 1 else 0.7

    def sample(self, K, rng, steps=None):
        """Total drift over K refits (array of ints) by resampling observed per-refit steps."""
        steps = self.steps if steps is None else steps
        K = np.asarray(K, int)
        out = np.zeros(K.shape)
        for j in range(int(K.max()) if K.size else 0):
            m = K > j
            out[m] += rng.choice(steps, size=int(m.sum()))
        return out + self.within_sd * rng.standard_normal(K.shape) * (K > 0)

    def summary(self):
        s = self.steps
        return dict(n_transitions=int(len(s)), steps=[round(float(x), 2) for x in s], mean=round(float(s.mean()), 2),
                    sd=round(float(s.std(ddof=1)), 2), share_above_3=round(float((s > 3).mean()), 2),
                    within_sd=round(self.within_sd, 2))
