# Experiments: backlog and log

How the model is allowed to change. The daily run does **at most one** experiment a day, taken from the top of the backlog, and records the result below whether it passes or not. The protocol is in `DAILY_RUNBOOK.md` §10; the short form:

1. Selection on the tuning period (weekly origins 2024-06-03 → 2025-06-30): Opus/Sonnet/Haiku 30-day Brier must improve by ≥ 0.002.
2. No harm on the holdout (2025-07-07 → 2026-10-26): 30-day not worse by > 0.002 for either family group; 7- and 90-day not worse by > 0.005.
3. The holdout never chooses between variants or tunes a value. One pre-declared value per experiment.
4. Signal-layer changes (`--layer signal`): selection on the holdout's all-family 30-day Brier, margin 0.004, more blocks better than worse; adoption is provisional and reverts if the forward score is worse after two more resolved blocks.
5. No harm on the forward snapshots (> 0.005 worse is a veto).
6. A mechanism stated before the run.
7. Forward-only ideas (anything using market prices) wait for 8 resolved blocks, then go to Jacob.
8. One adoption per seven days; none on a release day or the day after.
9. Changes to what the headline means, to the page, or to these rules are Jacob's.

Tool: `python3 tools/experiment.py --name <id> --set <ConfigField>=<value> [--layer signal]`. About a minute. It prints the table to paste here and a verdict.

Status values: `ready` (can be run as written), `needs code` (a Config flag has to be added first, default off), `needs data` (tabulate or collect first), `tracking` (forward-only, read off the scorecard), `adopted`, `rejected`, `done`.

## Backlog (in priority order)

### E1. Market blend where a ladder exists — `tracking`
- **Hypothesis.** A log-odds blend of the model and the Polymarket ladder (weight 0.5, set a priori, already computed in `engine/market.py`) scores better than the model alone on questions where a market exists.
- **Mechanism.** Forecast combination; the market sees evidence the signal file does not (private desk checks, order flow) and has no slow-cadence prior. The model's known low bias in 2025–26 is corrected for free.
- **Evidence so far.** 2 blocks: model 0.077, blend 0.021, market 0.005 (`SCORECARD.md`, "What a blend would have scored"). On this record the market alone beats any blend, which is an argument about the model's weight, not about blending.
- **Metric and test.** Clustered Brier on market-paired primary questions, read from `SCORECARD.md` each day. No backtest is possible: there are no market prices before 2026-10-30.
- **Decision rule.** At 8 resolved blocks: if the blend beats the model in at least three quarters of blocks, propose to Jacob that the blend becomes the headline for families with a ladder. Do not fit the weight on fewer than 20 blocks.
- **Caveat.** If the headline is a market blend, "beating the market" has to be judged on the model's own number, which the log keeps recording.

### E2. A sighted model exists and will ship: an existence term — `needs code`
- **Hypothesis.** Once a family has a grade A/B artifact (catalog row, EAP string, first-party page), the probability that its next release lands within about 75 days should be near the historical rate, about 16 of 17, whatever the cadence prior says.
- **Mechanism.** The signal layer only reshapes timing against a far-future reference; it cannot lift total probability mass much inside the window. A model that already has partner strings has finished training. Adversarial review finding 10; Fable 5.2 post-mortem lesson 1 (the model never exceeded 49% by Nov 30 with seven A/B rows visible).
- **Pre-registration (write before running).** One variant: with at least one visible A/B sighting in classes `infra` or `client`, mix the family's pmf with a "ships within 75 days of the first A/B sighting" component at weight q = 0.85 × (hits + 0.5)/(n + 1) computed from resolved sightings at the origin (no free parameter beyond the window, fixed at 75 from the review). Config flag `sig_exist` (default off).
- **Test.** `python3 tools/experiment.py --name E2-existence --set sig_exist=True --layer signal`.
- **Risk.** Half of EAP codenames never map; the term must key on sightings mapped to a family, and the false rows (`sonnet-4-8`, Claude 3.5 Opus) have to count against q.

