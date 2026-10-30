# Claude pre-release signals: notes

Companion to `signals.csv` (99 rows). Built 2026-10-30 from Jacob's vault (`2-Areas/Claude-Rumors/`, read-only), the `claude-model-guide` repo's release data, and web search. Every row has a URL or a vault path. Rows marked APPROXIMATE in the note column have a bounded date, not an exact one.

## Release-date checks and corrections

| Release | Given | Verified | Basis |
|---|---|---|---|
| Opus 5 | 2026-07-23/24 | **2026-07-24 (Fri)** | Vault briefings 8/4 and 8/11 ("Opus 5 shipped 7/24"), the codename registry, and the system-card index all give 7/24. 7/23 was only Polymarket's same-day leg (78.5%), which resolved NO. |
| Sonnet 5.5 | 9/28 or 9/29 | **2026-09-28 (Mon, about 11 AM PT)** | Platform release notes ("Sonnet 5.5 on 9/28", per the 9/29 briefing feed log), the 9/29 briefing ("shipped Monday"), PREDICTIONS.md and the system-card index. The hub's "9/29" in *Resolved* is wrong. |
| Opus 4.6 | 2026-02-05 | 2026-02-05 confirmed | TestingCatalog's launch article is dated Feb 6. That is the outlet's date, not the release date. |
| Fable 5.1 + Mythos 5.1 | 2026-09-01 | confirmed (Tue, about 9 AM) | 9/2 briefing; TestingCatalog 9/1. |
| Claude 3.5 Haiku | 10/22 announce, 11/04 available | confirmed | Simon Willison; the model guide. |
| Mythos Preview | 2026-04-07 | confirmed as an announcement only. It was never generally available; access came through Glasswing. | Fortune, vault |
| All others in the brief | | consistent with the vault and the model guide | |

**Still unreleased as of the last check (10/27 instrument run): Fable 5.5 (also called "5.2").** The CSV carries 11 of its signals with a blank `release_date`. Treat them as right-censored observations, not as negatives.

## False and failed signals (for likelihood ratios)

1. **Claude 3.5 Opus**: Anthropic said "later this year" on 2024-06-20, and the models page still said so on 10/08. The line was removed on 10/22 and the model never shipped. This is a first-party false positive.
2. **`sonnet-4-8` / Sonnet 4.8**: the 3/31/2026 Claude Code source leak, followed by expected launches at three Code with Claude events. It never shipped; the line jumped from 4.6 to 5.
3. **Numbat**: in the same leak, with zero references afterwards.
4. **Sonnet 5 in "Super Bowl week" (TestingCatalog 2/2/2026)**: a Sonnet (4.6) shipped 15 days later. The Sonnet 5 name shipped 148 days later.
5. **"Opus 5 ships Thursday 7/16"** (unrooted Vertex `claude-opus-5`): eight days late. Dan McAteer's 7/14 call also missed.
6. **jupiter-v1-p tied to the 5/6 event**: wrong. The probable Opus 4.8 shipped 27 days later.
7. **Fable 5.2/5.5 timing calls**: kimmonismus "end of Sept or early Oct", the Kingy AI tracker "10/6", kie.ai's "launched 9/10", and TestingCatalog/lyra "week of 10/19". All missed.
8. **Market false positive: Polymarket "Next Fable by Oct 24" at 79–88% on 10/14**, after the Azure catalog row appeared. It resolved with no release. The Azure `claude-fable-5-5` row itself is the only CLOUD_CATALOG artifact without a shipped model, 17+ days on.
9. **Unmapped EAP codenames**: churro (2/11), nougat (4/17), snickerdoodle (6/16) and marshmallow (~8/24) never mapped. Five of the six Devin IDs (orzata, odango, verrine, vanilla, boba) were pruned unmapped on 10/23. The desk counted 11+ EAP names against 8 launches from June to October, so roughly half of the names never map.
10. **A/B-routing "Fable 5.2"** from 9/18: still unresolved after 42 days. The "Claude Next under Opus 5.5" routing from 10/11 is also open.
11. **Vague or noise signals**: the Claude-Next pitch deck (Apr 2023), Kalshi Opus 6 at 9¢, the FT's "$3/$15 Opus 4.8" (wrong on spec), and the Oceanus "$80/M" price.
12. **Near-misses that never crossed 50%**: Manifold "frontier system card by 8/31" peaked at 40.2% on 8/27. It resolved NO hours before Fable 5.1 launched.

