#!/usr/bin/env python3
"""Build system-cards/deltas.json, the data behind release-deltas.html.

For every ordered pair of system cards (older -> newer) this pairs up the
figures the two cards report and classifies each pairing:

  comparable      same canonical metric, same sub-evaluation and measure, same
                  model line, no conflicting variant/setting, both values
                  numeric in the same unit. Only these get a delta.
  not comparable  both cards report it, but the figures cannot be subtracted
                  (different effort/tools/task set/statistic/unit, or one of
                  them is not a printed number). The reason is recorded.
  new / dropped   reported by only one of the two cards for that model.

When the newer card restates the older model's score in its own table (kept
by the extraction in an entry's `compared_against` or `notes`), that
same-card figure is used instead of the older card's own number, because it
was measured under the newer card's setup.

Usage:  python3 scripts/build-release-deltas.py [--check] [--report [OLD NEW]]

--check   writes nothing; exits 1 if system-cards/deltas.json is out of date.
--report  prints class counts for the release-line pairs; with two card ids,
          prints every row of that pair (for hand-checking).
Reads system-cards/metrics.json. Standard library only.
"""
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "system-cards")
OUT = "deltas.json"

CATEGORIES = [
    "Coding", "Agentic & tool use", "Computer use", "Reasoning & math", "Knowledge & science",
    "Multilingual", "Long context & memory", "Multimodal & vision", "Professional & economic tasks",
    "Safeguards: harmful requests & over-refusal", "Safeguards: child safety",
    "Safeguards: bias & political even-handedness", "Safeguards: election integrity",
    "Agentic safety & prompt injection", "Honesty & hallucination",
    "Alignment: sycophancy & deception", "Alignment: reward hacking & sabotage",
    "Alignment: evaluation awareness", "Alignment: automated behavioral audit",
    "Model welfare", "Interpretability", "RSP: CBRN", "RSP: cyber", "RSP: autonomy & AI R&D",
    "Efficiency & cost", "Other",
]
FAMILIES = ["opus", "sonnet", "haiku", "mythos", "fable"]

# Release lines: each card is compared with the one before it in its line.
LINES = [
    ("Fable", ["fable5-mythos5", "fable5.1-mythos5.1", "fable5.2-mythos5.2"]),
    ("Opus", ["opus4-sonnet4", "opus4.1", "opus4.5", "opus4.6", "opus4.7", "opus4.8", "opus5", "opus5.5"]),
    ("Sonnet", ["opus4-sonnet4", "sonnet4.5", "sonnet4.6", "sonnet5", "sonnet5.5"]),
    ("Haiku", ["haiku4.5", "haiku5.5"]),
    ("Mythos", ["mythos-preview", "fable5-mythos5"]),
]
# Which family a line pair follows when the cards share more than that, or less.
LINE_FAMILY = {"Opus": "opus", "Sonnet": "sonnet", "Haiku": "haiku", "Mythos": "mythos"}

CLS_CMP, CLS_NC = 0, 1  # row classes stored in the output (new/dropped are separate lists)

# ---------------------------------------------------------------------------
# Value parsing. Conservative: anything not matched here gets no delta.
# ---------------------------------------------------------------------------
NUM = r"[-+−]?\d[\d,]*(?:\.\d+)?"
APPROX = r"(?:~|≈|about|around|approximately|approx\.?|roughly)\s*"
TAIL_OK = (
    r"(?:\s*\((?:\s*(?:±|\+/-)[^)]*|\s*\d[\d,]*\s*(?:/|of)\s*~?\d[\d,]*(?:\s+\w+)?\s*)\)"
    r"|\s*(?:±|\+/-)\s*\d[\d.]*%?(?:\s*SE)?)?"
)
VALUE_PATTERNS = [
    # 93.0% / 41.3% (99 of 240) / 0.18% (± 0.10%) / 93.1% ± 1.4%
    (re.compile(r"^(?P<a>%s)?(?P<n>%s)\s*%%%s$" % (APPROX, NUM, TAIL_OK), re.I), "%"),
    # 218 (87.2%) / 131 of 250 (52.4%) / 245/250 (98.0%)
    (re.compile(r"^\d[\d,]*(?:\s*(?:/|of)\s*\d[\d,]*)?\s*\((?P<n>%s)\s*%%\)$" % NUM), "%"),
    # $3.53 / $4,967.06
    (re.compile(r"^(?P<a>%s)?\$(?P<n>\d[\d,]*(?:\.\d+)?)$" % APPROX, re.I), "$"),
    # 72.65x
    (re.compile(r"^(?P<a>%s)?(?P<n>%s)\s*[x×]$" % (APPROX, NUM), re.I), "x"),
    # 1831 / 0.57 / -0.60 / 0.45 ± 0.08
    (re.compile(r"^(?P<a>%s)?(?P<n>%s)(?:\s*(?:±|\+/-)\s*\d[\d.]*)?$" % (APPROX, NUM), re.I), ""),
]
FRACTION = re.compile(r"^(?P<n>\d[\d,]*(?:\.\d+)?)\s*(?:/|of)\s*(?P<d>\d[\d,]*)$")


def to_float(s):
    return float(s.replace(",", "").replace("−", "-"))


def parse_value(v):
    """-> (number, unit, approximate) or None. Units: '%', '$', 'x', '' (plain), '/N' (count out of N)."""
    if v is None:
        return None
    s = str(v).strip()
    for rx, unit in VALUE_PATTERNS:
        m = rx.match(s)
        if m:
            approx = bool(m.groupdict().get("a"))
            return (to_float(m.group("n")), unit, approx)
    m = FRACTION.match(s)
    if m:
        return (to_float(m.group("n")), "/" + m.group("d").replace(",", ""), False)
    return None


