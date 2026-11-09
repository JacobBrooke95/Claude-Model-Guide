"""Build the site page (../release-forecast.html) and the artifact body
(output/release-forecast.artifact.html) from the template plus the JSON outputs.

    python3 tools/build_page.py
"""
import json
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
F = json.load(open(os.path.join(ROOT, "output/forecast.json")))
B = json.load(open(os.path.join(ROOT, "output/backtest.json")))
R = json.load(open(os.path.join(ROOT, "data/input_registry.json")))
rel = pd.read_csv(os.path.join(ROOT, "data/anthropic_releases.csv"))
mk = pd.read_csv(os.path.join(ROOT, F.get("market_file", "data/raw/markets_2026-10-30.csv")))
TEXT = json.load(open(os.path.join(ROOT, "page_text.json")))

last = {}
for f in ["opus", "sonnet", "haiku", "fable", "mythos"]:
    r = rel[rel.family == f].sort_values("date").iloc[-1]
    last[f] = dict(model=r.model, date=r.date)


def q(platform, needle):
    m = mk[(mk.platform == platform) & mk.question.str.contains(needle, regex=False)]
    return float(m.prob.iloc[0]) if len(m) else None


claude6 = {
    "polymarket": {"2027-03-31": q("Polymarket", "Claude 6 released by March 31, 2027"),
                   "2027-06-30": q("Polymarket", "Claude 6 released by June 30, 2027"),
                   "2027-12-31": q("Polymarket", "Claude 6 released by December 31, 2027")},
    "manifold": {"2026-12-31": q("Manifold", "Claude 6 release date: Before January 2027"),
                 "2027-03-31": q("Manifold", "Claude 6 release date: Before April 2027")},
}

meta = dict(TEXT)
meta.update(last_release=last, claude6_markets=claude6,
            n_origins=sum(v[2] for k, v in B.get("periods", {}).items() if k != "all") or 126,
            repo="https://github.com/JacobBrooke95/Claude-Model-Guide/tree/main/forecast")
gp = os.path.join(ROOT, "output/grades.json")
G = json.load(open(gp)) if os.path.exists(gp) else None
data = dict(forecast=F, backtest=B, registry=R, meta=meta, grades=G)
blob = json.dumps(data, default=str, separators=(",", ":")).replace("</", "<\\/")
tpl = open(os.path.join(ROOT, "page_template.html")).read()
body = tpl.replace("/*__DATA__*/null", blob)

# artifact: body only (the artifact host adds the document skeleton)
open(os.path.join(ROOT, "output/release-forecast.artifact.html"), "w").write(body)

# site page: full document with the site's navbar
title_end = body.index("</title>") + len("</title>")
head_bits, rest = body[:title_end], body[title_end:]
site = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
{head_bits}
<link rel="stylesheet" href="styles.css?v=5">
"""
style_end = rest.index("</style>") + len("</style>")
site += rest[:style_end] + """
<style>.navbar ul.nav-links { flex-wrap: wrap; } body { margin: 0; }</style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <h1 class="logo">Jacob Brooke</h1>
            <ul class="nav-links">
                <li><a href="claude-models.html">Claude Guide</a></li>
                <li><a href="release-forecast.html" class="active">Release Forecast</a></li>
                <li><a href="system-card-metrics.html">System Card Metrics</a></li>
                <li><a href="release-deltas.html">Release Deltas</a></li>
            </ul>
        </div>
    </nav>
""" + rest[style_end:] + "\n</body>\n</html>\n"
open(os.path.join(ROOT, "..", "release-forecast.html"), "w").write(site)
print("built", len(site), "bytes")
