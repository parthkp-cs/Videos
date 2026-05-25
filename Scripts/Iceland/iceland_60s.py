from manim import *
import os

WHITE_BG  = "#FFFFFF"
DARK      = "#1A1A1A"
RED       = "#CC1B21"
AMBER     = "#D4821A"
BLUE      = "#1E5FA8"
GREEN     = "#2A7A3A"
GREY      = "#5A5A5A"
L_GREY    = "#BBBBBB"
FLAG_BLUE = "#003897"
FLAG_RED  = "#DC1E35"
H_PAD     = 1.5
V_PAD     = 0.9


def make_banker():
    """Stick figure in prison-stripe suit, built around ORIGIN."""
    body = Rectangle(width=0.68, height=1.0, color="#CCCCCC",
                     fill_color="#CCCCCC", fill_opacity=1, stroke_width=1.5
                     ).move_to(ORIGIN)
    stripes = VGroup(*[
        Line(UP * 0.5 + RIGHT * (i * 0.17 - 0.25),
             DOWN * 0.5 + RIGHT * (i * 0.17 - 0.25),
             color=DARK, stroke_width=3.5)
        for i in range(4)
    ])
    head = Circle(radius=0.27, color="#D4A47A", fill_color="#D4A47A",
                  fill_opacity=1, stroke_width=1.5).move_to(UP * 0.82)
    tie = Polygon(
        UP * 0.38 + LEFT * 0.08,
        UP * 0.38 + RIGHT * 0.08,
        UP * 0.02,
        color=RED, fill_color=RED, fill_opacity=1, stroke_width=0,
    )
    leg_l = Rectangle(width=0.27, height=0.48, color=DARK,
                      fill_color=DARK, fill_opacity=1, stroke_width=0
                      ).move_to(DOWN * 0.74 + LEFT * 0.18)
    leg_r = Rectangle(width=0.27, height=0.48, color=DARK,
                      fill_color=DARK, fill_opacity=1, stroke_width=0
                      ).move_to(DOWN * 0.74 + RIGHT * 0.18)
    return VGroup(leg_l, leg_r, body, stripes, tie, head)


def make_building(label, height=2.2, fill=DARK):
    body = Rectangle(width=1.05, height=height, color=fill,
                     fill_color=fill, fill_opacity=1, stroke_width=0)
    wins = VGroup(*[
        Rectangle(width=0.19, height=0.19, fill_color=AMBER,
                  fill_opacity=0.75, stroke_width=0, color=AMBER
                  ).move_to(body.get_center()
                            + RIGHT * (c * 0.38 - 0.19)
                            + UP * (r * 0.4 - height / 2 + 0.52))
        for r in range(int(height / 0.4)) for c in range(2)
    ])
    roof = Triangle(color=fill, fill_color=fill, fill_opacity=1,
                    stroke_width=0).scale(0.38).next_to(body, UP, buff=0)
    lbl = Text(label, font="Poppins", weight=BOLD,
               color=RED, font_size=13).next_to(body, DOWN, buff=0.12)
    return VGroup(body, wins, roof, lbl)