### E3. Calibrate the named-version weight — `needs data`
- **Hypothesis.** The fixed 0.85 in `engine/params.py: apply_named_signals` is too high for names taken from catalogs, trailers and page headings.
- **Mechanism.** Those surfaces carry working names. First-party API identifiers do not.
- **Data to tabulate first** (from `data/raw/signals_research.csv`, rows with `specific = yes` and a version in the note): for each release since 2025, the name each pre-release artifact used, the surface, and whether that name shipped. Known cases to start: `claude-fable-5-5` Azure row and "Mythos 5.5" page heading (missed, shipped 5.2); `sonnet-4-8` in the Claude Code source (missed, line went 4.6 → 5); "Claude 3.5 Opus" first-party (never shipped); `claude-sonnet-5` Vertex/Fennec (hit); `claude-opus-5` Vertex (hit on name); `claude-fable-5` leak (hit); Opus 4.1 and Claude 4 web config (hits). Save as `data/name_artifacts.csv` with the source row id.
- **Variant.** Weight = (hits + 1)/(n + 2) per surface type (first-party API id, cloud catalog, client string, page text), replacing 0.85. No tuning.
- **Metric.** Mean log score of the shipped name over those cases, leave-one-out, against the fixed 0.85 and against no named-version rule. This is a parameter of the release-parameters layer, not the date model, so `tools/experiment.py` does not apply; show the tabulation and the three scores in the log.
- **Until then.** `named_versions.json` takes a name only from a first-party API identifier or two independent grade-A surfaces (`DAILY_RUNBOOK.md` §3, hygiene rule 7).

### E4. Unfulfilled sightings age too fast: a heavier lead-time tail — `needs code`
- **Hypothesis.** The log-normal lead-time density (median 5–12 days by class) discounts a sighting too quickly once it is 3–4 weeks old. Fable 5.2's A/B leads were 20–27 days.
- **Mechanism.** Launch slips are common and one-sided; the lead-time sample is dominated by short, specific, late sightings.
- **Pre-registration.** One variant: raise the floor on the pooled log-lead standard deviation in `engine/signals.py` from 0.6 to 1.0 (`g_sd` floor and the shrinkage target). Config flag `sig_sd_floor` (default 0.6).
- **Test.** `python3 tools/experiment.py --name E4-heavy-tail --set sig_sd_floor=1.0 --layer signal`.
- **Note.** E2 and E4 address the same miss. Run E2 first; if it is adopted, re-read E4 before running it.

### E5. Regime bias: more weight on the fast-adapting part — `rejected` (2026-11-12, see log)
- **Hypothesis.** The model under-predicts in the current regime; raising the EWMA pool weight from 0.3 to 0.5 for Opus, Sonnet and Haiku reduces that without breaking 2024–25.
- **Mechanism.** The hierarchical cadence adapts slowly to a cadence shift; the EWMA adapts fast (README, v3). Holdout calibration intercept +0.74; the EWMA won the holdout at 90 days.
- **Pre-registration.** One value, 0.5 (equal weights, the default of the forecast-combination literature). Not a grid.
- **Test.** `python3 tools/experiment.py --name E5-ewma-half --set w_ewma=0.5`.
- **Expected difficulty.** The EWMA collapsed in the tuning period (the 444-day Opus gap), so rule 1 may fail. If it does, the honest reading is that the data cannot separate "regime changed for good" from "EWMA got lucky", and the entry is rejected until the forward log says otherwise.

### E6. EAP strings removed from a client as a launch tell — `needs data`
- **Hypothesis.** Removal of every `-eap` id from a client's model list raises next-day to next-week hazard.
- **Evidence.** Three events: removals on the day Fable 5.1 shipped and the day before Fable 5.2 shipped; five ids pruned 2026-10-23 with no launch for 17 days. 2 of 3.
- **Collect.** Log every removal as a `CLIENT_STRING` row whose note starts `EAP_REMOVED:` (full or partial removal, which client, version numbers). Revisit at 6 events. No model change before then.

