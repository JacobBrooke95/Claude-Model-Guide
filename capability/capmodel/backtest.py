"""Rolling-origin backtests (v2). Every fold refits everything on models released strictly
before its origin.

  A. machine folds  - the shared level process itself (level.LevelProcess.paths, the same
                      code the 2026-2030 projection runs) forecasting the running-max
                      frontier 0.5, 1.0 and 1.5 years ahead, for all labs and for Anthropic.
                      Yields the out-of-sample bias term and the calibration factors.
  B. release folds  - every Claude release at leads of 0, 3 and 6 months, date given and
                      date not given, against named baselines, on ALL folds.
  C. reference class of earlier slope changes.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

from .common import rng as mkrng, yr, AS_OF
from .level import LevelProcess, WEIGHTS, bias_beta, BIAS_H_CAP
from .trend import stack_crps, crps_sample, NU
from . import links as lk
from . import families as fam

MACHINE_H = (0.5, 1.0, 1.5)
LEADS = (0.0, 0.25, 0.5)
T_NOW = yr(AS_OF)
N_S = 2000
CADENCE_SIGMA = 0.42          # the release forecaster's shared log-gap sigma (forecast.json)
BASELINES = ["prev_plus_slope", "prev_in_family", "family_mean_step", "trailing_12m_linear", "all_history_linear"]


def interval_stats(samples, y):
    s = np.asarray(samples, float)
    qs = np.quantile(s, [0.5, 0.25, 0.75, 0.10, 0.90, 0.025, 0.975])
    return dict(median=float(qs[0]), err=float(y - qs[0]), in50=int(qs[1] <= y <= qs[2]), in80=int(qs[3] <= y <= qs[4]),
                in95=int(qs[5] <= y <= qs[6]), crps=crps_sample(s[:1500], y), lo50=float(qs[1]), hi50=float(qs[2]),
                lo80=float(qs[3]), hi80=float(qs[4]), lo95=float(qs[5]), hi95=float(qs[6]))


def conformal_ratio(st):
    out = {}
    y, m = st["median"] + st["err"], st["median"]
    for lv, tag in ((0.5, "50"), (0.8, "80"), (0.95, "95")):
        half = (st["hi" + tag] - m) if y >= m else (m - st["lo" + tag])
        out[lv] = abs(y - m) / max(half, 1e-9)
    return out


def conformal_factor(ratios, lv, floor=1.0):
    r = np.sort(np.asarray(ratios, float))
    n = len(r)
    if n < 6:
        return 1.0
    k = min(int(np.ceil((n + 1) * lv)), n) - 1
    return float(max(r[k], floor))


def rolling_calibration(R: pd.DataFrame, floor=1.0, min_prior=6):
    """Conformal-style widening. Each fold is scored with the stretch factor learned from
    folds whose target date precedes its origin; the final factors (all folds) are what
    the live forecast applies. Factors are floored at 1 (never narrow on thin evidence)."""
    g = R.sort_values("t").reset_index(drop=True)
    rat = [conformal_ratio(row) for _, row in g.iterrows()]
    cal = {0.5: [], 0.8: [], 0.95: []}
    raw = {0.5: [], 0.8: [], 0.95: []}
    for i, row in g.iterrows():
        prior = [rat[j] for j in range(len(g)) if g.t.iloc[j] < row["t0"] and j != i]
        if len(prior) < min_prior:
            continue
        for lv in cal:
            cal[lv].append(int(rat[i][lv] <= conformal_factor([p[lv] for p in prior], lv, floor)))
            raw[lv].append(int(rat[i][lv] <= 1.0))
    out = {"n_folds": int(len(g)), "n_scored_rolling": int(len(cal[0.5]))}
    for lv, tag in ((0.5, "50"), (0.8, "80"), (0.95, "95")):
        allr = [p[lv] for p in rat]
        out["raw_cov" + tag] = round(float(np.mean([v <= 1.0 for v in allr])), 2) if len(g) else None
        out["raw_cov%s_rolling_folds" % tag] = round(float(np.mean(raw[lv])), 2) if raw[lv] else None
        out["calibrated_cov" + tag] = round(float(np.mean(cal[lv])), 2) if cal[lv] else None
        out["factor" + tag] = round(conformal_factor(allr, lv, floor), 3)
        out["factor%s_unfloored" % tag] = round(conformal_factor(allr, lv, 0.0), 3)
    return out


def factors(cal: dict):
    return {0.5: cal["factor50"], 0.8: cal["factor80"], 0.95: cal["factor95"]}


def scores(g: pd.DataFrame):
    s = dict(n=int(len(g)), bias=round(float(g.err.mean()), 2), mae=round(float(g.err.abs().mean()), 2),
             rmse=round(float(np.sqrt((g.err ** 2).mean())), 2))
    if "crps" in g and g.crps.notna().any():
        gi = g.dropna(subset=["crps"])
        s.update(crps=round(float(gi.crps.mean()), 2), cov50=round(float(gi.in50.mean()), 2),
                 cov80=round(float(gi.in80.mean()), 2), cov95=round(float(gi.in95.mean()), 2))
    return s


# ------------------------------------------------------------------- A. the level process itself
def machine_folds(d, B, abilities=None, n=1500):
    """Monthly origins from mid-2024 (all labs) / 2025 (Anthropic). At each, the level
    process is fitted and simulated exactly as in the live projection (central scenario
    weights - a prior, fixed in advance, not tuned to these folds)."""
    e, _ = d.ability_table(abilities)
    out = {"all": [], "anthropic": []}
    for t0 in np.arange(2024.5, T_NOW - 0.49, 1 / 12):
        for which, start in (("all", 2024.5), ("anthropic", 2025.0)):
            if t0 < start:
                continue
            r = mkrng(f"mf-{which}-{t0:.3f}")
            lp = LevelProcess(d.series(which, abilities), t0, B, r)
            if not lp.ok:
                continue
            assert lp.ens.series.t.max() < t0, "future model in machine fold"
            P = lp.paths(n, WEIGHTS["central"], t0 + max(MACHINE_H) + 0.1)
            pool = e if which == "all" else e[e.lab == "Anthropic"]
            for h in MACHINE_H:
                T = t0 + h
                if T > T_NOW:
                    continue
                y = float(pool[pool.t <= T].eci.max())
                s = lp.frontier_at(P, T)
                out[which].append(dict(which=which, t0=float(t0), h=h, T=float(T), t=float(T), y=y, samples=s,
                                       err_raw=float(y - np.median(s)), cutoff=float(lp.ens.series.t.max()), F0=lp.F0))
    return out


def score_machine(folds):
    """Raw, bias-corrected (beta learned from folds whose target precedes the origin) and
    calibrated scores by horizon; plus the live beta and factors."""
    rows = []
    for f in folds:
        beta, nprior = bias_beta(folds, before=f["t0"])
        f["beta_rolling"] = beta
        raw = interval_stats(f["samples"], f["y"])
        cor = interval_stats(f["samples"] + beta * min(f["h"], BIAS_H_CAP), f["y"])
        rows.append(dict(t0=f["t0"], t=f["T"], h=f["h"], y=f["y"], variant="raw", n_prior=nprior, **raw))
        rows.append(dict(t0=f["t0"], t=f["T"], h=f["h"], y=f["y"], variant="bias_corrected", n_prior=nprior, **cor))
    R = pd.DataFrame(rows)
    tab, cal = [], {}
    for h in MACHINE_H:
        for v in ("raw", "bias_corrected"):
            g = R[(R.h == h) & (R.variant == v)]
            if len(g):
                tab.append(dict(horizon_years=h, variant=v, **scores(g)))
        g = R[(R.h == h) & (R.variant == "bias_corrected")]
        if len(g):
            cal[h] = rolling_calibration(g)
    return R, tab, cal


# ------------------------------------------------------------------- B. release folds
def _records(series, t0):
    s = series.cut(t0)
    t, y, _ = s.published_records()
    return t, y


def _ols(t, y):
    b = np.polyfit(t, y, 1)
    return lambda x: float(np.polyval(b, x)), float(b[0])


def prev_plus_slope(rt, ry, t0, T, prev):
    """The reviewer's two-line baseline: previous-in-family + trailing-12-month Anthropic
    record slope x elapsed time; a new family is placed on that line."""
    m = rt >= t0 - 1.0
    if m.sum() < 3:
        m = np.zeros(len(rt), bool)
        m[-4:] = True
    line, slope = _ols(rt[m], ry[m])
    return (line(T) if prev is None else prev[1] + slope * (T - prev[0])), slope


def release_folds(d, B, mfolds, abilities_by_date=None, with_bench=True, variants=True, leads=LEADS, seed_tag=""):
    """Folds = (Claude release, lead). Origin = release date - lead. A fold exists if the
    release is the next one in its family as seen from the origin (or the family's first).
    Methods scored on every fold:
      model            the release date is given
      model_date_unknown  only the family's cadence so far is known (lead > 0): previous
                       release + median earlier gap x lognormal(0, 0.42), conditioned on not
                       having shipped by the origin - how the live forecast is used
      baselines        see BASELINES
    abilities_by_date: None = published ECI; else {date: (Series, info)} vintage refits
    (history from the origin's vintage, the target's actual from the release date's)."""
    claude_all = d.claude()
    bench, meta_i = d.bench, d.meta.set_index("benchmark")
    rows, brows = [], []
    pool_hist = []
    targets = [t for t in claude_all.itertuples() if t.t >= 2024.45]
    jobs = sorted([(tgt.t - ld, ld, tgt) for tgt in targets for ld in leads], key=lambda x: (x[0], x[1]))
    for t0, lead, tgt in jobs:
        ab = y_ab = None
        if abilities_by_date is not None:
            ab = abilities_by_date[round(float(t0), 4)][0]
            y_ab = abilities_by_date[round(float(tgt.t), 4)][0]
            if tgt.model_id not in y_ab.index:
                continue
        hist = d.claude(ab)
        hist = hist[hist.t < t0]
        full_f = claude_all[(claude_all.family == tgt.family) & (claude_all.t < tgt.t)]
        if lead > 0 and len(full_f) and full_f.t.max() >= t0:
            continue                      # another release of the family falls inside the lead window
        r = mkrng(f"rel{seed_tag}-{tgt.model_id}-{lead}")
        lp = LevelProcess(d.series("anthropic", ab), t0, B, r)
        if not lp.ok:
            continue
        assert lp.ens.series.t.max() < t0 and (hist.t.max() < t0 if len(hist) else True), "future data in release fold"
        y = float(tgt.eci) if ab is None else float(y_ab[tgt.model_id])
        T = float(tgt.t)
        hf = hist[hist.family == tgt.family].sort_values("t")
        prev = None if not len(hf) else (float(hf.t.iloc[-1]), float(hf.eci.iloc[-1]))
        beta, _ = bias_beta(mfolds["anthropic"], before=t0)
        c, s, nst, _ = fam.gain_stats(hist, lp.ref)
        # cadence reconstruction of the release date
        allg = hist.sort_values("t").groupby("family").t.diff().dropna()
        Ts = None
        if lead > 0 and prev is not None and len(allg):
            gf = hf.t.diff().dropna()
            med = float(gf.median()) if len(gf) else float(allg.median())
            Ts = prev[0] + med * np.exp(CADENCE_SIGMA * r.standard_normal(N_S))
            Ts = np.clip(np.where(Ts < t0, t0 + r.random(N_S) * med, Ts), t0, t0 + 2.4)
        P = lp.paths(N_S, WEIGHTS["central"], t0 + 2.6)
        ref0 = float(lp.ref([t0])[0])

        def predict(Tx, b=beta, ratio=True):
            hx = np.maximum(np.asarray(Tx, float) - t0, 0.0)
            LT = lp.at(P, Tx) + b * np.minimum(hx, BIAS_H_CAP)
            if prev is None:      # first of a family: on the record line, with record scatter
                return LT + lp.S * r.standard_t(NU, N_S) / np.sqrt(NU / (NU - 2)) + lp.meas_sd * r.standard_normal(N_S), LT
            gain = LT - P["L0"] + P["b_post"] * (t0 - prev[0])     # recent slope x time already elapsed + path from here
            return fam.predict_step(prev[1], gain, c, s, lp.meas_sd, r, ratio), LT
        model, LT = predict(T)
        preds = {"model": model}
        if Ts is not None:
            preds["model_date_unknown"] = predict(Ts)[0]
        if variants:
            preds["variant_no_bias_term"] = predict(T, b=0.0)[0]
            preds["variant_no_step_ratio"] = predict(T, ratio=False)[0]
            # mean-reverting alternative: record line + pooled family offset; and a stacked mix with the core
            ht = fam.offsets_table(hist, lp.ref, t0)
            if len(ht) >= 3:
                ff = fam.fit_families(ht)
                off = fam.predict_offset(ff, tgt.family, None, N_S, r, False)["mean"]
                pooled = LT + off
                preds["variant_line_plus_pooled_offset"] = pooled
                prior = [x for x in pool_hist if x[0] < t0]
                a = 0.5
                if len(prior) >= 6:
                    w_, _, _ = stack_crps([[x[1], x[2]] for x in prior], [x[3] for x in prior], floor=0.0)
                    a = float(w_[0])
                preds["variant_mix_with_pooled_offset"] = np.where(r.random(N_S) < a, model, pooled)
                pool_hist.append((T, model, pooled, y))
        rt, ry = lp.rt, lp.ry                                   # Anthropic records before the origin (era window)
        rt_full, ry_full = _records(d.series("anthropic", ab), t0)
        at_, ay_ = _records(d.series("all", ab), t0)
        base, base_u = {}, {}
        Tm = float(np.median(Ts)) if Ts is not None else None
        base["prev_plus_slope"], slope12 = prev_plus_slope(rt_full, ry_full, t0, T, prev)
        if Tm is not None:
            base_u["prev_plus_slope"] = prev_plus_slope(rt_full, ry_full, t0, Tm, prev)[0]
        if prev is not None:
            base["prev_in_family"] = prev[1]
            steps = hist.sort_values("t").groupby("family").eci.diff().dropna()
            fs = hf.eci.diff().dropna()
            base["family_mean_step"] = prev[1] + float(fs.mean() if len(fs) else (steps.mean() if len(steps) else 0.0))
        m12 = at_ >= t0 - 1.0
        if m12.sum() >= 3:
            base["trailing_12m_linear"] = _ols(at_[m12], ay_[m12])[0](T)
        base["all_history_linear"] = _ols(at_, ay_)[0](T)
        row = dict(fold=f"{tgt.model_id}|{lead}", model_id=tgt.model_id, family=tgt.family, lead=lead, t0=float(t0), t=T, y=y,
                   cutoff=float(lp.ens.series.t.max()), first_of_family=int(prev is None), beta=beta, n_steps=nst,
                   prev_eci=None if prev is None else prev[1])
        for k, s_ in preds.items():
            rows.append(dict(row, method=k, **interval_stats(s_, y)))
        for k, v in base.items():
            rows.append(dict(row, method=k, median=float(v), err=float(y - v)))
        for k, v in base_u.items():
            rows.append(dict(row, method=k + "_date_unknown", median=float(v), err=float(y - v)))
        if not with_bench or prev is None:
            continue
        # ---- benchmark scores, anchored on the family's previous score (links fitted before the origin)
        rl = mkrng(f"lnk-{tgt.model_id}-{lead}")
        e_all, _ = d.ability_table(ab)
        abil = e_all[e_all.t < t0].set_index("model_id").eci
        L_, _ = lk.fit_links(bench, d.meta, abil, t0, 15, rl)
        mine = bench[bench.model_id == tgt.model_id]
        cl_ids = hist.set_index("model_id")
        for b in mine.itertuples():
            if b.benchmark not in L_:
                continue
            link = L_[b.benchmark]
            pb = bench[(bench.benchmark == b.benchmark) & (bench.family == tgt.family) & (bench.t < t0) &
                       bench.model_id.isin(cl_ids.index)].sort_values("t")
            if not len(pb):
                continue
            sp, tp = float(pb.value.iloc[-1]), float(cl_ids.loc[pb.model_id.iloc[-1], "eci"])
            sd = step_sd(link, bench, hist, b.benchmark, t0)
            br = dict(fold=f"{tgt.model_id}|{lead}", model_id=tgt.model_id, family=tgt.family, lead=lead, t0=float(t0), t=T,
                      benchmark=b.benchmark, kind=link.kind, y=float(b.value), prev=sp, n_fit=link.n,
                      cutoff=float(lp.ens.series.t.max()),
                      range=float(link.hi - link.lo) if link.kind == "bounded" else np.nan)
            brows.append(dict(br, method="anchored", **interval_stats(link.anchored(model, tp, sp, sd, rl), b.value)))
            brows.append(dict(br, method="curve_level", **interval_stats(link.sample(model, rl), b.value)))
            brows.append(dict(br, method="prev_in_family", median=sp, err=float(b.value - sp)))
    return pd.DataFrame(rows), pd.DataFrame(brows)


def step_sd(link, bench, hist, key, t_cut, default=None):
    """Robust sd of historical within-family anchored step residuals for one benchmark,
    using Claude releases before t_cut; pooled default when fewer than four steps exist."""
    b = bench[(bench.benchmark == key) & (bench.t < t_cut)].merge(hist[["model_id", "eci"]].rename(columns={"eci": "th"}), on="model_id")
    pairs = []
    for _, g in b.sort_values("t").groupby("family"):
        v, th = g.value.to_numpy(), g.th.to_numpy()
        pairs += [(th[i], v[i], th[i + 1], v[i + 1]) for i in range(len(g) - 1)]
    if default is None:
        default = 0.6 if link.kind in ("bounded", "loghorizon") else 2.0 * link.s
    if len(pairs) < 4:
        return float(default)
    res = link.step_residuals(pairs)
    sd = max(1.4826 * np.median(np.abs(res - np.median(res))), 0.7 * np.sqrt(np.mean(res ** 2)))
    return float(max(sd, 1e-3))


def summary_by_lead(R: pd.DataFrame, methods):
    out = {}
    for ld in LEADS:
        g = R[R.lead == ld]
        out[str(ld)] = {m: scores(g[g.method == m]) for m in methods if (g.method == m).any()}
    return out


def paired(R: pd.DataFrame, a: str, b: str, lead, rng, nboot=4000):
    """Mean difference in absolute error (a minus b; negative = a better) on the folds
    where both exist, with a bootstrap 90% interval over folds."""
    g = R[R.lead == lead]
    A = g[g.method == a].set_index("fold").err.abs()
    Bv = g[g.method == b].set_index("fold").err.abs()
    idx = A.index.intersection(Bv.index)
    if len(idx) < 2:
        return None
    dif = (A[idx] - Bv[idx]).to_numpy()
    bs = dif[rng.integers(0, len(dif), (nboot, len(dif)))].mean(axis=1)
    return dict(lead_years=lead, a=a, b=b, n=int(len(dif)), mae_a=round(float(A[idx].mean()), 2), mae_b=round(float(Bv[idx].mean()), 2),
                rmse_a=round(float(np.sqrt((A[idx] ** 2).mean())), 2), rmse_b=round(float(np.sqrt((Bv[idx] ** 2).mean())), 2),
                diff=round(float(dif.mean()), 2), lo90=round(float(np.quantile(bs, 0.05)), 2), hi90=round(float(np.quantile(bs, 0.95)), 2),
                a_better_in=int((dif < 0).sum()))


# ------------------------------------------------------------------- C. reference class
def _slope(t, y):
    if len(t) < 3 or t.max() - t.min() < 0.3:
        return np.nan
    return float(np.polyfit(t, y, 1)[0])


def break_reference_class(series_dict, step=0.25, thresh=1.3):
    """s0 = slope over (t0-3, t0-1], s1 over (t0-1, t0], s2 over (t0, t0+1]. An apparent
    acceleration is s1/s0 >= thresh; it 'reverted' if s2/s0 < (1+thresh)/2, 'accelerated
    again' if s2/s1 >= thresh, else 'held'."""
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
                             apparent_acceleration=int(acc), outcome=out))
    return pd.DataFrame(rows)
