"""Iceland EP1 - Scene 03: IcelandEP1_S03_TheNumbers
Three brutal statistics.
  Stat 1: Bank assets = 11x GDP  (pie chart — tiny blue GDP slice, massive blinking red bank)
  Stats 2+3: Currency halved + Stock market -90% (side-by-side, simultaneous)
White background, Poppins Bold, red impact numbers.
Render: manim -qh scene_03.py IcelandEP1_S03_TheNumbers
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))

STAT_RED = "#CC0000"
DARK_TXT = "#1A1A1A"
GREY_TXT = "#888888"
BAR_BLUE = "#4A6FA5"
BAR_RED  = "#CC0000"
PIE_R    = 2.3


class IcelandEP1_S03_TheNumbers(Scene):
    VD = 13.5

    # VO split (29 words total at 145 wpm)
    VO_PART1 = 16 / 145 * 60   # 6.62s — "...11x the size of entire country's GDP"
    VO_PART2 = 13 / 145 * 60   # 5.38s — "The fall devalued...stock market shed over 90%"

    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Text.set_default(font="Poppins")

        # ══════════════════════════════════════════════════════
        # STAT 1 — Pie chart: GDP (1x, blue) vs Bank Assets (11x, red + blink)
        # ══════════════════════════════════════════════════════
        gdp_angle  = (1 / 12) * TAU   # ~30°  — tiny blue slice at top
        bank_angle = (11 / 12) * TAU  # ~330° — massive red sector

        gdp_sector = AnnularSector(
            inner_radius=0, outer_radius=PIE_R,
            angle=gdp_angle, start_angle=PI / 2,
            color=BAR_BLUE, fill_opacity=1,
            stroke_color=WHITE, stroke_width=3,
        )
        bank_sector = AnnularSector(
            inner_radius=0, outer_radius=PIE_R,
            angle=bank_angle, start_angle=PI / 2 + gdp_angle,
            color=BAR_RED, fill_opacity=1,
            stroke_color=WHITE, stroke_width=3,
        )
        pie = VGroup(gdp_sector, bank_sector).move_to(ORIGIN)

        # GDP connector + label (tiny slice, upper-left direction ~105°)
        gdp_mid_a = PI / 2 + gdp_angle / 2
        gdp_outer = PIE_R * np.array([np.cos(gdp_mid_a), np.sin(gdp_mid_a), 0])
        gdp_anchor = np.array([-1.2, 3.6, 0])
        gdp_conn  = Line(gdp_outer * 1.05, gdp_anchor + np.array([0, -0.45, 0]),
                         color=BAR_BLUE, stroke_width=1.8)
        gdp_lbl   = VGroup(
            Text("Iceland's GDP", font="Poppins", font_size=20, color=BAR_BLUE),
            Text("1×",            font="Poppins", weight=BOLD, font_size=32, color=BAR_BLUE),
        ).arrange(DOWN, buff=0.1).move_to(gdp_anchor)

        # Bank label — right of screen (the sector covers the bottom-right arc)
        bank_lbl = VGroup(
            Text("Bank Assets", font="Poppins", font_size=24, color=BAR_RED),
            Text("11×",         font="Poppins", weight=BOLD, font_size=72, color=BAR_RED),
        ).arrange(DOWN, buff=0.12).move_to([4.5, -0.4, 0])

        self.play(Create(gdp_sector), Create(bank_sector), run_time=1.0)
        self.play(
            Create(gdp_conn), FadeIn(gdp_lbl),
            FadeIn(bank_lbl),
            run_time=0.5,
        )

        # Blink bank sector 3 times to emphasise the 11x scale
        for _ in range(3):
            self.play(bank_sector.animate.set_fill(opacity=0.2), run_time=0.22)
            self.play(bank_sector.animate.set_fill(opacity=1.0),  run_time=0.22)

        # Pad remaining time so pie section fills VO part 1 (6.62s)
        T1 = 1.0 + 0.5 + 3 * (0.22 + 0.22) + 0.45   # ~4.27s of animations
        self.wait(max(self.VO_PART1 - T1, 0))

        self.play(FadeOut(Group(pie, gdp_conn, gdp_lbl, bank_lbl)), run_time=0.45)

        # ══════════════════════════════════════════════════════
        # STATS 2 + 3 — Side-by-side, drawn simultaneously
        #   Left:  ISK/USD currency halved
        #   Right: OMX Iceland 15 stock market -90%
        # ══════════════════════════════════════════════════════

        divider = DashedLine([0, -3.4, 0], [0, 3.4, 0],
                             color=GREY_TXT, stroke_width=1.5, dash_length=0.2)

        # ── LEFT: ISK / USD ────────────────────────────────
        ax2 = Axes(
            x_range=[0, 6, 1], y_range=[0, 1.2, 0.3],
            x_length=5.6, y_length=3.4,
            axis_config={"color": "#AAAAAA", "stroke_width": 1.5},
            tips=False,
        ).move_to([-3.2, -0.5, 0])

        title2 = Text("ISK / USD exchange rate", font="Poppins",
                      font_size=21, color=DARK_TXT).next_to(ax2, UP, buff=0.2)

        isk_pts = [
            (0.0, 1.00), (0.5, 1.03), (1.0, 1.01),
            (1.4, 0.98), (1.7, 0.88), (2.0, 0.72),
            (2.3, 0.61), (2.6, 0.52), (3.0, 0.49),
            (3.5, 0.50), (4.5, 0.51), (6.0, 0.50),
        ]
        isk_path = VMobject(color=BAR_RED, stroke_width=4)
        isk_path.set_points_smoothly([ax2.c2p(x, y) for x, y in isk_pts])

        half_line = DashedLine(
            [ax2.c2p(0, 0.5)[0] - 0.15, ax2.c2p(0, 0.5)[1], 0],
            [ax2.c2p(6, 0.5)[0],          ax2.c2p(0, 0.5)[1], 0],
            color=BAR_RED, stroke_width=1.5, dash_length=0.12,
        )
        pct2 = Text("-50%", font="Poppins", weight=BOLD, font_size=54, color=BAR_RED)
        pct2.move_to(ax2.c2p(4.2, 0.92))

        # ── RIGHT: OMX Iceland 15 ──────────────────────────
        ax3 = Axes(
            x_range=[0, 8, 1], y_range=[0, 1.2, 0.3],
            x_length=5.6, y_length=3.4,
            axis_config={"color": "#AAAAAA", "stroke_width": 1.5},
            tips=False,
        ).move_to([3.2, -0.5, 0])

        title3 = Text("OMX Iceland 15 (Stock Exchange)", font="Poppins",
                      font_size=21, color=DARK_TXT).next_to(ax3, UP, buff=0.2)

        stock_pts = [
            (0.0, 1.00), (0.3, 1.05), (0.7, 1.08),
            (1.0, 1.05), (1.4, 0.95), (1.8, 0.80),
            (2.2, 0.60), (2.6, 0.40), (3.0, 0.25),
            (3.5, 0.15), (4.0, 0.10), (5.0, 0.10),
            (6.0, 0.10), (8.0, 0.10),
        ]
        stock_path = VMobject(color=BAR_RED, stroke_width=4)
        stock_path.set_points_smoothly([ax3.c2p(x, y) for x, y in stock_pts])

        floor_line = DashedLine(
            [ax3.c2p(0, 0.10)[0] - 0.15, ax3.c2p(0, 0.10)[1], 0],
            [ax3.c2p(8, 0.10)[0],          ax3.c2p(0, 0.10)[1], 0],
            color=BAR_RED, stroke_width=1.5, dash_length=0.12,
        )
        pct3 = Text("-90%", font="Poppins", weight=BOLD, font_size=54, color=BAR_RED)
        pct3.move_to(ax3.c2p(6.0, 0.92))

        # Both axes appear together
        self.play(
            Create(ax2), FadeIn(title2),
            Create(ax3), FadeIn(title3),
            Create(divider),
            run_time=0.55,
        )
        # Both crash lines draw simultaneously
        self.play(
            Create(isk_path),
            Create(stock_path),
            run_time=2.2, rate_func=linear,
        )
        # Both dashed reference lines simultaneously
        self.play(
            Create(half_line),
            Create(floor_line),
            run_time=0.35,
        )
        # Both impact numbers slam in simultaneously
        self.play(
            FadeIn(pct2, scale=1.6),
            FadeIn(pct3, scale=1.6),
            run_time=0.45, rate_func=rush_into,
        )

        # Pad remaining time so charts section fills VO part 2 (5.38s), then 1.5s visual hold
        T2 = 0.55 + 2.2 + 0.35 + 0.45   # ~3.55s of animations
        self.wait(max(self.VO_PART2 - T2, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