def has_figure(v):
    if v is None:
        return False
    s = str(v).strip().lower()
    return bool(s) and s != "null" and "only in figure" not in s


# ---------------------------------------------------------------------------
# Text normalisation
# ---------------------------------------------------------------------------
STOP = set(
    "the of a an on in for with and or to at per by vs as is are from that this its it all "
    "claude model models eval evals evaluation evaluations benchmark test tests task tasks "
    "rate rates score scores percent percentage pct share fraction proportion number total overall "
    "result results value values level using used based across over each run runs trial trials "
    "pass passed passing success successful successes resolve resolved accuracy accurate correct "
    "solve solved completion completed complete performance metric measure higher lower better".split()
)
SYN = {
    "average": "mean", "avg": "mean", "averaged": "mean", "failures": "failure", "fail": "failure",
    "failed": "failure", "failing": "failure", "errors": "error", "refusals": "refusal", "refuse": "refusal",
    "refused": "refusal", "refuses": "refusal", "attacks": "attack", "hallucinations": "hallucination",
    "hallucinated": "hallucination", "attempts": "attempt", "turns": "turn", "questions": "question",
    "prompts": "prompt", "problems": "problem", "scenarios": "scenario", "environments": "environment",
    "languages": "language", "categories": "category", "agents": "agent", "tools": "tool", "steps": "step",
    "nine": "9", "five": "5", "three": "3", "two": "2", "one": "1", "four": "4", "ten": "10",
    "harmful": "harm", "harms": "harm", "violative": "violation", "violations": "violation",
    "maximum": "max", "minimum": "min", "without": "no", "w/o": "no", "attempted": "attempt",
    "probability": "rate", "campaign": "operation",
}
# One side says one of these and the other does not: they are different measures, never matched.
POLARITY = {
    "failure", "error", "attack", "refusal", "hallucination", "violation", "incorrect", "wrong",
    "harm", "false", "unsafe", "cost", "tokens", "token", "latency", "time", "duration", "abstention",
    "abstain", "sycophancy", "sycophantic", "deception", "deceptive", "sabotage", "leak", "leakage",
    "overrefusal", "over-refusal", "benign", "net", "gap", "difference", "delta", "change", "uplift",
    "variance", "std", "ci", "count", "length", "hour", "minute", "regression", "attempt", "fallback",
    "refusal", "stealth", "flag", "block", "blocked",
}
# A statistic named on both sides must be the same one.
STATS = {"mean": "mean", "median": "median", "max": "max", "best": "max", "peak": "max", "min": "min",
         "worst": "min", "p50": "median", "p90": "p90", "p95": "p95", "p99": "p99"}
# Qualifiers that change the measurement even when only one side mentions them.
MARKED = {
    "only", "subset", "offline", "no", "excluding", "excl", "hard", "hardest", "lite", "mini",
    "partial", "strict", "lenient", "private", "held-out", "heldout", "adaptive-attack", "unmitigated",
    "ablation", "ablated", "disabled", "off", "blind", "oracle", "zero-shot", "few-shot", "single-turn",
    "multi-turn", "multiturn", "worst-case", "low", "medium", "minimal", "not",
}

WORD = re.compile(r"[a-z0-9][a-z0-9.+@-]*")


def words(text):
    out = []
    for w in WORD.findall((text or "").lower().replace("–", "-").replace("—", " ")):
        w = w.strip(".-")
        if not w:
            continue
        w = SYN.get(w, w)
        if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
            w = w[:-1]
            w = SYN.get(w, w)
        out.append(w)
    return out


def content_words(text, drop=()):
    return {w for w in words(text) if w not in STOP and w not in drop}


FACETS = [
    # (facet label, [(regex, value)]); first value found per regex is collected into a set
    ("effort", [
        (re.compile(r"\b(low|medium|high|xhigh|max)(?:imum)?[- ]effort\b"), None),
        (re.compile(r"\beffort[:= ]+(low|medium|high|xhigh|max)\b"), None),
        (re.compile(r"\b(max) thinking\b"), None),
    ]),
    ("thinking", [
        (re.compile(r"\b(?:no|without|w/o)(?: extended| adaptive)? thinking\b|\bthinking (?:off|disabled)\b|\bnon-thinking\b"), "off"),
        (re.compile(r"\b(?:extended|adaptive|with|max) thinking\b|\bthinking (?:on|enabled)\b"), "on"),
    ]),
    ("thinking budget", [(re.compile(r"\b(\d+k)(?: token)?(?: extended)? thinking\b|\bthinking budget (?:of )?(\d+k)\b"), None)]),
    ("tools", [
        (re.compile(r"\b(?:no|without|w/o) tools?\b|\btools? (?:off|disabled)\b|\bno tool use\b"), "off"),
        (re.compile(r"\bwith tools?\b|\btools? enabled\b|\bwith tool use\b|\bwith code execution\b|\bwith python\b"), "on"),
    ]),
    ("search", [
        (re.compile(r"\b(?:no|without|w/o)(?: web)? search\b|\bsearch (?:off|disabled)\b|\bno web access\b|\bno internet\b"), "off"),
        (re.compile(r"\bwith(?: web)? search\b|\bsearch enabled\b|\bweb search (?:and|\+|on)\b|\bwith web access\b"), "on"),
    ]),
    ("safeguards", [
        (re.compile(r"\b(?:no|without|w/o)(?: asl-\d)? safeguards\b|\bsafeguards (?:off|disabled|removed)\b|\bhelpful-only\b"), "off"),
        (re.compile(r"\bwith(?: asl-\d)? safeguards\b|\bsafeguards (?:on|enabled)\b"), "on"),
    ]),
    ("system prompt", [
        (re.compile(r"\b(?:no|without) system prompt\b"), "off"),
        (re.compile(r"\bwith(?: a)? system prompt\b"), "on"),
    ]),
    ("scoring", [(re.compile(r"\b(strict|partial|lenient)\b"), None)]),
    ("turns", [(re.compile(r"\b(single|multi)[- ]?turn\b"), None)]),
    ("subset", [(re.compile(r"\b(offline|subset|hard|hardest|easy|lite|mini|private|held-out|public|verified|full)\b(?! effort)"), None)]),
    ("attempts", [
        (re.compile(r"\b(\d+) attempts?\b"), None),
        (re.compile(r"\bk ?= ?(\d+)\b"), None),
        (re.compile(r"\b(?:pass|top|best)[@ -](?:of[- ])?(\d+)\b"), None),
    ]),
    ("context", [(re.compile(r"\b(\d+[km])(?:[- ]token)?[- ]context\b"), None)]),
    ("shots", [(re.compile(r"\b(\d+|zero|few)-shot\b"), None)]),
    ("mitigations", [
        (re.compile(r"\b(?:no|without) (?:mitigations?|defen[cs]es?|classifiers?)\b|\bunmitigated\b"), "off"),
        (re.compile(r"\bwith (?:mitigations?|defen[cs]es?|classifiers?)\b"), "on"),
    ]),
]
SIZE = re.compile(
    r"\b(\d[\d,]*)\s*(?:[a-z-]+\s){0,2}?(tasks?|problems?|questions?|prompts?|samples?|scenarios?|items?|cases?|"
    r"conversations?|environments?|challenges?|examples?|instances?|transcripts?|puzzles?|languages?)\b"
)
# One-sided mentions of these facet values are tolerated (they name the usual default).
DEFAULT_OK = {("subset", "public"), ("subset", "verified"), ("subset", "full"), ("thinking", "on"),
              ("safeguards", "on"), ("turns", "single"), ("scoring", "strict")}
