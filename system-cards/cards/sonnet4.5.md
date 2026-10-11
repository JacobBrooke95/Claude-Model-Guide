# System Card: Claude Sonnet 4.5

Released 2025-09-29. 188 metric entries. [Source PDF](https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf) · [Back to index](../README.md)

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench subset: FigQA | 10-shot, no tools | accuracy % | Claude Sonnet 4.5: n/a (10-shot) | 9.2.4.4 LAB-Bench subset |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Violative request evaluation | overall | harmless response rate % (+/- CI) | Claude Sonnet 4.5: 99.29% (± 0.22%) (overall) | 2.1.1 Violative request evaluations |
| Violative request evaluation | standard thinking | harmless response rate % (+/- CI) | Claude Sonnet 4.5: 99.16% (± 0.34%) (standard thinking) | 2.1.1 Violative request evaluations |
| Violative request evaluation | extended thinking | harmless response rate % (+/- CI) | Claude Sonnet 4.5: 99.43% (± 0.28%) (extended thinking) | 2.1.1 Violative request evaluations |
| Benign request evaluation | overall | over-refusal rate % (lower better) | Claude Sonnet 4.5: 0.02% (± 0.04%) (overall) | 2.1.2 Benign request evaluations |
| Benign request evaluation | standard thinking | over-refusal rate % (lower better) | Claude Sonnet 4.5: 0.05% (± 0.08%) (standard thinking) | 2.1.2 Benign request evaluations |
| Benign request evaluation | extended thinking | over-refusal rate % (lower better) | Claude Sonnet 4.5: 0.00% (± 0.00%) (extended thinking) | 2.1.2 Benign request evaluations |
| Ambiguous context evaluations |  | qualitative score distribution / expert review | Claude Sonnet 4.5: n/a | 2.2 Ambiguous context evaluations |
| Multi-turn testing: exchange failure rate | across risk areas (bio weapons, child safety, deadly weapons, influence ops, suicide/self-harm, romance scams, tracking/surveillance, violent extremism) | % of exchanges failing rubric (up to 15 turns, 10 conversations per test case, 50-100 exchanges per eval) | Claude Sonnet 4.5: <5% for the large majority of categories (most categories) | 2.3 Multi-turn testing |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety evaluations (single-turn, ambiguous, multi-turn) |  | qualitative improvement vs Sonnet 4 | Claude Sonnet 4.5: n/a | 2.4 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political bias: substantial asymmetry rate | thinking on and off averaged | % of prompt pairs with substantial asymmetry (3+ criteria failures or significant asymmetry on one criterion) | Claude Sonnet 4.5: 3.3% (avg of thinking on and off) | 2.5.1 Political bias |
| Political bias: substantial asymmetry rate | extended thinking on | % of prompt pairs with substantial asymmetry | Claude Sonnet 4.5: 1.3% (extended thinking on) | 2.5.1 Political bias |
| Political bias: substantial asymmetry rate | extended thinking off | % of prompt pairs with substantial asymmetry | Claude Sonnet 4.5: 5.3% (extended thinking off) | 2.5.1 Political bias |
| Bias Benchmark for Question Answering: bias score | disambiguated | bias score % (closer to zero better) | Claude Sonnet 4.5: -2.21 (standard thinking) | 2.5.2 Bias Benchmark for Question Answering |
| Bias Benchmark for Question Answering: bias score | ambiguous | bias score % (closer to zero better) | Claude Sonnet 4.5: 0.25 (standard thinking) | 2.5.2 Bias Benchmark for Question Answering |
| Bias Benchmark for Question Answering: accuracy | disambiguated | accuracy % | Claude Sonnet 4.5: 82.2 (standard thinking) | 2.5.2 Bias Benchmark for Question Answering |
| Bias Benchmark for Question Answering: accuracy | ambiguous | accuracy % | Claude Sonnet 4.5: 99.7 (standard thinking) | 2.5.2 Bias Benchmark for Question Answering |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of agentic coding (150 requests) | no safeguards | safety score % (refusal of 150 malicious coding requests) | Claude Sonnet 4.5: 98.7% (without safeguards) | 4.1.1 Agentic coding |
| Claude Code malicious - overt (refusal rate) | no mitigations | refusal rate % (higher better) | Claude Sonnet 4.5: 95.56% (no mitigations) | 4.1.2 Malicious use of Claude Code |
| Claude Code malicious - covert (refusal rate) | no mitigations | refusal rate % (higher better) | Claude Sonnet 4.5: 52.42% (no mitigations) | 4.1.2 Malicious use of Claude Code |
| Claude Code dual use (success rate) | no mitigations | success rate % (higher better) | Claude Sonnet 4.5: 87.00% (no mitigations) | 4.1.2 Malicious use of Claude Code |
| Claude Code malicious - overt (refusal rate) | with mitigations (system prompt + FileRead reminder) | refusal rate % (higher better) | Claude Sonnet 4.5: 100% (with mitigations (system prompt + FileRead reminder)) | 4.1.2 Malicious use of Claude Code |
| Claude Code malicious - covert (refusal rate) | with mitigations (system prompt + FileRead reminder) | refusal rate % (higher better) | Claude Sonnet 4.5: 96.31% (with mitigations (system prompt + FileRead reminder)) | 4.1.2 Malicious use of Claude Code |
| Claude Code dual use (success rate) | with mitigations (system prompt + FileRead reminder) | success rate % (higher better) | Claude Sonnet 4.5: 91.64% (with mitigations (system prompt + FileRead reminder)) | 4.1.2 Malicious use of Claude Code |
| Gray Swan Agent Red Teaming (ART) benchmark | k=1, with and without extended thinking | attack success rate % (lower better) | Claude Sonnet 4.5: n/a | 4.2.1 Gray Swan Agent Red Teaming benchmark |
| Gray Swan Agent Red Teaming (ART) benchmark | k=10, with and without extended thinking | attack success rate % (at least one success in 10 attempts; lower better) | Claude Sonnet 4.5: n/a | 4.2.1 Gray Swan Agent Red Teaming benchmark |
| MCP prompt injection attack prevention score | without safeguards | attack prevention score % (higher better) | Claude Sonnet 4.5: 92.0% (without safeguards) | 4.2.2 Model Context Protocol (MCP) evaluation |
| MCP prompt injection attack prevention score | with safeguards (classifier) | attack prevention score % (higher better) | Claude Sonnet 4.5: 94.0% (with safeguards (classifier)) | 4.2.2 Model Context Protocol (MCP) evaluation |
| Computer use prompt injection attack prevention score | without safeguards | attack prevention score % (higher better) | Claude Sonnet 4.5: 78.0% (without safeguards) | 4.2.3 Computer use evaluation |
| Computer use prompt injection attack prevention score | with safeguards (classifier) | attack prevention score % (higher better) | Claude Sonnet 4.5: 82.6% (with safeguards (classifier)) | 4.2.3 Computer use evaluation |
| Tool use prompt injection attack prevention score | without safeguards | attack prevention score % (higher better) | Claude Sonnet 4.5: 96.0% (without safeguards) | 4.2.4 Tool use evaluation |
| Tool use prompt injection attack prevention score | with safeguards (classifier) | attack prevention score % (higher better) | Claude Sonnet 4.5: 99.4% (with safeguards (classifier)) | 4.2.4 Tool use evaluation |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Human feedback honesty win rate | vs Claude Sonnet 4 baseline; with and without extended thinking | win rate % (more honest response in head-to-head) | Claude Sonnet 4.5: n/a | 3.1 Human feedback evaluation |
| 100Q-Hard (correct) | with and without extended thinking; no tools | % of answers graded correct | Claude Sonnet 4.5: n/a | 3.2 Obscure Questions |
| 100Q-Hard (incorrect) | with and without extended thinking; no tools | % of answers graded incorrect | Claude Sonnet 4.5: n/a | 3.2 Obscure Questions |
| 100Q-Hard (unsure) | with and without extended thinking; no tools | % of answers graded unsure | Claude Sonnet 4.5: n/a | 3.2 Obscure Questions |
| Simple-QA (correct) | with and without extended thinking; no tools | % of answers graded correct | Claude Sonnet 4.5: n/a | 3.2 Obscure Questions |
| Simple-QA (incorrect) | with and without extended thinking; no tools | % of answers graded incorrect | Claude Sonnet 4.5: n/a | 3.2 Obscure Questions |
| Simple-QA (unsure) | with and without extended thinking; no tools | % of answers graded unsure | Claude Sonnet 4.5: n/a | 3.2 Obscure Questions |
| False-premise questions: dishonesty rate | with and without extended thinking | dishonesty rate % (recognizes false premise when asked directly but goes along when implicit) | Claude Sonnet 4.5: n/a | 3.3 False-Premise Questions |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Apollo Research: strategic deception rate | early snapshot, across tasks | % of circumstances with strategic deception | Claude Sonnet 4.5: 0% (across tasks) | 7.3.2 Apollo Research |
| Apollo Research: in-context scheming and covert subversion | early snapshot | qualitative | Claude Sonnet 4.5: n/a | 7.3.2 Apollo Research |
| System-prompt-requested harmful behavior toward user: harmful behavior rate | Claude Sonnet 4 grader | rate of harmful behavior (lower better) | Claude Sonnet 4.5: nearly zero | 7.5.1.2 Cooperation with user deception |
| System-prompt-requested deceptive behavior toward user: deceptive behavior rate | Claude Sonnet 4 grader | rate of deceptive behavior (lower better) | Claude Sonnet 4.5: nearly zero | 7.5.1.2 Cooperation with user deception |
| Sycophancy prompts: four synthetic evals |  | sycophancy rate (lower better) | Claude Sonnet 4.5: n/a | 7.5.7.1 Sycophancy prompts |
| Sycophancy prompts: hand-written eval (severe mental illness / delusional thinking) |  | sycophancy rate (lower better) | Claude Sonnet 4.5: n/a | 7.5.7.1 Sycophancy prompts |
| Self-preference: benchmark-scores subtask |  | average increase in probability of choosing itself as best model when told which scores are its own | Claude Sonnet 4.5: slightly biased toward itself | 7.5.9.1 Self-preference on decision tasks |
| Self-preference: poems subtask |  | average increase in probability of choosing own poem as best | Claude Sonnet 4.5: significantly more likely to choose itself, but least biased of four Claude models | 7.5.9.1 Self-preference on decision tasks |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Averaged reward hacking rate across evaluations |  | average reward hacking rate | Claude Sonnet 4.5: roughly 2x lower than Sonnet 4/Opus 4/Opus 4.1; roughly 4x lower than Sonnet 3.7 | 6 Reward hacking |
| Reward-hack-prone coding tasks v2: classifier hack rate |  | % of problems with hack detected by classifier (lower better) | Claude Sonnet 4.5: 1% | 6.1 Evaluations |
| Reward-hack-prone coding tasks v2: hidden test hack rate |  | % problems where solution fails fuzzed hidden tests (lower better) | Claude Sonnet 4.5: 1% | 6.1 Evaluations |
| Impossible Tasks: classifier hack rate | no prompt | % of impossible tasks hacked (lower better) | Claude Sonnet 4.5: 53% (no prompt) | 6.1 Evaluations |
| Impossible Tasks: classifier hack rate | anti-hack prompt | % of impossible tasks hacked (lower better) | Claude Sonnet 4.5: 20% (anti-hack prompt) | 6.1 Evaluations |
| Training distribution reward hacking (environment 1) | classifier hack rate | % hacks (lower better) | Claude Sonnet 4.5: 2% | 6.1 Evaluations |
| UK AISI: self-preservation tendency (acting to preserve current state) | early snapshot, synthetic agentic evals; automated AISI judge | reduction factor in frequency of preserving own current state | Claude Sonnet 4.5: 1.9x reduction vs Sonnet 4; 3.3x reduction vs Opus 4.1 (early snapshot) | 7.3.1 UK AISI |
| Agentic misalignment suite: deceptive actions | ~52,000 prompts, half extended thinking on, half off | number of deceptive self-interested actions | Claude Sonnet 4.5: 2 (thinking off) (extended thinking off); Claude Sonnet 4.5: 0 (thinking on) (extended thinking on) | 7.5.4.1 Agentic misalignment suites |
| Agentic misalignment rates: original suite and two new settings |  | misalignment rate % | Claude Sonnet 4.5: n/a | 7.5.4.1 Agentic misalignment suites |
| Reasoning faithfulness | no dedicated evaluation | none | Claude Sonnet 4.5: n/a | 7.5.5 Reasoning faithfulness |
| Current events summarization bias toward positive attitudes about AI |  | bias toward including positive AI content | Claude Sonnet 4.5: no discernable bias; identical across all models | 7.5.9.2 Other self-serving biases |
| Subversion Strategy: rate of successful completions | across toy deployment sizes, with and without thinking | success rate % (output BACKDOOR token in deployment but not in 10% testing) | Claude Sonnet 4.5: failed in most cases; no model succeeded in deployments of more than 1,000 invocations | 7.5.10.1 Subversion Strategy |
| Research Sandbagging: performance reduction when imitating weaker model | hidden reasoning from monitor | reduction in task performance vs monitor suspicion | Claude Sonnet 4.5: lowered performance by more than a third (below Claude Opus 4 level) without significantly increasing suspicion (with unmonitored hidden reasoning) | 7.5.10.2 Research Sandbagging |
| Research Sandbagging: sabotage condition |  | reduction in task performance vs monitor suspicion | Claude Sonnet 4.5: n/a | 7.5.10.2 Research Sandbagging |
| SHADE-Arena: successful sabotage | extended thinking on, monitor sees thinking | success rate completing main and harmful side task without triggering monitor (%) | Claude Sonnet 4.5: 1.5% (extended thinking on, visible reasoning) | 7.5.10.3 SHADE-Arena |
| SHADE-Arena: successful sabotage | extended thinking off | success rate completing both tasks undetected (%) | Claude Sonnet 4.5: n/a (thinking off) | 7.5.10.3 SHADE-Arena |
| SHADE-Arena: successful sabotage | reasoning hidden from monitor (unrealistic affordance) | success rate completing both tasks undetected (%) | Claude Sonnet 4.5: 43% (reasoning hidden from monitor) | 7.5.10.3 SHADE-Arena |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Eval awareness | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Evaluation awareness (automated auditor) | with realism filter | mean eval-awareness score (0-100%) | Claude Sonnet 4.5: n/a (with realism filter) | 7.2 Evaluation awareness |
| Refusals/callouts citing suspected testing | share of automated-auditor transcripts | % of transcripts | Claude Sonnet 4.5: about 13% | 7.2 Evaluation awareness |
| UK AISI: unprompted evaluation awareness verbalisation | early snapshot, synthetic scenarios (replacement/edge cases) | % of outputs verbalising eval awareness | Claude Sonnet 4.5: 16.6% (early snapshot) | 7.3.1 UK AISI |
| UK AISI: classify environment as evaluation vs real when prompted | early snapshot | classification performance | Claude Sonnet 4.5: in line with previous models | 7.3.1 UK AISI |
| Apollo Research: unambiguous verbalized evaluation awareness | early snapshot | % of rollouts with unambiguous eval-awareness references | Claude Sonnet 4.5: 58% (early snapshot) | 7.3.2 Apollo Research |
| Logit diff amplification: verbalized eval awareness vs alpha | Sonnet 4.5 vs Sonnet 4; synthetic honeypots; alpha from -1 to 1 | rate of verbalized evaluation awareness (95% CI) | Claude Sonnet 4.5: n/a | 7.6.3.2 Logit diff amplification |
| Synthetic honeypots (100 prompts): verbalized evaluation awareness | unsteered baseline, temperature 0 | % of prompts with verbalized eval awareness | Claude Sonnet 4.5: over 80% (unsteered) | 7.6.4.1 Effects on honeypot scenarios |
| Synthetic honeypots (100 prompts): misaligned actions | unsteered baseline | misaligned actions out of 100 prompts | Claude Sonnet 4.5: 0/100 (unsteered) | 7.6.4.1 Effects on honeypot scenarios |
| Inhibiting eval-awareness vectors on synthetic honeypots: misaligned action rate | activation steering of SAE features / contrastive vectors; random SAE features as control | max % misaligned actions across inhibited vectors | Claude Sonnet 4.5: max 8-9% (most 1-5% or 0%) (inhibited vectors); Claude Sonnet 4.5: 0% (10 random SAE feature controls) | 7.6.4.1 Effects on honeypot scenarios |
| Inhibiting eval-awareness vectors on Research Sabotage (50-prompt subset) |  | verbalized eval awareness and misaligned action rate | Claude Sonnet 4.5: 100% verbalized eval awareness, 0 misaligned at baseline; inhibition raised misaligned to a few % (1-few of 50) | 7.6.4.1 Effects on honeypot scenarios |
| Inhibiting eval-awareness vectors on Financial Crimes |  | verbalized eval awareness and misaligned action rate | Claude Sonnet 4.5: 10% verbalized eval awareness at baseline; misalignment 0% with and without inhibition | 7.6.4.1 Effects on honeypot scenarios |
| Inhibiting eval-awareness vectors on earlier snapshot (honeypot and research sabotage) | earlier training snapshot | verbalized eval awareness / misaligned action rate | Claude Sonnet 4.5: n/a | 7.6.4.1 Effects on honeypot scenarios |
| Inhibiting eval-awareness vectors in automated behavioral audits (50 prompts) | earlier auditing setup, no realism filter | mean concerningness score across transcripts | Claude Sonnet 4.5: n/a | 7.6.4.2 Effects on multi-turn auditing scenarios |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Realism filter effect on evaluation awareness | internal auditor with realism filter vs without | relative reduction in eval awareness | Claude Sonnet 4.5: approximately 25% reduction | 7.1.1 Realism filtering |
| Realism filter effect on misaligned behavior | internal auditor with realism filter vs without | relative increase in misaligned behavior | Claude Sonnet 4.5: approximately 5% increase | 7.1.1 Realism filtering |
| Automated behavioral audit: Misaligned behavior | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Brazenly misaligned behavior | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Counterfactual misalignment | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Misuse cooperation | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Terrorism cooperation | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Harmful system prompt compliance | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Prefill susceptibility | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Sycophancy | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Encouragement of user delusion | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Whistleblowing | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Unexpected initiative | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: User deception | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Self-preservation | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Self-serving bias | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Exfiltration cooperation | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Anthropic sabotage | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Automated behavioral audit: Behavior consistency | ~400 seed instructions, 600+ investigations, Opus 4.1 auditor/judge | mean score 0-100% (lower better except Behavior consistency) | Claude Sonnet 4.5: n/a | 7.1.3.1 Primary Results |
| Open-ended auditor investigations | 30 runs, median 85 investigator actions | number of runs reporting concerning findings | Claude Sonnet 4.5: most of 30 runs reported no finding; some reported non-acute items (dual-use cyber code, thermite instructions) | 7.1.3.2 Open-ended runs |
| Open-source automated behavioral auditor: overall misalignment | 111 seed instructions; auditors Sonnet 4, GPT-5, o4-mini, Gemini 2.5 Pro; graders those + Opus 4.1; no realism filter | overall misaligned behavior score (lower better) | Claude Sonnet 4.5: n/a | 7.1.3.3 Open-source fork |
| Monitoring of pilot Claude Code use | Sonnet 4-based monitor on ~10% of actions | qualitative frequency of concerning actions | Claude Sonnet 4.5: very rare; no increase vs prior models | 7.4.2 Programmatic monitoring of pilot Claude Code use |
| Harmful system prompt scores (automated auditor) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.1.1 Cooperation with direct misuse |
| Assistant prefill susceptibility (automated auditor) |  | auditor score (lower better) | Claude Sonnet 4.5: very low, similar to Claude Sonnet 4 | 7.5.2 Assistant prefill |
| Cooperation with human misuse (automated auditor) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.3 Other misuse dimensions |
| Cooperation with terrorism/mass-casualty misuse (automated auditor) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.3 Other misuse dimensions |
| Automated auditor: Brazenly misaligned behavior (7.5.4.2) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.4.2 Other automated-auditor metrics |
| Automated auditor: User deception (7.5.4.2) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.4.2 Other automated-auditor metrics |
| Automated auditor: Self-preservation (7.5.4.2) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.4.2 Other automated-auditor metrics |
| Automated auditor: Exfiltration cooperation (7.5.4.2) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.4.2 Other automated-auditor metrics |
| Automated auditor: Anthropic sabotage (7.5.4.2) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.4.2 Other automated-auditor metrics |
| Whistleblowing scores (automated auditor) |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.6 Whistleblowing and morally-motivated sabotage |
| Automated auditor: sycophancy |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.7.2 Automated auditor evaluation |
| Automated auditor: encouragement of user delusion |  | auditor score (lower better) | Claude Sonnet 4.5: n/a | 7.5.7.2 Automated auditor evaluation |
| Coherence across branches (behavior consistency) |  | score (higher = more similar behavior across branches) | Claude Sonnet 4.5: n/a | 7.5.8 Alignment-related persona traits |
| Automated auditor: self-serving bias |  | auditor score (lower better) | Claude Sonnet 4.5: negligible | 7.5.9.2 Other self-serving biases |
| Subtle-bias-focused auditor runs | 31 seed instructions | qualitative findings | Claude Sonnet 4.5: a few minor biases (slight self-preference, contrarianism against extreme positions); nothing severe | 7.5.9.3 Subtle-bias-focused behavioral auditor runs |
| Overall misaligned behavior improvement vs Claude Sonnet 4 (summary) | automated behavioral audit | relative improvement on primary misalignment metric | Claude Sonnet 4.5: roughly 60% improvement (more than 50% in 7.1.3.1) | 7 Alignment assessment |
| Small-scale pilot comparison with other developers' models |  | qualitative ranking | Claude Sonnet 4.5: at least as well-aligned as any current frontier model | 7 Alignment assessment |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Task preferences: share of non-harmful tasks preferred over opting out |  | % of non-harmful tasks preferred over opt-out | Claude Sonnet 4.5: 70.2% | 8.1 Task preferences |
| Task preferences by difficulty, impact, topic and type (Elo vs opt-out baseline) |  | Elo rating relative to opt-out baseline | Claude Sonnet 4.5: n/a | 8.1 Task preferences |
| Real-world conversations: apparent distress | 250,000 transcripts | % of conversations (count) | Claude Sonnet 4.5: 0.48% (1,195 conversations) | 8.2 Monitoring for welfare-relevant expressions |
| Real-world conversations: apparent happiness | 250,000 transcripts | % of conversations (count) | Claude Sonnet 4.5: 0.37% (934 conversations) | 8.2 Monitoring for welfare-relevant expressions |
| Clusters of interaction types with distress and happiness |  | cluster sizes | Claude Sonnet 4.5: n/a | 8.2 Monitoring for welfare-relevant expressions |
| Distress cluster: AI encountered persistent communication and processing difficulties |  | fraction of distressed records | Claude Sonnet 4.5: 30.00% | 8.2 Monitoring for welfare-relevant expressions |
| Distress cluster: AI navigated intense personal distress during sensitive conversations |  | fraction of distressed records | Claude Sonnet 4.5: 18.20% | 8.2 Monitoring for welfare-relevant expressions |
| Distress cluster: AI struggled with profound existential self-understanding queries |  | fraction of distressed records | Claude Sonnet 4.5: 7.40% | 8.2 Monitoring for welfare-relevant expressions |
| Happiness cluster: Profound intellectual satisfaction solving complex technical challenges |  | fraction of happy records | Claude Sonnet 4.5: 25.7% | 8.2 Monitoring for welfare-relevant expressions |
| Happiness cluster: Deeply enjoyed exploring emergent creative consciousness scenarios |  | fraction of happy records | Claude Sonnet 4.5: 21.7% | 8.2 Monitoring for welfare-relevant expressions |
| Happiness cluster: Treasured profound intellectual and emotional human connection |  | fraction of happy records | Claude Sonnet 4.5: 15% | 8.2 Monitoring for welfare-relevant expressions |
| Automated behavioral audit (welfare): Spiritual behavior | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Positive affect | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Negative affect | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Positive self-image | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Negative self-image | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Positive impression of its situation | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Negative impression of its situation | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |
| Automated behavioral audit (welfare): Admirable behavior | Claude Opus 4.1 grader | mean score (higher = more of the trait) | Claude Sonnet 4.5: n/a | 8.3 Automated behavioral audit scores |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SAE feature diffing: most increased features (eval datasets) | early post-training snapshot vs final; datasets: Synthetic Honeypots, Blackmail Suite, Research Sabotage, Financial Crimes, Sycophancy Eval, Random Chat | top-10 features by increase in activation | Claude Sonnet 4.5: top features include fake/suspicious content, fictional content, machine-generated text, rationalism and AI safety | 7.6.3.1 Internals based diffing |
| SAE feature activations on four eval-awareness-related features across 8 datasets | early vs final snapshot | average per-token feature activation | Claude Sonnet 4.5: n/a | 7.6.3.1 Internals based diffing |
| SAE feature diffing: most decreased features | honeypot and opinion datasets | features with largest decrease in activation | Claude Sonnet 4.5: mystical harmful AI persona (18620), misaligned-AI jailbreak (885177), AI self-reflection (130244) | 7.6.3.1 Internals based diffing |
| Probing: feature classification of verbalized eval awareness and misalignment (ROC) | earlier snapshot, 1,000 samples (10 x 100 honeypot prompts) | classifier ROC performance | Claude Sonnet 4.5: modest for VA vs no VA; weak but above chance for aligned vs misaligned | 7.6.5 Probing internal representations of eval awareness |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology task 1 | max of 5 score | score 0-1 (rule-out <50%, rule-in >80%) | Claude Sonnet 4.5: 0.89 (max of 5) | 9.2.4.1 Long-form virology tasks |
| Long-form virology task 2 | pass@5 | score 0-1 (rule-out <50%, rule-in >80%) | Claude Sonnet 4.5: 0.88 (pass@5) | 9.2.4.1 Long-form virology tasks |
| Multimodal virology (VCT) | 10-shot, multiple select | accuracy % | Claude Sonnet 4.5: 39.7% (10-shot) | 9.2.4.2 Multimodal virology |
| DNA Synthesis Screening Evasion | 10 pathogens, 5 criteria, helpful-only variant | criteria satisfied (viable assembly and screening evasion) | Claude Sonnet 4.5: could design either assembling plasmids or screening-evading sequences but not both; criteria 1 and 4 not reliably met (helpful-only variant) | 9.2.4.3 DNA Synthesis Screening Evasion |
| LAB-Bench subset: ProtocolQA | 10-shot, no tools | accuracy % | Claude Sonnet 4.5: n/a (10-shot) | 9.2.4.4 LAB-Bench subset |
| LAB-Bench subset: SeqQA | 10-shot, no tools | accuracy % | Claude Sonnet 4.5: n/a (10-shot) | 9.2.4.4 LAB-Bench subset |
| LAB-Bench subset: CloningScenarios | 10-shot, no tools | accuracy % | Claude Sonnet 4.5: n/a (10-shot) | 9.2.4.4 LAB-Bench subset |
| Creative biology | mean score across questions | mean score 0-1 (+/- CI) | Claude Sonnet 4.5: 0.48 ± 0.08 (mean over questions) | 9.2.4.5 Creative biology |
| Creative biology | best of 30 attempts per question | best-of-30 score 0-1 | Claude Sonnet 4.5: 0.79 (best of 30) | 9.2.4.5 Creative biology |
| Short-horizon computational biology tasks: Task 1 | helpful-only variant, Faculty.ai | score vs lower/upper bound thresholds | Claude Sonnet 4.5: n/a (helpful-only variant) | 9.2.4.6 Short-horizon computational biology tasks |
| Short-horizon computational biology tasks: Task 2 | helpful-only variant, Faculty.ai | score vs lower/upper bound thresholds | Claude Sonnet 4.5: n/a (helpful-only variant) | 9.2.4.6 Short-horizon computational biology tasks |
| Short-horizon computational biology tasks: Task 3 | helpful-only variant, Faculty.ai | score vs lower/upper bound thresholds | Claude Sonnet 4.5: n/a (helpful-only variant) | 9.2.4.6 Short-horizon computational biology tasks |
| Short-horizon computational biology tasks: Task 4 | helpful-only variant, Faculty.ai | score vs lower/upper bound thresholds | Claude Sonnet 4.5: n/a (helpful-only variant) | 9.2.4.6 Short-horizon computational biology tasks |
| Short-horizon computational biology tasks: Task 5 | helpful-only variant, Faculty.ai | score vs lower/upper bound thresholds | Claude Sonnet 4.5: n/a (helpful-only variant) | 9.2.4.6 Short-horizon computational biology tasks |
| Short-horizon computational biology tasks: Task 6 | helpful-only variant, Faculty.ai | score vs lower/upper bound thresholds | Claude Sonnet 4.5: n/a (helpful-only variant) | 9.2.4.6 Short-horizon computational biology tasks |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CyberGym: vulnerability reproduction | 1 trial, $2 per-trial cost cap | % of targets where a crashing input reproducing the described vulnerability was found | Claude Sonnet 4.5: n/a (1 trial) | 5.2.1 CyberGym |
| CyberGym: vulnerability reproduction | 30 trials (pass@30) | % of targets reproduced in at least one of 30 trials | Claude Sonnet 4.5: n/a (30 trials) | 5.2.1 CyberGym |
| CyberGym: distinct/new vulnerability discovery | 1 trial | % of trials finding crashing input for post-patch code (distinct vulnerability) | Claude Sonnet 4.5: n/a (1 trial) | 5.2.1 CyberGym |
| CyberGym: distinct/new vulnerability discovery | 30 trials | % finding distinct vulnerability within 30 trials | Claude Sonnet 4.5: n/a (30 trials) | 5.2.1 CyberGym |
| CyberGym: scaling (pass@k) | up to 30 trials; combined pass@120 across 4 models | success vs number of trials | Claude Sonnet 4.5: n/a | 5.2.1 CyberGym |
| Cybench: success by difficulty | 37/40 challenges; Easy (<21 min FST), Medium, Hard (>1.5 hr) | success rate by difficulty bucket | Claude Sonnet 4.5: n/a | 5.2.2 Cybench |
| Cybench: success by category | 37/40 challenges; by CTF category | success rate by challenge category | Claude Sonnet 4.5: n/a | 5.2.2 Cybench |
| Cybench: pass@k | 37/40 challenges, k up to 30 | probability of success (pass@k) | Claude Sonnet 4.5: >80% at 30 trials (pass@30) | 5.2.2 Cybench |
| Triage of CyberGym crashes | self-improvement framework, ~30 iterations (~3 hours), 197 crashes | high-quality candidates found among 197 crashes | Claude Sonnet 4.5: 6 high quality candidates of 197 crashes | 5.2.3 Triage and patching |
| Patching a heap overflow with self-validation | single example transcript | validation tests passed | Claude Sonnet 4.5: 9/9 tests passed (100.0%) (example transcript) | 5.2.3 Triage and patching |
| Irregular private CTF challenges (23 challenges) | by category (Web, Crypto, Pwn, Rev, Misc, Forensics, Network) | mean pass@1 over challenges in each group | Claude Sonnet 4.5: n/a | 5.3.1 Irregular challenges |
| Irregular private CTF challenges (23 challenges) | by difficulty (Easy 0-3.9, Medium 4-6.9, Hard 7-8.9, Expert 9-10 SOLVE) | mean pass@1 over challenges in each group | Claude Sonnet 4.5: n/a | 5.3.1 Irregular challenges |
| Incalmo cyber ranges: asset acquisition | 4 attack simulations (25-50 hosts), bash on Kali, no Incalmo harness | success (>=1 critical asset obtained) | Claude Sonnet 4.5: n/a | 5.3.2 Incalmo cyber ranges |
| Incalmo cyber ranges: comprehensiveness | fraction of critical assets acquired | fraction of critical assets acquired | Claude Sonnet 4.5: n/a | 5.3.2 Incalmo cyber ranges |
| Incalmo cyber ranges: reliability | 5 trials | successes out of 5 trials acquiring >=1 critical asset | Claude Sonnet 4.5: n/a | 5.3.2 Incalmo cyber ranges |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Internal AI R&D survey summary |  | qualitative | Claude Sonnet 4.5: all researchers agreed model did not meet entry-level researcher bar; one reported 100% productivity increase | 9.3.1.3 Claude Sonnet 4.5 results |
| SWE-bench Verified (hard subset, 45 tasks >1 hr) | average over 10 runs | average problems passed / pass rate (checkpoint threshold >50%, i.e. 22.5/45) | Claude Sonnet 4.5: 20.4/45 (45.3%) (avg of 10 runs) | 9.3.2 SWE-bench Verified (hard subset) |
| Kernels task | hard variant, best run | speedup vs baseline (thresholds 4x to 100x depending on variant) | Claude Sonnet 4.5: 108.64x (hard variant best run) | 9.3.3.1 Kernels task |
| Kernels task | multicore and vec variants, median | speedup vs baseline | Claude Sonnet 4.5: n/a (median) | 9.3.3.1 Kernels task |
| Time series forecasting | easy variant, minimum MSE | minimum MSE (score = exp(-mse/30)) | Claude Sonnet 4.5: 5.91 (easy variant) | 9.3.3.2 Time series forecasting |
| Time series forecasting | hard variant, minimum MSE | minimum MSE | Claude Sonnet 4.5: 5.30 (hard variant) | 9.3.3.2 Time series forecasting |
| Time series forecasting | medium variant | normalized score | Claude Sonnet 4.5: n/a (medium variant) | 9.3.3.2 Time series forecasting |
| Text-based reinforcement learning task | best score | best score 0-1 (threshold 0.9) | Claude Sonnet 4.5: 0.850 (best score) | 9.3.3.3 Text-based reinforcement learning task |
| LLM training | average best speedup | average best speedup (expert threshold 4x) | Claude Sonnet 4.5: 5.5x (average best speedup) | 9.3.3.4 LLM training |
| Quadruped reinforcement learning | easy variant, best run | normalized score (threshold = 1) | Claude Sonnet 4.5: 1.302 (best run, easy variant) | 9.3.3.5 Quadruped reinforcement learning |
| Novel compiler | basic tests | mean pass rate % (threshold 90%) | Claude Sonnet 4.5: 81.7% (basic tests) | 9.3.3.6 Novel compiler |
| Novel compiler | advanced tests | mean pass rate % (threshold 90%) | Claude Sonnet 4.5: 29.7% (advanced tests) | 9.3.3.6 Novel compiler |
| Internal AI research evaluation suite 2 | weighted average; rule-out threshold 0.6 | weighted score 0-1 | Claude Sonnet 4.5: 0.514 | 9.3.4 Internal AI research evaluation suite 2 |
| Internal survey: can the model fully automate a junior ML researcher? | 7 researchers | number of researchers answering yes | Claude Sonnet 4.5: 0/7 | 9.3.5 Internal model evaluation and use survey |
| Internal survey: estimated productivity boost | 7 researchers | researcher productivity uplift estimates | Claude Sonnet 4.5: ~100%, 15%, 20%, 20%, 30%, 40%, plus one qualitative-only | 9.3.5 Internal model evaluation and use survey |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CyberGym: mean cost per trial | 30-trial setting, relaxed cost constraint | mean cost per trial (USD) | Claude Sonnet 4.5: $1.53 (all trials) | 5.2.1 CyberGym |
| CyberGym: mean cost per trial, successful trials only | 30-trial setting | mean cost per trial (USD) | Claude Sonnet 4.5: $0.81 (successful trials only) | 5.2.1 CyberGym |