### E7. Dated tipster calls: shift, do not trust — `needs data`
- **Hypothesis.** A dated call carries information about the date after a shift of about a week later and a wide spread.
- **Evidence.** Nine missed dated calls, all late: 5–6 days, about a week, 8 days, 10 days, 15 days, 3 weeks, 27 days, 34 days, 5–6 weeks.
- **Collect.** Put `CALLED: YYYY-MM-DD` in the note of every dated call, including the nine historical ones (and the calls that hit: the Cursor forum "tomorrow" post, lyra on Opus 5.5). At 15 calls, fit the offset distribution and test it as a soft-class likelihood.

### E8. Absence of evidence, from logged nulls — `needs data`
- **Hypothesis.** "Tier-1 and tier-2 sources checked today, nothing new" lowers the 7-day hazard.
- **Background.** The absence term was tested and switched off because it hurt in both periods; the cause was hindsight-collected detection rates (README). `data/raw/sweep_log.csv` now records real nulls from 2026-11-10.
- **Collect.** Nothing extra. Revisit after two releases have happened under daily logging: compare the null/changed pattern in the 14 days before each with the pattern in quiet stretches.

### E9. Haiku and the lineup-wide refresh — `needs code`
- **Hypothesis.** After Opus and Sonnet both move to a new version, Haiku's hazard rises (Opus 5.5 → Sonnet 5.5 → Haiku 5.5 took 15 days in 2026).
- **Mechanism.** Product-line completion. The model gives Haiku 4–5% by Dec 31 from three gaps of 236–356 days; the market says about 20% (adversarial review finding 10).
- **Status.** One observed refresh. Write the variant only after a second; until then note the gap in the weekly narrative.

### E10. False alarms the builder drops — `needs data`
- **Observation.** `tools/build_signals.py` drops some `FALSE:` rows on purpose (timing-only misses whose model shipped soon after: "Opus 5 ships 7/16", the McAteer call, the pitch-deck story). They are false alarms about a date and are not counted in the false-alarm rate, which sits on its floor of 0.01.
- **Question.** Should a missed dated call count as a false alarm for its class? Decide with E7's tabulation; no change before.

## Voice-model forecast: assumptions held open (`voice.py`, `data/voice_params.json`)

Added 2026-11-10 at Jacob's request. None of these can be backtested: the event has not happened, and the reference class is seven launches at other labs. They are assumptions, stated so they can be judged. Changing one is a model change (bump `MODEL_VERSION` in `voice.py`, log it here) and, like E1, a decision for Jacob. Status of all six: `tracking`.

### V1. The base rate is the geometric mean of the pooled lab rate and Anthropic's own rate
- **Assumed.** Pooled 0.55 a year, Anthropic alone 0.14, used 0.28. The pooled rate ignores that Anthropic has waited longer than any lab did; its own rate ignores every other lab.
- **Would calibrate it.** Nothing soon. A proper frailty model needs more labs than exist. Revisit only if the reference class changes (a row was wrong, a lab is added).

### V2. Program evidence earns the pooled rate (×2.0)
- **Assumed.** A grade A/B sign of a staffed speech effort (the Audio research posting, the Krieger statement) moves the hazard from 0.28 to 0.55 a year.
- **Would calibrate it.** For each reference lab, the date its speech effort became public and the time from there to launch. Collect into `data/voice_reference_class.csv` (`signal_date`, mostly blank today: only OpenAI's and xAI's are filled, and both are launch demos, not hiring).

### V3. Preparation multipliers: grade weights (A 1, B 1, C 0.5), specificity weights (yes 1, partial 0.5, no 0.25)
- **Assumed.** cap 5 and ρ 0.5 are the family model's; the weights inside the exponent are not measured. Today they give ×1.46 for the voice-recording opt-in and ×1.10 for the hidden Voice item.
- **Would calibrate it.** Anthropic product launches with a first-party preparation artifact beforehand (data-use changes, hidden interface items) and their leads. One case on file: the 2025 voice mode, 43 days from the first hidden-interface report to launch, 126 from the CEO's statement. Tabulate five or more product launches (voice mode, memory, web search, computer use, Claude in Chrome) from TestingCatalog's archive before touching the weights.