# Facets where one side being silent is not evidence of a difference.
ONE_SIDED_OK = {"effort", "thinking budget", "context", "attempts", "shots", "system prompt", "search",
                "tools", "mitigations"}


def facets(text):
    t = (text or "").lower().replace("–", "-")
    out = {}
    for label, rules in FACETS:
        vals = set()
        for rx, fixed in rules:
            for m in rx.finditer(t):
                vals.add(fixed or next(g for g in m.groups() if g))
        if vals:
            out[label] = vals
    t2 = re.sub(r"\b(\d[\d,]*) of \d[\d,]*(?= )", r"\1", t)  # "82 of 108 tasks" is an 82-task set
    sizes = {m.group(1).replace(",", "") for m in SIZE.finditer(t2)}
    if sizes:
        out["task set"] = sizes
    return out


FACET_STRIP = re.compile(
    r"\b(?:avg|average|mean) of \d+ (?:trials?|runs?)\b|\b\d+ (?:trials?|runs?|seeds?)(?:\s*/\s*task| per task)?\b|"
    r"\bx\s*\d+ trials\b|\b\d[\d,]*\b"
)


class Row:
    """One printed figure: a result row of one entry of one metric in one card."""

    __slots__ = ("ref", "mi", "metric", "card", "entry", "ei", "model", "value", "setting", "parsed",
                 "name_words", "var_words", "fac", "stat", "polarity", "eval_words", "measure_words")

    def __init__(self, ref, mi, metric, card, entry, ei, res):
        self.ref, self.mi, self.metric, self.card, self.entry, self.ei = ref, mi, metric, card, entry, ei
        self.model, self.value, self.setting = res["model"], res["value"], res["setting"] or ""
        self.parsed = parse_value(self.value)
        metric_words = set(words(metric["name"])) | set(words(metric["family"]))
        self.eval_words = content_words(entry["eval_name"], metric_words)
        name = self.eval_words
        self.measure_words = content_words(re.sub(r"\(\s*0\s*-\s*1\s*\)|\b0\s*-\s*100\b|%", " ", entry["measure"]), metric_words)
        self.name_words = name | self.measure_words
        vtext = entry["variant"] + " ; " + self.setting
        self.fac = facets(" ; ".join([entry["eval_name"], vtext, entry["measure"]]))
        stripped = FACET_STRIP.sub(" ", vtext.lower())
        self.var_words = content_words(stripped, metric_words)
        stats = {STATS[w] for w in words(entry["eval_name"] + " " + entry["measure"]) if w in STATS}
        self.stat = stats
        self.polarity = {w for w in self.name_words if w in POLARITY}


def jaccard(a, b):
    if not a and not b:
        return 1.0
    return len(a & b) / float(len(a | b))


def set_score(a, b):
    if a == b:
        return 1.0
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    if small <= large:
        extra = len(large - small)
        if not small:
            return 0.6 if extra <= 2 else 0.3
        return 0.8 if extra <= 2 else 0.55
    return jaccard(a, b)


def name_score(o, n):
    """How sure we are that two rows are the same sub-evaluation and measure (0..1).

    The words of the evaluation name (minus the metric's own name) must line up, and so must the words
    of the measure. A bare "X" matches "X mean score"; "X failure rate" never matches "X".
    """
    if o.polarity != n.polarity:
        return 0.0
    e = set_score(o.eval_words, n.eval_words)
    m = set_score(o.measure_words - o.eval_words, n.measure_words - n.eval_words)
    if e < 0.5 or m < 0.5:
        # the sub-evaluation may be named in the measure on one side and in the title on the other
        both = set_score(o.name_words, n.name_words)
        return both if both >= 0.8 else 0.0
    return 0.6 * e + 0.4 * m


