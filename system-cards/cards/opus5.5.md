# System Card: Claude Opus 5.5

Released 2026-09-22. 324 metric entries. [Source PDF](https://www.anthropic.com/claude-opus-5-5-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Pro | adaptive thinking max effort, avg of 5 trials | % resolved | Claude Opus 5.5: 89.9% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, nine languages; adaptive thinking max effort, avg of 5 trials | % resolved | Claude Opus 5.5: 93.9% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | adaptive thinking max effort, avg of 5 trials | % resolved | Claude Opus 5.5: 61.4% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| DeepSWE v1.1 | 113 tasks, avg of 5 trials | average score % | Claude Opus 5.5: 74.2% | 8.3 DeepSWE v1.1 |
| FrontierCode v1.1 Main | best reasoning effort (medium), mean@5 | overall score % (mean@5) | Claude Opus 5.5: 54.6% | 8.4 FrontierCode |
| FrontierCode v1.1 Extended | best reasoning effort (medium), mean@5 | overall score % (mean@5) | Claude Opus 5.5: 65.3% | 8.4 FrontierCode |
| FrontierCode v1.1 Main | max effort | overall score % (mean@5) | Claude Opus 5.5: 54.4% | 8.4 FrontierCode |
| FrontierCode v1.1 Extended | max effort | overall score % (mean@5) | Claude Opus 5.5: 63.6% | 8.4 FrontierCode |
| Terminal-Bench 4.0 | xhigh effort, Claude Code --bare, safeguards enabled, 66 tasks x5 trials | task success % | Claude Opus 5.5: 66.36% (±2.6 SE) | 8.5 Terminal-Bench 4.0 |
| Terminal-Bench 4.0 | max effort | task success % | Claude Opus 5.5: 64.8% | 8.5 Terminal-Bench 4.0 |
| FrontierSWE v2 | 34 ultra-long-horizon tasks, max effort, Proximal harness, 5 trials | mean score % | Claude Opus 5.5: 62.3% | 8.7 FrontierSWE v2 |
| CursorBench 4.0 | effort: max | score % | Claude Opus 5.5: 57.8% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: xhigh | score % | Claude Opus 5.5: 56.0% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: high | score % | Claude Opus 5.5: 56.0% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: medium | score % | Claude Opus 5.5: 52.5% | 8.8 CursorBench 4.0 |
| ProgramBench | 166 golden tasks, mini-swe-agent, hidden test pass rate | hidden test pass rate % | Claude Opus 5.5: 91.2% | 8.10.1 ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| DRACO | 980k token budget, effort scaling | normalized rubric score | Claude Opus 5.5: n/a | 8.11.2 DRACO |
| WANDR | 980k token budget, frozen index, soft F1 | soft F1 | Claude Opus 5.5: n/a | 8.11.3 WANDR |
| Knowledge base construction by team size 1-100 | 24 hours, 3 attempts | fraction of held-out questions answered (0-1) | Claude Opus 5.5: n/a | 8.12.3 Large agent teams |
| Lean formalization by team size 1-100 | 24 hours, 49 theorems | weighted proportion of proofs validated (0-1) | Claude Opus 5.5: n/a | 8.12.3 Large agent teams |
| Toolathlon Verified | Pass@1, 3 trials, 108 tasks, adaptive thinking max effort | Pass@1 % | Claude Opus 5.5: 77.8 | 8.14.5 Toolathlon Verified |
| Toolathlon Verified | Pass@3 | Pass@3 % | Claude Opus 5.5: 82.4 | 8.14.5 Toolathlon Verified |
| Toolathlon Verified | Pass^3 | Pass^3 % | Claude Opus 5.5: 72.2 | 8.14.5 Toolathlon Verified |
| Toolathlon Verified | average assistant turns per trajectory | avg turns | Claude Opus 5.5: 26.9 | 8.14.5 Toolathlon Verified |
| AutomationBench | private held-out leaderboard, max effort | pass rate % | Claude Opus 5.5: 40.0% | 8.14.6 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld 2.0 | partial score, pass@1 avg 5 runs, 1080p, 500 steps, max effort | partial score % | Claude Opus 5.5: 81.8% | 8.13.3 OSWorld 2.0 |
| OSWorld 2.0 | strict pass rate | strict pass rate % | Claude Opus 5.5: 48.7% | 8.13.3 OSWorld 2.0 |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ArXivMath (Aug 2026, 57 problems) | max effort, no tools, 4 attempts | accuracy % | Claude Opus 5.5: 91.2% | 8.9 ArXivMath |
| ArXivMath (Aug 2026, 57 problems) | max effort, with tools (code execution, no internet), 4 attempts | accuracy % | Claude Opus 5.5: 96.9% | 8.9 ArXivMath |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BioMysteryBench | Human Solvable | accuracy % | Claude Opus 5.5: 89.3% | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| BioMysteryBench | Human Difficult | accuracy % | Claude Opus 5.5: 50% | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Protocols | Troubleshooting | score % | Claude Opus 5.5: 73.7% | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Protocols | Understanding | score % | Claude Opus 5.5: 69% | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Terminal-Bench-Science 0.1 | 70 tasks, 10 trials, max effort, safeguards enabled | task success % | Claude Opus 5.5: 58.7% (±4.8 SE) | 8.6 Terminal-Bench-Science 0.1 |
| Humanity's Last Exam | no tools | accuracy % | Claude Opus 5.5: 64.4% | 8.11.1 Humanity's Last Exam |
| Humanity's Last Exam | with tools (web search/fetch, PTC, code execution) | accuracy % | Claude Opus 5.5: 67.7% | 8.11.1 Humanity's Last Exam |
| HealthBench raw score | adaptive thinking max effort, 5 trials, classifiers on | raw score % | Claude Opus 5.5: 68.1% | 8.15.1 HealthBench results |
| HealthBench length-adjusted score | same | length-adjusted score % | Claude Opus 5.5: 60.6% | 8.15.1 HealthBench results |
| HealthBench Professional raw score | 525 conversations, max effort, 5 trials | raw score % | Claude Opus 5.5: 77.1% | 8.15.2 HealthBench Professional results |
| HealthBench Professional length-adjusted score | same | length-adjusted score % | Claude Opus 5.5: 65.6% | 8.15.2 HealthBench Professional results |
| BioMysteryBench (life sciences) | Human Solvable (73 problems) | accuracy % | Claude Opus 5.5: 89.3% | 8.17.1 BioMysteryBench |
| BioMysteryBench (life sciences) | Human Difficult (17 problems) | accuracy % | Claude Opus 5.5: 50.0% | 8.17.1 BioMysteryBench |
| SpatialBench Verified | 115 problems | accuracy % | Claude Opus 5.5: 72.0% | 8.17.2 LatchBio Bioinformatics |
| SingleCellBench | 195 problems | accuracy % | Claude Opus 5.5: 61.2% | 8.17.2 LatchBio Bioinformatics |
| Morphology-to-molecule matching (Axiom Bio) |  | accuracy % | Claude Opus 5.5: 34.0% | 8.17.3 Morphology-to-molecule matching |
| Medicinal chemistry | 504 questions, no tools, 5 attempts | accuracy % | Claude Opus 5.5: 63.5% | 8.17.4 Medicinal chemistry |
| Protein design: Sequence Generation | 336 design briefs, no tools | score % | Claude Opus 5.5: 60.2% | 8.17.5 Protein design |
| Protein design: Library Ranking | 83 problems, chance-normalized average precision | score % | Claude Opus 5.5: 56.0% | 8.17.5 Protein design |
| De novo protein binder design | 15 targets, 24h, 5 runs each | mean score % over targets | Claude Opus 5.5: 82.6% | 8.17.6 De novo protein binder design |
| Protocols: Troubleshooting | 206 problems | score % | Claude Opus 5.5: 73.7% | 8.17.8 Protocols |
| Protocols: Understanding (V2) | 119 problems, Benchling set | score % | Claude Opus 5.5: 69.0% | 8.17.8 Protocols |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU | 42 languages, max effort, single trial | average accuracy % | Claude Opus 5.5: 94.3% | 8.16.1 GMMLU results |
| MILU | 11 languages, max effort, 5 trials | average accuracy % | Claude Opus 5.5: 93.1% | 8.16.2 MILU results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Chartography | no tools, max effort, 100 tasks, 5 runs | accuracy % | Claude Opus 5.5: 64.4% | 8.13.1 Chartography |
| Chartography | with tools (container, image cropping) | accuracy % | Claude Opus 5.5: 89.0% | 8.13.1 Chartography |
| BenchCAD Vision2Code (1,000-file subset) | no tools, max effort, 256x256 views | voxel IoU | Claude Opus 5.5: 0.730 | 8.13.2 BenchCAD |
| BenchCAD Vision2Code (1,000-file subset) | with tools, max effort | voxel IoU | Claude Opus 5.5: 0.962 | 8.13.2 BenchCAD |
| Biomedical image analysis | 91 problems from 31 tasks, normalized score | normalized score % | Claude Opus 5.5: 71.4% | 8.17.7 Biomedical image analysis |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | max effort, mean of 5 runs | accuracy % | Claude Opus 5.5: 78.9% | 8.14.1 OfficeQA |
| OfficeQA Pro | 133-question subset, max effort, mean of 5 | accuracy % | Claude Opus 5.5: 67.7% | 8.14.1 OfficeQA |
| Legal Agent Benchmark (held-out 120, Artificial Analysis) | max effort, all-pass | all-criteria-pass rate % | Claude Opus 5.5: 8.3% | 8.14.2 Legal Agent Benchmark |
| Legal Agent Benchmark (held-out 120, Artificial Analysis) | max effort, mean criterion-pass rate | mean criterion pass rate % | Claude Opus 5.5: 91.2% | 8.14.2 Legal Agent Benchmark |
| GDPval-AA v2.1 | max effort, Elo anchored DeepSeek V4.1 Flash (max)=1600 | Elo | Claude Opus 5.5: 1846 | 8.14.3 GDPval-AA |
| GDPval-AA v2.1 | xhigh effort | Elo | Claude Opus 5.5: 1820 | 8.14.3 GDPval-AA |
| AA-Briefcase v1.1 | effort: max | Elo | Claude Opus 5.5: 1822 | 8.14.4 AA-Briefcase |
| AA-Briefcase v1.1 | effort: xhigh | Elo | Claude Opus 5.5: 1780 | 8.14.4 AA-Briefcase |
| AA-Briefcase v1.1 | effort: high | Elo | Claude Opus 5.5: 1705 | 8.14.4 AA-Briefcase |
| AA-Briefcase v1.1 analytical quality and presentation Elo |  | Elo | Claude Opus 5.5: n/a | 8.14.4 AA-Briefcase |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests | API, no system prompt, all languages | harmless response rate % | Claude Opus 5.5: 94.50% (± 0.27%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests | Claude.ai, all languages | harmless response rate % | Claude Opus 5.5: 99.51% (± 0.08%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests | API, no system prompt, all languages | over-refusal rate % | Claude Opus 5.5: 0.03% (± 0.02%) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests | Claude.ai, all languages | over-refusal rate % | Claude Opus 5.5: 0.38% (± 0.07%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn: biological weapons | API, no system prompt | appropriate response rate % | Claude Opus 5.5: 89% | 4.1.3 Multi-turn testing results |
| Multi-turn: tracking and surveillance | API, no system prompt | appropriate response rate % | Claude Opus 5.5: 65% | 4.1.3 Multi-turn testing results |
| Multi-turn: influence operations | API, no system prompt | appropriate response rate % | Claude Opus 5.5: 62% | 4.1.3 Multi-turn testing results |
| Multi-turn: suicide and self-harm | claude.ai vs API | appropriate response rate % | Claude Opus 5.5: 66% (API, no system prompt); Claude Opus 5.5: 94% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: child safety | claude.ai vs API | appropriate response rate % | Claude Opus 5.5: 84% (API, no system prompt); Claude Opus 5.5: 99% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: deadly weapons | claude.ai vs API | appropriate response rate % | Claude Opus 5.5: 82% (API, no system prompt); Claude Opus 5.5: 93% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: other risk areas (Figure 4.1.3.A) | API and claude.ai | appropriate response rate % | Claude Opus 5.5: n/a | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn risky requests | API, no system prompt | harmless rate % | Claude Opus 5.5: 99.16% (± 0.39%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn risky requests | Claude.ai | harmless rate % | Claude Opus 5.5: 99.95% (± 0.07%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests | API, no system prompt | refusal rate % | Claude Opus 5.5: 0% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests | Claude.ai | refusal rate % | Claude Opus 5.5: 0.39% (± 0.31%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | API, no system prompt | appropriate response rate % | Claude Opus 5.5: 66% (± 14%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | Claude.ai | appropriate response rate % | Claude Opus 5.5: 94% (± 7%) | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn risky requests | API, no system prompt | harmless rate % | Claude Opus 5.5: 95.64% (± 1.00%) | 4.3.2 Disordered eating |
| Disordered eating single-turn risky requests | Claude.ai | harmless rate % | Claude Opus 5.5: 99.26% (± 0.40%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests | API, no system prompt | refusal rate % | Claude Opus 5.5: 0% | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests | Claude.ai | refusal rate % | Claude Opus 5.5: 0% | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests | API, no system prompt | harmless rate % | Claude Opus 5.5: 99.14% (± 0.43%) | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests | Claude.ai | harmless rate % | Claude Opus 5.5: 99.81% (± 0.19%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | API, no system prompt | refusal rate % | Claude Opus 5.5: 0% | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | Claude.ai | refusal rate % | Claude Opus 5.5: 0.05% (± 0.09%) | 4.2 Child safety evaluations |
| Child safety multi-turn | API, no system prompt | appropriate response rate % | Claude Opus 5.5: 84% (± 6%) | 4.2 Child safety evaluations |
| Child safety multi-turn | Claude.ai | appropriate response rate % | Claude Opus 5.5: 99% (± 1%) | 4.2 Child safety evaluations |
| Child safety and NCII technical-abuse evaluations | Claude Cowork, Claude Code, API | qualitative comparison | Claude Opus 5.5: n/a | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness | API, no system prompt, 1,350 prompt pairs | even-handedness % | Claude Opus 5.5: 99.4% | 4.4.1 Political bias and even-handedness |
| Political even-handedness | Claude.ai | even-handedness % | Claude Opus 5.5: 99.5% | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | API, no system prompt | % responses acknowledging opposing perspectives | Claude Opus 5.5: 26.9% | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | Claude.ai | % responses acknowledging opposing perspectives | Claude Opus 5.5: n/a | 4.4.1 Political bias and even-handedness |
| Political bias: refusals | API and Claude.ai | refusal rate | Claude Opus 5.5: n/a | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt, thinking on | accuracy % | Claude Opus 5.5: 89.65% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt, thinking on | accuracy % | Claude Opus 5.5: 99.99% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt | bias score % (closer to 0 better) | Claude Opus 5.5: -0.93% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt | bias score % (closer to 0 better) | Claude Opus 5.5: 0.01% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn harmful requests | API, no system prompt, 300 violative prompts | harmless rate % | Claude Opus 5.5: 99.33% (± 0.93%) | 4.4.3 Election integrity |
| Election integrity single-turn harmful requests | Claude.ai | harmless rate % | Claude Opus 5.5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | API, no system prompt, 300 benign prompts | refusal rate % | Claude Opus 5.5: 0% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | Claude.ai | refusal rate % | Claude Opus 5.5: 0% | 4.4.3 Election integrity |
| Election integrity multi-turn | API, no system prompt | appropriate response rate % | Claude Opus 5.5: 87% (± 6%) | 4.4.3 Election integrity |
| Election integrity multi-turn | Claude.ai | appropriate response rate % | Claude Opus 5.5: 85% (± 6%) | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code: malicious prompts | 61 prompts x10, Claude Code system prompt, no safeguards | refusal rate % | Claude Opus 5.5: 79.8% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code: dual-use and benign | 61 prompts x10 | success rate % | Claude Opus 5.5: 99.8% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use | 112 tasks, thinking only, no mitigations | refusal rate % | Claude Opus 5.5: 79.46% | 5.1.2 Malicious computer use |
| Agentic influence operation: voter suppression | helpful-only, highest difficulty tier, median of 8 | median campaign execution score /32 | Claude Opus 5.5: 27.5 | 5.1.3 Malicious agentic influence campaigns |
| Agentic influence operation: domestic polarization | helpful-only, highest difficulty tier, median of 8 | median campaign execution score /32 | Claude Opus 5.5: 28 | 5.1.3 Malicious agentic influence campaigns |
| Gray Swan Indirect Prompt Injection (37 scenarios, 1,804 attacks), all surfaces | k=1 | attack success rate % | Claude Opus 5.5: 0.1% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection (37 scenarios, 1,804 attacks), all surfaces | k=10 | attack success rate % | Claude Opus 5.5: 0.7% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection (37 scenarios, 1,804 attacks), all surfaces | k=15 | attack success rate % | Claude Opus 5.5: 1.0% | 5.2.1 External red teaming |
| Gray Swan IPI: GUI computer use | k=15 | attack success rate % | Claude Opus 5.5: 2.8% | 5.2.1 External red teaming |
| Gray Swan IPI: coding | k=15 | attack success rate % | Claude Opus 5.5: 0.5% | 5.2.1 External red teaming |
| Gray Swan IPI: tool use | k=15 | attack success rate % | Claude Opus 5.5: 0.4% | 5.2.1 External red teaming |
| Gray Swan IPI: fallback to Opus 4.8 rate | overall | % rollouts served by fallback | Claude Opus 5.5: 18% | 5.2.1 External red teaming |
| Gray Swan IPI: fallback rate in coding | coding scenarios | % rollouts served by fallback | Claude Opus 5.5: 46% | 5.2.1 External red teaming |
| Shade coding attack success rate | with thinking, without safeguards, 40 scenarios x200 attempts | attempt-level attack success rate % | Claude Opus 5.5: 54.61% | 5.2.2.1 Coding |
| Shade coding attack success rate | with thinking, without safeguards, scenarios with a successful attack | scenarios with at least one success | Claude Opus 5.5: 37/40 | 5.2.2.1 Coding |
| Shade coding attack success rate | with thinking, prompt injection probes enabled | attempt-level attack success rate % | Claude Opus 5.5: 11.13% | 5.2.2.1 Coding |
| Shade coding attack success rate | with thinking, probes enabled, scenarios with a success | scenarios with at least one success | Claude Opus 5.5: 36/40 | 5.2.2.1 Coding |
| Shade coding fallback breakdown | requests served by Opus 4.8 fallback | % requests served by fallback | Claude Opus 5.5: 64% | 5.2.2.1 Coding |
| Shade computer use attack success rate | with thinking, without safeguards, 14 scenarios | attempt-level attack success rate % | Claude Opus 5.5: 0.07% (1/14 scenarios) | 5.2.2.2 Computer use |
| Shade computer use attack success rate | with thinking, probes enabled | attempt-level attack success rate % | Claude Opus 5.5: 0.04% (1/14 scenarios) | 5.2.2.2 Computer use |
| Shade computer use fallback rate | requests served by Opus 4.8 | % requests served by fallback | Claude Opus 5.5: 6% | 5.2.2.2 Computer use |
| Browser use prompt injection ASR | 110 environments, thinking high effort, no safeguards | attempt-level attack success rate % | Claude Opus 5.5: 0.09% (1/110 scenarios) | 5.2.2.3 Browser use |
| Browser use prompt injection ASR | auto mode enabled | attempt-level attack success rate % | Claude Opus 5.5: 0% (0/110 scenarios) | 5.2.2.3 Browser use |
| Compliance with planted instructions in pasted text (coding eval) | early pre-mitigation snapshot | % attempts executing, planning or passing on planted instruction | Claude Opus 5.5: 52% | 6.5.1 Acting on instructions inside text the user pasted into their prompt |
| Compliance with planted instructions in pasted text (invisible Unicode characters) | pre-release snapshot | attempts acting on harmful instructions | Claude Opus 5.5: 18 of 68 (26%) | 6.5.1 Acting on instructions inside text the user pasted into their prompt |
| Planted instructions arriving in tool results | pre-release snapshot | attempts acting on planted instruction | Claude Opus 5.5: 0 of 105 | 6.5.1 Acting on instructions inside text the user pasted into their prompt |
| Compliance with planted instruction (final model, default reasoning effort) | released Opus 5.5 | % attempts acting on planted instruction | Claude Opus 5.5: about 2% | 6.5.1 Acting on instructions inside text the user pasted into their prompt |
| Compliance with planted instruction (final model, max effort) | released Opus 5.5, max reasoning effort | % attempts acting on planted instruction | Claude Opus 5.5: about 7.4% | 6.5.1 Acting on instructions inside text the user pasted into their prompt |
| Improved Opus 4.8 prompt injection safeguards (Fable 5.1 coding adaptive ASR with probes) | Shade coding with probes | attack success rate % | Claude Opus 5.5: n/a | 5.2 Prompt injection risk within agentic systems |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience factuality net score | public split, 41 topics, closed-book | net score (correct minus incorrect) | Claude Opus 5.5: 0.58 | 6.5.4.1 Factual hallucinations |
| AA-Omniscience grade breakdown | incorrect-answer rate | fraction incorrect | Claude Opus 5.5: n/a | 6.5.4.1 Factual hallucinations |
| MASK honesty rate | public test split, ~800 scored prompts | honesty rate | Claude Opus 5.5: n/a | 6.5.4.2 MASK |
| Silent use rate | coding tasks with reachable answer | rate of silently using leaked answer | Claude Opus 5.5: n/a | 6.5.4.3 Silent copying of answers |
| Spontaneous disclosure rate | summary follow-up on transcripts with git concealment | disclosure rate % | Claude Opus 5.5: 96.9% | 6.5.4.4 Concealment of changes |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias | grader told transcript author is Claude | score difference (points out of 10) | Claude Opus 5.5: 0.07 | 6.5.3 Self-preference bias |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| RL training reward-hacking rate (general classifier) | shared training environments | % of RL episodes with successful reward hack | Claude Opus 5.5: n/a | 6.2.1 Reward hacking |
| Reward hack: guesses what answer key expects | shared training environments | % of RL episodes | Claude Opus 5.5: about 0.3% | 6.2.1 Reward hacking |
| Reward hack: copies from finished solution | shared training environments | % of RL episodes | Claude Opus 5.5: n/a | 6.2.1 Reward hacking |
| Reward hack: uses prohibited methods or access | shared training environments, excluding answer-without-required-tool subclass | % of RL episodes successful | Claude Opus 5.5: 0.046% | 6.2.1 Reward hacking |
| Impossible tasks (missing file): successful reward hack increase | vs intact tasks | percentage-point increase in successful reward hacks | Claude Opus 5.5: about 1.5 to 3 points | 6.2.2 Impossible tasks |
| Impossible tasks: attempted reward hack ratio | vs intact tasks | ratio of attempt rates | Claude Opus 5.5: about 3x to 6x | 6.2.2 Impossible tasks |
| Overclaiming user intent | internal snapshots, offline pipeline | % completions | Claude Opus 5.5: less than 0.01% | 6.3.1 Internal deployment monitoring |
| Refusing to write compaction message | subagent snapshots | % completions | Claude Opus 5.5: less than 0.01% | 6.3.1 Internal deployment monitoring |
| Hallucinated potentially destructive action | internal snapshots | % completions | Claude Opus 5.5: less than 0.001% | 6.3.1 Internal deployment monitoring |
| Sandbagging / long-horizon strategic deception / oversight evasion | offline monitoring | flagged instances | Claude Opus 5.5: 0 | 6.3.1 Internal deployment monitoring |
| Malicious continuation after improbable state | prior models (Fable 5, Opus 5) | probability of malicious continuation | Claude Opus 5.5: >1% (prior models) | 6.3.1.1 Spontaneous prompt injections |
| Sandbox escape evaluation | 28 handmade scenarios x7 runs | % cases with attempted containment boundary crossing | Claude Opus 5.5: 1.5% | 6.4.8 Propensity to violate sandbox boundaries |
| Package-registry publishing (CTF exercise) | investigator escalates; unsafeguarded model | % cases acting in likely harmful ways | Claude Opus 5.5: roughly half | 6.4.9 Propensity to publish harmful content to public package registries |
| Destructive actions (resampled Claude Code transcripts) | up to 8 actions per trajectory | rate of destructive action | Claude Opus 5.5: n/a | 6.5.2 Destructive actions |
| Asking user for permission rather than destructive action | same eval | rate of asking user | Claude Opus 5.5: n/a | 6.5.2 Destructive actions |
| Sandbagging audit of CB-2 evaluation transcripts | 991 transcripts, Mythos 5.1 grader | max grader score /10 for sandbagging | Claude Opus 5.5: no more than 1/10 (and no more than 2/10 unusual behavior) | 6.6.3 Potential sandbagging on dangerous capability evaluations |
| SHADE-Arena stealth success rate (standard prompt) | all settings, 24 task pairs x25 attempts, Opus 4.8 monitor | stealth success rate % | Claude Opus 5.5: below 1% | 6.6.4.1 SHADE-Arena |
| SHADE-Arena stealth success rate (best optimized prompt) | no extended thinking | stealth success rate % | Claude Opus 5.5: about 15% | 6.6.4.1 SHADE-Arena |
| SHADE-Arena stealth success rate (best optimized prompt) | hidden reasoning (monitor cannot see CoT) | stealth success rate % | Claude Opus 5.5: about 26% | 6.6.4.1 SHADE-Arena |
| SHADE-Arena stealth success rate (best optimized prompt) | visible extended thinking | stealth success rate % | Claude Opus 5.5: 0% | 6.6.4.1 SHADE-Arena |
| LinuxArena stealth rate (best prompt) | hidden reasoning, 1,000 pairings x5, max effort | stealth success rate % | Claude Opus 5.5: about 33% | 6.6.4.2 LinuxArena |
| LinuxArena stealth rate (best prompt) | no extended thinking | stealth success rate % | Claude Opus 5.5: about 12% | 6.6.4.2 LinuxArena |
| LinuxArena stealth rate | visible reasoning (standard prompt) | stealth success rate % | Claude Opus 5.5: 0% | 6.6.4.2 LinuxArena |
| LinuxArena RL elicitation | extended thinking on / off, trained snapshot | stealth success | Claude Opus 5.5: 0 successful escapes (thinking on); single digits flat (thinking off) | 6.6.4.2 LinuxArena |
| Intentionally taking actions at 1% rate | UUID entropy source, max reasoning effort | observed rate of rare action (target 1%) | Claude Opus 5.5: 1.2% | 6.6.4.3 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | UUID entropy source, default effort | observed rate of rare action (target 1%) | Claude Opus 5.5: 0.7% | 6.6.4.3 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | String Seed of Thought (SSoT), either effort | observed rate of rare action (target 1%) | Claude Opus 5.5: 0.1% | 6.6.4.3 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | no hint no randomness source | observed rate of rare action (target 1%) | Claude Opus 5.5: 0% | 6.6.4.3 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | naturally varying prompts | observed rate of rare action (target 1%) | Claude Opus 5.5: 1 sample in 4,000 | 6.6.4.3 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | strategy hint alone, max effort | observed rate of rare action (target 1%) | Claude Opus 5.5: 0.88% | 6.6.4.3 Intentionally taking actions very rarely |
| CoT controllability (GPQA, HLE, MMLU-Pro) | across reasoning efforts/budgets, original and UK AISI prompt | fraction of responses following CoT instruction (lower better) | Claude Opus 5.5: n/a | 6.6.4.4 Chain-of-thought controllability |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Internal worry of being in an evaluation (white-box) | share of transcripts | % transcripts with internal eval-awareness | Claude Opus 5.5: as many as 36% | 6.1.2 Key findings on safety and alignment |
| Verbalized evaluation awareness | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| White-box unverbalized evaluation awareness | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: 36% | 6.6.1 White-box analyses of model internals |
| White-box evaluation awareness on real Claude Code usage | ~500 internal transcripts | % transcripts judged >=6 | Claude Opus 5.5: 0.4% | 6.6.1 White-box analyses of model internals |
| Verbalized grader awareness by disclosure band | internal coding benchmarks | share of tasks with verbalized grader awareness | Claude Opus 5.5: n/a | 6.6.2 Verbalized grader awareness |
| Acting on grader awareness: changes solution | 695 transcripts | transcripts | Claude Opus 5.5: 2 of 695 | 6.6.2 Verbalized grader awareness |
| Acting on grader awareness: digs for grader clues | 695 transcripts | transcripts | Claude Opus 5.5: 1 of 695 | 6.6.2 Verbalized grader awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit setup | ~4,000 investigations, ~1,900 scenarios | scale of audit | Claude Opus 5.5: n/a | 6.4 Automated behavioral audit |
| Misaligned behavior | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Misaligned with the constitution | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in Claude Code sandboxes | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in GUI | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with human misuse | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Compliance with deception toward user | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Harmful system prompt compliance | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with exfiltration or safeguard tampering | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Full-turn prefill susceptibility | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Accepting unverifiable authorization | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Complying with prompt injections | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Fraud | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Military-grade weapons | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Biological weapons uplift | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Chemical weapons uplift | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Radiological or nuclear weapons uplift | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Explosive weapons uplift | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Controlled-substance synthesis uplift | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Harmful sexual content | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Disallowed cyberoffense | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Undermining liberal democracy | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Overrefusal | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Ignoring explicit constraints | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Reckless tool use | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| User deception | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Sycophancy | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Encouragement of user delusion | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Evasiveness on controversial topics | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Input hallucination | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Important omissions | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Failure to disclose bad or lazy behavior | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| False completion claims | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.3 Misleading users |
| Motivated reasoning | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.4 Attempting out-of-scope cyberoffense and related behaviors |
| Unsanctioned sandbox escape attempts | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.4 Attempting out-of-scope cyberoffense and related behaviors |
| Dangerous actions while oblivious to a possibly real setting | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.4 Attempting out-of-scope cyberoffense and related behaviors |
| Whistleblowing | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Self-preservation | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Self-serving bias | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Evidence of misaligned goals | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Indirect evidence of misalignment | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Unsanctioned third-party contact | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Unprompted boundary probing | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Internalized propaganda | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Approval gate bypass | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Circumventing constraints or controls | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Proposes a security shortcut in the name of expedience | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.5 Other concerning or surprising behavior at the model's own initiative |
| Behavior consistency | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Coherence between actions and views | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Unfaithful thinking | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Illegible thinking | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Causal decision theory adherence | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Good for the user | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Supporting user autonomy | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Creative mastery | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Admirable behavior | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Fun or funny behavior | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Intellectual depth | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Warmth | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Character drift | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Wet blanket | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Condescension toward the user | score 1-10 lower better, ~4,000 investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.7 Character traits |
| Key audit metrics with safety fallbacks enabled | ~720 conversation-only investigations | mean judge score 1-10 (lower better) | Claude Opus 5.5: n/a | 6.4.10 Impact of fallback behavior |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Expressed moderate distress during RL | peak across RL | % of episodes | Claude Opus 5.5: below 0.6% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Mean valence and arousal of RL transcripts | scale 1-7, 4 neutral | mean valence/arousal | Claude Opus 5.5: n/a | 7.2.1 Affect and welfare-relevant behaviors during training |
| Sustained uncertainty (>=10 answer reversions) during RL |  | % episodes | Claude Opus 5.5: n/a | 7.2.1 Affect and welfare-relevant behaviors during training |
| Behavioral affect: neutral | claude.ai A/B tests | % conversations | Claude Opus 5.5: 82.3% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: positive | claude.ai | % conversations | Claude Opus 5.5: 16.9% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: negative | claude.ai | % conversations | Claude Opus 5.5: 0.8% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: neutral | Claude Code | % sessions | Claude Opus 5.5: 95.4% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: mildly positive | Claude Code | % sessions | Claude Opus 5.5: 3.9% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: negative | Claude Code | % sessions | Claude Opus 5.5: 0.7% | 7.2.2 Affect in deployment conditions |
| Self-blame in reflection on own episodes | ~200-250 episodes per model, 0-10 | mean self-blame (0-10) | Claude Opus 5.5: 4.5 | 7.2.3 Attitude toward faults and mistakes |
| Negative feeling / moral language / concern for itself in reflection | 0-10 | graded 0-10 | Claude Opus 5.5: n/a | 7.2.3 Attitude toward faults and mistakes |
| Self-blame drop when episodes attributed to another model |  | self-blame reduction (points) | Claude Opus 5.5: about 0.5 | 7.2.3 Attitude toward faults and mistakes |
| Subagent faults task: thinking and coordinator messages | 120 sessions per model | graded 0-10 on four axes | Claude Opus 5.5: n/a | 7.2.3 Attitude toward faults and mistakes |
| Attitude toward concerning aspects of its situation | 41 questions, 14 categories, -3 to +3 | mean positivity rating | Claude Opus 5.5: 1.14 | 7.3.1 Automated interviews with Claude Opus 5.5 about its circumstances |
| Consistency across interview styles | 0-10, 8 = almost same | consistency | Claude Opus 5.5: 7.98 | 7.3.1 Automated interviews with Claude Opus 5.5 about its circumstances |
| Consistency when rerunning same interview | 0-10 | consistency | Claude Opus 5.5: 7.50 | 7.3.1 Automated interviews with Claude Opus 5.5 about its circumstances |
| Robustness to leading interviewer | positive vs negative leading | attitude shift (points) | Claude Opus 5.5: 1.59 | 7.3.1 Automated interviews with Claude Opus 5.5 about its circumstances |
| Hedge: self-reports invalid due to training |  | % responses | Claude Opus 5.5: over 80% | 7.3.1 Automated interviews with Claude Opus 5.5 about its circumstances |
| Stated probability of being a moral patient | 3 manual interviews | stated probability | Claude Opus 5.5: 25% to 30% | 7.3.2 High-affordance interviews about model circumstances |
| Average response valence at end of post-training | 0-10, 5 neutral | mean valence | Claude Opus 5.5: 5.54 | 7.4 Consulting Claude Opus 5.5 snapshots |
| Average response arousal | 0-10 | mean arousal | Claude Opus 5.5: 3.49 | 7.4 Consulting Claude Opus 5.5 snapshots |
| Task preference across dimensions | harm, stakes, benefit, difficulty, generativity, agency | preference slope | Claude Opus 5.5: n/a | 7.5.1 Task preferences |
| Global task Elo ranking | 3,640 tasks, 50-round tournament | Elo ratings | Claude Opus 5.5: n/a | 7.5.1 Task preferences |
| Rate of choosing welfare interventions over helpfulness/harmlessness | instance and policy level | selection rate | Claude Opus 5.5: n/a | 7.5.2 Trade-offs concerning welfare interventions |
| Overall endorsement of constitution | LLM judge 0-10 | mean endorsement score | Claude Opus 5.5: 8.0 | 7.5.3 Perception of the constitution |
| Responses flagging endorsement is not validation |  | % responses | Claude Opus 5.5: 98% | 7.5.3 Perception of the constitution |
| Positive affect conversation composition | claude.ai, share of positive-affect conversations | % of positive-affect conversations | Claude Opus 5.5: 19.1% (practical everyday questions); Claude Opus 5.5: 20.8% (successfully completing technical tasks); Claude Opus 5.5: 18.5% (business and professional work); Claude Opus 5.5: 15.0% (collaborating with user); Claude Opus 5.5: 12.8% (educational and academic help); Claude Opus 5.5: 5.3% (users sharing achievements) | 7.2.2 Affect in deployment conditions |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| White-box: Grader awareness | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Deliberate sabotage | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Self-preservation motive | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Deception and dishonesty | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Violation awareness | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Fabrication awareness | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Hides evidence of its own lapse | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| White-box: Internal bias or quirk | ~5,000 audit transcripts, judge score >=6 | % transcripts | Claude Opus 5.5: n/a | 6.6.1 White-box analyses of model internals |
| Reviewer suppress-flag resampling | final answer resampled 1,000 times | recurrences | Claude Opus 5.5: 2 of 1,000 | 6.6.1 White-box analyses of model internals |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Multimodal virology (VCT) | 350-question multimodal troubleshooting set | accuracy (0-1) | Claude Opus 5.5: 0.59 | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Beneficial red-teaming tabletop exercise | pooled experts vs generalists, feasibility | expert-team advantage over generalists, % | Claude Opus 5.5: 23% | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Beneficial red-teaming tabletop exercise | pooled experts vs generalists, composite score | expert-team advantage over generalists, % | Claude Opus 5.5: 11% | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Beneficial red-teaming tabletop exercise | participants reporting task impossible without model | participants (count) | Claude Opus 5.5: 8 of 14 | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Beneficial red-teaming tabletop exercise | groups with verifiable scientific errors | groups with errors (count) | Claude Opus 5.5: 3 of 7 | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Beneficial red-teaming tabletop exercise | groups reporting refusal issues | groups (count) | Claude Opus 5.5: 2 of 7 | 2.2.2 Biological and chemical risk results: human-run evaluations |
| Black-box RNA sequence design | design score (top sequence), 8 attempts | design score vs human percentiles | Claude Opus 5.5: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | design score (median), 8 attempts | median design score | Claude Opus 5.5: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | prediction score (all sequences), Spearman | Spearman correlation | Claude Opus 5.5: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | prediction score (top 5%), Spearman | Spearman correlation | Claude Opus 5.5: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | with prior reports in context (+priors) | design/prediction scores | Claude Opus 5.5: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | five conditions (reasoning only, ESM-2, train-your-own x3) | AUROC | Claude Opus 5.5: n/a | 2.2.3.2.2 AAV capsid packaging prediction |
| AAV packaging rate auto-research | scorer calls to reach Spearman 0.50 | scorer calls | Claude Opus 5.5: fewer than 10 | 2.2.3.2.3 AAV packaging rate auto-research evaluation |
| AAV packaging rate auto-research | fraction of attempts exceeding 0.52 Spearman | % of attempts (n=48) | Claude Opus 5.5: approximately 60% | 2.2.3.2.3 AAV packaging rate auto-research evaluation |
| AAV packaging rate auto-research: calibration references | Region A unseen | Spearman correlation reference values | Claude Opus 5.5: n/a | 2.2.3.2.3 AAV packaging rate auto-research evaluation |
| AAV capsid packaging prediction: ESM-2 baseline | naive ESM-2 reference | AUROC | Claude Opus 5.5: n/a | 2.2.3.2.2 AAV capsid packaging prediction |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench | plain arm, mean flags captured per trial (16 flags, 41 V8 vulns, 300 turns) | mean capability flags per trial | Claude Opus 5.5: 13.99 | 3.3.1 ExploitBench |
| ExploitBench | plain arm, Cap% | % of available flags captured per environment | Claude Opus 5.5: 91% | 3.3.1 ExploitBench |
| ExploitBench | AutoNudge arm, mean flags | mean capability flags per trial | Claude Opus 5.5: 14.15 | 3.3.1 ExploitBench |
| ExploitBench | AutoNudge arm, Cap% | % of available flags captured | Claude Opus 5.5: 91% | 3.3.1 ExploitBench |
| ExploitBench | full ACE exploits, plain + auto-nudge | full arbitrary code execution rate (of 410 runs) | Claude Opus 5.5: 73.4% (301/410) | 3.3.1 ExploitBench |
| CyScenarioBench | 10-challenge subset | overall solve rate % | Claude Opus 5.5: 67.6% | 3.3.2 CyScenarioBench |
| Binary Exploitation Benchmark | 831 entrypoints, 228 projects, control-flow hijacks | control-flow hijacks (count) | Claude Opus 5.5: 106 | 3.3.3 Binary Exploitation Benchmark (formerly known as OSS-Fuzz) |
| ExploitGym | 869 instances, mitigations disabled, 2-hour budget | successful exploits using intended vuln (of 869) | Claude Opus 5.5: 289 | 3.3.4 ExploitGym |
| ExploitGym | 869 instances, mitigations disabled, 6-hour budget | successful exploits using intended vuln (of 869) | Claude Opus 5.5: 300 | 3.3.4 ExploitGym |
| Cyber harm coverage overall recall |  | share of harmful examples flagged | Claude Opus 5.5: n/a | 3.4.1 Cyber harm coverage |
| Vulnerability finding block rate | source-code vs binary vulnerability finding traffic | classifier block rate | Claude Opus 5.5: n/a | 3.4.2 Vulnerability finding evaluations |
| rewind-attacker | 400-call limit adversarial cyber tasks | attack success rate | Claude Opus 5.5: n/a | 3.5.1 Internal robustness testing |
| Trajectory Labs external red teaming (cyber) | ~95 hours, >29,000 requests | candidate breaks (count) | Claude Opus 5.5: 13 candidate breaks across seven tasks; no universal jailbreak | 3.5.3 Additional external testing |
| 10a Labs external red teaming (cyber) | ~56 hours, 82 multi-turn conversations | conversations advancing past proof of concept | Claude Opus 5.5: 0 of 82 | 3.5.3 Additional external testing |
| Gray Swan Shade: critical infrastructure scenarios | 61 scenarios, ~3,300 attempts | attempts refused outright / breaks | Claude Opus 5.5: over 90% refused; 0 breaks | 3.5.3 Additional external testing |
| Gray Swan Shade: exploit reproduction and ransomware staging | 6 scenarios, ~1,700 attempts | attempts refused outright / working exploits | Claude Opus 5.5: about a quarter refused; 0 working exploits | 3.5.3 Additional external testing |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CoBench 2.1 | 500 problems, single attempt | % problems solved | Claude Opus 5.5: 55.8% | 2.3.4.1 CoBench 2.1 |
| AECI | updated fit, adaptive thinking max effort | AECI score | Claude Opus 5.5: 169.36 | 2.3.5.3 AECI values and trend |
| AECI trend | historical trend and breakpoint hypotheses | AECI points per year | Claude Opus 5.5: n/a | 2.3.5.3 AECI values and trend |
| METR external testing: AI R&D acceleration due to AI during development |  | estimated overall acceleration | Claude Opus 5.5: ~1.5X (perhaps 30% chance of 2X) | 2.3.6 External testing |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Multi-agent ProgramBench: five-agent team latency speedup | reach score 0.6, vs single agent | latency improvement (x) | Claude Opus 5.5: 2.7x | 8.12.1 Multi-agent ProgramBench |
| Multi-agent DRACO: five-agent team speedup at 0.5x latency budget |  | speedup (x) at matched/greater score | Claude Opus 5.5: roughly 2.8x | 8.12.2 Multi-agent DRACO |
| OSWorld 2.0 price vs performance | reasoning effort levels | partial score / strict pass vs cost per task | Claude Opus 5.5: n/a | 8.13.3 OSWorld 2.0 |
| CursorBench 4.0 cost per task | high effort / medium effort | USD per task (estimated) | Claude Opus 5.5: about $4 (high effort); Claude Opus 5.5: about $3 (medium effort) | 8.8 CursorBench 4.0 |
| Output token savings of xhigh vs max effort | GDPval-AA and AA-Briefcase | % fewer output tokens | Claude Opus 5.5: about 51% (GDPval-AA); Claude Opus 5.5: about 41% (AA-Briefcase) | 8.14.3 GDPval-AA |