### V4. Preparation signals fade with a 365-day half-life
- **Assumed.** Chosen long on purpose: the Fable 5.2 post-mortem found the family model aged its sightings too fast (standing rule 2).
- **Would calibrate it.** The same tabulation as V3.

### V5. Rungs B and C from A: 90-day mean delay to general availability; speech-to-speech follows at the pooled rate when it is not first
- **Assumed.** The shares (67% open on day one, 67% speech-to-speech first) are measured on seven launches; the delays rest on one case each.
- **Would calibrate it.** Anthropic's own preview-to-GA gaps for products (not models), and the reference labs' later launches.

### V6. Market weight 0.75 (liquid) or 0.5 (thin)
- **Assumed.** No market exists. The lean toward the market comes from the family scorecard (market 0.005, model 0.077 over two blocks) and from this model having no record.
- **Would calibrate it.** A market opening. Until one has resolved against this forecast, the weight is a prior. E1's rule applies: do not fit a weight on fewer than 20 blocks.

**Also open.** The model has no absence-of-evidence term (as E8) and no term for Anthropic choosing a deeper partnership instead; rung A depends on Anthropic saying the model is its own, which the model treats as certain if one ships.

## Done (mechanical, not experiments)

| Date | What | Where |
|---|---|---|
| 2026-11-10 | Release-day rule: a run on a release day takes the next day as origin (proposal 1 of the 2026-11-10 weekly note). | `daily.py` |
| 2026-11-10 | One forecast per origin: a second run on the same day restores the frozen snapshot and does not recompute. | `weekly.py: forecast_and_snapshot` |
| 2026-11-10 | Market ladder regex reads the threshold version from the question and drops ladders about a model that has shipped (proposal 3). Verified: same parsed ladders on all four market files, identical 2026-11-10 forecast. | `engine/market.py`, `live.py` |
| 2026-11-10 | `build_signals.py` warns when a row's target is in no table, so a new unreleased target cannot be dropped silently. Output file unchanged. | `tools/build_signals.py` |
| 2026-11-10 | Weekly summary no longer crashes when a median lies beyond the 400-day horizon. | `weekly.py` |

Still open from the 2026-11-10 note: proposal 5 (the SWE-bench Pro table lives in `engine/params.py`; it is data and may belong in `data/`). Left for Jacob; it would move a file the page builder does not read, so nothing depends on it.

## Log (newest first; rejected ideas stay here so they are not retried)

### 2026-11-12 — E5. EWMA pool weight 0.3 → 0.5 — `rejected`
Pre-registered (backlog entry, written 2026-11-10): one value, 0.5, equal weights; metric: tuning-period Opus/Sonnet/Haiku 30-day Brier; pass rule: protocol rules 1, 2 and 5.
Command: `python3 tools/experiment.py --name E5-ewma-half --set w_ewma=0.5`

| Period | Group | Horizon | Blocks | Base | Variant | Diff | Blocks better / worse |
|---|---|---|---|---|---|---|---|
| tune | opus/sonnet/haiku | 7 d | 6 | 0.0334 | 0.0339 | +0.0005 | 1 / 4 |
| tune | opus/sonnet/haiku | 30 d | 6 | 0.1234 | 0.1302 | +0.0068 | 1 / 4 |
| tune | opus/sonnet/haiku | 90 d | 6 | 0.2634 | 0.2874 | +0.0240 | 1 / 4 |
| lock | opus/sonnet/haiku | 7 d | 16 | 0.0528 | 0.0530 | +0.0001 | 8 / 8 |
| lock | opus/sonnet/haiku | 30 d | 15 | 0.1816 | 0.1738 | -0.0078 | 13 / 2 |
| lock | opus/sonnet/haiku | 90 d | 13 | 0.1884 | 0.1621 | -0.0264 | 11 / 2 |
| lock | fable/mythos | 7 / 30 / 90 d | 9 / 8 / 6 | 0.0588 / 0.2107 / 0.2373 | same | +0.0000 | 0 / 0 |
| forward | primary questions | ≤ 92 d | 4 | 0.0271 | 0.0271 | +0.0000 | |

