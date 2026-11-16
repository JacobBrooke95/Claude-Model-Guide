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


ENT = ["opus", "sonnet", "haiku", "fable_mythos"]
ECOL = {"opus": PAL[0], "sonnet": PAL[1], "haiku": PAL[2], "fable_mythos": PAL[3]}


def _proj_chart(R, key, title, sub, yr_, ylabel, hist, name, nextkey, note, thr=None):
    P = R["projection"]
    tq = np.array([yr(q) for q in P["quarters"]])
    b = P["series"][key]
    c = Chart(title, sub, xr=(2024.0, 2031.05), yr_=yr_, ylabel=ylabel, xticks=_yticks_years(2024, 2031), right=235)
    col = PAL[6]
    for lo, hi, a in (("lo95", "hi95", 0.82), ("lo80", "hi80", 0.66), ("lo50", "hi50", 0.48)):
        c.band(tq, [x[lo] for x in b], [x[hi] for x in b], _light(col, a), 255)
    c.line(tq, [x["median"] for x in b], col, 2)
    if thr is not None and thr < yr_[1]:
        c.band([2024.0, 2031.05], [thr, thr], [yr_[1], yr_[1]], "#8a8983", 38)
        c.line([2024.0, 2031.05], [thr, thr], INK2, 1, dash=3)
        c.text(2024.05, thr, "beyond the measured scale: today's benchmarks no longer separate models", 9, INK2, dx=4, dy=-15)
    c.vline(T_NOW, "as of " + AS_OF)
    c.vline(yr(P["backtested_through"]), "uncorrected code backtested to here; scenario projection after")
    for f in ["legacy"] + FAMILIES:
        pts = [p for p in hist["points"] if p["family"] == f]
        if pts:
            c.points([p["t"] for p in pts], [p["v"] for p in pts], FAMCOL[f], 4, label=f.capitalize() if f != "legacy" else "Earlier Claude")
    if hist.get("hollow"):
        c.points([p["t"] for p in hist["hollow"]], [p["v"] for p in hist["hollow"]], INK2, 4, hollow=True, label=hist["hollow_label"])
    for e in ENT:
        v = R["next_models"]["entities"][e]
        t = yr(v["release_date"]["median"])
        s = v[nextkey]
        c.err([t], [s["lo80"]], [min(s["hi80"], yr_[1])], ECOL[e], 2)
        c.err([s["median"]], [yr(v["release_date"]["q10"])], [yr(v["release_date"]["q90"])], ECOL[e], 2, horizontal=True)
        c.points([t], [s["median"]], ECOL[e], 5, square=True)
    c.legend_items += [("square", INK2, "Next model (Fable/Mythos in\nyellow): median, 80% interval,\n10-90% release window", None),
                       ("line", col, "Anthropic frontier,\nmixture median", None), ("band", _light(col, 0.48), "50% band", None),
                       ("band", _light(col, 0.66), "80% band", None), ("band", _light(col, 0.82), "95% band", None)]
    c.text(2031.0, min(b[-1]["median"], yr_[1] - 4), f"{b[-1]['median']:.0f}", 10, INK, dx=-30, dy=-16, bold=True)
    c.d.text((c.l, c.H - 16 * SS), note, font=_font(9), fill=INK2)
    c.save(name)


