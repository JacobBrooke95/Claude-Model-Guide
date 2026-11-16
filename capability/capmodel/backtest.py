"""Rolling-origin backtests. Every fold refits everything on models released strictly
before the origin; `assert_no_leak` is called on each fold and the fold's data cut-off is
recorded so the tests can check it again.

Three backtests:
  A. frontier folds   - fixed-horizon forecasts of the running-max frontier (all labs and
                        Anthropic), monthly origins. Used to stack the trend candidates.
  B. release folds    - each Claude release predicted at its actual date: ability, then
                        benchmark scores through links fitted on earlier models.
  C. reference class  - how past apparent slope changes evolved over the next 12 months.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

from .common import rng as mkrng, yr, AS_OF
from .core import OriginModel, TREND, CANDS
from .trend import stack_crps, crps_sample, mixture_sample, records
from . import links as lk
from . import families as fam

HORIZONS = (0.25, 0.5, 1.0, 1.5, 2.0)
N_S = 400
MIN_STACK_FOLDS = 10
T_NOW = yr(AS_OF)


def assert_no_leak(om: OriginModel, t0):
    assert om.anth.series.t.size == 0 or om.anth.series.t.max() < t0, "future Anthropic model in fold"
    if om.all is not None:
        assert om.all.series.t.max() < t0, "future model in fold"
    assert om.hist.t.size == 0 or om.hist.t.max() < t0, "future Claude release in family history"


def interval_stats(samples, y):
    s = np.asarray(samples, float)
    qs = np.quantile(s, [0.5, 0.25, 0.75, 0.10, 0.90, 0.025, 0.975])
    return dict(median=float(qs[0]), err=float(y - qs[0]), in50=int(qs[1] <= y <= qs[2]), in80=int(qs[3] <= y <= qs[4]),
                in95=int(qs[5] <= y <= qs[6]), crps=crps_sample(s, y), lo80=float(qs[3]), hi80=float(qs[4]),
                lo95=float(qs[5]), hi95=float(qs[6]), lo50=float(qs[1]), hi50=float(qs[2]))


def conformal_ratio(st):
    """Per level, the stretch factor about the median needed for the interval to just cover y."""
    out = {}
    y, m = st["median"] + st["err"], st["median"]
    for lv, tag in ((0.5, "50"), (0.8, "80"), (0.95, "95")):
        half = (st["hi" + tag] - m) if y >= m else (m - st["lo" + tag])
        out[lv] = abs(y - m) / max(half, 1e-9)
    return out


def conformal_factor(ratios, lv, floor=1.0):
    r = np.sort(np.asarray(ratios, float))
    n = len(r)
    if n < 8:
        return 1.0
    k = min(int(np.ceil((n + 1) * lv)), n) - 1
    return float(max(r[k], floor))


def summarize_method(rows: pd.DataFrame):
    return dict(n=int(len(rows)), bias=round(float(rows.err.mean()), 2), mae=round(float(rows.err.abs().mean()), 2),
                rmse=round(float(np.sqrt((rows.err ** 2).mean())), 2), crps=round(float(rows.crps.mean()), 2),
                cov50=round(float(rows.in50.mean()), 2), cov80=round(float(rows.in80.mean()), 2),
                cov95=round(float(rows.in95.mean()), 2))


# ---------------------------------------------------------------------- A. frontier folds
def frontier_folds(d, B, abilities=None, start_all=2024.5, start_anth=2025.0):
    """Monthly origins. Returns list of fold dicts with per-candidate sample arrays."""
    e, _ = d.ability_table(abilities)
    folds = []
    origins = np.arange(start_all, T_NOW - 0.24, 1 / 12)
    for t0 in origins:
        r = mkrng(f"ff-{t0:.3f}")          # one stream per origin (common random numbers across variants)
        om = OriginModel(d, t0, B, r, abilities)
        if not om.all.ok:
            continue
        assert_no_leak(om, t0)
        for which, ens, names in (("all", om.all, CANDS), ("anth", om.anth, TREND)):
            if which == "anth" and (t0 < start_anth or not om.anth.ok):
                continue
            pool = e if which == "all" else e[e.lab == "Anthropic"]
            for h in HORIZONS:
                T = t0 + h
                if T > T_NOW:
                    continue
                y = float(pool[pool.t <= T].eci.max())
                samples = {c: om.frontier(c, T, N_S, which) for c in names}
                samples["persistence"] = np.full(N_S, ens.F0) + 1e-6 * r.standard_normal(N_S)
                folds.append(dict(which=which, t0=float(t0), h=h, T=float(T), y=y, F0=ens.F0, samples=samples,
                                  cutoff=float(ens.series.t.max())))
    return folds


def stack_weights(folds, which, before=None, hmax=1.0):
    names = CANDS if which == "all" else TREND
    use = [f for f in folds if f["which"] == which and f["h"] <= hmax and (before is None or f["T"] < before)]
    if len(use) < MIN_STACK_FOLDS:
        return {c: 1.0 / len(names) for c in names}, len(use)
    w, _, _ = stack_crps([[f["samples"][c] for c in names] for f in use], [f["y"] for f in use])
    return {c: float(v) for c, v in zip(names, w)}, len(use)


def score_frontier(folds):
    """Per-method scores by series and horizon, with rolling (out-of-sample) stacking."""
    r = mkrng("score-frontier")
    rows = []
    for f in folds:
        names = CANDS if f["which"] == "all" else TREND
        w, nprior = stack_weights(folds, f["which"], before=f["t0"])
        stacked = mixture_sample([f["samples"][c] for c in names], np.array([w[c] for c in names]), 2000, r)
        f["stacked"] = stacked
        f["w_rolling"] = w
        for meth, s in list(f["samples"].items()) + [("stacked", stacked)]:
            st = interval_stats(s, f["y"])
            rows.append(dict(which=f["which"], t0=f["t0"], h=f["h"], T=f["T"], method=meth, y=f["y"], n_prior_folds=nprior, **st))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------- B. release folds
RULES = ("blend", "stack_frontier", "equal", "stack_release")


def blend_weights(*ws):
    """Average of several weight dicts over the trend candidates (the 'blend' rule)."""
    ws = [w for w in ws if w is not None]
    return {c: float(np.mean([w[c] for w in ws])) for c in TREND}
LEADS = (0.0, 0.25, 0.5)
INTERVAL_METHODS = ("model", "model_with_type", "offset_mean_only", "offset_last_only", "model_date_uncertain")


def release_folds(d, B, ffolds, abilities_by_date=None, use_type=False, with_bench=True, rule="blend",
                  variants=False, leads=LEADS):
    """Folds = (Claude release, lead). The origin is `lead` years before the release; the
    model sees only models released strictly before the origin and is told the release's
    actual date and version type. A fold exists only if the release is the *next* one in
    its family as seen from the origin (the family's previous release precedes the origin).
    lead 0 is a day-of nowcast; the live forecast has leads of roughly 1-8 months.

    abilities_by_date: None = today's published ECI; otherwise a dict mapping a date
    (rounded) to (vintage ability Series, info): history comes from the origin's vintage,
    the target's 'actual' from the release date's vintage.

    rule: how the trend candidates are combined for the method called 'model':
      blend           the average of the three weight vectors below (the rule the live forecast uses)
      stack_frontier  CRPS-stacking weights from frontier folds whose target precedes the origin
      equal           equal weights
      stack_release   CRPS-stacking weights from earlier release folds with lead > 0 (needs 8;
                      falls back to stack_frontier until then)
    variants=True also scores every rule, every single candidate, and the version-type effect."""
    claude_all = d.claude()
    bench = d.bench
    rows, brows = [], []
    comp_hist = []    # (target t, lead, {'mean','last'}, y) for the rolling weight on the 'last' offset
    cand_hist = []    # (target t, lead, [samples per trend candidate], y) for rolling release-fold stacking
    n = 2000
    targets = [t for t in claude_all.itertuples() if t.t >= 2024.45]
    jobs = sorted([(tgt.t - ld, ld, tgt) for tgt in targets for ld in leads], key=lambda x: (x[0], x[1]))
    for t0, lead, tgt in jobs:
        ab = y_ab = None
        if abilities_by_date is not None:
            ab = abilities_by_date[round(float(t0), 4)][0]
            y_ab = abilities_by_date[round(float(tgt.t), 4)][0]
            if tgt.model_id not in y_ab.index:
                continue
        hist_all = d.claude(ab)
        hf0 = hist_all[(hist_all.family == tgt.family) & (hist_all.t < tgt.t)]
        if lead > 0 and len(hf0) and hf0.t.max() >= t0:
            continue                      # another release of the family falls inside the lead window
        r = mkrng(f"rel-{tgt.model_id}-{lead}")     # one stream per fold: variants share random numbers
        rl = mkrng(f"lnk-{tgt.model_id}-{lead}")
        om = OriginModel(d, t0, B, r, ab)
        if not om.ok or om.ff is None or len(om.anth.rt) < 4:
            continue
        assert_no_leak(om, t0)
        y = float(tgt.eci) if ab is None else float(y_ab[tgt.model_id])
        hist = om.hist
        hf = hist[hist.family == tgt.family].sort_values("t")
        T = float(tgt.t)
        Lc = {c: om.level(c, [T], n)[0][:, 0] for c in TREND}
        off = fam.predict_offset(om.ff, tgt.family, {tgt.version_type: 1.0}, n, r, use_type)
        prior = [c for c in comp_hist if c[0] < t0]
        alpha = 0.5
        if len(prior) >= 6:
            a, _, _ = stack_crps([[c[2]["mean"], c[2]["last"]] for c in prior], [c[3] for c in prior])
            alpha = float(a[1])
        pick = r.random(n) < alpha
        offmix = np.where(pick, off["last"], off["mean"])
        w_f, nprior = stack_weights(ffolds, "anth", before=t0)
        priorc = [c for c in cand_hist if c[0] < t0 and c[1] > 0]
        w_r = w_f
        if len(priorc) >= 8:
            wr, _, _ = stack_crps([c[2] for c in priorc], [c[3] for c in priorc])
            w_r = {c: float(v) for c, v in zip(TREND, wr)}
        W = {"stack_frontier": w_f, "equal": {c: 1.0 / len(TREND) for c in TREND}, "stack_release": w_r}
        W["blend"] = blend_weights(W["stack_frontier"], W["equal"], W["stack_release"])

        def mixL(w):
            k = r.choice(len(TREND), size=n, p=np.array([w[c] for c in TREND]) / sum(w.values()))
            return np.choose(k, [Lc[c] for c in TREND])
        Lm = mixL(W[rule])
        model = Lm + offmix
        comp_hist.append((T, lead, {"mean": Lm + off["mean"], "last": Lm + off["last"]}, y))
        cand_hist.append((T, lead, [Lc[c] + offmix for c in TREND], y))
        preds = {"model": model, "offset_mean_only": Lm + off["mean"], "offset_last_only": Lm + off["last"]}
        if variants:
            for rn in RULES:
                preds["rule_" + rn] = mixL(W[rn]) + offmix
            for c in TREND:
                preds["cand_" + c] = Lc[c] + offmix
            rt_ = mkrng(f"typ-{tgt.model_id}-{lead}")
            offt = fam.predict_offset(om.ff, tgt.family, {tgt.version_type: 1.0}, n, rt_, True)
            offn = fam.predict_offset(om.ff, tgt.family, {tgt.version_type: 1.0}, n, mkrng(f"typ-{tgt.model_id}-{lead}"), False)
            preds["type_effect_on"] = Lm + np.where(pick, offt["last"], offt["mean"])
            preds["type_effect_off"] = Lm + np.where(pick, offn["last"], offn["mean"])
        # date-uncertain variant: the release date is not known, only the family's cadence so far
        # (previous release + median earlier gap x lognormal(0, 0.42), the release forecaster's shared sigma)
        allg = hist.sort_values("t").groupby("family").t.diff().dropna()
        if lead > 0 and len(hf) and len(allg):
            gf = hf.t.diff().dropna()
            med = float(gf.median()) if len(gf) else float(allg.median())
            Ts = hf.t.iloc[-1] + med * np.exp(0.42 * r.standard_normal(n))
            Ts = np.clip(np.where(Ts < t0, t0 + r.random(n) * med, Ts), t0, t0 + 2.5)   # not yet released at the origin
            cu, _ = om.family_components(tgt.family, Ts, {tgt.version_type: 1.0}, n, W[rule], use_type)
            preds["model_date_uncertain"] = np.where(pick, cu["last"], cu["mean"])
        L = Lm
        # ---- baselines (point forecasts; intervals are added below from their own earlier errors)
        base = {}
        if len(hf):
            base["prev_in_family"] = float(hf.eci.iloc[-1])
            steps = hist.sort_values("t").groupby("family").eci.diff().dropna()
            fsteps = hf.eci.diff().dropna()
            base["family_mean_step"] = float(hf.eci.iloc[-1] + (fsteps.mean() if len(fsteps) >= 1 else (steps.mean() if len(steps) else 0.0)))
        base["all_history_linear"] = float(om.all.fits["lin_all"][0].mean([T])[0])
        base["trailing_12m_linear"] = float(om.all.fits["lin_12"][0].mean([T])[0])
        row = dict(fold=f"{tgt.model_id}|{lead}", model_id=tgt.model_id, family=tgt.family, version_type=tgt.version_type,
                   lead=lead, t0=float(t0), t=T, y=y, cutoff=float(om.all.series.t.max()), alpha=alpha,
                   n_prior_trend_folds=nprior, trend_level=float(np.median(L)))
        for k, s_ in preds.items():
            rows.append(dict(row, method=k, **interval_stats(s_, y)))
        for k, v in base.items():
            rows.append(dict(row, method=k, median=v, err=y - v))
        if not with_bench:
            continue
        # ---- benchmark scores through links fitted on models released before the origin
        e_all, _ = d.ability_table(ab)
        abil_all = e_all[e_all.t < t0].set_index("model_id").eci
        L_, _ = lk.fit_links(bench, d.meta, abil_all, t0, 20, rl)
        mine = bench[bench.model_id == tgt.model_id]
        meta_i = d.meta.set_index("benchmark")
        for b in mine.itertuples():
            if b.benchmark not in L_:
                continue
            link = L_[b.benchmark]
            prevb = bench[(bench.benchmark == b.benchmark) & (bench.family == tgt.family) & (bench.t < t0)].sort_values("t")
            scale = float(meta_i.loc[b.benchmark, "hi"] - meta_i.loc[b.benchmark, "lo"]) if link.kind == "bounded" else np.nan
            br = dict(fold=f"{tgt.model_id}|{lead}", model_id=tgt.model_id, family=tgt.family, lead=lead, t0=float(t0), t=T,
                      benchmark=b.benchmark, kind=link.kind, y=float(b.value), n_fit=link.n, range=scale,
                      cutoff=float(om.all.series.t.max()))
            brows.append(dict(br, method="model", **interval_stats(link.sample(model, rl), b.value)))
            brows.append(dict(br, method="link_given_true_ability", **interval_stats(link.sample(np.full(n, y), rl), b.value)))
            if len(prevb):
                brows.append(dict(br, method="prev_in_family", median=float(prevb.value.iloc[-1]),
                                  err=float(b.value - prevb.value.iloc[-1])))
    R = pd.DataFrame(rows)
    # empirical intervals for the point baselines: normal centred on the baseline with the sd of that
    # baseline's earlier errors at the same lead (from its 5th fold)
    out = []
    for (meth, lead), g in R.groupby(["method", "lead"], sort=False):
        g = g.sort_values("t").copy()
        if meth in INTERVAL_METHODS or meth.startswith(("rule_", "cand_", "type_")):
            out.append(g)
            continue
        errs = []
        for i, row in g.iterrows():
            if len(errs) >= 4:
                sd = float(np.std(errs, ddof=1))
                s_ = row["median"] + sd * mkrng(f"{meth}{i}").standard_normal(1000)
                st = interval_stats(s_, row["y"])
                for k in ("in50", "in80", "in95", "crps", "lo80", "hi80", "lo95", "hi95", "lo50", "hi50"):
                    g.loc[i, k] = st[k]
            errs.append(row["err"])
        out.append(g)
    res = pd.concat(out, ignore_index=True)
    a_all = 0.5
    if len(comp_hist) >= 6:
        a, _, _ = stack_crps([[c[2]["mean"], c[2]["last"]] for c in comp_hist], [c[3] for c in comp_hist])
        a_all = float(a[1])
    res.attrs["alpha_all_folds"] = a_all
    w_rel = None
    lead_c = [c for c in cand_hist if c[1] > 0]
    if len(lead_c) >= 8:
        wr, _, _ = stack_crps([c[2] for c in lead_c], [c[3] for c in lead_c])
        w_rel = {c: float(v) for c, v in zip(TREND, wr)}
    res.attrs["w_release_all_folds"] = w_rel
    return res, pd.DataFrame(brows)


def release_summary(R: pd.DataFrame, lead=None, common_only=True):
    """Scores per method on the folds where every baseline has a prediction."""
    if lead is not None:
        R = R[R.lead == lead]
    core = R[R.method.isin(["model", "prev_in_family", "family_mean_step", "all_history_linear", "trailing_12m_linear"])]
    piv = core.pivot_table(index="fold", columns="method", values="err")
    keep = piv.dropna().index if common_only else piv.index
    out = {}
    for meth, g in R[R.fold.isin(keep)].groupby("method", sort=False):
        s = dict(n=int(len(g)), bias=round(float(g.err.mean()), 2), mae=round(float(g.err.abs().mean()), 2),
                 rmse=round(float(np.sqrt((g.err ** 2).mean())), 2))
        gi = g.dropna(subset=["crps"]) if "crps" in g else g.iloc[:0]
        if len(gi):
            s.update(n_interval=int(len(gi)), crps=round(float(gi.crps.mean()), 2), cov50=round(float(gi.in50.mean()), 2),
                     cov80=round(float(gi.in80.mean()), 2), cov95=round(float(gi.in95.mean()), 2))
        out[meth] = s
    return out


def rolling_calibration(R: pd.DataFrame, floor=1.0, min_prior=8):
    """Conformal-style widening. For each fold, the stretch factor is learned from folds
    whose target date precedes this fold's origin (strictly out of sample); the fold is then
    scored with its intervals stretched by that factor. Returns raw and calibrated coverage
    and the final factors (learned from all folds) that the live forecast applies.
    Factors are floored at 1: intervals are never narrowed on backtest evidence this thin."""
    g = R.sort_values("t").reset_index(drop=True)
    t0col = "t0" if "t0" in g else "t"
    rat = [conformal_ratio(row) for _, row in g.iterrows()]
    cal = {0.5: [], 0.8: [], 0.95: []}
    raw = {0.5: [], 0.8: [], 0.95: []}
    for i, row in g.iterrows():
        prior = [rat[j] for j in range(len(g)) if g.t.iloc[j] < row[t0col] and j != i]
        if len(prior) < min_prior:
            continue
        for lv in cal:
            f = conformal_factor([p[lv] for p in prior], lv, floor)
            cal[lv].append(int(rat[i][lv] <= f))
            raw[lv].append(int(rat[i][lv] <= 1.0))
    out = {"n_folds": int(len(g)), "n_scored_rolling": int(len(cal[0.5])), "floor": floor}
    for lv, tag in ((0.5, "50"), (0.8, "80"), (0.95, "95")):
        allr = [p[lv] for p in rat]
        out["raw_cov" + tag] = round(float(np.mean([v <= 1.0 for v in allr])), 2) if len(g) else None
        out["raw_cov%s_same_folds" % tag] = round(float(np.mean(raw[lv])), 2) if raw[lv] else None
        out["calibrated_cov" + tag] = round(float(np.mean(cal[lv])), 2) if cal[lv] else None
        out["factor" + tag] = round(conformal_factor(allr, lv, floor), 3)
        out["factor%s_unfloored" % tag] = round(conformal_factor(allr, lv, 0.0), 3)
    return out


def factors(cal: dict):
    return {0.5: cal["factor50"], 0.8: cal["factor80"], 0.95: cal["factor95"]}


# ---------------------------------------------------------------------- C. reference class
def _slope(t, y):
    if len(t) < 3 or t.max() - t.min() < 0.3:
        return np.nan
    return float(np.polyfit(t, y, 1)[0])


def break_reference_class(series_dict, step=0.25, thresh=1.3):
    """For each record series and each quarterly origin: s0 = slope over (t0-3, t0-1],
    s1 = slope over (t0-1, t0], s2 = slope over (t0, t0+1]. An 'apparent acceleration' is
    s1/s0 >= thresh. Its outcome: 'reverted' if s2/s0 < (1+thresh)/2, 'accelerated again'
    if s2/s1 >= thresh, otherwise 'held'."""
    rows = []
    for name, (t, y) in series_dict.items():
        t, y = np.asarray(t, float), np.asarray(y, float)
        for t0 in np.arange(t.min() + 2.0, T_NOW - 1.0 + 1e-9, step):
            s0 = _slope(t[(t > t0 - 3) & (t <= t0 - 1)], y[(t > t0 - 3) & (t <= t0 - 1)])
            s1 = _slope(t[(t > t0 - 1) & (t <= t0)], y[(t > t0 - 1) & (t <= t0)])
            s2 = _slope(t[(t > t0) & (t <= t0 + 1)], y[(t > t0) & (t <= t0 + 1)])
            if not np.all(np.isfinite([s0, s1, s2])) or s0 <= 0:
                continue
            acc = s1 / s0 >= thresh
            out = None
            if acc:
                out = "reverted" if s2 / s0 < (1 + thresh) / 2 else ("accelerated_again" if s2 / s1 >= thresh else "held")
            rows.append(dict(series=name, t0=round(float(t0), 2), s0=round(s0, 2), s1=round(s1, 2), s2=round(s2, 2),
                             ratio_recent=round(s1 / s0, 2), ratio_next=round(s2 / s1, 2), apparent_acceleration=int(acc),
                             outcome=out))
    return pd.DataFrame(rows)
