"""End-to-end run: backtests -> weights and calibration -> live fit -> next-model
predictions -> 2026-2030 projection. Returns one results dict; report.py writes it out."""
from __future__ import annotations
import time
import numpy as np
import pandas as pd

from .common import (rng as mkrng, yr, from_yr, AS_OF, MODEL_VERSION, SEED, FAMILIES, RAW, summarize, widen,
                     wsummary, wquantile)
from .data import D
from .core import OriginModel, TREND, CANDS
from .trend import Ensemble, Series, break_analysis, stack_crps, NU
from . import backtest as bt
from . import irt, aeci, links as lk, predict as pr, project as pj, families as fam

T_NOW = yr(AS_OF)
N_MC = 20000
N_SCN = 6000
B_BT = 30                     # bootstrap replicates per backtest fold
INTERNAL_AECI = 178.78
H_CAP_HOURS = 100000
REASONING_START = 2024.15     # Claude 3 Opus; Epoch's 'reasoning era' break is April 2024


def log(msg, t0):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def _rows(df: pd.DataFrame, cols=None, nd=3):
    df = df if cols is None else df[cols]
    out = []
    for r in df.to_dict("records"):
        out.append({k: (round(float(v), nd) if isinstance(v, (float, np.floating)) else v) for k, v in r.items()})
    return out


def data_only_weights(rc: pd.DataFrame, ba_anth: dict, ba_all: dict):
    """Scenario weights from data alone (see METHODS section 8). Three lines of evidence for
    'the step-up reverts', averaged with equal weight; the remainder is split between
    'hold' and 'compounding' by the reference class of past breaks. Slowdown and explosive
    have no precedent in the sample and get zero here by construction."""
    acc = rc[rc.apparent_acceleration == 1]
    # one vote per independent episode: ECI (all labs) and METR (TH1.0 and TH1.1 averaged)
    ep = {}
    for name, grp in (("eci", ["eci_all"]), ("metr", ["metr_TH1.0", "metr_TH1.1"])):
        shares = []
        for s in grp:
            g = acc[acc.series == s]
            if len(g):
                shares.append(g.outcome.value_counts(normalize=True).to_dict())
        if shares:
            ep[name] = {k: float(np.mean([s.get(k, 0.0) for s in shares])) for k in ("reverted", "held", "accelerated_again")}
    cnt = {k: sum(e[k] for e in ep.values()) for k in ("reverted", "held", "accelerated_again")}
    n = sum(cnt.values())
    lap = {k: (v + 1) / (n + 3) for k, v in cnt.items()}                       # Laplace rule
    p_rev_ref = lap["reverted"]
    p_rev_anth = ba_anth["jump"]["bic_weight"] + ba_anth["linear"]["bic_weight"]
    p_rev_all = ba_all["jump"]["bic_weight"] + ba_all["linear"]["bic_weight"] + \
        (ba_all["hinge"]["bic_weight"] if ba_all["hinge"]["ratio"] < 1.15 else 0.0)
    p_rev = float(np.mean([p_rev_ref, p_rev_anth, p_rev_all]))
    share_comp = lap["accelerated_again"] / (lap["accelerated_again"] + lap["held"])
    w = {"slowdown": 0.0, "reversion": p_rev, "hold": (1 - p_rev) * (1 - share_comp),
         "compounding": (1 - p_rev) * share_comp, "explosive": 0.0}
    detail = dict(episodes=ep, episode_counts=cnt, laplace=lap, p_revert_reference_class=round(p_rev_ref, 3),
                  p_revert_anthropic_public_bic=round(p_rev_anth, 3), p_revert_all_lab_bic=round(p_rev_all, 3),
                  p_revert_combined=round(p_rev, 3), compounding_share_of_persisting=round(share_comp, 3))
    return w, detail


def central_weights(data_only):
    """Central prior = data-only weights scaled to 84%, plus 10% slowdown and 6% explosive
    (judgement; evidence in METHODS section 8)."""
    w = {k: 0.84 * v for k, v in data_only.items()}
    w["slowdown"] += 0.10
    w["explosive"] += 0.06
    s = sum(w.values())
    return {k: round(v / s, 4) for k, v in w.items()}


