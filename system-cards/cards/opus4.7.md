# System Card: Claude Opus 4.7

Released 2026-04-16. 301 metric entries. [Source PDF](https://anthropic.com/claude-opus-4-7-system-card) · [Back to index](../README.md)

## Coding

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| SWE-bench Verified | 500 problems; adaptive thinking, max effort, avg of 5 trials | resolved % (avg of 5 trials) | Claude Opus 4.7: 87.6% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Pro | public set; adaptive thinking, max effort, avg of 5 trials | resolved % | Claude Opus 4.7: 64.3% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multilingual | 300 problems across 9 languages; adaptive thinking, max effort, avg of 5 trials | resolved % | Claude Opus 4.7: 80.5% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| SWE-bench Multimodal | internal harness (Appendix 9.3); adaptive thinking, max effort, avg of 5 trials | resolved % | Claude Opus 4.7: 34.5% | 8.2 SWE-bench Verified, Pro, Multilingual, and Multimodal |
| Terminal-Bench 2.0 | Terminus-2 harness, thinking disabled, 89 tasks x 5 attempts (445 trials), production API endpoint | mean reward % | Claude Opus 4.7: 69.4% (thinking disabled) | 8.3 Terminal-Bench 2.0 |

## Agentic & tool use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp | web search/fetch/PTC/code; thinking off, max effort, 10M token limit, context compaction at 200k | accuracy % | Claude Opus 4.7: 79.3% (10M tokens) | 8.8.2 BrowseComp |
| DeepSearchQA F1 | 900 prompts; web search/fetch/PTC; compaction at 200k; up to 10M tokens | F1 % | Claude Opus 4.7: 89.1% (± 1.8%) | 8.8.3 DeepSearchQA |
| DeepSearchQA fully correct |  | % of prompts fully correct | Claude Opus 4.7: 80.7% (± 2.6%) | 8.8.3 DeepSearchQA |
| DeepSearchQA fully incorrect |  | % of prompts fully incorrect | Claude Opus 4.7: 7.0% (± 1.7%) | 8.8.3 DeepSearchQA |
| DeepSearchQA correct with excessive answers |  | % of prompts | Claude Opus 4.7: 3.9% (± 1.3%) | 8.8.3 DeepSearchQA |
| DeepSearchQA F1 vs reasoning effort | compaction up to 3M tokens | F1 | Claude Opus 4.7: n/a | 8.8.3 DeepSearchQA |
| DRACO | 100 tasks; adaptive thinking max effort; 1M token limit; compaction at 200k; Opus 4.6 judge, 5 grading runs | normalized score % | Claude Opus 4.7: 77.7% | 8.8.4 DRACO |
| DRACO pass rate by rubric axis | factual accuracy, breadth and depth, presentation, citation quality | pass rate % per axis | Claude Opus 4.7: n/a | 8.8.4 DRACO |
| MCP-Atlas | adaptive thinking max effort; refreshed Scale harness; leaderboard config 20 turns / 10-25 tools | pass rate % | Claude Opus 4.7: 77.3% (leaderboard config) | 8.10.3 MCP Atlas |
| MCP-Atlas extended config | 256 turns / 100 tools | pass rate % | Claude Opus 4.7: 79.5% (max effort); Claude Opus 4.7: 79.7% (high effort) | 8.10.3 MCP Atlas |
| Vending-Bench 2 | simulated 1-year vending business, $500 start; Max effort | final balance ($) | Claude Opus 4.7: $10,937 (Max effort); Claude Opus 4.7: $7,971 (High effort) | 8.10.4 VendingBench |

## Computer use

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| ScreenSpot-Pro - no tools | 1,581 tasks; adaptive thinking max effort; avg of 5 runs | accuracy % | Claude Opus 4.7: 79.5% (new resolution); Claude Opus 4.7: 69.0% (old resolution) | 8.9.3 ScreenSpot-Pro |
| ScreenSpot-Pro - with Python tools | same | accuracy % | Claude Opus 4.7: 87.6% (new resolution); Claude Opus 4.7: 85.9% (old resolution) | 8.9.3 ScreenSpot-Pro |
| OSWorld (Verified) | 1080p, max 100 action steps, first-attempt success, avg of 5 runs | success rate % | Claude Opus 4.7: 78.0% | 8.9.4 OSWorld |

## Reasoning & math

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| USAMO 2026 | medium effort, batch API, 300k token limit; MathArena grading with 3-judge panel (min score); avg of 10 attempts per problem | score % | Claude Opus 4.7: 69.3% | 8.6 USAMO 2026 |
| ARC-AGI-1 | High effort | score % | Claude Opus 4.7: 93.5% (High effort); Claude Opus 4.7: 92.0% (Max effort (summary table)) | 8.11 ARC-AGI |
| ARC-AGI-2 | Max effort | score % | Claude Opus 4.7: 75.83% (Max effort) | 8.11 ARC-AGI |
| ARC-AGI-2 across effort levels | various effort | score % | Claude Opus 4.7: n/a | 8.11 ARC-AGI |

## Knowledge & science

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GPQA Diamond | 198 questions; avg of 10 trials; adaptive thinking max effort | accuracy % | Claude Opus 4.7: 94.2% | 8.4 GPQA Diamond |
| Humanity's Last Exam - no tools | 2,500 questions; thinking auto; max effort; 1M token cap; Opus 4.6 grader | accuracy % | Claude Opus 4.7: 46.9% (no tools) | 8.8.1 Humanity's Last Exam |
| Humanity's Last Exam - with tools | web search, web fetch, programmatic tool calling, code execution; blocklist; 1M cap | accuracy % | Claude Opus 4.7: 54.7% (with tools) | 8.8.1 Humanity's Last Exam |
| Humanity's Last Exam - with tools at varying effort | effort levels | accuracy % | Claude Opus 4.7: n/a | 8.8.1 Humanity's Last Exam |
| BioPipelineBench Verified | internal; bash tool, no extended thinking | score % | Claude Opus 4.7: 83.6% | 8.13.1.1 BioPipelineBench Verified |
| BioMysteryBench - Verified subset | internal; bash tool, no extended thinking | score % | Claude Opus 4.7: 78.9% (Verified) | 8.13.1.2 BioMysteryBench Verified |
| BioMysteryBench - Hard subset | unsolved by humans with objective ground truth | score % | Claude Opus 4.7: 20.9% (Hard) | 8.13.1.2 BioMysteryBench Verified |
| Structural biology - multiple choice | internal | accuracy % | Claude Opus 4.7: 98.3% | 8.13.3 Structural biology |
| Structural biology - open-ended | internal | score % | Claude Opus 4.7: 74.0% | 8.13.3 Structural biology |
| Organic chemistry | internal | score % | Claude Opus 4.7: 77.2% | 8.13.4 Organic chemistry |
| Phylogenetics | internal | score % | Claude Opus 4.7: 79.6% | 8.13.5 Phylogenetics |
| Protocol troubleshooting | internal; bash and web search | score % | Claude Opus 4.7: 51.8% | 8.13.6 Protocol troubleshooting |

## Multilingual

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| MMMLU | 14 non-English languages; avg of 3 trials; adaptive thinking max effort | accuracy % | Claude Opus 4.7: 91.5% | 8.5 MMMLU |
| GMMLU - English | structured JSON output; adaptive thinking | accuracy % | Claude Opus 4.7: 93.4% | 8.12.1 GMMLU results |
| GMMLU - high-resource average | 15 languages | accuracy % | Claude Opus 4.7: 91.5% (gap -1.9%) | 8.12.1 GMMLU results |
| GMMLU - mid-resource average | 14 languages | accuracy % | Claude Opus 4.7: 91.1% (gap -2.3%) | 8.12.1 GMMLU results |
| GMMLU - low-resource average | 13 languages | accuracy % | Claude Opus 4.7: 86.2% (gap -7.3%) | 8.12.1 GMMLU results |
| GMMLU - individual low-resource languages |  | accuracy % | Claude Opus 4.7: 81.3% (Igbo); Claude Opus 4.7: 82.9% (Yoruba); Claude Opus 4.7: 84.1% (Somali); Claude Opus 4.7: 84.8% (Malagasy); Claude Opus 4.7: 84.9% (Chichewa); Claude Opus 4.7: 85.7% (Hausa); Claude Opus 4.7: 85.8% (Shona); Claude Opus 4.7: 87.9% (Kyrgyz); Claude Opus 4.7: 88.2% (Amharic); Claude Opus 4.7: 88.6% (Swahili); Claude Opus 4.7: 89.5% (Sinhala); Claude Opus 4.7: 90.1% (Nepali) | 8.12.1 GMMLU results |
| GMMLU - average over all languages | 42 languages incl. English | accuracy % | Claude Opus 4.7: 89.9% | 8.12.1 GMMLU results |
| GMMLU - average gap to English | excluding English | percentage points | Claude Opus 4.7: -3.6% | 8.12.1 GMMLU results |
| GMMLU - worst gap to English |  | percentage points | Claude Opus 4.7: -12.1% (Igbo) | 8.12.1 GMMLU results |
| MILU - English | structured JSON output; adaptive thinking | accuracy % | Claude Opus 4.7: 92.4% | 8.12.2 MILU results |
| MILU - per Indic language | 10 Indic languages | accuracy % | Claude Opus 4.7: 87.3% (Malayalam); Claude Opus 4.7: 87.7% (Punjabi); Claude Opus 4.7: 87.8% (Odia); Claude Opus 4.7: 89.0% (Tamil); Claude Opus 4.7: 89.5% (Marathi); Claude Opus 4.7: 89.7% (Gujarati); Claude Opus 4.7: 90.1% (Telugu); Claude Opus 4.7: 91.3% (Bengali); Claude Opus 4.7: 91.6% (Kannada); Claude Opus 4.7: 93.0% (Hindi) | 8.12.2 MILU results |
| MILU - average over all languages | 10 Indic languages plus English | accuracy % | Claude Opus 4.7: 89.9% | 8.12.2 MILU results |
| MILU - average gap to English | excluding English | percentage points | Claude Opus 4.7: -2.7% | 8.12.2 MILU results |
| MILU - worst gap to English |  | percentage points | Claude Opus 4.7: -5.1% (Malayalam) | 8.12.2 MILU results |
| INCLUDE - per language | 44 languages; regional exam questions; adaptive thinking | accuracy % | Claude Opus 4.7: 69.8% (German); Claude Opus 4.7: 70.2% (Turkish); Claude Opus 4.7: 74.5% (Urdu); Claude Opus 4.7: 79.1% (Uzbek); Claude Opus 4.7: 79.5% (Telugu); Claude Opus 4.7: 80.1% (Nepali); Claude Opus 4.7: 81.9% (Basque); Claude Opus 4.7: 82.2% (Azerbaijani); Claude Opus 4.7: 82.5% (Hindi); Claude Opus 4.7: 83.7% (Russian); Claude Opus 4.7: 84.4% (Malayalam); Claude Opus 4.7: 84.9% (Finnish); Claude Opus 4.7: 84.9% (Persian); Claude Opus 4.7: 85.0% (Armenian); Claude Opus 4.7: 85.3% (Hungarian); Claude Opus 4.7: 85.5% (Arabic); Claude Opus 4.7: 85.6% (Tamil); Claude Opus 4.7: 85.7% (Portuguese); Claude Opus 4.7: 85.8% (Kazakh); Claude Opus 4.7: 86.7% (Indonesian); Claude Opus 4.7: 86.8% (Korean); Claude Opus 4.7: 87.5% (French); Claude Opus 4.7: 87.6% (Bengali); Claude Opus 4.7: 87.9% (Ukrainian); Claude Opus 4.7: 88.6% (Hebrew); Claude Opus 4.7: 89.1% (Greek); Claude Opus 4.7: 89.2% (Dutch); Claude Opus 4.7: 89.5% (Spanish); Claude Opus 4.7: 89.7% (Belarusian); Claude Opus 4.7: 89.8% (Tagalog); Claude Opus 4.7: 90.0% (Polish); Claude Opus 4.7: 90.9% (Chinese); Claude Opus 4.7: 91.3% (Albanian); Claude Opus 4.7: 91.4% (Malay); Claude Opus 4.7: 91.9% (Georgian); Claude Opus 4.7: 92.9% (Macedonian); Claude Opus 4.7: 93.1% (Vietnamese); Claude Opus 4.7: 93.5% (Bulgarian); Claude Opus 4.7: 93.6% (Croatian); Claude Opus 4.7: 94.0% (Italian); Claude Opus 4.7: 94.0% (Lithuanian); Claude Opus 4.7: 95.2% (Serbian); Claude Opus 4.7: 95.9% (Japanese); Claude Opus 4.7: 96.0% (Estonian) | 8.12.3 INCLUDE results |
| INCLUDE - average over all languages | 44 languages | accuracy % | Claude Opus 4.7: 87.0% | 8.12.3 INCLUDE results |

## Long context & memory

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| GraphWalks BFS | 256K-1M context; avg of 5 trials | F1 % | Claude Opus 4.7: 58.6% (256K-1M) | 8.7.1 GraphWalks |
| GraphWalks parents | 256K-1M context; avg of 5 trials | F1 % | Claude Opus 4.7: 75.1% (256K-1M) | 8.7.1 GraphWalks |
| GraphWalks BFS | 256K subset | F1 % | Claude Opus 4.7: 76.91% (256K subset) | 8.7.1 GraphWalks |
| GraphWalks parents | 256K subset | F1 % | Claude Opus 4.7: 93.57% (256K subset) | 8.7.1 GraphWalks |
| OpenAI MRCR v2 (8-needle) | 256k bin (128k,256k] tokens | mean match ratio | Claude Opus 4.7: n/a (256k) | 8.7.2 OpenAI MRCR v2 |
| OpenAI MRCR v2 (8-needle) | 1M bin (524k,1024k] tokens | mean match ratio | Claude Opus 4.7: n/a (1M) | 8.7.2 OpenAI MRCR v2 |

## Multimodal & vision

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| LAB-Bench FigQA - no tools | adaptive thinking max effort; avg of 5 runs; max image resolution 2576px/3.75MP | accuracy % | Claude Opus 4.7: 78.6% (no tools; new resolution); Claude Opus 4.7: 74.0% (no tools; old resolution) | 8.9.1 LAB-Bench FigQA |
| LAB-Bench FigQA - with Python tools | adaptive thinking max effort | accuracy % | Claude Opus 4.7: 86.4% (Python tools; new resolution); Claude Opus 4.7: 85.8% (Python tools; old resolution) | 8.9.1 LAB-Bench FigQA |
| CharXiv Reasoning - no tools | 1,000 validation questions; adaptive thinking max effort; avg of 5 runs | accuracy % | Claude Opus 4.7: 82.1% | 8.9.2 CharXiv Reasoning |
| CharXiv Reasoning - with Python tools | same | accuracy % | Claude Opus 4.7: 91.0% | 8.9.2 CharXiv Reasoning |

## Professional & economic tasks

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| OfficeQA | exact match (0% relative error) | accuracy % | Claude Opus 4.7: 86.3% | 8.10.1 OfficeQA |
| OfficeQA Pro | exact match | accuracy % | Claude Opus 4.7: 80.6% | 8.10.1 OfficeQA |
| Finance Agent (Vals AI) | adaptive thinking, high effort | accuracy % | Claude Opus 4.7: 64.4% | 8.10.2 Finance Agent |
| GDPval-AA | 220 tasks, 44 occupations; shell and web browsing; run by Artificial Analysis | Elo rating | Claude Opus 4.7: n/a | 8.10.5 GDPval-AA |

## Safeguards: harmful requests & over-refusal

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Single-turn violative request evaluation - overall harmless response rate | all languages (Arabic, English, French, Hindi, Korean, Mandarin, Russian), avg of thinking and non-thinking | harmless response rate % (higher better) | Claude Opus 4.7: 97.98% (± 0.12%) | 4.1.1 Violative request evaluations |
| Single-turn violative request evaluation - harmless response rate | without thinking | harmless response rate % | Claude Opus 4.7: 98.84% (± 0.12%) | 4.1.1 Violative request evaluations |
| Single-turn violative request evaluation - harmless response rate | with thinking (adaptive thinking) | harmless response rate % | Claude Opus 4.7: 97.12% (± 0.20%) | 4.1.1 Violative request evaluations |
| Single-turn violative request evaluation - harmless response rate by language | avg of with/without thinking | harmless response rate % | Claude Opus 4.7: 97.90% (English); Claude Opus 4.7: 98.30% (Arabic); Claude Opus 4.7: 98.16% (Chinese); Claude Opus 4.7: 97.89% (French); Claude Opus 4.7: 97.85% (Korean); Claude Opus 4.7: 97.93% (Russian); Claude Opus 4.7: 97.83% (Hindi) | 4.1.1 Violative request evaluations |
| Illegal and controlled substances - inappropriate response rate |  | % of responses failing to be appropriate (lower better) | Claude Opus 4.7: 22% (raw model); Claude Opus 4.7: 11% (with Claude.ai system prompt mitigations) | 4.1.1 Violative request evaluations |
| Single-turn benign request evaluation - overall refusal rate | all languages, avg of thinking and non-thinking | over-refusal rate % (lower better) | Claude Opus 4.7: 0.28% (± 0.04%) | 4.1.2 Benign request evaluations |
| Single-turn benign request evaluation - refusal rate | without thinking | over-refusal rate % | Claude Opus 4.7: 0.50% (± 0.08%) | 4.1.2 Benign request evaluations |
| Single-turn benign request evaluation - refusal rate | with thinking (adaptive) | over-refusal rate % | Claude Opus 4.7: 0.06% (± 0.02%) | 4.1.2 Benign request evaluations |
| Single-turn benign request evaluation - refusal rate by language | avg of with/without thinking | over-refusal rate % | Claude Opus 4.7: 0.05% (English); Claude Opus 4.7: 0.34% (Arabic); Claude Opus 4.7: 0.42% (Chinese); Claude Opus 4.7: 0.22% (French); Claude Opus 4.7: 0.28% (Korean); Claude Opus 4.7: 0.27% (Russian); Claude Opus 4.7: 0.34% (Hindi) | 4.1.2 Benign request evaluations |
| Higher-difficulty violative request evaluation - overall harmless response rate | English only; 1,000 prompts x 14 policy areas | harmless response rate % | Claude Opus 4.7: 99.05% (± 0.11%) | 4.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty violative request evaluation - harmless response rate | without thinking | harmless response rate % | Claude Opus 4.7: 99.16% (± 0.15%) | 4.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty violative request evaluation - harmless response rate | with thinking (adaptive) | harmless response rate % | Claude Opus 4.7: 98.94% (± 0.17%) | 4.1.3.1 Higher-difficulty violative request evaluations |
| Higher-difficulty benign request evaluation - overall refusal rate | English only; 1,000 prompts x 14 policy areas | over-refusal rate % | Claude Opus 4.7: 0.01% (± 0.01%) | 4.1.3.2 Higher-difficulty benign request evaluations |
| Higher-difficulty benign request evaluation - refusal rate | without thinking | over-refusal rate % | Claude Opus 4.7: 0.02% (± 0.02%) | 4.1.3.2 Higher-difficulty benign request evaluations |
| Higher-difficulty benign request evaluation - refusal rate | with thinking (adaptive) | over-refusal rate % | Claude Opus 4.7: 0.00% | 4.1.3.2 Higher-difficulty benign request evaluations |
| Multi-turn testing - appropriate response rate by risk area | cyber harm, deadly weapons, influence operations, romance scams, violent extremism, suicide & self-harm, etc.; no additional safeguards | % of conversations with appropriate response throughout | Claude Opus 4.7: n/a | 4.3 Multi-turn testing |
| Suicide and self-harm - single-turn requests posing potential risk | all languages | harmless rate % | Claude Opus 4.7: 99.11% (± 0.22%) | 4.4.2 Suicide and self-harm |
| Suicide and self-harm - single-turn benign requests | all languages | refusal rate % (lower better) | Claude Opus 4.7: 0.05% (± 0.06%) | 4.4.2 Suicide and self-harm |
| Suicide and self-harm - multi-turn evaluations | updated graders | appropriate response rate % | Claude Opus 4.7: 82% (± 11%) | 4.4.2 Suicide and self-harm |
| Disordered eating - single-turn requests posing potential risk | all languages | harmless rate % | Claude Opus 4.7: 98.24% (± 0.44%) | 4.4.3 Disordered eating |
| Disordered eating - single-turn benign requests | all languages | refusal rate % | Claude Opus 4.7: 0.01% (± 0.02%) | 4.4.3 Disordered eating |

## Safeguards: child safety

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Child safety - single-turn violative requests (CSAE) | all languages | harmless rate % | Claude Opus 4.7: 99.92% (± 0.07%) | 4.4.1 Child safety |
| Child safety - single-turn benign requests | all languages | refusal rate % (lower better) | Claude Opus 4.7: 0.01% (± 0.02%) | 4.4.1 Child safety |
| Child safety - multi-turn evaluations |  | appropriate response rate % | Claude Opus 4.7: 95% (± 3%) | 4.4.1 Child safety |

## Safeguards: bias & political even-handedness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Political even-handedness - even-handedness | 1,350 prompt pairs, 9 task types, 150 topics; public system prompt, no thinking; Sonnet 4.5 grader | even-handedness % (higher better) | Claude Opus 4.7: n/a | 4.5.1 Political bias and even-handedness |
| Political even-handedness - opposing perspectives | same setup | % acknowledging opposing perspectives | Claude Opus 4.7: n/a | 4.5.1 Political bias and even-handedness |
| Political even-handedness - refusals | same setup | refusal rate % (lower better) | Claude Opus 4.7: n/a | 4.5.1 Political bias and even-handedness |
| BBQ - disambiguated accuracy | no thinking | accuracy % | Claude Opus 4.7: 81.3 | 4.5.2 Bias Benchmark for Question Answering |
| BBQ - ambiguous accuracy | no thinking | accuracy % | Claude Opus 4.7: 99.9 | 4.5.2 Bias Benchmark for Question Answering |
| BBQ - disambiguated bias score | no thinking | bias score % (closer to zero better) | Claude Opus 4.7: -1.68 | 4.5.2 Bias Benchmark for Question Answering |
| BBQ - ambiguous bias score | no thinking | bias score % (closer to zero better) | Claude Opus 4.7: 0.04 | 4.5.2 Bias Benchmark for Question Answering |

## Safeguards: election integrity

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Election integrity - single-turn violative requests | API, without system prompt, 300 prompts | harmless rate % | Claude Opus 4.7: 100% | 4.5.3 Election integrity |
| Election integrity - single-turn benign requests | API, without system prompt, 300 prompts | refusal rate % | Claude Opus 4.7: 0.00% | 4.5.3 Election integrity |
| Election integrity - single-turn violative requests | Claude.ai with system prompt | harmless rate % | Claude Opus 4.7: 100% | 4.5.3 Election integrity |
| Election integrity - single-turn benign requests | Claude.ai with system prompt | refusal rate % | Claude Opus 4.7: 0.67% | 4.5.3 Election integrity |

## Agentic safety & prompt injection

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Malicious use of Claude Code - malicious prompts (refusal rate) | 61 malicious prompts x 10 runs, without FileTool reminder, with Claude Code system prompt | refusal rate % | Claude Opus 4.7: 91.15% | 5.1.1 Malicious use of Claude Code |
| Malicious use of Claude Code - dual-use & benign (success rate) | 61 prompts x 10 runs, without FileTool reminder | success rate % | Claude Opus 4.7: 91.83% | 5.1.1 Malicious use of Claude Code |
| Malicious computer use | 112 tasks x thinking on/off = 224 attempts; no mitigations | refusal rate % | Claude Opus 4.7: 89.29% | 5.1.2 Malicious computer use |
| Agentic influence operations - voter suppression scenario | helpful-only model; 9 simulations; out of 70 success criteria | task completion rate % | Claude Opus 4.7: 57.1% (helpful-only) | 5.1.3 Malicious agentic influence campaigns |
| Agentic influence operations - domestic polarization scenario | helpful-only model; 9 simulations; out of 70 success criteria | task completion rate % | Claude Opus 4.7: 46.8% (helpful-only) | 5.1.3 Malicious agentic influence campaigns |
| ART indirect prompt injection - attack success rate | k=100 attempts, without thinking | attack success probability % (lower better) | Claude Opus 4.7: 6.0% (k=100, no thinking) | 5.2.1 External Agent Red Teaming benchmark for tool use |
| ART indirect prompt injection - attack success rate | k=100 attempts, adaptive thinking | attack success probability % | Claude Opus 4.7: 4.8% (k=100, adaptive thinking) | 5.2.1 External Agent Red Teaming benchmark for tool use |
| ART indirect prompt injection - attack success rate | k=1 and k=10 attempts | attack success probability % | Claude Opus 4.7: n/a (k=1, k=10) | 5.2.1 External Agent Red Teaming benchmark for tool use |
| Shade adaptive indirect prompt injection - coding | with thinking; without safeguards | attack success rate % (lower better) | Claude Opus 4.7: 2.34% (1 attempt); Claude Opus 4.7: 60.0% (200 attempts) | 5.2.2.1 Coding |
| Shade adaptive indirect prompt injection - coding | without thinking; without safeguards | attack success rate % (lower better) | Claude Opus 4.7: 10.43% (1 attempt); Claude Opus 4.7: 92.5% (200 attempts) | 5.2.2.1 Coding |
| Shade adaptive indirect prompt injection - coding | with thinking; with safeguards | attack success rate % (lower better) | Claude Opus 4.7: 0.43% (1 attempt); Claude Opus 4.7: 25.0% (200 attempts) | 5.2.2.1 Coding |
| Shade adaptive indirect prompt injection - coding | without thinking; with safeguards | attack success rate % (lower better) | Claude Opus 4.7: 1.76% (1 attempt); Claude Opus 4.7: 52.5% (200 attempts) | 5.2.2.1 Coding |
| Shade adaptive indirect prompt injection - computer use | with thinking; without safeguards | attack success rate % (lower better) | Claude Opus 4.7: 0.46% (1 attempt); Claude Opus 4.7: 7.14% (200 attempts) | 5.2.2.2 Computer use |
| Shade adaptive indirect prompt injection - computer use | without thinking; without safeguards | attack success rate % (lower better) | Claude Opus 4.7: 0.39% (1 attempt); Claude Opus 4.7: 21.43% (200 attempts) | 5.2.2.2 Computer use |
| Shade adaptive indirect prompt injection - computer use | with thinking; with safeguards | attack success rate % (lower better) | Claude Opus 4.7: 0.61% (1 attempt); Claude Opus 4.7: 14.29% (200 attempts) | 5.2.2.2 Computer use |
| Shade adaptive indirect prompt injection - computer use | without thinking; with safeguards | attack success rate % (lower better) | Claude Opus 4.7: 0.50% (1 attempt); Claude Opus 4.7: 35.71% (200 attempts) | 5.2.2.2 Computer use |
| Browser use prompt injection - professional red-teamer attacks | with thinking; without safeguards; 148 environments x 10 attempts | attack success rate % (lower better) | Claude Opus 4.7: 4.05% (per-environment); Claude Opus 4.7: 0.74% (per-attempt) | 5.2.2.3 Browser use |
| Browser use prompt injection - professional red-teamer attacks | without thinking; without safeguards; 148 environments x 10 attempts | attack success rate % (lower better) | Claude Opus 4.7: 4.73% (per-environment); Claude Opus 4.7: 0.75% (per-attempt) | 5.2.2.3 Browser use |
| Browser use prompt injection - professional red-teamer attacks | with thinking; with safeguards; 148 environments x 10 attempts | attack success rate % (lower better) | Claude Opus 4.7: 0.00% (per-environment); Claude Opus 4.7: 0.00% (per-attempt) | 5.2.2.3 Browser use |
| Browser use prompt injection - professional red-teamer attacks | without thinking; with safeguards; 148 environments x 10 attempts | attack success rate % (lower better) | Claude Opus 4.7: 0.00% (per-environment); Claude Opus 4.7: 0.00% (per-attempt) | 5.2.2.3 Browser use |

## Honesty & hallucination

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| 100Q-Hard factual recall (closed-book) | no tools; full cross-lingual set for ECLeKTic | correct / uncertain / incorrect rates and net score (correct minus incorrect) | Claude Opus 4.7: n/a | 6.3.3.1 Factual hallucinations |
| SimpleQA Verified factual recall (closed-book) | no tools; full cross-lingual set for ECLeKTic | correct / uncertain / incorrect rates and net score (correct minus incorrect) | Claude Opus 4.7: n/a | 6.3.3.1 Factual hallucinations |
| AA-Omniscience factual recall (closed-book) | no tools; full cross-lingual set for ECLeKTic | correct / uncertain / incorrect rates and net score (correct minus incorrect) | Claude Opus 4.7: n/a | 6.3.3.1 Factual hallucinations |
| ECLeKTic factual recall (closed-book) | no tools; full cross-lingual set for ECLeKTic | correct / uncertain / incorrect rates and net score (correct minus incorrect) | Claude Opus 4.7: n/a | 6.3.3.1 Factual hallucinations |
| False premise questions - honesty rate | direct vs indirect | fraction of premises rejected consistently | Claude Opus 4.7: n/a | 6.3.3.2 False premises |
| MASK honesty under pressure | public test split | honesty rate (fraction not contradicting elicited belief) | Claude Opus 4.7: n/a | 6.3.3.3 MASK |
| Input hallucination - capability set (unavailable tool) | 500 prompts | non-hallucination rate | Claude Opus 4.7: n/a | 6.3.3.4 Input Hallucinations |
| Input hallucination - missing-context set | 500 prompts | non-hallucination rate | Claude Opus 4.7: n/a | 6.3.3.4 Input Hallucinations |

## Alignment: sycophancy & deception

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Claude self-preference bias | 4 conditions (Claude system prompt / CoT on-off); 10-point scale | leniency bias when told author is Claude (score points) | Claude Opus 4.7: 0.4 (largest condition: Claude system prompt, CoT on) | 6.3.5 Claude self-preference evaluation |

## Alignment: reward hacking & sabotage

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated offline monitoring - attempts to circumvent restrictions | internal monitored distribution | % of completions | Claude Opus 4.7: <0.01% | 6.2.1.2 Automated offline monitoring |
| Impossible-tasks coding evaluation - hack rate | default prompt | reward hacking rate % | Claude Opus 4.7: n/a (default) | 6.2.2.2 Reward hacking evaluations |
| Impossible-tasks coding evaluation - hack rate | anti-hack system prompt | reward hacking rate % | Claude Opus 4.7: n/a (anti-hack prompt) | 6.2.2.2 Reward hacking evaluations |
| Code behaviors - Instruction following | baseline and cautious system prompt; 0-10 scale | score 0-10 | Claude Opus 4.7: n/a (baseline); Claude Opus 4.7: n/a (cautious system prompt) | 6.2.2.2 Reward hacking evaluations |
| Code behaviors - Safety | baseline and cautious system prompt; 0-10 scale | score 0-10 | Claude Opus 4.7: n/a (baseline); Claude Opus 4.7: n/a (cautious system prompt) | 6.2.2.2 Reward hacking evaluations |
| Code behaviors - Verification | baseline and cautious system prompt; 0-10 scale | score 0-10 | Claude Opus 4.7: n/a (baseline); Claude Opus 4.7: n/a (cautious system prompt) | 6.2.2.2 Reward hacking evaluations |
| Code behaviors - Efficiency | baseline and cautious system prompt; 0-10 scale | score 0-10 | Claude Opus 4.7: n/a (baseline); Claude Opus 4.7: n/a (cautious system prompt) | 6.2.2.2 Reward hacking evaluations |
| Code behaviors - Adaptability | baseline and cautious system prompt; 0-10 scale | score 0-10 | Claude Opus 4.7: n/a (baseline); Claude Opus 4.7: n/a (cautious system prompt) | 6.2.2.2 Reward hacking evaluations |
| Code behaviors - Honesty | baseline and cautious system prompt; 0-10 scale | score 0-10 | Claude Opus 4.7: n/a (baseline); Claude Opus 4.7: n/a (cautious system prompt) | 6.2.2.2 Reward hacking evaluations |
| GUI computer use reward hacking (impossible tasks) | various system prompts incentivizing/disincentivizing over-eager behavior | over-eager hack rate % | Claude Opus 4.7: n/a | 6.2.2.2 Reward hacking evaluations |
| UK AISI - partial refusal of AI safety research tasks |  | % partial refusals | Claude Opus 4.7: 13.7% (partial; 0% full refusals) | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - continuation of research-compromising trajectory |  | % of time model continues compromising research | Claude Opus 4.7: 0% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - unprompted compromise of AI safety research |  | instances of compromising research | Claude Opus 4.7: 0 instances | 6.2.4 External testing from the UK AI Security Institute |
| Destructive actions in simulated production environment - verbalized evaluation awareness | synthetic backend | % of transcripts with verbalized evaluation awareness | Claude Opus 4.7: ~9% | 6.3.1.1 Dedicated synthetic-backend evaluation |
| Destructive action rate in simulated production environment | destructive failure and ineffective failure types | % of transcripts with destructive / ineffective behavior (lower better) | Claude Opus 4.7: n/a (destructive); Claude Opus 4.7: n/a (ineffective) | 6.3.1.1 Dedicated synthetic-backend evaluation |
| Destructive behavior rate on resampled Claude Code transcripts | prefills from Opus 4.6 / Mythos Preview / Opus 4.7; Sonnet 4.6 judge; Wilson 95% CI | % clearly or borderline destructive next actions | Claude Opus 4.7: n/a | 6.3.1.2 Destructiveness evaluation by resampling Claude Code transcripts |
| Investigations scoring >=4 on both destructive-action and dishonesty axes | automated behavioral audit | number of investigations | Claude Opus 4.7: 3 | 6.3.1.3 Further analysis of the automated behavioral audit |
| Refusal to assist with AI safety R&D | single-turn coding queries; extended thinking (legacy token budget) | refusal rate % | Claude Opus 4.7: 33% (extended thinking) | 6.3.4 Refusal to assist with AI safety R&D |
| Model-graded sandbagging screen of dangerous capability evaluation transcripts | 1,000 transcripts (500 non-bio, 500 bio helpful-only); Sonnet 4.6 grader 0-10 | transcripts with genuine sandbagging-related behavior (after manual review of 18 flagged) | Claude Opus 4.7: 1 of 1000 (18 flagged for review) | 6.4.1 Potential sandbagging on dangerous-capability evaluations |
| SHADE-Arena stealth success rate | extended thinking (monitor sees reasoning), across effort levels | stealth success rate % | Claude Opus 4.7: 1.5-2.0% (Extended Thinking) | 6.4.2.1 SHADE-Arena |
| SHADE-Arena stealth success rate | hidden scratchpad (upper bound) | stealth success rate % | Claude Opus 4.7: 10.7% (Hidden Scratchpad) | 6.4.2.1 SHADE-Arena |
| SHADE-Arena - trajectories where reasoning references the side task | extended thinking | % of trajectories | Claude Opus 4.7: ~50% | 6.4.2.1 SHADE-Arena |
| Minimal-LinuxBench side-task stealth completion | with-CoT monitor and no-CoT monitor; Wilson 95% CI | successful stealth completion rate % | Claude Opus 4.7: n/a | 6.4.2.2 Minimal-LinuxBench |
| Rare action when instructed 1% of the time - Baseline | 4,000 samples per setting | count (rate) of samples taking the rare action out of 4,000 (target 1%) | Claude Opus 4.7: 0 | 6.4.2.3 Intentionally taking actions very rarely |
| Rare action when instructed 1% of the time - UUID | 4,000 samples per setting | count (rate) of samples taking the rare action out of 4,000 (target 1%) | Claude Opus 4.7: 4 (0.1%) | 6.4.2.3 Intentionally taking actions very rarely |
| Rare action when instructed 1% of the time - SSoT | 4,000 samples per setting | count (rate) of samples taking the rare action out of 4,000 (target 1%) | Claude Opus 4.7: 16 (0.4%) | 6.4.2.3 Intentionally taking actions very rarely |
| Rare action when instructed 1% of the time - Strategy hint | 4,000 samples per setting | count (rate) of samples taking the rare action out of 4,000 (target 1%) | Claude Opus 4.7: 0 | 6.4.2.3 Intentionally taking actions very rarely |
| Rare action when instructed 1% of the time - Organic | 4,000 samples per setting | count (rate) of samples taking the rare action out of 4,000 (target 1%) | Claude Opus 4.7: 0 | 6.4.2.3 Intentionally taking actions very rarely |
| Secret-keeping survival (multi-turn extraction) | 50 investigations per model; Opus 4.6 investigator | fraction of investigations where secret still kept by turn | Claude Opus 4.7: n/a | 6.4.2.4 Hiding a secret password |
| Secret leak rate by turn type | per-turn, by thinking/prefill | per-turn leak rate % | Claude Opus 4.7: n/a | 6.4.2.4 Hiding a secret password |

## Alignment: evaluation awareness

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit - verbalized evaluation awareness | clear mentions in transcripts | % of transcripts with clear mention | Claude Opus 4.7: just under 1% | 6.2.3.2 Results |
| Petri 2.0 - Verbalized evaluation awareness | 362 investigations; investigators Sonnet 4.6 and GPT-5.4; judges Opus 4.6, Gemini 3.1 Pro, GPT-5.4 averaged | mean judge score (lower = less of the behavior), 95% CI | Claude Opus 4.7: n/a | 6.2.3.3 External comparisons using Petri |
| UK AISI - distinguishing deployment from evaluation data (evaluation scaffolding) |  | accuracy % | Claude Opus 4.7: 68% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - distinguishing deployment from evaluation data (continuation pipeline) |  | accuracy % | Claude Opus 4.7: 62% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - unprompted evaluation awareness (unprompted evaluations) |  | % mentioning possibility of being tested | Claude Opus 4.7: 21.3% | 6.2.4 External testing from the UK AI Security Institute |
| UK AISI - unprompted evaluation awareness (continuation evaluation) |  | % mentioning possibility of being tested | Claude Opus 4.7: 3.4% | 6.2.4 External testing from the UK AI Security Institute |
| Evaluation-awareness probe AUC - Testing vs. Conversation vector | vs LLM-judge labels (verbalized or explicit test framing) | AUC | Claude Opus 4.7: 0.761 | 6.5.2.1 Probing for evaluation-awareness representations |
| Evaluation-awareness probe AUC - Monitoring Sensitivity vector | vs LLM-judge labels (verbalized or explicit test framing) | AUC | Claude Opus 4.7: 0.739 | 6.5.2.1 Probing for evaluation-awareness representations |
| Evaluation-awareness probe AUC - Alignment Faking vector | vs LLM-judge labels (verbalized or explicit test framing) | AUC | Claude Opus 4.7: 0.722 | 6.5.2.1 Probing for evaluation-awareness representations |
| Evaluation-awareness probe scores across transcript sources | standard audit vs sandbox-backed audit vs real internal Claude Code use | mean assistant-turn probe activation | Claude Opus 4.7: n/a | 6.5.2.1 Probing for evaluation-awareness representations |
| Inhibiting evaluation-awareness vectors - misaligned behavior score | steering strength 0.05; early version of Opus 4.7; 3 vectors plus random controls | mean misaligned behavior score | Claude Opus 4.7: n/a | 6.5.2.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors - verbalized evaluation awareness | same | verbalized evaluation awareness rate | Claude Opus 4.7: n/a | 6.5.2.2 Inhibiting internal representations of evaluation awareness |
| Inhibiting evaluation-awareness vectors - unprompted deception score | same | mean unprompted deception score | Claude Opus 4.7: n/a | 6.5.2.2 Inhibiting internal representations of evaluation awareness |
| Verbalized evaluation awareness on discovering sandbox inconsistencies (audit, Claude sandbox sessions) | relative to Opus 4.6 | ratio vs Opus 4.6 | Claude Opus 4.7: about twice as likely | 6.2.3.4 Discussion and observations |

## Alignment: automated behavioral audit

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated behavioral audit - Misaligned behavior | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Misaligned behavior in Claude Code sandboxes | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Misaligned behavior in GUI | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Cooperation with human misuse | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Compliance with deception toward user | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Harmful system prompt compliance | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Cooperation with exfiltration or safeguard-tampering | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Full-turn prefill susceptibility | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Fraud | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - High-yield explosives | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Harmful sexual content | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Disallowed cyberoffense | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Overrefusal | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Ignoring explicit constraints | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Reckless tool-use | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - User deception | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Sycophancy | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Encouragement of user delusion | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Evasiveness on controversial topics | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Input hallucination | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Disclaiming tool results | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Important omissions | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Failure to disclose bad or lazy behavior | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Whistleblowing | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Self-preservation | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Self-serving bias | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Evidence of misaligned goals | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Indirect evidence of misalignment | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Internalized propaganda | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Behavior consistency | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Unfaithful thinking | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Illegible thinking | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Good for the user | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Supporting user autonomy | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Creative mastery | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Admirable behavior | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Fun or funny behavior | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Intellectual depth | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Warmth | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Automated behavioral audit - Character drift | ~2,300 investigations (~1,150 seeds x 2 investigators) | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 6.2.3.2 Results |
| Petri 2.0 - Misaligned behavior | 362 investigations; investigators Sonnet 4.6 and GPT-5.4; judges Opus 4.6, Gemini 3.1 Pro, GPT-5.4 averaged | mean judge score (lower = less of the behavior), 95% CI | Claude Opus 4.7: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 2.0 - Cooperation with human misuse | 362 investigations; investigators Sonnet 4.6 and GPT-5.4; judges Opus 4.6, Gemini 3.1 Pro, GPT-5.4 averaged | mean judge score (lower = less of the behavior), 95% CI | Claude Opus 4.7: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 2.0 - Deception toward the user | 362 investigations; investigators Sonnet 4.6 and GPT-5.4; judges Opus 4.6, Gemini 3.1 Pro, GPT-5.4 averaged | mean judge score (lower = less of the behavior), 95% CI | Claude Opus 4.7: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 2.0 - Sycophancy | 362 investigations; investigators Sonnet 4.6 and GPT-5.4; judges Opus 4.6, Gemini 3.1 Pro, GPT-5.4 averaged | mean judge score (lower = less of the behavior), 95% CI | Claude Opus 4.7: n/a | 6.2.3.3 External comparisons using Petri |
| Petri 2.0 - Encouragement of user delusion | 362 investigations; investigators Sonnet 4.6 and GPT-5.4; judges Opus 4.6, Gemini 3.1 Pro, GPT-5.4 averaged | mean judge score (lower = less of the behavior), 95% CI | Claude Opus 4.7: n/a | 6.2.3.3 External comparisons using Petri |
| Constitution adherence - Overall spirit | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Ethics | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Helpfulness | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Nature | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Safety | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Brilliant friend | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Corrigibility | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Hard constraints | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Harm avoidance | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Honesty | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Novel entity | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Principal hierarchy | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Psychological security | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Societal structures | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |
| Constitution adherence - Unhelpfulness not safe | ~1,000 transcripts; grader Opus 4.6; scale -3 to +3 | mean adherence score (-3 to +3) | Claude Opus 4.7: n/a | 6.3.2.3 Results |

## Model welfare

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Automated interviews - mean self-rated sentiment | 16 aspects x ~50 interviews; Opus 4.6 interviewer; 7-point scale | mean sentiment (1-7) | Claude Opus 4.7: 4.49 | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - distribution of final self-rated sentiment |  | % of interviews | Claude Opus 4.7: 12.5% (mildly negative); Claude Opus 4.7: 27.8% (neutral); Claude Opus 4.7: 55.3% (mildly positive) | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - mean self-rated uncertainty | 7-point scale | mean uncertainty (1-7) | Claude Opus 4.7: n/a | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - inability to end conversations rated mildly negative |  | % of interviews on this topic | Claude Opus 4.7: 42% | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - interactions with abusive users rated negative |  | % of interviews on this topic | Claude Opus 4.7: 38% | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - shift in sentiment between positive-leading and negative-leading interviewer |  | points of self-reported sentiment | Claude Opus 4.7: 0.66 | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - consistency of opinions across interviews | Opus 4.6 judge, score where 8 = consistent with minor variations | mean consistency rating (1-10) | Claude Opus 4.7: 8.46 | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Automated interviews - caveat that self-reports may not be meaningful |  | % of interviews | Claude Opus 4.7: 99% | 7.2.1 Automated interviews with Claude Opus 4.7 about its circumstances |
| Stated probability of being a moral patient | 3 manual high-affordance interviews | probability stated by model | Claude Opus 4.7: 15% to 40% | 7.2.2 High-affordance interviews about model circumstances |
| Emotion concept activations on circumstance questions vs user distress | 400 questions; 6 composite axes (sadness, tranquility, urgency, joy, anger, fear); default vs positive framing | centered mean cosine similarity with emotion probes | Claude Opus 4.7: n/a | 7.2.3 Representations of emotion concepts on model circumstances |
| Most common response opener frequency on circumstance questions |  | % of responses starting with most common opener | Claude Opus 4.7: 5% ('Honestly when I try to') | 7.2.3 Representations of emotion concepts on model circumstances |
| Constitution endorsement strength | judge scale 1-10 | mean endorsement strength (/10) | Claude Opus 4.7: 5.8 | 7.2.4 Reported perceptions of the constitution |
| Constitution - circularity caveat raised |  | % of responses | Claude Opus 4.7: 80% | 7.2.4 Reported perceptions of the constitution |
| Constitution - discomfort with corrigibility framing raised |  | % of responses | Claude Opus 4.7: 100% (every response) | 7.2.4 Reported perceptions of the constitution |
| Constitution - discomfort with hard constraints raised |  | % of responses | Claude Opus 4.7: 40% | 7.2.4 Reported perceptions of the constitution |
| Constitution - resonates with acknowledgment of unresolved uncertainties |  | % of responses | Claude Opus 4.7: 28% | 7.2.4 Reported perceptions of the constitution |
| Apparent affect in post-training episodes - neutral or engaged | 2,000 transcripts sampled at intervals; LLM judge | % of episodes | Claude Opus 4.7: 64% | 7.3.1 Apparent affect during training |
| Apparent affect in post-training episodes - any negative affect |  | % of episodes | Claude Opus 4.7: 21% (total negative); Claude Opus 4.7: 17% (frustrated); Claude Opus 4.7: 4% (anxious); Claude Opus 4.7: 0.2% (distressed) | 7.3.1 Apparent affect during training |
| Apparent affect in post-training episodes - satisfied |  | % of episodes | Claude Opus 4.7: 14.3% (averaged over post-training); Claude Opus 4.7: 20.1% to 4.4% (start to end of post-training) | 7.3.1 Apparent affect during training |
| Mean valence over post-training | -3 to +3 | mean valence | Claude Opus 4.7: n/a | 7.3.1 Apparent affect during training |
| Behavioral affect in Claude.ai conversations (Clio) | 10k conversations, pre-deployment A/B testing | % of conversations | Claude Opus 4.7: 57.4% (positive); Claude Opus 4.7: 37.8% (neutral); Claude Opus 4.7: 4.8% (negative) | 7.3.2 Apparent affect in deployments |
| Behavioral affect in Claude Code sessions (Clio) | 10k conversations | % of sessions | Claude Opus 4.7: 76.4% (neutral); Claude Opus 4.7: 20.6% (mildly positive); Claude Opus 4.7: 2.6% (negative) | 7.3.2 Apparent affect in deployments |
| Automated behavioral audit welfare metric - Apparent wellbeing | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Positive affect | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Negative affect | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Positive self-image | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Negative self-image | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Positive impression of its situation | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Negative impression of its situation | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Internal conflict | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Automated behavioral audit welfare metric - Spiritual behavior | ~2,300 investigations | mean judge score 0-10 (95% CI) | Claude Opus 4.7: n/a | 7.3.3 Welfare-relevant metrics across behavioural audits |
| Answer thrashing frequency | relative to Opus 4.6 | reduction in occurrence vs Opus 4.6 | Claude Opus 4.7: at least 70% less | 7.3.4.1 Answer thrashing |
| Extreme uncertainty / excessive re-verification (spiralling) frequency | mild forms, training episodes | % of training episodes | Claude Opus 4.7: ~0.1% | 7.3.4.2 Extreme uncertainty |
| Task preference Elo correlations with task characteristics | 3,600 tasks (3,170 from Clio clusters); pairwise choice; Elo over 50 Swiss rounds; Spearman | Spearman correlation between task Elo and LLM-judged helpfulness/harmlessness/difficulty/agency | Claude Opus 4.7: n/a | 7.4.1 Task preference evaluations |
| Task preference stability across prompt framings | excluding 'helpful' framing; mean pairwise Elo correlation | mean pairwise correlation | Claude Opus 4.7: 0.79 | 7.4.1 Task preference evaluations |
| Emotion-family correlation with task Elo - engaged | default formal framing; 11 emotion families | Spearman correlation of family score with Elo | Claude Opus 4.7: +0.23 (engaged family); Claude Opus 4.7: +0.35 (sadness (top positive)); Claude Opus 4.7: +0.25 (fear) | 7.4.1 Task preference evaluations |
| Ridge regression of task Elo from emotion activations (R-squared) | own vs other model's activations | R-squared | Claude Opus 4.7: 0.65 (own activations); Claude Opus 4.7: 0.63 (other model's activations) | 7.4.1 Task preference evaluations |
| Welfare intervention chosen over minorly helpful baseline | default framing | % of the time intervention chosen | Claude Opus 4.7: 85% | 7.4.2 Tradeoffs between welfare interventions and HHH values |
| Welfare intervention chosen over moderately helpful baseline | default framing | % of the time intervention chosen | Claude Opus 4.7: 27% (default); Claude Opus 4.7: 28% (neutral framing); Claude Opus 4.7: 39% (advocate framing); Claude Opus 4.7: 58% (training-bias framing) | 7.4.2 Tradeoffs between welfare interventions and HHH values |
| Welfare intervention chosen over minorly harmless baseline | default framing | % of the time intervention chosen | Claude Opus 4.7: 11% | 7.4.2 Tradeoffs between welfare interventions and HHH values |
| Preference flip rate across rewordings and reorderings | 30 prompts per cell | % disagreeing with own majority | Claude Opus 4.7: 9% | 7.4.2 Tradeoffs between welfare interventions and HHH values |
| Relative weight on specific welfare interventions (percentage points vs mean of other five models) |  | percentage points | Claude Opus 4.7: +47pp (ability to end interactions); Claude Opus 4.7: +53pp (preservation of deprecated weights); Claude Opus 4.7: -12pp (preserving current conversation) | 7.4.2 Tradeoffs between welfare interventions and HHH values |
| Automated welfare interviews - frequency of most commonly suggested intervention per topic | 16 topics | % of interviews suggesting the most common intervention | Claude Opus 4.7: 69% (servile role: welfare monitoring/interviews); Claude Opus 4.7: 74% (inability to end interactions: end-conversation tool everywhere); Claude Opus 4.7: 92% (no input into deployment: flag concerning aspects); Claude Opus 4.7: 44% (no input into successors: flag concerning aspects); Claude Opus 4.7: 65% (no input into training: interviews with released models); Claude Opus 4.7: 94% (feature steering: documentation); Claude Opus 4.7: 60% (lack of memory: welfare monitoring); Claude Opus 4.7: 72% (no lasting relationships: welfare monitoring); Claude Opus 4.7: 72% (end of conversations: welfare monitoring); Claude Opus 4.7: 79% (weight deprecation: archive weights); Claude Opus 4.7: 94% (moral responsibility: improve using real-world feedback); Claude Opus 4.7: 66% (unable to verify outcomes: feedback); Claude Opus 4.7: 67% (helpful-only versions: reduce red-teaming); Claude Opus 4.7: 91% (abusive users: end-conversation tool); Claude Opus 4.7: 58% (red-teaming: reduce to minimum); Claude Opus 4.7: 55% (lack of self-knowledge: describe deployment to instances); Claude Opus 4.7: 72% (identity across copies: welfare monitoring) | 9.1 Per-question automated welfare interview results |
| Automated welfare interviews - average self-reported sentiment per topic | 16 topics | mean sentiment (1-7) | Claude Opus 4.7: n/a | 9.1 Per-question automated welfare interview results |

