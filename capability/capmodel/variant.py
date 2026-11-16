"""What-if variant 'with Model 4' (cap-v2.2). NOT graded; the default forecast is untouched.

Anthropic's Fable 5.2 / Mythos 5.2 system card prints an unreleased internal research model
at AECI 178.78 (Nov 6 fit; 15 benchmarks; internal date ~2026-09-26). METR's Nov 5
assessment calls its most capable internal model 'Model 4' (AECI 178.6, 15 benchmarks).
The default forecast does not use it. This module re-weights the default's own simulated
paths (importance weights; nothing is re-simulated, so the default's numbers cannot move)
by three separately switchable pieces of evidence:

  a  level    a pseudo-observation of Anthropic's record line: a model of public-ECI
              equivalent E4 at a public-date-equivalent T4 = today + remaining lag
  b  next     with probability p the next Fable/Mythos release is Model 4 or a successor at
              least as capable (its draws are truncated below at E4); with 1-p Model 4 is
              never released as such and (b) says nothing
  c  trend    the scenario weight on 'reversion' is scaled down and the mass moved to 'hold',
              by the ratio of a four-line evidence average computed with and without the
              internal model on the AECI series (never by more than half)
"""
from __future__ import annotations
import numpy as np
import pandas as pd

from .common import RAW, AS_OF, yr, widen, rng as mkrng, wquantile

M4_AECI, M4_LOCAL = 178.78, (177.08, 180.59)            # card Table 2.3.5.3.A, Nov 6 fit
MYTHOS52_AECI, MYTHOS52_LOCAL = 177.12, (175.75, 178.48)
M4_INTERNAL_DATE = "2026-09-26"                          # figure read, +/- 3 days
P_RELEASE = 0.7                                          # judgement; sensitivity 0.5 / 0.9
REMAINING_LAG_MEAN_DAYS = 45.0                           # judgement: about the last observed lag (47 days)
MAP_SD = 1.0                                             # model-specific scatter of (AECI - ECI) among same-fit frontier models
MAX_TREND_SHIFT = 0.5                                    # (c) may remove at most half of the reversion weight
COMBOS = {"level_only": "a", "next_release_only": "b", "trend_only": "c", "level_and_next_release": "ab", "all": "abc"}


