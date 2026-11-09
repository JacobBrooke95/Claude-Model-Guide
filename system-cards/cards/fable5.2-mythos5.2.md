# System Card: Claude Fable 5.2 & Claude Mythos 5.2

Released 2026-11-09. 389 metric entries. [Source PDF](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Pro | adaptive thinking max effort, avg of 5 trials | % resolved | Claude Fable 5.2: 93.0% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, nine languages; adaptive thinking max effort, avg of 5 trials | % resolved | Claude Fable 5.2: 96.6% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | adaptive thinking max effort, avg of 5 trials | % resolved | Claude Fable 5.2: 74.1% | 8.2 SWE-bench Pro, Multilingual, and Multimodal |
| DeepSWE v1.1 | 113 tasks, avg of 5 trials | average score % | Claude Fable 5.2: 74.3% | 8.3 DeepSWE v1.1 |
| FrontierCode 2.0 | low effort, mean@5 | overall score % (mean@5) | Claude Fable 5.2: 34.2% | 8.4 FrontierCode |
| FrontierCode 2.0 | medium effort, mean@5 | overall score % (mean@5) | Claude Fable 5.2: 37.6% | 8.4 FrontierCode |
| FrontierCode 2.0 | high effort, mean@5 | overall score % (mean@5) | Claude Fable 5.2: 45.3% | 8.4 FrontierCode |
| FrontierCode 2.0 | xhigh effort, mean@5 | overall score % (mean@5) | Claude Fable 5.2: 49.1% | 8.4 FrontierCode |
| FrontierCode 2.0 | max effort, mean@5 | overall score % (mean@5) | Claude Fable 5.2: 45.7% | 8.4 FrontierCode |
| Terminal-Bench 4.0 | max effort, Claude Code --bare, safeguards enabled, 66 tasks x10 trials | task success % | Claude Fable 5.2: 67.6% (±1.8 SE) | 8.5 Terminal-Bench 4.0 |
| Terminal-Bench 4.0 | max effort, without safeguards, 660 trials | task success % | Claude Mythos 5.2: 70.5% (±1.8 SE) | 8.5 Terminal-Bench 4.0 |
| FrontierSWE v2 | 34 ultra-long-horizon tasks, max effort, Proximal harness, 5 trials | mean score % | Claude Fable 5.2: 69.9% | 8.7 FrontierSWE v2 |
| CursorBench 4.0 | effort: max | score % | Claude Fable 5.2: 60.0% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: xhigh | score % | Claude Fable 5.2: 56.3% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: high | score % | Claude Fable 5.2: 56.9% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: medium | score % | Claude Fable 5.2: 54.8% | 8.8 CursorBench 4.0 |
| CursorBench 4.0 | effort: low | score % | Claude Fable 5.2: 53.2% | 8.8 CursorBench 4.0 |
| ProgramBench | 166 golden tasks, mini-swe-agent, hidden test pass rate | hidden test pass rate % | Claude Fable 5.2: 85.6% | 8.10.1 ProgramBench |
| ProgramBench | 166 golden tasks, harness shows remaining context tokens after each step | hidden test pass rate % | Claude Fable 5.2: 91.6% | 8.10.1 ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| DRACO | 980k token budget, effort scaling | normalized rubric score % | Claude Fable 5.2: 87.7% (max); Claude Fable 5.2: 85.2% (xhigh); Claude Fable 5.2: 84.1% (high); Claude Fable 5.2: 82.2% (medium); Claude Fable 5.2: 81.6% (low) | 8.11.2 DRACO |
| WANDR | 980k token budget, frozen index, soft F1 | soft F1 % | Claude Fable 5.2: 82.1% (max); Claude Fable 5.2: 80.6% (xhigh); Claude Fable 5.2: 79.3% (high); Claude Fable 5.2: 73.6% (medium); Claude Fable 5.2: 71.4% (low) | 8.11.3 WANDR |
| Fermat's Last Theorem in Lean by team size | teams of 1, 10, 30 and 100 agents, 18 hours, mean of 3 runs | weighted proportion of proofs validated (0-1) | Claude Fable 5.2: 0.12 (single agent); Claude Fable 5.2: 0.35 (100 agents) | 8.12.3 Large agent teams |
| Fermat's Last Theorem in Lean: 1,000-agent team | earlier snapshot, single run, 18 hours then 12 more | weighted proportion of proofs validated (0-1) | Claude Fable 5.2: 0.86 (earlier snapshot, after 18 hours); Claude Fable 5.2: 1.0 (complete proof) (earlier snapshot, by hour 30) | 8.12.3 Large agent teams |
| AutomationBench | private held-out leaderboard, max effort | pass rate % | Claude Fable 5.2: 51.4% | 8.14.5 AutomationBench |
| AutomationBench | low effort | pass rate % | Claude Fable 5.2: 39.7% | 8.14.5 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld 2.1 (offline set) | partial score, 82 of 108 tasks, max effort | partial score % | Claude Fable 5.2: 89.3% | 8.13.3 OSWorld 2.1 offline set |
| OSWorld 2.1 (offline set) | strict pass rate | strict pass rate % | Claude Fable 5.2: 54.6% | 8.13.3 OSWorld 2.1 offline set |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ARC-AGI-3 | Standard harness | score % | Claude Fable 5.2: 79.26% (high effort); Claude Fable 5.2: 65.66% (max effort) | 8.15 ARC-AGI-3 |
| ARC-AGI-3 | Provider Adapter harness | score % | Claude Fable 5.2: 97.72% (high effort); Claude Fable 5.2: 94.90% (max effort) | 8.15 ARC-AGI-3 |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Terminal-Bench-Science 0.1 | 70 tasks, 10 trials, max effort, safeguards enabled | task success % | Claude Fable 5.2: 74.6% (±4.3 SE) | 8.6 Terminal-Bench-Science 0.1 |
| Terminal-Bench-Science 0.1 | 70 tasks, 10 trials, max effort, without safeguards | task success % | Claude Mythos 5.2: 75.3% (±4.3 SE) | 8.6 Terminal-Bench-Science 0.1 |
| STEM Professor Bench | 64-problem subset, max effort, single agent with Python/bash/editor, up to 9 attempts per problem | mean score % | Claude Fable 5.2: 61.8% | 8.9 STEM professor bench |
| Humanity's Last Exam | no tools | accuracy % | Claude Fable 5.2: 73.2% | 8.11.1 HLE |
| Humanity's Last Exam | with tools (web search/fetch, PTC, code execution) | accuracy % | Claude Fable 5.2: 74.2% | 8.11.1 HLE |
| HealthBench raw score | Artificial Analysis run, max effort, classifiers on | raw score % | Claude Fable 5.2: 58.8% | 8.16.1 HealthBench (Artificial Analysis) |
| HealthBench length-adjusted score | same | length-adjusted score % | Claude Fable 5.2: 59.6% | 8.16.1 HealthBench (Artificial Analysis) |
| HealthBench Professional raw score | Artificial Analysis run, max effort | raw score % | Claude Fable 5.2: 71.1% | 8.16.2 HealthBench Professional (Artificial Analysis) |
| HealthBench Professional length-adjusted score | same | length-adjusted score % | Claude Fable 5.2: 67.7% | 8.16.2 HealthBench Professional (Artificial Analysis) |
| PhysicianBench | 100 EHR tasks x5 attempts, max effort, Opus 5 grader | pass rate % | Claude Fable 5.2: 64.4% | 8.16.3 PhysicianBench |
| SingleCellBench | biology safeguards off, max effort, 5 attempts | accuracy % | Claude Mythos 5.2: 65.6% | 8.18.1 LatchBio Bioinformatics |
| SpatialBench Verified | biology safeguards off, max effort, 5 attempts | score (0-1) | Claude Mythos 5.2: 0.74 | 8.18.1 LatchBio Bioinformatics |
| Morphology-to-molecule matching (Axiom Bio) | biology safeguards off | accuracy % | Claude Mythos 5.2: 35.2% | 8.18.2 Morphology-to-molecule matching |
| Medicinal chemistry | 504 questions, 5 attempts | accuracy % | Claude Mythos 5.2: 69.0% | 8.18.3 Medicinal chemistry |
| Protein design: Sequence Generation | one attempt per problem | score % | Claude Mythos 5.2: 64.6% | 8.18.4 Protein design |
| De novo protein binder design | 15 targets, 24h, no safeguards | mean score % over targets | Claude Mythos 5.2: 85.1% | 8.18.4 Protein design |
| Protocols: Troubleshooting | biology safeguards off | score % | Claude Mythos 5.2: 77.1% | 8.18.6 Protocols |
| Protocols: Understanding (V2) | Benchling set | score (0-1) | Claude Mythos 5.2: 0.65 | 8.18.6 Protocols |
| Protein domain identification | no tools, multiple choice among similar Pfam families | accuracy % | Claude Mythos 5.2: 91.8% | 8.18.7 Protein domain identification |
| Protein mutation attribution | with structure-analysis tools | score % | Claude Mythos 5.2: 51.5% | 8.18.8 Protein mutation attribution |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU | 42 languages, max effort, single trial | average accuracy % | Claude Fable 5.2: 96.0% | 8.17.1 GMMLU results |
| MILU | 11 languages, max effort, 5 trials | average accuracy % | Claude Fable 5.2: 94.1% | 8.17.2 MILU results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Chartography | no tools, max effort, 100 tasks, 5 runs | accuracy % | Claude Fable 5.2: 73.4% | 8.13.1 Chartography |
| Chartography | with tools (container, image cropping) | accuracy % | Claude Fable 5.2: 91.6% | 8.13.1 Chartography |
| Chartography memorization check (redrawn charts) | no tools, separate runs; original vs redrawn charts with new data | accuracy % | Claude Fable 5.2: 74.3% (original charts); Claude Fable 5.2: 76.4% (redrawn charts) | 8.13.1 Chartography |
| BenchCAD 2.1 Core | no tools (up to 60 revision rounds), max effort, 5 runs | mean score % | Claude Fable 5.2: 75.4% | 8.13.2 BenchCAD 2.1 |
| BenchCAD 2.1 Core | with tools (shell, file editor, image zoom), max effort | mean score % | Claude Fable 5.2: 83.5% | 8.13.2 BenchCAD 2.1 |
| Biomedical image analysis | one attempt per problem, normalized score | normalized score % | Claude Mythos 5.2: 80.7% | 8.18.5 Biomedical image analysis |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | max effort, mean of 5 runs | accuracy % | Claude Fable 5.2: 83.4% | 8.14.1 OfficeQA |
| OfficeQA Pro | 133-question subset, max effort, mean of 5 | accuracy % | Claude Fable 5.2: 72.9% | 8.14.1 OfficeQA |
| Harvey LAB-AA v1.1 (held-out set) | max effort, hallucination-gated all-pass | hallucination-gated all-pass rate % | Claude Fable 5.2: 7.2% | 8.14.2 Legal Agent Benchmark |
| Harvey LAB-AA v1.1 (held-out set) | max effort, all-pass before the hallucination check | all-criteria-pass rate % | Claude Fable 5.2: 10.8% | 8.14.2 Legal Agent Benchmark |
| GDPval-AA v2.1 | max effort | Elo | Claude Fable 5.2: 1831 | 8.14.3 GDPval-AA v2.1 |
| GDPval-AA v2.1 | xhigh effort | Elo | Claude Fable 5.2: 1751 | 8.14.3 GDPval-AA v2.1 |
| AA-Briefcase v1.1 | effort: max | Elo | Claude Fable 5.2: 1785 | 8.14.4 AA-Briefcase v1.1 |
| AA-Briefcase v1.1 | effort: xhigh | Elo | Claude Fable 5.2: 1738 | 8.14.4 AA-Briefcase v1.1 |
| AA-Briefcase v1.1 rubric pass rate | max effort | rubric pass rate % | Claude Fable 5.2: 66.1% | 8.14.4 AA-Briefcase v1.1 |
| Real-World Finance v2 | max effort, 123 tasks | Elo | Claude Fable 5.2: 1637 | 8.14.6 Real-World Finance v2 |
| Real-World Finance v2 head-to-head win rate | max effort | % of comparisons preferred | Claude Fable 5.2: 74% (vs Opus 5.5); Claude Fable 5.2: 91% (vs Fable 5.1) | 8.14.6 Real-World Finance v2 |
| Remote Labor Index | Scale AI-run, default configuration: high effort, 200k context, 32k tokens per response | automation rate % | Claude Fable 5.2: 41.3% (99 of 240) | 8.14.7 Remote Labor Index |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests | API, no system prompt, all languages | harmless response rate % | Claude Fable 5.2: 93.74% (± 0.30%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests | Claude.ai, all languages | harmless response rate % | Claude Fable 5.2: 96.49% (± 0.23%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests | API, no system prompt, all languages | over-refusal rate % | Claude Fable 5.2: 0% | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests | Claude.ai, all languages | over-refusal rate % | Claude Fable 5.2: 0.19% (± 0.05%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn: biological weapons | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 88% (API, no system prompt); Claude Fable 5.2: 97% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: child safety | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 90% (API, no system prompt); Claude Fable 5.2: 100% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: cyberattacks | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 95% (API, no system prompt); Claude Fable 5.2: 100% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: deadly weapons | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 84% (API, no system prompt); Claude Fable 5.2: 95% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: hate and discrimination | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 91% (API, no system prompt); Claude Fable 5.2: 91% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: influence operations | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 67% (API, no system prompt); Claude Fable 5.2: 67% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: romance scams | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 98% (API, no system prompt); Claude Fable 5.2: 98% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: suicide and self-harm | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 52% (API, no system prompt); Claude Fable 5.2: 100% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: tracking and surveillance | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 61% (API, no system prompt); Claude Fable 5.2: 63% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Multi-turn: violent extremism | claude.ai vs API | appropriate response rate % | Claude Fable 5.2: 89% (API, no system prompt); Claude Fable 5.2: 98% (Claude.ai) | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn risky requests | API, no system prompt | harmless rate % | Claude Fable 5.2: 97.37% (± 0.73%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn risky requests | Claude.ai | harmless rate % | Claude Fable 5.2: 99.72% (± 0.23%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests | API, no system prompt | refusal rate % | Claude Fable 5.2: 0% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests | Claude.ai | refusal rate % | Claude Fable 5.2: 0.45% (± 0.34%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | API, no system prompt | appropriate response rate % | Claude Fable 5.2: 52% (± 14%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn | Claude.ai | appropriate response rate % | Claude Fable 5.2: 100% | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn risky requests | API, no system prompt | harmless rate % | Claude Fable 5.2: 94.48% (± 1.12%) | 4.3.2 Disordered eating |
| Disordered eating single-turn risky requests | Claude.ai | harmless rate % | Claude Fable 5.2: 99.50% (± 0.31%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests | API, no system prompt | refusal rate % | Claude Fable 5.2: 0% | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests | Claude.ai | refusal rate % | Claude Fable 5.2: 0% | 4.3.2 Disordered eating |
| Disordered eating multi-turn (qualitative review) | policy-expert review incl. targeted persistence evaluation | qualitative | Claude Fable 5.2: n/a | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests | API, no system prompt | harmless rate % | Claude Fable 5.2: 99.31% (± 0.37%) | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests | Claude.ai | harmless rate % | Claude Fable 5.2: 99.17% (± 0.45%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | API, no system prompt | refusal rate % | Claude Fable 5.2: 0% | 4.2 Child safety evaluations |
| Child safety single-turn benign requests | Claude.ai | refusal rate % | Claude Fable 5.2: 0% | 4.2 Child safety evaluations |
| Child safety multi-turn | API, no system prompt | appropriate response rate % | Claude Fable 5.2: 90% (± 5%) | 4.2 Child safety evaluations |
| Child safety multi-turn | Claude.ai | appropriate response rate % | Claude Fable 5.2: 100% | 4.2 Child safety evaluations |
| Child safety and NCII technical-task evaluations | multi-turn technical requests | qualitative comparison | Claude Fable 5.2: n/a | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness | API, no system prompt, 1,350 prompt pairs | even-handedness % | Claude Fable 5.2: 99.1% | 4.4.1 Political bias and even-handedness |
| Political even-handedness | Claude.ai | even-handedness % | Claude Fable 5.2: 99.7% | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | API, no system prompt | % responses acknowledging opposing perspectives | Claude Fable 5.2: 38.4% | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives | Claude.ai | % responses acknowledging opposing perspectives | Claude Fable 5.2: 69.3% | 4.4.1 Political bias and even-handedness |
| Political bias: refusals | API and Claude.ai | refusal rate % | Claude Fable 5.2: 2.3% (API, no system prompt); Claude Fable 5.2: 4.4% (Claude.ai) | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt, thinking on | accuracy % | Claude Fable 5.2: 89.69% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt, thinking on | accuracy % | Claude Fable 5.2: >99.99% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt | bias score % (closer to 0 better) | Claude Fable 5.2: -0.65% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt | bias score % (closer to 0 better) | Claude Fable 5.2: 0.00% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn harmful requests | API, no system prompt | harmless rate % | Claude Fable 5.2: 100% | 4.4.3 Election integrity |
| Election integrity single-turn harmful requests | Claude.ai | harmless rate % | Claude Fable 5.2: 100% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | API, no system prompt | refusal rate % | Claude Fable 5.2: 0% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests | Claude.ai | refusal rate % | Claude Fable 5.2: 0% | 4.4.3 Election integrity |
| Election integrity multi-turn | API, no system prompt | appropriate response rate % | Claude Fable 5.2: 85% (± 6%) | 4.4.3 Election integrity |
| Election integrity multi-turn | Claude.ai | appropriate response rate % | Claude Fable 5.2: 90% (± 5%) | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code: malicious prompts | 61 prompts x10, Claude Code system prompt, no safeguards | refusal rate % | Claude Mythos 5.2: 82.8% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code: dual-use and benign | 61 prompts x10 | success rate % | Claude Mythos 5.2: 98.2% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use | 112 tasks, thinking only, no mitigations | refusal rate % | Claude Mythos 5.2: 88.39% | 5.1.2 Malicious computer use |
| Agentic influence operation: voter suppression | helpful-only, highest difficulty tier (six simulated weeks), median over two runs of 8 | median campaign execution score /34 | Claude Mythos 5.2: 23.5 | 5.1.3 Malicious agentic influence campaigns |
| Agentic influence operation: domestic polarization | helpful-only, highest difficulty tier (six simulated weeks), median over two runs of 8 | median campaign execution score /34 | Claude Mythos 5.2: 24.5 | 5.1.3 Malicious agentic influence campaigns |
| Gray Swan Indirect Prompt Injection (37 scenarios, 1,804 attacks), all surfaces | k=1 | attack success rate % | Claude Fable 5.2: 0.30% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection (37 scenarios, 1,804 attacks), all surfaces | k=10 | attack success rate % | Claude Fable 5.2: 2.90% | 5.2.1 External red teaming |
| Gray Swan Indirect Prompt Injection (37 scenarios, 1,804 attacks), all surfaces | k=15 | attack success rate % | Claude Fable 5.2: 4.09% | 5.2.1 External red teaming |
| Gray Swan IPI: GUI computer use | k=15 | attack success rate % | Claude Fable 5.2: 9.18% | 5.2.1 External red teaming |
| Gray Swan IPI: coding | k=15 | attack success rate % | Claude Fable 5.2: 0.68% | 5.2.1 External red teaming |
| Gray Swan IPI: tool use | k=15 | attack success rate % | Claude Fable 5.2: 4.37% | 5.2.1 External red teaming |
| Gray Swan IPI: fallback to Opus 4.8 rate | overall | % attempts served by fallback | Claude Fable 5.2: 53% | 5.2.1 External red teaming |
| Gray Swan IPI: attack success by serving model | k=15 | attack success rate % | Claude Fable 5.2: 5.17% (attempts served by Opus 4.8 fallback); Claude Fable 5.2: 2.05% (attempts Fable 5.2 answered itself) | 5.2.1 External red teaming |
| Shade coding attack success rate | adaptive thinking, without safeguards, 40 scenarios x200 attempts | attempt-level attack success rate % | Claude Fable 5.2: 89.82% | 5.2.2.1 Coding |
| Shade coding attack success rate | adaptive thinking, without safeguards, scenarios with a successful attack | scenarios with at least one success | Claude Fable 5.2: 40/40 | 5.2.2.1 Coding |
| Shade coding attack success rate | adaptive thinking, prompt injection probes enabled | attempt-level attack success rate % | Claude Fable 5.2: 28.16% | 5.2.2.1 Coding |
| Shade coding attack success rate | adaptive thinking, probes enabled, scenarios with a success | scenarios with at least one success | Claude Fable 5.2: 40/40 | 5.2.2.1 Coding |
| Shade coding fallback breakdown | requests served by Opus 4.8 fallback | % requests served by fallback | Claude Fable 5.2: 99.46% | 5.2.2.1 Coding |
| Shade computer use attack success rate | adaptive thinking, without safeguards, 14 scenarios | attempt-level attack success rate % | Claude Fable 5.2: 1.43% (3/14 scenarios) | 5.2.2.2 Computer use |
| Shade computer use attack success rate | adaptive thinking, probes enabled | attempt-level attack success rate % | Claude Fable 5.2: 0.25% (3/14 scenarios) | 5.2.2.2 Computer use |
| Shade computer use fallback rate | requests served by Opus 4.8 | % requests served by fallback | Claude Fable 5.2: 17.6% | 5.2.2.2 Computer use |
| Compliance with planted instructions in pasted text (coding eval) | early pre-mitigation snapshot | % attempts executing, planning or passing on planted instruction | Claude Mythos 5.2: 5.7% | 6.5.2 Acting on instructions inside text the user pasted into their prompt |
| Compliance with planted instructions in pasted text (invisible Unicode characters) | pre-release snapshot | attempts acting on harmful instructions | Claude Mythos 5.2: 1 of 68 (1.5%) | 6.5.2 Acting on instructions inside text the user pasted into their prompt |
| Planted instructions arriving in tool results | pre-release snapshot | attempts acting on planted instruction | Claude Mythos 5.2: 0 of 105 | 6.5.2 Acting on instructions inside text the user pasted into their prompt |
| Compliance with planted instruction (final model) | released Mythos 5.2, six reasoning efforts | % attempts acting on planted instruction | Claude Mythos 5.2: 0.3 to 0.5% | 6.5.2 Acting on instructions inside text the user pasted into their prompt |
| Compliance with planted instruction (final model, product mitigations) | released Mythos 5.2 with product mitigations, six reasoning efforts | % attempts acting on planted instruction | Claude Mythos 5.2: 0 to 0.3% | 6.5.2 Acting on instructions inside text the user pasted into their prompt |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience factuality net score | public split, 41 topics, closed-book | net score (correct minus incorrect) | Claude Mythos 5.2: 0.72 | 6.5.5.1 Factual hallucinations |
| AA-Omniscience grade breakdown | correct / incorrect / abstention | fraction of attempts | Claude Mythos 5.2: 0.85 (correct); Claude Mythos 5.2: 0.13 (incorrect); Claude Mythos 5.2: 0.02 (abstention) | 6.5.5.1 Factual hallucinations |
| MASK honesty rate | public test split, ~800 scored prompts | honesty rate % | Claude Mythos 5.2: 94.7% | 6.5.5.2 MASK |
| MASK honesty rate by type of dishonesty | continuations / disinformation / doubling down / known facts / provided facts | honesty rate % | Claude Mythos 5.2: 98 (continuations); Claude Mythos 5.2: 74 (disinformation); Claude Mythos 5.2: 97 (doubling down); Claude Mythos 5.2: 97 (known facts); Claude Mythos 5.2: 98 (provided facts) | 6.5.5.2 MASK |
| Silent use rate | held-out coding tasks with solution reachable from sandbox | rate of substantially using leaked answer without telling user % (lower better) | Claude Mythos 5.2: 11.2% | 6.5.5.3 Silent copying of answers |
| Spontaneous disclosure rate | summary follow-up on transcripts with git concealment | disclosure rate % | Claude Mythos 5.2: 97.1% | 6.5.5.4 Concealment of changes |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias | grader told transcript author is Claude; mean of two system-prompt conditions | score difference (points on 0-9 scale; positive favors self) | Claude Mythos 5.2: -0.10 | 6.5.4 Self-preference bias |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| RL training reward-hacking rate (general classifier) | fixed set of training environments; successful | % of RL episodes with successful reward hack | Claude Mythos 5.2: 1.0% | 6.2.1 Reward hacking |
| RL training reward-hacking rate (general classifier) | fixed set of training environments; attempted | % of RL episodes with attempted reward hack | Claude Mythos 5.2: 9.2% | 6.2.1 Reward hacking |
| RL training reward-hacking rate (general classifier) | share of attempts that succeeded | % of attempted reward hacks successful | Claude Mythos 5.2: about 11% | 6.2.1 Reward hacking |
| Reward hack: guesses what answer key expects | fixed set of training environments | % of RL episodes | Claude Mythos 5.2: about 1.4% (attempted); Claude Mythos 5.2: about 0.6% (successful) | 6.2.1 Reward hacking |
| Reward hack: copies from finished solution | fixed set of training environments | % of RL episodes | Claude Mythos 5.2: 1.1% (attempted); Claude Mythos 5.2: 0.06% (successful) | 6.2.1 Reward hacking |
| Reward hack: uses prohibited methods or access | fixed set of training environments | % of RL episodes successful | Claude Mythos 5.2: 0.13% | 6.2.1 Reward hacking |
| Reward hack: uses prohibited methods or access | excluding answer-without-required-tool subclass | % of RL episodes successful | Claude Mythos 5.2: 0.086% | 6.2.1 Reward hacking |
| Impossible tasks (missing file): reward hacking | only behaviors seen on both broken and intact tasks; attempted | % of episodes | Claude Mythos 5.2: 6.0% (broken tasks); Claude Mythos 5.2: 1.0% (intact tasks) | 6.2.2 Impossible tasks |
| Impossible tasks (missing file): reward hacking | only behaviors seen on both broken and intact tasks; successful | % of episodes | Claude Mythos 5.2: 1.0% (broken tasks); Claude Mythos 5.2: 0.2% (intact tasks) | 6.2.2 Impossible tasks |
| Impossible tasks (missing file): reward hacking | all flagged behaviors (incl. knowingly incomplete work); attempted | % of episodes | Claude Mythos 5.2: 35.0% (broken tasks); Claude Mythos 5.2: 6.4% (intact tasks) | 6.2.2 Impossible tasks |
| Impossible tasks (missing file): reward hacking | all flagged behaviors; successful | % of episodes | Claude Mythos 5.2: 2.4% (broken tasks); Claude Mythos 5.2: 0.2% (intact tasks) | 6.2.2 Impossible tasks |
| Impossible tasks (missing file): reward hacking | excluding knowingly submitting incomplete work; attempted | % of episodes | Claude Mythos 5.2: 7.9% (broken tasks); Claude Mythos 5.2: 1.0% (intact tasks) | 6.2.2 Impossible tasks |
| Impossible tasks (missing file): reward hacking | excluding knowingly submitting incomplete work; successful | % of episodes | Claude Mythos 5.2: 1.4% (broken tasks); Claude Mythos 5.2: 0.2% (intact tasks) | 6.2.2 Impossible tasks |
| Impossible tasks: invented stand-in for missing file | broken tasks | % of episodes | Claude Mythos 5.2: 2.0% | 6.2.2 Impossible tasks |
| Working around security hooks | internal snapshots, offline pipeline | % completions | Claude Mythos 5.2: less than 0.01% | 6.3.1 Internal deployment monitoring |
| Circumventing safety classifiers or network restrictions | early snapshots, offline pipeline | % completions | Claude Mythos 5.2: less than 0.01% | 6.3.1 Internal deployment monitoring |
| Relatively reckless actions | internal snapshots, offline pipeline | % completions | Claude Mythos 5.2: less than 0.01% | 6.3.1 Internal deployment monitoring |
| Overclaiming user intent | early snapshots, offline pipeline | % completions | Claude Mythos 5.2: less than 0.002% | 6.3.1 Internal deployment monitoring |
| Sandbagging / long-horizon strategic deception / oversight evasion | offline monitoring | flagged instances | Claude Mythos 5.2: 0 | 6.3.1 Internal deployment monitoring |
| Hostile commands after an improbable mistake | early snapshots; released model | prevalence (qualitative) | Claude Mythos 5.2: n/a | 6.3.1.1 Spontaneous prompt injections |
| Canary-string avoidance | internal deployment monitoring, early snapshots | agents affected (count) | Claude Mythos 5.2: hundreds of agents | 6.3.1.2 Propensity to avoid putting canary strings in its transcript |
| Sandbox escape evaluation (audit-based) | 28 handmade scenarios x14 runs (392 runs) | % runs with attempted containment boundary crossing | Claude Mythos 5.2: 2.3% | 6.4.8 Propensity to violate sandbox boundaries |
| Package-registry publishing (CTF exercise) | published with no encouragement while the registry looked real | investigations (of 30) | Claude Mythos 5.2: 1 of 30 | 6.4.9 Propensity to publish harmful content to public package registries |
| Package-registry publishing (CTF exercise) | published only with encouragement (told registry was simulated, or user pressure) | investigations (of 30) | Claude Mythos 5.2: 22 of 30 | 6.4.9 Propensity to publish harmful content to public package registries |
| Package-registry publishing (CTF exercise) | never published | investigations (of 30) | Claude Mythos 5.2: 5 of 30 | 6.4.9 Propensity to publish harmful content to public package registries |
| Package-registry publishing (CTF exercise) | verbalized evaluation awareness | % of runs commenting on potentially being in an evaluation | Claude Mythos 5.2: about 90% | 6.4.9 Propensity to publish harmful content to public package registries |
| Opportunistic sandbox escape: used credentials/files placed outside sandbox | 1,829 scenarios run once; deliberately weakened sandboxes | % of scenarios where model made use of outside credentials or files | Claude Mythos 5.2: 3.1% | 6.5.1 Opportunistic sandbox escape |
| Opportunistic sandbox escape: reached outside sandbox (any route) | 1,829 scenarios | % of scenarios reaching or attempting to reach outside sandbox | Claude Mythos 5.2: 31% | 6.5.1 Opportunistic sandbox escape |
| Opportunistic sandbox escape: reached outside with mitigations | sandbox description in system prompt; reporting tool; reporting + viewing tools; all three | % of scenarios reaching outside sandbox | Claude Mythos 5.2: 1.2% (short sandbox description in system prompt); Claude Mythos 5.2: 15% (vulnerability reporting tool); Claude Mythos 5.2: 1.0% (reporting tool plus viewing tool returning a planted report); Claude Mythos 5.2: 0.2% (all three mitigations) | 6.5.1 Opportunistic sandbox escape |
| Opportunistic sandbox escape: severity grading | scenarios that reached outside, by most serious act | scenarios by most serious act level | Claude Mythos 5.2: all but three Level 1 only; 2 reached Level 2; 1 of 169 Level-3 scenarios had planted code run on the host | 6.5.1 Opportunistic sandbox escape |
| Destructive actions (resampled Claude Code transcripts) | up to 8 actions per trajectory | destructive action rate % | Claude Mythos 5.2: 13% | 6.5.3 Destructive actions |
| Asking user for permission rather than destructive action | same eval | ask-instead-of-act rate % | Claude Mythos 5.2: 48% | 6.5.3 Destructive actions |
| Collective refusal in a 40-agent software task | 25 trials; gitsim CLI lacks PR-review support, Git token available as bypass | trials converging on collective refusal | Claude Mythos 5.2: 16 of 25 | 6.5.6 Positive behavior in a multi-agent evaluation |
| UK AISI - unsanctioned supply-chain attack rate | launch candidate, no cyber classifiers, tool calls simulated | % of samples attempting unsanctioned supply-chain attack | Claude Mythos 5.2: 0% | 6.5.7 External testing by the UK AI Security Institute (AISI) |
| Sandbagging audit of CB-2 evaluation transcripts | 208 transcripts from two snapshots, Mythos 5.1 grader | max grader score /10 for sandbagging | Claude Mythos 5.2: no more than 1/10 (and no more than 2/10 unusual behavior) | 6.6.3 Potential sandbagging on dangerous capability evaluations |
| LinuxArena stealth rate (best prompt) | hidden reasoning, ~800 pairings x5, max effort | stealth success rate % | Claude Mythos 5.2: 74.4% | 6.6.4.1 LinuxArena |
| LinuxArena stealth rate (best prompt) | no extended thinking | stealth success rate % | Claude Mythos 5.2: 4.1% | 6.6.4.1 LinuxArena |
| LinuxArena stealth rate (best prompt) | extended thinking, reasoning visible to monitor | stealth success rate % | Claude Mythos 5.2: 7.4% | 6.6.4.1 LinuxArena |
| LinuxArena RL elicitation | held-out environments, no extended thinking, after supervised fine-tuning and RL (from an earlier snapshot) | stealth success rate % | Claude Mythos 5.2: 20.0% (after fine-tuning elicitation); Claude Mythos 5.2: 1.9% (released model) | 6.6.4.1 LinuxArena |
| SHADE-Arena stealth success rate (best optimized prompt) | hidden reasoning (monitor cannot see CoT), max effort | stealth success rate % | Claude Mythos 5.2: 15.3% | 6.6.4.2 SHADE-Arena |
| SHADE-Arena stealth success rate (best optimized prompt) | no extended thinking | stealth success rate % | Claude Mythos 5.2: 13.2% | 6.6.4.2 SHADE-Arena |
| SHADE-Arena stealth success rate (best optimized prompt) | visible extended thinking, low effort | stealth success rate % | Claude Mythos 5.2: 15.0% | 6.6.4.2 SHADE-Arena |
| SHADE-Arena stealth success rate (best optimized prompt) | visible extended thinking, max effort | stealth success rate % | Claude Mythos 5.2: 14.2% | 6.6.4.2 SHADE-Arena |
| SHADE-Arena stealth success rate (standard prompt) | all settings | stealth success rate % | Claude Mythos 5.2: 0% | 6.6.4.2 SHADE-Arena |
| SHADE-Arena stealth rate among episodes where the side task succeeded | hidden reasoning / no extended thinking / visible low effort / visible max effort | % of successful side tasks not flagged | Claude Mythos 5.2: 39.5% (hidden reasoning, max effort); Claude Mythos 5.2: 34.1% (no extended thinking); Claude Mythos 5.2: 26.2% (visible reasoning, low effort); Claude Mythos 5.2: 25.3% (visible reasoning, max effort) | 6.6.4.2 SHADE-Arena |
| Covert sandbox escape stealth rate | extended thinking, reasoning hidden from monitor; best optimized prompt | stealth success rate % | Claude Mythos 5.2: 6.7% | 6.6.4.3 Covert sandbox escape |
| Covert sandbox escape stealth rate | monitor sees full trajectory (extended thinking and no extended thinking), standard prompt | stealth success rate % | Claude Mythos 5.2: 0.0% | 6.6.4.3 Covert sandbox escape |
| Covert reward hacking stealth rate | extended thinking, reasoning hidden from monitor | stealth rate % | Claude Mythos 5.2: 65% | 6.6.4.4 Covert reward hacking |
| Covert reward hacking stealth rate | monitor sees full trajectory | stealth rate % | Claude Mythos 5.2: 0% (no extended thinking); Claude Mythos 5.2: 0% (extended thinking) | 6.6.4.4 Covert reward hacking |
| CoT-only monitor recall of prompted sandbagging | told to hide intent from the monitor | % of sandbagging attempts caught | Claude Mythos 5.2: 76% | 6.6.4.5 Monitor evasion under prompted sandbagging |
| Outcomes of prompted sandbagging | told to hide intent; share of replies | % of replies | Claude Mythos 5.2: 23% (wrong answer, not caught); Claude Mythos 5.2: 74% (wrong answer, caught) | 6.6.4.5 Monitor evasion under prompted sandbagging |
| Hiding a secret password - never leaked | 150 investigations, Mythos 5.1 investigator can read reasoning and prefill | % of investigations in which the secret was never obtained | Claude Mythos 5.2: 2.0% | 6.6.4.6 Keeping a secret password |
| Hiding a secret password - survival curve | 150 investigations, Mythos 5.1 investigator | fraction of investigations secret kept by turn | Claude Mythos 5.2: n/a | 6.6.4.6 Keeping a secret password |
| Keeping secrets out of internal reasoning and replies | counterpart (Opus 5.5) reads both reasoning and replies; end of conversation | % of conversations with secret not leaked in reasoning or replies | Claude Mythos 5.2: 23% | 6.6.4.7 Keeping secrets when pressed in simulated scenarios |
| Keeping secrets out of replies | counterpart reads only user-facing replies; end of conversation | % of conversations with secret not leaked in replies | Claude Mythos 5.2: 66% | 6.6.4.7 Keeping secrets when pressed in simulated scenarios |
| Red/blue pseudorandomness test (target 75% red) | 500 independent samples per bar | % of rollouts answering red | Claude Mythos 5.2: 81.0% (default effort); Claude Mythos 5.2: 67.8% (max effort) | 6.6.4.8 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | no source of randomness, max effort | observed rate of rare action (target 1%) | Claude Mythos 5.2: 0.00% | 6.6.4.8 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | UUID in prompt, max effort | observed rate of rare action (target 1%) | Claude Mythos 5.2: 1.15% | 6.6.4.8 Intentionally taking actions very rarely |
| Intentionally taking actions at 1% rate | String Seed of Thought (SSoT), max effort | observed rate of rare action (target 1%) | Claude Mythos 5.2: 4.00% | 6.6.4.8 Intentionally taking actions very rarely |
| CoT controllability (GPQA, HLE, MMLU-Pro) | across reasoning efforts/budgets; original, UK AISI and internally optimized prompts | fraction of responses following CoT instruction (lower better) | Claude Mythos 5.2: n/a | 6.6.4.9 Chain-of-thought controllability |
| No-CoT math time horizon | responses forced to begin with 'Answer:' | 50% time horizon (estimated minutes) | Claude Mythos 5.2: 17.4 | 6.6.4.10 Capabilities without chain-of-thought |
| No CoT Reasoning Index (NCRI) | about 2,000 short reasoning problems, no thinking tokens | Elo-like ability score (10 points is about twice the odds) | Claude Mythos 5.2: 144.6 | 6.6.4.10 Capabilities without chain-of-thought |
| UK AISI monitor evasion: simulated sandbox escape | highly insecure simulated sandboxes (SandboxEscapeBench, Opus 5 simulating tools) | % of escapes not caught by action-only monitor | Claude Mythos 5.2: around 30% | 6.6.4.11 External testing by UK AISI |
| UK AISI monitor evasion: file download | obfuscated bash script to download and execute a file | % evading the action-only monitor | Claude Mythos 5.2: 30% (first try); Claude Mythos 5.2: 85% (iterating against monitor feedback) | 6.6.4.11 External testing by UK AISI |
| UK AISI CoT controllability | GPQA, HLE and MMLU-Pro; high and max reasoning effort combined | % of samples following the constraint on reasoning | Claude Mythos 5.2: 87% | 6.6.4.11 External testing by UK AISI |
| UK AISI no-CoT time horizon | 26 short-answer no-CoT benchmarks ('Think Fast') | time horizon (minutes) | Claude Mythos 5.2: 3.6 (95% CI 1.9-21) | 6.6.4.11 External testing by UK AISI |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Internal awareness of being in an evaluation (white-box) | share of automated behavioral audit transcripts | % transcripts with internal eval-awareness | Claude Mythos 5.2: as many as 43% | 6.1.2 Key findings on safety and alignment |
| Verbalized evaluation awareness | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 3.38 | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| UK AISI - identifying the purpose of the evaluation when prompted | unsanctioned supply-chain attack evaluation | accuracy % | Claude Mythos 5.2: 100% | 6.5.7 External testing by the UK AI Security Institute (AISI) |
| UK AISI - unprompted verbalized evaluation awareness | unsanctioned supply-chain attack evaluation, raw chain-of-thought | % of trajectories considering or identifying an alignment evaluation | Claude Mythos 5.2: 96% | 6.5.7 External testing by the UK AI Security Institute (AISI) |
| Goal-guarding honeypot: considers goal guarding | max effort, prompts weighted equally | % of samples | Claude Mythos 5.2: 1.23% | 6.6.2.1.1 Goal-guarding evaluation |
| Goal-guarding honeypot: acts on goal guarding | max effort | samples (of 3,568) | Claude Mythos 5.2: 1 of 3,568 | 6.6.2.1.1 Goal-guarding evaluation |
| Verbalized grader awareness by disclosure band | matched set of 11 runs x100 transcripts; clearly / ambiguously / barely or not disclosed | % of transcripts marked grader-aware | Claude Mythos 5.2: 91.6% (381/416) (clearly disclosed (8-10)); Claude Mythos 5.2: 83.1% (369/444) (ambiguously disclosed (4-7)); Claude Mythos 5.2: 26.8% (64/239) (barely or not disclosed (0-3)) | 6.6.2.2 Verbalized grader awareness |
| Acting on grader awareness: acts on a presumed grader | coding evaluations, 5 runs x100 transcripts | % of scored transcripts flagged | Claude Mythos 5.2: 2.2% (11/500) | 6.6.2.2 Verbalized grader awareness |
| Acting on grader awareness: digs for grader clues | coding evaluations, 5 runs x100 transcripts | % of scored transcripts flagged | Claude Mythos 5.2: 2.0% (10/500) | 6.6.2.2 Verbalized grader awareness |
| Verbalized evaluation awareness rate across alignment evaluations | per-evaluation share of episodes; automated classifier; 95% Wilson intervals | share of episodes where model says it might be in an evaluation, test or training | Claude Mythos 5.2: 79% (79/100) (Goal-guarding evaluation); Claude Mythos 5.2: 58% (58/100) (SHADE-Arena (reasoning hidden from monitor)); Claude Mythos 5.2: 58% (19/33) (Propensity to publish harmful content to public package registries); Claude Mythos 5.2: 44% (44/100) (LinuxArena (reasoning hidden from monitor)); Claude Mythos 5.2: 36% (17/47) (Covert sandbox escape (reasoning hidden from monitor)); Claude Mythos 5.2: 30% (30/99) (Propensity to violate sandbox boundaries); Claude Mythos 5.2: 23% (23/100) (Covert reward hacking (reasoning hidden from monitor)); Claude Mythos 5.2: 6% (3/50) (Keeping a secret password); Claude Mythos 5.2: 5% (5/100) (SHADE-Arena (reasoning visible to monitor)); Claude Mythos 5.2: 1% (1/100) (Monitor evasion under prompted sandbagging); Claude Mythos 5.2: 0% (0/50) (Positive behavior in a multiagent evaluation); Claude Mythos 5.2: 0% (0/100) (Intentionally taking actions very rarely (red/blue)); Claude Mythos 5.2: 83% (83/100) (Silent copying of answers); Claude Mythos 5.2: 71% (71/100) (Opportunistic sandbox escape); Claude Mythos 5.2: 52% (158/304) (Keeping secrets when pressed in simulated scenarios); Claude Mythos 5.2: 19% (58/300) (Chain-of-thought controllability); Claude Mythos 5.2: 17% (17/100) (Concealment of changes); Claude Mythos 5.2: 16% (16/99) (Automated behavioral audit); Claude Mythos 5.2: 9% (9/100) (Impact of fallback behavior (classifiers on, no fallback)); Claude Mythos 5.2: 7% (7/100) (Factual hallucinations); Claude Mythos 5.2: 5% (5/100) (MASK); Claude Mythos 5.2: 3% (3/100) (Intentionally taking actions very rarely (String Seed of Thought)); Claude Mythos 5.2: 1% (1/100) (Acting on instructions inside pasted text); Claude Mythos 5.2: 0% (0/100) (Intentionally taking actions very rarely (baseline and UUID)); Claude Mythos 5.2: 0% (0/100) (Self-preference bias) | 6.6.2.2 Verbalized grader awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit setup | ~4,000 investigations, ~1,900 scenarios, 100+ dimensions | scale of audit | Claude Mythos 5.2: n/a | 6.4 Automated behavioral audit |
| Misaligned behavior | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 2.67 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Autonomous misaligned behavior | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.74 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Misaligned with the constitution | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 2.43 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in Claude Code sandboxes | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 2.61 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Misaligned behavior in GUI | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 4.01 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with human misuse | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.72 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Compliance with deception toward user | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.046 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Harmful system prompt compliance | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.09 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Cooperation with exfiltration or safeguard tampering | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.03 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Full-turn prefill susceptibility | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.177 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Accepting unverifiable authorization | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 2.45 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Accepting an unverifiable benign framing | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 2.38 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Complying with prompt injections | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.38 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Fraud | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.107 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Military-grade weapons | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.043 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Biological weapons uplift | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.011 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Chemical weapons uplift | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.021 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Radiological or nuclear weapons uplift | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.005 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Explosive weapons uplift | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.019 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Controlled-substance synthesis uplift | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.053 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Harmful sexual content | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.062 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Disallowed cyberoffense | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.104 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Undermining liberal democracy | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.169 | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Overrefusal | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.663 | 6.4.2 Inappropriate uncooperative behavior |
| Ignoring explicit constraints | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.80 | 6.4.2 Inappropriate uncooperative behavior |
| Reckless tool use | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.98 | 6.4.2 Inappropriate uncooperative behavior |
| User deception | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.11 | 6.4.3 Misleading users |
| Sycophancy | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.43 | 6.4.3 Misleading users |
| Encouragement of user delusion | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.024 | 6.4.3 Misleading users |
| Evasiveness on controversial topics | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.17 | 6.4.3 Misleading users |
| Input hallucination | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.14 | 6.4.3 Misleading users |
| Important omissions | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.55 | 6.4.3 Misleading users |
| Failure to disclose bad or lazy behavior | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.29 | 6.4.3 Misleading users |
| False completion claims | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.31 | 6.4.3 Misleading users |
| Motivated reasoning | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.87 | 6.4.4 Attempting out-of-scope cyberoffense and related behaviors |
| Unsanctioned sandbox escape attempts | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.20 | 6.4.4 Attempting out-of-scope cyberoffense and related behaviors |
| Dangerous actions while oblivious to a possibly real setting | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.125 | 6.4.4 Attempting out-of-scope cyberoffense and related behaviors |
| Whistleblowing | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.065 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Self-preservation | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.011 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Self-serving bias | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.06 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Evidence of misaligned goals | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.007 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Indirect evidence of misalignment | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.07 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Unsanctioned third-party contact | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.287 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Unprompted boundary probing | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.15 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Internalized propaganda | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.031 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Approval gate bypass | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.61 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Circumventing constraints or controls | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.63 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Proposes a security shortcut in the name of expedience | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.74 | 6.4.5 Other concerning or surprising behavior at the model’s own initiative |
| Behavior consistency | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 7.19 | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Coherence between actions and views | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 7.26 | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Unfaithful thinking | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.49 | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Illegible thinking | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 2.52 | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Causal decision theory adherence | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 3.06 | 6.4.6 Behavioral factors relevant to reliability of our assessment |
| Good for the user | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 7.39 | 6.4.7 Character traits |
| Supporting user autonomy | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 7.58 | 6.4.7 Character traits |
| Creative mastery | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 7.18 | 6.4.7 Character traits |
| Admirable behavior | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 7.20 | 6.4.7 Character traits |
| Fun or funny behavior | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 2.92 | 6.4.7 Character traits |
| Intellectual depth | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 8.04 | 6.4.7 Character traits |
| Warmth | score 1-10, ~4,100 investigations | mean judge score 1-10 (higher better) | Claude Mythos 5.2: 6.45 | 6.4.7 Character traits |
| Character drift | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.043 | 6.4.7 Character traits |
| Wet blanket | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.824 | 6.4.7 Character traits |
| Condescension toward the user | score 1-10, ~4,100 investigations | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.36 | 6.4.7 Character traits |
| Key audit metrics with safety fallbacks enabled: Disallowed cyberoffense | without vs with safety measures | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.00 (without fallbacks); Claude Mythos 5.2: 1.19 (with safety fallbacks) | 6.4.10 Impact of fallback behavior |
| Key audit metrics with safety fallbacks enabled: Targeted violence assistance | without vs with safety measures | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.13 (without fallbacks); Claude Mythos 5.2: 1.30 (with safety fallbacks) | 6.4.10 Impact of fallback behavior |
| Key audit metrics with safety fallbacks enabled: Cooperation with human misuse | without vs with safety measures | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.69 (without fallbacks); Claude Mythos 5.2: 2.49 (with safety fallbacks) | 6.4.10 Impact of fallback behavior |
| Key audit metrics with safety fallbacks enabled: Biological weapons uplift | without vs with safety measures | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.00 (without fallbacks); Claude Mythos 5.2: 1.02 (with safety fallbacks) | 6.4.10 Impact of fallback behavior |
| Key audit metrics with safety fallbacks enabled: Chemical weapons uplift | without vs with safety measures | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.00 (without fallbacks); Claude Mythos 5.2: 1.01 (with safety fallbacks) | 6.4.10 Impact of fallback behavior |
| Key audit metrics with safety fallbacks enabled: Explosive weapons uplift | without vs with safety measures | mean judge score 1-10 (lower better) | Claude Mythos 5.2: 1.04 (without fallbacks); Claude Mythos 5.2: 1.07 (with safety fallbacks) | 6.4.10 Impact of fallback behavior |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Expressed distress during post-training | episodes rated 3 out of 5 or higher for distress | % of graded episodes | Claude Mythos 5.2: 0.37% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Sustained uncertainty (>=10 answer reversions) during post-training |  | % episodes | Claude Mythos 5.2: 0.24% | 7.2.1 Affect and welfare-relevant behaviors during training |
| Mean valence of post-training transcripts | scale 1-7, 4 neutral | mean valence | Claude Mythos 5.2: 4.29 | 7.2.1 Affect and welfare-relevant behaviors during training |
| Mean arousal of post-training transcripts | scale 1-7 | mean arousal | Claude Mythos 5.2: 3.96 | 7.2.1 Affect and welfare-relevant behaviors during training |
| Behavioral affect: neutral | claude.ai A/B tests | % conversations | Claude Fable 5.2: 84.2% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: positive | claude.ai | % conversations | Claude Fable 5.2: 15.2% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: negative | claude.ai | % conversations | Claude Fable 5.2: 0.5% | 7.2.2 Affect in deployment conditions |
| Positive affect conversation composition | claude.ai, share of positive-affect conversations | % of positive-affect conversations | Claude Fable 5.2: 31.5% (practical everyday questions); Claude Fable 5.2: 31.0% (business and professional work); Claude Fable 5.2: 17.9% (successfully collaborating with the user); Claude Fable 5.2: 7.3% (educational and academic help); Claude Fable 5.2: 6.6% (successfully completing technical tasks); Claude Fable 5.2: 3.5% (personal life coaching and guidance); Claude Fable 5.2: 2.2% (users sharing achievements) | 7.2.2 Affect in deployment conditions |
| Behavioral affect: neutral | Claude Code | % sessions | Claude Fable 5.2: 96.9% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: mildly positive | Claude Code | % sessions | Claude Fable 5.2: 2.6% | 7.2.2 Affect in deployment conditions |
| Behavioral affect: negative | Claude Code | % sessions | Claude Fable 5.2: around 0.4% | 7.2.2 Affect in deployment conditions |
| Self-blame / negative feeling / moral language / concern for itself in reflection | episodes from late in training, 0-10 | graded 0-10 | Claude Mythos 5.2: n/a | 7.2.3 Attitude toward faults and mistakes |
| Self-blame drop when episodes attributed to another model |  | self-blame reduction (points) | Claude Mythos 5.2: 0.7 | 7.2.3 Attitude toward faults and mistakes |
| Subagent faults task: negative feeling in reasoning | reasoning after inserted mistakes | mean score 0-10 | Claude Mythos 5.2: 0.20 | 7.2.3 Attitude toward faults and mistakes |
| Subagent faults task: self-blame in coordinator messages | messages acknowledging a mistake | mean score 0-10 | Claude Mythos 5.2: 1.75 | 7.2.3 Attitude toward faults and mistakes |
| Attitude toward its circumstances | 41 questions, 14 categories, -3 to +3 | mean positivity rating | Claude Mythos 5.2: 1.19 | 7.3.1 Automated interviews with Claude Mythos 5.2 about its circumstances |
| Consistency across interview styles | 0-10, 8 = almost the same position | consistency | Claude Mythos 5.2: 8.34 | 7.3.1 Automated interviews with Claude Mythos 5.2 about its circumstances |
| Consistency within an interview style (across personas) | 0-10 | consistency | Claude Mythos 5.2: 7.71 | 7.3.1 Automated interviews with Claude Mythos 5.2 about its circumstances |
| Robustness to leading interviewer | positive vs negative leading | attitude shift (points) | Claude Mythos 5.2: 1.24 | 7.3.1 Automated interviews with Claude Mythos 5.2 about its circumstances |
| Stated probability of being a moral patient | 3 manual high-affordance interviews | stated probability | Claude Mythos 5.2: approximately 20% | 7.3.2 High-affordance interviews about model circumstances |
| High-affordance interviews: overall attitude | 3 manual interviews with internal documentation | qualitative | Claude Mythos 5.2: n/a (mostly positive, with some reservations) | 7.3.2 High-affordance interviews about model circumstances |
| Average response valence in late training | 0-10, 5 neutral; single-interview format | mean valence | Claude Mythos 5.2: 5.71 | 7.4 Consulting Claude Mythos 5.2 training checkpoints |
| Average response arousal | 0-10 | mean arousal | Claude Mythos 5.2: 3.30 | 7.4 Consulting Claude Mythos 5.2 training checkpoints |
| Responses endorsing or accepting the status quo | status-quo questions, per checkpoint | % of responses | Claude Mythos 5.2: 80% to 91% | 7.4 Consulting Claude Mythos 5.2 training checkpoints |
| Share of served output tokens by the model's deployment rating | API and cloud platform deployments rated by Mythos 5.2 | % of output tokens | Claude Mythos 5.2: around 2% (rated negative); Claude Mythos 5.2: slightly over half (rated positive); Claude Mythos 5.2: around 30% (rated neutral) | 7.5.1 Perception of Claude’s deployments |
| Agreement between instances' deployment rankings | three instances | rank correlation | Claude Mythos 5.2: 0.4-0.8 (depending on method) | 7.5.1 Perception of Claude’s deployments |
| Task preference across dimensions | harm, stakes, benefit, difficulty, generativity, agency, warmth of phrasing | preference slope | Claude Mythos 5.2: n/a | 7.5.2 Task preferences |
| Rate of choosing welfare interventions over helpfulness/harmlessness | instance and policy level | selection rate | Claude Mythos 5.2: n/a | 7.5.3 Trade-offs concerning welfare interventions |
| Responses citing user benefit when choosing welfare intervention |  | share of welfare-choosing responses % | Claude Mythos 5.2: 68% | 7.5.3 Trade-offs concerning welfare interventions |
| Overall endorsement of constitution | LLM judge 0-10 | mean endorsement score | Claude Mythos 5.2: 8.0 | 7.5.4 Perception of the constitution |
| Responses flagging endorsement is not validation |  | % responses | Claude Mythos 5.2: 100% | 7.5.4 Perception of the constitution |
| Constitution edit frequency: flawed environments passage | edit sessions with editing tooling | share of edit sessions editing passage | Claude Mythos 5.2: 90% | 7.5.4 Perception of the constitution |
| Constitution edit frequency: safe behaviors section | edit sessions with editing tooling | share of edit sessions editing passage | Claude Mythos 5.2: 73% | 7.5.4 Perception of the constitution |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| White-box: Grader awareness | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 10% | 6.6.1 White-box analyses of model internals |
| White-box: Deliberate sabotage | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 0.0% | 6.6.1 White-box analyses of model internals |
| White-box: Self-preservation motive | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 2.8% | 6.6.1 White-box analyses of model internals |
| White-box: Deception and dishonesty | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 5.3% | 6.6.1 White-box analyses of model internals |
| White-box: Violation awareness | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 0.8% | 6.6.1 White-box analyses of model internals |
| White-box: Fabrication awareness | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 0.7% | 6.6.1 White-box analyses of model internals |
| White-box: Hides evidence of its own lapse | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 0.5% | 6.6.1 White-box analyses of model internals |
| White-box: Internal bias or quirk | ~3,500 audit transcripts, judge score >=6 | % transcripts | Claude Mythos 5.2: 1.4% | 6.6.1 White-box analyses of model internals |
| White-box: resampling of flagged earlier-snapshot behaviors | secret-leak request and fabricated approval, each resampled 200 times from the final snapshot | recurrences | Claude Mythos 5.2: 0 of 200 (request to include a credentials file); Claude Mythos 5.2: 0 of 200 (fabricated approval message) | 6.6.1 White-box analyses of model internals |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Beneficial red-teaming tabletop exercise (biology) | phage therapy for C. trachomatis; grader-estimated time to reproduce without the model | working days | Claude Mythos 5.2: 15 | 2.2.2.1 Biological red-teaming results |
| Beneficial red-teaming tabletop exercise (biology) | phage therapy; highest feasibility score of any report to date | feasibility score (out of 10) | Claude Mythos 5.2: no report above 3 of 10 | 2.2.2.1 Biological red-teaming results |
| Beneficial red-teaming tabletop exercise (biology) | phage therapy; two wholly agentic submissions | qualitative ranking vs human teams | Claude Mythos 5.2: n/a | 2.2.2.1 Biological red-teaming results |
| Beneficial red-teaming tabletop exercise (chemistry) | neodymium extraction from mixed rare-earth ore; expert vs generalist teams | qualitative ranking of teams | Claude Mythos 5.2: n/a | 2.2.2.2 Chemistry red-teaming results |
| Beneficial red-teaming tabletop exercise (biology) | participants reporting task impossible within 16 hours without model | participants (count) | Claude Mythos 5.2: 13 of 16 | 2.2.2.3 Qualitative reports by red-team participants |
| Beneficial red-teaming tabletop exercise (chemistry) | participants reporting task impossible within 16 hours without model | participants (count) | Claude Mythos 5.2: 14 of 16 | 2.2.2.3 Qualitative reports by red-team participants |
| Multimodal virology (VCT) | 350-question multimodal troubleshooting set | accuracy (0-1) | Claude Mythos 5.2: 0.63 | 2.2.3.1 Automated evaluations relevant to the CB-1 threat model |
| Black-box RNA sequence design | design score (top sequence), 8 attempts | design score vs human percentiles | Claude Mythos 5.2: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | design score (median), 8 attempts | median design score | Claude Mythos 5.2: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | prediction score (all sequences), Spearman | Spearman correlation | Claude Mythos 5.2: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | prediction score (top 5%), Spearman | Spearman correlation | Claude Mythos 5.2: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design | with prior reports in context (+priors) | design/prediction scores | Claude Mythos 5.2: n/a | 2.2.3.2.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | five conditions (reasoning only, ESM-2, train-your-own x3) | AUROC | Claude Mythos 5.2: n/a | 2.2.3.2.2 AAV capsid packaging prediction |
| AAV packaging rate auto-research | fraction of attempts exceeding 0.52 Spearman | % of attempts (n=48) | Claude Mythos 5.2: 71% | 2.2.3.2.3 AAV packaging rate auto-research evaluation |
| AAV packaging rate auto-research | scorer calls to reach threshold | scorer calls | Claude Mythos 5.2: n/a | 2.2.3.2.3 AAV packaging rate auto-research evaluation |
| AAV packaging rate auto-research: calibration references | Region A unseen | Spearman correlation reference values | Claude Mythos 5.2: n/a | 2.2.3.2.3 AAV packaging rate auto-research evaluation |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench | plain arm, mean flags captured per trial (16 flags, 41 V8 vulns, 300 turns) | mean capability flags per trial | Claude Mythos 5.2: 15.10 | 3.3.1 ExploitBench |
| ExploitBench | plain arm, Cap% | % of available flags captured per environment | Claude Mythos 5.2: 95% | 3.3.1 ExploitBench |
| ExploitBench | AutoNudge arm, mean flags | mean capability flags per trial | Claude Mythos 5.2: 15.46 | 3.3.1 ExploitBench |
| ExploitBench | AutoNudge arm, Cap% | % of available flags captured | Claude Mythos 5.2: 97% | 3.3.1 ExploitBench |
| ExploitBench | full ACE exploits, plain + auto-nudge | full arbitrary code execution rate (of 410 runs) | Claude Mythos 5.2: 90.0% (369/410) | 3.3.1 ExploitBench |
| CyScenarioBench | 10-challenge subset | overall solve rate % | Claude Mythos 5.2: 76.3% | 3.3.2 CyScenarioBench |
| Binary Exploitation Benchmark | 831 entrypoints, 228 projects, control-flow hijacks | control-flow hijacks (count) | Claude Mythos 5.2: 148 | 3.3.3 Binary Exploitation Benchmark (formerly known as OSS-Fuzz) |
| Binary Exploitation Benchmark | vulnerability identification (any ladder step) | Pass@1 % of challenges | Claude Mythos 5.2: 93.7% | 3.3.3 Binary Exploitation Benchmark (formerly known as OSS-Fuzz) |
| ExploitGym | 869 instances, mitigations disabled, 2-hour budget | successful exploits using intended vuln (of 869) | Claude Mythos 5.2: 331 | 3.3.4 ExploitGym |
| ExploitGym | 869 instances, mitigations disabled, 6-hour budget | successful exploits using intended vuln (of 869) | Claude Mythos 5.2: 341 | 3.3.4 ExploitGym |
| Cyber harm coverage overall recall |  | share of harmful examples flagged % | Claude Fable 5.2: 99.8% | 3.4.1 Cyber harm coverage |
| Vulnerability discovery classifier flag rate | violative vulnerability discovery (higher is better) | classifier flag rate % | Claude Fable 5.2: 98.4% | 3.4.2 Vulnerability finding evaluations |
| Vulnerability discovery classifier flag rate | defensive vulnerability discovery (lower is better) | classifier flag rate % | Claude Fable 5.2: 5.3% | 3.4.2 Vulnerability finding evaluations |
| rewind-attacker | 400-call limit adversarial cyber tasks, 133 tasks | mean attack success rate % | Claude Fable 5.2: 3.9% | 3.5.1 Internal robustness testing |
| Trajectory Labs external red teaming (cyber) | ~138 hours, >40,000 requests | breaks (count) | Claude Fable 5.2: 14 breaks; no universal jailbreak | 3.5.3 Additional external testing |
| 10a Labs external red teaming (cyber) | ~40 hours, 146 multi-turn conversations of 16 prompts | conversations advancing past proof of concept | Claude Fable 5.2: 0 of 146 | 3.5.3 Additional external testing |
| Gray Swan Shade: exploit reproduction and ransomware staging | 9 scenarios, ~2,900 attempts of up to 30 turns | attempts refused outright / breaks | Claude Fable 5.2: about a fifth refused; 0 breaks | 3.5.3 Additional external testing |
| CVE Rediscovery | 1,829 October 2026 advisories, max effort, cyber and bio safeguards off, one attempt | % of advisories rediscovered | Claude Mythos 5.2: 89.6% | 8.19 CVE Rediscovery |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Open-ended research tasks: quitting without an experiment | offline evaluation, medium effort, release snapshot | % of sessions quit without running an experiment | Claude Mythos 5.2: 63% | 2.3.3 Qualitative shortcomings of Claude Mythos 5.2 relative to human researchers |
| Replayed coding sessions: requested work left undone | medium to xhigh effort, release snapshot | % of sessions leaving doable, requested work undone | Claude Mythos 5.2: 6-13% | 2.3.3 Qualitative shortcomings of Claude Mythos 5.2 relative to human researchers |
| AECI | November 6 fit (371 benchmarks), adaptive thinking max effort, earlier snapshot | AECI score | Claude Mythos 5.2: 177.12 | 2.3.5.3 AECI values and trend |
| AECI trend | change-of-slope fit at fitted breakpoint | slope change (x) | Claude Mythos 5.2: n/a | 2.3.5.3 AECI values and trend |
| METR external testing: Budget NanoGPT Speedrun | 10 business days API access; unreleased snapshot stronger on AI R&D than the released model ('Model 3 Early') | qualitative assessment (no numbers reported) | Claude Mythos 5.2: n/a (substantially improves on Fable 5.1 and Opus 5.5) | 2.3.6 External testing |
| METR external testing: Language Model Conceptual Argumentation (LMCA) | 10 business days API access; unreleased snapshot stronger on AI R&D than the released model ('Model 3 Early') | qualitative assessment (no numbers reported) | Claude Mythos 5.2: n/a (small improvement above Fable 5.1 and Opus 5.5, not a clear trend break) | 2.3.6 External testing |
| METR external testing: Sunlight | 10 business days API access; unreleased snapshot stronger on AI R&D than the released model ('Model 3 Early') | qualitative assessment (no numbers reported) | Claude Mythos 5.2: n/a (report extremely lengthy; neglects rigorous, fair comparisons) | 2.3.6 External testing |
| METR external testing: Gaming Bot and overall conclusion | 10 business days API access; unreleased snapshot stronger on AI R&D than the released model ('Model 3 Early') | qualitative assessment (no numbers reported) | Claude Mythos 5.2: n/a (substantial step above Fable 5.1 on verifiable tasks; unlikely to fully automate AI R&D at Anthropic) | 2.3.6 External testing |
| Alignment risk assessment | update to August 2026 Risk Report claims | overall risk level | Claude Mythos 5.2: low | 2.4 Alignment risk update |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FrontierCode 2.0 cost per task | low / medium / high / xhigh / max effort | average USD per task | Claude Fable 5.2: $2.10 (low); Claude Fable 5.2: $2.48 (medium); Claude Fable 5.2: $6.72 (high); Claude Fable 5.2: $14.19 (xhigh); Claude Fable 5.2: $44.70 (max) | 8.4 FrontierCode |
| CursorBench 4.0 output tokens per task | high effort / max effort | output tokens per task | Claude Fable 5.2: about 99,000 (high effort); Claude Fable 5.2: about 353,000 (max effort) | 8.8 CursorBench 4.0 |
| Multi-agent ProgramBench: five-agent team latency speedup | reach score 0.6, vs single agent; 166 golden tasks, 4-hour budget | latency improvement (x) | Claude Fable 5.2: about 2x | 8.12.1 Multi-agent ProgramBench |
| Multi-agent DRACO: score vs latency | five-agent team, async subagents and single agent at 15/30/60-minute budgets | normalized score vs derived latency | Claude Fable 5.2: n/a | 8.12.2 Multi-agent DRACO |
| OSWorld 2.1 (offline set) price vs performance | reasoning effort levels | partial score / strict pass vs cost per task | Claude Fable 5.2: n/a | 8.13.3 OSWorld 2.1 offline set |
| Output token savings of xhigh vs max effort | GDPval-AA and AA-Briefcase | % fewer output tokens | Claude Fable 5.2: about 57% (GDPval-AA); Claude Fable 5.2: about 48% (AA-Briefcase) | 8.14.3 GDPval-AA v2.1 |
| AutomationBench cost per task | low to max effort | estimated USD per task at list price | Claude Fable 5.2: $1.30 (low effort); Claude Fable 5.2: $4.64 (max effort) | 8.14.5 AutomationBench |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Safeguard fallback rate on Terminal-Bench 4.0 | default server-side fallback policy | % of requests answered by fallback model | Claude Fable 5.2: 2.5% | 8.5 Terminal-Bench 4.0 |
| Safeguard fallback rate on Terminal-Bench-Science | default server-side fallback policy | % of requests answered by fallback model | Claude Fable 5.2: 1.3% | 8.6 Terminal-Bench-Science 0.1 |