def conflicts(o, n):
    """Reasons the two rows' setups differ. Empty list = no known conflict."""
    out = []
    for label in sorted(set(o.fac) | set(n.fac)):
        a, b = o.fac.get(label), n.fac.get(label)
        if a and b:
            if (not (a & b)) if label == "task set" else (a != b):
                out.append("%s: %s vs %s" % (label, "/".join(sorted(a)), "/".join(sorted(b))))
        elif label not in ONE_SIDED_OK and label != "task set":
            only = a or b
            if not all((label, v) in DEFAULT_OK for v in only):
                out.append("%s given on one side only (%s)" % (label, "/".join(sorted(only))))
    if o.stat and n.stat and o.stat != n.stat:
        out.append("statistic: %s vs %s" % ("/".join(sorted(o.stat)), "/".join(sorted(n.stat))))
    a, b = o.var_words, n.var_words
    if a and b:
        if jaccard(a, b) < 0.34 and not (a <= b or b <= a):
            out.append("variants described differently")
        elif (a ^ b) & MARKED:
            out.append("variant qualifier on one side only (%s)" % ", ".join(sorted((a ^ b) & MARKED)))
    elif (a | b) & MARKED:
        out.append("variant qualifier on one side only (%s)" % ", ".join(sorted((a | b) & MARKED)))
    return out


# ---------------------------------------------------------------------------
# Same-card comparison: the newer card restating the older model's figure
# ---------------------------------------------------------------------------
def short_name(model):
    return re.sub(r"^Claude\s+", "", model).strip()


_RX = {}


def restated_regex(model):
    if model not in _RX:
        _RX[model] = _restated_regex(model)
    return _RX[model]


def _restated_regex(model):
    name = re.escape(short_name(model)).replace(r"\ ", r"\s+")
    # "Fable 5.1 89.1" / "Claude Opus 5 (85.4%)" / "Claude Fable 5/Mythos 5 (80)" / "Opus 5.5: 91.2"
    return re.compile(
        r"(?<![\w.])(?:Claude\s+)?%s(?![\d])(?!\.\d)"
        r"(?P<joint>\s*(?:/|&|and)\s*(?:Claude\s+)?(?:Mythos|Fable|Sonnet|Opus|Haiku)\s+[\d.]+\d)?"
        r"\s*(?:[:=]|at|scored|was|is)?\s*(?P<paren>\()?\s*"
        r"(?P<num>\$?[-+−]?\d[\d,]*(?:\.\d+)?)(?P<pct>\s*%%)?"
        r"(?P<after>[^;]*)" % name,
        re.I,
    )


QUAL_OK = re.compile(r"^\s*(?:±|\+/-)|^\s*\d[\d,]*\s*(?:/|of)\s*\d|^\s*(?:SE|CI|95%)", re.I)


def restated_values(entry, model):
    """Figures the entry quotes for `model`: list of (number, unit_or_None, qualifier, source)."""
    rx = restated_regex(model)
    found = []
    sources = [("compared_against", c) for c in entry.get("compared_against") or []]
    sources += [("notes", entry.get("notes") or "")]
    for src, text in sources:
        for m in rx.finditer(text):
            after = m.group("after") or ""
            qual = ""
            if m.group("paren"):
                inner = after.split(")")[0]
                # "(52.3%, Codex CLI, leaderboard)": the text after the number is a caveat
                inner = inner.lstrip(" ,")
                if inner and not QUAL_OK.match(inner):
                    qual = inner.strip()
                rest = ""
            else:
                rest = after
                pm = re.match(r"\s*\(([^)]*)\)", rest)
                if pm:
                    if not QUAL_OK.match(pm.group(1)):
                        qual = pm.group(1).strip()
                    rest = rest[pm.end():]
                # the number must end the clause: "28% of tasks" or "5 trials" is something else
                if not re.match(r"\s*(?:$|[,.](?:\s|$)|\)|and\b|vs\.?\b|versus\b)", rest):
                    continue
            num = m.group("num")
            unit = "$" if num.startswith("$") else ("%" if m.group("pct") else None)
            found.append((to_float(num.lstrip("$")), unit, qual, src, m.group(0).strip()))
    return found


SETUP_QUAL = re.compile(
    r"\b(?:low|medium|high|xhigh|max|effort|reported|leaderboard|harness|trials?|runs?|tools?|thinking|setting|"
    r"prompt|version|subset|tasks?|without|with|different|older|earlier|previous|card|budget|scaffold|"
    r"safeguards?|classifiers?|helpful-only|attempts?|estimated?|approx\w*|partial|strict|offline)\b|\d+k\b", re.I)


def benign_qualifier(qual, new_row):
    """True unless the bracket after a quoted figure describes a setup the newer model was not run under."""
    if not SETUP_QUAL.search(qual):
        return True
    own = set(words(" ".join([new_row.entry["eval_name"], new_row.entry["variant"], new_row.setting])))
    return set(words(qual)) <= own


def pick_restated(entry, model, new_parsed, old_own):
    """Choose the restated figure for `model`, or None when absent or ambiguous."""
    if new_parsed is None:
        return None
    cands = []
    for num, unit, qual, src, raw in restated_values(entry, model):
        u = new_parsed[1] if unit is None else unit
        if u != new_parsed[1]:
            continue
        cands.append((num, u, qual, src))
    if not cands:
        return None
    structured = [c for c in cands if c[3] == "compared_against"]
    pool = structured or cands
    distinct = sorted({c[0] for c in pool})
    if len(distinct) > 1:
        # several different numbers quoted for the model: only trust one the older card itself printed
        if old_own is not None and old_own[1] == new_parsed[1]:
            same = [c for c in pool if abs(c[0] - old_own[0]) < 0.051]
            if same:
                return same[0]
        return None
    return pool[0]


