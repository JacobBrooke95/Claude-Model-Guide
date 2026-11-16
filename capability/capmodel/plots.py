"""Diagnostic PNG plots drawn with Pillow (matplotlib is not installed here).

Static review figures: one y-axis each, recessive grid, 2px lines, a legend whenever two
or more series share a panel, text in ink colours only. Colours are the dataviz reference
palette in fixed slot order; a family keeps its colour in every figure."""
from __future__ import annotations
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .common import OUT, yr, AS_OF, FAMILIES

SS = 2   # supersampling factor
SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
PAL = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
FAMCOL = {"opus": PAL[0], "sonnet": PAL[1], "haiku": PAL[2], "fable": PAL[3], "mythos": PAL[4], "legacy": "#8a8983",
          "all": PAL[6], "other": "#b9b8b2"}
T_NOW = yr(AS_OF)


def _font(size, bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")
    try:
        return ImageFont.truetype(p, size * SS)
    except OSError:
        return ImageFont.load_default()


def _rgb(hexc, a=255):
    hexc = hexc.lstrip("#")
    return tuple(int(hexc[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


class Chart:
    def __init__(self, title, subtitle="", w=1200, h=680, xr=(0, 1), yr_=(0, 1), ylog=False, xlabel="", ylabel="",
                 xticks=None, yticks=None, left=78, right=200, top=74, bottom=58, title_size=17):
        self.W, self.H = w * SS, h * SS
        self.img = Image.new("RGBA", (self.W, self.H), _rgb(SURF))
        self.d = ImageDraw.Draw(self.img)
        self.l, self.r, self.t, self.b = left * SS, (w - right) * SS, top * SS, (h - bottom) * SS
        self.xr, self.yr, self.ylog = xr, yr_, ylog
        self.legend_items = []
        self.d.text((self.l, 14 * SS), title, font=_font(title_size, True), fill=INK)
        if subtitle:
            self.d.text((self.l, 40 * SS), subtitle, font=_font(11), fill=INK2)
        xticks = xticks if xticks is not None else [(v, f"{v:g}") for v in np.linspace(xr[0], xr[1], 6)]
        yticks = yticks if yticks is not None else [(v, f"{v:g}") for v in self._nice(yr_[0], yr_[1])]
        for v, lab in yticks:
            y = self.py(v)
            self.d.line([(self.l, y), (self.r, y)], fill=GRID, width=SS)
            tw = self.d.textlength(lab, font=_font(10))
            self.d.text((self.l - tw - 6 * SS, y - 7 * SS), lab, font=_font(10), fill=INK2)
        for v, lab in xticks:
            x = self.px(v)
            self.d.line([(x, self.b), (x, self.b + 4 * SS)], fill=INK2, width=SS)
            tw = self.d.textlength(lab, font=_font(10))
            self.d.text((x - tw / 2, self.b + 7 * SS), lab, font=_font(10), fill=INK2)
        self.d.line([(self.l, self.b), (self.r, self.b)], fill=INK2, width=SS)
        if xlabel:
            tw = self.d.textlength(xlabel, font=_font(11))
            self.d.text(((self.l + self.r) / 2 - tw / 2, self.b + 28 * SS), xlabel, font=_font(11), fill=INK2)
        if ylabel:
            self.d.text((self.l, self.t - 18 * SS), ylabel, font=_font(11), fill=INK2)

    @staticmethod
    def _nice(lo, hi, n=6):
        span = hi - lo
        step = 10 ** math.floor(math.log10(span / n))
        for m in (1, 2, 5, 10):
            if span / (step * m) <= n + 1:
                step *= m
                break
        v = math.ceil(lo / step) * step
        out = []
        while v <= hi + 1e-9:
            out.append(round(v, 6))
            v += step
        return out

    def px(self, x):
        return self.l + (np.asarray(x, float) - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.r - self.l)

    def py(self, y):
        y = np.asarray(y, float)
        if self.ylog:
            f = (np.log10(np.maximum(y, 1e-12)) - math.log10(self.yr[0])) / (math.log10(self.yr[1]) - math.log10(self.yr[0]))
        else:
            f = (y - self.yr[0]) / (self.yr[1] - self.yr[0])
        return self.b - np.clip(f, -0.02, 1.02) * (self.b - self.t)

    def band(self, x, lo, hi, color, alpha=60):
        ov = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
        pts = list(zip(self.px(x), self.py(hi))) + list(zip(self.px(x)[::-1], self.py(lo)[::-1]))
        ImageDraw.Draw(ov).polygon(pts, fill=_rgb(color, alpha))
        self.img = Image.alpha_composite(self.img, ov)
        self.d = ImageDraw.Draw(self.img)

    def line(self, x, y, color, width=2, dash=None, label=None):
        pts = list(zip(self.px(x), self.py(y)))
        if dash is None:
            self.d.line(pts, fill=color, width=width * SS, joint="curve")
        else:
            for i in range(len(pts) - 1):
                (x0, y0), (x1, y1) = pts[i], pts[i + 1]
                L = math.hypot(x1 - x0, y1 - y0)
                n = max(int(L / (dash * SS * 2)), 1)
                for k in range(n):
                    a, b = k / n, (k + 0.5) / n
                    self.d.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)],
                                fill=color, width=width * SS)
        if label:
            self.legend_items.append(("line", color, label, dash))

    def points(self, x, y, color, r=4, hollow=False, label=None, square=False):
        for xi, yi in zip(np.atleast_1d(self.px(x)), np.atleast_1d(self.py(y))):
            if xi < self.l - 1 or xi > self.r + 1:
                continue
            box = [xi - r * SS, yi - r * SS, xi + r * SS, yi + r * SS]
            f = self.d.rectangle if square else self.d.ellipse
            f(box, fill=SURF if hollow else color, outline=color if hollow else SURF, width=(2 if hollow else 1) * SS)
        if label:
            self.legend_items.append(("hollow" if hollow else ("square" if square else "dot"), color, label, None))

    def err(self, x, lo, hi, color, width=2, horizontal=False):
        for xi, a, b in zip(np.atleast_1d(x), np.atleast_1d(lo), np.atleast_1d(hi)):
            if horizontal:
                self.d.line([(float(self.px(a)), float(self.py(xi))), (float(self.px(b)), float(self.py(xi)))], fill=color, width=width * SS)
            else:
                self.d.line([(float(self.px(xi)), float(self.py(a))), (float(self.px(xi)), float(self.py(b)))], fill=color, width=width * SS)

    def text(self, x, y, s, size=10, color=INK2, dx=6, dy=-7, bold=False):
        self.d.text((float(self.px(x)) + dx * SS, float(self.py(y)) + dy * SS), s, font=_font(size, bold), fill=color)

    def vline(self, x, label=None):
        X = float(self.px(x))
        for k in range(int(self.t), int(self.b), 8 * SS):
            self.d.line([(X, k), (X, k + 4 * SS)], fill=INK2, width=SS)
        if label:
            self.d.text((X + 4 * SS, self.t + 2 * SS), label, font=_font(9), fill=INK2)

    def legend(self, extra=None):
        items = self.legend_items + (extra or [])
        x, y = self.r + 14 * SS, self.t
        for kind, color, label, dash in items:
            if kind == "line":
                self.d.line([(x, y + 7 * SS), (x + 22 * SS, y + 7 * SS)], fill=color, width=2 * SS)
                if dash:
                    self.d.line([(x + 8 * SS, y + 7 * SS), (x + 14 * SS, y + 7 * SS)], fill=SURF, width=3 * SS)
            elif kind == "band":
                self.d.rectangle([x, y + 2 * SS, x + 22 * SS, y + 12 * SS], fill=_rgb(color, 255))
            else:
                box = [x + 6 * SS, y + 2 * SS, x + 16 * SS, y + 12 * SS]
                if kind == "square":
                    self.d.rectangle(box, fill=color)
                else:
                    self.d.ellipse(box, fill=SURF if kind == "hollow" else color, outline=color, width=2 * SS)
            for i, ln in enumerate(label.split("\n")):
                self.d.text((x + 28 * SS, y + i * 13 * SS), ln, font=_font(10), fill=INK2)
            y += (16 + 13 * label.count("\n")) * SS

    def save(self, name):
        if self.legend_items:
            self.legend()
        OUT.mkdir(exist_ok=True)
        im = self.img.convert("RGB").resize((self.W // SS, self.H // SS), Image.LANCZOS)
        im.save(OUT / name, optimize=True)


def _light(color, f=0.6):
    r, g, b, _ = _rgb(color)
    s = _rgb(SURF)
    return "#%02x%02x%02x" % tuple(int(c + (sc - c) * f) for c, sc in ((r, s[0]), (g, s[1]), (b, s[2])))


def _yticks_years(a, b):
    return [(y, str(y)) for y in range(int(math.ceil(a)), int(b) + 1)]


def _proj_chart(R, key, title, sub, yr_, ylabel, hist, name, nextkey, hist_note):
    P = R["projection"]
    tq = np.array([yr(q) for q in P["quarters"]])
    mixb = P["series"][key]["mixture"]
    c = Chart(title, sub, xr=(2024.0, 2031.05), yr_=yr_, ylabel=ylabel, xticks=_yticks_years(2024, 2031), right=230)
    col = PAL[6]
    x = np.concatenate([[T_NOW], tq])
    cur = hist["cur"]
    for lo, hi, a in (("lo95", "hi95", 0.82), ("lo80", "hi80", 0.66), ("lo50", "hi50", 0.48)):
        c.band(x, np.concatenate([[cur], [b[lo] for b in mixb]]), np.concatenate([[cur], [b[hi] for b in mixb]]), _light(col, a), 255)
    c.line(x, np.concatenate([[cur], [b["median"] for b in mixb]]), col, 2)
    c.vline(T_NOW, "as of " + AS_OF)
    for f in ["legacy"] + FAMILIES:
        pts = [p for p in hist["points"] if p["family"] == f]
        if pts:
            c.points([p["t"] for p in pts], [p["v"] for p in pts], FAMCOL[f], 4, label=f.capitalize() if f != "legacy" else "Earlier Claude")
    if hist.get("hollow"):
        c.points([p["t"] for p in hist["hollow"]], [p["v"] for p in hist["hollow"]], INK2, 4, hollow=True, label=hist["hollow_label"])
    for f in FAMILIES:
        v = R["next_models"]["families"][f]
        if not v["resolvable"]["aeci" if "aeci" in nextkey else "eci"]:
            continue
        t = yr(v["release_date"]["median"])
        s = v[nextkey]
        c.err([t], [s["lo80"]], [s["hi80"]], FAMCOL[f], 2)
        c.err([s["median"]], [yr(v["release_date"]["q10"])], [yr(v["release_date"]["q90"])], FAMCOL[f], 2, horizontal=True)
        c.points([t], [s["median"]], FAMCOL[f], 5, square=True)
    c.legend_items += [("square", INK2, "Next model in family:\nmedian, 80% interval,\n10-90% release window", None),
                       ("line", col, "Anthropic frontier,\nmixture median", None), ("band", _light(col, 0.48), "50% band", None),
                       ("band", _light(col, 0.66), "80% band", None), ("band", _light(col, 0.82), "95% band", None)]
    for b in (mixb[-1],):
        c.text(2031.0, b["median"], f"{b['median']:.0f}", 10, INK, dx=-30, dy=-16, bold=True)
    c.d.text((c.l, c.H - 16 * SS), hist_note, font=_font(9), fill=INK2)
    c.save(name)


def make_all(R):
    O = R["_objects"]
    d, om = O["d"], O["om"]
    m = d.models
    fam = lambda f: f if f in FAMILIES else "legacy"
    # ---- 1/2. main charts
    a6 = d.aeci("fable5.2")
    pr_ = a6[a6.value_type.isin(["printed", "anchor_by_definition"]) & a6.t.notna()]
    fr = a6[(a6.value_type == "figure_read") & a6.t.notna()]
    est = d.aeci("fable5.2_repo_rescaled")
    hist_a = dict(cur=177.12, points=[dict(t=r.t, v=r.value, family=fam(r.family)) for r in pr_.itertuples()],
                  hollow=[dict(t=r.t, v=r.value) for r in fr.itertuples()] + [dict(t=r.t, v=r.value) for r in est.itertuples()],
                  hollow_label="Figure read or site\nestimate (not printed)")
    ymax_a = round(R["projection"]["series"]["anthropic_frontier_aeci"]["mixture"][-1]["hi80"] * 1.03, -1)
    _proj_chart(R, "anthropic_frontier_aeci", "Anthropic frontier on the AECI scale, 2024-2030",
                "AECI points on the November 6 2026 fit (later cards re-estimate the scale). Bands: scenario mixture, central weights. "
                "Axis cut at %d; the 95%% band continues above." % ymax_a,
                (120, ymax_a), "AECI", hist_a, "main_aeci.png", "aeci_nov6_scale",
                "History: values printed in the Fable 5.2 / Mythos 5.2 card (filled) and figure reads (hollow). Fable has no printed AECI (Mythos twin is shown).")
    cl = m[(m.lab == "Anthropic") & m.eci.notna()]
    hist_e = dict(cur=float(om.anth.F0), points=[dict(t=r.t, v=r.eci, family=fam(r.family)) for r in cl.itertuples()])
    ymax_e = round(R["projection"]["series"]["anthropic_frontier_eci"]["mixture"][-1]["hi80"] * 1.03, -1)
    _proj_chart(R, "anthropic_frontier_eci", "Anthropic frontier on Epoch's public ECI, 2024-2030",
                "Public ECI (Epoch's Bayesian fit of November 2026). Bands: scenario mixture, central weights. Axis cut at %d." % ymax_e,
                (110, ymax_e), "Public ECI", hist_e, "main_eci.png", "eci",
                "History: every Claude model Epoch scores. Mythos is not scored by Epoch (Fable twin is shown).")
    # ---- 3. scenario fan
    P = R["projection"]
    tq = np.array([yr(q) for q in P["quarters"]])
    c = Chart("Scenario fan: Anthropic frontier, public ECI", "Median path of each scenario (lines) and the 80% band of the mixture. "
              "Weights in the legend are the central prior.", xr=(2026.5, 2031.05), yr_=(165, 400), ylabel="Public ECI",
              xticks=_yticks_years(2027, 2031), right=250)
    mixb = P["series"]["anthropic_frontier_eci"]["mixture"]
    c.band(tq, [b["lo80"] for b in mixb], [b["hi80"] for b in mixb], _light(PAL[6], 0.75), 255)
    scol = {"slowdown": PAL[7], "reversion": PAL[1], "hold": PAL[0], "compounding": PAL[2], "explosive": PAL[3]}
    for s, colr in scol.items():
        b = P["series"]["anthropic_frontier_eci"][s]
        c.line(tq, [x["median"] for x in b], colr, 2, label=f"{s} ({P['weights']['central'][s]:.0%})")
        c.text(tq[-1], min(b[-1]["median"], 398), f"{b[-1]['median']:.0f}", 10, INK, dx=-28, dy=-15)
    c.line(tq, [b["median"] for b in mixb], INK, 2, dash=4, label="mixture median")
    c.legend_items.append(("band", _light(PAL[6], 0.75), "mixture 80% band", None))
    c.save("scenario_fan.png")
    # ---- 4. trend-model comparison
    cv = R["trend"]["candidate_curves_anthropic"]
    c = Chart("Trend candidates for Anthropic's record line", "Each line is one candidate's median level, fitted on public-ECI records to "
              + AS_OF + ". Weights are the live combination weights.", xr=(2025.5, 2028.0), yr_=(140, 215), ylabel="Public ECI",
              xticks=[(2025.5, "mid-2025"), (2026, "2026"), (2026.5, "mid-2026"), (2027, "2027"), (2027.5, "mid-2027"), (2028, "2028")], right=250)
    w = R["release_backtest"]["live_trend_weights"]
    for i, (k, v) in enumerate(cv.items()):
        keep = [j for j, t in enumerate(v["t"]) if k != "pool_all" or t >= T_NOW]   # the pooled candidate is defined forward only
        c.line([v["t"][j] for j in keep], [v["median"][j] for j in keep], PAL[i], 2, label=f"{k} ({w[k]:.0%})")
    rec = R["trend"]["records_anthropic"]
    c.points([r["t"] for r in rec], [r["eci"] for r in rec], INK, 4, label="Anthropic record-setters")
    c.vline(T_NOW, "as of " + AS_OF)
    c.save("trend_models.png")
    # ---- 5. backtest predicted vs actual (lead 0 and lead>0)
    rel = O["rel"]
    mm = rel[rel.method == "model"]
    c = Chart("Backtest: predicted vs actual public ECI of each Claude release",
              "Rolling origin, no future data. Bars are the model's 80% interval (before calibration). Points on the diagonal are perfect.",
              xr=(120, 180), yr_=(120, 180), xlabel="Predicted (median)", ylabel="Actual public ECI", w=900, h=760, right=210)
    c.line([120, 180], [120, 180], INK2, 1)
    for ld, colr, lab in ((0.0, PAL[0], "day-of nowcast"), (0.25, PAL[1], "3 months ahead"), (0.5, PAL[2], "6 months ahead")):
        g = mm[mm.lead == ld]
        c.err(g.y.to_numpy(), g.lo80.to_numpy(), g.hi80.to_numpy(), _light(colr, 0.45), 2, horizontal=True)
        c.points(g["median"].to_numpy(), g.y.to_numpy(), colr, 4, label=f"{lab} (n={len(g)})")
    c.save("backtest_pred_vs_actual.png")
    # ---- 6. backtest errors vs baselines
    s0 = R["release_backtest"]["summary_by_lead"]["0.0"]
    meths = [("model", "Model"), ("trailing_12m_linear", "Trailing-12-month\nall-lab trend"), ("all_history_linear", "All-history\nall-lab trend"),
             ("family_mean_step", "Previous + mean\nfamily step"), ("prev_in_family", "Previous model\nin family")]
    c = Chart("Backtest error by method (day-of folds, n=%d)" % s0["model"]["n"], "Root-mean-square error in public-ECI points; lower is better.",
              xr=(0, 10), yr_=(0, len(meths)), w=900, h=440, xlabel="RMSE, ECI points", yticks=[], left=170, right=60)
    for i, (k, lab) in enumerate(meths):
        v = s0[k]["rmse"]
        y = len(meths) - i - 0.5
        c.d.rounded_rectangle([c.l, float(c.py(y + 0.28)), float(c.px(v)), float(c.py(y - 0.28))], radius=4 * SS,
                              fill=PAL[0] if k == "model" else "#b9b8b2")
        c.text(v, y, f"{v:.1f}", 11, INK, dx=6, dy=-8, bold=True)
        for j, ln in enumerate(lab.split("\n")):
            c.d.text((12 * SS, float(c.py(y)) - (14 - j * 14) * SS), ln, font=_font(10), fill=INK2)
    c.save("backtest_vs_baselines.png")
    # ---- 7. calibration
    c = Chart("Interval coverage in backtest", "Share of actual values inside the nominal interval. On the diagonal = calibrated; above = intervals too wide.",
              xr=(0.4, 1.0), yr_=(0.2, 1.05), xlabel="Nominal coverage", ylabel="Observed coverage", w=900, h=640,
              xticks=[(0.5, "50%"), (0.8, "80%"), (0.95, "95%")], right=280)
    c.line([0.4, 1.0], [0.4, 1.0], INK2, 1)
    cal = R["release_backtest"]["calibration"]
    bc = R["benchmark_backtest"]["calibration"]["pooled"]
    sets = [("Ability, day-of (n=%d)" % cal["lead_0"]["n_folds"], cal["lead_0"], "raw_cov", PAL[0]),
            ("Ability, 3-6 months (n=%d)" % cal["lead_3_to_6_months"]["n_folds"], cal["lead_3_to_6_months"], "raw_cov", PAL[1]),
            ("Benchmark scores, raw (n=%d)" % bc["n_folds"], bc, "raw_cov", PAL[2]),
            ("Benchmark scores, calibrated\n(rolling, out of sample)", bc, "calibrated_cov", PAL[3])]
    for lab, cc, pre, colr in sets:
        xs, ys = [0.5, 0.8, 0.95], [cc[pre + "50"], cc[pre + "80"], cc[pre + "95"]]
        if any(v is None for v in ys):
            continue
        c.line(xs, ys, colr, 2, label=lab)
        c.points(xs, ys, colr, 4)
    c.save("calibration.png")
    # ---- 8. family offsets
    F = R["families"]
    c = Chart("Family offsets from Anthropic's record line", "Each dot is one release (public ECI minus the reference line). "
              "At right: square = pooled estimate, hollow = unpooled mean.", xr=(2024.0, 2027.0), yr_=(-13, 5),
              ylabel="ECI points relative to the record line", xticks=_yticks_years(2024, 2027), right=230)
    c.line([2024, 2027], [0, 0], INK2, 1)
    for f in ["opus", "sonnet", "haiku", "fable"]:
        pts = [o for o in F["offsets"] if o["family"] == f]
        c.points([o["t"] for o in pts], [o["offset"] for o in pts], FAMCOL[f], 4, label=f.capitalize())
        row = [r for r in F["table"] if r["family"] == f][0]
        c.points([2026.93], [row["unpooled_mean"]], FAMCOL[f], 5, hollow=True)
        c.points([2026.98], [row["pooled_mean"]], FAMCOL[f], 5, square=True)
    c.legend_items += [("hollow", INK2, "Unpooled recency-\nweighted mean", None), ("square", INK2, "Pooled estimate", None)]
    c.save("family_offsets.png")
    # ---- 9. benchmark links (small multiples)
    L = [r for r in R["links"]["table"] if r["group"] == "site"] + [r for r in R["links"]["table"] if r["group"] != "site"]
    n = len(L)
    cols = 4
    rows = math.ceil(n / cols)
    cw, ch = 330, 250
    sheet = Image.new("RGB", (cols * cw, rows * ch + 40), SURF)
    ImageDraw.Draw(sheet).text((14, 10), "Benchmark links: score against public ECI, fitted curve, and the next Fable's predicted score (80% interval)",
                               font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13), fill=INK)
    nf = R["next_models"]["families"]["fable"]
    for i, r in enumerate(L):
        ys = [p["score"] for p in r["points"]]
        lo, hi = (r["lo"], r["hi"]) if r["kind"] == "bounded" else (min(ys), max(max(ys), nf["benchmarks"][r["benchmark"]]["hi80"]))
        if r["kind"] == "bounded":
            lo, hi = 0, 100
        ylog = r["kind"] == "loghorizon"
        if ylog:
            lo, hi = 1, 1e5
        pad = 0 if ylog else (hi - lo) * 0.05
        cc = Chart(r["title"], f"{r['unit']}; n={r['n']}", w=cw, h=ch, xr=(115, 185), yr_=(lo - pad if not ylog else lo, hi + pad if not ylog else hi), ylog=ylog,
                   xticks=[(120, "120"), (140, "140"), (160, "160"), (180, "180")], left=52, right=14, top=62, bottom=34, title_size=12,
                   yticks=[(v, f"{v:g}") for v in ([1, 10, 100, 1000, 10000, 100000] if ylog else Chart._nice(lo, hi, 4))])
        cc.points([p["eci"] for p in r["points"]], ys, "#b9b8b2", 2)
        cur = r["curve"]
        mk = [(115 <= e <= 185) for e in cur["eci"]]
        cc.line([e for e, k in zip(cur["eci"], mk) if k], [s for s, k in zip(cur["score"], mk) if k], PAL[0], 2)
        b = nf["benchmarks"][r["benchmark"]]
        cc.err([nf["eci"]["median"]], [b["lo80"]], [b["hi80"]], PAL[3], 2)
        cc.points([nf["eci"]["median"]], [b["median"]], PAL[3], 4, square=True)
        cc.legend_items = []
        im = cc.img.convert("RGB").resize((cw, ch), Image.LANCZOS)
        sheet.paste(im, ((i % cols) * cw, 40 + (i // cols) * ch))
    sheet.save(OUT / "benchmark_links.png", optimize=True)
    # ---- 10. AECI mapping
    ov = R["aeci"]["overlap"]
    c = Chart("AECI (Nov 6 fit) against public ECI for the same Claude models", "Mythos values are paired with the Fable twin's public ECI. "
              "The two mapping forms differ only in how they extrapolate.", xr=(120, 190), yr_=(120, 200), xlabel="Public ECI",
              ylabel="AECI, November 6 2026 fit", w=900, h=700, right=220)
    c.line([120, 190], [120, 190], INK2, 1, label="AECI = ECI")
    gx = np.linspace(120, 190, 141)
    mp = O["mp"]
    c.line(gx, mp.apply_point(gx, "hinge"), PAL[1], 2, label="hinge form")
    c.line(gx, mp.apply_point(gx, "offset"), PAL[2], 2, label="level-shift form")
    c.points([o["eci"] for o in ov], [o["aeci"] for o in ov], PAL[0], 4, label="overlap models (n=%d)" % len(ov))
    c.save("aeci_mapping.png")
    return sorted(p.name for p in OUT.glob("*.png"))
