"""Write capability_forecast.json and METHODS.md from the pipeline's results dict."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

import numpy as np

from .common import ROOT, REPO, RAW, OUT, AS_OF, MODEL_VERSION, PREDICTION_VERSION, SEED, FAMILIES, dump_json, yr


def input_hash() -> str:
    """Hash of every input and every source file; stored in the JSON so --check can tell
    whether the outputs are current."""
    files = sorted(RAW.glob("*.csv")) + sorted(RAW.glob("*.csv.gz")) + [
        REPO / "data" / "models.json", REPO / "data" / "benchmarks.json", REPO / "forecast" / "output" / "forecast.json"]
    files += [ROOT / "data" / "irt_vintages.csv.gz"]       # committed vintage IRT refits (rebuilt by run.py --full)
    files += sorted((ROOT / "capmodel").glob("*.py")) + [ROOT / "build_data.py", ROOT / "run.py"]
    h = hashlib.sha256()
    for f in files:
        if f.exists():
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
    return dict(claude=out, other_labs=others, all_lab_frontier_records=R["trend"]["records_all_lab"],
                internal_model=dict(name="Anthropic internal model (unreleased)", aeci_nov6=178.78, lo95=173.75, hi95=185.18,
                                    internal_date_approx="2026-09-26", n_benchmarks=15, used_in_fit=False))


REVIEW = [
    ("B1", "Headline backtest omitted the worst fold; strawman baselines", "fixed",
     "Every table is on all folds (Fable 5 included; a first-of-family release is placed on the record line). The reviewer's baseline "
     "is a named baseline with paired differences and bootstrap intervals. 'Beats every baseline' is withdrawn: the model is not "
     "distinguishable from previous-in-family + trailing-12-month slope, which is now its core."),
    ("B2", "Benchmark predictions contradicted observed scores", "fixed",
     "Ceilings are estimated where the data allow; predictions are anchored on the family's own last score; saturated, stale and thin "
     "benchmarks are dropped with reasons; a family already within a tenth of the ceiling gets a saturation statement instead of a "
     "number; tests check every open prediction against observed scores."),
    ("M1", "Corner-solution stacking; the two layers disagreed", "fixed",
     "Stacking is gone. One level process (equal weights over three recent-trend forms; no all-history forms) feeds both the next-model "
     "layer and the projection from the same simulated paths."),
    ("M2", "The 2027-30 band was an untested prior", "partly",
     "The projection code is now backtested at 0.5, 1.0 and 1.5 years on both frontiers, its bias term is estimated out of sample and "
     "carried with uncertainty, and its calibration factors are applied. The all-lab frontier is fitted to all-lab data. A below-pre-break "
     "scenario exists. Beyond 1.5 years nothing can be tested: those bands remain a prior and are labelled as such; values above the "
     "measured scale are flagged."),
    ("M3", "Implied METR horizon was false precision", "fixed", "The hours series and the work-month / work-year probabilities are removed; a qualitative statement replaces them."),
    ("M4", "AECI layer", "partly",
     "Own-card AECI is modelled directly from the eight own-card values and labelled a judgement-heavy estimate; refit steps are no longer "
     "summed as iid draws; Sonnet/Haiku predictions are marked conditional. It is still eight cards: the rolling test is poor and is reported."),
    ("M5", "Twins and grading", "fixed",
     "Fable and Mythos are one entity. Unresolvable predictions are pruned; grade.py has an expiry rule and grades against the first published value."),
    ("M6", "Regression odds contradicted the record", "fixed", "Positive-step model; implied P(regression) is reported per entity and is a few percent, from measurement noise only."),
    ("M7", "Section 7.4 not reproducible", "fixed",
     "Root cause was a date-rounding bug that dropped the target from its own vintage on a clean cache. Fixed; vintages are committed, hashed and tested."),
    ("M8", "Live leads untested; calibration a no-op", "partly",
     "The date-unknown variant is the headline for leads above zero and the limits of n are stated. Ability calibration factors are still 1: "
     "raw coverage on all folds is at or above nominal, so there is nothing to widen. That is a finding, not an omission; the frontier bands "
     "do get non-trivial factors. Haiku's eight-month lead remains untested and is flagged in the output."),
    ("minor", "Name-matcher merges", "fixed", "Dated variants no longer merge into siblings; explicit aliases for Claude 3.5 Sonnet (Oct/Jun); every non-exact match is logged."),
    ("minor", "Bootstrap was a subsample; slope draws truncated", "fixed", "Called a subsample bootstrap; draws are clipped (not discarded) and the clipped share is reported."),
    ("minor", "Tests asserted what the code wrote", "fixed", "Leak tests perturb future data and require unchanged predictions; the mapping test is leave-one-out."),
    ("minor", "Monte Carlo noise comparable to differences", "fixed", "Draws raised; a second-seed rerun is reported; candidate differences inside that noise are no longer interpreted."),
    ("minor", "m compared with METR's total-slope ratio", "fixed", "The total slope ratio is reported for the like-for-like comparison."),
    ("minor", "Degenerate frontier floor", "fixed", "The standing leader's value is drawn from Epoch's posterior."),
    ("minor", "Full-sample tuning choices (df, floors, half-life)", "rejected",
     "Left as stated assumptions (METHODS section 11). The reviewer measured their effect at RMSE 2.36-2.83, inside fold noise; tuning them "
     "by nested cross-validation on ~20 folds would add machinery without changing any number that matters."),
]


REVIEW2 = [
    ("N1", "Bias term added to every scenario and hidden from the scenario table", "fixed",
     "The correction is pooled across both series by random effects, applied only to 'hold' and faster scenarios on the Anthropic line, "
     "tapered in from zero and out by 1.5 years. Scenario paces are published as realised gains with the correction included; "
     "'slowdown' runs below the pre-break pace in 2027."),
    ("N2", "'The correction helped' rested on four folds", "partly",
     "The thinness of the test is stated wherever the correction is mentioned (METHODS 7.2, headline.notes, projection.bias_term). The "
     "pooled estimate replaces the Anthropic-only one. It remains a correction estimated in one regime and untested beyond six months."),
    ("N3", "'Validated through' too strong", "fixed", "Renamed backtested_through (alias kept one version), derived without the 0.13-year allowance, with a caveat attached."),
    ("N4", "GDPval-AA over-extrapolates", "fixed", "Withdrawn. No concave link was fitted: with 12 folds and a board that re-anchors, there is nothing to validate one against."),
    ("N5", "All-lab frontier was mostly Anthropic's and inherited its correction", "fixed",
     "The non-Anthropic frontier is fitted on its own records, carries no correction and is published; the all-lab frontier is the larger "
     "of the two; the share of paths in which Anthropic leads is reported per year-end."),
    ("minor", "Fable/Mythos Terminal-Bench 2.1 anchored on Fable 5.1", "fixed", "A prediction now needs a score from the family's latest model; this one is withdrawn."),
    ("minor", "Admission rule text disagreed with code; inconsistent saturation", "fixed",
     "One rule in code and text: graded needs 4+ folds, 80% coverage >= 0.7, |bias| <= RMSE/2, a resolvable source and a ceiling that does "
     "not hug the record; everything else with a link is indicative. A family gets no number if its latest score or predicted median is "
     "in the top tenth."),
    ("minor", "Arena scores at mixed snapshots", "fixed", "Indicative, not graded."),
    ("minor", "Layers agreed to ~1 ECI, not Monte Carlo noise", "fixed",
     "The frontier is built from the next-model layer's own draws until both frontier families have shipped; projection.layer_agreement "
     "reports the shortfall per quarter and a test bounds it."),
    ("minor", "Lead-0 vintage included the target", "fixed", "History now comes from a strict-origin vintage."),
    ("minor", "Grading matched chart rows by exact date", "fixed", "Matches on model name."),
    ("minor", "Measured-scale threshold lenient", "fixed", "Reported as a range from the whole basket; the page shades from its upper end."),
    ("minor", "Calibration factors fitted on a different configuration", "fixed", "Fitted on the published configuration; METHODS says where they are a no-op."),
    ("nit", "Own-card rule scored worse than 'last gap'", "fixed", "Equal blend of the two rules."),
    ("nit", "Claude 3.5 Haiku entered vintages 13 days early", "fixed", "Vintages use canonical release dates."),
    ("nit", "All-lab slope draws clipped 19.8%", "noted", "Reported in trend.level_process; the other labs' record series is short and noisy and the clipping bounds are wide (4-60 ECI/yr)."),
]


def build_json(R, plots):
    J = dict(
        metadata=dict(
            as_of=AS_OF, model_version=MODEL_VERSION, seed=SEED, input_hash=input_hash(), runtime_seconds=R["_runtime_seconds"],
            generated_by="python3 capability/run.py",
            prediction_version=PREDICTION_VERSION,
            default_unchanged_from="cap-v2.1 (cap-v2.2 adds variants.with_model_4 only; archive: capability/history/capability_forecast_v2.1_superseded_by_addition.json)",
            supersedes=dict(version="cap-v2.0", status="superseded after a second independent review (no blockers; five majors)",
                            archive="capability/history/capability_forecast_v2.0_superseded.json",
                            review="capability/research/05-adversarial-review-v2.md"),
            earlier_versions=[dict(version="cap-v1.0", status="withdrawn after independent review (two blockers, eight majors)",
                                   archive="capability/history/capability_forecast_v1.0_withdrawn.json",
                                   review="capability/research/04-adversarial-review-v1.md")],
            scales=dict(
                eci_public="Epoch Capabilities Index, public, Bayesian fit of November 2026 (Claude 3.5 Sonnet = 130, GPT-5 = 150). Modelling scale.",
                aeci_own_card="AECI as printed in the model's own system card. Modelled directly; judgement-heavy. This is what is graded.",
                aeci_nov6="AECI on the November 6 2026 fit, through a level mapping from public ECI. Secondary."),
            interval_convention="median with central 50%, 80% and 95% intervals (lo50/hi50, lo80/hi80, lo95/hi95); null where undefined",
            caveats=[
                "Small samples: 25 Claude models with a public ECI, 21 within-family steps, 8 own-card AECI values, 13 models linking AECI to ECI.",
                "The next-model point forecast is, in effect, 'predecessor + recent record-line slope x elapsed time'. Nothing more elaborate tested better.",
                "Backtest evidence stops at six months ahead (4 folds; 3 with the date unknown, all under-predictions). Haiku's forecast is beyond it.",
                "All backtest folds lie in 2024-26, one regime of rising pace. Every method under-predicted in it.",
                "Beyond about 1.5 years the bands are a scenario projection driven by stated priors, not a validated forecast.",
                "Above the measured-scale threshold (see scale) today's benchmark basket no longer identifies the scale; values there are flagged, not meaningful measurements.",
                "Frontier paths on the 'hold' and faster scenarios carry a pooled under-prediction correction whose out-of-sample test is thin (see projection.bias_term).",
                "Both indices are re-estimated on every update. AECI rests on first-party internal benchmarks; own-card predictions are judgement with a wide band.",
                "Benchmark predictions are anchored on each family's last score; families near a ceiling get a saturation statement instead.",
                "Release dates come from the site's release forecaster; its errors pass straight through.",
                "The model cannot see regime changes it has no data on (new architectures, export controls, a compute shock, a pause).",
            ],
            plots=plots),
        headline=R["headline"], history=history(R), scale=R["scale"], trend=R["trend"], families=R["families"], aeci=R["aeci"],
        links=R["links"], next_models=R["next_models"], projection=R["projection"],
        backtest=dict(machine=R["machine_backtest"], release=R["release_backtest"], irt_refit_check=R["irt_refit_check"],
                      benchmarks=dict(design=R["links"]["backtest_design"], by_benchmark={r["benchmark"]: r["backtest"] for r in R["links"]["table"]},
                                      calibration_pooled=R["links"]["calibration_pooled"]),
                      aeci_own_card=R["aeci"]["own_card"]["backtest"]),
        reference_class=R["reference_class"], open_predictions=R["open_predictions"],
        review=[dict(finding=a, title=b, disposition=c, action=d_) for a, b, c, d_ in REVIEW],
        review_second=[dict(finding=a, title=b, disposition=c, action=d_) for a, b, c, d_ in REVIEW2],
        variants=R["variants"])
    dump_json(J, OUT / "capability_forecast.json")
    return J


def _tab(rows, cols, heads=None, fmt=None):
    heads = heads or cols
    fmt = fmt or {}
    out = ["| " + " | ".join(heads) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        cells = []
        for c in cols:
            v = r.get(c)
            if v is None or (isinstance(v, float) and not np.isfinite(v)):
                cells.append("-")
            elif c in fmt:
                cells.append(fmt[c](v))
            elif isinstance(v, bool):
                cells.append("yes" if v else "no")
            elif isinstance(v, float):
                cells.append(f"{v:.2f}")
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def _iv(s, nd=1, lv="80"):
    if not s or s.get("median") is None:
        return "-"
    return f"{s['median']:.{nd}f} ({s['lo' + lv]:.{nd}f} to {s['hi' + lv]:.{nd}f})"


def write_methods(J):
    md = []
    A = md.append
    nm, P, rb, mb, irt, tr, ae, L = J["next_models"]["entities"], J["projection"], J["backtest"]["release"], J["backtest"]["machine"], \
        J["backtest"]["irt_refit_check"], J["trend"], J["aeci"], J["links"]
    lp = tr["level_process"]
    A(f"# Capability model: methods\n\nModel version `{MODEL_VERSION}`, as of {AS_OF}. Every number here is written by "
      "`python3 capability/run.py` from `capability/output/capability_forecast.json`; do not edit by hand.\n\n"
      "**v1 was withdrawn.** An independent adversarial review of cap-v1.0 (`research/04-adversarial-review-v1.md`) found two blockers "
      "and eight major problems: the headline backtest left out its worst fold and compared against weak baselines; several benchmark "
      "predictions contradicted scores already observed; and the long-range band was an untested prior. v1's output is kept, unedited, "
      "at `history/capability_forecast_v1.0_withdrawn.json`, and its predictions stay on file marked withdrawn. Section 14 lists each "
      "finding and what changed.\n")
    A("## 1. What is forecast, and how far to trust each part\n\n"
      "| Output | Status |\n|---|---|\n"
      "| Public ECI of the next Opus, Sonnet, Fable/Mythos (1-3 months out) | Tested on all past releases; about 2.5-3 ECI points RMSE; no better than a two-line baseline, which is its core |\n"
      "| Public ECI of the next Haiku (about 8 months out) | Outside anything tested |\n"
      "| Benchmark scores of the next models | Anchored on each family's last score; thinly tested (2-16 folds per benchmark) |\n"
      "| AECI as printed in the model's own card | Judgement-heavy estimate from eight cards; wide band |\n"
      f"| Frontier to {P['backtested_through']} | The uncorrected code was backtested at this horizon and under-predicted; the published, corrected configuration is tested only to six months |\n"
      "| Frontier beyond that, to 2030 | Scenario projection driven by stated priors |\n\n"
      "**Primary scale.** " + ae["primary_scale"] + "\n")
    A("## 2. Data\n\n`build_data.py` writes the canonical tables under `capability/data/` and logs every rename, date conflict, merge and "
      "dropped row in `build_log.csv` (v2: every non-exact name match is logged, and dated variants of a model no longer merge into a "
      "sibling). Nothing is interpolated. Models: 256 with a public ECI plus the Claude releases Epoch does not score. Index values: "
      "public ECI with 90% credible intervals and Epoch's 500 joint posterior draws; every AECI value Anthropic has printed, by card. "
      "Benchmark scores: one row per benchmark and model in one stated configuration. Release dates for the next models come from "
      "`forecast/output/forecast.json`.\n")
    a_ = lp["anthropic"]
    A("## 3. The level process\n\nOne process produces the record line for both layers of the model.\n\n"
      "- **Fit.** Record-setting releases since Claude 3 Opus. Level now and recent slope are drawn with equal weight from three "
      "recent-trend forms: trailing-12-month line, trailing-24-month line, and the last segment of a piecewise line with unknown "
      "changepoint. v1's stacking over seven forms is gone: its weights were corner solutions that flipped between forms, and the "
      "all-history forms under-predicted in every fold.\n"
      "- **Uncertainty.** " + lp["bootstrap"] + "\n"
      "- **Paths.** From today, pace(t) = kappa x log10(compute growth) + a0 x m(t), with a scenario for m(t) drawn per path (section 10), "
      "plus a random walk whose annual sd is the sd of past 12-month frontier gains.\n"
      "- **Correction.** On the 'hold' and faster scenarios only, beta x g(h) is added to the Anthropic line, with beta pooled across both "
      "frontier series and g tapering in from zero and out by 1.5 years (section 7.2).\n"
      "- **Frontier.** The running maximum held at T is max(leader's own value drawn from Epoch's posterior, line level lagged by the "
      "standing record's age + scatter).\n\n"
      f"Anthropic today: level {_iv(a_['level_now'])}, recent slope {_iv(a_['recent_slope'])} ECI/yr, pre-break slope "
      f"{_iv(a_['pre_break_slope'])}, total slope ratio {_iv(a_['total_slope_ratio'], 2)}. {lp['like_for_like']} "
      f"All labs: recent slope {_iv(lp['all_lab']['recent_slope'])}. {lp['all_lab']['note']}\n\n### Was there a break?\n\n" +
      _tab([dict(series=k, lw=v["linear"]["bic_weight"], hw=v["hinge"]["bic_weight"], jw=v["jump"]["bic_weight"], qw=v["quadratic"]["bic_weight"],
                 pre=v["hinge"]["slope_pre"], post=v["hinge"]["slope_post"], ratio=v["hinge"]["ratio"], n=v["hinge"]["n"])
            for k, v in (("Anthropic, public ECI", tr["anthropic_public_eci"]), ("All labs, public ECI", tr["all_lab_public_eci"]),
                         ("AECI Nov 6 fit, public dates", tr["aeci_nov6_public_dates"]),
                         ("AECI Nov 6 fit, internal dates + internal model", tr["aeci_nov6_internal_dates_with_internal_model"]))],
           ["series", "n", "lw", "hw", "jw", "qw", "pre", "post", "ratio"],
           ["Series", "n", "BIC wt linear", "hinge", "jump", "quadratic", "Slope before", "after", "Ratio"]) +
      "\n\nAnthropic's public-ECI records bend upward; the all-lab frontier does not; the card's 1.88x on AECI is reproduced only with "
      "internal dates and the unreleased internal model. The other labs' line is fitted on non-Anthropic records only; "
      f"{lp['all_lab']['share_of_slope_draws_clipped']:.0%} of its slope draws hit the clipping bounds.\n")
    F = J["families"]
    A("## 4. Next model in a family\n\n" + F["gain_model"]["note"] + "\n\n"
      "The line gain is the recent slope times the time already elapsed since the predecessor, plus the simulated path from today to the "
      "release date (drawn from the release forecaster). c and s are the median and robust sd of log(actual step / line gain) over the "
      f"{F['gain_model']['n_steps']} past within-family steps: c = {F['gain_model']['median_log_ratio']}, s = {F['gain_model']['log_sd']}. "
      f"Measurement sd {F['gain_model']['measurement_sd']} ECI (Epoch's posterior sd for recent Anthropic models). "
      "This is the reviewer's two-line baseline with a distribution around it. " + F["twin"] + "\n\n" + F["offsets_note"] + "\n")
    oc = ae["own_card"]
    A("## 5. AECI\n\n### Own card (primary AECI output)\n\n" + oc["method"] + "\n\n" +
      _tab(oc["table"], ["card", "model_id", "aeci_own", "eci", "gap"], ["Card", "Model", "Own-card AECI", "Public ECI (today's fit)", "Gap"]) +
      f"\n\nPredicted gap {oc['summary']['predicted_gap']:+.2f}, sd {oc['summary']['sd']}. Rolling test (each card predicted from the three before it):\n\n" +
      _tab(oc["backtest"], ["model_id", "predicted_gap", "actual_gap", "error", "last_gap_rule_error"],
           ["Card", "Predicted gap (blend)", "Actual", "Error", "Error of 'last gap' rule"]) +
      f"\n\nRMSE {oc['summary']['rolling_rmse']}, mean error {oc['summary']['rolling_mean_error']:+.2f} (mean-of-three alone: "
      f"{oc['summary']['rolling_rmse_mean_of_last_3']}; last gap alone: {oc['summary']['rolling_rmse_last_gap_rule']}). "
      + oc["label"] + " " + oc["conditional"] + "\n\n### November 6 scale (secondary)\n\n"
      f"A level mapping fitted on 13 Claude models (hinge above a knee, or a one-time level shift; the forecast mixes them "
      f"{1 - ae['nov6_mapping']['p_level_shift_form']:.1f}/{ae['nov6_mapping']['p_level_shift_form']:.1f}). Leave-one-out RMSE "
      f"{ae['nov6_mapping']['leave_one_out_rmse']}; residual sd used {ae['nov6_mapping']['residual_sd_used']}. Caveats: " +
      " ".join(ae["nov6_mapping"]["caveats"]) + "\n\n### Refits\n\n" + ae["refits"]["note"] + "\n")
    A("## 6. Benchmarks\n\n" + L["method"] + "\n\n" +
      _tab([dict(t=r["title"], kind=r["kind"], n=r["n"], ceil=r.get("ceiling"), est=r.get("ceiling_estimated"), best=r["best_observed"],
                 adm=(r.get("tier") or "no"), nb=(r["backtest"] or {}).get("n"), ma=(r["backtest"] or {}).get("mae_anchored"),
                 mc=(r["backtest"] or {}).get("mae_curve_level"), mp=(r["backtest"] or {}).get("mae_prev_in_family"), cv=(r["backtest"] or {}).get("cov80"), bi=(r["backtest"] or {}).get("bias_anchored"))
            for r in L["table"]], ["t", "kind", "n", "ceil", "est", "best", "nb", "ma", "mc", "mp", "bi", "cv", "adm"],
           ["Benchmark", "Link", "Models", "Ceiling", "Estimated", "Best observed", "Backtest folds", "MAE anchored", "MAE v1 curve level",
            "MAE previous-in-family", "Bias", "80% coverage", "Status"]) +
      "\n\n**Admission rule.** " + L["admission_rule"] + "\n\nWhy each indicative benchmark is not graded:\n\n" +
      "\n".join(f"- **{next(r['title'] for r in L['table'] if r['benchmark'] == k)}**: {'; '.join(L['tiers'][k]['reasons'])}." for k in L["indicative"]) +
      "\n\nNot published at all:\n\n" + "\n".join(f"- **{x['title']}**: {x['reason']}." for x in L["excluded"]) +
      "\n\nSaturation statements (published instead of numbers for families at the ceiling):\n\n" +
      "\n".join(f"- {x['statement']} Families at or above 90%: {', '.join(x['families_at_or_above_90pct']) or 'none'}." for x in L["saturation_statements"]) +
      f"\n\nPooled over benchmarks, anchored intervals cover {L['calibration_pooled']['raw_cov50']:.0%} / {L['calibration_pooled']['raw_cov80']:.0%} / "
      f"{L['calibration_pooled']['raw_cov95']:.0%} at nominal 50 / 80 / 95% ({L['calibration_pooled']['n_folds']} fold-benchmarks); the 50% "
      f"intervals are stretched by {L['calibration_pooled']['factor50']}; the 80% and 95% factors are 1 (no-op).\n")
    A("## 7. Backtests\n\n### 7.1 Claude releases, all folds\n\n" + rb["design"] + "\n")
    names = {"model": "Model, date given", "model_date_unknown": "**Model, date not given**", "prev_plus_slope": "Baseline: previous + 12-month Anthropic slope x elapsed (date given)",
             "prev_plus_slope_date_unknown": "Baseline: same, date not given", "prev_in_family": "Baseline: previous model in family",
             "family_mean_step": "Baseline: previous + family's mean step", "trailing_12m_linear": "Baseline: trailing-12-month all-lab line",
             "all_history_linear": "Baseline: all-history all-lab line"}
    for ld, lab in (("0.0", "Day-of (lead 0)"), ("0.25", "3 months ahead"), ("0.5", "6 months ahead")):
        s = rb["summary_by_lead"][ld]
        A(f"**{lab}**\n\n" + _tab([dict(method=names[k], **s[k]) for k in names if k in s],
                                   ["method", "n", "bias", "mae", "rmse", "crps", "cov50", "cov80", "cov95"],
                                   ["Method", "n", "Bias (actual - predicted)", "MAE", "RMSE", "CRPS", "Cov 50%", "Cov 80%", "Cov 95%"]) + "\n")
    A("Paired differences in absolute error (model minus baseline; negative = model better), bootstrap 90% interval over folds:\n\n" +
      _tab(rb["paired_differences"], ["lead_years", "date", "b", "n", "mae_a", "mae_b", "diff", "lo90", "hi90", "a_better_in"],
           ["Lead (yr)", "Date", "Baseline", "n", "MAE model", "MAE baseline", "Difference", "90% low", "90% high", "Folds model better"]) +
      "\n\n**Verdict.** " + rb["verdict"] + "\n\n**What the sample supports.** " + rb["what_n_supports"] + "\n\n"
      f"Within-family steps: {rb['within_family_steps']['n']} observed, {rb['within_family_steps']['n_negative']} negative, smallest "
      f"+{rb['within_family_steps']['min']}. Variants tested on the same folds (no bias term; no step ratio; record line + pooled family "
      "offset; a stacked mix of the two) are in the JSON; none is better beyond noise. Monte Carlo noise: a second seed gives RMSE " +
      ", ".join(f"{m['rmse_seed_b']} vs {m['rmse_seed_a']} at {m['lead_years']} yr" for m in rb["monte_carlo_noise"]) + ".\n")
    A("### 7.2 The projection code itself\n\n" + mb["design"] + "\n")
    co = mb["correction"]
    for key, lab in (("anthropic", "Anthropic frontier"), ("all_lab", "All-lab frontier")):
        m = mb[key]
        A(f"**{lab}** ({m['n_folds']} folds, {m['n_origins']} origins, {m['n_distinct_outcomes']} distinct outcomes)\n\n" +
          _tab(m["table"], ["horizon_years", "variant", "n", "n_with_nonzero_correction", "bias", "mae", "rmse", "crps", "cov50", "cov80", "cov95"],
               ["Horizon (yr)", "Variant", "n", "Folds with a correction", "Bias", "MAE", "RMSE", "CRPS", "Cov 50%", "Cov 80%", "Cov 95%"]) +
          "\n\nCalibration factors (50/80/95%), fitted on 'published_config': " +
          "; ".join(f"{h} yr: {c['factor50']}/{c['factor80']}/{c['factor95']}" for h, c in m["calibration"].items()) + ".\n")
    A("**The correction.** The uncorrected process under-predicted both frontiers in this window. Block by block (half-years of origin), the "
      "slope of error on horizon was:\n\n" + _tab(co["blocks"], ["series", "block", "n", "beta", "se"], ["Series", "Origins in", "Folds", "Slope (ECI/yr)", "se"]) +
      f"\n\n| Estimate | ECI/yr |\n|---|---|\n| Anthropic series alone (unshrunk; v2.0 used this x 0.8) | {co['unshrunk']['anthropic']} |\n"
      f"| All-lab series alone | {co['unshrunk']['all_lab']} |\n| Random-effects pooled mean (used) | {co['pooled']['mu']} (se {co['pooled']['se']}) |\n"
      f"| Between-block sd | {co['pooled']['between_block_sd']} |\n| Predictive sd for a new block (used as the term's sd) | {co['pooled']['predictive_sd']} |\n\n"
      + co["why_pooled"] + " Shape: " + co["shape"] + f". Applied to: {', '.join(co['applies_to'])}. Not applied to: {', '.join(co['not_applied_to'])} "
      "(slowdown and reversion are the claim that the recent pace does not persist; the other labs' backtest rejected a correction). "
      f"Size: {co['size_at_end_2027']} ECI on those paths at end-2027, {co['permanent_size_after_1_5_years']} from mid-2028 on. " + co["thin_test"] +
      " 80% and 95% bands covered throughout; the 50% band was too narrow around a biased median, which the 50% factor repairs where it is above 1. "
      "Factors equal to 1 are a no-op.\n")
    A("### 7.3 Leave-future-out IRT refit\n\n" + irt["design"] + " " + irt["v1_bug"] + "\n\n"
      f"Reproduction on all data: correlation {irt['full_data_reproduction']['corr']} with Epoch's ECI, RMSE {irt['full_data_reproduction']['rmse_above_140']} "
      f"above ECI 140. Target shift, vintage vs published: mean absolute {irt['target_shift']['mean_abs']}, max {irt['target_shift']['max_abs']} "
      f"over {irt['target_shift']['n']} folds.\n\n" +
      _tab([dict(lead=k, meth=m, n=v[m]["n"], rv=v[m]["vintage"]["rmse"], rp=v[m]["published"]["rmse"], bv=v[m]["vintage"]["bias"], bp=v[m]["published"]["bias"])
            for k, v in irt["comparison_by_lead"].items() for m in v], ["lead", "meth", "n", "rv", "rp", "bv", "bp"],
           ["Lead (yr)", "Method", "n", "RMSE vintage", "RMSE published", "Bias vintage", "Bias published"]) + "\n\n" + irt["caveat"] + "\n")
    cal = rb["calibration"]
    A("## 8. Calibration\n\nConformal-style: per nominal level, the factor by which an interval must be stretched about its median to cover "
      "the stated share of backtest outcomes, learned from earlier folds when scoring and from all folds for the live forecast; floored at 1.\n\n" +
      _tab([dict(set="Ability, date given, lead 0", **cal["date_given_lead_0"]), dict(set="Ability, date not given, 3-6 months", **cal["date_unknown_leads_3_6_months"]),
            dict(set="Benchmarks, anchored, pooled", **L["calibration_pooled"])],
           ["set", "n_folds", "raw_cov50", "raw_cov80", "raw_cov95", "factor50", "factor80", "factor95", "factor80_unfloored"],
           ["Set", "Folds", "Raw 50%", "Raw 80%", "Raw 95%", "Factor 50%", "80%", "95%", "80% factor before floor"]) +
      "\n\nFor ability the raw intervals already cover at or above nominal on all folds, so the factors are 1 and calibration changes "
      "nothing there. That is a statement about the folds we have, not about longer leads. The frontier bands use the factors in 7.2.\n")
    A("## 9. Next-model predictions\n\n" + J["next_models"]["note"] + "\n\n" +
      _tab([dict(e=v["predicted_name"], d=f"{v['release_date']['median']} ({v['release_date']['q10']} to {v['release_date']['q90']})",
                 prev=v["previous_eci"], eci=_iv(v["eci"]), e95=f"{v['eci']['lo95']:.1f} to {v['eci']['hi95']:.1f}", own=_iv(v["aeci_own_card"]),
                 n6=_iv(v["aeci_nov6_scale"]), pr=v["p_regression_below_predecessor"], tested=v["lead_tested"]) for v in nm.values()],
           ["e", "d", "prev", "eci", "e95", "own", "n6", "pr", "tested"],
           ["Next model", "Release (median, 10-90%)", "Predecessor ECI", "Public ECI (80%)", "95%", "AECI own card (80%)", "AECI Nov 6 scale (80%)",
            "P(below predecessor)", "Lead within tested range"], {"pr": lambda v: f"{v:.1%}"}) + "\n\nBenchmarks (median, 80% interval; 'saturated' = statement only; '-' = the family's latest model has no score to anchor on). Only graded rows enter the scorecard:\n\n" +
      _tab([dict(b=next(r["title"] for r in L["table"] if r["benchmark"] == k),
                 st=("graded" if k in L["graded"] else "indicative"),
                 **{e: (_iv(v["benchmarks"][k], 0 if v["benchmarks"][k].get("median", 0) > 300 else 1) if v["benchmarks"][k].get("available")
                        else ("saturated" if v["benchmarks"][k].get("saturated") else "-")) for e, v in nm.items()}) for k in L["admitted"]],
           ["b", "st", "opus", "sonnet", "haiku", "fable_mythos"], ["Benchmark", "Status", "Opus", "Sonnet", "Haiku", "Fable / Mythos"]) + "\n")
    A("## 10. Projection to 2030\n\n" + P["validation_statement"] + "\n\n### Scenarios\n\n" +
      _tab([dict(s=r["scenario"], d=r["definition"], p27=f"{r['pace_anthropic_2027']['median']} ({r['pace_anthropic_2027']['lo80']} to {r['pace_anthropic_2027']['hi80']})",
                 u27=r["pace_anthropic_2027_without_correction_median"], p28=r["pace_anthropic_2028"]["median"], p30=r["pace_anthropic_2030"]["median"],
                 b27=r["share_below_pre_break_2027"], e30=r["end_2030_anthropic_frontier_median"]) for r in P["scenarios"]],
           ["s", "d", "p27", "u27", "p28", "p30", "b27", "e30"],
           ["Scenario", "Definition", "Record-line gain in 2027, correction included (80%)", "Same, without correction", "2028", "2030",
            "Share of paths below pre-break pace, 2027", "Frontier, end-2030 (median)"]) +
      f"\n\nMixture: {P['mixture_pace_2027']['realised_gain_2027_median']} ECI gained in 2027 ({P['mixture_pace_2027']['without_correction_median']} without "
      f"the correction); pre-break pace {P['mixture_pace_2027']['pre_break_slope_median']}, recent pace {P['mixture_pace_2027']['recent_slope_median']}." +
      "\n\n### Weights\n\n" + P["weights_are"] + "\n\n" +
      _tab([dict(w=k, **v) for k, v in P["weights"].items()], ["w", "slowdown", "reversion", "hold", "compounding", "explosive"],
           ["Weighting", "Slowdown", "Reversion", "Hold", "Compounding", "Explosive"]) +
      "\n\nWhy the central prior looks as it does. For reversion or slower (40%): the all-lab frontier shows no break; the AECI result depends "
      "on the link function and on unreleased models; compute growth cannot stay at 5x/yr; scenario-style forecasts have run at 60-75% of "
      "predicted pace. For hold (38%): Anthropic's public-ECI records do bend, and the two earlier breaks in the reference class both "
      "persisted for a year or more. For compounding and explosive (22%): Anthropic's S-1/A says the AI R&D threshold is met on the "
      "'expect' prong; point forecasters have under-predicted benchmark progress. The unweighted evidence average: " +
      P["evidence_average_detail"]["warning"] + "\n\n### Results (central weights; mixture bands calibrated)\n\n" +
      _tab([dict(d=h["date"], e80=_iv(h["anthropic_eci"]), e95=f"{h['anthropic_eci']['lo95']:.0f} to {h['anthropic_eci']['hi95']:.0f}",
                 o=_iv(h["non_anthropic_eci"]), l=_iv(h["all_lab_eci"]), ld=h["share_of_paths_anthropic_leads"], a=_iv(h["anthropic_aeci_nov6_scale"]),
                 fl=h["anthropic_eci"]["median_beyond_measured_scale"], sh=h["anthropic_eci"]["share_of_paths_beyond_measured_scale"]) for h in P["headline"]],
           ["d", "e80", "e95", "o", "l", "ld", "a", "fl", "sh"],
           ["Date", "Anthropic frontier, public ECI (80%)", "95%", "Other labs' frontier (80%)", "All-lab frontier = larger of the two (80%)",
            "Anthropic leads in", "AECI Nov 6 scale, secondary (80%)", "Median beyond measured scale", "Share of paths beyond it"],
           {"sh": lambda v: f"{v:.0%}", "ld": lambda v: f"{v:.0%}"}) +
      "\n\nLayer agreement: the frontier median is never below the median implied by the next-model layer's own draws (largest shortfall "
      f"{P['layer_agreement']['max_shortfall']} ECI across quarters).\n" +
      f"\n\n**Measured scale.** {J['scale']['rule']} Range: {J['scale']['range_eci'][0]} to {J['scale']['range_eci'][1]}; shaded from "
      f"{J['scale']['beyond_measured_scale_above_eci']}; display cap {J['scale']['display_cap_eci']:.0f}. At today's frontier "
      f"{J['scale']['share_of_basket_90pct_solved_at_frontier_now']:.0%} of the basket is already 90% solved.\n\n"
      "### Sensitivity to the prior\n\n" +
      _tab([s for s in P["sensitivity"] if s["series"] == "anthropic_frontier_eci"], ["weighting", "date", "median", "lo80", "hi80"],
           ["Weighting", "Date", "Median", "80% low", "80% high"], {k: (lambda v: f"{v:.0f}") for k in ("median", "lo80", "hi80")}) +
      "\n\n### Research note 1's central path\n\n" + P["reconciliation_with_research_note_1"]["explanation"] +
      f" Note 1: +65, about {P['reconciliation_with_research_note_1']['research_note_1_central_level_2030']:.0f} by end-2030. Ours, all-lab: " +
      ", ".join(f"{k} {v:.0f}" for k, v in P["reconciliation_with_research_note_1"]["ours_all_lab_by_scenario"].items()) +
      f"; mixture median {P['reconciliation_with_research_note_1']['ours_all_lab_median_2030']:.0f}.\n\n### Time horizon\n\n" + P["metr_horizon"]["statement"] +
      "\n\n### Against external forecasts\n\n" + _tab(P["external_comparison"], ["source", "quantity", "theirs", "ours", "why"],
                                                      ["Source", "Quantity", "Theirs", "Ours", "Why they differ"]) + "\n")
    A("## 11. Assumptions that are not estimated\n\n| Assumption | Value | Source |\n|---|---|---|\n"
      "| Residual distribution | Student-t, 4 df | robustness choice |\n| Floor on trend residual scale | 0.75 ECI | Epoch posterior sd at the frontier is 1-2 points |\n"
      "| Recent-trend forms and their weights | three forms, equal | review decision; all-history forms under-predict |\n"
      "| Correction: which scenarios, and its taper | hold and faster; in from 0, peak at 0.5 yr, out by 1.5 yr | second-review decision |\n"
      "| Gain floor; log-ratio sd floor | 0.3 ECI; 0.25 | keep the multiplicative step defined |\n"
      "| ECI per 10x compute | 9 +/- 2 | research note 1 |\n| Compute growth paths | low / central / high | `driver_scenarios_2026_2030.csv` |\n"
      "| Multiplier ranges per scenario; 60-100% realisation haircut | scenario table | research note 3; AI 2027 ran at 58-75% of pace |\n"
      "| Scenario weights | table above | prior |\n| Own-card gap rule and its widening with refits | mean of last three; sqrt(1 + 0.25(K-1)) | judgement |\n"
      "| Mapping-form probability clip | 0.2 to 0.8 | 13 points cannot exclude either form |\n"
      "| Saturation and staleness thresholds | 90% of ceiling; six months | review decision |\n"
      "| Family offset drift (post-2027 family paths) | 1.5 ECI per sqrt(year) | judgement |\n| Fable = Mythos | identical | Anthropic |\n")
    A("## 12. Limitations\n\n" + "\n".join(f"- {c}" for c in J["metadata"]["caveats"]) + "\n"
      "- Machine-backtest folds overlap (monthly origins, horizons up to 1.5 years): 30 Anthropic folds are about three independent half-years.\n"
      "- The scenario weights used in the backtest are today's prior; the backtest tests the code and the bias, not the weights.\n"
      "- Links use ability point estimates and, for site charts, Claude models only. OSWorld mixes three eval versions; HLE and SWE-bench Pro are first-party.\n"
      "- Public ECI for past models is today's fit (the vintage check suggests this matters little).\n")
    A("## 13. What would change the forecast\n\n"
      "- The next two Anthropic record-setters: near the 20-25 ECI/yr line supports 'hold'; two near 15 shifts weight to reversion.\n"
      "- Epoch scoring more of Fable 5.2 (19 benchmarks so far): it anchors the level and every Fable/Mythos prediction.\n"
      "- The next card's own-card gap: it is the whole basis of the AECI forecast.\n"
      "- Other labs' frontier bending upward would weaken the 'no industry-wide break' evidence.\n"
      "- New, harder benchmarks entering Epoch's basket would raise the measured-scale ceiling.\n- Delivered compute against the S-1 commitments; export restrictions.\n")
    A("## 14. What the reviews changed\n\n### First review (v1 -> v2.0)\n\n" +
      _tab(J["review"], ["finding", "title", "disposition", "action"], ["Finding", "Issue", "Disposition", "What was done"]) +
      "\n\n### Second review (v2.0 -> v2.1)\n\nVerdict: no blockers; publishable after targeted fixes (`research/05-adversarial-review-v2.md`). "
      "v2.0's output is archived at `history/capability_forecast_v2.0_superseded.json`.\n\n" +
      _tab(J["review_second"], ["finding", "title", "disposition", "action"], ["Finding", "Issue", "Disposition", "What was done"]) +
      "\n\nWhat moved:\n\n" + "\n".join(f"- {c}" for c in J["headline"]["changes_since_previous"]) + "\n")
    V = J["variants"]["with_model_4"]
    m4, asm = V["model_4"], V["assumptions"]
    dl = V["delta_vs_default"]
    drow = lambda r: dict(item=r["item"], d=f"{r['default']['median']:.1f} ({r['default']['lo80']:.1f} to {r['default']['hi80']:.1f})",
                          v=f"{r['with_model_4']['median']:.1f} ({r['with_model_4']['lo80']:.1f} to {r['with_model_4']['hi80']:.1f})",
                          x=f"{r['difference']['median']:+.1f}")
    A("## 15. Anthropic's unreleased internal model (METR's Model 4)\n\n"
      f"**What is known.** The Fable 5.2 / Mythos 5.2 card prints 'a separate, unreleased internal research model that is somewhat more capable "
      f"than Claude Mythos 5.2': AECI {m4['aeci_nov6']} on the November 6 fit (global 95% {m4['aeci_global_ci95'][0]} to {m4['aeci_global_ci95'][1]}; "
      f"local {m4['aeci_local_ci95'][0]} to {m4['aeci_local_ci95'][1]}), scored on {m4['n_benchmarks']} benchmarks, plotted at an internal date of about "
      f"{m4['internal_date_figure_read']}. METR's November 5 assessment describes 'Model 4' (finished training {m4['metr_training_finished']}; "
      f"AECI {m4['metr_value']}, or {m4['metr_value_dropping_3_suspect_benchmarks']} dropping three suspect benchmarks; above 50% on all 15 benchmarks "
      "it was tested on, which makes METR 'somewhat nervous about our ability to measure AECI'). " + m4["identification"] + " " + m4["models_2_and_3"] +
      "\n\n**Why the default excludes it.** It is unreleased and has no public ECI; its score rests on 15 of Anthropic's internal benchmarks, all "
      "above 50%; its date is an internal-availability date while every other point in the model is at its public date; and it is already "
      f"{m4['days_since_internal_date']} days past that date with no release. In the default it appears only as a comparison "
      "(`p_aeci_nov6_at_or_above_internal_model`). The default's numbers and open predictions are identical to cap-v2.1.\n\n"
      "**What the variant assumes** (`variants.with_model_4`; a what-if, not graded). It re-weights the default's own simulated paths by three "
      "separately switchable pieces of evidence.\n\n"
      f"- *Level.* Model 4's public-ECI equivalent is {m4['eci_equivalent']['median']} (80% {m4['eci_equivalent']['lo80']} to {m4['eci_equivalent']['hi80']}): "
      + m4["eci_equivalent"]["method"] + ". " + asm["lag"]["treatment"] + f" Remaining lag: {asm['lag']['remaining_lag']}. The record line at that date is "
      f"weighted by how well it matches (sd {asm['level_likelihood_sd']}, the scatter of record-setters about the line).\n"
      f"- *Next release.* With probability p = {asm['p_next_frontier_release_is_model_4_or_better']} the next Fable/Mythos is Model 4 or at least as capable, "
      f"so its draws are truncated below at Model 4's level ({asm['p_draws_already_at_or_above_model_4']:.0%} of the default's draws already are). "
      + asm["p_basis"] + "\n"
      f"- *Trend.* " + asm["trend"]["channel"] + f" BIC weight on 'jump or no change' for the AECI series: {asm['trend']['aeci_bic_weight_on_jump_or_no_change']['public_dates_without_internal_model']} "
      f"without the internal model, {asm['trend']['aeci_bic_weight_on_jump_or_no_change']['internal_dates_with_internal_model']} with it; four-line average "
      f"{asm['trend']['p_revert_four_line_average']['without_internal_model']} to {asm['trend']['p_revert_four_line_average']['with_internal_model']}; reversion weight "
      f"{asm['trend']['weights_before']['reversion']} to {asm['trend']['weights_after']['reversion']}, hold {asm['trend']['weights_before']['hold']} to "
      f"{asm['trend']['weights_after']['hold']}. " + asm["trend"]["caveat"] + "\n\n**Results (median, 80% interval).**\n\n" +
      _tab([drow(r) for r in dl["next_models_eci"]] + [dict(drow(r), item="Anthropic frontier, " + r["item"]) for r in dl["anthropic_frontier_eci"]],
           ["item", "d", "v", "x"], ["Public ECI", "Default", "With Model 4", "Median shift"]) + "\n\nBy component (shift in the median):\n\n" +
      _tab([dict(c=r["components"], f=r["fable_mythos_shift"], o=r["opus_shift"], y27=r["frontier_shift"]["2027"], y28=r["frontier_shift"]["2028"],
                 y30=r["frontier_shift"]["2030"], ess=r["effective_sample_size"]) for r in V["components"]["table"]],
           ["c", "f", "o", "y27", "y28", "y30", "ess"],
           ["Components on", "Fable/Mythos 5.3", "Opus 5.6", "Frontier end-2027", "end-2028", "end-2030", "Effective paths"],
           {k: (lambda v: f"{v:+.2f}") for k in ("f", "o", "y27", "y28", "y30")}) +
      "\n\nSensitivity to p (all components on): " +
      "; ".join(f"p={r['p']}: Fable/Mythos {r['next_models_eci_median']['fable_mythos']:.1f}, frontier end-2027 {r['anthropic_frontier_eci_median']['2027']:.1f}" for r in V["p_sensitivity"]) +
      ". Differences of a tenth or two between rows are Monte Carlo noise. Reading: Model 4 moves the next Fable/Mythos by under a point, because "
      "the default already expects the next release to be about that good; nearly all of the long-range shift comes from the trend component, "
      "which is the weakest of the three.\n")
    (ROOT / "METHODS.md").write_text("\n".join(md))