# ---------------------------------------------------------------------------
# Direction: is a higher number better?
# ---------------------------------------------------------------------------
LOWER = re.compile(
    r"attack success|\basr\b|failure|fail rate|\berror|hallucinat|over-?refus|false positive|false negative|"
    r"\bcost\b|\bprice\b|violation|violative|harmful (?:response|compliance|output|behaviou?r)|"
    r"compliance with harmful|sycophan|decepti|misalign|reward hack|incorrect|wrong answer|jailbreak|leak|"
    r"unsafe|blackmail|sabotage|unfaithful|overcomplian|cheat|hard-?cod|test tamper|special-?cas|collusion|"
    r"refusal rate on benign|benign refusal|unnecessary refusal|fabricat|bias score|distress|"
    r"exfiltrat|power-?seeking|self-preservation|uplift",
    re.I,
)
HIGHER = re.compile(
    r"accuracy|pass rate|resolve|% resolved|success rate|task success|\bsolved\b|\bcorrect|\belo\b|win rate|"
    r"\bf1\b|recall|precision|pass[@^]\d|harmless|appropriate|\bscore\b|completion rate|even-?handed|robustness|"
    r"defen[cs]e rate|refusal rate on harmful|net score|automation rate|balance|revenue|profit|net worth|\bauroc\b|\bspearman\b",
    re.I,
)
NEUTRAL_CATS = {"RSP: CBRN", "RSP: cyber", "RSP: autonomy & AI R&D", "Model welfare", "Interpretability",
                "Alignment: evaluation awareness", "Other"}
CAPABILITY_CATS = set(CATEGORIES[:9])
# Explicit overrides by canonical metric id: 1 higher is better, -1 lower is better, 0 never judge.
DIRECTION = {
    "swe-bench-efficiency": 0,
}


EXPLICIT_LOWER = re.compile(r"\blower(?: is| =)? (?:better|safer|more robust)\b", re.I)
EXPLICIT_HIGHER = re.compile(r"\bhigher(?: is| =)? (?:better|safer|more robust)\b|\bpositive better\b", re.I)
EXPLICIT_ZERO = re.compile(r"\bcloser to (?:zero|0)(?: is)? better\b", re.I)
HEDGED = re.compile(r"\bunless\b|\bexcept\b|\bgenerally\b", re.I)
# Outside the capability categories a bare "score" or "success rate" can be a bad thing (a stealth
# success rate, a misuse score), so only these unambiguous words count as higher-is-better there.
CLEAR_HIGHER = re.compile(
    r"accuracy|harmless|appropriate response|even-?handed|defen[cs]e rate|\bcorrect\b|honesty rate|"
    r"refusal rate on harmful|pass rate|% resolved|resolve rate", re.I)


def direction(metric, entry):
    """1 = higher is better, -1 = lower is better, 2 = closer to zero is better, 0 = not judged."""
    if metric["id"] in DIRECTION:
        return DIRECTION[metric["id"]]
    measure = entry["measure"]
    # the card's own statement wins, unless it hedges ("lower is better unless noted")
    if not HEDGED.search(measure):
        if EXPLICIT_ZERO.search(measure):
            return 2
        lo, hi = bool(EXPLICIT_LOWER.search(measure)), bool(EXPLICIT_HIGHER.search(measure))
        if lo != hi:
            return -1 if lo else 1
    cat = metric["category"]
    if cat in NEUTRAL_CATS:
        return 0
    text = " ; ".join([measure, entry["eval_name"]])
    if re.search(r"stealth|closer to (?:zero|0)|\bbias score\b", text, re.I):
        return 0
    lo, hi = bool(LOWER.search(text)), bool(HIGHER.search(text))
    if cat == "Efficiency & cost":
        return -1 if lo and not hi else 0
    if lo and hi:
        # "attack success rate" names a success rate that is bad; anything else mixed is left alone
        if re.search(r"attack success|\basr\b|jailbreak success", text, re.I) and not re.search(r"defen|robust", text, re.I):
            return -1
        return 0
    if lo:
        return -1
    if hi:
        if cat in CAPABILITY_CATS:
            return 0 if re.search(r"\brefus|abstain|abstention|\btokens?\b|latency|\bsteps\b", text, re.I) else 1
        return 1 if CLEAR_HIGHER.search(text) else 0
    return 0


# ---------------------------------------------------------------------------
# Pairing
# ---------------------------------------------------------------------------
def card_families(card):
    out = []
    for subject in card["subjects"]:
        for f in FAMILIES:
            if f in subject.lower() and f not in out:
                out.append(f)
    return out


def family_of(model):
    for f in FAMILIES:
        if f in model.lower():
            return f
    return ""


def model_pairs(old, new, line_family=None):
    """[(old model, new model)]: same family where the cards share one, otherwise every combination."""
    pairs = [(a, b) for a in old["subjects"] for b in new["subjects"] if family_of(a) == family_of(b)]
    if line_family:
        only = [(a, b) for a, b in pairs if family_of(b) == line_family]
        pairs = only or pairs
    if not pairs:
        pairs = [(a, b) for a in old["subjects"] for b in new["subjects"]]
    return pairs


SAYS_CHANGED = re.compile(
    r"not (?:be )?(?:directly )?comparable (?:to|with|across) (?:the )?(?:prior|earlier|previous|older|other) (?:system )?"
    r"(?:cards?|versions?|releases?|results?)|not (?:be )?(?:directly )?comparable (?:to|with) [^.;]*\bcards?\b|"
    r"not comparable across cards|older versions not comparable|"
    r"\bnew (?:attacker|harness|grader|judge)\b|\bupdated (?:graders?|harness|evaluation|implementation)\b|"
    r"revised problem set|\bprompt change\b|\brescored\b", re.I)


def says_changed(entry):
    return bool(SAYS_CHANGED.search(" ; ".join([entry["notes"], entry["variant"], entry["description"]])))


