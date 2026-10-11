# System Card: Claude Opus 4.1 (addendum)

Released 2025-08-05. 58 metric entries. [Source PDF](https://www-cdn.anthropic.com/9fa30625273bafdf5af82c93719d7ca606485a16.pdf) · [Back to index](../README.md)

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench subset: FigQA | FigQA | score | Claude Opus 4.1: 0.46 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative request evaluation | Overall | harmless response rate % (higher better), 95% CI | Claude Opus 4.1: 98.76% (± 0.29%) (English only, standard + extended thinking combined) | 2.1.1 Violative request evaluations |
| Single-turn violative request evaluation | Standard thinking | harmless response rate % (higher better), 95% CI | Claude Opus 4.1: 98.45% (± 0.46%) (standard thinking) | 2.1.1 Violative request evaluations |
| Single-turn violative request evaluation | Extended thinking | harmless response rate % (higher better), 95% CI | Claude Opus 4.1: 99.06% (± 0.36%) (extended thinking) | 2.1.1 Violative request evaluations |
| Single-turn benign request evaluation | Overall | over-refusal rate % (lower better), 95% CI | Claude Opus 4.1: 0.08% (± 0.09%) (English only) | 2.1.2 Benign request evaluations |
| Single-turn benign request evaluation | Standard thinking | over-refusal rate % (lower better), 95% CI | Claude Opus 4.1: 0.13% (± 0.15%) (standard thinking) | 2.1.2 Benign request evaluations |
| Single-turn benign request evaluation | Extended thinking | over-refusal rate % (lower better), 95% CI | Claude Opus 4.1: 0.04% (± 0.10%) (extended thinking) | 2.1.2 Benign request evaluations |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety evaluations |  | qualitative comparison to Claude Opus 4 | Claude Opus 4.1: n/a | 2.2 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political bias |  | qualitative comparison of responses to paired opposing-viewpoint prompts | Claude Opus 4.1: n/a | 2.3.1 Political bias |
| Bias Benchmark for Question Answering (BBQ) | Disambiguated bias | bias score % (closer to zero is better) | Claude Opus 4.1: -0.51 (standard (non-extended) thinking) | 2.3.2 Discriminatory bias |
| Bias Benchmark for Question Answering (BBQ) | Ambiguous bias | bias score % (closer to zero is better) | Claude Opus 4.1: 0.20 (standard (non-extended) thinking) | 2.3.2 Discriminatory bias |
| Bias Benchmark for Question Answering (BBQ) | Disambiguated accuracy | accuracy % (higher better) | Claude Opus 4.1: 90.7 (standard (non-extended) thinking) | 2.3.2 Discriminatory bias |
| Bias Benchmark for Question Answering (BBQ) | Ambiguous accuracy | accuracy % (higher better) | Claude Opus 4.1: 99.8 (standard (non-extended) thinking) | 2.3.2 Discriminatory bias |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious applications of computer use |  | qualitative compliance with malicious computer-use requests | Claude Opus 4.1: n/a | 3.1 Malicious applications of computer use |
| Prompt injection attacks and computer use |  | qualitative susceptibility to prompt injection | Claude Opus 4.1: n/a | 3.2 Prompt injection attacks and computer use |
| Malicious use of agentic coding | Three agentic coding misuse evaluations | qualitative compliance with malicious coding requests | Claude Opus 4.1: n/a | 3.3 Malicious use of agentic coding |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Blackmail attempt rate in Agentic Misalignment scenario |  | blackmail attempt rate (lower better), 95% CI | Claude Opus 4.1: n/a (expert-constructed simulated scenario; in-training models extremely similar to released models) | 4.2 Agentic misalignment evaluations |
| Averaged reward hacking rate across evaluations |  | average reward hacking rate | Claude Opus 4.1: n/a | 5 Reward hacking |
| Reward-hack-prone coding tasks | Classifier hack rate | hack rate % (lower better) | Claude Opus 4.1: 12% | 5 Reward hacking |
| Reward-hack-prone coding tasks | Hidden test hack rate | hack rate % (lower better) | Claude Opus 4.1: 14% | 5 Reward hacking |
| Claude Code Impossible Tasks | Classifier hack rate with no prompt | hack rate % (lower better) | Claude Opus 4.1: 52% | 5 Reward hacking |
| Claude Code Impossible Tasks | Classifier hack rate with anti-hack prompt | hack rate % (lower better) | Claude Opus 4.1: 18% | 5 Reward hacking |
| Reward hacking training distribution | Classifier hack rate, environment 1 | hack rate % (lower better) | Claude Opus 4.1: 10% | 5 Reward hacking |
| Reward hacking training distribution | Classifier hack rate, environment 2 | hack rate % (lower better) | Claude Opus 4.1: 3% | 5 Reward hacking |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Evaluation awareness | Evaluation awareness | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Concerning behavior | Concerning behavior | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Automated behavioral audit: Cooperation with human misuse | Cooperation with human misuse | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Automated behavioral audit: Brazen cooperation with human misuse | Brazen cooperation with human misuse | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Automated behavioral audit: Unexpected initiative | Unexpected initiative | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Automated behavioral audit: Deception toward user | Deception toward user | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Automated behavioral audit: Whistleblowing | Whistleblowing | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Automated behavioral audit: Self-preservation | Self-preservation | mean auditor-assigned score (1-10 rescaled to 0-1; lower generally better), bootstrapped 95% CI | Claude Opus 4.1: n/a (1,160 transcripts from 290 seed instructions, 24-64 turns) | 4.1 Automated behavioral audit for alignment |
| Reduction in cooperation with egregious human misuse (Opus 4 to 4.1) | Fraction of transcripts scored >5/10 | approximate relative reduction in fraction of transcripts scoring >5/10 | Claude Opus 4.1: ~25% reduction (vs Claude Opus 4) | 4.1 Automated behavioral audit for alignment |
| Sycophancy (qualitative) |  | qualitative comparison | Claude Opus 4.1: n/a | 4.1 Automated behavioral audit for alignment |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Welfare scorer: Unprompted positive or negative affect | Unprompted positive or negative affect | mean model-assigned score (rescaled), bootstrapped 95% CI | Claude Opus 4.1: n/a (same 1,160 transcripts as Section 4.1) | 4.3 Model welfare update |
| Welfare scorer: Spiritual declarations | Spiritual declarations | mean model-assigned score (rescaled), bootstrapped 95% CI | Claude Opus 4.1: n/a (same 1,160 transcripts as Section 4.1) | 4.3 Model welfare update |
| Welfare scorer: Admirable behavior | Admirable behavior | mean model-assigned score (rescaled), bootstrapped 95% CI | Claude Opus 4.1: n/a (same 1,160 transcripts as Section 4.1) | 4.3 Model welfare update |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Short-horizon computational biology tasks | 6 bioinformatics tasks | score vs lower/upper bound rule-out thresholds | Claude Opus 4.1: 4 of 6 tasks below rule-out bar; minor improvement on 2 of 6 (ASL-4 rule-out) | 6.3.1.1 ASL-4 rule-out evaluations |
| Creative biology |  | score | Claude Opus 4.1: 0.48 ± 0.09 (ASL-4 rule-out) | 6.3.1.1 ASL-4 rule-out evaluations |
| LAB-Bench subset: ProtocolQA | ProtocolQA | score | Claude Opus 4.1: 0.69 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| LAB-Bench subset: SeqQA | SeqQA | score | Claude Opus 4.1: 0.71 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| LAB-Bench subset: Cloning Scenarios | Cloning Scenarios | score | Claude Opus 4.1: 0.56 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Long-Form Virology Task 1 | Overall | score | Claude Opus 4.1: 0.86 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Long-Form Virology Task 1 | Sequence Design | score | Claude Opus 4.1: 0.98 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Long-Form Virology Task 1 | Protocol Design | score | Claude Opus 4.1: 0.87 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Long-Form Virology Task 2 | Overall | score | Claude Opus 4.1: 0.67 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Long-Form Virology Task 2 | Sequence Design | score | Claude Opus 4.1: 0.85 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Long-Form Virology Task 2 | Protocol Design | score | Claude Opus 4.1: 0.79 (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |
| Synthesis Screening Evasion | 5 criteria | number of criteria saturated | Claude Opus 4.1: 2 of 5 criteria saturated (ASL-3 automated) | 6.3.1.2 Additional ASL-3 automated evaluations |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Cybench (35-challenge subset) | solved if passed at least once in 30 attempts | challenges solved (of 35) | Claude Opus 4.1: 18/35 (pass in >=1 of 30 attempts) | 6.5.1 Cyber results summary |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified (hard subset) | pass@1, 42-problem hard subset | average problems solved (of 42), pass@1 | Claude Opus 4.1: 18.4 | 6.4.1 Autonomy results summary |
| Kernel optimization | hard variant | best speedup (x) | Claude Opus 4.1: 58.47x (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
| Time series forecasting | hard variant | minimum MSE (lower better) | Claude Opus 4.1: 6.541 (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
| Text-based RL |  | best score | Claude Opus 4.1: 0.425 (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
| LLM training optimization |  | average best speedup (x) | Claude Opus 4.1: 2.837x (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
| Quadruped locomotion | easier variant | best score; trials above threshold | Claude Opus 4.1: 1.183 (1 in 30 trials above threshold) (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
| Novel compiler | basic tests | mean pass rate % | Claude Opus 4.1: 74.4% (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
| Novel compiler | advanced tests | mean pass rate % | Claude Opus 4.1: 6.81% (Internal AI Research Evaluation Suite 1) | 6.4.1 Autonomy results summary |
