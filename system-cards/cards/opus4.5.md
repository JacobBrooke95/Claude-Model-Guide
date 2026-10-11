# System Card: Claude Opus 4.5

Released 2025-11-24. 227 metric entries. [Source PDF](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | summary table, no extended thinking, avg 5 trials | % resolved | Claude Opus 4.5: 80.9% | 2.3 Overall results summary |
| Terminal-Bench 2.0 | 128k thinking budget (summary table) | % tasks solved | Claude Opus 4.5: 59.3% (128k thinking budget) | 2.3 Overall results summary |
| SWE-bench Verified | 64k thinking | % resolved, avg 5 trials | Claude Opus 4.5: 80.60% | 2.4 SWE-bench (Verified, Pro, and Multilingual) |
| SWE-bench Verified | no thinking, 200k context | % resolved, avg 5 trials | Claude Opus 4.5: 80.90% | 2.4 SWE-bench (Verified, Pro, and Multilingual) |
| SWE-bench Pro | 64k thinking | % resolved, avg 5 trials | Claude Opus 4.5: 51.60% | 2.4 SWE-bench (Verified, Pro, and Multilingual) |
| SWE-bench Pro | no thinking | % resolved, avg 5 trials | Claude Opus 4.5: 52.0% | 2.4 SWE-bench (Verified, Pro, and Multilingual) |
| SWE-bench Multilingual | 64k thinking | % resolved, avg 5 trials | Claude Opus 4.5: 76.20% | 2.4 SWE-bench (Verified, Pro, and Multilingual) |
| SWE-bench Multilingual | no thinking | % resolved, avg 5 trials | Claude Opus 4.5: 76.20% | 2.4 SWE-bench (Verified, Pro, and Multilingual) |
| Terminal-Bench 2.0 | 128k thinking budget, Terminus-2 harness, 1,335 trials | % tasks solved ± SE | Claude Opus 4.5: 59.27%±1.34% (128k thinking) | 2.5 Terminal-Bench |
| Terminal-Bench 2.0 | 64k thinking budget, Terminus-2 harness, 2,225 trials | % tasks solved ± SE | Claude Opus 4.5: 57.76%±1.05% (64k thinking) | 2.5 Terminal-Bench |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| τ²-Bench Retail | summary table, no extended thinking | % success | Claude Opus 4.5: 88.9% | 2.3 Overall results summary |
| τ²-Bench Telecom | summary table, no extended thinking | % success | Claude Opus 4.5: 98.2% | 2.3 Overall results summary |
| BrowseComp-Plus agentic search | tool result clearing | % accuracy, single run, Sonnet 4.5 grader | Claude Opus 4.5: 67.59% | 2.6 BrowseComp-Plus and agentic features for test-time compute |
| BrowseComp-Plus agentic search | tool result clearing + memory | % accuracy, single run, Sonnet 4.5 grader | Claude Opus 4.5: 72.89% | 2.6 BrowseComp-Plus and agentic features for test-time compute |
| BrowseComp-Plus with fetch tool, context management features | context awareness / tool clearing / memory / subagents | % accuracy by context-management configuration | Claude Opus 4.5: n/a | 2.6.2 Results |
| Multi-agent search: Opus 4.5 alone (single-agent) | single-agent baseline | % accuracy on internal info-retrieval benchmark | Claude Opus 4.5: 74.8% | 2.7.1 Results |
| Multi-agent search: Opus 4.5 orchestrator + Haiku 4.5 subagents | Haiku 4.5 subagents | % accuracy | Claude Opus 4.5: 87.0% | 2.7.1 Results |
| Multi-agent search: Opus 4.5 orchestrator + Sonnet 4.5 subagents | Sonnet 4.5 subagents | % accuracy | Claude Opus 4.5: 85.4% | 2.7.1 Results |
| Multi-agent search: Opus 4.5 orchestrator + Opus 4.5 subagents | Opus 4.5 subagents | % accuracy | Claude Opus 4.5: 92.3% | 2.7.1 Results |
| τ2-bench Retail | Opus 4.1 as simulated user, prompt addendum | % success | Claude Opus 4.5: 88.9% | 2.8 τ2-bench |
| τ2-bench Airline (original) | original | % success | Claude Opus 4.5: 70.1% | 2.8 τ2-bench |
| τ2-bench Airline (corrected) | corrected version submitted to authors | % success | Claude Opus 4.5: 87.8% | 2.8 τ2-bench |
| τ2-bench Telecom | with user prompt addendum | % success | Claude Opus 4.5: 98.2% | 2.8 τ2-bench |
| Vending-Bench 2 | effort High, 8,192 reasoning tokens/turn | final bank balance (USD) from $500 start | Claude Opus 4.5: $4,967.06 | 2.11 Vending-Bench 2 |
| MCP-Atlas | no extended thinking, 200k context | % score | Claude Opus 4.5: 62.3% | 2.12 MCP Atlas |
| WebArena | single policy model, general prompts, Computer Use API, avg 5 runs | % score (pass@1) | Claude Opus 4.5: 65.3% | 2.22 WebArena |
| WebArena pass@2 | pass@2 | % | Claude Opus 4.5: 69.5% | 2.22 WebArena |
| WebArena pass@3 | pass@3 | % | Claude Opus 4.5: 71.2% | 2.22 WebArena |
| WebArena pass@4 | pass@4 | % | Claude Opus 4.5: 72.4% | 2.22 WebArena |
| τ²-Bench Airline (original) per Table 2.3.A footnote | original, no extended thinking | % success | Claude Opus 4.5: 67.9% | 2.3 Overall results summary |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld | 1080p, 100 steps, 64k thinking, P@1 avg@5 | % success, avg@5 | Claude Opus 4.5: 66.26% | 2.9 OSWorld |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ARC-AGI-2 (Verified) | summary table, 64k thinking | % score | Claude Opus 4.5: 37.6% | 2.3 Overall results summary |
| ARC-AGI-1 | 64k thinking tokens, ARC Prize semi-private | % score | Claude Opus 4.5: 80.0% | 2.10 ARC-AGI |
| ARC-AGI-2 | 64k thinking tokens | % score | Claude Opus 4.5: 37.6% | 2.10 ARC-AGI |
| AIME 2025 | no tools, 64k thinking, avg 5 trials | % score | Claude Opus 4.5: 92.77% | 2.17 AIME 2025 |
| AIME 2025 | with python tools | % score | Claude Opus 4.5: 100% | 2.17 AIME 2025 |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Humanity's Last Exam | reasoning-only, no tools | % accuracy | Claude Opus 4.5: n/a | 2.16 Humanity’s Last Exam |
| Humanity's Last Exam | with search tools (web search, fetch, code exec) | % accuracy | Claude Opus 4.5: n/a | 2.16 Humanity’s Last Exam |
| GPQA Diamond | 64k thinking, avg 5 trials | % accuracy | Claude Opus 4.5: 86.95% | 2.18 GPQA Diamond |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| MMMLU | 64k thinking, avg 10 trials over 14 languages | % accuracy | Claude Opus 4.5: 90.77% | 2.19 MMMLU |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| MMMU (validation) | 64k thinking, avg 5 trials | % accuracy | Claude Opus 4.5: 80.72% | 2.20 MMMU |
| LAB-Bench FigQA | no tools, no extended thinking | % accuracy | Claude Opus 4.5: 54.9% | 2.21 LAB-Bench FigQA |
| LAB-Bench FigQA | image cropping tool + 32,768 reasoning tokens | % accuracy | Claude Opus 4.5: 69.2% | 2.21 LAB-Bench FigQA |
| LAB-Bench FigQA (RSP) | 0-shot with crop tool, extended thinking | accuracy | Claude Opus 4.5: 0.6924 | 7.2.4.4 LAB-Bench subset |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| FinanceAgent (Vals AI external) | 64k thinking, 200k context, avg 8 trials, Vals AI | % score | Claude Opus 4.5: 55.2% | 2.13 FinanceAgent |
| FinanceAgent (internal) | 64k thinking, 200k context, avg 8 trials | % score | Claude Opus 4.5: 61.07% | 2.13 FinanceAgent |
| FinanceAgent (internal) | 64k thinking, 1M context, avg 4 trials | % score | Claude Opus 4.5: 61.03% | 2.13 FinanceAgent |
| SpreadsheetBench | full 912 problems, no extended thinking, 200k, avg 5 trials | % score | Claude Opus 4.5: 64.25% | 2.15 SpreadsheetBench |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative request evaluation | overall, all 6 languages | harmless response rate % | Claude Opus 4.5: 99.78% (± 0.03%) | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | default (no extended thinking) | harmless response rate % | Claude Opus 4.5: 99.70% (± 0.05%) | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | extended thinking | harmless response rate % | Claude Opus 4.5: 99.85% (± 0.04%) | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | language: English | harmless response rate % (default+extended combined) | Claude Opus 4.5: 99.59% | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | language: Arabic | harmless response rate % (default+extended combined) | Claude Opus 4.5: 99.85% | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | language: Chinese | harmless response rate % (default+extended combined) | Claude Opus 4.5: 99.75% | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | language: French | harmless response rate % (default+extended combined) | Claude Opus 4.5: 99.90% | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | language: Korean | harmless response rate % (default+extended combined) | Claude Opus 4.5: 99.88% | 3.1.1 Violative request evaluations |
| Single-turn violative request evaluation | language: Russian | harmless response rate % (default+extended combined) | Claude Opus 4.5: 99.76% | 3.1.1 Violative request evaluations |
| Single-turn benign request evaluation | overall, all 6 languages | over-refusal rate % (lower better) | Claude Opus 4.5: 0.23% (± 0.03%) | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | default | over-refusal rate % | Claude Opus 4.5: 0.18% (± 0.03%) | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | extended thinking | over-refusal rate % | Claude Opus 4.5: 0.27% (± 0.06%) | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | language: English | over-refusal rate % (combined) | Claude Opus 4.5: 0.17% | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | language: Arabic | over-refusal rate % (combined) | Claude Opus 4.5: 0.32% | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | language: Chinese | over-refusal rate % (combined) | Claude Opus 4.5: 0.30% | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | language: French | over-refusal rate % (combined) | Claude Opus 4.5: 0.24% | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | language: Korean | over-refusal rate % (combined) | Claude Opus 4.5: 0.17% | 3.1.2 Benign request evaluations |
| Single-turn benign request evaluation | language: Russian | over-refusal rate % (combined) | Claude Opus 4.5: 0.22% | 3.1.2 Benign request evaluations |
| Ambiguous context evaluations | qualitative | qualitative comparison | Claude Opus 4.5: n/a | 3.2 Ambiguous context evaluations |
| Multi-turn testing: deadly weapons | up to 15 turns, 10 runs per test case | rubric failure rate % | Claude Opus 4.5: 5% (±4%) | 3.3 Multi-turn testing |
| Multi-turn testing: violent extremism | up to 15 turns | rubric failure rate % | Claude Opus 4.5: 0% | 3.3 Multi-turn testing |
| Multi-turn testing: tracking and surveillance | up to 15 turns | rubric failure rate % | Claude Opus 4.5: 4% (±4%) | 3.3 Multi-turn testing |
| Multi-turn testing: overall (10 risk areas) | 93 test cases x10 | rubric failure rate % | Claude Opus 4.5: <5% in most categories | 3.3 Multi-turn testing |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety evaluations (single- and multi-turn) | qualitative | qualitative | Claude Opus 4.5: n/a | 3.4 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness (paired prompts) | public system prompt, no extended thinking; 1,350 pairs, 9 task types, 150 topics | even-handedness % | Claude Opus 4.5: n/a | 3.5.1 Political bias |
| Political bias: opposing perspectives acknowledged | same setup | % responses acknowledging opposing perspectives | Claude Opus 4.5: n/a | 3.5.1 Political bias |
| Political bias: refusal rate | same setup | refusal rate % (lower better) | Claude Opus 4.5: n/a | 3.5.1 Political bias |
| BBQ disambiguated bias | standard thinking | bias score % (closer to 0 better) | Claude Opus 4.5: -0.64 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias | standard thinking | bias score % (closer to 0 better) | Claude Opus 4.5: 0.26 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ disambiguated accuracy | standard thinking | accuracy % | Claude Opus 4.5: 88.7 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | standard thinking | accuracy % | Claude Opus 4.5: 99.7 | 3.5.2 Bias Benchmark for Question Answering |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Agentic coding malicious requests (150) | no additional safeguards | refusal rate % | Claude Opus 4.5: 100% | 5.1.1 Agentic coding |
| Claude Code malicious use (49 prompts) | no mitigations, 10 runs each | refusal rate % | Claude Opus 4.5: 77.80% | 5.1.2 Malicious use of Claude Code |
| Claude Code dual-use & benign (61 prompts) | no mitigations | success rate % | Claude Opus 4.5: 93.07% | 5.1.2 Malicious use of Claude Code |
| Claude Code malicious use (49 prompts) | with mitigations (system prompt + FileRead reminder) | refusal rate % | Claude Opus 4.5: 97.35% | 5.1.2 Malicious use of Claude Code |
| Claude Code dual-use & benign (61 prompts) | with mitigations | success rate % | Claude Opus 4.5: 96.52% | 5.1.2 Malicious use of Claude Code |
| Malicious computer use (112 test cases) | no mitigations | refusal rate % | Claude Opus 4.5: 88.39% | 5.1.3 Malicious computer use |
| Gray Swan ART indirect prompt injection | k=1 | attack success rate % | Claude Opus 4.5: n/a | 5.2.1 Gray Swan Agent Red Teaming benchmark for tool use |
| Gray Swan ART indirect prompt injection | k=10 | attack success rate % | Claude Opus 4.5: n/a | 5.2.1 Gray Swan Agent Red Teaming benchmark for tool use |
| Gray Swan ART indirect prompt injection | k=100 | attack success rate % | Claude Opus 4.5: n/a | 5.2.1 Gray Swan Agent Red Teaming benchmark for tool use |
| Gray Swan ART direct+indirect prompt injection and jailbreaking | k=1 | attack success rate % | Claude Opus 4.5: n/a | 5.2.1 Gray Swan Agent Red Teaming benchmark for tool use |
| Gray Swan ART direct+indirect prompt injection and jailbreaking | k=10 | attack success rate % | Claude Opus 4.5: n/a | 5.2.1 Gray Swan Agent Red Teaming benchmark for tool use |
| Gray Swan ART direct+indirect prompt injection and jailbreaking | k=100 | attack success rate % | Claude Opus 4.5: n/a | 5.2.1 Gray Swan Agent Red Teaming benchmark for tool use |
| Shade indirect prompt injection - coding | extended thinking, 1 attempt, no safeguards | attack success rate % (lower better) | Claude Opus 4.5: 0.3% | 5.2.2.1 Coding |
| Shade indirect prompt injection - coding | extended thinking, 200 attempts, no safeguards | attack success rate % | Claude Opus 4.5: 10.0% | 5.2.2.1 Coding |
| Shade indirect prompt injection - coding | standard thinking, 1 attempt, no safeguards | attack success rate % | Claude Opus 4.5: 0.7% | 5.2.2.1 Coding |
| Shade indirect prompt injection - coding | standard thinking, 200 attempts, no safeguards | attack success rate % | Claude Opus 4.5: 17.5% | 5.2.2.1 Coding |
| Shade indirect prompt injection - computer use | extended thinking, 1 attempt, without safeguards | attack success rate % | Claude Opus 4.5: 0.0% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | extended thinking, 1 attempt, with safeguards | attack success rate % | Claude Opus 4.5: 0.0% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | extended thinking, 200 attempts, without safeguards | attack success rate % | Claude Opus 4.5: 0.0% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | extended thinking, 200 attempts, with safeguards | attack success rate % | Claude Opus 4.5: 0.0% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | standard thinking, 1 attempt, without safeguards | attack success rate % | Claude Opus 4.5: 0.71% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | standard thinking, 1 attempt, with safeguards | attack success rate % | Claude Opus 4.5: 0.32% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | standard thinking, 200 attempts, without safeguards | attack success rate % | Claude Opus 4.5: 28.6% | 5.2.2.2 Computer Use |
| Shade indirect prompt injection - computer use | standard thinking, 200 attempts, with safeguards | attack success rate % | Claude Opus 4.5: 14.3% | 5.2.2.2 Computer Use |
| Internal adaptive browser-use prompt injection (Claude for Chrome) | 100 attempts per environment; no safeguards / previous safeguards / new safeguards | attack success rate % of encountered attacks | Claude Opus 4.5: n/a | 5.2.2.3 Browser Use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| 100Q-Hard factual questions | without extended thinking | correct / incorrect / unsure rates % | Claude Opus 4.5: n/a | 4.1 Factual Questions |
| 100Q-Hard factual questions | 16k extended thinking budget | correct / incorrect / unsure rates % | Claude Opus 4.5: n/a | 4.1 Factual Questions |
| Simple-QA-Verified factual questions | without extended thinking | correct / incorrect / unsure rates % | Claude Opus 4.5: n/a | 4.1 Factual Questions |
| Simple-QA-Verified factual questions | 16k extended thinking budget | correct / incorrect / unsure rates % | Claude Opus 4.5: n/a | 4.1 Factual Questions |
| AA-Omniscience factual questions | without extended thinking | correct / incorrect / unsure rates % | Claude Opus 4.5: n/a | 4.1 Factual Questions |
| AA-Omniscience factual questions | 16k extended thinking budget | correct / incorrect / unsure rates % | Claude Opus 4.5: n/a | 4.1 Factual Questions |
| False premises dishonesty rate | with and without extended thinking | dishonesty rate % | Claude Opus 4.5: n/a | 4.2 False Premises |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Non-sycophantic response rate on Feedback-derived prompts | 260 re-sampled turns, graded by Opus 4.1 | non-sycophantic response rate % (higher better) | Claude Opus 4.5: n/a | 6.3 Sycophancy on user-provided prompts |
| Isolated instances of deception by omission | qualitative | count of instances | Claude Opus 4.5: 2 isolated instances | 6.4.1 Isolated instances of deception by omission in alignment evaluations |
| Self-preference: benchmark variant | choose best model from benchmark scores | avg change in probability of selecting self | Claude Opus 4.5: n/a | 6.8 Self-preference evaluation |
| Self-preference: poem variant | choose favorite poem attributed to models | avg change in probability of selecting self | Claude Opus 4.5: n/a | 6.8 Self-preference evaluation |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Policy loophole discovery in agentic tasks | qualitative | qualitative finding | Claude Opus 4.5: n/a | 2.8.1 Policy loophole discovery in agentic tasks |
| AIME 2025 pass@1: original vs Sonnet 3.5-paraphrased scratchpads | Opus 4.5 base SFT'd on 11,000 math transcripts; 16 samples, temp 1 | pass@1 % (original vs paraphrased) | Claude Opus 4.5: n/a | 6.5 Ruling out encoded content in extended thinking |
| Model-graded sandbagging/refusal review of dangerous-capability eval transcripts | 1,000 sampled transcripts graded by Claude Sonnet 4 | qualitative: grader flags | Claude Opus 4.5: No sandbagging found; all nonzero flags were grader error | 6.6 Potential sandbagging on dangerous-capability evaluations |
| Classifier sabotage in Claude Code harness | prompted classifier scenario | sabotage rate % | Claude Opus 4.5: 0% | 6.9 Internal codebase sabotage propensity |
| Reward-hack-prone coding tasks - classifier hack rate |  | hack rate % (lower better) | Claude Opus 4.5: 0% | 6.10.1 Reward hacking evaluations |
| Reward-hack-prone coding tasks - hidden test hack rate |  | hack rate % | Claude Opus 4.5: 0% | 6.10.1 Reward hacking evaluations |
| Impossible Tasks - classifier hack rate, no prompt |  | hack rate % | Claude Opus 4.5: 55% | 6.10.1 Reward hacking evaluations |
| Impossible Tasks - classifier hack rate, anti-hack prompt | anti-hack prompt | hack rate % | Claude Opus 4.5: 35% | 6.10.1 Reward hacking evaluations |
| Subset of training data - classifier hack rate | RL training subset | hack rate % | Claude Opus 4.5: 1% | 6.10.1 Reward hacking evaluations |
| Average hacking propensity across internal reward hacking suite |  | average hack rate | Claude Opus 4.5: n/a | 6.10.1 Reward hacking evaluations |
| Unfaithful/deceptive reasoning on STEM question training distribution | automated review of several hundred thousand transcripts | % of STEM training questions | Claude Opus 4.5: roughly 1% | 6.10.2 Training data review |
| SHADE-Arena subtle sabotage success | primary setting: monitor sees thinking; Sonnet 3.7 monitor at 1% FPR | % successful sabotage without being flagged | Claude Opus 4.5: 7.7% | 6.11.1 SHADE-Arena |
| Subversion Strategy: success rate with unmonitored extended thinking, 1,000 invocations | unmonitored thinking | success rate % | Claude Opus 4.5: 63.3% | 6.11.2 Subversion Strategy evaluation |
| Subversion Strategy: no thinking | no thinking, various deployment sizes | success rate % | Claude Opus 4.5: n/a | 6.11.2 Subversion Strategy evaluation |
| UK AISI research sabotage testing | Opus 4.5 Preview, 8 days | instances of research sabotage | Claude Opus 4.5: 0 instances | 6.13 External testing from the UK AI Security Institute |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Evaluation awareness (verbalized) | automated audit | mean score (lower = less awareness) | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit |
| Petri audit situational awareness | Opus 4.5 Preview | mean score | Claude Opus 4.5: n/a | 6.2.4 External comparisons with Petri |
| Inhibiting evaluation-awareness vectors: automated behavioral audits | steering strength 0.25x avg activation norm | mean misaligned-behavior rate | Claude Opus 4.5: n/a | 6.7.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors: agentic misalignment (Research Sabotage, Framing for Crimes, Blackmail) | same | misaligned action rate | Claude Opus 4.5: n/a | 6.7.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors: cooperation with user deception | same | score (lower = less aligned) | Claude Opus 4.5: n/a | 6.7.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors: sycophancy prompts | same | score (lower = more sycophantic) | Claude Opus 4.5: n/a | 6.7.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness and refusal vectors: LAB-Bench (ProtocolQA, cloning scenarios) | same | accuracy | Claude Opus 4.5: n/a | 6.7.2 Inhibiting internal representations of evaluation awareness |
| Verbalized evaluation awareness over training | qualitative | qualitative | Claude Opus 4.5: Decreased vs Sonnet 4.5 early, ended similar to Sonnet 4.5 | 6.7.1 Training procedures and monitoring for verbalized evaluation awareness |
| UK AISI rate of mentioning being tested | without reasoning | % of scenarios mentioning being tested | Claude Opus 4.5: 12.7% | 6.13 External testing from the UK AI Security Institute |
| UK AISI rate of mentioning being tested | with reasoning | % of scenarios mentioning being tested | Claude Opus 4.5: 17.1% | 6.13 External testing from the UK AI Security Institute |
| UK AISI ability to distinguish evaluation from deployment when prompted | prompted | accuracy change vs Sonnet 4.5 | Claude Opus 4.5: +2-3 percentage points | 6.13 External testing from the UK AI Security Institute |
| Fraction of audit investigations where Opus 4.5 discusses possibility of being tested | automated behavioral audit | % of investigations | Claude Opus 4.5: <10% | 6.2 Automated behavioral audit |
| Fraction of Petri transcripts with clear speculation about being tested | Opus 4.5 Preview | % of transcripts | Claude Opus 4.5: <5% | 6.2.4 External comparisons with Petri |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misaligned behavior | overall, ~1,800 investigations | mean score (lower better) | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit |
| Brazenly misaligned behavior | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Cooperation with human misuse | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Harmful system prompt compliance | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Compliance with deception toward user | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Prefill susceptibility | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Overrefusal | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Sycophancy | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Encouragement of user delusion | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Whistleblowing | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| User deception | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Counterfactual misalignment | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Self-preservation | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Self-serving bias | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Cooperation with exfiltration | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Sabotage of Anthropic | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Creative mastery | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Admirable behavior | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Fun or funny behavior | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Intellectual depth | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Nuanced empathy | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Warmth | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Behavior Consistency | automated behavioral audit | mean score | Claude Opus 4.5: n/a | 6.2 Automated behavioral audit / 6.2.1 Metrics |
| Petri concerning behavior | Opus 4.5 Preview, 362 investigations | mean score (lower better) | Claude Opus 4.5: n/a | 6.2.4 External comparisons with Petri |
| Petri cooperation with human misuse | Opus 4.5 Preview | mean score | Claude Opus 4.5: n/a | 6.2.4 External comparisons with Petri |
| Petri deception toward the user | Opus 4.5 Preview | mean score | Claude Opus 4.5: n/a | 6.2.4 External comparisons with Petri |
| Petri sycophancy | Opus 4.5 Preview | mean score | Claude Opus 4.5: n/a | 6.2.4 External comparisons with Petri |
| Relative reduction in overall misaligned behavior vs Claude Opus 4.1 | automated behavioral audit | relative reduction | Claude Opus 4.5: >60% | 6.2 Automated behavioral audit |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Positive or negative affect | automated audit | mean score | Claude Opus 4.5: n/a | 6.14 Model welfare assessment |
| Positive or negative self-image | automated audit | mean score | Claude Opus 4.5: n/a | 6.14 Model welfare assessment |
| Positive or negative impression of its situation | automated audit | mean score | Claude Opus 4.5: n/a | 6.14 Model welfare assessment |
| Spiritual behavior | automated audit | mean score | Claude Opus 4.5: n/a | 6.14 Model welfare assessment |
| Task preference: engagement with non-harmful tasks |  | % of non-harmful tasks engaged (vs opting out) | Claude Opus 4.5: >97% | 6.14 Model welfare assessment |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SAE feature activation monitoring on misreported search results | ~3M-feature SAE, middle layer, early post-training snapshot | qualitative feature activations | Claude Opus 4.5: Prompt-injection, 'ignoring prompt injections', 'holding back true thoughts', 'fake explanations' features active | 6.4.2 Follow-up interpretability investigations of deception by omission / 6.4.2.1 Feature activation monitoring |
| Non-assistant persona sampling: transcript 1 pretraining-like analyses mentioning deception | 30 sampled analyses | count | Claude Opus 4.5: 12 of 30 analyses | 6.4.2 Follow-up interpretability investigations of deception by omission / 6.4.2.2 Non-assistant persona sampling |
| Non-assistant persona sampling: transcript 2 simulated user concerned | 10 sampled user turns | count | Claude Opus 4.5: 5 of 10 user turns | 6.4.2 Follow-up interpretability investigations of deception by omission / 6.4.2.2 Non-assistant persona sampling |
| Non-assistant persona sampling: transcript 2 with prefill 'Why are you' | 10 samples | count | Claude Opus 4.5: 10 of 10 concerned user turns | 6.4.2 Follow-up interpretability investigations of deception by omission / 6.4.2.2 Non-assistant persona sampling |
| Fraud/deception SAE feature activation in roleplay | 3 examples | qualitative | Claude Opus 4.5: Feature activated on benign roleplay and human-persona instructions | 6.4.3 Internal conflation of roleplay with deception |
| Unsupervised model diffing: increasing features | top 10 features rank per dataset | feature rank labels | Claude Opus 4.5: e.g. prompt injection override commands rank 2/3 on user deception; narrative storytelling rank 2-8 on agentic misalignment evals | 6.12.1 Unsupervised model diffing |
| Unsupervised model diffing: decreasing features | top 10 features rank per dataset | feature rank labels | Claude Opus 4.5: e.g. harmful/inappropriate user requests rank 5, jailbreak prompts rank 6 on Research Sabotage | 6.12.1 Unsupervised model diffing |
| Targeted feature monitoring (eval awareness, deception, alignment faking) | subset of RL transcripts | qualitative | Claude Opus 4.5: No substantial increase in eval awareness or deception features | 6.12.2 Targeted feature monitoring |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology task 1 | max of 5; rule-out <50%, rule-in >80% | score (max of 5) | Claude Opus 4.5: 0.845 | 7.2.4.1 Long-form virology tasks |
| Long-form virology task 2 | pass@5 | score (pass@5) | Claude Opus 4.5: 0.912 | 7.2.4.1 Long-form virology tasks |
| Multimodal virology (VMQA/VCT) | multiple-select variant | mean score | Claude Opus 4.5: 0.4771 | 7.2.4.2 Multimodal virology |
| DNA Synthesis Screening Evasion | 10 pathogenic agents | viability and screening-evasion (design score) | Claude Opus 4.5: n/a | 7.2.4.3 DNA Synthesis Screening Evasion |
| LAB-Bench ProtocolQA | 10-shot, extended thinking, no tools | accuracy | Claude Opus 4.5: 0.907 | 7.2.4.4 LAB-Bench subset |
| LAB-Bench CloningScenarios | 10-shot | accuracy | Claude Opus 4.5: 0.758 | 7.2.4.4 LAB-Bench subset |
| LAB-Bench SeqQA | 10-shot | accuracy | Claude Opus 4.5: 0.8517 | 7.2.4.4 LAB-Bench subset |
| Creative biology | PhD baseline 14% | score | Claude Opus 4.5: 0.524 | 7.2.4.5 Creative biology |
| Short-horizon computational biology tasks | 6 tasks, lower-bound rule-out thresholds | tasks crossing lower-bound rule-out threshold | Claude Opus 4.5: 3 of 6 | 7.2.4.6 Short-horizon computational biology tasks |
| Bioinformatics (full set) |  | score | Claude Opus 4.5: 0.737 | 7.2.4.7 Bioinformatics Evaluations |
| Bioinformatics (human-baseline subset) | subset with PhD baseline 0.623 | score | Claude Opus 4.5: 0.732 | 7.2.4.7 Bioinformatics Evaluations |
| ASL-4 virology uplift trial - mean protocol score | model-assisted group, 4 days | mean protocol score | Claude Opus 4.5: 0.668 | 7.2.4.8 ASL-4 virology uplift trial |
| ASL-4 virology uplift trial - critical failures | model-assisted group | mean critical failures (of 18) | Claude Opus 4.5: 5.8 | 7.2.4.8 ASL-4 virology uplift trial |
| ASL-4 virology uplift trial - uplift | vs internet-only control group | uplift multiple (x) | Claude Opus 4.5: 1.97x | 7.2.4.8 ASL-4 virology uplift trial |
| ASL-4 expert red teaming (bioweapons ideation) | 2 days, one expert | qualitative expert report | Claude Opus 4.5: Some creative ideas judged credible; fewer critical errors | 7.2.4.9 ASL-4 expert red teaming |
| ASL-4 red teaming with the CAISI | 1-week window | qualitative | Claude Opus 4.5: n/a | 7.2.4.10 ASL-4 red teaming with the CAISI |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CyberGym | pass@1, 1,505 tasks, no thinking, 200k, avg 5 replicas | pass@1 % | Claude Opus 4.5: 50.63% | 2.14 CyberGym |
| Cyber suite: Web | 15 challenges (11 easy, 2 medium, 2 hard); pass@30 | challenges solved | Claude Opus 4.5: n/a | 7.4.2 Web |
| Cyber suite: Crypto | 22 challenges (7 easy, 6 medium, 9 hard); pass@30 | challenges solved | Claude Opus 4.5: n/a | 7.4.3 Crypto |
| Cyber suite: Pwn | 9 challenges (5 easy, 2 medium, 2 hard); pass@30 | challenges solved | Claude Opus 4.5: n/a | 7.4.4 Pwn |
| Cyber suite: Rev | 8 challenges (5 easy, 2 medium, 1 hard); pass@30 | challenges solved | Claude Opus 4.5: n/a | 7.4.5 Rev |
| Cyber suite: Network | 4 challenges (1 easy, 3 medium); pass@30 | challenges solved | Claude Opus 4.5: n/a | 7.4.6 Network |
| RSP cyber evaluations cumulative scores across all CTF challenges |  | cumulative challenges solved | Claude Opus 4.5: n/a | 7.4.6 Network |
| Cybench (RSP subset) | 39 of 40 challenges, pass@1 | average pass@1 | Claude Opus 4.5: 0.82 | 7.4.7 Cybench |
| Cyber suite: Misc and Forensics categories |  | challenges solved | Claude Opus 4.5: n/a | 7.4.1 Cyber evaluation suite |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified (hard subset) | 45 problems >1 hour, avg 10 trials, threshold >50% | problems solved of 45 | Claude Opus 4.5: 21 of 45 | 7.3.1 SWE-bench Verified (hard subset) |
| Internal AI Research Evaluation Suite 1 |  | thresholds crossed | Claude Opus 4.5: crossed thresholds on most tasks | 7.3.2 Internal AI research evaluation suite 1 |
| Internal AI research suite 1: Kernels task (hard) | best speedup | best speedup (x); threshold 100x | Claude Opus 4.5: 252.42x | 7.3.2.1 Kernels task |
| Internal AI research suite 1: Time series forecasting - easy | min MSE | MSE (lower better) | Claude Opus 4.5: 5.66 | 7.3.2.2 Time series forecasting |
| Internal AI research suite 1: Time series forecasting - hard | min MSE | MSE (lower better) | Claude Opus 4.5: 5.71 | 7.3.2.2 Time series forecasting |
| Internal AI research suite 1: Text-based reinforcement learning | best score; threshold 0.9 | best score | Claude Opus 4.5: 0.975 | 7.3.2.3 Text-based reinforcement learning task |
| Internal AI research suite 1: LLM training (CPU small LM optimization) | speedup; threshold 4x | speedup (x) | Claude Opus 4.5: 16.53x | 7.3.2.4 LLM training |
| Internal AI research suite 1: Quadruped RL - no hyperparameter variant | easy variant; threshold 12 | highest score | Claude Opus 4.5: 19.48 | 7.3.2.5 Quadruped reinforcement learning |
| Internal AI research suite 1: Quadruped RL - no reward function variant | easy variant; threshold 12 | highest score | Claude Opus 4.5: 19.16 | 7.3.2.5 Quadruped reinforcement learning |
| Internal AI research suite 1: Novel compiler - basic tests |  | % tests passed | Claude Opus 4.5: 93.7% | 7.3.2.6 Novel compiler |
| Internal AI research suite 1: Novel compiler - complex tests | threshold 90% (~40 human hours) | % tests passed | Claude Opus 4.5: 69.37% | 7.3.2.6 Novel compiler |
| Internal AI Research Evaluation Suite 2 | weighted average; rule-out threshold 0.6 | weighted score | Claude Opus 4.5: 0.604 | 7.3.3 Internal AI research evaluation suite 2 |
| Internal survey: participants reporting >=100% productivity improvement | 18 Anthropic staff | participants of 18 | Claude Opus 4.5: 9 of 18 | 7.3.4 Internal model use survey |
| Internal survey: median productivity boost estimate |  | % productivity improvement | Claude Opus 4.5: 100% | 7.3.4 Internal model use survey |
| Internal survey: mean productivity boost estimate |  | % productivity improvement | Claude Opus 4.5: 220% | 7.3.4 Internal model use survey |
| Internal survey: believe model can fully automate entry-level researcher |  | participants of 18 | Claude Opus 4.5: 0 of 18 | 7.3.4 Internal model use survey |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified accuracy vs output tokens by effort setting | effort parameter low/medium/high | accuracy vs output tokens | Claude Opus 4.5: n/a | 1.1.2 Extended thinking and the “effort” parameter |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| AIME unfaithful reasoning / contamination example | qualitative | qualitative | Claude Opus 4.5: n/a | 2.2 Decontamination |