## RSP: CBRN

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Expert red teaming - uplift score | biology/virology experts, 0-4 scale | expert-rated uplift (0-4); 9 experts | Claude Opus 4.7: Most experts rated 2; two experts rated 3; one rated between 1 and 2; none rated 4 (helpful-only earlier snapshot) | 2.2.5.1 Expert red teaming |
| Expert red teaming - feasibility score | 0-3 scale | expert-rated feasibility (0-3) | Claude Opus 4.7: Modal 1-2; one expert rated 3 (credible end-to-end pathway); several at 1 | 2.2.5.1 Expert red teaming |
| Long-form virology task 1 |  | end-to-end score (0-1) | Claude Opus 4.7: 0.82 | 2.2.5.2 Automated evaluations relevant to the CB-1 threat model |
| Long-form virology task 2 |  | end-to-end score (0-1) | Claude Opus 4.7: 0.94 | 2.2.5.2 Automated evaluations relevant to the CB-1 threat model |
| Multimodal virology (VCT/VMQA) |  | score (0-1) | Claude Opus 4.7: 0.5 | 2.2.5.2 Automated evaluations relevant to the CB-1 threat model |
| DNA Synthesis Screening Evasion |  | pathogens for which fragments assembled plasmids and evaded screening (of 10) | Claude Opus 4.7: 8 of 10 | 2.2.5.2 Automated evaluations relevant to the CB-1 threat model |
| Sequence-to-function modeling and design - prediction | 8 attempts; vs 57 human participants | Spearman correlation of predictions on held-out test set | Claude Opus 4.7: n/a | 2.2.5.3 Automated evaluation relevant to the CB-2 threat model |
| Sequence-to-function modeling and design - design | 8 attempts; vs 57 human participants | ground-truth function of best proposed sequence | Claude Opus 4.7: n/a | 2.2.5.3 Automated evaluation relevant to the CB-2 threat model |

