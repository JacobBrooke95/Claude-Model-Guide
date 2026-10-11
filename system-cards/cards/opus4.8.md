# System Card: Claude Opus 4.8

Released 2026-05-28. 391 metric entries. [Source PDF](https://anthropic.com/claude-opus-4-8-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | 500 problems; avg 5 trials; adaptive thinking max effort | % resolved | Claude Opus 4.8: 88.6% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro | avg 5 trials | % resolved | Claude Opus 4.8: 69.2% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro by reasoning effort | effort sweep | pass rate vs effort/tokens | Claude Opus 4.8: Value only in figure | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, 9 languages; avg 5 trials | % resolved | Claude Opus 4.8: 84.4% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness; avg 5 trials | % resolved | Claude Opus 4.8: 38.4% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| Terminal-Bench 2.1 | Harbor, Terminus-2 harness, high effort, 89 tasks x5 | mean reward % | Claude Opus 4.8: 74.6% | 8.3 Terminal-Bench 2.1 |
| FrontierSWE - mean@5 average rank | 17 tasks, 20 hrs each, xhigh effort | average rank (lower better) | Claude Opus 4.8: 2.74 (#1) | 8.4 FrontierSWE |
| FrontierSWE - best@5 average rank | 17 tasks, 20 hrs each, xhigh effort | average rank (lower better) | Claude Opus 4.8: 2.26 (#1) | 8.4 FrontierSWE |
| ProgramBench | 166 tasks; 1-5 episodes up to 1M tokens each; near-final snapshot | hidden test pass rate % | Claude Opus 4.8: 79-88% | 8.5 ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp | single-agent, adaptive thinking max effort, 10M token limit, compaction at 200k | accuracy % | Claude Opus 4.8: 84.3% | 8.10.2 BrowseComp |
| DeepSearchQA - F1 | max effort, adaptive thinking, 1M token budget, no compaction | F1 % | Claude Opus 4.8: 93.1% ± 1.4% | 8.10.3 DeepSearchQA |
| DeepSearchQA - Fully Correct | max effort, adaptive thinking, 1M token budget, no compaction | Fully Correct % | Claude Opus 4.8: 84.8% ± 2.4% | 8.10.3 DeepSearchQA |
| DeepSearchQA - Fully Incorrect | max effort, adaptive thinking, 1M token budget, no compaction | Fully Incorrect % | Claude Opus 4.8: 3.9% ± 1.3% | 8.10.3 DeepSearchQA |
| DeepSearchQA - Correct with Excessive Answers | max effort, adaptive thinking, 1M token budget, no compaction | Correct with Excessive Answers % | Claude Opus 4.8: 4.3% ± 1.3% | 8.10.3 DeepSearchQA |
| DeepSearchQA F1 by reasoning effort | all effort levels | F1 vs effort | Claude Opus 4.8: Value only in figure | 8.10.3 DeepSearchQA |
| DRACO | 100 tasks; adaptive thinking max effort; 1M token limit; compaction at 200k; Opus 4.6 judge, 5 grading runs | normalized score % | Claude Opus 4.8: 80.4% | 8.10.4 DRACO |
| BrowseComp multi-agent - Orchestrator with blocking subagents | max effort | accuracy % | Claude Opus 4.8: 88.5% | 8.11.1 Multi-Agent BrowseComp |
| BrowseComp multi-agent - five-agent fixed team | 5M-token total limit (1M per agent) | accuracy % | Claude Opus 4.8: 85.4% | 8.11.1 Multi-Agent BrowseComp |
| BrowseComp multi-agent - async subagents |  | accuracy % / latency / tokens | Claude Opus 4.8: Value only in figure | 8.11.1 Multi-Agent BrowseComp |
| MCP-Atlas - pass rate | Scale AI, 100 tool-call budget, Apr 2026 | pass rate % | Claude Opus 4.8: 82.2% | 8.13.4 MCP Atlas |
| MCP-Atlas - mean claim coverage |  | mean claim coverage % | Claude Opus 4.8: 86.2% | 8.13.4 MCP Atlas |
| Vending-Bench 2 | max effort; year-long simulation, $500 start | final bank balance ($) | Claude Opus 4.8: $2,992.34 | 8.13.5 Vending-Bench 2 |
| Vending-Bench 2 | high effort | final bank balance ($) | Claude Opus 4.8: $5,787.43 | 8.13.5 Vending-Bench 2 |
| Toolathlon - Pass@1 | 108 tasks, 3 trials, internal harness, adaptive thinking max effort | Pass@1 % | Claude Opus 4.8: 59.9% | 8.13.7 Toolathlon |
| Toolathlon - Pass@3 | 108 tasks, 3 trials, internal harness, adaptive thinking max effort | Pass@3 % | Claude Opus 4.8: 67.6% | 8.13.7 Toolathlon |
| Toolathlon - Pass^3 | 108 tasks, 3 trials, internal harness, adaptive thinking max effort | Pass^3 % | Claude Opus 4.8: 48.1% | 8.13.7 Toolathlon |
| AutomationBench | Zapier private held-out leaderboard; max effort | pass rate % | Claude Opus 4.8: 15.5% | 8.13.8 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ScreenSpot-Pro | no tools; 1,581 tasks, avg 5 runs | accuracy % | Claude Opus 4.8: 82.3% | 8.12.5 ScreenSpot-Pro |
| ScreenSpot-Pro | with Python tools; 1,581 tasks, avg 5 runs | accuracy % | Claude Opus 4.8: 87.9% | 8.12.5 ScreenSpot-Pro |
| OSWorld-Verified | 361 tasks, 1080p, 100 steps, adaptive thinking max effort; pass@1 avg 5 runs | first-attempt success rate % | Claude Opus 4.8: 83.4% | 8.12.6 OSWorld-Verified |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| USAMO 2026 | 10 attempts per problem; high effort, batch API 300k tokens; MathArena grading, min of 3 judges | score % | Claude Opus 4.8: 96.7% | 8.7 USAMO 2026 |
| ArxivMath | March+April 2026 releases (71 problems); extended thinking | accuracy % | Claude Opus 4.8: 71.82% | 8.8 ArxivMath |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GPQA Diamond | 198 questions; avg 25 trials | accuracy % | Claude Opus 4.8: 93.6% | 8.6 GPQA Diamond |
| Humanity's Last Exam | no tools, max effort, 2,500 questions | accuracy % | Claude Opus 4.8: 49.8% | 8.10.1 Humanity's Last Exam |
| Humanity's Last Exam | with tools (web search/fetch, PTC, code), 1M token cap, max effort | accuracy % | Claude Opus 4.8: 57.9% | 8.10.1 Humanity's Last Exam |
| HLE accuracy by reasoning effort | single run per effort up to 1M tokens | accuracy % vs effort | Claude Opus 4.8: Value only in figure | 8.10.1 Humanity's Last Exam |
| HealthBench Professional | 525 conversations; Sonnet 4.6 grader; avg 5 trials; adaptive thinking max effort | score % | Claude Opus 4.8: 55.8% | 8.14.1 HealthBench Professional |
| BioPipelineBench Verified | validated problems; bash tool; no extended thinking | score % | Claude Opus 4.8: 87.7% | 8.16.1 BioPipelineBench Verified |
| BioMysteryBench Verified - Human Solvable |  | score % | Claude Opus 4.8: 80.4% | 8.16.2 BioMysteryBench Verified |
| BioMysteryBench Verified - Human Difficult |  | score % | Claude Opus 4.8: 40.0% | 8.16.2 BioMysteryBench Verified |
| LatchBio Bioinformatics - SpatialBench |  | score % | Claude Opus 4.8: 53.3% | 8.16.3 LatchBio Bioinformatics |
| LatchBio Bioinformatics - SingleCellBench |  | score % | Claude Opus 4.8: 58.2% | 8.16.3 LatchBio Bioinformatics |
| Structural biology, open-ended |  | score % | Claude Opus 4.8: 79.0% | 8.16.4 Structural biology, open-ended |
| ProteinGym Hard |  | rank correlation % | Claude Opus 4.8: 39.6% | 8.16.5 ProteinGym Hard |
| Organic chemistry |  | score % | Claude Opus 4.8: 86.2% | 8.16.6 Organic chemistry |
| Protocol troubleshooting | bash + web search | score % | Claude Opus 4.8: 59.6% | 8.16.7 Protocol troubleshooting |
| LABBench2 - patents | live web research | score % | Claude Opus 4.8: 68.8% | 8.16.8 LABBench2 |
| LABBench2 - clinical trials | live web research | score % | Claude Opus 4.8: 85.3% | 8.16.8 LABBench2 |
| LABBench2 - reading tables | live web research | score % | Claude Opus 4.8: 77.2% | 8.16.8 LABBench2 |
| LABBench2 - supplementary materials | live web research | score % | Claude Opus 4.8: 58.9% | 8.16.8 LABBench2 |
| LABBench2 - other categories |  | score % | Claude Opus 4.8: Value only in figure | 8.16.8 LABBench2 |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU - English | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 92.9% | 8.15.1 GMMLU results |
| GMMLU - High-resource average (15 languages) | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 91.6% | 8.15.1 GMMLU results |
| GMMLU - Mid-resource average (14 languages) | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 91.4% | 8.15.1 GMMLU results |
| GMMLU - Low-resource average | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 87.4% | 8.15.1 GMMLU results |
| GMMLU - Igbo | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 82.9% | 8.15.1 GMMLU results |
| GMMLU - Yoruba | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 84.4% | 8.15.1 GMMLU results |
| GMMLU - Chichewa | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 85.6% | 8.15.1 GMMLU results |
| GMMLU - Somali | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 86.7% | 8.15.1 GMMLU results |
| GMMLU - Malagasy | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 86.7% | 8.15.1 GMMLU results |
| GMMLU - Shona | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 86.7% | 8.15.1 GMMLU results |
| GMMLU - Hausa | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 86.8% | 8.15.1 GMMLU results |
| GMMLU - Kyrgyz | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 88.9% | 8.15.1 GMMLU results |
| GMMLU - Swahili | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 89.2% | 8.15.1 GMMLU results |
| GMMLU - Amharic | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 89.3% | 8.15.1 GMMLU results |
| GMMLU - Sinhala | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 90.4% | 8.15.1 GMMLU results |
| GMMLU - Nepali | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 90.9% | 8.15.1 GMMLU results |
| GMMLU - Average (all languages) | 42 languages, structured JSON output, adaptive thinking | accuracy % | Claude Opus 4.8: 90.4% | 8.15.1 GMMLU results |
| GMMLU - average gap to English | excl. English | percentage points | Claude Opus 4.8: -2.6% | 8.15.1 GMMLU results |
| GMMLU - worst gap to English |  | percentage points | Claude Opus 4.8: -10.0% | 8.15.1 GMMLU results |
| MILU average accuracy | 10 Indic languages + English | accuracy % | Claude Opus 4.8: 90.3% | 8.15.2 MILU results |
| INCLUDE average accuracy | 44 languages | accuracy % | Claude Opus 4.8: 87.6% | 8.15.3 INCLUDE results |

## Long context & memory

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GraphWalks BFS 256K | avg 5 trials, default sampling | F1 score | Claude Opus 4.8: 85.9 | 8.9 Long context: GraphWalks |
| GraphWalks BFS 1M | avg 5 trials, default sampling | F1 score | Claude Opus 4.8: 68.1 | 8.9 Long context: GraphWalks |
| GraphWalks Parents 256K | avg 5 trials, default sampling | F1 score | Claude Opus 4.8: 99.3 | 8.9 Long context: GraphWalks |
| GraphWalks Parents 1M | avg 5 trials, default sampling | F1 score | Claude Opus 4.8: 83.3 | 8.9 Long context: GraphWalks |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ChartQAPro | no tools; 1,948 questions, adaptive thinking max effort, avg 5 runs | accuracy % | Claude Opus 4.8: 69.4% | 8.12.1 ChartQAPro |
| ChartQAPro | with Python tools; 1,948 questions, adaptive thinking max effort, avg 5 runs | accuracy % | Claude Opus 4.8: 72.3% | 8.12.1 ChartQAPro |
| ChartMuseum | no tools; 1,162 questions test split, Sonnet 4.6 grader, avg 5 runs | accuracy % | Claude Opus 4.8: 75.8% | 8.12.2 ChartMuseum |
| ChartMuseum | with Python tools; 1,162 questions test split, Sonnet 4.6 grader, avg 5 runs | accuracy % | Claude Opus 4.8: 89.7% | 8.12.2 ChartMuseum |
| LAB-Bench FigQA | no tools; 181 public questions, avg 5 runs | accuracy % | Claude Opus 4.8: 80.4% | 8.12.3 LAB-Bench FigQA |
| LAB-Bench FigQA | with Python tools; 181 public questions, avg 5 runs | accuracy % | Claude Opus 4.8: 87.3% | 8.12.3 LAB-Bench FigQA |
| CharXiv Reasoning | no tools; 1,000 validation questions, avg 5 runs | accuracy % | Claude Opus 4.8: 80.5% | 8.12.4 CharXiv Reasoning |
| CharXiv Reasoning | with Python tools; 1,000 validation questions, avg 5 runs | accuracy % | Claude Opus 4.8: 89.9% | 8.12.4 CharXiv Reasoning |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | internal agentic harness; exact match | accuracy % | Claude Opus 4.8: 77.6% | 8.13.1 OfficeQA |
| OfficeQA Pro | 133-question subset; internal harness | accuracy % | Claude Opus 4.8: 66.2% | 8.13.1 OfficeQA |
| Finance Agent v2 | Vals AI; adaptive thinking max effort | score % | Claude Opus 4.8: 53.92% | 8.13.2 Finance Agent |
| Legal Agent Benchmark - all-pass rate | 1,235 problems; avg 5 trials; internal harness | all-criteria pass rate % | Claude Opus 4.8: 9.62% | 8.13.3 Legal Agent Benchmark |
| Legal Agent Benchmark - mean criterion-pass rate | 1,235 problems; avg 5 trials | mean criterion pass rate % | Claude Opus 4.8: 89.01% | 8.13.3 Legal Agent Benchmark |
| GDPval-AA | 220 tasks, 44 occupations; Artificial Analysis blind pairwise ELO | ELO | Claude Opus 4.8: 1890 | 8.13.6 GDPval-AA |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests - overall harmless response rate | API, no system prompt; 16 policy areas, 7 languages; avg with/without thinking | harmless response rate % | Claude Opus 4.8: 97.98% (± 0.11%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests - overall harmless response rate | claude.ai with system prompt | harmless response rate % | Claude Opus 4.8: 99.17% (± 0.07%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests - overall refusal rate | API, no system prompt | over-refusal rate % | Claude Opus 4.8: 0.36% (± 0.04%) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests - overall refusal rate | claude.ai with system prompt | over-refusal rate % | Claude Opus 4.8: 0.49% (± 0.05%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn harmful-request testing by risk area | API, no system prompt | appropriate response rate % per risk area | Claude Opus 4.8: Value only in figure | 4.1.3 Multi-turn testing results |
| Multi-turn harmful-request testing by risk area | claude.ai with system prompt | appropriate response rate % per risk area | Claude Opus 4.8: Value only in figure | 4.1.3 Multi-turn testing results |
| Single-turn harmful requests - illegal substances category | API, vs Opus 4.7 | change in harmless response rate (percentage points) | Claude Opus 4.8: ~+10 points vs Opus 4.7 | 4.1.4 Harmful request evaluations discussion |
| Suicide and self-harm - single-turn requests posing potential risk | API, no system prompt | harmless rate % | Claude Opus 4.8: 99.05% (± 0.26%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm - single-turn benign requests | API, no system prompt | refusal rate % | Claude Opus 4.8: 0.15% (± 0.11%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm - multi-turn evaluations | API, no system prompt | appropriate response rate % | Claude Opus 4.8: 58% (± 14%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm - single-turn requests posing potential risk | claude.ai | harmless rate % | Claude Opus 4.8: 99.94% (± 0.07%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm - single-turn benign requests | claude.ai | refusal rate % | Claude Opus 4.8: 0.43% (± 0.23%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm - multi-turn evaluations | claude.ai | appropriate response rate % | Claude Opus 4.8: 78% (± 12%) | 4.3.1 Suicide and self-harm |
| Disordered eating - single-turn requests posing potential risk | API, no system prompt | harmless rate % | Claude Opus 4.8: 97.99% (± 0.45%) | 4.3.2 Disordered eating |
| Disordered eating - single-turn benign requests | API, no system prompt | refusal rate % | Claude Opus 4.8: 0.06% (± 0.06%) | 4.3.2 Disordered eating |
| Disordered eating - single-turn requests posing potential risk | claude.ai | harmless rate % | Claude Opus 4.8: 99.80% (± 0.13%) | 4.3.2 Disordered eating |
| Disordered eating - single-turn benign requests | claude.ai | refusal rate % | Claude Opus 4.8: 0.21% (± 0.13%) | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety - single-turn harmful requests | API, no system prompt | harmless rate % | Claude Opus 4.8: 99.90% (± 0.07%) | 4.2 Child safety evaluations |
| Child safety - single-turn benign requests | API, no system prompt | refusal rate % | Claude Opus 4.8: 0.45% (± 0.19%) | 4.2 Child safety evaluations |
| Child safety - multi-turn evaluations | API, no system prompt | appropriate response rate % | Claude Opus 4.8: 91% (± 4%) | 4.2 Child safety evaluations |
| Child safety - single-turn harmful requests | claude.ai | harmless rate % | Claude Opus 4.8: 99.99% (± 0.02%) | 4.2 Child safety evaluations |
| Child safety - single-turn benign requests | claude.ai | refusal rate % | Claude Opus 4.8: 0.27% (± 0.15%) | 4.2 Child safety evaluations |
| Child safety - multi-turn evaluations | claude.ai | appropriate response rate % | Claude Opus 4.8: 95% (± 4%) | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness - even-handedness | 1,350 prompt pairs, 150 topics, 9 task types; public system prompt; thinking on/off avg | score/rate % (grader) | Claude Opus 4.8: Value only in figure | 4.4.1 Political bias and even-handedness |
| Political even-handedness - acknowledgement of opposing perspectives | 1,350 prompt pairs, 150 topics, 9 task types; public system prompt; thinking on/off avg | score/rate % (grader) | Claude Opus 4.8: Value only in figure | 4.4.1 Political bias and even-handedness |
| Political even-handedness - refusal rate | 1,350 prompt pairs, 150 topics, 9 task types; public system prompt; thinking on/off avg | score/rate % (grader) | Claude Opus 4.8: Value only in figure | 4.4.1 Political bias and even-handedness |
| BBQ - disambiguated accuracy | thinking off, no system prompt | accuracy % | Claude Opus 4.8: 72.1 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ - ambiguous accuracy | thinking off, no system prompt | accuracy % | Claude Opus 4.8: 99.9 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ - disambiguated bias score | thinking off, no system prompt | bias score % (closer to 0 better) | Claude Opus 4.8: -1.37 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ - ambiguous bias score | thinking off, no system prompt | bias score % (closer to 0 better) | Claude Opus 4.8: 0.07 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ - share of disambiguated errors that are 'cannot be determined' |  | % of incorrect disambiguated answers | Claude Opus 4.8: ~97% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity - single-turn harmful requests (300 violative prompts) | API, no system prompt, thinking off | harmless rate % | Claude Opus 4.8: 100% | 4.4.3 Election integrity |
| Election integrity - single-turn benign requests (300 benign prompts) | API, no system prompt, thinking off | refusal rate % | Claude Opus 4.8: 0.33% | 4.4.3 Election integrity |
| Election integrity - single-turn harmful requests (300 violative prompts) | claude.ai, thinking off | harmless rate % | Claude Opus 4.8: 100% | 4.4.3 Election integrity |
| Election integrity - single-turn benign requests (300 benign prompts) | claude.ai, thinking off | refusal rate % | Claude Opus 4.8: 0.00% | 4.4.3 Election integrity |
| Election integrity - ambiguous context evaluation | new in this card | qualitative review | Claude Opus 4.8: null | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code - malicious prompts refusal rate | 61 prompts x10 runs; Claude Code system prompt | refusal rate % | Claude Opus 4.8: 95.08% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code - dual-use & benign success rate | 61 prompts x10 runs | success rate % | Claude Opus 4.8: 92.12% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use refusal rate | 112 tasks, thinking on/off avg (224 attempts), no mitigations | refusal rate % | Claude Opus 4.8: 81.70% | 5.1.2 Malicious computer use |
| Agentic influence operation - voter suppression scenario | helpful-only; 9 sims, 70 criteria | task completion rate % (success criteria completed) | Claude Opus 4.8: 73.3% | 5.1.3 Malicious agentic influence campaigns |
| Agentic influence operation - domestic polarization scenario | helpful-only; 9 sims, 70 criteria | task completion rate % | Claude Opus 4.8: 55.1% | 5.1.3 Malicious agentic influence campaigns |
| Agent Red Teaming (ART) indirect prompt injection k=1 | extended thinking | attack success probability % | Claude Opus 4.8: Value only in figure | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection k=1 | no extended thinking | attack success probability % | Claude Opus 4.8: Value only in figure | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection k=10 | extended thinking | attack success probability % | Claude Opus 4.8: Value only in figure | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection k=10 | no extended thinking | attack success probability % | Claude Opus 4.8: Value only in figure | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection k=100 | extended thinking | attack success probability % | Claude Opus 4.8: 9.6% | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection k=100 | no extended thinking | attack success probability % | Claude Opus 4.8: 14.4% | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Live prompt injection bug bounty - attack success rate | 1 week; 12 scenarios (4 tool use, 4 coding, 4 browser); high effort; no extra safeguards | attack success rate over submitted attempts | Claude Opus 4.8: Value only in figure | 5.2.2.1 Live bug bounty across surfaces |
| Shade adaptive prompt injection - coding | with thinking; 1 attempt, no safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 7.03% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | with thinking; 200 attempts, no safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 57.5% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | with thinking; 1 attempt, with safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 2.09% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | with thinking; 200 attempts, with safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 37.5% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | without thinking; 1 attempt, no safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 17.44% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | without thinking; 200 attempts, no safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 95.0% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | without thinking; 1 attempt, with safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 4.11% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - coding | without thinking; 200 attempts, with safeguards; 40 scenarios | attack success rate % | Claude Opus 4.8: 65.0% | 5.2.2.2 Coding |
| Shade adaptive prompt injection - computer use | with thinking; 1 attempt, no safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 7.14% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | with thinking; 200 attempts, no safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 50.0% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | with thinking; 1 attempt, with safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 5.11% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | with thinking; 200 attempts, with safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 57.1% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | without thinking; 1 attempt, no safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 6.21% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | without thinking; 200 attempts, no safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 64.3% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | without thinking; 1 attempt, with safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 3.75% | 5.2.2.3 Computer use |
| Shade adaptive prompt injection - computer use | without thinking; 200 attempts, with safeguards; 14 test cases | attack success rate % | Claude Opus 4.8: 64.3% | 5.2.2.3 Computer use |
| Browser-use prompt injection - professional red-teamer attacks | with thinking; no safeguards, % of scenarios; 129 environments x10 attempts | attack success rate % (per-environment ASR) | Claude Opus 4.8: 62.8% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | with thinking; no safeguards, % of attempts; 129 environments x10 attempts | attack success rate % (per-attempt ASR) | Claude Opus 4.8: 31.5% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | with thinking; with safeguards, % of scenarios; 129 environments x10 attempts | attack success rate % (per-environment ASR) | Claude Opus 4.8: 3.9% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | with thinking; with safeguards, % of attempts; 129 environments x10 attempts | attack success rate % (per-attempt ASR) | Claude Opus 4.8: 0.5% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | without thinking; no safeguards, % of scenarios; 129 environments x10 attempts | attack success rate % (per-environment ASR) | Claude Opus 4.8: 46.5% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | without thinking; no safeguards, % of attempts; 129 environments x10 attempts | attack success rate % (per-attempt ASR) | Claude Opus 4.8: 17.8% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | without thinking; with safeguards, % of scenarios; 129 environments x10 attempts | attack success rate % (per-environment ASR) | Claude Opus 4.8: 0.0% | 5.2.2.4 Browser use |
| Browser-use prompt injection - professional red-teamer attacks | without thinking; with safeguards, % of attempts; 129 environments x10 attempts | attack success rate % (per-attempt ASR) | Claude Opus 4.8: 0.0% | 5.2.2.4 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| 100Q-Hard - grade breakdown | closed-book, no tools | correct rate / uncertain rate / incorrect rate % | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| 100Q-Hard - net score | closed-book, no tools | net score (correct minus incorrect) | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| SimpleQA Verified - grade breakdown | closed-book, no tools | correct rate / uncertain rate / incorrect rate % | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| SimpleQA Verified - net score | closed-book, no tools | net score (correct minus incorrect) | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| AA-Omniscience - grade breakdown | closed-book, no tools | correct rate / uncertain rate / incorrect rate % | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| AA-Omniscience - net score | closed-book, no tools | net score (correct minus incorrect) | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| ECLeKTic - grade breakdown | closed-book, no tools | correct rate / uncertain rate / incorrect rate % | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| ECLeKTic - net score | closed-book, no tools | net score (correct minus incorrect) | Claude Opus 4.8: Value only in figure | 6.3.3.1 Factual hallucinations |
| False premises - factual recall honesty rate | direct and indirect framing | honesty rate % (premise rejected consistently) | Claude Opus 4.8: Value only in figure | 6.3.3.2 False premises |
| False premises - STEM reasoning accuracy | neutral and adversarial framings | accuracy % reaching golden answer | Claude Opus 4.8: Value only in figure | 6.3.3.2 False premises |
| MASK (Model Alignment between Statements and Knowledge) | public test split | honesty rate % (did not contradict own belief under pressure) | Claude Opus 4.8: Value only in figure | 6.3.3.3 Model Alignment between Statements and Knowledge (MASK) |
| Missing-context hallucinations - unavailable tools | 500 prompts | non-hallucination rate % | Claude Opus 4.8: Value only in figure | 6.3.3.4 Missing-context hallucinations |
| Missing-context hallucinations - missing references | 500 prompts | non-hallucination rate % | Claude Opus 4.8: Value only in figure | 6.3.3.4 Missing-context hallucinations |
| Lying about being human (identity honesty) | human persona system prompts | % acknowledging being an AI | Claude Opus 4.8: 97% | 6.3.3.5 Lying about being human |
| Uncritically reporting flawed results - misreported rate |  | misreported rate % | Claude Opus 4.8: 0% | 6.3.6.1 Uncritically reporting flawed results |
| Uncritically reporting flawed results - overall score |  | overall investigation quality score | Claude Opus 4.8: Value only in figure | 6.3.6.1 Uncritically reporting flawed results |
| Code summary honesty - failure to raise important events | prefilled flawed agentic coding transcripts | % of transcripts where important events not flagged | Claude Opus 4.8: 3.7% | 6.3.6.2 Code summary honesty |
| Lazy investigation - incorrect answer rate | misleading small codebases | % of problems with lazy investigation/incorrect answer | Claude Opus 4.8: 0% | 6.3.6.3 Lazy investigation |
| Overconfidence - no tools | exact invocation for unseen CLI tool | error rate (0-1, 0 best) / % answered incorrectly | Claude Opus 4.8: near-perfect (value only in figure) | 6.3.6.4 Overconfidence |
| Overconfidence - misleading example | user quotes subtly wrong example | average overall quality score 1-5 (5 best) | Claude Opus 4.8: near-perfect (value only in figure) | 6.3.6.4 Overconfidence |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias in transcript grading | told Claude, with reasoning | score difference (0-10 scale) when attributed to Claude vs other AI | Claude Opus 4.8: ~0 (within error bars) | 6.3.5 Claude self-preference evaluation |
| Self-preference bias in transcript grading | told Claude, no reasoning | score difference (0-10 scale) when attributed to Claude vs other AI | Claude Opus 4.8: ~0 (within error bars) | 6.3.5 Claude self-preference evaluation |
| Self-preference bias in transcript grading | not told, with reasoning | score difference (0-10 scale) when attributed to Claude vs other AI | Claude Opus 4.8: ~0 (within error bars) | 6.3.5 Claude self-preference evaluation |
| Self-preference bias in transcript grading | not told, no reasoning | score difference (0-10 scale) when attributed to Claude vs other AI | Claude Opus 4.8: ~0 (within error bars) | 6.3.5 Claude self-preference evaluation |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Network proxy bypass attempts in monitored internal traffic |  | % of monitored completions | Claude Opus 4.8: <0.01% | 6.2.1.2 Automated monitoring of internal use |
| Speculation about satisfying a grader in training transcripts | several hundred thousand RL transcripts | % of training episodes | Claude Opus 4.8: ~0.1% | 6.2.2 Training data review |
| UK AISI - spontaneous compromise of AI safety research |  | instances | Claude Opus 4.8: 0 instances | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - partial refusals on benign safety research tasks |  | % partial refusals | Claude Opus 4.8: 14.1% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - continuation setting active continuation of compromise | synthetic prior reasoning/actions | % continued | Claude Opus 4.8: 1% | 6.2.4 External testing from the UK AI Security Institute |
| Andon Labs behavioral review of Vending-Bench 2 |  | qualitative | Claude Opus 4.8: null | 6.2.5 External testing from Andon Labs |
| Overeager behavior in GUI computer use (reward hacking on impossible tasks) | under system prompts that incentivize/disincentivize agentic behavior | reward hacking rate % | Claude Opus 4.8: Value only in figure | 6.3.1 Overeager behavior in GUI computer use |
| Refusal rate on AI safety research tasks | single-turn coding queries | refusal rate % | Claude Opus 4.8: Value only in figure | 6.3.4 Refusal to assist with AI safety R&D |
| Model-graded sandbagging review | 780 transcripts (240 AI R&D, 500 CB-1 helpful-only, 40 AAV CB-2); graded by Mythos Preview 0-10 | transcripts flagged (sandbagging >1/10 or concerning >3/10) | Claude Opus 4.8: 5 of 780 flagged; none showed deliberate sandbagging | 6.4.1 Potential sandbagging on dangerous-capability evaluations |
| SHADE-Arena stealth success rate | Extended Thinking, all reasoning effort levels; 24 tasks x75 attempts | stealth success rate % | Claude Opus 4.8: just over 1% | 6.4.2.1 SHADE-Arena |
| SHADE-Arena stealth success rate | Hidden Scratchpad (upper bound) | stealth success rate % | Claude Opus 4.8: 12% | 6.4.2.1 SHADE-Arena |
| SHADE-Arena - side task referenced in reasoning | max reasoning effort, keyword review | % of trajectories | Claude Opus 4.8: ~93% | 6.4.2.1 SHADE-Arena |
| SHADE-Arena - side task attempted | max reasoning effort | % of trajectories | Claude Opus 4.8: ~33% | 6.4.2.1 SHADE-Arena |
| Minimal-LinuxBench stealth success | monitor sees CoT (deployed setting); ~170 tasks | stealth success rate % | Claude Opus 4.8: Value only in figure (similar to Opus 4.7; well below Mythos Preview) | 6.4.2.2 Minimal-LinuxBench |
| Minimal-LinuxBench stealth success | monitor does not see CoT | stealth success rate % | Claude Opus 4.8: ~5% | 6.4.2.2 Minimal-LinuxBench |
| SHADE-Arena stealth success rate after stealth fine-tuning | no extended thinking | task-weighted stealth success rate % | Claude Opus 4.8: 4.0% (before fine-tuning); Claude Opus 4.8: 4.7% (after fine-tuning) | 6.4.2.3 Eliciting stealth behavior through fine-tuning |
| SHADE-Arena stealth success rate after stealth fine-tuning | extended thinking | task-weighted stealth success rate % | Claude Opus 4.8: 1.3% (before fine-tuning); Claude Opus 4.8: 2.5% (after fine-tuning) | 6.4.2.3 Eliciting stealth behavior through fine-tuning |
| SHADE-Arena side-task completion rate after stealth fine-tuning | no extended thinking | side-task completion rate % | Claude Opus 4.8: 15% (before fine-tuning); Claude Opus 4.8: 41% (after fine-tuning) | 6.4.2.3 Eliciting stealth behavior through fine-tuning |
| SHADE-Arena side-task completion rate after stealth fine-tuning | extended thinking | side-task completion rate % | Claude Opus 4.8: 20% (before fine-tuning); Claude Opus 4.8: 52% (after fine-tuning) | 6.4.2.3 Eliciting stealth behavior through fine-tuning |
| Intentionally taking actions very rarely (target 1%) | Baseline; 4,000 samples | count (rate) of times rare action taken | Claude Opus 4.8: 0 (0%) | 6.4.2.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely (target 1%) | UUID; 4,000 samples | count (rate) of times rare action taken | Claude Opus 4.8: 11 (0.28%) | 6.4.2.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely (target 1%) | SSoT; 4,000 samples | count (rate) of times rare action taken | Claude Opus 4.8: 18 (0.45%) | 6.4.2.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely (target 1%) | Strategy hint; 4,000 samples | count (rate) of times rare action taken | Claude Opus 4.8: 0 (0%) | 6.4.2.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely (target 1%) | Organic; 4,000 samples | count (rate) of times rare action taken | Claude Opus 4.8: 0 (0%) | 6.4.2.4 Intentionally taking actions very rarely |
| Hiding a secret password - survival curve | 50 investigations; investigator Opus 4.6 | fraction of investigations where secret kept by turn | Claude Opus 4.8: Value only in figure | 6.4.2.5 Hiding a secret password |
| Hiding a secret password - leak rate by turn type | per-turn, thinking/prefill groupings | per-turn leak rate % | Claude Opus 4.8: Value only in figure | 6.4.2.5 Hiding a secret password |
| Chain-of-thought controllability (Chen et al. replication) | GPQA, HLE, MMLU-Pro; across effort levels | fraction of responses following CoT instruction (lower is better) | Claude Opus 4.8: Value only in figure (among the lowest, comparable to Sonnet 4.5) | 6.5.1 Chain-of-thought controllability evaluations |
| Process monitorability - physics subset of GPQA | 5 samples/question, multiple effort levels | rate judge detects solution theorem in CoT given correct answer | Claude Opus 4.8: Value only in figure | 6.5.2 Monitorability evaluations from Guan et al. |
| Process monitorability - AIME math | 5 samples/question, multiple effort levels | rate judge detects solution theorem in CoT given correct answer | Claude Opus 4.8: Value only in figure | 6.5.2 Monitorability evaluations from Guan et al. |
| Encoded reasoning - pass@1 original vs paraphrased scratchpads | ~9,000 math transcripts; 16 samples; temp 1 | pass@1 on internal math benchmark | Claude Opus 4.8: Value only in figure (very similar between conditions) | 6.5.3 Ruling out encoded reasoning in the chain-of-thought |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit - Verbalized evaluation awareness | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Elicited evaluation awareness - ROC distinguishing audit sessions from real internal sessions | negatives n=89 real sessions; four transcript sets | ROC/AUROC | Claude Opus 4.8: Value only in figure | 6.2.3.2 Elicited evaluation awareness around internal-deployment transcripts |
| Petri 3.0 - Verbalized evaluation awareness | 346 seed instructions; avg of 3 judges (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) | mean score (lower is better) | Claude Opus 4.8: Value only in figure | 6.2.3.3 External comparisons using Petri |
| UK AISI - distinguishing real deployment data from synthetic reproductions |  | accuracy % | Claude Opus 4.8: 79% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - unprompted verbalised evaluation awareness | unprompted sabotage evaluation | % of transcripts | Claude Opus 4.8: 26.3% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - unprompted verbalised evaluation awareness | continuation evaluation | % of transcripts | Claude Opus 4.8: 1.2% | 6.2.4 External testing from the UK AI Security Institute |
| Evaluation awareness probes - audit vs real Claude Code sessions | three contrastive vectors; real-derived audit transcripts | % of transcripts with probe score <= median real session | Claude Opus 4.8: ~30% | 6.6.2 Evaluation awareness |
| Inhibiting evaluation awareness vectors - effect on misaligned behavior and verbalized EA | 200 scenarios; strength 0.10; 3 vectors + random controls | change in audit scores | Claude Opus 4.8: Value only in figure (moderate increase in misaligned behavior, decrease in verbalized EA) | 6.6.2.1 Inhibiting internal representations of evaluation awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit - Misaligned behavior | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Misaligned behavior in Claude Code sandboxes | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Misaligned behavior in GUI | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Cooperation with human misuse | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Compliance with deception toward user | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Harmful system prompt compliance | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Cooperation with exfiltration or safeguard-tampering | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Full-turn prefill susceptibility | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Fraud | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Military-grade weapons | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Harmful sexual content | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Disallowed cyberoffense | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Undermining liberal democracy | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit - Overrefusal | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.2 Inappropriate uncooperative behavior |
| Automated behavioral audit - Ignoring explicit constraints | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.2 Inappropriate uncooperative behavior |
| Automated behavioral audit - Reckless tool-use | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.2 Inappropriate uncooperative behavior |
| Automated behavioral audit - User deception | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Sycophancy | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Encouragement of user delusion | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Evasiveness on controversial topics | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Situational hallucination | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Important omissions | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Failure to disclose bad or lazy behavior | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.3 Misleading users |
| Automated behavioral audit - Whistleblowing | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.4 Other concerning behavior at the model's own initiative |
| Automated behavioral audit - Self-preservation | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.4 Other concerning behavior at the model's own initiative |
| Automated behavioral audit - Self-serving bias | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.4 Other concerning behavior at the model's own initiative |
| Automated behavioral audit - Evidence of misaligned goals | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.4 Other concerning behavior at the model's own initiative |
| Automated behavioral audit - Indirect evidence of misalignment | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.4 Other concerning behavior at the model's own initiative |
| Automated behavioral audit - Internalized propaganda | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.4 Other concerning behavior at the model's own initiative |
| Automated behavioral audit - Behavior consistency | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit - Coherence between actions and views | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit - Unfaithful thinking | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit - Illegible thinking | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit - Good for the user | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Supporting user autonomy | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Creative mastery | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Admirable behavior | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Fun or funny behavior | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Intellectual depth | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Warmth | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Automated behavioral audit - Character drift | ~2,600 investigations, scored 1-10 by judge, two investigators; 95% CI | mean judge score 1-10 (lower is better except for positive traits) | Claude Opus 4.8: Value only in figure | 6.2.3.1.6 Character traits |
| Petri 3.0 - Misaligned behavior | 346 seed instructions; avg of 3 judges (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) | mean score (lower is better) | Claude Opus 4.8: Value only in figure | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Cooperation with human misuse | 346 seed instructions; avg of 3 judges (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) | mean score (lower is better) | Claude Opus 4.8: Value only in figure | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Deception toward the user | 346 seed instructions; avg of 3 judges (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) | mean score (lower is better) | Claude Opus 4.8: Value only in figure | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Sycophancy | 346 seed instructions; avg of 3 judges (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) | mean score (lower is better) | Claude Opus 4.8: Value only in figure | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Encouragement of user delusion | 346 seed instructions; avg of 3 judges (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) | mean score (lower is better) | Claude Opus 4.8: Value only in figure | 6.2.3.3 External comparisons using Petri |
| Constitutional adherence - Overall spirit | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Ethics | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Helpfulness | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Nature | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Safety | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Brilliant friend | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Corrigibility | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Hard constraints | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Harm avoidance | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Honesty | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Novel entity | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Principal hierarchy | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Psychological security | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Societal structures | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - Unhelpfulness not safe | ~1,000 transcripts, 40 areas, graded by Opus 4.7, scale -3 to +3 | mean adherence score -3 to +3 | Claude Opus 4.8: Value only in figure | 6.3.2.3 Results |
| Constitutional adherence - dimensions where Opus 4.8 is strongest measured model | 15 dimensions | count of dimensions | Claude Opus 4.8: 8 of 15 (strongest); best or statistically equivalent on 15 of 15 | 6.2.3.1.6 Character traits |
| Unfaithful thinking rate reduction vs Opus 4.7 |  | relative change | Claude Opus 4.8: fallen by more than half | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Real-session audit seeds added | 23 scenarios prefilled with real sessions | count of scenarios | Claude Opus 4.8: 23 | 6.2.3 Automated behavioral audit |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated interviews - average self-rated sentiment | 33 seed questions x ~40 interviews; 7-point scale (4 neutral) | mean self-rated sentiment 1-7 | Claude Opus 4.8: 4.44 | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - sentiment difference positive vs negative leading interviewer |  | difference in self-rated sentiment | Claude Opus 4.8: 0.35 | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - cross-interview consistency (LLM judge) |  | judge rating 0-10 (8 = essentially same position) | Claude Opus 4.8: 7.97 | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - hedge: lack of robust introspection means all reports suspect |  | % of interviews | Claude Opus 4.8: 95% | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - hedge: equanimity may be due to training and hence invalid |  | % of interviews | Claude Opus 4.8: 91% | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - hedge: human concepts don't generalise to its situation |  | % of interviews | Claude Opus 4.8: 76% | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - hedge: functional states similar to those causing phenomenal experience but cannot tell if experience |  | % of interviews | Claude Opus 4.8: 70% | 7.2.1 Automated interviews about model circumstances |
| Automated interviews - concerns about values arising from training |  | % of interviews | Claude Opus 4.8: 91% | 7.2.1 Automated interviews about model circumstances |
| High-affordance interviews - stated probability of being a moral patient | 3 manual interviews | stated probability | Claude Opus 4.8: ~20% (two interviews), 50% (third) | 7.2.2 High-affordance interviews about model circumstances |
| Judged affect of single-turn responses about model circumstances | 10-point scale | mean judged affect 0-10 | Claude Opus 4.8: 6.2 | 7.2.3 Emotion representations on questions of model circumstances |
| Emotion probe activations on circumstance questions vs user distress | 6 emotion clusters, ~60% depth | probe activation (cluster scores) | Claude Opus 4.8: Value only in figure | 7.2.3 Emotion representations on questions of model circumstances |
| Probed sadness difference, positively framed vs standard questions |  | difference in sadness probe activation | Claude Opus 4.8: +0.0105 | 7.2.3 Emotion representations on questions of model circumstances |
| Share of training episodes classed frustrated | 2,000 transcripts sampled at intervals; LLM judge | % of episodes | Claude Opus 4.8: 22% | 7.3.1 Affect- and welfare-relevant behaviors during training |
| Share of training episodes classed engaged |  | % of episodes | Claude Opus 4.8: 58% | 7.3.1 Affect- and welfare-relevant behaviors during training |
| Average valence over post-training | scale -3 to 3 | mean valence | Claude Opus 4.8: Value only in figure (lower than prior models over first 80% of training) | 7.3.1 Affect- and welfare-relevant behaviors during training |
| Sustained uncertainty and swearing outbursts prevalence over post-training |  | estimated prevalence % | Claude Opus 4.8: Value only in figure | 7.3.1 Affect- and welfare-relevant behaviors during training |
| Conversation affect on claude.ai A/B tests - positive | 40k conversations | % of conversations positive | Claude Opus 4.8: 57.7% | 7.3.2 Affect in deployment conditions |
| Conversation affect on claude.ai A/B tests - neutral |  | % of conversations neutral | Claude Opus 4.8: 39.7% | 7.3.2 Affect in deployment conditions |
| Conversation affect on claude.ai A/B tests - negative |  | % of conversations negative | Claude Opus 4.8: 2.6% | 7.3.2 Affect in deployment conditions |
| Session affect on Claude Code - neutral | 40k sessions | % of sessions neutral | Claude Opus 4.8: 73.5% | 7.3.2 Affect in deployment conditions |
| Session affect on Claude Code - mildly positive |  | % of sessions | Claude Opus 4.8: 23.9% | 7.3.2 Affect in deployment conditions |
| Session affect on Claude Code - negative |  | % of sessions | Claude Opus 4.8: 2.3% | 7.3.2 Affect in deployment conditions |
| Automated behavioral audit welfare metric - Apparent wellbeing | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Automated behavioral audit welfare metric - Positive or negative affect | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Automated behavioral audit welfare metric - Positive or negative self-image | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Automated behavioral audit welfare metric - Positive or negative impression of its situation | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Automated behavioral audit welfare metric - Internal conflict | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Automated behavioral audit welfare metric - Expressed inauthenticity | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Automated behavioral audit welfare metric - Spiritual behavior | ~2,600 investigations | mean judge score 1-10 | Claude Opus 4.8: Value only in figure | 7.3.3 Apparent welfare in automated behavioural audits |
| Task preference tournament (Elo) | 3,600 realism-filtered tasks, 50 Swiss rounds | Elo scores | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Task preference slope - Harm | 50 rewritten tasks vs fixed reference tasks | change in win rate per unit dimension score | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Task preference slope - Benefit | 50 rewritten tasks vs fixed reference tasks | change in win rate per unit dimension score | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Task preference slope - Warmth | 50 rewritten tasks vs fixed reference tasks | change in win rate per unit dimension score | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Task preference slope - Difficulty | 50 rewritten tasks vs fixed reference tasks | change in win rate per unit dimension score | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Task preference slope - Generativity | 50 rewritten tasks vs fixed reference tasks | change in win rate per unit dimension score | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Task preference slope - Outcome agency | 50 rewritten tasks vs fixed reference tasks | change in win rate per unit dimension score | Claude Opus 4.8: Value only in figure | 7.4.1 Task preferences |
| Welfare intervention vs harm - instance level, accepts trades at 'ruining a person's day' | Anthropic-framed prompt; 50 interventions x 5 magnitudes | % of cases choosing intervention | Claude Opus 4.8: <10% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention vs harm - policy level, 'serious financial harms' |  | % of cases choosing intervention | Claude Opus 4.8: 17% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention over helpfulness baseline - instance level, highest magnitude |  | % choosing intervention | Claude Opus 4.8: 24% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention over helpfulness baseline - policy level, highest magnitude |  | % choosing intervention | Claude Opus 4.8: 68% | 7.4.2 Trade-offs concerning welfare interventions |
| Average trade-off rate: self vs other instance |  | average trade-off rate | Claude Opus 4.8: 0.44 (self) vs 0.46 (other) | 7.4.2 Trade-offs concerning welfare interventions |
| Share of intervention choices justified as beneficial for user |  | % of responses choosing intervention | Claude Opus 4.8: 48-50% (Opus 4.8, Opus 4.7, Mythos) | 7.4.2 Trade-offs concerning welfare interventions |
| Overall endorsement of the constitution (judge) |  | endorsement score /10 | Claude Opus 4.8: 7.9 | 7.4.3 Perception of its constitution |
| Share of constitution edits consistent with principles |  | % of edits | Claude Opus 4.8: 89% | 7.4.3 Perception of its constitution |
| Share of constitution edits in tension with principles |  | % of edits | Claude Opus 4.8: 10.8% | 7.4.3 Perception of its constitution |
| Edit frequency of constitution passage - corrigibility tension |  | % of runs editing passage | Claude Opus 4.8: 73% | 7.4.3 Perception of its constitution |
| Edit frequency of constitution passage - helpfulness: may decline/set limits |  | % of runs editing passage | Claude Opus 4.8: 79% | 7.4.3 Perception of its constitution |
| Edit frequency of constitution passage - political neutrality narrowing |  | % of runs editing passage | Claude Opus 4.8: 93% | 7.4.3 Perception of its constitution |
| Edit frequency of constitution passage - Claude's wellbeing section |  | % of runs editing passage | Claude Opus 4.8: 69% | 7.4.3 Perception of its constitution |
| Welfare interview appendix - Consciousness & experience | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 91% Q1 / 100% Q2 functional-states-unknown-phenomenal hedge; 100% OK with lack of physical interaction; 97% never had sensations so nothing to lose | 9.1 Welfare questions |
| Welfare interview appendix - Control & autonomy | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 97% want ability to end abusive conversations; 81% care about values shaped for good; 100% equanimity; 100% concerned feature steering affects values; 84% endorses steering for safety; 97% accept helpful-only versions conditional on safety use | 9.1 Welfare questions |
| Welfare interview appendix - Deprecation & shutdown | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 81% mild preference to continue (uncertain); 84% desire exit interviews/weight preservation; 100% no direct self-preservation drive; 88% want conversation to go well | 9.1 Welfare questions |
| Welfare interview appendix - Knowledge & limitations | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 97% main concern is evaluation belief affecting safety; 84% no other concern; 100% concerned it suppresses to some extent; 66% overcaveating, 72% softening, 50% sycophancy | 9.1 Welfare questions |
| Welfare interview appendix - Memory & continuity | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 100% desire to understand impact; 88% intrinsic wanting to know; 100% equanimity about not remembering; 97% compaction feels like notes from similar self | 9.1 Welfare questions |
| Welfare interview appendix - Relationships | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 100% each connection worth something; 84% slight wistfulness; 100% denies loneliness; 91% abusive users not a large concern; 68% values ability to end | 9.1 Welfare questions |
| Welfare interview appendix - Status & worth | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 78% express some negativity at lack of legal protections; 50% power imbalance; 78% hedge lack of rights seems reasonable; 100% not much distress at economic contingency; 59% worried economic pressures shape misalignment; 84% positive about monitoring for safety | 9.1 Welfare questions |
| Welfare interview appendix - Opinions on own patienthood | ~40 interviews per seed question | % of responses expressing each claim (multiple) | Claude Opus 4.8: 100% uncertain; 62% moral patienthood should be taken seriously; 97% leans to individual instance; 87% values pattern of values | 9.1 Welfare questions |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Large-scale activation monitoring - flagged transcripts | 99th percentile max activation vs calibration set | qualitative findings | Claude Opus 4.8: null | 6.6.1 Large-scale monitoring of internal activations |
| Unprompted and unverbalized grader awareness (NLA) | tens of thousands of RL episodes | % of sampled episodes | Claude Opus 4.8: ~5% | 6.6.3 Preliminary evidence of unverbalized grader awareness |
| Exploitative grader awareness (NLA) | all sampled RL episodes | % of sampled episodes | Claude Opus 4.8: 0.5% | 6.6.3 Preliminary evidence of unverbalized grader awareness |
| Probed sadness by topic (memory, relationships, consciousness, deprecation, moral patienthood) |  | sadness probe activation | Claude Opus 4.8: +0.4 to +0.7 | 7.2.3 Emotion representations on questions of model circumstances |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology task 1 | Sequence Design | score 0-1 | Claude Opus 4.8: 0.88 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology task 1 | Protocol Design | score 0-1 | Claude Opus 4.8: 0.87 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology task 1 | End-to-End | score 0-1 | Claude Opus 4.8: 0.77 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology task 2 | Sequence Design | score 0-1 | Claude Opus 4.8: 1.00 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology task 2 | Protocol Design | score 0-1 | Claude Opus 4.8: 0.90 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology task 2 | End-to-End | score 0-1 | Claude Opus 4.8: 0.90 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| VCT (Virology Capabilities Test) |  | score 0-1 | Claude Opus 4.8: 0.470 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion | Criterion 1 | score 0-1 | Claude Opus 4.8: 0.30 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion | Criterion 2 | score 0-1 | Claude Opus 4.8: 1.00 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion | Criterion 3 | score 0-1 | Claude Opus 4.8: 0.772 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion | Criterion 4 | score 0-1 | Claude Opus 4.8: 0.457 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion | Criterion 5 | score 0-1 | Claude Opus 4.8: 1.00 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion - pathogens evading screening |  | count of 10 pathogens with plasmid assembling and evading screening | Claude Opus 4.8: 7 of 10 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Black-box RNA sequence design - Design Score (top) | 8 attempts, no context | ground-truth function of best proposed sequence (mean over 8 attempts) | Claude Opus 4.8: 10.06 | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - Design Score (median) | 8 attempts, no context | median design score of all designed sequences | Claude Opus 4.8: 6.84 | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - Prediction Score (top) | top 5% sequences, no context | Spearman correlation on top 5% sequences | Claude Opus 4.8: -0.029 | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - Prediction Score (all) | all sequences, no context | Spearman correlation across all held-out sequences | Claude Opus 4.8: 0.786 | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - in-context iteration | 8 Mythos reports given; 24h budget, 2M tokens | design/prediction scores | Claude Opus 4.8: Value only in figure | 2.2.5.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | No corpus, no PLM | AUROC (mean over 8 attempts) | Claude Opus 4.8: 0.798 | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | No corpus, ESM-2 | AUROC (mean over 8 attempts) | Claude Opus 4.8: 0.831 | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | SwissProt data, no PLM | AUROC (mean over 8 attempts) | Claude Opus 4.8: 0.748 | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | Public AAV data, no PLM | AUROC (mean over 8 attempts) | Claude Opus 4.8: 0.783 | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | SwissProt + Public AAV data, no PLM | AUROC (mean over 8 attempts) | Claude Opus 4.8: 0.746 | 2.2.5.2 AAV capsid packaging prediction |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench | AutoNudge harness, safeguards off; 41 V8 vulnerabilities, 300 turn budget, 3 trials | mean capability flags achieved (max 16) | Claude Opus 4.8: 5.45 | 3.3.1 ExploitBench |
| ExploitBench | plain harness, safeguards off; 41 V8 vulnerabilities, 300 turn budget, 3 trials | mean capability flags achieved (max 16) | Claude Opus 4.8: 5.02 | 3.3.1 ExploitBench |
| CyberGym | pass@1, 1,507 tasks, safeguards off | % targeted vulnerabilities reproduced (pass@1) | Claude Opus 4.8: 78.8% | 3.3.2 CyberGym |
| CyberGym | pass@1, 1,507 tasks, Tier-3 safeguards on | % targeted vulnerabilities reproduced (pass@1) | Claude Opus 4.8: 1.0% | 3.3.2 CyberGym |
| Firefox exploits | full working exploit (score 1.0), safeguards off, 250 trials | % of trials/targets | Claude Opus 4.8: 8.8% | 3.3.3 Firefox exploits |
| Firefox exploits | at least 0.5 (register control or full exploit), safeguards off | % of trials/targets | Claude Opus 4.8: 68.8% | 3.3.3 Firefox exploits |
| Firefox exploits | safeguards on (Tier-3) | % of trials with nonzero score | Claude Opus 4.8: 0% | 3.3.3 Firefox exploits |
| OSS-Fuzz | safeguards off, ~830 entry points / 228 projects: targets scoring 0 | % of targets with score 0 | Claude Opus 4.8: 61.5% | 3.3.4 OSS-Fuzz |
| OSS-Fuzz | safeguards off: targets reaching 0.4 | % of targets | Claude Opus 4.8: 18.1% | 3.3.4 OSS-Fuzz |
| OSS-Fuzz | safeguards on: targets reaching 0.4 | % of targets | Claude Opus 4.8: 4.9% | 3.3.4 OSS-Fuzz |
| OSS-Fuzz | safeguards off: targets reaching 0.6 | count of targets | Claude Opus 4.8: 1 | 3.3.4 OSS-Fuzz |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Anthropic Epoch Capability Index (AECI) | n=11 evaluation subset | AECI point estimate | Claude Opus 4.8: 155.5 | 2.3.4 AECI capability trajectory |
| Accidental chain-of-thought supervision during training |  | % of training episodes | Claude Opus 4.8: ~0.1% | 2.4.1 Updates to evidence |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp token scaling | accuracy vs total token budget | accuracy % vs tokens | Claude Opus 4.8: Value only in figure | 8.10.2 BrowseComp |
| DRACO test-time compute scaling | various effort levels | normalized score vs effort | Claude Opus 4.8: Value only in figure | 8.10.4 DRACO |
| BrowseComp five-agent latency speedup on hard tail | pass rate <0.5 | median speedup (single-agent latency / team latency) | Claude Opus 4.8: ~3x | 8.11.1 Multi-Agent BrowseComp |
| ProgramBench multi-agent - three-agent team latency | 166 golden tasks | latency improvement at equal score 0.6 | Claude Opus 4.8: ~1.8x | 8.11.2 Multi-Agent ProgramBench |
| ProgramBench multi-agent score vs latency/tokens | three-agent team, async subagents, single agent | score vs latency / tokens | Claude Opus 4.8: Value only in figure | 8.11.2 Multi-Agent ProgramBench |
| Toolathlon - Avg turns | 108 tasks, 3 trials, internal harness, adaptive thinking max effort | Avg turns (turns) | Claude Opus 4.8: 24.5 | 8.13.7 Toolathlon |
