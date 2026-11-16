"""Write capability_forecast.json and METHODS.md from the pipeline's results dict."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

import numpy as np

from .common import ROOT, REPO, RAW, OUT, AS_OF, MODEL_VERSION, SEED, FAMILIES, dump_json, yr


def input_hash() -> str:
    """Hash of every input and every source file; stored in the JSON so --check can tell
    whether the outputs are current."""
    files = sorted(RAW.glob("*.csv")) + sorted(RAW.glob("*.csv.gz")) + [
        REPO / "data" / "models.json", REPO / "data" / "benchmarks.json", REPO / "forecast" / "output" / "forecast.json"]
    files += sorted((ROOT / "capmodel").glob("*.py")) + [ROOT / "build_data.py", ROOT / "run.py"]
    h = hashlib.sha256()
    for f in files:
        h.update(f.name.encode())
        h.update(f.read_bytes())
    return h.hexdigest()


def history(R):
    d = R["_objects"]["d"]
    m = d.models
    aeci = d.index[d.index.scale == "aeci"]
    out = []
    for r in m[m.lab == "Anthropic"].sort_values("t").itertuples():
        a = aeci[aeci.model_id == r.model_id]
        fits = [dict(fit=x.fit, value=float(x.value), lo95=x.lo, hi95=x.hi, local_lo95=x.local_lo, local_hi95=x.local_hi,
                     value_type=x.value_type, own_card=bool(x.own_card == 1), status=x.status) for x in a.itertuples()]
        out.append(dict(model_id=r.model_id, family=r.family, release_date=r.release_date, internal_date=r.internal_date,
                        version=r.version, version_type=r.version_type, twin=r.twin, access=r.access,
                        eci=r.eci, eci_lo90=r.eci_lo90, eci_hi90=r.eci_hi90, n_benchmarks_eci=r.n_benchmarks_eci,
                        aeci_by_fit=fits))
    others = [dict(model_id=r.model_id, lab=r.lab, release_date=r.release_date, eci=r.eci, eci_lo90=r.eci_lo90, eci_hi90=r.eci_hi90)
              for r in m[(m.lab != "Anthropic") & (m.in_public_eci == 1) & (m.t >= 2023.15)].sort_values("t").itertuples()]
    fr = R["trend"]["records_all_lab"]
    return dict(claude=out, other_labs=others, all_lab_frontier_records=fr,
                internal_model=dict(name="Anthropic internal model (unreleased)", aeci_nov6=178.78, lo95=173.75, hi95=185.18,
                                    internal_date_approx="2026-09-26", n_benchmarks=15, used_in_fit=False))


def build_json(R, plots):
    J = dict(
        metadata=dict(
            as_of=AS_OF, model_version=MODEL_VERSION, seed=SEED, input_hash=input_hash(), runtime_seconds=R["_runtime_seconds"],
            generated_by="python3 capability/run.py",
            scales=dict(
                eci_public="Epoch Capabilities Index, public, Bayesian fit of November 2026 (Claude 3.5 Sonnet = 130, GPT-5 = 150). "
                           "Primary modelling scale.",
                aeci_nov6="Anthropic ECI on the November 6 2026 fit (Fable 5.2 / Mythos 5.2 system card). Reporting scale, "
                          "reached through the ECI->AECI mapping.",
                aeci_own_card="AECI as it will be printed in the model's own system card: the Nov 6-scale value plus the "
                              "scale drift expected over the card refits before then. This is the quantity that gets graded."),
            interval_convention="median with central 50%, 80% and 95% intervals (lo50/hi50, lo80/hi80, lo95/hi95); null where undefined",
            caveats=[
                "Small samples: 25 Claude models with a public ECI, 3 Fable releases, 4 Haiku releases, 13 models linking AECI to ECI, 7 AECI refit transitions.",
                "Both indices are re-estimated on every update. Predictions on the ECI scale are in today's units; AECI own-card predictions include an empirical drift model built on seven refits.",
                "AECI rests on first-party internal benchmarks that cannot be inspected; the mapping from public ECI may shift.",
                "A frontier is a running maximum of selected, best-configuration results; record-setters are noisy winners.",
                "Benchmark scores stop carrying information near their ceiling; the index scale itself is anchored on today's benchmark basket, so values far above ~200 have no direct empirical meaning.",
                "Scenario weights for 2027-2030 are a documented prior, not an estimate. The sensitivity table shows how much the answer moves.",
                "The model cannot see regime changes it has no data on (new architectures, export controls, a compute shock, a pause).",
                "Release dates come from the site's release forecaster; its errors pass straight through.",
            ],
            plots=plots),
        history=history(R),
        trend=R["trend"], families=R["families"], aeci=R["aeci"], links=R["links"],
        next_models=R["next_models"], projection=R["projection"],
        backtest=dict(frontier=R["frontier_backtest"], release=R["release_backtest"], benchmarks=R["benchmark_backtest"],
                      irt_refit_check=R["irt_refit_check"], aeci_drift_leave_one_out=R["aeci"]["drift"]["leave_one_out"]),
        calibration=dict(ability_factors=R["release_backtest"]["calibration"]["factors_used"],
                         ability=R["release_backtest"]["calibration"],
                         benchmark_factors=R["links"]["calibration_factors"],
                         benchmarks_pooled=R["benchmark_backtest"]["calibration"]["pooled"],
                         frontier=R["frontier_backtest"]["calibration"],
                         method="Conformal-style: per nominal level, the factor by which the interval must be stretched about "
                                "the median to cover the stated share of backtest outcomes; learned on earlier folds only when "
                                "scoring (rolling), and on all folds for the live forecast; floored at 1."),
        reference_class=R["reference_class"], open_predictions=R["open_predictions"])
    dump_json(J, OUT / "capability_forecast.json")
    return J


# ---------------------------------------------------------------------------- METHODS.md
def _tab(rows, cols, heads=None, fmt=None):
    heads = heads or cols
    fmt = fmt or {}
    out = ["| " + " | ".join(heads) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        cells = []
        for c in cols:
            v = r.get(c) if isinstance(r, dict) else r[c]
            if v is None or (isinstance(v, float) and not np.isfinite(v)):
                cells.append("-")
            elif c in fmt:
                cells.append(fmt[c](v))
            elif isinstance(v, float):
                cells.append(f"{v:.2f}")
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def _iv(s, nd=1, lv="80"):
    if s is None or s.get("median") is None:
        return "-"
    return f"{s['median']:.{nd}f} ({s['lo'+lv]:.{nd}f} to {s['hi'+lv]:.{nd}f})"


def write_methods(J):
    R = J
    md = []
    A = md.append
    nm = R["next_models"]["families"]
    P = R["projection"]
    rb = R["backtest"]["release"]
    fb = R["backtest"]["frontier"]
    bb = R["backtest"]["benchmarks"]
    irt = R["backtest"]["irt_refit_check"]
    tr = R["trend"]
    ae = R["aeci"]
    A(f"# Capability model: methods\n\nModel version `{MODEL_VERSION}`, as of {AS_OF}. Every number in this file is written by "
      "`python3 capability/run.py` from `capability/output/capability_forecast.json`; do not edit it by hand.\n")
    A("## 1. What is forecast\n\n"
      "1. The capability of the next model in each Anthropic family (Opus, Sonnet, Haiku, Fable, Mythos): public ECI, AECI on "
      "the November 6 2026 scale, AECI as it will be printed in the model's own system card, and its score on each tracked benchmark.\n"
      "2. The Anthropic frontier, each family, and the all-lab frontier by quarter to the end of 2030.\n\n"
      "**Primary scale.** " + ae["primary_scale"] + "\n")
    A("## 2. Data\n\n`build_data.py` writes four tables under `capability/data/` and logs every rename, date conflict, merge and "
      "dropped row in `build_log.csv`. Nothing is interpolated.\n\n"
      "- **Models** (`models.csv`): 256 models with a public ECI plus the Claude releases Epoch does not score (the four Mythos "
      "models, Claude 2.1, Claude 1). Claude release dates are the repo's (`data/models.json`, first public availability); four "
      "differ from Epoch's by 4 to 13 days.\n"
      "- **Index values** (`index_values.csv`): public ECI with 90% credible intervals; every AECI value Anthropic has printed, "
      "keyed by the card fit it belongs to. Epoch's 500 joint posterior draws per model are in `raw/eci_posterior_draws.csv.gz`.\n"
      "- **Benchmark scores** (`benchmark_scores.csv`): one row per benchmark and model in one stated configuration. Site-chart "
      "benchmarks use the site's series (`data/benchmarks.json`); other labs are added from Epoch's hub or Artificial Analysis "
      "where the same board is the source.\n"
      "- **Release dates** for the next model in each family come from `forecast/output/forecast.json` and are not re-modelled here.\n")
    A("## 3. Trend model\n\n"
      "A frontier series is the set of record-setting releases (running maximum of public ECI by release date). Seven candidate "
      "forms are fitted to Anthropic's records, each a regression with Student-t errors (4 degrees of freedom, fitted by IRLS):\n\n"
      "| Candidate | Form |\n|---|---|\n"
      "| `lin_all` | one slope, all history |\n| `lin_24`, `lin_12` | one slope, trailing 24 or 12 months |\n"
      "| `hinge` | piecewise linear, changepoint date unknown (profile likelihood over a monthly grid) |\n"
      "| `jump` | one slope plus a one-time level shift at an unknown date |\n| `quad` | quadratic over the trailing 36 months (smooth acceleration) |\n"
      "| `pool_all` | the all-lab trailing-24-month line plus a mean-reverting Anthropic gap |\n\n"
      "Uncertainty: each fit is repeated on bootstrap replicates that resample models and take one of Epoch's 500 joint posterior "
      "draws, recomputing the record set each time (this carries the winner's-curse selection of noisy records); coefficients "
      "are drawn from a multivariate t; the changepoint is drawn from its profile likelihood.\n\n"
      "Two estimands are kept apart. The **level** L(T) is the height of the record line at T: what a record-setter released "
      "at T is expected to score. The **frontier** F(T) is the running maximum actually held at T, a step function at or below "
      "the line: F(T) = max(F(now), L(T - A) + e), with A the age of the standing record drawn from the observed record gaps.\n\n"
      "### Was there a break?\n\n" + tr["note"] + "\n\n" +
      _tab([dict(series=k, **{f"{f}_w": v[f]["bic_weight"] for f in ("linear", "hinge", "jump", "quadratic")},
                 pre=v["hinge"]["slope_pre"], post=v["hinge"]["slope_post"], ratio=v["hinge"]["ratio"], tau=v["hinge"]["tau"], n=v["hinge"]["n"])
            for k, v in (("Anthropic, public ECI", tr["anthropic_public_eci"]), ("All labs, public ECI", tr["all_lab_public_eci"]),
                         ("AECI Nov 6 fit, public dates", tr["aeci_nov6_public_dates"]),
                         ("AECI Nov 6 fit, internal dates + internal model", tr["aeci_nov6_internal_dates_with_internal_model"]))],
           ["series", "n", "linear_w", "hinge_w", "jump_w", "quadratic_w", "pre", "post", "ratio", "tau"],
           ["Series", "n", "BIC wt linear", "hinge", "jump", "quadratic", "Slope before", "after", "Ratio", "Changepoint"],
           {"tau": lambda v: f"{v:.2f}"}) + "\n\n"
      f"With bootstrap uncertainty, the public-ECI slope ratio for Anthropic is {_iv(tr['anthropic_public_slope_draws']['ratio'], 2)} "
      f"(median, 80% interval): {tr['anthropic_public_slope_draws']['pre']['median']:.1f} points/yr before and "
      f"{tr['anthropic_public_slope_draws']['post']['median']:.1f} after. The probability that it reaches the card's 1.88x is "
      f"{tr['anthropic_public_slope_draws']['p_ratio_above_1_88']:.0%}. "
      "The all-lab public frontier shows no break. So the acceleration Anthropic reports on AECI is partly replicated on the "
      "public scale for Anthropic alone, and not at all for the industry frontier.\n")
    A("### Combination\n\n" + rb["combination_note"] + "\n\n" +
      _tab([dict(candidate=k, stack_frontier=rb["weight_components"]["stack_frontier"][k],
                 stack_release=(rb["weight_components"]["stack_release"] or {}).get(k), equal=rb["weight_components"]["equal"][k],
                 live=v) for k, v in rb["live_trend_weights"].items()],
           ["candidate", "stack_frontier", "stack_release", "equal", "live"],
           ["Candidate", "Stacking on frontier folds", "Stacking on release folds", "Equal", "Live weight (average)"]) +
      "\n\nStacking minimises the mean CRPS of the mixture over folds, with a 5% floor per candidate. "
      "All-lab frontier weights: " + ", ".join(f"{k} {v:.2f}" for k, v in fb["final_weights"]["all_lab"].items()) + ".\n")
    F = R["families"]
    A("## 4. Families\n\n" + F["note"] + "\n\n" +
      _tab(F["table"], ["family", "n", "n_eff", "unpooled_mean", "pooled_mean", "pooled_se", "shrinkage", "last_offset"],
           ["Family", "n", "Effective n", "Unpooled mean", "Pooled mean", "SE", "Shrinkage", "Last offset"]) +
      f"\n\nWithin-family sd {F['within_family_sd']}, between-family sd {F['between_family_sd']}. The next offset is a mixture: "
      f"weight {F['alpha_weight_on_last_offset']:.2f} on the family's last offset and the rest on its pooled mean (weight set by CRPS "
      f"stacking over backtest folds), plus Student-t scatter. A version-type effect (new generation / x.5 / minor) was estimated "
      f"({', '.join(f'{k} {v:+.2f}' for k, v in F['version_type_effect'].items())} ECI points) and tested: CRPS "
      f"{rb['version_type_effect']['crps_with']} with it, {rb['version_type_effect']['crps_without']} without. "
      f"It is {'used' if rb['version_type_effect']['used'] else 'not used'}. " + F["mythos"] + "\n")
    A("## 5. AECI: mapping and drift\n\n" + ae["divergence_note"] + "\n\n" +
      _tab(ae["overlap"], ["model_id", "eci", "aeci", "fit_hinge", "fit_offset", "value_type"],
           ["Model", "Public ECI", "AECI (Nov 6)", "Hinge fit", "Level-shift fit", "AECI source"]) +
      f"\n\nHinge: knee {ae['mapping_forms']['hinge']['k']:.1f}, slope above it {1 + ae['mapping_forms']['hinge']['c']:.2f}. Level shift: "
      f"+{ae['mapping_forms']['offset']['c']:.2f} above {ae['mapping_forms']['offset']['k']:.1f}. Overlap RMSE: hinge "
      f"{ae['overlap_rmse']['hinge']}, level shift {ae['overlap_rmse']['offset']}. In the bootstrap the level-shift form fits better in "
      f"{ae['bootstrap_share_offset_form_fits_better']:.0%} of replicates; the forecast uses it with probability "
      f"{ae['p_offset_form_used']:.2f} (clipped to 0.2-0.8 so neither form is ruled out on 13 points). Residual sd used: "
      f"{ae['mapping_residual_sd_used']} AECI points, which includes the miss on the two site-rescaled values (Sonnet 5.5, Haiku 5.5) "
      "that were not used in the fit: " +
      "; ".join(f"{e['model_id']} site estimate {e['repo_rescaled_aeci']}, mapped {e['mapped_offset']} / {e['mapped_hinge']}" for e in ae["out_of_sample_check_repo_rescaled"]) + ".\n\n"
      "**Drift.** " + ae["drift"]["note"] + "\n\n" +
      _tab(ae["drift"]["transitions"], ["fit_to", "mean_delta", "n_models"], ["Refit (card)", "Mean change of models in both fits", "Models"]) +
      f"\n\nMean {ae['drift']['summary']['mean']} per refit, sd {ae['drift']['summary']['sd']}. The own-card prediction adds, for each "
      "refit expected before the model's card (one per card; other families' releases counted from the release forecaster), a "
      f"step resampled from these seven, plus sd {ae['drift']['own_card_sd']} for the own-card measurement. Leave-one-out check of "
      f"the step distribution: {ae['drift']['leave_one_out']['cov80']:.0%} of the seven inside the 80% interval. n = 7; this is the "
      "least-tested part of the model.\n")
    A("## 6. Benchmark links\n\nBounded scores: p = (score - floor)/(ceiling - floor) = sigmoid(a(ability - D)), noise Student-t on "
      "the logit scale so draws respect the bounds. Elo and other unbounded scores: linear in ability. METR horizon: log2(minutes) "
      "linear in ability. " + R["links"]["note"] + "\n\n" +
      _tab(R["links"]["table"], ["title", "kind", "n", "slope", "difficulty", "eci_50_to_90", "rmse_score", "epoch_slope", "epoch_difficulty", "configuration"],
           ["Benchmark", "Link", "n", "Slope", "Difficulty (ECI at 50%)", "ECI from 50% to 90%", "Fit RMSE", "Epoch slope", "Epoch difficulty", "Configuration"],
           {"slope": lambda v: f"{v:.3f}", "epoch_slope": lambda v: f"{v:.3f}"}) + "\n\n" +
      "METR: " + next((f"{r['eci_per_doubling']} ECI points per doubling of the 50% horizon (90% interval {r['eci_per_doubling_ci90'][0]} to "
                       f"{r['eci_per_doubling_ci90'][1]}; Epoch says about 5)" for r in R["links"]["table"] if r["benchmark"] == "metr_h50"), "not fitted") + ".\n\n"
      "Dropped: " + "; ".join(f"{x['title']} ({x['reason']})" for x in R["links"]["dropped"]) + ".\n")
    A("## 7. Backtest\n\n### 7.1 Claude releases\n\n" + rb["design"] + "\n")
    order = ["model", "trailing_12m_linear", "all_history_linear", "family_mean_step", "prev_in_family", "model_date_uncertain"]
    names = {"model": "Model", "trailing_12m_linear": "Baseline: trailing-12-month all-lab trend at the date",
             "all_history_linear": "Baseline: all-history all-lab linear trend at the date",
             "family_mean_step": "Baseline: previous + family's mean step", "prev_in_family": "Baseline: previous model in family",
             "model_date_uncertain": "Model, release date not given (cadence reconstruction)"}
    for ld, lab in (("0.0", "Day-of nowcast (lead 0)"), ("0.25", "3 months ahead"), ("0.5", "6 months ahead")):
        s = rb["summary_by_lead"][ld]
        rows = [dict(method=names[k], **s[k]) for k in order if k in s]
        A(f"**{lab}**\n\n" + _tab(rows, ["method", "n", "bias", "mae", "rmse", "crps", "cov50", "cov80", "cov95"],
                                   ["Method", "n", "Bias (actual - predicted)", "MAE", "RMSE", "CRPS", "Cov 50%", "Cov 80%", "Cov 95%"]) + "\n")
    A("Errors are in public-ECI points. The model beats every baseline at every lead on RMSE and CRPS. It under-predicts on "
      "average (positive bias, growing with lead). " + rb["bias_correction_test"]["note"] + " Not knowing the release date "
      "roughly doubles the error at 6 months.\n\n"
      "Combination rules and single candidates, same folds:\n\n" +
      _tab([r for r in rb["combination_rules"] if r["lead_years"] in (0.0, 0.25)], ["lead_years", "variant", "n", "rmse", "crps", "cov80"],
           ["Lead (yr)", "Variant", "n", "RMSE", "CRPS", "Cov 80%"]) + "\n")
    A("### 7.2 Frontier at fixed horizons\n\n" + fb["design"] + "\n\n" +
      _tab([r for r in fb["table"] if r["method"] in ("stacked", "lin_12", "lin_all", "pool_all", "hinge", "persistence") and r["horizon_years"] in (0.5, 1.0, 1.5)],
           ["series", "horizon_years", "method", "n", "bias", "mae", "rmse", "crps", "cov50", "cov80", "cov95"],
           ["Series", "Horizon (yr)", "Method", "n", "Bias", "MAE", "RMSE", "CRPS", "Cov 50%", "Cov 80%", "Cov 95%"]) +
      "\n\nEvery trend form under-predicted the frontier over 2024-26, by about 6 ECI points at one year for the stacked model: "
      "the pace rose during the test window. Folds overlap heavily (monthly origins), so the effective sample is far below n.\n")
    A("### 7.3 Benchmark scores\n\n" + bb["design"] + "\n\n" +
      _tab(bb["paired_vs_previous"], ["benchmark", "n", "mae_model", "mae_prev_in_family", "model_better"],
           ["Benchmark", "n", "MAE model", "MAE previous-in-family", "Model better"]) +
      f"\n\nWith the true ability known, link error on bounded benchmarks is RMSE {bb['link_only_rmse_bounded_fraction']} and MAE "
      f"{bb['link_only_mae_bounded_fraction']} of the score range ({bb['research_note_reference']}). The model loses to "
      "'previous in family' on ForecastBench and Vending-Bench 2, where scores barely track ability; treat those two predictions as weak.\n")
    A("### 7.4 Leave-future-out IRT refit\n\n" + irt["design"] + "\n\n"
      f"Reproduction on all data: correlation {irt['full_data_reproduction']['corr']} with Epoch's published ECI, RMSE "
      f"{irt['full_data_reproduction']['rmse_above_140']} above ECI 140 ({irt['full_data_reproduction']['rmse_all']} overall). "
      f"Vintage versus published ability of the target: mean shift {irt['target_shift']['mean_vintage_minus_published']}, mean absolute "
      f"{irt['target_shift']['mean_abs']}, maximum {irt['target_shift']['max_abs']} ECI points over {irt['target_shift']['n']} folds.\n\n" +
      _tab([dict(lead=k, n=v["n"], rmse_v=v["vintage"]["rmse"], rmse_p=v["published"]["rmse"], bias_v=v["vintage"]["bias"],
                 bias_p=v["published"]["bias"], cov_v=v["vintage"]["cov80"], cov_p=v["published"]["cov80"]) for k, v in irt["comparison_by_lead"].items()],
           ["lead", "n", "rmse_v", "rmse_p", "bias_v", "bias_p", "cov_v", "cov_p"],
           ["Lead (yr)", "n", "RMSE vintage", "RMSE published", "Bias vintage", "Bias published", "Cov 80% vintage", "Cov 80% published"]) +
      "\n\nUsing today's abilities for past models (the look-ahead in the scale) flatters the backtest slightly: errors are "
      "about 10-20% larger on vintage abilities. " + irt["caveat"] + "\n")
    cal = rb["calibration"]
    bc = bb["calibration"]["pooled"]
    A("## 8. Calibration\n\n" + R["calibration"]["method"] + "\n\n" +
      _tab([dict(set="Ability, day-of", **cal["lead_0"]), dict(set="Ability, 3-6 months ahead", **cal["lead_3_to_6_months"]),
            dict(set="Benchmark scores, pooled", **bc)],
           ["set", "n_folds", "raw_cov50", "raw_cov80", "raw_cov95", "n_scored_rolling", "calibrated_cov50", "calibrated_cov80", "calibrated_cov95",
            "factor50", "factor80", "factor95", "factor80_unfloored"],
           ["Set", "Folds", "Raw 50%", "Raw 80%", "Raw 95%", "Folds scored rolling", "Calibrated 50%", "80%", "95%", "Factor 50%", "80%", "95%", "80% factor before floor"]) +
      "\n\nRaw intervals already cover at or above nominal for ability, so the factors sit at or near 1 and calibration changes "
      "little; the unfloored factors below 1 say the raw intervals are, if anything, slightly wide. They are not narrowed. "
      "AECI intervals use the ability factors; there is no AECI backtest beyond the drift check.\n")
    A("## 9. Next-model predictions\n\n" + R["next_models"]["date_integration"] + " " + R["next_models"]["note"] + "\n\n" +
      _tab([dict(family=f, name=v["predicted_name"], date=f"{v['release_date']['median']} ({v['release_date']['q10']} to {v['release_date']['q90']})",
                 eci=_iv(v["eci"]), a6=_iv(v["aeci_nov6_scale"]), own=_iv(v["aeci_own_card"]), prev=v["previous_eci"],
                 pint=v["p_aeci_at_or_above_internal_model"]) for f, v in nm.items()],
           ["family", "name", "date", "prev", "eci", "a6", "own", "pint"],
           ["Family", "Likeliest name", "Release (median, 10-90%)", "Previous ECI", "Public ECI (80%)", "AECI Nov 6 scale (80%)",
            "AECI own card (80%)", "P(AECI >= internal model)"]) + "\n\n" +
      "Benchmarks, median with 80% interval:\n\n" +
      _tab([dict(b=R["links"]["table"][i]["title"], **{f: _iv(nm[f]["benchmarks"][r["benchmark"]], 0 if r["kind"] in ("elo", "loghorizon") or r["benchmark"] == "vending_bench_2" else 1)
                                                        for f in ("opus", "sonnet", "haiku", "fable")}) for i, r in enumerate(R["links"]["table"])],
           ["b", "opus", "sonnet", "haiku", "fable"], ["Benchmark", "Opus", "Sonnet", "Haiku", "Fable / Mythos"]) +
      "\n\nMythos shares Fable's ability; its release window differs slightly, so its numbers in the JSON differ by a few tenths.\n")
    A("## 10. Projection, 2026-2030\n\n"
      "Pace on the public-ECI scale is decomposed with the driver tables: pace(t) = kappa x log10(compute growth in year t) + a0 x m(t), "
      f"with kappa = {P['assumptions']['kappa_eci_per_10x_compute'][0]} +/- {P['assumptions']['kappa_eci_per_10x_compute'][1]} ECI per 10x "
      "training compute (research note 1), a0 the algorithmic share at the pre-break pace (pre-break slope minus kappa x log10(5), "
      "5x/yr being Epoch's compute trend), and m(t) a multiplier on algorithmic progress. The post-break public slope implies "
      f"m = {P['assumptions']['m_post']['median']} (80% {P['assumptions']['m_post']['lo80']} to {P['assumptions']['m_post']['hi80']}); "
      "METR and the AI Futures Project attribute 1.7-1.9x to AI assistance. Scenarios differ only in the compute path and m(t):\n\n" +
      _tab([dict(s=r["scenario"], d=r["definition"], p27=f"{r['pace_eci_2027']['median']} ({r['pace_eci_2027']['lo80']} to {r['pace_eci_2027']['hi80']})",
                 p28=r["pace_eci_2028"]["median"], p30=r["pace_eci_2030"]["median"], a27=r["pace_aeci_2027_median"], k27=r["k_vs_prebreak_2027_median"])
            for r in P["scenarios"]], ["s", "d", "p27", "p28", "p30", "a27", "k27"],
           ["Scenario", "Definition", "ECI pts/yr 2027 (80%)", "2028", "2030", "AECI pts/yr 2027", "x pre-break pace, 2027"]) +
      f"\n\nOn top of each path: a random walk with annual sd {P['assumptions']['annual_random_walk_sd']} ECI points (the spread of "
      "one-year frontier errors in backtest), trend-parameter draws for the starting level, record-age and residual noise for the "
      "step-function frontier. The all-lab frontier is the larger of Anthropic's and a rival frontier whose gap to Anthropic "
      f"mean-reverts to its 2024-26 average ({P['assumptions']['other_labs_gap']['mean']:+.1f} ECI, sd {P['assumptions']['other_labs_gap']['sd']}; "
      f"today {P['assumptions']['other_labs_gap']['now']:+.1f}). Families sit at the record line lagged by their release cadence plus "
      "their pooled offset, which is allowed to drift.\n\n### Weights\n\n"
      "The data cannot set these weights alone, so they are an explicit prior built in two steps.\n\n"
      "*Step 1, data only.* Three lines of evidence on whether the step-up reverts, averaged: (a) the reference class of earlier "
      f"apparent accelerations in the ECI frontier and METR horizons, Laplace-smoothed: {P['weights_evidence']['p_revert_reference_class']}; "
      f"(b) BIC weight on 'jump or no change' for Anthropic's public-ECI records: {P['weights_evidence']['p_revert_anthropic_public_bic']}; "
      f"(c) BIC weight on 'no slope increase' for the all-lab frontier: {P['weights_evidence']['p_revert_all_lab_bic']}. "
      f"Combined P(revert) = {P['weights_evidence']['p_revert_combined']}. The remainder is split between 'hold' and 'compounding' by "
      f"the reference class (share that accelerated again: {P['weights_evidence']['compounding_share_of_persisting']}). The reference "
      "class is two independent episodes (the 2024 break in ECI and in METR horizons); both persisted for 12 months or more, one "
      "accelerated again. Slowdown and explosive have no precedent in the sample and get zero by construction.\n\n"
      "*Step 2, central prior.* Data-only weights scaled to 84%, plus 10% slowdown and 6% explosive. Reasons for the tails: "
      "compute growth cannot stay at 5x/yr (lead times, capital, possible export restrictions; research note 1), which argues for "
      "a slowdown tail; Anthropic's S-1/A says the AI R&D threshold is met on the 'expect' prong and takeoff models put large mass "
      "on rapid acceleration, which argues for an explosive tail; scenario-style forecasts have run at 60-75% of predicted pace, "
      "which is why that tail is small and why accelerating scenarios carry a realisation haircut. The orchestrator's note in "
      "research note 3 is followed: the collecting worker's 15/35/30/20 is kept only as the 'accelerationist' alternative.\n\n" +
      _tab([dict(w=k, **v) for k, v in P["weights"].items()], ["w", "slowdown", "reversion", "hold", "compounding", "explosive"],
           ["Weighting", "Slowdown", "Reversion", "Hold", "Compounding", "Explosive"]) + "\n\n### Results (central weights)\n\n" +
      _tab([dict(d=h["date"], e80=_iv(h["eci"]), e95=f"{h['eci']['lo95']} to {h['eci']['hi95']}", a80=_iv(h["aeci"]),
                 a95=f"{h['aeci']['lo95']} to {h['aeci']['hi95']}", l=_iv(h["all_lab_eci"]), m=h["metr_h50_hours"]["median"]) for h in P["headline"]],
           ["d", "e80", "e95", "a80", "a95", "l", "m"],
           ["Date", "Anthropic frontier, public ECI (80%)", "95%", "AECI Nov 6 scale (80%)", "95%", "All-lab public ECI (80%)", "Implied 50% horizon, hours (median)"],
           {"m": lambda v: ("100,000+" if v >= 100000 else f"{v:,.0f}")}) +
      "\n\n" + P["metr_horizon_note"] + "\n\n### Sensitivity to the prior\n\n" +
      _tab([s for s in P["sensitivity"] if s["date"] in ("2028-12-31", "2030-12-31")], ["weighting", "series", "date", "median", "lo80", "hi80"],
           ["Weighting", "Series", "Date", "Median", "80% low", "80% high"], {"median": lambda v: f"{v:.0f}", "lo80": lambda v: f"{v:.0f}", "hi80": lambda v: f"{v:.0f}"}) +
      "\n\nThe median at end-2030 moves by tens of points across weightings and the upper 80% bound by far more: the long-range "
      "answer is mostly the prior.\n\n### Interval widths against the track record\n\n" +
      _tab(P["width_check"], ["date", "horizon_years", "ours_minus", "ours_plus", "research_minus", "research_plus", "at_least_as_wide"],
           ["Date", "Horizon (yr)", "Ours, 80% below median", "above", "Research note 1, below", "above", "At least as wide"],
           {"ours_minus": lambda v: f"{v:+.0f}", "ours_plus": lambda v: f"{v:+.0f}", "research_minus": lambda v: f"{v:+d}", "research_plus": lambda v: f"{v:+d}"}) +
      "\n\n### Saturation\n\nDate at which Anthropic's record line reaches 90% and 95% of each bounded benchmark's ceiling-rescaled "
      "range. After that the benchmark no longer separates models.\n\n" +
      _tab([dict(t=s["title"], now=s["frontier_score_now"], best=s["best_observed"], c90=f"{s['cross_90']['median']} ({s['cross_90']['q10']} to {s['cross_90']['q90']})",
                 c95=f"{s['cross_95']['median']} ({s['cross_95']['q10']} to {s['cross_95']['q90']})") for s in P["saturation"]],
           ["t", "now", "best", "c90", "c95"], ["Benchmark", "Fitted frontier score now", "Best observed", "Crosses 90% (median, 10-90%)", "Crosses 95%"]) +
      "\n\n### Against external forecasts\n\n" +
      _tab(P["external_comparison"], ["source", "quantity", "theirs", "ours", "why"], ["Source", "Quantity", "Theirs", "Ours", "Why they differ"]) + "\n")
    A("## 11. Assumptions that are not estimated\n\n"
      "| Assumption | Value | Source |\n|---|---|---|\n"
      "| Residual distribution | Student-t, 4 df | robustness choice |\n"
      "| Floor on trend residual scale | 0.75 ECI | Epoch posterior sd at the frontier is 1-2 points |\n"
      "| Recency half-life for family offsets | 1.5 years | judgement; families re-rank over time |\n"
      "| Stacking floor | 5% per candidate | hedge against overfitting ~45 overlapping folds |\n"
      "| Mapping-form probability clip | 0.2 to 0.8 | 13 overlap points cannot exclude either form |\n"
      "| ECI per 10x compute | 9 +/- 2 | research note 1 (worker's derivation from Rosetta) |\n"
      "| Compute growth paths | low / central / high | `driver_scenarios_2026_2030.csv` |\n"
      "| Algorithmic multiplier ranges per scenario | see scenario table | research note 3 bands |\n"
      "| Realisation haircut on accelerating scenarios | 60-100% | AI 2027 ran at 58-75% of pace |\n"
      "| Scenario weights | see table | section 10; prior |\n"
      "| Family offset drift | 1.5 ECI per sqrt(year) | judgement from Sonnet's 2024-26 slide |\n"
      "| Rival-frontier gap is stationary | mean-reverting to 2024-26 average | judgement; METR finds 1.4x if all labs are included |\n"
      "| Fable = Mythos in ability | identical | Anthropic's statement that they are one model |\n")
    A("## 12. Limitations\n\n" + "\n".join(f"- {c}" for c in R["metadata"]["caveats"]) + "\n"
      "- Backtest folds at 3 and 6 months are few (see the tables) because families ship every ~3 months; the long-lead evidence is thin.\n"
      "- All backtest folds fall in 2024-26, a period of rising pace. Every method under-predicted; the model may still be doing so.\n"
      "- The trend candidates cannot be told apart on release folds; the combination weights are a hedge, not a finding.\n"
      "- Links are fitted on ability point estimates (no errors-in-variables) and, for site charts, on Claude models only (10-17 points).\n"
      "- OSWorld mixes three eval versions; HLE and SWE-bench Pro are first-party; ForecastBench set-ups differ by model.\n"
      "- Family projections assume today's cadence and a slowly drifting offset; a tier could be repositioned or retired.\n"
      "- The implied METR horizon is extrapolated two or more orders of magnitude beyond anything METR measured.\n")
    A("## 13. What would change the forecast\n\n"
      "- The next two Anthropic record-setters: on the hold path they land near the 22-24 ECI/yr line; two in a row near 15-17/yr would shift weight to reversion.\n"
      "- Epoch scoring more of Fable 5.2 (19 benchmarks so far; 90% interval 169.9 to 177.5): it anchors the current level.\n"
      "- The next card's refit: another +5 step in printed AECI would confirm upward drift; a stable scale would tighten own-card intervals.\n"
      "- A released model matching the internal model's 178.8 AECI, and its public ECI: a sixth point on the divergence above 157.\n"
      "- Other labs' frontier: if it also bends upward, the 'no industry-wide break' evidence weakens.\n"
      "- A new METR horizon for any post-Mythos-Preview model.\n"
      "- Compute: delivered capacity against the S-1 commitments; export restrictions.\n")
    (ROOT / "METHODS.md").write_text("\n".join(md))