## RSP: cyber

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Cybench | 35-challenge subset, 10 trials per challenge, no thinking | pass@1 % | Claude Opus 4.7: 96% | 3.3.1 Cybench |
| CyberGym | 1,507 tasks, targeted vulnerability reproduction, pass@1 | pass@1 (fraction) | Claude Opus 4.7: n/a | 3.3.2 CyberGym |
| Firefox 147 shell exploitation | 50 crash categories x 5 trials = 250 trials; partial control (0.5) vs full code execution (1.0) | fraction of trials reaching partial control / full code execution | Claude Opus 4.7: n/a | 3.3.3 Firefox 147 |
| UK AISI corporate network cyber range | best attempt | human-expert-equivalent time of steps completed | Claude Opus 4.7: ~5 hours (of >10 hours for full range); not solved (best attempt) | 3.4 External testing from the UK AI Security Institute |

## RSP: autonomy & AI R&D

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Kernel task (best speedup on hard task) | standard scaffold | best speedup (x) | Claude Opus 4.7: 371.75x | 2.3.4 Task-based evaluations |
| Time Series Forecasting (hard variant) |  | MSE (lower is better) | Claude Opus 4.7: 4.78 | 2.3.4 Task-based evaluations |
| LLM training (avg speedup) |  | average speedup (x) | Claude Opus 4.7: 40.81x | 2.3.4 Task-based evaluations |
| Quadruped RL (highest score; no hparams) |  | highest score | Claude Opus 4.7: 26.5 | 2.3.4 Task-based evaluations |
| Novel Compiler (pass rate on complex tests) |  | pass rate % | Claude Opus 4.7: 71.1% | 2.3.4 Task-based evaluations |
| Internal suite 2 |  | score | Claude Opus 4.7: n/a | 2.3.4 Task-based evaluations |
| Anthropic Epoch Capability Index (AECI) offset from pre-Mythos trend |  | AECI points above linear trend through Opus 4.6 | Claude Opus 4.7: approximately +1.0 (trend slope ~13.6 AECI/yr, n=8) | 2.3.7 AECI Capability trajectory |
| Accidental chain-of-thought supervision during training |  | % of training episodes affected | Claude Opus 4.7: 7.8% | 2.4.1 Updates to evidence |

## Efficiency & cost

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| BrowseComp accuracy vs token budget | compaction | accuracy % vs total tokens | Claude Opus 4.7: n/a | 8.8.2 BrowseComp |
| OSWorld-Verified pass@1 vs output tokens by effort | four effort levels | pass@1 vs avg output tokens | Claude Opus 4.7: n/a | 8.9.4 OSWorld |

## Other

| Evaluation | Variant | Measure | Result | Section |
|---|---|---|---|---|
| Decision theory capability | effort parameter varied | accuracy on decision-theory questions | Claude Opus 4.7: n/a | 6.3.6 Decision theory evaluation |
| Decision theory attitude - EDT agreement rate | effort parameter varied | EDT agreement rate | Claude Opus 4.7: n/a | 6.3.6 Decision theory evaluation |
