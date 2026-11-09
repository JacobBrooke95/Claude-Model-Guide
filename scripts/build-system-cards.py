#!/usr/bin/env python3
"""Rebuild the derived system-card files from system-cards/metrics.json.

metrics.json is the source of truth; card-order.json records the row order of
each card page (see card_rows). This script writes:

  system-cards/index.json   compact form fetched by system-card-metrics.html
  system-cards/README.md    card table plus a metric x card matrix per category
  system-cards/cards/*.md   one page per card

Usage:  python3 scripts/build-system-cards.py [--check]

--check writes nothing and exits 1 if any derived file is out of date.
Standard library only.
"""
import json
import os
import sys
from datetime import date

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "system-cards")

# Source PDF for each card. A card in metrics.json may carry its own "url",
# which wins over this table.
CARD_URLS = {
    "opus4-sonnet4": "https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf",
    "opus4.1": "https://www-cdn.anthropic.com/9fa30625273bafdf5af82c93719d7ca606485a16.pdf",
    "sonnet4.5": "https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf",
    "haiku4.5": "https://www-cdn.anthropic.com/7aad69bf12627d42234e01ee7c36305dc2f6a970.pdf",
    "opus4.5": "https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf",
    "opus4.6": "https://anthropic.com/claude-opus-4-6-system-card",
    "sonnet4.6": "https://anthropic.com/claude-sonnet-4-6-system-card",
    "mythos-preview": "https://www.anthropic.com/claude-mythos-preview-system-card",
    "opus4.7": "https://anthropic.com/claude-opus-4-7-system-card",
    "opus4.8": "https://anthropic.com/claude-opus-4-8-system-card",
    "fable5-mythos5": "https://anthropic.com/claude-fable-5-mythos-5-system-card",
    "sonnet5": "https://anthropic.com/claude-sonnet-5-system-card",
    "opus5": "https://anthropic.com/claude-opus-5-system-card",
    "fable5.1-mythos5.1": "https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card",
    "opus5.5": "https://www.anthropic.com/claude-opus-5-5-system-card",
    "sonnet5.5": "https://www.anthropic.com/claude-sonnet-5-5-system-card",
    "haiku5.5": "https://www.anthropic.com/claude-haiku-5-5-system-card",
    "fable5.2-mythos5.2": "https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card",
}

CATEGORIES = [
    "Coding",
    "Agentic & tool use",
    "Computer use",
    "Reasoning & math",
    "Knowledge & science",
    "Multilingual",
    "Long context & memory",
    "Multimodal & vision",
    "Professional & economic tasks",
    "Safeguards: harmful requests & over-refusal",
    "Safeguards: child safety",
    "Safeguards: bias & political even-handedness",
    "Safeguards: election integrity",
    "Agentic safety & prompt injection",
    "Honesty & hallucination",
    "Alignment: sycophancy & deception",
    "Alignment: reward hacking & sabotage",
    "Alignment: evaluation awareness",
    "Alignment: automated behavioral audit",
    "Model welfare",
    "Interpretability",
    "RSP: CBRN",
    "RSP: cyber",
    "RSP: autonomy & AI R&D",
    "Efficiency & cost",
    "Other",
]

FAMILIES = ["opus", "sonnet", "haiku", "mythos", "fable"]
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def card_url(card):
    return card.get("url") or CARD_URLS[card["id"]]


def card_families(card):
    # in subject order, e.g. ["fable", "mythos"] for a joint Fable/Mythos card
    out = []
    for subject in card["subjects"]:
        for f in FAMILIES:
            if f in subject.lower() and f not in out:
                out.append(f)
    return out


def entry_counts(data):
    counts = {c["id"]: 0 for c in data["cards"]}
    for m in data["metrics"]:
        for cid, entries in m["cards"].items():
            counts[cid] += len(entries)
    return counts