## Summary statistics (shipped releases only; lead = release − first seen)

All rows (n per code, median / min–max days):

| Code | n | median | range | median, specific=yes only |
|---|---|---|---|---|
| CLIENT_STRING | 19 | 5 | 0–70 | 1 (n=6) |
| TIPSTER | 11 | 10 | 0–88 | 5.5 (n=6) |
| FIRST_PARTY_DOC | 10 | 12.5 | 6–124 | 12.5 (n=6) |
| OTHER (red-team codenames, A/B routing, benchmark listing) | 7 | 9 | 0–32 | — |
| CLOUD_CATALOG | 6 | 9.5 | 0–149 | 9 (n=5) |
| PRESS_REPORT | 6 | 9.5 | 2–332 | 5 (n=2) |
| EAP_PARTNER | 4 | 4.5 | 2–73 | 4 (n=3) |
| MARKET (≥50% for a dated window) | 4 | 13 | 2–47 | 31.5 (n=2) |
| EXEC_TEASE | 1 | 34 | — | — |
| ARENA_CODENAME | **0** | — | — | No Anthropic model was ever documented as an anonymous arena entry, and the vault's P11 resolved NO. |

**Earliest correctly named signal per release** (17 shipped items that have one): median **6 days**. Most fall in the 0–15 day range; the outliers are Sonnet 5 at 149 days (an old Fennec artifact), Opus 5 at 47 (a Manifold market) and Fable 5.1 at 47 (a YouTube title that the tracker itself discarded).

## Patterns worth modelling

- **Specific signals are late.** Client and partner strings that name the model land 0–5 days out: Claude 4 web config 1 day, Opus 4.1 config 1, the `claude-fable-5` leak 1, Factory Droid's Sonnet 5.5 entry 1, LiveBench's melon commit 4, lyra on Opus 5.5 2. Codenamed EAP strings run longer, at 1–29 days (Honeycomb 16, wafer about 29).
- **First-party "coming weeks" means 6–18 days** (Haiku 3: 9, Sonnet 5.5: 6, Haiku 5.5: 15, Fable 5: 12, Glasswing: 18). **"Later this year" means about 124 days or never** (3.5 Haiku vs 3.5 Opus).
- **Red-team planet codenames lead by 6–32 days** (Neptune 9, Neptune v3 32, Neptune v4 4, Jupiter 27, Oceanus 6). They are good evidence that *something* is coming and weak evidence on tier.
- **Cloud catalogs are bimodal**: 0–1 day (the 3.7 Bedrock page, the Opus 4.6 Vertex 403 probe) against 16–149 days (Fennec), plus one censored or false case (the Azure Fable 5.5 row). Don't use them for timing on their own.
- **Dated tipster calls tend to miss by about a week** (Sonnet 5 "week of 6/23", Opus 5 "7/16", Fable 5.5 "week of 10/19"). The same tipsters are often right on the name.
- **Public model IDs never pre-stage** in the SDK, docs, Claude Code binaries or OpenRouter (vault result: 0 of 4, and Claude Code ships no `-eap` strings). A NONE on those surfaces carries almost no information.
- **The record gets denser over time, and the sample is biased by that.** Six releases from 2023–2025 have no signal at all (Claude 2, 2.1, 3.5 Sonnet, 3.5 Sonnet new, Sonnet 4.5, Haiku 4.5). That says more about how little monitoring existed then than about what Anthropic did. TestingCatalog's Claude coverage went from about 5 to about 9 articles a month. Weight by era, or fit only on 2025-H2 onward.
- **2026 launch weekdays**: Tuesday dominates (6 of 12 per the vault). Opus 5 was the only Friday.

## Caveats

- X and Reddit weren't directly readable. Tweet dates come from vault snowflake decodes (for example, Curran's Fable 5.1 post is dated 2026-08-18) or from outlet relays.
- The Sonnet 5.5 "coming weeks" quote is relayed by explainx; I didn't open Anthropic's page for it.
- The decodethefuture "Opus 4.7 roadmap" row (grade C) couldn't be opened, so it is unverified.
- The 2026 market rows come from vault beat briefs, some marked "per brief, not re-fetched".
