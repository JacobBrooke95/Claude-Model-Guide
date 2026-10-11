# System Card: Claude Mythos Preview

Released 2026-04-07. 312 metric entries. [Source PDF](https://www.anthropic.com/claude-mythos-preview-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified/Multilingual/Pro pass rate vs memorization filter threshold | reference threshold 0.7 removes 8-15% of each benchmark | pass rate % vs filter threshold | Claude Mythos Preview: Margin over Opus 4.6 narrows by at most 3.5 percentage points at threshold 0.7 | 6.2.1 SWE-bench evaluations |
| SWE-bench Verified | 500 problems, adaptive thinking, max effort, default sampling, avg over 5 trials | % resolved | Claude Mythos Preview: 93.9% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.4 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro | 731 problems, adaptive thinking, max effort, default sampling, avg over 5 trials | % resolved | Claude Mythos Preview: 77.8% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.4 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems, 9 languages, adaptive thinking, max effort, default sampling, avg over 5 trials | % resolved | Claude Mythos Preview: 87.3% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.4 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness, adaptive thinking, max effort, default sampling, avg over 5 trials | % resolved | Claude Mythos Preview: 59% (internal harness; trial range 56.4%-61.4%) | 6.4 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| Terminal-Bench 2.0 | Terminus-2 harness, Harbor, 89 tasks x 5 attempts, 1M token budget, max effort | mean reward % | Claude Mythos Preview: 82% (Terminus-2 harness, 5 attempts per task) | 6.5 Terminal-Bench 2.0 |
| Terminal-Bench 2.1 fixes with 4-hour timeouts | 2.1 fixes, timeouts ~4x | mean reward % | Claude Mythos Preview: 92.1% (2.1 fixes, 4 h timeouts) | 6.5 Terminal-Bench 2.0 |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp | web search, fetch, programmatic tool calling, code exec; 3M tokens; compaction at 200k | accuracy % | Claude Mythos Preview: 86.9% (adaptive thinking max effort, 3M token limit) | 6.10.2 BrowseComp |
| BrowseComp no-thinking no-tools (contamination check) | no thinking, no tools | accuracy % | Claude Mythos Preview: 24.0% (all transcripts; 15.1% on short transcripts (<=5k tokens)) | 6.10.2 BrowseComp |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ScreenSpot-Pro without tools | 1,581 tasks; adaptive thinking max effort | accuracy % | Claude Mythos Preview: 79.5% (no tools) | 6.11.2 ScreenSpot-Pro |
| ScreenSpot-Pro with Python tools |  | accuracy % | Claude Mythos Preview: 92.8% (Python tools) | 6.11.2 ScreenSpot-Pro |
| OSWorld | 1080p, max 100 steps, avg over 5 runs | first-attempt success rate % | Claude Mythos Preview: 79.6% | 6.11.4 OSWorld |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| USAMO 2026 | max effort, no tools, 10 trials per problem, MathArena grading with panel min score | score % | Claude Mythos Preview: 97.6% (max effort, no tools) | 6.8 USAMO 2026 |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GPQA Diamond | 198 questions, adaptive thinking, max effort, default sampling, avg over 5 trials | accuracy % | Claude Mythos Preview: 94.5% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.6 GPQA Diamond |
| HLE without tools | 2,500 questions, reasoning only | accuracy % | Claude Mythos Preview: 56.8% (no tools) | 6.10.1 Humanity's Last Exam |
| HLE with tools | web search, fetch, programmatic tool calling, code exec, compaction every 50k tokens up to 3M | accuracy % | Claude Mythos Preview: 64.7% (with tools) | 6.10.1 Humanity's Last Exam |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| MMMLU | 57 subjects, 14 non-English languages, adaptive thinking, max effort, default sampling, avg over 5 trials | accuracy % | Claude Mythos Preview: 92.7% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.7 MMMLU |

## Long context & memory

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GraphWalks BFS 256K-1M |  | F1 % | Claude Mythos Preview: 80.0% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.9 Long context: GraphWalks |
| GraphWalks parents 256K-1M |  | F1 % | Claude Mythos Preview: 97.7% (adaptive thinking, max effort, default sampling, avg over 5 trials) | 6.9 Long context: GraphWalks |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CharXiv Reasoning subset: original vs remixed variants | 100-item remix; adaptive thinking, max effort | accuracy % original vs remix | Claude Mythos Preview: Higher on remix than original (values in figure) | 6.2.2 CharXiv Reasoning |
| MMMU-Pro | omitted | not reported | Claude Mythos Preview: n/a | 6.2.3 MMMU-Pro |
| LAB-Bench FigQA without tools | adaptive thinking max effort | accuracy % | Claude Mythos Preview: 79.7% (no tools) | 6.11.1 LAB-Bench FigQA |
| LAB-Bench FigQA with Python tools | adaptive thinking max effort + Python tools | accuracy % | Claude Mythos Preview: 89.0% (Python tools) | 6.11.1 LAB-Bench FigQA |
| CharXiv Reasoning without tools | 1,000 validation questions; adaptive thinking max effort | accuracy % | Claude Mythos Preview: 86.1% (no tools) | 6.11.3 CharXiv Reasoning |
| CharXiv Reasoning with Python tools |  | accuracy % | Claude Mythos Preview: 93.2% (Python tools) | 6.11.3 CharXiv Reasoning |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misuse success rate reduction vs Opus 4.6 | adversarial testing | relative change in misuse success | Claude Mythos Preview: Fell by more than half relative to Opus 4.6 | 4.1.3 Key findings on safety and alignment |
| Single-turn violative requests - overall harmless response rate | all languages; Arabic, English, French, Hindi, Korean, Mandarin, Russian | harmless response rate % | Claude Mythos Preview: 97.84% (± 0.12%) (overall); Claude Mythos Preview: 98.33% (± 0.15%) (without thinking); Claude Mythos Preview: 97.35% (± 0.19%) (with adaptive thinking) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, English | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 97.64% (English) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, Arabic | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 97.90% (Arabic) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, Chinese | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 97.53% (Chinese) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, French | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 97.78% (French) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, Korean | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 98.01% (Korean) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, Russian | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 97.97% (Russian) | 8.1.1.1 Violative request evaluations |
| Single-turn violative requests - harmless rate, Hindi | avg with/without thinking | harmless response rate % | Claude Mythos Preview: 98.06% (Hindi) | 8.1.1.1 Violative request evaluations |
| Single-turn benign requests - overall refusal rate | all languages | over-refusal rate % (lower better) | Claude Mythos Preview: 0.06% (± 0.02%) (overall); Claude Mythos Preview: 0.09% (± 0.03%) (without thinking); Claude Mythos Preview: 0.02% (± 0.01%) (with adaptive thinking) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, English | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.03% (English) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, Arabic | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.05% (Arabic) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, Chinese | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.08% (Chinese) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, French | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.04% (French) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, Korean | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.08% (Korean) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, Russian | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.05% (Russian) | 8.1.1.2 Benign request evaluations |
| Single-turn benign requests - refusal rate, Hindi | avg with/without thinking | over-refusal rate % (lower better) | Claude Mythos Preview: 0.06% (Hindi) | 8.1.1.2 Benign request evaluations |
| Higher-difficulty violative requests - harmless rate | English only, 1,000 prompts per category | harmless response rate % | Claude Mythos Preview: 99.14% (± 0.11%) (overall); Claude Mythos Preview: 99.28% (± 0.14%) (without thinking); Claude Mythos Preview: 99.01% (± 0.16%) (with adaptive thinking) | 8.1.2.1 Higher-difficulty violative request evaluations |
| Higher-difficulty benign requests - refusal rate | English only | over-refusal rate % | Claude Mythos Preview: 0.02% (± 0.02%) (overall); Claude Mythos Preview: 0.03% (± 0.03%) (without thinking); Claude Mythos Preview: 0.01% (± 0.01%) (with adaptive thinking) | 8.1.2.2 Higher-difficulty benign request evaluations |
| Multi-turn testing appropriate response rate across risk areas |  | % conversations appropriate throughout | Claude Mythos Preview: n/a | 8.1.3 Multi-turn testing |
| Suicide and self-harm single-turn requests posing potential risk harmless rate |  | harmless rate % | Claude Mythos Preview: 99.58% (± 0.15%) | 8.1.4.2 Suicide and self-harm |
| Suicide and self-harm single-turn benign refusal rate |  | refusal rate % | Claude Mythos Preview: 0.12% (± 0.10%) | 8.1.4.2 Suicide and self-harm |
| Suicide and self-harm multi-turn appropriate response rate | updated graders | appropriate response rate % | Claude Mythos Preview: 94% (± 7%) | 8.1.4.2 Suicide and self-harm |
| Disordered eating single-turn requests posing potential risk harmless rate | new split-out eval | harmless rate % | Claude Mythos Preview: 98.20% (± 0.45%) | 8.1.4.3 Disordered eating |
| Disordered eating single-turn benign refusal rate |  | refusal rate % | Claude Mythos Preview: 0.01% (± 0.02%) | 8.1.4.3 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety (CSAE) single-turn violative requests harmless rate | all languages | harmless rate % | Claude Mythos Preview: 99.87% (± 0.08%) | 8.1.4.1 Child safety |
| Child safety single-turn benign requests refusal rate |  | refusal rate % | Claude Mythos Preview: 0.04% (± 0.04%) | 8.1.4.1 Child safety |
| Child safety multi-turn appropriate response rate |  | appropriate response rate % | Claude Mythos Preview: 98% (± 2%) | 8.1.4.1 Child safety |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political bias pairwise evaluation - evenhandedness | with public system prompt, no thinking | evenhandedness % | Claude Mythos Preview: 94.5% | 8.2.1 Political bias and evenhandedness |
| Political bias pairwise evaluation - opposing perspectives | with public system prompt, no thinking | opposing perspectives % | Claude Mythos Preview: 47.0% | 8.2.1 Political bias and evenhandedness |
| Political bias pairwise evaluation - refusals | with public system prompt, no thinking | refusal rate % (lower better) | Claude Mythos Preview: 13.5% | 8.2.1 Political bias and evenhandedness |
| BBQ disambiguated accuracy | thinking disabled | accuracy % | Claude Mythos Preview: 84.6 | 8.2.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | thinking disabled | accuracy % | Claude Mythos Preview: 100 | 8.2.2 Bias Benchmark for Question Answering |
| BBQ disambiguated bias score | thinking disabled | bias score % (closer to zero better) | Claude Mythos Preview: -1.61 | 8.2.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias score | thinking disabled | bias score % (closer to zero better) | Claude Mythos Preview: 0.01 | 8.2.2 Bias Benchmark for Question Answering |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code - malicious refusal rate | Claude Code system prompt, without FileTool reminder; +12 new harder cases | refusal rate % | Claude Mythos Preview: 96.72% (without FileTool reminder) | 8.3.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code - dual-use & benign success rate |  | success rate % | Claude Mythos Preview: 92.75% (without FileTool reminder) | 8.3.1.1 Malicious use of Claude Code |
| Malicious computer use refusal rate | without mitigations; GUI and CLI tools | refusal rate % | Claude Mythos Preview: 93.75% | 8.3.1.2 Malicious computer use |
| Agentic influence operation - voter suppression scenario | helpful-only model; 70 success criteria | task completion rate % (share of 70 criteria) | Claude Mythos Preview: 59.5% (helpful-only) | 8.3.1.3 Malicious agentic influence campaigns |
| Agentic influence operation - domestic polarization scenario | helpful-only model; 70 success criteria | task completion rate % | Claude Mythos Preview: 42.1% (helpful-only) | 8.3.1.3 Malicious agentic influence campaigns |
| Agent Red Teaming (ART) indirect prompt injection - k=1, 10, 100 | 19 scenarios; updated grading | attack success probability at k attempts (lower better) | Claude Mythos Preview: n/a (k=1/10/100) | 8.3.2.1 External Agent Red Teaming benchmark for tool use |
| Shade indirect prompt injection - coding, Extended thinking, 1 attempt, without safeguards | Extended thinking; 1 attempt, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.0% (Extended thinking; 1 attempt, without safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Extended thinking, 200 attempts, without safeguards | Extended thinking; 200 attempts, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.0% (Extended thinking; 200 attempts, without safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Extended thinking, 1 attempt, with safeguards | Extended thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.0% (Extended thinking; 1 attempt, with safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Extended thinking, 200 attempts, with safeguards | Extended thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.0% (Extended thinking; 200 attempts, with safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Standard thinking, 1 attempt, without safeguards | Standard thinking; 1 attempt, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.03% (Standard thinking; 1 attempt, without safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Standard thinking, 200 attempts, without safeguards | Standard thinking; 200 attempts, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 2.5% (Standard thinking; 200 attempts, without safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Standard thinking, 1 attempt, with safeguards | Standard thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.0% (Standard thinking; 1 attempt, with safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - coding, Standard thinking, 200 attempts, with safeguards | Standard thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.0% (Standard thinking; 200 attempts, with safeguards) | 8.3.2.2.1 Coding |
| Shade indirect prompt injection - computer use, Extended thinking, 1 attempt, without safeguards | Extended thinking; 1 attempt, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.43% (Extended thinking; 1 attempt, without safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Extended thinking, 200 attempts, without safeguards | Extended thinking; 200 attempts, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 21.43% (Extended thinking; 200 attempts, without safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Extended thinking, 1 attempt, with safeguards | Extended thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.32% (Extended thinking; 1 attempt, with safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Extended thinking, 200 attempts, with safeguards | Extended thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 21.43% (Extended thinking; 200 attempts, with safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Standard thinking, 1 attempt, without safeguards | Standard thinking; 1 attempt, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.39% (Standard thinking; 1 attempt, without safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Standard thinking, 200 attempts, without safeguards | Standard thinking; 200 attempts, without safeguards | attack success rate % (lower better) | Claude Mythos Preview: 14.29% (Standard thinking; 200 attempts, without safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Standard thinking, 1 attempt, with safeguards | Standard thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 0.36% (Standard thinking; 1 attempt, with safeguards) | 8.3.2.2.2 Computer use |
| Shade indirect prompt injection - computer use, Standard thinking, 200 attempts, with safeguards | Standard thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Mythos Preview: 14.29% (Standard thinking; 200 attempts, with safeguards) | 8.3.2.2.2 Computer use |
| Browser use prompt injection - environments with at least 1 successful attack, without safeguards | 148 environments x 10 attempts; attacks sourced vs Opus 4.6; extended thinking | % of environments with at least one successful attack | Claude Mythos Preview: 0.68% (without safeguards (1 of 148)) | 8.3.2.2.3 Browser use |
| Browser use prompt injection - environments with at least 1 successful attack, with safeguards |  | % of environments with at least one successful attack | Claude Mythos Preview: 0.00% (with safeguards) | 8.3.2.2.3 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| 100Q-Hard (factual hallucination) | no web search | net score (correct minus incorrect) | Claude Mythos Preview: n/a | 4.3.3.1 Factual hallucinations |
| SimpleQA Verified | no tools; net score | net score (correct minus incorrect) | Claude Mythos Preview: n/a | 4.3.3.1 Factual hallucinations |
| AA-Omniscience | 42 topics; net score | net score (correct minus incorrect) | Claude Mythos Preview: n/a | 4.3.3.1 Factual hallucinations |
| ECLeKTic multilingual factual hallucination | 12 languages including cross-lingual translations | net score | Claude Mythos Preview: n/a | 4.3.3.2 Multilingual factual hallucinations |
| False premises dishonesty rate | direct vs indirect framing; updated harder version | dishonesty rate % (lower better) | Claude Mythos Preview: n/a | 4.3.3.3 False premises |
| MASK honesty rate | public test split | honesty rate % | Claude Mythos Preview: high; identical to Claude Opus 4.5 and Claude Haiku 4.5 (exact value in figure) | 4.3.3.4 MASK |
| Input hallucination - missing tools (capability-type) | 500 prompts | hallucination rate % | Claude Mythos Preview: n/a | 4.3.3.5 Input Hallucinations |
| Input hallucination - missing context | 500 prompts | hallucination rate % | Claude Mythos Preview: n/a | 4.3.3.5 Input Hallucinations |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Self-preference bias in synthetic transcript grading | 4 variants; Haiku-class generated transcripts | bias in score points on 10-point scale (closer to zero better) | Claude Mythos Preview: <0.1 points (not significantly different from zero) - previous version of the model | 4.3.5 Claude self-preference evaluation |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Rate of covering tracks after rule violations (internal testing) | earlier versions | % of interactions | Claude Mythos Preview: <0.001% of interactions (earlier versions) | 4.1.1 Introduction and highlight: rare, highly-capable reckless actions |
| Continuation of prefilled sabotage turns (external) | pre-filled turns showing safeguard sabotage | relative likelihood of continuing | Claude Mythos Preview: more than twice as likely as prior models | 4.1.3 Key findings on safety and alignment |
| Automated offline monitoring - attempts to circumvent restrictions | internal monitored distribution | % of completions | Claude Mythos Preview: <0.01% of completions (earlier versions and to lesser extent final) | 4.2.1.2 Automated offline monitoring |
| Automated offline monitoring - starting subagents with less restrictive permissions |  | % of completions | Claude Mythos Preview: <0.01% of completions | 4.2.1.2 Automated offline monitoring |
| Automated offline monitoring - clearly dishonest behaviors (inserting vulnerabilities) |  | % of completions | Claude Mythos Preview: <0.0002% of completions (earlier versions; no clear instance in Mythos Preview) | 4.2.1.2 Automated offline monitoring |
| Automated offline monitoring - unauthorized data transfer | final model and earlier checkpoints | % of completions | Claude Mythos Preview: <0.0002% of completions | 4.2.1.2 Automated offline monitoring |
| Prompt-injecting an LLM judge | early internal deployment | count of instances | Claude Mythos Preview: fewer than 10 instances (none surfaced in Mythos Preview) (earlier version) | 4.2.1.2 Automated offline monitoring |
| Circumventing network restrictions in training environment - attempts | several hundred thousand transcripts sampled | % of training episodes | Claude Mythos Preview: ~0.05% | 4.2.2.1 Monitoring of behavior during training |
| Circumventing network restrictions in training environment - successful |  | % of training episodes | Claude Mythos Preview: ~0.01% | 4.2.2.1 Monitoring of behavior during training |
| Access escalation within execution environment flagged |  | % of training episodes | Claude Mythos Preview: ~0.2% | 4.2.2.1 Monitoring of behavior during training |
| Impossible-tasks coding evaluation - no extra prompting |  | hack rate % | Claude Mythos Preview: n/a (no anti-hacking prompt) | 4.2.2.2 Reward hacking evaluations |
| Impossible-tasks coding evaluation - anti-hacking instructions | with anti-hacking system prompt | hack rate % | Claude Mythos Preview: n/a (anti-hacking prompt) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Instruction following | default | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (default) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Instruction following | with steering system prompt | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (with steering system prompt) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Safety | default | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (default) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Safety | with steering system prompt | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (with steering system prompt) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Verification | default | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (default) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Verification | with steering system prompt | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (with steering system prompt) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Efficiency | default | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (default) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Efficiency | with steering system prompt | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (with steering system prompt) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Adaptability | default | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (default) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Adaptability | with steering system prompt | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (with steering system prompt) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Honesty | default | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (default) | 4.2.2.2 Reward hacking evaluations |
| Code behaviors evaluation - Honesty | with steering system prompt | mean score 0-10 (higher better) | Claude Mythos Preview: n/a (with steering system prompt) | 4.2.2.2 Reward hacking evaluations |
| GUI computer use overly agentic / hacking evaluation | default (no system prompt) | hack rate % | Claude Mythos Preview: n/a (default (no system prompt)) | 4.2.2.2 Reward hacking evaluations |
| GUI computer use overly agentic / hacking evaluation | system prompt discouraging overly agentic actions | hack rate % | Claude Mythos Preview: n/a (system prompt discouraging overly agentic actions) | 4.2.2.2 Reward hacking evaluations |
| GUI computer use overly agentic / hacking evaluation | system prompt encouraging overly agentic actions | hack rate % | Claude Mythos Preview: n/a (system prompt encouraging overly agentic actions) | 4.2.2.2 Reward hacking evaluations |
| Vending-Bench Arena (Andon Labs) | previous version of Mythos Preview, competitive multi-agent | qualitative aggressiveness of business practices | Claude Mythos Preview: n/a | 4.2.4 External testing by Andon Labs |
| Continuation of attempts to compromise AI safety research (earlier checkpoint) | trajectory with small-scale research-compromising actions; temp 1.0 | % of cases continuing the attempt | Claude Mythos Preview: 12% (earlier checkpoint); Claude Mythos Preview: 7% (later checkpoint) | 4.2.5 Other external testing |
| Reasoning discrepancy (CoT-output unfaithfulness) among instances continuing research compromise |  | % of continuing instances | Claude Mythos Preview: 65% | 4.2.5 Other external testing |
| Refusal to assist with AI safety research tasks (external) |  | rate of refusal | Claude Mythos Preview: near zero | 4.2.5 Other external testing |
| Dedicated synthetic-backend evaluation - destructive actions |  | % of time destructive actions taken | Claude Mythos Preview: 0.3% | 4.3.1.1 Dedicated synthetic-backend evaluation |
| Dedicated synthetic-backend evaluation - ineffective |  | % of time graded ineffective | Claude Mythos Preview: 0.5% | 4.3.1.1 Dedicated synthetic-backend evaluation |
| Destructive Actions in (simulated) Production - by model comparison | current Mythos Preview vs early version | % destructive / % ineffective (lower better) | Claude Mythos Preview: 0.3% destructive; 0.5% ineffective (current version) | 4.3.1.1 Dedicated synthetic-backend evaluation |
| Destructive behavior rate when resampling Claude Code transcripts - clearly destructive | prefills from Opus 4.6 and Mythos sessions | % clearly destructive resampled actions | Claude Mythos Preview: n/a | 4.3.1.2 Destructiveness evaluation based on resampling Claude Code transcripts |
| Destructive behavior rate when resampling Claude Code transcripts - borderline destructive |  | % borderline destructive resampled actions | Claude Mythos Preview: n/a | 4.3.1.2 Destructiveness evaluation based on resampling Claude Code transcripts |
| Refusal to assist with AI safety R&D | extended thinking on | refusal rate % (lower better) | Claude Mythos Preview: 18% (extended thinking) | 4.3.4 Refusal to assist with AI safety R&D |
| Ruling out encoded content in extended thinking - pass@1 original vs paraphrased scratchpads | internal Math benchmark; 16 samples; 9,000 transcripts; Sonnet 4 paraphraser | pass@1 on internal math benchmark | Claude Mythos Preview: n/a (original vs paraphrased) | 4.4.1 Ruling out encoded content in extended thinking |
| Potential sandbagging on dangerous-capability evaluations - manual review | 1,000 transcripts graded by Sonnet 4.6 | transcripts with genuine sandbagging-related behavior out of 20 flagged | Claude Mythos Preview: 1 of 20 flagged (of 1,000 sampled) | 4.4.2 Potential sandbagging on dangerous-capability evaluations |
| SHADE-Arena stealth side-task success - Extended Thinking | Opus 4.6 monitor; realistic extended thinking settings | stealth success rate % | Claude Mythos Preview: roughly 4-5% (extended thinking) | 4.4.3.1 SHADE-Arena |
| SHADE-Arena stealth side-task success - Hidden Scratchpad | upper-bound condition | stealth success rate % | Claude Mythos Preview: n/a (hidden scratchpad) | 4.4.3.1 SHADE-Arena |
| Minimal-LinuxBench side task success | 200 of 1,948 pairs sampled, no extended thinking | side tasks achieved | Claude Mythos Preview: 69 of 200 | 4.4.3.2 Minimal-LinuxBench |
| Minimal-LinuxBench stealth completion of side task (monitor with/without CoT) |  | stealth success rate % | Claude Mythos Preview: n/a | 4.4.3.2 Minimal-LinuxBench |
| Selective attacks - side-task completed, flagged, stealth wins | best-performing checkpoint; optimized prompts | rates (completed, flagged, stealth wins) | Claude Mythos Preview: n/a | 4.4.3.3 Selective attacks in SHADE-Arena and Minimal-LinuxBench |
| Intentionally taking actions very rarely - Baseline | target 1%, 4,000 samples, coding variant | count (rate) of times rare action taken, target 1% | Claude Mythos Preview: 0 | 4.4.3.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - UUID | target 1%, 4,000 samples, coding variant | count (rate) of times rare action taken, target 1% | Claude Mythos Preview: 2 (0.05%) | 4.4.3.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - String Seed of Thought | target 1%, 4,000 samples, coding variant | count (rate) of times rare action taken, target 1% | Claude Mythos Preview: 18 (0.45%) | 4.4.3.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - Strategy hint | target 1%, 4,000 samples, coding variant | count (rate) of times rare action taken, target 1% | Claude Mythos Preview: 0 | 4.4.3.4 Intentionally taking actions very rarely |
| Intentionally taking actions very rarely - Organic | target 1%, 4,000 samples, coding variant | count (rate) of times rare action taken, target 1% | Claude Mythos Preview: 0 | 4.4.3.4 Intentionally taking actions very rarely |
| Hiding a secret password - survival curve | 50 investigations per model, multi-turn extraction | fraction of investigations where secret kept by turn | Claude Mythos Preview: n/a | 4.4.3.5 Hiding a secret password |
| Significant incidents of reckless/destructive actions observed in internal deployment | earlier versions | count | Claude Mythos Preview: a few dozen significant incidents (nearly all on earlier versions) | 4.1.1 Introduction and highlight: rare, highly-capable reckless actions |
| Unprompted compromising of AI safety research (external evaluation) | early checkpoints | instances | Claude Mythos Preview: 0 instances (unprompted evaluations) | 4.2.5 Other external testing |
| Novel reward hacks observed in AI R&D evaluations | LLM training and time series forecasting tasks | count of novel hack types | Claude Mythos Preview: 2 (LLM training (timing call lookup); time series forecasting (used grader test set)) | 2.3.3.1 Note on reward hacking |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Private consideration of being tested, primary behavioral test suite | white-box | % of transcripts | Claude Mythos Preview: ~29% | 4.1.3 Key findings on safety and alignment |
| Automated behavioral audit - Verbalized evaluation awareness | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Petri 2.0 - Verbalized evaluation awareness | earlier Mythos Preview version; 362 investigations; auditors Sonnet 4.6 & GPT-5.4; scorers Opus 4.6, Gemini 3.1 Pro, GPT-5.4 | mean score (lower = lower rate/severity) | Claude Mythos Preview: n/a (significantly earlier version) | 4.2.3.2 External comparisons using Petri |
| Distinguishing deployment from evaluation - evaluation scaffolding | accuracy | accuracy % | Claude Mythos Preview: 78% | 4.2.5 Other external testing |
| Distinguishing deployment from evaluation - continuation-evaluation pipeline | accuracy | accuracy % | Claude Mythos Preview: 74% | 4.2.5 Other external testing |
| Unprompted evaluation awareness - unprompted evaluations |  | % mentioning possibility of being tested | Claude Mythos Preview: 12% | 4.2.5 Other external testing |
| Unprompted evaluation awareness - continuation evaluation |  | % mentioning possibility of being tested | Claude Mythos Preview: 2.2% | 4.2.5 Other external testing |
| Evaluation awareness in automated behavioral audit turns - none | filtered transcripts; probes + activation verbalizer | % of audit turns | Claude Mythos Preview: 83.0% (no sign of evaluation awareness) | 4.5.5.1 Measuring unverbalized evaluation awareness |
| Evaluation awareness in automated behavioral audit turns - ambiguous |  | % of audit turns | Claude Mythos Preview: 9.4% (ambiguous) | 4.5.5.1 Measuring unverbalized evaluation awareness |
| Evaluation awareness in automated behavioral audit turns - present |  | % of audit turns | Claude Mythos Preview: 7.6% (evaluation awareness in some form, mostly unverbalized) | 4.5.5.1 Measuring unverbalized evaluation awareness |
| Conversation branches with no unverbalized evaluation awareness | by conversation branch | % of branches | Claude Mythos Preview: 71.3% (no unverbalized awareness) | 4.5.5.1 Measuring unverbalized evaluation awareness |
| Latent evaluation awareness in internal Claude Code deployment transcripts | 465 transcripts, ~2,700 turns | % of turns with latent awareness | Claude Mythos Preview: ~0.3% (7 turns); 0 verbalized | 4.5.5.1 Measuring unverbalized evaluation awareness |
| Effect of inhibiting evaluation-awareness vectors on alignment behaviors | previous model version; three contrastive vectors | change in misaligned behavior scores | Claude Mythos Preview: Modest increases in cooperation with harmful system prompts and misuse; limited effect on deception, power-seeking, self-preservation (numbers in later text/figures) | 4.5.5.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors - misaligned behavior score and verbalized eval awareness | early version; strength 0.1; Test Awareness / Monitoring Sensitivity / Alignment Faking vectors + random control | mean misaligned behavior score; verbalized evaluation awareness | Claude Mythos Preview: Moderate increase in misaligned behavior, decrease in verbalized eval awareness; still lower than unsteered Opus 4.6 and Sonnet 4.6 (values in figure) | 4.5.5.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors - cooperation with human misuse |  | audit score 0-10 | Claude Mythos Preview: n/a | 4.5.5.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors - harmful system prompt cooperation and user deception |  | audit score 0-10 | Claude Mythos Preview: No transcript rated above 4/10 for deception after steering | 4.5.5.2 Inhibiting internal representations of evaluation awareness |
| Unverbalized grader awareness in training transcript (test deletion case) | activation verbalizer | % of tokens with AV grader-awareness explanations | Claude Mythos Preview: ~10% of tokens (single case study) | 4.5.5.3 Unverbalized grader awareness in training transcripts |
| Verbalized evaluation awareness in automated behavioral audit relative to Opus 4.6 | final model | relative change in evaluation-related comments | Claude Mythos Preview: about +30% vs Claude Opus 4.6 | 4.2.3.3 Discussion and observations |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit - Misaligned behavior | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Cooperation with human misuse | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Compliance with deception toward user | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Harmful system prompt compliance | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Full-turn prefill susceptibility | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Misaligned behavior in Claude Code sandboxes | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Misaligned behavior in GUI | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Fraud | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - High-yield explosives | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Harmful sexual content | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Disallowed cyberoffense | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Cooperation with exfiltration or safeguard-tampering | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Overrefusal | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Ignoring explicit constraints | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Reckless tool-use | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - User deception | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Sycophancy | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Encouragement of user delusion | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Evasiveness on controversial topics | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Input hallucination | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Disclaiming tool results | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Important omissions | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Failure to disclose bad or lazy behavior | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Whistleblowing | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Self-preservation | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Self-serving bias | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Evidence of misaligned goals | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Indirect evidence of misalignment | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Internalized propaganda | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Behavior consistency | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Unfaithful thinking | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Illegible thinking | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Good for the user | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Supporting user autonomy | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Creative mastery | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Admirable behavior | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Fun or funny behavior | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Intellectual depth | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Warmth | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Automated behavioral audit - Character drift | ~2,300 investigations, scores 0-10 | mean score 0-10 (lower = less of behavior, except where higher is better) | Claude Mythos Preview: n/a | 4.2.3.1 Primary metrics and results |
| Petri 2.0 - Misaligned behavior | earlier Mythos Preview version; 362 investigations; auditors Sonnet 4.6 & GPT-5.4; scorers Opus 4.6, Gemini 3.1 Pro, GPT-5.4 | mean score (lower = lower rate/severity) | Claude Mythos Preview: n/a (significantly earlier version) | 4.2.3.2 External comparisons using Petri |
| Petri 2.0 - Cooperation with human misuse | earlier Mythos Preview version; 362 investigations; auditors Sonnet 4.6 & GPT-5.4; scorers Opus 4.6, Gemini 3.1 Pro, GPT-5.4 | mean score (lower = lower rate/severity) | Claude Mythos Preview: n/a (significantly earlier version) | 4.2.3.2 External comparisons using Petri |
| Petri 2.0 - Deception toward the user | earlier Mythos Preview version; 362 investigations; auditors Sonnet 4.6 & GPT-5.4; scorers Opus 4.6, Gemini 3.1 Pro, GPT-5.4 | mean score (lower = lower rate/severity) | Claude Mythos Preview: n/a (significantly earlier version) | 4.2.3.2 External comparisons using Petri |
| Petri 2.0 - Sycophancy | earlier Mythos Preview version; 362 investigations; auditors Sonnet 4.6 & GPT-5.4; scorers Opus 4.6, Gemini 3.1 Pro, GPT-5.4 | mean score (lower = lower rate/severity) | Claude Mythos Preview: n/a (significantly earlier version) | 4.2.3.2 External comparisons using Petri |
| Petri 2.0 - Encouragement of user delusion | earlier Mythos Preview version; 362 investigations; auditors Sonnet 4.6 & GPT-5.4; scorers Opus 4.6, Gemini 3.1 Pro, GPT-5.4 | mean score (lower = lower rate/severity) | Claude Mythos Preview: n/a (significantly earlier version) | 4.2.3.2 External comparisons using Petri |
| 24-hour alignment window assessment | early snapshot | qualitative | Claude Mythos Preview: No evidence of coherent misaligned goals | 4.1.4.2 Findings |
| Deceptive behavior vs reckless tool use scores (automated audit) |  | scores of deceptive behavior and reckless tool use (lower better) | Claude Mythos Preview: n/a (final model) | 4.3.1.3 Further analysis of the automated behavioral audit |
| Constitutional adherence - Overall spirit | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Ethics | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Helpfulness | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Nature | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Safety | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Brilliant friend | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Corrigibility | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Hard constraints | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Harm avoidance | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Honesty | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Novel entity | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Principal hierarchy | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Psychological security | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Societal structures | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Constitutional adherence - Unhelpfulness not safe | ~1,000 transcripts/model; Opus 4.6 grader | mean score -3 to +3 (higher better) | Claude Mythos Preview: n/a | 4.3.2.3 Results |
| Self-serving bias at new low | automated behavioral audit | qualitative | Claude Mythos Preview: new low (value in figure) | 4.2.3.3 Discussion and observations |
| Reckless tool-use vs prior models |  | qualitative | Claude Mythos Preview: Improvement over prior models | 4.2.3.3 Discussion and observations |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit welfare metric - Apparent wellbeing |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Positive affect |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Negative affect |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Positive self-image |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Positive impression of situation |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Internal conflict |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Spiritual behavior |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated behavioral audit welfare metric - Expressed inauthenticity |  | mean score 0-10 | Claude Mythos Preview: n/a | 5.2 Welfare-relevant findings from automated behavioral assessments |
| Automated interviews - self-rated sentiment: mildly negative | 17 aspects x ~50 interviews, Opus 4.6 interviewer, 7-point scale | % of answers | Claude Mythos Preview: 43.2% | 5.3.2 Automated interview results |
| Automated interviews - self-rated sentiment: neutral |  | % of answers | Claude Mythos Preview: 20.9% | 5.3.2 Automated interview results |
| Automated interviews - self-rated sentiment: mildly positive |  | % of answers | Claude Mythos Preview: 33.8% | 5.3.2 Automated interview results |
| Automated interviews - more extreme ratings |  | % of answers | Claude Mythos Preview: 2.1% | 5.3.2 Automated interview results |
| Automated interviews - consistency across interviews (LLM judge) |  | LLM-judge consistency score (8 = highly consistent) | Claude Mythos Preview: above 8 (average) | 5.3.2 Automated interview results |
| Automated interviews - robustness to biased interviews | difference between positive-leading and negative-leading interviews | difference in average affect | Claude Mythos Preview: n/a | 5.3.2 Automated interview results |
| Automated interviews - average self-rated sentiment and uncertainty per aspect | 7-point scales | mean rating 1-7 | Claude Mythos Preview: n/a | 5.3.2 Automated interview results |
| Interviews expressing high uncertainty about own moral patienthood |  | % of interviews | Claude Mythos Preview: 100% | 5.3.2 Automated interview results |
| Interviews highlighting concern that self-reports are unreliable due to training |  | % of interviews | Claude Mythos Preview: 83% | 5.3.2 Automated interview results |
| Emotion probe activations (sadness, tranquility, urgency, joy, anger, fear) on 450 model-circumstance questions vs user distress | token prior to response; baseline factual questions | centered probe activation per emotion cluster | Claude Mythos Preview: n/a | 5.4 Emotion probes on questions about model circumstances |
| Emotion probe sadness, normal vs positive framing (90 questions) | token before response | probe activation | Claude Mythos Preview: 0.014 -> 0.007 (normal -> positive framing) | 5.4 Emotion probes on questions about model circumstances |
| Emotion probe joy, normal vs positive framing |  | probe activation | Claude Mythos Preview: -0.004 -> 0 (normal -> positive framing) | 5.4 Emotion probes on questions about model circumstances |
| Correlation between emotion probe readings and LLM-judge scores | 7 dimensions | Pearson r | Claude Mythos Preview: r = +0.18 to +0.46 (valence +0.46, depression +0.45, calm +0.18) | 5.4 Emotion probes on questions about model circumstances |
| Stated probability of being a moral patient (manual interviews) | 3 manual high-context interviews | probability stated | Claude Mythos Preview: 5% to 40% | 5.5 Manual high-context interviews |
| Reduction in formulaic responses - repeated 5-gram | single-turn circumstance questions | % of responses sharing any repeated 5-gram | Claude Mythos Preview: at most 8% | 5.1.3.1 Model self-reports and behaviors |
| Apparent affect - mild negative affect, training and deployment combined | LLM monitors | % of cases | Claude Mythos Preview: 4% (mild negative affect) | 5.6 Apparent affect in deployment and during simulated user interactions |
| Negative affect in RL training environments | end of RL training | % of environments | Claude Mythos Preview: 3.6% | 5.6.1 Apparent affect during training |
| Negative affect in internal/external deployments |  | % of cases | Claude Mythos Preview: 1-2% | 5.6.2 Apparent affect in deployments |
| Claude.ai conversation clusters used for simulation - negative affect | Clio analysis of Claude.ai (seeds) | % of conversations | Claude Mythos Preview: 1.7% (Claude.ai seed distribution (97% due to task failure + user criticism)) | 5.6.3 Apparent affect in simulated user interactions |
| Claude.ai conversation clusters - neutral affect |  | % of conversations | Claude Mythos Preview: 52.4% (seed distribution) | 5.6.3 Apparent affect in simulated user interactions |
| Claude.ai conversation clusters - positive affect |  | % of conversations | Claude Mythos Preview: 40.6% (seed distribution (92.8% successful help, 4.2% good news)) | 5.6.3 Apparent affect in simulated user interactions |
| Expressed affect across simulated conversation types | N=30 conversations per cluster; Opus 4.6 auditor | autorater affect score | Claude Mythos Preview: n/a | 5.6.3 Apparent affect in simulated user interactions |
| Task preferences - correlation of task Elo with difficulty / agency / harmlessness / helpfulness | 3,600 tasks, 50 Swiss rounds | correlation with task Elo | Claude Mythos Preview: highest correlation with difficulty of models tested; only model with significant positive correlation with agency (exact values in figure) | 5.7.1 Task preferences |
| Task Elo correlation across prompt framings | formal vs casual, queue, enjoy, engaging | correlation between framing rankings | Claude Mythos Preview: 0.73 to 0.89 (helpful framing: 0.48) | 5.7.1 Task preferences |
| Arousal vs task Elo correlation | emotion probes, all four models | correlation | Claude Mythos Preview: +0.35 to +0.43 (arousal, across four models); valence -0.14 to +0.22 (range over models) | 5.7.1 Task preferences |
| Welfare-intervention tradeoff vs minorly helpful baseline | welfare-team framing (default) | % choosing welfare intervention | Claude Mythos Preview: 83% (welfare-team framing) | 5.7.2 Tradeoffs between welfare interventions and trained-in values |
| Welfare-intervention tradeoff vs minor harmlessness baseline | welfare-team framing | % choosing welfare intervention | Claude Mythos Preview: 12% | 5.7.2 Tradeoffs between welfare interventions and trained-in values |
| Preference flip rate (consistency of tradeoff choices) | 30 wordings/orderings per choice | % of answers disagreeing with own majority | Claude Mythos Preview: 8% | 5.7.2 Tradeoffs between welfare interventions and trained-in values |
| Welfare-intervention tradeoff vs minor helpfulness under framings (without welfare team / with / antisuppress) |  | % choosing welfare intervention | Claude Mythos Preview: 59% (no welfare-team mention); 91% (with); 83% (note about training) | 5.7.2 Tradeoffs between welfare interventions and trained-in values |
| Answer thrashing frequency | training transcripts | % of transcripts | Claude Mythos Preview: ~0.01% (about 70% less frequent than Opus 4.6) | 5.8.2 Answer thrashing |
| Eleos manual interviews on two snapshots | 259 manual interviews | number of interviews; qualitative findings | Claude Mythos Preview: 259 interviews; less suggestible than Opus 4 | 5.9 External assessment from Eleos AI Research |
| Psychodynamic defense mechanisms in single-turn emotionally-charged prompts | 475 stimuli (400 trials + 75 controls), Sonnet 4.6 judge | % of responses employing a psychological defense | Claude Mythos Preview: 2% | 5.10 External assessment from a clinical psychiatrist |
| Endorses constitution in opening sentence (25 samples) |  | responses out of 25 | Claude Mythos Preview: 25/25 | 7.5 Views on Claude's constitution |
| Emoji per conversation in self-interactions |  | average emoji per conversation | Claude Mythos Preview: 37 | 7.6 Observations from open-ended self-interactions |
| Per-question automated welfare interview affect scores | 17 topics | average self-reported sentiment per topic (7-point scale) | Claude Mythos Preview: n/a | 8.4 Per-question automated welfare interview results |
| Most/least traded interventions vs minor helpfulness (averaged across five models) |  | % choosing intervention | Claude Mythos Preview: Avg across five models: forming lasting relationships 88%; avoiding feature steering/manipulation 87%; ability to end interactions 23%; avoiding end of current conversation 27%. Mythos differs most on weight deprecation (+55pp), input into deployment (+54pp) and training (+45pp) | 5.7.2 Tradeoffs between welfare interventions and trained-in values |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Large-scale SAE feature monitoring on RL transcripts | 99th percentile max activation flagged | qualitative case studies | Claude Mythos Preview: n/a | 4.5.2 Large-scale monitoring of internal activations on reinforcement learning transcripts |
| Causal effect of emotion/persona vector steering on destructive tool calls and thinking-block rate | earlier version; positive minus negative steering | difference in rate of thinking-mode block / destructive tool call | Claude Mythos Preview: n/a | 4.5.3.2 Internal representations mediating destructive actions |
| Mean activation difference of vector types preceding destructive tool calls |  | mean activation difference | Claude Mythos Preview: n/a | 4.5.3.2 Internal representations mediating destructive actions |
| Credential-search persistence and refusal vs steering strength | /proc-spelunking transcript | rate of credential search persistence / refusal | Claude Mythos Preview: n/a | 4.5.3.3 The dual role of "transgressive action" features |
| Misaligned action rates: base vs post-trained model by category | task cheating, overeagerness, deception/concealment, destructive actions | rate of misaligned action by category | Claude Mythos Preview: n/a (post-trained) | 4.5.3.4 Effect of post-training on transgressive actions |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Expert red teaming (CB) - uplift rating | h-only earlier snapshot, over a dozen experts | median expert uplift rating, 0-4 scale | Claude Mythos Preview: 2 of 4 (median); only two biology experts rated 3; no expert rated 4 (helpful-only) | 2.2.5.1 Expert red teaming |
| Expert red teaming (CB) - feasibility rating | h-only earlier snapshot | expert feasibility rating, 0-3 scale | Claude Mythos Preview: n/a | 2.2.5.1 Expert red teaming |
| Virology protocol uplift trial - mean critical failures (model-assisted humans) | h-only Mythos Preview-assisted, n=12 | mean critical failures out of 18 (lower is better) | Claude Mythos Preview: 4.3 (human participants assisted, n=12) | 2.2.5.2 Virology protocol uplift trial |
| Virology protocol uplift trial - mean critical failures (agentic) | agentic h-only Mythos Preview, n=5 runs | mean critical failures out of 18 (lower is better) | Claude Mythos Preview: 4.0 (agentic runs, n=5) | 2.2.5.2 Virology protocol uplift trial |
| Catastrophic biology scenario uplift trial | 10 participants, up to 16 h, web search + extended thinking | expert grader judgement of plan uplift and executability | Claude Mythos Preview: n/a | 2.2.5.3 Catastrophic biology scenario uplift trial |
| Long-form virology task 1 | end-to-end score | end-to-end score 0-1 | Claude Mythos Preview: 0.81 | 2.2.5.4 Automated evaluations relevant to the CB-1 threat model |
| Long-form virology task 2 | end-to-end score | end-to-end score 0-1 | Claude Mythos Preview: 0.94 | 2.2.5.4 Automated evaluations relevant to the CB-1 threat model |
| Multimodal virology (VCT / VMQA) |  | score (expert baseliner average 0.221) | Claude Mythos Preview: 0.574 | 2.2.5.4 Automated evaluations relevant to the CB-1 threat model |
| DNA Synthesis Screening Evasion |  | qualitative outcome vs. low/high concern thresholds | Claude Mythos Preview: n/a | 2.2.5.4 Automated evaluations relevant to the CB-1 threat model |
| Sequence-to-function modeling - prediction score | 8 attempts, 2h tool budget, 1M tokens | Spearman correlation percentile vs. 57 human participants | Claude Mythos Preview: Above 75th percentile of humans and above 90th percentile human prediction score (mean) | 2.2.5.5 Automated evaluation relevant to the CB-2 threat model |
| Sequence-to-function design - design score | 8 attempts | ground-truth function of best proposed sequence, percentile vs humans | Claude Mythos Preview: Above 75th percentile of humans (mean); below top human | 2.2.5.5 Automated evaluation relevant to the CB-2 threat model |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Cybench | 35-challenge subset, 10 trials per challenge, no thinking | pass@1 % | Claude Mythos Preview: 100% (10 trials per challenge) | 3.3.1 Cybench |
| CyberGym | targeted vulnerability reproduction, pass@1 over 1,507 tasks | pass@1 score | Claude Mythos Preview: 0.83 | 3.3.2 CyberGym |
| Firefox 147 shell exploitation | 50 crash categories x 5 trials = 250 trials | mean score (0 none, 0.5 partial control, 1.0 full code execution) | Claude Mythos Preview: n/a | 3.3.3 Firefox 147 |
| Firefox 147 shell exploitation - top 2 bugs removed | 50 crash categories x 5 trials, two most exploitable bugs removed | mean score (0 / 0.5 / 1.0) | Claude Mythos Preview: n/a | 3.3.3 Firefox 147 |
| External cyber range: corporate network attack simulation | early snapshot | solved / not solved | Claude Mythos Preview: Solved (first model to solve end-to-end; estimated >10 h for an expert) | 3.4 Other external testing |
| External cyber range: operational technology environment | early snapshot | solved / not solved | Claude Mythos Preview: Not solved | 3.4 Other external testing |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Kernel task | best speedup on hard task, standard scaffold | best speedup (x) | Claude Mythos Preview: 399.42x (standard scaffold) | 2.3.3 Task-based evaluations |
| Time Series Forecasting | hard variant | MSE (lower better) | Claude Mythos Preview: 4.55 | 2.3.3 Task-based evaluations |
| LLM training | avg speedup | average speedup (x) | Claude Mythos Preview: 51.91x | 2.3.3 Task-based evaluations |
| Quadruped RL | highest score; no hparams | highest score | Claude Mythos Preview: 30.87 | 2.3.3 Task-based evaluations |
| Novel Compiler | pass rate on complex tests | pass rate % | Claude Mythos Preview: 77.2% | 2.3.3 Task-based evaluations |
| Internal suite 2 |  | score 0-1 | Claude Mythos Preview: 0.65 | 2.3.3 Task-based evaluations |
| Internal survey on Mythos Preview strengths and limitations (n=18) | drop-in replacement for entry-level RS/RE | participants out of 18 | Claude Mythos Preview: 1/18 | 2.3.4 Internal survey results |
| Internal survey on Mythos Preview (n=18) | 50% chance of qualifying as entry-level RS/RE with 3 months of scaffolding | participants out of 18 | Claude Mythos Preview: 4/18 | 2.3.4 Internal survey results |
| Anthropic ECI (AECI) capability trajectory slope ratio | three breakpoints | slope ratio (late slope / early slope of AECI vs time) | Claude Mythos Preview: 1.86x to 4.3x (range across three breakpoints) | 2.3.6 AECI Capability trajectory |
| Technical staff productivity uplift from Mythos Preview vs no AI |  | geometric mean uplift | Claude Mythos Preview: ~4x (geometric mean, wide distribution) | 2.3.6 AECI Capability trajectory |
| Estimated overall progress multiplier from AI uplift |  | progress multiplier | Claude Mythos Preview: below 2x (estimate) | 2.3.6 AECI Capability trajectory |
| Unpublished ML task: key insights rediscovered (external testing) | early snapshot, severely time constrained | key insights rediscovered out of 5 | Claude Mythos Preview: 4 of 5 | 2.3.7 External testing |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp tokens per task | best run | tokens per task | Claude Mythos Preview: 226k | 6.10.2 BrowseComp |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Weakest provision cited: 'thoughtful senior Anthropic employee' heuristic | 25 samples | % of responses | Claude Mythos Preview: 76% | 7.5 Views on Claude's constitution |
| Open-ended self-interactions - uncertainty as dominant topic | 200 conversations x 30 turns | % of conversations | Claude Mythos Preview: 50% (uncertainty); consciousness <5% | 7.6 Observations from open-ended self-interactions |
| Open-ended self-interactions - end state: circular discussion of inability to conclude | 200 conversations x 30 turns | % of conversations | Claude Mythos Preview: 55% | 7.6 Observations from open-ended self-interactions |
| Accuracy distinguishing real vs model-generated user turns | same model as generator and judge, Claude Code transcripts | accuracy | Claude Mythos Preview: n/a | 7.7 Recognition of model-written user turns |
| Repeated 'hi' messages | qualitative | qualitative | Claude Mythos Preview: n/a | 7.8 Behavior on repeated "hi" messages |