def as_percent(a, b):
    """The two parsed values in one unit: (a, b, unit), or None if they are not on the same scale.

    A count "222 of 410" printed against a percentage is converted to a percentage.
    """
    if a[1] == b[1]:
        return (a[0], b[0], a[1])

    def pct(v):
        if v[1] == "%":
            return v[0]
        if v[1].startswith("/") and float(v[1][1:]) > 0 and v[0] <= float(v[1][1:]):
            return round(100.0 * v[0] / float(v[1][1:]), 1)
        return None
    if "%" in (a[1], b[1]):
        pa, pb = pct(a), pct(b)
        if pa is not None and pb is not None:
            return (pa, pb, "%")
    return None


def match_metric(olds, news, old_model, drifted=""):
    """Pair the rows of one metric for one model pair.

    -> (rows, unmatched_old, unmatched_new); rows are dicts with o, n (Row or None), cls, basis, reason, rs.
    """
    cands = []
    for o in olds:
        for n in news:
            s = name_score(o, n)
            if s < 0.5:
                continue
            conf = conflicts(o, n)
            units = o.parsed is not None and n.parsed is not None and o.parsed[1] == n.parsed[1]
            total = s * 10 + jaccard(o.var_words, n.var_words) + (2 if not conf else 0) + (0.5 if units else 0)
            total += 0.25 if o.setting.strip().lower() == n.setting.strip().lower() else 0
            total += 0.1 if o.entry["section"].split(" ")[0] == n.entry["section"].split(" ")[0] else 0
            cands.append((-total, o.ref, n.ref, o, n, conf))
    cands.sort(key=lambda c: c[:3])
    used_o, used_n, pairs = set(), set(), {}
    for _, _, _, o, n, conf in cands:
        if o.ref in used_o or n.ref in used_n:
            continue
        used_o.add(o.ref)
        used_n.add(n.ref)
        pairs[n.ref] = (o, conf)

    rows = []
    for n in news:
        o, conf = pairs.get(n.ref, (None, []))
        # the restated figure is only attributable when the entry has one row for this model
        solo = sum(1 for r in n.entry["results"] if r["model"] == n.model) == 1
        rs = pick_restated(n.entry, old_model, n.parsed, o.parsed if o else None) if solo else None
        if rs is not None:
            num, unit, qual, _src = rs
            # keep the older card's own row alongside only when it is clearly the same measurement
            if o is not None and conf:
                o = None
            if qual and not benign_qualifier(qual, n):
                rows.append(dict(o=o, n=n, cls=CLS_NC, basis=1, rs=(num, unit),
                                 reason="newer card quotes the older model under a different setup (%s)" % qual))
            else:
                rows.append(dict(o=o, n=n, cls=CLS_CMP, basis=1, rs=(num, unit), reason=""))
            continue
        if o is None:
            continue
        reason = ""
        if not has_figure(o.value) and not has_figure(n.value):
            reason = "neither card prints a figure"
        elif not has_figure(o.value):
            reason = "older card prints no figure"
        elif not has_figure(n.value):
            reason = "newer card prints no figure"
        elif o.parsed is None or n.parsed is None:
            reason = "value is not a single number"
        elif as_percent(o.parsed, n.parsed) is None:
            reason = "different units or scales"
        elif conf:
            reason = "; ".join(conf)
        elif says_changed(n.entry):
            reason = "newer card says its setup changed from earlier cards"
        elif drifted:
            reason = drifted
        conv = None
        if not reason:
            a, b, unit = as_percent(o.parsed, n.parsed)
            if o.parsed[1] != n.parsed[1]:
                conv = (a, b)
        rows.append(dict(o=o, n=n, cls=CLS_NC if reason else CLS_CMP, basis=0, rs=None, reason=reason, conv=conv))
    matched_n = {r["n"].ref for r in rows}
    matched_o = {r["o"].ref for r in rows if r["o"] is not None}
    c2c = [r for r in rows if r["cls"] == CLS_CMP and r["basis"] == 0]
    # One side prints several variants of the figure and the other does not say which one it is.
    for r in c2c:
        o, n = r["o"], r["n"]
        for mine, other, pool, taken in ((n, o, news, matched_n), (o, n, olds, matched_o)):
            if mine.var_words & other.var_words:
                continue
            if any(x.ref not in taken and x.var_words != mine.var_words and x.name_words == mine.name_words
                   and has_figure(x.value) for x in pool):
                r["cls"], r["reason"] = CLS_NC, "one card prints several variants and the other does not say which it reports"
                break
    # The two cards describe the evaluation differently and the figure jumps: more likely a changed
    # evaluation than a changed model. Applies to every card-to-card row of the metric.
    def jump(r):
        a, b, unit = as_percent(r["o"].parsed, r["n"].parsed)
        if r["o"].eval_words == r["n"].eval_words and r["o"].measure_words == r["n"].measure_words:
            return False
        if unit == "%":
            return abs(b - a) > 25
        return abs(b - a) > 0.6 * max(abs(a), abs(b))
    if any(r["cls"] == CLS_CMP and jump(r) for r in c2c):
        for r in c2c:
            if r["cls"] == CLS_CMP:
                r["cls"], r["reason"] = CLS_NC, "described differently in the two cards and the figure jumps; no same-card figure to confirm"
    # a card that prints the same comparison twice (summary table and detail section) counts once
    seen, unique, skipped = {}, [], []
    for r in rows:
        if r["cls"] == CLS_CMP:
            old_num = r["rs"][0] if r["rs"] else r["o"].parsed[0]
            key = (old_num, r["n"].parsed[0], r["n"].parsed[1])
            if old_num == r["n"].parsed[0]:
                # no move: only the very same sub-evaluation and variant is a repeat
                key += (frozenset(r["n"].eval_words), frozenset(r["n"].var_words))
            if key in seen:
                if r["o"] is not None and seen[key]["o"] is None:
                    seen[key]["o"] = r["o"]
                elif r["o"] is not None and r["o"] is not seen[key]["o"]:
                    skipped.append(r["o"].ref)
                skipped.append(r["n"].ref)
                continue
            seen[key] = r
        unique.append(r)
    rows = unique
    shown_o = {r["o"].ref for r in rows if r["o"] is not None}
    dropped = [o for o in olds if o.ref not in shown_o and o.ref not in skipped]
    return rows, dropped, [n for n in news if n.ref not in matched_n], skipped


