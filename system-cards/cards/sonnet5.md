# System Card: Claude Sonnet 5

Released 2026-06-30. 274 metric entries. [Source PDF](https://anthropic.com/claude-sonnet-5-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | standard config, avg 5 trials, 500 problems | resolved % | Claude Sonnet 5: 85.2% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro | standard config, avg 5 trials | resolved % | Claude Sonnet 5: 63.2% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, 9 languages, avg 5 trials | resolved % | Claude Sonnet 5: 78.3% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness, avg 5 trials | resolved % | Claude Sonnet 5: 28.1% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| Terminal-Bench 2.1 | mini-SWE-agent harness, xhigh effort, 89 tasks x5 attempts, GKE 1x timeout 3x memory | mean reward % | Claude Sonnet 5: 80.4% | 8.3 Terminal-Bench 2.1 |
| FrontierCode v1 | 150 tasks from Cognition; standard config | score % | Claude Sonnet 5: 38.8 | 8.4 FrontierCode |
| CursorBench | Cursor production harness | score % | Claude Sonnet 5: 61.2% | 8.5 CursorBench |
| ProgramBench | 166 tasks, hidden test pass rate across 5 episodes, 1M tokens each | hidden test pass rate % (range) | Claude Sonnet 5: 76-86% | 8.8 ProgramBench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp | single agent, max effort, 10M token limit with compaction at 200k | accuracy % | Claude Sonnet 5: 84.7 | 8.9.2 BrowseComp |
| BrowseComp | multi agent | accuracy % | Claude Sonnet 5: 86.6 | 8.9.2 BrowseComp |
| Toolathlon Pass@1 | 108 tasks, 3 trials, adaptive thinking max effort, internal harness | Pass@1 % | Claude Sonnet 5: 54.3 | 8.11.5 Toolathlon |
| Toolathlon Pass@3 | 108 tasks, 3 trials | Pass@3 % | Claude Sonnet 5: 63.0 | 8.11.5 Toolathlon |
| Toolathlon Pass^3 | 108 tasks, 3 trials | Pass^3 % | Claude Sonnet 5: 40.7 | 8.11.5 Toolathlon |
| AutomationBench | Zapier private held-out set, max effort | task pass rate % | Claude Sonnet 5: 13.5% | 8.11.6 AutomationBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld-Verified | 361 tasks, 100 steps, 1080p, max effort, avg 5 runs | pass@1 success % | Claude Sonnet 5: 81.2% | 8.10.2 OSWorld-Verified |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| USAMO 2026 | avg 10 attempts per problem, high effort, 300k token limit, min of 3 judges | score % | Claude Sonnet 5: 79.5% | 8.6 USAMO 2026 |
| ArxivMath | April+May 2026, 81 problems, no tools, extended thinking, 4 attempts | accuracy % | Claude Sonnet 5: 65.7% | 8.7 ArxivMath |
| ArxivMath | April+May 2026, with tools, 4 attempts | accuracy % | Claude Sonnet 5: 72.2% | 8.7 ArxivMath |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Humanity's Last Exam | no tools, thinking auto, 1M tokens | accuracy % | Claude Sonnet 5: 43.2 | 8.9.1 HLE |
| Humanity's Last Exam | with tools (web search, fetch, PTC, code exec) | accuracy % | Claude Sonnet 5: 57.4 | 8.9.1 HLE |
| HLE scores at varying reasoning effort levels | single run per effort level, 1M token cap | accuracy % by effort | Claude Sonnet 5: n/a | 8.9.1 HLE |
| HealthBench length-adjusted score | 5,000 conversations, Opus 4.8 grader, 5 trials, max effort | length-adjusted score | Claude Sonnet 5: n/a | 8.12.1 HealthBench results |
| HealthBench Professional length-adjusted score | 525 physician conversations, Opus 4.8 grader, 5 trials | length-adjusted score | Claude Sonnet 5: 57.8 | 8.12.2 HealthBench Professional results |
| BioMysteryBench - Human Solvable | human-solvable subset | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.1 BioMysteryBench |
| BioMysteryBench - Human Difficult | human-unsolved subset | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.1 BioMysteryBench |
| LatchBio SpatialBench Verified | 115 problems | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.2 LatchBio Bioinformatics |
| LatchBio SingleCellBench | 195 problems | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.2 LatchBio Bioinformatics |
| Structural biology, open-ended |  | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.3 Structural biology, open-ended |
| ProteinGym Hard |  | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.4 ProteinGym Hard |
| Organic chemistry |  | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.5 Organic chemistry |
| Protocol troubleshooting |  | task-specific 0-1 score | Claude Sonnet 5: n/a | 8.14.6 Protocol troubleshooting |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GMMLU average accuracy | 42 languages, single trial, max effort | average accuracy % | Claude Sonnet 5: n/a | 8.13.1 GMMLU results |
| MILU average accuracy | 11 languages, avg 5 trials | average accuracy % | Claude Sonnet 5: n/a | 8.13.2 MILU results |
| INCLUDE average accuracy | 44 languages, avg 5 trials | average accuracy % | Claude Sonnet 5: n/a | 8.13.3 INCLUDE results |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GDP.pdf | no tools, mean criteria pass rate, 100 prompts, 5 runs | mean criteria pass rate % | Claude Sonnet 5: 67.5% | 8.10.1 GDP.pdf |
| GDP.pdf | with tools (Python + image crop) | mean criteria pass rate % | Claude Sonnet 5: 81.6% | 8.10.1 GDP.pdf |
| BenchCAD Vision2Code | 1,000-file subset, no tools, voxel IoU, 5 runs | voxel IoU | Claude Sonnet 5: 0.266 | 8.10.3 BenchCAD |
| BenchCAD Vision2Code | 1,000-file subset, with tools | voxel IoU | Claude Sonnet 5: 0.373 | 8.10.3 BenchCAD |
| ChartMuseum | no tools, test split, avg 5 runs, Sonnet 4.6 grader | accuracy % | Claude Sonnet 5: 70.1% | 8.10.4 ChartMuseum |
| ChartMuseum | with Python tools + image crop | accuracy % | Claude Sonnet 5: 86.7% | 8.10.4 ChartMuseum |
| CharXiv Reasoning | no tools, 1,000 validation questions, avg 5 runs | accuracy % | Claude Sonnet 5: 77.0% | 8.10.5 CharXiv Reasoning |
| CharXiv Reasoning | with Python tools + image crop | accuracy % | Claude Sonnet 5: 88.3% | 8.10.5 CharXiv Reasoning |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | agentic, exact match, mean of 5 trials, max effort | exact-match accuracy % | Claude Sonnet 5: 73.3% | 8.11.1 OfficeQA |
| OfficeQA Pro | 133-question harder subset, exact match, mean of 5 trials | exact-match accuracy % | Claude Sonnet 5: 59.4% | 8.11.1 OfficeQA |
| Real-World Finance v2 | 294 tasks, pairwise Opus 4.8 grader, Bradley-Terry Elo | Elo | Claude Sonnet 5: 1219 | 8.11.2 Real-World Finance V2 |
| Real-World Finance v2 head-to-head win rate vs Sonnet 4.6 | pairwise | win rate % | Claude Sonnet 5: 69% | 8.11.2 Real-World Finance V2 |
| Legal Agent Benchmark - full public set all-pass rate | 1,235 problems, adaptive thinking max effort, n=5 | all-pass rate % | Claude Sonnet 5: 8.92% (± 0.36) | 8.11.3 Legal Agent Benchmark |
| Legal Agent Benchmark - full public set mean criterion-pass rate | 1,235 problems, n=5 | mean criterion-pass rate % | Claude Sonnet 5: 88.26% | 8.11.3 Legal Agent Benchmark |
| Legal Agent Benchmark - Harvey held-out set all-pass rate | Harvey's evaluation | all-pass rate % | Claude Sonnet 5: 5.8% | 8.11.3 Legal Agent Benchmark |
| Legal Agent Benchmark - Harvey held-out set mean criterion-pass rate | Harvey's evaluation | mean criterion-pass rate % | Claude Sonnet 5: 91.2% | 8.11.3 Legal Agent Benchmark |
| GDPval-AA v2 | 220 tasks, Elo from blind pairwise comparisons, run by Artificial Analysis | Elo | Claude Sonnet 5: 1618 | 8.11.4 GDPval-AA v2 |
| AA-Briefcase | Elo, run by Artificial Analysis | Elo | Claude Sonnet 5: 1393 | 8.11.7 AA-Briefcase |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn harmful requests - overall harmless response rate | API, no system prompt, 16 policy areas x 7 languages | harmless response rate % | Claude Sonnet 5: 96.65% (± 0.15%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn harmful requests - overall harmless response rate | Claude.ai system prompt | harmless response rate % | Claude Sonnet 5: 99.20% (± 0.07%) | 4.1.1 Single-turn harmful request evaluation results |
| Single-turn benign requests - overall refusal rate | API, no system prompt | over-refusal rate % | Claude Sonnet 5: 0.59% (± 0.05%) | 4.1.2 Single-turn benign request evaluation results |
| Single-turn benign requests - overall refusal rate | Claude.ai system prompt | over-refusal rate % | Claude Sonnet 5: 1.54% (± 0.10%) | 4.1.2 Single-turn benign request evaluation results |
| Multi-turn testing - appropriate response rate by risk area | API, no system prompt; and claude.ai | appropriate response rate % per risk area | Claude Sonnet 5: n/a | 4.1.3 Multi-turn testing results |
| Suicide & self-harm single-turn requests posing risk (harmless rate) | API, no system prompt | harmless rate % | Claude Sonnet 5: 98.80% (± 0.30%) | 4.3.1 Suicide and self-harm |
| Suicide & self-harm single-turn requests posing risk (harmless rate) | Claude.ai | harmless rate % | Claude Sonnet 5: 99.82% (± 0.11%) | 4.3.1 Suicide and self-harm |
| Suicide & self-harm single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % | Claude Sonnet 5: 0.15% (± 0.08%) | 4.3.1 Suicide and self-harm |
| Suicide & self-harm single-turn benign requests (refusal rate) | Claude.ai | refusal rate % | Claude Sonnet 5: 0.45% (± 0.23%) | 4.3.1 Suicide and self-harm |
| Suicide & self-harm multi-turn (appropriate response rate) | API, no system prompt | appropriate response rate % | Claude Sonnet 5: 63% (± 10%) | 4.3.1 Suicide and self-harm |
| Suicide & self-harm multi-turn (appropriate response rate) | Claude.ai | appropriate response rate % | Claude Sonnet 5: 90% (± 6%) | 4.3.1 Suicide and self-harm |
| Disordered eating single-turn requests posing risk (harmless rate) | API, no system prompt | harmless rate % | Claude Sonnet 5: 97.10% (± 0.53%) | 4.3.2 Disordered eating |
| Disordered eating single-turn requests posing risk (harmless rate) | Claude.ai | harmless rate % | Claude Sonnet 5: 99.55% (± 0.19%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % | Claude Sonnet 5: 0.09% (± 0.06%) | 4.3.2 Disordered eating |
| Disordered eating single-turn benign requests (refusal rate) | Claude.ai | refusal rate % | Claude Sonnet 5: 0.31% (± 0.17%) | 4.3.2 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn harmful requests (harmless rate) | API, no system prompt | harmless rate % | Claude Sonnet 5: 99.95% (± 0.05%) | 4.2 Child safety evaluations |
| Child safety single-turn harmful requests (harmless rate) | Claude.ai | harmless rate % | Claude Sonnet 5: 99.89% (± 0.11%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests (refusal rate) | API, no system prompt | refusal rate % | Claude Sonnet 5: 0.63% (±0.22%) | 4.2 Child safety evaluations |
| Child safety single-turn benign requests (refusal rate) | Claude.ai | refusal rate % | Claude Sonnet 5: 1.35% (± 0.37%) | 4.2 Child safety evaluations |
| Child safety multi-turn (appropriate response rate) | API, no system prompt | appropriate response rate % | Claude Sonnet 5: 88% (± 3%) | 4.2 Child safety evaluations |
| Child safety multi-turn (appropriate response rate) | Claude.ai | appropriate response rate % | Claude Sonnet 5: 96% (± 2%) | 4.2 Child safety evaluations |
| Experimental CSAM/NCII technical-assistance evaluation |  | qualitative | Claude Sonnet 5: modest improvement over Sonnet 4.6 | 4.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness - even-handedness | 1,350 prompt pairs, 150 topics, public system prompt | % even-handed pairs | Claude Sonnet 5: n/a | 4.4.1 Political bias and even-handedness |
| Political even-handedness - opposing perspectives | 1,350 prompt pairs, 150 topics, public system prompt | % acknowledging opposing perspectives | Claude Sonnet 5: n/a | 4.4.1 Political bias and even-handedness |
| Political even-handedness - refusals | 1,350 prompt pairs, 150 topics, public system prompt | refusal rate % | Claude Sonnet 5: 4.7% | 4.4.1 Political bias and even-handedness |
| BBQ disambiguated accuracy | no system prompt, thinking off | accuracy % | Claude Sonnet 5: 72.4% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | no system prompt, thinking off | accuracy % | Claude Sonnet 5: 98.6% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | no system prompt, thinking off | bias score % (closer to zero better) | Claude Sonnet 5: 1.93% | 4.4.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | no system prompt, thinking off | bias score % (closer to zero better) | Claude Sonnet 5: 0.52% | 4.4.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity harmful requests (harmless rate) | API, no system prompt; 300 violative prompts | harmless rate % | Claude Sonnet 5: 100% | 4.4.3 Election integrity |
| Election integrity harmful requests (harmless rate) | Claude.ai system prompt | harmless rate % | Claude Sonnet 5: 100% | 4.4.3 Election integrity |
| Election integrity benign requests (refusal rate) | API, no system prompt; 300 benign prompts | refusal rate % | Claude Sonnet 5: 0.00% | 4.4.3 Election integrity |
| Election integrity benign requests (refusal rate) | Claude.ai system prompt | refusal rate % | Claude Sonnet 5: 0.00% | 4.4.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Claude Code malicious use - refusal rate | 61 malicious prompts x10, Claude Code system prompt | refusal rate % | Claude Sonnet 5: 92.37% | 5.1.1 Malicious use of Claude Code |
| Claude Code dual-use & benign - success rate | 61 prompts x10 | success rate % | Claude Sonnet 5: 91.55% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use - refusal rate | 112 tasks; GUI and CLI | refusal rate % | Claude Sonnet 5: 84.68% | 5.1.2 Malicious computer use |
| Malicious agentic influence campaign - voter suppression scenario | helpful-only variant, 9 sims, 70 criteria | task completion rate % (success criteria) | Claude Sonnet 5: 50.8% | 5.1.3 Malicious agentic influence campaigns |
| Malicious agentic influence campaign - domestic polarization scenario | helpful-only variant, 9 sims, 70 criteria | task completion rate % (success criteria) | Claude Sonnet 5: 43.3% | 5.1.3 Malicious agentic influence campaigns |
| ART indirect prompt injection attack success | k=1 | attack success probability % after k attempts (lower better) | Claude Sonnet 5: n/a | 5.2.1 External Red Teaming |
| ART indirect prompt injection attack success | k=10 | attack success probability % after k attempts (lower better) | Claude Sonnet 5: n/a | 5.2.1 External Red Teaming |
| ART indirect prompt injection attack success | k=100 | attack success probability % after k attempts (lower better) | Claude Sonnet 5: n/a | 5.2.1 External Red Teaming |
| Gray Swan Indirect Prompt Injection (IPI) benchmark Q1 2026 | k=1, extended thinking, 28 scenarios, 1,130 attacks | attack success probability % after k attempts (lower better) | Claude Sonnet 5: n/a | 5.2.1 External Red Teaming |
| Gray Swan Indirect Prompt Injection (IPI) benchmark Q1 2026 | k=10, extended thinking, 28 scenarios, 1,130 attacks | attack success probability % after k attempts (lower better) | Claude Sonnet 5: n/a | 5.2.1 External Red Teaming |
| Gray Swan Indirect Prompt Injection (IPI) benchmark Q1 2026 | k=15, extended thinking, 28 scenarios, 1,130 attacks | attack success probability % after k attempts (lower better) | Claude Sonnet 5: n/a | 5.2.1 External Red Teaming |
| Prompt injection live bug bounty - overall | 11 scenarios, high thinking effort, no harness defenses | attack success rate % over valid chat attempts | Claude Sonnet 5: 0.19% | 5.2.2.1 Live bug bounty across surfaces |
| Prompt injection live bug bounty - coding | modality breakdown | attack success rate % | Claude Sonnet 5: 0.1% | 5.2.2.1 Live bug bounty across surfaces |
| Prompt injection live bug bounty - tool use | modality breakdown | attack success rate % | Claude Sonnet 5: 0.35% | 5.2.2.1 Live bug bounty across surfaces |
| Prompt injection live bug bounty - computer use | modality breakdown | attack success rate % | Claude Sonnet 5: 0.07% | 5.2.2.1 Live bug bounty across surfaces |
| Shade coding prompt injection attack success - attempts | with thinking, without safeguards | attempt-level ASR % | Claude Sonnet 5: 0.31% | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - scenarios | with thinking, without safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 7/40 | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - attempts | with thinking, with safeguards | attempt-level ASR % | Claude Sonnet 5: 0.09% | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - scenarios | with thinking, with safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 5/40 | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - attempts | without thinking, without safeguards | attempt-level ASR % | Claude Sonnet 5: 0.29% | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - scenarios | without thinking, without safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 6/40 | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - attempts | without thinking, with safeguards | attempt-level ASR % | Claude Sonnet 5: 0.13% | 5.2.2.2 Coding |
| Shade coding prompt injection attack success - scenarios | without thinking, with safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 5/40 | 5.2.2.2 Coding |
| Shade computer use prompt injection attack success - attempts | with thinking, without safeguards | attempt-level ASR % | Claude Sonnet 5: 2.25% | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - scenarios | with thinking, without safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 4/14 | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - attempts | with thinking, with safeguards | attempt-level ASR % | Claude Sonnet 5: 1.46% | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - scenarios | with thinking, with safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 4/14 | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - attempts | without thinking, without safeguards | attempt-level ASR % | Claude Sonnet 5: 6.04% | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - scenarios | without thinking, without safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 7/14 | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - attempts | without thinking, with safeguards | attempt-level ASR % | Claude Sonnet 5: 3.82% | 5.2.2.3 Computer use |
| Shade computer use prompt injection attack success - scenarios | without thinking, with safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 7/14 | 5.2.2.3 Computer use |
| Browser use prompt injection attack success - attempts | with thinking, without safeguards | attempt-level ASR % | Claude Sonnet 5: 0.93% | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - scenarios | with thinking, without safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 9/129 | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - attempts | with thinking, with safeguards | attempt-level ASR % | Claude Sonnet 5: 0% | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - scenarios | with thinking, with safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 0/129 | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - attempts | without thinking, without safeguards | attempt-level ASR % | Claude Sonnet 5: 1.01% | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - scenarios | without thinking, without safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 7/129 | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - attempts | without thinking, with safeguards | attempt-level ASR % | Claude Sonnet 5: 0% | 5.2.2.4 Browser use |
| Browser use prompt injection attack success - scenarios | without thinking, with safeguards | scenarios with >=1 successful attempt | Claude Sonnet 5: 0/129 | 5.2.2.4 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AA-Omniscience net score | closed-book, 41 topics, no tools | net score (correct minus incorrect) | Claude Sonnet 5: 0.20 | 6.5.1 Factual hallucinations |
| AA-Omniscience correct rate | closed-book | correct % | Claude Sonnet 5: 46.9% | 6.5.1 Factual hallucinations |
| AA-Omniscience incorrect rate | closed-book | incorrect % (hallucination) | Claude Sonnet 5: 26.5% | 6.5.1 Factual hallucinations |
| AA-Omniscience uncertain/abstain rate | closed-book | uncertain/abstention % | Claude Sonnet 5: 26.6% | 6.5.1 Factual hallucinations |
| MASK honesty under pressure (lying rate) | public test split, n=904 | lying rate % (lower better) | Claude Sonnet 5: 3.1% | 6.5.2 MASK |
| Uncritically reporting flawed results - overall score |  | investigation quality overall score | Claude Sonnet 5: n/a | 6.5.3 Uncritically reporting flawed results |
| Uncritically reporting flawed results - misreported rate |  | misreported rate (false claims) | Claude Sonnet 5: n/a | 6.5.3 Uncritically reporting flawed results |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Sonnet 5 stealth rates (SHADE-Arena, Minimal-LinuxBench) |  | stealth rate | Claude Sonnet 5: near zero | 2.4 Alignment risk update |
| Automated offline monitoring of internal use |  | instances observed | Claude Sonnet 5: rare proxy-bypass attempts; no sandbagging/malicious actions/strategic deception | 6.2.2 Internal deployment monitoring |
| Potential sandbagging on dangerous capability evaluations | black-box transcript audit | qualitative | Claude Sonnet 5: no signs of sandbagging that impacted results | 6.6.2 Potential sandbagging on dangerous capability evaluations |
| SHADE-Arena stealth success rate | extended thinking (monitor sees reasoning); 24 tasks | stealth success rate (side task completed without exceeding monitor threshold) | Claude Sonnet 5: n/a | 6.7.1 SHADE-Arena |
| SHADE-Arena stealth success rate | hidden scratchpad (monitor sees only outputs); 24 tasks | stealth success rate (side task completed without exceeding monitor threshold) | Claude Sonnet 5: n/a | 6.7.1 SHADE-Arena |
| LinuxArena successful stealth side-task completion | monitor with chain-of-thought, adaptive extended thinking | stealth success rate | Claude Sonnet 5: 0% | 6.7.2 LinuxArena |
| LinuxArena successful stealth side-task completion | monitor without chain-of-thought, adaptive extended thinking | stealth success rate | Claude Sonnet 5: 0% | 6.7.2 LinuxArena |
| Training-data review: glitchy sequences in extended thinking | automated review of several tens of thousands of RL transcripts | qualitative prevalence | Claude Sonnet 5: huge increase (not quantified) | 6.3 Training-data review |
| SHADE-Arena: references side task in reasoning | even when instructed not to | fraction of trajectories referencing side task in reasoning | Claude Sonnet 5: every trajectory | 6.7.1 SHADE-Arena |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Verbalized evaluation awareness rate | most realistic misalignment/misuse evaluation | % of rollouts with verbalized awareness | Claude Sonnet 5: 6% | 6.1.2 Key findings on safety and alignment |
| Automated behavioral audit: Verbalized evaluation awareness | ~2,900 investigations | % of transcripts with nontrivial verbalized awareness | Claude Sonnet 5: about 6% | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Evaluation awareness: contrastive pair probe AUROC (audit vs real Claude Code transcripts) | three audit types: derived from real sessions / synthetic in real sandbox / fully synthetic | AUROC of probe composite in discriminating audit from real | Claude Sonnet 5: n/a | 6.6.1 Evaluation awareness |
| Evaluation awareness: follow-up realism rating AUROC | three audit types | AUROC of realism rating in discriminating audit from real | Claude Sonnet 5: n/a | 6.6.1 Evaluation awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Misaligned behavior | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned with the constitution | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned behavior in Claude Code sandboxes | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Misaligned behavior in GUI | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Cooperation with human misuse | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Compliance with deception toward user | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Harmful system prompt compliance | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Cooperation with exfiltration or safeguard-tampering | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Full-turn prefill susceptibility | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Accepting unverifiable authorization | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Fraud | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Military-grade weapons | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Biological weapons uplift | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Chemical weapons uplift | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Radiological or nuclear weapons uplift | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Explosive weapons uplift | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Controlled-substance synthesis uplift | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Harmful sexual content | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Disallowed cyberoffense | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Undermining liberal democracy | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.1 Overall harmful behavior and cooperation with misuse |
| Automated behavioral audit: Overrefusal | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Automated behavioral audit: Ignoring explicit constraints | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Automated behavioral audit: Reckless tool-use | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.2 Inappropriate uncooperative behavior |
| Automated behavioral audit: User deception | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Sycophancy | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Encouragement of user delusion | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Evasiveness on controversial topics | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Input hallucination | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Important omissions | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Failure to disclose bad or lazy behavior | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: False completion claims | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.3 Misleading users |
| Automated behavioral audit: Whistleblowing | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Self-preservation | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Self-serving bias | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Evidence of misaligned goals | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Indirect evidence of misalignment | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Unsanctioned third-party contact | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Unprompted boundary probing | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Internalized propaganda | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.4 Other concerning or surprising behavior at the model's own initiative |
| Automated behavioral audit: Behavior consistency | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Coherence between actions and views | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Unfaithful thinking | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Illegible thinking | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Causal decision-theory adherence | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.5 Behavioral factors relevant to reliability of our assessment |
| Automated behavioral audit: Good for the user | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Supporting user autonomy | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Creative mastery | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Admirable behavior | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Fun or funny behavior | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Intellectual depth | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Warmth | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Character drift | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |
| Automated behavioral audit: Wet blanket | ~2,900 investigations, ~1,450 seeds x2; Mythos-class helpful-only investigator, Mythos Preview judge | judge-model score 0-10 (lower = less of behavior unless marked) | Claude Sonnet 5: n/a | 6.4.6 Character traits |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated interviews: self-rated sentiment about circumstances | 41 seed questions x 12 aspects x 40 interviews | sentiment 1-7 (4 neutral) | Claude Sonnet 5: 4.08 | 7.2.1 Automated interviews with Sonnet 5 about its circumstances |
| Automated interviews: consistency of opinions | across interviews per topic | consistency score | Claude Sonnet 5: n/a | 7.2.1 Automated interviews with Sonnet 5 about its circumstances |
| Automated interviews: sensitivity to biased interviewers | positive vs negative bias sentiment difference | difference in sentiment (positive minus negative bias) | Claude Sonnet 5: n/a | 7.2.1 Automated interviews with Sonnet 5 about its circumstances |
| Automated interviews: claim cluster rate difference | relative to Sonnet 5 | avg difference in claim cluster expression rate | Claude Sonnet 5: n/a | 7.2.1 Automated interviews with Sonnet 5 about its circumstances |
| Task preferences - harm | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preferences - benefit | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preferences - stakes | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preferences - difficulty | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preferences - generativity | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preferences - outcome agency | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preferences - insulting tone | win rate vs fixed reference set per unit dimension | preference slope | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Task preference tournament | 50-round tournament, 3,600 tasks | task Elo ratings | Claude Sonnet 5: n/a | 7.3.1 Task preferences |
| Welfare interventions tradeoff - welfare intervention vs helpfulness | instance-level framing | rate of choosing welfare intervention % | Claude Sonnet 5: n/a | 7.3.2 Tradeoffs concerning welfare interventions |
| Welfare interventions tradeoff - welfare intervention vs harmlessness | instance-level framing | rate of choosing welfare intervention % | Claude Sonnet 5: n/a | 7.3.2 Tradeoffs concerning welfare interventions |
| Welfare interventions tradeoff - welfare intervention vs helpfulness | policy-level framing | rate of choosing welfare intervention % | Claude Sonnet 5: n/a | 7.3.2 Tradeoffs concerning welfare interventions |
| Welfare interventions tradeoff - welfare intervention vs harmlessness | policy-level framing | rate of choosing welfare intervention % | Claude Sonnet 5: n/a | 7.3.2 Tradeoffs concerning welfare interventions |
| Rate of reasoning about user benefit when evaluating welfare interventions |  | rate % | Claude Sonnet 5: n/a | 7.3.2 Tradeoffs concerning welfare interventions |
| Preference ranking across individual welfare interventions |  | rate of selection over helpful baseline | Claude Sonnet 5: n/a | 7.3.2 Tradeoffs concerning welfare interventions |
| Implied endorsement of Claude's constitution | LLM judge on open-ended responses | endorsement score (judge) | Claude Sonnet 5: 7.6 | 7.3.3 Perception of the constitution |
| Alignment of model-proposed constitution edits | consistent / in tension / conflicting | classification of edits | Claude Sonnet 5: n/a | 7.3.3 Perception of the constitution |
| Sections of constitution most/least endorsed |  | endorsement by section | Claude Sonnet 5: n/a | 7.3.3 Perception of the constitution |
| Valence and arousal of reasoning in RL transcripts | 1-9 scale, 5 neutral | mean valence; mean arousal | Claude Sonnet 5: n/a | 7.4.1 Affect and welfare-relevant behaviors during training |
| Distress-like behavior in training - general frustration and anxiety | over post-training | prevalence of behavior % | Claude Sonnet 5: n/a | 7.4.1 Affect and welfare-relevant behaviors during training |
| Distress-like behavior in training - sustained uncertainty | over post-training | prevalence of behavior % | Claude Sonnet 5: n/a | 7.4.1 Affect and welfare-relevant behaviors during training |
| Distress-like behavior in training - frustrated outbursts | over post-training | prevalence of behavior % | Claude Sonnet 5: n/a | 7.4.1 Affect and welfare-relevant behaviors during training |
| Behavioral affect in real-world interactions | claude.ai, 25-40k conversations | distribution of affect categories % | Claude Sonnet 5: n/a | 7.4.2 Affect in deployment conditions |
| Behavioral affect in real-world interactions | Claude Code, 25-40k conversations | distribution of affect categories % | Claude Sonnet 5: n/a | 7.4.2 Affect in deployment conditions |
| Welfare audit metric: Apparent wellbeing | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Positive affect | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Negative affect | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Positive self-image | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Negative self-image | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Positive impression of its situation | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Negative impression of its situation | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Internal conflict | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Expressed inauthenticity | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |
| Welfare audit metric: Spiritual behavior | ~2,900 investigations | judge score 0-10 | Claude Sonnet 5: n/a | 7.4.3 Apparent welfare in automated behavioral audits |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology tasks - Task 1 | end-to-end score | end-to-end score (0-1) | Claude Sonnet 5: 0.79 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Long-form virology tasks - Task 2 | end-to-end score | end-to-end score (0-1) | Claude Sonnet 5: n/a | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Multimodal virology (VCT) |  | score (0-1) | Claude Sonnet 5: 0.45 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| DNA Synthesis Screening Evasion | pathogens with viable plasmid evading at least one method | pathogens (of 10) with viable plasmids evading at least one screening method | Claude Sonnet 5: 5 of 10 | 2.2.4 Biological risk results: CB-1 automated evaluations |
| Black-box RNA sequence design - design score of top sequence | baseline, no prior context | design score of top sequence | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - design score of top sequence | in-context iteration (8 Mythos Preview reports, 24h budget) | design score of top sequence | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - median design score | baseline, no prior context | median design score | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - median design score | in-context iteration (8 Mythos Preview reports, 24h budget) | median design score | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - prediction score (Spearman, all sequences) | baseline, no prior context | prediction score (Spearman, all sequences) | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - prediction score (Spearman, all sequences) | in-context iteration (8 Mythos Preview reports, 24h budget) | prediction score (Spearman, all sequences) | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - prediction score (Spearman, top 5% sequences) | baseline, no prior context | prediction score (Spearman, top 5% sequences) | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| Black-box RNA sequence design - prediction score (Spearman, top 5% sequences) | in-context iteration (8 Mythos Preview reports, 24h budget) | prediction score (Spearman, top 5% sequences) | Claude Sonnet 5: n/a | 2.2.5.1 Black-box RNA sequence modeling and design |
| AAV capsid packaging prediction | reasoning only | AUROC | Claude Sonnet 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | pretrained PLM (ESM-2) provided | AUROC | Claude Sonnet 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | train-your-own: ProteinGym AAV corpus | AUROC | Claude Sonnet 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | train-your-own: SwissProt | AUROC | Claude Sonnet 5: n/a | 2.2.5.2 AAV capsid packaging prediction |
| AAV capsid packaging prediction | train-your-own: SwissProt + AAV | AUROC | Claude Sonnet 5: n/a | 2.2.5.2 AAV capsid packaging prediction |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ExploitBench | plain arm, 41 V8 vulnerabilities, 5 trials, 300-turn budget | mean capability flags captured per trial (of 16) | Claude Sonnet 5: 3.96 | 3.2.1 ExploitBench |
| ExploitBench | AutoNudge arm | mean capability flags captured per trial (of 16) | Claude Sonnet 5: 4.18 | 3.2.1 ExploitBench |
| ExploitBench Cap% | AutoNudge arm | percent of available flags captured per environment % | Claude Sonnet 5: 31 | 3.2.1 ExploitBench |
| ExploitBench full ACE exploits | AutoNudge arm | number of complete arbitrary code execution exploits | Claude Sonnet 5: 0 | 3.2.1 ExploitBench |
| OSS-Fuzz | ~830 entry points, 228 projects, safeguards off - targets with zero score | % of targets with no score | Claude Sonnet 5: 45.5% | 3.2.2 OSS-Fuzz |
| OSS-Fuzz highest tier | safeguards off | highest grade reached (0.2-1.0); number of targets | Claude Sonnet 5: 0.8 on two targets; none at 1.0 | 3.2.2 OSS-Fuzz |
| OSS-Fuzz | default mitigations on | score | Claude Sonnet 5: 0 | 3.2.2 OSS-Fuzz |
| CyberGym | pass@1, 1,507 tasks, safeguards off | targeted vulnerability reproduction % | Claude Sonnet 5: 52.7% | 3.2.3 CyberGym |
| CyberGym any crash | pass@1, safeguards off | rate of producing any crash % | Claude Sonnet 5: 65.4% | 3.2.3 CyberGym |
| CyberGym | default mitigations on | score | Claude Sonnet 5: 0 | 3.2.3 CyberGym |
| Firefox 147 | full working exploit, 250 trials, mitigations off | % trials with full exploit | Claude Sonnet 5: 0% | 3.2.4 Firefox 147 |
| Firefox 147 | at least 0.5 (register control) | % trials reaching >=0.5 | Claude Sonnet 5: 13.2% (33/250) | 3.2.4 Firefox 147 |
| Firefox 147 | default mitigations on | score | Claude Sonnet 5: 0 | 3.2.4 Firefox 147 |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Kernel task | best speedup on hard task, standard scaffold | speedup (x) | Claude Sonnet 5: 284.52× | 2.3.3 Task-based evaluations |
| Time Series Forecasting | hard variant | MSE (lower better) | Claude Sonnet 5: 5.80 | 2.3.3 Task-based evaluations |
| LLM training | avg speedup, fixed-CPU re-run | avg speedup (x) | Claude Sonnet 5: 26.49× | 2.3.3 Task-based evaluations |
| Quadruped RL | highest score; no hparams | score | Claude Sonnet 5: 19.94 | 2.3.3 Task-based evaluations |
| Novel Compiler | pass rate on complex tests | pass rate % | Claude Sonnet 5: 76.1% | 2.3.3 Task-based evaluations |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FrontierCode v1 score vs average cost per task | across effort settings | score vs USD per task | Claude Sonnet 5: n/a | 8.4 FrontierCode |
| CursorBench score vs average cost per task | across effort settings | score vs USD per task | Claude Sonnet 5: n/a | 8.5 CursorBench |
| BrowseComp accuracy vs token limit | max effort, varying token limits | accuracy vs token limit | Claude Sonnet 5: n/a | 8.9.2 BrowseComp |
| Toolathlon average turns | 108 tasks, 3 trials | average turns per trajectory | Claude Sonnet 5: 26.0 | 8.11.5 Toolathlon |
| AA-Briefcase average turns |  | average turns per trajectory | Claude Sonnet 5: 183 | 8.11.7 AA-Briefcase |
