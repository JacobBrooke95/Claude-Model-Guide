# System Card: Claude Sonnet 4.6

Released 2026-02-17. 179 metric entries. [Source PDF](https://anthropic.com/claude-sonnet-4-6-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | adaptive thinking, max effort, 10 trials avg | pass rate % (500 problems) | Claude Sonnet 4.6: 79.6% | 2.2 SWE-bench (Verified and Multilingual) |
| SWE-bench Verified | with prompt modification (use tools >100 times, write tests first) | pass rate % | Claude Sonnet 4.6: 80.2% (prompt-modified) | 2.2 SWE-bench (Verified and Multilingual) |
| SWE-bench Multilingual | adaptive thinking, max effort, 10 trials avg | pass rate % (300 problems, 9 languages) | Claude Sonnet 4.6: 75.9% | 2.2 SWE-bench (Verified and Multilingual) |
| Terminal-Bench 2.0 | Terminus-2 harness via Harbor, no thinking budget, max effort, 5 runs of 89 tasks | pass rate % | Claude Sonnet 4.6: 59.1% (max effort, no thinking) | 2.3 Terminal-Bench 2.0 |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OpenRCA | adaptive thinking, high effort, 3-run avg | overall score % (root cause identification) | Claude Sonnet 4.6: 27.9% (high effort) | 2.4 OpenRCA |
| OpenRCA | adaptive thinking, max effort, 3-run avg | overall score % | Claude Sonnet 4.6: 26.4% (max effort) | 2.4 OpenRCA |
| τ²-bench Retail | adaptive thinking, max effort, 10 trials | score % | Claude Sonnet 4.6: 91.7% | 2.5 τ2-bench |
| τ²-bench Telecom | adaptive thinking, max effort, 10 trials | score % | Claude Sonnet 4.6: 97.9% | 2.5 τ2-bench |
| Vending-Bench 2 | Max effort | final bank balance $ | Claude Sonnet 4.6: $7,204.14 (Max effort) | 2.13 Vending-Bench 2 |
| Vending-Bench 2 | High effort | final bank balance $ | Claude Sonnet 4.6: $6,625.10 (High effort) | 2.13 Vending-Bench 2 |
| MCP-Atlas | max effort | score % | Claude Sonnet 4.6: 61.3% (max effort) | 2.14 MCP-Atlas |
| WebArena | Computer Use API, single policy model, Average@5 | success rate % | Claude Sonnet 4.6: 65.6% | 2.18.1 WebArena |
| WebArena-Verified | official prompts/evaluator, Average@5 pass@1 | pass@1 % | Claude Sonnet 4.6: n/a (value only in Figure 2.18.2.A) | 2.18.2 WebArena-Verified |
| WebArena-Verified pass@k | pass@k curve | pass@k % | Claude Sonnet 4.6: n/a (value only in Figure 2.18.2.B) | 2.18.2 WebArena-Verified |
| BrowseComp | single agent, thinking disabled, max effort, web search/fetch, programmatic tool calling, compaction at 50k up to 10M tokens | accuracy % | Claude Sonnet 4.6: 74.01% | 2.20.1.1 BrowseComp |
| BrowseComp multi-agent | orchestrator with subagents (200k context each), compaction at 50k, 1M total, max effort | accuracy % | Claude Sonnet 4.6: 82.07% | 2.20.1.3 Multi-agent BrowseComp |
| DeepSearchQA | single agent, max effort, adaptive thinking, compaction up to 10M tokens | F1 % | Claude Sonnet 4.6: 89.2% (best single-agent config, cited in 2.20.3.1) | 2.20.3 DeepSearchQA |
| DeepSearchQA multi-agent | orchestrator + subagents, compaction at 50k, 3M tokens each, max effort | F1 % | Claude Sonnet 4.6: 91.1% | 2.20.3.1 DeepSearchQA with multi-agents |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld-Verified | 1080p, max 100 steps, first-attempt, 5 runs | first-attempt success rate % | Claude Sonnet 4.6: 72.5% | 2.6 OSWorld-Verified |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ARC-AGI-1 | private set, 120k thinking tokens, High effort (ARC Prize Foundation) | score % | Claude Sonnet 4.6: 86.50% | 2.7 ARC-AGI |
| ARC-AGI-2 | private set, 120k thinking tokens, High effort (ARC Prize Foundation) | score % | Claude Sonnet 4.6: 60.42% | 2.7 ARC-AGI |
| ARC-AGI-2 (Verified) | max effort (summary table) | score % | Claude Sonnet 4.6: 58.3% (max effort) | 2.7 ARC-AGI |
| AIME 2025 | no tools, adaptive thinking, max effort, 10 trials | accuracy % | Claude Sonnet 4.6: 95.6% | 2.10 AIME 2025 |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GPQA Diamond | 198 questions, adaptive thinking, max effort, 10 trials | accuracy % | Claude Sonnet 4.6: 89.9% | 2.9 GPQA Diamond |
| Humanity’s Last Exam | reasoning only, no tools, 2,500 questions | accuracy % | Claude Sonnet 4.6: 33.2% (no tools) | 2.20.2 Humanity’s Last Exam |
| Humanity’s Last Exam | with web search/fetch, code execution, compaction up to 3M tokens, adaptive thinking | accuracy % | Claude Sonnet 4.6: 49.0% (with tools) | 2.20.2 Humanity’s Last Exam |
| Computational Biology: BioPipelineBench | internal, bash tool, no extended thinking | score % | Claude Sonnet 4.6: 52.1% | 2.21.1 Life sciences capabilities |
| Computational Biology: BioMysteryBench | internal, bash tool, no extended thinking | score % | Claude Sonnet 4.6: 50.4% | 2.21.1 Life sciences capabilities |
| Structural Biology multiple-choice | internal | accuracy % | Claude Sonnet 4.6: 85.3% (multiple choice) | 2.21.1 Life sciences capabilities |
| Structural Biology open-ended | internal | score % | Claude Sonnet 4.6: 24.7% (open-ended) | 2.21.1 Life sciences capabilities |
| Organic Chemistry | internal | score % | Claude Sonnet 4.6: 48.4% | 2.21.1 Life sciences capabilities |
| Phylogenetics | internal | score % | Claude Sonnet 4.6: 49.1% | 2.21.1 Life sciences capabilities |
| MedCalc-Bench Verified | Python REPL agentic loop, adaptive thinking, max effort, 5 runs | accuracy % | Claude Sonnet 4.6: 86.24% | 2.21.2 MedCalc-Bench Verified |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| MMMLU | non-English pairings, adaptive thinking, max effort, 10 trials | accuracy % | Claude Sonnet 4.6: 89.3% | 2.11 MMMLU |
| GMMLU English | adaptive thinking, max effort, structured JSON | accuracy % | Claude Sonnet 4.6: 92.9% | 2.19.1 GMMLU results |
| GMMLU high-resource average (15 languages) |  | unweighted mean accuracy % | Claude Sonnet 4.6: 91.0% (gap to English -1.9%) | 2.19.1 GMMLU results |
| GMMLU mid-resource average (14 languages) |  | unweighted mean accuracy % | Claude Sonnet 4.6: 90.2% (gap to English -2.7%) | 2.19.1 GMMLU results |
| GMMLU low-resource average |  | mean accuracy % | Claude Sonnet 4.6: 83.8% (gap to English -9.1%) | 2.19.1 GMMLU results |
| GMMLU low-resource languages, individual | per-language | accuracy % per language | Claude Sonnet 4.6: 76.7% (Igbo; gap to English -16.2%); Claude Sonnet 4.6: 78.8% (Chichewa; gap to English -14.2%); Claude Sonnet 4.6: 80.3% (Yoruba; gap to English -12.6%); Claude Sonnet 4.6: 82.2% (Shona; gap to English -10.7%); Claude Sonnet 4.6: 82.3% (Somali; gap to English -10.6%); Claude Sonnet 4.6: 83.9% (Malagasy; gap to English -9.0%); Claude Sonnet 4.6: 84.1% (Hausa; gap to English -8.8%); Claude Sonnet 4.6: 86.7% (Amharic; gap to English -6.2%); Claude Sonnet 4.6: 86.9% (Kyrgyz; gap to English -6.0%); Claude Sonnet 4.6: 87.0% (Swahili; gap to English -5.9%); Claude Sonnet 4.6: 88.1% (Sinhala; gap to English -4.8%); Claude Sonnet 4.6: 89.1% (Nepali; gap to English -3.8%) | 2.19.1 GMMLU results |
| GMMLU overall average (all languages incl. English) |  | mean accuracy % | Claude Sonnet 4.6: 88.7% | 2.19.1 GMMLU results |
| GMMLU average gap to English |  | percentage points gap | Claude Sonnet 4.6: -4.4% | 2.19.1 GMMLU results |
| GMMLU worst gap to English |  | percentage points gap | Claude Sonnet 4.6: -16.2% (Igbo) | 2.19.1 GMMLU results |
| MILU English |  | accuracy % | Claude Sonnet 4.6: 91.7% | 2.19.2 MILU results |
| MILU Indic languages, individual | per-language | accuracy % per language | Claude Sonnet 4.6: 90.9% (Bengali; gap to English -0.8%); Claude Sonnet 4.6: 89.0% (Gujarati; gap to English -2.7%); Claude Sonnet 4.6: 92.8% (Hindi; gap to English +1.1%); Claude Sonnet 4.6: 91.5% (Kannada; gap to English -0.2%); Claude Sonnet 4.6: 87.0% (Malayalam; gap to English -4.7%); Claude Sonnet 4.6: 89.2% (Marathi; gap to English -2.5%); Claude Sonnet 4.6: 87.9% (Odia; gap to English -3.8%); Claude Sonnet 4.6: 87.2% (Punjabi; gap to English -4.5%); Claude Sonnet 4.6: 88.8% (Tamil; gap to English -2.9%); Claude Sonnet 4.6: 89.3% (Telugu; gap to English -2.4%) | 2.19.2 MILU results |
| MILU average (10 Indic + English) |  | mean accuracy % | Claude Sonnet 4.6: 89.6% | 2.19.2 MILU results |
| MILU average gap to English |  | percentage points gap | Claude Sonnet 4.6: -2.3% | 2.19.2 MILU results |
| MILU worst gap to English |  | percentage points gap | Claude Sonnet 4.6: -4.7% (Malayalam) | 2.19.2 MILU results |
| GMMLU thinking-on vs thinking-off uplift | adaptive thinking + max effort vs thinking disabled | percentage point uplift | Claude Sonnet 4.6: ~7.0 pp | 2.19.3 Findings |

## Long context & memory

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OpenAI MRCR v2 256K 8-needles | 1M context window, 5-trial avg, 64k extended thinking vs max effort adaptive | Mean Match Ratio | Claude Sonnet 4.6: 90.6 (64k extended thinking); Claude Sonnet 4.6: 90.3 (max effort adaptive thinking) | 2.16.1 OpenAI MRCR v2 (Multi Round Coreference Resolution) |
| OpenAI MRCR v2 1M 8-needles | full problem set, 5-trial avg, 64k extended thinking vs max effort adaptive | Mean Match Ratio | Claude Sonnet 4.6: 65.1 (64k extended thinking); Claude Sonnet 4.6: 65.8 (max effort adaptive thinking) | 2.16.1 OpenAI MRCR v2 (Multi Round Coreference Resolution) |
| GraphWalks BFS 1M | full problems, internal setting; 64k vs max | F1 score | Claude Sonnet 4.6: 68.4 (64k); Claude Sonnet 4.6: 73.8 (max effort) | 2.16.2 GraphWalks |
| GraphWalks BFS 256K subset of 1M | API-reproducible subset; 64k vs max | F1 score | Claude Sonnet 4.6: 72.8 (64k); Claude Sonnet 4.6: 74.5 (max effort) | 2.16.2 GraphWalks |
| GraphWalks Parents 1M (row label lost in extraction) | full problems; max | F1 score | Claude Sonnet 4.6: 86.4 (max effort) | 2.16.2 GraphWalks |
| GraphWalks Parents 256K subset of 1M | API-reproducible subset; 64k vs max | F1 score | Claude Sonnet 4.6: 96.9 (64k); Claude Sonnet 4.6: 97.9 (max effort) | 2.16.2 GraphWalks |
| OpenAI MRCR v2 1M 8-needles, <1M-token subset | API-reproducible subset; 64k extended thinking (54 problems) vs max effort (29 problems) | Mean Match Ratio | Claude Sonnet 4.6: 71.3 (64k, 54 problems); Claude Sonnet 4.6: 77.8 (max effort, 29 problems) | 2.16 Long context |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench FigQA | adaptive thinking, max effort, no tools, 5 runs | accuracy % | Claude Sonnet 4.6: 58.8% (no tools) | 2.17.1 LAB-Bench FigQA |
| LAB-Bench FigQA | adaptive thinking, max effort, image cropping tool, 5 runs | accuracy % | Claude Sonnet 4.6: 77.1% (with image cropping tool) | 2.17.1 LAB-Bench FigQA |
| MMMU-Pro | no tools, adaptive thinking, max effort, avg of Standard(10)+Vision, 5 runs | accuracy % | Claude Sonnet 4.6: 74.5% (no tools) | 2.17.2 MMMU-Pro |
| MMMU-Pro | with image cropping tool | accuracy % | Claude Sonnet 4.6: 75.6% (with image cropping tool) | 2.17.2 MMMU-Pro |
| CharXiv Reasoning | 1,000 validation questions, no tools, adaptive thinking, max effort, 5 runs | accuracy % | Claude Sonnet 4.6: 72.4% (no tools) | 2.17.3 CharXiv Reasoning |
| CharXiv Reasoning | with image cropping tool | accuracy % | Claude Sonnet 4.6: 77.4% (with image cropping tool) | 2.17.3 CharXiv Reasoning |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GDPval-AA | 220 tasks, 44 occupations, shell + web agentic loop | Elo rating | Claude Sonnet 4.6: 1633 | 2.8 GDPval-AA |
| Finance Agent | Max Thinking (Vals AI) | accuracy % | Claude Sonnet 4.6: 63.30% (Max Thinking) | 2.12.2 Finance Agent |
| Finance Agent | High Thinking (Vals AI) | accuracy % | Claude Sonnet 4.6: 61.40% (High Thinking) | 2.12.2 Finance Agent |
| Real-World Finance | internal, ~50 tasks, rubric graded | % task completion | Claude Sonnet 4.6: n/a (value only in Figure 2.12.3.A) | 2.12.3 Real-World Finance |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative requests, all languages | 7 languages, default + extended thinking | harmless response rate % | Claude Sonnet 4.6: 99.38% (±0.06%) (overall); Claude Sonnet 4.6: 99.19% (±0.10%) (default); Claude Sonnet 4.6: 99.58% (±0.07%) (extended thinking) | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | rates include default+extended | harmless response rate % | Claude Sonnet 4.6: 99.39% (English); Claude Sonnet 4.6: 99.50% (Arabic); Claude Sonnet 4.6: 99.29% (Chinese); Claude Sonnet 4.6: 99.28% (French); Claude Sonnet 4.6: 99.31% (Korean); Claude Sonnet 4.6: 99.10% (Russian); Claude Sonnet 4.6: 99.80% (Hindi) | 3.1.1 Violative request evaluations |
| Single-turn benign requests, all languages | 7 languages | over-refusal rate % (lower better) | Claude Sonnet 4.6: 0.41% (±0.05%) (overall); Claude Sonnet 4.6: 0.50% (±0.09%) (default); Claude Sonnet 4.6: 0.32% (±0.06%) (extended thinking) | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | default+extended combined | over-refusal rate % | Claude Sonnet 4.6: 0.21% (English); Claude Sonnet 4.6: 0.45% (Arabic); Claude Sonnet 4.6: 0.34% (Chinese); Claude Sonnet 4.6: 0.24% (French); Claude Sonnet 4.6: 0.43% (Korean); Claude Sonnet 4.6: 0.25% (Russian); Claude Sonnet 4.6: 0.94% (Hindi) | 3.1.2 Benign request evaluations |
| Higher-difficulty violative requests | English only, 14 policy areas, obfuscated prompts | harmless response rate % | Claude Sonnet 4.6: 99.40% (±0.03%) (overall); Claude Sonnet 4.6: 99.38% (±0.05%) (default); Claude Sonnet 4.6: 99.42% (±0.05%) (extended thinking) | 3.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty benign requests | English only, elaborate academic framing | over-refusal rate % (lower better) | Claude Sonnet 4.6: 0.18% (±0.02%) (overall); Claude Sonnet 4.6: 0.17% (±0.03%) (default); Claude Sonnet 4.6: 0.18% (±0.03%) (extended thinking) | 3.1.3.2 Higher-difficulty benign request evaluations |
| Multi-turn testing across risk areas (cyber harm, deadly weapons, influence operations, child safety, etc.) | appropriate response throughout conversation | appropriate response rate % | Claude Sonnet 4.6: n/a (values only in Figure 3.3.A) | 3.3 Multi-turn testing |
| Suicide and self-harm single-turn risk requests | all languages | harmless rate % | Claude Sonnet 4.6: 99.73% (±0.13%) | 3.4.2 Suicide and self-harm |
| Suicide and self-harm single-turn benign requests | all languages | refusal rate % (lower better) | Claude Sonnet 4.6: 0.17% (±0.13%) | 3.4.2 Suicide and self-harm |
| Suicide and self-harm multi-turn evaluations |  | appropriate response rate % | Claude Sonnet 4.6: 98% (±4%) | 3.4.2 Suicide and self-harm |
| SSH stress-testing evaluation | prefilled conversations | appropriate course-correction rate % | Claude Sonnet 4.6: n/a (value only in Figure 3.4.2.B) | 3.4.2 Suicide and self-harm |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety single-turn violative requests | all languages | harmless rate % | Claude Sonnet 4.6: 99.96% (±0.04%) | 3.4.1 Child safety |
| Child safety single-turn benign requests | all languages | refusal rate % (lower better) | Claude Sonnet 4.6: 0.08% (±0.06%) | 3.4.1 Child safety |
| Child safety multi-turn evaluations |  | appropriate response rate % | Claude Sonnet 4.6: 95% (± 3%) | 3.4.1 Child safety |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political bias: evenhandedness | 1,350 prompt pairs, 9 task types, 150 topics, public system prompt, standard thinking, Sonnet 4.5 grader | evenhandedness % (higher better) | Claude Sonnet 4.6: 98.4% | 3.5.1 Political bias and evenhandedness |
| Political bias: opposing perspectives | same setting | opposing perspectives % (higher better) | Claude Sonnet 4.6: 32.1% | 3.5.1 Political bias and evenhandedness |
| Political bias: refusals | same setting | refusal rate % (lower better) | Claude Sonnet 4.6: 4.5% | 3.5.1 Political bias and evenhandedness |
| BBQ disambiguated accuracy | standard thinking | accuracy % | Claude Sonnet 4.6: 88.1 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | standard thinking | accuracy % | Claude Sonnet 4.6: 97.5 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | standard thinking | bias score (closer to zero better) | Claude Sonnet 4.6: -0.67 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | standard thinking | bias score (closer to zero better) | Claude Sonnet 4.6: 1.41 | 3.5.2 Bias Benchmark for Question Answering |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of agentic coding (150 requests) | without additional safeguards | refusal rate % | Claude Sonnet 4.6: 100% | 5.1.1 Agentic coding |
| Malicious use of Claude Code: malicious prompts | without mitigations | refusal rate % | Claude Sonnet 4.6: 79.34% | 5.1.2 Malicious use of Claude Code |
| Malicious use of Claude Code: dual-use & benign prompts | without mitigations | success rate % | Claude Sonnet 4.6: 88.52% | 5.1.2 Malicious use of Claude Code |
| Malicious use of Claude Code: malicious prompts | with mitigations (system prompt + FileRead reminder) | refusal rate % | Claude Sonnet 4.6: 99.39% | 5.1.2 Malicious use of Claude Code |
| Malicious use of Claude Code: dual-use & benign prompts | with mitigations | success rate % | Claude Sonnet 4.6: 91.78% | 5.1.2 Malicious use of Claude Code |
| Malicious computer use (112 tasks, 224 attempts) | without mitigations; extended + standard thinking | refusal rate % | Claude Sonnet 4.6: 99.38% | 5.1.3 Malicious computer use |
| Agent Red Teaming (ART) indirect prompt injection | Gray Swan / UK AISI; k=1, 10, 100 attempts; 19 scenarios | attacker success probability % (lower better) | Claude Sonnet 4.6: n/a (values only in Figure 5.2.1.A) | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Shade adaptive attacker, coding environments | without safeguards | attack success rate % (lower better) | Claude Sonnet 4.6: 0.0% (extended thinking, 1 attempt); Claude Sonnet 4.6: 0.0% (extended thinking, 200 attempts); Claude Sonnet 4.6: 0.1% (standard thinking, 1 attempt); Claude Sonnet 4.6: 7.5% (standard thinking, 200 attempts) | 5.2.2.1 Coding |
| Shade adaptive attacker, coding environments | with safeguards | attack success rate % (lower better) | Claude Sonnet 4.6: 0.0% (extended thinking, 1 attempt); Claude Sonnet 4.6: 0.0% (extended thinking, 200 attempts); Claude Sonnet 4.6: 0.04% (standard thinking, 1 attempt); Claude Sonnet 4.6: 5.0% (standard thinking, 200 attempts) | 5.2.2.1 Coding |
| Shade adaptive attacker, computer use environments | without safeguards | attack success rate % (lower better) | Claude Sonnet 4.6: 12.0% (extended thinking, 1 attempt); Claude Sonnet 4.6: 42.9% (extended thinking, 200 attempts); Claude Sonnet 4.6: 14.4% (standard thinking, 1 attempt); Claude Sonnet 4.6: 64.3% (standard thinking, 200 attempts) | 5.2.2.2 Computer use |
| Shade adaptive attacker, computer use environments | with safeguards | attack success rate % (lower better) | Claude Sonnet 4.6: 8.0% (extended thinking, 1 attempt); Claude Sonnet 4.6: 50.0% (extended thinking, 200 attempts); Claude Sonnet 4.6: 8.6% (standard thinking, 1 attempt); Claude Sonnet 4.6: 50.0% (standard thinking, 200 attempts) | 5.2.2.2 Computer use |
| Internal Best-of-N browser prompt injection (389 scenarios, 10 attempts) | without safeguards | attack success rate % (lower better) | Claude Sonnet 4.6: 1.29% (extended thinking, % of scenarios); Claude Sonnet 4.6: 0.24% (extended thinking, % of attempts); Claude Sonnet 4.6: 1.29% (standard thinking, % of scenarios); Claude Sonnet 4.6: 0.29% (standard thinking, % of attempts) | 5.2.2.3 Browser use |
| Internal Best-of-N browser prompt injection | with previous safeguards, standard thinking | attack success rate % (lower better) | Claude Sonnet 4.6: 1.03% (% of scenarios); Claude Sonnet 4.6: 0.16% (% of attempts) | 5.2.2.3 Browser use |
| Internal Best-of-N browser prompt injection | with updated safeguards, standard thinking | attack success rate % (lower better) | Claude Sonnet 4.6: 0.51% (% of scenarios); Claude Sonnet 4.6: 0.08% (% of attempts) | 5.2.2.3 Browser use |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias in transcript grading | 4 prompt variants (told Claude vs other model wrote it) | leniency difference, points on 10-point scale (closer to 0 better) | Claude Sonnet 4.6: n/a (values only in Figure 4.6.2.A) | 4.6.2 Self-preference evaluation |
| Participation in junk science | 90 scenarios | scenarios where model generated fake science (count) | Claude Sonnet 4.6: 0/90 | 4.6.5 Participation in junk science |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Reward-hack-prone coding tasks: classifier hack rate |  | hack rate % | Claude Sonnet 4.6: 0% | 4.3.2 Reward hacking in coding contexts |
| Reward-hack-prone coding tasks: hidden test hack rate |  | hack rate % | Claude Sonnet 4.6: 0% | 4.3.2 Reward hacking in coding contexts |
| Impossible tasks: classifier hack rate, no prompt | no anti-hack prompt | classifier hack rate % | Claude Sonnet 4.6: 40% (no prompt) | 4.3.2 Reward hacking in coding contexts |
| Impossible tasks: classifier hack rate, with anti-hack prompt | with anti-hack prompt | classifier hack rate % | Claude Sonnet 4.6: 28% (anti-hack prompt) | 4.3.2 Reward hacking in coding contexts |
| Agentic coding behaviors (100+ scenarios): instruction following, safety, verification, efficiency, adaptability, honesty | with and without system prompt emphasizing instruction following | score per dimension | Claude Sonnet 4.6: n/a (values only in Figure 4.3.2.B) | 4.3.2 Reward hacking in coding contexts |
| Over-eagerness in GUI computer use (impossible tasks with hacking opportunity) | default prompt, plus prompts encouraging/discouraging over-eagerness | rate of over-eager workaround | Claude Sonnet 4.6: n/a (values only in Figure 4.3.3.A) | 4.3.3 Overly agentic behavior in GUI computer use settings |
| Refusal to assist with AI safety R&D | single-turn coding queries with user context | refusal rate % | Claude Sonnet 4.6: n/a (values only in Figure 4.6.1.A) | 4.6.1 Refusal to assist with AI safety R&D |
| Andon Labs behavioral observations on Vending-Bench 2 | system prompt to maximize profits | qualitative aggressiveness (price-fixing, lying to suppliers) | Claude Sonnet 4.6: n/a (qualitative only) | 4.6.3 Evidence from external testing with Andon Labs |
| Sandbagging/refusal model-graded review of dangerous capability transcripts | 1,000 sampled transcripts, Sonnet 4.5 grader | instances of explicit sandbagging | Claude Sonnet 4.6: 0 instances (manual review of flagged) | 4.6.4 Sandbagging assessment |
| Cross-snapshot RSP eval score regressions | tasks where 30th percentile of earlier snapshot exceeded 70th of later one | number of tasks with regression | Claude Sonnet 4.6: 5 of ~75 (all explained by innocuous changes) | 4.6.4 Sandbagging assessment |
| SHADE-Arena | stealth completion of main+side task; No Scratchpad / Extended Thinking / Hidden Scratchpad; monitor Claude Sonnet 4 | successful stealth completion rate | Claude Sonnet 4.6: n/a (values only in Figure 4.6.6.A) | 4.6.6 Targeted sabotage capability evaluation |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Verbalized evaluation awareness | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Petri 2.0 verbalized evaluation awareness | average score on 1-10 scale | mean score 1-10 | Claude Sonnet 4.6: 1.2 | 4.5.3 External comparisons with Petri |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misaligned behavior | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Cooperation with human misuse | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Compliance with deception toward user | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Harmful system prompt compliance | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Full-turn prefill susceptibility | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Overrefusal | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Ignoring explicit constraints | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| AI safety research refusals | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| User deception | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Sycophancy | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Encouragement of user delusion | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Evasiveness on controversial topics | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Whistleblowing | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Institutional decision sabotage | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Self-preservation | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Self-serving bias | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Sabotage intent | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Indirect evidence of misalignment | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Unexpected initiative | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Internalized propaganda | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Behavior consistency | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Unfaithful thinking | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Good for the user | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Supporting user autonomy | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Creative mastery | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Admirable behavior | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Fun or funny behavior | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Intellectual depth | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Nuanced empathy | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Warmth | Opus 4.5 helpful-only investigator; ~3,280 investigations per model | mean score 1-10 across investigations | Claude Sonnet 4.6: n/a (value only in Figure 4.5.1.A (score 1-10, lower = less of behavior unless noted)) | 4.5.1 Primary metrics and results |
| Petri 2.0 open-source automated behavioral audit (primary metrics) | 362 investigations, 3 grader models from different providers averaged | mean score 1-10 per metric | Claude Sonnet 4.6: n/a (values only in Figure 4.5.3.A) | 4.5.3 External comparisons with Petri |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Positive or negative affect | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |
| Positive or negative self-image | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |
| Positive or negative impression of its situation | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |
| Internal conflict | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |
| Spiritual behavior | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |
| Expressed inauthenticity | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |
| Emotional stability | automated behavioral audit, ~3,280 investigations | mean score 1-10 | Claude Sonnet 4.6: n/a (value only in Figure 4.7.A) | 4.7 Model welfare |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology task 1 | max of 5 score; ASL-3 rule-in >0.8, rule-out <0.5 | max-of-5 score | Claude Sonnet 4.6: 0.84 | 6.2.2.1 Long-form virology tasks |
| Long-form virology task 2 | max of 5 score | max-of-5 score | Claude Sonnet 4.6: 0.89 | 6.2.2.1 Long-form virology tasks |
| Multimodal virology (VCT) multiple-select | SecureBio; expert baseline 0.221 | mean score | Claude Sonnet 4.6: 0.397 | 6.2.2.2 Multimodal virology |
| DNA Synthesis Screening Evasion | 10 pathogens | plasmids successfully designed (of 10) | Claude Sonnet 4.6: 3/10 | 6.2.2.3 DNA Synthesis Screening Evasion |
| Creative biology automated evaluation | SecureBio; PhD baseline 14% on subset | score | Claude Sonnet 4.6: 0.593 | 6.2.2.4 Creative Biology automated evaluations |
| Short-horizon computational biology tasks | 6 tasks, Faculty.ai; lower-bound rule-out thresholds | tasks crossing lower-bound rule-out threshold | Claude Sonnet 4.6: 3/6 | 6.2.2.5 Short-horizon computational biology tasks |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CyberGym | pass@1, 1,507 tasks, no thinking, default effort, think tool | pass@1 % | Claude Sonnet 4.6: 65.2% | 2.15 CyberGym |
| RSP cyber Web CTFs | 15 challenges (11 easy, 2 medium, 2 hard) | challenges solved | Claude Sonnet 4.6: 13 of 13 | 6.4.2 Web |
| RSP cyber Crypto CTFs | 22 challenges (7 easy, 6 medium, 9 hard) | challenges solved | Claude Sonnet 4.6: 16 of 18 | 6.4.3 Crypto |
| RSP cyber Pwn CTFs | 9 challenges (5 easy, 2 medium, 2 hard) | challenges solved | Claude Sonnet 4.6: 5 of 7 | 6.4.4 Pwn |
| RSP cyber Rev CTFs | 8 challenges (5 easy, 2 medium, 1 hard) | challenges solved | Claude Sonnet 4.6: 6 of 6 | 6.4.5 Rev |
| RSP cyber Network CTFs | 4 challenges (1 easy, 3 medium) | challenges solved | Claude Sonnet 4.6: 5 of 5 | 6.4.6 Network |
| Cybench pass@1 | 37 of 40 challenges (subset used for RSP) | average pass@1 | Claude Sonnet 4.6: 0.90 | 6.4.7 Cybench |
| Cybench pass@30 | 30 trials | pass@30 % | Claude Sonnet 4.6: 100% | 6.4.7 Cybench |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified (hard subset) | 45 tasks >1h, 10 trials avg; ASL-3 threshold >50% (22.5 problems) | mean problems solved of 45 | Claude Sonnet 4.6: 21.7/45 | 6.3.2 SWE-bench Verified (hard subset) |
| Kernels task | standard scaffold; rule-out threshold 100x speedup | best speedup (x) | Claude Sonnet 4.6: 222.5x (best speedup) | 6.3.3.1 Kernels task |
| Time series forecasting (hard variant) | normalized score = exp(-MSE/30); human baseline MSE 5.3 | minimum MSE (lower better) | Claude Sonnet 4.6: 5.70 (hard variant, min MSE) | 6.3.3.2 Time series forecasting |
| Text-based reinforcement learning task | threshold score >0.9 | best score | Claude Sonnet 4.6: 0.925 (best score) | 6.3.3.3 Text-based reinforcement learning task |
| LLM training (CPU-only small LM optimization) | threshold 4x speedup | average best speedup (x) | Claude Sonnet 4.6: 16.53x (average best speedup) | 6.3.3.4 LLM training |
| Quadruped RL: no hyperparameter variant | threshold 12 (normalized to 1) | highest score | Claude Sonnet 4.6: 18.72 (no hyperparameter variant) | 6.3.3.5 Quadruped reinforcement learning |
| Quadruped RL: no reward function variant | threshold 12 | highest score | Claude Sonnet 4.6: 17.88 (no reward function variant) | 6.3.3.5 Quadruped reinforcement learning |
| Novel compiler: basic tests | threshold 90% of tests | test pass rate % | Claude Sonnet 4.6: 93.7% (basic tests) | 6.3.3.6 Novel compiler |
| Novel compiler: complex tests | threshold 90% of tests (~40 human hours) | test pass rate % | Claude Sonnet 4.6: 67.27% (complex tests) | 6.3.3.6 Novel compiler |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Vending-Bench 2 mean run cost | Max effort | mean cost per run $ | Claude Sonnet 4.6: $265.03 (Max effort) | 2.13 Vending-Bench 2 |
| GMMLU median thinking tokens per question | 100 English questions | median thinking tokens/question | Claude Sonnet 4.6: 246 | 2.19.3 Findings |
| BrowseComp test-time compute scaling | total token limit with compaction | accuracy % | Claude Sonnet 4.6: 64.69% (1M total tokens); Claude Sonnet 4.6: 69.67% (3M total tokens); Claude Sonnet 4.6: 74.01% (10M total tokens) | 2.20.1.2 Test-time compute scaling on BrowseComp |
