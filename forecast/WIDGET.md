# Forecast widget

A small version of [`release-forecast.html`](../release-forecast.html) for a daily note: one row per family (probability of the next release by the forecast's two near checkpoints, median date, 80% window), the most likely next release in one line, and one line for the voice model. Two forms:

| | Use it when | Trade-off |
|---|---|---|
| **iframe** (`forecast-widget.html`) | You read the note with a network connection | Always matches the site. Needs the network; shows nothing in an exported note or anywhere iframes are not rendered. |
| **Markdown** (`tools/widget_md.py`) | You want the numbers to stay in the note | A permanent record, works offline, searchable. Fixed at the moment it was pasted. |

Both read the same files and round the same way, so they show the same numbers.

## iframe, in an Obsidian daily note

Paste under `## Claude's Update 🦀`. Keep the `<iframe>` on one line with no blank line inside it.

Dated (for a daily log; the note keeps showing the forecast as it stood that day):

```markdown
### Claude Forecast
<iframe src="https://jacobbrooke95.github.io/Claude-Model-Guide/forecast-widget.html?date=2026-11-12" title="Claude release forecast" width="100%" height="260" style="border:0; max-width:720px;" loading="lazy"></iframe>
```

Live (always the latest forecast; for a pinned note or a dashboard):

```markdown
### Claude Forecast
<iframe src="https://jacobbrooke95.github.io/Claude-Model-Guide/forecast-widget.html" title="Claude release forecast" width="100%" height="260" style="border:0; max-width:720px;" loading="lazy"></iframe>
```

Compact (five rows, no bars, no headline):

```markdown
<iframe src="https://jacobbrooke95.github.io/Claude-Model-Guide/forecast-widget.html?date=2026-11-12&compact=1" title="Claude release forecast" width="100%" height="190" style="border:0; max-width:720px;" loading="lazy"></iframe>
```

Dark vault: add `theme=dark`. An iframe cannot see Obsidian's theme, only the operating system's, so `auto` is right only when the two agree.

```markdown
<iframe src="https://jacobbrooke95.github.io/Claude-Model-Guide/forecast-widget.html?date=2026-11-12&theme=dark" title="Claude release forecast" width="100%" height="260" style="border:0; max-width:720px;" loading="lazy"></iframe>
```

### Size

Width `100%`, capped at 720px. It is laid out for 360 to 720px.

| Mode | Height to set | Content height measured at 360px | at 600–720px |
|---|---|---|---|
| default | **260** | 245 | 210 |
| `compact=1` | **190** | 176 | 160 |

The height to set is the phone case plus a margin for font differences, so one snippet works on the iMac, the MacBook and the phone with no inner scrollbar. The background is transparent, so the spare space on a wide screen is just a gap. On a note that is only ever read on a desktop, 225 and 175 are enough. `voice=0` does not change these: the last line still carries the link.

### Options

| Parameter | Values | Effect |
|---|---|---|
| `date` | `YYYY-MM-DD` | Show the snapshot of that day (`history/forecast_<date>.json`). Without it, the latest forecast. |
| `theme` | `light`, `dark`, `auto` (default) | Text and bar colours. `auto` follows the operating system. The background is always transparent. |
| `voice` | `0` | Hide the voice line. |
| `compact` | `1` | Rows only: no headline, no 80% window bars. |

### What a dated widget shows

- **A run that day:** that day's snapshot, unchanged for good.
- **No run that day:** the newest snapshot on or before the date, with the first line reading "No snapshot for Nov 11; showing Nov 10, 2026". If today's note is opened before today's run, it shows yesterday's numbers this way and switches by itself once the run is published.
- **A date before the first snapshot:** the latest forecast, with "No snapshot on or before …".
- **Voice line:** from the voice snapshot on or before the date; left out for dates before the first voice forecast (2026-11-10).

The widget finds snapshots from `forecast_log.csv` and `voice_forecast_log.csv`, which list every origin date, so it never requests a file that does not exist.

### Reading it

- Percentages are the model's own estimate with signals, the big number on each card of the full page. Market prices and the blend are on the full page only.
- ▲6 / ▼3 after a number: it moved that many points against the snapshot before it. Shown only for a move of 3 points or more. A large ▼ usually means the family just shipped a model and the row now refers to the one after it.
- The bar is the 80% window (10th to 90th percentile of the release date) and the tick is the median, on one time axis shared by all rows. Hover, or read the full page, for the dates.
- The voice line is rung A (any Anthropic-built speech model with outside access): the two nearest horizons and the median date.

## Filling in the date from a template

Put the dated snippet in the daily-note template and let the template write the date:

Obsidian core Templates plugin:

```markdown
<iframe src="https://jacobbrooke95.github.io/Claude-Model-Guide/forecast-widget.html?date={{date:YYYY-MM-DD}}" title="Claude release forecast" width="100%" height="260" style="border:0; max-width:720px;" loading="lazy"></iframe>
```

Templater:

```markdown
<iframe src="https://jacobbrooke95.github.io/Claude-Model-Guide/forecast-widget.html?date=<% tp.date.now("YYYY-MM-DD") %>" title="Claude release forecast" width="100%" height="260" style="border:0; max-width:720px;" loading="lazy"></iframe>
```

In a note created for another day, use the note's own date instead: `{{date:YYYY-MM-DD}}` is the day the template is inserted, and in Templater `<% tp.file.title %>` works when the file is named `YYYY-MM-DD`.

## Markdown fallback

For places where an iframe does not render (some mobile views, exported or printed notes, other apps reading the vault) and for a record that stays in the note:

```
python3 forecast/tools/widget_md.py              # the latest forecast
python3 forecast/tools/widget_md.py 2026-11-12   # the snapshot of that day, or the newest one before it
python3 forecast/tools/widget_md.py --heading    # start with "### Claude Forecast"
```

Standard library only; it reads `output/` and `history/` and writes nothing. An automated daily-note writer can paste the output as is. Output on 2026-11-10:

```markdown
### Claude Forecast

*As of Nov 10, 2026 · v3e · [Full forecast →](https://jacobbrooke95.github.io/Claude-Model-Guide/release-forecast.html)*

**Next most likely: Opus — 67% by Dec 31, median Dec 10**

| Next | by Nov 30 | by Dec 31 | Median | 80% window |
|:--|--:|--:|:--|:--|
| Opus | 33% | 67% ▲6 | Dec 10 | Nov 16 – Feb 16 ’27 |
| Sonnet | 12% | 33% | Jan 19 ’27 | Nov 27 – Mar 30 ’27 |
| Haiku | 2% | 4% ▼3 | Jul 13 ’27 | Feb 2 ’27 – Nov 23 ’27 |
| Fable | 4% ▼42 | 18% ▼44 | Feb 1 ’27 | Dec 14 – Apr 7 ’27 |
| Mythos | 4% ▼53 | 19% ▼54 | Jan 27 ’27 | Dec 11 – Mar 30 ’27 |

Voice model (rung A): **9%** by Dec 31 · **25%** by Mar 31, 2027 · median Oct 12, 2027
```

To have both, paste the Markdown block and put the iframe above it.

## Where the numbers come from

| Shown | Field |
|---|---|
| as-of date, model version | `as_of`, `model_version` |
| the two "by" columns | `checkpoints[0..1]`, then `targets.<family>.with_signals.by[<date>]`. They roll forward when the forecast's checkpoints do. |
| median, 80% window | `targets.<family>.with_signals.median`, `.q10`, `.q90` |
| voice line | `rungs.A.by[<date>].final` for the first two `horizons`, `rungs.A.median` |
| ▲/▼ | the same target and checkpoint in the previous origin of `forecast_log.csv` (`p_model`) or `voice_forecast_log.csv` (`p_final`) |

Rounding and date forms follow `page_template.html`: `(100 * p).toFixed(0)`, and the year is written only when it differs from the as-of year.