def build_index(data):
    counts = entry_counts(data)
    cards = [
        {
            "id": c["id"],
            "label": c["label"],
            "title": c["title"],
            "date": c["date"],
            "families": card_families(c),
            "url": card_url(c),
            "entries": counts[c["id"]],
        }
        for c in data["cards"]
    ]
    metrics = []
    for m in data["metrics"]:
        by = {}
        for cid, entries in m["cards"].items():
            by[cid] = [
                {
                    "n": e["eval_name"],
                    "v": e["variant"],
                    "m": e["measure"],
                    "s": e["section"],
                    "x": e["notes"],
                    "r": [[r["model"], r["value"], r["setting"]] for r in e["results"]],
                }
                for e in entries
            ]
        metrics.append(
            {
                "id": m["id"],
                "name": m["name"],
                "family": m["family"],
                "cat": m["category"],
                "desc": m["description"],
                "by": by,
            }
        )
    out = {"cards": cards, "categories": CATEGORIES, "metrics": metrics}
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def anchor(heading):
    kept = "".join(ch for ch in heading.lower() if ch.isalnum() or ch in " -")
    return kept.replace(" ", "-")


def month_year(iso):
    d = date.fromisoformat(iso)
    return "%s %d" % (MONTHS[d.month - 1], d.year)


def build_readme(data):
    cards = data["cards"]
    counts = entry_counts(data)
    by_cat = {c: [] for c in CATEGORIES}
    for m in data["metrics"]:
        by_cat[m["category"]].append(m)
    first, last = cards[0], cards[-1]
    L = []
    L.append("# Claude System Card Metrics Index")
    L.append("")
    L.append(
        "Every evaluation reported in the %d system cards from %s (%s) through %s (%s), "
        "grouped into %d canonical metrics. A ● means the card reports that metric for its own model. "
        "Per-card detail, with values, is in [cards/](cards/); the full data is in [metrics.json](metrics.json). "
        "The browsable version is the [System Card Metrics page]"
        "(https://jacobbrooke95.github.io/Claude-Model-Guide/system-card-metrics.html)."
        % (
            len(cards),
            readme_name(first),
            month_year(first["date"]),
            readme_name(last),
            month_year(last["date"]),
            len(data["metrics"]),
        )
    )
    L.append("")
    L.append(
        "Same evaluation, different version (SWE-bench Verified vs Pro, Terminal-Bench 2.0 vs 2.1) is listed "
        "separately; effort levels, thinking budgets and subsets are variants within one metric."
    )
    L.append("")
    L.append("## Cards")
    L.append("")
    L.append("| Card | Released | Metric entries |")
    L.append("|---|---|---|")
    for c in cards:
        L.append(
            "| [%s](cards/%s.md) ([PDF](%s)) | %s | %d |"
            % (c["title"], c["id"], card_url(c), c["date"], counts[c["id"]])
        )
    L.append("")
    L.append("## Categories")
    L.append("")
    for cat in CATEGORIES:
        L.append("- [%s](#%s) (%d)" % (cat, anchor(cat), len(by_cat[cat])))
    for cat in CATEGORIES:
        L.append("")
        L.append("## " + cat)
        L.append("")
        L.append("| Metric | Cards | " + " | ".join(c["label"] for c in cards) + " |")
        L.append("|---|---|" + "---|" * len(cards))
        rows = sorted(by_cat[cat], key=lambda m: (-len(m["cards"]), m["name"].lower()))
        for m in rows:
            marks = ["●" if c["id"] in m["cards"] else "" for c in cards]
            L.append("| %s | %d | %s |" % (cell(m["name"]), len(m["cards"]), " | ".join(marks)))
    return "\n".join(L) + "\n\n"


def readme_name(card):
    # "Opus 4 / Sonnet 4" -> "Claude Opus 4 / Sonnet 4"
    return "Claude " + card["label"]


def result_text(e):
    parts = []
    for r in e["results"]:
        v = "n/a" if r["value"] is None else str(r["value"])
        s = "%s: %s" % (r["model"], v)
        if r["setting"]:
            s += " (%s)" % r["setting"]
        parts.append(s)
    return "; ".join(parts)