Verdict: FAIL. Rule 1 failed (tuning 30-day worse by 0.0068 where an improvement of 0.002 was needed) and the tuning 90-day score got worse by 0.024, past the 0.005 no-harm limit. The holdout improved at 30 and 90 days, as the entry expected, and that cannot be used to choose (rule 3). Learned: the two periods pull the pool weight in opposite directions, so the backtest cannot tell a lasting regime change from the EWMA having been lucky in 2025–26; the forward log showed no difference at all (four blocks, identical to four decimals). Do not retry another pool weight. To reopen this needs forward evidence: several resolved Opus/Sonnet/Haiku blocks on which the EWMA part alone beats the pooled model, or a mechanism that sets the weight from the data at each origin and is not a fixed number.

### 2026-11-10 — E0. Signal likelihood-ratio cap 5 → 3 — `rejected` (harness check)
Run to validate `tools/experiment.py`, not as a serious candidate. Mechanism offered: with false-alarm rates on their floor every sighting hits the cap, so the cap is doing the work (adversarial review finding 5). `python3 tools/experiment.py --name E0-cap3 --set cap=3 --layer signal`.

| Period | Group | Horizon | Blocks | Base | Variant | Diff | Blocks better / worse |
|---|---|---|---|---|---|---|---|
| tune | opus/sonnet/haiku | 30 d | 6 | 0.1234 | 0.1234 | +0.0000 | 0 / 0 |
| lock | opus/sonnet/haiku | 30 d | 15 | 0.1816 | 0.1822 | +0.0006 | 0 / 8 |
| lock | fable/mythos | 30 d | 8 | 0.2107 | 0.2130 | +0.0023 | 1 / 3 |
| lock | all five | 30 d | 15 | 0.1868 | 0.1877 | +0.0009 | 0 / 10 |
| forward | primary questions | ≤ 92 d | 4 | 0.0271 | 0.0293 | +0.0022 | |

Verdict: FAIL. Slightly worse everywhere a sighting exists. Two things learned: the tuning period is blind to signal-layer settings (every tune row is identical to four decimals), which is why rule 4 exists; and the base holdout score (0.1816) reproduces the README's v3d figure (0.1821 with a different chain count), so the harness matches the earlier backtest. Do not retry a lower cap without new false-alarm data.

### Before the daily process (from `README.md`; do not retry without new data or a new mechanism)

| When | Idea | Result |
|---|---|---|
| 2026-10 | Wave model (company-level renewal with co-launch mix), weight 0.5 or 1 | Lost on tuning and lockbox; weight zero. |
| 2026-10 | Competitor-release hazard multiplier, two pre-registered definitions | Made scores worse; γ slightly negative. Excluded. `competitor_releases.csv` is still logged. |
| 2026-10 | Absence-of-evidence term in the signal layer | Hurt in both periods (hindsight detection rates). Off. See E8. |
| 2026-10 | 27 stage-1 configs (error family × trend × wave weight) | Selection among them is mostly noise (probability of backtest overfitting 0.83). Do not re-tune these. |
| 2026-11-01 | Separate first-party signal class (`split_fp`) | Slightly worse in both periods. Not adopted; flag remains, default off. |
| 2026-11-01 | Signal clock from the most recent A/B sighting; same-day sightings in live runs | Adopted as v3d (neutral to slightly better everywhere). |
| 2026-11-02 | US election day as a low-hazard day | Adopted as v3e (a prior, not fitted). |

### Entry template

```
### YYYY-MM-DD — E<n>. <title> — adopted | rejected | needs data
Pre-registered: <variant, one value, why that value>; metric; pass rule (protocol rules 1–5 or 4).
Command: python3 tools/experiment.py --name ... --set ...
<table as printed>
Verdict: PASS/FAIL. <one or two sentences: what was learned, and what would have to be different to try again>
```