class Iceland60s(Scene):
    def construct(self):
        self.camera.background_color = WHITE_BG
        fw = config.frame_width
        fh = config.frame_height

        # ============================================================
        # BEAT 0 — Opening Title  0 → 5s  (SILENT)
        # ============================================================
        flag_bg = Rectangle(width=fw, height=fh, color=FLAG_BLUE,
                            fill_color=FLAG_BLUE, fill_opacity=1, stroke_width=0)
        cx = -fw * (2.0 / 18.0)
        wt = fh * (4.0 / 18.0)
        rt = fh * (2.0 / 18.0)
        wh = Rectangle(width=fw, height=wt, color=WHITE,
                       fill_color=WHITE, fill_opacity=1, stroke_width=0)
        wv = Rectangle(width=wt, height=fh, color=WHITE,
                       fill_color=WHITE, fill_opacity=1, stroke_width=0).shift(RIGHT * cx)
        rh = Rectangle(width=fw, height=rt, color=FLAG_RED,
                       fill_color=FLAG_RED, fill_opacity=1, stroke_width=0)
        rv = Rectangle(width=rt, height=fh, color=FLAG_RED,
                       fill_color=FLAG_RED, fill_opacity=1, stroke_width=0).shift(RIGHT * cx)
        flag = VGroup(flag_bg, wh, wv, rh, rv)

        t1 = Text("ICELAND", font="Poppins", weight=BOLD, color=DARK, font_size=56)
        t2 = Text("How to Steal an Island", font="Poppins", weight=LIGHT, color=DARK, font_size=27)
        t3 = Text("Episode 1  ·  874 AD – Present", font="Poppins", weight=LIGHT, color=DARK, font_size=17)
        tg = VGroup(t1, t2, t3).arrange(DOWN, buff=0.22)
        tg.to_corner(DR, buff=0).shift(LEFT * H_PAD + UP * V_PAD)
        card = Rectangle(width=tg.width + 0.65, height=tg.height + 0.38,
                         fill_color=WHITE, fill_opacity=0.88, stroke_width=0,
                         color=WHITE).move_to(tg.get_center())

        self.play(FadeIn(flag), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(card), FadeIn(tg), run_time=0.6)
        self.wait(2.4)
        fade_white = Rectangle(width=fw + 1, height=fh + 1,
                               fill_color=WHITE_BG, fill_opacity=0,
                               stroke_width=0).set_z_index(20)
        self.add(fade_white)
        self.play(fade_white.animate.set_fill(opacity=1), run_time=0.5)
        self.remove(flag, wh, wv, rh, rv, flag_bg, card, tg, fade_white)
        # t = 5s — VO begins

        # ============================================================
        # BEAT 1 — October 2008 + Global Collapse
        # Duration: 8.55s  →  5s → 13.55s
        # ============================================================
        oc = Text("October", font="Poppins", weight=BOLD, color=DARK, font_size=80)
        yr = Text("2008.", font="Poppins", weight=BOLD, color=RED, font_size=80)
        hl = VGroup(oc, yr).arrange(RIGHT, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(oc, shift=UP * 0.2), run_time=0.35)
        self.play(FadeIn(yr, shift=UP * 0.2), run_time=0.35)
        self.wait(0.3)
        self.play(FadeOut(hl), run_time=0.25)

        # Global contagion: Lehman (New York) → Iceland banks
        lehman = make_building("LEHMAN\nBROTHERS", height=2.6, fill="#2A3A5A")
        lehman.shift(LEFT * 4.5 + UP * 0.5)
        nyc = Text("New York", font="Poppins", weight=LIGHT,
                   color=GREY, font_size=15).next_to(lehman, DOWN, buff=0.08)

        b1 = make_building("KAUPTHING",  height=1.9)
        b2 = make_building("LANDSBANKI", height=2.1)
        b3 = make_building("GLITNIR",    height=1.8)
        banks = VGroup(b1, b2, b3).arrange(RIGHT, buff=0.55).shift(RIGHT * 2.5 + UP * 0.3)
        reyk = Text("Reykjavík", font="Poppins", weight=LIGHT,
                    color=GREY, font_size=15).next_to(banks, DOWN, buff=0.06)

        arrow = Arrow(lehman.get_right() + RIGHT * 0.1,
                      banks.get_left() + LEFT * 0.1,
                      color=RED, stroke_width=2.5, buff=0.1, max_tip_length_to_length_ratio=0.08)
        ctag = Text("contagion", font="Poppins", weight=LIGHT,
                    color=RED, font_size=14).next_to(arrow, UP, buff=0.07)

        # Floating global context bubbles
        def bubble(txt, pos):
            t = Text(txt, font="Poppins", weight=LIGHT, color=GREY, font_size=13)
            b = Rectangle(width=t.width + 0.3, height=t.height + 0.22,
                          color=L_GREY, fill_color=L_GREY, fill_opacity=0.5,
                          stroke_width=1).move_to(t.get_center())
            return VGroup(b, t).move_to(pos)

        bub1 = bubble("NYSE −40%",   UP * 2.4 + LEFT * 5.0)
        bub2 = bubble("UK banks",    UP * 2.4 + LEFT * 0.8)
        bub3 = bubble("€ in crisis", UP * 2.4 + RIGHT * 2.6)

        self.play(FadeIn(lehman), FadeIn(nyc), run_time=0.3)
        self.play(GrowArrow(arrow), FadeIn(ctag), run_time=0.45)
        self.play(GrowFromCenter(b1), GrowFromCenter(b2), GrowFromCenter(b3),
                  FadeIn(reyk), run_time=0.4)
        self.play(FadeIn(bub1), FadeIn(bub2), FadeIn(bub3), run_time=0.4)
        self.wait(0.7)

        # Lehman falls first
        self.play(lehman.animate.rotate(-PI / 2.1).shift(DOWN * 4.0 + LEFT * 0.5),
                  run_time=0.45, rate_func=rush_into)
        # Iceland banks follow
        self.play(
            b1.animate.rotate(-PI / 2.1).shift(DOWN * 4.5 + LEFT * 0.3),
            b2.animate.rotate(PI  / 2.1).shift(DOWN * 4.5),
            b3.animate.rotate(-PI / 2.1).shift(DOWN * 4.5 + RIGHT * 0.3),
            run_time=0.8, rate_func=rush_into,
        )
        crash = Text("COLLAPSED.", font="Poppins", weight=BOLD,
                     color=RED, font_size=96)
        self.play(GrowFromCenter(crash), run_time=0.35)
        self.wait(2.8)
        self.play(FadeOut(crash), FadeOut(arrow), FadeOut(ctag),
                  FadeOut(nyc), FadeOut(reyk),
                  FadeOut(bub1), FadeOut(bub2), FadeOut(bub3), run_time=0.3)
        # Fallen buildings are off-screen but still in the scene — remove them cleanly
        self.remove(lehman, banks, b1, b2, b3)
        self.wait(0.7)
        # t ≈ 13.5s ✓

        # ============================================================
        # BEAT 2 — 11×
        # Duration: 4.16s  →  13.55s → 17.71s
        # ============================================================
        big  = Text("11×", font="Poppins", weight=BOLD, color=DARK, font_size=290)
        stat = Text("bank assets  vs  entire economy",
                    font="Poppins", weight=LIGHT, color=GREY, font_size=26
                    ).next_to(big, DOWN, buff=0.5)
        self.play(GrowFromCenter(big), run_time=0.4)
        self.play(FadeIn(stat), run_time=0.3)
        self.wait(2.8)
        self.play(FadeOut(big), FadeOut(stat), run_time=0.35)
        # t ≈ 17.5s ✓

        # ============================================================
        # BEAT 3 — Crash Graphs
        # Duration: 5.39s  →  17.5s → 23s
        # ============================================================
        ax1 = Axes(x_range=[0, 10], y_range=[0, 10], x_length=5.0, y_length=3.4,
                   axis_config={"color": DARK, "stroke_width": 2}, tips=False
                   ).shift(LEFT * 3.2)
        ax2 = Axes(x_range=[0, 10], y_range=[0, 10], x_length=5.0, y_length=3.4,
                   axis_config={"color": DARK, "stroke_width": 2}, tips=False
                   ).shift(RIGHT * 3.2)
        l1 = Text("ISK (króna)", font="Poppins", weight=BOLD,
                  color=DARK, font_size=22).next_to(ax1, UP, buff=0.2)
        l2 = Text("Stock Market", font="Poppins", weight=BOLD,
                  color=DARK, font_size=22).next_to(ax2, UP, buff=0.2)
        ln1 = ax1.plot(lambda x: max(10 - x * 1.8, -0.5), x_range=[0, 5.8],
                       color=RED, stroke_width=4)
        ln2 = ax2.plot(lambda x: max(10 - x * 2.9, -0.5), x_range=[0, 3.8],
                       color=RED, stroke_width=4)
        p1 = Text("−55%", font="Poppins", weight=BOLD, color=RED,
                  font_size=30).next_to(ax1, DOWN, buff=0.15)
        p2 = Text("−90%", font="Poppins", weight=BOLD, color=RED,
                  font_size=30).next_to(ax2, DOWN, buff=0.15)

        self.play(FadeIn(ax1), FadeIn(l1), FadeIn(ax2), FadeIn(l2), run_time=0.3)
        self.play(Create(ln1), Create(ln2), run_time=1.6)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.3)
        self.wait(2.6)
        self.play(FadeOut(ax1), FadeOut(l1), FadeOut(ln1), FadeOut(p1),
                  FadeOut(ax2), FadeOut(l2), FadeOut(ln2), FadeOut(p2), run_time=0.3)
        # t ≈ 23s ✓

        # ============================================================
        # BEAT 4 — Grocery Shelves + Impact Stats
        # Duration: 12.9s  →  23s → 36s
        # ============================================================
        shelf_y = [1.5, 0.1, -1.3]
        planks = VGroup(*[
            Rectangle(width=10.0, height=0.16, color="#8B5E3C",
                      fill_color="#8B5E3C", fill_opacity=1, stroke_width=0
                      ).move_to([0, y, 0])
            for y in shelf_y
        ])
        bcols = [AMBER, BLUE, RED, GREEN, "#993399"] * 3
        boxes = VGroup(*[
            Rectangle(width=0.82, height=0.70, color=bcols[i],
                      fill_color=bcols[i], fill_opacity=1,
                      stroke_width=1.5, stroke_color=DARK,
                      ).move_to([(-1.9 + (i % 5) * 0.95), shelf_y[i // 5] + 0.44, 0])
            for i in range(15)
        ])
        shelf_lbl = Text("Imported food.", font="Poppins", weight=LIGHT,
                         color=GREY, font_size=20).to_edge(UP, buff=V_PAD)

        def stat_pill(val, lbl, c=RED):
            vt = Text(val, font="Poppins", weight=BOLD, color=c, font_size=26)
            lt = Text(lbl, font="Poppins", weight=LIGHT, color=DARK, font_size=13)
            g  = VGroup(vt, lt).arrange(DOWN, buff=0.08)
            bg = Rectangle(width=g.width + 0.45, height=g.height + 0.32,
                           color=c, fill_color=c, fill_opacity=0.1,
                           stroke_width=1.8).move_to(g.get_center())
            return VGroup(bg, vt, lt)

        # ±4.5 keeps pills well inside frame; y positions avoid all three shelf rows
        # Shelf rows: top boxes at y≈1.94, mid at y≈0.54, bottom at y≈-0.86
        sp1 = stat_pill("↑ 9%",  "Unemployment", RED  ).move_to(LEFT  * 4.5 + UP   * 2.5)
        sp2 = stat_pill("−10%", "GDP",           RED  ).move_to(LEFT  * 4.5 + DOWN * 1.7)
        sp3 = stat_pill("−55%", "Króna",         AMBER).move_to(RIGHT * 4.5 + UP   * 2.5)
        sp4 = stat_pill("800%", "Debt / GDP",    RED  ).move_to(RIGHT * 4.5 + DOWN * 1.7)

        self.play(FadeIn(planks), FadeIn(boxes), FadeIn(shelf_lbl), run_time=0.4)
        self.play(FadeIn(sp1), FadeIn(sp2), FadeIn(sp3), FadeIn(sp4), run_time=0.5)
        self.wait(0.4)
        self.play(LaggedStart(*[FadeOut(boxes[i]) for i in range(15)], lag_ratio=0.07),
                  run_time=1.5)
        self.wait(0.4)
        self.play(FadeOut(planks), FadeOut(shelf_lbl),
                  FadeOut(sp1), FadeOut(sp2), FadeOut(sp3), FadeOut(sp4), run_time=0.35)

        n1 = Text("300,000", font="Poppins", weight=BOLD, color=DARK,
                  font_size=130).move_to(UP * 0.9)
        n2 = Text("people.", font="Poppins", weight=LIGHT, color=GREY,
                  font_size=54).next_to(n1, DOWN, buff=0.2)
        n3 = Text("Bankrupt.", font="Poppins", weight=BOLD, color=RED,
                  font_size=54).next_to(n2, DOWN, buff=0.12)

        self.play(FadeIn(n1), run_time=0.4)
        self.play(FadeIn(n2), run_time=0.3)
        self.play(FadeIn(n3), run_time=0.35)
        self.wait(5.0)
        self.play(FadeOut(n1), FadeOut(n2), FadeOut(n3), run_time=0.4)
        # Beat 4 ≈ 0.4+0.5+0.4+1.5+0.4+0.35+0.4+0.3+0.35+7.0+0.4 = 12.0 → pad
        self.wait(0.6)
        # t ≈ 36s ✓

        # ============================================================
        # BEAT 5 — IMF Icons → Sweep → Banker Arrest
        # Duration: 15s  →  36s → 51s
        # ============================================================
        imf_hdr = Text("What most countries did:", font="Poppins",
                       weight=BOLD, color=DARK, font_size=26
                       ).to_edge(UP, buff=V_PAD)
        self.play(FadeIn(imf_hdr), run_time=0.3)

        # ── Icon builders ─────────────────────────────────────────
        def bail_out_icon():
            circ = Circle(radius=0.44, color=AMBER, fill_color=AMBER,
                          fill_opacity=0.15, stroke_width=2.5)
            neck = Rectangle(width=0.26, height=0.2, color=AMBER,
                             fill_color=AMBER, fill_opacity=0.5,
                             stroke_width=0).next_to(circ, UP, buff=-0.12)
            dol  = Text("$", font="Poppins", weight=BOLD, color=AMBER,
                        font_size=30).move_to(circ.get_center())
            return VGroup(circ, neck, dol)

        def repay_icon():
            h1 = Rectangle(width=0.58, height=0.19, color=BLUE,
                            fill_color=BLUE, fill_opacity=0.3,
                            stroke_width=2).rotate(PI / 6)
            h2 = Rectangle(width=0.58, height=0.19, color=BLUE,
                            fill_color=BLUE, fill_opacity=0.3,
                            stroke_width=2).rotate(-PI / 6)
            return VGroup(h1, h2).arrange(RIGHT, buff=-0.08)

        def scissors_icon():
            s1 = Line(LEFT * 0.38 + DOWN * 0.38, RIGHT * 0.38 + UP * 0.38,
                      color=RED, stroke_width=3)
            s2 = Line(LEFT * 0.38 + UP * 0.38, RIGHT * 0.38 + DOWN * 0.38,
                      color=RED, stroke_width=3)
            piv = Dot(ORIGIN, radius=0.09, color=RED)
            return VGroup(s1, s2, piv)

        def camera_icon():
            cb = Rectangle(width=0.78, height=0.52, color=GREY,
                           fill_color=GREY, fill_opacity=0.3, stroke_width=2)
            cl = Circle(radius=0.17, color=DARK, fill_color=DARK,
                        fill_opacity=0.6, stroke_width=2).move_to(cb.get_center())
            ct = Rectangle(width=0.26, height=0.17, color=GREY,
                           fill_color=GREY, fill_opacity=0.5,
                           stroke_width=0).next_to(cb, UP, buff=-0.07).shift(LEFT * 0.2)
            return VGroup(cb, cl, ct)

        icon_data = [
            (bail_out_icon(),  "BAIL OUT\nTHE BANKS"),
            (repay_icon(),     "REPAY\nDEPOSITORS"),
            (scissors_icon(),  "AUSTERITY\nPACKAGE"),
            (camera_icon(),    "SMILE FOR\nCAMERAS"),
        ]

        all_icons = VGroup()
        for ico, lbl_txt in icon_data:
            lt = Text(lbl_txt, font="Poppins", weight=BOLD,
                      color=DARK, font_size=22)
            grp = VGroup(ico, lt).arrange(DOWN, buff=0.28)
            all_icons.add(grp)
        all_icons.arrange(RIGHT, buff=1.3).move_to(DOWN * 0.3)

        for grp in all_icons:
            self.play(FadeIn(grp, shift=UP * 0.12), run_time=0.4)
            self.wait(2.0)

        self.wait(0.4)

        # Sweep everything off to the right
        self.play(
            all_icons.animate.shift(RIGHT * 18),
            FadeOut(imf_hdr, shift=RIGHT * 2),
            run_time=0.7, rate_func=rush_into,
        )

        # ── Banker Arrest ─────────────────────────────────────────
        arrest_hdr = Text("Iceland did this instead:", font="Poppins",
                          weight=BOLD, color=DARK, font_size=26
                          ).to_edge(UP, buff=V_PAD)
        self.play(FadeIn(arrest_hdr), run_time=0.3)

        bkr1 = make_banker()
        bkr2 = make_banker()
        bkr3 = make_banker()
        bankers = VGroup(bkr1, bkr2, bkr3).arrange(RIGHT, buff=1.1).move_to(DOWN * 0.1)

        self.play(
            LaggedStart(
                FadeIn(bkr1, shift=UP * 0.2),
                FadeIn(bkr2, shift=UP * 0.2),
                FadeIn(bkr3, shift=UP * 0.2),
                lag_ratio=0.28,
            ),
            run_time=0.8,
        )
        self.wait(0.4)

        # Bars drop from above
        bar_w = 0.2
        n_bars = 9
        bar_h = 4.5
        bars = VGroup(*[
            Rectangle(width=bar_w, height=bar_h,
                      color=DARK, fill_color=DARK, fill_opacity=1, stroke_width=0
                      ).move_to([-4.0 + i * 1.0, 0, 0])
            for i in range(n_bars)
        ])
        h_bar = Rectangle(width=9.5, height=0.28,
                          color=DARK, fill_color=DARK, fill_opacity=1, stroke_width=0
                          ).move_to(UP * (bar_h / 2 - 0.14))
        cage = VGroup(bars, h_bar)
        cage.set_z_index(5).shift(UP * 6)
        self.add(cage)
        self.play(cage.animate.shift(DOWN * 6), run_time=0.55, rate_func=rush_into)

        jailed = Text("JAILED.", font="Poppins", weight=BOLD,
                      color=RED, font_size=72).to_edge(DOWN, buff=V_PAD + 0.2)
        self.play(FadeIn(jailed, shift=UP * 0.1), run_time=0.35)
        self.wait(1.1)
        self.play(FadeOut(bankers), FadeOut(cage), FadeOut(jailed),
                  FadeOut(arrest_hdr), run_time=0.4)
        # Beat 5 ≈ 0.3+4*(0.4+2.0)+0.4+0.7+0.3+0.8+0.4+0.55+0.35+1.1+0.4 = 15.0s ✓
        # t ≈ 51s ✓

        # ============================================================
        # BEAT 6 — NEI + Recovery Charts vs France / Greece / UK
        # Duration: 11s  →  51s → 62s
        # ============================================================
        nei = Text("NEI.", font="Poppins", weight=BOLD, color=AMBER, font_size=180)
        nei_sub = Text("(Icelandic: No.)", font="Poppins", weight=LIGHT,
                       color=GREY, font_size=20).next_to(nei, DOWN, buff=0.3)

        self.play(GrowFromCenter(nei), run_time=0.5)
        self.play(FadeIn(nei_sub), run_time=0.3)
        self.wait(1.4)
        self.play(FadeOut(nei), FadeOut(nei_sub), run_time=0.35)

        # Recovery chart
        ct = Text("Recovery: Iceland vs the world",
                  font="Poppins", weight=BOLD, color=DARK, font_size=24
                  ).to_edge(UP, buff=V_PAD)

        ax = Axes(
            x_range=[2008, 2014, 1],
            y_range=[-13, 7, 3],
            x_length=10.0,
            y_length=4.2,
            axis_config={"color": DARK, "stroke_width": 1.5, "include_tip": False},
            tips=False,
        ).move_to(DOWN * 0.35)

        # Manual year labels along x-axis
        year_lbls = VGroup(*[
            Text(str(yr), font="Poppins", font_size=14, color=DARK
                 ).next_to(ax.c2p(yr, -13), DOWN, buff=0.18)
            for yr in [2008, 2009, 2010, 2011, 2012, 2013]
        ])
        y_lbl = Text("GDP growth %", font="Poppins", weight=LIGHT,
                     color=GREY, font_size=15
                     ).next_to(ax, LEFT, buff=0.1).rotate(PI / 2)
        zero = DashedLine(ax.c2p(2008, 0), ax.c2p(2014, 0),
                          color=L_GREY, stroke_width=1.2, dash_length=0.12)

        # GDP growth data (approximate actuals)
        #              2008   2009   2010   2011   2012   2013
        d_isl = [(-1.2, 0), (-6.6, 1), (-3.5, 2), (2.0, 3), (1.2, 4), (4.4, 5)]
        d_fra = [( 0.2, 0), (-2.9, 1), ( 2.0, 2), (2.1, 3), (0.2, 4), (0.6, 5)]
        d_grc = [(-0.3, 0), (-4.3, 1), (-5.5, 2), (-9.1, 3), (-7.3, 4), (-3.2, 5)]
        d_uk  = [(-0.5, 0), (-4.2, 1), ( 1.7, 2), (2.0, 3), (1.4, 4), (2.0, 5)]
        years = [2008, 2009, 2010, 2011, 2012, 2013]

        def chart_line(data, c, sw=3):
            pts = [ax.c2p(years[t], v) for v, t in data]
            return VGroup(*[
                Line(pts[i], pts[i + 1], color=c, stroke_width=sw)
                for i in range(len(pts) - 1)
            ])

        ln_grc = chart_line(d_grc, RED,  2.5)
        ln_fra = chart_line(d_fra, BLUE, 2.5)
        ln_uk  = chart_line(d_uk,  GREY, 2.5)
        ln_isl = chart_line(d_isl, GREEN, 4)

        def leg_item(c, txt):
            d = Dot(color=c, radius=0.1)
            t = Text(txt, font="Poppins", weight=LIGHT, color=DARK, font_size=16)
            return VGroup(d, t).arrange(RIGHT, buff=0.15)

        # Legend inside chart — top-right, clear of all data lines in that zone
        legend = VGroup(
            leg_item(GREEN, "Iceland"),
            leg_item(BLUE,  "France"),
            leg_item(RED,   "Greece"),
            leg_item(GREY,  "UK"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        legend.move_to(ax.c2p(2012.2, 5.8))

        self.play(FadeIn(ct), FadeIn(ax), FadeIn(year_lbls),
                  FadeIn(y_lbl), FadeIn(zero), run_time=0.4)
        self.play(Create(ln_grc), Create(ln_fra), Create(ln_uk), run_time=1.1)
        self.play(Create(ln_isl), run_time=0.7)
        self.play(FadeIn(legend), run_time=0.35)
        self.wait(1.5)
        self.play(
            FadeOut(ct), FadeOut(ax), FadeOut(year_lbls), FadeOut(y_lbl),
            FadeOut(zero), FadeOut(ln_isl), FadeOut(ln_fra),
            FadeOut(ln_grc), FadeOut(ln_uk), FadeOut(legend),
            run_time=0.4,
        )
        self.wait(0.3)
        # t ≈ 55s ✓

        # ============================================================
        # BEAT 7 — Time Rewind  ~10s
        # VO: "To understand how a tiny island builds that kind of
        #      backbone, you have to go back to the very beginning. 874 AD."
        # ============================================================
        MAP_PATH = ("C:/Users/parth.pandya/Projects/YouTube/Output/Iceland"
                    "/Needed Final Files/assets/maps/north_atlantic.png")
        map_bg = ImageMobject(MAP_PATH).set_height(fh)
        self.add(map_bg)

        backbone = Text(
            "To understand how a tiny island\nbuilds that kind of backbone...",
            font="Poppins", weight=LIGHT, font_size=32, color=WHITE,
            line_spacing=1.35,
        ).to_edge(UP, buff=V_PAD + 0.3)
        self.play(FadeIn(backbone, shift=DOWN * 0.1), run_time=0.7)
        self.wait(1.3)

        # Year counter — 2008 spins backward to 874
        year_lbl = Text("2008", font="Poppins", weight=BOLD,
                        color=RED, font_size=100).move_to(ORIGIN)
        self.play(FadeIn(year_lbl, scale=0.85), run_time=0.4)
        self.wait(0.3)

        milestones = [("1944", RED), ("1800", RED), ("1262", AMBER), ("874", AMBER)]
        for yr_str, col in milestones:
            new_lbl = Text(yr_str, font="Poppins", weight=BOLD,
                           color=col, font_size=100).move_to(ORIGIN)
            self.play(
                FadeOut(year_lbl, shift=UP * 0.4),
                FadeIn(new_lbl, shift=UP * 0.4),
                run_time=0.45,
            )
            year_lbl = new_lbl
            if yr_str != "874":
                self.wait(0.2)

        # 874 lands with a thud — scale pulse
        self.play(year_lbl.animate.scale(1.12), run_time=0.15, rate_func=rush_into)
        self.play(year_lbl.animate.scale(1 / 1.12), run_time=0.2)
        self.wait(3.0)

        self.play(FadeOut(backbone), FadeOut(year_lbl), run_time=0.5)
        self.remove(map_bg)

        # ============================================================
        # BEAT 8 — Not Vikings: Irish Monks + Ireland→Iceland map
        # ============================================================
        self.camera.background_color = WHITE_BG

        CHARS_PATH = ("C:/Users/parth.pandya/Projects/YouTube/Output/Iceland"
                      "/Needed Final Files/assets/characters/")
        viking_path = CHARS_PATH + "viking_settler.png"

        if os.path.exists(viking_path):
            viking = ImageMobject(viking_path).set_height(3.5).move_to(RIGHT * 2.2)
        else:
            v_body = Rectangle(width=0.8, height=1.6, fill_color="#3A3A5A",
                               fill_opacity=1, stroke_width=0)
            v_head = Circle(radius=0.3, fill_color="#C8956A", fill_opacity=1,
                            stroke_width=0).move_to(v_body.get_top() + UP * 0.32)
            h_pts  = [[-0.42, 0, 0], [-0.42, 0.35, 0], [0, 0.55, 0],
                      [0.42, 0.35, 0], [0.42, 0, 0]]
            v_helm = Polygon(*h_pts, fill_color="#5A5A7A", fill_opacity=1,
                             stroke_width=0).move_to(v_head.get_center() + UP * 0.25)
            viking = VGroup(v_body, v_head, v_helm).move_to(RIGHT * 2.2)

        q_text = Text("Iceland's first settlers?", font="Poppins", weight=BOLD,
                      font_size=42, color=DARK).move_to(LEFT * 1.8 + UP * 0.7)
        v_lbl  = Text("Norse Vikings", font="Poppins", weight=SEMIBOLD,
                      font_size=30, color=GREY).move_to(LEFT * 1.8 + DOWN * 0.1)

        self.play(GrowFromCenter(viking), FadeIn(q_text), run_time=0.8)
        self.play(FadeIn(v_lbl), run_time=0.4)
        self.wait(0.9)

        # Big red X — wrong answer
        x1 = Line(LEFT * 5.0 + DOWN * 2.2, RIGHT * 5.0 + UP * 2.2,
                  color=RED, stroke_width=12).set_z_index(10)
        x2 = Line(LEFT * 5.0 + UP * 2.2, RIGHT * 5.0 + DOWN * 2.2,
                  color=RED, stroke_width=12).set_z_index(10)
        self.play(Create(x1), Create(x2), run_time=0.4)
        self.wait(0.4)
        self.play(FadeOut(viking), FadeOut(q_text), FadeOut(v_lbl),
                  FadeOut(x1), FadeOut(x2), run_time=0.4)

        # "Not Vikings. Irish Monks." text slam
        not_v = Text("Not Vikings.", font="Poppins", weight=BOLD,
                     font_size=68, color=RED).move_to(UP * 1.1)
        monks = Text("Irish Monks.", font="Poppins", weight=BOLD,
                     font_size=68, color=AMBER).move_to(UP * 0.05)
        first = Text("Iceland's first settlers.", font="Poppins", weight=LIGHT,
                     font_size=30, color=GREY).move_to(DOWN * 1.1)

        self.play(GrowFromCenter(not_v), run_time=0.4)
        self.play(GrowFromCenter(monks), run_time=0.4)
        self.play(FadeIn(first), run_time=0.35)
        self.wait(2.2)
        self.play(FadeOut(not_v), FadeOut(monks), FadeOut(first), run_time=0.4)

        # ── Ireland → Iceland map ─────────────────────────────────
        # Use clean map (ICELAND text painted out of PNG)
        CLEAN_MAP = ("C:/Users/parth.pandya/Projects/YouTube/Output/Iceland"
                     "/Needed Final Files/assets/maps/north_atlantic_clean.png")
        map_bg3 = ImageMobject(CLEAN_MAP).set_height(fh)
        self.add(map_bg3)

        ireland_pos = [3.0, -2.1, 0]
        iceland_pos = [-0.4,  0.5, 0]

        # Papar icon — tiny monk geo inline (BROWN not in scope, define inline)
        _brown = "#5A3A1A"
        p_head = Circle(radius=0.20, fill_color="#C8956A", fill_opacity=1,
                        stroke_color=DARK, stroke_width=1.0)
        p_robe = Triangle(fill_color=_brown, fill_opacity=1,
                          stroke_color=DARK, stroke_width=0.8).scale(0.52)
        p_robe.next_to(p_head, DOWN, buff=0.02)
        p_bald = Circle(radius=0.08, fill_color="#8B6A4A", fill_opacity=0.75,
                        stroke_width=0).move_to(p_head.get_center() + UP * 0.06)
        papar_icon = VGroup(p_robe, p_head, p_bald)
        papar_icon.scale(0.9).move_to([-0.9, 1.0, 0])
        papar_lbl = Text("The Papar", font="Poppins", weight=SEMIBOLD,
                         font_size=15, color=WHITE).next_to(papar_icon, DOWN, buff=0.06)

        ire_dot = Dot(ireland_pos, radius=0.16, color=AMBER, fill_opacity=1)
        ice_dot = Dot(iceland_pos, radius=0.18, color=GREEN,  fill_opacity=1)
        ire_lbl = Text("Ireland", font="Poppins", weight=SEMIBOLD,
                       font_size=22, color=WHITE).next_to(ire_dot, DOWN, buff=0.14)
        ice_lbl = Text("Iceland", font="Poppins", weight=SEMIBOLD,
                       font_size=22, color=WHITE).next_to(ice_dot, UP,   buff=0.14)

        route = CubicBezier(
            ireland_pos,
            [2.2,  0.8, 0],
            [0.8,  1.3, 0],
            iceland_pos,
        )
        route.set_stroke(color=AMBER, width=3.5, opacity=0.85)

        # Tiny monk boat (inline)
        b_hull = Polygon([-0.3, -0.08, 0], [-0.3, 0.02, 0],
                         [ 0.3,  0.02, 0], [ 0.3, -0.08, 0],
                         fill_color="#3A2A1A", fill_opacity=1, stroke_width=0)
        b_mast = Line([0, 0.02, 0], [0, 0.35, 0],
                      stroke_color=DARK, stroke_width=2.5)
        b_sail = Triangle(fill_color="#D4B88A", fill_opacity=0.85,
                          stroke_width=0).scale(0.13).move_to([0, 0.2, 0])
        monk_boat = VGroup(b_hull, b_mast, b_sail)
        monk_boat.move_to(ireland_pos)

        date_lbl   = Text("Year 800 AD", font="Poppins", weight=SEMIBOLD,
                          font_size=22, color=AMBER).to_corner(UR, buff=V_PAD)
        settle_lbl = Text("Iceland's first known settlers", font="Poppins",
                          weight=LIGHT, font_size=22, color=WHITE
                          ).to_edge(DOWN, buff=V_PAD + 0.1)

        # Show Papar on Iceland + Ireland dot simultaneously
        self.play(
            FadeIn(papar_icon), FadeIn(papar_lbl),
            FadeIn(ire_dot), FadeIn(ire_lbl),
            run_time=0.4,
        )
        self.wait(0.9)   # hold: Papar already living quietly in Iceland

        # Boat departs Ireland — faster route + sail
        self.play(Create(route), run_time=1.0)
        self.play(MoveAlongPath(monk_boat, route), run_time=1.5, rate_func=linear)

        # Arrival: Papar fades, "Iceland" label appears — cover stays to keep map text hidden
        # VO sync: "They found Iceland"
        self.play(
            FadeOut(papar_icon), FadeOut(papar_lbl),
            GrowFromCenter(ice_dot), FadeIn(ice_lbl),
            FadeIn(date_lbl), FadeIn(settle_lbl),
            run_time=0.5,
        )
        self.wait(1.7)
