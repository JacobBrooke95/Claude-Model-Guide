"""End-to-end run (v2): backtests -> bias term and calibration -> one live level process ->
next-model predictions and the 2026-2030 projection drawn from the same paths."""
from __future__ import annotations
import time
import numpy as np
import pandas as pd

from .common import rng as mkrng, yr, from_yr, AS_OF, MODEL_VERSION, RAW, summarize, widen, wsummary, wquantile
from .data import D
from .level import (LevelProcess, WEIGHTS, SCENARIOS, SCENARIO_DEFS, COMPUTE, KAPPA_MEAN, KAPPA_SD, HAIRCUT, BIAS_H_CAP, DT,
                    bias_beta, bias_beta_se, crossing_date, date_summary, bias_shape, block_betas, pooled_beta, TREND_SCENARIOS)
from .trend import break_analysis, records, NU
from . import backtest as bt
from . import irt, aeci, links as lk, predict as pr, families as fam

T_NOW = yr(AS_OF)
N_PATHS = 40000
B_BT = 30
B_LIVE = 150
INTERNAL_AECI = 178.78
REASONING_START = 2024.15
ENTITIES = ["opus", "sonnet", "haiku", "fable_mythos"]
ENT_FAMILY = {"opus": "opus", "sonnet": "sonnet", "haiku": "haiku", "fable_mythos": "fable"}
QUARTERS = [q for q in (f"{y}-{md}" for y in range(2026, 2031) for md in ("03-31", "06-30", "09-30", "12-31")) if yr(q) > T_NOW]
TQ = np.array([yr(q) for q in QUARTERS])
STALE_DAYS = 183
MIN_FOLDS, MIN_COV80 = 4, 0.7          # a benchmark prediction is graded only with this much backtest support
WITHDRAWN = {"gdpval_aa": "the linear Elo link over-extrapolates (the six highest-ECI models sit about 250 Elo below it; the backtest "
                          "over-predicted in 10 of 12 folds; v2.0's 80% lower bounds exceeded the best score ever recorded)"}
EXPIRY_MONTHS = 18


def log(msg, t0):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def _rows(df, cols=None, nd=3):
    df = df if cols is None else df[[c for c in cols if c in df]]
    return [{k: (round(float(v), nd) if isinstance(v, (float, np.floating)) else v) for k, v in r.items()} for r in df.to_dict("records")]


def _factor_at(cal_by_h, h, lv):
    """Calibration factor at horizon h: linear interpolation between backtested horizons,
    held flat outside them."""
    hs = sorted(cal_by_h)
    tag = {0.5: "factor50", 0.8: "factor80", 0.95: "factor95"}[lv]
    return float(np.interp(h, hs, [cal_by_h[k][tag] for k in hs]))


def _bands(x, w, cal_by_h=None, nd=2, thr=None):
    out = []
    for j in range(x.shape[1]):
        s = wsummary(x[:, j], w, 4)
        row = dict(date=QUARTERS[j])
        if cal_by_h is not None:
            h = TQ[j] - T_NOW
            m, lo_w, hi_w = s["median"], 0.0, 0.0
            row["median"] = round(m, nd)
            for lv, tag in ((0.5, "50"), (0.8, "80"), (0.95, "95")):
                f = _factor_at(cal_by_h, h, lv)
                lo_w, hi_w = max(lo_w, f * (m - s["lo" + tag])), max(hi_w, f * (s["hi" + tag] - m))
                row["lo" + tag], row["hi" + tag] = round(m - lo_w, nd), round(m + hi_w, nd)
        else:
            row.update({k: round(v, nd) for k, v in s.items()})
        if thr is not None:
            row["median_beyond_measured_scale"] = bool(row["median"] > thr)
            row["hi80_beyond_measured_scale"] = bool(row["hi80"] > thr)
            row["share_of_paths_beyond_measured_scale"] = round(float(np.sum(w[x[:, j] > thr]) / np.sum(w)), 3)
        out.append(row)
    return out


def evidence_average(rc, ba_anth, ba_all):
    """An UNWEIGHTED average of three unlike pieces of evidence on whether the step-up
    reverts. Shown for transparency; it is a judgement device, not an estimate, and the
    three inputs disagree wildly."""
    acc = rc[rc.apparent_acceleration == 1]
    ep = {}
    for name, grp in (("eci", ["eci_all"]), ("metr", ["metr_TH1.0", "metr_TH1.1"])):
        sh = [acc[acc.series == s].outcome.value_counts(normalize=True).to_dict() for s in grp if (acc.series == s).any()]
        if sh:
            ep[name] = {k: float(np.mean([s.get(k, 0.0) for s in sh])) for k in ("reverted", "held", "accelerated_again")}
    cnt = {k: sum(e[k] for e in ep.values()) for k in ("reverted", "held", "accelerated_again")}
    n = sum(cnt.values())
    lap = {k: (v + 1) / (n + 3) for k, v in cnt.items()}
    p_ref = lap["reverted"]
    p_anth = ba_anth["jump"]["bic_weight"] + ba_anth["linear"]["bic_weight"]
    p_all = ba_all["jump"]["bic_weight"] + ba_all["linear"]["bic_weight"] + (ba_all["hinge"]["bic_weight"] if ba_all["hinge"]["ratio"] < 1.15 else 0.0)
    p_rev = float(np.mean([p_ref, p_anth, p_all]))
    sc = lap["accelerated_again"] / (lap["accelerated_again"] + lap["held"])
    w = {"slowdown": 0.0, "reversion": round(p_rev, 4), "hold": round((1 - p_rev) * (1 - sc), 4),
         "compounding": round((1 - p_rev) * sc, 4), "explosive": 0.0}
    w["hold"] = round(1 - w["reversion"] - w["compounding"], 4)
    return w, dict(independent_episodes=len(ep), episodes=ep, laplace=lap, p_revert_reference_class=round(p_ref, 3),
                   p_revert_anthropic_public_bic=round(p_anth, 3), p_revert_all_lab_bic=round(p_all, 3),
                   p_revert_unweighted_mean=round(p_rev, 3), compounding_share_of_persisting=round(sc, 3),
                   warning="Three numbers that span 0.01 to 0.86 are averaged with equal weight; slowdown and explosive are zero "
                           "only because the sample contains no such episode. Not an estimate.")


