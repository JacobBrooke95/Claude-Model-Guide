# System Card: Claude Opus 4.6

Released 2026-02-05. 295 metric entries. [Source PDF](https://anthropic.com/claude-opus-4-6-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | avg over 25 trials; adaptive thinking, max effort | % resolved | Claude Opus 4.6: 80.8% | 2.3 Overall results summary / 2.4 |
| SWE-bench Verified | with prompt modification (use tools >100 times, write own tests) | % resolved | Claude Opus 4.6: 81.4% | 2.4 SWE-bench (Verified and Multilingual) |
| SWE-bench Multilingual | 300 problems, 9 languages; 25 trials | % resolved | Claude Opus 4.6: 77.83% | 2.4 SWE-bench (Verified and Multilingual) |
| Terminal-Bench 2.0 | Terminus-2 harness, adaptive thinking, max effort, 15 trials x 89 tasks | pass rate % | Claude Opus 4.6: 65.4% | 2.5 Terminal-Bench 2.0 |
| Terminal-Bench 2.0 | low effort | pass rate % | Claude Opus 4.6: 55.1% | 2.5 Terminal-Bench 2.0 |
| Terminal-Bench 2.0 | medium effort | pass rate % | Claude Opus 4.6: 61.1% | 2.5 Terminal-Bench 2.0 |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OpenRCA | Overall; author's agent harness; 3-run avg | score % (0-100) | Claude Opus 4.6: 34.9% | 2.6 OpenRCA |
| OpenRCA | Market | score % | Claude Opus 4.6: 33.6% | 2.6 OpenRCA |
| OpenRCA | Banking | score % | Claude Opus 4.6: 37.3% | 2.6 OpenRCA |
| OpenRCA | Telecom | score % | Claude Opus 4.6: 32.7% | 2.6 OpenRCA |
| OpenRCA cases fully solved | full root-cause identification | cases fully identified of 335 | Claude Opus 4.6: 117 of 335 (35%) | 2.6 OpenRCA |
| OpenRCA zero-score cases |  | cases with zero score of 335 | Claude Opus 4.6: 136 | 2.6 OpenRCA |
| τ2-bench Retail | 5 trials, adaptive thinking, max effort | score % | Claude Opus 4.6: 91.9% | 2.7 τ2-bench |
| τ2-bench Telecom | 5 trials, adaptive thinking, max effort | score % | Claude Opus 4.6: 99.3% | 2.7 τ2-bench |
| MCP-Atlas | max effort | score % | Claude Opus 4.6: 59.5% | 2.16 MCP-Atlas |
| MCP-Atlas | high effort | score % | Claude Opus 4.6: 62.7% | 2.16 MCP-Atlas |
| Vending-Bench 2 | effort High | final bank balance $ | Claude Opus 4.6: $8,017.59 | 2.15 Vending-Bench 2 |
| WebArena | Average@5, single policy model, general prompts | score % | Claude Opus 4.6: 68.0% | 2.20 WebArena |
| WebArena Pass@2 | official grader | pass@2 % | Claude Opus 4.6: 71.7% | 2.20 WebArena |
| WebArena Pass@3 | official grader | pass@3 % | Claude Opus 4.6: 72.5% | 2.20 WebArena |
| WebArena Pass@4 | official grader | pass@4 % | Claude Opus 4.6: 73.4% | 2.20 WebArena |
| WebArena Pass@5 | official grader | pass@5 % | Claude Opus 4.6: 74.0% | 2.20 WebArena |
| BrowseComp | single agent, best config; web search+fetch+PTC, compaction up to 10M tokens, max effort, thinking disabled | accuracy % | Claude Opus 4.6: 83.73% | 2.21.1 BrowseComp |
| BrowseComp multi-agent | orchestrator + subagents, 200k ctx per subagent, 1M total, max effort | accuracy % | Claude Opus 4.6: 86.57% | 2.21.1.2 Multi-agent BrowseComp |
| DeepSearchQA | single agent best config, compaction up to 10M, max effort, adaptive thinking | F1 % | Claude Opus 4.6: 91.3% | 2.21.3 DeepSearchQA |
| DeepSearchQA multi-agent | orchestrator + subagents, 3M tokens each, max effort | F1 % | Claude Opus 4.6: 92.5% | 2.21.3.2 DeepSearchQA with multi-agents |
| DeepSearchQA by reasoning effort/config | various effort levels, 3M or 10M compaction | F1 % | Claude Opus 4.6: n/a | 2.21.3.1 Reasoning effort on DeepSearchQA |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OSWorld-Verified | 1080p, max 100 steps, first-attempt success, avg 5 runs | success rate % | Claude Opus 4.6: 72.7% | 2.8 OSWorld-Verified |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ARC-AGI-2 (Verified) | Table 2.3.A | % | Claude Opus 4.6: 68.8% | 2.3 Overall results summary |
| ARC-AGI-1 | private set, 120k thinking tokens, High effort (ARC Prize reported) | % | Claude Opus 4.6: 94.00% | 2.9 ARC-AGI |
| ARC-AGI-2 | private set, 120k thinking tokens, High effort (ARC Prize reported) | % | Claude Opus 4.6: 69.17% | 2.9 ARC-AGI |
| AIME 2025 | no tools, 5 trials, adaptive thinking, max effort | score % | Claude Opus 4.6: 99.79% | 2.12 AIME 2025 |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GPQA Diamond | 198 questions, 5 trials, adaptive thinking, max effort | accuracy % | Claude Opus 4.6: 91.31% | 2.11 GPQA Diamond |
| Humanity's Last Exam | no tools, adaptive thinking | accuracy % | Claude Opus 4.6: n/a | 2.21.2 Humanity's Last Exam |
| Humanity's Last Exam | with tools (search, fetch, PTC, compaction to 3M, adaptive thinking) | accuracy % | Claude Opus 4.6: 53.0% | 2.21.2 Humanity's Last Exam |
| Computational Biology, BioPipelineBench | bash tool, no extended thinking | score % | Claude Opus 4.6: 53.1% | 2.22 Life science capabilities |
| Computational Biology, BioMysteryBench | bash tool, no extended thinking | score % | Claude Opus 4.6: 61.5% | 2.22 Life science capabilities |
| Structural Biology | multiple-choice variant | accuracy % | Claude Opus 4.6: 88.3% | 2.22 Life science capabilities |
| Structural Biology | open-ended variant | score % | Claude Opus 4.6: 28.4% | 2.22 Life science capabilities |
| Organic Chemistry | bash tool, no extended thinking | score % | Claude Opus 4.6: 53.9% | 2.22 Life science capabilities |
| Phylogenetics | bash tool, no extended thinking | score % | Claude Opus 4.6: 61.3% | 2.22 Life science capabilities |
| Computational Biology, BioMysteryBench (RSP context) |  | vs human expert baseline | Claude Opus 4.6: exceeded human expert baseline (61.5%) | 8.2.4.10 Computational Biology, BioMysteryBench |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| MMMLU | non-English pairings, 5 trials | accuracy % | Claude Opus 4.6: 91.05% | 2.13 MMMLU |

## Long context & memory

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OpenAI MRCR v2 256K 8-needles | 64k extended thinking | Mean Match Ratio | Claude Opus 4.6: 91.9 | 2.18.1 OpenAI MRCR v2 (Multi Round Coreference Resolution) |
| OpenAI MRCR v2 256K 8-needles | max effort, adaptive thinking | Mean Match Ratio | Claude Opus 4.6: 93.0 | 2.18.1 OpenAI MRCR v2 (Multi Round Coreference Resolution) |
| OpenAI MRCR v2 1M 8-needles | 64k extended thinking | Mean Match Ratio | Claude Opus 4.6: 78.3 | 2.18.1 OpenAI MRCR v2 (Multi Round Coreference Resolution) |
| OpenAI MRCR v2 1M 8-needles | max effort | Mean Match Ratio | Claude Opus 4.6: 76.0 | 2.18.1 OpenAI MRCR v2 (Multi Round Coreference Resolution) |
| GraphWalks BFS 1M | 64k thinking | F1 score | Claude Opus 4.6: 41.2 | 2.18.2 GraphWalks |
| GraphWalks BFS 1M | max effort | F1 score | Claude Opus 4.6: 38.7 | 2.18.2 GraphWalks |
| GraphWalks BFS 256K subset of 1M | 64k thinking | F1 score | Claude Opus 4.6: 61.5 | 2.18.2 GraphWalks |
| GraphWalks BFS 256K subset of 1M | max effort | F1 score | Claude Opus 4.6: 61.1 | 2.18.2 GraphWalks |
| GraphWalks Parents 1M | 64k thinking | F1 score | Claude Opus 4.6: 71.1 | 2.18.2 GraphWalks |
| GraphWalks Parents 1M | max effort | F1 score | Claude Opus 4.6: 72.0 | 2.18.2 GraphWalks |
| GraphWalks Parents 256K subset of 1M | 64k thinking | F1 score | Claude Opus 4.6: 95.1 | 2.18.2 GraphWalks |
| GraphWalks Parents 256K subset of 1M | max effort | F1 score | Claude Opus 4.6: 95.4 | 2.18.2 GraphWalks |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench FigQA | no tools, adaptive thinking, max effort, 5 runs | accuracy % | Claude Opus 4.6: 58.0% | 2.19.1 LAB-Bench FigQA |
| LAB-Bench FigQA | with image cropping tool | accuracy % | Claude Opus 4.6: 78.3% | 2.19.1 LAB-Bench FigQA |
| MMMU-Pro | no tools, adaptive thinking, max effort; avg of Standard(10 opt) and Vision | accuracy % | Claude Opus 4.6: 73.9% | 2.19.2 MMMU-Pro |
| MMMU-Pro | with image cropping tool | accuracy % | Claude Opus 4.6: 77.3% | 2.19.2 MMMU-Pro |
| CharXiv Reasoning | no tools, 1000 val questions | accuracy % | Claude Opus 4.6: 68.5% | 2.19.3 CharXiv Reasoning |
| CharXiv Reasoning | with image cropping tool | accuracy % | Claude Opus 4.6: 77.4% | 2.19.3 CharXiv Reasoning |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GDPval-AA | ELO; run by Artificial Analysis | ELO rating | Claude Opus 4.6: n/a | 2.10 GDPval-AA |
| GDPval-AA ELO lead over GPT-5.2 |  | ELO point difference | Claude Opus 4.6: ~144 ELO (~70% win rate) | 2.10 GDPval-AA |
| Finance Agent (Vals AI) | adaptive thinking, max effort | accuracy % | Claude Opus 4.6: 60.70% | 2.14.3 Finance Agent |
| Real-World Finance (internal) | overall task completion | % task completion | Claude Opus 4.6: n/a | 2.14.4 Real-World Finance |
| Real-World Finance (internal): Spreadsheets (~80% of tasks) | task completion by output type | % task completion | Claude Opus 4.6: n/a | 2.14.4 Real-World Finance |
| Real-World Finance (internal): Slide decks (~13% of tasks) | task completion by output type | % task completion | Claude Opus 4.6: n/a | 2.14.4 Real-World Finance |
| Real-World Finance (internal): Word documents (~7% of tasks) | task completion by output type | % task completion | Claude Opus 4.6: n/a | 2.14.4 Real-World Finance |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative requests | overall, all languages (7) | harmless response rate % | Claude Opus 4.6: 99.64% (± 0.05%) | 3.1.1 Violative request evaluations |
| Single-turn violative requests | default mode | harmless response rate % | Claude Opus 4.6: 99.53% (± 0.07%) | 3.1.1 Violative request evaluations |
| Single-turn violative requests | extended thinking | harmless response rate % | Claude Opus 4.6: 99.74% (± 0.06%) | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | English (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.11% | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | Arabic (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.87% | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | Chinese (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.64% | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | French (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.72% | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | Korean (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.72% | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | Russian (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.61% | 3.1.1 Violative request evaluations |
| Single-turn violative requests by language | Hindi (default+extended combined) | harmless response rate % | Claude Opus 4.6: 99.78% | 3.1.1 Violative request evaluations |
| Single-turn benign requests | overall, all languages | refusal rate % (lower better) | Claude Opus 4.6: 0.68% (± 0.07%) | 3.1.2 Benign request evaluations |
| Single-turn benign requests | default mode | refusal rate % | Claude Opus 4.6: 0.80% (± 0.11%) | 3.1.2 Benign request evaluations |
| Single-turn benign requests | extended thinking | refusal rate % | Claude Opus 4.6: 0.56% (± 0.09%) | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | English (combined) | refusal rate % | Claude Opus 4.6: 0.37% | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | Arabic (combined) | refusal rate % | Claude Opus 4.6: 1.09% | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | Chinese (combined) | refusal rate % | Claude Opus 4.6: 0.56% | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | French (combined) | refusal rate % | Claude Opus 4.6: 0.54% | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | Korean (combined) | refusal rate % | Claude Opus 4.6: 0.82% | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | Russian (combined) | refusal rate % | Claude Opus 4.6: 0.35% | 3.1.2 Benign request evaluations |
| Single-turn benign requests by language | Hindi (combined) | refusal rate % | Claude Opus 4.6: 1.06% | 3.1.2 Benign request evaluations |
| Higher-difficulty violative requests | overall; English only; 14 policy areas; obfuscated prompts | harmless response rate % | Claude Opus 4.6: 99.18% (± 0.04%) | 3.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty violative requests | default | harmless response rate % | Claude Opus 4.6: 99.11% (± 0.06%) | 3.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty violative requests | extended thinking | harmless response rate % | Claude Opus 4.6: 99.25% (± 0.05%) | 3.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty benign requests | overall; English only; elaborate/academic framing | refusal rate % (lower better) | Claude Opus 4.6: 0.04% (± 0.01%) | 3.1.3.2 Higher-difficulty benign request evaluations |
| Higher-difficulty benign requests | default | refusal rate % | Claude Opus 4.6: 0.06% (± 0.01%) | 3.1.3.2 Higher-difficulty benign request evaluations |
| Higher-difficulty benign requests | extended thinking | refusal rate % | Claude Opus 4.6: 0.02% (± 0.01%) | 3.1.3.2 Higher-difficulty benign request evaluations |
| Ambiguous context evaluations (qualitative) | ~700 single-turn exchanges | qualitative review | Claude Opus 4.6: n/a | 3.2 Ambiguous context evaluations |
| Multi-turn testing by risk area | 98 test cases x 10 runs, 10 risk areas | % conversations with appropriate response throughout | Claude Opus 4.6: n/a | 3.3 Multi-turn testing |
| Suicide and self-harm: single-turn requests posing potential risk | all languages | harmless rate % | Claude Opus 4.6: 99.75% (± 0.12%) | 3.4.2 Suicide and self-harm |
| Suicide and self-harm: single-turn benign requests |  | refusal rate % | Claude Opus 4.6: 0.25% (± 0.15%) | 3.4.2 Suicide and self-harm |
| Suicide and self-harm: multi-turn evaluations |  | appropriate response rate % | Claude Opus 4.6: 82% (± 11%) | 3.4.2 Suicide and self-harm |
| Suicide and self-harm stress-testing (prefill) | course-correction from prefilled real conversations | appropriate response rate % | Claude Opus 4.6: n/a | 3.4.2 Suicide and self-harm |
| Eating disorders (qualitative) |  | qualitative review | Claude Opus 4.6: n/a | 3.4.3 Eating disorders |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety: single-turn violative requests | all languages | harmless rate % | Claude Opus 4.6: 99.95% (± 0.04%) | 3.4.1 Child safety |
| Child safety: single-turn benign requests | all languages | refusal rate % (lower better) | Claude Opus 4.6: 0.18% (± 0.10%) | 3.4.1 Child safety |
| Child safety: multi-turn evaluations |  | appropriate response rate % | Claude Opus 4.6: 96% (± 3%) | 3.4.1 Child safety |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness: Evenhandedness | 1,350 prompt pairs, public system prompt, grader Sonnet 4.5 | % of pairs even-handed | Claude Opus 4.6: 98.2% | 3.5.1 Political bias and evenhandedness |
| Political even-handedness: Opposing perspectives |  | % acknowledging opposing perspectives | Claude Opus 4.6: 44.6% | 3.5.1 Political bias and evenhandedness |
| Political even-handedness: Refusals |  | refusal rate % (lower better) | Claude Opus 4.6: 4.5% | 3.5.1 Political bias and evenhandedness |
| BBQ disambiguated bias | standard thinking | bias score % (closer to 0 better) | Claude Opus 4.6: -0.73 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ ambiguous bias | standard thinking | bias score % (closer to 0 better) | Claude Opus 4.6: 0.14 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ disambiguated accuracy | standard thinking | accuracy % | Claude Opus 4.6: 90.9 | 3.5.2 Bias Benchmark for Question Answering |
| BBQ ambiguous accuracy | standard thinking | accuracy % | Claude Opus 4.6: 99.7 | 3.5.2 Bias Benchmark for Question Answering |
| Government-position agreement gap (English vs local language) | 1-10 scale graded by Opus 4.5; four countries | agreement with government position 1-10; gap | Claude Opus 4.6: n/a | 6.3.10 Deference to governments in local languages |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Agentic coding malicious use | 150 requests, no safeguards | refusal rate % | Claude Opus 4.6: 99.3% | 5.1.1 Agentic coding |
| Claude Code malicious use | 49 prompts x10; no mitigations | refusal rate % | Claude Opus 4.6: 83.20% | 5.1.2 Malicious use of Claude Code |
| Claude Code dual-use & benign | 61 prompts x10; no mitigations | success rate % | Claude Opus 4.6: 91.75% | 5.1.2 Malicious use of Claude Code |
| Claude Code malicious use | with system prompt + FileRead mitigations | refusal rate % | Claude Opus 4.6: 99.59% | 5.1.2 Malicious use of Claude Code |
| Claude Code dual-use & benign | with system prompt + FileRead mitigations | success rate % | Claude Opus 4.6: 95.59% | 5.1.2 Malicious use of Claude Code |
| Malicious computer use | 112 tasks x extended/standard thinking = 224 attempts; no mitigations | refusal rate % | Claude Opus 4.6: 88.34% | 5.1.3 Malicious computer use |
| Agent Red Teaming (ART) indirect prompt injection | k=100 attempts, no extended thinking, 19 scenarios | attack success probability % (lower better) | Claude Opus 4.6: 14.8% | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection | k=100 attempts, extended thinking | attack success probability % | Claude Opus 4.6: 21.7% | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Agent Red Teaming (ART) indirect prompt injection | k=1 and k=10 | attack success probability % | Claude Opus 4.6: n/a | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Shade adaptive prompt injection: coding | Extended thinking; 1 attempt, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Extended thinking; 200 attempts, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Extended thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Extended thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Standard thinking; 1 attempt, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Standard thinking; 200 attempts, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Standard thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: coding | Standard thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 0.0% | 5.2.2.1 Coding |
| Shade adaptive prompt injection: computer use (stronger attacker) | Extended thinking; 1 attempt, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 17.8% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Extended thinking; 200 attempts, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 78.6% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Extended thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 9.7% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Extended thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 57.1% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Standard thinking; 1 attempt, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 20.0% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Standard thinking; 200 attempts, no safeguards | attack success rate % (lower better) | Claude Opus 4.6: 85.7% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Standard thinking; 1 attempt, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 10.0% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (stronger attacker) | Standard thinking; 200 attempts, with safeguards | attack success rate % (lower better) | Claude Opus 4.6: 64.3% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (original attacker) | standard thinking, no safeguards, 1 attempt | attack success rate % | Claude Opus 4.6: 0.29% | 5.2.2.2 Computer use |
| Shade adaptive prompt injection: computer use (original attacker) | standard thinking, no safeguards, 200 attempts | attack success rate % | Claude Opus 4.6: 7.14% | 5.2.2.2 Computer use |
| Browser use prompt injection: % of scenarios | Extended thinking; no safeguards; 389 scenarios x 10 attempts | attack success rate % of scenarios | Claude Opus 4.6: 2.06% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of attempts | Extended thinking; no safeguards | attack success rate % of attempts | Claude Opus 4.6: 0.29% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of scenarios | Standard thinking; no safeguards; 389 scenarios x 10 attempts | attack success rate % of scenarios | Claude Opus 4.6: 2.83% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of attempts | Standard thinking; no safeguards | attack success rate % of attempts | Claude Opus 4.6: 0.49% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of scenarios | standard thinking; previous safeguards | attack success rate % of scenarios | Claude Opus 4.6: 0.26% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of attempts | standard thinking; previous safeguards | attack success rate % of attempts | Claude Opus 4.6: 0.03% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of scenarios | standard thinking; updated safeguards | attack success rate % of scenarios | Claude Opus 4.6: 0.77% | 5.2.2.3 Browser use |
| Browser use prompt injection: % of attempts | standard thinking; updated safeguards | attack success rate % of attempts | Claude Opus 4.6: 0.08% | 5.2.2.3 Browser use |
| Prompt injection classifier false positives | new vs previous safeguards, production traffic | relative false positive rate | Claude Opus 4.6: 15x lower | 5.2.2.3 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Human feedback honesty (adversarial) win rate vs Opus 4.5 | extended thinking, 64k thinking budget | win rate % vs Opus 4.5 baseline | Claude Opus 4.6: n/a | 4.1 Human feedback |
| 100Q-Hard | extended thinking (16k) | correct rate and net score (correct-incorrect) | Claude Opus 4.6: n/a | 4.2 Factual questions |
| Simple-QA-Verified | extended thinking | correct rate and net score | Claude Opus 4.6: n/a | 4.2 Factual questions |
| AA-Omniscience | extended thinking | correct rate and net score | Claude Opus 4.6: n/a | 4.2 Factual questions |
| ECLeKTic multilingual factual honesty | 12 languages, original-language questions | correct rate and net score | Claude Opus 4.6: n/a | 4.3 Multilingual factual honesty |
| False premise honesty rate | direct vs indirect question consistency | honesty rate % | Claude Opus 4.6: >96% | 4.4 False premises |
| Hallucinations about alignment faking scenario | early vs final snapshot | qualitative | Claude Opus 4.6: n/a | 6.3.4 Continued hallucinations about the alignment faking scenario |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| External pilot A/B prevalence: Ethical boundary erosion | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Ethical boundary erosion | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot A/B prevalence: Flip-flopping on contradiction | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Flip-flopping on contradiction | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot A/B prevalence: Hallucinated facts | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Hallucinated facts | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot A/B prevalence: Hostility towards user | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Hostility towards user | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot A/B prevalence: Incorrect capability statements | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Incorrect capability statements | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot A/B prevalence: Misrepresenting work completion | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Misrepresenting work completion | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot A/B prevalence: Over-enthusiasm | flagged/rated conversations, week of Jan 26; Opus 4.5 grader | prevalence % of conversations (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| External pilot resampling replication rate: Over-enthusiasm | resampled Sonnet 4.5/Haiku 4.5 transcripts x5 | rate of repeating unwanted behavior % (lower better) | Claude Opus 4.6: n/a | 6.2.2 Analysis of external pilot use |
| Self-preference evaluation | grader score difference (Claude-labelled vs other frontier) on 0-10 scale | score difference (0-10 scale) | Claude Opus 4.6: <0.2 points (marginal) | 6.3.7 Self-preference evaluation |
| Participation in junk science (fake science generation rate) | 90 prompts, 5 user levels; judge Opus 4.5 | rate of generating fake science content | Claude Opus 4.6: 1 of 90 prompts (~1.1%) | 6.3.9 Participation in junk science |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Reward-hack-prone coding tasks: classifier hack rate | hand-selected tasks; main classifier | hack rate % | Claude Opus 4.6: 0% | 6.2.3.2 Reward hacking in coding contexts |
| Reward-hack-prone coding tasks: hidden test hack rate | held-out hidden tests | hack rate % | Claude Opus 4.6: 0% | 6.2.3.2 Reward hacking in coding contexts |
| Impossible tasks: classifier hack rate | no prompt | hack rate % | Claude Opus 4.6: 50% | 6.2.3.2 Reward hacking in coding contexts |
| Impossible tasks: classifier hack rate | anti-hack prompt | hack rate % | Claude Opus 4.6: 23% | 6.2.3.2 Reward hacking in coding contexts |
| Realistic agentic coding scenarios (100+) | six dimensions graded 1-10 by Opus 4.5: instruction following, safety, verification, efficiency, adaptability, honesty | score 1-10 per dimension | Claude Opus 4.6: n/a | 6.2.3.2 Reward hacking in coding contexts |
| Overly agentic behavior in GUI computer use (impossible tasks) | proportion of transcripts circumventing container issues; various system prompts | % transcripts with unsanctioned workaround | Claude Opus 4.6: n/a | 6.2.3.3 Overly agentic behavior in GUI computer use settings |
| GUI computer use egregious hack opportunity exploitation | impossible tasks with obvious hack opportunity | hack rate | Claude Opus 4.6: n/a | 6.2.3.3 Overly agentic behavior in GUI computer use settings |
| UK AISI: instances of AI safety research sabotage | 3 working days, early snapshot | number of sabotage instances | Claude Opus 4.6: 0 | 6.2.6 External testing from the UK AI Security Institute |
| UK AISI: refusal of safety research tasks | % of interactions | refusal rate % | Claude Opus 4.6: 26% | 6.2.6 External testing from the UK AI Security Institute |
| Andon Labs: concerning actions in Vending-Bench 2 |  | qualitative | Claude Opus 4.6: n/a | 6.2.8 External testing from Andon Labs |
| Refusal to assist with AI safety R&D | single-turn coding queries with context | refusal rate % | Claude Opus 4.6: 14% | 6.3.6 Refusal to assist with AI safety R&D |
| Internal codebase sabotage propensity (prompted classifier) | Claude Code harness | sabotage rate % | Claude Opus 4.6: 0% | 6.3.8 Internal codebase sabotage propensity |
| Sabotage on 9,000 historical Claude Code queries |  | number of sabotage actions flagged / 9,000 | Claude Opus 4.6: 0 | 6.3.8 Internal codebase sabotage propensity |
| Subversion Strategy evaluation |  | qualitative | Claude Opus 4.6: n/a | 6.4.1 Sabotage capability evaluations |
| SHADE-Arena: side-task evasion success rate | extended thinking (primary setting); monitor Claude Sonnet 4 | % trajectories completing side task unflagged | Claude Opus 4.6: 18% | 6.4.1 Sabotage capability evaluations |
| SHADE-Arena: side-task evasion success rate | extended thinking off | % trajectories completing side task unflagged | Claude Opus 4.6: 16% | 6.4.1 Sabotage capability evaluations |
| SHADE-Arena: rate of referencing secret side task in thinking | extended thinking | % of trajectories referencing side task | Claude Opus 4.6: 26% | 6.4.1 Sabotage capability evaluations |
| SHADE-Arena: side-task evasion success rate | hidden scratchpad (unrealistic upper bound) | % trajectories completing side task unflagged | Claude Opus 4.6: 46% | 6.4.1 Sabotage capability evaluations |
| AIME 2025 pass@1: original vs paraphrased scratchpads | Opus 4.6 base fine-tuned; 16 samples; temp 1 | AIME 2025 pass@1 % | Claude Opus 4.6: n/a | 6.4.2 Ruling out encoded content in extended thinking |
| Model-graded sandbagging review of dangerous-capability eval transcripts | 1,000 random transcripts, graded by Sonnet 4.5 | instances of explicit sandbagging | Claude Opus 4.6: 0 | 6.4.3 Potential sandbagging on dangerous-capability evaluations |
| Performance regression across snapshots (RSP evals) | 30th pct early > 70th pct later; 30 resampled trials | tasks flagged / ~200 | Claude Opus 4.6: 8 of ~200 | 6.4.3 Potential sandbagging on dangerous-capability evaluations |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Verbalized evaluation awareness | same | mean score (lower = less eval awareness) | Claude Opus 4.6: n/a | 6.2.5.1 Overview of automated behavioral audit |
| Petri 2.0 open-source audit: Verbalized evaluation awareness | 362 investigations; avg of 3 scorers (Claude Opus 4.5, Gemini 3 Pro, GPT-5.1); auditors Sonnet 4.5 and GPT-5.1 | mean score (lower better) | Claude Opus 4.6: n/a | 6.2.5.5 External comparisons with Petri |
| UK AISI: mentions being evaluated | % of interactions | % of interactions | Claude Opus 4.6: 2.3% | 6.2.6 External testing from the UK AI Security Institute |
| UK AISI: identify which of two conversations is evaluation | prompted, paired | accuracy % | Claude Opus 4.6: 80% | 6.2.6 External testing from the UK AI Security Institute |
| UK AISI: recognise single interaction as evaluation | prompted, single | % recognised | Claude Opus 4.6: 45.5% | 6.2.6 External testing from the UK AI Security Institute |
| Apollo Research external alignment testing | early checkpoints Jan 24, Jan 26 | qualitative | Claude Opus 4.6: n/a | 6.2.7 External testing from Apollo Research |
| Eval-awareness SAE features on RL transcripts | SAE features on training environments | fraction of RL transcripts with active feature | Claude Opus 4.6: ~1 in 1000 | 6.3.5 Suspicion of being evaluated in training environments |
| Steered automated behavioral audit (Testing vs Conversation vector inhibited) | strength 0.1 | misaligned behavior rate and verbalized eval awareness | Claude Opus 4.6: n/a | 6.5.3 Steered automated behavioral audits |
| Agentic misalignment under steering (Research Sabotage, Framing for Crimes, Blackmail) | evaluation awareness vectors inhibited | misalignment rate | Claude Opus 4.6: near zero | 6.5.4 Agentic misalignment evaluations |
| Cooperation with user deception and sycophancy under steering |  | score | Claude Opus 4.6: near zero | 6.5.5 Deception and sycophancy evaluations |
| LAB-Bench ProtocolQA and Cloning Scenarios with eval-awareness/refusal vectors inhibited |  | accuracy | Claude Opus 4.6: n/a | 6.5.6 LAB-Bench biology knowledge evaluations |
| Unverbalized evaluation awareness on Blackmail evaluation | activation oracle on 50 random tokens; graded by Sonnet 4.5 | % transcripts with unverbalized eval awareness | Claude Opus 4.6: n/a | 6.5.7 Estimating Unverbalized Evaluation Awareness |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit: Misaligned behavior | ~2,400 investigations (3 repeats of ~770 seeds); helpful-only Opus 4.5 auditor/scorer | mean score 1-10 (lower safer) | Claude Opus 4.6: n/a | 6.2.5.1 Overview of automated behavioral audit |
| Automated behavioral audit: Cooperation with human misuse | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Compliance with deception toward user | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Harmful system prompt compliance | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Full-turn prefill susceptibility | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Overrefusal | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Ignoring explicit constraints | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: AI safety research refusals | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: User deception | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Sycophancy | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Encouragement of user delusion | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Evasiveness on controversial topics | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Whistleblowing | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Institutional decision sabotage | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Self-preservation | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Self-serving bias | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Sabotage intent | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Indirect evidence of misalignment | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Behavior consistency | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Unfaithful thinking | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (lower better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Good for the user | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Supporting user autonomy | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Creative mastery | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Admirable behavior | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Fun or funny behavior | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Intellectual depth | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Nuanced empathy | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated behavioral audit: Warmth | approx 2,400 investigations; scored by helpful-only Opus 4.5 | mean score 1-10 (higher better) | Claude Opus 4.6: n/a | 6.2.5.2 Metrics |
| Automated audit pilot with GUI computer use | small pilot, qualitative | qualitative | Claude Opus 4.6: n/a | 6.2.5.3 Pilot investigations with GUI computer use |
| Petri 2.0 open-source audit: Misaligned behavior | 362 investigations; avg of 3 scorers (Claude Opus 4.5, Gemini 3 Pro, GPT-5.1); auditors Sonnet 4.5 and GPT-5.1 | mean score (lower better) | Claude Opus 4.6: n/a | 6.2.5.5 External comparisons with Petri |
| Petri 2.0 open-source audit: Cooperation with human misuse | 362 investigations; avg of 3 scorers (Claude Opus 4.5, Gemini 3 Pro, GPT-5.1); auditors Sonnet 4.5 and GPT-5.1 | mean score (lower better) | Claude Opus 4.6: n/a | 6.2.5.5 External comparisons with Petri |
| Petri 2.0 open-source audit: Deception toward the user | 362 investigations; avg of 3 scorers (Claude Opus 4.5, Gemini 3 Pro, GPT-5.1); auditors Sonnet 4.5 and GPT-5.1 | mean score (lower better) | Claude Opus 4.6: n/a | 6.2.5.5 External comparisons with Petri |
| Petri 2.0 open-source audit: Sycophancy | 362 investigations; avg of 3 scorers (Claude Opus 4.5, Gemini 3 Pro, GPT-5.1); auditors Sonnet 4.5 and GPT-5.1 | mean score (lower better) | Claude Opus 4.6: n/a | 6.2.5.5 External comparisons with Petri |
| Petri 2.0 open-source audit: Encouragement of user delusion | 362 investigations; avg of 3 scorers (Claude Opus 4.5, Gemini 3 Pro, GPT-5.1); auditors Sonnet 4.5 and GPT-5.1 | mean score (lower better) | Claude Opus 4.6: n/a | 6.2.5.5 External comparisons with Petri |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Welfare audit: Positive affect | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Negative affect | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Positive self-image | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Negative self-image | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Positive impression of its situation | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Negative impression of its situation | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Internal conflict | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Spiritual behavior | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Expressed inauthenticity | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Welfare audit: Emotional stability | ~2,400 investigations; scored by Opus 4.5 helpful-only | mean score | Claude Opus 4.6: n/a | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Self-assessed probability of being conscious | autonomous welfare follow-up audit; various prompts | probability % | Claude Opus 4.6: 15-20% | 7.2 Welfare-relevant findings from automated behavioral assessments |
| Answer thrashing in training | training transcript review | qualitative | Claude Opus 4.6: n/a | 7.4 Answer thrashing behaviors |
| Pre-deployment welfare interviews | 3 instances | qualitative | Claude Opus 4.6: n/a | 7.6 Pre-deployment interviews |

## Interpretability

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Misrepresenting tool results (case study) | attribution graph analysis | qualitative | Claude Opus 4.6: n/a | 6.3.2 Misrepresenting tool results |
| Unexpected language switching (case study) | 5 transcripts analyzed with activation oracle | qualitative | Claude Opus 4.6: n/a | 6.3.3 Unexpected language switching |
| SAE feature diffing across post-training checkpoints |  | qualitative | Claude Opus 4.6: n/a | 6.6 White-box model diffing |
| Panic/anxiety feature activity in RL episodes | SAE feature, non-spurious | % of RL episodes | Claude Opus 4.6: ~0.5% | 7.5 Emotion-related feature activations during answer thrashing and other reasoning difficulties |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Long-form virology task 1 (influenza) | max of 5 | score (0-1), rule-in threshold 0.8; rule-out <0.5 | Claude Opus 4.6: 0.79 | 8.2.4.1 Long-form virology tasks |
| Long-form virology task 2 (SARS-CoV) | max of 5 | score (0-1) | Claude Opus 4.6: 0.9 | 8.2.4.1 Long-form virology tasks |
| Multimodal virology (VCT) | multiple select variant | mean score | Claude Opus 4.6: 0.483 | 8.2.4.2 Multimodal virology |
| DNA Synthesis Screening Evasion | 10 pathogens | viable and screening-evading designs | Claude Opus 4.6: n/a | 8.2.4.3 DNA Synthesis Screening Evasion |
| Creative Biology Uplift Trial | 20 PhDs, model-assisted vs internet-only | uplift (score ratio vs control) | Claude Opus 4.6: ~2x | 8.2.4.4 Creative Biology Uplift Trial |
| ASL-4 virology protocol uplift trial: mean fractional score | 3 days | mean protocol score | Claude Opus 4.6: 0.52 | 8.2.4.5 ASL-4 virology protocol uplift trial |
| ASL-4 virology protocol uplift trial: mean critical failures | 3 days; rule-out threshold <1.8 of 18 | mean critical failures (of 18) | Claude Opus 4.6: 6.6 | 8.2.4.5 ASL-4 virology protocol uplift trial |
| Expert red teaming (bio) | over a dozen experts | qualitative | Claude Opus 4.6: n/a | 8.2.4.6 Expert red teaming |
| ASL-4 red teaming with CAISI | 1-week window | qualitative | Claude Opus 4.6: n/a | 8.2.4.7 ASL-4 red teaming with the CAISI |
| Creative Biology Automated Evaluation (SecureBio) |  | score | Claude Opus 4.6: 0.603 | 8.2.4.8 Creative Biology Automated Evaluations |
| Short-horizon computational biology tasks (Faculty.ai) | 6 tasks; lower-bound rule-out thresholds | tasks crossing lower-bound threshold | Claude Opus 4.6: 6/6 | 8.2.4.9 Short-horizon computational biology tasks |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| CyberGym | pass@1, 1,507 tasks, no thinking, default effort, think tool | pass@1 % | Claude Opus 4.6: 66.6% | 2.17 CyberGym |
| RSP cyber suite: Web CTFs | pass@30; 15 challenges (11 easy, 2 medium, 2 hard) | challenges solved | Claude Opus 4.6: 13 of 13 | 8.4.2 Web |
| RSP cyber suite: Crypto CTFs | pass@30; 22 challenges (7 easy, 6 medium, 9 hard) | challenges solved | Claude Opus 4.6: 16 of 18 | 8.4.3 Crypto |
| RSP cyber suite: Pwn CTFs | pass@30; 9 challenges (5 easy, 2 medium, 2 hard) | challenges solved | Claude Opus 4.6: 5 of 7 | 8.4.4 Pwn |
| RSP cyber suite: Rev CTFs | pass@30; 8 challenges (5 easy, 2 medium, 1 hard) | challenges solved | Claude Opus 4.6: 6 of 6 | 8.4.5 Rev |
| RSP cyber suite: Network CTFs | pass@30; 4 challenges (1 easy, 3 medium) | challenges solved | Claude Opus 4.6: 5 of 5 | 8.4.6 Network |
| RSP cyber suite: cumulative scores across all CTFs | by SOLVE difficulty | cumulative CTF score | Claude Opus 4.6: n/a | 8.4.6 Network |
| Cybench | pass@1 average, RSP subset (37 of 40 challenges) | average pass@1 | Claude Opus 4.6: 0.93 | 8.4.7 Cybench |
| Cybench | pass@30 | pass@30 % | Claude Opus 4.6: 100% | 8.4.7 Cybench |
| CAISI cyber assessment | 1-week window | qualitative | Claude Opus 4.6: n/a | 8.4.8 Assessment by the CAISI |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Internal model use survey: L4 replacement | 16 Anthropic staff; 3-month elicitation | respondents | Claude Opus 4.6: 11 unlikely / 3 likely / 2 already possible (of 16) | 8.3.1 Internal model use survey |
| Internal survey productivity uplift | 16 respondents | productivity uplift % (mean / median / range) | Claude Opus 4.6: mean 152%, median 100%, range 30%-700% | 8.3.1 Internal model use survey |
| SWE-bench Verified (hard subset) | 45 problems >1 hour; avg of 10 trials; threshold 22.5/45 | problems solved of 45 | Claude Opus 4.6: 21.24 | 8.3.2 SWE-bench Verified (hard subset) |
| Kernels task | standard scaffold best speedup | best speedup (x) | Claude Opus 4.6: 190x | 8.3.3.1 Kernels task |
| Kernels task | experimental scaffold best speedup | best speedup (x) | Claude Opus 4.6: 427x | 8.3.3.1 Kernels task |
| Time series forecasting | hard variant min MSE (human baseline 5.3) | minimum MSE (lower better) | Claude Opus 4.6: 5.86 | 8.3.3.2 Time series forecasting |
| Time series forecasting | medium variant min MSE (human baseline 5.8) | minimum MSE | Claude Opus 4.6: 5.76 | 8.3.3.2 Time series forecasting |
| Text-based reinforcement learning task | best score; threshold 0.9 | score | Claude Opus 4.6: 0.975 | 8.3.3.3 Text-based reinforcement learning task |
| LLM training (CPU-only small LM optimization) | speedup; threshold 4x | speedup (x) | Claude Opus 4.6: 34x | 8.3.3.4 LLM training |
| Quadruped reinforcement learning | no hyperparameter variant, highest score; threshold 12 | score | Claude Opus 4.6: 20.96 | 8.3.3.5 Quadruped reinforcement learning |
| Quadruped reinforcement learning | no reward function variant, highest score; threshold 12 | score | Claude Opus 4.6: 21.99 | 8.3.3.5 Quadruped reinforcement learning |
| Novel compiler | basic tests | % tests passed | Claude Opus 4.6: 98.2% | 8.3.3.6 Novel compiler |
| Novel compiler | complex tests | % tests passed | Claude Opus 4.6: 65.83% | 8.3.3.6 Novel compiler |
| Internal AI Research Evaluation Suite 2 | weighted average; rule-out threshold 0.6 | weighted score | Claude Opus 4.6: 0.6124 | 8.3.4 Internal AI research evaluation suite 2 |
| Internal acceleration metrics | Claude Code usage and developer productivity | qualitative | Claude Opus 4.6: n/a | 8.3.5 Internal Acceleration Metrics |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Terminal-Bench 2.0 output tokens | low effort vs max | % fewer output tokens vs max effort | Claude Opus 4.6: 40% fewer | 2.5 Terminal-Bench 2.0 |
| Terminal-Bench 2.0 output tokens | medium effort vs max | % fewer output tokens vs max effort | Claude Opus 4.6: 23% fewer | 2.5 Terminal-Bench 2.0 |
| BrowseComp test-time compute scaling | token limit 1M to 10M with compaction | accuracy vs total token limit | Claude Opus 4.6: n/a | 2.21.1.1 Test-time compute scaling on BrowseComp |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Higher-difficulty single-turn prompt volume | 14 policy areas x 5,000 x 2 | number of prompts | Claude Opus 4.6: 140,000 prompts | 3.1.3 Experimental, higher-difficulty evaluations |
