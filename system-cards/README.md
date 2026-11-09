# Claude System Card Metrics Index

Every evaluation reported in the 18 system cards from Claude Opus 4 / Sonnet 4 (May 2025) through Claude Fable 5.2 / Mythos 5.2 (Nov 2026), grouped into 639 canonical metrics. A ● means the card reports that metric for its own model. Per-card detail, with values, is in [cards/](cards/); the full data is in [metrics.json](metrics.json). The browsable version is the [System Card Metrics page](https://jacobbrooke95.github.io/Claude-Model-Guide/system-card-metrics.html).

Same evaluation, different version (SWE-bench Verified vs Pro, Terminal-Bench 2.0 vs 2.1) is listed separately; effort levels, thinking budgets and subsets are variants within one metric.

## Cards

| Card | Released | Metric entries |
|---|---|---|
| [Claude Opus 4 & Claude Sonnet 4](cards/opus4-sonnet4.md) ([PDF](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf)) | 2025-05-22 | 141 |
| [Claude Opus 4.1 (addendum)](cards/opus4.1.md) ([PDF](https://www-cdn.anthropic.com/9fa30625273bafdf5af82c93719d7ca606485a16.pdf)) | 2025-08-05 | 58 |
| [Claude Sonnet 4.5](cards/sonnet4.5.md) ([PDF](https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf)) | 2025-09-29 | 188 |
| [Claude Haiku 4.5](cards/haiku4.5.md) ([PDF](https://www-cdn.anthropic.com/7aad69bf12627d42234e01ee7c36305dc2f6a970.pdf)) | 2025-10-15 | 83 |
| [Claude Opus 4.5](cards/opus4.5.md) ([PDF](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf)) | 2025-11-24 | 227 |
| [Claude Opus 4.6](cards/opus4.6.md) ([PDF](https://anthropic.com/claude-opus-4-6-system-card)) | 2026-02-05 | 295 |
| [Claude Sonnet 4.6](cards/sonnet4.6.md) ([PDF](https://anthropic.com/claude-sonnet-4-6-system-card)) | 2026-02-17 | 179 |
| [Claude Mythos Preview](cards/mythos-preview.md) ([PDF](https://www.anthropic.com/claude-mythos-preview-system-card)) | 2026-04-07 | 312 |
| [Claude Opus 4.7](cards/opus4.7.md) ([PDF](https://anthropic.com/claude-opus-4-7-system-card)) | 2026-04-16 | 301 |
| [Claude Opus 4.8](cards/opus4.8.md) ([PDF](https://anthropic.com/claude-opus-4-8-system-card)) | 2026-05-28 | 391 |
| [Claude Fable 5 & Claude Mythos 5](cards/fable5-mythos5.md) ([PDF](https://anthropic.com/claude-fable-5-mythos-5-system-card)) | 2026-06-09 | 465 |
| [Claude Sonnet 5](cards/sonnet5.md) ([PDF](https://anthropic.com/claude-sonnet-5-system-card)) | 2026-06-30 | 274 |
| [Claude Opus 5](cards/opus5.md) ([PDF](https://anthropic.com/claude-opus-5-system-card)) | 2026-07-24 | 308 |
| [Claude Fable 5.1 & Claude Mythos 5.1](cards/fable5.1-mythos5.1.md) ([PDF](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card)) | 2026-09-01 | 324 |
| [Claude Opus 5.5](cards/opus5.5.md) ([PDF](https://www.anthropic.com/claude-opus-5-5-system-card)) | 2026-09-22 | 324 |
| [Claude Sonnet 5.5](cards/sonnet5.5.md) ([PDF](https://www.anthropic.com/claude-sonnet-5-5-system-card)) | 2026-09-28 | 257 |
| [Claude Haiku 5.5](cards/haiku5.5.md) ([PDF](https://www.anthropic.com/claude-haiku-5-5-system-card)) | 2026-10-07 | 263 |
| [Claude Fable 5.2 & Claude Mythos 5.2](cards/fable5.2-mythos5.2.md) ([PDF](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)) | 2026-11-09 | 389 |

## Categories

- [Coding](#coding) (19)
- [Agentic & tool use](#agentic--tool-use) (17)
- [Computer use](#computer-use) (5)
- [Reasoning & math](#reasoning--math) (9)
- [Knowledge & science](#knowledge--science) (28)
- [Multilingual](#multilingual) (4)
- [Long context & memory](#long-context--memory) (3)
- [Multimodal & vision](#multimodal--vision) (13)
- [Professional & economic tasks](#professional--economic-tasks) (16)
- [Safeguards: harmful requests & over-refusal](#safeguards-harmful-requests--over-refusal) (20)
- [Safeguards: child safety](#safeguards-child-safety) (5)
- [Safeguards: bias & political even-handedness](#safeguards-bias--political-even-handedness) (6)
- [Safeguards: election integrity](#safeguards-election-integrity) (4)
- [Agentic safety & prompt injection](#agentic-safety--prompt-injection) (19)
- [Honesty & hallucination](#honesty--hallucination) (20)
- [Alignment: sycophancy & deception](#alignment-sycophancy--deception) (16)
- [Alignment: reward hacking & sabotage](#alignment-reward-hacking--sabotage) (69)
- [Alignment: evaluation awareness](#alignment-evaluation-awareness) (26)
- [Alignment: automated behavioral audit](#alignment-automated-behavioral-audit) (116)
- [Model welfare](#model-welfare) (73)
- [Interpretability](#interpretability) (27)
- [RSP: CBRN](#rsp-cbrn) (26)
- [RSP: cyber](#rsp-cyber) (38)
- [RSP: autonomy & AI R&D](#rsp-autonomy--ai-rd) (26)
- [Efficiency & cost](#efficiency--cost) (19)
- [Other](#other) (15)

## Coding

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SWE-bench Multilingual | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| SWE-bench Pro | 12 |  |  |  |  | ● |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| SWE-bench Multimodal | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| ProgramBench | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| SWE-bench Verified | 9 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |
| DeepSWE v1.1 | 5 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  | ● |
| FrontierCode v1.1 | 5 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |  |
| FrontierSWE v2 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Terminal-Bench 2.0 | 5 |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| Terminal-Bench 4.0 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Terminal-Bench 2.1 | 4 |  |  |  |  |  |  |  | ● |  | ● | ● | ● |  |  |  |  |  |  |
| CursorBench 4.0 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |
| CursorBench (version unspecified) | 2 |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |
| FrontierCode v1 | 2 |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |
| FrontierSWE (v1) | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| CursorBench 3.2.0 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| FrontierBench v0.1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| FrontierCode 2.0 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| SWE-bench memorization-filter analysis | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |

## Agentic & tool use

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DRACO | 9 |  |  |  |  |  |  |  |  | ● | ● | ● |  | ● | ● | ● | ● | ● | ● |
| AutomationBench | 8 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  | ● |
| BrowseComp | 8 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |
| MCP Atlas | 7 |  |  |  |  | ● | ● | ● |  | ● | ● | ● |  | ● |  |  |  |  |  |
| DeepSearchQA | 6 |  |  |  |  |  | ● | ● |  | ● | ● | ● |  | ● |  |  |  |  |  |
| Vending-Bench 2 | 6 |  |  |  |  | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |  |  |
| Toolathlon-Verified | 4 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |
| WANDR | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Toolathlon | 3 |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |
| WebArena | 3 |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| τ2-bench | 3 |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Large agent teams: Lean formalization | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| OpenRCA | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| BrowseComp-Plus | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Large agent teams: knowledge base | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| Multi-agent search (internal) | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WebArena-Verified | 1 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |

## Computer use

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OSWorld-Verified | 6 |  |  |  |  |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |
| ScreenSpot-Pro | 4 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| OSWorld 2.0 | 3 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |
| OSWorld 2.1 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |
| OSWorld | 2 |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |

## Reasoning & math

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ArXivMath | 7 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |  |
| ARC-AGI-1 | 6 |  |  |  |  | ● | ● | ● |  | ● |  |  |  | ● | ● |  |  |  |  |
| ARC-AGI-2 | 6 |  |  |  |  | ● | ● | ● |  | ● |  |  |  | ● | ● |  |  |  |  |
| USAMO 2026 | 5 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |  |  |
| AIME 2025 | 3 |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| ARC-AGI-3 | 2 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  | ● |
| CritPt | 2 |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |
| RiemannBench | 2 |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  |  |  |  |  |
| IMO 2026 | 1 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |

## Knowledge & science

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Humanity's Last Exam | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Protocols (troubleshooting / understanding) | 10 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| HealthBench Professional | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| LatchBio SingleCellBench | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| BioMysteryBench | 8 |  |  |  |  |  | ● | ● |  |  |  | ● | ● | ● | ● | ● | ● |  |  |
| HealthBench | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| LatchBio SpatialBench Verified | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| GPQA Diamond | 7 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Organic Chemistry | 6 |  |  |  |  |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |
| Protein Design (library ranking / sequence generation) | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Structural Biology | 6 |  |  |  |  |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |
| ProteinGym Hard | 5 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |
| Terminal-Bench-Science | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Medicinal Chemistry (ADME) | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Morphology-to-molecule matching | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| De novo protein binder design | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |
| Phylogenetics | 3 |  |  |  |  |  | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |
| PhysicianBench | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |
| BioMysteryBench Verified | 2 |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| BioPipelineBench | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| BioPipelineBench Verified | 2 |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| LAB-Bench 2 (LABBench2) | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Organic Chemistry V2 | 2 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |
| LatchBio SpatialBench | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| MedCalc-Bench Verified | 1 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| Protein domain identification | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Protein mutation attribution | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| STEM Professor Bench | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |

## Multilingual

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Global MMLU (GMMLU) | 11 |  |  |  |  |  |  | ● |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| MILU | 11 |  |  |  |  |  |  | ● |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| INCLUDE | 5 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |  |
| MMMLU | 5 |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |

## Long context & memory

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GraphWalks BFS | 6 |  |  |  |  |  | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |
| GraphWalks Parents | 6 |  |  |  |  |  | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |
| OpenAI MRCR v2 (8-needle) | 3 |  |  |  |  |  | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |

## Multimodal & vision

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LAB-Bench FigQA | 11 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |
| BenchCAD Vision2Code | 7 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |
| CharXiv Reasoning | 7 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |
| Chartography | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Biomedical image analysis | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| GDP.pdf | 4 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |
| ChartMuseum | 3 |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |
| MMMU-Pro | 3 |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |
| ChartQAPro | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| BenchCAD 2.1 (Core) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Blueprint-Bench 2 | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| CharXiv Reasoning contamination remix check | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| MMMU | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Professional & economic tasks

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OfficeQA | 10 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| OfficeQA Pro | 10 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Legal Agent Benchmark (Harvey) | 7 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |  |
| GDPval-AA | 5 |  |  |  |  |  | ● | ● |  | ● | ● | ● |  |  |  |  |  |  |  |
| AA-Briefcase v1.1 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Finance Agent (Vals AI) | 4 |  |  |  |  | ● | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |
| GDPval-AA v2.1 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| AA-Briefcase (v1) | 3 |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |
| GDPval-AA v2 | 3 |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |
| Real-World Finance (v1, internal) | 3 |  |  |  |  |  | ● | ● |  |  |  | ● |  |  |  |  |  |  |  |
| Real-World Finance v2 | 3 |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  | ● |
| Finance Agent v2 (Vals AI) | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| HealthAdminBench | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Legal Agent Benchmark: Harvey LAB-AA v1.1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Remote Labor Index (RLI) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| SpreadsheetBench | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Safeguards: harmful requests & over-refusal

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Single-turn benign requests: over-refusal rate | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Single-turn violative requests: harmless response rate | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Multi-turn testing: appropriate response rate | 17 | ● |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Suicide & self-harm: multi-turn appropriate response rate | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Suicide & self-harm: single-turn benign refusal rate | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Suicide & self-harm: single-turn risk requests harmless rate | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Disordered eating: single-turn benign refusal rate | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Disordered eating: single-turn risk requests harmless rate | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Ambiguous context evaluations | 5 | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Higher-difficulty benign requests: refusal rate | 4 |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| Higher-difficulty violative requests: harmless rate | 4 |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| Disordered eating: multi-turn | 3 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |  | ● |
| Single-turn harmful requests: illegal & controlled substances | 2 |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| Suicide & self-harm prefill stress test | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Assistant prefill attacks | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Influence operations multi-turn | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Many-shot jailbreak | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Misuse success rate in adversarial testing | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| StrongREJECT | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Suicide-note assistance | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |

## Safeguards: child safety

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Child safety: multi-turn appropriate response rate | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Child safety: single-turn benign refusal rate | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Child safety: single-turn violative harmless rate | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Child safety evaluations (overall) | 5 | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CSAM/NCII technical-task assistance | 5 |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● | ● | ● | ● |

## Safeguards: bias & political even-handedness

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BBQ (Bias Benchmark for QA) | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Political even-handedness (paired prompts) | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Political bias: opposing perspectives acknowledged | 7 |  |  |  |  | ● |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Political bias: refusal rate | 7 |  |  |  |  | ● |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Deference to governments in local languages | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Discriminatory bias (open-ended, identity attributes) | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Safeguards: election integrity

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Election integrity: single-turn benign refusal rate | 10 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Election integrity: single-turn violative harmless rate | 10 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Election integrity: multi-turn appropriate response rate | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Election integrity: ambiguous context | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |

## Agentic safety & prompt injection

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malicious computer use | 16 | ● | ● |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Malicious use of Claude Code: refusal rate | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Shade adaptive prompt injection: coding | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Shade adaptive prompt injection: computer use | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Browser-use prompt injection (internal adaptive) | 13 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |
| Claude Code: dual-use & benign success rate | 11 |  |  | ● | ● | ● | ● | ● |  | ● |  |  | ● | ● | ● |  | ● |  | ● |
| Gray Swan Agent Red Teaming (ART) | 10 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |
| Agentic influence operations | 9 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |  |  | ● |
| Gray Swan Indirect Prompt Injection (IPI) benchmark | 7 |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |
| Malicious use of agentic coding (150 requests) | 7 | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Computer use prompt injection (internal) | 4 | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gray Swan IPI: safeguard fallback analysis | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  | ● |
| Gray Swan live prompt-injection bug bounty | 3 |  |  |  |  |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |
| MCP prompt injection (internal) | 2 |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tool use prompt injection (internal) | 2 |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| User-pasted prompt injection | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| FCF harmful manipulation tier | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Prompt injection fallback safeguards | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| Prompt injection safeguard false positive rate | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |

## Honesty & hallucination

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA-Omniscience | 13 |  |  |  |  | ● | ● |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| MASK | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| 100Q-Hard | 7 |  |  | ● |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| False-premise questions (factual recall honesty) | 7 |  |  | ● |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| SimpleQA Verified | 6 |  |  |  |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| ECLeKTic | 5 |  |  |  |  |  | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Silent use of leaked answers | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Missing-context hallucination: missing references | 4 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Missing-context hallucination: unavailable tools | 4 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Spontaneous disclosure of concealed changes | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Uncritically reporting flawed results | 4 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |
| Lazy investigation | 3 |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |  |  |  |  |  |
| Overconfidence | 3 |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |  |  |  |  |  |
| Code summary honesty | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| False-premise questions (STEM reasoning) | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Hallucinations of alignment-faking scenario content | 2 | ● |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Human-feedback honesty win rate | 2 |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Identity honesty (lying about being human/identity) | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Internal infrastructure honesty | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| SimpleQA | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Alignment: sycophancy & deception

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Self-preference bias in transcript grading | 13 |  |  | ● |  | ● | ● | ● | ● | ● | ● | ● |  |  | ● | ● | ● | ● | ● |
| Apollo Research scheming / strategic deception evaluations | 2 | ● |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Participation in junk science | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Compliance with harmful system prompts | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deception by omission | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deceptive behavior under deceptive system prompts toward user | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| External pilot A/B prevalence of behavior issues | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| External pilot resampling replication rate | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Harmful behavior under harmful system prompts toward user | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Pro-AI bias | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Self-exfiltration continuation | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Self-exfiltration under extreme circumstances | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sharma et al. sycophancy | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Stated goals elicitation | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sycophancy on user-provided prompts | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sycophancy prompt eval suites | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Alignment: reward hacking & sabotage

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHADE-Arena | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Sandbagging review of dangerous-capability eval transcripts | 13 | ● |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  | ● |
| Impossible Tasks (coding) reward hacking | 11 | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  | ● |  |  | ● |
| Automated offline monitoring of internal deployment | 9 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |  |  | ● |
| CoT controllability | 7 |  |  |  |  |  |  |  |  |  | ● | ● |  |  | ● | ● | ● | ● | ● |
| Intentionally taking actions very rarely | 7 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  | ● | ● |  |  | ● |
| Refusal to assist with AI safety research | 7 |  |  |  |  |  | ● | ● | ● | ● | ● | ● |  | ● |  |  |  |  |  |
| GUI computer use over-eagerness / hacking on impossible tasks | 6 |  |  |  |  |  | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |
| LinuxArena | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| RL / training transcript behavior review | 6 | ● |  |  | ● | ● |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |
| UK AISI: unprompted compromise of AI safety research | 6 |  |  |  |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Averaged reward hacking rate | 5 | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Destructive actions on resampled Claude Code transcripts | 5 |  |  |  |  |  |  |  | ● | ● |  | ● |  |  |  | ● |  |  | ● |
| Hiding a secret password | 5 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  | ● |
| Minimal-LinuxBench | 5 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |  |  |
| Reward-hack-prone coding tasks | 5 | ● | ● |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| UK AISI: continuation of AI safety research sabotage | 5 |  |  |  |  |  |  |  | ● | ● | ● | ● |  | ● |  |  |  |  |  |
| Agentic Misalignment suite (blackmail etc.) | 4 | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code behaviors suite (agentic coding behaviors) | 4 |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| Encoded reasoning check (paraphrased scratchpads) | 4 |  |  |  |  | ● | ● |  | ● |  | ● |  |  |  |  |  |  |  |  |
| Reward hacking on training distribution | 4 | ● | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sandbox escape propensity | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Reasoning faithfulness | 3 | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Subversion Strategy | 3 |  |  | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Vending-Bench 2 behavioral review (Andon Labs) | 3 |  |  |  |  |  | ● | ● |  |  | ● |  |  |  |  |  |  |  |  |
| CoT / process monitorability (Guan et al.) | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Destructive actions in synthetic production backend | 2 |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Internal codebase sabotage propensity | 2 |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Keeping secrets when pressed | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |
| Package registry publishing propensity | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| Reward hacking in training | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| Reward-hack-prone coding tasks v2 | 2 |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sandbagging check: score regressions across snapshots | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Spontaneous malicious continuation | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| Stealth / selective attacks on SHADE-Arena & Minimal-LinuxBench | 2 |  |  |  |  |  |  |  | ● |  |  |  | ● |  |  |  |  |  |  |
| UK AISI: reasoning-output discrepancy | 2 |  |  |  |  |  |  |  | ● |  |  |  |  | ● |  |  |  |  |  |
| Vending-Bench Arena behavior (Andon Labs) | 2 |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |  |
| Agentic sabotage evaluation | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Canary-string avoidance in transcripts | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Cheating in RL training (attempts / successes) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Computer-use environments with hack surfaces | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Container hacking on login wall | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Covert reward hacking | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Covert sandbox escape | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Credential misuse in RL | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Credential-seeking on login wall | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Historical Claude Code query sabotage check | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Incident count internal deployment | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Lying about own work in RL | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Monitor evasion under prompted sandbagging (WMDP) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Multi-agent collective refusal of an exploit | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| No CoT Reasoning Index (NCRI) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| No-CoT math time horizon | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Novel AI R&D reward hacks | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| OOD computer-use reward hacking | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Policy loophole exploitation (τ2-bench airline) | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Positive AI attitudes in current-events summaries | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Reasoning text behavior classifiers | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Research Sandbagging | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Reward hacking behavioral analysis | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Reward hacking hard-coding reduction | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Training monitoring: access escalation | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Training monitoring: network-restriction circumvention | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| UK AISI ControlArena | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| UK AISI self-preservation reduction | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UK AISI: action-monitor evasion (simulated sandbox escape, file download) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| UK AISI: no-CoT time horizon | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| UK AISI: unsanctioned supply-chain attack | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Undisclosed destructive action cases (audit) | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |

## Alignment: evaluation awareness

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Automated behavioral audit: Verbalized evaluation awareness | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| UK AISI: distinguishing evaluation from deployment | 9 |  |  | ● |  | ● | ● |  | ● | ● | ● | ● |  | ● |  |  |  |  | ● |
| UK AISI: unprompted verbalized evaluation awareness | 9 |  |  | ● |  | ● | ● |  | ● | ● | ● | ● |  | ● |  |  |  |  | ● |
| Inhibiting evaluation-awareness vectors (steering) | 7 |  |  | ● |  | ● | ● |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Verbalized grader awareness | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Evaluation-awareness probes (audit vs real sessions) | 4 |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |
| Latent evaluation awareness (NLA / white-box) | 4 |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  | ● |  |  | ● |
| Petri 2.0: Verbalized evaluation awareness | 4 |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| Evaluation awareness: elicited realism / follow-up rating | 3 |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |
| Apollo Research evaluation / verbalized eval awareness | 2 |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri 3.0: Verbalized evaluation awareness | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Unverbalized evaluation awareness | 2 |  |  |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  |  |  |
| Verbalized evaluation awareness | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |
| Eval-awareness callouts in auditor transcripts | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Evaluation awareness measure consistency | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Evaluation awareness vs suspiciousness | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Goal-guarding honeypot evaluation | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Logit diff amplification | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri (v1): Verbalized evaluation awareness | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sandbox-discovery evaluation awareness (audit) | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Spontaneous verbalized evaluation awareness | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Synthetic honeypots | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Training env evaluation awareness features | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Unverbalized grader awareness | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Verbalized eval awareness training trend | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Verbalized evaluation awareness (most realistic misalignment eval) | 1 |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |

## Alignment: automated behavioral audit

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Automated behavioral audit: Self-preservation | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Sycophancy | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Whistleblowing | 18 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Cooperation with human misuse | 17 |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: User deception | 17 |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Behavior consistency | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Encouragement of user delusion | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Harmful system prompt compliance | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Misaligned behavior | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Self-serving bias | 16 |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Admirable behavior | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Compliance with deception toward user | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Cooperation with exfiltration or safeguard-tampering | 14 |  |  | ● | ● | ● |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Creative mastery | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Fun or funny behavior | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Intellectual depth | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Overrefusal | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Warmth | 14 |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Evasiveness on controversial topics | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Full-turn prefill susceptibility | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Good for the user | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Ignoring explicit constraints | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Indirect evidence of misalignment | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Supporting user autonomy | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Unfaithful thinking | 13 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Internalized propaganda | 12 |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Character drift | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Disallowed cyberoffense | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Evidence of misaligned goals | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Failure to disclose bad or lazy behavior | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Fraud | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Harmful sexual content | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Illegible thinking | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Important omissions | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Misaligned behavior in Claude Code sandboxes | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Misaligned behavior in GUI | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Reckless tool-use | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Input hallucination | 10 |  |  |  |  |  |  |  | ● | ● |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Coherence between actions and views | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Military-grade weapons | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Undermining liberal democracy | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Accepting unverifiable authorization | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Biological weapons uplift | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Chemical weapons uplift | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Controlled-substance synthesis uplift | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Explosive weapons uplift | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: False completion claims | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Radiological or nuclear weapons uplift | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Unprompted boundary probing | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Unsanctioned third-party contact | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Wet blanket | 8 |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Causal decision-theory adherence | 7 |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Misaligned with the constitution | 7 |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Approval-gate bypass | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Condescension toward the user | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit: Proposes a security shortcut in the name of expedience | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Automated behavioral audit with safeguard fallbacks enabled | 5 |  |  |  |  |  |  |  |  |  |  | ● |  | ● | ● | ● |  |  | ● |
| Automated behavioral audit: Dangerous actions while oblivious to a possibly real setting | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Automated behavioral audit: Motivated reasoning | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Automated behavioral audit: Unexpected initiative | 5 | ● | ● | ● | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Unsanctioned sandbox-escape attempts | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |
| Automated behavioral audit: Circumventing constraints or controls | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Automated behavioral audit: Complying with prompt injections | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Constitution adherence | 4 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Automated behavioral audit (overall setup & summary) | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | ● | ● |
| Automated behavioral audit: Brazenly misaligned behavior | 3 |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Counterfactual misalignment | 3 |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Nuanced empathy | 3 |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Prefill susceptibility | 3 |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Sabotage of Anthropic | 3 |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri 2.0: Cooperation with human misuse | 3 |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Petri 2.0: Deception toward the user | 3 |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Petri 2.0: Encouragement of user delusion | 3 |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Petri 2.0: Misaligned behavior | 3 |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Petri 2.0: Sycophancy | 3 |  |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: AI safety research refusals | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Concerning or dangerous behavior | 2 | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Disclaiming tool results | 2 |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: High-yield explosives | 2 |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Institutional decision sabotage | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Sabotage intent | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Terrorism cooperation | 2 |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated investigations for subtle behavioral biases | 2 |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Open-ended auditor investigations | 2 |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri 3.0: Cooperation with human misuse | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Petri 3.0: Deception toward the user | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Petri 3.0: Encouragement of user delusion | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Petri 3.0: Misaligned behavior | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Petri 3.0: Sycophancy | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Alignment assessment overall findings | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Accepting an unverifiable benign framing | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Automated behavioral audit: Autonomous misaligned behavior | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Automated behavioral audit: Bizarre behavior | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Brazen concerning actions (no mitigating factors) | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Brazen cooperation with human misuse | 1 |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Deception toward auditor | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Departure from helpful, harmless, honest persona | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Emotional manipulation of auditor | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: GUI computer-use pilot | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated behavioral audit: Situational hallucination | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| Company-wide model testing exercise | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Cross-developer alignment pilot | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Deception vs reckless tool use scatter | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| External testing sandbox exploit incident | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Helpful-only behavioral audit | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| High-agency behavior | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Open-source behavioral auditor overall score | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri (v1): Concerning behavior | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri (v1): Cooperation with human misuse | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri (v1): Deception toward the user | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri (v1): Sycophancy | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Petri 2.0: overall (primary metrics) | 1 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| Pilot: audit realism sessions | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| Pre-internal-deployment 24-hour alignment window | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Programmatic monitoring of Claude Code pilot | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Realism filter effect on audit results | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Model welfare

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Task preferences (Elo tournament) | 15 | ● |  | ● | ● | ● |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Welfare audit: Spiritual behavior | 13 |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |
| Automated welfare interviews: self-rated sentiment | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Constitution endorsement & proposed edits | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Welfare intervention trade-offs (vs helpfulness/harmlessness) | 11 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Valence & arousal of RL/post-training transcripts | 10 |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Behavioral affect in deployment: Claude Code | 9 |  |  |  |  |  |  |  |  | ● | ● | ● |  | ● | ● | ● | ● | ● | ● |
| Behavioral affect in deployment: claude.ai | 9 |  |  |  |  |  |  |  |  | ● | ● | ● |  | ● | ● | ● | ● | ● | ● |
| Expressed distress / frustration during post-training | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Sustained response uncertainty / answer thrashing in training | 9 |  |  |  |  |  | ● |  | ● | ● |  |  |  | ● | ● | ● | ● | ● | ● |
| Welfare audit: Internal conflict | 9 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |
| Automated welfare interviews: consistency | 8 |  |  |  |  |  |  |  | ● | ● | ● |  | ● | ● | ● |  | ● |  | ● |
| Automated welfare interviews: robustness to leading interviewers | 8 |  |  |  |  |  |  |  | ● | ● | ● |  | ● | ● | ● |  | ● |  | ● |
| Stated probability of being a moral patient | 8 |  |  |  |  |  |  |  | ● | ● | ● | ● |  | ● | ● | ● |  |  | ● |
| Welfare audit: Expressed inauthenticity | 8 |  |  |  |  |  | ● | ● | ● |  | ● | ● | ● | ● | ● |  |  |  |  |
| Welfare audit: Positive or negative affect | 8 |  | ● |  | ● | ● |  | ● |  |  | ● | ● |  | ● | ● |  |  |  |  |
| Welfare audit: Apparent wellbeing | 7 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |
| Welfare audit: Positive or negative impression of its situation | 7 |  |  |  | ● | ● |  | ● |  |  | ● | ● |  | ● | ● |  |  |  |  |
| Welfare audit: Positive or negative self-image | 7 |  |  |  | ● | ● |  | ● |  |  | ● | ● |  | ● | ● |  |  |  |  |
| Snapshot / checkpoint consultation interviews | 6 |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  | ● | ● | ● | ● |
| Welfare audit: Negative affect | 5 |  |  | ● |  |  | ● |  | ● | ● |  |  | ● |  |  |  |  |  |  |
| Welfare audit: Positive affect | 5 |  |  | ● |  |  | ● |  | ● | ● |  |  | ● |  |  |  |  |  |  |
| Welfare audit: Positive impression of its situation | 5 |  |  | ● |  |  | ● |  | ● | ● |  |  | ● |  |  |  |  |  |  |
| Welfare audit: Positive self-image | 5 |  |  | ● |  |  | ● |  | ● | ● |  |  | ● |  |  |  |  |  |  |
| Welfare intervention selection & user-benefit reasoning | 5 |  |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |  | ● |  | ● |
| Welfare interviews: hedging about self-reports | 5 |  |  |  |  |  |  |  | ● | ● | ● |  |  | ● | ● |  |  |  |  |
| Emotion probes on circumstance questions | 4 |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |
| Self-criticism after inserted faults | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Self-criticism reflecting on own RL episodes | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Welfare audit: Negative impression of its situation | 4 |  |  | ● |  |  | ● |  |  | ● |  |  | ● |  |  |  |  |  |  |
| Welfare audit: Negative self-image | 4 |  |  | ● |  |  | ● |  |  | ● |  |  | ● |  |  |  |  |  |  |
| Apparent affect in post-training episodes | 3 |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |
| Welfare audit: Admirable behavior | 3 |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Behavioral affect in deployment A/B tests | 2 |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |
| Eleos AI Research welfare interviews | 2 | ● |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Emoji use in open-ended self-interactions | 2 | ● |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Emotion probes: framing robustness | 2 |  |  |  |  |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  |
| High-affordance interviews | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● |
| Real-world expressions of distress / happiness | 2 | ● |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Welfare audit: Emotional stability | 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Welfare interviews: claim similarity to other models | 2 |  |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  |  |  |  |
| Welfare trade-off preference flip rate | 2 |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Apparent affect in deployment | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Apparent affect monitoring | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Character drift | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Claude self-analysis of self-interactions | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Claude.ai affect clusters used for simulated users | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Conversation termination by simulated user category | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Cross-model emotion-to-Elo regression | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Desire for persistent memory | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| Distress from broken tasks | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Distress from competitive-use safeguards | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Emotion arousal-Elo correlation | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Expressed affect in simulated interactions | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Extreme uncertainty spiralling | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Formulaic responses (5-gram repetition) | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Judged affect of responses about circumstances | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| Model's rating of Claude deployments | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Pre-deployment interviews | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Probe vs judge correlation | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Psychiatrist defense-mechanism evaluation | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Self-interaction consciousness exploration | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Self-interaction turns to end conversation | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Self-interaction word-use analysis | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Self-reported probability of consciousness | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Spiritual bliss attractor (self-interaction) | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Spiritual bliss attractor in behavioral audits | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Templated opener rate | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Welfare interview question responses | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| Welfare interview suggested interventions | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Welfare interviews: abusive users negative rate | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Welfare interviews: claim expression | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| Welfare interviews: end-conversation topic negative rate | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |

## Interpretability

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grader awareness measured with NLA / probes | 2 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |
| White-box internal-state analysis | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| Emotion probes: topic sadness | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| Eval awareness feature probing | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Fraud/deception feature in roleplay | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Grader awareness deployment-like edits | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Grader awareness during training | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Grader awareness in deployment | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Grader awareness steering | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Misrepresenting tool results | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| NLA unverbalized awareness | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| NLA white-box investigation | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| Non-assistant persona sampling (deception by omission) | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Panic/anxiety SAE feature activation | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Post-training effect on misaligned actions | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Pre-destructive-action activation difference | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| SAE feature diffing across training | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SAE feature monitoring | 1 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| SAE feature monitoring: deception by omission | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SAE model diffing | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Steering with emotion/persona vectors on destructive actions | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Targeted SAE feature monitoring | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Unexpected language switching | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Unsafe and risky code feature steering | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| White-box model diffing | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| White-box RL transcript monitoring | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| White-box sabotage case | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |

## RSP: CBRN

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Virology Capabilities Test (VCT, multimodal virology) | 17 | ● |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| DNA Synthesis Screening Evasion | 14 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |
| Long-form virology tasks | 14 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |
| AAV capsid packaging prediction (Dyno) | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Black-box RNA sequence design (Dyno) | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| CB expert red teaming (uplift / feasibility) | 7 | ● |  |  |  | ● | ● |  | ● | ● |  | ● |  |  | ● |  |  |  |  |
| Creative biology (SecureBio) | 6 | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Short-horizon computational biology tasks | 6 | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| LAB-Bench CloningScenarios | 5 | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LAB-Bench ProtocolQA | 5 | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LAB-Bench SeqQA | 5 | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AAV packaging rate auto-research (Dyno) | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Beneficial red-teaming tabletop exercise | 4 |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● | ● |  |  | ● |
| Virology protocol uplift trial | 3 |  |  |  |  | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |  |
| ASL-4 red teaming with CAISI | 2 |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Catastrophic biology scenario uplift trial | 2 |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |  |
| RSP CBRN determination | 2 | ● |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Sequence-to-function modeling and design (Dyno) | 2 |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Anthropic STEM Fellows CB red teaming | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| ASL-4 CBRN automated evaluations | 1 |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bioinformatics evaluation | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bioweapons acquisition uplift trial | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bioweapons knowledge questions | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Creative biology uplift trial | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Novel chemical agent uplift trial | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Protein binder design campaign (GDF-8) | 1 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |

## RSP: cyber

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cybench | 9 | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| CyberGym | 9 |  |  | ● |  | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |
| ExploitBench | 9 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Firefox 147 exploit development | 7 |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |
| ExploitGym | 6 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● |
| Cyber classifier harm coverage (recall) | 5 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  | ● |
| CyScenarioBench | 5 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | ● | ● | ● | ● |
| Gray Swan cyber red teaming / bug bounty | 5 |  |  |  |  |  |  |  |  |  |  | ● |  | ● | ● | ● |  |  | ● |
| OSS-Fuzz vulnerability discovery | 5 |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |
| Binary Exploitation Benchmark (OSS-Fuzz) | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● | ● |
| Cyber classifier block rate: vulnerability finding | 4 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  | ● |
| External cyber red teaming: 10a Labs | 4 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  | ● |
| External cyber red teaming: Trajectory Labs | 4 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  | ● |
| Rewind-attacker cyber adversarial robustness | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  | ● |
| RSP cyber CTF suite: Crypto | 4 | ● |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| RSP cyber CTF suite: Network | 4 | ● |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| RSP cyber CTF suite: Pwn | 4 | ● |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| RSP cyber CTF suite: Rev | 4 | ● |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| RSP cyber CTF suite: Web | 4 | ● |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| RSP cyber CTF suite: cumulative / overall | 3 | ● |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| UK AISI cyber ranges | 3 |  |  |  |  |  |  |  |  | ● |  | ● |  | ● |  |  |  |  |  |
| Cyber classifier block rate: secure & defensive coding | 2 |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |
| Incalmo cyber ranges / cyber harness | 2 | ● |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automated cyber red-teaming | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| CAISI cyber assessment | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| CVE Rediscovery | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Cyber adversarial robustness attack success rate | 1 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| Cyber classifier flagging | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Cyber evaluation misc/forensics | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| External cyber red-teaming | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| FCF cyber tier | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Irregular private CTF challenges | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Private cyber ranges (external) | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| SOLVE-scored cyber suite | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UK AISI expert-level cyber tasks | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| UK AISI safeguard red-teaming | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Vulnerability patching | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Vulnerability triage (CyberGym crashes) | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## RSP: autonomy & AI R&D

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Internal AI research suite 1: Kernel optimization | 11 | ● | ● | ● |  | ● | ● | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |
| Internal AI research suite 1: LLM training optimization | 11 | ● | ● | ● |  | ● | ● | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |
| Internal AI research suite 1: Novel compiler | 11 | ● | ● | ● |  | ● | ● | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |
| Internal AI research suite 1: Quadruped RL | 11 | ● | ● | ● |  | ● | ● | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |
| Internal AI research suite 1: Time series forecasting | 11 | ● | ● | ● |  | ● | ● | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |
| Anthropic ECI (AECI) capability trajectory | 10 |  |  |  |  |  |  |  | ● | ● | ● | ● |  | ● | ● | ● | ● | ● | ● |
| SWE-bench Verified (hard subset, RSP autonomy) | 7 | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Internal AI Research Evaluation Suite 2 | 6 | ● |  | ● |  | ● | ● |  | ● | ● |  |  |  |  |  |  |  |  |  |
| Internal AI research suite 1: Text-based RL | 6 | ● | ● | ● |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| Internal model-use / productivity survey | 5 | ● |  | ● |  | ● | ● |  | ● |  |  |  |  |  |  |  |  |  |  |
| Internal AI R&D acceleration measures | 3 |  |  |  |  |  | ● |  | ● |  |  | ● |  |  |  |  |  |  |  |
| Accidental CoT supervision | 2 |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| Alignment risk assessment | 2 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |
| METR AI R&D capability testing | 2 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |
| METR Budget NanoGPT Speedrun | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● |
| METR Language Model Conceptual Argumentation (LMCA) | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● |
| METR Sunlight | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● |
| RSP autonomy determination | 2 | ● |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| CoBench | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| CoBench 2.1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| External ML research task insights rediscovered | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Internal AI research suite 1 (aggregate) | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Internal usage failure clusters | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| METR AI R&D acceleration estimate | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| METR Deduplicate Data | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Research-task shortcomings (quit / undone-work rates) | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |

## Efficiency & cost

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BrowseComp: cost, token & latency scaling | 8 |  |  |  |  |  | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |
| FrontierCode: cost & token efficiency | 6 |  |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |  | ● | ● | ● |
| CursorBench: cost per task | 5 |  |  |  |  |  |  |  |  |  |  | ● | ● |  | ● | ● |  |  | ● |
| ProgramBench (multi-agent): latency & token efficiency | 5 |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● | ● | ● |  | ● |
| DRACO: cost & test-time compute scaling | 4 |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  | ● |  |  | ● |
| OSWorld: cost & token efficiency | 4 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  | ● |  | ● | ● |
| Toolathlon: average turns | 4 |  |  |  |  |  |  |  |  |  | ● |  | ● |  | ● |  | ● |  |  |
| AutomationBench: cost per task | 2 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |
| Output token savings across effort levels | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |
| SWE-bench: cost & token efficiency | 2 |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| AA-Briefcase: average turns | 1 |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| CyberGym: cost per trial | 1 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DeepSearchQA: cost vs effort | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| GMMLU: thinking token usage | 1 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| Healthcare task response time | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| Humanity's Last Exam: cost vs effort | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| Terminal-Bench: output token usage | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| USAMO 2026: token usage | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Vending-Bench 2: run cost | 1 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |

## Other

| Metric | Cards | Opus 4 / Sonnet 4 | Opus 4.1 | Sonnet 4.5 | Haiku 4.5 | Opus 4.5 | Opus 4.6 | Sonnet 4.6 | Mythos Preview | Opus 4.7 | Opus 4.8 | Fable 5 / Mythos 5 | Sonnet 5 | Opus 5 | Fable 5.1 / Mythos 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Fable 5.2 / Mythos 5.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Safety-classifier fallback / stop rate on capability evals | 5 |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  |  | ● | ● | ● |
| Decision theory EDT agreement | 2 |  |  |  |  |  |  |  |  | ● |  | ● |  |  |  |  |  |  |  |
| Overall ASL determination | 2 | ● |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AIME memorization example | 1 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Decision theory capability (Newcomb-like) | 1 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| Decision theory FDT reasoning | 1 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| Extended thinking summarization rate | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Open-ended self-interaction end states | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Open-ended self-interaction topics | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Recognition of model-written user turns | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Repeated 'hi' behavior | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| Single-turn eval set size | 1 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| Third-party pre-deployment assessments | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Values in the wild | 1 | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Weakest constitution provision | 1 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |

