"""Iceland EP1 - Scene 07: IcelandEP1_S07_Recovered
Payoff scene — "And yet, recovered faster than anyone."
"And yet." slams in huge → recovery chart: everyone else crawls, Iceland rockets up.
Render: manim -qh scene_07.py IcelandEP1_S07_Recovered
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))

DARK_BG  = "#0D1B2A"
GREEN    = "#00CC66"
STAT_RED = "#CC0000"
GOLD     = "#FFD700"

# Country line colours
C_GREECE      = "#C0392B"   # deep red
C_IRELAND     = "#27AE60"   # dark green
C_BRITAIN     = "#2980B9"   # steel blue
C_FRANCE      = "#8E44AD"   # purple
C_NETHERLANDS = "#E67E22"   # orange
C_GERMANY     = "#95A5A6"   # grey


class IcelandEP1_S07_Recovered(Scene):
    VD = 4.0   # 6 words / 145wpm * 60 ≈ 2.5s + dramatic delivery = ~4.0s

    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(font="Poppins")

        # ══════════════════════════════════════════════════════
        # BEAT 1 — "And yet." slams in full screen
        # ══════════════════════════════════════════════════════
        and_yet = Text("And yet.", font="Poppins", weight=BOLD,
                       font_size=108, color="#1A1A1A")
        and_yet.move_to(ORIGIN)

        self.play(FadeIn(and_yet, scale=1.8), run_time=0.3, rate_func=rush_into)
        self.wait(0.45)

        # Shrink and push to top-left — stay within safe zone (y ≤ 3.2, x ≥ -5.7)
        self.play(
            and_yet.animate.scale(0.38).move_to([-4.2, 2.8, 0]).set_opacity(0.4),
            run_time=0.35,
        )

        # ══════════════════════════════════════════════════════
        # BEAT 2 — Recovery chart: country lines crawl, Iceland rockets
        # Safe zone: x ∈ [-5.7, 5.7], y ∈ [-3.2, 3.2]
        # ══════════════════════════════════════════════════════
        ax = Axes(
            x_range=[0, 6, 1], y_range=[-1.6, 2.0, 0.5],
            x_length=8.0, y_length=4.2,
            axis_config={"color": "#333333", "stroke_width": 1.5},
            tips=False,
        ).move_to([0, 0.2, 0])

        # Dashed baseline — pre-crisis level
        baseline = DashedLine(
            [ax.c2p(0, 0)[0], ax.c2p(0, 0)[1], 0],
            [ax.c2p(6, 0)[0], ax.c2p(0, 0)[1], 0],
            color="#555555", stroke_width=1.5, dash_length=0.18,
        )
        base_lbl = Text("Pre-crisis level", font="Poppins", font_size=13, color="#555555")
        base_lbl.next_to(ax.c2p(0, 0), LEFT, buff=0.1)

        # Year labels — below bottom of chart, within safe zone
        for yr, x in [("2008", 0), ("2010", 2), ("2012", 4), ("2014", 6)]:
            self.add(Text(yr, font="Poppins", font_size=14, color="#666666")
                     .next_to(ax.c2p(x, -1.6), DOWN, buff=0.12))

        # Country recovery paths — end-y values spread for legible labels
        country_data = [
            # (name, color, pts, end_y_nudge)
            ("Greece",      C_GREECE,
             [(0,0),(0.5,-0.2),(1,-0.5),(1.8,-0.9),(2.5,-1.1),(3.5,-1.25),(5,-1.38),(6,-1.4)],
             0),
            ("Ireland",     C_IRELAND,
             [(0,0),(0.5,-0.3),(1,-0.65),(1.8,-0.6),(2.5,-0.5),(3.5,-0.45),(5,-0.4),(6,-0.38)],
             0),
            ("Britain",     C_BRITAIN,
             [(0,0),(0.5,-0.2),(1,-0.32),(2,-0.28),(3,-0.22),(4,-0.18),(5,-0.14),(6,-0.12)],
             0),
            ("France",      C_FRANCE,
             [(0,0),(0.5,-0.15),(1,-0.22),(2,-0.18),(3,-0.12),(4,-0.06),(5,-0.03),(6, 0.02)],
             0),
            ("Netherlands", C_NETHERLANDS,
             [(0,0),(0.5,-0.18),(1,-0.28),(2,-0.24),(3,-0.18),(4,-0.12),(5,-0.08),(6,-0.05)],
             0),
            ("Germany",     C_GERMANY,
             [(0,0),(0.5,-0.18),(1,-0.25),(1.8,-0.1),(2.5, 0.05),(3.5, 0.12),(5, 0.18),(6, 0.22)],
             0),
        ]

        others_paths = []
        others_lbls  = []
        for name, color, pts, _ in country_data:
            path = VMobject(color=color, stroke_width=2.8)
            path.set_points_smoothly([ax.c2p(x, y) for x, y in pts])
            lbl = Text(name, font="Poppins", font_size=14, color=color)
            lbl.next_to(ax.c2p(pts[-1][0], pts[-1][1]), RIGHT, buff=0.1)
            others_paths.append(path)
            others_lbls.append(lbl)

        # Iceland — crashes then rockets above everyone
        iceland_pts = [
            (0, 0.0), (0.5,-0.42), (1.0,-0.46),
            (1.5, 0.08), (2.0, 0.5), (2.8, 0.95),
            (3.8, 1.4), (5.0, 1.68), (6.0, 1.82),
        ]
        iceland_path = VMobject(color=GREEN, stroke_width=5.5)
        iceland_path.set_points_smoothly([ax.c2p(x, y) for x, y in iceland_pts])
        iceland_lbl = Text("Iceland", font="Poppins", weight=BOLD,
                           font_size=20, color=GREEN)
        iceland_lbl.next_to(ax.c2p(6.0, 1.82), RIGHT, buff=0.1)

        # Draw axes + baseline
        self.play(Create(ax), Create(baseline), FadeIn(base_lbl), run_time=0.3)

        # All country lines draw simultaneously
        self.play(
            *[Create(p, rate_func=linear) for p in others_paths],
            run_time=0.75,
        )
        self.play(*[FadeIn(l) for l in others_lbls], run_time=0.2)

        # Iceland rockets up
        self.play(Create(iceland_path), run_time=0.7, rate_func=linear)
        self.play(FadeIn(iceland_lbl, scale=1.3), run_time=0.2, rate_func=rush_into)

        # Bottom tagline
        tagline = Text("Recovered faster than anyone.", font="Poppins",
                       weight=BOLD, font_size=38, color=GREEN)
        tagline.move_to([0, -2.9, 0])
        self.play(FadeIn(tagline, shift=UP * 0.2), run_time=0.28)

        T = 0.3 + 0.45 + 0.35 + 0.3 + 0.75 + 0.2 + 0.7 + 0.2 + 0.28
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