def run(full=False):
    t_start = time.time()
    R = {}
    d = D()
    edi = pd.read_csv(RAW / "eci_benchmark_difficulty.csv")
    pub = d.eci_models.set_index("model_id").eci
    meta = d.meta.set_index("benchmark")

    # ------------------------------------------------------------- 1. the level process, backtested
    mf = bt.machine_folds(d, B_BT)
    blocks = block_betas(mf["all"] + mf["anthropic"])
    pool = pooled_beta(blocks)
    BETA, BETA_SD = pool["mu"], pool["predictive_sd"]
    mach, cal_h = {}, {}
    for which in ("all", "anthropic"):
        Rm, tab, cal = bt.score_machine(mf[which], mf)
        b_hat, _ = bias_beta(mf[which])
        se, nblk = bias_beta_se(mf[which], mkrng("beta-" + which))
        tested = Rm[(Rm.variant == "published_config") & (Rm.beta != 0)]
        tested_raw = Rm[(Rm.variant == "raw") & (Rm.beta != 0)]
        cal_h[which] = cal
        mach[which] = dict(table=tab, calibration={str(h): c for h, c in cal.items()}, n_folds=len(mf[which]),
                           n_origins=len({f["t0"] for f in mf[which]}), n_distinct_outcomes=len({f["y"] for f in mf[which]}),
                           unpooled_beta=dict(beta_per_year=round(b_hat, 2), block_bootstrap_se=round(se, 2), n_blocks=nblk),
                           correction_test=dict(n_folds_with_a_rolling_correction=int(len(tested)),
                                                n_distinct_outcomes=int(tested.y.nunique()) if len(tested) else 0,
                                                horizons=sorted(tested.h.unique().tolist()) if len(tested) else [],
                                                mae_raw=None if not len(tested) else round(float(tested_raw.err.abs().mean()), 2),
                                                mae_published_config=None if not len(tested) else round(float(tested.err.abs().mean()), 2)),
                           per_fold=[dict(t0=round(f["t0"], 5), h=f["h"], t=round(f["T"], 5), y=f["y"], cutoff=round(f["cutoff"], 5),
                                          err_raw=round(f["err_raw"], 2), beta_rolling=round(f["beta_rolling"], 2)) for f in mf[which]])
    g_end27 = float(bias_shape(yr("2027-12-31") - T_NOW))
    R["machine_backtest"] = dict(
        design="The projection code itself (level.LevelProcess.paths, central scenario weights) run at monthly historical origins "
               "and scored on the running-max public ECI 0.5, 1.0 and 1.5 years later. 'raw' has no correction. 'published_config' "
               "is the configuration the live forecast uses: the pooled correction, learned only from folds (of either series) whose "
               "target precedes the origin, added on trend-continuation paths. Calibration factors are fitted on 'published_config'. "
               "Folds overlap heavily; origins span 2024-07 to 2026-05, one regime of rising pace. The scenario weights are today's "
               "prior, so this is not a test of the weights.",
        all_lab=mach["all"], anthropic=mach["anthropic"],
        correction=dict(
            blocks=[dict(series=b_["series"], block=b_["block"], n=b_["n"], beta=round(b_["beta"], 2), se=round(float(np.sqrt(b_["var"])), 2)) for b_ in blocks],
            unshrunk=dict(anthropic=mach["anthropic"]["unpooled_beta"]["beta_per_year"], all_lab=mach["all"]["unpooled_beta"]["beta_per_year"]),
            pooled=dict(mu=round(pool["mu"], 2), se=round(pool["se"], 2), between_block_sd=round(pool["tau"], 2),
                        predictive_sd=round(pool["predictive_sd"], 2), n_blocks=pool["n_blocks"]),
            value_used=round(BETA, 2), sd_used=round(BETA_SD, 2),
            shape="level adjustment = beta x g(h): g = h^2 up to 0.5 yr, 0.25 + (h-0.5) - (h-0.5)^2/2 up to 1.5 yr, 0.75 after "
                  "(the correction rate tapers in from zero, peaks at 0.5 yr, and is zero from 1.5 yr)",
            applies_to=[SCENARIOS[i] for i in TREND_SCENARIOS],
            not_applied_to=["slowdown", "reversion", "non-Anthropic frontier"],
            size_at_end_2027=round(BETA * g_end27, 2), permanent_size_after_1_5_years=round(BETA * 0.75, 2),
            thin_test="A rolling (out-of-sample) correction exists for only %d Anthropic folds with %d distinct outcomes, at horizons %s yr (mostly six months). "
                      "On those it lowered MAE from %s to %s; on the all-lab series the same correction changed MAE from %s to %s over %d folds. "
                      "Nothing at 1.5 years has been scored with a correction, and at one year only three overlapping folds have."
                      % (mach["anthropic"]["correction_test"]["n_folds_with_a_rolling_correction"], mach["anthropic"]["correction_test"]["n_distinct_outcomes"],
                         mach["anthropic"]["correction_test"]["horizons"], mach["anthropic"]["correction_test"]["mae_raw"],
                         mach["anthropic"]["correction_test"]["mae_published_config"], mach["all"]["correction_test"]["mae_raw"],
                         mach["all"]["correction_test"]["mae_published_config"], mach["all"]["correction_test"]["n_folds_with_a_rolling_correction"]),
            why_pooled="Trend fits ran low on both frontiers over 2024-26, but block slopes range from %.1f to %.1f and the series disagree; "
                       "a random-effects mean across all blocks is used instead of the Anthropic-only estimate, with the between-block "
                       "spread carried as its uncertainty." % (min(b_["beta"] for b_ in blocks), max(b_["beta"] for b_ in blocks))))
    log(f"machine backtest: {len(mf['all'])}+{len(mf['anthropic'])} folds; pooled beta {BETA:.2f} (sd {BETA_SD:.2f}); unshrunk anth {mach['anthropic']['unpooled_beta']['beta_per_year']}", t_start)

    # ------------------------------------------------------------- 2. release folds (all folds)
    rel, benchbt = bt.release_folds(d, B_BT, mf)
    rel2, _ = bt.release_folds(d, B_BT, mf, with_bench=False, variants=False, seed_tag="-mc")     # Monte Carlo noise check
    meths = ["model", "model_date_unknown", "prev_plus_slope", "prev_plus_slope_date_unknown", "prev_in_family", "family_mean_step",
             "trailing_12m_linear", "all_history_linear"] + sorted(m for m in rel.method.unique() if m.startswith("variant"))
    by_lead = bt.summary_by_lead(rel, meths)
    rp = mkrng("paired")
    pairs = []
    for ld in bt.LEADS:
        for b in bt.BASELINES:
            p = bt.paired(rel, "model", b, ld, rp)
            if p:
                pairs.append(dict(p, date="given"))
        p = bt.paired(rel, "model_date_unknown", "prev_plus_slope_date_unknown", ld, rp)
        if p:
            pairs.append(dict(p, date="not given"))
    mc = []
    for ld in bt.LEADS:
        a = rel[(rel.method == "model") & (rel.lead == ld)].set_index("fold").err
        b2 = rel2[(rel2.method == "model") & (rel2.lead == ld)].set_index("fold").err
        mc.append(dict(lead_years=ld, rmse_seed_a=round(float(np.sqrt((a ** 2).mean())), 2), rmse_seed_b=round(float(np.sqrt((b2 ** 2).mean())), 2)))
    m0 = rel[(rel.method == "model") & (rel.lead == 0)]
    mu = rel[(rel.method == "model_date_unknown")]
    cal0 = bt.rolling_calibration(m0)
    calu = bt.rolling_calibration(mu, min_prior=4)
    f_ability = {lv: max(bt.factors(cal0)[lv], bt.factors(calu)[lv]) for lv in (0.5, 0.8, 0.95)}
    steps_hist = d.claude().sort_values("t").groupby("family").eci.diff().dropna()
    R["release_backtest"] = dict(
        design="Folds are (Claude release, lead) for leads of 0, 3 and 6 months; origin = release date minus lead; everything is "
               "refitted on models released strictly before the origin. ALL folds are reported, including the first release of a "
               "family (Fable 5), which the model places on the record line. 'model' is told the release date; "
               "'model_date_unknown' is given only the family's cadence up to the origin and is the relevant test of the live "
               "forecasts at leads above zero. A baseline is scored on every fold where it is defined (n is shown per row).",
        n_folds_by_lead={str(ld): int(((rel.method == "model") & (rel.lead == ld)).sum()) for ld in bt.LEADS},
        summary_by_lead=by_lead, paired_differences=pairs, monte_carlo_noise=mc,
        verdict="On all folds the model's point forecast is not distinguishable from 'previous-in-family + trailing-12-month Anthropic "
                "record slope x elapsed time' at any lead (every paired interval spans zero, or favours the baseline). That baseline "
                "is therefore the core of the model: next = predecessor + recent record-line gain. What the model adds is a "
                "predictive distribution with tested coverage, a positive-step constraint, and consistency with the long-range "
                "paths. It does clearly beat 'previous model in family', 'family mean step' and the two all-lab trend lines.",
        what_n_supports="Lead 0 (n=%d) supports an error of roughly 2.5 ECI points RMSE with the date known. Three months ahead (n=%d, "
                        "%d with the date unknown) supports 'about the same, perhaps 3'. Six months ahead (n=%d, %d date-unknown) supports "
                        "nothing firmer than 'errors of 4-6 points happened and every one was an under-prediction'. No fold has a lead "
                        "beyond six months: the Haiku forecast (median lead about eight months) is outside anything tested."
                        % (len(m0), int(((rel.method == "model") & (rel.lead == 0.25)).sum()), int(((mu.lead == 0.25)).sum()),
                           int(((rel.method == "model") & (rel.lead == 0.5)).sum()), int((mu.lead == 0.5).sum())),
        calibration=dict(date_given_lead_0=cal0, date_unknown_leads_3_6_months=calu, factors_used={str(k): v for k, v in f_ability.items()},
                         rule="Per level, the larger of the two sets' factors; never below 1."),
        by_family={f: bt.scores(g) for f, g in m0.groupby("family")},
        within_family_steps=dict(n=int(len(steps_hist)), n_negative=int((steps_hist < 0).sum()), min=round(float(steps_hist.min()), 2),
                                 median=round(float(steps_hist.median()), 2)),
        per_release=_rows(rel[~rel.method.str.startswith("variant")],
                          ["fold", "model_id", "family", "lead", "t0", "t", "cutoff", "first_of_family", "y", "method", "median", "err",
                           "lo50", "hi50", "lo80", "hi80", "lo95", "hi95", "beta"], nd=5))
    log(f"release backtest: {len(m0)}/{int(((rel.method == 'model') & (rel.lead == 0.25)).sum())}/{int(((rel.method == 'model') & (rel.lead == 0.5)).sum())} folds", t_start)

    # ------------------------------------------------------------- 3. vintage IRT (deterministic, cached in data/)
    claude = d.claude()
    dates = sorted({round(float(t - ld) - bt.STRICT_EPS, 4) for t in claude.t if t >= 2024.45 for ld in bt.LEADS} |
                   {round(float(t), 4) for t in claude.t if t >= 2024.45})
    vint = irt.vintage_abilities(dates, pub, full)
    cfull, _ = irt.fit_irt(irt.load_inputs(), pub)
    x = pd.DataFrame({"mine": cfull, "pub": pub}).dropna()
    rel_v, _ = bt.release_folds(d, B_BT, mf, abilities_by_date=vint, with_bench=False, variants=False)
    cmp_ = {}
    for ld in bt.LEADS:
        for meth in ("model", "prev_plus_slope"):
            v = rel_v[(rel_v.method == meth) & (rel_v.lead == ld)].set_index("fold")
            p = rel[(rel.method == meth) & (rel.lead == ld)].set_index("fold")
            idx = v.index.intersection(p.index)
            if len(idx):
                cmp_.setdefault(str(ld), {})[meth] = dict(n=len(idx), n_published_folds=int(len(p)), vintage=bt.scores(v.loc[idx]), published=bt.scores(p.loc[idx]))
    mv = rel_v[rel_v.method == "model"].set_index("fold")
    mp_ = rel[rel.method == "model"].set_index("fold")
    com = mv.index.intersection(mp_.index)
    R["irt_refit_check"] = dict(
        design="Own least-squares 2PL refit of Epoch's benchmark-level inputs, refitted at every fold origin on models released on "
               "or before that date, mapped to ECI units by a monotone alignment to the published ECI of those same models. The "
               "release backtest is rerun with history from a strict-origin vintage (models released before the origin; in v2.0 the "
               "lead-0 vintage included the target) and the target's actual from the release date's vintage. The fit is deterministic; the vintages are stored in data/irt_vintages.csv.gz, which is committed and "
               "covered by the input hash (run.py --full rebuilds it; a test recomputes two vintages and compares).",
        v1_bug="In v1 a date-rounding slip excluded the target from its own vintage on a clean cache, which is why the reviewer's "
               "clean run found 18 folds instead of 33. Fixed (tolerance on 'on or before'); numbers below are from a clean rebuild.",
        full_data_reproduction=dict(n_models=int(len(x)), rmse_all=round(float(np.sqrt(((x.mine - x.pub) ** 2).mean())), 2),
                                    rmse_above_140=round(float(np.sqrt(((x.mine - x.pub)[x.pub > 140] ** 2).mean())), 2),
                                    corr=round(float(x.corr().iloc[0, 1]), 4)),
        target_shift=dict(n=int(len(com)), mean_abs=round(float((mv.loc[com, "y"] - mp_.loc[com, "y"]).abs().mean()), 2),
                          max_abs=round(float((mv.loc[com, "y"] - mp_.loc[com, "y"]).abs().max()), 2)),
        comparison_by_lead=cmp_, n_vintages=len(dates),
        caveat="Scores in Epoch's input file are today's collection; a score measured after the origin for a model released before "
               "it cannot be removed (no timestamps).")
    log("vintage IRT backtest done", t_start)

    # ------------------------------------------------------------- 4. break analysis, reference class
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
    rs_a, rs_l = d.series("anthropic"), d.series("all")
    rs_a.start = rs_l.start = REASONING_START
    ta, ya, _ = rs_a.published_records()
    tl, yl, _ = rs_l.published_records()
    ba_anth, _ = break_analysis(ta, ya, T_NOW)
    ba_all, _ = break_analysis(tl, yl, T_NOW)
    a6 = d.aeci("fable5.2")
    a6 = a6[a6.value_type.isin(["printed", "figure_read", "anchor_by_definition"])]
    a6p = a6[a6.t.notna()].sort_values("t")
    ba_aeci, _ = break_analysis(a6p.t.to_numpy(), a6p.value.to_numpy(), T_NOW)
    ai = a6.copy()
    ai["ti"] = [yr(v) if isinstance(v, str) else np.nan for v in ai.internal_date]
    ai.loc[ai.model_id.str.contains("internal"), "ti"] = yr("2026-09-26")
    ai = ai[ai.ti.notna()].sort_values("ti")
    ix = records(ai.ti.to_numpy(), ai.value.to_numpy())
    ba_aeci_int, _ = break_analysis(ai.ti.to_numpy()[ix], ai.value.to_numpy()[ix], T_NOW)

    # ------------------------------------------------------------- 5. the live level process (one set of paths)
    r = mkrng("live")
    lpA = LevelProcess(d.series("anthropic"), T_NOW + 1e-6, B_LIVE, r)
    lpL = LevelProcess(d.series("others"), T_NOW + 1e-6, B_LIVE, mkrng("live-all"))     # the non-Anthropic frontier, fitted on its own records
    W = dict(WEIGHTS)
    ev_w, ev_detail = evidence_average(rc, ba_anth, ba_all)
    W["unweighted_evidence_average"] = ev_w
    PA = lpA.paths(N_PATHS, W["central"], 2031.0)
    PL = lpL.paths(N_PATHS, W["central"], 2031.0, scn=PA["scn"])
    clipA, clipL = lpA.clip_share, lpL.clip_share
    scn = PA["scn"]
    # The pooled correction: trend-continuation scenarios only, Anthropic line only, tapered in and out (level.bias_shape).
    # It is part of the level from here on, so the next-model layer and the projection carry exactly the same term.
    betaA = (BETA + BETA_SD * r.standard_normal(N_PATHS)) * np.isin(scn, TREND_SCENARIOS)
    PA["level_uncorrected"] = PA["level"].copy()
    PA["level"] = PA["level"] + betaA[:, None] * bias_shape(PA["tm"] - PA["tm"][0])[None, :]
    wts = {wn: np.array([wv[SCENARIOS[s]] / max(W["central"][SCENARIOS[s]], 1e-12) for s in scn]) for wn, wv in W.items()}
    for wn in wts:
        wts[wn] = wts[wn] / wts[wn].sum()
    one = {s: (scn == i).astype(float) for i, s in enumerate(SCENARIOS)}
    sd = lpA.draws(6000)
    ratio = sd[1] / np.maximum(sd[2], 1e-9)
    R["trend"] = dict(
        note="Record-setting releases since Claude 3 Opus (March 2024). 'hinge' = piecewise linear with unknown changepoint; 'jump' = "
             "constant slope with a one-time level shift. BIC weights compare four forms on the published point estimates.",
        anthropic_public_eci=ba_anth, all_lab_public_eci=ba_all, aeci_nov6_public_dates=ba_aeci,
        aeci_nov6_internal_dates_with_internal_model=ba_aeci_int,
        level_process=dict(
            forms=["trailing-12-month line", "trailing-24-month line", "hinge (last segment)"], weights="equal",
            anthropic=dict(level_now=summarize(sd[0]), recent_slope=summarize(sd[1]), pre_break_slope=summarize(sd[2]),
                           total_slope_ratio=summarize(ratio, 3), annual_pace_sd=round(lpA.sigma_w, 2), record_scatter=round(lpA.S, 2),
                           share_of_slope_draws_clipped=round(clipA, 3), era_start=lpA.era_start),
            all_lab=dict(level_now=summarize(lpL.draws(6000)[0]), recent_slope=summarize(lpL.draws(6000)[1]),
                         annual_pace_sd=round(lpL.sigma_w, 2), share_of_slope_draws_clipped=round(clipL, 3), era_start=lpL.era_start,
                         series="non-Anthropic records (v2.1; the all-lab frontier is the larger of this line and Anthropic's)",
                         note="Fitted to the other labs' records; no step-up is found, so 'pre-break' pace is at most the recent pace "
                              "and 'reversion' nearly coincides with 'hold' for this series. No under-prediction correction is applied "
                              "to it. A sizeable share of its slope draws hit the clipping bounds (reported above)."),
            bootstrap="Subsample bootstrap: each replicate keeps the distinct members of a with-replacement resample of models "
                      "(about 63%) and one of Epoch's 500 joint posterior draws; record sets are recomputed per replicate. Slope "
                      "draws outside 4-60 (recent) or 4-40 (pre-break) ECI/yr are clipped to the bound; the share is reported.",
            like_for_like="The total slope ratio above (recent / pre-break, public ECI, Anthropic) is the quantity comparable to "
                          "METR's 1.9x and the card's 1.88x, which are total-slope ratios on AECI. The algorithmic multiplier m "
                          "used inside the scenarios is a different quantity (it excludes the compute term) and is larger."),
        records_anthropic=[dict(t=round(float(t), 3), eci=float(y)) for t, y in zip(lpA.rt, lpA.ry)],
        records_all_lab=[dict(t=round(float(t), 3), eci=float(y)) for t, y in zip(lpL.rt, lpL.ry)])

    # scale identification: where today's public basket stops separating models
    ed = edi.assign(a90=edi.edi + 2.197 / edi.estimated_slope_scaled)       # ECI at which each benchmark is 90% solved (Epoch's item parameters)
    lvl80, lvl90 = float(np.quantile(ed.a90, 0.80)), float(np.quantile(ed.a90, 0.90))
    beyond = lvl90
    mpg = aeci.Mapping(d, 400, mkrng("mapping"))
    R["scale"] = dict(
        beyond_measured_scale_above_eci=round(beyond, 1),
        range_eci=[round(lvl80, 1), round(lvl90, 1)],
        range_meaning="public ECI at which 80%% / 90%% of the %d benchmarks in Epoch's current basket are at least 90%% solved" % len(ed),
        share_of_basket_90pct_solved_at_frontier_now=round(float((ed.a90 <= lpA.F0).mean()), 2),
        display_cap_eci=float(np.ceil((lvl90 + 30) / 10) * 10),
        rule="For each benchmark in Epoch's basket, the ECI at which it is 90% solved is difficulty + 2.2/slope (Epoch's item "
             "parameters; all benchmarks, no slope cut-off). The range reported runs from the level where 80% of the basket is that "
             "far solved to the level where 90% is; the upper end is the one value the page shades from (the lower end is already "
             "close to today's frontier because the basket still holds many old, solved benchmarks). Above the upper end only about "
             "one benchmark in ten still separates models, so ECI values are extrapolations of the scale itself. "
             "Bands above it are kept in the data and flagged.",
        hardest_benchmarks=[dict(benchmark=b_.benchmark_name, difficulty=round(b_.edi, 1), slope=round(b_.estimated_slope_scaled, 3), eci_at_90pct=round(b_.a90, 1))
                            for b_ in ed.sort_values("a90", ascending=False).head(6).itertuples()],
        frontier_now=float(lpA.F0))
    thr = beyond

    # ------------------------------------------------------------- 6. families, AECI, links
    hist = d.claude()
    ht = fam.offsets_table(hist, lpA.ref, T_NOW + 1)
    ff = fam.fit_families(ht)
    c_g, s_g, n_g, min_step = fam.gain_stats(hist, lpA.ref)
    R["families"] = dict(
        gain_model=dict(median_log_ratio=round(c_g, 3), log_sd=round(s_g, 3), n_steps=n_g, min_historical_step=min_step,
                        measurement_sd=round(lpA.meas_sd, 2),
                        note="Next = predecessor + max(line gain, %.1f) x exp(c + s z) + measurement noise. The latent step is "
                             "positive by construction (0 of %d historical within-family steps were negative); the published "
                             "score can still fall below the predecessor through measurement noise alone." % (fam.GAIN_FLOOR, n_g)),
        offsets_table=[dict(family=f, n=int(v["n"]), unpooled_mean=round(v["mean"], 2), pooled_mean=round(v["pooled"], 2),
                            pooled_se=round(v["pooled_se"], 2), last_offset=round(v["last"], 2), last_eci=round(v["last_eci"], 2))
                       for f, v in ff["fam"].items()],
        offsets_note="Offsets from the record line (pooled across families by empirical Bayes) are used only for the family paths "
                     "after 2027; the next-model forecast uses the gain model. A 'record line + pooled offset' predictor was "
                     "tested on all folds and is not better (see variants in the release backtest).",
        offsets=_rows(ht, ["model_id", "family", "t", "eci", "offset"]),
        twin="Fable and Mythos are one underlying model. They are forecast as one entity, 'fable_mythos': one release-date "
             "distribution (the forecaster's Fable distribution), one ability draw, one set of benchmark predictions. Public ECI "
             "attaches to the Fable label, AECI to the Mythos label.")
    oc = aeci.OwnCard(d)
    dr = aeci.Drift(d)
    sel = float(np.mean([h["sse"] > o["sse"] for h, o in zip(mpg.draws["hinge"], mpg.draws["offset"])]))
    p_offset = float(np.clip(sel, 0.2, 0.8))
    est = d.index[(d.index.scale == "aeci") & (d.index.fit == "fable5.2_repo_rescaled")].merge(d.models[["model_id", "eci"]], on="model_id")
    est_chk = [dict(model_id=x_.model_id, eci=x_.eci, site_rescaled_aeci=x_.value,
                    mapped_hinge=round(float(mpg.apply_point(np.array([x_.eci]), "hinge")[0]), 2),
                    mapped_offset=round(float(mpg.apply_point(np.array([x_.eci]), "offset")[0]), 2)) for x_ in est.itertuples()]
    tab = mpg.tab
    # leave-one-out error of the mapping (each overlap model predicted from the others)
    loo = []
    for i in range(len(tab)):
        keep = np.arange(len(tab)) != i
        errs = []
        for form in ("hinge", "offset"):
            try:
                p_ = aeci._fit(tab.eci.to_numpy()[keep], tab.aeci.to_numpy()[keep], form)
                xx = max(tab.eci.iloc[i] - p_["k"], 0.0) if form == "hinge" else float(tab.eci.iloc[i] > p_["k"])
                errs.append(tab.aeci.iloc[i] - (p_["a0"] + tab.eci.iloc[i] + p_["c"] * xx))
            except TypeError:
                errs.append(np.nan)
        loo.append(dict(model_id=tab.model_id.iloc[i], err_hinge=round(float(errs[0]), 2), err_offset=round(float(errs[1]), 2)))
    loo_mix = np.array([p_offset * l["err_offset"] + (1 - p_offset) * l["err_hinge"] for l in loo])
    res_extra = np.array([e["site_rescaled_aeci"] - (p_offset * e["mapped_offset"] + (1 - p_offset) * e["mapped_hinge"]) for e in est_chk])
    map_sd = float(np.sqrt(np.mean(np.concatenate([loo_mix[np.isfinite(loo_mix)], res_extra]) ** 2)))
    for f_ in ("hinge", "offset"):
        mpg.point[f_]["sd"] = map_sd
    multi = dr.rows[(dr.rows.fit_from == "opus5.5") & (dr.rows.fit_to == "fable5.2")]
    R["aeci"] = dict(
        primary_scale="Public ECI is the modelling scale (256 models, four years, posterior draws, refittable inputs). AECI is "
                      "reported two ways: (1) 'own card', the value Anthropic will print in the model's own system card, which is "
                      "what gets graded and is modelled directly; (2) the November 6 2026 scale, secondary, through a mapping.",
        own_card=dict(table=_rows(oc.tab), summary=oc.summary(), backtest=oc.backtest,
                      method=aeci.OwnCard.__doc__.split("\n\n", 1)[1].replace("\n    ", " ").strip(),
                      label="Judgement-heavy estimate with a wide band. The rolling test (five cards) has RMSE %.1f AECI points; "
                            "the Haiku 5.5 card missed by %.1f." % (oc.rmse, max(abs(b["error"]) for b in oc.backtest)),
                      conditional="Sonnet and Haiku own-card predictions are conditional on Anthropic printing one: the Sonnet 5 "
                                  "card printed no AECI. They expire unresolved if the card has none."),
        nov6_mapping=dict(
            overlap=_rows(tab), forms=mpg.point, p_level_shift_form=round(p_offset, 3), bootstrap_share_level_shift_fits_better=round(sel, 3),
            leave_one_out=loo, leave_one_out_rmse=round(float(np.sqrt(np.nanmean(loo_mix ** 2))), 2), residual_sd_used=round(map_sd, 2),
            held_out_site_rescaled=est_chk,
            caveats=["The gap between AECI and public ECI tracks how recent the model and the fit are, not the model's level: "
                     "Haiku 5.5 (ECI 160.4) printed 167.11 in its own card. A mapping in level alone under-states Sonnet- and "
                     "Haiku-tier AECI by roughly 2-4 points; the residual sd is set from leave-one-out and held-out errors to cover that.",
                     "The level-shift threshold is not identified between ECI 156.3 and 164.1 (no model in between).",
                     "Thirteen models on one fit. Secondary quantity."]),
        refits=dict(matrix=_rows(dr.piv.reset_index()), per_refit=_rows(dr.trans.reset_index().rename(columns={"mean": "mean_delta", "count": "n_models"})),
                    across_three_opus55_only_refits=_rows(multi, ["model_id", "delta"]),
                    note="Descriptive only in v2 (the own-card forecast no longer sums refit steps). Three of the seven card-to-card "
                         "transitions are observed for Opus 5.5 alone, read from cards that state no fit; over those three refits "
                         "combined, the other models moved +3.8 to +4.5 and Opus 5.5 +5.4. The two large steps coincide with basket "
                         "changes, so steps are not exchangeable draws."))
    e_all, _ = d.ability_table()
    abil = e_all.set_index("model_id").eci
    links, dropped_fit = lk.fit_links(d.bench, d.meta, abil, T_NOW + 1, 300, mkrng("links"), edi)
    # admission rule
    bstat = {}
    for key, g in benchbt.groupby("benchmark"):
        a_ = g[g.method == "anchored"]
        p_ = g[g.method == "prev_in_family"]
        c_ = g[g.method == "curve_level"]
        bstat[key] = dict(n=int(len(a_)), mae_anchored=round(float(a_.err.abs().mean()), 2), mae_curve_level=round(float(c_.err.abs().mean()), 2),
                          mae_prev_in_family=round(float(p_.err.abs().mean()), 2), bias_anchored=round(float(a_.err.mean()), 2),
                          rmse_anchored=round(float(np.sqrt((a_.err ** 2).mean())), 2),
                          cov50=round(float(a_.in50.mean()), 2), cov80=round(float(a_.in80.mean()), 2), cov95=round(float(a_.in95.mean()), 2))
    pooled_cal = bt.rolling_calibration(benchbt[benchbt.method == "anchored"])
    fpool = bt.factors(pooled_cal)
    admitted, excluded, sat_statements, tier = {}, [], [], {}
    last_date = d.bench.groupby("benchmark").release_date.max()
    for key in meta.index:
        title = meta.loc[key, "title"]
        if key not in links:
            excluded.append(dict(benchmark=key, title=title, reason="too thin: " + dict(dropped_fit).get(key, "no fit")))
            continue
        l = links[key]
        st = bstat.get(key, dict(n=0))
        age = (pd.Timestamp(AS_OF) - pd.Timestamp(last_date[key])).days
        latest = d.bench[(d.bench.benchmark == key) & d.bench.family.isin(["opus", "sonnet", "haiku", "fable"])].sort_values("t").groupby("family").tail(1)
        fr_f = {r_.family: float((r_.value - l.lo) / (l.hi - l.lo)) for r_ in latest.itertuples()} if l.kind == "bounded" else {}
        if age > STALE_DAYS:
            excluded.append(dict(benchmark=key, title=title, reason=f"stale: newest scored model was released {last_date[key]} ({age} days before {AS_OF})"))
            continue
        if l.kind == "bounded" and float((l.y.max() - l.lo) / (l.hi - l.lo)) >= 0.9:
            sat_statements.append(dict(benchmark=key, title=title, best_observed=round(float(l.y.max()), 2), ceiling=round(float(l.hi), 2),
                                       ceiling_estimated=l.ceiling_estimated, group=meta.loc[key, "group"],
                                       families_at_or_above_90pct=sorted(f_ for f_, v_ in fr_f.items() if v_ >= 0.9),
                                       statement=f"{title} is saturating: the best score so far is {l.y.max():.1f} against a"
                                                 f"{'n estimated' if l.ceiling_estimated else ' nominal'} ceiling of about {l.hi:.1f}. A family already "
                                                 "within a tenth of that ceiling gets no numeric prediction: expect its next model at or just "
                                                 "below the ceiling, with differences inside the noise."))
            if not fr_f or min(fr_f.values()) >= 0.9:
                excluded.append(dict(benchmark=key, title=title, reason="saturated: every family's latest score is at or above 90%% of the %s ceiling (best %.1f, ceiling %.1f)"
                                     % ("estimated" if l.ceiling_estimated else "nominal", l.y.max(), l.hi)))
                continue
        if key in WITHDRAWN:
            excluded.append(dict(benchmark=key, title=title, reason="withdrawn: " + WITHDRAWN[key]))
            continue
        if st["n"] >= MIN_FOLDS and st["mae_anchored"] > st["mae_prev_in_family"]:
            excluded.append(dict(benchmark=key, title=title, reason=f"no skill: anchored MAE {st['mae_anchored']} vs previous-in-family "
                                 f"{st['mae_prev_in_family']} on {st['n']} folds"))
            continue
        hugging = bool(l.kind == "bounded" and l.ceiling_estimated and (l.hi - l.y.max()) < 0.02 * (l.hi - l.lo))
        fails = []
        if st["n"] < MIN_FOLDS:
            fails.append(f"{st['n']} backtest folds (needs {MIN_FOLDS})")
        else:
            if st["cov80"] < MIN_COV80:
                fails.append(f"80% coverage {st['cov80']} (needs {MIN_COV80})")
            if abs(st["bias_anchored"]) > 0.5 * st["rmse_anchored"]:
                fails.append(f"bias {st['bias_anchored']} is more than half the RMSE {st['rmse_anchored']}")
        if meta.loc[key, "group"] != "site":
            fails.append("no resolvable source (not a site chart; arena ratings and outside indices are read at mixed snapshots)")
        if hugging:
            fails.append("estimated ceiling %.1f merely hugs the best observed score %.1f" % (l.hi, l.y.max()))
        tier[key] = dict(tier="indicative" if fails else "graded", reasons=fails, hugging_ceiling=hugging)
        admitted[key] = "graded" if not fails else "indicative: " + "; ".join(fails)
    excluded.append(dict(benchmark="terminal_bench_4_0", title="Terminal-Bench 4.0", reason="too thin: scores for five Claude models only, all released Sept-Nov 2026"))
    R["links"] = dict(
        method="Bounded scores follow p = (score - floor)/(ceiling - floor) = sigmoid(a (ability - D)); the ceiling is estimated "
               "(with a bootstrap interval) wherever at least four scores lie above 75% of the nominal range, otherwise the nominal "
               "ceiling is kept. Predictions are ANCHORED: the family's own last score, moved along the link by the predicted "
               "ability gain (on the logit scale for bounded scores, under a ceiling drawn from its bootstrap and never below "
               "the last score), plus step noise estimated from past within-family steps. A benchmark is published only if it is "
               "not stale (a model scored in the last six months), not saturated (best score below 90% of the ceiling), not too "
               "thin; whether it is graded or only indicative is decided by the admission rule below.",
        table=[dict(l.describe(), title=meta.loc[k, "title"], unit=meta.loc[k, "unit"], group=meta.loc[k, "group"], lo=meta.loc[k, "lo"],
                    hi_nominal=meta.loc[k, "hi"], configuration=meta.loc[k, "configuration"], source=meta.loc[k, "source"],
                    admitted=k in admitted, admission=admitted.get(k), tier=tier.get(k, {}).get("tier"), backtest=bstat.get(k)) for k, l in links.items()],
        admitted=list(admitted), graded=[k for k in admitted if tier[k]["tier"] == "graded"],
        indicative=[k for k in admitted if tier[k]["tier"] == "indicative"], tiers=tier,
        admission_rule="A benchmark with a fitted link is dropped if it is stale (no model scored in six months), withdrawn, shows no skill "
                       "against 'previous in family' on %d or more folds, or every family is saturated. Otherwise it is GRADED only if it has at "
                       "least %d backtest folds, 80%% coverage of at least %.1f, |bias| no more than half its RMSE, a resolvable source (a "
                       "site chart still reporting the family), and an estimated ceiling that does not merely hug the record; every other "
                       "benchmark is INDICATIVE: shown, not graded. Per family, no number is published if the family's latest score or its "
                       "predicted median is at or above 90%% of the ceiling (a saturation statement is given instead), or if the family's "
                       "latest model has no score to anchor on." % (MIN_FOLDS, MIN_FOLDS, MIN_COV80),
        excluded=excluded, saturation_statements=sat_statements,
        calibration_pooled=pooled_cal, calibration_factors={str(k): v for k, v in fpool.items()},
        backtest_design="Same folds as the release backtest (families with an earlier score on the benchmark). 'anchored' is the "
                        "published method; 'curve_level' is v1's method (the fitted curve's level at the predicted ability), kept "
                        "for comparison; baseline: the previous model in the family.",
        backtest_per_release=_rows(benchbt[benchbt.method == "anchored"], ["fold", "model_id", "benchmark", "lead", "t0", "t", "cutoff", "y", "prev",
                                                                             "median", "err", "lo80", "hi80", "lo95", "hi95"]))
    for row in R["links"]["table"]:
        l = links[row["benchmark"]]
        gx = np.linspace(110, 200, 91)
        row["curve"] = dict(eci=[float(v) for v in gx], score=[round(float(v), 3) for v in l.mean(gx)])
        row["points"] = [dict(eci=round(float(a), 2), score=round(float(b), 3)) for a, b in zip(l.x, l.y)]
    log(f"links: admitted {list(admitted)}; excluded {len(excluded)}", t_start)

    # ------------------------------------------------------------- 7. next models (same paths)
    rd = pr.ReleaseDates()
    cur_aeci = {"opus": ("Claude Opus 5.5", 174.78, "printed, Nov 6 fit"), "fable_mythos": ("Claude Mythos 5.2", 177.12, "printed, Nov 6 fit"),
                "sonnet": ("Claude Sonnet 5.5", 173.6, "site estimate on the Nov 6 fit, not Anthropic's"),
                "haiku": ("Claude Haiku 5.5", 167.3, "site estimate on the Nov 6 fit, not Anthropic's")}
    own_prev = {"opus": 169.36, "sonnet": 167.93, "haiku": 167.11, "fable_mythos": 177.12}
    charts = __import__("json").loads((RAW.parents[2] / "data" / "benchmarks.json").read_text())["charts"]
    nxt, open_preds, keep = {}, [], {}
    expires = (pd.Timestamp(AS_OF) + pd.DateOffset(months=EXPIRY_MONTHS)).date().isoformat()
    for ent in ENTITIES:
        f = ENT_FAMILY[ent]
        rr = mkrng("next-" + ent)
        days = rd.sample_days(f, N_PATHS, rr)
        T = T_NOW + days / 365.25
        hf = hist[hist.family == f].sort_values("t")
        last = hf.iloc[-1]
        LT = lpA.at(PA, T)
        gain = LT - PA["L0"] + PA["b_post"] * (T_NOW - last.t)
        theta = fam.predict_step(float(last.eci), gain, c_g, s_g, lpA.meas_sd, rr)
        names = rd.names(f) if ent != "fable_mythos" else {k.replace("Claude Fable", "Claude Fable / Mythos"): v for k, v in rd.names("fable").items()}
        top_name = max(names, key=names.get)
        K = pr.refit_count(rd, f, days, N_PATHS, rr)
        a_own = theta + oc.sample(K, rr)
        forms = (rr.random(N_PATHS) < p_offset).astype(int)
        a_nov6 = mpg.sample(theta, forms, rr)
        eci_s = widen(theta, f_ability)
        cond = []
        for qk in ("q10", "median", "q90"):
            dd = rd.fc["targets"][f]["with_signals"][qk]
            Tq = max(yr(dd), T_NOW)
            g_ = lpA.at(PA, Tq) - PA["L0"] + PA["b_post"] * (T_NOW - last.t)
            cond.append(dict(release_date=dd, quantile=qk, eci_median=round(float(np.median(fam.predict_step(float(last.eci), g_, c_g, s_g, lpA.meas_sd, rr))), 2)))
        benches = {}
        for k in admitted:
            l = links[k]
            pb = d.bench[(d.bench.benchmark == k) & (d.bench.family == f) & d.bench.eci.notna()].sort_values("t")
            series_fam = f
            site = meta.loc[k, "group"] == "site"
            live_series = None
            if site:
                srs = charts[k]["series"].get(series_fam, [])
                live_series = bool(srs) and (pd.Timestamp(AS_OF) - pd.Timestamp(max(p["date"] for p in srs))).days <= STALE_DAYS
            if not len(pb) or pb.model_id.iloc[-1] != last.model_id:
                benches[k] = dict(available=False, graded=False, title=meta.loc[k, "title"], resolvable=False,
                                  reason="the family's latest model has no score on this benchmark to anchor on")
                continue
            sp, tp = float(pb.value.iloc[-1]), float(pb.eci.iloc[-1])
            sdv = bt.step_sd(l, d.bench, hist, k, T_NOW + 1)
            s = l.anchored(theta, tp, sp, sdv, rr)
            sat_line = l.lo + 0.9 * (l.hi - l.lo) if l.kind == "bounded" else np.inf
            if sp >= sat_line or float(np.median(s)) >= sat_line:     # one rule: the latest score OR the predicted median is in the top tenth
                benches[k] = dict(available=False, graded=False, saturated=True, title=meta.loc[k, "title"], resolvable=False,
                                  previous_in_family=dict(model_id=pb.model_id.iloc[-1], value=sp), ceiling=round(float(l.hi), 2),
                                  reason=f"saturated for this family: its latest score ({sp:.1f}) or its predicted next score is within a tenth "
                                         f"of the ceiling (~{l.hi:.1f}); expect the next model at or just below the ceiling")
                continue
            if l.kind == "bounded":
                lo_, hi_ = float(l.lo), float(meta.loc[k, "hi"])
                pz = np.clip((s - lo_) / (hi_ - lo_), 1e-4, 1 - 1e-4)
                ws = widen(np.log(pz / (1 - pz)), fpool, nd=4)
                w_ = {kk: round(float(lo_ + (hi_ - lo_) / (1 + np.exp(-v))), 1) for kk, v in ws.items()}
            else:
                w_ = {kk: round(v, 0) for kk, v in widen(s, fpool).items()}
            w_.pop("mean", None)
            is_graded = bool(tier[k]["tier"] == "graded" and live_series)
            benches[k] = dict(available=True, graded=is_graded, status="graded" if is_graded else "indicative, not graded",
                              not_graded_because=None if is_graded else (tier[k]["reasons"] or ["the site chart no longer reports this family"]),
                              **w_, title=meta.loc[k, "title"], unit=meta.loc[k, "unit"], method="anchored on previous score",
                              previous_in_family=dict(model_id=pb.model_id.iloc[-1], value=sp, eci=tp), step_noise=round(sdv, 3),
                              best_observed_any_model=round(float(l.y.max()), 2), ceiling=None if l.kind != "bounded" else round(float(l.hi), 2),
                              p_below_previous=round(float((s < sp).mean()), 3), resolvable=is_graded,
                              resolution_series=(f"data/benchmarks.json charts.{k}.series.{series_fam}" if site else None))
        nxt[ent] = dict(
            entity=ent, labels=(["Claude Fable", "Claude Mythos"] if ent == "fable_mythos" else [f"Claude {f.capitalize()}"]),
            previous_model=last.model_id if ent != "fable_mythos" else "Claude Fable 5.2 / Claude Mythos 5.2", previous_eci=float(last.eci),
            previous_aeci_own_card=own_prev[ent], previous_aeci_nov6=dict(model=cur_aeci[ent][0], value=cur_aeci[ent][1], kind=cur_aeci[ent][2]),
            predicted_name=top_name, name_probabilities={k: round(v, 3) for k, v in names.items()},
            release_date=rd.summary(f), median_lead_years=round(float(np.median(days)) / 365.25, 2),
            lead_tested=bool(np.median(days) / 365.25 <= 0.5),
            eci=eci_s, aeci_own_card=widen(a_own, f_ability), aeci_nov6_scale=widen(a_nov6, f_ability),
            aeci_own_card_conditional=ent in ("sonnet", "haiku"),
            refits_before_own_card=dict(median=int(np.median(K)), p_one=round(float((K == 1).mean()), 3)),
            eci_given_release_date=cond, benchmarks=benches,
            p_regression_below_predecessor=round(float((theta < last.eci).mean()), 4),
            p_eci_above_current_anthropic_best=round(float((theta > lpA.F0).mean()), 3),
            p_aeci_nov6_at_or_above_internal_model=round(float((a_nov6 >= INTERNAL_AECI).mean()), 3),
            components=dict(line_gain=summarize(gain), step=summarize(theta - last.eci)),
            scale_labels=dict(eci="Fable label (Epoch scores Fable)" if ent == "fable_mythos" else "public ECI",
                              aeci="Mythos label (Anthropic prints AECI for Mythos)" if ent == "fable_mythos" else "AECI"))
        keep[ent] = dict(theta=theta, T=T)
        base = f"{AS_OF}:{MODEL_VERSION}:{ent}:next"
        gfam = "fable" if ent == "fable_mythos" else f
        common = dict(entity=ent, issued=AS_OF, expires=expires, release_rule=f"first {gfam} release after {AS_OF} in data/models.json")
        pick = lambda sdict: {k: sdict[k] for k in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")}
        open_preds.append(dict(id=base + ":eci", family=gfam, quantity="eci_public", unit="ECI points", **common, **pick(eci_s),
                               resolution_source="capability/data/raw/eci_public.csv, row for the model",
                               resolution="First ECI value Epoch publishes for the model (grade.py records the first value it sees in "
                                          "history/first_values.csv and grades against that, not later refits)."))
        afam = "mythos" if ent == "fable_mythos" else f
        open_preds.append(dict(id=base + ":aeci_own_card", family=afam, quantity="aeci_own_card", unit="AECI points", **common,
                               **pick(nxt[ent]["aeci_own_card"]), conditional=ent in ("sonnet", "haiku"),
                               resolution_source="capability/data/raw/aeci_all.csv, row with own_card=1 for the model",
                               resolution="AECI printed for the model in its own system card. If the card prints none, the prediction "
                                          "expires unresolved."))
        for k, bb in benches.items():
            if not bb.get("available") or not bb.get("graded"):
                continue
            open_preds.append(dict(id=base + ":" + k, family=gfam, quantity=k, unit=meta.loc[k, "unit"], **common, **pick(bb),
                                   resolution_source=bb["resolution_series"],
                                   resolution=f"First score charted for the model in that series ({meta.loc[k, 'configuration']})."))
    R["next_models"] = dict(
        entities=nxt, n_draws=N_PATHS, calibration_factors_ability={str(k): v for k, v in f_ability.items()},
        note="Each draw takes a release date from the release forecaster, the record-line gain from the shared level paths (scenario "
             "mixture, central weights, bias term included), a positive step and measurement noise. Anthropic's Fable 5.2 card "
             "prints an unreleased internal model at AECI %.2f (15 benchmarks); it is not used in the fit." % INTERNAL_AECI,
        monte_carlo="%d draws; medians are stable to about 0.05 ECI and interval ends to about 0.2 across seeds." % N_PATHS)
    R["open_predictions"] = open_preds
    log("next-model predictions done", t_start)

    # ------------------------------------------------------------- 8. projection (same paths)
    rp = mkrng("projection")
    lpA.rng = rp
    lpL.rng = mkrng("projection-all")
    f0A, f0L = rp.choice(lpA.F0_draws, N_PATHS), lpL.rng.choice(lpL.F0_draws, N_PATHS)

    def frontier(lp, P, f0):
        out = np.empty((N_PATHS, len(TQ)))
        for j, tq in enumerate(TQ):
            age = np.minimum(lp.ens.sample_age(N_PATHS, lp.rng), tq - T_NOW)
            out[:, j] = lp.at(P, tq - age) + lp.S * lp.rng.standard_t(NU, N_PATHS) / np.sqrt(NU / (NU - 2))
        return np.maximum.accumulate(np.maximum(out, f0[:, None]), axis=1)
    # Anthropic frontier, built so the two layers agree: until both frontier families (Opus, Fable/Mythos) have shipped
    # their next model, the frontier is the best of the standing leader and whichever next models are out, taken from the
    # very draws the next-model layer publishes; after that, later releases follow the record line.
    line = np.empty((N_PATHS, len(TQ)))
    for j, tq in enumerate(TQ):
        age = np.minimum(lpA.ens.sample_age(N_PATHS, rp), tq - T_NOW)
        line[:, j] = lpA.at(PA, tq - age) + lpA.S * rp.standard_t(NU, N_PATHS) / np.sqrt(NU / (NU - 2))
    rel_best = np.full((N_PATHS, len(TQ)), -np.inf)
    for ent in ENTITIES:
        shipped = keep[ent]["T"][:, None] <= TQ[None, :]
        rel_best = np.maximum(rel_best, np.where(shipped, keep[ent]["theta"][:, None], -np.inf))
    both = np.maximum(keep["opus"]["T"], keep["fable_mythos"]["T"])[:, None] <= TQ[None, :]
    next_only = np.maximum(f0A[:, None], rel_best)
    FA = np.maximum.accumulate(np.where(both, np.maximum(next_only, line), next_only), axis=1)
    FO = frontier(lpL, PL, f0L)                          # other labs, fitted on their own records, no correction
    FL = np.maximum(FO, FA)                              # the all-lab frontier is the larger of the two
    agree = []
    for j in range(len(TQ)):
        a_, b_ = wquantile(FA[:, j], wts["central"], [0.5])[0], wquantile(np.maximum.accumulate(next_only, axis=1)[:, j], wts["central"], [0.5])[0]
        agree.append(dict(date=QUARTERS[j], frontier_median=round(a_, 3), next_models_layer_median=round(b_, 3), shortfall=round(b_ - a_, 3),
                          share_paths_both_frontier_families_shipped=round(float(np.sum(wts["central"] * both[:, j])), 3)))
    forms = (rp.random(N_PATHS) < p_offset).astype(int)
    pidx = rp.integers(0, 10 ** 6, N_PATHS)
    AA = mpg.sample(FA, forms, rp, noise=False, pidx=pidx) + map_sd * rp.standard_normal((N_PATHS, 1))
    AA = np.maximum.accumulate(np.where(FA <= lpA.F0 + 0.5, np.maximum(AA, 177.12), AA), axis=1)
    calA, calL = cal_h["anthropic"], cal_h["all"]
    wc = wts["central"]
    proj = dict(quarters=QUARTERS, series={}, scenario_series={})
    proj["series"]["anthropic_frontier_eci"] = _bands(FA, wc, calA, thr=thr)
    proj["series"]["all_lab_frontier_eci"] = _bands(FL, wc, calL, thr=thr)
    proj["series"]["non_anthropic_frontier_eci"] = _bands(FO, wc, calL, thr=thr)
    proj["series"]["anthropic_frontier_aeci_nov6_scale"] = _bands(AA, wc, calA)
    for s in SCENARIOS:
        proj["scenario_series"][s] = dict(anthropic_frontier_eci=_bands(FA, one[s], None, thr=thr),
                                          all_lab_frontier_eci=_bands(FL, one[s], None, thr=thr),
                                          non_anthropic_frontier_eci=_bands(FO, one[s], None, thr=thr),
                                          anthropic_frontier_aeci_nov6_scale=_bands(AA, one[s], None))
    # families: latest released model per family
    fam_cur = {e_: float(hist[hist.family == ENT_FAMILY[e_]].sort_values("t").eci.iloc[-1]) for e_ in ENTITIES}
    proj["families"] = {}
    for ent in ENTITIES:
        f = ENT_FAMILY[ent]
        v = ff["fam"][f]
        wait = (keep[ent]["T"] - T_NOW)
        first = keep[ent]["theta"]
        gap = rd.gap_years(f) * np.exp(0.42 * rp.standard_normal(N_PATHS))
        delta = v["pooled"] + v["pooled_se"] * rp.standard_normal(N_PATHS)
        dz = rp.standard_normal(N_PATHS)
        out = np.empty((N_PATHS, len(TQ)))
        for j, tq in enumerate(TQ):
            h = tq - T_NOW
            a_ = np.minimum(rp.random(N_PATHS) * gap, np.maximum(h - wait, 0.0))
            val = lpA.at(PA, tq - a_) + delta + 1.5 * np.sqrt(h) * dz + np.sqrt(ff["s2"]) * rp.standard_normal(N_PATHS)
            # until the family's next release: its current model; just after it: the predicted next model; later: line + offset
            later = (h - wait) > gap
            out[:, j] = np.where(h <= wait, fam_cur[ent], np.where(later, np.maximum(val, first), first))
        out = np.maximum.accumulate(out, axis=1)
        proj["families"][ent] = dict(eci=_bands(out, wc, calA, thr=thr), current_eci=fam_cur[ent],
                                     note="Latest released model in the family. First step is the next-model forecast; later steps "
                                          "follow the record line at the family's pooled offset and cadence.")
    # scenario table, sensitivity, headline
    scn_tab = []
    tm = PA["tm"]
    iy = {y: int(np.argmin(np.abs(tm - y))) for y in range(2027, 2032)}
    for i, s in enumerate(SCENARIOS):
        mk = scn == i
        row = dict(scenario=s, definition=SCENARIO_DEFS[s], n_paths=int(mk.sum()), carries_correction=i in TREND_SCENARIOS)
        for y in range(2027, 2031):
            pc = PA["level"][mk][:, iy[y + 1]] - PA["level"][mk][:, iy[y]]              # realised gain of the record line over the year,
            pu = PA["level_uncorrected"][mk][:, iy[y + 1]] - PA["level_uncorrected"][mk][:, iy[y]]   # correction included / excluded
            pl = PL["level"][mk][:, iy[y + 1]] - PL["level"][mk][:, iy[y]]
            row[f"pace_anthropic_{y}"] = dict(median=round(float(np.median(pc)), 1), lo80=round(float(np.quantile(pc, 0.1)), 1), hi80=round(float(np.quantile(pc, 0.9)), 1))
            row[f"pace_anthropic_{y}_without_correction_median"] = round(float(np.median(pu)), 1)
            row[f"pace_all_lab_{y}_median"] = round(float(np.median(pl)), 1)
            row[f"x_pre_break_{y}_median"] = round(float(np.median(pc / PA["b_pre"][mk])), 2)
            row[f"share_below_pre_break_{y}"] = round(float(np.mean(pc < PA["b_pre"][mk])), 2)
        row["realised_gain_2027"] = row["pace_anthropic_2027"]
        row["end_2030_anthropic_frontier_median"] = round(wquantile(FA[:, -1], one[s], [0.5])[0], 1)
        row["weights"] = {wn: W[wn][s] for wn in W}
        scn_tab.append(row)
    pcm = PA["level"][:, iy[2028]] - PA["level"][:, iy[2027]]
    pum = PA["level_uncorrected"][:, iy[2028]] - PA["level_uncorrected"][:, iy[2027]]
    mix_pace = dict(realised_gain_2027_median=round(wquantile(pcm, wts["central"], [0.5])[0], 1),
                    without_correction_median=round(wquantile(pum, wts["central"], [0.5])[0], 1),
                    pre_break_slope_median=round(float(np.median(PA["b_pre"])), 1), recent_slope_median=round(float(np.median(PA["b_post"])), 1))
    qi = {q: i for i, q in enumerate(QUARTERS)}
    sens = []
    for wn in W:
        for lab, X, cal in (("anthropic_frontier_eci", FA, calA), ("all_lab_frontier_eci", FL, calL)):
            b = _bands(X, wts[wn], cal, nd=1)
            for q in ("2027-12-31", "2028-12-31", "2030-12-31"):
                sens.append(dict(weighting=wn, series=lab, **b[qi[q]]))
    head = []
    for q in ("2026-12-31", "2027-12-31", "2028-12-31", "2029-12-31", "2030-12-31"):
        j = qi[q]
        head.append(dict(date=q, anthropic_eci=proj["series"]["anthropic_frontier_eci"][j], all_lab_eci=proj["series"]["all_lab_frontier_eci"][j],
                         non_anthropic_eci=proj["series"]["non_anthropic_frontier_eci"][j],
                         share_of_paths_anthropic_leads=round(float(np.sum(wc * (FA[:, j] >= FO[:, j]))), 3),
                         correction_in_record_line_median=round(
                             wquantile(PA["level"][:, min(int(round((TQ[j] - T_NOW) / DT)), len(tm) - 1)], wc, [0.5])[0] -
                             wquantile(PA["level_uncorrected"][:, min(int(round((TQ[j] - T_NOW) / DT)), len(tm) - 1)], wc, [0.5])[0], 2),
                         anthropic_aeci_nov6_scale=proj["series"]["anthropic_frontier_aeci_nov6_scale"][j]))
    # backtested-through: last quarter end within the longest horizon that has at least 10 Anthropic folds (no rounding up)
    hv = max([h for h in bt.MACHINE_H if sum(1 for f in mf["anthropic"] if f["h"] == h) >= 10] or [0.5])
    vt = [q for q in QUARTERS if yr(q) <= T_NOW + hv][-1]
    f_hv = [f for f in mf["anthropic"] if f["h"] == hv]
    bt_caveat = ("'Backtested through %s' means only this: the UNCORRECTED code was run at a %.1f-year horizon from %d overlapping monthly "
                 "origins (%d distinct outcomes) in one regime, and under-predicted in %d of them (mean error %+.1f ECI; 50%% coverage %.2f). "
                 "The corrected configuration that is published has been scored out of sample on only %d overlapping folds with %d distinct "
                 "outcomes, nine of them at six months and none beyond one year." % (vt, hv, len(f_hv), len({f["y"] for f in f_hv}), sum(1 for f in f_hv if f["err_raw"] > 0),
                                         float(np.mean([f["err_raw"] for f in f_hv])), cal_h["anthropic"][hv]["raw_cov50"],
                                         mach["anthropic"]["correction_test"]["n_folds_with_a_rolling_correction"],
                                         mach["anthropic"]["correction_test"]["n_distinct_outcomes"]))
    # reconciliation with research note 1's central path
    j30 = qi["2030-12-31"]
    medL, medA = wquantile(FL[:, j30], wc, [0.5])[0], wquantile(FA[:, j30], wc, [0.5])[0]
    note1 = lpL.F0 + 65.0
    recon = dict(research_note_1_central_gain=65.0, research_note_1_central_level_2030=round(note1, 1),
                 ours_all_lab_median_2030=round(medL, 1), ours_anthropic_median_2030=round(medA, 1),
                 ours_all_lab_by_scenario={s: round(wquantile(FL[:, j30], one[s], [0.5])[0], 1) for s in SCENARIOS},
                 ours_anthropic_by_scenario={s: round(wquantile(FA[:, j30], one[s], [0.5])[0], 1) for s in SCENARIOS},
                 explanation="Research note 1's central path (17, 17, 16, 15 ECI/yr) is the all-lab frontier continuing at Epoch's "
                             "reasoning-era slope. For the all-lab series that is our 'hold' and 'reversion' scenarios, which land "
                             "near it. Our medians are higher for three reasons, in order of size: the Anthropic series has a "
                             "steeper recent slope than the all-lab series, and Anthropic currently holds the frontier; some "
                             "prior weight sits on accelerating scenarios; and an explicit under-prediction term is carried where "
                             "it helped out of sample.")
    # saturation dates for admitted bounded benchmarks (record line reaches 90% of the estimated ceiling)
    sat = []
    for k in admitted:
        l = links[k]
        if l.kind != "bounded":
            continue
        bi = rp.integers(0, len(l.boot), N_PATHS)
        tc = crossing_date(tm, PA["level"], l.boot[bi, 1] + np.log(9.0) / l.boot[bi, 0])
        sat.append(dict(benchmark=k, title=meta.loc[k, "title"], best_observed=round(float(l.y.max()), 1), ceiling=round(float(l.hi), 1),
                        frontier_reaches_90pct_of_ceiling=date_summary(tc, wc, T_NOW),
                        note="Date the record line reaches 90% of the ceiling on the fitted curve; after it the benchmark stops separating models."))
    xl = FL[:, qi["2029-12-31"]] - FL[:, qi["2028-12-31"]]
    r29 = wquantile(xl, wc, [0.1, 0.25, 0.5, 0.75, 0.9])
    j28 = qi["2028-09-30"]
    ros = wsummary(FL[:, j28], wc, 1)
    ext = [dict(source="FutureSearch (2026-11-14)", quantity="Rise in the highest public ECI held by OpenAI/Anthropic/GDM during 2029",
                theirs="p10 11.7, p25 18.5, p50 27.3, p75 42.7, p90 74", ours="p10 %.1f, p25 %.1f, p50 %.1f, p75 %.1f, p90 %.1f" % tuple(r29),
                why="Same right-skewed shape. Ours is lower in the middle because the central compute path slows by 2029."),
           dict(source="Ho et al., Rosetta Stone naive extrapolation (2025-10; conversion approximate)", quantity="All-lab public ECI frontier, Oct 2028",
                theirs="~189 (182-196)", ours="median %.1f (80%% %.1f to %.1f) at 2028-09-30" % (ros["median"], ros["lo80"], ros["hi80"]),
                why="Rosetta extrapolates the 2023-25 slope; the frontier is already about 8 ECI above that line."),
           dict(source="Epoch AI trend (not a forecast), Nov 2026", quantity="All-lab frontier at 16.6 ECI/yr (14.6-18.7)",
                theirs="straight line reaches %.0f at end-2030" % (lpL.F0 + 16.6 * (2031.0 - T_NOW)), ours="all-lab median %.1f at 2030-12-31" % medL,
                why="See the reconciliation with research note 1."),
           dict(source="AI Futures Project milestones (Automated Coder mid-2028 / mid-2030; SAR 2027 under a held 1.7-1.9x trend)",
                quantity="Capability milestones from a takeoff model", theirs="dates of qualitative milestones", ours="no equivalent output",
                why="v1 translated ECI into METR-style hours to compare; that translation extrapolated two orders of magnitude beyond "
                    "METR's measurements and has been withdrawn. The 'compounding' and 'explosive' scenarios are the nearest analogue.")]
    mlink = links.get("metr_h50")
    metr_max_eci = float(np.max(mlink.x)) if mlink is not None else None
    proj.update(
        scenarios=scn_tab, weights=W, weights_are="priors. 'central' is the author's judgement; 'sceptic' and 'accelerationist' bracket it; "
        "'unweighted_evidence_average' is an unweighted average of three unlike data-based numbers, shown for transparency, not an estimate.",
        evidence_average_detail=ev_detail, sensitivity=sens, headline=head, backtested_through=vt, validated_through=vt,
        validated_through_deprecated="alias of backtested_through, kept for one version", backtested_through_caveat=bt_caveat,
        layer_agreement=dict(rows=agree, max_shortfall=round(max(a_["shortfall"] for a_ in agree), 3),
                             note="Frontier median minus the median implied by the next-model layer's own draws (leader and released next "
                                  "models). Zero by construction until both frontier families have shipped; the frontier is never below it."),
        mixture_pace_2027=mix_pace,
        validation_statement=bt_caveat + " Beyond %s the bands are a scenario projection driven by the stated priors: read each scenario "
                             "path separately and treat the mixture as a summary of the prior." % vt,
        calibration_applied=dict(anthropic={str(h): bt.factors(c) for h, c in calA.items()}, all_lab={str(h): bt.factors(c) for h, c in calL.items()},
                                 rule="Factors are fitted on the published configuration (pooled correction on trend scenarios). Mixture "
                                      "bands are stretched about the median by the factor for their horizon (interpolated between 0.5, 1.0 "
                                      "and 1.5 years, held flat beyond). Scenario-conditional bands are not stretched.",
                                 no_op_where="Every factor equal to 1.0 changes nothing: that is all three levels at 0.5 and 1.5 years "
                                             "and the 80%/95% levels wherever raw coverage was already at or above nominal."),
        bias_term=dict(R["machine_backtest"]["correction"], anthropic=dict(mean=round(BETA, 2), sd=round(BETA_SD, 2)),
                       all_lab=dict(mean=0.0, sd=0.0), form=R["machine_backtest"]["correction"]["shape"]),
        reconciliation_with_research_note_1=recon, saturation=sat, external_comparison=ext,
        metr_horizon=dict(statement="No hours series is published. METR's last measurement is 17.4 hours (Claude Mythos Preview, April 2026) "
                                    "and METR calls estimates above 16 hours unreliable; the fitted link (about 4.75 ECI points per doubling) "
                                    "has no model above public ECI %.1f. Every released frontier model since then, and every projected "
                                    "value, lies beyond that range, so any hours figure would be extrapolation. Qualitatively: if the link "
                                    "held, each further 5 ECI points would double the horizon." % metr_max_eci,
                          measured_max_hours=17.4, link_max_eci=metr_max_eci, implied_horizon_published=False),
        assumptions=dict(kappa_eci_per_10x_compute=[KAPPA_MEAN, KAPPA_SD], compute_paths=COMPUTE, haircut_realised_share=list(HAIRCUT),
                         n_paths=N_PATHS, family_drift_sd_per_sqrt_year=1.5))
    R["projection"] = proj
    R["reference_class"] = dict(rows=_rows(rc), note="Nearly all rows are the 2024 break seen through overlapping windows: two independent episodes.")

    # ------------------------------------------------------------- 9. headline block for the page
    def trio(s):
        return {k: s[k] for k in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")}
    hl_f = []
    for ent in ENTITIES:
        v = nxt[ent]
        av = [k for k in admitted if v["benchmarks"].get(k, {}).get("available")]
        bsel = ([k for k in av if v["benchmarks"][k]["graded"]] + [k for k in ("terminal_bench_2_1", "rli", "aa_index", "vals_index", "osworld")
                                                                    if k in av and not v["benchmarks"][k]["graded"]])[:3]
        hl_f.append(dict(entity=ent, name=v["predicted_name"], labels=v["labels"],
                         release_window=dict(q10=v["release_date"]["q10"], median=v["release_date"]["median"], q90=v["release_date"]["q90"]),
                         eci=trio(v["eci"]), aeci_own_card=trio(v["aeci_own_card"]), aeci_own_card_conditional=v["aeci_own_card_conditional"],
                         lead_tested=v["lead_tested"],
                         benchmarks=[dict(benchmark=k, title=v["benchmarks"][k]["title"], unit=v["benchmarks"][k]["unit"], graded=v["benchmarks"][k]["graded"],
                                          status=v["benchmarks"][k]["status"], **trio(v["benchmarks"][k])) for k in bsel]))
    corr = R["machine_backtest"]["correction"]
    h27 = next(h for h in head if h["date"] == "2027-12-31")
    sc = {r_["scenario"]: r_ for r_ in scn_tab}
    s0, s3 = by_lead["0.0"], by_lead["0.25"]
    nfolds_b = [v_["n"] for v_ in bstat.values()]
    notes = [
        "Intervals are 50/80/95% central intervals.",
        "The next-model point forecasts are, in effect, predecessor + recent Anthropic record slope x elapsed time; in backtest (RMSE %.1f at "
        "release, n=%d) they are no better than that two-line rule (RMSE %.1f)." % (s0["model"]["rmse"], s0["model"]["n"], s0["prev_plus_slope"]["rmse"]),
        "Frontier figures include an under-prediction correction on the 'hold' and faster scenarios only: a pooled %.1f ECI/yr (sd %.1f; "
        "Anthropic-only estimate %.1f, all-lab %.1f), tapered in from zero and out by 1.5 years. It adds %.1f ECI to those paths at end-2027 "
        "(%.1f to the mixture's record-line median). Its out-of-sample check is %d overlapping six-month folds with %d distinct outcomes."
        % (corr["value_used"], corr["sd_used"], corr["unshrunk"]["anthropic"], corr["unshrunk"]["all_lab"], corr["size_at_end_2027"],
           h27["correction_in_record_line_median"], mach["anthropic"]["correction_test"]["n_folds_with_a_rolling_correction"],
           mach["anthropic"]["correction_test"]["n_distinct_outcomes"]),
        "Scenario paces in 2027, correction included (ECI points gained by the record line): " +
        ", ".join("%s %.1f" % (k, sc[k]["realised_gain_2027"]["median"]) for k in SCENARIOS) +
        "; mixture %.1f; pre-break pace %.1f, recent pace %.1f." % (mix_pace["realised_gain_2027_median"], mix_pace["pre_break_slope_median"], mix_pace["recent_slope_median"]),
        bt_caveat,
        "The all-lab frontier is the larger of Anthropic's and the other labs'; Anthropic leads in %.0f%% of paths at end-2027 and %.0f%% at "
        "end-2030. The other labs' line is fitted on their own records and carries no correction."
        % (100 * h27["share_of_paths_anthropic_leads"], 100 * head[-1]["share_of_paths_anthropic_leads"]),
        "Benchmark forecasts are thinly tested (%d to %d backtest folds per benchmark). Only those marked graded are scored; arena, index and "
        "other 'indicative' rows are shown for orientation and are not graded." % (min(nfolds_b), max(nfolds_b)),
        "The Haiku forecast (median lead about %.0f months) lies beyond any tested lead (the longest is six months, %d folds)."
        % (12 * nxt["haiku"]["median_lead_years"], int(((rel.method == "model") & (rel.lead == 0.5)).sum())),
        "AECI own-card values are judgement-heavy estimates from eight cards (rolling RMSE %.1f)." % oc.rmse,
        "Above public ECI %.0f (80%% of today's benchmark basket is already 90%% solved at %.0f, 90%% at %.0f) the basket no longer identifies "
        "the scale; rows flagged beyond_measured_scale are extrapolations of the scale itself."
        % (R["scale"]["beyond_measured_scale_above_eci"], *R["scale"]["range_eci"]),
    ]
    changes = []
    try:
        old = __import__("json").loads((RAW.parents[1] / "history" / "capability_forecast_v2.0_superseded.json").read_text())
        of = {f_["date"]: f_ for f_ in old["headline"]["frontier"]}
        changes.append("Frontier, end-2027 median: %.1f -> %.1f; end-2030: %.1f -> %.1f. The under-prediction correction is now pooled across both "
                       "series (%.1f instead of 5.0 ECI/yr), applied only to 'hold' and faster scenarios, and tapered to zero by 1.5 years instead "
                       "of being added to every path permanently." % (of["2027-12-31"]["eci"]["median"], h27["anthropic_eci"]["median"],
                                                                     of["2030-12-31"]["eci"]["median"], head[-1]["anthropic_eci"]["median"], corr["value_used"]))
        for f_ in old["headline"]["families"]:
            changes.append("%s public ECI median: %.1f -> %.1f." % (f_["name"], f_["eci"]["median"], nxt[f_["entity"]]["eci"]["median"]))
        changes += [
            "'Slowdown' and 'reversion' no longer carry the correction; slowdown now runs below the pre-break pace in 2027. Scenario paces are published as realised gains, correction included.",
            "validated_through renamed backtested_through (%s; the old key is kept as an alias for this version) and now carries a caveat." % vt,
            "Benchmarks split into graded and indicative. GDPval-AA predictions and the Fable/Mythos Terminal-Bench 2.1 prediction are withdrawn; "
            "one saturation rule (latest score or predicted median in the top tenth) replaces per-family inconsistencies. Graded: %s."
            % (", ".join(sorted({p_["quantity"] for p_ in open_preds if p_["quantity"] not in ("eci_public", "aeci_own_card")})) or "none"),
            "All-lab frontier: the non-Anthropic line is now fitted separately and published; the share of paths in which Anthropic leads is reported.",
            "Own-card AECI: gap rule changed to an equal blend of the last gap and the mean of the last three (rolling RMSE %.1f)." % oc.rmse,
            "Measured-scale threshold is now a range derived from the whole basket (%.0f-%.0f); the page shades from %.0f (was 207.6)."
            % (*R["scale"]["range_eci"], R["scale"]["beyond_measured_scale_above_eci"]),
        ]
    except FileNotFoundError:
        pass
    R["headline"] = dict(
        families=hl_f,
        frontier=[dict(date=h["date"], eci=trio(h["anthropic_eci"]), all_lab_eci=trio(h["all_lab_eci"]), non_anthropic_eci=trio(h["non_anthropic_eci"]),
                       share_of_paths_anthropic_leads=h["share_of_paths_anthropic_leads"],
                       beyond_measured_scale=h["anthropic_eci"]["median_beyond_measured_scale"]) for h in head],
        backtested_through=vt, validated_through=vt, backtested_through_caveat=bt_caveat,
        beyond_measured_scale_above=R["scale"]["beyond_measured_scale_above_eci"], beyond_measured_scale_range=R["scale"]["range_eci"],
        display_cap_eci=R["scale"]["display_cap_eci"],
        correction=dict(value_eci_per_year=corr["value_used"], sd=corr["sd_used"], size_at_end_2027=corr["size_at_end_2027"],
                        in_mixture_record_line_median_at_end_2027=h27["correction_in_record_line_median"], applies_to=corr["applies_to"]),
        notes=notes, changes_since_previous=changes)
    R["_runtime_seconds"] = round(time.time() - t_start, 1)
    R["_objects"] = dict(d=d, lpA=lpA, lpL=lpL, links=links, mp=mpg, rel=rel, benchbt=benchbt, FA=FA, FL=FL, AA=AA, wts=wts, one=one,
                         admitted=admitted, oc=oc)
    log("projection done", t_start)
    return R
