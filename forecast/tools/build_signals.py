"""Normalize the researched signal timeline (data/raw/signals_research.csv)
into data/signals.csv: one row per (signal, family), with the target release,
an is_false flag, and an estimation code. MARKET rows are dropped here —
markets enter separately (engine/market.py) so their evidence isn't counted
twice. Unresolved signals ('Claude Next') are kept with blank
release_date and is_false = 0: they are live evidence, not misses."""
import re
import pandas as pd

raw = pd.read_csv("data/raw/signals_research.csv")
rel = pd.read_csv("data/anthropic_releases.csv")

MAP = {
    "Claude 1 + Instant": ["claude1"], "Claude 2": ["claude2"], "Claude 2.1": ["claude21"],
    "Claude 3 Opus/Sonnet": ["opus3", "sonnet3"], "Claude 3 Haiku": ["haiku3"],
    "Claude 3.5 Sonnet": ["sonnet35"], "Claude 3.5 Sonnet (new)": ["sonnet35new"],
    "Claude 3.5 Haiku (announce)": [], "Claude 3.5 Haiku (availability)": ["haiku35"],
    "Claude 3.7 Sonnet": ["sonnet37"], "Claude Opus 4 + Sonnet 4": ["opus4", "sonnet4"],
    "Claude Opus 4.1": ["opus41"], "Claude Sonnet 4.5": ["sonnet45"], "Claude Haiku 4.5": ["haiku45"],
    "Claude Opus 4.5": ["opus45"], "Claude Opus 4.6": ["opus46"], "Claude Sonnet 4.6": ["sonnet46"],
    "Claude Mythos Preview (Glasswing)": ["mythosprev"], "Claude Opus 4.7": ["opus47"],
    "Claude Opus 4.8": ["opus48"], "Claude Fable 5 + Mythos 5": ["fable5", "mythos5"],
    "Claude Sonnet 5": ["sonnet5"], "Claude Opus 5": ["opus5"],
    "Claude Fable 5.1 + Mythos 5.1": ["fable51", "mythos51"], "Claude Opus 5.5": ["opus55"],
    "Claude Sonnet 5.5": ["sonnet55"], "Claude Haiku 5.5": ["haiku55"],
    "Claude Fable 5.2 + Mythos 5.2": ["fable52", "mythos52"],
}
# false / open rows → family (None = drop). Timing-only misses whose model
# shipped soon after (Opus 5 7/16, McAteer) are already in the true rows.
FALSE_FAM = {
    "FALSE: Claude 3.5 Opus": "opus", "FALSE: sonnet-4-8 / Claude Sonnet 4.8": "sonnet",
    "FALSE: Numbat codename": "unknown", "FALSE: Sonnet 5 in Super Bowl week": "sonnet",
    "FALSE: jupiter-v1-p at Code with Claude 5/6": "opus",
    "FALSE: kie.ai 'Fable 5.2 launched 9/10'": "fable", "FALSE: Kingy AI tracker Fable launch 10/6": "fable",
    "FALSE: marshmallow-eap / snickerdoodle / nougat / churro": "unknown",
    "FALSE: Devin EAP IDs orzata/odango/verrine/vanilla/boba": "unknown",
}
# "UNRELEASED Fable 5.5 (aka 5.2)" resolved on 2026-11-09 as Claude Fable 5.2 + Mythos 5.2 (see MAP);
# two of its rows were judged not to point at that release and carry DUPLICATE: / UNMAPPED:
# ids, which no table here lists, so they are dropped.
LIVE = {"OPEN: 'Claude Next' routed under Opus 5.5": ["opus"]}


def code(r):
    if r.signal_code != "OTHER":
        return r.signal_code
    m = re.match(r"([A-Z_]+):", str(r.note))
    tag = m.group(1) if m else "OTHER"
    return {"RED_TEAM_CODENAME": "RED_TEAM", "AB_ROUTING": "AB_ROUTING", "BENCH_TRACKER_LISTING": "FIRST_PARTY_DOC",
            "COMMIT_TRAILER": "CLIENT_STRING"}.get(tag, "OTHER")


rows = []
dropped = {}
fam_of =dict(zip(rel.release_id, rel.family))
date_of = dict(zip(rel.release_id, rel.date))
for i, r in raw.iterrows():
    if r.signal_code in ("NONE", "MARKET") or pd.isna(r.first_seen_date):
        continue
    c = code(r)
    base = dict(signal_id=f"s{i:03d}", signal_code=c, first_seen=r.first_seen_date, grade=r.source_grade,
                specific=r.specific, source=r.source_url, note=str(r.note)[:240])
    if r.release_id in MAP:
        for rid in MAP[r.release_id]:
            rows.append({**base, "release_id": rid, "family": fam_of[rid], "release_date": date_of[rid], "is_false": 0,
                         "lead_days": (pd.Timestamp(date_of[rid]) - pd.Timestamp(r.first_seen_date)).days})
    elif r.release_id in FALSE_FAM:
        rows.append({**base, "release_id": r.release_id, "family": FALSE_FAM[r.release_id], "release_date": None,
                     "is_false": 1, "lead_days": None})
    elif r.release_id in LIVE:
        if "Unmapped" in str(r.note) or "unmapped" in str(r.note):
            continue  # pruned, never-mapped EAP IDs are counted as false alarms, not Fable evidence
        for f in LIVE[r.release_id]:
            rows.append({**base, "release_id": r.release_id, "family": f, "release_date": None, "is_false": 0, "lead_days": None})
    else:
        dropped.setdefault(str(r.release_id), 0)
        dropped[str(r.release_id)] += 1
# A release_id that no table lists is left out of signals.csv without affecting the model.
# That is intended for DUPLICATE:/UNMAPPED: rows and timing-only FALSE rows, but it is also
# what happens to a new "UNRELEASED ..." or "OPEN: ..." target that was not added to LIVE,
# or a shipped model missing from MAP. Say so every time, loudly for the second kind.
for k, n in dropped.items():
    live = k.startswith(("UNRELEASED", "OPEN")) or not k.startswith(("FALSE", "DUPLICATE", "UNMAPPED"))
    print(f"{'WARNING: ' if live else 'note: '}{n} row(s) with release_id '{k}' not in MAP, FALSE_FAM or LIVE: dropped"
          + (" - the model will NOT see them; add the target to LIVE (or MAP if it shipped)" if live else ""))
out = pd.DataFrame(rows)
out = out[~((out.family == "legacy"))]
out.to_csv("data/signals.csv", index=False)
print(out.groupby(["is_false"]).size(), out.signal_code.value_counts(), sep="\n")
