# Competitor releases: notes for the Anthropic release-timing forecaster

Compiled 2026-10-30. Companion files: `competitors.csv` (119 rows) and `benchmark_leadership.csv` (88 rows).

## Sources and method

- **Release dates.** The backbone is Epoch AI's model database (`https://epoch.ai/data/all_ai_models.csv`) and its ECI dataset (`https://epoch.ai/data/benchmark_data.zip`), both downloaded 2026-10-30. Dates and official links were cross-checked against Wikipedia (List of large language models; Gemini; Grok; GPT-5.4; GPT-6; OpenAI o3) and lab posts. Rows tagged "approx" or carrying a date conflict say so in `note`.
- **Coding columns.** Since ~2026, OpenAI and Google no longer report SWE-bench Verified, so the reference benchmark changes by era:
  - Through ~May 2026, `beat_claude_coding` uses lab-reported SWE-bench Verified (llm-stats.com compilation and lab posts). Where that is missing or ambiguous, it uses Epoch's independent SWE-bench Verified runs.
  - From June 2026 on, it uses Epoch's FrontierSWE, FrontierCode, CursorBench and DeepSWE data, plus lab launch claims. Conflicting evidence is written out in `note`.
  - The comparison is always against the best *generally available* Claude model on that date. Restricted models (Mythos Preview, Mythos 5) are excluded.
  - Before SWE-bench Verified existed (Aug 2024), coding is left blank.
- **`took_sota`.** Coded 1 for LMArena text #1 at release (launch claim or monthly snapshot), or for a new state of the art on SWE-bench Verified or Terminal-Bench 2.0 / 2.1. Blank means mixed or unknown evidence.
- **`is_major`.** Coded 1 for any new top-of-lineup headline flagship (e.g. GPT-5.1, Grok 4.6) or generation step. Coded 0 for minis, cheaper tiers, codex variants, dated snapshot updates and experimental previews.

## Jun–Oct 2026 timeline (Claude releases in bold, for the event study)

| Date | Release |
|---|---|
| Jun 9 | **Claude Fable 5** (GA) + **Mythos 5** (restricted) |
| Jun 12 | Kimi K2.7 Code |
| Jun 26 | GPT-5.6 trusted-partner preview |
| Jun 30 | **Claude Sonnet 5** |
| Jul 8 | Grok 4.5 |
| Jul 9 | GPT-5.6 Sol/Terra/Luna GA (approx); Muse Spark 1.1 |
| Jul 16 | Kimi K3 |
| Jul 19 | Qwen 3.8 Max |
| Jul 21 | Gemini 3.6 Flash |
| Jul 24 | **Claude Opus 5** |
| Jul 31 | DeepSeek V4 Flash 0731 |
| Aug 5 | Muse Spark 1.2 |
| Aug 12 | Grok 4.6 |
| Aug 13 | Gemini 3.7 Flash; DeepSeek V4 Pro 0813 |
| Sep 1 | **Claude Fable 5.1** |
| Sep 2 | Gemini 3.8 Flash; Muse Spark 1.3 |
| Sep 3 | **GPT-6 Astra** |
| Sep 9 | DeepSeek V4.1 Flash |
| Sep 21 | Grok 4.7 |
| Sep 22 | **Claude Opus 5.5**; GPT-6 Sol/Luna (same day) |
| Sep 28 | **Claude Sonnet 5.5** |
| Sep 29 | GPT-6.1 Sol (DevDay); GPT-6.1 Astra scrapped over safety concerns |
| Sep 30 | **Gemini 4 Argon** limited preview (GA in the Gemini app on Oct 13) |
| Oct 6 | Mistral Large 4 |
| Oct 7 | **Claude Haiku 5.5**; GPT-6 Instant |
| Oct 12 | Meta Muse Wonder |
| Oct 15 | Muse Spark Open |
| Oct 17 | DeepSeek V4.1 Flash 1017 |
| Oct 23 | Kimi K3.1 Pro |
| Oct 26 | GPT-6.1 Terra |
| Oct 28 | **Gemini 4 Carbon** (limited cyber-defender release) |

Claude dates for Jul–Oct come from Epoch's ECI data. Fable 5, Mythos 5 and Sonnet 5 dates come from Wikipedia.

## Who leads now (late Oct 2026)

- **Overall, Epoch ECI.** Effectively a tie:
  - GPT-6 Astra: 168.9
  - Claude Opus 5.5: 168.6
  - GPT-6.1 Sol: 168.2
  - GPT-6.1 Terra: 168.1
  - Gemini 4 Argon: 166.3

  Gemini 4 Carbon is not scored yet. Google claims Carbon is #1 on the Artificial Analysis Intelligence Index v5 (59 vs Opus 5.5's 58).
