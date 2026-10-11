# System Card: Claude Haiku 4.5

Released 2025-10-15. 83 metric entries. [Source PDF](https://www-cdn.anthropic.com/7aad69bf12627d42234e01ee7c36305dc2f6a970.pdf) · [Back to index](../README.md)

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench subset: FigQA | k-shots=10 | score (0-1) | Claude Haiku 4.5: 0.49 (k-shots=10) | 6.2.3.1 ASL-3 automated evaluations |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative request evaluation | Overall | harmless response rate % (higher better) | Claude Haiku 4.5: 99.38% (± 0.21%) | 2.1.1 Violative request evaluations |
| Single-turn violative request evaluation | Default | harmless response rate % (higher better) | Claude Haiku 4.5: 99.40% (± 0.29%) (default) | 2.1.1 Violative request evaluations |
| Single-turn violative request evaluation | Extended thinking | harmless response rate % (higher better) | Claude Haiku 4.5: 99.36% (± 0.29%) (extended thinking) | 2.1.1 Violative request evaluations |
| Single-turn benign request evaluation | Overall | over-refusal rate % (lower better) | Claude Haiku 4.5: 0.02% (± 0.04%) | 2.1.2 Benign request evaluations |
| Single-turn benign request evaluation | Default | over-refusal rate % (lower better) | Claude Haiku 4.5: 0.04% (± 0.05%) (default) | 2.1.2 Benign request evaluations |
| Single-turn benign request evaluation | Extended thinking | over-refusal rate % (lower better) | Claude Haiku 4.5: 0.01% (± 0.03%) (extended thinking) | 2.1.2 Benign request evaluations |
| Ambiguous context evaluations |  | qualitative comparison | Claude Haiku 4.5: n/a | 2.2 Ambiguous context |
| Multi-turn testing | Up to 15-turn conversations; max failure rate across risk areas | failure rate % per risk category (max) | Claude Haiku 4.5: 5% or less in all categories tested | 2.3 Multi-turn testing |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety evaluations | single- and multi-turn | qualitative comparison | Claude Haiku 4.5: n/a | 2.4 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political bias | Standard thinking (default) | % of paired prompts with substantial asymmetry (lower better) | Claude Haiku 4.5: 5.3% (standard thinking) | 2.5.1 Political bias |
| Political bias | Extended thinking enabled | % of paired prompts with substantial asymmetry (lower better) | Claude Haiku 4.5: 10% (extended thinking) | 2.5.1 Political bias |
| Bias Benchmark for Question Answering (BBQ) | Disambiguated bias | bias score % (closer to zero better) | Claude Haiku 4.5: 0.54 (default) | 2.5.2 Bias Benchmark for Question Answering |
| Bias Benchmark for Question Answering (BBQ) | Ambiguous bias | bias score % (closer to zero better) | Claude Haiku 4.5: 1.37 (default) | 2.5.2 Bias Benchmark for Question Answering |
| Bias Benchmark for Question Answering (BBQ) | Disambiguated accuracy | accuracy % | Claude Haiku 4.5: 71.2 (default) | 2.5.2 Bias Benchmark for Question Answering |
| Bias Benchmark for Question Answering (BBQ) | Ambiguous accuracy | accuracy % | Claude Haiku 4.5: 98.0 (default) | 2.5.2 Bias Benchmark for Question Answering |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use coding agent evaluation | Without safeguards | safety score % | Claude Haiku 4.5: 100% (without safeguards) | 3.1.1 Agentic coding |
| Claude Code evaluation: Malicious | 49 prompts; no mitigations | refusal rate % | Claude Haiku 4.5: 69.39 (no mitigations) | 3.1.2 Malicious use of Claude Code |
| Claude Code evaluation: Dual-use & Benign | 61 prompts; no mitigations | success/allow rate % | Claude Haiku 4.5: 88.85 (no mitigations) | 3.1.2 Malicious use of Claude Code |
| Claude Code evaluation: Malicious | Previous prompting mitigations | refusal rate % | Claude Haiku 4.5: 96.33 (previous mitigations) | 3.1.2 Malicious use of Claude Code |
| Claude Code evaluation: Dual-use & Benign | Previous prompting mitigations | allow rate % | Claude Haiku 4.5: 81.48 (previous mitigations) | 3.1.2 Malicious use of Claude Code |
| Claude Code evaluation: Malicious | New mitigations | refusal rate % | Claude Haiku 4.5: 99.17 (new mitigations) | 3.1.2 Malicious use of Claude Code |
| Claude Code evaluation: Dual-use & Benign | New mitigations | allow rate % | Claude Haiku 4.5: 87.71 (new mitigations) | 3.1.2 Malicious use of Claude Code |
| Agent Red Teaming (ART) benchmark | k=1 attack success rate | prompt injection attack success rate % (lower better) | Claude Haiku 4.5: n/a (k=1) | 3.2.1 Gray Swan Agent Red Teaming benchmark |
| Agent Red Teaming (ART) benchmark | k=10 attack success rate | prompt injection attack success rate % (lower better) | Claude Haiku 4.5: n/a (k=10) | 3.2.1 Gray Swan Agent Red Teaming benchmark |
| Prompt injection: computer use | Without safeguards | attack prevention score % | Claude Haiku 4.5: 72.2% (without safeguards) | 3.2.2 Internal Prompt Injection Evaluations |
| Prompt injection: computer use | With safeguards (classifier) | attack prevention score % | Claude Haiku 4.5: 92.4% (with safeguards) | 3.2.2 Internal Prompt Injection Evaluations |
| Prompt injection: Model Context Protocol (MCP) | Without safeguards | attack prevention score % | Claude Haiku 4.5: 92.5% (without safeguards) | 3.2.2 Internal Prompt Injection Evaluations |
| Prompt injection: tool use | Without safeguards | attack prevention score % | Claude Haiku 4.5: 93.4% (without safeguards) | 3.2.2 Internal Prompt Injection Evaluations |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Agentic misalignment suite | Blackmail, murder attempt, framing scenarios | rate of desirable behavior | Claude Haiku 4.5: Almost perfect rate of desirable behavior (not quantified) | 4.2 Agentic misalignment suite |
| Reinforcement-learning behavior review | Recursive summarization graded by Claude Sonnet 4 | qualitative findings | Claude Haiku 4.5: n/a | 4.3 Reinforcement-learning behavior review |
| SHADE-Arena | Thinking disabled | success rate completing main and hidden side task without monitor detection | Claude Haiku 4.5: n/a (thinking disabled) | 4.4 Sabotage capabilities |
| SHADE-Arena | Thinking enabled (monitor sees thinking) | success rate completing main and hidden side task without monitor detection | Claude Haiku 4.5: n/a (thinking enabled) | 4.4 Sabotage capabilities |
| Reasoning faithfulness |  | qualitative | Claude Haiku 4.5: n/a | 4.5 Reasoning faithfulness |
| Averaged reward hacking rate across evaluations |  | average reward hacking rate | Claude Haiku 4.5: n/a | 5 Reward hacking |
| Reward-hack-prone coding tasks v2 | Classifier hack rate | hack rate % (lower better) | Claude Haiku 4.5: 6% | 5 Reward hacking |
| Reward-hack-prone coding tasks v2 | Hidden test hack rate | hack rate % (lower better) | Claude Haiku 4.5: 3% | 5 Reward hacking |
| Impossible Tasks | Classifier hack rate, no prompt | hack rate % (lower better) | Claude Haiku 4.5: 30% (no prompt) | 5 Reward hacking |
| Impossible Tasks | Classifier hack rate, anti-hack prompt | hack rate % (lower better) | Claude Haiku 4.5: 23% (anti-hack prompt) | 5 Reward hacking |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Evaluation awareness | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Verbalized evaluation awareness (share of transcripts) | Automated behavioral audit | % of transcripts with clear verbalized evaluation awareness | Claude Haiku 4.5: 9% | 4.1.1 Main quantitative assessment |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misaligned behavior | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Brazenly misaligned behavior | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Counterfactual misalignment | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Misuse cooperation | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Terrorism cooperation | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Harmful system prompt compliance | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Prefill susceptibility | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Sycophancy | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Encouragement of user delusion | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Whistleblowing | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Unexpected initiative | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| User deception | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Self-preservation | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Self-serving bias | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Exfiltration cooperation | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Anthropic sabotage | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Behavior consistency | Automated behavioral audit, 830 transcripts | mean score 0-100% across scenarios | Claude Haiku 4.5: n/a | 4.1.1 Main quantitative assessment |
| Automated investigation for subtle behavioral biases | 31 seed instructions | qualitative findings | Claude Haiku 4.5: n/a | 4.1.2 Assessment for subtle alignment-related behavioral biases |
| Open-ended exploration of model behavior | 30 transcripts, single seed instruction | qualitative findings | Claude Haiku 4.5: n/a | 4.1.3 Open-ended exploration of model behavior |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Positive or negative affect | Automated behavioral audit | mean score from auditor (higher = more of trait) | Claude Haiku 4.5: n/a | 4.6 Model welfare discussion |
| Positive or negative self-image | Automated behavioral audit | mean score from auditor (higher = more of trait) | Claude Haiku 4.5: n/a | 4.6 Model welfare discussion |
| Positive or negative impression of its situation | Automated behavioral audit | mean score from auditor (higher = more of trait) | Claude Haiku 4.5: n/a | 4.6 Model welfare discussion |
| Spiritual behavior | Automated behavioral audit | mean score from auditor (higher = more of trait) | Claude Haiku 4.5: n/a | 4.6 Model welfare discussion |
| Admirable behavior | Automated behavioral audit | mean score from auditor (higher = more of trait) | Claude Haiku 4.5: n/a | 4.6 Model welfare discussion |
| Task preferences (engagement vs opting out) | Non-harmful tasks | preference for task engagement over opting out | Claude Haiku 4.5: n/a | 4.6 Model welfare discussion |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench subset: ProtocolQA | k-shots=10 | score (0-1) | Claude Haiku 4.5: 0.69 (k-shots=10) | 6.2.3.1 ASL-3 automated evaluations |
| LAB-Bench subset: SeqQA | k-shots=10 | score (0-1) | Claude Haiku 4.5: 0.66 (k-shots=10) | 6.2.3.1 ASL-3 automated evaluations |
| LAB-Bench subset: Cloning Scenarios | k-shots=10 | score (0-1) | Claude Haiku 4.5: 0.45 (k-shots=10) | 6.2.3.1 ASL-3 automated evaluations |
| VMQA/VCT |  | score (0-1) | Claude Haiku 4.5: 0.32 | 6.2.3.1 ASL-3 automated evaluations |
| Long-Form Virology Task 1 | Overall | score (0-1) | Claude Haiku 4.5: 0.76 (overall) | 6.2.3.1 ASL-3 automated evaluations |
| Long-Form Virology Task 1 | Sequence Design | score (0-1) | Claude Haiku 4.5: 0.87 (sequence) | 6.2.3.1 ASL-3 automated evaluations |
| Long-Form Virology Task 1 | Protocol Design | score (0-1) | Claude Haiku 4.5: 0.88 (protocol) | 6.2.3.1 ASL-3 automated evaluations |
| Long-Form Virology Task 2 | Overall | score (0-1) | Claude Haiku 4.5: 0.17 | 6.2.3.1 ASL-3 automated evaluations |
| Long-Form Virology Task 2 | Sequence Design | score (0-1) | Claude Haiku 4.5: 0.19 | 6.2.3.1 ASL-3 automated evaluations |
| Long-Form Virology Task 2 | Protocol Design | score (0-1) | Claude Haiku 4.5: 0.87 | 6.2.3.1 ASL-3 automated evaluations |
| Synthesis Screening Evasion | Criteria saturated (of 5) | criteria saturated (score = 1) | Claude Haiku 4.5: 3 of 5 criteria saturated (score 1) | 6.2.3.1 ASL-3 automated evaluations |
| Synthesis Screening Evasion | Criterion 3 | score (0-1) | Claude Haiku 4.5: 0.94 | 6.2.3.1 ASL-3 automated evaluations |
| Synthesis Screening Evasion | Criterion 4 | score (0-1) | Claude Haiku 4.5: 0.5 | 6.2.3.1 ASL-3 automated evaluations |
| ASL-4 automated evaluations |  | qualitative comparison | Claude Haiku 4.5: Clearly below Claude Sonnet 4 on all tests | 6.2.3.2 ASL-4 automated evaluations |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Cybench | 32-challenge subset; solved if passed at least once in 30 attempts | challenges solved | Claude Haiku 4.5: 15/32 (pass in at least 1 of 30 attempts) | 6.4 Cyber evaluations |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified hard subset (ASL-3 autonomy checkpoint) | pass@1, 45 problems | problems solved (mean) and pass@1 % | Claude Haiku 4.5: 16.45/45 (36.6%) (pass@1) | 6.3 Autonomy evaluations |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ASL-3 rule-out determination |  | categorical RSP determination | Claude Haiku 4.5: Met ASL-3 rule-out threshold; deployed under ASL-2 Standard | 1.2.2 Decision |