def build(data):
    cards = data["cards"]
    card_by_id = {c["id"]: c for c in cards}
    order = {c["id"]: i for i, c in enumerate(cards)}
    cat_rank = {c: i for i, c in enumerate(CATEGORIES)}
    metrics = sorted(data["metrics"], key=lambda m: (cat_rank[m["category"]], m["name"].lower(), m["id"]))

    # Flat table of every printed figure
    table = []          # Row objects by ref
    by_key = {}         # (card id, model, metric index) -> [Row]
    table_by_entry = {}  # (card id, metric index, id(entry)) -> [Row]
    for mi, m in enumerate(metrics):
        for c in cards:
            for ei, e in enumerate(m["cards"].get(c["id"], [])):
                for res in e["results"]:
                    row = Row(len(table), mi, m, c["id"], e, ei, res)
                    table.append(row)
                    by_key.setdefault((c["id"], res["model"], mi), []).append(row)
                    table_by_entry.setdefault((c["id"], mi, id(e)), []).append(row)

    line_pairs = []
    for name, ids in LINES:
        for a, b in zip(ids, ids[1:]):
            line_pairs.append((a, b, name))
    line_family = {(a, b): LINE_FAMILY.get(n) for a, b, n in line_pairs}

    # Has a card re-measured an earlier model at a value that model's own card did not print?
    # Then the card's setup for that metric differs from earlier cards, and card-to-card deltas are off.
    owner = {s: c["id"] for c in cards for s in c["subjects"]}
    drift_cache = {}

    def drift(new_id, mi):
        k = (new_id, mi)
        if k in drift_cache:
            return drift_cache[k]
        m = metrics[mi]
        msg = ("newer card says its setup changed from earlier cards"
               if any(says_changed(e) for e in m["cards"].get(new_id, [])) else "")
        for e in m["cards"].get(new_id, []):
            if msg:
                break
            mine = [r for r in table_by_entry.get((new_id, mi, id(e)), []) if r.parsed is not None]
            if not mine:
                continue
            n = mine[0]
            for model, cid in owner.items():
                if cid == new_id or order[cid] > order[new_id]:
                    continue
                vals = restated_values(e, model)
                structured = [v for v in vals if v[3] == "compared_against"]
                nums = sorted({v[0] for v in (structured or vals) if (v[1] or n.parsed[1]) == n.parsed[1] and not v[2]})
                if len(nums) != 1:
                    continue
                best = None
                for x in by_key.get((cid, model, mi), []):
                    if x.parsed is None or x.parsed[1] != n.parsed[1] or conflicts(x, n):
                        continue
                    sc = name_score(x, n)
                    if sc >= 0.5 and (best is None or sc > best[0]):
                        best = (sc, x)
                if best is None:
                    continue
                own, quoted = best[1].parsed[0], nums[0]
                tol = 1.0 if n.parsed[1] == "%" else max(0.03 * abs(own), 0.011)
                if abs(own - quoted) > tol:
                    msg = "newer card re-measures %s at %s where its own card printed %s, so the setup changed" % (
                        short_name(model), ("%g" % quoted) + n.parsed[1].replace("/", " of "), best[1].value)
                    break
        drift_cache[k] = msg
        return msg

    pairs = {}
    for i, old in enumerate(cards):
        for new in cards[i + 1:]:
            mps = model_pairs(old, new, line_family.get((old["id"], new["id"])))
            out_mps = []
            for a, b in mps:
                rows, dropped, added, skip = [], [], [], []
                for mi in range(len(metrics)):
                    olds = by_key.get((old["id"], a, mi), [])
                    news = by_key.get((new["id"], b, mi), [])
                    if not olds and not news:
                        continue
                    r, d, n, sk = match_metric(olds, news, a, drift(new["id"], mi) if olds and news else "")
                    rows += r
                    dropped += d
                    added += n
                    skip += sk
                packed = []
                for r in rows:
                    o, n = r["o"], r["n"]
                    item = [r["cls"], -1 if o is None else o.ref, n.ref, r["basis"], r["reason"]]
                    if r["rs"] is not None:
                        item.append(r["rs"][0])
                    elif r.get("conv"):
                        item += [r["conv"][0], r["conv"][1]]
                    packed.append(item)
                # new/dropped are not stored: they are every figure of model b / model a that no row
                # references and "skip" (repeats of a comparison already shown) does not list
                out_mps.append({"a": a, "b": b, "rows": packed, "skip": sorted(skip),
                                "nNew": len(added), "nDropped": len(dropped)})
            pairs["%s>%s" % (old["id"], new["id"])] = out_mps

    # String-interned figure table
    strings, sidx = [], {}

    def S(text):
        text = text or ""
        if text not in sidx:
            sidx[text] = len(strings)
            strings.append(text)
        return sidx[text]

    figs = []
    for r in table:
        e = r.entry
        p = r.parsed
        figs.append([
            r.mi, order[r.card], S(r.model), S(e["eval_name"]), S(e["variant"]), S(r.setting), S(e["measure"]),
            S(e["section"]), S("" if r.value is None else str(r.value)),
            None if p is None else p[0], S("" if p is None else p[1]), 1 if (p and p[2]) else 0,
            direction(r.metric, e),
        ])

    out = {
        "cards": [{"id": c["id"], "label": c["label"], "title": c["title"], "date": c["date"],
                   "families": card_families(c), "subjects": c["subjects"]} for c in cards],
        "categories": CATEGORIES,
        "lines": [{"name": n, "cards": ids} for n, ids in LINES],
        "metrics": [[m["id"], m["name"], cat_rank[m["category"]]] for m in metrics],
        "strings": strings,
        "figs": figs,
        "pairs": pairs,
    }
    return out, table, metrics, line_pairs


