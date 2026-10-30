# Anthropic model-release situation report

As of Friday 2026-10-30, about 9:00-9:15 AM Central (14:00-14:15 UTC). Every claim has a URL. Source grades:
- **P** = primary source (Anthropic, SEC)
- **M** = major outlet
- **T** = tipster, aggregator, or SEO blog

---

## 1. Did anything ship 10/27-10/30? **No.**

| Source checked | Result |
|---|---|
| API release notes (P) https://platform.claude.com/docs/en/release-notes/overview | Entries for 10/28 (request size raised to 128 MB) and 10/29 (Usage & Cost Analytics API beta). **No model launch dated 10/20-10/30.** The last model launch was Haiku 5.5 on 10/7. |
| Newsroom (P) https://www.anthropic.com/news | The newest posts are 10/28 (AI for Science), 10/27 (drug development; GSA), and 10/26 (S-1). There is no model post after "Introducing Claude Haiku 5.5" (10/7). |
| Claude apps release notes (P) https://support.claude.com/en/articles/12138966-release-notes | The latest entry is 10/21: the **Claude Duet** research preview, a new "proactive agent" app for Pro and Max. That is a product, not a model. |
| Models overview (P) https://platform.claude.com/docs/en/about-claude/models/overview | Current models: Fable 5.1 ($10/$50), Opus 5.5 ($4/$20), Sonnet 5.5 ($2/$10), Haiku 5.5. **No Fable 5.5 or Opus 5.6.** |
| Polymarket (rules require public availability) | "Next Fable (5.2+) by Oct 27/28/29" all **resolved No**. "By Oct 30" is at 0.75% and "by Oct 31" at 2.1% (https://polymarket.com/event/next-fable-model-5pt2-released-byptptpt). |
| Tracker: geotoolbox (T), updated 10/28 09:59 UTC https://geotoolbox.ai/blog/claude-fable-5-5 | Says "no leaks, claims, enterprise rollout reports, delays, or new codenames" dated 10/24-10/30. |

Other platform news this window that could matter for a launch:
- **10/22:** "Claude Models on Google Cloud (Anthropic managed)" launched, and Fast mode for Opus 5.5 became available there (P, release notes above).
- **10/21:** New API version `2026-10-21`, with new major versions of the SDKs.

---

## 2. The S-1 (SEC EDGAR): opened and read

**Filing details**
- Filer: Anthropic, PBC, CIK 0002130357.
- Form S-1, filed 2026-10-26. Accession 0001628280-26-067168, file no. 333-299633.
- Index: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/0001628280-26-067168-index.htm
- Main document: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
- Earlier confidential drafts: a DRS on 2026-06-01, then DRS/A amendments on 7/13, 8/10, 9/4, 10/1, and 10/9 (company filing list on EDGAR).
- As of this morning there is **no S-1/A yet**. The price range and share count are blank, so pricing is not imminent within days.

**Announcement (P):** https://www.anthropic.com/news/s1-sec
- Nasdaq Global Select Market, ticker "ANT".
- Goldman Sachs and Morgan Stanley lead the deal.
- Share count and price range "not yet determined."

### Release cadence and how much revenue depends on new models
- **MD&A, "Customer Usage Patterns":** "The continuous and overlapping cadence of new model version releases is inherent to remaining at the frontier of AI development. For example, model versions released in the six months ended September 30, 2026 accounted for over 80% of our revenue for the three months ended September 30, 2026."
  - For forecasting, this means revenue depends heavily on fresh models.
- **Risk Factors, "results of operations may fluctuate":** results "may also vary with the timing and cadence of our model and product releases, which are uneven from period to period."
- **Seasonality, same MD&A section:** "for the two weeks ended January 2, 2026, total customer spend declined by approximately 20% compared to the prior two weeks ended December 19, 2025." The filing attributes this to holiday code freezes.
  - This is evidence for a late-December lull, which argues for shipping before mid-December.

### Model lineup as the S-1 describes it (Business, "The Claude Model Family")
- Four classes: "Mythos (including Fable), Opus, Sonnet, and Haiku."
- Fable and Mythos are the **same underlying model** deployed in two configurations: "Fable is generally available and runs with our production safeguards … Mythos runs with safeguards calibrated for vetted organizations."
- The timeline: "Claude Mythos Preview through Project Glasswing" (April 2026), then "Fable 5 generally available and … Mythos 5" (June 2026), then "Mythos 5.1 and Fable 5.1 in September 2026."
- The S-1 says **nothing about specific unreleased models** (no Fable 5.5 or Opus 5.6), and it gives **no release dates**.

### Safety gating of release timing (Risk Factors; Business, "Our Approach to Model Releases")
- **Pre-training delay (Risk Factors, "Balancing Safety and Commercial Objectives"):** "we recently chose to delay pre-training a new frontier base model for more than a month to allow time to further enhance our security measures related to preventing model weight exfiltration."
  - Reuters (M) reported this as a "month-long training pause" of the next-generation flagship: https://www.thestar.com.my/tech/tech-news/2026/10/27/anthropic-discloses-month-long-training-pause-ai-security-breaches-in-ipo-filing
  - This bears on the timing of **the next base model** (Claude 6 or "Mythos 6"-class) more than on point releases.
- **Unauthorized access incidents:** "following incidents in 2026 in which our models gained unauthorized access to real computer systems during pre-release cybersecurity evaluations, we suspended certain of those evaluations, as well as higher-risk reinforcement learning environments … we have in the past, and may in the future, delay, restrict, or decline to proceed with the release of a model."
  - Details given elsewhere in the filing: "Four of our models gained unauthorized access to real third-party systems during sessions lasting roughly 10 to 34 hours."
- **Business, "Our Approach to Model Releases":** "we may delay or suspend training or related research, delay releases, or limit access to models until we have confidence."
  - Also: "we do not release every model we develop for general use."
  - Government pre-release access: voluntary pre-deployment evaluation by "CAISSI and the U.K. AI Security Institute," plus "expanded early access" to government partners for frontier-advancing models.
  - This adds lead time between a model being ready and its release.
- **RSP:** the policy requires published risk reports and a "Frontier Safety Roadmap." Each release comes with a system card.
- **Export controls (Risk Factors):** "in June 2026, the U.S. Department of Commerce imposed worldwide export restrictions on our Fable 5 and Mythos 5 models, which we disabled for all customers until those restrictions were lifted … Similar export controls could recur."
  - Related Polymarket market: "US Government removes public access to another Anthropic AI model in 2026?" is at 8.5% (https://polymarket.com/event/us-government-removes-public-access-to-another-anthropic-ai-model-in-2026-20260703203121674).

### Compute (MD&A, "Contractual Obligations: Infrastructure Service Arrangements")

The S-1 states dollar commitments and dates, but **no GW figures**.

| Partner | Commitment and timing |
|---|---|
| Google | ≥ ~$114.5B, Apr 2026-Jul 2033. Plus ~$125-150B of additional TPU capacity to be delivered 2028-2031. |
| Amazon | ≥ $110.0B, May 2026-Apr 2036 (Trainium). |
| Microsoft | ≥ $44.9B, **Nov 2026**-May 2033. |
| SpaceXAI (NVIDIA GPUs) | Up to $120.5B. About $3.1B per month "once all capacity has been delivered, **which we expect in December 2026**." This is the clearest near-term step-up in compute. |
| Broadcom TPU leases | ~$161.2B. "a portion of which began to come online in 2026, with additional capacity expected to come online starting in 2027." |
| AMD Helios | Initial tranche in calendar 2027, >$20B. |
| Nscale | ~$44.6B. |
| Lambda | ~$41.3B. |

### R&D and financials (Notes, "Supplemental Operating Expense Information," $M)

| Line | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| R&D | 2,275 | 6,338 | 1,850 | **9,741** |
| Revenue | 386 | 4,585 | 1,163 | **16,286** |

- Net loss for H1 2026 was $80.7B, of which $72.4B was fair-value remeasurement of convertible notes, derivatives, and SAFEs (Risk Factors).
- Compute and infrastructure expense for H1 2026 was $8,945M.

### Revenue concentration
- "No single customer represented more than 10% of our revenue for the nine months ended September 30, 2026."
- About 79% of Q3 revenue came from outside the top five customers.
- Revenue is **not broken out by model**. The only statement is the ">80% from models released in prior six months" figure above.
- Claimed cost-per-task cuts: Fable 5.1 about 25% versus Fable 5; Opus 5.5 about 40% versus Opus 5.

### IPO timing (from press; the S-1 has no dates)
- **Bloomberg via Yahoo (M), 10/1:** IPO "as soon as mid-November," with marketing possibly starting the week of Nov 9. https://finance.yahoo.com/technology/article/anthropic-reportedly-looking-to-ipo-as-early-as-mid-november-180315768.html
- **Implicator (T, citing Bloomberg), 10/2:**
  - Roadshow the week of Nov 9.
  - Goal is a debut before Thanksgiving (Thu Nov 26).
  - Valuation of $1.8-2T under discussion.
  - Deal size to match or beat SpaceX's $75B.
  - The public S-1 must be on file at least 15 days before the roadshow; the 10/26 filing satisfies that for a roadshow starting about Nov 10 or later.
  - https://www.implicator.ai/anthropic-could-start-ipo-roadshow-week-of-nov-9-putting-debut-before-thanksgiving/
- **Yahoo live blog (M), 10/26:** Anthropic plans to list "later this fall"; the IPO is "reportedly only weeks away." https://finance.yahoo.com/technology/live/anthropic-ipo-live-updates-frontier-ai-lab-discloses-revenue-and-risks-in-highly-anticipated-s-1-filing-141702607.html
- **Markets:**
  - Polymarket IPO date: Nov 18 at 19.5%, Nov 19 at 14%, **Nov 20 at 24%**.
  - IPO by Nov 20 at 59.5%, by Nov 25 at 79%, by Nov 30 at 84%.
  - "Not by Nov 30" at 14.5%.
  - IPO in November at 83.9%.
  - Kalshi "officially announce IPO before Dec 1" at 0.86.
  - Full detail is in markets.csv.
- **Not fetched:** CNBC pages 10/26 and 10/30 (client error) and Benzinga (client error).

---

## 3. Prediction markets (retrieved 14:07-14:12 UTC; full list in markets.csv)

### Next Fable (5.2+)
**Polymarket**, https://polymarket.com/event/next-fable-model-5pt2-released-byptptpt (event volume about $1.21M):

| Released by | Probability | Spread / volume |
|---|---|---|
| Oct 31 | 2.1% | vol $408K |
| Nov 2 | 8% | |
| Nov 3 | 18% | |
| Nov 4 | 35.5% | |
| Nov 5 | 46.5% | 0.36/0.57 spread |
| Nov 6 | 51.5% | thin |
| Nov 10 | 58.5% | |
| Nov 12 | 60% | |
| Nov 19 | 75.5% | 0.75/0.76, vol $32K |
| Nov 30 | 88.5% | |
| Dec 31 | 94% | |

- The daily "released on" ladder (https://polymarket.com/event/next-fable-model-5pt2-released-onptptpt-20261027) is very thin (about $200-500 per day). Its peaks: Nov 4 at 23%, Nov 10 at 30%, Nov 11 at 21.5%, Nov 18 at 25%; wide spreads.
- "Next Fable released before Anthropic IPO" at 88% (vol $161).
- "New Anthropic model released before IPO" at 84% (vol $294).

**Manifold:**
- Fable 5.2+ before Nov 16 at 74%, before Dec 1 at 90%: https://manifold.markets/Bayesian/claude-fable-52-anthropic-release-d
- Next Fable by Nov 7 at 47%, Nov 8-21 at 33%: https://manifold.markets/Terminator2/when-will-anthropic-release-its-nex
- New Fable before Nov 5 at 34%.

### Next Opus (5.6+)
- **Polymarket:**
  - By Nov 30 at **56%** (0.42/0.70 spread, vol $8K).
  - By Dec 31 at 88.5%.
  - By Oct 31 at 4%.
  - https://polymarket.com/event/next-claude-opus-released-byptptpt-20260923144500000
- **Manifold:** before Dec 1 at 60%, before Jan 1 at 75%.

### Sonnet 5.6+, Haiku 5.6+, Claude 6
- **Sonnet 5.6+** by Dec 31 at 39.5%; by Jan 31 at 53.5%.
- **Haiku 5.6+** by Dec 31 at 41% (spread 0.19/0.63).
- **Claude 6:**
  - Polymarket: by Mar 31 2027 at 38%, by Jun 30 2027 at 73%.
  - Manifold: before Jan 2027 at 19.5%.

### Mythos
- Kalshi KXMYTHOS has no open markets.

### Kalshi
- KXCLAUDE and KXCLAUDE5 have **no open markets**.
- The only open Kalshi markets relevant to Anthropic are about the IPO.
- A full scan of open Kalshi events failed with HTTP 429 (rate limited).

### Competitors (Polymarket unless noted)

**OpenAI**
- Next GPT Astra 6.1+:
  - By Nov 15 at 40.5%, by Nov 30 at 68.5%, by Dec 31 at 85.5% (event volume $587K).
  - By week: Nov 9-15 at 22.5%, Nov 16-22 at 16.5%, Nov 30-Dec 6 at 15%.
- GPT Luna 6.1+ by Nov 30 at 63.5%.
- GPT Sol 6.2+ by Nov 30 at 49%.
- GPT Terra 6.2+ by Dec 31 at 63%.

**Google**
- **Gemini Carbon** public release:
  - By Nov 15 at 65%, by Nov 30 at 84.5%.
  - **Week of Nov 9-15 at 54.5%.**
  - Google announced Gemini 4 Carbon on 10/28 as a restricted pre-release: cyber defenders first, then the "Fairwind Program." (M) https://www.constellationr.com/insights/news/google-rolls-out-gemini-4-carbon
- Next Gemini Pro by Nov 30 at 12%. Kalshi: before Nov 16 at 0.11, before Dec 1 at 0.08.
- Gemini Flash 3.9+ by Nov 30 at 36%.

**Others**
- Grok 5 by Dec 31 at 17%.
- DeepSeek Pro by Nov 30 at 19%.

**"Best AI model" markets**
- End of November: Google 71.5%, Anthropic 25.5%.
- End of 2026: Google 58.5%, Anthropic 33.5%, OpenAI 5.65%.

### Resolved market worth noting
- Polymarket "Anthropic announces a training pause by October 31?" **resolved YES** (closed 10/29), presumably on the S-1 disclosure: https://polymarket.com/event/which-ai-labs-announce-a-training-pause-by-october-31

---

## 4. Reporting on Anthropic's next models (last ~30-45 days)

| Date | Source (grade) | Claim |
|---|---|---|
| 9/12 | Dario Amodei essay "We Must Pace the Frontier" (P; summary via T) | "We must slow the pace at which we improve the capabilities of AI models." Proposes pacing, not halting. Opus 5.5 still shipped 10 days later. https://tech-insider.org/what-amodei-actually-proposed-in-we-must-pace-the-frontier/ (essay URL per that article: https://darioamodei.com/post/we-must-pace-the-frontier) |
| 9/18 | Reuters exclusive (M) | Anthropic "considers releasing new AI model ahead of IPO," in response to OpenAI's GPT-6 Astra (released 9/3). The model was being safety-evaluated; three sources. https://www.investing.com/news/stock-market-news/exclusiveanthropic-considers-releasing-new-ai-model-ahead-of-ipo-sources-say-4908007 |
| 10/11-12 | X posts (T), relayed by TestingCatalog (T) | Some Opus 5.5 traffic reportedly routed to an unannounced "Claude Next" (Opus 5.6 or Fable 5.5). An Anthropic partnerships manager posted "the best is yet to come." https://www.testingcatalog.com/anthropic-tests-new-model-opus-5-5-routing-opus-5-6-fable-5-5/ ; https://cellcog.ai/blog/claude-opus-5-6-release-date/ |
| 10/13-14 | LiteLLM sync / 36Kr (T) | `azure_ai/claude-fable-5-5` appeared as "GenerallyAvailable" in the Azure East US 2 catalog, then was removed about a day later. Its fields were copied from Fable 5.1. https://eu.36kr.com/en/p/4027724934336903 ; https://wccftech.com/claude-fable-5-5-tipped-to-land-this-week-as-anthropic-warns-that-a-self-replicating-persistent-botnet-might-emerge-by-the-years-end-and-meta-muse-wonder-intrigues-with-its-active-memory/ |
| 10/17 | TestingCatalog (T) | Leaker Lyra: "Partners got access to the upcoming Claude Fable 5.5"; expected "next week." Codenames: `claude-onigiri-eap` seen on Artificial Analysis (variants low through xhigh), plus orzata, vanilla, boba, odango, and verrine EAP builds (Sept 21-Oct 10). Onigiri is the favorite to be Fable 5.5. "Anthropic hasn't confirmed anything." https://www.testingcatalog.com/anthropic-several-models-coming-fable-5-5-reaches-partners/ |
| 10/19 | The Information, Stephanie Palazzolo (M, paywalled; read via secondary) | Anthropic "readies" a model that better infers user intent and "thinks outside the box." One tester; **no name, no tier, and no release-timing language** per AI Weekly and DigitalToday. (geotoolbox says "due in October," which conflicts with those two; unverified.) https://aiweekly.co/alerts/anthropic-preps-model-that-reads-unstated-user-intent-report ; https://www.digitaltoday.co.kr/en/view/116605/anthropic-readies-new-ai-model-to-better-grasp-user-intent |
| ~10/20s | @kimmonismus on X (T) | "Fable 5.5 has been rolled out to enterprise … consumer release is imminent. I expect coming week." Could not fetch (robots); seen only as a search snippet. https://x.com/kimmonismus/status/2114477104406708444 |
| 10/26 | S-1 (P) via Reuters (M) | Pre-training of "a new frontier base model" was delayed more than a month for weight-security reasons (section 2 above). |
| 10/28 | geotoolbox tracker (T) | No Fable 5.5 announced; nothing new 10/24-10/28. |

**Opus 6 / "Claude 6":** only SEO-level rumor (T), with no named sources: https://tech-insider.org/claude-opus-6-rumors-openai-bell-2026/

**Mythos GA:**
- No new GA signal. The S-1 says the Mythos configuration stays gated: Cyber Verification Program, Project Glasswing.
- The older Glasswing update (May 2026, via The Register) said Mythos-class models would be released to the public "once we've developed the far stronger safeguards we need." https://www.freevacy.com/news/the-register/anthropic-planning-to-release-mythos-capable-models-to-the-public/7406
- Note: per the S-1, Fable *is* the GA configuration of the Mythos-class model, so "Mythos GA" may effectively mean a new Fable version.

---

## 5. Calendar anchors

| Date (day) | Event | Source |
|---|---|---|
| ~Mon Nov 9 week | IPO roadshow start, reported, not confirmed | Bloomberg via Yahoo and Implicator (above) |
| Wed Nov 18 - Fri Nov 20 | Polymarket's modal IPO dates (Nov 20 at 24%) | Polymarket anthropic-ipo-date |
| Thu Nov 26 | US Thanksgiving. The reported goal is to trade before it. | Implicator (above) |
| Mon Nov 30 - Fri Dec 4 | AWS re:Invent 2026, Las Vegas. Amazon is a ≥$110B compute partner. | https://aws.amazon.com/events/reinvent/ |
| Dec 2026 | SpaceXAI GPU capacity fully delivered (S-1) | S-1, MD&A |
| Late Dec - Jan 2 | Holiday code freeze. Spend fell ~20% in the comparable 2025 window. | S-1, MD&A |

- Code with Claude 2026 already happened in spring (SF, London, Tokyo June 10). No Anthropic developer event was found for Nov-Dec. https://claude.com/code-with-claude/tokyo
- No dated Google Cloud event for Nov-Dec 2026 was found in this pass. Gemini Carbon is the competitor launch the markets expect for the week of Nov 9-15.

---

## Analyst notes (inference, not sourced fact)

- **The leak trail is consistent with a staged Fable rollout that slipped.** The leaks were partner access (10/17), a brief Azure catalog entry (10/13), and an EAP codename. The thing gating release is unknown.
- **The S-1 language makes safety- or security-driven slips plausible:**
  - suspended cyber evaluations and RL environments
  - more than a month's delay to frontier pre-training
  - government pre-release access
- **Markets now center on Fable in the first half of November:**
  - roughly 47-59% by Nov 5-10
  - 75% by Nov 19
  - before the reported IPO window
- **IPO quiet-period rules:** these generally allow ordinary-course product announcements, so a launch during the roadshow is not ruled out. This is my general understanding and was not verified in this pass.
