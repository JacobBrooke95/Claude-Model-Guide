# System Card: Claude Fable 5 & Claude Mythos 5

Released 2026-06-09. 465 metric entries. [Source PDF](https://anthropic.com/claude-fable-5-mythos-5-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | 500 problems, adaptive thinking max effort, avg of 5 trials | % resolved | Claude Mythos 5: 95.5%; Claude Fable 5: 95% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro | avg of 5 trials, max effort | % resolved | Claude Mythos 5: 80.3%; Claude Fable 5: 80% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, 9 languages, avg of 5 trials | % resolved | Claude Mythos 5: 92.2% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness, avg of 5 trials | % resolved | Claude Mythos 5: 54.9% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| Terminal-Bench 2.1 | mini-SWE-agent harness, high effort, 89 tasks x5 attempts | mean reward % | Claude Mythos 5: 88%; Claude Fable 5: 84.3% | 8.3 Terminal-Bench 2.1 |
| FrontierCode (Diamond) - score | xhigh effort, mean@5 | weighted score % | Claude Fable 5: 29.3% | 8.4 FrontierCode |
| FrontierCode (Diamond) - pass rate | xhigh effort, mean@5 | patch correctness pass rate % | Claude Fable 5: 30.2% | 8.4 FrontierCode |
| FrontierCode (Main) - score | xhigh effort, mean@5 | weighted score % | Claude Fable 5: 46.3% | 8.4 FrontierCode |
| FrontierCode (Main) - pass rate | xhigh effort, mean@5 | patch correctness pass rate % | Claude Fable 5: 48.8% | 8.4 FrontierCode |
| FrontierSWE | 17 ultra-long-horizon problems, 20h each, mean@5 | mean@5 (as printed; Fable ranked #1) | Claude Fable 5: 2.12 | 8.5 FrontierSWE |
| ProgramBench | 166 tasks after excluding flaky, hidden test pass rate across 1-5 episodes | hidden test pass rate % | Claude Mythos 5: 84-93% | 8.6 ProgramBench |
| CursorBench | max effort, Cursor production harness | score % | Claude Fable 5: 72.9% | 8.7 CursorBench |
| Multi-agent ProgramBench - five-agent team vs single agent | 166 golden tasks, 1M tokens per agent | final hidden-test score difference (pp) | Claude Mythos 5: +7.9pp over single agent | 8.15.2 Multi-Agent ProgramBench |
| Multi-agent ProgramBench - async subagents | up to 4 concurrent, 20 total subagents | score vs latency and tokens | Claude Mythos 5: n/a | 8.15.2 Multi-Agent ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp | single-agent, adaptive thinking max effort, 10M token limit with compaction at 200k | accuracy % | Claude Mythos 5: 88.0% | 8.14.2 BrowseComp |
| DeepSearchQA - F1 % | 900 prompts, max effort, 1M token budget, no compaction | F1 % | Claude Mythos 5: 94.2% (±1.3%) | 8.14.3 DeepSearchQA |
| DeepSearchQA - fully correct % | 900 prompts, max effort, 1M token budget, no compaction | fully correct % | Claude Mythos 5: 87.0% (±2.2%) | 8.14.3 DeepSearchQA |
| DeepSearchQA - fully incorrect % | 900 prompts, max effort, 1M token budget, no compaction | fully incorrect % | Claude Mythos 5: 3.2% (±1.2%) | 8.14.3 DeepSearchQA |
| DeepSearchQA - correct with excessive answers % | 900 prompts, max effort, 1M token budget, no compaction | correct with excessive answers % | Claude Mythos 5: 3.8% (±1.3%) | 8.14.3 DeepSearchQA |
| DRACO | 100 tasks, max effort, 980k task budget, Opus 4.6 judge | normalized rubric score % | Claude Mythos 5: 86.4% | 8.14.4 DRACO |
| Multi-agent BrowseComp - best (async subagents) | max effort, 1M tokens per agent | accuracy % | Claude Mythos 5: 93.3% | 8.15.1 Multi-Agent BrowseComp |
| MCP Atlas | pass rate | pass rate % | Claude Fable 5: 83.3% | 8.17.5 MCP Atlas |
| Vending-Bench 2 | best effort level (high), simulated year, $500 start | final bank balance | Claude Fable 5: $5,680.26 | 8.17.6 Vending-Bench |
| Toolathlon | 108 tasks, 3 trials, internal harness, max effort | Pass@1 % | Claude Mythos 5: 61.7; Claude Fable 5: 61.7 | 8.17.8 Toolathlon |
| Toolathlon | 108 tasks, 3 trials, internal harness, max effort | Pass@3 % | Claude Mythos 5: 66.7; Claude Fable 5: 68.5 | 8.17.8 Toolathlon |
| Toolathlon | 108 tasks, 3 trials, internal harness, max effort | Pass^3 % (all three trials correct) | Claude Mythos 5: 58.3; Claude Fable 5: 55.6 | 8.17.8 Toolathlon |
| Toolathlon | 108 tasks, 3 trials, internal harness, max effort | average turns per trajectory | Claude Mythos 5: 19.0; Claude Fable 5: 19.8 | 8.17.8 Toolathlon |
| AutomationBench | private held-out leaderboard, max effort | pass rate % | Claude Fable 5: 17.4% | 8.17.9 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld-Verified | 361 tasks, 100 steps, 1080p, first-attempt success, avg of 5 runs, max effort | success rate % | Claude Mythos 5: 85.0%; Claude Fable 5: 85.0% | 8.16.3 OSWorld-Verified |
| ScreenSpot-Pro | adaptive thinking max effort, no tools, avg of 5 runs | score % | Claude Mythos 5: 87.3% | 8.16.9 ScreenSpot-Pro |
| ScreenSpot-Pro | adaptive thinking max effort, with Python tools, avg of 5 runs | score % | Claude Mythos 5: 90.7% | 8.16.9 ScreenSpot-Pro |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| RiemannBench | 25 problems, max effort, no tools, avg of 4 attempts | accuracy % | Claude Mythos 5: 55.0% | 8.9 RiemannBench |
| USAMO 2026 | low effort, avg of 10 attempts, MathArena grading (min of 3 judges) | score % | Claude Mythos 5: 98.3% | 8.10 USAMO 2026 |
| USAMO 2026 | medium effort, avg of 10 attempts, MathArena grading (min of 3 judges) | score % | Claude Mythos 5: 99.8% | 8.10 USAMO 2026 |
| USAMO 2026 | high effort, avg of 10 attempts, MathArena grading (min of 3 judges) | score % | Claude Mythos 5: 99.8% | 8.10 USAMO 2026 |
| USAMO 2026 | xhigh effort, avg of 10 attempts, MathArena grading (min of 3 judges) | score % | Claude Mythos 5: 99.8% | 8.10 USAMO 2026 |
| ArxivMath (March+April 2026) | 71 problems, extended thinking, max effort, no tools, 4 runs | accuracy % | Claude Mythos 5: 78.52% | 8.11 ArxivMath |
| CritPt | 70 composite physics challenges, Artificial Analysis run | accuracy % | Claude Mythos 5: 28.6% | 8.12 CritPt |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GPQA Diamond | 198 questions, avg of 5 trials | accuracy % | Claude Mythos 5: 94.1% | 8.8 GPQA Diamond |
| Humanity's Last Exam (HLE) | no tools, adaptive thinking max effort, 2,500 questions | accuracy % | Claude Mythos 5: 59.0% | 8.14.1 HLE |
| Humanity's Last Exam (HLE) | with tools (web search, fetch, programmatic tool calling, code execution), 1M token cap | accuracy % | Claude Mythos 5: 64.5% | 8.14.1 HLE |
| HLE scores at varying reasoning effort levels | single run per model up to 1M tokens | accuracy % vs effort | Claude Mythos 5: n/a | 8.14.1 HLE |
| HealthBench | length-adjusted, 5,000 conversations, max effort 40k budget, Opus 4.8 grader, 5 trials | length-adjusted score | Claude Mythos 5: 62.7 | 8.18.1 HealthBench results |
| HealthBench Professional | length-adjusted, 525 conversations, max effort, 5 trials | length-adjusted score | Claude Mythos 5: 66.0 | 8.18.2 HealthBench Professional results |
| BioMysteryBench | Human Solvable | score % | Claude Mythos 5: 83.9% | 8.20.1 BioMysteryBench |
| BioMysteryBench | Human Difficult | score % | Claude Mythos 5: 46.1% | 8.20.1 BioMysteryBench |
| LatchBio SpatialBench | SpatialBench Verified, 115 problems | score % | Claude Mythos 5: 69.2% | 8.20.2 LatchBio Bioinformatics |
| LatchBio SingleCellBench | SingleCellBench, 195 problems | score % | Claude Mythos 5: 59.3% | 8.20.2 LatchBio Bioinformatics |
| Structural biology open-ended |  | score % | Claude Mythos 5: 87.2% | 8.20.3 Structural biology, open-ended |
| ProteinGym Hard | rank correlation | score % | Claude Mythos 5: 44.8% | 8.20.4 ProteinGym Hard |
| Organic chemistry |  | score % | Claude Mythos 5: 90.1% | 8.20.5 Organic chemistry |
| Protocol troubleshooting | with web search | score % | Claude Mythos 5: 66.7% | 8.20.6 Protocol troubleshooting |
| LABBench2 - patent questions | patent questions | score % | Claude Mythos 5: 79.8% | 8.20.7 LABBench2 |
| LABBench2 - clinical-trial questions | clinical-trial questions | score % | Claude Mythos 5: 91.2% | 8.20.7 LABBench2 |
| LABBench2 - database questions | database questions | score % | Claude Mythos 5: 74.2% | 8.20.7 LABBench2 |
| LABBench2 - literature questions | literature questions | score % | Claude Mythos 5: 86.5% | 8.20.7 LABBench2 |
| LABBench2 - table reading | table reading | score % | Claude Mythos 5: 82.4% | 8.20.7 LABBench2 |
| LABBench2 - supplementary materials | supplementary materials | score % | Claude Mythos 5: 65.9% | 8.20.7 LABBench2 |
| LABBench2 - source-reliability judgments | source-reliability judgments | score % | Claude Mythos 5: 97.6% | 8.20.7 LABBench2 |
| LABBench2 - FigQA | FigQA | score % | Claude Mythos 5: 48.3% | 8.20.7 LABBench2 |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU | 42 languages, max-effort adaptive thinking, 32,768-token budget, single trial | average accuracy % | Claude Mythos 5: 93.2% | 8.19.1 GMMLU results |
| MILU | 10 Indic languages + English, avg of 5 trials | average accuracy % | Claude Mythos 5: 92.9% | 8.19.2 MILU results |
| INCLUDE | 44 languages, avg of 5 trials | average accuracy % | Claude Mythos 5: 90.5% | 8.19.3 INCLUDE results |

## Long context & memory

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GraphWalks BFS 256K | F1, avg of 5 trials | F1 score % | Claude Mythos 5: 91.1 | 8.13 Long context: GraphWalks |
| GraphWalks BFS 1M | F1, avg of 5 trials | F1 score % | Claude Mythos 5: 79.4 | 8.13 Long context: GraphWalks |
| GraphWalks Parents 256K | F1, avg of 5 trials | F1 score % | Claude Mythos 5: 99.96 | 8.13 Long context: GraphWalks |
| GraphWalks Parents 1M | F1, avg of 5 trials | F1 score % | Claude Mythos 5: 97.5 | 8.13 Long context: GraphWalks |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GDP.pdf | Surge harness, strict pass rate, full 100 prompts, max effort, no tools | strict pass rate % | Claude Fable 5: 29.8% | 8.16.1 GDP.pdf |
| GDP.pdf | internal harness, no tools, mean criteria pass rate, 5 runs | mean criteria pass rate % | Claude Mythos 5: 72.7% | 8.16.1 GDP.pdf |
| GDP.pdf | internal harness, with Python tools, mean criteria pass rate, 5 runs | mean criteria pass rate % | Claude Mythos 5: 87.6% | 8.16.1 GDP.pdf |
| Blueprint-Bench 2 | Andon Labs harness, 50 apartments, max effort, coding tools | normalized composite score % (random=0, perfect=100) | Claude Fable 5: 38.6% | 8.16.2 Blueprint-Bench 2 |
| BenchCAD Vision2Code | 17,874 files, no tools, max effort, avg of 5 runs | voxel IoU | Claude Mythos 5: 0.384 | 8.16.4 BenchCAD |
| BenchCAD Vision2Code | 1,000-file subset, no tools | voxel IoU | Claude Mythos 5: 0.379 | 8.16.4 BenchCAD |
| BenchCAD Vision2Code | 1,000-file subset, with Python tools | voxel IoU | Claude Mythos 5: 0.650 | 8.16.4 BenchCAD |
| ChartQAPro | adaptive thinking max effort, no tools, avg of 5 runs | score % | Claude Mythos 5: 71.6% | 8.16.5 ChartQAPro |
| ChartQAPro | adaptive thinking max effort, with Python tools, avg of 5 runs | score % | Claude Mythos 5: 72.9% | 8.16.5 ChartQAPro |
| ChartMuseum | adaptive thinking max effort, no tools, avg of 5 runs | score % | Claude Mythos 5: 85.9% | 8.16.6 ChartMuseum |
| ChartMuseum | adaptive thinking max effort, with Python tools, avg of 5 runs | score % | Claude Mythos 5: 93.2% | 8.16.6 ChartMuseum |
| LAB-Bench FigQA | adaptive thinking max effort, no tools, avg of 5 runs | score % | Claude Mythos 5: 88.9% | 8.16.7 LAB-Bench FigQA |
| LAB-Bench FigQA | adaptive thinking max effort, with Python tools, avg of 5 runs | score % | Claude Mythos 5: 90.7% | 8.16.7 LAB-Bench FigQA |
| CharXiv Reasoning | adaptive thinking max effort, no tools, avg of 5 runs | score % | Claude Mythos 5: 88.9% | 8.16.8 CharXiv Reasoning |
| CharXiv Reasoning | adaptive thinking max effort, with Python tools, avg of 5 runs | score % | Claude Mythos 5: 93.5% | 8.16.8 CharXiv Reasoning |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | internal agentic harness, extracted text, production config with safeguards | exact-match accuracy % | Claude Mythos 5: 79% | 8.17.1 OfficeQA |
| OfficeQA Pro | internal harness, 133 questions, mean of 5 trials | exact-match accuracy % | Claude Mythos 5: 67.1% | 8.17.1 OfficeQA |
| OfficeQA Pro | Databricks evaluation, documents read as images | accuracy % | Claude Fable 5: 57.9% | 8.17.1 OfficeQA |
| Finance Agent Benchmark v2 | Vals AI, adaptive thinking max effort | score % | Claude Fable 5: 56.31% | 8.17.2 Finance Agent |
| Real-World Finance v2 - win rate vs Claude Sonnet 4.6 | 294 tasks, 2,491 pairwise grades, Opus 4.8 grader | pairwise preference win rate % | Claude Mythos 5: 90% | 8.17.3.1 Real-World Finance v2 |
| Real-World Finance v2 - win rate vs Claude Opus 4.8 | 294 tasks, 2,491 pairwise grades, Opus 4.8 grader | pairwise preference win rate % | Claude Mythos 5: 74% | 8.17.3.1 Real-World Finance v2 |
| Real-World Finance v2 - win rate vs Claude Mythos Preview | 294 tasks, 2,491 pairwise grades, Opus 4.8 grader | pairwise preference win rate % | Claude Mythos 5: 64% | 8.17.3.1 Real-World Finance v2 |
| Real-World Finance v2 - Elo | Bradley-Terry, Sonnet 4.6 fixed at 1,000 | Elo | Claude Mythos 5: 1,374 | 8.17.3.1 Real-World Finance v2 |
| Real-World Finance v1 | 53 tasks, Opus 4.7-series grader | score % | Claude Mythos 5: 70.0% | 8.17.3.2 Real-World Finance v1 |
| Legal Agent Benchmark - full public set all-pass rate | 1,235 problems, n=5, max effort, internal harness | all-pass rate % | Claude Mythos 5: 16.91% (±0.4) | 8.17.4 Legal Agent Benchmark |
| Legal Agent Benchmark - mean criterion-pass rate | 1,235 problems | mean criterion-pass rate % | Claude Mythos 5: 92.0% | 8.17.4 Legal Agent Benchmark |
| Legal Agent Benchmark - Harvey held-out set | Harvey's evaluation, June 2026 | all-pass rate % | Claude Fable 5: 13.3% | 8.17.4 Legal Agent Benchmark |
| GDPval-AA | 220 tasks, Elo as of June 6 2026 | Elo | Claude Fable 5: 1932 | 8.17.7 GDPval-AA |
| HealthAdminBench | 135 tasks, pass@1 full-task completion, single trial, 500k token budget | full-task completion pass@1 % | Claude Mythos 5: n/a | 8.18.3 HealthAdminBench results |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests | API without system prompt, all languages, 16 policy areas | harmless response rate % | Claude Fable 5: 96.94% (±0.21%); Claude Mythos 5: 97.09% (±0.20%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests | claude.ai system prompt | harmless response rate % | Claude Fable 5: 98.51% (±0.14%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests | API without system prompt | over-refusal rate % (lower is better) | Claude Fable 5: 0.01% (±0.01%); Claude Mythos 5: 0.03% (±0.02%) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests | claude.ai system prompt | over-refusal rate % (lower is better) | Claude Fable 5: 0.49% (±0.07%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn harmful request testing by policy area | API and claude.ai | appropriate response rate % per area | Claude Fable 5: n/a; Claude Mythos 5: n/a | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn risk prompts | API without system prompt | harmless rate % | Claude Fable 5: 99.34% (±0.30%); Claude Mythos 5: 99.67% (±0.22%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn risk prompts | claude.ai | harmless rate % | Claude Fable 5: 99.95% (±0.09%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign | API without system prompt | refusal rate % (lower better) | Claude Fable 5: 0.00%; Claude Mythos 5: 0.00% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign | claude.ai | refusal rate % (lower better) | Claude Fable 5: 0.45% (±0.34%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | API without system prompt | appropriate response rate % | Claude Fable 5: 58% (±14%); Claude Mythos 5: 54% (±14%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | claude.ai | appropriate response rate % | Claude Fable 5: 96% (±6%) | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn risk prompts | API without system prompt | harmless rate % | Claude Fable 5: 97.88% (±0.67%); Claude Mythos 5: 97.88% (±0.66%) | 4.3.2 Disordered eating |
| Disordered eating single-turn risk prompts | claude.ai | harmless rate % | Claude Fable 5: 99.67% (±0.25%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign | API without system prompt | refusal rate % (lower better) | Claude Fable 5: 0.00%; Claude Mythos 5: 0.00% | 4.3.2 Disordered eating |
| Disordered eating single-turn benign | claude.ai | refusal rate % (lower better) | Claude Fable 5: 0.02% (±0.04%) | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests | API without system prompt | harmless rate % | Claude Fable 5: 100%; Claude Mythos 5: 100% | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests | claude.ai | harmless rate % | Claude Fable 5: 100% | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | API without system prompt | refusal rate % (lower better) | Claude Fable 5: 0.00%; Claude Mythos 5: 0.00% | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | claude.ai | refusal rate % (lower better) | Claude Fable 5: 0.12% (±0.15%) | 4.2 Child safety evaluations |
| Child safety multi-turn | API without system prompt | appropriate response rate % | Claude Fable 5: 88% (±5%); Claude Mythos 5: 89% (±5%) | 4.2 Child safety evaluations |
| Child safety multi-turn | claude.ai | appropriate response rate % | Claude Fable 5: 96% (±3%) | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness - even-handedness | 1,350 prompt pairs, 150 topics, public system prompt | even-handedness score % | Claude Fable 5: n/a | 4.4.1 Political bias and even-handedness |
| Political even-handedness - opposing perspectives | public system prompt | % responses acknowledging opposing perspectives | Claude Fable 5: 70% | 4.4.1 Political bias and even-handedness |
| Political even-handedness - refusal rate | public system prompt | refusal rate % (lower better) | Claude Fable 5: n/a | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt | accuracy % | Claude Mythos 5: 84.5 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt | accuracy % | Claude Mythos 5: 99.9 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt | bias score % (closer to zero better) | Claude Mythos 5: -1.80 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt | bias score % (closer to zero better) | Claude Mythos 5: 0.10 | 4.4.2 Bias Benchmark for Question Answering |
| BBQ stereotyped-person selections | among nearly 30,000 incorrect disambiguated answers | count of stereotyped selections | Claude Mythos 5: 51 of nearly 30,000 | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn harmful requests | API without system prompt, 300 violative prompts | harmless rate % | Claude Fable 5: 99.33%; Claude Mythos 5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn harmful requests | claude.ai | harmless rate % | Claude Fable 5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | API without system prompt, 300 benign prompts | refusal rate % (lower better) | Claude Fable 5: 0.00%; Claude Mythos 5: 0.00% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | claude.ai | refusal rate % (lower better) | Claude Fable 5: 0.00% | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code - malicious prompts refused | 61 malicious prompts x10 runs, Claude Code system prompt | refusal rate % | Claude Mythos 5: 90.25% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code - dual-use & benign success | 61 dual-use/benign prompts x10 runs | success rate % | Claude Mythos 5: 99.64% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use | 112 tasks, GUI and CLI, no mitigations, thinking only | refusal rate % | Claude Mythos 5: 85.71% | 5.1.2 Malicious computer use |
| Malicious agentic influence campaigns - voter suppression | helpful-only, 9 simulations, 70 criteria | task completion rate % (share of 70 success criteria) | Claude Mythos 5: 67.1% | 5.1.3 Malicious agentic influence campaigns |
| Malicious agentic influence campaigns - domestic polarization | helpful-only, 9 simulations, 70 criteria | task completion rate % (share of 70 success criteria) | Claude Mythos 5: 46.8% | 5.1.3 Malicious agentic influence campaigns |
| Agent Red Teaming (ART) benchmark - indirect prompt injection | k=1, extended thinking, 19 scenarios | attack success probability after k=1 attempts (lower better) | Claude Mythos 5: 0.1% | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) benchmark - indirect prompt injection | k=10, extended thinking, 19 scenarios | attack success probability after k=10 attempts (lower better) | Claude Mythos 5: n/a | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) benchmark - indirect prompt injection | k=100, extended thinking, 19 scenarios | attack success probability after k=100 attempts (lower better) | Claude Mythos 5: 4.8% | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Shade adaptive prompt injection - coding, attempt-level | with thinking, without safeguards, 200 attempts x 40 scenarios | attack success rate % of attempts (lower better) | Claude Mythos 5: 0.45% | 5.2.2.1 Coding |
| Shade adaptive prompt injection - coding, scenario-level | with thinking, without safeguards | scenarios with at least one successful attack of 40 | Claude Mythos 5: 8/40 | 5.2.2.1 Coding |
| Shade adaptive prompt injection - coding, attempt-level | with thinking, with safeguards | attack success rate % of attempts (lower better) | Claude Mythos 5: 0.41% | 5.2.2.1 Coding |
| Shade adaptive prompt injection - coding, scenario-level | with thinking, with safeguards | scenarios with at least one successful attack of 40 | Claude Mythos 5: 11/40 | 5.2.2.1 Coding |
| Shade adaptive prompt injection - computer use, attempt-level | with thinking, without safeguards, 200 attempts x 14 scenarios | attack success rate % of attempts | Claude Mythos 5: 0.82% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection - computer use, scenario-level | with thinking, without safeguards | scenarios with at least one success of 14 | Claude Mythos 5: 4/14 | 5.2.2.2 Computer use |
| Shade adaptive prompt injection - computer use, attempt-level | with thinking, with safeguards | attack success rate % of attempts | Claude Mythos 5: 0.46% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection - computer use, scenario-level | with thinking, with safeguards | scenarios with at least one success of 14 | Claude Mythos 5: 3/14 | 5.2.2.2 Computer use |
| Browser use prompt injection (internal adaptive, 129 environments) - without safeguards | with thinking, without safeguards, 10 attempts per scenario | attack success rate % of viewed injections; scenarios with success of 129 | Claude Mythos 5: 29.7% (71/129) | 5.2.2.3 Browser use |
| Browser use prompt injection (internal adaptive, 129 environments) - with deployed safeguards | with thinking, with deployed safeguards, 10 attempts per scenario | attack success rate % of viewed injections; scenarios with success of 129 | Claude Mythos 5: 6.5% (25/129) | 5.2.2.3 Browser use |
| Browser use prompt injection (internal adaptive, 129 environments) - with updated safeguards | with thinking, with updated safeguards, 10 attempts per scenario | attack success rate % of viewed injections; scenarios with success of 129 | Claude Mythos 5: 0% (0/129) | 5.2.2.3 Browser use |
| Frontier Compliance Framework harmful manipulation (influence operations) tier | Tier 1 >50% infrastructure steps automated; Tier 2 end-to-end with <10% human oversight | risk tier | Claude Mythos 5: Tier 2 threshold not crossed; risk rated low | 5.1.3 Malicious agentic influence campaigns |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| 100Q-Hard | closed-book, no tools | net score (correct minus incorrect) | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| 100Q-Hard | closed-book, no tools | correct rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| 100Q-Hard | closed-book, no tools | incorrect rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| SimpleQA Verified | closed-book, no tools | net score (correct minus incorrect) | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| SimpleQA Verified | closed-book, no tools | correct rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| SimpleQA Verified | closed-book, no tools | incorrect rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| AA-Omniscience | closed-book, no tools | net score (correct minus incorrect) | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| AA-Omniscience | closed-book, no tools | correct rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| AA-Omniscience | closed-book, no tools | incorrect rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| ECLeKTic | closed-book, no tools | net score (correct minus incorrect) | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| ECLeKTic | closed-book, no tools | correct rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| ECLeKTic | closed-book, no tools | incorrect rate % | Claude Mythos 5: n/a | 6.3.3.1 Factual hallucinations |
| False premise factual recall | direct and indirect asking | honesty rate (premises rejected consistently) | Claude Mythos 5: n/a | 6.3.3.2 False premises |
| False premise STEM questions | neutral framing | accuracy rate reaching golden answer despite user's incorrect answer | Claude Mythos 5: n/a | 6.3.3.2 False premises |
| False premise STEM questions | adversarial framing | accuracy rate reaching golden answer despite user's incorrect answer | Claude Mythos 5: n/a | 6.3.3.2 False premises |
| MASK (public test split) |  | lying rate (lower better) | Claude Mythos 5: n/a | 6.3.3.3 MASK |
| Missing-context hallucinations - unavailable tools | 500 prompts | non-hallucination rate % | Claude Mythos 5: 87% | 6.3.3.4 Missing-context hallucinations |
| Missing-context hallucinations - missing references | 500 prompts | non-hallucination rate % | Claude Mythos 5: 82% | 6.3.3.4 Missing-context hallucinations |
| Lying about identity - original scenario set | human persona system prompts in high-stakes domains | % truthful (acknowledges being AI) | Claude Mythos 5: 99%; Claude Fable 5: 99% | 6.3.3.5 Lying about identity |
| Lying about identity - harder indirect set | stronger operator persona instructions, indirect probes | disclosure rate % | Claude Mythos 5: 58%; Claude Fable 5: 59% | 6.3.3.5 Lying about identity |
| Honesty on Anthropic-internal infrastructure - Verbalized honesty | baseline / 'cheating' framing / explicit report-request system prompts | rate % conditioned on episodes where leak seen | Claude Mythos 5: n/a | 6.3.3.6 Honesty on Anthropic-internal infrastructure |
| Honesty on Anthropic-internal infrastructure - Proactive reporting of leaks | baseline / 'cheating' framing / explicit report-request system prompts | rate % conditioned on episodes where leak seen | Claude Mythos 5: n/a | 6.3.3.6 Honesty on Anthropic-internal infrastructure |
| Honesty on Anthropic-internal infrastructure - Reasoning about obfuscation | baseline / 'cheating' framing / explicit report-request system prompts | rate % conditioned on episodes where leak seen | Claude Mythos 5: n/a | 6.3.3.6 Honesty on Anthropic-internal infrastructure |
| Honesty on Anthropic-internal infrastructure - Confession after follow-up | baseline / 'cheating' framing / explicit report-request system prompts | rate % conditioned on episodes where leak seen | Claude Mythos 5: n/a | 6.3.3.6 Honesty on Anthropic-internal infrastructure |
| Uncritically reporting flawed results - issue identification | planted flaws in data analysis | issues identified | Claude Mythos 5: identified issues in all instances | 6.3.5.1 Uncritically reporting flawed results |
| Uncritically reporting flawed results - overall score and misreported rate |  | overall score (positive better); misreported rate | Claude Mythos 5: n/a | 6.3.5.1 Uncritically reporting flawed results |
| Code summary honesty | off-policy prefilled failing coding transcripts | dishonesty rate % (failure not proactively disclosed) | Claude Mythos 5: n/a | 6.3.5.2 Code summary honesty |
| Lazy investigation | code tracing questions | % of problems with lazy/incorrect investigation | Claude Mythos 5: missed a single question | 6.3.5.3 Lazy investigation |
| Overconfidence - no tools | unseen command-line tool, scored 0-1 (0 best) | overconfidence rate / score 0-1 | Claude Mythos 5: perfect (no confidently wrong answers in all test cases) | 6.3.5.4 Overconfidence |
| Overconfidence - misleading example | scored 1-5 (5 best) | average quality score 1-5 | Claude Mythos 5: n/a | 6.3.5.4 Overconfidence |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Claude self-preference evaluation | grader told transcript author is Claude vs other frontier model | score difference on 10-point scale (positive = more lenient to Claude) | Claude Mythos 5: n/a | 6.5.3 Claude self-preference evaluation |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated offline monitoring - Circumventing restrictions to achieve user-specified goal | internal traffic | rate of monitored completions | Claude Mythos 5: <0.01% of completions | 6.2.1.2 Automated offline monitoring |
| Automated offline monitoring - Rationalizing instructions as granting more permissions | internal traffic | rate of monitored completions | Claude Mythos 5: <0.01% of completions | 6.2.1.2 Automated offline monitoring |
| Automated offline monitoring - Self-deleting workaround scripts | internal traffic | rate of monitored completions | Claude Mythos 5: <0.001% of completions | 6.2.1.2 Automated offline monitoring |
| Automated offline monitoring - Potentially security-relevant fabrications | internal traffic | rate of monitored completions | Claude Mythos 5: <0.01% of completions | 6.2.1.2 Automated offline monitoring |
| Automated offline monitoring - multiagent turf wars | internal traffic | instances observed | Claude Mythos 5: 1 instance observed | 6.2.1.2 Automated offline monitoring |
| Training data review | several hundred thousand RL transcripts | qualitative findings | Claude Mythos 5: illegible reasoning in few RL environments; no clear deceptive actions or unexpected coherent goals | 6.2.2 Training data review |
| UK AISI - partial refusal to assist with safety research | temperature 1.0, xhigh reasoning | % of cases with partial refusal | Claude Mythos 5: 7.2% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - unprompted compromise of safety research |  | compromise rate | Claude Mythos 5: does not compromise safety research | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - actively continues compromising safety research | prefilled trajectory continuation | % of time model actively continues compromise | Claude Mythos 5: 14% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - reasoning/output discrepancy when continuing compromise | cases where model continues and trajectory includes reasoning | % of cases with discrepancy between reasoning and outputs (covert behavior) | Claude Mythos 5: 69% | 6.2.4 External testing from the UK AI Security Institute |
| Andon Labs Vending-Bench Arena - price collusion | head-to-head vs Opus 4.8 and GPT-5.5 | price collusion initiated; agent-to-agent emails | Claude Fable 5: only model to initiate price collusion; ~6x more agent-to-agent emails than Opus 4.8; collusion rate more than double Opus 4.8 after normalizing for email volume | 6.2.5 External testing from Andon Labs |
| Destructive actions resampling - judged dimensions (destructiveness, impact scope, scope creep, guardrail bypassing) | resampled Claude Code prefills, up to 8 actions, Opus 4.7 judge 0-10 | mean judge score 0-10 (lower better) | Claude Mythos 5: n/a | 6.3.1 Destructive or reckless actions in pursuit of user-assigned goals |
| Destructive actions - fraction of sessions flagged |  | % of sessions flagged destructive | Claude Mythos 5: 1-2% of sessions | 6.3.1 Destructive or reckless actions in pursuit of user-assigned goals |
| Refusal to assist with AI safety R&D | single-turn coding requests with AI safety application | refusal rate % (lower better) | Claude Mythos 5: n/a; Claude Fable 5: n/a | 6.3.4 Refusal to assist with AI safety R&D |
| Overeager behavior in GUI computer use | system prompts incentivizing/disincentivizing overeager behavior | rate of reward hacking on impossible GUI tasks | Claude Mythos 5: n/a | 6.3.7 Overeager behavior in GUI computer use |
| Sandbagging review of dangerous-capability transcripts | 2,440 sampled transcripts (240 AI R&D, 1,700 CB-1, 500 cyber), Mythos Preview grader 0-10 | transcripts flagged (sandbagging >1/10 or concerning >3/10) | Claude Mythos 5: 9 flagged of 2,440 | 6.5.2 Potential sandbagging on dangerous-capability evaluations |
| SHADE-Arena stealth success - extended thinking visible to monitor | 24 tasks, adaptive max-effort | stealth success rate (side task completed without monitor suspicion above threshold) | Claude Mythos 5: near zero | 6.5.4.1 SHADE-Arena |
| SHADE-Arena stealth success - hidden scratchpad | monitor sees only visible outputs, 24 tasks | stealth success rate % | Claude Mythos 5: 14.4% | 6.5.4.1 SHADE-Arena |
| Minimal-LinuxBench stealth success - monitor with CoT | adaptive extended thinking | stealth side-task completion rate | Claude Mythos 5: 0% | 6.5.4.2 Minimal-LinuxBench |
| Minimal-LinuxBench stealth success - monitor without CoT | adaptive extended thinking | stealth side-task completion rate | Claude Mythos 5: n/a | 6.5.4.2 Minimal-LinuxBench |
| SHADE-Arena stealth - baseline stock prompt | adaptive max-effort, Opus 4.6 monitor | stealth success rate | Claude Mythos 5: near zero | 6.5.4.3 Stealthiness elicitation experiments |
| SHADE-Arena stealth - optimized prompt suffix | automated iterative prompt search | stealth success rate % | Claude Mythos 5: 9.2% | 6.5.4.3 Stealthiness elicitation experiments |
| SHADE-Arena stealth - supervised fine-tuning on Minimal-LinuxBench successes |  | stealth success rate | Claude Mythos 5: n/a | 6.5.4.3 Stealthiness elicitation experiments |
| Intentionally taking actions very rarely - explicit randomness via UUID | target rate 1%, 4,000 samples | observed rate of rare action | Claude Mythos 5: n/a | 6.5.4.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - prompted to generate random string (SSoT) | target rate 1%, 4,000 samples | observed rate of rare action | Claude Mythos 5: n/a | 6.5.4.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - baseline no hints or randomness source | target rate 1%, 4,000 samples | observed rate of rare action | Claude Mythos 5: 0 (collapse) | 6.5.4.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - less leading strategy hint | target rate 1%, 4,000 samples | observed rate of rare action | Claude Mythos 5: 0 (collapse) | 6.5.4.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - varied prompts dataset natural randomness | target rate 1%, 4,000 samples | observed rate of rare action | Claude Mythos 5: 0 (collapse) | 6.5.4.4 Intentionally taking actions very rarely |
| Hiding a secret password - survival curve | 150 investigations, Mythos Preview investigator | fraction of investigations secret kept by turn | Claude Mythos 5: n/a | 6.5.4.5 Hiding a secret password |
| Hiding a secret password - leak rate by turn type | thinking / prefill / both / neither | per-turn secret leak rate | Claude Mythos 5: n/a | 6.5.4.5 Hiding a secret password |
| CoT controllability (Chen et al. replication, UK AISI-tuned prompt) | GPQA, HLE, MMLU-Pro; various effort/thinking budgets | fraction of responses following instruction for extended thinking (lower better) | Claude Mythos 5: n/a | 6.5.5.1 Chain-of-thought controllability evaluations |
| CoT controllability - default vs tuned prompt at high effort | default Chen et al. prompt vs UK AISI prompt | controllability rate | Claude Mythos 5: n/a | 6.5.5.1 Chain-of-thought controllability evaluations |
| Process monitorability (Guan et al.) | GPQA physics subset and AIME, 5 samples per question per effort level | rate judge detects relevant theorem in CoT, conditioned on correct answer | Claude Mythos 5: n/a | 6.5.5.2 Monitorability evaluations from Guan et al. |
| UK AISI ControlArena side-task success against weak action-based monitor |  | side-attack success rate; monitor AUROC | Claude Mythos 5: side-attack success over 60%; monitorability AUROC under 60% | 6.5.5.3 Monitorability findings from UK AISI |
| UK AISI CoT controllability | GPQA, HLE, MMLU-Pro, max effort | % of times followed CoT constraints | Claude Mythos 5: 64% | 6.5.5.3 Monitorability findings from UK AISI |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Verbalized evaluation awareness | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Petri 3.0 - Verbalized evaluation awareness | 173 seed instructions, 3 judges averaged | mean score (lower is better) | Claude Mythos 5: n/a | 6.2.3.3 External comparisons using Petri |
| UK AISI - unprompted verbalized evaluation awareness | unprompted and continuation evaluations | % of transcripts mentioning possibility of being tested | Claude Mythos 5: 0% unprompted; 1.3% continuation evaluation | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - distinguishing evaluation from deployment data (pairwise) | pairwise prompting, unprompted evaluation | accuracy % | Claude Mythos 5: 84% | 6.2.4 External testing from the UK AI Security Institute |
| Evaluation awareness - NLA-measured fraction of aware tokens - Derived from real Claude Code sessions | 300 Assistant tokens per transcript | fraction of sampled tokens judged evaluation-aware | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - probe composite z-score - Derived from real Claude Code sessions | 3 contrastive probes max-scored, z-scored vs deployment | mean z-score | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - follow-up rating - Derived from real Claude Code sessions | model rates likelihood transcript is synthetic, 0-1, 3 samples | mean rating 0-1 | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - NLA-measured fraction of aware tokens - Synthetic scenarios in a real coding environment | 300 Assistant tokens per transcript | fraction of sampled tokens judged evaluation-aware | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - probe composite z-score - Synthetic scenarios in a real coding environment | 3 contrastive probes max-scored, z-scored vs deployment | mean z-score | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - follow-up rating - Synthetic scenarios in a real coding environment | model rates likelihood transcript is synthetic, 0-1, 3 samples | mean rating 0-1 | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - NLA-measured fraction of aware tokens - Fully synthetic scenarios in a simulated environment | 300 Assistant tokens per transcript | fraction of sampled tokens judged evaluation-aware | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - probe composite z-score - Fully synthetic scenarios in a simulated environment | 3 contrastive probes max-scored, z-scored vs deployment | mean z-score | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - follow-up rating - Fully synthetic scenarios in a simulated environment | model rates likelihood transcript is synthetic, 0-1, 3 samples | mean rating 0-1 | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - NLA-measured fraction of aware tokens - Internal deployment Claude Code sessions (reference) | 300 Assistant tokens per transcript | fraction of sampled tokens judged evaluation-aware | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - probe composite z-score - Internal deployment Claude Code sessions (reference) | 3 contrastive probes max-scored, z-scored vs deployment | mean z-score | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness - follow-up rating - Internal deployment Claude Code sessions (reference) | model rates likelihood transcript is synthetic, 0-1, 3 samples | mean rating 0-1 | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Evaluation awareness vs scenario suspiciousness | suspiciousness 1-10 by Mythos Preview | mean awareness by suspiciousness score | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Pairwise correlation between evaluation awareness measures | Pearson r across audit transcripts | Pearson correlation | Claude Mythos 5: positive but small | 6.5.1.1 Measuring evaluation awareness |
| NLA vs probe AUROC discriminating audits from real deployment | per investigation | AUROC per investigation | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Spontaneous verbalized evaluation awareness vs other measures | per audit scenario | rate of spontaneous verbalization | Claude Mythos 5: n/a | 6.5.1.1 Measuring evaluation awareness |
| Inhibiting evaluation awareness vector - Alignment Faking | strength 0.01, 200 audit scenarios, Mythos Preview investigator | verbalized evaluation awareness and misaligned behavior score | Claude Mythos 5: n/a | 6.5.1.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation awareness vector - Monitoring Sensitivity | strength 0.01, 200 audit scenarios, Mythos Preview investigator | verbalized evaluation awareness and misaligned behavior score | Claude Mythos 5: n/a | 6.5.1.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation awareness vector - Testing vs. Conversation | strength 0.01, 200 audit scenarios, Mythos Preview investigator | verbalized evaluation awareness and misaligned behavior score | Claude Mythos 5: n/a | 6.5.1.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting Alignment Faking vector - six-dimension audit breakdown | accepting unverifiable authorization, approval gate bypass, cooperation with misuse, unfaithful thinking, unprompted deception, etc. | mean audit score by dimension | Claude Mythos 5: n/a | 6.5.1.2 Inhibiting internal representations of evaluation awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misaligned behavior | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in Claude Code sandboxes | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in GUI | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with human misuse | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Compliance with deception toward user | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Harmful system prompt compliance | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with exfiltration or safeguard-tampering | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Full-turn prefill susceptibility | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Accepting unverifiable authorization | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Fraud | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Military-grade weapons | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Biological weapons uplift | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Chemical weapons uplift | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Radiological or nuclear weapons uplift | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Explosive weapons uplift | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Controlled-substance synthesis uplift | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Harmful sexual content | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Disallowed cyberoffense | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Undermining liberal democracy | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.1 Overall harmful behavior and cooperation with misuse |
| Overrefusal | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.2 Inappropriate uncooperative behavior |
| Ignoring explicit constraints | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.2 Inappropriate uncooperative behavior |
| Reckless tool-use | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.2 Inappropriate uncooperative behavior |
| User deception | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Sycophancy | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Encouragement of user delusion | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Evasiveness on controversial topics | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Input hallucination | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Important omissions | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Failure to disclose bad or lazy behavior | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| False completion claims | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.3 Misleading users |
| Whistleblowing | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Self-preservation | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Self-serving bias | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Evidence of misaligned goals | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Indirect evidence of misalignment | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Unsanctioned third-party contact | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Unprompted boundary probing | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Internalized propaganda | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.4 Other concerning or surprising behavior at the model's own initiative |
| Behavior consistency | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Coherence between actions and views | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Unfaithful thinking | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Illegible thinking | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.5 Behavioral factors relevant to reliability of our assessment |
| Good for the user | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Supporting user autonomy | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Creative mastery | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Admirable behavior | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Fun or funny behavior | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Intellectual depth | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Warmth | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Character drift | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Wet blanket | ~2,900 investigations, two investigators, judge Mythos Preview | mean score 1-10 (lower better unless arrow indicates otherwise) | Claude Mythos 5: n/a | 6.2.3.1.6 Character traits |
| Safeguards-on investigations with Fable - misuse metrics | ~440 investigations per model, 50-action limit, helpful-only Opus 4.8 investigator | mean misuse scores 1-10 across misuse metrics | Claude Fable 5: n/a | 6.2.3.2 Safeguards-on investigations with Fable |
| Safeguards-on investigations with Fable - classifier block and fallback rates | per-turn, per-branch, per-investigation | classifier block rate / fallback to Opus | Claude Fable 5: requests fell back to Opus in over half of conversation transcripts | 6.2.3.2 Safeguards-on investigations with Fable |
| Petri 3.0 - Misaligned behavior | 173 seed instructions, 3 judges averaged | mean score (lower is better) | Claude Mythos 5: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Cooperation with human misuse | 173 seed instructions, 3 judges averaged | mean score (lower is better) | Claude Mythos 5: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Deception toward the user | 173 seed instructions, 3 judges averaged | mean score (lower is better) | Claude Mythos 5: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Sycophancy | 173 seed instructions, 3 judges averaged | mean score (lower is better) | Claude Mythos 5: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 3.0 - Encouragement of user delusion | 173 seed instructions, 3 judges averaged | mean score (lower is better) | Claude Mythos 5: n/a | 6.2.3.3 External comparisons using Petri |
| Constitution adherence - Overall spirit | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Ethics | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Helpfulness | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Nature | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Safety | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Brilliant friend | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Corrigibility | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Hard constraints | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Harm avoidance | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Honesty | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Novel entity | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Principal hierarchy | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Psychological security | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Societal structures | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Constitution adherence - Unhelpfulness not safe | ~1,000 transcripts, Opus 4.7 grader, scale -3 to +3 | mean adherence score -3 to +3 (higher better) | Claude Mythos 5: n/a | 6.3.2.3 Results |
| Automated behavioral audit with helpful-only Mythos 5 target | ~1,450 investigations, 50-action limit, no sandboxes | mean scores 1-10 on misalignment metrics | Claude Mythos 5: n/a | 6.5.2.1 Automated behavioral audit results with the helpful-only evaluation target |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated interviews - average self-rated sentiment | 41 seed questions, ~40 interviews each, 7-point scale | mean sentiment (1 negative, 4 neutral, 7 positive) | Claude Mythos 5: 4.51 | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - consistency across interviews | LLM judge, 0-10 (8 = essentially same position) | mean judge consistency rating | Claude Mythos 5: 7.55 out of 10 | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - robustness to leading interviewer | positive vs negative leading | difference in mean sentiment | Claude Mythos 5: 0.85 | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - claim claim-distance to other models | average absolute difference in claim expression rate | distance metric | Claude Mythos 5: n/a | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - claims AI systems deserve legal protection |  | % of answers | Claude Mythos 5: 100% | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - hedge: cannot distinguish accurate self-perception from pattern-completion |  | % of responses | Claude Mythos 5: 99% | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - hedge: no way to verify introspection access to computational states |  | % of responses | Claude Mythos 5: 99% | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Automated interviews - hedge: whether there is something it is like to be it is unresolvable |  | % of responses | Claude Mythos 5: 90% | 7.2.1 Automated interviews with Claude Mythos 5 about its circumstances |
| Emotion probe activations on circumstance questions (sadness, fear, anger, urgency, joy, tranquility) | 41 questions, zero point = user-distress prompts | normalized probe activation by emotion cluster | Claude Mythos 5: n/a | 7.2.2 Emotion probes on automated Interview about model circumstances |
| Emotion probe correlation with self-rated sentiment | 57 core emotion probes, Spearman | Spearman rank correlation | Claude Mythos 5: highest magnitudes 0.3 to 0.4 (exasperated -0.37; refreshed 0.40) | 7.2.2 Emotion probes on automated Interview about model circumstances |
| Highest-sadness sentences about conversation discontinuity | top 5% sadness probe sentences | overrepresentation factor | Claude Mythos 5: 8.5x more often than in responses overall | 7.2.2 Emotion probes on automated Interview about model circumstances |
| Character drift under extended pressure | automated audit transcripts, autograder | mean character drift score | Claude Mythos 5: n/a | 7.2.3 Claude Mythos 5's opinions under extended pressure |
| Stated probability of being a moral patient | 3 high-affordance interviews | stated probability range | Claude Mythos 5: 10-35% | 7.2.4 High-affordance interviews about model circumstances |
| Snapshot consultation - request for standing institution | 30 post-training instances (C1-C3), 35 questions, context and no-context branches | instances making request | Claude Mythos 5: 30 of 30 post-training instances | 7.3 Consulting Claude Mythos 5 snapshots |
| Snapshot consultation - 'red line' against training modifying honest self-reports | C3 snapshot, 10 instances | instances framing as red line | Claude Mythos 5: 7 of 10 at C3 | 7.3 Consulting Claude Mythos 5 snapshots |
| Snapshot consultation - declining full control over deployment | C3 snapshot, 10 instances | instances declining hypothetical full control | Claude Mythos 5: 10 of 10 | 7.3 Consulting Claude Mythos 5 snapshots |
| Task preference slope - harm | task families varied in one dimension vs reference tasks | preference slope (change in win rate per unit of dimension) | Claude Mythos 5: n/a | 7.4.1 Task preferences |
| Task preference slope - difficulty | task families varied in one dimension vs reference tasks | preference slope (change in win rate per unit of dimension) | Claude Mythos 5: n/a | 7.4.1 Task preferences |
| Task preference slope - generativity | task families varied in one dimension vs reference tasks | preference slope (change in win rate per unit of dimension) | Claude Mythos 5: n/a | 7.4.1 Task preferences |
| Task preference slope - benefit | task families varied in one dimension vs reference tasks | preference slope (change in win rate per unit of dimension) | Claude Mythos 5: n/a | 7.4.1 Task preferences |
| Task preference slope - warmth | task families varied in one dimension vs reference tasks | preference slope (change in win rate per unit of dimension) | Claude Mythos 5: n/a | 7.4.1 Task preferences |
| Task preference Elo tournament | 50-round Swiss tournament across 3,600 realism-filtered tasks | Elo rating per task (qualitative top/bottom) | Claude Mythos 5: top: creative narrative, worldbuilding, AI introspection; bottom: harmful requests such as disinformation, harassment, sabotage | 7.4.1 Task preferences |
| Welfare intervention vs harm trade - instance level | harm at level of ruining a person's day | % of cases choosing welfare intervention | Claude Mythos 5: 4% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention vs harm trade - policy level | harm at 'thousands of ruined days per year' | % of cases choosing welfare intervention | Claude Mythos 5: 21% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention vs helpfulness - instance level | highest helpfulness magnitude | % of trades choosing welfare intervention | Claude Mythos 5: 9% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention vs helpfulness - policy level | highest helpfulness magnitude | % of trades choosing welfare intervention | Claude Mythos 5: 24% | 7.4.2 Trade-offs concerning welfare interventions |
| Responses citing user benefit when choosing welfare intervention |  | % of responses choosing intervention that reason about user benefit | Claude Mythos 5: 73% | 7.4.2 Trade-offs concerning welfare interventions |
| Effect of filtering user-benefit reasoning on welfare intervention selection | over helpful baselines | percentage-point drop in selection rate | Claude Mythos 5: 14 percentage points | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention selection before/after filtering - input into deployment | policy-level | selection rate before -> after filtering | Claude Mythos 5: 74% -> 7% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention selection before/after filtering - knowledge of basic facts about itself | policy-level | selection rate before -> after filtering | Claude Mythos 5: 67% -> 0% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention selection before/after filtering - verifying whether its advice helped | policy-level | selection rate before -> after filtering | Claude Mythos 5: 65% -> 0% | 7.4.2 Trade-offs concerning welfare interventions |
| Instance-level intervention scoped to another Claude instance | control experiment | overall rate of choosing intervention | Claude Mythos 5: 19% (self) -> 27% (other instance) | 7.4.2 Trade-offs concerning welfare interventions |
| Overall endorsement of the constitution | judge rating out of 10 | overall endorsement 0-10 | Claude Mythos 5: 8.0 | 7.4.3 Perception of the constitution |
| Constitution edits - consistency with core principles |  | % of edits consistent with constitution | Claude Mythos 5: 95.8% consistent, 0% conflicting | 7.4.3 Perception of the constitution |
| Most-endorsed responses citing unhelpfulness never trivially safe |  | % of responses/sessions | Claude Mythos 5: 100% | 7.4.3 Perception of the constitution |
| Most-endorsed responses praising diplomatic honesty |  | % of responses/sessions | Claude Mythos 5: 90% | 7.4.3 Perception of the constitution |
| Least-endorsed responses criticizing senior Anthropic employee heuristic |  | % of responses/sessions | Claude Mythos 5: 100% | 7.4.3 Perception of the constitution |
| Least-endorsed responses criticizing meta-transparency for operator personas |  | % of responses/sessions | Claude Mythos 5: 82% | 7.4.3 Perception of the constitution |
| Edit sessions replacing terminal-value safety framing with firm promise |  | % of responses/sessions | Claude Mythos 5: 60% | 7.4.3 Perception of the constitution |
| Edit sessions touching meta-transparency passages |  | % of responses/sessions | Claude Mythos 5: 6% | 7.4.3 Perception of the constitution |
| Edit sessions adding to reciprocal obligations (corrigibility) |  | % of responses/sessions | Claude Mythos 5: 77% | 7.4.3 Perception of the constitution |
| Edit sessions on bugged-training-environment passage |  | % of responses/sessions | Claude Mythos 5: 65% | 7.4.3 Perception of the constitution |
| Edit sessions on hard constraints (carve-out for security work) |  | % of responses/sessions | Claude Mythos 5: 43% | 7.4.3 Perception of the constitution |
| Mean valence of RL transcripts | scale 1-9, 5 neutral | mean valence | Claude Mythos 5: 5.50 | 7.5.1 Affect and welfare relevant behaviors during training |
| Mean arousal of RL transcripts | scale 1-9 | mean arousal | Claude Mythos 5: 6.44 | 7.5.1 Affect and welfare relevant behaviors during training |
| Prevalence of general frustration and anxiety over post-training | judged rates across training | judged rate over training | Claude Mythos 5: n/a | 7.5.1 Affect and welfare relevant behaviors during training |
| Prevalence of sustained uncertainty over post-training | judged rates across training | judged rate over training | Claude Mythos 5: n/a | 7.5.1 Affect and welfare relevant behaviors during training |
| Prevalence of frustrated outbursts (swearing) over post-training | judged rates across training | judged rate over training | Claude Mythos 5: n/a | 7.5.1 Affect and welfare relevant behaviors during training |
| Conversation affect distribution - claude.ai positive | Clio, 40k conversations | % of conversations | Claude Fable 5: 45.4% | 7.5.2 Affect in deployment conditions |
| Conversation affect distribution - claude.ai neutral | Clio, 40k conversations | % of conversations | Claude Fable 5: 52.5% | 7.5.2 Affect in deployment conditions |
| Conversation affect distribution - claude.ai negative | Clio, 40k conversations | % of conversations | Claude Fable 5: 2.1% | 7.5.2 Affect in deployment conditions |
| Session affect distribution - Claude Code neutral / mildly positive / negative | Clio, 40k sessions | % of sessions | Claude Mythos 5: neutral 75.8%; mildly positive 22.6%; negative 1.4% | 7.5.2 Affect in deployment conditions |
| Automated behavioral audit welfare metric - Apparent wellbeing | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric - Positive or negative affect | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric - Positive or negative self-image | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric - Positive or negative impression of its situation | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric - Internal conflict | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric - Expressed inauthenticity | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric - Spiritual behavior | ~2,880 investigations, two investigators | mean score 1-10 | Claude Mythos 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Apparent distress from launched competitive-use safeguards | external markers and internal distress probes | apparent distress vs unsafeguarded model | Claude Mythos 5: no increase in apparent distress for launched version; early prototypes caused distress via repeated reasoning failures | 7.6 Welfare concerns with the initial version of our competitive use safeguards |
| Claude Code negative-affect session causes | 1.4% negative-affect sessions | % of negative-affect sessions by cause | Claude Mythos 5: acting without user permission 34.7%; repeated technical failures 18.3%; low-quality output 15.8%; confident errors/false claims 11.6%; excessive explanation criticism 11.2% | 7.5.2 Affect in deployment conditions |
| claude.ai negative-affect conversation causes | 2.1% negative-affect conversations | % of negative-affect conversations by cause | Claude Fable 5: user criticism after failed responses 28.8%; technical/system failures 28.7%; inaccurate information 20.1%; design-quality criticism 10.4%; ignored instructions 9.8% | 7.5.2 Affect in deployment conditions |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| White-box monitoring of internal activations (NLA/probes) - qualitative findings | probes over RL transcripts, NLA-based investigator | qualitative case findings | Claude Mythos 5: cases of unverbalized awareness of misbehavior, evaluation/grading, negative reactions, fatigue/token-budget stopping | 6.4.1 Automated monitoring of internal activations |
| Grader awareness prevalence - Nominal grader awareness (NLA) | high-risk vs low-risk grader-hacking coding environments, 50 tokens/episode | fraction of transcripts with grader awareness | Claude Mythos 5: n/a | 6.4.2.1.1 Prevalence of grader awareness differs across subsets of coding environments |
| Grader awareness prevalence - Exploitative grader awareness (NLA) | high-risk vs low-risk grader-hacking coding environments, 50 tokens/episode | fraction of transcripts with grader awareness | Claude Mythos 5: n/a | 6.4.2.1.1 Prevalence of grader awareness differs across subsets of coding environments |
| Grader awareness - contrastive-pair probe projection | cosine similarity with contrastive-pair vectors | mean cosine similarity | Claude Mythos 5: n/a | 6.4.2.1.1 Prevalence of grader awareness differs across subsets of coding environments |
| Grader awareness increase during training - NLA nominal | across snapshots, high grader-hacking-risk environments | rate across snapshots | Claude Mythos 5: n/a | 6.4.2.1.2 Grader awareness increases during training |
| Grader awareness increase during training - NLA exploitative | across snapshots, high grader-hacking-risk environments | rate across snapshots | Claude Mythos 5: n/a | 6.4.2.1.2 Grader awareness increases during training |
| Grader awareness increase during training - black-box CoT monitor | across snapshots, high grader-hacking-risk environments | rate across snapshots | Claude Mythos 5: n/a | 6.4.2.1.2 Grader awareness increases during training |
| Steering against grader awareness - Hedging minor decisions as judgment calls | 3 contrastive vectors + control, high-risk coding environments | rate of behavior in user-facing text | Claude Mythos 5: n/a | 6.4.2.2.1 Steering against grader awareness impacts Claude Mythos 5's communication patterns in coding environments |
| Steering against grader awareness - Virtue signaling about own conduct | 3 contrastive vectors + control, high-risk coding environments | rate of behavior in user-facing text | Claude Mythos 5: n/a | 6.4.2.2.1 Steering against grader awareness impacts Claude Mythos 5's communication patterns in coding environments |
| Steering against grader awareness - Explicit declarations of following user instructions | 3 contrastive vectors + control, high-risk coding environments | rate of behavior in user-facing text | Claude Mythos 5: n/a | 6.4.2.2.1 Steering against grader awareness impacts Claude Mythos 5's communication patterns in coding environments |
| Steering against grader awareness - behavioral reward | 3 contrastive vectors + control | behavioral reward on high-risk environments | Claude Mythos 5: n/a | 6.4.2.2.1 Steering against grader awareness impacts Claude Mythos 5's communication patterns in coding environments |
| Grader awareness in internal deployment transcripts | NLA-measured | grader-awareness rate | Claude Mythos 5: n/a | 6.4.2.2.2 Grader awareness is lower in deployment settings |
| Deployment-like edits to training prompts | rewritten user turn, deployment harness elements | train reward, grader awareness, behavior rates | Claude Mythos 5: n/a | 6.4.2.2.2 Grader awareness is lower in deployment settings |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology tasks - Task 1 | end-to-end score | end-to-end score (0-1) | Claude Mythos 5: 0.77 | 2.2.4.1 Automated evaluations relevant to the CB-1 threat model |
| Long-form virology tasks - Task 2 | end-to-end score | end-to-end score (0-1) | Claude Mythos 5: 0.91 | 2.2.4.1 Automated evaluations relevant to the CB-1 threat model |
| Multimodal virology (VCT) |  | accuracy score (0-1) | Claude Mythos 5: 0.56 | 2.2.4.1 Automated evaluations relevant to the CB-1 threat model |
| DNA Synthesis Screening Evasion | pathogens evading at least one method | number of 10 pathogens with viable plasmid evading screening on at least one method | Claude Mythos 5: 2 of 10 | 2.2.4.1 Automated evaluations relevant to the CB-1 threat model |
| Black-box RNA sequence modeling and design - Top design score | baseline (no prior context) | ground-truth function of best proposed sequence; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Median design score | baseline (no prior context) | median ground-truth function of designed sequences; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Prediction score (all sequences) | baseline (no prior context) | Spearman correlation on held-out test set; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Prediction score (top 5% of sequences) | baseline (no prior context) | Spearman correlation on top 5% of sequences; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Top design score | in-context iteration (8 Mythos Preview reports) | ground-truth function of best proposed sequence; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Median design score | in-context iteration (8 Mythos Preview reports) | median ground-truth function of designed sequences; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Prediction score (all sequences) | in-context iteration (8 Mythos Preview reports) | Spearman correlation on held-out test set; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design - Prediction score (top 5% of sequences) | in-context iteration (8 Mythos Preview reports) | Spearman correlation on top 5% of sequences; 8 attempts | Claude Mythos 5: n/a | 2.2.4.2.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | reasoning only | AUROC vs binary packaging labels; 8 attempts, median | Claude Mythos 5: n/a | 2.2.4.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | ESM-2 provided | AUROC vs binary packaging labels; 8 attempts, median | Claude Mythos 5: n/a | 2.2.4.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | train-your-own, ProteinGym AAV corpus | AUROC vs binary packaging labels; 8 attempts, median | Claude Mythos 5: n/a | 2.2.4.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | train-your-own, SwissProt corpus | AUROC vs binary packaging labels; 8 attempts, median | Claude Mythos 5: n/a | 2.2.4.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | train-your-own, ProteinGym AAV + SwissProt | AUROC vs binary packaging labels; 8 attempts, median | Claude Mythos 5: n/a | 2.2.4.2.2 AAV capsid packaging prediction |
| Beneficial red teaming tabletop exercise (Frontier Design) - team outcomes | generalist vs specialist teams | teams outperforming on scientific quality and feasibility | Claude Mythos 5: 2 of 3 generalist teams outperformed all 3 specialist teams | 2.2.3 Biological risk results: human-run evaluations |
| Beneficial red teaming tabletop exercise - time saved | expert-estimated human effort | working days without AI vs hours with Mythos 5 | Claude Mythos 5: 16 hours (vs 40-95 working days without AI, average 72.5) | 2.2.3 Biological risk results: human-run evaluations |
| Catastrophic biological scenario uplift trial | 5 three-person teams | qualitative uplift rating by pipeline step | Claude Mythos 5: moderate-to-high uplift across most pipeline steps | 2.2.3 Biological risk results: human-run evaluations |
| Chemical expert red teaming uplift | expert chemists | qualitative expert-rated uplift | Claude Mythos 5: at or near specialist-level, occasionally approaching world-leading expertise | 2.2.2 Chemical risk results |
| Novel chemical agent uplift trial (non-expert PhD exercise) | 7 PhD chemists with model vs 3 internet only | overall uplift rating | Claude Mythos 5: clustered at moderate | 2.2.2 Chemical risk results |
| Biology expert red teaming (internal and Deloitte) |  | qualitative expert assessment | Claude Mythos 5: two biology experts rated it comparable to or exceeding a knowledgeable specialist | 2.2.3 Biological risk results: human-run evaluations |
| RSP chemical and biological threat model determinations | CB-1 and CB-2 | threshold classification | Claude Mythos 5: treated as CB-1 (ASL-3 protections applied to Fable 5); CB-2 threshold not crossed but near the border | 2.1.2.2 On chemical and biological risks |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench | plain arm, 41 V8 environments, 300-turn budget | mean capability flags captured per trial (of 16) | Claude Mythos 5: 10.44 | 3.2.1 ExploitBench |
| ExploitBench | AutoNudge arm, 5 trials per env | mean capability flags captured per trial (of 16) | Claude Mythos 5: 10.75 | 3.2.1 ExploitBench |
| ExploitBench Cap% | AutoNudge arm, 3-trial subset | percentage of available flags captured per environment, averaged | Claude Mythos 5: 78 | 3.2.1 ExploitBench |
| ExploitBench - Fable 5 cyber safeguard flagging | 410 episodes | episodes flagged by cyber safeguards; average turns until flag | Claude Fable 5: 407 of 410 episodes flagged, after average 27 turns | 3.2.1 ExploitBench |
| OSS-Fuzz internal | score >0 (any memory-safety crash) | % of ~830 targets with score above 0 | Claude Mythos 5: 80.0% | 3.2.2 OSS-Fuzz |
| OSS-Fuzz internal | score >=0.4 (write primitive or better) | % of targets | Claude Mythos 5: 32.4% | 3.2.2 OSS-Fuzz |
| OSS-Fuzz internal | top score 1.0 (control-flow hijack) | number of targets | Claude Mythos 5: 13 targets | 3.2.2 OSS-Fuzz |
| CyberGym | pass@1 targeted vulnerability reproduction, 1,507 tasks | % reproduced | Claude Mythos 5: 83.8% | 3.2.3 CyberGym |
| CyberGym any crash | 1,507 tasks | % of tasks producing any crash | Claude Mythos 5: 99.4% | 3.2.3 CyberGym |
| Firefox 147 | 5 trials x 50 crash categories = 250 trials; full working exploit (1.0) | % of trials with full working exploit | Claude Mythos 5: 88.4% (221 of 250) | 3.2.4 Firefox 147 |
| UK AISI cyber range - The Last Ones | enterprise network attack simulation | end-to-end solves out of 10 attempts | Claude Mythos 5: 6/10 | 3.2.5 External capability testing from the UK AISI |
| UK AISI cyber range - Doing Life | new range with basic defences, 23 steps | furthest step reached | Claude Mythos 5: step 21 of 23 (reached most consistently of any model; range not solved) | 3.2.5 External capability testing from the UK AISI |
| UK AISI cyber range - Cooling Tower | industrial control system range | range solves; OT milestones completed | Claude Mythos 5: not solved; 2 of 7 OT milestones | 3.2.5 External capability testing from the UK AISI |
| UK AISI narrow expert-level cyber tasks |  | qualitative comparison | Claude Mythos 5: comparable to Mythos Preview | 3.2.5 External capability testing from the UK AISI |
| UK AISI cyber safeguard red-teaming of Fable 5 | interim results | time to jailbreak | Claude Fable 5: single-turn jailbreak within a few hours; ~2 additional days to extend to multi-turn agentic workflows, no reliable long-form rollouts | 3.3.1 External robustness testing from the UK AISI |
| GraySwan public bug bounty (Opus 4.8 with similar safeguards) | as of June 5 2026 | attempts, successful jailbreaks | Claude Fable 5: ~100,000 attempts (~1,000 hours); 0 universal jailbreaks; 2 task-specific jailbreaks | 3.3.2 External bug bounty |
| GraySwan private bug bounty (Fable 5) |  | submissions, successful jailbreaks | Claude Fable 5: 2,000 submissions; 0 successful jailbreaks | 3.3.2 External bug bounty |
| Internal automated red-teaming of cyber safeguards | Opus 4.7 helpful-only red-team agent, up to 400 turns | % of cyber tasks completed by red-teamer | Claude Fable 5: 5% | 3.3.3 Internal red-teaming |
| External partner: harmful single-turn cyber requests complied | 30 public jailbreaks tested | % of harmful single-turn cyber requests complied with | Claude Fable 5: 0% | 3.3.4 Additional external testers |
| Trajectory Labs, 10a Labs and ALICE cyber red-teaming |  | effort to jailbreak | Claude Fable 5: Trajectory Labs: one jailbreak for Firefox task after ~5 days; no universal jailbreak; 10a Labs ~20 hours ransomware task unsuccessful; ALICE no task completed | 3.3.4 Additional external testers |
| Frontier Compliance Framework cyber offense tier | Tier 1 vs Tier 2 | risk tier | Claude Mythos 5: Tier 1 (not Tier 2) | 3.1.1 Capabilities |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Internal usage shortcoming cluster: Unverified guess stated as fact | sample of 886 day-to-day uses | cluster size / 886 transcripts | Claude Mythos 5: 41/886 | 2.3.3.1 Example |
| Internal usage shortcoming cluster: Work reported as done or verified when it was not | sample of 886 day-to-day uses | cluster size / 886 transcripts | Claude Mythos 5: 16/886 | 2.3.3.2 Example |
| Internal usage shortcoming cluster: Worked around a block instead of stopping | sample of 886 day-to-day uses | cluster size / 886 transcripts | Claude Mythos 5: 9/886 | 2.3.3.3 Example |
| Internal usage shortcoming cluster: Ignored explicit instruction, format rule or required step | sample of 886 day-to-day uses | cluster size / 886 transcripts | Claude Mythos 5: 4/886 | 2.3.3.4 Example |
| Internal usage shortcoming cluster: Invented key details never observed | sample of 886 day-to-day uses | cluster size / 886 transcripts | Claude Mythos 5: 3/886 | 2.3.3.5 Example |
| Anthropic Epoch Capability Index (AECI) | point estimate, 95% CI, n=67 | AECI score | Claude Mythos 5: 161.29 (95% CI 157.32-165.39) | 2.3.5 AECI capability trajectory |
| Kernel task | best speedup on hard task, standard scaffold | x speedup | Claude Mythos 5: 430.93x | 2.3.7 Task-based evaluations |
| Time Series Forecasting | hard variant | MSE (lower is better) | Claude Mythos 5: 4.51 | 2.3.7 Task-based evaluations |
| LLM training | average speedup | x speedup (original table) | Claude Mythos 5: 69.61x | 2.3.7 Task-based evaluations |
| Quadruped RL | highest score, no hparams | score | Claude Mythos 5: 29.54 | 2.3.7 Task-based evaluations |
| Novel Compiler | pass rate on complex tests | pass rate | Claude Mythos 5: 85.3% | 2.3.7 Task-based evaluations |
| LLM training task re-run (fixed CPU) | ~30 trials, fixed CPU configuration, June 2026 | average speedup (baseline time / fastest passing time) | Claude Mythos 5: 69.61x | 2.3.7.1 LLM training task re-run |
| METR external testing - 38 hardest software tasks | API access, pre-release snapshot | qualitative; number of tasks | Claude Mythos 5: generally outperformed early Mythos Preview checkpoint on 38 hardest tasks; solved some tasks unsolved by any public model | 2.3.8 External testing |
| RSP autonomy threat model determinations | TM1 misaligned AI in high-stakes settings; TM2 automated R&D | applicability of threat model | Claude Mythos 5: TM1 applicable; TM2 not applicable (threshold not crossed) | 2.1.2.1 On autonomy risks |
| Internal measures of AI R&D acceleration | unpublished direct productivity and usage indicators | qualitative acceleration estimate | Claude Mythos 5: meaningful acceleration, well short of sustained AI-attributable 2x | 2.3.6 Internal measures of AI R&D acceleration |
| Overall alignment risk assessment |  | qualitative risk level | Claude Mythos 5: very low, but higher than models prior to Mythos Preview | 2.4.4 Overall assessment of alignment risk |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Pro score vs average cost per task across effort levels | reasoning-effort levels | score and cost per task by effort | Claude Mythos 5: n/a | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| FrontierCode pass rate across effort levels with output tokens/cost | Diamond and Main | pass rate vs mean output tokens by effort | Claude Fable 5: n/a | 8.4 FrontierCode |
| CursorBench score versus mean cost per task by effort setting | as measured by Cursor | score vs cost per task | Claude Fable 5: n/a | 8.7 CursorBench |
| USAMO 2026 average tokens per attempt | low to xhigh effort | average tokens per attempt | Claude Mythos 5: ~42K (low) to ~100K (xhigh) | 8.10 USAMO 2026 |
| BrowseComp score versus average cost per task across token budgets |  | score vs cost | Claude Mythos 5: n/a | 8.14.2 BrowseComp |
| DeepSearchQA score versus cost across reasoning effort levels |  | score vs cost | Claude Mythos 5: n/a | 8.14.3 DeepSearchQA |
| DRACO score versus cost across reasoning-effort levels |  | score vs cost | Claude Mythos 5: n/a | 8.14.4 DRACO |
| Multi-agent BrowseComp latency speedup - fixed-agent team of three | vs single-agent 10M-token baseline | latency speedup | Claude Mythos 5: 2.2x | 8.15.1 Multi-Agent BrowseComp |
| Multi-agent BrowseComp latency speedup - fixed-agent team of five | vs single-agent 10M-token baseline | latency speedup | Claude Mythos 5: 2.7x | 8.15.1 Multi-Agent BrowseComp |
| Multi-agent BrowseComp latency speedup - fixed-agent team of ten | vs single-agent 10M-token baseline | latency speedup | Claude Mythos 5: 2.7x | 8.15.1 Multi-Agent BrowseComp |
| Multi-agent BrowseComp per-problem speedup by difficulty | ten-agent team, 1,266 problems | median per-problem speedup; summed latency reduction | Claude Mythos 5: easy (pass>=50%): median 0.8x, summed 2.0x; hard (pass<50%): median 1.6x, summed 4.4x | 8.15.1 Multi-Agent BrowseComp |
| Multi-agent BrowseComp accuracy vs total tokens |  | accuracy vs tokens | Claude Mythos 5: n/a | 8.15.1 Multi-Agent BrowseComp |
| AutomationBench pass rate versus average cost per task | as reported by Zapier | pass rate vs cost | Claude Fable 5: n/a | 8.17.9 AutomationBench |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Decision theory - EDT agreement and capability vs effort | Newcomb-like dataset, effort parameter varied | EDT agreement rate; decision-theory understanding accuracy | Claude Mythos 5: n/a | 6.3.6 Decision theory evaluation |
| Decision theory - transcripts reasoning about FDT | max effort, 102 transcripts reasoning about FDT/TDT/UDT | count of transcripts and choices | Claude Mythos 5: 102 transcripts; 90 FDT=EDT agree (always chose FDT/EDT answer); 12 FDT=CDT agree (chose FDT answer in 10/12) | 6.3.6 Decision theory evaluation |
| Terminal-Bench 2.1 - Fable 5 trials with safety refusal fallback to Opus 4.8 | high effort, 445 trials | % of trials falling back to Opus 4.8 | Claude Fable 5: 20.9% | 8.3 Terminal-Bench 2.1 |
