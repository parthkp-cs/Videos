"""Iceland EP1 - Scene 02: IcelandEP1_S02_BanksCollapse
North Atlantic map → crash graph over US → spreads → zoom to Iceland →
wipe white → 3 Icelandic banks appear → shake → red X → topple.
Render: manim -qh scene_02.py IcelandEP1_S02_BanksCollapse
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_map, ICELAND_RED

# Positions on north_atlantic_wide.png (extent -100 to 30 lon, 20 to 75 lat)
# Frame 14.22 × 8.0 manim units.  lon→x: (-100..30) maps to (-7.11..7.11)
# lat→y: (20..75) maps to (-4.0..4.0)
# x = (lon - (-100)) / 130 * 14.22 - 7.11
# y = (lat - 20) / 55 * 8.0 - 4.0
# New York:  lon=-74, lat=41  → x≈2.31-7.11=-4.80? let me recalc
# x = (-74+100)/130*14.22 - 7.11 = 26/130*14.22-7.11 = 2.84-7.11 = -4.27
# y = (41-20)/55*8.0-4.0 = 21/55*8-4 = 3.05-4 = -0.95
# London: lon=0, lat=51.5 → x=(100/130)*14.22-7.11=10.94-7.11=3.83, y=(31.5/55)*8-4=4.58-4=0.58
# Iceland: lon=-18, lat=65 → x=(82/130)*14.22-7.11=8.98-7.11=1.87, y=(45/55)*8-4=6.55-4=2.55
US_DOT      = np.array([-4.3, -0.9, 0])   # New York area
EUROPE_DOT  = np.array([ 3.8,  0.6, 0])   # London/western Europe
ICELAND_DOT = np.array([ 1.9,  2.5, 0])   # Iceland

BANK_RED  = "#CC0000"
BANK_GREY = "#333333"


def make_crash_graph(origin: np.ndarray) -> VMobject:
    """Hand-crafted stock crash path."""
    ox, oy = origin[0], origin[1]
    pts = [
        [ox,      oy     ],
        [ox+0.3,  oy-0.1 ],
        [ox+0.55, oy+0.05],   # dead-cat
        [ox+0.8,  oy-0.2 ],
        [ox+1.0,  oy+0.02],   # last gasp
        [ox+1.25, oy-0.4 ],
        [ox+1.5,  oy-0.9 ],
        [ox+1.7,  oy-1.5 ],
    ]
    line = VMobject(color=BANK_RED, stroke_width=3.5)
    line.set_points_as_corners([[x, y, 0] for x, y in pts])
    return line


def make_bank_building(fill="#444444") -> VGroup:
    """Greek-revival bank silhouette."""
    steps = VGroup(
        Rectangle(width=2.9, height=0.18, fill_color=fill, fill_opacity=1, stroke_width=0).shift(DOWN*1.46),
        Rectangle(width=2.6, height=0.18, fill_color=fill, fill_opacity=1, stroke_width=0).shift(DOWN*1.28),
    )
    body = Rectangle(width=2.2, height=1.55, fill_color=fill, fill_opacity=1, stroke_width=0).shift(DOWN*0.3)
    cols = VGroup(*[
        Rectangle(width=0.16, height=1.35, fill_color="#F0F0F0",
                  fill_opacity=1, stroke_width=0).move_to([-0.88+i*0.35, -0.3, 0])
        for i in range(6)
    ])
    roof = Triangle(fill_color=fill, fill_opacity=1, stroke_width=0)
    roof.set_width(2.4).set_height(0.52).shift(UP*0.60)
    return VGroup(steps, body, cols, roof)


def make_red_x(size=1.4) -> VGroup:
    d = size / 2
    line1 = Line([-d, -d, 0], [d,  d, 0], color=BANK_RED, stroke_width=12)
    line2 = Line([-d,  d, 0], [d, -d, 0], color=BANK_RED, stroke_width=12)
    return VGroup(line1, line2)


class IcelandEP1_S02_BanksCollapse(Scene):
    VD = 18.5

    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Text.set_default(font="Poppins")

        # ══════════════════════════════════════════════════════
        # PHASE 1 — North Atlantic map, crash graph over US
        # ══════════════════════════════════════════════════════
        na_map = load_map("north_atlantic_wide")
        self.play(FadeIn(na_map), run_time=0.7)

        # Crash graph draws over US region
        graph = make_crash_graph(US_DOT)
        self.play(Create(graph), run_time=2.2, rate_func=linear)

        # ══════════════════════════════════════════════════════
        # PHASE 2 — Crash spreads: US → Europe → Iceland
        # ══════════════════════════════════════════════════════
        us_dot  = Dot(US_DOT,      radius=0.14, color=BANK_RED)
        eu_dot  = Dot(EUROPE_DOT,  radius=0.14, color=BANK_RED)
        ic_dot  = Dot(ICELAND_DOT, radius=0.14, color=BANK_RED)

        self.play(FadeIn(us_dot), run_time=0.3)

        # Arc from US to Europe
        arc_us_eu = ArcBetweenPoints(US_DOT, EUROPE_DOT,
                                     angle=-TAU/6, color=BANK_RED,
                                     stroke_width=2.5)
        self.play(Create(arc_us_eu), FadeIn(eu_dot), run_time=1.0)

        # Arc from US to Iceland
        arc_us_ic = ArcBetweenPoints(US_DOT, ICELAND_DOT,
                                     angle=TAU/8, color=BANK_RED,
                                     stroke_width=2.5)
        self.play(Create(arc_us_ic), FadeIn(ic_dot), run_time=0.8)

        # Pulse ring on Iceland
        ring = Circle(radius=0.45, color=BANK_RED, stroke_width=3)
        ring.move_to(ICELAND_DOT)
        self.play(Create(ring), run_time=0.5)
        self.play(ring.animate.scale(1.8).set_stroke(opacity=0),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════
        # PHASE 3 — Zoom into Iceland: crossfade to iceland_overview
        # ══════════════════════════════════════════════════════
        ic_overview = load_map("iceland_overview")
        ic_overview.set_opacity(0)
        self.add(ic_overview)   # added behind the overlay elements

        self.play(
            FadeOut(Group(na_map, graph, us_dot, eu_dot, ic_dot,
                          arc_us_eu, arc_us_ic)),
            ic_overview.animate.set_opacity(1),
            run_time=1.2
        )

        # Iceland label
        ic_lbl = Text("Iceland", font="Poppins", weight=BOLD,
                      font_size=36, color=BANK_RED).move_to([0.0, 2.6, 0])
        self.play(FadeIn(ic_lbl), run_time=0.5)
        self.wait(0.8)

        # ══════════════════════════════════════════════════════
        # PHASE 4 — Wipe to white
        # ══════════════════════════════════════════════════════
        wipe = Rectangle(
            width=config.frame_width * 2 + 1, height=config.frame_height + 1,
            fill_color=WHITE, fill_opacity=1, stroke_width=0
        ).move_to([-config.frame_width, 0, 0])

        self.play(wipe.animate.move_to([0.5, 0, 0]),
                  run_time=0.5, rate_func=linear)
        self.remove(ic_overview, ic_lbl, wipe)

        # ══════════════════════════════════════════════════════
        # PHASE 5 — Three Icelandic bank buildings
        # ══════════════════════════════════════════════════════
        positions = [np.array([-4.0, 0.4, 0]),
                     np.array([ 0.0, 0.4, 0]),
                     np.array([ 4.0, 0.4, 0])]
        names = ["Kaupthing", "Landsbanki", "Glitnir"]

        buildings, labels, xs = [], [], []
        for pos, name in zip(positions, names):
            bld = make_bank_building(BANK_GREY)
            bld.scale(0.70).move_to(pos)
            lbl = Text(name, font="Poppins", weight=BOLD,
                       font_size=34, color=BANK_RED)
            lbl.next_to(bld, DOWN, buff=0.28)
            buildings.append(bld)
            labels.append(lbl)

        self.play(
            LaggedStart(*[FadeIn(b, shift=UP*0.25) for b in buildings],
                        lag_ratio=0.3),
            run_time=1.0
        )
        self.play(
            LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.3),
            run_time=0.7
        )
        self.wait(1.0)

        # Each bank: shake → red X slams in → topples
        for bld, lbl in zip(buildings, labels):
            # Shake
            cx = bld.get_center()
            self.play(
                bld.animate.shift(RIGHT*0.08), run_time=0.08)
            self.play(
                bld.animate.shift(LEFT*0.16),  run_time=0.08)
            self.play(
                bld.animate.shift(RIGHT*0.08), run_time=0.08)

            # Red X slams in over the building
            red_x = make_red_x(size=1.5)
            red_x.move_to(bld.get_center())
            red_x.scale(3)
            self.play(red_x.animate.scale(1/3),
                      run_time=0.25, rate_func=rush_into)

            # Building topples right
            pivot = bld.get_corner(DR) + np.array([0, -0.05, 0])
            self.play(
                Rotate(bld, angle=-PI/2, about_point=pivot),
                lbl.animate.set_opacity(0.25),
                run_time=0.6, rate_func=rush_into
            )
            xs.append(red_x)

        # "October 2008"
        date = Text("October  2008", font="Poppins", weight=BOLD,
                    font_size=54, color=BANK_RED).move_to([0, -3.0, 0])
        self.play(FadeIn(date), run_time=0.7)

        T = 17.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
