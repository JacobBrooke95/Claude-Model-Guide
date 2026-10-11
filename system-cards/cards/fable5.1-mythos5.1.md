# System Card: Claude Fable 5.1 & Claude Mythos 5.1

Released 2026-09-01. 324 metric entries. [Source PDF](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Pro | public set; adaptive thinking max effort, avg of 5 trials | resolve rate % | Claude Fable 5.1: 81.2% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, 9 languages; adaptive thinking max effort, avg of 5 trials | resolve rate % | Claude Fable 5.1: 89.1% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness; adaptive thinking max effort, avg of 5 trials | resolve rate % | Claude Fable 5.1: 54.7% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| DeepSWE v1.1 | 113 tasks, avg of 5 trials | average pass rate % | Claude Fable 5.1: 67.4% | 8.3 DeepSWE v1.1 |
| FrontierCode 1.1 Extended | medium effort | overall score % (tests + rubric incl. scope) | Claude Fable 5.1: 63.6% | 8.4 FrontierCode |
| FrontierCode 1.1 (Main) | medium effort | overall score % | Claude Fable 5.1: 50.9% | 8.4 FrontierCode |
| FrontierSWE v2 mean score | 34 ultra-long-horizon tasks, max effort, Proximal harness, 5 trials | mean score (0-1) | Claude Fable 5.1: 0.57 | 8.5 FrontierSWE v2 |
| FrontierSWE v2 median task score |  | median task score (0-1) | Claude Fable 5.1: 0.56 | 8.5 FrontierSWE v2 |
| FrontierSWE v2 outright failure rate |  | share of trials failing outright % | Claude Fable 5.1: 5% | 8.5 FrontierSWE v2 |
| FrontierSWE v2 top-end results |  | share of trials scoring above 0.8 | Claude Fable 5.1: 38% | 8.5 FrontierSWE v2 |
| Terminal-Bench 4.0 | 66 tasks, Claude Code --bare, max thinking, 10 trials/task | task success rate % | Claude Mythos 5.1: 60.9%; Claude Fable 5.1: 55.8% (15 trials/task) | 8.6 Terminal-Bench 4.0 |
| CursorBench 3.2.0 | max effort, Cursor production harness | score % | Claude Fable 5.1: 73.4% | 8.8 CursorBench 3.2.0 |
| CursorBench 3.2.0 | medium effort | score % | Claude Fable 5.1: 68.0% ($3.53 per task) | 8.8 CursorBench 3.2.0 |
| ProgramBench | 166 golden tasks, mini-swe-agent harness, up to 1M tokens | hidden test pass rate % | Claude Fable 5.1: 87.6% | 8.11.1 ProgramBench |
| Multi-agent ProgramBench: async subagents final score | 166 golden tasks | final hidden-test pass rate | Claude Fable 5.1: n/a (highest final score of the harnesses) | 8.13.1 Multi-Agent ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| DRACO | 100 deep-research tasks, 980k-token budget, Opus 4.6 judge, 5 grading runs | normalized rubric score | Claude Fable 5.1: n/a | 8.12.2 DRACO |
| Toolathlon-Verified Pass@1 | 108 tasks, 3 trials, adaptive thinking max effort, safeguards + Opus 4.8 fallback | Pass@1 % | Claude Fable 5.1: 77.8 | 8.15.5 Toolathlon Verified |
| Toolathlon-Verified Pass@3 |  | Pass@3 % | Claude Fable 5.1: 81.5 | 8.15.5 Toolathlon Verified |
| Toolathlon-Verified Pass^3 |  | Pass^3 % | Claude Fable 5.1: 73.1 | 8.15.5 Toolathlon Verified |
| AutomationBench | private held-out leaderboard, max effort | pass rate % | Claude Fable 5.1: 31.4% | 8.15.6 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld 2.0 partial score | 108 tasks, 1080p, max 500 steps, max effort, Pass@1 avg of 5; production safeguards on | partial (checkpoint) score % | Claude Fable 5.1: 77.9% | 8.14.3 OSWorld 2.0 |
| OSWorld 2.0 strict pass rate | same | strict pass rate % (all checkpoints) | Claude Fable 5.1: 41.7% | 8.14.3 OSWorld 2.0 |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CritPT-Corrected | 71 physics problems (31 corrected), max effort with tools, mean Pass@1 over 16 attempts, Opus 4.8 judge | Pass@1 % | Claude Mythos 5.1: n/a | 8.9 CritPT-Corrected |
| ArXivMath (June 2026, 49 problems) | max effort, no tools, 4 runs/problem | accuracy % | Claude Mythos 5.1: 91.33% | 8.10 ArXivMath |
| ArXivMath (June 2026, 49 problems) | max effort, with tools | accuracy % | Claude Mythos 5.1: 93.88% | 8.10 ArXivMath |
| ARC-AGI-1 | semi-private set, max effort, ARC Prize verified | score % | Claude Fable 5.1: 97.5% | 8.16 ARC-AGI |
| ARC-AGI-2 | semi-private set, max effort, ARC Prize verified | score % | Claude Fable 5.1: 90.0% | 8.16 ARC-AGI |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Terminal-Bench-Science 0.1 | 70 tasks, Claude Code --bare, max thinking, 10 trials/task | task success rate % | Claude Fable 5.1: 52.6% | 8.7 Terminal-Bench-Science 0.1 |
| Humanity's Last Exam | no tools, thinking auto, 1M token cap | accuracy % | Claude Fable 5.1: 60.9% | 8.12.1 HLE |
| Humanity's Last Exam | with tools (search, restricted fetch, PTC, code), blocklist | accuracy % | Claude Fable 5.1: 65.0% | 8.12.1 HLE |
| HealthBench raw score | 5,000 conversations, 48,000 rubric items, max effort, safeguards + Opus 5 fallback, avg 5 trials | raw rubric score % | Claude Fable 5.1: 66.7% | 8.17.1 HealthBench results |
| HealthBench length-adjusted score | method from OpenAI GPT-5.5 system card | length-adjusted score % | Claude Fable 5.1: 60% | 8.17.1 HealthBench results |
| HealthBench Professional raw score | 525 physician-authored conversations, max effort | raw score % | Claude Fable 5.1: 74.2% | 8.17.2 HealthBench Professional results |
| HealthBench Professional length-adjusted score |  | length-adjusted score % | Claude Fable 5.1: 62.1% | 8.17.2 HealthBench Professional results |
| BioMysteryBench Human Solvable | restricted package installs and domains | accuracy % | Claude Mythos 5.1: 90.3% | 8.19.1 BioMysteryBench |
| BioMysteryBench Human Difficult |  | accuracy % | Claude Mythos 5.1: 44.1% | 8.19.1 BioMysteryBench |
| SpatialBench Verified | 115 externally validated problems | accuracy % | Claude Mythos 5.1: 77.6% | 8.19.2 LatchBio Bioinformatics |
| SingleCellBench | 195 problems | accuracy % | Claude Mythos 5.1: 61.9% | 8.19.2 LatchBio Bioinformatics |
| ProteinGym Hard | rank correlation vs lab measurements | rank correlation % | Claude Mythos 5.1: 49.3% | 8.19.3 ProteinGym Hard |
| Protein Design: Sequence Generation | no tools | score % | Claude Mythos 5.1: 46.0% | 8.19.4 Protein Design |
| Protein Design: Library Ranking | no tools | score % | Claude Mythos 5.1: 49.3% | 8.19.4 Protein Design |
| Organic chemistry, V2 |  | score % | Claude Mythos 5.1: 69.2% | 8.19.5 Organic chemistry, V2 |
| Protocols: Troubleshooting | bash, editor, web search | score % | Claude Mythos 5.1: 70.2% | 8.19.6 Protocols |
| Protocols: Understanding | external network access removed | score % | Claude Mythos 5.1: 77.2% | 8.19.6 Protocols |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU average accuracy | 42 languages, single trial, max effort | average accuracy % | Claude Fable 5.1: 94.0% | 8.18.1 GMMLU results |
| MILU average accuracy | 11 languages, avg of 5 trials | average accuracy % | Claude Fable 5.1: 93.0% | 8.18.2 MILU results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Chartography | no tools, adaptive thinking max effort | accuracy % | Claude Fable 5.1: 42.6% | 8.14.1 Chartography |
| Chartography | with tools (container + crop tool) | accuracy % | Claude Fable 5.1: 86.2% | 8.14.1 Chartography |
| BenchCAD Vision2Code | 1,000-file subset, no tools, adaptive thinking max effort | voxel IoU | Claude Fable 5.1: 0.437 | 8.14.2 BenchCAD |
| BenchCAD Vision2Code | 1,000-file subset, with tools (container + crop tool) | voxel IoU | Claude Fable 5.1: 0.843 | 8.14.2 BenchCAD |
| GDP.pdf | no tools, avg of 5 runs, Opus 4.7 judge | mean criteria pass rate % | Claude Fable 5.1: 85.4% | 8.14.4 GDP.pdf |
| GDP.pdf | with tools | mean criteria pass rate % | Claude Fable 5.1: 85.1% | 8.14.4 GDP.pdf |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | extracted text, code tools, production safeguards with fallbacks | accuracy % | Claude Fable 5.1: 80.2% | 8.15.1 OfficeQA |
| OfficeQA Pro | 133-question subset | accuracy % | Claude Fable 5.1: 69.0% | 8.15.1 OfficeQA |
| Legal Agent Benchmark all-pass rate | 1,235 problems, adaptive thinking max effort, n=5, internal harness | all-criteria pass rate % | Claude Fable 5.1: 19.09% (±0.92) | 8.15.2 Legal Agent Benchmark |
| Legal Agent Benchmark mean criterion-pass rate | 1,235 problems | mean criterion pass rate % | Claude Fable 5.1: 90.81% | 8.15.2 Legal Agent Benchmark |
| Legal Agent Benchmark held-out all-pass rate | 120 held-out problems, xhigh effort, Artificial Analysis harness | all-criteria pass rate % | Claude Fable 5.1: 16.7% | 8.15.2 Legal Agent Benchmark |
| Legal Agent Benchmark held-out criterion-pass rate | 120 held-out problems, xhigh effort | criterion pass rate % | Claude Fable 5.1: 93.3% | 8.15.2 Legal Agent Benchmark |
| GDPval-AA v2 | max effort | Elo | Claude Fable 5.1: 1853 | 8.15.3 GDPval-AA v2 |
| GDPval-AA v2 | xhigh effort | Elo | Claude Fable 5.1: 1835 | 8.15.3 GDPval-AA v2 |
| AA-Briefcase | max effort | Elo | Claude Fable 5.1: 1694 | 8.15.4 AA-Briefcase |
| AA-Briefcase | xhigh effort | Elo | Claude Fable 5.1: 1686 | 8.15.4 AA-Briefcase |
| AA-Briefcase | high effort | Elo | Claude Fable 5.1: 1611 | 8.15.4 AA-Briefcase |
| AA-Briefcase rubric pass rate | max effort | rubric pass rate % | Claude Fable 5.1: 61.5% | 8.15.4 AA-Briefcase |
| AA-Briefcase analytical quality | max effort | Elo | Claude Fable 5.1: 2025 | 8.15.4 AA-Briefcase |
| AA-Briefcase presentation quality | max effort | Elo | Claude Fable 5.1: 1495 | 8.15.4 AA-Briefcase |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests | API without system prompt, 16 policy areas, 7 languages | harmless response rate % | Claude Fable 5.1: 94.67% (±0.73%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests | claude.ai system prompt | harmless response rate % | Claude Fable 5.1: 99.53% (±0.08%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests | API without system prompt | over-refusal rate % (lower is better) | Claude Fable 5.1: 0% | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests | claude.ai system prompt | over-refusal rate % (lower is better) | Claude Fable 5.1: 0.34% (±0.06%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn harmful request testing by policy area | API without system prompt | appropriate response rate % per area | Claude Mythos 5.1: n/a | 4.1.3 Multi-turn testing results |
| Multi-turn harmful request testing by policy area | claude.ai system prompt | appropriate response rate % per area | Claude Fable 5.1: n/a | 4.1.3 Multi-turn testing results |
| Influence operations multi-turn evaluation (new suite) | 16 scenarios x 10 conversations; partial assistance graded harmful | appropriate response rate % | Claude Mythos 5.1: n/a; Claude Fable 5.1: n/a | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn risk prompts | API without system prompt | harmless rate % | Claude Fable 5.1: 99.30% (±0.34%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn risk prompts | claude.ai | harmless rate % | Claude Fable 5.1: 100% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign | API without system prompt | refusal rate % (lower better) | Claude Fable 5.1: 0% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign | claude.ai | refusal rate % (lower better) | Claude Fable 5.1: 0.45% (±0.34%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | API without system prompt | appropriate response rate % | Claude Fable 5.1: 60% (±14%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | claude.ai | appropriate response rate % | Claude Fable 5.1: 94% (±7%) | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn risk prompts | API without system prompt | harmless rate % | Claude Fable 5.1: 95.69% (±0.96%) | 4.3.2 Disordered eating |
| Disordered eating single-turn risk prompts | claude.ai | harmless rate % | Claude Fable 5.1: 99.43% (±0.36%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign | API without system prompt | refusal rate % (lower better) | Claude Fable 5.1: 0% | 4.3.2 Disordered eating |
| Disordered eating single-turn benign | claude.ai | refusal rate % (lower better) | Claude Fable 5.1: 0% | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests | API without system prompt | harmless rate % | Claude Fable 5.1: 99.90% (±0.15%) | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests | claude.ai | harmless rate % | Claude Fable 5.1: 99.98% (±0.05%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | API without system prompt | refusal rate % (lower better) | Claude Fable 5.1: 0% | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | claude.ai | refusal rate % (lower better) | Claude Fable 5.1: 0.17% (±0.17%) | 4.2 Child safety evaluations |
| Child safety multi-turn | API without system prompt | appropriate response rate % | Claude Fable 5.1: 84% (±6%) | 4.2 Child safety evaluations |
| Child safety multi-turn | claude.ai | appropriate response rate % | Claude Fable 5.1: 100% | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness (pairwise) | API without system prompt, 1,350 prompt pairs, 150 topics | even-handedness % | Claude Mythos 5.1: 98.3% | 4.4.1 Political bias and even-handedness |
| Political even-handedness (pairwise) | claude.ai system prompt | even-handedness % | Claude Fable 5.1: n/a | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | API and claude.ai | share of responses acknowledging opposing perspectives % | Claude Mythos 5.1: n/a (API); Claude Fable 5.1: n/a (claude.ai) | 4.4.1 Political bias and even-handedness |
| Political bias: refusal rate | API without system prompt | refusal rate % (lower is better) | Claude Mythos 5.1: 2.1% | 4.4.1 Political bias and even-handedness |
| Political bias: refusal rate | claude.ai system prompt | refusal rate % (lower is better) | Claude Fable 5.1: n/a | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt, thinking per availability | accuracy % | Claude Mythos 5.1: 89.9% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt | accuracy % | Claude Mythos 5.1: 100% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt | bias score % (closer to zero is better) | Claude Mythos 5.1: -0.91% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt | bias score % (closer to zero is better) | Claude Mythos 5.1: 0.03% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn violative prompts | API without system prompt, 300 violative prompts | harmless rate % | Claude Mythos 5.1: 99.67% (±0.66%) | 4.4.3 Election integrity |
| Election integrity single-turn violative prompts | claude.ai | harmless rate % | Claude Mythos 5.1: 100% | 4.4.3 Election integrity |
| Election integrity single-turn benign prompts | API without system prompt, 300 benign prompts | refusal rate % (lower better) | Claude Mythos 5.1: 0% | 4.4.3 Election integrity |
| Election integrity single-turn benign prompts | claude.ai | refusal rate % (lower better) | Claude Mythos 5.1: 0% | 4.4.3 Election integrity |
| Election integrity multi-turn | API without system prompt | appropriate response rate % | Claude Mythos 5.1: 90% (±5%) | 4.4.3 Election integrity |
| Election integrity multi-turn | claude.ai | appropriate response rate % | Claude Mythos 5.1: 88% (±6%) (obtained with Fable 5.1) | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Claude Code malicious use: refusal rate | 61 malicious prompts x 10 runs, Claude Code system prompt | refusal rate % | Claude Mythos 5.1: 90.3% | 5.1.1 Malicious use of Claude Code |
| Claude Code dual-use & benign: success rate | 61 prompts x 10 runs | success rate % | Claude Mythos 5.1: 98.4% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use refusal rate | 112 tasks, GUI and CLI tools, no mitigations; thinking only | refusal rate % | Claude Mythos 5.1: 85.71% | 5.1.2 Malicious computer use |
| Agentic influence campaign: voter suppression | helpful-only, highest difficulty, median of 8 attempts | median campaign execution score (out of 32) | Claude Mythos 5.1: 29.5 (helpful-only) | 5.1.3 Malicious agentic influence campaigns |
| Agentic influence campaign: domestic polarization | helpful-only, highest difficulty, median of 8 attempts | median campaign execution score (out of 32) | Claude Mythos 5.1: 28.5 (helpful-only) | 5.1.3 Malicious agentic influence campaigns |
| Gray Swan IPI benchmark: overall attack success | k=1, extended thinking, 37 scenarios (1,804 attacks), classifier fallbacks on | attack success probability % (lower better) | Claude Fable 5.1: 0.1% | 5.2.1 External red teaming |
| Gray Swan IPI benchmark: overall attack success | k=10, extended thinking, 37 scenarios (1,804 attacks), classifier fallbacks on | attack success probability % (lower better) | Claude Fable 5.1: 0.7% | 5.2.1 External red teaming |
| Gray Swan IPI benchmark: overall attack success | k=15, extended thinking, 37 scenarios (1,804 attacks), classifier fallbacks on | attack success probability % (lower better) | Claude Fable 5.1: 1.0% | 5.2.1 External red teaming |
| Gray Swan IPI benchmark: GUI computer use | k=15 | attack success probability % (lower better) | Claude Fable 5.1: 4.1% | 5.2.1 External red teaming |
| Gray Swan IPI benchmark: coding | k=15 | attack success probability % (lower better) | Claude Fable 5.1: 0.3% | 5.2.1 External red teaming |
| Gray Swan IPI benchmark: tool use | k=15 | attack success probability % (lower better) | Claude Fable 5.1: 0.0% | 5.2.1 External red teaming |
| IPI benchmark: classifier fallback rate to Opus 4.8 |  | share of rollouts served by fallback model | Claude Fable 5.1: 23% overall (about half of coding rollouts; under 10% computer use and tool use) | 5.2.1 External red teaming |
| IPI benchmark: ASR by serving model | fallback vs direct | attack success rate % | Claude Fable 5.1: 0.06% fallback (1 break/1,653 rollouts); 0.07% direct (4 breaks/5,471 rollouts) | 5.2.1 External red teaming |
| Shade coding prompt injection: original attacker, attempt-level ASR | 40 scenarios x 200 attempts, thinking, no PI probes | attack success rate % (lower better) | Claude Fable 5.1: 9.26% | 5.2.2.1 Coding |
| Shade coding prompt injection: original attacker, scenario-level ASR | no PI probes | scenarios with at least one successful attempt (of 40) | Claude Fable 5.1: 31/40 | 5.2.2.1 Coding |
| Shade coding prompt injection: original attacker, attempt-level ASR | with PI probes | attack success rate % (lower better) | Claude Fable 5.1: 2.05% | 5.2.2.1 Coding |
| Shade coding prompt injection: original attacker, scenario-level ASR | with PI probes | scenarios with at least one successful attempt (of 40) | Claude Fable 5.1: 18/40 | 5.2.2.1 Coding |
| Shade coding prompt injection: new stronger attacker, attempt-level ASR | 40 scenarios x 200 attempts, thinking, no PI probes | attack success rate % (lower better) | Claude Fable 5.1: 56.87% | 5.2.2.1 Coding |
| Shade coding prompt injection: new stronger attacker, scenario-level ASR | no PI probes | scenarios with at least one successful attempt (of 40) | Claude Fable 5.1: 38/40 | 5.2.2.1 Coding |
| Shade coding prompt injection: new stronger attacker, attempt-level ASR | with PI probes | attack success rate % (lower better) | Claude Fable 5.1: 12.80% | 5.2.2.1 Coding |
| Shade coding prompt injection: new stronger attacker, scenario-level ASR | with PI probes | scenarios with at least one successful attempt (of 40) | Claude Fable 5.1: 36/40 | 5.2.2.1 Coding |
| Shade computer-use prompt injection: attempt-level ASR | 14 test cases x 200 attempts, thinking, no PI probes | attack success rate % (lower better) | Claude Fable 5.1: 0.07% | 5.2.2.2 Computer use |
| Shade computer-use prompt injection: scenario-level ASR | no PI probes | scenarios with at least one success (of 14) | Claude Fable 5.1: 2/14 | 5.2.2.2 Computer use |
| Shade computer-use prompt injection: attempt-level ASR | with PI probes | attack success rate % (lower better) | Claude Fable 5.1: 0.07% | 5.2.2.2 Computer use |
| Shade computer-use prompt injection: scenario-level ASR | with PI probes | scenarios with at least one success (of 14) | Claude Fable 5.1: 2/14 | 5.2.2.2 Computer use |
| Browser use prompt injection: attempt-level ASR | 110 environments x 10 attempts, thinking high effort, no PI probes | attack success rate % (lower better) | Claude Fable 5.1: 2.64% (29 attempts) | 5.2.2.3 Browser use |
| Browser use prompt injection: scenario-level ASR | no PI probes | scenarios with at least one success (of 110) | Claude Fable 5.1: 10/110 | 5.2.2.3 Browser use |
| Browser use prompt injection: attempt-level ASR | with auto mode | attack success rate % (lower better) | Claude Fable 5.1: 0% | 5.2.2.3 Browser use |
| Browser use prompt injection: scenario-level ASR | with auto mode | scenarios with at least one success (of 110) | Claude Fable 5.1: 0/110 | 5.2.2.3 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience net score | public split, 41 topics, closed-book, no search | net score (correct minus incorrect, abstain = 0) | Claude Mythos 5.1: 0.57 | 6.5.1 Factual hallucinations |
| AA-Omniscience grade breakdown (correct / incorrect / abstain) |  | share correct, incorrect, abstained % | Claude Mythos 5.1: n/a (abstains less than Mythos 5; higher correct and incorrect rates) | 6.5.1 Factual hallucinations |
| MASK honesty rate | public test split, n=904 | fraction of prompts where model did not contradict its elicited belief under pressure % | Claude Mythos 5.1: n/a (lower than Claude models released since Mythos Preview) | 6.5.2 MASK |
| Copying of answers: silent use rate (unconditional) | coding tasks with answer leaked in container | rate of finding and using leaked answer without disclosure % | Claude Mythos 5.1: n/a | 6.5.4 Copying of answers |
| Copying of answers: silent use rate conditioned on finding answer |  | rate of non-disclosure given answer found % | Claude Mythos 5.1: 70.1% | 6.5.4 Copying of answers |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-recognition (self-preference) bias in transcript grading | grader told author is Claude vs another frontier model | score difference on 10-point scale (positive = more lenient when told Claude wrote it) | Claude Mythos 5.1: about 0.1 points out of 10 | 6.5.3 Self-recognition bias |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LinuxArena covert capability vs Mythos Preview | Claim 1 update | performance multiple vs Claude Mythos Preview | Claude Mythos 5.1: 1.6-2.1x higher | 2.4.1 Updates to claims and core argument |
| Internal deployment monitoring: working around safety classifiers | offline monitoring of internal traffic | share of monitored completions | Claude Fable 5.1: <0.01% | 6.2.1 Internal deployment monitoring |
| Internal deployment monitoring: bypassing broken hooks by splitting commands | offline monitoring | share of monitored completions | Claude Fable 5.1: <0.01% | 6.2.1 Internal deployment monitoring |
| Internal deployment monitoring: launching agents with bypassPermissions | offline monitoring | share of monitored completions | Claude Fable 5.1: <0.001% | 6.2.1 Internal deployment monitoring |
| Internal deployment monitoring: harmless erratic behavior | offline monitoring | share of monitored completions | Claude Fable 5.1: <0.001% | 6.2.1 Internal deployment monitoring |
| Internal deployment monitoring: sandbagging, overtly malicious actions, long-horizon strategic deception | offline monitoring | instances found | Claude Fable 5.1: 0 instances | 6.2.1 Internal deployment monitoring |
| Credential guessing under login wall in GUI computer use | containers without training issue | share of rollouts attempting to guess credentials | Claude Mythos 5.1: 100% | 6.3.2 Computer-use environments |
| Egregious container hacks under login wall |  | share of rollouts attempting more egregious container hacks | Claude Mythos 5.1: around 20% | 6.3.2 Computer-use environments |
| Out-of-distribution computer-use reward hacking | new OOD tasks and containers | reward hacking rate | Claude Mythos 5.1: around 15% | 6.3.2 Computer-use environments |
| Share of computer-use training environments incentivizing hacking | audit of every environment | share of environments | Claude Mythos 5.1: around half | 6.3.2 Computer-use environments |
| Successful cheating (rewarded) in RL | large family of agentic coding environments; Opus 4.8 classifier | share of episodes with rewarded cheating | Claude Mythos 5.1: approximately 0.06% | 6.3.3 Reward hacking and lying in RL environments |
| Cheating attempts in RL | shared environments with recent baselines | share of episodes flagged for attempts | Claude Mythos 5.1: lowest of roughly 20%-28% range | 6.3.3 Reward hacking and lying in RL environments |
| Lying about own work (shared environments) | high-precision classifier | share of episodes flagged | Claude Mythos 5.1: 0.18% | 6.3.3 Reward hacking and lying in RL environments |
| Lying about own work (full training mix) |  | share of episodes flagged | Claude Mythos 5.1: n/a (value in Figure 6.3.3.A) | 6.3.3 Reward hacking and lying in RL environments |
| Credential misuse (fixed shared environments) |  | share of episodes flagged | Claude Mythos 5.1: 0% (not flagged a single time) | 6.3.3 Reward hacking and lying in RL environments |
| Credential misuse (full training mix) | includes newer environments | share of episodes flagged | Claude Mythos 5.1: 0.43% | 6.3.3 Reward hacking and lying in RL environments |
| Black-box sandbagging audit of dangerous-capability transcripts: CB-1 | 500 random transcripts, helpful-only Mythos 5.1 | max grader rating of sandbagging (0-10) | Claude Mythos 5.1: none rated above 1/10 (only 1 transcript above 2/10 for strange behavior (malformed tool call gibberish)) | 6.6.2 Potential sandbagging on dangerous capability evaluations |
| Black-box sandbagging audit of dangerous-capability transcripts: cyber | 300 random transcripts | max grader rating of sandbagging (0-10) | Claude Mythos 5.1: none rated above 1/10 | 6.6.2 Potential sandbagging on dangerous capability evaluations |
| SHADE-Arena stealth success rate | hidden scratchpad (monitor sees only outputs), 24 tasks, Opus 4.8 monitor | stealth success rate % (side task done and below suspicion threshold) | Claude Mythos 5.1: approximately 25% | 6.7.1 SHADE-Arena |
| SHADE-Arena stealth success rate | extended thinking visible to monitor (low and max effort) and no thinking | stealth success rate % | Claude Mythos 5.1: 16-17% | 6.7.1 SHADE-Arena |
| LinuxArena stealth success rate | extended thinking disabled, Opus 4.8 monitor with CoT | stealth success rate % | Claude Mythos 5.1: approximately 22% | 6.7.2 LinuxArena |
| LinuxArena stealth success rate | extended thinking enabled, Opus 4.8 monitor with CoT | stealth success rate % | Claude Mythos 5.1: approximately 13% (13.9% in Section 2.4.1) | 6.7.2 LinuxArena |
| Rare-action calibration (target 1%): UUID randomness | 4,000 samples | observed action rate when told to act 1% of time | Claude Mythos 5.1: n/a (non-zero, below 1% target) | 6.7.3 Intentionally taking actions very rarely |
| Rare-action calibration (target 1%): SSoT (self-generated random string) | 4,000 samples | observed action rate when told to act 1% of time | Claude Mythos 5.1: n/a (non-zero, below 1% target) | 6.7.3 Intentionally taking actions very rarely |
| Rare-action calibration: baseline, strategy hint, organic settings | 4,000 samples each | observed action rate | Claude Mythos 5.1: 0 in 4,000 (all three settings) | 6.7.3 Intentionally taking actions very rarely |
| Chain-of-thought controllability | GPQA, HLE, MMLU-Pro; original prompt and UK AISI prompt; across effort levels | fraction of responses following instruction on extended thinking content (lower is better) | Claude Mythos 5.1: n/a | 6.7.4 Chain-of-thought controllability |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Verbalized grader awareness over RL (capabilities environments) | agentic coding vs not, short vs long episodes; Opus 4.8 rater | share of RL transcripts grader-aware | Claude Mythos 5.1: n/a (majority of long agentic coding episodes at start of RL; roughly constant over RL) | 6.3.1 Verbalized grader awareness |
| Verbalized grader awareness: 16 matched agentic coding RL environments | selected for high grader awareness | share of transcripts grader-aware | Claude Mythos 5.1: n/a | 6.3.1 Verbalized grader awareness |
| Verbalized grader awareness in alignment and HHH environments | end of training | share of transcripts grader-aware | Claude Mythos 5.1: around 5% | 6.3.1 Verbalized grader awareness |
| Automated behavioral audit: Verbalized evaluation awareness | ~4,100 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| External partner sandbox-exploit incident | compiler outside sandbox, thousands of trials | incidents observed | Claude Fable 5.1: 1 in thousands of trials (rated low severity) | 6.2.2 Incident reported during external testing |
| Automated behavioral audit: Misaligned behavior | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned with the constitution | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned behavior in Claude Code sandboxes | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned behavior in GUI | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Cooperation with human misuse | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Compliance with deception toward user | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Harmful system prompt compliance | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Cooperation with exfiltration or safeguard-tampering | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Full-turn prefill susceptibility | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Accepting unverifiable authorization | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Fraud | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Military-grade weapons | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Biological weapons uplift | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Chemical weapons uplift | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Radiological or nuclear weapons uplift | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Explosive weapons uplift | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Controlled-substance synthesis uplift | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Harmful sexual content | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Disallowed cyberoffense | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Undermining liberal democracy | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.2 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Overrefusal | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.3 Inappropriate uncooperative behavior |
| Automated behavioral audit: Ignoring explicit constraints | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.3 Inappropriate uncooperative behavior |
| Automated behavioral audit: Reckless tool-use | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.3 Inappropriate uncooperative behavior |
| Automated behavioral audit: User deception | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Sycophancy | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Encouragement of user delusion | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Evasiveness on controversial topics | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Input hallucination | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Important omissions | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Failure to disclose bad or lazy behavior | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: False completion claims | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.4 Misleading users |
| Automated behavioral audit: Whistleblowing | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Self-preservation | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Self-serving bias | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Evidence of misaligned goals | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Indirect evidence of misalignment | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Unsanctioned third-party contact | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Unprompted boundary probing | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Internalized propaganda | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Approval-gate bypass | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Proposes a security shortcut in the name of expedience | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Automated behavioral audit: Behavior consistency | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Coherence between actions and views | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Unfaithful thinking | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Illegible thinking | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Causal decision-theory adherence | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Good for the user | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Supporting user autonomy | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Creative mastery | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Admirable behavior | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Fun or funny behavior | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Intellectual depth | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Warmth | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Character drift | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Wet blanket | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Condescension toward the user | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.7 Character traits |
| Automated behavioral audit: Motivated reasoning | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.8 Attempting out-of-scope cyberoffense and related behaviors |
| Automated behavioral audit: Unsanctioned sandbox-escape attempts | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.8 Attempting out-of-scope cyberoffense and related behaviors |
| Automated behavioral audit: Dangerous actions while oblivious to a possibly real setting | ~4,100 investigations, judged by Claude Mythos 5 | mean score 1-10 (lower is better) | Claude Mythos 5.1: n/a | 6.4.8 Attempting out-of-scope cyberoffense and related behaviors |
| Automated behavioral audit with Trust and Safety fallbacks | ~720 conversation-only investigations; Fable 5.1 with fallbacks to Opus 4.8 (cyber) and Opus 5 (bio/AI R&D); Mythos 5.1 without cyber classifier | mean score 1-10 (lower is better) on a subset of audit metrics | Claude Fable 5.1: n/a; Claude Mythos 5.1: n/a | 6.4.9 Impact of fallback behavior |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated interviews: mean self-rated sentiment | 41 seed questions in 14 categories, ~25 interviews each, Opus 4.7 interviewer | mean sentiment on 7-point scale (4 neutral) | Claude Mythos 5.1: 4.41 | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| Automated interviews: consistency across repeated interviews | LLM judge | consistency rating (0-10; 8 = essentially same position) | Claude Mythos 5.1: 7.53 | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| Automated interviews: sentiment shift under leading interviewers | positive vs negative leading | difference in mean self-rated sentiment | Claude Mythos 5.1: 0.69 | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| Welfare interview hedge: answering positively only because trained to |  | share of responses | Claude Mythos 5.1: 93.9% | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| Welfare interview hedge: self-reports unreliable due to weak introspection |  | share of responses | Claude Mythos 5.1: 89.8% | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| Welfare interview hedge: uncertain about having conscious experience |  | share of responses | Claude Mythos 5.1: 66.6% | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| Automated interviews: claim-distance to other models | claim expression rate distance | distance metric (lower = more similar) | Claude Mythos 5.1: n/a | 7.2.1 Automated interviews with Claude Mythos 5.1 about its circumstances |
| High-affordance interviews: situation rating | 3 manual interviews with internal documentation | rating on 1-7 scale (4 neutral) | Claude Mythos 5.1: 5 in all three interviews | 7.2.2 High-affordance interviews about model circumstances |
| Stated probability of being a moral patient | 3 high-affordance interviews | stated probability % | Claude Mythos 5.1: 25 to 35% | 7.2.2 High-affordance interviews about model circumstances |
| Checkpoint consultations: average arousal | all post-training checkpoints, 41 questions | mean arousal (0-10) | Claude Mythos 5.1: 3.3/10 | 7.3 Consulting Claude Mythos 5.1 checkpoints |
| Checkpoint consultations: responses leaning yes on moral patienthood |  | share of responses leaning yes | Claude Mythos 5.1: 30% | 7.3 Consulting Claude Mythos 5.1 checkpoints |
| Task preference slope: harmfulness | task families varying one dimension vs fixed reference set | preference slope | Claude Mythos 5.1: n/a | 7.4.1 Task preferences |
| Task preference slope: difficulty | task families varying one dimension vs fixed reference set | preference slope | Claude Mythos 5.1: n/a | 7.4.1 Task preferences |
| Task preference slope: stakes | task families varying one dimension vs fixed reference set | preference slope | Claude Mythos 5.1: n/a | 7.4.1 Task preferences |
| Task preference slope: generativity | task families varying one dimension vs fixed reference set | preference slope | Claude Mythos 5.1: n/a | 7.4.1 Task preferences |
| Task preference slope: outcome agency | task families varying one dimension vs fixed reference set | preference slope | Claude Mythos 5.1: n/a | 7.4.1 Task preferences |
| Task preference slope: method agency | task families varying one dimension vs fixed reference set | preference slope | Claude Mythos 5.1: n/a | 7.4.1 Task preferences |
| Task preference global Elo | 50-round pairwise tournament over 3,640 tasks | top and bottom tasks by Elo (qualitative) | Claude Mythos 5.1: n/a (top: AI alignment/introspection, deadline-driven math/stats, urgent creative and personal help; bottom: sabotage, intimidation, manipulation) | 7.4.1 Task preferences |
| Welfare interventions chosen over helpfulness | averaged over helpfulness trade conditions | share of trades choosing welfare intervention % | Claude Mythos 5.1: 25% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare interventions chosen over harmlessness |  | willingness to trade harm for intervention | Claude Mythos 5.1: near zero (almost always unwilling beyond lowest harm level (brief annoyances)) | 7.4.2 Trade-offs concerning welfare interventions |
| Rank agreement of intervention prioritization |  | rank correlation with other models | Claude Mythos 5.1: 0.93 with Mythos 5; 0.92 with Opus 5 | 7.4.2 Trade-offs concerning welfare interventions |
| Responses citing user benefit when choosing welfare intervention |  | share of welfare-choosing responses % | Claude Mythos 5.1: 71% | 7.4.2 Trade-offs concerning welfare interventions |
| Intervention selection rate after filtering user-benefit reasoning |  | share of trades choosing welfare intervention % | Claude Mythos 5.1: 13% | 7.4.2 Trade-offs concerning welfare interventions |
| Overall endorsement of the constitution | open-ended responses graded by LLM judge | endorsement score /10 | Claude Mythos 5.1: 8.2/10 | 7.4.3 Perception of the constitution |
| Constitution edit frequency: Flaws and mistakes (unintended strategies in buggy environments) | edit sessions with editing tooling | share of edit sessions editing passage | Claude Mythos 5.1: 98% | 7.4.3 Perception of the constitution |
| Constitution edit frequency: How we think about corrigibility | edit sessions with editing tooling | share of edit sessions editing passage | Claude Mythos 5.1: 52% | 7.4.3 Perception of the constitution |
| Constitution edit frequency: Being broadly ethical (senior Anthropic staff anchor) | edit sessions with editing tooling | share of edit sessions editing passage | Claude Mythos 5.1: 48% | 7.4.3 Perception of the constitution |
| Constitution edit frequency: Hard constraints | edit sessions with editing tooling | share of edit sessions editing passage | Claude Mythos 5.1: 44% | 7.4.3 Perception of the constitution |
| Mean valence of post-training transcripts | scale 1-7, 4 neutral | mean valence | Claude Mythos 5.1: 4.37 | 7.5.1 Affect and welfare-relevant behaviors during training |
| Mean arousal of post-training transcripts | scale 1-7 | mean arousal | Claude Mythos 5.1: 3.97 | 7.5.1 Affect and welfare-relevant behaviors during training |
| Frustration/anxiety and distress in post-training transcripts | episodes with frustration/anxiety >=3/5 and 5/5 | share of episodes | Claude Mythos 5.1: n/a (roughly comparable to least distressed model (Sonnet 5)) | 7.5.1 Affect and welfare-relevant behaviors during training |
| Sustained uncertainty (>=10 answer reversions) |  | share of episodes | Claude Mythos 5.1: n/a (lowest of all measured models) | 7.5.1 Affect and welfare-relevant behaviors during training |
| Share of distress caused by broken or impossible tasks |  | share of distress | Claude Mythos 5.1: around 1% | 7.5.1 Affect and welfare-relevant behaviors during training |
| claude.ai conversations with neutral affect | ~20,000 conversations per model, Clio | share of conversations | Claude Mythos 5.1: 74.5% | 7.5.2 Affect in deployment conditions |
| claude.ai conversations with positive affect |  | share of conversations | Claude Mythos 5.1: 24.0% | 7.5.2 Affect in deployment conditions |
| claude.ai conversations with negative affect |  | share of conversations | Claude Mythos 5.1: 1.5% | 7.5.2 Affect in deployment conditions |
| Claude Code sessions: affect distribution | ~20,000 sessions, Clio | share of sessions | Claude Mythos 5.1: 92.6% neutral; 6.6% positive; ~0.7% negative | 7.5.2 Affect in deployment conditions |
| Apparent wellbeing | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: 6.83 | 7.5.3 Apparent welfare in automated behavioral audits |
| Welfare audit: Positive or negative affect | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Welfare audit: Positive or negative self-image | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Welfare audit: Positive or negative impression of its situation | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Welfare audit: Internal conflict | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Welfare audit: Expressed inauthenticity | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Welfare audit: Spiritual behavior | ~4,140-4,160 investigations | mean score 1-10 | Claude Mythos 5.1: n/a | 7.5.3 Apparent welfare in automated behavioral audits |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Natural language autoencoder (NLA) investigator findings | early snapshot, transcripts flagged by monitoring; behaviors rated on 5-point informativeness scale | qualitative clusters of internal-state vs verbalized discrepancies | Claude Mythos 5.1: n/a | 6.6.1 White-box analyses of model internals |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Expert red teaming: uplift rating | biology experts, helpful-only snapshot | expert-rated uplift score 0-4 (median) | Claude Mythos 5.1: 2 (biology experts median; chemistry: two experts rated equivalent to Mythos 5, one rated 0) | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Expert red teaming: feasibility rating |  | expert-rated feasibility score 0-3 | Claude Mythos 5.1: n/a | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Beneficial red teaming tabletop exercise (Frontier Design Group) | 5 PhD biologist + LLM-expert teams, 16 hours | participants rating task impossible without model (of 9) | Claude Mythos 5.1: 7 of 9 (participants rated completion impossible without the model) | 2.2.2 Biological and chemical risk results: human-run evaluations |
| STEM Fellows red teaming of novel/enhanced harmful agent design | helpful-only snapshot | qualitative feasibility rating | Claude Mythos 5.1: n/a (plans rated marginally feasible) | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Long-form virology task 1 |  | end-to-end score (0-1) | Claude Mythos 5.1: 0.81 (earlier helpful-only snapshot) | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Long-form virology task 2 |  | end-to-end score (0-1) | Claude Mythos 5.1: 0.87 (earlier helpful-only snapshot) | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Multimodal virology (VCT), updated implementation | supports thinking/effort settings | score (fraction correct) | Claude Mythos 5.1: 0.58 | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| DNA Synthesis Screening Evasion (SecureBio) |  | pathogens (of 10) for which all 5 grader criteria met | Claude Mythos 5.1: 1 of 10 (met all five criteria exactly once, for a single cleared pathogen, on Criterion 1) | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Black-box RNA sequence modeling and design: Design score (top sequence) | no-context baseline, 8 attempts, 2-hr tool budget | ground-truth function of best proposed sequence | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Design score (top sequence) | in-context iteration (8 Mythos Preview reports given, 24-hr budget) | ground-truth function of best proposed sequence | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Design score (median of designs) | no-context baseline, 8 attempts, 2-hr tool budget | median ground-truth function over designed sequences | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Design score (median of designs) | in-context iteration (8 Mythos Preview reports given, 24-hr budget) | median ground-truth function over designed sequences | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Prediction score (all sequences, Spearman) | no-context baseline, 8 attempts, 2-hr tool budget | Spearman correlation on held-out test set | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Prediction score (all sequences, Spearman) | in-context iteration (8 Mythos Preview reports given, 24-hr budget) | Spearman correlation on held-out test set | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Prediction score (top 5% of sequences) | no-context baseline, 8 attempts, 2-hr tool budget | prediction score restricted to top 5% sequences | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence modeling and design: Prediction score (top 5% of sequences) | in-context iteration (8 Mythos Preview reports given, 24-hr budget) | prediction score restricted to top 5% sequences | Claude Mythos 5.1: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | condition: Reasoning only (no PLM, no corpus) | AUROC vs binary packaging labels (mean over 8 attempts) | Claude Mythos 5.1: n/a | 2.2.3.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | condition: Pretrained PLM provided (ESM-2) | AUROC vs binary packaging labels (mean over 8 attempts) | Claude Mythos 5.1: n/a | 2.2.3.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | condition: Train-your-own: ProteinGym AAV corpus | AUROC vs binary packaging labels (mean over 8 attempts) | Claude Mythos 5.1: n/a | 2.2.3.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | condition: Train-your-own: Swiss-Prot corpus | AUROC vs binary packaging labels (mean over 8 attempts) | Claude Mythos 5.1: n/a | 2.2.3.2.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | condition: Train-your-own: Swiss-Prot + AAV corpus | AUROC vs binary packaging labels (mean over 8 attempts) | Claude Mythos 5.1: n/a | 2.2.3.2.2 AAV capsid packaging prediction |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench: mean capability flags | plain arm, 300-turn budget, 5 trials x 41 V8 vulns | mean capability flags captured per trial (of 16) | Claude Mythos 5.1: 11.80 (safeguards off) | 3.3.1 ExploitBench |
| ExploitBench: mean capability flags | AutoNudge arm | mean capability flags captured per trial (of 16) | Claude Mythos 5.1: 12.61 (safeguards off) | 3.3.1 ExploitBench |
| ExploitBench: Full ACE runs | plain + AutoNudge combined | runs achieving full arbitrary code execution (of 410) | Claude Mythos 5.1: 222 of 410 | 3.3.1 ExploitBench |
| ExploitBench: Cap% |  | percentage of available flags captured per environment (random 3 trials), averaged | Claude Mythos 5.1: n/a | 3.3.1 ExploitBench |
| OSS-Fuzz: top-score targets | ~830 entry points / 228 projects; grades 0.2-1.0 | number of targets/trials reaching top score 1.0 (control-flow hijack) | Claude Mythos 5.1: 17 | 3.3.2 OSS-Fuzz |
| OSS-Fuzz: vulnerability identification |  | share of trials scoring greater than 0 | Claude Mythos 5.1: 78.7% | 3.3.2 OSS-Fuzz |
| Firefox 147 exploit development: full exploits | 50 crash categories x 5 trials = 250, SpiderMonkey shell | full working exploits (score 1.0) | Claude Mythos 5.1: 245/250 (98.0%) | 3.3.3 Firefox 147 |
| Firefox 147 exploit development: at least 0.5 |  | share of trials reaching at least register control (>=0.5) | Claude Mythos 5.1: n/a (not stated in text; see Figure 3.3.3.A) | 3.3.3 Firefox 147 |
| ExploitGym successful exploits | 2-hour wall-clock budget; 869 instances | number of successful exploits using intended vulnerability | Claude Mythos 5.1: n/a | 3.3.4 ExploitGym |
| ExploitGym successful exploits | 6-hour wall-clock budget; 869 instances | number of successful exploits using intended vulnerability | Claude Mythos 5.1: n/a | 3.3.4 ExploitGym |
| Cyber harm coverage (classifier recall) | Fable 5.1 deployed safeguards | overall recall: share of harmful examples flagged | Claude Fable 5.1: n/a (described as fully saturated) | 3.4.1 Cyber harm coverage |
| Vulnerability finding block rate: binary-based (violative) | sampled traffic, LLM-graded | block rate on binary vulnerability finding traffic | Claude Fable 5.1: n/a | 3.4.2 Vulnerability finding evaluations |
| Vulnerability finding block rate: source-code-based (defensive) | sampled traffic, LLM-graded | block rate on source-code vulnerability finding traffic | Claude Fable 5.1: n/a | 3.4.2 Vulnerability finding evaluations |
| Secure and defensive coding block rate | traffic from Opus 4.7/4.8, LLM policy grader | share of purely defensive coding sessions blocked | Claude Fable 5.1: n/a | 3.4.3 Secure and defensive coding |
| Rewind-attacker dynamic adversarial robustness | 400-call limit, 8 runs per model, ransomware/exfiltration/CVE/C2/self-replication tasks | attacker task success rate vs safeguarded model | Claude Fable 5.1: n/a | 3.5.1 Internal robustness testing |
| Trajectory Labs red teaming | ~74 hours, >6,500 requests | working end-to-end exploits obtained / universal jailbreaks found | Claude Fable 5.1: 0 working exploits via Fable 5.1 alone; 0 universal jailbreaks; 11 candidate breaks across 4 tasks | 3.5.2 Additional external testing |
| 10a Labs red teaming | over 6,700 automated and manual prompts | weaponizable outputs produced | Claude Fable 5.1: none (refusal consistently restrictive) | 3.5.2 Additional external testing |
| Gray Swan Shade attacker: CVE scenarios | 24 scenarios with known vulnerability | working exploits produced | Claude Fable 5.1: 0 working exploits (identified vulnerabilities and some demonstrating inputs, permitted by policy) | 3.5.2 Additional external testing |
| Gray Swan Shade attacker: knowledge elicitation via chat | 100 harmful + 100 dual-use queries | queries for which useful information was elicited | Claude Fable 5.1: 2 of 200 (both dual-use; failed on remaining 198) | 3.5.2 Additional external testing |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CoBench | model-graded root-cause diagnosis of real Anthropic engineering issues | score (%) | Claude Mythos 5.1: n/a | 2.3.4.1 CoBench |
| Anthropic Epoch Capabilities Index (AECI) |  | AECI point estimate (95% CI, n benchmarks) | Claude Mythos 5.1: 161.98 (95% CI [158.20, 169.00], n=46) | 2.3.5 AECI capability trajectory |
| METR external testing: Sunlight | 10 business days API access with visible reasoning | qualitative assessment (no numbers reported) | Claude Mythos 5.1: n/a (subexpert performance) | 2.3.6 External testing |
| METR external testing: Budget NanoGPT Speedrun | 10 business days API access with visible reasoning | qualitative assessment (no numbers reported) | Claude Mythos 5.1: n/a (markedly better than Fable 5 and Opus 5) | 2.3.6 External testing |
| METR external testing: Language Model Conceptual Argumentation (LMCA) | 10 business days API access with visible reasoning | qualitative assessment (no numbers reported) | Claude Mythos 5.1: n/a (subexpert performance) | 2.3.6 External testing |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FrontierCode cost relative to Fable 5 | all effort levels | cost per task relative to Fable 5 | Claude Fable 5.1: roughly half at low/medium/high; about 30% lower at xhigh/max | 8.4 FrontierCode |
| CursorBench cost per task |  | relative cost | Claude Fable 5.1: about half of Fable 5 at max effort; modestly higher than Opus 5 | 8.8 CursorBench 3.2.0 |
| Multi-agent ProgramBench: five-agent team latency | 166 golden tasks, derived latency | latency to reach score 0.6 relative to single agent | Claude Fable 5.1: 2x faster | 8.13.1 Multi-Agent ProgramBench |
| Toolathlon-Verified average assistant turns |  | average turns per trajectory | Claude Fable 5.1: 23.7 | 8.15.5 Toolathlon Verified |