def make_all(R):
    O = R["_objects"]
    d = O["d"]
    m = d.models
    fam = lambda f: f if f in FAMILIES else "legacy"
    P = R["projection"]
    thr, cap = R["scale"]["beyond_measured_scale_above_eci"], R["scale"]["display_cap_eci"]
    for old in OUT.glob("*.png"):
        old.unlink()
    cl = m[(m.lab == "Anthropic") & m.eci.notna()]
    hist_e = dict(points=[dict(t=r.t, v=r.eci, family=fam(r.family)) for r in cl.itertuples()])
    _proj_chart(R, "anthropic_frontier_eci", "Anthropic frontier on Epoch's public ECI, 2024-2030",
                "Bands: scenario mixture (central prior), calibrated on the backtest of this code. Axis stops at the display cap (%d)." % cap,
                (110, cap), "Public ECI", hist_e, "main_eci.png", "eci",
                "History: every Claude model Epoch scores (Mythos is not scored; its Fable twin is shown).", thr)
    a6 = d.aeci("fable5.2")
    pr_ = a6[a6.value_type.isin(["printed", "anchor_by_definition"]) & a6.t.notna()]
    fr = a6[(a6.value_type == "figure_read") & a6.t.notna()]
    hist_a = dict(points=[dict(t=r.t, v=r.value, family=fam(r.family)) for r in pr_.itertuples()],
                  hollow=[dict(t=r.t, v=r.value) for r in fr.itertuples()], hollow_label="Figure read\n(not printed)")
    acap = float(O["mp"].apply_point(np.array([cap]), "offset")[0])
    _proj_chart(R, "anthropic_frontier_aeci_nov6_scale", "Anthropic frontier on the AECI scale (November 6 2026 fit), 2024-2030",
                "Secondary: public-ECI paths carried through the ECI-to-AECI mapping. Squares are next-model values on this same scale.",
                (120, round(acap, -1)), "AECI, Nov 6 fit", hist_a, "main_aeci.png", "aeci_nov6_scale",
                "History: values printed in the Fable 5.2 / Mythos 5.2 card (filled) and figure reads (hollow). Later cards will re-estimate the scale.",
                float(O["mp"].apply_point(np.array([thr]), "offset")[0]))
    # ---- scenario fan
    tq = np.array([yr(q) for q in P["quarters"]])
    c = Chart("Scenario paths: Anthropic frontier, public ECI", "Median path of each scenario (prior weight in the legend) and the 80% band of the mixture.",
              xr=(2026.8, 2031.05), yr_=(165, cap + 60), ylabel="Public ECI", xticks=_yticks_years(2027, 2031), right=250)
    mixb = P["series"]["anthropic_frontier_eci"]
    c.band(tq, [b["lo80"] for b in mixb], [min(b["hi80"], cap + 60) for b in mixb], _light(PAL[6], 0.75), 255)
    c.line([2026.8, 2031.05], [thr, thr], INK2, 1, dash=3)
    c.text(2026.85, thr, "beyond the measured scale above this line", 9, INK2, dy=-15)
    scol = {"slowdown": PAL[7], "reversion": PAL[1], "hold": PAL[0], "compounding": PAL[2], "explosive": PAL[3]}
    for s_, colr in scol.items():
        b = P["scenario_series"][s_]["anthropic_frontier_eci"]
        c.line(tq, [min(x["median"], cap + 60) for x in b], colr, 2, label=f"{s_} ({P['weights']['central'][s_]:.0%})")
    c.line(tq, [b["median"] for b in mixb], INK, 2, dash=4, label="mixture median")
    c.legend_items.append(("band", _light(PAL[6], 0.75), "mixture 80% band", None))
    c.vline(yr(P["backtested_through"]), "backtested to here")
    c.save("scenario_paths.png")
    # ---- release backtest
    rel = O["rel"]
    c = Chart("Backtest: predicted vs actual public ECI of each Claude release (all folds)",
              "Rolling origin. Bars: the model's 80% interval. On the diagonal = perfect.", xr=(120, 180), yr_=(120, 180),
              xlabel="Predicted (median)", ylabel="Actual public ECI", w=900, h=760, right=235)
    c.line([120, 180], [120, 180], INK2, 1)
    for meth, ld, colr, lab in (("model", 0.0, PAL[0], "day-of, date given"), ("model_date_unknown", 0.25, PAL[1], "3 months ahead,\ndate not given"),
                                ("model_date_unknown", 0.5, PAL[2], "6 months ahead,\ndate not given")):
        g = rel[(rel.method == meth) & (rel.lead == ld)]
        c.err(g.y.to_numpy(), g.lo80.to_numpy(), g.hi80.to_numpy(), _light(colr, 0.45), 2, horizontal=True)
        c.points(g["median"].to_numpy(), g.y.to_numpy(), colr, 4, label=f"{lab} (n={len(g)})")
    c.save("backtest_pred_vs_actual.png")
    s0 = R["release_backtest"]["summary_by_lead"]
    meths = [("model", "Model"), ("prev_plus_slope", "Previous + 12-month\nAnthropic slope"), ("all_history_linear", "All-history\nall-lab line"),
             ("trailing_12m_linear", "Trailing-12-month\nall-lab line"), ("family_mean_step", "Previous + mean\nfamily step"), ("prev_in_family", "Previous model\nin family")]
    c = Chart("Backtest error by method, all folds", "RMSE in public-ECI points at lead 0 (dark) and 3 months (light); n per bar differs where a baseline is undefined.",
              xr=(0, 12), yr_=(0, len(meths)), w=900, h=520, xlabel="RMSE, ECI points", yticks=[], left=170, right=60)
    for i, (k, lab) in enumerate(meths):
        y = len(meths) - i - 0.5
        for ld, off, shade in (("0.0", 0.17, 0.0), ("0.25", -0.17, 0.5)):
            v = s0[ld].get(k)
            if not v:
                continue
            colr = _light(PAL[0] if k == "model" else "#8a8983", shade)
            c.d.rounded_rectangle([c.l, float(c.py(y + off + 0.15)), float(c.px(v["rmse"])), float(c.py(y + off - 0.15))], radius=3 * SS, fill=colr)
            c.text(v["rmse"], y + off, f"{v['rmse']:.1f} (n={v['n']})", 10, INK, dx=6, dy=-7)
        for j, ln in enumerate(lab.split("\n")):
            c.d.text((12 * SS, float(c.py(y)) - (14 - j * 14) * SS), ln, font=_font(10), fill=INK2)
    c.save("backtest_vs_baselines.png")
    # ---- machine backtest: errors by target date
    c = Chart("Backtest of the projection code: frontier error by horizon", "Actual minus predicted median (raw, before the bias term). Positive = under-prediction.",
              xr=(2024.9, 2027.0), yr_=(-8, 16), ylabel="ECI points", xticks=[(2025, "2025"), (2025.5, "mid-2025"), (2026, "2026"), (2026.5, "mid-2026"), (2027, "2027")], right=235)
    c.line([2024.9, 2027.0], [0, 0], INK2, 1)
    for key, hollow in (("anthropic", False), ("all_lab", True)):
        for h, colr in ((0.5, PAL[0]), (1.0, PAL[1]), (1.5, PAL[2])):
            pts = [f for f in R["machine_backtest"][key]["per_fold"] if f["h"] == h]
            c.points([f["t"] for f in pts], [f["err_raw"] for f in pts], colr, 4, hollow=hollow,
                     label=f"{'Anthropic' if key == 'anthropic' else 'All labs'}, {h} yr (n={len(pts)})")
    c.save("machine_backtest.png")
    # ---- calibration
    c = Chart("Interval coverage in backtest (raw, before calibration)", "Share of actual values inside the nominal interval. On the diagonal = calibrated; above = too wide.",
              xr=(0.4, 1.0), yr_=(0.0, 1.05), xlabel="Nominal coverage", ylabel="Observed coverage", w=900, h=640,
              xticks=[(0.5, "50%"), (0.8, "80%"), (0.95, "95%")], right=290)
    c.line([0.4, 1.0], [0.4, 1.0], INK2, 1)
    cal = R["release_backtest"]["calibration"]
    mb = R["machine_backtest"]
    sets = [("Ability, lead 0 (n=%d)" % cal["date_given_lead_0"]["n_folds"], cal["date_given_lead_0"]),
            ("Ability, date unknown,\n3-6 months (n=%d)" % cal["date_unknown_leads_3_6_months"]["n_folds"], cal["date_unknown_leads_3_6_months"]),
            ("Benchmarks, anchored (n=%d)" % R["links"]["calibration_pooled"]["n_folds"], R["links"]["calibration_pooled"]),
            ("Anthropic frontier, 0.5 yr (n=%d)" % mb["anthropic"]["calibration"]["0.5"]["n_folds"], mb["anthropic"]["calibration"]["0.5"]),
            ("Anthropic frontier, 1 yr (n=%d)" % mb["anthropic"]["calibration"]["1.0"]["n_folds"], mb["anthropic"]["calibration"]["1.0"]),
            ("All-lab frontier, 1 yr (n=%d)" % mb["all_lab"]["calibration"]["1.0"]["n_folds"], mb["all_lab"]["calibration"]["1.0"])]
    for i, (lab, cc) in enumerate(sets):
        xs, ys = [0.5, 0.8, 0.95], [cc["raw_cov50"], cc["raw_cov80"], cc["raw_cov95"]]
        c.line(xs, ys, PAL[i], 2, label=lab)
        c.points(xs, ys, PAL[i], 4)
    c.save("calibration.png")
    # ---- family steps
    hs = d.claude().sort_values("t")
    c = Chart("Within-family steps in public ECI", "Each dot: one release's gain over its predecessor in the same family, against months since that predecessor. None is negative.",
              xr=(0, 13), yr_=(-2, 20), xlabel="Months since the family's previous release", ylabel="ECI gain", w=900, h=600, right=200)
    c.line([0, 13], [0, 0], INK2, 1)
    for f in ["opus", "sonnet", "haiku", "fable"]:
        g = hs[hs.family == f]
        c.points(np.diff(g.t.to_numpy()) * 12, np.diff(g.eci.to_numpy()), FAMCOL[f], 5, label=f.capitalize())
    sl = R["trend"]["level_process"]["anthropic"]["recent_slope"]["median"]
    c.line([0, 13], [0, sl * 13 / 12], INK2, 1, dash=3, label=f"recent record-line slope\n({sl:.0f} ECI/yr)")
    c.save("family_steps.png")
    # ---- benchmark links
    L = [r for r in R["links"]["table"] if r["admitted"]] + [r for r in R["links"]["table"] if not r["admitted"]]
    cols = 4
    rows = math.ceil(len(L) / cols)
    cw, ch = 330, 250
    sheet = Image.new("RGB", (cols * cw, rows * ch + 40), SURF)
    ImageDraw.Draw(sheet).text((14, 10), "Benchmark links: scores against public ECI, fitted curve, estimated ceiling (dashed), and next-model predictions "
                               "(squares, 80% interval) where published", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12), fill=INK)
    for i, r in enumerate(L):
        ys = [p["score"] for p in r["points"]]
        ylog = r["kind"] == "loghorizon"
        if r["kind"] == "bounded":
            lo, hi = 0, 100
        elif ylog:
            lo, hi = 1, 1e4
        else:
            lo, hi = min(ys), max(ys) * 1.25
        pad = 0 if ylog else (hi - lo) * 0.05
        cc = Chart(r["title"] + ("" if r["admitted"] else "  [not published]"), f"{r['unit']}; n={r['n']}", w=cw, h=ch, xr=(115, 190),
                   yr_=(lo - pad if not ylog else lo, hi + pad if not ylog else hi), ylog=ylog,
                   xticks=[(120, "120"), (140, "140"), (160, "160"), (180, "180")], left=52, right=14, top=62, bottom=34, title_size=11,
                   yticks=[(v, f"{v:g}") for v in ([1, 10, 100, 1000, 10000] if ylog else Chart._nice(lo, hi, 4))])
        cc.points([p["eci"] for p in r["points"]], ys, "#b9b8b2", 2)
        cur = r["curve"]
        mk = [(115 <= e <= 190) for e in cur["eci"]]
        cc.line([e for e, k in zip(cur["eci"], mk) if k], [s_ for s_, k in zip(cur["score"], mk) if k], PAL[0], 2)
        if r.get("ceiling") is not None:
            cc.line([115, 190], [r["ceiling"], r["ceiling"]], INK2, 1, dash=3)
        if r["admitted"]:
            for e in ENT:
                v = R["next_models"]["entities"][e]
                b = v["benchmarks"].get(r["benchmark"], {})
                if b.get("available"):
                    cc.err([v["eci"]["median"]], [b["lo80"]], [min(b["hi80"], hi)], ECOL[e], 2)
                    cc.points([v["eci"]["median"]], [b["median"]], ECOL[e], 3, square=True)
        cc.legend_items = []
        sheet.paste(cc.img.convert("RGB").resize((cw, ch), Image.LANCZOS), ((i % cols) * cw, 40 + (i // cols) * ch))
    sheet.save(OUT / "benchmark_links.png", optimize=True)
    # ---- AECI own-card gap
    oc = R["aeci"]["own_card"]
    n = len(oc["table"])
    c = Chart("Own-card AECI minus public ECI, by system card", "One point per card that printed the model's own AECI. Band: the predicted gap for the next card (80%).",
              xr=(-0.5, n + 0.8), yr_=(-10, 14), ylabel="AECI points", w=1000, h=560, right=40,
              xticks=[(i, r["model_id"].replace("Claude ", "")) for i, r in enumerate(oc["table"])] + [(n, "next card")])
    c.line([-0.5, n + 0.8], [0, 0], INK2, 1)
    pg, sd = oc["summary"]["predicted_gap"], oc["summary"]["sd"]
    c.band([n - 0.3, n + 0.3], [pg - 1.28 * sd] * 2, [pg + 1.28 * sd] * 2, _light(PAL[6], 0.6), 255)
    c.line([n - 0.3, n + 0.3], [pg, pg], PAL[6], 2)
    c.line(list(range(n)), [r["gap"] for r in oc["table"]], _light(PAL[0], 0.5), 2)
    c.points(list(range(n)), [r["gap"] for r in oc["table"]], PAL[0], 5)
    c.legend_items = []
    c.save("aeci_own_card_gap.png")
    ov = R["aeci"]["nov6_mapping"]["overlap"]
    c = Chart("AECI (Nov 6 fit) against public ECI for the same Claude models (secondary mapping)", "Mythos values are paired with the Fable twin's public ECI.",
              xr=(120, 190), yr_=(120, 200), xlabel="Public ECI", ylabel="AECI, November 6 2026 fit", w=900, h=700, right=220)
    c.line([120, 190], [120, 190], INK2, 1, label="AECI = ECI")
    gx = np.linspace(120, 190, 141)
    c.line(gx, O["mp"].apply_point(gx, "hinge"), PAL[1], 2, label="hinge form")
    c.line(gx, O["mp"].apply_point(gx, "offset"), PAL[2], 2, label="level-shift form")
    c.points([o["eci"] for o in ov], [o["aeci"] for o in ov], PAL[0], 4, label="overlap models (n=%d)" % len(ov))
    c.save("aeci_mapping.png")
    return sorted(p.name for p in OUT.glob("*.png"))