def run(full=False, verbose=True):
    t_start = time.time()
    R = {}
    d = D()
    edi = pd.read_csv(RAW / "eci_benchmark_difficulty.csv")
    pub = d.eci_models.set_index("model_id").eci

    # ------------------------------------------------------------------ 1. frontier backtest
    ffolds = bt.frontier_folds(d, B_BT)
    fscore = bt.score_frontier(ffolds)
    w_all, n_all = bt.stack_weights(ffolds, "all")
    w_anth, n_anth = bt.stack_weights(ffolds, "anth")
    log(f"frontier backtest: {len(ffolds)} folds; anth weights {{{', '.join(f'{k}:{v:.2f}' for k, v in w_anth.items())}}}", t_start)
    ftab = []
    for which in ("all", "anth"):
        for h in bt.HORIZONS:
            g = fscore[(fscore.which == which) & (fscore.h == h)]
            for meth, x in g.groupby("method", sort=False):
                ftab.append(dict(series=which, horizon_years=h, method=meth, **bt.summarize_method(x)))
    fcal = {}
    for which in ("all", "anth"):
        for lab, hs in (("h<=0.5", (0.25, 0.5)), ("h=1", (1.0,)), ("h>=1.5", (1.5, 2.0))):
            g = fscore[(fscore.which == which) & (fscore.method == "stacked") & fscore.h.isin(hs)]
            if len(g):
                fcal[f"{which}|{lab}"] = bt.rolling_calibration(g.rename(columns={"T": "t"}))
    R["frontier_backtest"] = dict(
        design="Monthly origins; target = running-max public ECI held at origin + h. Candidates are refitted on "
               "models released before each origin (bootstrap B=30). 'stacked' uses weights learned only from "
               "folds whose target date precedes the origin (equal weights until 10 such folds exist).",
        table=ftab, calibration=fcal, n_folds=len(ffolds),
        final_weights={"all_lab": {k: round(v, 3) for k, v in w_all.items()},
                       "anthropic": {k: round(v, 3) for k, v in w_anth.items()}},
        n_folds_used_for_weights={"all_lab": n_all, "anthropic": n_anth},
        min_cutoff_gap_days=round(float(min((f["t0"] - f["cutoff"]) for f in ffolds) * 365.25), 1))

    # ------------------------------------------------------------------ 2. release backtest
    relv, _ = bt.release_folds(d, B_BT, ffolds, with_bench=False, variants=True)
    tv = relv[relv.method.isin(["type_effect_on", "type_effect_off"])].groupby("method").crps.mean()
    use_type = bool(tv["type_effect_on"] < 0.98 * tv["type_effect_off"])    # needs a 2% CRPS gain to be switched on
    rel, benchbt = bt.release_folds(d, B_BT, ffolds, use_type=use_type)
    alpha_final = float(rel.attrs["alpha_all_folds"])
    w_rel = rel.attrs["w_release_all_folds"]
    w_equal = {c: 1.0 / len(TREND) for c in TREND}
    w_live = bt.blend_weights(w_anth, w_equal, w_rel)
    mrows = rel[rel.method == "model"].sort_values("t")
    by_lead = {str(ld): bt.release_summary(rel, ld) for ld in bt.LEADS}
    rules = []
    for ld in bt.LEADS:
        sm = bt.release_summary(relv, ld)
        for k, v in sm.items():
            if k.startswith(("rule_", "cand_", "type_")):
                rules.append(dict(lead_years=ld, variant=k, **v))
    cal_lead0 = bt.rolling_calibration(mrows[mrows.lead == 0])
    cal_lead = bt.rolling_calibration(mrows[mrows.lead > 0], min_prior=4)
    cal_all = bt.rolling_calibration(mrows)
    f_ability = {lv: max(bt.factors(cal_lead0)[lv], bt.factors(cal_lead)[lv]) for lv in (0.5, 0.8, 0.95)}
    # does a rolling bias correction help? (it does not; reported, not applied)
    deb = []
    for ld in bt.LEADS:
        g = mrows[mrows.lead == ld]
        e0, e1 = [], []
        for _, row in g.iterrows():
            prior = g[g.t < row.t0]
            if len(prior) >= 4:
                e0.append(row.err)
                e1.append(row.err - prior.err.mean())
        if e0:
            deb.append(dict(lead_years=ld, n=len(e0), mae_raw=round(float(np.mean(np.abs(e0))), 2),
                            mae_bias_corrected=round(float(np.mean(np.abs(e1))), 2)))
    log(f"release backtest: {mrows.fold.nunique()} folds ({', '.join(str(int((mrows.lead == l).sum())) for l in bt.LEADS)} by lead); "
        f"use_type={use_type}; alpha={alpha_final:.2f}", t_start)
    R["release_backtest"] = dict(
        design="Folds are (Claude release, lead) for leads of 0, 3 and 6 months. The origin is the release date minus "
               "the lead; everything is refitted on models released strictly before the origin; the model is given the "
               "release's actual date and version type. A fold exists only if the release is the next one in its family "
               "as seen from the origin, which is why few folds exist at 3 and 6 months (families ship every ~3 months). "
               "Lead 0 is a day-of nowcast. Baseline intervals are a normal centred on the baseline with the sd of its "
               "own earlier errors at that lead (from its 5th fold). Tables use the folds on which every baseline exists.",
        n_folds_by_lead={str(ld): int((mrows.lead == ld).sum()) for ld in bt.LEADS},
        summary_by_lead=by_lead, summary=by_lead["0.0"],
        combination_rules=rules,
        combination_note="The four combination rules and the seven single candidates score within noise of each other on "
                         "release folds (the lead is short, so the candidates barely differ at the target date). The "
                         "frontier folds, with longer horizons, favour the pooled candidate. The live forecast therefore "
                         "uses the 'blend' rule: the average of the frontier-fold stacking weights, the release-fold "
                         "stacking weights and equal weights.",
        live_trend_weights={k: round(v, 3) for k, v in w_live.items()},
        weight_components=dict(stack_frontier={k: round(v, 3) for k, v in w_anth.items()},
                               stack_release=None if w_rel is None else {k: round(v, 3) for k, v in w_rel.items()},
                               equal={k: round(v, 3) for k, v in w_equal.items()}),
        per_release=_rows(rel[rel.method.isin(["model", "model_date_uncertain", "prev_in_family", "family_mean_step",
                                                 "all_history_linear", "trailing_12m_linear"])],
                          ["fold", "model_id", "family", "version_type", "lead", "t0", "t", "cutoff", "y", "method", "median", "err",
                           "lo50", "hi50", "lo80", "hi80", "lo95", "hi95", "alpha"]),
        calibration=dict(lead_0=cal_lead0, lead_3_to_6_months=cal_lead, all_leads=cal_all,
                         factors_used={str(k): v for k, v in f_ability.items()},
                         rule="Per level, the larger of the lead-0 and lead>0 factors; never below 1."),
        version_type_effect=dict(crps_with=round(float(tv["type_effect_on"]), 3), crps_without=round(float(tv["type_effect_off"]), 3),
                                 used=use_type, rule="switched on only if it lowers CRPS by 2% or more"),
        bias_correction_test=dict(rows=deb, applied=False,
                                  note="The model under-predicted on average (positive bias). Subtracting the rolling mean of "
                                       "earlier errors did not reduce out-of-sample error, so no correction is applied."),
        by_family={f: bt.summarize_method(g) for f, g in mrows[mrows.lead == 0].groupby("family")})
    relsum = by_lead["0.0"]

    # benchmarks
    btab, bcal = [], {}
    bm = benchbt[benchbt.method == "model"]
    for key, g in benchbt.groupby("benchmark", sort=False):
        for meth, x in g.groupby("method", sort=False):
            s = dict(benchmark=key, method=meth, n=int(len(x)), bias=round(float(x.err.mean()), 2),
                     mae=round(float(x.err.abs().mean()), 2), rmse=round(float(np.sqrt((x.err ** 2).mean())), 2))
            if "in80" in x and x.in80.notna().any():
                s.update(cov50=round(float(x.in50.mean()), 2), cov80=round(float(x.in80.mean()), 2),
                         cov95=round(float(x.in95.mean()), 2))
            btab.append(s)
    pooled_cal = bt.rolling_calibration(bm.sort_values("t"))
    bcal["pooled"] = pooled_cal
    bfac = {}
    for key, g in bm.groupby("benchmark"):
        c = bt.rolling_calibration(g.sort_values("t"))
        bcal[key] = c
        # per-benchmark factor only with 20+ folds; otherwise pooled; never below the pooled factor
        own = bt.factors(c) if len(g) >= 20 else bt.factors(pooled_cal)
        bfac[key] = {lv: max(own[lv], bt.factors(pooled_cal)[lv]) for lv in own}
    bounded = benchbt[(benchbt.kind == "bounded")]
    ks = bounded[bounded.method == "link_given_true_ability"]
    # paired comparison with the previous-in-family baseline on the same folds
    pair = bm.merge(benchbt[benchbt.method == "prev_in_family"][["fold", "benchmark", "err"]], on=["fold", "benchmark"],
                    suffixes=("", "_prev"))
    pair_tab = [dict(benchmark=k, n=int(len(g)), mae_model=round(float(g.err.abs().mean()), 2),
                     mae_prev_in_family=round(float(g.err_prev.abs().mean()), 2),
                     model_better=bool(g.err.abs().mean() < g.err_prev.abs().mean())) for k, g in pair.groupby("benchmark")]
    R["benchmark_backtest"] = dict(
        design="Same folds as the release backtest. Each benchmark's link is refitted on models released before the "
               "origin (and must pass the inclusion rule at that date); the release's score is predicted from (a) its "
               "predicted ability ('model') and (b) its true ability ('link_given_true_ability', isolating link error). "
               "Baseline: the previous model in the family on the same benchmark.",
        table=btab, paired_vs_previous=pair_tab, calibration=bcal,
        link_only_rmse_bounded_fraction=round(float(np.sqrt(((ks.err / ks.range) ** 2).mean())), 3),
        link_only_mae_bounded_fraction=round(float((ks.err / ks.range).abs().mean()), 3),
        research_note_reference="held-out RMSE 0.092, MAE 0.067 with ability known (research note 1)",
        per_release=_rows(bm, ["fold", "model_id", "benchmark", "lead", "t0", "t", "cutoff", "y", "median", "err", "lo80", "hi80", "lo95", "hi95", "n_fit"]))
    log("benchmark backtest done", t_start)

    # ------------------------------------------------------------------ 3. leave-future-out IRT
    claude = d.claude()
    dates = sorted({round(float(t - ld), 4) for t in claude.t if t >= 2024.45 for ld in bt.LEADS})
    vint = irt.vintage_abilities(dates, pub, full)
    cfull, info_full = irt.fit_irt(irt.load_inputs(), pub)
    x = pd.DataFrame({"mine": cfull, "pub": pub}).dropna()
    rel_v, _ = bt.release_folds(d, B_BT, ffolds, abilities_by_date=vint, use_type=use_type, with_bench=False)
    mv = rel_v[rel_v.method == "model"].set_index("fold")
    mp_ = mrows.set_index("fold")
    common = mv.index.intersection(mp_.index)
    cmp_ = {}
    for ld in bt.LEADS:
        cv = [f for f in common if mv.loc[f, "lead"] == ld]
        if cv:
            cmp_[str(ld)] = dict(n=len(cv), vintage=bt.summarize_method(mv.loc[cv]), published=bt.summarize_method(mp_.loc[cv]))
    R["irt_refit_check"] = dict(
        design="Own least-squares 2PL refit of Epoch's benchmark-level inputs. For every fold origin, the IRT is "
               "refitted on models released on or before that date only and mapped to ECI units by a monotone "
               "alignment to the published ECI of those same models; the release backtest is rerun with history from "
               "the origin's vintage and the target's 'actual' from the release date's vintage.",
        full_data_reproduction=dict(n_models=int(len(x)), rmse_all=round(float(np.sqrt(((x.mine - x.pub) ** 2).mean())), 2),
                                    rmse_above_140=round(float(np.sqrt(((x.mine - x.pub)[x.pub > 140] ** 2).mean())), 2),
                                    corr=round(float(x.corr().iloc[0, 1]), 4)),
        target_shift=dict(n=int(len(common)),
                          mean_vintage_minus_published=round(float((mv.loc[common, "y"] - mp_.loc[common, "y"]).mean()), 2),
                          mean_abs=round(float((mv.loc[common, "y"] - mp_.loc[common, "y"]).abs().mean()), 2),
                          max_abs=round(float((mv.loc[common, "y"] - mp_.loc[common, "y"]).abs().max()), 2)),
        comparison_by_lead=cmp_, n_vintages=len(dates),
        caveat="Scores in Epoch's input file are today's collection; a score measured after the origin for a model "
               "released before it cannot be removed (no timestamps).",
        per_release=_rows(rel_v[rel_v.method == "model"], ["fold", "model_id", "lead", "t0", "t", "y", "median", "err", "lo80", "hi80"]))
    log(f"IRT vintage backtest: lead-0 rmse {cmp_['0.0']['vintage']['rmse']} vs published {cmp_['0.0']['published']['rmse']}", t_start)

    # ------------------------------------------------------------------ 4. reference class of breaks
    ser = {}
    for nm, which in (("eci_all", "all"), ("eci_anthropic", "anthropic")):
        t, y, _ = d.series(which).published_records()
        ser[nm] = (t, y)
    mh = pd.read_csv(RAW / "metr_horizons.csv")
    for suite in ("TH1.0", "TH1.1"):
        m = mh[mh.suite_version.astype(str).str.startswith(suite + " (METR-Horizon") & (mh.is_sota.astype(str) == "True")]
        m = m[m.release_date >= "2022-01-01"]
        ser["metr_" + suite] = (m.release_date.map(yr).to_numpy(), np.log2(m.horizon_50_minutes.astype(float).to_numpy()))
    rc = bt.break_reference_class(ser)

    # ------------------------------------------------------------------ 5. live fit
    r = mkrng("live")
    om = OriginModel(d, T_NOW + 1e-6, 150, r)
    rs_anth = d.series("anthropic"); rs_anth.start = REASONING_START
    rs_all = d.series("all"); rs_all.start = REASONING_START
    ta, ya, _ = rs_anth.published_records()
    tl, yl, _ = rs_all.published_records()
    ba_anth, _ = break_analysis(ta, ya, T_NOW)
    ba_all, _ = break_analysis(tl, yl, T_NOW)
    a6 = d.aeci("fable5.2")
    a6 = a6[a6.value_type.isin(["printed", "figure_read", "anchor_by_definition"]) & a6.t.notna()].sort_values("t")
    ba_aeci, _ = break_analysis(a6.t.to_numpy(), a6.value.to_numpy(), T_NOW)
    ai = d.aeci("fable5.2")
    ai = ai[ai.value_type.isin(["printed", "figure_read", "anchor_by_definition"])].copy()
    ai["ti"] = [yr(x) if isinstance(x, str) else np.nan for x in ai.internal_date]
    ai.loc[ai.model_id.str.contains("internal"), "ti"] = yr("2026-09-26")
    ai = ai[ai.ti.notna()].sort_values("ti")
    idx = __import__("capmodel.trend", fromlist=["records"]).records(ai.ti.to_numpy(), ai.value.to_numpy())
    ba_aeci_int, _ = break_analysis(ai.ti.to_numpy()[idx], ai.value.to_numpy()[idx], T_NOW)
    ens_reason = Ensemble(rs_anth, T_NOW + 1e-6, 200, r, cands=["hinge"])
    sl = np.concatenate([f.sample_slopes(60, r) for f in ens_reason.fits["hinge"] if f.kind_eff == "hinge"])
    sl = sl[(sl[:, 0] > 5) & (sl[:, 0] < 30) & (sl[:, 1] > 5) & (sl[:, 1] < 60)]
    R["trend"] = dict(
        note="Record-setting releases since Claude 3 Opus (March 2024). 'hinge' = piecewise linear with unknown "
             "changepoint; 'jump' = constant slope with a one-time level shift. BIC weights compare the four forms "
             "on the published point estimates; the slope-ratio interval is from the bootstrap over models and "
             "Epoch posterior draws.",
        anthropic_public_eci=ba_anth, all_lab_public_eci=ba_all, aeci_nov6_public_dates=ba_aeci,
        aeci_nov6_internal_dates_with_internal_model=ba_aeci_int,
        anthropic_public_slope_draws=dict(pre=summarize(sl[:, 0]), post=summarize(sl[:, 1]), ratio=summarize(sl[:, 1] / sl[:, 0], 3),
                                          tau=summarize(sl[:, 2], 3), n=int(len(sl)),
                                          p_ratio_above_1_3=round(float((sl[:, 1] / sl[:, 0] > 1.3).mean()), 3),
                                          p_ratio_above_1_88=round(float((sl[:, 1] / sl[:, 0] > 1.88).mean()), 3)),
        records_anthropic=[dict(model_id=n, t=round(float(t), 3), eci=float(y)) for n, t, y in
                           zip(np.asarray(om.anth.series.names)[om.anth.series.published_records()[2]], om.anth.rt, om.anth.ry)],
        records_all_lab=[dict(model_id=n, t=round(float(t), 3), eci=float(y)) for n, t, y in
                         zip(np.asarray(om.all.series.names)[om.all.series.published_records()[2]], om.all.rt, om.all.ry)],
        published_statements=dict(aeci_card="15.3 -> 28.7 AECI/yr from Oct 2025, 1.88x (1.62-2.28)",
                                  epoch="16.6 ECI/yr (14.6-18.7) reasoning-era all-lab frontier"))
    # trend-model comparison curves for plotting
    grid = np.round(np.arange(2024.0, 2028.01, 0.05), 3)
    curves = {}
    for c in TREND:
        L, _ = om.level(c, grid[grid >= 2025.5], 2000)
        curves[c] = dict(t=[float(v) for v in grid[grid >= 2025.5]], median=[round(float(v), 2) for v in np.median(L, 0)],
                         lo80=[round(float(v), 2) for v in np.quantile(L, 0.1, 0)], hi80=[round(float(v), 2) for v in np.quantile(L, 0.9, 0)])
    R["trend"]["candidate_curves_anthropic"] = curves

    # families
    ff = om.ff
    R["families"] = dict(
        note="Offsets are ECI minus the piecewise reference line through Anthropic's record-setters, weighted "
             "toward recent releases (half-life %.1f years). 'pooled' is the empirical-Bayes estimate used by the "
             "'mean' predictor; 'last' is the family's most recent offset, used by the 'last' predictor." % fam.HALF_LIFE,
        table=[dict(family=f, n=int(v["n"]), n_eff=round(v["n_eff"], 2), unpooled_mean=round(v["mean"], 2),
                    pooled_mean=round(v["pooled"], 2), pooled_se=round(v["pooled_se"], 2), shrinkage=round(v["shrink"], 3),
                    last_offset=round(v["last"], 2), last_eci=round(v["last_eci"], 2)) for f, v in ff["fam"].items()],
        within_family_sd=round(float(np.sqrt(ff["s2"])), 2), between_family_sd=round(float(np.sqrt(ff["tau2"])), 2),
        grand_mean=round(ff["mu"], 2), version_type_effect={k: round(v, 2) for k, v in ff["type"].items()},
        version_type_effect_used=use_type, alpha_weight_on_last_offset=round(alpha_final, 3),
        offsets=_rows(om.hist, ["model_id", "family", "version_type", "t", "eci", "offset", "w"]),
        mythos="Mythos is the restricted twin of Fable (same underlying model per Anthropic). Public ECI scores Fable "
               "only, so on the ECI scale Mythos uses Fable's history; AECI is printed for Mythos only.")

    # AECI mapping and drift
    mp = aeci.Mapping(d, 400, mkrng("mapping"))
    dr = aeci.Drift(d)
    sel = np.mean([h["sse"] > o["sse"] for h, o in zip(mp.draws["hinge"], mp.draws["offset"])])
    p_offset = float(np.clip(sel, 0.2, 0.8))
    est = d.index[(d.index.scale == "aeci") & (d.index.fit == "fable5.2_repo_rescaled")].merge(
        d.models[["model_id", "eci"]], on="model_id")
    est_chk = [dict(model_id=x.model_id, eci=x.eci, repo_rescaled_aeci=x.value,
                    mapped_hinge=round(float(mp.apply_point(np.array([x.eci]), "hinge")[0]), 2),
                    mapped_offset=round(float(mp.apply_point(np.array([x.eci]), "offset")[0]), 2)) for x in est.itertuples()]
    res_extra = [e["repo_rescaled_aeci"] - (p_offset * e["mapped_offset"] + (1 - p_offset) * e["mapped_hinge"]) for e in est_chk]
    tab = mp.tab
    res_fit = tab.aeci - (p_offset * tab.fit_offset + (1 - p_offset) * tab.fit_hinge)
    map_sd = float(np.sqrt(np.mean(np.concatenate([res_fit.to_numpy(), np.asarray(res_extra)]) ** 2)))
    for f_ in ("hinge", "offset"):
        mp.point[f_]["sd"] = max(mp.point[f_]["sd"], map_sd)
    R["aeci"] = dict(
        primary_scale="Public ECI is the modelling scale: 256 models from all labs over four years, published posterior "
                      "draws, and benchmark-level inputs that let the scale be refitted. AECI has 14 released models on "
                      "one fit, is built on first-party internal benchmarks and is re-estimated by every card. AECI is "
                      "the headline *reporting* scale: every prediction is carried to it through the mapping below.",
        overlap=_rows(tab), mapping_forms=mp.point, mapping_bic={k: round(float(v), 2) for k, v in mp.bic.items()},
        bootstrap_share_offset_form_fits_better=round(float(sel), 3), p_offset_form_used=round(p_offset, 3),
        slope_above_knee_hinge=summarize(mp.slope_above(), 3), mapping_residual_sd_used=round(map_sd, 2),
        overlap_rmse=dict(hinge=round(float(np.sqrt(np.mean((tab.aeci - tab.fit_hinge) ** 2))), 2),
                          offset=round(float(np.sqrt(np.mean((tab.aeci - tab.fit_offset) ** 2))), 2)),
        out_of_sample_check_repo_rescaled=est_chk,
        divergence_note="Below public ECI ~157 (through Opus 4.6) the two scales agree within about 1 point. For every "
                        "model released since June 2026 AECI is 3.7-6.2 points higher. A one-time level shift fits that "
                        "better than a steadily widening gap, but five points cannot separate the two, so both forms "
                        "are carried.",
        drift=dict(summary=dr.summary(), transitions=_rows(dr.trans.reset_index().rename(columns={"mean": "mean_delta", "count": "n_models"})),
                   rows=_rows(dr.rows), own_card_sd=aeci.OWN_SD,
                   matrix=_rows(dr.piv.reset_index()),
                   note="Per-refit change in printed AECI of frontier models between consecutive card fits. Seven "
                        "transitions: five near zero, two near +5 (the Sept 18 fit and the Haiku 5.5 card fit)."))
    # leave-one-out check of the drift model (tiny n)
    steps = dr.steps
    loo = []
    for i in range(len(steps)):
        others = np.delete(steps, i)
        s = mkrng("drift" + str(i)).choice(others, 4000) + dr.within_sd * mkrng("driftn" + str(i)).standard_normal(4000)
        st = bt.interval_stats(s, steps[i])
        loo.append(dict(transition=aeci.FIT_ORDER[i + 1], actual=round(float(steps[i]), 2), median=round(st["median"], 2),
                        lo80=round(st["lo80"], 2), hi80=round(st["hi80"], 2), in80=st["in80"], in95=st["in95"]))
    R["aeci"]["drift"]["leave_one_out"] = dict(rows=loo, cov80=round(float(np.mean([x["in80"] for x in loo])), 2),
                                               cov95=round(float(np.mean([x["in95"] for x in loo])), 2), n=len(loo),
                                               caveat="n=7 transitions; coverage figures are indicative only")
    # links
    e_all, _ = d.ability_table()
    abil = e_all.set_index("model_id").eci
    links, dropped = lk.fit_links(d.bench, d.meta, abil, T_NOW + 1, 300, mkrng("links"), edi)
    meta = d.meta.set_index("benchmark")
    R["links"] = dict(
        table=[dict(l.describe(), title=meta.loc[k, "title"], unit=meta.loc[k, "unit"], group=meta.loc[k, "group"],
                    lo=meta.loc[k, "lo"], hi=meta.loc[k, "hi"], configuration=meta.loc[k, "configuration"],
                    source=meta.loc[k, "source"], n_claude=int(meta.loc[k, "n_claude"])) for k, l in links.items()],
        dropped=[dict(benchmark=k, title=meta.loc[k, "title"], reason=why) for k, why in dropped] + [
            dict(benchmark="terminal_bench_4_0", title="Terminal-Bench 4.0", reason="scores exist for five Claude models only (Artificial Analysis), all released Sept-Nov 2026")],
        calibration_factors={k: {str(lv): v for lv, v in f.items()} for k, f in bfac.items()},
        note="Own fit for every benchmark. Where the benchmark is in public ECI, Epoch's item parameters are shown "
             "beside the fit and the fit's RMSE under Epoch's parameters is reported; they agree closely wherever "
             "the data are the same (GPQA, FrontierMath, ARC-AGI-2, RLI, Terminal-Bench 2.0).")
    for row in R["links"]["table"]:
        l = links[row["benchmark"]]
        gx = np.linspace(110, 215, 106)
        row["curve"] = dict(eci=[float(v) for v in gx], score=[round(float(v), 3) for v in l.mean(gx)])
        row["points"] = [dict(eci=round(float(a), 2), score=round(float(b), 3)) for a, b in zip(l.x, l.y)]
    log(f"live fit, mapping (p_offset={p_offset:.2f}), {len(links)} links, dropped {len(dropped)}", t_start)

    # ------------------------------------------------------------------ 6. next-model predictions
    rd = pr.ReleaseDates()
    cl = d.claude()
    internal_note = ("Anthropic's Fable 5.2 card prints an unreleased internal model at AECI %.2f (15 benchmarks, internal "
                     "date ~2026-09-26). It is not used in the fit; p_aeci_at_or_above_internal_model compares the "
                     "prediction with it." % INTERNAL_AECI)
    cur_aeci = {"opus": ("Claude Opus 5.5", 174.78, "printed"), "mythos": ("Claude Mythos 5.2", 177.12, "printed"),
                "fable": ("Claude Mythos 5.2 (twin)", 177.12, "printed for Mythos twin"),
                "sonnet": ("Claude Sonnet 5.5", 173.6, "repo estimate, not Anthropic's"),
                "haiku": ("Claude Haiku 5.5", 167.3, "repo estimate, not Anthropic's")}
    nxt, open_preds = {}, []
    samples_keep = {}
    for f in FAMILIES:
        rr = mkrng("next-" + f)
        om.rng = rr
        days = rd.sample_days(f, N_MC, rr)
        T = T_NOW + days / 365.25
        hf = cl[cl.family == fam.twin_family(f)].sort_values("t")
        last = hf.iloc[-1]
        names = rd.names(f)
        tprobs = pr.type_probs(names, float(last.version), int(last.generation))
        theta, comps, L = om.family_predict(f, T, tprobs, N_MC, w_live, alpha_final, use_type)
        forms = (rr.random(N_MC) < p_offset).astype(int)
        a_nov6 = mp.sample(theta, forms, rr)
        K = pr.refit_count(rd, f, days, N_MC, rr)
        a_own = a_nov6 + dr.sample(K, rr) + aeci.OWN_SD * rr.standard_normal(N_MC)
        top_name = max(names, key=names.get)
        cond = []
        for lab, qk in (("q10", "q10"), ("median", "median"), ("q90", "q90")):
            dd = rd.fc["targets"][f]["with_signals"][qk]
            th_c, _, _ = om.family_predict(f, yr(dd), tprobs, 4000, w_live, alpha_final, use_type)
            cond.append(dict(release_date=dd, quantile=lab, eci_median=round(float(np.median(th_c)), 2)))
        benches = {}
        for k, l in links.items():
            s = l.sample(theta, rr)
            fk = bfac.get(k, bt.factors(pooled_cal))
            if l.kind == "bounded":      # stretch on the logit scale so intervals stay inside the bounds
                lo_, hi_ = float(meta.loc[k, "lo"]), float(meta.loc[k, "hi"])
                pz = np.clip((s - lo_) / (hi_ - lo_), 1e-4, 1 - 1e-4)
                ws = widen(np.log(pz / (1 - pz)), fk, nd=4)
                w_ = {kk: round(float(lo_ + (hi_ - lo_) / (1 + np.exp(-v))), 2) for kk, v in ws.items()}
                w_["mean"] = round(float(s.mean()), 2)
            elif l.kind == "loghorizon":   # stretch in log space
                ws = widen(np.log2(s), fk, nd=4)
                w_ = {kk: round(float(2.0 ** v), 1) for kk, v in ws.items()}
            else:
                w_ = widen(s, fk)
            prev = d.bench[(d.bench.benchmark == k) & (d.bench.family == fam.twin_family(f))].sort_values("t")
            benches[k] = dict(w_, title=meta.loc[k, "title"], unit=meta.loc[k, "unit"],
                              previous_in_family=None if not len(prev) else dict(model_id=prev.model_id.iloc[-1], value=float(prev.value.iloc[-1])),
                              p_above_90pct_of_range=None if l.kind != "bounded" else round(float(
                                  (s >= meta.loc[k, "lo"] + 0.9 * (meta.loc[k, "hi"] - meta.loc[k, "lo"])).mean()), 3))
        eci_s = widen(theta, f_ability)
        nxt[f] = dict(
            family=f, previous_model=last.model_id if f != "mythos" else "Claude Mythos 5.2",
            previous_eci=float(last.eci), previous_aeci_nov6=dict(model=cur_aeci[f][0], value=cur_aeci[f][1], kind=cur_aeci[f][2]),
            predicted_name=top_name, name_probabilities={k: round(v, 3) for k, v in names.items()},
            version_type_probabilities={k: round(v, 3) for k, v in tprobs.items()},
            release_date=rd.summary(f), eci=eci_s, eci_raw_uncalibrated=summarize(theta),
            aeci_nov6_scale=widen(a_nov6, f_ability), aeci_own_card=widen(a_own, f_ability),
            refits_before_own_card=dict(median=int(np.median(K)), mean=round(float(K.mean()), 2), p_one=round(float((K == 1).mean()), 3)),
            eci_given_release_date=cond, benchmarks=benches,
            p_eci_above_previous_in_family=round(float((theta > last.eci).mean()), 3),
            p_eci_above_current_anthropic_best=round(float((theta > om.anth.F0).mean()), 3),
            p_aeci_at_or_above_internal_model=round(float((a_nov6 >= INTERNAL_AECI).mean()), 3),
            components=dict(trend_level_at_release=summarize(L), offset_mean_predictor=summarize(comps["mean"] - L),
                            offset_last_predictor=summarize(comps["last"] - L)),
            resolvable=dict(eci=f != "mythos", aeci=f != "fable",
                            note=("Epoch does not score Mythos; this is the Fable twin's scale." if f == "mythos" else
                                  "Anthropic prints AECI for the Mythos twin only; resolves against the co-launched Mythos."
                                  if f == "fable" else "")))
        samples_keep[f] = dict(theta=theta, T=T)
        # open predictions
        base_id = f"{AS_OF}:{f}:next"
        crit = f"The first {f.capitalize()} release after {AS_OF} listed in data/models.json."
        if f != "mythos":
            open_preds.append(dict(id=base_id + ":eci", family=f, quantity="eci_public", unit="ECI points",
                                   applies_to=crit, **{k: eci_s[k] for k in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")},
                                   resolution="Epoch public ECI of the model in capability/data/raw/eci_public.csv at first appearance "
                                              "(Epoch refits the scale; grade on the first published value)."))
        if f != "fable":
            ao = nxt[f]["aeci_own_card"]
            open_preds.append(dict(id=base_id + ":aeci_own_card", family=f, quantity="aeci_own_card", unit="AECI points",
                                   applies_to=crit, **{k: ao[k] for k in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")},
                                   resolution="AECI printed for the model in its own system card (aeci_all.csv row with own_card=1)."))
        for k in benches:
            if meta.loc[k, "group"] != "site":
                continue
            bb = benches[k]
            open_preds.append(dict(id=base_id + ":" + k, family=f, quantity=k, unit=meta.loc[k, "unit"], applies_to=crit,
                                   **{kk: bb[kk] for kk in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")},
                                   resolution=f"Score of the model on data/benchmarks.json chart '{k}' in the series' stated "
                                              f"configuration ({meta.loc[k, 'configuration']})."))
    R["next_models"] = dict(note=internal_note, calibration_factors_ability={str(k): v for k, v in f_ability.items()},
                            trend_weights={k: round(v, 3) for k, v in w_live.items()}, families=nxt,
                            n_draws=N_MC,
                            date_integration="Each draw samples a release date from the forecaster's distribution, then the "
                                             "trend level at that date, the family offset and the version type.")
    R["open_predictions"] = open_preds
    log("next-model predictions done", t_start)

    # ------------------------------------------------------------------ 7. projection
    rp = mkrng("projection")
    om.rng = rp
    g1 = fscore[(fscore.method == "stacked") & (fscore.h == 1.0)]
    sigma_w = max(float(g1.groupby("which").err.std().max()), 2.0)
    data_w, data_detail = data_only_weights(rc, ba_anth, ba_all)
    W = dict(pj.WEIGHTS)
    W["data_only"] = {k: round(v, 4) for k, v in data_w.items()}
    W["central"] = central_weights(data_w)
    # historical gap of the other labs' frontier to Anthropic's
    e_ = d.eci_models
    tg = np.arange(2024.2, T_NOW, 1 / 52)
    fa = np.array([e_[(e_.lab == "Anthropic") & (e_.t <= t)].eci.max() for t in tg])
    fo = np.array([e_[(e_.lab != "Anthropic") & (e_.t <= t)].eci.max() for t in tg])
    G = fo - fa
    lag = 13
    phi_q = float(np.clip(np.corrcoef(G[:-lag], G[lag:])[0, 1], 0.0, 0.95))
    g_mu, g_sd, g0 = float(G.mean()), float(G.std()), float(G[-1])
    mlink = links["metr_h50"]
    S_res = float(np.mean([p[3] for f_ in om.anth.fits["hinge"][:50] for p in f_.parts]))
    paths = {}
    fam_cur = {f: float(cl[cl.family == fam.twin_family(f)].sort_values("t").eci.iloc[-1]) for f in FAMILIES}
    aeci_cur_front = 177.12
    for scn in pj.SCENARIOS:
        n = N_SCN
        L0, _, _ = om.stacked_level([T_NOW], n, w_live)
        ii = rp.integers(0, len(sl), n)
        level, pace, drv = pj.simulate(scn, n, rp, L0[:, 0], sl[ii, 0], sl[ii, 1], sigma_w)
        Lq, gq = pj.at_quarters(level), pj.at_quarters(pace)
        Q = len(pj.TQ)
        age = np.stack([om.anth.sample_age(n, rp) for _ in range(Q)], 1)
        cand = Lq - gq * age + S_res * rp.standard_t(NU, (n, Q)) / np.sqrt(NU / (NU - 2))
        F = np.maximum.accumulate(np.maximum(cand, om.anth.F0), axis=1)
        # other labs: mean-reverting gap to Anthropic's frontier
        Gq = np.empty((n, Q))
        gprev = np.full(n, g0)
        for j in range(Q):
            steps_q = (pj.TQ[j] - (T_NOW if j == 0 else pj.TQ[j - 1])) / 0.25
            ph = phi_q ** steps_q
            gprev = g_mu + ph * (gprev - g_mu) + g_sd * np.sqrt(1 - ph ** 2) * rp.standard_normal(n)
            Gq[:, j] = gprev
        F_all = np.maximum.accumulate(np.maximum(F, F + Gq), axis=1)
        forms = (rp.random(n) < p_offset).astype(int)
        pidx = rp.integers(0, 10 ** 6, n)
        A = mp.sample(F, forms, rp, noise=False, pidx=pidx) + map_sd * rp.standard_normal((n, 1))
        A = np.where(F <= om.anth.F0 + 1e-9, aeci_cur_front, A)
        A = np.maximum.accumulate(np.maximum(A, aeci_cur_front), axis=1)
        mslope = np.where(forms == 1, 1.0, 1.0 + np.array([mp.draws["hinge"][i % len(mp.draws["hinge"])]["c"] for i in pidx]))
        # implied METR horizon at the frontier (link parameters drawn per path, no observation noise)
        bi = rp.integers(0, len(mlink.boot), n)
        H = 2.0 ** (mlink.boot[bi, 0][:, None] + mlink.boot[bi, 1][:, None] * F)
        # families: latest released model in each family
        fams = {}
        for f in FAMILIES:
            tf = fam.twin_family(f)
            wait = rd.sample_days(f, n, rp) / 365.25
            gap = rd.gap_years(f) * np.exp(0.42 * rp.standard_normal(n))
            v = ff["fam"][tf]
            delta = v["pooled"] + v["pooled_se"] * rp.standard_normal(n)
            drift_z = rp.standard_normal(n)
            out = np.empty((n, Q))
            for j in range(Q):
                h = pj.TQ[j] - T_NOW
                a_ = np.minimum(rp.random(n) * gap, np.maximum(h - wait, 0.0))
                pos = np.clip((pj.TQ[j] - a_ - pj.TM[0]) / pj.DT, 0, len(pj.TM) - 1 - 1e-9)
                i0 = pos.astype(int)
                frc = pos - i0
                rr_ = np.arange(n)
                lv = level[rr_, i0] * (1 - frc) + level[rr_, i0 + 1] * frc
                val = lv + delta + pj.FAMILY_DRIFT_SD * np.sqrt(h) * drift_z + np.sqrt(ff["s2"]) * rp.standard_normal(n)
                out[:, j] = np.where(h > wait, np.maximum(val, fam_cur[f]), fam_cur[f])
            out = np.maximum.accumulate(out, axis=1)
            Af = mp.sample(out, forms, rp, noise=False, pidx=pidx) + map_sd * rp.standard_normal((n, 1))
            Af = np.where(out <= fam_cur[f] + 1e-9, cur_aeci[f][1], Af)
            fams[f] = (out, np.maximum.accumulate(Af, axis=1))
        sat = {}
        for k, l in links.items():
            if l.kind != "bounded":
                continue
            bi2 = rp.integers(0, len(l.boot), n)
            for frac in (0.9, 0.95):
                thr = l.boot[bi2, 1] + np.log(frac / (1 - frac)) / l.boot[bi2, 0]
                sat[(k, frac)] = pj.crossing_date(level, thr)
        # frontier score on each benchmark (link mean with parameter draws; no model-level noise)
        bq = {}
        for k, l in links.items():
            bi3 = rp.integers(0, len(l.boot), n)
            a_, b_ = l.boot[bi3, 0][:, None], l.boot[bi3, 1][:, None]
            if l.kind == "bounded":
                bq[k] = l.lo + (l.hi - l.lo) / (1 + np.exp(-np.clip(a_ * (F - b_), -40, 40)))
            elif l.kind == "loghorizon":
                bq[k] = 2.0 ** (a_ + b_ * F)
            else:
                bq[k] = a_ + b_ * F
        yr_pace = {}
        for y in range(2027, 2031):
            mk = (pj.TM >= y) & (pj.TM < y + 1)
            yr_pace[y] = pace[:, mk].mean(1)
        paths[scn] = dict(F=F, A=A, F_all=F_all, H=H, fams=fams, sat=sat, bq=bq, pace=yr_pace, mslope=mslope,
                          b_pre=sl[ii, 0], m_post=drv["m_post"], level=Lq)
    log("scenario simulation done", t_start)

    def mix(weights, key, sub=None):
        xs, ws = [], []
        for s in pj.SCENARIOS:
            x = paths[s][key] if sub is None else paths[s][key][sub]
            if isinstance(x, tuple):
                x = x[0]
            xs.append(x)
            ws.append(np.full(len(x), weights[s] / len(x)))
        return np.concatenate(xs), np.concatenate(ws)

    def mixfam(weights, f, i):
        xs = np.concatenate([paths[s]["fams"][f][i] for s in pj.SCENARIOS])
        ws = np.concatenate([np.full(N_SCN, weights[s] / N_SCN) for s in pj.SCENARIOS])
        return xs, ws

    wc = W["central"]
    one = lambda s: {k: (1.0 if k == s else 0.0) for k in pj.SCENARIOS}
    proj = dict(quarters=pj.QUARTERS, scale_note="AECI values are on the November 6 2026 fit; later cards will "
                "re-estimate the scale (see aeci.drift).", series={})
    def series_block(key, nd=2):
        blk = {"mixture": pj.bands(*mix(wc, key), nd)}
        for s in pj.SCENARIOS:
            blk[s] = pj.bands(*mix(one(s), key), nd)
        return blk
    proj["series"]["anthropic_frontier_eci"] = series_block("F")
    proj["series"]["anthropic_frontier_aeci"] = series_block("A")
    proj["series"]["all_lab_frontier_eci"] = series_block("F_all")
    def _hours(b):   # minutes -> hours; values past the cap are reported as the cap (flagged in metadata)
        return dict(date=b["date"], **{kk: (None if vv is None else round(min(vv / 60.0, H_CAP_HOURS), 1)) for kk, vv in b.items() if kk != "date"})
    proj["series"]["anthropic_frontier_metr_h50_hours"] = {k: [_hours(b) for b in v] for k, v in series_block("H", 1).items()}
    proj["metr_horizon_note"] = ("Implied METR-style 50%% time horizon from the fitted link (%.2f ECI points per doubling; METR's own "
                                 "measurements stop at 17.4 hours, Mythos Preview, and METR calls anything above 16 hours unreliable). "
                                 "Everything here is extrapolation; values are capped at %d hours (about 50 work-years), beyond which "
                                 "the number has no operational meaning." % (1 / mlink.par[1], H_CAP_HOURS))
    proj["families"] = {}
    for f in FAMILIES:
        proj["families"][f] = dict(eci=pj.bands(*mixfam(wc, f, 0)), aeci=pj.bands(*mixfam(wc, f, 1)),
                                   current_eci=fam_cur[f], current_aeci=cur_aeci[f][1], current_aeci_kind=cur_aeci[f][2])
    proj["benchmarks_at_frontier"] = {}
    for k, l in links.items():
        xs = np.concatenate([paths[s]["bq"][k] for s in pj.SCENARIOS])
        ws = np.concatenate([np.full(N_SCN, wc[s] / N_SCN) for s in pj.SCENARIOS])
        proj["benchmarks_at_frontier"][k] = dict(title=meta.loc[k, "title"], unit=meta.loc[k, "unit"], kind=l.kind,
                                                 bands=pj.bands(xs, ws, 2 if l.kind != "linear" or k == "forecastbench" else 0))
    # scenario table
    scn_tab = []
    for s in pj.SCENARIOS:
        p = paths[s]
        row = dict(scenario=s, definition=pj.SCENARIO_DEFS[s])
        for y in range(2027, 2031):
            row[f"pace_eci_{y}"] = dict(median=round(float(np.median(p["pace"][y])), 1),
                                        lo80=round(float(np.quantile(p["pace"][y], 0.1)), 1),
                                        hi80=round(float(np.quantile(p["pace"][y], 0.9)), 1))
            row[f"pace_aeci_{y}_median"] = round(float(np.median(p["pace"][y] * p["mslope"])), 1)
            row[f"k_vs_prebreak_{y}_median"] = round(float(np.median(p["pace"][y] / p["b_pre"])), 2)
        row["weights"] = {wn: W[wn][s] for wn in W}
        scn_tab.append(row)
    qi = {qd: i for i, qd in enumerate(pj.QUARTERS)}
    sens = []
    for wn, wv in W.items():
        for key, lab in (("F", "anthropic_frontier_eci"), ("A", "anthropic_frontier_aeci")):
            x, w_ = mix(wv, key)
            for qd in ("2027-12-31", "2028-12-31", "2030-12-31"):
                sens.append(dict(weighting=wn, series=lab, date=qd, **wsummary(x[:, qi[qd]], w_, 1)))
    # headline rows (end of each year)
    head = []
    for qd in ("2026-12-31", "2027-12-31", "2028-12-31", "2029-12-31", "2030-12-31"):
        j = qi[qd]
        xe, w_ = mix(wc, "F"); xa, _ = mix(wc, "A"); xh, _ = mix(wc, "H"); xl, _ = mix(wc, "F_all")
        head.append(dict(date=qd, eci=wsummary(xe[:, j], w_, 1), aeci=wsummary(xa[:, j], w_, 1),
                         all_lab_eci=wsummary(xl[:, j], w_, 1),
                         metr_h50_hours={k: (None if v is None else round(min(v / 60, H_CAP_HOURS), 1)) for k, v in wsummary(xh[:, j], w_, 2).items()}))
    # saturation
    sat_tab = []
    for k, l in links.items():
        if l.kind != "bounded":
            continue
        row = dict(benchmark=k, title=meta.loc[k, "title"], group=meta.loc[k, "group"],
                   frontier_score_now=round(float(l.mean(om.anth.F0)), 1),
                   best_observed=round(float(np.max(l.y)), 1), ceiling=float(l.hi),
                   ability_at_90=round(l.ability_at(0.9), 1), ability_at_95=round(l.ability_at(0.95), 1))
        for frac, tag in ((0.9, "90"), (0.95, "95")):
            xs = np.concatenate([paths[s]["sat"][(k, frac)] for s in pj.SCENARIOS])
            ws = np.concatenate([np.full(N_SCN, wc[s] / N_SCN) for s in pj.SCENARIOS])
            row["cross_" + tag] = pj.date_summary(xs, ws)
        sat_tab.append(row)
    # width check vs research note 1
    xe, w_ = mix(wc, "F")
    widths = []
    for qd, hy, ref in (("2027-12-31", 1.1, (-5, 5)), ("2028-12-31", 2.1, (-8, 14)), ("2030-12-31", 4.1, (-20, 45))):
        s = wsummary(xe[:, qi[qd]], w_, 1)
        widths.append(dict(date=qd, horizon_years=hy, ours_minus=round(s["lo80"] - s["median"], 1), ours_plus=round(s["hi80"] - s["median"], 1),
                           research_minus=ref[0], research_plus=ref[1],
                           at_least_as_wide=bool(s["lo80"] - s["median"] <= ref[0] and s["hi80"] - s["median"] >= ref[1])))
    # external comparison
    xl, wl = mix(wc, "F_all")
    rise29 = xl[:, qi["2029-12-31"]] - xl[:, qi["2028-12-31"]]
    r29 = wquantile(rise29, wl, [0.1, 0.25, 0.5, 0.75, 0.9])
    j28 = qi["2028-09-30"]
    ros = wsummary(xl[:, j28], wl, 1)
    xh, wh = mix(wc, "H")
    def first_cross_h(thr_minutes):
        out = []
        for s in pj.SCENARIOS:
            Hs = paths[s]["H"]
            above = Hs >= thr_minutes
            first = np.where(above.any(1), pj.TQ[above.argmax(1)], np.inf)
            out.append(first)
        return np.concatenate(out)
    ext = [
        dict(source="FutureSearch (2026-11-14)", quantity="Rise in the highest public ECI held by OpenAI/Anthropic/GDM during 2029",
             theirs="p10 11.7, p25 18.5, p50 27.3, p75 42.7, p90 74", ours="p10 %.1f, p25 %.1f, p50 %.1f, p75 %.1f, p90 %.1f" % tuple(r29),
             ours_values=dict(p10=round(r29[0], 1), p25=round(r29[1], 1), p50=round(r29[2], 1), p75=round(r29[3], 1), p90=round(r29[4], 1)),
             why="Same shape (right-skewed). Ours is built from a scenario mixture whose 'hold' pace decays with the central compute path."),
        dict(source="Ho et al., Rosetta Stone naive extrapolation (2025-10; conversion approximate)",
             quantity="All-lab public ECI frontier, Oct 2028", theirs="~189 (182-196)",
             ours="median %.1f (80%% %.1f-%.1f) at 2028-09-30" % (ros["median"], ros["lo80"], ros["hi80"]), ours_values=ros,
             why="Rosetta extrapolates the 2023-25 slope; the frontier is already ~8 ECI above that line (research note 1)."),
        dict(source="Epoch AI trend (not a forecast), Nov 2026", quantity="All-lab frontier slope",
             theirs="16.6 ECI/yr (14.6-18.7); straight-line value at end-2030: %.0f" % (om.all.F0 + 16.6 * (2031.0 - T_NOW)),
             ours="median %.1f at 2030-12-31" % wsummary(xl[:, qi["2030-12-31"]], wl, 1)["median"],
             ours_values=wsummary(xl[:, qi["2030-12-31"]], wl, 1),
             why="Our median sits above Epoch's straight line because %.0f%% of the weight is on 'hold' or faster for "
                 "Anthropic and the rival frontier is assumed to keep pace; our 'reversion' scenario is close to Epoch's line."
                 % (100 * (wc["hold"] + wc["compounding"] + wc["explosive"]))),
    ]
    for lab, thr in (("1 work-month (167 h)", 167 * 60), ("1 work-year (2,000 h)", 2000 * 60)):
        fc = first_cross_h(thr)
        wts = np.concatenate([np.full(N_SCN, wc[s] / N_SCN) for s in pj.SCENARIOS])
        ds = pj.date_summary(np.where(np.isinf(fc), np.inf, fc), wts)
        ext.append(dict(source="METR-style horizon milestones (for AI Futures comparison)",
                        quantity=f"Implied 50% time horizon of Anthropic's frontier reaches {lab}",
                        theirs="AI Futures: Automated Coder median mid-2028 (Kokotajlo) / mid-2030 (Lifland); Superhuman AI "
                               "Researcher medians 2027 under a held 1.7-1.9x trend",
                        ours=f"quarter ending {ds['median']} at the median (10-90%: {ds['q10']} to {ds['q90']}); P(by end-2030) {ds['p_by_end_2030']}",
                        ours_values=ds,
                        why="Not the same quantity: ours is an extrapolated METR 50% horizon from the ECI link (4.75 ECI per "
                            "doubling), far outside the measured range (max 17 h); theirs are capability milestones from a "
                            "takeoff model. Read as an order-of-magnitude cross-check only."))
    proj.update(scenarios=scn_tab, weights=W, weights_evidence=data_detail, sensitivity=sens, headline=head,
                saturation=sat_tab, width_check=widths, external_comparison=ext,
                assumptions=dict(kappa_eci_per_10x_compute=[pj.KAPPA_MEAN, pj.KAPPA_SD], compute_paths=pj.COMPUTE,
                                 haircut_realised_share=list(pj.HAIRCUT), annual_random_walk_sd=round(sigma_w, 2),
                                 family_drift_sd_per_sqrt_year=pj.FAMILY_DRIFT_SD,
                                 other_labs_gap=dict(mean=round(g_mu, 2), sd=round(g_sd, 2), now=round(g0, 2), quarterly_autocorr=round(phi_q, 2)),
                                 slope_draws=dict(b_pre=summarize(sl[:, 0]), b_post=summarize(sl[:, 1])),
                                 m_post=summarize(np.concatenate([paths[s]["m_post"] for s in pj.SCENARIOS]), 2),
                                 n_paths_per_scenario=N_SCN))
    R["projection"] = proj
    R["reference_class"] = dict(rows=_rows(rc), note="Quarterly origins on record series; slopes over (t0-3,t0-1], (t0-1,t0], (t0,t0+1]. "
                                "Nearly all rows are the same 2024 episode seen through overlapping windows.")
    R["_runtime_seconds"] = round(time.time() - t_start, 1)
    R["_objects"] = dict(d=d, om=om, links=links, mp=mp, paths=paths, fscore=fscore, rel=rel, benchbt=benchbt,
                         samples=samples_keep, W=W, rd=rd)
    log("projection done", t_start)
    return R