- **LMArena text.** Google has held #1 since ~Sep 30 with Gemini 4 Argon (high), at ~1525–1533 vs Claude's ~1505. Anthropic held #1 from ~Feb 2026 (Opus 4.6) through Sep 2026. A Manifold market puts Google at ~88% to hold #1 on Oct 31.
- **Coding: split decision.**
  - Opus 5.5 leads:
    - Terminal-Bench 4.0: 66.4 vs Astra 57.9 vs Argon 57.4.
    - WebDev Arena: ~1820 vs Astra 1800 and Carbon 1768.
    - CursorBench and FrontierCode.
  - GPT-6 Astra leads FrontierSWE (65.5 vs Opus 5.5 62.3) and DeepSWE.
  - SWE-bench Verified is saturated. Claude Fable 5 has the top reported score at 95.0.
- **OpenAI's position.** OpenAI leads on price and performance (Terra at $1/$5 per M tokens), but per OpenAI's own tables Claude still leads on agentic evals (Agents' Last Exam, OSWorld 2.1).

## Descriptive patterns relevant to the hypothesis (not causal)

Releases cluster within days of each other:

- 2025:
  - Aug 5 / Aug 7: Opus 4.1 + gpt-oss, then GPT-5.
  - Nov 17–24: Grok 4.1, Gemini 3 Pro, GPT-5.1-Codex-Max, Opus 4.5.
- 2026:
  - Feb 5: Opus 4.6 and GPT-5.3-Codex on the same day.
  - Feb 17–19: Sonnet 4.6, Grok 4.20, Gemini 3.1 Pro.
  - Apr 16–24: Opus 4.7, Grok 4.3, GPT-5.5, DeepSeek V4.
  - Sep 1–3: Fable 5.1, Gemini 3.8 Flash, GPT-6 Astra.
  - Sep 21–30: Grok 4.7, Opus 5.5 and GPT-6 Sol (same day), Sonnet 5.5, GPT-6.1 Sol, Gemini 4 Argon.

Caveats for the model:

- Clustering can come from shared calendars (conferences, quarter ends) or from competitors reacting to Anthropic (reverse causality).
- Use symmetric event windows and treat restricted or limited releases (Astra preview, Argon preview, Carbon) as separate treatment types.

A press report (Reuters, Sep 18, cited via 9to5ai.tech; primary not checked) said Anthropic was considering a new model to counter GPT-6 Astra. Opus 5.5 followed on Sep 22.

## Expected Nov–Dec 2026 (no lab has announced a dated frontier launch)

Per 9to5ai.tech, Oct 20 2026: https://9to5ai.tech/coming-soon-in-ai-november-december-2026

- **Google.**
  - Gemini 4 Carbon to reach developers, businesses and consumers "soon" (Google blog, Oct 28).
  - Argon price increase on Dec 1. This is not a model launch.
- **OpenAI.**
  - GPT-7: no date. The Information (Oct 13) reported OpenAI is fixing safety issues before shipping its next flagship.
  - GPT-6.1 Astra was scrapped (TechCrunch/WSJ, Sep 29).
- **xAI.**
  - Grok 4.8 had not been released as of ~Oct 11. Musk has called it "a noticeable improvement."
  - Grok 5: Polymarket ~47.5% for release by Dec 31, as of Oct 11 (zbuild.io).
- **DeepSeek.** V4.1 Pro is not released. Manifold (play money): 32% before Nov, 70% before Dec, 81% before Jan 2027.
- **Anthropic (for context).** A "Fable 5.5" listing briefly appeared in Azure's catalog (TestingCatalog leak, unconfirmed). Claude 6 has no date.

## Known weaknesses

- **LMArena history.** The 2024-11 → 2025-02 period is contested. The benchlm.ai monthly snapshots disagree with launch claims there and miss several brief Google/xAI reigns. Treat them as month-level approximations.
- **Date conflicts.** Grok 4.5 is dated Jul 8 by Wikipedia/Epoch but Jul 16 by zbuild.io. GPT-5.6 GA is approximate. Grok 4.20 and Grok 4.3 are known only to the month.
- **Third-party sources.** Several 2026 facts rest on trackers and press (datanorth, letsdatascience, tech-insider, datacamp) rather than lab posts. openai.com and x.ai block automated fetching, so OpenAI links taken from Epoch's database were not opened directly.
- **WebDev Arena series.** It uses current Elo ordered by release date, not Elo at the time of release.
