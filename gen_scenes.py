#!/usr/bin/env python3
"""Generate all 44 Manim scene Python files for Iceland EP1."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pathlib import Path

SCENES_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\scenes")
SCENES_DIR.mkdir(exist_ok=True)

# --- helpers.py ---
HELPERS = r'''"""Iceland EP1 shared helpers imported by every scene file."""
from manim import *
from pathlib import Path

BASE = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland")
SFX  = BASE / "sfx"
VO   = BASE / "vo"

def load_map(name: str) -> ImageMobject:
    img = ImageMobject(str(BASE / "maps" / f"{name}.png"))
    img.set_width(config.frame_width)
    return img

def load_character(name: str, width: float = 2.5) -> ImageMobject:
    img = ImageMobject(str(BASE / "characters" / f"{name}.png"))
    img.set_width(width)
    return img

def make_subscribe_cta() -> VGroup:
    box   = RoundedRectangle(corner_radius=0.12, width=3.2, height=0.65,
                              fill_color="#CC0000", fill_opacity=0.92,
                              stroke_color=WHITE, stroke_width=1.5)
    label = Text("\U0001f514  Subscribe", font="Poppins", font_size=22, color=WHITE)
    label.move_to(box)
    cta = VGroup(box, label)
    cta.move_to([2.2, -1.2, 0])
    return cta

ICELAND_BLUE  = "#003897"
ICELAND_WHITE = "#FFFFFF"
ICELAND_RED   = "#D72828"
AMBER         = "#C87941"
DARK_TXT      = "#2B1A0E"
WARM_TXT      = "#5A4A3A"
GREY_TXT      = "#888888"
MID_TXT       = "#AAAAAA"
GREEN_ACC     = "#8A9A6A"
DARK_RED      = "#8B1A1A"
RED_ACC       = "#FF4444"
BLUE_ACC      = "#4A90D9"
PURPLE_TXT    = "#5A4A8A"
ORANGE_ACC    = "#FF812E"
CORNER_TL     = [-2.4,  1.2, 0]
BODY_LEFT     = [-1.8,  0.0, 0]
BODY_RIGHT    = [ 1.8,  0.0, 0]
BODY_CTR      = [ 0.0,  0.0, 0]
'''

(SCENES_DIR / "helpers.py").write_text(HELPERS, encoding="utf-8")
print("wrote helpers.py")

# --- scene bodies ---
SCENES = {}

SCENES[1] = (
    "IcelandEP1_S01_TitleCard", "#003897", 20.3,
'''        Text.set_default(font="Poppins")
        title    = Text("ICELAND", font="Poppins", weight=BOLD, font_size=72, color=WHITE).move_to([0, 1.2, 0])
        subtitle = Text("Forged in Fire, Frozen in Principle", font_size=36, color="#AAAAAA")
        tagline  = Text("World's first direct democracy",     font_size=22, color="#888888")
        subtitle.next_to(title,   DOWN, buff=0.5)
        tagline.next_to(subtitle, DOWN, buff=0.3)
        self.play(FadeIn(title),    run_time=2.0)
        self.play(FadeIn(subtitle), run_time=1.5)
        self.play(FadeIn(tagline),  run_time=1.0)
        T = 4.50
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[2] = (
    "IcelandEP1_S02_BanksCollapse", "#003C9E", 18.6,
'''        Text.set_default(font="Poppins")
        sea_map = load_map("north_atlantic_dark")
        self.play(FadeIn(sea_map), run_time=1.5)
        b1 = Text("Kaupthing",  font_size=28, color=WHITE).move_to([-1.5, 0.5, 0])
        b2 = Text("Landsbanki", font_size=28, color=WHITE).move_to([ 0.0, 0.5, 0])
        b3 = Text("Glitnir",    font_size=28, color=WHITE).move_to([ 1.5, 0.5, 0])
        self.play(FadeIn(b1), run_time=0.5)
        self.play(FadeIn(b2), run_time=0.5)
        self.play(FadeIn(b3), run_time=0.5)
        banks = VGroup(b1, b2, b3)
        self.play(Flash(b1.get_center(), color=RED, flash_radius=0.8),
                  Flash(b2.get_center(), color=RED, flash_radius=0.8),
                  Flash(b3.get_center(), color=RED, flash_radius=0.8), run_time=0.5)
        self.play(FadeOut(banks), run_time=1.0)
        date_lbl = Text("October 2008", font_size=28, color="#FF4444").move_to([0, -0.5, 0])
        self.play(FadeIn(date_lbl), run_time=1.0)
        T = 5.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[3] = (
    "IcelandEP1_S03_TheNumbers", "#003C9E", 12.0,
'''        Text.set_default(font="Poppins")
        # Axes
        axes = Axes(x_range=[0,3,1], y_range=[0,12,2],
                    x_length=5, y_length=5,
                    axis_config={"color":WHITE,"stroke_width":2}, tips=False)
        axes.move_to([0, -0.3, 0])
        xl1 = Text("GDP",         font_size=20, color=WHITE).next_to(axes.x_axis.n2p(1), DOWN, buff=0.2)
        xl2 = Text("Bank Assets", font_size=20, color=WHITE).next_to(axes.x_axis.n2p(2), DOWN, buff=0.2)
        self.play(Create(axes), Create(xl1), Create(xl2), run_time=1.0)

        unit = axes.y_axis.unit_size
        bar_gdp = Rectangle(width=0.7, height=unit*1.0,
                            fill_color="#4A90D9", fill_opacity=1, stroke_width=0)
        bar_gdp.align_to(axes.x_axis.n2p(1), DOWN)
        bar_gdp.move_to([axes.x_axis.n2p(1)[0], axes.c2p(0,0.5)[1], 0])
        bar_ast = Rectangle(width=0.7, height=unit*11.0,
                            fill_color="#FF4444", fill_opacity=1, stroke_width=0)
        bar_ast.move_to([axes.x_axis.n2p(2)[0], axes.c2p(0,5.5)[1], 0])

        self.play(DrawBorderThenFill(bar_gdp), run_time=1.0)
        self.play(DrawBorderThenFill(bar_ast), run_time=0.5)
        self.play(bar_ast.animate.shift(UP*1.5).stretch(1.3, 1), run_time=1.0)
        mult = Text("11x", font="Poppins", weight=BOLD, font_size=64, color="#FF4444").move_to([2.2, 1.2, 0])
        self.play(FadeIn(mult), run_time=0.5)
        T = 4.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[4] = (
    "IcelandEP1_S04_EmptyShelves", "#003C9E", 11.2,
'''        Text.set_default(font="Poppins")
        shelf_lines = VGroup(
            Line([-3.5, 0.6,0],[3.5, 0.6,0], color="#8B5E3C", stroke_width=8),
            Line([-3.5,-0.2,0],[3.5,-0.2,0], color="#8B5E3C", stroke_width=8),
            Line([-3.5,-1.0,0],[3.5,-1.0,0], color="#8B5E3C", stroke_width=8),
        )
        cols = ["#E05A2B","#3A7ABF","#E5C32E","#A0C050","#E05A2B","#3A7ABF","#E5C32E","#A0C050"]
        items = VGroup(*[
            Square(side_length=0.32, fill_color=cols[i%8], fill_opacity=0.9, stroke_width=0)
            .move_to([-3.0+i*0.46, 0.9-int(i/8)*0.8, 0])
            for i in range(16)
        ])
        self.play(FadeIn(shelf_lines), FadeIn(items), run_time=1.0)
        self.play(LaggedStart(*[FadeOut(it) for it in reversed(items)],
                              lag_ratio=0.25, run_time=6.0))
        pop_txt = Text("300,000 people", font_size=32, color="#FF4444").move_to([0, -1.5, 0])
        self.play(FadeIn(pop_txt), run_time=0.8)
        T = 7.8
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[5] = (
    "IcelandEP1_S05_MostCountries", "#003C9E", 13.2,
'''        Text.set_default(font="Poppins")
        puppet = load_character("puppet_most_countries", width=3.0).move_to([0, 0.3, 0])
        strings = VGroup(*[
            Line([puppet.get_center()[0]+dx, puppet.get_top()[1]+0.05,0],
                 [puppet.get_center()[0]+dx, puppet.get_top()[1]+1.1, 0],
                 color="#888888", stroke_width=1.5)
            for dx in [-0.6, 0.0, 0.6]
        ])
        self.play(FadeIn(puppet), run_time=1.0)
        self.play(FadeIn(strings), run_time=0.5)
        for _ in range(3):
            self.play(Rotate(puppet, angle=5*DEGREES),  run_time=0.3)
            self.play(Rotate(puppet, angle=-5*DEGREES), run_time=0.3)
        bail  = Text("Bail out the banks.",     font_size=28, color=WHITE).move_to([0, -1.5, 0])
        repay = Text("Repay the foreign debt.", font_size=28, color=WHITE).move_to([0, -1.2, 0])
        self.play(FadeIn(bail),  run_time=0.8)
        self.play(FadeIn(repay), run_time=0.8)
        T = 5.1
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[6] = (
    "IcelandEP1_S06_IcelandAnswer", "#003897", 7.9,
'''        Text.set_default(font="Poppins")
        bars = VGroup(*[
            Line([x,-2.0,0],[x,2.0,0], color=GREY, stroke_width=6)
            for x in [-1.0,-0.6,-0.2,0.2,0.6,1.0]
        ]).move_to([-1.5, 0, 0])
        cross_bar = Line([-2.0, 0.8,0],[0.2, 0.8,0], color=GREY, stroke_width=6)
        door = VGroup(bars, cross_bar)
        banker = Text("Banker", font_size=26, color="#FF4444").move_to([-1.5, -0.3, 0])
        self.play(FadeIn(door), run_time=0.8)
        self.play(FadeIn(banker), run_time=0.5)

        flag_bg  = Rectangle(width=1.8,  height=1.2, fill_color="#003897", fill_opacity=1, stroke_color=WHITE, stroke_width=1.5)
        cross_v  = Rectangle(width=0.25, height=1.2, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cross_h  = Rectangle(width=1.8,  height=0.22,fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cross_vr = Rectangle(width=0.16, height=1.2, fill_color="#D72828", fill_opacity=1, stroke_width=0)
        cross_hr = Rectangle(width=1.8,  height=0.14,fill_color="#D72828", fill_opacity=1, stroke_width=0)
        cross_v.move_to([-0.3, 0, 0]); cross_vr.move_to([-0.3, 0, 0])
        flag = VGroup(flag_bg, cross_h, cross_v, cross_hr, cross_vr).move_to([2.2, 0, 0])
        self.play(FadeIn(flag), run_time=0.8)
        self.play(Rotate(flag, angle=2*DEGREES,  about_point=flag.get_left()), run_time=0.5)
        self.play(Rotate(flag, angle=-2*DEGREES, about_point=flag.get_left()), run_time=0.5)
        T = 3.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[7] = (
    "IcelandEP1_S07_Recovered", "#003897", 2.5,
'''        Text.set_default(font="Poppins")
        flag_bg  = Rectangle(width=4.5, height=3.0,  fill_color="#003897", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        cross_v  = Rectangle(width=0.62,height=3.0,  fill_color="#FFFFFF", fill_opacity=1, stroke_width=0).move_to([-0.7,0,0])
        cross_h  = Rectangle(width=4.5, height=0.55, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cross_vr = Rectangle(width=0.40,height=3.0,  fill_color="#D72828", fill_opacity=1, stroke_width=0).move_to([-0.7,0,0])
        cross_hr = Rectangle(width=4.5, height=0.35, fill_color="#D72828", fill_opacity=1, stroke_width=0)
        flag = VGroup(flag_bg, cross_h, cross_v, cross_hr, cross_vr)
        self.play(FadeIn(flag), run_time=0.8)
        self.play(flag.animate.scale(1.03), run_time=1.0)
        self.play(flag.animate.scale(1/1.03), run_time=1.0)
        T = 2.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[8] = (
    "IcelandEP1_S08_TimeRewind", "#003897", 9.1,
'''        Text.set_default(font="Poppins")
        sea_map = load_map("north_atlantic_dark")
        sea_map.set_opacity(0.8)
        self.add(sea_map)
        self.play(sea_map.animate.scale(0.15), run_time=3.0)
        years = ["2008","1944","1874","1262","1000","874"]
        yr_txt = Text(years[0], font_size=40, color="#C87941").move_to([0,-0.5,0])
        self.play(FadeIn(yr_txt), run_time=0.2)
        for y in years[1:]:
            new_t = Text(y, font_size=40, color="#C87941").move_to([0,-0.5,0])
            self.play(FadeTransform(yr_txt, new_t), run_time=0.15)
            yr_txt = new_t
        self.play(FadeOut(yr_txt), run_time=0.3)
        year_lbl = Text("874 AD", font="Poppins", weight=BOLD, font_size=80, color="#C87941").move_to([0,0,0])
        self.play(FadeIn(year_lbl), run_time=1.5)
        glow = Rectangle(width=5, height=1.8, fill_color="#C87941", fill_opacity=0, stroke_width=0).move_to(year_lbl)
        self.add(glow)
        self.play(glow.animate.set_fill(opacity=0.12), run_time=2.0)
        T = 7.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[9] = (
    "IcelandEP1_S09_BackUpFurther", "#003897", 6.2,
'''        Text.set_default(font="Poppins")
        yr_old = Text("874 AD",  font="Poppins", weight=BOLD, font_size=60, color="#C87941").move_to([0,1.2,0])
        yr_new = Text("c. 800s", font="Poppins", weight=BOLD, font_size=60, color="#C87941").move_to([0,1.2,0])
        self.add(yr_old)
        self.play(FadeTransform(yr_old, yr_new), run_time=1.0)
        iceland_map = load_map("iceland_blank")
        iceland_map.set_opacity(0.7).set_width(7)
        self.play(FadeIn(iceland_map), run_time=1.5)
        no_one = Text("No one home. Yet.", font_size=28, color="#888888").move_to([0,-1.5,0])
        self.play(FadeIn(no_one), run_time=0.8)
        T = 3.3
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[10] = (
    "IcelandEP1_S10_TheMonks", "#EEF4FC", 23.2,
'''        Text.set_default(font="Poppins")
        route_map = load_map("ireland_to_iceland_route")
        self.play(FadeIn(route_map), run_time=1.5)
        monk = load_character("irish_monk_packing", width=2.5).move_to([-2.0, 0, 0])
        self.play(FadeIn(monk), run_time=1.0)
        lbl  = Text("The Papar", font_size=24, color="#5A4A3A").next_to(monk, DOWN, buff=0.2)
        desc = Text("Irish Christian hermits", font_size=26, color="#5A4A3A").move_to([0,-1.2,0])
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(FadeIn(desc), run_time=0.8)
        route_line = DashedLine([-4.5,-1.0,0],[1.5,1.5,0],
                                dash_length=0.15, dashed_ratio=0.6,
                                color="#C87941", stroke_width=2.5)
        self.play(Create(route_line), run_time=3.0)
        T = 6.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[11] = (
    "IcelandEP1_S11_PerfectExistence", "#EEF4FC", 8.7,
'''        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        self.play(FadeIn(iceland_map), run_time=1.5)
        date_lbl = Text("c. 800 AD", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        txt = Text("Perfectly good solitary existence.", font_size=30, color="#5A4A3A").move_to([0,-1.5,0])
        self.play(FadeIn(txt), run_time=1.0)
        T = 3.0
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[12] = (
    "IcelandEP1_S12_MonkDeparts", "#EEF4FC", 7.9,
'''        Text.set_default(font="Poppins")
        ship = Polygon([3.0,-0.5,0],[5.5,-0.5,0],[4.5,0.5,0],
                       fill_color="#5A4A3A", fill_opacity=0.8, stroke_width=0)
        self.play(FadeIn(ship), run_time=1.0)
        monk = load_character("irish_monk_seated", width=2.0).move_to([-1.0, 0, 0])
        self.play(FadeIn(monk), run_time=0.8)
        self.play(monk.animate.move_to([-8, 0, 0]), run_time=2.0)
        farewell = Text("They were never coming back.", font_size=28, color="#5A4A3A").move_to([0,-0.5,0])
        self.play(FadeIn(farewell), run_time=0.8)
        T = 4.6
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[13] = (
    "IcelandEP1_S13_FirstInstinct", "#EEF4FC", 14.5,
'''        Text.set_default(font="Poppins")
        t1 = Text("They came to be alone.", font="Poppins", weight=BOLD, font_size=40, color="#2B1A0E").move_to([0,0,0])
        self.play(FadeIn(t1), run_time=1.2)
        self.play(FadeOut(t1), run_time=0.3)
        t2 = Text("Iceland's first residents.", font_size=30, color="#2B1A0E").move_to([0,0,0])
        self.play(FadeIn(t2), run_time=1.0)
        self.play(FadeOut(t2), run_time=0.3)
        t3 = Text("Iceland's founders.", font_size=30, color="#2B1A0E").move_to([0,0,0])
        t4 = Text("Same instinct.", font_size=36, color="#C87941").move_to([0,-0.9,0])
        self.play(FadeIn(t3), run_time=1.0)
        self.play(FadeIn(t4), run_time=1.0)
        T = 4.5
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[14] = (
    "IcelandEP1_S14_IngoflrSetsOut", "#EEF4FC", 22.8,
'''        Text.set_default(font="Poppins")
        ingolfr = load_character("ingolfr_arnarson", width=2.5).move_to([4, 0, 0])
        self.play(ingolfr.animate.move_to([1.5, 0, 0]), run_time=1.0)
        name_lbl = Text("Ingolfr Arnarson", font_size=26, color="#2B1A0E")
        sub_lbl  = Text("874 AD", font_size=20, color="#888888")
        labels = VGroup(name_lbl, sub_lbl).arrange(DOWN, buff=0.1)
        labels.next_to(ingolfr, DOWN, buff=0.2)
        self.play(FadeIn(labels), run_time=0.5)
        norway_map = load_map("norway_coast")
        norway_map.set_width(6).move_to([-3, 0, 0]).set_opacity(0.7)
        self.play(FadeIn(norway_map), run_time=1.0)
        ship = Triangle(fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ship.set_width(0.8).rotate(-90*DEGREES).move_to([-4, -1.5, 0])
        self.add(ship)
        self.play(ship.animate.move_to([3, -1.5, 0]), run_time=5.0)
        corner_date = Text("874 AD", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.play(FadeIn(corner_date), run_time=0.5)
        T = 8.0
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[15] = (
    "IcelandEP1_S15_PillarsOverboard", "#F0F6FE", 18.6,
'''        Text.set_default(font="Poppins")
        ocean = Rectangle(width=14.22, height=3, fill_color="#003060",
                          fill_opacity=0.5, stroke_width=0).move_to([0,-2.5,0])
        ship_body = Polygon([-1.5,0.3,0],[1.5,0.3,0],[1.0,-0.5,0],[-1.0,-0.5,0],
                            fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ingolfr = load_character("ingolfr_releasing_pillars", width=1.8).move_to([0, 0.6, 0])
        self.play(FadeIn(ocean), FadeIn(ship_body), FadeIn(ingolfr), run_time=0.5)
        p1 = Rectangle(width=0.2, height=1.2, fill_color="#C87941", fill_opacity=1, stroke_width=0).move_to([-0.4, 0.5, 0])
        p2 = Rectangle(width=0.2, height=1.2, fill_color="#C87941", fill_opacity=1, stroke_width=0).move_to([ 0.4, 0.5, 0])
        self.add(p1, p2)
        self.play(p1.animate.move_to([-2,-2,0]).set_opacity(0),
                  p2.animate.move_to([ 2,-2,0]).set_opacity(0), run_time=0.8)
        t1 = Text("Wherever they land...", font_size=30, color=WHITE).move_to([0,-1.5,0])
        t2 = Text("...that\'s home.", font="Poppins", weight=BOLD, font_size=36, color="#C87941").move_to([0, 0.3,0])
        self.play(FadeIn(t1), run_time=1.0)
        self.play(FadeIn(t2), run_time=1.0)
        T = 4.0
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[16] = (
    "IcelandEP1_S16_ThreeYears", "#F0F6FE", 5.0,
'''        Text.set_default(font="Poppins")
        coast_map = load_map("iceland_coastline")
        self.add(coast_map)
        arc = Arc(radius=2.5, start_angle=-PI/2, angle=2*PI,
                  color="#C87941", stroke_width=2.5)
        self.play(Create(arc), run_time=4.5)
        for i, yr in enumerate(["Year 1", "Year 2", "Year 3"]):
            lbl = Text(yr, font="Poppins", weight=BOLD, font_size=40, color="#2B1A0E").move_to([0,-0.5,0])
            self.play(FadeIn(lbl), run_time=0.1)
            self.wait(0.2)
            if i < 2:
                self.play(FadeOut(lbl), run_time=0.1)
        self.wait(1.0)
''')

SCENES[17] = (
    "IcelandEP1_S17_ReykjavikFounded", "#F5F8FD", 15.7,
'''        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        self.add(iceland_map)
        self.play(iceland_map.animate.set_width(10).move_to([0.5,-0.3,0]), run_time=1.5)
        steam = VGroup(*[
            Triangle(fill_color="#AADDFF", fill_opacity=0.5-0.1*i, stroke_width=0)
            .scale(0.4).move_to([-1.5+i*0.3, -0.5+i*0.5, 0])
            for i in range(4)
        ])
        self.play(FadeIn(steam), run_time=1.0)
        self.play(steam.animate.shift(UP*1.0).set_opacity(0), run_time=1.0)
        city_name = Text("Reykjavik", font="Poppins", weight=BOLD, font_size=40, color="#2B1A0E").move_to([0,1.0,0])
        self.play(FadeIn(city_name), run_time=1.0)
        meaning = Text("Smoky Bay.", font_size=28, color="#5A4A3A").next_to(city_name, DOWN, buff=0.3)
        self.play(FadeIn(meaning), run_time=0.8)
        footer = Text("Iceland\'s capital. Day one.", font_size=26, color="#888888").move_to([0,-1.5,0])
        self.play(FadeIn(footer), run_time=0.8)
        T = 6.4
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[18] = (
    "IcelandEP1_S18_GreatMigration", "#F5F8FD", 17.0,
'''        Text.set_default(font="Poppins")
        import random; random.seed(42)
        iceland_map = load_map("iceland_overview")
        self.play(FadeIn(iceland_map), run_time=1.0)
        dots = VGroup(*[
            Dot(point=[random.uniform(-3.5,3.5), random.uniform(-1.5,1.5), 0],
                radius=0.08, color="#C87941")
            for _ in range(40)
        ])
        pop_lbl = Text("0", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.add(pop_lbl)
        groups = [dots[i:i+8] for i in range(0,40,8)]
        pop_vals = ["8,000","12,000","16,000","20,000","20,000"]
        for grp, pop in zip(groups, pop_vals):
            self.play(LaggedStart(*[FadeIn(d) for d in grp], lag_ratio=0.1, run_time=1.2))
            new_lbl = Text(pop, font_size=24, color="#888888").move_to([-2.4,1.2,0])
            self.play(FadeTransform(pop_lbl, new_lbl), run_time=0.2)
            pop_lbl = new_lbl
        date_lbl = Text("874 - 930 AD", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.play(FadeTransform(pop_lbl, date_lbl), run_time=0.5)
        T = 7.5
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[19] = (
    "IcelandEP1_S19_WhyTheyCame", "#F5F8FD", 18.6,
'''        Text.set_default(font="Poppins")
        norway_map = load_map("norway_coast")
        norway_map.set_width(6).move_to([-2, 0, 0]).set_opacity(0.7)
        self.play(FadeIn(norway_map), run_time=1.5)
        king = load_character("king_Harald_Fairhair", width=2.2).move_to([1.5, 0, 0])
        king_lbl = Text("Harald Fairhair", font_size=22, color="#2B1A0E").next_to(king, DOWN, buff=0.2)
        self.play(FadeIn(king), FadeIn(king_lbl), run_time=1.0)
        arrows = VGroup(*[
            Arrow([-1.0, y, 0],[1.5, y+0.3, 0], color="#FF4444", stroke_width=3)
            for y in [-0.5, 0, 0.5]
        ])
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.3, run_time=1.5))
        t1 = Text("Too crowded.",          font_size=30, color="#2B1A0E").move_to([0, 0.5, 0])
        t2 = Text("Bad king.",             font_size=30, color="#2B1A0E").move_to([0,-0.1, 0])
        t3 = Text("Active volcano? Fine.", font_size=30, color="#C87941").move_to([0,-0.7, 0])
        self.play(FadeIn(t1), run_time=0.5)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), run_time=0.8)
        T = 5.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[20] = (
    "IcelandEP1_S20_BuiltGovernment", "#F5F8FD", 9.1,
'''        Text.set_default(font="Poppins")
        settlers = load_character("viking_settler", width=2.5).move_to([0, 0, 0])
        self.play(FadeIn(settlers), run_time=1.0)
        qmark = Text("?", font="Poppins", weight=BOLD, font_size=80, color="#C87941").next_to(settlers, UP, buff=0.3)
        self.play(FadeIn(qmark), run_time=0.8)
        question = Text("How do we govern this?", font="Poppins", weight=BOLD,
                        font_size=34, color="#2B1A0E").move_to([0,-1.5,0])
        self.play(FadeIn(question), run_time=1.0)
        self.play(qmark.animate.scale(1.1), run_time=0.5)
        self.play(qmark.animate.scale(1/1.1), run_time=0.5)
        self.play(qmark.animate.scale(1.1), run_time=0.5)
        self.play(qmark.animate.scale(1/1.1), run_time=0.5)
        T = 4.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[21] = (
    "IcelandEP1_S21_AlthingConvenes", "#F5F8FD", 16.1,
'''        Text.set_default(font="Poppins")
        valley_map = load_map("thingvellir")
        self.play(FadeIn(valley_map), run_time=1.5)
        date_lbl   = Text("930 AD", font_size=32, color="#C87941").move_to([-2.4,1.2,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        place_name = Text("Thingvellir", font="Poppins", weight=BOLD, font_size=36, color="#2B1A0E").move_to([0,0.5,0])
        self.play(FadeIn(place_name), run_time=0.8)
        rift = DashedLine([-5.0,-0.5,0],[5.0,-0.5,0], dash_length=0.3, dashed_ratio=0.5,
                          color="#888888", stroke_width=2)
        self.play(Create(rift), run_time=2.0)
        althing_txt = Text("The Althing", font="Poppins", weight=BOLD, font_size=40, color="#8A9A6A").move_to([0,-1.2,0])
        self.play(FadeIn(althing_txt), run_time=1.0)
        T = 8.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[22] = (
    "IcelandEP1_S22_ThirtyChieftains", "#F5F8FD", 24.0,
'''        Text.set_default(font="Poppins")
        import math
        chieftains = VGroup(*[
            Dot(point=[2.5*math.cos(i*2*PI/36), 2.5*math.sin(i*2*PI/36), 0],
                radius=0.12, color="#C87941")
            for i in range(36)
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in chieftains], lag_ratio=0.06, run_time=1.5))
        count_lbl  = Text("36 chieftains", font_size=30, color="#2B1A0E").move_to([0,0,0])
        self.play(FadeIn(count_lbl), run_time=0.5)
        self.play(chieftains.animate.scale(1.15), run_time=6.0)
        parl_txt  = Text("World\'s oldest surviving parliament", font_size=28, color="#8A9A6A").move_to([0,-1.2,0])
        still_txt = Text("930 AD  -  still active today",        font_size=24, color="#888888").move_to([0,-1.7,0])
        self.play(FadeIn(parl_txt),  run_time=1.0)
        self.play(FadeIn(still_txt), run_time=0.8)
        cta = make_subscribe_cta()
        self.play(FadeIn(cta), run_time=0.5)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(cta), run_time=0.5)
        T = 9.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[23] = (
    "IcelandEP1_S23_ItWorked", "#F5F8FD", 9.9,
'''        Text.set_default(font="Poppins")
        timeline  = Line([-4.5,0.5,0],[4.5,0.5,0], color="#8A9A6A", stroke_width=3)
        left_lbl  = Text("930 AD", font_size=22, color="#8A9A6A").move_to([-4.5,0.9,0])
        right_lbl = Text("Today",  font_size=22, color="#8A9A6A").move_to([ 4.5,0.9,0])
        self.play(Create(timeline), FadeIn(left_lbl), FadeIn(right_lbl), run_time=1.5)
        tick = Dot([-4.3,0.5,0], radius=0.12, color="#C87941")
        self.play(tick.animate.move_to([4.3,0.5,0]), run_time=0.5)
        not_perfect = Text("Not a perfect democracy.", font_size=28, color="#5A4A3A").move_to([0,-0.3,0])
        but_worked  = Text("But it worked.", font="Poppins", weight=BOLD, font_size=40, color="#8A9A6A").move_to([0,-1.0,0])
        self.play(FadeIn(not_perfect), run_time=0.8)
        self.play(FadeIn(but_worked),  run_time=1.0)
        T = 3.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[24] = (
    "IcelandEP1_S24_ConversionCrisis", "#EAF0F8", 17.8,
'''        Text.set_default(font="Poppins")
        cross_v = Rectangle(width=0.28,height=1.6, fill_color=WHITE, fill_opacity=0.9, stroke_width=0).move_to([-3.0,0.0,0])
        cross_h = Rectangle(width=1.2, height=0.28,fill_color=WHITE, fill_opacity=0.9, stroke_width=0).move_to([-3.0,0.3,0])
        cross = VGroup(cross_v, cross_h)
        hammer_head = Rectangle(width=1.0,height=0.4, fill_color="#C87941", fill_opacity=0.9, stroke_width=0).move_to([3.0, 0.3,0])
        hammer_hndl = Rectangle(width=0.3,height=0.9, fill_color="#C87941", fill_opacity=0.9, stroke_width=0).move_to([3.0,-0.2,0])
        hammer = VGroup(hammer_head, hammer_hndl)
        divider = DashedLine([0,-2.5,0],[0,2.5,0], dash_length=0.2, color="#888888", stroke_width=1.5)
        self.play(FadeIn(cross), FadeIn(hammer), Create(divider), run_time=1.5)
        date_lbl = Text("c. Year 1000", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        title_txt = Text("The Conversion Question", font="Poppins", weight=BOLD, font_size=34, color="#2B1A0E").move_to([0,-1.5,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        self.play(FadeIn(title_txt), run_time=1.0)
        c1 = Text("Christianity", font_size=30, color="#4A90D9").move_to([-1.8,0.0,0])
        c2 = Text("Old Ways",     font_size=30, color="#C87941").move_to([ 1.8,0.0,0])
        self.play(FadeIn(c1), FadeIn(c2), run_time=0.8)
        T = 6.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[25] = (
    "IcelandEP1_S25_ThorgeIrDecides", "#EAF0F8", 17.4,
'''        Text.set_default(font="Poppins")
        thorgeir = load_character("thorgeir_under_cloak", width=2.5).move_to([0, 0, 0])
        self.play(FadeIn(thorgeir), run_time=1.0)
        lbl  = Text("Thorgeir Thorkelsson", font_size=22, color="#2B1A0E")
        sub  = Text("Lawspeaker - pagan",   font_size=18, color="#888888")
        lbls = VGroup(lbl, sub).arrange(DOWN, buff=0.1).next_to(thorgeir, DOWN, buff=0.2)
        self.play(FadeIn(lbls), run_time=0.5)
        t_hrs = Text("24 hours.",               font_size=36, color="#C87941").move_to([-2.5, 0.5,0])
        t_sil = Text("Silent. Under his cloak.", font_size=28, color="#5A4A3A").move_to([-2.5,-0.1,0])
        self.play(FadeIn(t_hrs), run_time=0.8)
        self.play(FadeIn(t_sil), run_time=0.8)
        clock_circle = Circle(radius=0.8, color=WHITE, stroke_width=2).move_to([2.5, 0, 0])
        clock_hand   = Line([2.5,0,0],[2.5,0.75,0], color=WHITE, stroke_width=3)
        self.play(Create(clock_circle), Create(clock_hand), run_time=0.5)
        self.play(Rotate(clock_hand, angle=-2*PI, about_point=[2.5,0,0]), run_time=4.0)
        stood = Text("Then he stood up.", font="Poppins", weight=BOLD, font_size=36, color="#2B1A0E").move_to([0,-1.5,0])
        self.play(FadeIn(stood), run_time=1.0)
        T = 8.1
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[26] = (
    "IcelandEP1_S26_HorsemeatExemption", "#EAF0F8", 28.1,
'''        Text.set_default(font="Poppins")
        christianity = Text("Christianity.", font="Poppins", weight=BOLD, font_size=48, color="#2B1A0E").move_to([0,0.5,0])
        self.play(FadeIn(christianity), run_time=1.0)
        hammer_icon = Text("Hammer gone.", font_size=24, color="#888888").move_to([2.5,-0.5,0])
        self.add(hammer_icon)
        self.play(FadeOut(hammer_icon), run_time=1.5)
        cross_v = Rectangle(width=0.3, height=1.8, fill_color=AMBER, fill_opacity=0.8, stroke_width=0)
        cross_h = Rectangle(width=1.2, height=0.3, fill_color=AMBER, fill_opacity=0.8, stroke_width=0).shift(UP*0.5)
        cross = VGroup(cross_v, cross_h).move_to([-3.0, 0, 0])
        self.play(FadeIn(cross), run_time=1.0)
        exceptions = Text("...with exceptions.", font_size=34, color="#C87941").move_to([0,-0.3,0])
        self.play(FadeIn(exceptions), run_time=0.8)
        self.play(FadeOut(christianity), run_time=0.3)
        ex1 = Text("Horsemeat at home: still fine.",    font_size=28, color="#888888").move_to([0, 0.3,0])
        ex2 = Text("Private pagan ritual: still fine.", font_size=28, color="#888888").move_to([0,-0.3,0])
        ex3 = Text("This is peak Iceland.", font="Poppins", weight=BOLD, font_size=30, color="#C87941").move_to([0,-1.0,0])
        self.play(FadeIn(ex1), run_time=0.8)
        self.play(FadeIn(ex2), run_time=0.8)
        self.play(FadeIn(ex3), run_time=1.0)
        T = 6.9
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[27] = (
    "IcelandEP1_S27_ErikExiled", "#EAF0F8", 20.3,
'''        Text.set_default(font="Poppins")
        erik = load_character("erik_the_red", width=2.5).move_to([-5.0, 0, 0])
        self.play(erik.animate.move_to([0.0, 0, 0]), run_time=1.0)
        lbl  = Text("Erik the Red",             font_size=26, color="#2B1A0E")
        sub  = Text("982 AD  -  twice exiled",  font_size=20, color="#888888")
        lbls = VGroup(lbl, sub).arrange(DOWN, buff=0.1).next_to(erik, DOWN, buff=0.2)
        self.play(FadeIn(lbls), run_time=0.5)
        exile_txt = Text("EXILE", font="Poppins", weight=BOLD, font_size=36, color="#FF4444").next_to(erik, UP, buff=0.3)
        self.play(FadeIn(exile_txt), run_time=0.8)
        map_lbl = Text("3 years exile.", font_size=28, color="#888888").move_to([2.5, 0, 0])
        self.play(FadeIn(map_lbl), run_time=0.5)
        ocean = Rectangle(width=14.22, height=8.0, fill_color="#003060", fill_opacity=0.7, stroke_width=0)
        self.play(FadeOut(map_lbl), FadeIn(ocean), run_time=1.5)
        west = Text("He went west anyway.", font_size=34, color="#C87941").move_to([0, 0, 0])
        self.play(FadeIn(west), run_time=0.8)
        T = 6.1
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[28] = (
    "IcelandEP1_S28_Greenland", "#EAF0F8", 23.6,
'''        Text.set_default(font="Poppins")
        atl_map = load_map("north_atlantic")
        self.play(FadeIn(atl_map), run_time=1.0)
        ship = Triangle(fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ship.set_width(0.5).rotate(-90*DEGREES).move_to([0.5,-0.3,0])
        self.add(ship)
        self.play(ship.animate.move_to([-2.5,-0.2,0]), run_time=3.0)
        gl_name = Text("Greenland", font="Poppins", weight=BOLD, font_size=40, color=WHITE).move_to([-2.5,1.0,0])
        self.play(FadeIn(gl_name), run_time=0.8)
        self.play(FadeOut(gl_name), run_time=0.3)
        ice_desc  = Text("Mostly covered in ice.",  font_size=28, color="#5A4A3A").move_to([0, 0.5,0])
        name_desc = Text("He named it Greenland.",  font_size=30, color="#888888").move_to([0,-0.1,0])
        arrow_lbl = Text("Iceland (the friendly name)", font_size=20, color=AMBER).move_to([2.5,-1.2,0])
        self.play(FadeIn(ice_desc), run_time=0.5)
        self.play(FadeIn(name_desc), run_time=0.5)
        self.play(FadeIn(arrow_lbl), run_time=1.0)
        T = 6.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[29] = (
    "IcelandEP1_S29_LeifNorthAmerica", "#EAF0F8", 29.0,
'''        Text.set_default(font="Poppins")
        atl_map = load_map("north_atlantic")
        leif = load_character("leif_eriksson", width=2.5).move_to([3.0, 0, 0])
        self.play(FadeIn(atl_map), FadeIn(leif), run_time=1.0)
        lbl = Text("Leif Eriksson  -  c. 1000 AD", font_size=22, color="#2B1A0E").next_to(leif, DOWN, buff=0.2)
        self.play(FadeIn(lbl), run_time=0.5)
        ship = Triangle(fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ship.set_width(0.5).rotate(-90*DEGREES).move_to([-2.0,-0.5,0])
        self.add(ship)
        self.play(ship.animate.move_to([-5.0,-0.8,0]), run_time=4.0)
        site_lbl = Text("L\'Anse aux Meadows", font_size=28, color=WHITE).move_to([-4.5,-0.2,0])
        self.play(FadeIn(site_lbl), run_time=0.5)
        columbus = Text("500 years before Columbus.", font="Poppins", weight=BOLD, font_size=34, color="#C87941").move_to([0,1.2,0])
        evidence = Text("Tree-ring evidence. 1021 AD. Confirmed.", font_size=24, color="#888888").move_to([0,0.6,0])
        self.play(FadeIn(columbus),  run_time=1.0)
        self.play(FadeIn(evidence),  run_time=0.8)
        T = 7.8
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[30] = (
    "IcelandEP1_S30_IcelandWasWriting", "#EAF0F8", 21.9,
'''        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        self.play(FadeIn(iceland_map), run_time=1.5)
        quill_trail = Line([-3,0,0],[3,0,0], color=AMBER, stroke_width=2.5)
        self.play(Create(quill_trail), run_time=2.0)
        sagas = VGroup(*[
            Text("Saga", font="Poppins", weight=BOLD, font_size=20, color="#5A4A3A")
            .move_to([2.5, -0.5+i*0.45, 0])
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(s) for s in sagas], lag_ratio=0.5, run_time=2.0))
        while_txt   = Text("While others were exploring...", font_size=28, color="#5A4A3A").move_to([0,-1.2,0])
        writing_txt = Text("Iceland was writing everything down.", font="Poppins", weight=BOLD, font_size=34, color="#2B1A0E").move_to([0,-1.8,0])
        self.play(FadeIn(while_txt),   run_time=0.8)
        self.play(FadeIn(writing_txt), run_time=1.0)
        T = 7.3
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[31] = (
    "IcelandEP1_S31_SnorriAndMarvel", "#EAF0F8", 32.3,
'''        Text.set_default(font="Poppins")
        snorri_y = load_character("snorri_young", width=2.5).move_to([-1.5, 0, 0])
        self.play(FadeIn(snorri_y), run_time=1.0)
        lbl = Text("Snorri Sturluson  -  born 1179", font_size=22, color="#2B1A0E").next_to(snorri_y, DOWN, buff=0.2)
        self.play(FadeIn(lbl), run_time=0.5)
        book_bg    = Rectangle(width=1.5, height=2.0, fill_color="#8A6030", fill_opacity=0.9, stroke_width=0).move_to([2.5,0,0])
        book_title = Text("Prose Edda", font_size=16, color=WHITE).move_to(book_bg.get_center())
        self.play(FadeIn(book_bg), FadeIn(book_title), run_time=1.0)
        for name, pos in [("Odin",[-3.5,0.8,0]),("Thor",[-3.5,0.0,0]),("Loki",[-3.5,-0.8,0])]:
            g = Text(name, font_size=24, color="#C87941").move_to(pos)
            self.play(FadeIn(g), run_time=0.5)
        if_we      = Text("If we know Norse mythology today...", font_size=28, color="#5A4A3A").move_to([0,-1.5,0])
        its_snorri = Text("it\'s because Snorri wrote it down.", font="Poppins", weight=BOLD, font_size=34, color="#8A9A6A").move_to([0,-2.0,0])
        self.play(FadeIn(if_we),     run_time=0.8)
        self.play(FadeIn(its_snorri), run_time=1.0)
        snorri_o = load_character("snorri_older", width=2.5).move_to([-1.5, 0, 0])
        self.play(FadeTransform(snorri_y, snorri_o), run_time=2.0)
        T = 10.3
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[32] = (
    "IcelandEP1_S32_SnorriPolitician", "#D0E0F0", 7.4,
'''        Text.set_default(font="Poppins")
        snorri_o = load_character("snorri_older", width=2.5).move_to([0, 0.3, 0])
        self.play(FadeIn(snorri_o), run_time=1.0)
        shadow = Triangle(fill_color="#000000", fill_opacity=0.55, stroke_width=0)
        shadow.set_width(5).rotate(180*DEGREES).move_to([5, 3, 0])
        self.add(shadow)
        self.play(shadow.animate.move_to([3.5, 1.5, 0]), run_time=1.5)
        pol_txt  = Text("Snorri was also a politician.",     font_size=32, color="#2B1A0E").move_to([0,-1.3,0])
        kill_txt = Text("This eventually got him killed.", font_size=32, color="#8B1A1A").move_to([0,-1.9,0])
        self.play(FadeIn(pol_txt),  run_time=0.8)
        self.play(FadeIn(kill_txt), run_time=0.8)
        T = 4.1
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[33] = (
    "IcelandEP1_S33_SturlungAge", "#D72828", 12.8,
'''        Text.set_default(font="Poppins")
        clan_map = load_map("iceland_clans")
        self.play(FadeIn(clan_map), run_time=1.5)
        date_lbl = Text("1220 - 1262", font_size=28, color="#FF4444").move_to([-2.4,1.2,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        sturlung = Text("The Sturlung Age", font="Poppins", weight=BOLD, font_size=40, color="#8B1A1A").move_to([0,0.5,0])
        self.play(FadeIn(sturlung), run_time=1.0)
        arrows = VGroup(*[
            Arrow(start, end, color="#FF4444", stroke_width=3)
            for start, end in [([-2.0,1.0,0],[1.5,-0.5,0]),
                               ([ 1.8,0.8,0],[-1.0,-1.0,0]),
                               ([-0.5,-1.2,0],[2.5,0.5,0])]
        ])
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.4, run_time=3.0))
        civil_war = Text("Iceland\'s civil war.", font_size=32, color="#FF4444").move_to([0,-1.5,0])
        self.play(FadeIn(civil_war), run_time=0.5)
        T = 6.5
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[34] = (
    "IcelandEP1_S34_HakonWatches", "#C42020", 14.1,
'''        Text.set_default(font="Poppins")
        norway_map = load_map("norway_coast")
        norway_map.set_width(5).move_to([-2.5, 0, 0]).set_opacity(0.6)
        self.play(FadeIn(norway_map), run_time=1.0)
        hakon = load_character("hakon", width=2.5).move_to([2.0, 0, 0])
        self.play(FadeIn(hakon), run_time=0.5)
        lbl = Text("King Hakon IV  -  Norway", font_size=22, color=WHITE).next_to(hakon, DOWN, buff=0.2)
        self.play(FadeIn(lbl), run_time=0.5)
        for _ in range(3):
            self.play(hakon.animate.shift(RIGHT*0.05), run_time=0.4)
            self.play(hakon.animate.shift(LEFT*0.05),  run_time=0.4)
        patient = Text("Patient.",     font="Poppins", weight=BOLD, font_size=36, color="#5A4A8A").move_to([2.0,0.8,0])
        calc    = Text("Calculating.", font_size=36, color="#5A4A8A").move_to([2.0,0.2,0])
        self.play(FadeIn(patient), run_time=0.8)
        self.play(FadeIn(calc),    run_time=0.8)
        T = 6.6
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[35] = (
    "IcelandEP1_S35_SeventyMen", "#B01818", 7.0,
'''        Text.set_default(font="Poppins")
        farm_map = load_map("reykholt_farm")
        self.play(FadeIn(farm_map), run_time=1.0)
        location_lbl = Text("Reykholt. Night.", font_size=32, color="#FF4444").move_to([0,1.2,0])
        self.play(FadeIn(location_lbl), run_time=0.5)
        crowd = VGroup(*[
            Dot([3.5+i*0.15, -0.3+(i%5)*0.2-0.4, 0], radius=0.08, color="#8B1A1A")
            for i in range(25)
        ])
        self.add(crowd)
        self.play(crowd.animate.shift(LEFT*3.5), run_time=2.5)
        seventy = Text("70 men.", font="Poppins", weight=BOLD, font_size=48, color="#8B1A1A").move_to([0,-1.5,0])
        self.play(FadeIn(seventy), run_time=0.5)
        T = 4.5
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[36] = (
    "IcelandEP1_S36_LastWords", "#8B1010", 7.4,
'''        Text.set_default(font="Poppins")
        torch_glow = Circle(radius=2.0, fill_color="#C87941", fill_opacity=0.15, stroke_width=0).move_to([3.0,-1.5,0])
        self.play(FadeIn(torch_glow), run_time=0.5)
        snorri = load_character("snorri_older", width=2.0).move_to([-1.5,-0.3,0])
        self.play(FadeIn(snorri), run_time=0.8)
        words_ic = Text("Eigi skal hoggva.", font="Poppins", weight=BOLD, font_size=36, color=WHITE).move_to([0,0.8,0])
        words_en = Text("Do not strike.",    font_size=28, color="#AAAAAA").move_to([0,0.2,0])
        self.play(FadeIn(words_ic), run_time=1.0)
        self.play(FadeIn(words_en), run_time=0.8)
        T = 3.1
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[37] = (
    "IcelandEP1_S37_TheyStruck", "#000000", 2.5,
'''        Text.set_default(font="Poppins")
        self.wait(0.2)
        struck = Text("They struck.", font="Poppins", weight=BOLD, font_size=56, color=WHITE).move_to([0,0,0])
        self.play(FadeIn(struck), run_time=1.5)
        T = 2.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(struck), run_time=1.0)
''')

SCENES[38] = (
    "IcelandEP1_S38_OldCovenant", "#A01818", 22.3,
'''        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        iceland_map.set_opacity(0.5)
        self.play(FadeIn(iceland_map), run_time=2.0)
        year_lbl = Text("1262", font_size=40, color="#8B1A1A").move_to([-2.4,1.2,0])
        over_lbl = Text("The Commonwealth: over.", font_size=32, color="#5A4A3A").move_to([0,0.5,0])
        self.play(FadeIn(year_lbl), run_time=0.8)
        self.play(FadeIn(over_lbl), run_time=0.8)
        seal_rect = Rectangle(width=2.5, height=1.5, fill_color="#C42020", fill_opacity=0.85,
                              stroke_color=WHITE, stroke_width=1.5)
        seal_txt  = Text("NORWAY", font_size=22, color=WHITE).move_to(seal_rect)
        seal = VGroup(seal_rect, seal_txt).move_to([1.5,-0.5,0])
        self.play(FadeIn(seal), run_time=1.5)
        self.play(FadeOut(over_lbl), run_time=0.3)
        exhausted = Text("Chieftains: exhausted.", font_size=28, color="#888888").move_to([0,-0.3,0])
        bloodshed = Text("Bloodshed: too high.",   font_size=28, color="#888888").move_to([0,-0.8,0])
        self.play(FadeIn(exhausted), run_time=0.8)
        self.play(FadeIn(bloodshed), run_time=0.8)
        cta = make_subscribe_cta()
        self.play(FadeIn(cta), run_time=0.5)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(cta), run_time=0.5)
        T = 6.7
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[39] = (
    "IcelandEP1_S39_SurrenderByChoice", "#B82020", 29.8,
'''        Text.set_default(font="Poppins")
        table = Rectangle(width=4, height=0.5, fill_color="#8B6030", fill_opacity=0.9, stroke_width=0).move_to([0,-0.5,0])
        doc   = Rectangle(width=1.5, height=2.0, fill_color="#FFFDE7", fill_opacity=0.9,
                          stroke_color="#888888", stroke_width=1).move_to([0,0.5,0])
        self.play(FadeIn(table), FadeIn(doc), run_time=1.0)
        reps = VGroup(*[Dot([-5+i*0.3,-0.2,0], radius=0.12, color="#EEE") for i in range(5)])
        self.add(reps)
        self.play(reps.animate.shift(RIGHT*4.5), run_time=2.0)
        not_conquest = Text("Not conquest.", font="Poppins", weight=BOLD, font_size=36, color=WHITE).move_to([0,1.2,0])
        surrender    = Text("A surrender by choice.",              font_size=36, color="#C87941").move_to([0,0.6,0])
        iceland_way  = Text("Which is somehow more Icelandic.",    font_size=28, color="#888888").move_to([0,0.0,0])
        self.play(FadeIn(not_conquest), run_time=0.8)
        self.play(FadeIn(surrender),    run_time=0.8)
        self.play(FadeIn(iceland_way),  run_time=0.8)
        T = 8.4
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[40] = (
    "IcelandEP1_S40_WentUnderground", "#D72828", 6.2,
'''        Text.set_default(font="Poppins")
        plain = Rectangle(width=12, height=3, fill_color="#557755", fill_opacity=0.7, stroke_width=0).move_to([0,-0.5,0])
        self.play(FadeIn(plain), run_time=1.5)
        self.play(plain.animate.stretch(1.02, 1), run_time=1.0)
        self.play(plain.animate.stretch(1/1.02, 1), run_time=1.0)
        didnt = Text("It didn\'t disappear.", font_size=32, color="#C87941").move_to([0,0.8,0])
        under = Text("It went underground.", font="Poppins", weight=BOLD, font_size=36, color=WHITE).move_to([0,0.2,0])
        self.play(FadeIn(didnt), run_time=0.8)
        self.play(FadeIn(under), run_time=0.8)
        T = 5.1
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[41] = (
    "IcelandEP1_S41_RapidMontage", "#EEF4FC", 21.1,
'''        Text.set_default(font="Poppins")
        segments = [
            ("Althing abolished",                   "#003897", 1.5),
            ("Danish rule begins\\n1397",            "#555555", 1.5),
            ("Plague and famine\\nPopulation halved","#D72828", 1.5),
            ("Laki eruption\\n1783",                 "#8B1010", 2.0),
            ("Althing restored\\n1845",              "#003897", 1.5),
            ("Independence\\n1944",                  "#003897", 2.0),
            ("2008 crisis\\nThey chose differently", "#003C9E", 2.0),
        ]
        for label, bg_col, duration in segments:
            self.camera.background_color = bg_col
            overlay = Rectangle(width=14.22, height=8.0, fill_color=bg_col, fill_opacity=1, stroke_width=0)
            txt = Text(label, font_size=36, color=WHITE, line_spacing=1.2).move_to([0,0,0])
            self.play(FadeIn(overlay), FadeIn(txt), run_time=0.3)
            self.wait(duration - 0.6)
            self.play(FadeOut(overlay), FadeOut(txt), run_time=0.3)
        self.camera.background_color = "#EEF4FC"
        T = 13.0
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[42] = (
    "IcelandEP1_S42_OriginalInstinct", "#EEF4FC", 19.9,
'''        Text.set_default(font="Poppins")
        modern_map = load_map("iceland_modern")
        self.play(FadeIn(modern_map), run_time=2.0)
        ingolfr_sm = load_character("ingolfr_arnarson", width=1.2).move_to([-0.5, 0, 0])
        self.play(FadeIn(ingolfr_sm), run_time=0.8)
        instinct_txt = Text("That original instinct.", font="Poppins", weight=BOLD,
                            font_size=36, color="#C87941").move_to([0,0.8,0])
        self.play(FadeIn(instinct_txt), run_time=1.0)
        t_sail  = Text("Sail into the unknown.",  font_size=28, color="#5A4A3A").move_to([0, 0.0,0])
        self.play(FadeIn(t_sail), run_time=0.8)
        self.play(FadeOut(t_sail), run_time=0.3)
        t_rules = Text("Build your own rules.",   font_size=28, color="#5A4A3A").move_to([0,-0.7,0])
        self.play(FadeIn(t_rules), run_time=0.8)
        self.play(FadeOut(t_rules), run_time=0.3)
        t_hold  = Text("Hold the line.",           font_size=28, color="#5A4A3A").move_to([0,-0.7,0])
        self.play(FadeIn(t_hold), run_time=0.8)
        T = 6.2
        self.wait(max(self.VD - T, 0) + 1.5)
''')

SCENES[43] = (
    "IcelandEP1_S43_FoundationWasLaid", "#003897", 11.6,
'''        Text.set_default(font="Poppins")
        atl_map = load_map("north_atlantic_dark")
        atl_map.set_opacity(0.8)
        self.play(FadeIn(atl_map), run_time=1.0)
        oct_lbl = Text("October 2008.", font_size=36, color="#FF4444").move_to([0,0.8,0])
        self.play(FadeIn(oct_lbl), run_time=0.8)
        self.play(FadeOut(oct_lbl), run_time=0.3)
        foundation = Text("The foundation was already there.", font="Poppins", weight=BOLD,
                          font_size=34, color="#C87941").move_to([0,0.5,0])
        since_930  = Text("It had been there since 930.", font_size=28, color="#888888").move_to([0,-0.1,0])
        self.play(FadeIn(foundation), run_time=1.0)
        self.play(FadeIn(since_930),  run_time=0.8)
        T = 3.6
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
''')

SCENES[44] = (
    "IcelandEP1_S44_EndCard", "#000000", 17.4,
'''        Text.set_default(font="Poppins")
        channel_txt = Text("History in Minutes", font="Poppins", weight=BOLD,
                           font_size=42, color=WHITE).move_to([0,1.5,0])
        self.play(FadeIn(channel_txt), run_time=1.0)
        next_ep = Text("Part 2: The World Takes Notice", font_size=36, color="#FF812E").move_to([0,0.3,0])
        self.play(FadeIn(next_ep), run_time=1.0)
        sub_btn = RoundedRectangle(corner_radius=0.2, width=3.5, height=0.8,
                                   fill_color="#CC0000", fill_opacity=1, stroke_width=0).move_to([0,-1.0,0])
        sub_txt = Text("Subscribe", font="Poppins", weight=BOLD, font_size=28, color=WHITE).move_to(sub_btn)
        self.play(FadeIn(sub_btn), FadeIn(sub_txt), run_time=0.8)
        self.wait(15.1)
''')

# ---- write files ----
FILE_TEMPLATE = '''"""Iceland EP1 - Scene {num:02d}: {classname}
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_{num:02d}.py {classname}
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from helpers import (load_map, load_character, make_subscribe_cta,
                     AMBER, DARK_TXT, WARM_TXT, GREY_TXT, MID_TXT,
                     GREEN_ACC, DARK_RED, RED_ACC, BLUE_ACC, PURPLE_TXT, ORANGE_ACC,
                     CORNER_TL, BODY_LEFT, BODY_RIGHT, BODY_CTR,
                     ICELAND_BLUE, ICELAND_WHITE, ICELAND_RED)


class {classname}(Scene):
    VD = {vd}  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "{bg}"
{body}
'''

for num in range(1, 45):
    classname, bg, vd, body = SCENES[num]
    content = FILE_TEMPLATE.format(
        num=num, classname=classname, vd=vd, bg=bg, body=body
    )
    fname = SCENES_DIR / f"scene_{num:02d}.py"
    fname.write_text(content, encoding="utf-8")

print(f"Wrote 44 scene files + helpers.py to {SCENES_DIR}")
print("Done.")
