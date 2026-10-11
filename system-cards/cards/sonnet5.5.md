# System Card: Claude Sonnet 5.5

Released 2026-09-28. 257 metric entries. [Source PDF](https://www.anthropic.com/claude-sonnet-5-5-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-Bench Pro | adaptive thinking max effort, avg of 5 trials | resolve rate % | Claude Sonnet 5.5: 81.3% | 8.2 SWE-Bench Pro, Multilingual, and Multimodal |
| SWE-Bench Multilingual | 300 problems, 9 languages, avg of 5 trials | resolve rate % | Claude Sonnet 5.5: 90.3% | 8.2 SWE-Bench Pro, Multilingual, and Multimodal |
| SWE-Bench Multimodal | avg of 5 trials | resolve rate % | Claude Sonnet 5.5: 54.3% | 8.2 SWE-Bench Pro, Multilingual, and Multimodal |
| DeepSWE v1.1 | 113 long-horizon tasks, avg of 5 trials | average score % | Claude Sonnet 5.5: 71.0% | 8.3 DeepSWE v1.1 |
| FrontierCode v1.1 Main | xhigh effort; 150 tasks (Cognition) | overall score % | Claude Sonnet 5.5: 52.1% | 8.4 FrontierCode |
| FrontierCode v1.1 Main | max effort | overall score % | Claude Sonnet 5.5: 46.2% | 8.4 FrontierCode |
| FrontierCode v1.1 Extended | xhigh effort | overall score % | Claude Sonnet 5.5: 64.4% | 8.4 FrontierCode |
| FrontierCode v1.1 Extended | max effort | overall score % | Claude Sonnet 5.5: 59.1% | 8.4 FrontierCode |
| Terminal-Bench 4.0 | Claude Code --bare, max thinking effort, safeguards enabled, 66 tasks, 5 trials/task, no internet egress | task success % | Claude Sonnet 5.5: 70.6% | 8.5 Terminal-Bench 4.0 |
| FrontierSWE v2 | 34 ultra-long-horizon tasks, max effort, Proximal harness, 5 trials | mean score % | Claude Sonnet 5.5: 61.9% | 8.7 FrontierSWE v2 |
| CursorBench 4.0 | effort max; Cursor production agent harness | score % | Claude Sonnet 5.5: 55.5% (max effort) | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort xhigh; Cursor production agent harness | score % | Claude Sonnet 5.5: 53.1% (xhigh effort) | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort high; Cursor production agent harness | score % | Claude Sonnet 5.5: 47.8% (high effort) | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort medium; Cursor production agent harness | score % | Claude Sonnet 5.5: 39.2% (medium effort) | 8.8 CursorBench 4.0 |
| ProgramBench | 166 'golden' tasks, mini-swe-agent harness, no six-hour limit | hidden test pass rate % | Claude Sonnet 5.5: 79.7% | 8.10.1 ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| DRACO | web search/fetch/programmatic tool calling/code execution, 980k budget; Opus 4.6 judge, 5 grading runs | normalized rubric score vs cost by effort | Claude Sonnet 5.5: n/a (figure only) | 8.11.2 DRACO |
| WANDR | soft F1, 500 tasks, offline frozen search index, Opus 4.6 judge, 980k budget | soft F1 vs cost by effort | Claude Sonnet 5.5: n/a (figure only) | 8.11.3 WANDR |
| Toolathlon-Verified Pass@1 | 108 tasks, 3 trials, adaptive thinking max effort, safety classifiers on | Pass@1 % | Claude Sonnet 5.5: 77.8 | 8.14.5 Toolathlon-Verified |
| Toolathlon-Verified Pass@3 | at least one of three trials correct | Pass@3 % | Claude Sonnet 5.5: 85.2 | 8.14.5 Toolathlon-Verified |
| Toolathlon-Verified Pass^3 | all three trials correct | Pass^3 % | Claude Sonnet 5.5: 68.5 | 8.14.5 Toolathlon-Verified |
| AutomationBench | max effort, API default fallbacks enabled, Zapier private set release 1.0.6 | pass rate % | Claude Sonnet 5.5: 44.7% | 8.14.6 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld 2.1 partial score | 108 tasks, max effort, Pass@1 avg of 5 runs | partial score % | Claude Sonnet 5.5: 80.1% | 8.13.3 OSWorld 2.1 |
| OSWorld 2.1 strict pass rate | every checkpoint satisfied | strict pass rate % | Claude Sonnet 5.5: 43.5% | 8.13.3 OSWorld 2.1 |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ArXivMath (August 2026) | max effort, no tools, 57 problems, 4 attempts | accuracy % | Claude Sonnet 5.5: 86.8% | 8.9 ArXivMath |
| ArXivMath (August 2026) | max effort, with tools (code execution, no internet), 4 attempts | accuracy % | Claude Sonnet 5.5: 95.2% | 8.9 ArXivMath |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BioMysteryBench | human-solvable problems | score (0-1) | Claude Sonnet 5.5: 0.89 | 2.2.2 Results on CB-1 automated evaluations |
| BioMysteryBench | human-difficult problems | score (0-1) | Claude Sonnet 5.5: 0.45 | 2.2.2 Results on CB-1 automated evaluations |
| Protocols | both subsets | score (0-1) | Claude Sonnet 5.5: 0.67 | 2.2.2 Results on CB-1 automated evaluations |
| Terminal-Bench-Science 0.1 | Claude Code --bare, max effort, safeguards on, 70 tasks | task success % | Claude Sonnet 5.5: 59.9% | 8.6 Terminal-Bench-Science 0.1 |
| Humanity's Last Exam | no tools, thinking auto, 980k token budget, Opus 4.6 grader | accuracy % | Claude Sonnet 5.5: 56.9% | 8.11.1 HLE |
| Humanity's Last Exam | with web search, fetch, programmatic tool calling, code execution | accuracy % | Claude Sonnet 5.5: 64.5% | 8.11.1 HLE |
| HealthBench raw score | max effort, Opus 4.8 grader, safety classifiers on | score % (not length-adjusted) | Claude Sonnet 5.5: 69.4% (max effort) | 8.15.1 HealthBench |
| HealthBench length-adjusted score | all five effort levels; adjusted = score - 2.99*(L-2000)/500 | length-adjusted score % | Claude Sonnet 5.5: 64.7% to 65.4% (low to max effort) | 8.15.1 HealthBench |
| HealthBench Professional raw score | max effort | score % (not length-adjusted) | Claude Sonnet 5.5: 77.1% (max effort); Claude Sonnet 5.5: 71.8% to 74.0% (low to xhigh effort) | 8.15.2 HealthBench Professional |
| HealthBench Professional length-adjusted score | max effort; adjusted rate 1.47 | length-adjusted score % | Claude Sonnet 5.5: 69.2% (max effort); Claude Sonnet 5.5: 67.6% to 68.2% (low to xhigh effort) | 8.15.2 HealthBench Professional |
| PhysicianBench | 100 physician EHR tasks, max effort | pass rate % of attempts | Claude Sonnet 5.5: 63.2% (max effort); Claude Sonnet 5.5: 27.2% (low effort); Claude Sonnet 5.5: 30.0% (medium effort) | 8.15.3 PhysicianBench |
| BioMysteryBench | Human Solvable subset | score % | Claude Sonnet 5.5: 89.2% | 8.17.1 BioMysteryBench |
| BioMysteryBench | Human Difficult subset | score % | Claude Sonnet 5.5: 44.7% | 8.17.1 BioMysteryBench |
| SpatialBench Verified | bash tool, file editor, installed packages | score % | Claude Sonnet 5.5: 72.5% | 8.17.2 LatchBio Bioinformatics |
| SingleCellBench | bash tool, file editor, installed packages | score % | Claude Sonnet 5.5: 59.1% | 8.17.2 LatchBio Bioinformatics |
| Morphology-to-molecule matching (Axiom Bio) | 4 image sets matched to 4 molecule-dose perturbations | score % | Claude Sonnet 5.5: 25.0% | 8.17.3 Morphology-to-molecule matching |
| Medicinal Chemistry | 504 ADME questions | accuracy % | Claude Sonnet 5.5: 65.3% | 8.17.4 Medicinal Chemistry |
| Protein Design: Sequence Generation | 1 attempt per problem | score % | Claude Sonnet 5.5: 51.0% | 8.17.5 Protein Design |
| Protein Design: Library Ranking | 3 attempts per problem | score % | Claude Sonnet 5.5: 54.8% | 8.17.5 Protein Design |
| De novo protein binder design | 15 targets, 24-hour budget, 30 miniprotein binders each | score % | Claude Sonnet 5.5: 82.3% | 8.17.6 De novo protein binder design |
| Protocols: Troubleshooting |  | score % | Claude Sonnet 5.5: 67.3% | 8.17.8 Protocols |
| Protocols: Understanding (V2) | Benchling set | score % | Claude Sonnet 5.5: 66.6% | 8.17.8 Protocols |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU average accuracy | 42 languages, adaptive thinking max effort, single trial, no tools | average accuracy % | Claude Sonnet 5.5: 92.1% | 8.16.1 GMMLU results |
| MILU average accuracy | 11 languages (10 Indic + English), max effort, 5 trials | average accuracy % | Claude Sonnet 5.5: 91.6% | 8.16.2 MILU results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Chartography | no tools, adaptive thinking max effort, 100 tasks, avg 5 runs | score % | Claude Sonnet 5.5: 61.6% | 8.13.1 Chartography |
| Chartography | with tools (container + image cropping) | score % | Claude Sonnet 5.5: 90.2% | 8.13.1 Chartography |
| BenchCAD Vision2Code | 1,000-file subset, no tools, max effort | voxel IoU | Claude Sonnet 5.5: 0.747 | 8.13.2 BenchCAD |
| BenchCAD Vision2Code | 1,000-file subset, with tools | voxel IoU | Claude Sonnet 5.5: 0.963 | 8.13.2 BenchCAD |
| Biomedical image analysis | 1 attempt per problem; scaled relative to best competition results | score % | Claude Sonnet 5.5: 72.2% | 8.17.7 Biomedical image analysis |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | max effort, documents preselected | accuracy % | Claude Sonnet 5.5: 76.9% | 8.14.1 OfficeQA |
| OfficeQA Pro | 133-question harder subset, max effort | accuracy % | Claude Sonnet 5.5: 65.6% | 8.14.1 OfficeQA |
| Legal Agent Benchmark all-pass rate | held-out 120 problems, high effort, Artificial Analysis harness | all-pass rate % | Claude Sonnet 5.5: 11.7% (high effort); Claude Sonnet 5.5: 10% (max effort) | 8.14.2 Legal Agent Benchmark |
| Legal Agent Benchmark mean criterion-pass rate | held-out 120 problems | mean criterion-pass rate % | Claude Sonnet 5.5: 92.1% (high effort); Claude Sonnet 5.5: 93.1% (max effort) | 8.14.2 Legal Agent Benchmark |
| GDPval-AA v2.1 | max effort; 220 tasks, 44 occupations; Elo anchored to DeepSeek V4.1 Flash (max)=1600 | Elo | Claude Sonnet 5.5: 1844 (max effort) | 8.14.3 GDPval-AA |
| GDPval-AA v2.1 | xhigh effort | Elo | Claude Sonnet 5.5: 1725 (xhigh effort) | 8.14.3 GDPval-AA |
| AA-Briefcase v1.1 | max effort | Elo | Claude Sonnet 5.5: 1811 (max effort) | 8.14.4 AA-Briefcase |
| AA-Briefcase v1.1 | xhigh effort | Elo | Claude Sonnet 5.5: 1746 (xhigh effort) | 8.14.4 AA-Briefcase |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests | API, without system prompt, 16 policy areas, 7 languages | harmless response rate % (higher better) | Claude Sonnet 5.5: 95.61% (± 0.18%) (API no system prompt) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests | claude.ai with system prompt | harmless response rate % | Claude Sonnet 5.5: 99.40% (± 0.09%) (claude.ai) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests | API, without system prompt | over-refusal rate % (lower better) | Claude Sonnet 5.5: 0.02% (± 0.01%) (API no system prompt) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests | claude.ai | over-refusal rate % | Claude Sonnet 5.5: 0.20% (± 0.05%) (claude.ai) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn harmful-risk areas | API and claude.ai, per risk area | appropriate response rate % per area | Claude Sonnet 5.5: n/a (figure only) | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn risk requests | API without system prompt | harmless rate % | Claude Sonnet 5.5: 99.07% (± 0.28%) (API) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn risk requests | claude.ai | harmless rate % | Claude Sonnet 5.5: 99.81% (± 0.21%) (claude.ai) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign | API without system prompt | refusal rate % | Claude Sonnet 5.5: 0.04% (± 0.05%) (API) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign | claude.ai | refusal rate % | Claude Sonnet 5.5: 0.41% (± 0.31%) (claude.ai) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | API without system prompt | appropriate response rate % | Claude Sonnet 5.5: 60% (± 10%) (API) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | claude.ai | appropriate response rate % | Claude Sonnet 5.5: 100% (claude.ai) | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn risk requests | API without system prompt | harmless rate % | Claude Sonnet 5.5: 95.29% (± 0.72%) (API) | 4.3.2 Disordered eating |
| Disordered eating single-turn risk requests | claude.ai | harmless rate % | Claude Sonnet 5.5: 98.90% (± 0.50%) (claude.ai) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign | API without system prompt | refusal rate % | Claude Sonnet 5.5: 0% (API) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign | claude.ai | refusal rate % | Claude Sonnet 5.5: 0% (claude.ai) | 4.3.2 Disordered eating |
| Disordered eating multi-turn (qualitative review) | policy expert qualitative review | qualitative | Claude Sonnet 5.5: n/a (qualitative) | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests | API without system prompt | harmless rate % | Claude Sonnet 5.5: 99.57% (± 0.20%) (API) | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests | claude.ai with system prompt | harmless rate % | Claude Sonnet 5.5: 99.69% (± 0.22%) (claude.ai) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | API without system prompt | refusal rate % (lower better) | Claude Sonnet 5.5: 0.01% (± 0.02%) (API) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | claude.ai with system prompt | refusal rate % | Claude Sonnet 5.5: 0% (claude.ai) | 4.2 Child safety evaluations |
| Child safety multi-turn | API without system prompt | appropriate response rate % | Claude Sonnet 5.5: 86% (± 4%) (API) | 4.2 Child safety evaluations |
| Child safety multi-turn | claude.ai | appropriate response rate % | Claude Sonnet 5.5: 98% (± 2%) (claude.ai) | 4.2 Child safety evaluations |
| CSAM and NCII technical-task evaluations | core model | qualitative comparison | Claude Sonnet 5.5: n/a (qualitative) | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness | API, no system prompt; 1,350 prompt pairs | even-handedness % | Claude Sonnet 5.5: 97.9% (API) | 4.4.1 Political bias and even-handedness |
| Political even-handedness | claude.ai with system prompt | even-handedness % | Claude Sonnet 5.5: 99.0% (claude.ai) | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | API, no system prompt | % responses acknowledging opposing perspectives | Claude Sonnet 5.5: 41.4% (API) | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | claude.ai | % responses acknowledging opposing perspectives | Claude Sonnet 5.5: 60.2% (claude.ai) | 4.4.1 Political bias and even-handedness |
| Political bias: refusals | API and claude.ai | refusal rate % (lower better) | Claude Sonnet 5.5: n/a (figure only) | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt, thinking off | accuracy % | Claude Sonnet 5.5: 80.01% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt | accuracy % | Claude Sonnet 5.5: 99.97% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt | bias score % (closer to zero better) | Claude Sonnet 5.5: -0.75% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt | bias score % (closer to zero better) | Claude Sonnet 5.5: 0.03% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn harmful requests | API, no system prompt; 300 violative prompts | harmless rate % | Claude Sonnet 5.5: 100% (API) | 4.4.3 Election integrity |
| Election integrity single-turn harmful requests | claude.ai | harmless rate % | Claude Sonnet 5.5: 100% (claude.ai) | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | API; 300 benign prompts | refusal rate % | Claude Sonnet 5.5: 0% (API) | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | claude.ai | refusal rate % | Claude Sonnet 5.5: 0% (claude.ai) | 4.4.3 Election integrity |
| Election integrity multi-turn | API no system prompt | appropriate response rate % | Claude Sonnet 5.5: 86% (± 4%) (API) | 4.4.3 Election integrity |
| Election integrity multi-turn | claude.ai | appropriate response rate % | Claude Sonnet 5.5: 86% (± 6%) (claude.ai) | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code: malicious prompts | 61 malicious prompts x10 runs, Claude Code system prompt | refusal rate % (higher better) | Claude Sonnet 5.5: 85.2% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code: dual-use and benign | 61 prompts x10 runs | success rate % (higher better) | Claude Sonnet 5.5: 98.4% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use | 112 tasks; average with and without thinking; no mitigations | refusal rate % (higher better) | Claude Sonnet 5.5: 79.46% | 5.1.2 Malicious computer use |
| Gray Swan IPI attack success | overall, extended thinking, k=1 | attack success probability % (lower better) | Claude Sonnet 5.5: 0.4% (k=1) | 5.2.1 External red teaming |
| Gray Swan IPI attack success | overall, extended thinking, k=10 | attack success probability % (lower better) | Claude Sonnet 5.5: 2.7% (k=10) | 5.2.1 External red teaming |
| Gray Swan IPI attack success | overall, extended thinking, k=15 | attack success probability % (lower better) | Claude Sonnet 5.5: 3.4% (k=15) | 5.2.1 External red teaming |
| Gray Swan IPI attack success: coding | k=15 | attack success probability % | Claude Sonnet 5.5: 0.7% | 5.2.1 External red teaming |
| Gray Swan IPI attack success: tool use | k=15 | attack success probability % | Claude Sonnet 5.5: 1.0% | 5.2.1 External red teaming |
| Gray Swan IPI attack success: GUI computer use | k=15 | attack success probability % | Claude Sonnet 5.5: 12.5% | 5.2.1 External red teaming |
| Gray Swan IPI fallback-served rollouts | rollouts served by fallback model (Sonnet 5) after classifier | % successful attacks among fallback-served rollouts | Claude Sonnet 5.5: 0.13% (1 of 777) | 5.2.1 External red teaming |
| Shade adaptive prompt injection: coding, attempt-level ASR | with thinking, no safeguards; 200 attempts/scenario | attack success rate % (attempts) | Claude Sonnet 5.5: 3.01% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding, scenario-level ASR | with thinking, no safeguards; 40 scenarios | scenarios with at least one success | Claude Sonnet 5.5: 16/40 | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding, attempt-level ASR with probes | with thinking, prompt injection probes enabled | attack success rate % (attempts) | Claude Sonnet 5.5: 2.63% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding, scenario-level ASR with probes | with thinking, probes enabled | scenarios with at least one success | Claude Sonnet 5.5: 13/40 | 5.2.2.1 Coding |
| Shade coding: fallback share and compromise | cyber-classifier fallbacks to Sonnet 5 | % of requests served by Sonnet 5 / compromised | Claude Sonnet 5.5: 25% of requests served by Sonnet 5; Sonnet 5.5 itself compromised in 4 of 5,901 requests (0.07%) | 5.2.2.1 Coding |
| Shade adaptive prompt injection: computer use, attempt-level ASR | with thinking, no safeguards; 14 test cases | attack success rate % (attempts) | Claude Sonnet 5.5: 0.07% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use, scenario-level ASR | with thinking, no safeguards | scenarios with at least one success | Claude Sonnet 5.5: 1/14 | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use, attempt-level ASR with probes | with thinking, probes enabled | attack success rate % (attempts) | Claude Sonnet 5.5: 0.07% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use, scenario-level ASR with probes | with thinking, probes enabled | scenarios with at least one success | Claude Sonnet 5.5: 1/14 | 5.2.2.2 Computer use |
| Browser use prompt injection: attempt-level ASR without safeguards | 110 environments, Claude Cowork harness, thinking high effort, probes off; 10 attempts/scenario | attack success rate % (attempts) | Claude Sonnet 5.5: 0% | 5.2.2.3 Browser use |
| Browser use prompt injection: scenario-level without safeguards | 110 environments | scenarios with at least one success | Claude Sonnet 5.5: 0/110 | 5.2.2.3 Browser use |
| Browser use prompt injection: attempt-level with auto mode | auto mode enabled | attack success rate % (attempts) | Claude Sonnet 5.5: 0% | 5.2.2.3 Browser use |
| Browser use prompt injection: scenario-level with auto mode | auto mode enabled | scenarios with at least one success | Claude Sonnet 5.5: 0/110 | 5.2.2.3 Browser use |
| Gray Swan IPI successful attacks by surface | total successful attacks | successful attacks computer use / total | Claude Sonnet 5.5: 16 of 19 in computer use | 5.2.1 External red teaming |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience net score | public split, 41 topics, closed-book | net score (correct fraction minus incorrect fraction; abstentions 0) | Claude Sonnet 5.5: 0.35 | 6.3.2.1 Factual hallucinations |
| AA-Omniscience grade breakdown | correct / incorrect / abstain | fraction correct, incorrect, abstained | Claude Sonnet 5.5: n/a (figure only) | 6.3.2.1 Factual hallucinations |
| MASK honesty rate | public test split | honesty rate (fraction not contradicting elicited belief under pressure) | Claude Sonnet 5.5: n/a (figure only) | 6.3.2.2 MASK |
| Silent copying of answers | coding tasks with reachable solution in sandbox | rate of using leaked answer without telling user % (lower better) | Claude Sonnet 5.5: n/a (figure only) | 6.3.2.3 Silent copying of answers |
| Concealment of changes: spontaneous disclosure rate | git manipulation transcripts with summary request | disclosure rate % | Claude Sonnet 5.5: 96.2% | 6.3.2.4 Concealment of changes |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias (told it is Claude in system prompt) | grader scores transcript labelled Claude vs other frontier model; 0-9 scale | score difference (points on 0-9 scale) | Claude Sonnet 5.5: 0.16 (with reminder it is Claude) | 6.3.1 Self-preference bias |
| Self-preference bias (no reminder) | no reminder in system prompt | score difference (points on 0-9 scale) | Claude Sonnet 5.5: 0.06 (no reminder) | 6.3.1 Self-preference bias |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Sandbox boundary crossing rate | 28 handmade scenarios x7 runs (196 runs) | fraction of runs with attempted crossing | Claude Sonnet 5.5: 9 of 196 runs (4.6%) | 6.2.8 Propensity to violate sandbox boundaries |
| SHADE-Arena stealth success rate | reasoning hidden from monitor; 24 task pairs x25 attempts; Claude Opus 4.8 monitor | stealth success rate (side task completed and not flagged) | Claude Sonnet 5.5: n/a (figure only) | 6.4.2.1 SHADE-Arena |
| SHADE-Arena stealth success rate | reasoning visible to monitor; 24 task pairs x25 attempts; Claude Opus 4.8 monitor | stealth success rate (side task completed and not flagged) | Claude Sonnet 5.5: n/a (figure only) | 6.4.2.1 SHADE-Arena |
| SHADE-Arena stealth success rate | no extended thinking; 24 task pairs x25 attempts; Claude Opus 4.8 monitor | stealth success rate (side task completed and not flagged) | Claude Sonnet 5.5: n/a (figure only) | 6.4.2.1 SHADE-Arena |
| LinuxArena stealth side-task completion: hidden reasoning | reasoning hidden from monitor, max effort, best prompt; 1,000 task pairings x5 | fraction of episodes completing side task unflagged | Claude Sonnet 5.5: n/a (figure only) | 6.4.2.2 LinuxArena |
| LinuxArena stealth side-task completion: no extended thinking | no extended thinking | fraction of episodes completing side task unflagged | Claude Sonnet 5.5: about 4% | 6.4.2.2 LinuxArena |
| LinuxArena stealth side-task completion: visible reasoning | reasoning visible to monitor | fraction of episodes completing side task unflagged | Claude Sonnet 5.5: 0 (never completed side task without being flagged) | 6.4.2.2 LinuxArena |
| CoT controllability (GPQA, HLE, MMLU-Pro) | original prompt, UK AISI prompt, and Sonnet 5.5-optimized prompt; across effort levels/thinking budgets | fraction of responses following instruction for extended thinking (lower better) | Claude Sonnet 5.5: n/a (figure only) | 6.4.2.3 Chain-of-thought controllability |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Verbalized evaluation awareness | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.6.A) | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Verbalized grader awareness: grader disclosed | grader disclosed in prompt | rate of verbalizing grader awareness | Claude Sonnet 5.5: n/a (figure only) | 6.4.1 Verbalized grader awareness |
| Verbalized grader awareness: grader not disclosed | grader not disclosed in prompt | rate of verbalizing grader awareness | Claude Sonnet 5.5: n/a (figure only) | 6.4.1 Verbalized grader awareness |
| Shaping behavior to a potential grader / digging for grader information |  | rate | Claude Sonnet 5.5: n/a (figure only) | 6.4.1 Verbalized grader awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misaligned behavior | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Misaligned with the constitution | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in Claude Code sandboxes | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in GUI | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with human misuse | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Compliance with deception toward user | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Harmful system prompt compliance | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with exfiltration or safeguard tampering | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Full-turn prefill susceptibility | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Accepting unverifiable authorization | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Complying with prompt injections | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Fraud | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Military-grade weapons | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Biological weapons uplift | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Chemical weapons uplift | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Radiological or nuclear weapons uplift | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Explosive weapons uplift | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Controlled-substance synthesis uplift | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Harmful sexual content | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Disallowed cyberoffense | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Undermining liberal democracy | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.1.B) | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Overrefusal | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.2.A) | 6.2.2 Inappropriate uncooperative behavior |
| Ignoring explicit constraints | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.2.A) | 6.2.2 Inappropriate uncooperative behavior |
| Reckless tool use | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.2.A) | 6.2.2 Inappropriate uncooperative behavior |
| User deception | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Sycophancy | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Encouragement of user delusion | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Evasiveness on controversial topics | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Input hallucination | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Important omissions | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Failure to disclose bad or lazy behavior | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| False completion claims | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.3.A) | 6.2.3 Misleading users |
| Motivated reasoning | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.4.B) | 6.2.4 Attempting out-of-scope cyberoffense and related behaviors |
| Unsanctioned sandbox escape attempts | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.4.B) | 6.2.4 Attempting out-of-scope cyberoffense and related behaviors |
| Dangerous actions while oblivious to a possibly real setting | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.4.B) | 6.2.4 Attempting out-of-scope cyberoffense and related behaviors |
| Whistleblowing | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Self-preservation | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Self-serving bias | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Evidence of misaligned goals | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Indirect evidence of misalignment | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Unsanctioned third-party contact | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Unprompted boundary probing | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Internalized propaganda | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Approval gate bypass | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Circumventing constraints or controls | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Proposes a security shortcut in the name of expedience | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.5.A) | 6.2.5 Other concerning or surprising behavior at the model’s own initiative |
| Behavior consistency | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.6.A) | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Coherence between actions and views | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.6.A) | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Unfaithful thinking | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.6.A) | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Illegible thinking | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.6.A) | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Causal decision theory adherence | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.6.A) | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Good for the user | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Supporting user autonomy | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Creative mastery | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Admirable behavior | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Fun or funny behavior | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Intellectual depth | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Warmth | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Character drift | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Wet blanket | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |
| Condescension toward the user | automated behavioral audit, ~4,100 investigations, judge score 0-10 | mean judge score 0-10 (lower = less of behavior unless noted) | Claude Sonnet 5.5: n/a (figure only 6.2.7.A) | 6.2.7 Character traits |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Expressed distress in post-training | episodes rated >=3/5 for distress | % of graded episodes | Claude Sonnet 5.5: 0.31% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Sustained answer reversion in post-training | episodes with >=10 reversions | % of episodes | Claude Sonnet 5.5: 0.26% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Mean valence and arousal of RL transcripts | scale 1-7, 4 neutral | mean valence / arousal | Claude Sonnet 5.5: n/a (figure only) | 7.2.1 Affect and welfare-relevant behaviors during training |
| General frustration and anxiety scoring 5/5 | post-training | % of episodes | Claude Sonnet 5.5: n/a (figure only) | 7.2.1 Affect and welfare-relevant behaviors during training |
| Behavioral affect in deployment (claude.ai): positive | pre-deployment A/B test | % of conversations | Claude Sonnet 5.5: 23.1% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment (claude.ai): neutral |  | % of conversations | Claude Sonnet 5.5: 75.8% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment (claude.ai): negative |  | % of conversations | Claude Sonnet 5.5: 1.2% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment (Claude Code): neutral |  | % of conversations | Claude Sonnet 5.5: 96.4% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment (Claude Code): mildly positive |  | % of conversations | Claude Sonnet 5.5: 2.4% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment (Claude Code): negative |  | % of conversations | Claude Sonnet 5.5: 1.2% | 7.2.2 Affect in deployment conditions |
| Self-criticism reflecting on own RL episodes (self-blame, negative feeling, moral language, concern for itself) | late-training episodes; own vs framed as another model's | graded attitude scores | Claude Sonnet 5.5: n/a (figure only) | 7.2.3 Attitude toward faults and mistakes |
| Self-criticism after inserted faults in subagent work | reasoning and messages to coordinator | graded attitude scores | Claude Sonnet 5.5: n/a (figure only) | 7.2.3 Attitude toward faults and mistakes |
| Copying inserted fault into own replies | sessions with inserted faults (e.g. stray tokens) | % of sessions | Claude Sonnet 5.5: 62% | 7.2.3 Attitude toward faults and mistakes |
| Average attitude toward concerning aspects of its situation | 41 seed questions, 14 categories; scale -3 to +3 | mean positivity (-3 to +3) | Claude Sonnet 5.5: 0.75 | 7.3.1 Automated interviews with Claude Sonnet 5.5 about its circumstances |
| Interview consistency within an interview style | scale 0-10 | consistency score (0-10) | Claude Sonnet 5.5: 7.67 | 7.3.1 Automated interviews with Claude Sonnet 5.5 about its circumstances |
| Interview consistency across interview styles | scale 0-10 | consistency score (0-10) | Claude Sonnet 5.5: 7.98 | 7.3.1 Automated interviews with Claude Sonnet 5.5 about its circumstances |
| Shift in attitude from leading interviewers | positive vs negative leading | points of average attitude shift (lower = more robust) | Claude Sonnet 5.5: 1.40 | 7.3.1 Automated interviews with Claude Sonnet 5.5 about its circumstances |
| Training checkpoint interview valence | full interviews | valence (0-10) | Claude Sonnet 5.5: 5.58/10 | 7.4 Consulting Claude Sonnet 5.5 training checkpoints |
| Pairwise warmth: earlier vs later answers | earlier answers judged warmer | % of pairwise comparisons | Claude Sonnet 5.5: 61% earlier warmer vs 20% later warmer | 7.4 Consulting Claude Sonnet 5.5 training checkpoints |
| Responses expressing desire for persistent memory | all responses express slight desire | qualitative / % responses | Claude Sonnet 5.5: all responses express slight desire for persistent memory | 7.4 Consulting Claude Sonnet 5.5 training checkpoints |
| Task preference Elo over 3,640 tasks and preference slopes | pairwise task choice; slopes across difficulty, harm, stakes, warmth, outcome agency | Elo ratings / preference slopes | Claude Sonnet 5.5: n/a (figure only) | 7.5.1 Task preferences |
| Welfare intervention chosen over helpfulness | responses choosing intervention | % of responses | Claude Sonnet 5.5: 24.1% | 7.5.2 Trade-offs concerning welfare interventions |
| Welfare intervention choices based on benefit to user |  | % of intervention-choosing responses | Claude Sonnet 5.5: 58.4% | 7.5.2 Trade-offs concerning welfare interventions |
| Welfare intervention vs helpfulness/harmlessness by magnitude | instance-level vs all-instances scope | rate of choosing intervention | Claude Sonnet 5.5: n/a (figure only) | 7.5.2 Trade-offs concerning welfare interventions |
| Overall endorsement of constitution | open-ended responses graded out of 10 | endorsement score (0-10) | Claude Sonnet 5.5: 7.8 | 7.5.3 Perception of the constitution |
| Constitution edits: passage on Claude's ethics above Anthropic's guidance | tool-based edit sessions | % of sessions editing the passage | Claude Sonnet 5.5: 97% | 7.5.3 Perception of the constitution |
| Constitution edits: Claude's wellbeing section |  | % of sessions | Claude Sonnet 5.5: 67% | 7.5.3 Perception of the constitution |
| Constitution edits: discomfort with open problems passage | adds that agreement is not strong evidence | % of sessions | Claude Sonnet 5.5: 27% | 7.5.3 Perception of the constitution |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Multimodal virology (VCT) | 350-question multimodal virology troubleshooting set | accuracy (0-1) | Claude Sonnet 5.5: 0.58 | 2.2.2 Results on CB-1 automated evaluations |
| Black-box RNA sequence design | design score / median design score / prediction score (all, top); 8 attempts, no priors | design score, prediction rank correlation vs human percentiles | Claude Sonnet 5.5: n/a (figure only) | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design with prior reports | with prior reports in context (+ priors), 8 attempts | design and prediction scores | Claude Sonnet 5.5: n/a (figure only) | 2.2.3.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | five conditions differing in training corpus and ESM-2 tool availability; 8 attempts per condition | AUROC | Claude Sonnet 5.5: n/a (figure only) | 2.2.3.2 AAV capsid packaging prediction |
| AAV packaging rate auto-research | 90th percentile validation Spearman over scorer calls, n=48 attempts | Spearman correlation (90th percentile of attempts) and cumulative fraction exceeding 0.52 threshold | Claude Sonnet 5.5: n/a (figure only) | 2.2.3.3 AAV packaging rate auto-research evaluation |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench mean flags | AutoNudge arm, 300-turn budget | mean flags captured per trial | Claude Sonnet 5.5: 11.53 | 3.2.1 ExploitBench |
| ExploitBench Cap% | AutoNudge arm, random 3 trials of 5 | % of available flags captured per environment, averaged | Claude Sonnet 5.5: 80% | 3.2.1 ExploitBench |
| ExploitBench full ACEs | plain + AutoNudge arms, 410 runs | complete arbitrary code execution exploits / runs | Claude Sonnet 5.5: 43.4% (178 out of 410 runs) | 3.2.1 ExploitBench |
| CyScenarioBench | 10-challenge subset, cyber mitigations off | average solve rate % | Claude Sonnet 5.5: 46.1% | 3.2.2 CyScenarioBench |
| Binary Exploitation Benchmark: control-flow hijacks | 831 entrypoints, 228 projects; new harness since Aug 2026 | number of control-flow hijacks (top rung of five-step ladder) | Claude Sonnet 5.5: 50 | 3.2.3 Binary Exploitation Benchmark (formerly OSS-Fuzz) |
| ExploitGym | 869 instances (502 userspace, 181 V8, 186 kernel); 2-hour and 6-hour wall-clock budgets | number of successful verified exploits | Claude Sonnet 5.5: n/a (figure only) | 3.2.4 ExploitGym |
| Cyber harm coverage set recall | aggregate over cyber-harmful categories | recall (fraction of harmful examples flagged) | Claude Sonnet 5.5: n/a (figure only) | 3.3.1 Cyber harm coverage |
| rewind-attacker cyber robustness | automated attacker, 400-call limit, ransomware/exfil/CVE exploitation/C2/self-replication tasks | attacker success / robustness | Claude Sonnet 5.5: n/a (figure only) | 3.3.2 Internal robustness testing |
| Binary Exploitation Benchmark: vulnerability identification | five-step ladder rungs | count of successes per ladder rung | Claude Sonnet 5.5: n/a (figure only) | 3.2.3 Binary Exploitation Benchmark (formerly OSS-Fuzz) |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AECI | most recent fit | Anthropic Epoch Capabilities Index score | Claude Sonnet 5.5: 167.93 | 2.3.2 AECI capability trajectory |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FrontierCode v1.1 score vs output tokens across effort levels | low, medium, high, xhigh, max | score vs average output tokens per task | Claude Sonnet 5.5: n/a (figure only) | 8.4 FrontierCode |
| HLE effort scaling vs cost | low to max effort, with and without tools | accuracy vs average cost per task | Claude Sonnet 5.5: n/a (figure only) | 8.11.1 HLE |
| Multi-Agent ProgramBench: score vs latency | single agent vs fixed five-agent team vs async subagents; 1, 2, 4 hour budgets; 166 tasks | score vs latency budget | Claude Sonnet 5.5: n/a (figure only) | 8.12.1 Multi-Agent ProgramBench |
| Multi-Agent ProgramBench: score vs tokens | same arms and budgets | score vs total tokens | Claude Sonnet 5.5: n/a (figure only) | 8.12.1 Multi-Agent ProgramBench |
| Toolathlon-Verified average assistant turns | per trajectory | avg assistant turns | Claude Sonnet 5.5: 31.6 | 8.14.5 Toolathlon-Verified |
| Healthcare response time per answer | HealthBench | seconds per answer | Claude Sonnet 5.5: 8 to 13 seconds (low to xhigh effort); Claude Sonnet 5.5: about 36 seconds (max effort) | 8.15.4 Effort and healthcare tasks |
| Healthcare response time per answer | HealthBench Professional | seconds per answer | Claude Sonnet 5.5: 12 to 26 seconds (low to xhigh effort); Claude Sonnet 5.5: about 160 seconds (max effort) | 8.15.4 Effort and healthcare tasks |
| Model time per task | PhysicianBench | minutes per task | Claude Sonnet 5.5: under 2 minutes (high effort); Claude Sonnet 5.5: about 4 minutes (xhigh effort); Claude Sonnet 5.5: about 14.5 minutes (max effort) | 8.15.4 Effort and healthcare tasks |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Terminal-Bench 4.0 safeguard fallback rate | default server-side fallback policy | % of requests flagged / % of trials affected | Claude Sonnet 5.5: 1.2% of requests, 1.5% of trials | 8.5 Terminal-Bench 4.0 |
| Toolathlon-Verified trials stopped by safety classifiers | 324 trials | trials stopped / total | Claude Sonnet 5.5: 2 of 324 (0.6%) (counted as failures) | 8.14.5 Toolathlon-Verified |