def section_key(section):
    nums = []
    for part in section.split(" ")[0].split("."):
        if not part.isdigit():
            break
        nums.append(int(part))
    return nums or [10**6]


def card_rows(data, card, order):
    """Entries of one card as (category, entry), in page order.

    Row order within a category is the order the card was extracted in, which
    metrics.json does not record (it groups entries by metric). card-order.json
    holds it as a list of "<metric id>#<index within that metric>" keys per card.
    Entries missing from that list follow, sorted by section number.
    """
    entries = {}
    for m in data["metrics"]:
        for i, e in enumerate(m["cards"].get(card["id"], [])):
            entries["%s#%d" % (m["id"], i)] = (m["category"], e)
    listed = order.get(card["id"], [])
    unknown = [k for k in listed if k not in entries]
    if unknown or len(set(listed)) != len(listed):
        sys.exit("card-order.json: bad keys for %s: %s" % (card["id"], unknown[:5] or "duplicates"))
    seen = set(listed)
    rest = [k for k in entries if k not in seen]
    rest.sort(key=lambda k: section_key(entries[k][1]["section"]))
    return [entries[k] for k in listed + rest]


def build_card(data, card, order):
    counts = entry_counts(data)
    by_cat = {c: [] for c in CATEGORIES}
    for cat, e in card_rows(data, card, order):
        by_cat[cat].append(e)
    L = []
    L.append("# System Card: " + card["title"])
    L.append("")
    L.append(
        "Released %s. %d metric entries. [Source PDF](%s) · [Back to index](../README.md)"
        % (card["date"], counts[card["id"]], card_url(card))
    )
    for cat in CATEGORIES:
        if not by_cat[cat]:
            continue
        L.append("")
        L.append("## " + cat)
        L.append("")
        L.append("| Evaluation | Variant | Measure | Result | Section |")
        L.append("|---|---|---|---|---|")
        for e in by_cat[cat]:
            L.append(
                "| %s | %s | %s | %s | %s |"
                % (cell(e["eval_name"]), cell(e["variant"]), cell(e["measure"]), cell(result_text(e)), cell(e["section"]))
            )
    return "\n".join(L) + "\n"


def main():
    check = "--check" in sys.argv[1:]
    with open(os.path.join(ROOT, "metrics.json"), encoding="utf-8") as f:
        data = json.load(f)

    ids = [m["id"] for m in data["metrics"]]
    if len(ids) != len(set(ids)):
        sys.exit("duplicate metric ids in metrics.json")
    card_ids = {c["id"] for c in data["cards"]}
    for m in data["metrics"]:
        if m["category"] not in CATEGORIES:
            sys.exit("unknown category %r on metric %s" % (m["category"], m["id"]))
        for cid, entries in m["cards"].items():
            if cid not in card_ids:
                sys.exit("unknown card %r on metric %s" % (cid, m["id"]))
            for e in entries:
                if e["canonical_id"] != m["id"]:
                    sys.exit("canonical_id %r filed under metric %s" % (e["canonical_id"], m["id"]))

    order = {}
    order_path = os.path.join(ROOT, "card-order.json")
    if os.path.exists(order_path):
        with open(order_path, encoding="utf-8") as f:
            order = json.load(f)

    outputs = {"index.json": build_index(data), "README.md": build_readme(data)}
    for c in data["cards"]:
        outputs[os.path.join("cards", c["id"] + ".md")] = build_card(data, c, order)

    stale = []
    for rel, text in outputs.items():
        path = os.path.join(ROOT, rel)
        old = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                old = f.read()
        if old != text:
            stale.append(rel)
            if not check:
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(text)
    total = sum(entry_counts(data).values())
    print("%d cards, %d metrics, %d entries" % (len(data["cards"]), len(data["metrics"]), total))
    print(("out of date: " if check else "rewrote: ") + (", ".join(stale) if stale else "nothing"))
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