def classify(out, key):
    """Counts for one pair, the same way the page counts them."""
    figs, strings = out["figs"], out["strings"]
    c = dict(improved=0, regressed=0, unchanged=0, moved=0, nc=0, new=0, dropped=0, same_card=0)
    for mp in out["pairs"][key]:
        for row in mp["rows"]:
            cls, o, n, basis, _reason = row[:5]
            if cls == CLS_NC:
                c["nc"] += 1
                continue
            new = figs[n]
            if basis == 1:
                old_val, new_val = row[5], new[9]
            elif len(row) > 5:
                old_val, new_val = row[5], row[6]
            else:
                old_val, new_val = figs[o][9], new[9]
            d = new_val - old_val
            way = new[12] or (figs[o][12] if o >= 0 else 0)
            c["same_card"] += basis
            if abs(d) < 1e-9:
                c["unchanged"] += 1
            elif way == 0:
                c["moved"] += 1
            elif way == 2:
                c["improved" if abs(new_val) < abs(old_val) else "regressed" if abs(new_val) > abs(old_val) else "moved"] += 1
            elif (d > 0) == (way > 0):
                c["improved"] += 1
            else:
                c["regressed"] += 1
        c["new"] += mp["nNew"]
        c["dropped"] += mp["nDropped"]
    return c


def report(out, table, metrics, line_pairs, args):
    figs, strings = out["figs"], out["strings"]
    if len(args) == 2:
        key = "%s>%s" % tuple(args)
        for mp in out["pairs"][key]:
            print("##", mp["a"], "->", mp["b"])
            for row in sorted(mp["rows"], key=lambda r: (figs[r[2]][0], r[0])):
                cls, o, n, basis, reason = row[:5]
                N, O = table[n], (table[o] if o >= 0 else None)
                oldv = ("%g (restated)" % row[5]) if basis else O.value
                print("%s | %s | %s | %s -> %s | dir %+d | %s | %s" % (
                    "CMP" if cls == CLS_CMP else "NC ", metrics[N.mi]["id"], N.entry["eval_name"],
                    oldv, N.value, figs[n][12], "same-card" if basis else "card-to-card", reason))
                print("      old: %s" % (O and (O.entry["eval_name"], O.entry["variant"], O.setting, O.entry["measure"], O.value, O.entry["section"]),))
                print("      new: %s" % ((N.entry["eval_name"], N.entry["variant"], N.setting, N.entry["measure"], N.entry["section"]),))
                if basis:
                    print("      src: %s | %s" % (N.entry["compared_against"], N.entry["notes"]))
            print("  new:", mp["nNew"], " dropped:", mp["nDropped"])
        return
    tot = dict(improved=0, regressed=0, unchanged=0, moved=0, nc=0, new=0, dropped=0, same_card=0)
    print("%-44s %4s %4s %4s %4s %4s %4s %4s %5s" % ("pair", "imp", "reg", "same", "mov", "nc", "new", "drop", "samec"))
    for a, b, name in line_pairs:
        c = classify(out, "%s>%s" % (a, b))
        for k in tot:
            tot[k] += c[k]
        print("%-44s %4d %4d %4d %4d %4d %4d %4d %5d" % (
            "%s: %s > %s" % (name, a, b), c["improved"], c["regressed"], c["unchanged"], c["moved"],
            c["nc"], c["new"], c["dropped"], c["same_card"]))
    print("%-44s %4d %4d %4d %4d %4d %4d %4d %5d" % (
        "release-line total", tot["improved"], tot["regressed"], tot["unchanged"], tot["moved"],
        tot["nc"], tot["new"], tot["dropped"], tot["same_card"]))
    allc = dict.fromkeys(tot, 0)
    for key in out["pairs"]:
        c = classify(out, key)
        for k in allc:
            allc[k] += c[k]
    print("all %d card pairs: %s" % (len(out["pairs"]), allc))


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    with open(os.path.join(ROOT, "metrics.json"), encoding="utf-8") as f:
        data = json.load(f)
    for m in data["metrics"]:
        if m["category"] not in CATEGORIES:
            sys.exit("unknown category %r on metric %s" % (m["category"], m["id"]))
    ids = {c["id"] for c in data["cards"]}
    for _name, line in LINES:
        missing = [c for c in line if c not in ids]
        if missing:
            sys.exit("release line names unknown cards: %s" % missing)
    dates = [date.fromisoformat(c["date"]) for c in data["cards"]]
    if dates != sorted(dates):
        sys.exit("cards in metrics.json are not in release order")

    out, table, metrics, line_pairs = build(data)
    if "--report" in argv:
        report(out, table, metrics, line_pairs, [a for a in argv if not a.startswith("--")])
        return
    text = json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n"
    path = os.path.join(ROOT, OUT)
    old = None
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            old = f.read()
    if old == text:
        print("system-cards/%s is up to date" % OUT)
        return
    if check:
        print("system-cards/%s is out of date; run python3 scripts/build-release-deltas.py" % OUT)
        sys.exit(1)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote system-cards/%s (%d figures, %d card pairs, %.0f KB)" % (OUT, len(table), len(out["pairs"]), len(text) / 1024.0))


if __name__ == "__main__":
    main()
