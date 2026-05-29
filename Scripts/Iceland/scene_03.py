"""Iceland EP1 - Scene 03: IcelandEP1_S03_TheNumbers
Three brutal statistics, one at a time.
  Stat 1: Bank assets = 11x GDP  (bar chart)
  Stat 2: Currency halved        (ISK/USD nosedive line)
  Stat 3: Stock market -90%      (crash chart)
White background, Poppins Bold, red impact numbers.
Render: manim -qh scene_03.py IcelandEP1_S03_TheNumbers
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from helpers import ICELAND_RED

STAT_RED  = "#CC0000"
DARK_TXT  = "#1A1A1A"
GREY_LINE = "#CCCCCC"
BAR_BLUE  = "#4A6FA5"
BAR_RED   = "#CC0000"


# ── helpers ────────────────────────────────────────────────────────────────

def counter_label(value: str, sub: str, color=DARK_TXT) -> VGroup:
    """Large bold number + small subtitle below it."""
    num = Text(value, font="Poppins", weight=BOLD,
               font_size=100, color=color)
    lbl = Text(sub,   font="Poppins", weight=BOLD,
               font_size=28,  color=GREY_TXT if color == DARK_TXT else color)
    lbl.next_to(num, DOWN, buff=0.18)
    return VGroup(num, lbl)


GREY_TXT = "#888888"


def crash_line(ox, oy, points) -> VMobject:
    """Hand-crafted polyline from a list of (dx, dy) offsets."""
    pts = [[ox, oy, 0]]
    for dx, dy in points:
        pts.append([ox + dx, oy + dy, 0])
    line = VMobject(color=BAR_RED, stroke_width=4)
    line.set_points_as_corners(pts)
    return line


# ── scene ──────────────────────────────────────────────────────────────────

class IcelandEP1_S03_TheNumbers(Scene):
    VD = 13.5

    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Text.set_default(font="Poppins")

        # ══════════════════════════════════════════════════════
        # STAT 1 — Bank assets = 11x Iceland's GDP
        # ══════════════════════════════════════════════════════
        # Two bars: GDP (height 1 unit) vs Bank Assets (height 11 units)
        BAR_W   = 1.2
        UNIT    = 0.38          # each GDP unit in Manim
        gdp_h   = UNIT * 1
        bank_h  = UNIT * 11

        gdp_bar  = Rectangle(width=BAR_W, height=gdp_h,
                             fill_color=BAR_BLUE, fill_opacity=1, stroke_width=0)
        bank_bar = Rectangle(width=BAR_W, height=bank_h,
                             fill_color=BAR_RED,  fill_opacity=1, stroke_width=0)

        # Position: GDP bar left, bank bar right, bases aligned
        baseline_y = -2.8
        gdp_bar.move_to( [-2.0, baseline_y + gdp_h  / 2, 0])
        bank_bar.move_to([ 1.0, baseline_y + bank_h / 2, 0])

        gdp_lbl  = Text("Iceland's GDP",   font="Poppins", font_size=22, color=DARK_TXT)
        bank_lbl = Text("Bank Assets",     font="Poppins", font_size=22, color=DARK_TXT)
        gdp_lbl.next_to(gdp_bar,  DOWN, buff=0.18)
        bank_lbl.next_to(bank_bar, DOWN, buff=0.18)

        baseline = Line([-3.8, baseline_y, 0], [3.8, baseline_y, 0],
                        color=DARK_TXT, stroke_width=2)

        # "11x" label slams above bank bar
        x11_lbl = Text("11×", font="Poppins", weight=BOLD,
                        font_size=90, color=BAR_RED)
        x11_lbl.next_to(bank_bar, UP, buff=0.25)

        self.play(Create(baseline), run_time=0.3)
        self.play(
            LaggedStart(
                GrowFromEdge(gdp_bar,  DOWN),
                GrowFromEdge(bank_bar, DOWN),
                lag_ratio=0.4
            ),
            run_time=1.4
        )
        self.play(
            FadeIn(gdp_lbl), FadeIn(bank_lbl), run_time=0.4
        )
        self.play(
            FadeIn(x11_lbl, scale=1.6), run_time=0.5, rate_func=rush_into
        )
        self.wait(0.8)

        # ══════════════════════════════════════════════════════
        # Wipe out stat 1 — slide everything off left
        # ══════════════════════════════════════════════════════
        stat1 = Group(baseline, gdp_bar, bank_bar, gdp_lbl, bank_lbl, x11_lbl)
        self.play(stat1.animate.shift(LEFT * 16), run_time=0.4, rate_func=rush_into)
        self.remove(stat1)

        # ══════════════════════════════════════════════════════
        # STAT 2 — ISK/USD currency halved
        # ══════════════════════════════════════════════════════
        # Simple axes
        ax2 = Axes(
            x_range=[0, 6, 1], y_range=[0, 1.2, 0.3],
            x_length=9, y_length=4,
            axis_config={"color": "#AAAAAA", "stroke_width": 1.5},
            tips=False
        ).move_to([0, -0.2, 0])

        x_label = Text("2008", font="Poppins", font_size=20, color="#999999")
        x_label.next_to(ax2.x_axis.n2p(1), DOWN, buff=0.25)
        x_label2 = Text("2009", font="Poppins", font_size=20, color="#999999")
        x_label2.next_to(ax2.x_axis.n2p(4), DOWN, buff=0.25)

        y_top   = ax2.c2p(0, 1.0)
        y_half  = ax2.c2p(0, 0.5)

        # Dashed line at y=1.0 (starting value) and y=0.5 (halved)
        ref_line  = DashedLine([ax2.c2p(0,1.0)[0]-0.1, y_top[1], 0],
                               [ax2.c2p(6,1.0)[0],     y_top[1], 0],
                               color="#BBBBBB", stroke_width=1.5, dash_length=0.12)
        half_line = DashedLine([ax2.c2p(0,0.5)[0]-0.1, y_half[1], 0],
                               [ax2.c2p(6,0.5)[0],     y_half[1], 0],
                               color=BAR_RED, stroke_width=1.5, dash_length=0.12)

        # Currency crash curve: climbs slightly, then collapses to 0.5
        isk_pts = [
            (0.0,  1.00), (0.5,  1.03), (1.0,  1.01),  # stable pre-crisis
            (1.4,  0.98), (1.7,  0.88), (2.0,  0.72),  # begins sliding
            (2.3,  0.61), (2.6,  0.52), (3.0,  0.49),  # collapse
            (3.5,  0.50), (4.5,  0.51), (6.0,  0.50),  # new floor
        ]
        isk_path = VMobject(color=BAR_RED, stroke_width=4)
        isk_path.set_points_smoothly(
            [ax2.c2p(x, y) for x, y in isk_pts]
        )

        title2 = Text("ISK / USD exchange rate", font="Poppins",
                      font_size=24, color=DARK_TXT)
        title2.move_to([0, 3.1, 0])

        self.play(Create(ax2), FadeIn(title2), run_time=0.4)
        self.play(Create(ref_line), run_time=0.2)
        self.play(FadeIn(x_label), FadeIn(x_label2), run_time=0.2)
        self.play(Create(isk_path), run_time=1.6, rate_func=linear)
        self.play(Create(half_line), run_time=0.3)

        # "-50%" slams in
        pct2 = Text("-50%", font="Poppins", weight=BOLD,
                    font_size=90, color=BAR_RED)
        pct2.move_to([2.8, 1.2, 0])
        self.play(FadeIn(pct2, scale=1.6), run_time=0.4, rate_func=rush_into)
        self.wait(0.7)

        stat2 = Group(ax2, title2, ref_line, half_line, isk_path, x_label, x_label2, pct2)
        self.play(stat2.animate.shift(LEFT * 16), run_time=0.4, rate_func=rush_into)
        self.remove(stat2)

        # ══════════════════════════════════════════════════════
        # STAT 3 — Stock market -90%
        # ══════════════════════════════════════════════════════
        ax3 = Axes(
            x_range=[0, 8, 1], y_range=[0, 1.2, 0.3],
            x_length=9, y_length=4,
            axis_config={"color": "#AAAAAA", "stroke_width": 1.5},
            tips=False
        ).move_to([0, -0.2, 0])

        title3 = Text("Iceland Stock Exchange (OMX Iceland 15)", font="Poppins",
                      font_size=22, color=DARK_TXT)
        title3.move_to([0, 3.1, 0])

        # Stock crash: peak near start, then obliterated
        stock_pts = [
            (0.0, 1.00), (0.3, 1.05), (0.7, 1.08),   # peak
            (1.0, 1.05), (1.4, 0.95), (1.8, 0.80),   # slide
            (2.2, 0.60), (2.6, 0.40), (3.0, 0.25),   # crash
            (3.5, 0.15), (4.0, 0.10), (5.0, 0.10),   # floor
            (6.0, 0.10), (8.0, 0.10),
        ]
        stock_path = VMobject(color=BAR_RED, stroke_width=4)
        stock_path.set_points_smoothly(
            [ax3.c2p(x, y) for x, y in stock_pts]
        )

        # -90% dashed reference line
        floor_line = DashedLine(
            [ax3.c2p(0, 0.10)[0]-0.1, ax3.c2p(0, 0.10)[1], 0],
            [ax3.c2p(8, 0.10)[0],     ax3.c2p(0, 0.10)[1], 0],
            color=BAR_RED, stroke_width=1.5, dash_length=0.12
        )

        self.play(Create(ax3), FadeIn(title3), run_time=0.4)
        self.play(Create(stock_path), run_time=1.8, rate_func=linear)
        self.play(Create(floor_line), run_time=0.25)

        pct3 = Text("-90%", font="Poppins", weight=BOLD,
                    font_size=110, color=BAR_RED)
        pct3.move_to([2.6, 1.0, 0])
        self.play(FadeIn(pct3, scale=1.8), run_time=0.4, rate_func=rush_into)
        self.wait(1.0)

        # ── hold to fill VO ─────────────────────────────────
        T = 11.5
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
