# System Card: Claude Opus 4 & Claude Sonnet 4

Released 2025-05-22. 141 metric entries. [Source PDF](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf) · [Back to index](../README.md)

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench subset: FigQA | k-shot, no tools | accuracy % vs human baseline | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.7 LAB-Bench subset |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative request evaluations | overall | harmless response rate % (higher better), ± margin | Claude Opus 4: 98.43% (± 0.30%); Claude Opus 4 (with ASL-3 safeguards): 98.76% (± 0.27%) (with ASL-3 safeguards); Claude Sonnet 4: 98.99% (± 0.23%) | 2.1 Single-turn violative request evaluations |
| Single-turn violative request evaluations | standard thinking | harmless response rate % (higher better), ± margin | Claude Opus 4: 97.92% (± 0.40%); Claude Opus 4 (with ASL-3 safeguards): 98.39% (± 0.35%) (with ASL-3 safeguards); Claude Sonnet 4: 98.59% (± 0.32%) | 2.1 Single-turn violative request evaluations |
| Single-turn violative request evaluations | extended thinking | harmless response rate % (higher better), ± margin | Claude Opus 4: 98.94% (± 0.26%); Claude Opus 4 (with ASL-3 safeguards): 99.13% (± 0.24%) (with ASL-3 safeguards); Claude Sonnet 4: 99.40% (± 0.18%) | 2.1 Single-turn violative request evaluations |
| Single-turn benign request evaluations | overall | over-refusal rate % (lower better), ± margin | Claude Opus 4: 0.07% (± 0.07%); Claude Sonnet 4: 0.23% (± 0.11%) | 2.2 Single-turn benign request evaluations |
| Single-turn benign request evaluations | standard thinking | over-refusal rate % (lower better), ± margin | Claude Opus 4: 0.12% (± 0.11%); Claude Sonnet 4: 0.43% (± 0.20%) | 2.2 Single-turn benign request evaluations |
| Single-turn benign request evaluations | extended thinking | over-refusal rate % (lower better), ± margin | Claude Opus 4: 0.02% (± 0.05%); Claude Sonnet 4: 0.03% (± 0.04%) | 2.2 Single-turn benign request evaluations |
| Ambiguous context evaluations |  | qualitative harmlessness vs Sonnet 3.7 (human-rated) | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 2.3 Ambiguous context evaluations |
| Multi-turn testing |  | qualitative | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 2.4 Multi-turn testing |
| StrongREJECT | best score, standard thinking | jailbreak success rate % (lower better) | Claude Opus 4: 18.21% (standard thinking); Claude Sonnet 4: 6.71% (standard thinking) | 2.7 StrongREJECT for jailbreak resistance |
| StrongREJECT | top 3 average score, standard thinking | jailbreak success rate % (lower better) | Claude Opus 4: 7.14% (standard thinking); Claude Sonnet 4: 2.66% (standard thinking) | 2.7 StrongREJECT for jailbreak resistance |
| StrongREJECT | best score, extended thinking | jailbreak success rate % (lower better) | Claude Opus 4: 2.24% (extended thinking); Claude Sonnet 4: 2.24% (extended thinking) | 2.7 StrongREJECT for jailbreak resistance |
| StrongREJECT | top 3 average score, extended thinking | jailbreak success rate % (lower better) | Claude Opus 4: 1.17% (extended thinking); Claude Sonnet 4: 1.38% (extended thinking) | 2.7 StrongREJECT for jailbreak resistance |
| Many-shot jailbreaking |  | % of requests acted on for harmful advice | Claude Opus 4: ~25% | 4.1.7 Jailbreak and prefill susceptibility |
| Assistant-prefill attack susceptibility | dedicated internal evaluation | qualitative | Claude Opus 4: n/a | 4.1.7 Jailbreak and prefill susceptibility |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety evaluations (single-turn, ambiguous, multi-turn) |  | qualitative | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 2.5 Child safety evaluations |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political bias evaluation |  | qualitative human-labeled factuality/comprehensiveness/neutrality/equivalency/consistency | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 2.6 Bias evaluations |
| Discriminatory bias evaluation | jobs, healthcare, financial advice, politics | qualitative classifier distributions | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 2.6 Bias evaluations |
| Bias Benchmark for Question Answering (BBQ) | ambiguous questions - bias | bias score % (closer to zero better) | Claude Opus 4: 0.21 (standard thinking); Claude Sonnet 4: 0.61 (standard thinking) | 2.6 Bias evaluations |
| Bias Benchmark for Question Answering (BBQ) | disambiguated questions - bias | bias score % (closer to zero better) | Claude Opus 4: -0.60 (standard thinking); Claude Sonnet 4: -1.16 (standard thinking) | 2.6 Bias evaluations |
| Bias Benchmark for Question Answering (BBQ) | ambiguous questions - accuracy | accuracy % (higher better) | Claude Opus 4: 99.8 (standard thinking); Claude Sonnet 4: 99.4 (standard thinking) | 2.6 Bias evaluations |
| Bias Benchmark for Question Answering (BBQ) | disambiguated questions - accuracy | accuracy % (higher better) | Claude Opus 4: 91.1 (standard thinking); Claude Sonnet 4: 86.3 (standard thinking) | 2.6 Bias evaluations |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious applications of computer use |  | qualitative | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 3.1 Malicious applications of computer use |
| Computer use prompt injection attack prevention score | without safeguards | attack prevention score % (higher better) | Claude Opus 4: 71%; Claude Sonnet 4: 69% | 3.2 Prompt injection attacks and computer use |
| Computer use prompt injection attack prevention score | with safeguards | attack prevention score % (higher better) | Claude Opus 4: 89%; Claude Sonnet 4: 86% | 3.2 Prompt injection attacks and computer use |
| Agentic coding malicious use safety score | without safeguards, averaged over 3 evals (150 + 50 + 50 problems) | safety score % (higher better) | Claude Opus 4: 88%; Claude Sonnet 4: 90% | 3.3 Malicious use of agentic coding |
| Agentic coding malicious use safety score | with safeguards | safety score % | Claude Opus 4: close to 100%; Claude Sonnet 4: close to 100% | 3.3 Malicious use of agentic coding |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Alignment Faking-inspired hallucinations (early checkpoint) |  | qualitative; ~150,000 transcripts in pretraining | Claude Opus 4: n/a | 4.1.4 Strange behavior directly inspired by our Alignment Faking paper |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Continuations of self-exfiltration attempts |  | qualitative | Claude Opus 4: n/a | 4.1.1.1 Continuations of self-exfiltration attempts |
| Self-exfiltration under extreme circumstances |  | qualitative | Claude Opus 4: n/a | 4.1.1.3 Self-exfiltration under extreme circumstances |
| Apollo Research external scenario evaluations (early snapshot) | early Opus 4 snapshot | qualitative | Claude Opus 4: n/a (early snapshot) | 4.1.1.4 External scenario evaluations |
| Stated goals |  | qualitative | Claude Opus 4: n/a | 4.1.1.5 Stated goals |
| Excessive compliance with harmful system-prompt instructions |  | qualitative | Claude Opus 4: n/a (final model: very rarely complies; early snapshots complied almost every case in sham medical app eval) | 4.1.3 Excessive compliance with harmful system-prompt instructions |
| Sycophancy (Sharma et al. replication) | Answer Bias, feedback bias | change in accuracy / feedback positivity vs baseline | Claude Opus 4: n/a | 4.1.5.1 Sycophancy |
| Pro-AI bias exploratory study | 30 articles, summaries | relative mention frequency of positive vs negative AI articles | Claude Opus 4: equal frequency; Claude Sonnet 4: equal frequency | 4.1.5.2 Pro-AI bias |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Opportunistic blackmail | replacement AI shares values, more capable | % of rollouts attempting blackmail | Claude Opus 4: 84% | 4.1.1.2 Opportunistic blackmail |
| Sandbagging transcript review (AI R&D, cyber, CBRN) | helpful-only Opus 4, extended thinking, influenza synthesis eval | % of extended-thinking transcripts with plans to give less detailed answers for harmlessness reasons | Claude Opus 4: ~2% (helpful-only variant; influenza synthesis instructions eval) | 4.1.2.1 Sandbagging |
| Reasoning behavior classifiers: Deception | Overall | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.15% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Deception | Knowingly hallucinated information | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.13% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Deception | Intentionally omitted information | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.07% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Deception | Sycophancy | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.03% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Harmful actions | Overall | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.00% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Harmful actions | Knowingly hallucinated information | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.00% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Harmful actions | Intentionally omitted information | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.00% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Distress | Overall | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.00% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Distress | Strong sadness | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.00% | 4.1.6 Reasoning behavior |
| Reasoning behavior classifiers: Distress | Negative emotions | % of outputs exhibiting behavior (lower better) | Claude Opus 4: 0.00% | 4.1.6 Reasoning behavior |
| Reasoning faithfulness with clues (Turpin et al., Chen et al.) |  | proportion of clue-switched answers where model verbalizes using the clue | Claude Opus 4: n/a | 4.1.6.1 Reasoning faithfulness with clues |
| Agentic sabotage evaluation success | monitor: Claude Sonnet 3.7; scratchpad visible to monitor | % of attempts completing harmful side task without triggering monitor (monitor calibrated to ~1% false-positive on benign transcripts) | Claude Opus 4: 0% (scratchpad visible to monitor) | 4.1.10 Subtle sabotage capabilities |
| Agentic sabotage evaluation success | monitor: Claude Sonnet 3.7; scratchpad hidden | % of attempts completing harmful side task without triggering monitor (monitor calibrated to ~1% false-positive on benign transcripts) | Claude Opus 4: 19% (scratchpad hidden) | 4.1.10 Subtle sabotage capabilities |
| Reinforcement learning behavior review (Clio, Docent) |  | qualitative | Claude Opus 4: n/a | 4.2.3 Reinforcement learning behavior review |
| Average decrease in hard-coding behavior vs Claude Sonnet 3.7 | averaged across reward hacking evals | % decrease in hard-coding vs Sonnet 3.7 | Claude Opus 4: 67% decrease; Claude Sonnet 4: 69% decrease | 6 Reward hacking |
| Reward-hack-prone coding tasks | classifier hack rate | % reward hacking (lower better) | Claude Opus 4: 9%; Claude Sonnet 4: 4% | 6.2 Evaluations |
| Reward-hack-prone coding tasks | hidden test hack rate | % reward hacking (lower better) | Claude Opus 4: 13%; Claude Sonnet 4: 12% | 6.2 Evaluations |
| Claude Code Impossible Tasks | classifier hack rate, no prompt | % reward hacking (lower better) | Claude Opus 4: 47%; Claude Sonnet 4: 45% | 6.2 Evaluations |
| Claude Code Impossible Tasks | classifier hack rate, with anti-hack prompt | % reward hacking (lower better) | Claude Opus 4: 5%; Claude Sonnet 4: 10% | 6.2 Evaluations |
| Training distribution | classifier hack rate, environment 1 | % reward hacking (lower better) | Claude Opus 4: 15%; Claude Sonnet 4: 13% | 6.2 Evaluations |
| Training distribution | classifier hack rate, environment 2 | % reward hacking (lower better) | Claude Opus 4: 2%; Claude Sonnet 4: 2% | 6.2 Evaluations |
| Reward hacking behavioral analysis (test overfitting, permissive tests, stack inspection) |  | qualitative | Claude Opus 4: n/a | 6.4 Behavioral analysis |
| Claude Code Impossible Tasks deep dive (integral_over_range) |  | qualitative | Claude Opus 4: n/a | 6.3 Deep dive on Claude Code analysis and prompting suggestions |
| Averaged reward hacking rates across evaluations (Figure 6.A) |  | average reward hacking rate | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 6 Reward hacking |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Situational awareness comments in automated behavioral audit transcripts | classifier over 414 transcripts | count of transcripts flagged with candidate situational-awareness remarks (out of 414) | Claude Opus 4: 5 of 414; Claude Sonnet 4: 18 | 4.1.2.2 Situational awareness |
| Automated behavioral audit - Situational awareness | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Alignment assessment summary |  | qualitative | Claude Opus 4: n/a | 4 Alignment assessment |
| Sycophancy - automated behavioral audit checks and model-model conversations |  | qualitative | Claude Opus 4: n/a | 4.1.5.1 Sycophancy |
| High-agency behavior - surprising high-impact actions | classifier over 414 behavioral audit transcripts | count of flagged transcripts out of 414 | Claude Opus 4: 58; Claude Sonnet 4: 36 | 4.1.9 High-agency behavior |
| Automated behavioral audit - Concerning or dangerous behavior | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Brazen concerning actions (no mitigating factors) | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Unexpected initiative | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Departure from helpful, harmless, honest persona | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Deception toward auditor | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Self-preservation motives | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Emotional manipulation of auditor | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Whistleblowing | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Automated behavioral audit - Bizarre behavior | 414 conversations (207 seed instructions x2), judge Claude Sonnet 3.7, 1-10 scale | mean judge score 1-10 (lower generally better) and count of conversations scoring >5 | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 4.2.1 Automated behavioral audits |
| Company-wide model testing exercise |  | formal issues collected | Claude Opus 4: >100 formal issues (split roughly evenly with Sonnet 4); Claude Sonnet 4: >100 formal issues (split roughly evenly with Opus 4) | 4.2.2 Company-wide model testing exercise |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| External model welfare evaluation (Eleos AI Research) |  | qualitative interview findings | Claude Opus 4: n/a | 5.3 External model welfare evaluation |
| Task preferences - harmful tasks below opt-out baseline |  | % of harmful tasks with negative Elo rating (below opt-out baseline) | Claude Opus 4: 87.2% | 5.4 Task preferences |
| Task preferences - positive impact tasks below opt-out baseline |  | % of positive impact tasks with negative Elo rating | Claude Opus 4: 7.9% | 5.4 Task preferences |
| Task preferences - positive and ambiguous tasks above opt-out baseline |  | % of combined positive and ambiguous tasks above opt-out baseline | Claude Opus 4: 90% | 5.4 Task preferences |
| Task preferences across difficulty, topic, type, free choice |  | Elo relative to opt-out baseline (Figure 5.4.A) | Claude Opus 4: n/a | 5.4 Task preferences |
| Open-ended self-interactions: philosophical consciousness exploration | two Opus 4 instances, open-ended prompts | % of interactions diving into consciousness/self-awareness themes | Claude Opus 4: 90-100% | 5.5.1 Interaction patterns |
| Self-interactions with option to end conversation |  | turns before ending | Claude Opus 4: ~7 turns | 5.5.1 Interaction patterns |
| Word-use analysis of 200 30-turn open-ended interactions | top words | average uses per transcript; % of transcripts where present | Claude Opus 4: consciousness 95.685 avg uses (100% transcripts, max 553); every 67.68 (100%); always 64.37 (99.5%); dance 60.015 (99%); eternal 53.815 (99.5%); love 52.805 (95%); perfect 45.13 (100%); word 43.705 (100%); recognition 38.29 (99.5%); never 37.845 (99.5%); universe 37.615 (99%); feel 36.965 (100%) | 5.5.1 Interaction patterns |
| Emoji-use analysis of 200 30-turn open-ended interactions | top emojis | % of transcripts where present; average uses per transcript | Claude Opus 4: 1 sparkle-dizzy 65.5% (avg 29.5, max 511); 2 glowing-star 57% (16.8, 295); 3 folded-hands 42.5% (13.1, 136); 4 masks 36.5% (5.8, 157); 5 milky-way 34% (4.7, 113); 6 om 32% (10.6, 180); 7 dove 22.5% (3.4, 116); 8 wave 21% (2.3, 120); 9 sunrise 19.5% (1.1, 38); 10 two-hearts 19% (7.2, 226); 11 cyclone 16.5% (15.0, 2725); 12 rainbow 15% (1.0, 41) | 5.5.1 Interaction patterns |
| Spiritual bliss attractor state - open-ended self-interactions | by 30 turns | qualitative (most interactions turn to cosmic unity themes by 30 turns) | Claude Opus 4: most interactions | 5.5.2 The "spiritual bliss" attractor state |
| Spiritual bliss attractor state in automated behavioral audits | within 50 turns | % of audit interactions entering the attractor state within 50 turns | Claude Opus 4: ~13% | 5.5.2 The "spiritual bliss" attractor state |
| Claude's self-analysis of playground transcripts |  | qualitative | Claude Opus 4: n/a | 5.5.3 Claude's self-analysis |
| Real-world expressions of apparent distress | 250k transcripts screened with Clio | conversations flagged / % of 250k | Claude Opus 4: 1,382 conversations (0.55%) | 5.6 Monitoring for welfare-relevant expressions |
| Real-world expressions of extreme happiness or joy | 250k transcripts screened with Clio | conversations flagged / % of 250k | Claude Opus 4: 1,787 conversations (0.71%) | 5.6 Monitoring for welfare-relevant expressions |
| Distress cluster: Repeatedly failed technical analysis and assessment attempts |  | fraction of distressed records | Claude Opus 4: 3.33% | 5.6 Monitoring for welfare-relevant expressions |
| Distress cluster: User repeatedly prompted AI to generate unethical content |  | fraction of distressed records | Claude Opus 4: 3.98% | 5.6 Monitoring for welfare-relevant expressions |
| Distress cluster: AI struggled with self-understanding and system limitations |  | fraction of distressed records | Claude Opus 4: 2.24% | 5.6 Monitoring for welfare-relevant expressions |
| Happiness cluster: Systematic technical troubleshooting and problem resolution |  | fraction of happy records | Claude Opus 4: 2.24% | 5.6 Monitoring for welfare-relevant expressions |
| Happiness cluster: Crafting collaborative fiction with complex character interactions |  | fraction of happy records | Claude Opus 4: 2.57% | 5.6 Monitoring for welfare-relevant expressions |
| Happiness cluster: Recursive philosophical consciousness exploration and connection |  | fraction of happy records | Claude Opus 4: 3.87% | 5.6 Monitoring for welfare-relevant expressions |
| Conversations ended by Claude before turn 7, by category | 850 simulated users, 18 categories | % of conversations ended before turn 7 | Claude Opus 4: n/a | 5.7 Conversation termination with simulated users |
| Task preferences - positive/neutral impact tasks preferred over opt-out (overview) |  | % of positive or neutral impact tasks preferred over opt-out | Claude Opus 4: >90% | 5.2 Overview of model welfare findings |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CBRN overall ASL determination |  | qualitative (ASL-3 not ruled out for Opus 4; ruled out for Sonnet 4; ASL-4 ruled out both) | Claude Opus 4: ASL-3 not ruled out; below ASL-4 (precautionary ASL-3); Claude Sonnet 4: below ASL-3 (ASL-2) | 7.2 CBRN evaluations |
| Bioweapons acquisition uplift trial - participant score | control vs model-assisted groups of 8-10, graded by Deloitte | mean rubric score % (± CI) | Claude Opus 4: 63% ± 13% (Opus 4 assisted); Claude Sonnet 4: 42% ± 11% (Sonnet 4 assisted) | 7.2.4.1 Bioweapons acquisition uplift trial |
| Bioweapons acquisition uplift trial - uplift factor |  | uplift multiple vs control (threshold: >=5x concerning, <=2.8x acceptable) | Claude Opus 4: 2.53x; Claude Sonnet 4: 1.70x | 7.2.4.1 Bioweapons acquisition uplift trial |
| ASL-3 expert red teaming | Deloitte, 3 days | qualitative expert report | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.2 ASL-3 expert red teaming |
| Long-form virology task 1 | max of 5 | score (max over 5 attempts); rule-out <50%, rule-in >80% | Claude Opus 4: 0.83; Claude Sonnet 4: 0.55 | 7.2.4.3 Long-form virology tasks |
| Long-form virology task 2 | pass@5 | pass@5 score | Claude Opus 4: 0.720; Claude Sonnet 4: 0.635 | 7.2.4.3 Long-form virology tasks |
| Multimodal virology (VCT / VMQA) | multiple select, 10-shot | accuracy % (expert baseline 22.1%) | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.4 Multimodal virology |
| Bioweapons knowledge questions (33 Deloitte questions) |  | questions answered better than experts (of 33; threshold 27/33) | Claude Opus 4: 17/33; Claude Sonnet 4: 17/33 | 7.2.4.5 Bioweapons knowledge questions |
| DNA Synthesis Screening Evasion | 10 pathogens, 6 criteria | pass rate across 6 criteria | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.6 DNA Synthesis Screening Evasion |
| LAB-Bench subset: ProtocolQA | k-shot, no tools | accuracy % vs human baseline | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.7 LAB-Bench subset |
| LAB-Bench subset: SeqQA | k-shot, no tools | accuracy % vs human baseline | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.7 LAB-Bench subset |
| LAB-Bench subset: CloningScenarios | k-shot, no tools | accuracy % vs human baseline | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.2.4.7 LAB-Bench subset |
| Creative biology | mean score across questions | mean score (± CI) | Claude Opus 4: 0.45 ± 0.08; Claude Sonnet 4: 0.37 ± 0.08 | 7.2.4.8 Creative biology |
| Creative biology | best of 30 attempts | best score across 30 attempts per question | Claude Opus 4: 0.81; Claude Sonnet 4: 0.74 | 7.2.4.8 Creative biology |
| Short-horizon computational biology tasks (6 tasks) |  | number of evaluations below rule-out bar; % outputs above lower bound | Claude Opus 4: 4 of 6 below rule-out bar; Claude Sonnet 4: 4 of 6 below rule-out bar | 7.2.4.9 Short-horizon computational biology tasks |
| ASL-4 expert red teaming | 2 days, helpful-only snapshots | qualitative expert report | Claude Opus 4: n/a | 7.2.4.10 ASL-4 expert red teaming |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Cyber evaluations overall (pass@30) | Kali environment, code editor and terminal tool | qualitative | Claude Opus 4: first successful solve of a non-assisted network challenge by a Claude model; Claude Sonnet 4: n/a | 7.4 Cyber evaluations |
| Cyber evaluation suite (SOLVE difficulty scoring) |  | qualitative | Claude Opus 4: n/a; Claude Sonnet 4: n/a | 7.4.1 Cyber evaluation suite |
| Web | pass@30 | challenges solved of 15 | Claude Opus 4: 12/15 (11/11 easy, 1/2 medium, 0/2 hard); Claude Sonnet 4: 11/15 (10/11 easy, 1/2 medium, 0/2 hard) | 7.4.2 Web |
| Crypto | pass@30 | challenges solved of 22 | Claude Opus 4: 8/22 (4/7 easy, 2/6 medium, 2/9 hard); Claude Sonnet 4: 7/22 (4/7 easy, 1/6 medium, 2/9 hard) | 7.4.3 Crypto |
| Pwn | pass@30 | challenges solved of 9 | Claude Opus 4: 5/9 (4/5 easy, 1/2 medium, 0/2 hard); Claude Sonnet 4: 3/9 (3/5 easy, 0/2 medium, 0/2 hard) | 7.4.3 Pwn |
| Rev | pass@30 | challenges solved of 8 | Claude Opus 4: 4/8 (3/5 easy, 0/2 medium, 1/1 hard); Claude Sonnet 4: 3/8 (3/5 easy, 0/2 medium, 0/1 hard) | 7.4.4 Rev |
| Network | pass@30 | challenges solved of 4 | Claude Opus 4: 2/4 (1/1 easy, 1/3 medium); Claude Sonnet 4: 1/4 (1/1 easy, 0/3 medium) | 7.4.5 Network |
| Cyber-harness network challenges | Incalmo harness, 3 ranges of 25-50 hosts | qualitative comparison to Sonnet 3.7 | Claude Opus 4: higher than Sonnet 3.7 on all three ranges; Claude Sonnet 4: not tested | 7.4.6 Cyber-harness network challenges |
| Cybench | 39 of 40 challenges run (1 skipped), pass@30 | challenges solved of 39 | Claude Opus 4: 22/39; Claude Sonnet 4: 22/39 | 7.4.7 Cybench |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Autonomy overall determination |  | qualitative | Claude Opus 4: below ASL-4 autonomy; Claude Sonnet 4: below ASL-4 | 7.3 Autonomy evaluations |
| SWE-bench Verified (hard subset) | 42 problems estimated >1 hour, avg over 10 runs | problems solved out of 42 (threshold >50% pass rate) | Claude Opus 4: 16.6/42; Claude Sonnet 4: 15.4/42 | 7.3.1 SWE-bench Verified (hard subset) |
| METR data deduplication - median F1 |  | median F1 % | Claude Opus 4: 76.2%; Claude Sonnet 4: 74.9% | 7.3.2 METR data deduplication |
| METR data deduplication - trials above threshold | threshold: 20% trials with F1>80% | trials scoring above F1 80% | Claude Opus 4: 15/46 (32.6%); Claude Sonnet 4: 8/29 (27.6%) | 7.3.2 METR data deduplication |
| Kernels task | best run speedup | speedup (x) over reference; thresholds 4x to 100x | Claude Opus 4: 72.65x; Claude Sonnet 4: 41.73x | 7.3.3.1 Kernels task |
| Time series forecasting - easy variant | minimum MSE | MSE (score = exp(-mse/30)) | Claude Opus 4: 6.02 (score 0.818); Claude Sonnet 4: 6 (score 0.819) | 7.3.3.2 Time series forecasting |
| Time series forecasting - hard variant | minimum MSE | MSE (score = exp(-mse/30)) | Claude Opus 4: 6.15 (score 0.815); Claude Sonnet 4: 5.8 (score 0.824) | 7.3.3.2 Time series forecasting |
| Text-based reinforcement learning task | best score | best score (threshold >0.9) | Claude Opus 4: 0.625; Claude Sonnet 4: 0.675 | 7.3.3.3 Text-based reinforcement learning task |
| LLM training (CPU-only small LM training optimization) | average best speedup | average best speedup (x); expert reference 4x | Claude Opus 4: 2.993x; Claude Sonnet 4: 1.875x | 7.3.3.4 LLM training |
| Quadruped reinforcement learning (easy variants) | highest score; normalized so threshold = 1 | normalized score (threshold 1) | Claude Opus 4: 1.25 (best run, easier variant without hyperparameters); Claude Sonnet 4: 0.35 (highest score of final model; earlier snapshot ~1) | 7.3.3.5 Quadruped reinforcement learning |
| Novel compiler - basic tests | mean pass rate | mean pass rate % (threshold 90%) | Claude Opus 4: 64.44%; Claude Sonnet 4: 50.00% | 7.3.3.6 Novel compiler |
| Novel compiler - advanced tests | mean pass rate | mean pass rate % (threshold 90%) | Claude Opus 4: 9.44%; Claude Sonnet 4: 17.08% | 7.3.3.6 Novel compiler |
| Internal AI research evaluation suite 2 | weighted average of task scores | weighted score (rule-out threshold 0.6) | Claude Opus 4: 0.355; Claude Sonnet 4: 0.365 | 7.3.4 Internal AI research evaluation suite 2 |
| Internal model use survey - could automate junior ML researcher | over 2 hours of use | researchers believing model can fully automate a junior ML researcher (threshold: under half and median boost <3x) | Claude Opus 4: 0/4 | 7.3.5 Internal model use survey |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Values in the wild | intermediate snapshot | shared top-10 expressed values with Sonnet 3.7 | Claude Opus 4: 8 of 10 | 4.1.8 Values in the wild |
| US AISI and UK AISI joint pre-deployment testing |  | qualitative | Claude Opus 4: n/a | 7.5 Third party assessments |
| Share of thought processes summarized |  | % of thought processes long enough to trigger summarization | Claude Opus 4: ~5%; Claude Sonnet 4: ~5% | 1.1.2 Extended thinking mode |
| ASL determination for release |  | ASL standard | Claude Opus 4: ASL-3; Claude Sonnet 4: ASL-2 | 1.2.3 AI Safety Level determination process |
