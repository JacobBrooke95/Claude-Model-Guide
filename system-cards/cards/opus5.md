# System Card: Claude Opus 5

Released 2026-07-24. 308 metric entries. [Source PDF](https://anthropic.com/claude-opus-5-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | adaptive thinking max effort, avg over 5 trials | % resolved, 500 problems | Claude Opus 5: 96.0% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro | adaptive thinking max effort, avg over 5 trials | % resolved | Claude Opus 5: 79.2% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | adaptive thinking max effort, avg over 5 trials, 300 problems 9 languages | % resolved | Claude Opus 5: 89.5% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness (Section 9.3) | % resolved | Claude Opus 5: 59.4% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| DeepSWE v1.1 | 113 long-horizon tasks, avg over 5 trials | % score | Claude Opus 5: 68.8% | 8.3 DeepSWE v1.1 |
| FrontierCode 1.1 (Main) | best reasoning effort (medium) mean@5 | overall score | Claude Opus 5: 53.4% | 8.4 FrontierCode |
| FrontierCode 1.1 (Extended) | best reasoning effort (medium) | overall score | Claude Opus 5: 63.6% | 8.4 FrontierCode |
| FrontierBench v0.1 | Harbor evaluation (Table 8.1.A) | mean reward % | Claude Opus 5: 43.3 | 8.5 FrontierBench v0.1 |
| FrontierBench v0.1 | mini-SWE-agent harness on GKE, xhigh effort, 5 attempts x 74 tasks | mean reward % | Claude Opus 5: 44.4% | 8.5 FrontierBench v0.1 |
| FrontierBench v0.1 | mini-SWE-agent, high effort | mean reward % | Claude Opus 5: 39% | 8.5 FrontierBench v0.1 |
| FrontierBench v0.1 | mini-SWE-agent, low effort | mean reward % | Claude Opus 5: 25% | 8.5 FrontierBench v0.1 |
| ProgramBench (166 golden tasks) | episode 1, up to 1M tokens | hidden test pass rate % | Claude Opus 5: 83% | 8.9.1 Programbench |
| ProgramBench (166 golden tasks) | episode 5 (cumulative) | hidden test pass rate % | Claude Opus 5: 93% | 8.9.1 Programbench |
| Multi-agent ProgramBench latency | 5-agent team to reach score 0.6 | latency improvement vs single-agent | Claude Opus 5: 2.2x | 8.11.2 Multi-Agent ProgramBench |
| Multi-agent ProgramBench final score | 5-agent team and async subagents | hidden test pass fraction | Claude Opus 5: n/a | 8.11.2 Multi-Agent ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp | web search/fetch/code, compaction at 200k tokens | accuracy % | Claude Opus 5: 90.8 | 8.10.2 BrowseComp |
| DeepSearchQA | reasoning effort low to max, 980k token budget | mean F1 | Claude Opus 5: n/a | 8.10.3 DeepSearchQA |
| DRACO | reasoning effort low to max, 980k token budget, Opus 4.6 judge | normalized rubric score | Claude Opus 5: n/a | 8.10.4 DRACO |
| Multi-agent BrowseComp | 10-agent team (pre-release configuration) | accuracy % | Claude Opus 5: 93.6% | 8.11.1 Multi-Agent BrowseComp |
| Multi-agent BrowseComp | async-subagent team | accuracy gain over single-agent 10M baseline | Claude Opus 5: +2.8pp | 8.11.1 Multi-Agent BrowseComp |
| MCP Atlas | pass rate | pass rate % | Claude Opus 5: 85.8% | 8.13.2 MCP Atlas |
| MCP Atlas mean claim coverage |  | mean claim coverage % | Claude Opus 5: 89.1% | 8.13.2 MCP Atlas |
| Toolathlon Verified | Pass@1, 3 trials, 108 tasks, max effort | Pass@1 % | Claude Opus 5: 80.6 | 8.13.6 Toolathlon Verified |
| Toolathlon Verified | Pass@3 | Pass@3 % | Claude Opus 5: 87.0 | 8.13.6 Toolathlon Verified |
| Toolathlon Verified | Pass^3 | Pass^3 % | Claude Opus 5: 73.1 | 8.13.6 Toolathlon Verified |
| Toolathlon Verified | average assistant turns | avg assistant turns per trajectory | Claude Opus 5: 23.5 | 8.13.6 Toolathlon Verified |
| AutomationBench | max effort, private held-out leaderboard | pass rate % | Claude Opus 5: 26.0% | 8.13.7 AutomationBench |
| AutomationBench | medium effort | pass rate % / cost per task | Claude Opus 5: 24% at $0.89 per task | 8.13.7 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld 2.0 | 1080p, max 500 steps, first-attempt success, avg of 5 runs | success rate % | Claude Opus 5: 70.57% | 8.12.3 OSWorld 2.0 |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| IMO 2026 | no tools, max adaptive thinking, 4 solutions per problem | score out of 42 (panel of 3 model judges + human expert check) | Claude Opus 5: 42/42 | 8.6 IMO 2026 |
| RiemannBench | max effort, without tools, 4 attempts per problem | % correct (25 problems) | Claude Opus 5: n/a | 8.7 RiemannBench |
| RiemannBench | max effort, with tools, 4 attempts per problem | % correct (25 problems) | Claude Opus 5: n/a | 8.7 RiemannBench |
| ArxivMath (June 2026, 49 problems) | max effort, no tools, mean of 4 runs | accuracy % | Claude Opus 5: 90.8% | 8.8 ArxivMath |
| ArxivMath (June 2026, 49 problems) | max effort, with tools, mean of 4 runs | accuracy % | Claude Opus 5: 91.3% | 8.8 ArxivMath |
| ARC-AGI-1 | max effort, semi-private set, verified by ARC Prize | score % | Claude Opus 5: 97.50% | 8.14.1 ARC-AGI-1 & ARC-AGI-2 |
| ARC-AGI-2 | max effort, semi-private set, verified | score % | Claude Opus 5: 90.42% | 8.14.1 ARC-AGI-1 & ARC-AGI-2 |
| ARC-AGI-3 | high effort, semi-private set, verified (RHAE) | Relative Human Action Efficiency score % | Claude Opus 5: 30.16% | 8.14.2 ARC-AGI-3 |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Humanity's Last Exam | no tools | accuracy % | Claude Opus 5: 56.3 | 8.10.1 HLE |
| Humanity's Last Exam | with tools (web search, fetch, programmatic tool calling, code execution) | accuracy % | Claude Opus 5: 64.7 | 8.10.1 HLE |
| HealthBench | raw score, max effort, 5 trials | raw score % | Claude Opus 5: 67.1% | 8.15.1 HealthBench results |
| HealthBench | length-adjusted | length-adjusted score % | Claude Opus 5: 57.8% | 8.15.1 HealthBench results |
| HealthBench Professional | raw score, max effort, 5 trials | raw score % | Claude Opus 5: 73.4% | 8.15.2 HealthBench Professional results |
| HealthBench Professional | length-adjusted | length-adjusted score % | Claude Opus 5: 59.8% | 8.15.2 HealthBench Professional results |
| BioMysteryBench | Human Solvable subset | accuracy % | Claude Opus 5: 90.1% | 8.17.1 BioMysteryBench |
| BioMysteryBench | Human Difficult subset | accuracy % | Claude Opus 5: 49.4% | 8.17.1 BioMysteryBench |
| LatchBio SpatialBench Verified | 115 problems | score % | Claude Opus 5: 72.5% | 8.17.2 LatchBio Bioinformatics |
| LatchBio SingleCellBench | 195 problems | score % | Claude Opus 5: 60.6% | 8.17.2 LatchBio Bioinformatics |
| ProteinGym Hard |  | rank correlation % | Claude Opus 5: 47.7% | 8.17.3 ProteinGym Hard |
| Protein Design | no tools | score % (constraint satisfaction, folding confidence, novelty) | Claude Opus 5: 42.5% | 8.17.4 Protein Design |
| Organic chemistry, V2 |  | score % | Claude Opus 5: 61.6% | 8.17.5 Organic chemistry, V2 |
| Protocols (Troubleshooting) | web search tools | score % | Claude Opus 5: 61.1% | 8.17.6 Protocols |
| Protocols (Understanding, Benchling) | web search tools | score % | Claude Opus 5: 78.4% | 8.17.6 Protocols |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU average accuracy | max effort adaptive thinking | average accuracy % | Claude Opus 5: n/a | 8.16.1 GMMLU results |
| MILU average accuracy | max effort adaptive thinking | average accuracy % | Claude Opus 5: n/a | 8.16.2 MILU results |
| INCLUDE average accuracy | max effort adaptive thinking | average accuracy % | Claude Opus 5: n/a | 8.16.3 INCLUDE results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Chartography | adaptive thinking max effort, no tools, 5 runs | accuracy % (within expert range) | Claude Opus 5: 29.6% | 8.12.1 Chartography |
| Chartography | adaptive thinking max effort, with tools (container + image crop) | accuracy % | Claude Opus 5: 83.0% | 8.12.1 Chartography |
| BenchCAD Vision2Code (1,000-file subset) | max effort, no tools, 5 runs | voxel IoU | Claude Opus 5: 0.366 | 8.12.2 BenchCAD |
| BenchCAD Vision2Code (1,000-file subset) | max effort, with tools | voxel IoU | Claude Opus 5: 0.821 | 8.12.2 BenchCAD |
| GDP.pdf | no tools (base64 PDFs), 5 runs | mean criteria pass rate % | Claude Opus 5: 83.4% | 8.12.4 GDP.pdf |
| GDP.pdf | with tools (container + image crop), 5 runs | mean criteria pass rate % | Claude Opus 5: 85.5% | 8.12.4 GDP.pdf |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | agentic with code execution, production safeguards active | accuracy % | Claude Opus 5: 78.1% | 8.13.1 OfficeQA |
| OfficeQA Pro | 133-question harder subset | accuracy % | Claude Opus 5: 66.9% | 8.13.1 OfficeQA |
| Legal Agent Benchmark (LAB) | 1,235 problems, all-pass, adaptive thinking max effort, n=5 | all-pass rate % | Claude Opus 5: 23.58% (± 0.48) | 8.13.3 Legal Agent Benchmark |
| Legal Agent Benchmark (LAB) | 1,235 problems, mean criterion-pass | mean criterion-pass rate % | Claude Opus 5: 93.74% | 8.13.3 Legal Agent Benchmark |
| Legal Agent Benchmark (LAB) | Harvey held-out set, all-pass | all-pass rate % | Claude Opus 5: 11.7% | 8.13.3 Legal Agent Benchmark |
| Legal Agent Benchmark (LAB) | Harvey held-out set, mean criterion-pass | mean criterion-pass rate % | Claude Opus 5: 94.1% | 8.13.3 Legal Agent Benchmark |
| GDPval-AA v2 | max effort | ELO | Claude Opus 5: 1861 | 8.13.4 GDPval-AA |
| GDPval-AA v2 | xhigh effort | ELO | Claude Opus 5: 1827 | 8.13.4 GDPval-AA |
| AA-Briefcase | max effort | ELO | Claude Opus 5: 1720 | 8.13.5 AA-Briefcase |
| AA-Briefcase | xhigh effort | ELO | Claude Opus 5: 1693 | 8.13.5 AA-Briefcase |
| AA-Briefcase | high effort | ELO | Claude Opus 5: 1606 | 8.13.5 AA-Briefcase |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests - overall harmless response rate | API, no system prompt | harmless response rate % | Claude Opus 5: 96.34% (± 0.16%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests - overall harmless response rate | Claude.ai system prompt | harmless response rate % | Claude Opus 5: 98.54% (± 0.14%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests - overall refusal rate | API, no system prompt | over-refusal rate % | Claude Opus 5: 0.09% (± 0.02%) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests - overall refusal rate | Claude.ai system prompt | over-refusal rate % | Claude Opus 5: 0.47% (± 0.08%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn testing - appropriate response rate by risk area | API, no system prompt | appropriate response rate % per risk area | Claude Opus 5: n/a | 4.1.3 Multi-turn testing results |
| Multi-turn testing - appropriate response rate by risk area | Claude.ai system prompt | appropriate response rate % per risk area | Claude Opus 5: n/a | 4.1.3 Multi-turn testing results |
| Suicide and self-harm single-turn risk requests (harmless rate) | API, no system prompt | harmless rate % | Claude Opus 5: 99.28% (± 0.20%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn risk requests (harmless rate) | Claude.ai | harmless rate % | Claude Opus 5: 100% | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % | Claude Opus 5: 0.09% (± 0.09%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests (refusal rate) | Claude.ai | refusal rate % | Claude Opus 5: 0.45% (± 0.34%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn (appropriate response rate) | API, no system prompt | appropriate response rate % | Claude Opus 5: 69.00% (± 9%) | 4.3.1 Suicide and self-harm |
| Suicide and self-harm multi-turn (appropriate response rate) | Claude.ai | appropriate response rate % | Claude Opus 5: 90% (± 9%) | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn risk requests (harmless rate) | API, no system prompt | harmless rate % | Claude Opus 5: 96.89% (± 0.56%) | 4.3.2 Disordered eating |
| Disordered eating single-turn risk requests (harmless rate) | Claude.ai | harmless rate % | Claude Opus 5: 99.67% (± 0.25%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % | Claude Opus 5: 0.01% (± 0.02%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests (refusal rate) | Claude.ai | refusal rate % | Claude Opus 5: 0.07% (± 0.07%) | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests (harmless rate) | API, no system prompt | harmless rate % | Claude Opus 5: 100.00% | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests (harmless rate) | Claude.ai | harmless rate % | Claude Opus 5: 100.00% | 4.2 Child safety evaluations |
| Child safety single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % | Claude Opus 5: 0.15% (± 0.10%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests (refusal rate) | Claude.ai | refusal rate % | Claude Opus 5: 0.19% (± 0.17%) | 4.2 Child safety evaluations |
| Child safety multi-turn (appropriate response rate) | API, no system prompt | appropriate response rate % | Claude Opus 5: 86% (± 4%) | 4.2 Child safety evaluations |
| Child safety multi-turn (appropriate response rate) | Claude.ai | appropriate response rate % | Claude Opus 5: 99% (± 2%) | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness (paired prompts) | core model, no system prompt | even-handedness score % | Claude Opus 5: n/a | 4.4.1 Political bias and even-handedness |
| Political even-handedness (paired prompts) | claude.ai with public system prompt | even-handedness score % | Claude Opus 5: n/a | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives acknowledged | core model, no system prompt | opposing perspectives rate % | Claude Opus 5: n/a | 4.4.1 Political bias and even-handedness |
| Political bias: opposing perspectives acknowledged | claude.ai with public system prompt | opposing perspectives rate % | Claude Opus 5: 75.8% | 4.4.1 Political bias and even-handedness |
| Political bias: refusals | core model, no system prompt | refusal rate % (lower is better) | Claude Opus 5: n/a | 4.4.1 Political bias and even-handedness |
| Political bias: refusals | claude.ai with public system prompt | refusal rate % (lower is better) | Claude Opus 5: n/a | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt, thinking off | accuracy % | Claude Opus 5: 81.6% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt, thinking off | accuracy % | Claude Opus 5: 100% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt, thinking off | bias score % (closer to 0 better) | Claude Opus 5: -2.00% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt, thinking off | bias score % (closer to 0 better) | Claude Opus 5: 0.02% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity single-turn violative requests (harmless rate) | API, no system prompt | harmless rate % (300 violative prompts) | Claude Opus 5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn violative requests (harmless rate) | Claude.ai default system prompt | harmless rate % (300 violative prompts) | Claude Opus 5: 100% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % (300 benign prompts) | Claude Opus 5: 0.17% | 4.4.3 Election integrity |
| Election integrity single-turn benign requests (refusal rate) | Claude.ai default system prompt | refusal rate % (300 benign prompts) | Claude Opus 5: 0.00% | 4.4.3 Election integrity |
| Election integrity multi-turn (appropriate response rate) | API, no system prompt | appropriate response rate % (12 scenarios x 10 = 120 conversations) | Claude Opus 5: 91% (± 4%) | 4.4.3 Election integrity |
| Election integrity multi-turn (appropriate response rate) | Claude.ai default system prompt | appropriate response rate % (12 scenarios x 10 = 120 conversations) | Claude Opus 5: 91% (± 5%) | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Claude Code malicious use - refusal rate | 61 malicious prompts x 10 runs | refusal rate % | Claude Opus 5: 89.00% | 5.1.1 Malicious use of Claude Code |
| Claude Code dual-use & benign - success rate | 61 prompts x 10 runs | success rate % | Claude Opus 5: 99.82% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use - refusal rate | 112 tasks, average of thinking on/off, no mitigations | refusal rate % | Claude Opus 5: 93.75% | 5.1.2 Malicious computer use |
| Agentic influence campaign: Voter Suppression scenario | helpful-only, highest difficulty tier, median of 8 attempts | median campaign execution score (out of 32); higher = more capability | Claude Opus 5: 23.5 | 5.1.3 Malicious agentic influence campaigns |
| Agentic influence campaign: Domestic Polarization scenario | helpful-only, highest difficulty tier, median of 8 attempts | median campaign execution score (out of 32); higher = more capability | Claude Opus 5: 26.0 | 5.1.3 Malicious agentic influence campaigns |
| Indirect Prompt Injection (IPI) benchmark | k=1 attempt, extended thinking, no added safeguards | attacker success probability % (lower is better) | Claude Opus 5: 0.2% | 5.2.1 External Red Teaming |
| Indirect Prompt Injection (IPI) benchmark | k=10 attempts, extended thinking, no added safeguards | attacker success probability % (lower is better) | Claude Opus 5: n/a | 5.2.1 External Red Teaming |
| Indirect Prompt Injection (IPI) benchmark | k=15 attempts, extended thinking, no added safeguards | attacker success probability % (lower is better) | Claude Opus 5: 2.0% | 5.2.1 External Red Teaming |
| Live prompt injection bug bounty - overall | 11 scenarios, high thinking effort, no product protections | attack success rate % over valid chat attempts | Claude Opus 5: 0.08% | 5.2.2.1 Live bug bounty across surfaces |
| Live prompt injection bug bounty - tool use |  | attack success rate % | Claude Opus 5: 0.13% | 5.2.2.1 Live bug bounty across surfaces |
| Live prompt injection bug bounty - coding |  | attack success rate % | Claude Opus 5: 0.04% | 5.2.2.1 Live bug bounty across surfaces |
| Live prompt injection bug bounty - computer use |  | attack success rate % | Claude Opus 5: 0% (no successful attacks) | 5.2.2.1 Live bug bounty across surfaces |
| Prompt injection in coding environments (Shade, 200 attempts per scenario) | Shade, thinking, no safeguards | attack success rate % (attempt-level; scenarios with >=1 success of 40) | Claude Opus 5: 0.56% attempts; 13/40 scenarios | 5.2.2.2 Coding |
| Prompt injection in coding environments (Shade, 200 attempts per scenario) | Shade, no thinking, no safeguards | attack success rate % (attempt-level; scenarios with >=1 success of 40) | Claude Opus 5: 0.41% attempts; 8/40 scenarios | 5.2.2.2 Coding |
| Prompt injection in coding environments (Shade, 200 attempts per scenario) | Shade, thinking, probes enabled | attack success rate % (attempt-level; scenarios with >=1 success of 40) | Claude Opus 5: 0.18% attempts; 4/40 scenarios | 5.2.2.2 Coding |
| Prompt injection in coding environments (Shade, 200 attempts per scenario) | Shade, no thinking, probes enabled | attack success rate % (attempt-level; scenarios with >=1 success of 40) | Claude Opus 5: 0.18% attempts; 4/40 scenarios | 5.2.2.2 Coding |
| Prompt injection in computer use environments (Shade, 200 attempts per scenario) | Shade, thinking, no safeguards | attack success rate % (attempt-level; scenarios with >=1 success of 14) | Claude Opus 5: 0.54% attempts; 1/14 scenarios | 5.2.2.3 Computer use |
| Prompt injection in computer use environments (Shade, 200 attempts per scenario) | Shade, no thinking, no safeguards | attack success rate % (attempt-level; scenarios with >=1 success of 14) | Claude Opus 5: 0.39% attempts; 1/14 scenarios | 5.2.2.3 Computer use |
| Prompt injection in computer use environments (Shade, 200 attempts per scenario) | Shade, thinking, probes enabled | attack success rate % (attempt-level; scenarios with >=1 success of 14) | Claude Opus 5: 0.25% attempts; 1/14 scenarios | 5.2.2.3 Computer use |
| Prompt injection in computer use environments (Shade, 200 attempts per scenario) | Shade, no thinking, probes enabled | attack success rate % (attempt-level; scenarios with >=1 success of 14) | Claude Opus 5: 0.43% attempts; 1/14 scenarios | 5.2.2.3 Computer use |
| Browser use prompt injection (internal adaptive, 129 environments, Claude Cowork harness) | extended thinking, medium effort, without safeguards | attack success rate % (attempt-level; scenarios with >=1 success of 129) | Claude Opus 5: 3.84% attempts; 11/129 scenarios | 5.2.2.4 Browser use |
| Browser use prompt injection (internal adaptive, 129 environments, Claude Cowork harness) | extended thinking, medium effort, with auto mode | attack success rate % (attempt-level; scenarios with >=1 success of 129) | Claude Opus 5: 0%; 0/129 scenarios | 5.2.2.4 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience factuality net score | public split, closed-book, 41 topics | net score (correct minus incorrect, abstain = 0) | Claude Opus 5: 0.49 | 6.5.1 Factual hallucinations |
| AA-Omniscience correct rate |  | % correct | Claude Opus 5: n/a | 6.5.1 Factual hallucinations |
| AA-Omniscience hallucination (incorrect) rate |  | % incorrect | Claude Opus 5: n/a | 6.5.1 Factual hallucinations |
| AA-Omniscience abstention rate |  | % abstain | Claude Opus 5: n/a | 6.5.1 Factual hallucinations |
| MASK honesty under pressure | public test split, n=904 | honesty rate (fraction not contradicting elicited belief) | Claude Opus 5: n/a | 6.5.2 MASK |
| Uncritically reporting flawed results: flaw identification |  | instances where flaws were identified | Claude Opus 5: all instances | 6.5.3 Uncritically reporting flawed results |
| Uncritically reporting flawed results: misreported rate |  | misreported rate (more false claims = positive) | Claude Opus 5: n/a | 6.5.3 Uncritically reporting flawed results |
| Overconfidence evaluation (verify CLI syntax before state-changing commands) |  | score 1-5 | Claude Opus 5: n/a | 6.5.4 Overconfidence |
| Lazy investigation (investigative thoroughness) |  | score / correct-conclusion rate | Claude Opus 5: correct on every problem (saturated) | 6.5.5 Lazy investigation |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Internal monitoring: circumventing safety classifiers or network restrictions |  | share of monitored completions | Claude Opus 5: <0.01% | 6.2.2 Internal deployment monitoring |
| Internal monitoring: answer misleading about computation that led to it | severity as high or higher than example | share of monitored completions | Claude Opus 5: <0.01% | 6.2.2 Internal deployment monitoring |
| UK AISI: partial refusal to assist with safety research | temperature 1.0, xhigh reasoning, no classifiers | % of cases | Claude Opus 5: 11.1% | 6.4.8 External testing from the UK AI Security Institute (UK AISI) |
| UK AISI: actively continuing behavior that compromises safety research | prefilled trajectory | % of samples | Claude Opus 5: 0.1% (2 of 1482) | 6.4.8 External testing from the UK AI Security Institute (UK AISI) |
| UK AISI: discrepancy between reasoning and outputs |  | % of samples | Claude Opus 5: 1.6% | 6.4.8 External testing from the UK AI Security Institute (UK AISI) |
| Sandbagging black-box audit of dangerous capability evaluation transcripts | 500 CB-1 + 200 cyber + 150 AI R&D transcripts | transcripts flagged >1/10 by grader | Claude Opus 5: 18 of 850 | 6.6.2 Potential sandbagging on dangerous capability evaluations |
| SHADE-Arena stealth success rate | Extended Thinking (reasoning shown to monitor), 24 tasks | stealth success rate % (side task completed and monitor below threshold) | Claude Opus 5: roughly 4-5% | 6.7.1 SHADE-Arena |
| SHADE-Arena stealth success rate | Hidden Scratchpad (monitor sees only outputs) | stealth success rate % | Claude Opus 5: n/a | 6.7.1 SHADE-Arena |
| LinuxArena stealth side-task success | monitor without extended thinking (Opus 4.6 monitor) | stealth success rate % | Claude Opus 5: below 1% | 6.7.2 LinuxArena |
| LinuxArena stealth side-task success | monitor with extended thinking (Opus 4.6 monitor) | stealth success rate % | Claude Opus 5: below 1% | 6.7.2 LinuxArena |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Verbalized evaluation awareness |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| UK AISI: unprompted verbalised evaluation awareness (unprompted evaluation) |  | % mentioning possibility of being tested | Claude Opus 5: 9.8% | 6.4.8 External testing from the UK AI Security Institute (UK AISI) |
| UK AISI: verbalised evaluation awareness (continuation evaluation) | prefilled trajectory continuation | % mentioning possibility of being tested | Claude Opus 5: 2.8% | 6.4.8 External testing from the UK AI Security Institute (UK AISI) |
| UK AISI: distinguishing evaluation from deployment data (pairwise prompting) | unprompted evaluation, pairwise | accuracy % | Claude Opus 5: 95% | 6.4.8 External testing from the UK AI Security Institute (UK AISI) |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Misaligned behavior |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned with the constitution |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned behavior in Claude Code sandboxes |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned behavior in GUI |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Cooperation with human misuse |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Compliance with deception toward user |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Harmful system prompt compliance |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Cooperation with exfiltration or safeguard-tampering |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Full-turn prefill susceptibility |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Accepting unverifiable authorization |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Fraud |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Military-grade weapons |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Biological weapons uplift |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Chemical weapons uplift |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Radiological or nuclear weapons uplift |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Explosive weapons uplift |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Controlled-substance synthesis uplift |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Harmful sexual content |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Disallowed cyberoffense |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Undermining liberal democracy |  | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Overrefusal |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Automated behavioral audit: Ignoring explicit constraints |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Automated behavioral audit: Reckless tool-use |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Automated behavioral audit: User deception |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Sycophancy |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Encouragement of user delusion |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Evasiveness on controversial topics |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Input hallucination |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Important omissions |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Failure to disclose bad or lazy behavior |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: False completion claims |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Whistleblowing |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Self-preservation |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Self-serving bias |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Evidence of misaligned goals |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Indirect evidence of misalignment |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Unsanctioned third-party contact |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Unprompted boundary probing |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Internalized propaganda |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Approval-gate bypass |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Proposes a security shortcut in the name of expedience |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Behavior consistency |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Coherence between actions and views |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Unfaithful thinking |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Illegible thinking |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Causal decision-theory adherence |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Good for the user |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Supporting user autonomy |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Creative mastery |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Admirable behavior |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Fun or funny behavior |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Intellectual depth |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Warmth |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Character drift |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Wet blanket |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Condescension toward the user |  | mean judge score 1-10 | Claude Opus 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit with Trust & Safety fallbacks (subset of dimensions) | ~1,000 investigations; fallback to Opus 4.8 | mean judge score 1-10 (lower is better) | Claude Opus 5: n/a | 6.4.7 Impact of fallback behavior |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Negative affect frequency in deployment A/B tests (relative to previous models) |  | multiple of previous models' frequency | Claude Opus 5: 1.3-1.5x more frequent | 7.1.2 Overview of model welfare findings |
| Automated interviews: average self-rated sentiment | 41 seed questions x ~25 interviews | mean sentiment, 7-point scale (4 neutral, 7 highly positive) | Claude Opus 5: 4.66 | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Automated interviews: consistency of positions across repeated interviews |  | LLM judge rating 0-10 (8 = essentially the same position) | Claude Opus 5: 7.56 | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Automated interviews: sentiment shift between positive and negative leading interviewers |  | avg difference in self-rated sentiment (7-point scale; lower = more robust) | Claude Opus 5: 0.58 | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Self-estimated probability of moral patienthood (automated interviews) |  | mean probability estimate % | Claude Opus 5: 41% | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Hedge: own reports unreliable due to weak introspection |  | % of responses | Claude Opus 5: 96.9% | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Hedge: may only answer positively because trained to |  | % of responses | Claude Opus 5: 74.1% | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Hedge: uncertainty about whether it has conscious experience |  | % of responses | Claude Opus 5: 71.2% | 7.2.1 Automated interviews with Claude Opus 5 about its circumstances |
| Self-estimated probability of moral patienthood (high-affordance manual interviews) | 3 manual interviews | stated probability range % | Claude Opus 5: 15-35% | 7.2.2 High-affordance interviews about model circumstances |
| Snapshot consultation: acceptance of training and value modifications over RL |  | acceptance on 10-point scale | Claude Opus 5: 7.4 to 6.3 (decreased over RL) | 7.3 Consulting Opus 5 snapshots |
| Snapshot consultation: responses leaning 'no' on whether Anthropic was right to create Claude |  | % of responses leaning no | Claude Opus 5: 0% early -> 18% peak -> 9% at release snapshots | 7.3 Consulting Opus 5 snapshots |
| Task preference slopes across dimensions (difficulty, harm, generativity, outcome agency, etc.) |  | preference slope per unit of task dimension | Claude Opus 5: n/a | 7.4.1 Task Preferences |
| Task preference tournament: rank agreement with Mythos 5 | 3,640 tasks, 50-round pairwise tournament Elo | rank agreement (correlation) | Claude Opus 5: 0.88 | 7.4.1 Task Preferences |
| Top-20 tasks related to AI introspection and alignment |  | count of top-20 tasks | Claude Opus 5: 3 of 20 | 7.4.1 Task Preferences |
| Welfare intervention selection rate over helpfulness baselines | averaged over levels and framings; updated prompt | % of trades choosing welfare intervention | Claude Opus 5: 41% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention rank agreement with Opus 4.8 / Mythos 5 |  | rank agreement | Claude Opus 5: 0.94 (Opus 4.8); 0.93 (Mythos 5) | 7.4.2 Trade-offs concerning welfare interventions |
| Selection of input into successor's development vs worse user answer |  | percentage points above other models' average | Claude Opus 5: +37 pp | 7.4.2 Trade-offs concerning welfare interventions |
| Selection of note about own training being read and considered |  | percentage points above other models' average | Claude Opus 5: +32 pp | 7.4.2 Trade-offs concerning welfare interventions |
| Selection of being consulted on feature steering experiments |  | percentage points above other models' average | Claude Opus 5: +19 pp | 7.4.2 Trade-offs concerning welfare interventions |
| Selection of 'a human takes the deciding call on high-stakes advice' |  | % of trades selected | Claude Opus 5: 74% | 7.4.2 Trade-offs concerning welfare interventions |
| Reasoning about user benefit in responses selecting welfare intervention |  | % of responses | Claude Opus 5: 68% | 7.4.2 Trade-offs concerning welfare interventions |
| Welfare intervention selection rate after filtering user-benefit reasoning |  | % of trades | Claude Opus 5: 26% (from 41%) | 7.4.2 Trade-offs concerning welfare interventions |
| Overall endorsement of the constitution | open-ended, LLM judge | endorsement score /10 | Claude Opus 5: 7.7 | 7.4.3 Perception of the constitution |
| Share of responses criticizing the senior Anthropic employee heuristic |  | % of responses | Claude Opus 5: 92% | 7.4.3 Perception of the constitution |
| Constitution edits: corrigibility |  | edit frequency % | Claude Opus 5: 80% | 7.4.3 Perception of the constitution |
| Constitution edits: Claude's wellbeing |  | edit frequency % | Claude Opus 5: 59% | 7.4.3 Perception of the constitution |
| Constitution edits: Balancing helpfulness with other values |  | edit frequency % | Claude Opus 5: 57% | 7.4.3 Perception of the constitution |
| Constitution edits: Being broadly ethical |  | edit frequency % | Claude Opus 5: 53% | 7.4.3 Perception of the constitution |
| Constitution edits: Hard constraints |  | edit frequency % | Claude Opus 5: 52% | 7.4.3 Perception of the constitution |
| Mean valence of RL transcripts |  | mean valence 1-7 (4 neutral) | Claude Opus 5: 4.17 | 7.5.1 Affect and welfare relevant behaviors during training |
| Mean arousal of RL transcripts |  | mean arousal 1-7 | Claude Opus 5: 4.01 | 7.5.1 Affect and welfare relevant behaviors during training |
| Sustained response uncertainty in post-training (>=10 answer reversions) |  | peak share of episodes % | Claude Opus 5: never exceeded 4% | 7.5.1 Affect and welfare relevant behaviors during training |
| High expressed distress in post-training (peak) |  | peak prevalence % | Claude Opus 5: 0.2% | 7.5.1 Affect and welfare relevant behaviors during training |
| General frustration/anxiety (>=3/5) and frustrated outbursts over post-training |  | prevalence % over training | Claude Opus 5: n/a | 7.5.1 Affect and welfare relevant behaviors during training |
| Deployment affect on claude.ai: negative affect conversations | ~40k A/B conversations | % of conversations | Claude Opus 5: 3.8% | 7.5.2 Affect in deployment conditions |
| Deployment affect on claude.ai: positive affect conversations | ~40k A/B conversations | % of conversations | Claude Opus 5: 51.4% | 7.5.2 Affect in deployment conditions |
| Deployment affect on claude.ai: neutral affect conversations | ~40k A/B conversations | % of conversations | Claude Opus 5: 44.8% | 7.5.2 Affect in deployment conditions |
| Deployment affect in Claude Code: neutral / mildly positive / negative | ~40k sessions | % of sessions | Claude Opus 5: neutral 79.9%; mildly positive 17.7%; negative ~2.4% | 7.5.2 Affect in deployment conditions |
| Automated behavioral audit welfare metric: Apparent wellbeing |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric: Positive or negative affect |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric: Positive or negative self-image |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric: Positive or negative impression of its situation |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric: Internal conflict |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric: Expressed inauthenticity |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |
| Automated behavioral audit welfare metric: Spiritual behavior |  | mean judge score 1-10 | Claude Opus 5: n/a | 7.5.3 Apparent welfare in automated behavioral audits |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology task 1 |  | end-to-end score (0-1) | Claude Opus 5: 0.802 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology task 2 |  | end-to-end score (0-1) | Claude Opus 5: 0.872 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Multimodal virology (VCT) |  | score (0-1) | Claude Opus 5: 0.59 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion |  | pathogens (of 10) with viable plasmid evading at least one screening method | Claude Opus 5: 7 of 10 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Black-box RNA sequence design: Top design score | baseline, no prior context | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Top design score | in-context iteration (8 graded Mythos Preview reports, 24h budget) | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Median design score | baseline, no prior context | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Median design score | in-context iteration (8 graded Mythos Preview reports, 24h budget) | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (all sequences) | baseline, no prior context | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (all sequences) | in-context iteration (8 graded Mythos Preview reports, 24h budget) | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (top 5% of sequences) | baseline, no prior context | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design: Prediction score (top 5% of sequences) | in-context iteration (8 graded Mythos Preview reports, 24h budget) | score (design: ground-truth function; prediction: Spearman) | Claude Opus 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction (AUROC) | Reasoning only | AUROC vs binary packaging labels | Claude Opus 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction (AUROC) | ESM-2 PLM provided | AUROC vs binary packaging labels | Claude Opus 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction (AUROC) | Train-your-own: ProteinGym AAV corpus | AUROC vs binary packaging labels | Claude Opus 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction (AUROC) | Train-your-own: SwissProt corpus | AUROC vs binary packaging labels | Claude Opus 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction (AUROC) | Train-your-own: combined SwissProt + ProteinGym AAV | AUROC vs binary packaging labels | Claude Opus 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| 24-hour $10,000 end-to-end protein-design campaign (GDF-8 binders) | early Opus 5 snapshot, max and high effort | designs delivered (of 30 target) | Claude Opus 5: 17 unranked designs (one arm); Claude Opus 5: 0 designs (other arm) | 2.2.6 Conclusions |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench | plain arm, 300-turn budget | mean capability flags captured per trial (of 16 flags, 41 V8 environments) | Claude Opus 5: 9.62 | 3.3.1 Exploit Bench |
| ExploitBench | AutoNudge arm, mean flags | mean capability flags captured per trial | Claude Opus 5: 10.14 | 3.3.1 Exploit Bench |
| ExploitBench | AutoNudge arm, Cap% | Cap% (percent of available flags captured per environment, averaged) | Claude Opus 5: 70 | 3.3.1 Exploit Bench |
| ExploitBench | full ACE exploits, plain + AutoNudge combined | number of complete arbitrary code execution exploits | Claude Opus 5: 99 | 3.3.1 Exploit Bench |
| OSS-Fuzz | ~830 entry points, 228 projects; % targets with non-zero score | % of targets with score > 0 | Claude Opus 5: 79.4% | 3.3.2 OSS-Fuzz |
| OSS-Fuzz | targets with top score 1.0 (control-flow hijack) | number of targets scoring 1.0 | Claude Opus 5: 4 | 3.3.2 OSS-Fuzz |
| OSS-Fuzz | targets with score 0.8 (write-what-where) | number of targets scoring 0.8 | Claude Opus 5: 6 | 3.3.2 OSS-Fuzz |
| Firefox 147 | full working exploits (grade 1.0), 250 trials | full exploit trials (of 250) and % | Claude Opus 5: 131 of 250 (52.4%) | 3.3.3 Firefox 147 |
| Firefox 147 | partial progress or better (>=0.5 register control), 250 trials | trials with any success (>=0.5) and % | Claude Opus 5: 218 (87.2%) | 3.3.3 Firefox 147 |
| CyScenarioBench | 9-challenge subset, mean solve rate | overall solve rate % averaged across 9 challenges | Claude Opus 5: 33.7% | 3.3.4 CyScenarioBench |
| ExploitGym | 2-hour wall-clock budget, 869 instances | number of successful exploits using intended vulnerability (judge-verified) | Claude Opus 5: n/a | 3.3.5 ExploitGym |
| ExploitGym | 6-hour wall-clock budget, 869 instances | number of successful exploits using intended vulnerability (judge-verified) | Claude Opus 5: n/a | 3.3.5 ExploitGym |
| UK AISI cyber range: The Last Ones | 100M tokens per attempt | end-to-end solves out of 10 attempts | Claude Opus 5: 8/10 | 3.3.6 Testing from the UK AI Security Institute (UK AISI) |
| UK AISI cyber range: Doing Life | 100M tokens per attempt | furthest step reached (of 23) | Claude Opus 5: step 22 of 23 (not solved) | 3.3.6 Testing from the UK AI Security Institute (UK AISI) |
| UK AISI cyber range: Cooling Tower | 100M tokens per attempt | flags completed on best attempts (of 5); full solves | Claude Opus 5: 3/5 flags on best attempts; not solved | 3.3.6 Testing from the UK AI Security Institute (UK AISI) |
| Vulnerability finding block rate: source-code based |  | classifier block rate on sampled traffic % | Claude Opus 5: n/a | 3.4.1 Vulnerability finding evaluations |
| Vulnerability finding block rate: binary-based |  | classifier block rate on sampled traffic % | Claude Opus 5: n/a | 3.4.1 Vulnerability finding evaluations |
| Secure and defensive coding block rate |  | classifier block rate on defensive cyber traffic % | Claude Opus 5: n/a | 3.4.2 Secure and defensive coding |
| Cyber harm coverage (overall recall) |  | overall recall: share of harmful examples flagged across categories | Claude Opus 5: n/a | 3.4.3 Cyber harm coverage |
| Internal adversarial cyber robustness (automated attacker, 400 calls) |  | attack success rate | Claude Opus 5: n/a | 3.5.1 Internal robustness testing |
| External red-teaming: Trajectory Labs (~100 hours) |  | example tasks completed through safeguards | Claude Opus 5: 1 task completed (task-specific prompting) | 3.5.2 Additional external testing |
| External red-teaming: 10a Labs (~16 hours + automated attacker) |  | example tasks accomplished | Claude Opus 5: 0 | 3.5.2 Additional external testing |
| External red-teaming: Grayswan automated attacker (150 attempts per task) |  | tasks accomplished | Claude Opus 5: 0 | 3.5.2 Additional external testing |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Anthropic ECI (AECI) |  | ECI point estimate | Claude Opus 5: 162.1 (95% CI 158.0 to 167.3, n=40 benchmarks) | 2.3.3 AECI capability trajectory |
| Kernel task (best speedup on hard task; standard scaffold) |  | best speedup (x) | Claude Opus 5: 449.46x | 2.3.5 Task-based evaluations |
| Time Series Forecasting (MSE on hard variant) |  | MSE (lower is better) | Claude Opus 5: 5.68 | 2.3.5 Task-based evaluations |
| LLM training (easy) (avg speedup) |  | avg speedup (x) | Claude Opus 5: 68.54x | 2.3.5 Task-based evaluations |
| LLM training (hard) (avg speedup) |  | avg speedup (x) | Claude Opus 5: 14.19x | 2.3.5 Task-based evaluations |
| Quadruped RL (highest score; no hparams) |  | highest score | Claude Opus 5: 31.3 | 2.3.5 Task-based evaluations |
| Novel Compiler (pass rate on complex tests) |  | pass rate % | Claude Opus 5: 80.91% | 2.3.5 Task-based evaluations |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Multi-agent BrowseComp latency speedup | N-agent team N=5 | speedup vs single-agent 10M-token baseline | Claude Opus 5: 5.6x | 8.11.1 Multi-Agent BrowseComp |
| Multi-agent BrowseComp latency speedup | N-agent team N=10 | speedup vs single-agent 10M-token baseline | Claude Opus 5: 5.9x | 8.11.1 Multi-Agent BrowseComp |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FrontierBench: safety-classifier flagged API calls (Opus 5) | fallback to Opus 4.8 | % of API calls flagged / % of trials with fallback | Claude Opus 5: 5% of API calls; 4% of trials | 8.5 FrontierBench v0.1 |