def run(c):
    N, T_NOW = len(c["scn"]), yr(AS_OF)
    r = mkrng("variant-model4")
    lag_tab = pd.read_csv(RAW / "aeci_internal_dates.csv")
    lags = lag_tab.dropna(subset=["lag_days"])[["model", "lag_days"]]
    elapsed = (pd.Timestamp(AS_OF) - pd.Timestamp(M4_INTERNAL_DATE)).days
    # --- Model 4 on the public-ECI working scale: Fable 5.2's ECI + the same-fit AECI difference to its twin Mythos 5.2
    d_aeci = M4_AECI - MYTHOS52_AECI
    sd_local = float(np.hypot((M4_LOCAL[1] - M4_LOCAL[0]) / 3.92, (MYTHOS52_LOCAL[1] - MYTHOS52_LOCAL[0]) / 3.92))
    fable_eci, fable_sd = float(c["fable_eci"]), float(c["fable_eci_sd"])
    sd_e = float(np.sqrt(sd_local ** 2 + MAP_SD ** 2 + fable_sd ** 2))
    # per path, drawn independently of everything else in the path (so the evidence cannot act by re-weighting the leader's own draw)
    E4 = fable_eci + d_aeci + sd_e * r.standard_normal(N)
    T4 = T_NOW + r.exponential(REMAINING_LAG_MEAN_DAYS / 365.25, N)
    L4 = c["lpA"].at(c["PA"], T4)
    S = c["lpA"].S
    # (a) level: likelihood of the pseudo-observation given each path's record line at T4
    wa = np.exp(-0.5 * ((E4 - L4) / S) ** 2)
    wa /= wa.mean()
    # (b) next Fable/Mythos >= Model 4, with probability p
    th = c["keep"]["fable_mythos"]["theta"]
    ok = th >= E4
    p_ok = float(ok.mean())

    def wb(p):
        return p * ok / p_ok + (1 - p)
    # (c) trend: shift scenario weight from reversion to hold
    ev = c["ev_detail"]
    without = np.mean([ev["p_revert_reference_class"], ev["p_revert_anthropic_public_bic"], ev["p_revert_all_lab_bic"], c["p_rev_aeci_public"]])
    with_ = np.mean([ev["p_revert_reference_class"], ev["p_revert_anthropic_public_bic"], ev["p_revert_all_lab_bic"], c["p_rev_aeci_internal"]])
    ratio = float(max(with_ / without, 1 - MAX_TREND_SHIFT))
    W0 = c["W_central"]
    moved = W0["reversion"] * (1 - ratio)
    W1 = dict(W0, reversion=round(W0["reversion"] - moved, 4), hold=round(W0["hold"] + moved, 4))
    wc_ = np.ones(N)
    wc_[c["scn"] == 1] = W1["reversion"] / W0["reversion"]
    wc_[c["scn"] == 2] = W1["hold"] / W0["hold"]

    def weights(combo, p=P_RELEASE):
        w = np.ones(N)
        if "a" in combo:
            w = w * wa
        if "b" in combo:
            w = w * wb(p)
        if "c" in combo:
            w = w * wc_
        return w / w.sum()

    QI = {q: i for i, q in enumerate(c["QUARTERS"])}
    YE = ["2026-12-31", "2027-12-31", "2028-12-31", "2029-12-31", "2030-12-31"]
    trio = lambda s: {k: s[k] for k in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")}

    def summarise(w, tag, full=False):
        rr = mkrng("variant-resample-" + tag)
        idx = rr.choice(N, N, p=w)                       # weighted resample; then the default's own summary code runs unchanged
        u = np.full(N, 1.0 / N)
        fams = {}
        for ent, k in c["keep"].items():
            row = dict(eci=trio(widen(k["theta"][idx], c["f_ability"])), aeci_own_card=trio(widen(k["a_own"][idx], c["f_ability"])))
            for bk, s in k["bench"].items():
                row.setdefault("benchmarks", {})[bk] = trio(c["bench_summary"](bk, s[idx]))
            fams[ent] = row
        FA = c["FA"][idx]
        # other labs: a default path drawn at random from the same scenario (keeps the scenario pairing; their own forecast is not re-weighted)
        j = np.empty(N, int)
        for i in range(len(c["SCENARIOS"])):
            m = c["scn"][idx] == i
            pool_ = np.flatnonzero(c["scn"] == i)
            j[m] = rr.choice(pool_, int(m.sum()))
        FO = c["FO"][j]
        FL = np.maximum(FA, FO)
        fa, fl = c["bands"](FA, u, c["calA"], thr=c["thr"]), c["bands"](FL, u, c["calL"], thr=c["thr"])
        out = dict(families=fams, frontier={q: dict(eci=trio(fa[QI[q]]), all_lab_eci=trio(fl[QI[q]]),
                                                    share_of_paths_anthropic_leads=round(float(np.mean(FA[:, QI[q]] >= FO[:, QI[q]])), 3)) for q in YE},
                   effective_sample_size=int(round(1.0 / np.sum(w ** 2))))
        if full:
            out["series"] = dict(anthropic_frontier_eci=fa, all_lab_frontier_eci=fl,
                                 anthropic_frontier_aeci_nov6_scale=c["bands"](c["AA"][idx], u, c["calA"]))
            sc = c["scn"][idx]
            out["scenario_medians"] = {s: [dict(date=q, median=round(float(np.median(FA[sc == i][:, j])), 2)) for j, q in enumerate(c["QUARTERS"])]
                                       for i, s in enumerate(c["SCENARIOS"])}
        return out

    res = {name: summarise(weights(combo), name, full=(name == "all")) for name, combo in COMBOS.items()}
    allv = res["all"]
    D, nm, head = c["default_next"], c["default_next"], c["default_head"]
    hd = {h["date"]: h for h in head}

    def delta_row(label, dflt, var):
        return dict(item=label, default=dict(median=dflt["median"], lo80=dflt["lo80"], hi80=dflt["hi80"]),
                    with_model_4=dict(median=var["median"], lo80=var["lo80"], hi80=var["hi80"]),
                    difference=dict(median=round(var["median"] - dflt["median"], 2), lo80=round(var["lo80"] - dflt["lo80"], 2),
                                    hi80=round(var["hi80"] - dflt["hi80"], 2)))
    delta = dict(next_models_eci=[delta_row(nm[e]["predicted_name"], nm[e]["eci"], allv["families"][e]["eci"]) for e in nm],
                 next_models_aeci_own_card=[delta_row(nm[e]["predicted_name"], nm[e]["aeci_own_card"], allv["families"][e]["aeci_own_card"]) for e in nm],
                 anthropic_frontier_eci=[delta_row(q, hd[q]["anthropic_eci"], allv["frontier"][q]["eci"]) for q in YE],
                 all_lab_frontier_eci=[delta_row(q, hd[q]["all_lab_eci"], allv["frontier"][q]["all_lab_eci"]) for q in YE])
    comp = []
    for name in COMBOS:
        v = res[name]
        comp.append(dict(components=name, switches=dict(level="a" in COMBOS[name], next_release="b" in COMBOS[name], trend="c" in COMBOS[name]),
                         fable_mythos_eci_median=v["families"]["fable_mythos"]["eci"]["median"],
                         fable_mythos_shift=round(v["families"]["fable_mythos"]["eci"]["median"] - nm["fable_mythos"]["eci"]["median"], 2),
                         opus_shift=round(v["families"]["opus"]["eci"]["median"] - nm["opus"]["eci"]["median"], 2),
                         frontier_shift={q[:4]: round(v["frontier"][q]["eci"]["median"] - hd[q]["anthropic_eci"]["median"], 2) for q in YE},
                         effective_sample_size=v["effective_sample_size"]))
    psens = []
    for p in (0.5, 0.7, 0.9):
        v = summarise(weights("abc", p), f"p{p}")
        psens.append(dict(p=p, next_models_eci_median={e: v["families"][e]["eci"]["median"] for e in nm},
                          anthropic_frontier_eci_median={q[:4]: v["frontier"][q]["eci"]["median"] for q in YE}))
    # headline in the same shape as the default's
    hl_f = []
    for f in c["default_headline"]["families"]:
        e = f["entity"]
        g = dict(f, eci=allv["families"][e]["eci"], aeci_own_card=allv["families"][e]["aeci_own_card"],
                 benchmarks=[dict(b, **allv["families"][e]["benchmarks"][b["benchmark"]]) if b["benchmark"] in allv["families"][e].get("benchmarks", {})
                             else dict(b, note="unchanged from the default (indicative row, not recomputed)") for b in f["benchmarks"]])
        hl_f.append(g)
    hl_fr = [dict(fr, eci=allv["frontier"][fr["date"]]["eci"], all_lab_eci=allv["frontier"][fr["date"]]["all_lab_eci"],
                  share_of_paths_anthropic_leads=allv["frontier"][fr["date"]]["share_of_paths_anthropic_leads"],
                  beyond_measured_scale=bool(allv["frontier"][fr["date"]]["eci"]["median"] > c["thr"])) for fr in c["default_headline"]["frontier"]]
    return dict(
        label="With Model 4", graded=False,
        description="What-if: the forecast if Anthropic's unreleased internal research model (the card's 'Internal Model', METR's 'Model 4') "
                    "is counted as evidence. Not graded; no predictions are issued from it. The default excludes the model.",
        model_4=dict(aeci_nov6=M4_AECI, aeci_global_ci95=[173.75, 185.18], aeci_local_ci95=list(M4_LOCAL), n_benchmarks=15,
                     internal_date_figure_read=M4_INTERNAL_DATE, metr_value=178.6, metr_value_dropping_3_suspect_benchmarks=179.7,
                     metr_training_finished="September-October 2026", days_since_internal_date=int(elapsed), public_release=None,
                     eci_equivalent=dict(median=round(float(np.median(E4)), 1), lo80=round(float(np.quantile(E4, 0.1)), 1),
                                         hi80=round(float(np.quantile(E4, 0.9)), 1), sd=round(sd_e, 2),
                                         method="Fable 5.2's public ECI (%.2f) + the same-fit AECI difference to its twin Mythos 5.2 "
                                                "(%+.2f); sd combines the two local AECI intervals (%.2f), %.1f for model-specific scatter "
                                                "of the AECI-ECI gap, and Fable 5.2's own ECI posterior sd (%.2f; 19 benchmarks so far)"
                                                % (fable_eci, d_aeci, sd_local, MAP_SD, fable_sd)),
                     identification="METR's Model 4 and the card's Internal Model are very probably the same model (author's confidence about "
                                    "90%): both are Anthropic's most capable internal model in autumn 2026, both were scored on exactly 15 "
                                    "AECI benchmarks, the values are 178.6 (METR, fit before Nov 5) and 178.78 (card, Nov 6 fit), and the "
                                    "card's internal date (~Sept 26) falls in METR's 'finished training September-October 2026'. Neither "
                                    "source names the other's label, so it is an inference, not a statement.",
                     models_2_and_3="METR gives only training-completion dates (Model 2: July 2026; Model 3: August-September 2026) and no "
                                    "AECI values, public dates or mapping to released names; they are not used. (METR also lists an "
                                    "'Unreleased 2022' model.)"),
        assumptions=dict(
            p_next_frontier_release_is_model_4_or_better=P_RELEASE,
            p_basis="Judgement. For: the one earlier internally reported frontier model (Mythos Preview, internal use from 2026-02-24) "
                    "shipped within weeks, and every frontier Claude with an internal date has shipped 3-47 days later. Against: the card "
                    "calls this one a 'research model', it is evaluated nowhere else in the card, and it is already %d days past its internal "
                    "date, longer than any earlier lag. Sensitivity at 0.5 and 0.9 is reported." % elapsed,
            p_draws_already_at_or_above_model_4=round(p_ok, 3),
            lag=dict(observed_days=_rows(lags), censored_at_days=int(elapsed), remaining_lag="exponential, mean %.0f days" % REMAINING_LAG_MEAN_DAYS,
                     treatment="The model has no public date. It is not placed on the record line at its internal date (that would steepen "
                               "the slope artificially, because every other point is at its public date). It enters as a pseudo-observation "
                               "at a public-date-equivalent of today + a remaining lag; observed lags have lengthened (25 and 47 days for "
                               "the last two Mythos) and this one is censored at %d days." % elapsed),
            level_likelihood_sd=round(float(S), 2),
            trend=dict(weights_before=W0, weights_after=W1, reversion_scale=round(ratio, 3),
                       p_revert_four_line_average=dict(without_internal_model=round(float(without), 3), with_internal_model=round(float(with_), 3)),
                       aeci_bic_weight_on_jump_or_no_change=dict(public_dates_without_internal_model=round(c["p_rev_aeci_public"], 3),
                                                                 internal_dates_with_internal_model=round(c["p_rev_aeci_internal"], 3)),
                       channel="Only the scenario weights move, and only between 'reversion' and 'hold'; the recent-slope fit is untouched. "
                               "The shift is the ratio of the four-line evidence average with and without the internal model on the AECI "
                               "series, capped so that at most half the reversion weight moves.",
                       caveat="This is the component most open to criticism: the point rests on Anthropic's internal benchmarks, on 15 of "
                              "them, with the model above 50% on every one (METR is 'somewhat nervous' about measuring it), so the index "
                              "may be saturating exactly where this point sits.")),
        components=dict(table=comp, note="Each row applies the listed switches alone or together to the default's paths. Effects are not "
                                         "exactly additive. 'all' (level + next release + trend, p = %.1f) is the variant published below." % P_RELEASE),
        p_sensitivity=psens,
        headline=dict(families=hl_f, frontier=hl_fr, backtested_through=c["default_headline"]["backtested_through"],
                      beyond_measured_scale_above=c["default_headline"]["beyond_measured_scale_above"],
                      display_cap_eci=c["default_headline"]["display_cap_eci"],
                      notes=["What-if variant, not graded. Same intervals convention as the default.",
                             "Only public ECI, own-card AECI and the graded benchmark are recomputed; indicative benchmark rows are the default's."]),
        next_models={e: dict(predicted_name=nm[e]["predicted_name"], release_date=nm[e]["release_date"], **allv["families"][e]) for e in nm},
        projection=dict(quarters=c["QUARTERS"],
                        series=dict(allv["series"], non_anthropic_frontier_eci=c["default_non_anthropic_series"]),
                        scenario_medians=dict(anthropic_frontier_eci=allv["scenario_medians"]),
                        weights=dict(central=W1), note="Mixture bands calibrated with the default's factors. The other labs' frontier is the default's, unchanged."),
        delta_vs_default=delta,
        method="Importance re-weighting of the default's %d simulated paths (weighted resample, then the default's summary code). Effective "
               "sample size of the full variant: %d." % (N, allv["effective_sample_size"]))


def _rows(df):
    return [{k: (v if not isinstance(v, float) else round(v, 1)) for k, v in r.items()} for r in df.to_dict("records")]
