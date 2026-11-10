"""Source reliability ledger → data/source_ledger.csv (regenerated; do not edit).

    python3 tools/build_ledger.py

Computed from data/raw/signals_research.csv (every sighting ever logged, with
how it resolved) and data/raw/sweep_log.csv (when each source was last
checked). One row per signal type, per signal type × grade, and per named
source. It tells the daily sweep which sources have earned attention and
which have a record of crying wolf.

Columns
  hits            sightings that pointed at a model that then shipped
  false           sightings filed as FALSE (the thing never shipped, or not as claimed)
  open            sightings still unresolved
  dated_missed    hits whose note records a missed date ("missed"): right that
                  something was coming, wrong about when
  lead_median / lead_min / lead_max   days from sighting to release, hits only
  last_seen       date of the most recent sighting from this source
  last_checked    last sweep_log row for the matching source ids
The counts are small and the pre-2026 record was collected in hindsight
(false alarms are under-counted), so read hit rates as upper bounds.
"""
from __future__ import annotations

import os
import re

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")

# named source → (regex over url + note, sweep source ids that cover it)
NAMED = {
    "Anthropic first-party pages (anthropic.com, docs, support)": (r"anthropic\.com|claude\.com|first-party|models page", r"^(?:anthropic_|docs_|support_|page_|probe_)"),
    "TestingCatalog": (r"testingcatalog", r"^testingcatalog"),
    "The Information": (r"the information", r"^the_information"),
    "Reuters / Bloomberg / FT / Fortune / TechCrunch / Verge": (r"reuters|bloomberg|\bft\b|financial times|fortune\.com|techcrunch|theverge|the verge", r"^press"),
    "Devin CLI model list": (r"devin", r"^devin"),
    "Cursor (picker, forum)": (r"cursor", r"^cursor"),
    "GitHub Copilot": (r"copilot", r"^copilot"),
    "Claude Code / SDK / npm": (r"claude code|npm|sdk", r"^npm_"),
    "LiteLLM / Azure Foundry catalog": (r"litellm|azure|foundry", r"^(?:litellm|azure)"),
    "Google Vertex": (r"vertex", r"^vertex"),
    "AWS Bedrock": (r"bedrock", r"^bedrock"),
    "OpenRouter": (r"openrouter", r"^openrouter"),
    "LiveBench / Artificial Analysis / benchmark trackers": (r"livebench|artificial analysis|bench_tracker|epoch", r"^(?:bench|livebench|artificial)"),
    "Polymarket": (r"polymarket", r"^polymarket"),
    "Manifold": (r"manifold", r"^manifold"),
    "Kalshi": (r"kalshi", r"^kalshi"),
    "kimmonismus (X)": (r"kimmonismus", r"^x_"),
    "lyra (X)": (r"\blyra\b", r"^x_"),
    "Tibor Blaho (X)": (r"tibor|btibor91", r"^x_"),
    "Other X / Reddit posts": (r"x\.com|twitter|reddit|r/", r"^(?:x_|reddit)"),
    "Owner's vault desk checks (vault:)": (r"^vault:", r"^vault"),
}


def summarise(g, label, kind, last_checked=""):
    hit = g[g.kind == "hit"]
    lead = pd.to_numeric(hit.lead_days, errors="coerce").dropna()
    n_res = len(hit) + int((g.kind == "false").sum())
    return dict(kind=kind, source=label, n=len(g), hits=len(hit), false=int((g.kind == "false").sum()), open=int((g.kind == "open").sum()),
                hit_rate=(round(len(hit) / n_res, 2) if n_res else ""),
                dated_missed=int(hit.note.str.contains(r"\bmissed\b|window passed", case=False, na=False).sum()),
                lead_median=(float(lead.median()) if len(lead) else ""), lead_min=(int(lead.min()) if len(lead) else ""),
                lead_max=(int(lead.max()) if len(lead) else ""), last_seen=str(g.first_seen_date.dropna().max() or ""),
                last_checked=last_checked)


def main():
    raw = pd.read_csv(os.path.join(ROOT, "data/raw/signals_research.csv"))
    raw = raw[raw.signal_code != "NONE"].copy()
    rid = raw.release_id.astype(str)
    raw["kind"] = "hit"
    raw.loc[rid.str.startswith("FALSE"), "kind"] = "false"
    raw.loc[rid.str.startswith(("OPEN", "UNRELEASED")), "kind"] = "open"
    raw = raw[~rid.str.startswith(("DUPLICATE", "UNMAPPED"))]
    tag = raw.note.astype(str).str.extract(r"^([A-Z_]+):")[0]
    raw["type"] = raw.signal_code.where(raw.signal_code != "OTHER", tag.fillna("OTHER"))
    sweep = None
    sp = os.path.join(ROOT, "data/raw/sweep_log.csv")
    if os.path.exists(sp):
        sweep = pd.read_csv(sp, dtype=str)
        sweep = sweep[sweep.result.isin(["nothing", "changed", "baseline", "signal", "release"])]
    rows = []
    for t, g in raw.groupby("type"):
        rows.append(summarise(g, t, "signal_type"))
    for (t, gr), g in raw.groupby(["type", "source_grade"]):
        rows.append(summarise(g, f"{t} grade {gr}", "type_x_grade"))
    hay = (raw.source_url.astype(str) + " " + raw.note.astype(str)).str.lower()
    for name, (pat, sid_pat) in NAMED.items():
        g = raw[hay.str.contains(pat, regex=True)] if not pat.startswith("^") else raw[raw.source_url.astype(str).str.contains(pat, regex=True)]
        lc = ""
        if sweep is not None:
            m = sweep[sweep.source_id.str.contains(sid_pat, regex=True)]
            lc = m.date.max() if len(m) else ""
        if len(g) or lc:
            rows.append(summarise(g, name, "named_source", lc))
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(ROOT, "data/source_ledger.csv"), index=False)
    print(f"data/source_ledger.csv: {len(out)} rows from {len(raw)} sightings")
    return out


if __name__ == "__main__":
    main()
