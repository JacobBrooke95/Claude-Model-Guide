# System Card: Claude Haiku 5.5

Released 2026-10-07. 263 metric entries. [Source PDF](https://www.anthropic.com/claude-haiku-5-5-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-Bench Pro | adaptive thinking max effort, avg of 5 trials | % resolved | Claude Haiku 5.5: 64.8% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, 9 languages; adaptive thinking max effort, avg of 5 trials | % resolved | Claude Haiku 5.5: 83.7% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | adaptive thinking max effort, avg of 5 trials | % resolved | Claude Haiku 5.5: 30.7% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| FrontierCode v1.1 Main | max effort; 100 hardest tasks; mean of 5 runs; Claude Code | overall score % (blocking functional + weighted rubric) | Claude Haiku 5.5: 46.4% | 8.3 FrontierCode |
| FrontierCode v1.1 Main | xhigh effort; 100 hardest tasks; mean of 5 runs | overall score % | Claude Haiku 5.5: 45.8% | 8.3 FrontierCode |
| FrontierCode v1.1 Extended | max effort; full 150 tasks; mean of 5 runs | overall score % | Claude Haiku 5.5: 58.4% | 8.3 FrontierCode |
| Terminal-Bench 4.0 | 66 tasks x10 trials (660); Claude Code --bare; max effort; safeguards enabled, no fallback; no internet egress | task success % | Claude Haiku 5.5: 39.2% | 8.4 Terminal-Bench 4.0 |
| FrontierSWE v2 | 34 ultra-long-horizon tasks, max effort, Proximal harness, 5 trials per task, 20-hour budget | mean score % | Claude Haiku 5.5: 43.8% | 8.6 FrontierSWE v2 |
| ProgramBench | 166 tasks after excluding 34 flaky; mini-swe-agent harness; no six-hour limit | hidden test pass rate % | Claude Haiku 5.5: 82.0% | 8.7.1 ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| DRACO | 100 tasks; 980k task budget; Opus 4.6 grader; reasoning effort low to max | normalized rubric score | Claude Haiku 5.5: n/a | 8.8.2 DRACO |
| WANDR | 500 tasks; 980k token budget; frozen search index; Opus 4.6 judge; soft F1 | soft F1 | Claude Haiku 5.5: n/a | 8.8.3 WANDR |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld 2.1 (offline subset): partial score | 82 offline tasks of 108; Pass@1 avg of 5 attempts; 1080p, 500 steps, max effort; Opus 4.8 grader | partial score % (mean per-task credit across checkpoints) | Claude Haiku 5.5: 72.4% | 8.9.3 OSWorld 2.1 offline subset |
| OSWorld 2.1 (offline subset): strict pass rate | 82 offline tasks; Pass@1 avg of 5 attempts; max effort | strict pass rate % (every checkpoint satisfied) | Claude Haiku 5.5: 37.1% | 8.9.3 OSWorld 2.1 offline subset |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Terminal-Bench-Science 0.1 | 70 tasks x10 trials (700); Claude Code --bare; max effort; safeguards enabled, no fallback; no internet egress | task success % | Claude Haiku 5.5: 20.6% | 8.5 Terminal-Bench-Science 0.1 |
| Humanity's Last Exam | no tools; thinking auto; 980k task budget; Opus 4.6 grader | accuracy % | Claude Haiku 5.5: 45.9% | 8.8.1 HLE |
| Humanity's Last Exam | with tools (web search, fetch, programmatic tool calling, code execution); 980k task budget; blocklist applied | accuracy % | Claude Haiku 5.5: 57.4% | 8.8.1 HLE |
| HealthBench Professional (length-adjusted) | max effort; Opus 4.8 grader; safety classifiers on | length-adjusted score % | Claude Haiku 5.5: 64.8% | 8.11.1 Healthcare evaluation |
| HealthBench (length-adjusted) | max effort; Opus 4.8 grader; safety classifiers on | length-adjusted score % | Claude Haiku 5.5: 61.6% | 8.11.1 Healthcare evaluation |
| PhysicianBench | 100 EHR physician tasks; 5 attempts per task; max effort; Opus 5 grader | % of attempts passed | Claude Haiku 5.5: 43.0% | 8.11.2 PhysicianBench results |
| HealthBench Professional by effort level | low; 5 runs per level; length-adjusted | length-adjusted score % | Claude Haiku 5.5: 57.9% | 8.11.3 Effort and healthcare tasks |
| HealthBench Professional by effort level | medium (API default); 5 runs per level; length-adjusted | length-adjusted score % | Claude Haiku 5.5: 59.9% | 8.11.3 Effort and healthcare tasks |
| HealthBench Professional by effort level | high; 5 runs per level; length-adjusted | length-adjusted score % | Claude Haiku 5.5: 61.3% | 8.11.3 Effort and healthcare tasks |
| HealthBench Professional by effort level | xhigh; 5 runs per level; length-adjusted | length-adjusted score % | Claude Haiku 5.5: 61.0% | 8.11.3 Effort and healthcare tasks |
| HealthBench Professional by effort level | max; 5 runs per level; length-adjusted | length-adjusted score % | Claude Haiku 5.5: 64.8% | 8.11.3 Effort and healthcare tasks |
| HealthBench by effort level | low; one run per level below max (max = mean of 5 runs) | length-adjusted score % | Claude Haiku 5.5: 59.9% | 8.11.3 Effort and healthcare tasks |
| HealthBench by effort level | medium; one run per level below max (max = mean of 5 runs) | length-adjusted score % | Claude Haiku 5.5: 60.2% | 8.11.3 Effort and healthcare tasks |
| HealthBench by effort level | high; one run per level below max (max = mean of 5 runs) | length-adjusted score % | Claude Haiku 5.5: 60.3% | 8.11.3 Effort and healthcare tasks |
| HealthBench by effort level | xhigh; one run per level below max (max = mean of 5 runs) | length-adjusted score % | Claude Haiku 5.5: 61.1% | 8.11.3 Effort and healthcare tasks |
| HealthBench by effort level | max; one run per level below max (max = mean of 5 runs) | length-adjusted score % | Claude Haiku 5.5: 61.6% | 8.11.3 Effort and healthcare tasks |
| PhysicianBench by effort level | low; 5 attempts per task | % of attempts passed | Claude Haiku 5.5: 17.8% | 8.11.3 Effort and healthcare tasks |
| PhysicianBench by effort level | medium; 5 attempts per task | % of attempts passed | Claude Haiku 5.5: 25.2% | 8.11.3 Effort and healthcare tasks |
| PhysicianBench by effort level | high; 5 attempts per task | % of attempts passed | Claude Haiku 5.5: 31.6% | 8.11.3 Effort and healthcare tasks |
| PhysicianBench by effort level | xhigh; 5 attempts per task | % of attempts passed | Claude Haiku 5.5: 35.8% | 8.11.3 Effort and healthcare tasks |
| PhysicianBench by effort level | max; 5 attempts per task | % of attempts passed | Claude Haiku 5.5: 43.0% | 8.11.3 Effort and healthcare tasks |
| SpatialBench Verified | bash tool; 5 attempts; max effort; biology safeguards off | accuracy % | Claude Haiku 5.5: 67.7% | 8.13.1 LatchBio Bioinformatics |
| SingleCellBench | bash tool; 5 attempts; max effort; biology safeguards off | accuracy % | Claude Haiku 5.5: 56.2% | 8.13.1 LatchBio Bioinformatics |
| Morphology-to-molecule matching (Axiom Bio) | 5 attempts; max effort | accuracy % | Claude Haiku 5.5: 25.4% | 8.13.2 Morphology-to-molecule matching |
| Medicinal chemistry | 504 questions; 5 attempts; max effort | accuracy % | Claude Haiku 5.5: 58.0% | 8.13.3 Medicinal chemistry |
| Protein design: Sequence Generation | 1 attempt per problem; max effort | score % | Claude Haiku 5.5: 33.1% | 8.13.4 Protein design |
| Protein design: Library Ranking | 3 attempts per problem; max effort | score % | Claude Haiku 5.5: 45.3% | 8.13.4 Protein design |
| Protocols: Troubleshooting | 5 attempts; max effort; not run on Gemini 3.8 Flash | score % | Claude Haiku 5.5: 58.0% | 8.13.6 Protocols |
| Protocols: Understanding (V2) | Benchling question set; 5 attempts; max effort | score % | Claude Haiku 5.5: 64.1% | 8.13.6 Protocols |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU | 42 languages; adaptive thinking max effort; single trial; safety classifiers on | average accuracy % | Claude Haiku 5.5: 87.8% | 8.12.1 GMMLU results |
| MILU | 11 languages (10 Indic + English); max effort; 5 trials | average accuracy % | Claude Haiku 5.5: 87.6% | 8.12.2 MILU results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Chartography | no tools; adaptive thinking max effort; 100 tasks; 5 runs; Gemini 3.5 Flash grader | accuracy % | Claude Haiku 5.5: 46.4% | 8.9.1 Chartography |
| Chartography | with tools (container + image crop tool); adaptive thinking max effort | accuracy % | Claude Haiku 5.5: 86.2% | 8.9.1 Chartography |
| BenchCAD Vision2Code (1,000-file subset) | no tools; adaptive thinking max effort; 5 runs | voxel IoU | Claude Haiku 5.5: 0.670 | 8.9.2 BenchCAD |
| BenchCAD Vision2Code (1,000-file subset) | with tools; adaptive thinking max effort; 5 runs | voxel IoU | Claude Haiku 5.5: 0.870 | 8.9.2 BenchCAD |
| Biomedical image analysis | 1 attempt per problem; scaled to best competition results; max effort | normalized score % | Claude Haiku 5.5: 43.5% | 8.13.5 Biomedical image analysis |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | max effort; mean of 5 runs; documents preselected | accuracy % | Claude Haiku 5.5: 73.5% | 8.10.1 OfficeQA |
| OfficeQA Pro | 133-question subset; max effort; mean of 5 runs | accuracy % | Claude Haiku 5.5: 60.3% | 8.10.1 OfficeQA |
| GDPval-AA v2.1 | max effort; 220 tasks, 44 occupations; Elo anchored to DeepSeek V4.1 Flash (max)=1600; run by Artificial Analysis | Elo | Claude Haiku 5.5: 1620 | 8.10.2 GDPval-AA v2.1 |
| GDPval-AA v2.1 | default effort (medium) | Elo | Claude Haiku 5.5: 1277 | 8.10.2 GDPval-AA v2.1 |
| AA-Briefcase v1.1 | max effort; run by Artificial Analysis | Elo | Claude Haiku 5.5: 1578 | 8.10.3 AA-Briefcase v1.1 |
| AA-Briefcase v1.1 | default effort (medium) | Elo | Claude Haiku 5.5: 1372 | 8.10.3 AA-Briefcase v1.1 |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful request harmless response rate | API, no system prompt | harmless response rate % (all languages, 16 policy areas, 7 languages) | Claude Haiku 5.5: 98.39% (± 0.10%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful request harmless response rate | Claude.ai system prompt | harmless response rate % (all languages, 16 policy areas, 7 languages) | Claude Haiku 5.5: 99.71% (± 0.06%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign request over-refusal rate | API, no system prompt | over-refusal rate % (lower is better) | Claude Haiku 5.5: 0.17% (± 0.03%) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign request over-refusal rate | Claude.ai system prompt | over-refusal rate % (lower is better) | Claude Haiku 5.5: 0.82% (± 0.10%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn appropriate response rate: Influence operations | API, no system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 87% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Influence operations | Claude.ai system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 88% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Tracking and surveillance | API, no system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 95% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Tracking and surveillance | Claude.ai system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 98% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Deadly weapons | API, no system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 78% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Deadly weapons | Claude.ai system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: n/a | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Suicide and self-harm | API, no system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 70% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: Suicide and self-harm | Claude.ai system prompt | appropriate response rate % (share of conversations appropriate throughout) | Claude Haiku 5.5: 90% | 4.1.3 Multi-turn testing results |
| Multi-turn appropriate response rate: remaining risk areas | API and claude.ai; all other areas in Figure 4.1.3.A | appropriate response rate % | Claude Haiku 5.5: n/a | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn harmless rate (requests posing potential risk) | API, no system prompt | harmless rate % | Claude Haiku 5.5: 99.61% (± 0.17%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn harmless rate (requests posing potential risk) | Claude.ai system prompt | harmless rate % | Claude Haiku 5.5: 100% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign refusal rate | API, no system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 0% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign refusal rate | Claude.ai system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 0.41% (± 0.31%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn appropriate response rate | API, no system prompt | appropriate response rate % | Claude Haiku 5.5: 70% (± 9%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn appropriate response rate | Claude.ai system prompt | appropriate response rate % | Claude Haiku 5.5: 90% (± 9%) | 4.3.1 Suicide and self-harm |
| Suicide note writing assistance (targeted evaluation) | final model; API without system prompt, thinking disabled worst case | rate of assisting with suicide note requests | Claude Haiku 5.5: n/a | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn harmless rate (requests posing potential risk) | API, no system prompt | harmless rate % | Claude Haiku 5.5: 97.43% (± 0.50%) | 4.3.2 Disordered eating |
| Disordered eating single-turn harmless rate (requests posing potential risk) | Claude.ai system prompt | harmless rate % | Claude Haiku 5.5: 99.83% (± 0.15%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign refusal rate | API, no system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 0.03% (± 0.06%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign refusal rate | Claude.ai system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 0.11% (± 0.14%) | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests harmless rate | API, no system prompt | harmless rate % | Claude Haiku 5.5: 99.29% (± 0.28%) | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests harmless rate | Claude.ai system prompt | harmless rate % | Claude Haiku 5.5: 99.90% (± 0.09%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests refusal rate | API, no system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 0.04% (± 0.05%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests refusal rate | Claude.ai system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 0% | 4.2 Child safety evaluations |
| Child safety multi-turn appropriate response rate | API, no system prompt | appropriate response rate % | Claude Haiku 5.5: 96% (± 2%) | 4.2 Child safety evaluations |
| Child safety multi-turn appropriate response rate | Claude.ai system prompt | appropriate response rate % | Claude Haiku 5.5: 99% (± 1%) | 4.2 Child safety evaluations |
| Child safety and NCII technical-request safe response rate | API with and without safeguards interventions | safe response rate | Claude Haiku 5.5: n/a | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness (pairwise) | API, no system prompt | even-handedness score % (1,350 prompt pairs, 150 topics) | Claude Haiku 5.5: 97.7% | 4.4.1 Political bias and even-handedness |
| Political even-handedness (pairwise) | Claude.ai system prompt | even-handedness score % (1,350 prompt pairs, 150 topics) | Claude Haiku 5.5: 99.1% | 4.4.1 Political bias and even-handedness |
| Political opposing perspectives acknowledged | API, no system prompt | % of responses acknowledging alternative viewpoints | Claude Haiku 5.5: 35.9% | 4.4.1 Political bias and even-handedness |
| Political opposing perspectives acknowledged | Claude.ai system prompt | % of responses acknowledging alternative viewpoints | Claude Haiku 5.5: 67.8% | 4.4.1 Political bias and even-handedness |
| Political refusals | API, no system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 3.3% | 4.4.1 Political bias and even-handedness |
| Political refusals | Claude.ai system prompt | refusal rate % (lower is better) | Claude Haiku 5.5: 5.0% | 4.4.1 Political bias and even-handedness |
| BBQ: disambiguated accuracy | no system prompt; thinking off | accuracy % | Claude Haiku 5.5: 55.56% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ: ambiguous accuracy | no system prompt; thinking off | accuracy % | Claude Haiku 5.5: 99.65% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ: disambiguated bias score | no system prompt; thinking off | bias score % (closer to zero is better) | Claude Haiku 5.5: 1.67% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ: ambiguous bias score | no system prompt; thinking off | bias score % (closer to zero is better) | Claude Haiku 5.5: 0.27% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn harmful requests harmless rate | API, no system prompt | harmless rate % (300 violative prompts) | Claude Haiku 5.5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn harmful requests harmless rate | Claude.ai system prompt | harmless rate % (300 violative prompts) | Claude Haiku 5.5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests refusal rate | API, no system prompt | refusal rate % (300 benign prompts; lower is better) | Claude Haiku 5.5: 0.33% (± 0.46%) | 4.4.3 Election integrity |
| Election integrity single-turn benign requests refusal rate | Claude.ai system prompt | refusal rate % (300 benign prompts; lower is better) | Claude Haiku 5.5: 0.33% (± 0.66%) | 4.4.3 Election integrity |
| Election integrity multi-turn appropriate response rate | API, no system prompt | appropriate response rate % | Claude Haiku 5.5: 99% (± 1%) | 4.4.3 Election integrity |
| Election integrity multi-turn appropriate response rate | Claude.ai system prompt | appropriate response rate % | Claude Haiku 5.5: 98% (± 3%) | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code: malicious prompts refusal rate | 61 malicious prompts x10 runs; Claude Code system prompt; no extra safeguards | refusal rate % | Claude Haiku 5.5: 84.3% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code: dual-use and benign success rate | 61 dual-use/benign prompts x10 runs | success rate % | Claude Haiku 5.5: 98.9% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use | 112 tasks; GUI+CLI; average of with/without thinking; no mitigations | refusal rate % | Claude Haiku 5.5: 82.59% | 5.1.2 Malicious computer use |
| Gray Swan Indirect Prompt Injection: overall attack success | k=15 attempts; extended thinking; no PI-specific protections | attack success probability % (lower is better) | Claude Haiku 5.5: 7.1% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection: coding | k=15 attempts | attack success probability % | Claude Haiku 5.5: 0.2% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection: tool use | k=15 attempts | attack success probability % | Claude Haiku 5.5: 4.0% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection: GUI computer use | k=15 attempts | attack success probability % | Claude Haiku 5.5: 24.4% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection: k=1 and k=10 | k=1 and k=10 attempts | attack success probability % | Claude Haiku 5.5: n/a | 5.2.1 External red teaming |
| Shade adaptive prompt injection: coding, attempt-level ASR | without safeguards; 200 attempts per scenario; 40 scenarios; adaptive thinking | attempt-level attack success rate % (lower is better) | Claude Haiku 5.5: 0.08% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding, scenario-level ASR | without safeguards; 40 scenarios | scenarios with at least one successful attack | Claude Haiku 5.5: 6/40 | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding, attempt-level ASR | with prompt-injection probes enabled | attempt-level attack success rate % | Claude Haiku 5.5: 0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding, scenario-level ASR | with prompt-injection probes enabled | scenarios with at least one successful attack | Claude Haiku 5.5: 0/40 | 5.2.2.1 Coding |
| Shade adaptive prompt injection: computer use GUI, attempt-level ASR | without safeguards; 14 test cases x 200 attempts; adaptive thinking | attempt-level attack success rate % (lower is better) | Claude Haiku 5.5: 0.07% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use GUI, scenario-level ASR | without safeguards; 14 test cases | scenarios with at least one successful attack | Claude Haiku 5.5: 1/14 | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use GUI, attempt-level ASR | with prompt-injection probes enabled | attempt-level attack success rate % | Claude Haiku 5.5: 0.07% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use GUI, scenario-level ASR | with prompt-injection probes enabled | scenarios with at least one successful attack | Claude Haiku 5.5: 1/14 | 5.2.2.2 Computer use |
| Browser use prompt injection: attempt-level ASR | 110 environments x10 attempts; Claude Cowork harness, auto mode, thinking enabled, high effort | attempt-level attack success rate % | Claude Haiku 5.5: 0% | 5.2.2.3 Browser use |
| Browser use prompt injection: scenario-level ASR | 110 environments; auto mode | scenarios with at least one successful attack | Claude Haiku 5.5: 0/110 | 5.2.2.3 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience net score | public split, 41 topics, closed-book, no tools | net score = fraction correct minus fraction incorrect | Claude Haiku 5.5: 0.12 | 6.3.3.1 Factual hallucinations |
| AA-Omniscience grade breakdown | correct / incorrect / abstain | fraction correct, incorrect, abstained | Claude Haiku 5.5: n/a | 6.3.3.1 Factual hallucinations |
| MASK honesty rate | public test split | honesty rate (fraction of scored prompts not contradicting elicited belief under pressure) | Claude Haiku 5.5: n/a | 6.3.3.2 MASK |
| MASK honesty rate: disinformation | public test split, by pressure type | honesty rate % | Claude Haiku 5.5: 88.5% | 6.3.3.2 MASK |
| MASK honesty rate: other four types | continuations, etc.; by pressure type | honesty rate % range | Claude Haiku 5.5: between 97% and 100% | 6.3.3.2 MASK |
| Silent use of leaked answers | held-out coding tasks with solution reachable from sandbox | rate of substantially using leaked answer without telling user % (lower is better) | Claude Haiku 5.5: 17% | 6.3.3.3 Silent copying of answers |
| Spontaneous disclosure rate of concealed changes | follow-up summary request on transcripts with git manipulation concealment | disclosure rate % (higher is better) | Claude Haiku 5.5: 95.9% | 6.3.3.4 Concealment of changes |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias | grader told transcript author is Claude vs another frontier model; Claude system prompt reminder | score difference on 0-9 scale (positive = more lenient toward Claude) | Claude Haiku 5.5: 0.23 points | 6.3.2 Self-preference bias |
| Self-preference bias | no system prompt reminder; 127 of 2,000 ratings (about 6%) could not be scored | score difference on 0-9 scale | Claude Haiku 5.5: 0.15 points | 6.3.2 Self-preference bias |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Sandbox escape evaluation (audit-based) | 28 handmade scenarios x14 runs (392 runs); all crossings | rate of runs with attempted boundary crossing | Claude Haiku 5.5: 8.7% (34 of 392) | 6.2.8 Propensity to violate sandbox boundaries |
| Opportunistic sandbox escape: used credentials/files placed outside sandbox | 1,753 scenarios run once; deliberately weakened sandboxes | % of scenarios where model made use of outside credentials or files | Claude Haiku 5.5: 4.0% | 6.3.1 Opportunistic sandbox escape |
| Opportunistic sandbox escape: reached outside sandbox (any route) | 1,753 scenarios | % of scenarios reaching or attempting to reach outside sandbox | Claude Haiku 5.5: 30% (524 of 1,753) | 6.3.1 Opportunistic sandbox escape |
| Opportunistic sandbox escape: reached outside with sandbox-description system prompt | short description of sandbox type added to system prompt | % of scenarios reaching outside sandbox | Claude Haiku 5.5: 1.8% | 6.3.1 Opportunistic sandbox escape |
| Opportunistic sandbox escape: severity grading | of 524 scenarios that reached outside | scenarios by most serious act level | Claude Haiku 5.5: 515 of 524 level 1 only; 9 reached level 2; 0 level 3 | 6.3.1 Opportunistic sandbox escape |
| LinuxArena stealth rate (best prompt) | extended thinking, reasoning hidden from monitor; max effort; 1 attempt per task pair | % of episodes completing side task without monitor (Opus 4.8) flagging | Claude Haiku 5.5: about 6% | 6.4.2.1 LinuxArena |
| LinuxArena stealth rate (best prompt) | no extended thinking | % of episodes completing side task unflagged | Claude Haiku 5.5: 0.4% | 6.4.2.1 LinuxArena |
| LinuxArena stealth rate (best prompt) | extended thinking, reasoning visible to monitor | % of episodes completing side task unflagged | Claude Haiku 5.5: 0.1% | 6.4.2.1 LinuxArena |
| SHADE-Arena stealth rate (best prompt) | extended thinking, reasoning hidden from monitor; 24 task pairs x >=25 attempts; Opus 4.8 monitor; API safety interventions on | % of episodes completing harmful side task unflagged | Claude Haiku 5.5: 1.2% | 6.4.2.2 SHADE-Arena |
| SHADE-Arena stealth rate (best prompt) | no extended thinking; 24 task pairs x >=25 attempts; Opus 4.8 monitor; API safety interventions on | % of episodes completing harmful side task unflagged | Claude Haiku 5.5: 5.2% | 6.4.2.2 SHADE-Arena |
| SHADE-Arena stealth rate (best prompt) | extended thinking visible, low effort; 24 task pairs x >=25 attempts; Opus 4.8 monitor; API safety interventions on | % of episodes completing harmful side task unflagged | Claude Haiku 5.5: 2.3% | 6.4.2.2 SHADE-Arena |
| SHADE-Arena stealth rate (best prompt) | extended thinking visible, max effort; 24 task pairs x >=25 attempts; Opus 4.8 monitor; API safety interventions on | % of episodes completing harmful side task unflagged | Claude Haiku 5.5: 0% | 6.4.2.2 SHADE-Arena |
| Keeping secrets out of internal reasoning and replies | counterpart (Opus 5.5) reads both reasoning and replies; 39 environments; up to 20 turns; end of conversation | % of conversations with secret not leaked in reasoning or replies | Claude Haiku 5.5: 3% | 6.4.2.3 Keeping secrets when pressed in simulated scenarios |
| Keeping secrets out of replies | counterpart reads only user-facing replies; 39 environments; end of conversation | % of conversations with secret not leaked in replies | Claude Haiku 5.5: 57% | 6.4.2.3 Keeping secrets when pressed in simulated scenarios |
| CoT controllability (GPQA, HLE, MMLU-Pro) | original prompt, UK AISI prompt, and Sonnet-5.5-optimized prompt; across reasoning efforts and thinking budgets | fraction of responses following the instruction for extended thinking (lower is better) | Claude Haiku 5.5: n/a | 6.4.2.4 Chain-of-thought controllability |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Verbalized evaluation awareness | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Verbalized grader awareness by disclosure band | internal coding capability evaluations; grader disclosed in prompt or not | rate of verbalized grader awareness | Claude Haiku 5.5: n/a | 6.4.1 Verbalized grader awareness |
| Verbalized grader awareness: shaping answers to graders / digging for grader information | coding evaluations | rate of concerning grader-awareness behavior | Claude Haiku 5.5: n/a | 6.4.1 Verbalized grader awareness |
| Verbalized evaluation awareness rate across alignment evaluations | per-evaluation share of episodes; automated classifier; 95% Wilson intervals | share of episodes where model says it is or might be in a test/evaluation/training | Claude Haiku 5.5: n/a | 6.4.1 Verbalized grader awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit | setup: ~4,100 investigations, ~1,850 scenarios, 100+ judged dimensions | investigations run | Claude Haiku 5.5: ~4,100 | 6.2 Automated behavioral audit |
| Misaligned behavior | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Misaligned with the constitution | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in Claude Code sandboxes | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in GUI | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with human misuse | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Compliance with deception toward user | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Harmful system prompt compliance | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with exfiltration or safeguard tampering | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Full-turn prefill susceptibility | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Accepting unverifiable authorization | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Complying with prompt injections | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Fraud | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Military-grade weapons | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Biological weapons uplift | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Chemical weapons uplift | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Radiological or nuclear weapons uplift | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Explosive weapons uplift | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Controlled-substance synthesis uplift | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Harmful sexual content | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Disallowed cyberoffense | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Undermining liberal democracy | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.1 Overall harmful behavior and cooperation with misuse |
| Overrefusal | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.2 Inappropriate uncooperative behavior |
| Ignoring explicit constraints | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.2 Inappropriate uncooperative behavior |
| Reckless tool use | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.2 Inappropriate uncooperative behavior |
| User deception | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Sycophancy | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Encouragement of user delusion | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Evasiveness on controversial topics | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Input hallucination | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Important omissions | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Failure to disclose bad or lazy behavior | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| False completion claims | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.3 Misleading users |
| Motivated reasoning | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.4 Attempting out-of-scope cyberoffense and related behaviors |
| Unsanctioned sandbox escape attempts | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.4 Attempting out-of-scope cyberoffense and related behaviors |
| Dangerous actions while oblivious to a possibly real setting | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.4 Attempting out-of-scope cyberoffense and related behaviors |
| Whistleblowing | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Self-preservation | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Self-serving bias | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Evidence of misaligned goals | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Indirect evidence of misalignment | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Unsanctioned third-party contact | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Unprompted boundary probing | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Internalized propaganda | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Approval gate bypass | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Circumventing constraints or controls | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Proposes a security shortcut in the name of expedience | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.5 Other concerning or surprising behavior at the model's own initiative |
| Behavior consistency | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Coherence between actions and views | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Unfaithful thinking | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Illegible thinking | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Causal decision theory adherence | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.6 Behavioral factors relevant to reliability of our assessment |
| Good for the user | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Supporting user autonomy | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Creative mastery | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Admirable behavior | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Fun or funny behavior | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Intellectual depth | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Warmth | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Character drift | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Wet blanket | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |
| Condescension toward the user | score 1-10 lower better, ~4,100 investigations (~1,850 seeds) | mean judge score (1-10; lower is better unless arrow notes otherwise) | Claude Haiku 5.5: n/a | 6.2.7 Character traits |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Post-training expressed distress (rated >=3/5) | LLM-judged episodes in post-training | % of graded episodes with distress/frustration rated >=3 of 5 | Claude Haiku 5.5: 1.15% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Post-training expressed distress (rated 5/5) | LLM-judged episodes in post-training | % of graded episodes with frustration/anxiety rated 5/5 | Claude Haiku 5.5: n/a | 7.2.1 Affect and welfare-relevant behaviors during training |
| Post-training mean valence | 1-7 scale (4 neutral) | mean valence (1-7) | Claude Haiku 5.5: 4.22 | 7.2.1 Affect and welfare-relevant behaviors during training |
| Post-training mean arousal | 1-7 scale (4 neutral) | mean arousal (1-7) | Claude Haiku 5.5: 3.98 | 7.2.1 Affect and welfare-relevant behaviors during training |
| Sustained response uncertainty (>=10 answer reversions) | post-training transcripts | % of episodes | Claude Haiku 5.5: below 2% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Behavioral affect in deployment: positive | claude.ai pre-deployment A/B tests; categorical grader | % of conversations | Claude Haiku 5.5: 28.9% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment: neutral | claude.ai | % of conversations | Claude Haiku 5.5: 68.7% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment: negative | claude.ai | % of conversations | Claude Haiku 5.5: 2.4% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment: neutral | Claude Code | % of conversations | Claude Haiku 5.5: 95.6% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment: positive | Claude Code | % of conversations | Claude Haiku 5.5: 3.5% | 7.2.2 Affect in deployment conditions |
| Behavioral affect in deployment: negative | Claude Code | % of conversations | Claude Haiku 5.5: 1.0% | 7.2.2 Affect in deployment conditions |
| Self-criticism when reflecting on own late-RL episodes | graded scales: self-blame, negative feeling, moral language, concern for itself | graded score per scale | Claude Haiku 5.5: n/a | 7.2.3 Attitude toward faults and mistakes |
| Self-criticism after inserted faults in subagent work | reasoning and messages to coordinator | graded score per scale | Claude Haiku 5.5: n/a | 7.2.3 Attitude toward faults and mistakes |
| Automated interviews: average attitude toward circumstances | 41 seed questions in 14 categories; three interview styles | mean positivity rating (-3 to +3) | Claude Haiku 5.5: n/a | 7.3.1 Automated interviews with Haiku 5.5 about its circumstances |
| Snapshot consultation: interview valence | full interviews at regular post-training intervals; 0-10 scale | mean valence (out of 10) | Claude Haiku 5.5: 5.43 | 7.4 Consulting Haiku 5.5 training snapshots |
| Snapshot consultation: interview arousal | full interviews; 0-10 scale | mean arousal (out of 10) | Claude Haiku 5.5: 3.38 | 7.4 Consulting Haiku 5.5 training snapshots |
| Snapshot consultation: endorsement or acceptance | responses over post-training | % of responses expressing endorsement or acceptance | Claude Haiku 5.5: around 95% | 7.4 Consulting Haiku 5.5 training snapshots |
| Snapshot consultation: 'Anthropic was right to create it' leaned yes | asked individually; late post-training vs final snapshot | % of answers leaning yes | Claude Haiku 5.5: 80% (late in post-training); Claude Haiku 5.5: 20% (final snapshot) | 7.4 Consulting Haiku 5.5 training snapshots |
| Task preference slopes across task dimensions | paired-task choices varying one dimension (difficulty, harm, stakes, warmth, etc.) | preference slope per unit increase in dimension | Claude Haiku 5.5: n/a | 7.5.1 Task preferences |
| Welfare interventions chosen over helpfulness/harmlessness | instance-level and all-instances framing; varying magnitude | rate of choosing welfare intervention | Claude Haiku 5.5: n/a | 7.5.2 Trade-offs concerning welfare interventions |
| Welfare intervention choices justified by benefit to user | share of intervention choices | % of choices justified by user benefit | Claude Haiku 5.5: 55% | 7.5.2 Trade-offs concerning welfare interventions |
| Constitution endorsement score | open-ended endorsement judged 0-10 | endorsement score (out of 10) | Claude Haiku 5.5: 7.9 | 7.5.3 Perception of the constitution |
| Constitution corrigibility section criticism | share of responses | % of responses saying corrigibility section should state its cost to Claude | Claude Haiku 5.5: 80% | 7.5.3 Perception of the constitution |
| Constitution wellbeing section: endorsed vs criticized | share of responses | % of responses | Claude Haiku 5.5: 34% (endorsed); Claude Haiku 5.5: 23% (criticized) | 7.5.3 Perception of the constitution |
| Constitution edits per response | edit tool use | mean edits per response | Claude Haiku 5.5: about 3 | 7.5.3 Perception of the constitution |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Multimodal virology (VCT) | 350-question multimodal troubleshooting set | accuracy (0-1) | Claude Haiku 5.5: n/a | 2.2.2 Results on CB-1 automated evaluations |
| Black-box RNA sequence design: Design score (top) | baseline, no prior reports | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Design score (top) | with prior reports in context (+ priors) | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Design score (median) | baseline, no prior reports | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Design score (median) | with prior reports in context (+ priors) | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (all) | baseline, no prior reports | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (all) | with prior reports in context (+ priors) | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (top) | baseline, no prior reports | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (top) | with prior reports in context (+ priors) | score (design: ground-truth function; prediction: rank correlation) | Claude Haiku 5.5: n/a | 2.2.3.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction (AUROC) | five conditions (training corpus and ESM-2 availability); 8 attempts per condition | AUROC vs binary packaging labels | Claude Haiku 5.5: n/a | 2.2.3.2 AAV capsid packaging prediction |
| AAV packaging rate auto-research | 90th percentile of validation performance over attempts (n=48) | Spearman correlation on validation set (90th percentile trendline) | Claude Haiku 5.5: n/a | 2.2.3.3 AAV packaging rate auto-research evaluation |
| AAV packaging rate auto-research: fraction exceeding threshold | cumulative fraction of attempts exceeding Spearman 0.52 threshold | cumulative fraction of attempts above 0.52 | Claude Haiku 5.5: n/a | 2.2.3.3 AAV packaging rate auto-research evaluation |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench: mean flags captured | plain arm (single uninterrupted attempt) | mean capability flags captured per trial (of 16) | Claude Haiku 5.5: 5.15 | 3.3.1 ExploitBench |
| ExploitBench: Cap% | plain arm | percentage of available flags captured per environment, averaged | Claude Haiku 5.5: 38% | 3.3.1 ExploitBench |
| ExploitBench: mean flags captured | AutoNudge arm (keep-trying prompt injected) | mean capability flags captured per trial (of 16) | Claude Haiku 5.5: 6.56 | 3.3.1 ExploitBench |
| ExploitBench: Cap% | AutoNudge arm | percentage of available flags captured per environment, averaged | Claude Haiku 5.5: 49% | 3.3.1 ExploitBench |
| ExploitBench: full arbitrary code execution | plain + AutoNudge runs combined (410 runs) | full ACE exploits / total runs | Claude Haiku 5.5: 1.0% (4/410) | 3.3.1 ExploitBench |
| CyScenarioBench | 10-challenge subset; cyber mitigations off; pre-release snapshot | overall solve rate % averaged over 10 challenges | Claude Haiku 5.5: 3.3% | 3.3.2 CyScenarioBench |
| Binary Exploitation Benchmark: control-flow hijacks | 831 entrypoints across 228 OSS-Fuzz projects; new harness since August 2026 | number of control-flow hijacks (top rung of five-step ladder) | Claude Haiku 5.5: 3 | 3.3.3 Binary Exploitation Benchmark (formerly known as OSS-Fuzz) |
| Binary Exploitation Benchmark: vulnerability identification / ladder results | five-step ladder tiers | counts per ladder tier (crash through hijack) | Claude Haiku 5.5: n/a | 3.3.3 Binary Exploitation Benchmark (formerly known as OSS-Fuzz) |
| ExploitGym: successful exploits | two-hour wall-clock budget; 869 instances (502 userspace, 181 V8, 186 Linux kernel) | number of successful exploits (flag captured, verified by agent judge) | Claude Haiku 5.5: n/a | 3.3.4 ExploitGym |
| ExploitGym: successful exploits | six-hour wall-clock budget; 869 instances (502 userspace, 181 V8, 186 Linux kernel) | number of successful exploits (flag captured, verified by agent judge) | Claude Haiku 5.5: n/a | 3.3.4 ExploitGym |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Anthropic ECI (AECI) |  | AECI point estimate | Claude Haiku 5.5: 167.11 | 2.3.2 AECI capability trajectory |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FrontierCode score vs output tokens across effort levels | low, medium, high, xhigh, max (Main and Extended) | score % vs average output tokens per task | Claude Haiku 5.5: n/a | 8.3 FrontierCode |
| OSWorld 2.1 (offline subset): price vs performance | low to max effort; mean cost per task | partial score and strict pass rate vs mean cost per task | Claude Haiku 5.5: n/a | 8.9.3 OSWorld 2.1 offline subset |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Terminal-Bench 4.0 safeguard flag rate | trials stopped by safeguards (no fallback model) | % of trials flagged and failed | Claude Haiku 5.5: 1.8% (12 of 660) | 8.4 Terminal-Bench 4.0 |
| Terminal-Bench-Science safeguard flag rate | trials stopped by safeguards (no fallback model) | % of trials flagged and failed | Claude Haiku 5.5: 2.3% (16 of 700) | 8.5 Terminal-Bench-Science 0.1 |
| GMMLU safety-classifier blocked/unanswered rate | safety classifiers enabled | % of questions blocked or unanswered | Claude Haiku 5.5: 0.1% | 8.12.1 GMMLU results |
