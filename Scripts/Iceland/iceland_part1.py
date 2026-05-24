"""
iceland_part1.py — Sections A–D: Monks + Ingólfr + Migration + Althing (~360s)
Visual script mapped to VO Part 1 content (post cold open).
"""
import random
from manim import *
from pathlib import Path

WHITE_BG = "#FFFFFF"
DARK     = "#1A1A1A"
RED      = "#CC1B21"
AMBER    = "#D4821A"
BLUE     = "#1E5FA8"
GREEN    = "#2A7A3A"
GREY     = "#5A5A5A"
L_GREY   = "#BBBBBB"
SEA_DARK = "#0F2030"
STONE    = "#7A7060"
BROWN    = "#5A3A1A"
H_PAD = 1.5
V_PAD = 0.9

PROD  = Path("/Users/dishastark/Claude Projects/YouTube/History/Output/Iceland/production")
MAPS  = PROD / "assets" / "maps"
CHARS = PROD / "assets" / "characters"


def load_map(name, height=7.5):
    p = MAPS / f"{name}.png"
    if p.exists():
        img = ImageMobject(str(p))
        img.set_height(height)
        return img
    return None


def load_char(name, height=3.5):
    p = CHARS / f"{name}.png"
    if p.exists():
        img = ImageMobject(str(p))
        img.set_height(height)
        return img
    return None


def make_monk_geo(scale=1.0):
    head = Circle(radius=0.32*scale, fill_color="#C8956A", fill_opacity=1,
                  stroke_color=DARK, stroke_width=1.5)
    robe = Triangle(fill_color=BROWN, fill_opacity=1, stroke_color=DARK,
                    stroke_width=1.5).scale(0.9*scale).next_to(head, DOWN, buff=0.04*scale)
    bald = Circle(radius=0.13*scale, fill_color="#8B6A4A", fill_opacity=0.7,
                  stroke_width=0).move_to(head.get_center() + UP*0.10*scale)
    return VGroup(robe, head, bald)


def make_cross(scale=1.0):
    v = Rectangle(width=0.12*scale, height=0.55*scale,
                  fill_color="#6B4A20", fill_opacity=1, stroke_width=0)
    h = Rectangle(width=0.38*scale, height=0.10*scale,
                  fill_color="#6B4A20", fill_opacity=1, stroke_width=0
                  ).move_to(v.get_center() + UP*0.12*scale)
    return VGroup(v, h)


def make_longship(scale=1.0):
    hull = Polygon(
        [-1.4*scale, 0, 0], [-1.0*scale, -0.35*scale, 0],
        [ 1.0*scale, -0.35*scale, 0], [ 1.4*scale, 0, 0],
        [ 0.8*scale,  0.08*scale, 0], [-0.8*scale,  0.08*scale, 0],
        fill_color="#3A2A1A", fill_opacity=1, stroke_width=0,
    )
    mast = Line(UP*1.2*scale, DOWN*0.05*scale, stroke_color=DARK, stroke_width=3*scale)
    sail = Polygon(
        [0, 1.15*scale, 0], [0.65*scale, 0.3*scale, 0], [-0.65*scale, 0.3*scale, 0],
        fill_color="#D4B88A", fill_opacity=0.9, stroke_width=0,
    )
    return VGroup(hull, mast, sail)


def make_steam(n=3, scale=1.0):
    wisps = []
    for i in range(n):
        x = (i - n//2) * 0.3 * scale
        path = VMobject()
        path.set_points_smoothly([
            [x, 0, 0], [x+0.15*scale, 0.3*scale, 0],
            [x-0.1*scale, 0.6*scale, 0], [x+0.05*scale, 0.9*scale, 0],
        ])
        path.set_stroke(color=GREY, width=2.5, opacity=0.5)
        wisps.append(path)
    return VGroup(*wisps)


def make_iceland_outline():
    pts = [
        [-1.8, 0.8, 0], [-2.1, 0.3, 0], [-2.4, -0.1, 0], [-2.2, -0.5, 0],
        [-1.6, -0.9, 0], [-0.8, -1.1, 0], [0.2, -1.0, 0], [0.9, -0.7, 0],
        [1.6, -0.3, 0], [2.0,  0.3, 0], [1.8,  0.8, 0], [1.2,  1.0, 0],
        [0.4,  1.1, 0], [-0.4, 1.2, 0], [-1.0, 1.0, 0], [-1.5, 0.9, 0],
    ]
    return Polygon(*pts, fill_color="#D4C8A8", fill_opacity=0.7,
                   stroke_color=DARK, stroke_width=2)


def make_pillar(scale=1.0):
    shaft = Rectangle(width=0.22*scale, height=1.4*scale,
                      fill_color="#6B4A20", fill_opacity=1, stroke_width=0)
    cap   = Rectangle(width=0.34*scale, height=0.14*scale,
                      fill_color="#5A3A10", fill_opacity=1, stroke_width=0
                      ).next_to(shaft, UP, buff=0)
    base  = Rectangle(width=0.34*scale, height=0.14*scale,
                      fill_color="#5A3A10", fill_opacity=1, stroke_width=0
                      ).next_to(shaft, DOWN, buff=0)
    knots = VGroup(*[
        Line(LEFT*0.08*scale, RIGHT*0.08*scale,
             stroke_color=AMBER, stroke_width=1.5
             ).move_to(shaft.get_center() + UP*(i*0.28 - 0.28)*scale)
        for i in range(4)
    ])
    return VGroup(base, shaft, cap, knots)


def make_meditation_arcs(center, n=3, scale=1.0):
    """Concentric ripple circles expanding from a center point — meditation energy."""
    circles = []
    for i in range(n):
        r = 0.45*(i+1)*scale
        c = Circle(radius=r, stroke_color=AMBER,
                   stroke_width=max(1.0, 3.0-i),
                   fill_opacity=0)
        c.set_stroke(opacity=0.75 - i*0.22)
        c.move_to(center)
        circles.append(c)
    return VGroup(*circles)


class IcelandPart1(Scene):
    """Sections A–D: Monks + Ingólfr + Migration + Althing. ~360s total."""

    def construct(self):
        self.camera.background_color = WHITE_BG
        self._a1_year_800()
        self._a2_the_papar()
        self._a3_sailing_to_edge()
        self._a4_they_found_it()
        self._a5_solitary_existence()
        self._a6_norse_arrived()
        self._a7_monks_pack_up()
        self._a8_shared_instinct()
        self._b1_the_man()
        self._b2_harald_problem()
        self._b3_he_left()
        self._b4_pillars()
        self._b5_three_years()
        self._b6_reykjavik()
        self._b7_furniture()
        self._c1_numbers()
        self._c2_who_they_were()
        self._c3_why_they_came()
        self._c4_refuge()
        self._c5_built_government()
        self._d1_thingvellir()
        self._d2_no_king()
        self._d3_just_laws()
        self._d4_it_worked()

    # ── SECTION A ─────────────────────────────────────────────────────────────

    def _a1_year_800(self):
        self.camera.background_color = WHITE_BG
        iceland = load_map("iceland_overview", height=7.5)
        if iceland is None:
            iceland = make_iceland_outline().scale(2.5)
        self.add(iceland)
        year_lbl = Text("Year 800", font="Poppins", weight=LIGHT,
                        font_size=32, color=GREY).to_corner(UR, buff=V_PAD)
        self.play(FadeIn(year_lbl), run_time=0.8)
        no_one = Text("No one lives here yet.", font="Poppins", weight=LIGHT,
                      font_size=38, color=GREY).to_edge(DOWN, buff=V_PAD*1.5)
        self.play(FadeIn(no_one, shift=UP*0.15), run_time=0.8)
        self.wait(5.4)
        self.play(FadeOut(year_lbl), FadeOut(no_one), run_time=0.5)
        self.remove(iceland)

    def _a2_the_papar(self):
        self.camera.background_color = WHITE_BG
        monk = load_char("irish_monk_seated", height=3.8)
        if monk is None:
            monk = make_monk_geo(scale=1.0)
        monk.move_to(ORIGIN + RIGHT*0.3)

        cross = make_cross(scale=1.0)
        cross.move_to(monk.get_center() + LEFT*1.6 + DOWN*0.3)

        self.play(GrowFromCenter(monk), run_time=1.0)
        # Cross grows from its base upward
        cross.move_to(monk.get_center() + LEFT*1.6 + DOWN*0.3)
        self.play(GrowFromPoint(cross, cross.get_bottom()), run_time=0.8)

        # Meditation arcs — concentric ripple circles from forehead
        forehead = monk.get_center() + UP*0.55
        arcs = make_meditation_arcs(forehead, n=3, scale=0.9)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in arcs], lag_ratio=0.45),
            run_time=1.5,
        )

        lbl_title = Text("The Papar", font="Poppins", weight=BOLD,
                         font_size=36, color=DARK).to_edge(DOWN, buff=V_PAD+0.8)
        lbl_sub   = Text("Irish Christian hermits", font="Poppins", weight=LIGHT,
                         font_size=24, color=GREY).next_to(lbl_title, DOWN, buff=0.2)
        self.play(FadeIn(lbl_title, shift=UP*0.1),
                  FadeIn(lbl_sub, shift=UP*0.1), run_time=0.7)
        self.wait(10.5)
        self.play(
            FadeOut(monk), FadeOut(cross), FadeOut(arcs),
            FadeOut(lbl_title), FadeOut(lbl_sub), run_time=0.6,
        )

    def _a3_sailing_to_edge(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)

        ireland_pos = [3.0, -2.2, 0]
        iceland_pos = [-0.5, 0.6, 0]
        route = VMobject()
        route.set_points_smoothly([ireland_pos, [2.0, 0.5, 0], [0.8, 1.2, 0], iceland_pos])
        route.set_stroke(color=AMBER, width=2.5, opacity=0.8)

        b_hull = Polygon(
            [-0.35, 0, 0], [-0.25, -0.1, 0], [0.25, -0.1, 0], [0.35, 0, 0],
            [0.2, 0.04, 0], [-0.2, 0.04, 0],
            fill_color=BROWN, fill_opacity=1, stroke_width=0,
        )
        b_mast = Line([0, 0.3, 0], [0, -0.04, 0], stroke_color=DARK, stroke_width=2)
        b_sail = Triangle(fill_color="#D4B88A", fill_opacity=0.9,
                          stroke_width=0).scale(0.18).move_to([0, 0.18, 0])
        monk_boat = VGroup(b_hull, b_mast, b_sail)
        monk_boat.move_to(ireland_pos)

        quote = Text(
            "somewhere between the known world\nand the edge of it.",
            font="Poppins", weight=LIGHT, font_size=24, color=AMBER,
            slant=ITALIC, line_spacing=1.4,
        ).to_corner(UL, buff=V_PAD).shift(RIGHT*0.3+DOWN*0.4)

        self.play(Create(route), run_time=2.5)
        self.play(FadeIn(quote, shift=RIGHT*0.15), run_time=0.7)
        self.play(MoveAlongPath(monk_boat, route), run_time=4.5, rate_func=linear)
        land_dot = Dot(point=iceland_pos, radius=0.1, color=AMBER)
        self.play(GrowFromCenter(land_dot), run_time=0.4)
        self.wait(7.4)

        self.play(
            FadeOut(route), FadeOut(monk_boat), FadeOut(quote),
            FadeOut(land_dot), run_time=0.5,
        )
        if map_img:
            self.remove(map_img)

    def _a4_they_found_it(self):
        self.camera.background_color = WHITE_BG
        iceland = load_map("iceland_overview", height=7.5)
        if iceland is None:
            iceland = make_iceland_outline().scale(2.5)
        self.add(iceland)

        # Amber glow pulse over island
        pulse = Ellipse(width=4.2, height=2.4,
                        fill_color=AMBER, fill_opacity=0.0,
                        stroke_color=AMBER, stroke_width=0).move_to(ORIGIN)
        self.add(pulse)
        self.play(pulse.animate.set_fill(opacity=0.20).scale(1.05), run_time=0.9)
        self.play(pulse.animate.set_fill(opacity=0.0).scale(0.95), run_time=0.9)

        monk = load_char("irish_monk_seated", height=2.8)
        if monk is None:
            monk = make_monk_geo(scale=0.8)
        monk.move_to(LEFT*0.5 + DOWN*0.2)

        cross_sm = make_cross(scale=0.7).move_to(LEFT*1.6 + DOWN*0.5)
        steam_sm = make_steam(n=3, scale=0.6).move_to(
            monk.get_center() + DOWN*0.8)

        self.play(GrowFromCenter(monk),
                  GrowFromPoint(cross_sm, cross_sm.get_bottom()), run_time=0.7)
        self.play(Create(steam_sm), run_time=0.8)

        t1 = Text("They found Iceland.", font="Poppins", weight=SEMIBOLD,
                  font_size=44, color=DARK).to_edge(DOWN, buff=V_PAD+0.7)
        self.play(FadeIn(t1, shift=UP*0.1), run_time=0.5)
        self.wait(1.8)
        t2 = Text("They settled in.", font="Poppins", weight=SEMIBOLD,
                  font_size=44, color=AMBER).next_to(t1, DOWN, buff=0.22)
        self.play(FadeIn(t2, shift=UP*0.1), run_time=0.5)
        self.wait(4.8)

        self.play(
            FadeOut(t1), FadeOut(t2), FadeOut(monk), FadeOut(cross_sm),
            FadeOut(steam_sm), FadeOut(pulse), run_time=0.5,
        )
        self.remove(iceland)

    def _a5_solitary_existence(self):
        self.camera.background_color = WHITE_BG
        monk = load_char("irish_monk_seated", height=3.8)
        if monk is None:
            monk = make_monk_geo(scale=1.0)
        monk.move_to(ORIGIN)

        cross_sm = make_cross(scale=0.85).move_to(RIGHT*1.7 + DOWN*0.5)
        steam_sm = make_steam(n=3, scale=0.8).move_to(
            monk.get_center() + DOWN*0.9)
        bell = Rectangle(width=0.22, height=0.28, fill_color=AMBER,
                         fill_opacity=1, stroke_width=1, stroke_color=DARK
                         ).move_to(monk.get_center() + LEFT*1.0 + DOWN*0.9)

        self.play(FadeIn(monk), FadeIn(cross_sm), FadeIn(bell), run_time=0.7)
        self.play(Create(steam_sm), run_time=0.8)

        # Meditation arcs
        forehead = monk.get_center() + UP*0.6
        arcs = make_meditation_arcs(forehead, n=3, scale=0.9)
        self.play(LaggedStart(*[GrowFromCenter(a) for a in arcs], lag_ratio=0.4),
                  run_time=1.5)

        quote = Text("A perfectly good solitary existence.", font="Poppins",
                     weight=LIGHT, font_size=28, color=GREY, slant=ITALIC
                     ).to_edge(DOWN, buff=V_PAD*1.5)
        self.play(FadeIn(quote, shift=UP*0.1), run_time=0.6)
        self.wait(4.9)

        self.play(
            FadeOut(monk), FadeOut(cross_sm), FadeOut(steam_sm),
            FadeOut(bell), FadeOut(arcs), FadeOut(quote), run_time=0.5,
        )

    def _a6_norse_arrived(self):
        self.camera.background_color = WHITE_BG
        monk = load_char("irish_monk_seated", height=3.0)
        if monk is None:
            monk = make_monk_geo(scale=0.85)
        monk.move_to(LEFT*2.5 + DOWN*0.2)

        forehead = monk.get_center() + UP*0.5
        arcs = make_meditation_arcs(forehead, n=3, scale=0.8)
        self.add(monk, arcs)
        self.wait(0.5)

        sea_bg = Rectangle(
            width=config.frame_width, height=config.frame_height,
            fill_color=SEA_DARK, fill_opacity=0, stroke_width=0,
        )
        self.add(sea_bg)
        ship = make_longship(scale=1.1)
        ship.move_to(RIGHT*9.0)
        self.add(ship)

        self.play(
            sea_bg.animate.set_fill(opacity=0.6),
            ship.animate.move_to(RIGHT*2.2),
            run_time=1.0,
        )
        self.play(*[a.animate.set_stroke(opacity=0.0) for a in arcs], run_time=0.25)

        slam_text = Text("Then the Norse arrived.", font="Poppins", weight=BOLD,
                         font_size=48, color=RED).to_edge(DOWN, buff=V_PAD+0.3)
        slam_text.shift(RIGHT*14)
        self.add(slam_text)
        self.play(slam_text.animate.shift(LEFT*14), run_time=0.45)
        self.wait(3.8)

        self.play(
            FadeOut(monk), FadeOut(arcs), FadeOut(sea_bg),
            FadeOut(ship), FadeOut(slam_text), run_time=0.5,
        )
        self.camera.background_color = WHITE_BG

    def _a7_monks_pack_up(self):
        self.camera.background_color = WHITE_BG
        monk = load_char("irish_monk_packing", height=3.2)
        if monk is None:
            monk = make_monk_geo(scale=0.9)
        monk.move_to(LEFT*1.5)

        bell_icon  = Rectangle(width=0.3, height=0.38, fill_color=AMBER,
                               fill_opacity=1, stroke_width=1.5, stroke_color=DARK
                               ).move_to(LEFT*3.6 + UP*1.2)
        book_icon  = Rectangle(width=0.28, height=0.36, fill_color="#D4C8A8",
                               fill_opacity=1, stroke_width=1.5, stroke_color=DARK
                               ).move_to(LEFT*3.6 + UP*0.3)
        staff_icon = Line([0, 0.55, 0], [0, -0.55, 0],
                          stroke_color=BROWN, stroke_width=5
                          ).move_to(LEFT*3.6 + DOWN*0.6)

        bell_lbl  = Text("Bell",    font="Poppins", weight=LIGHT, font_size=18,
                         color=GREY).next_to(bell_icon,  RIGHT, buff=0.15)
        book_lbl  = Text("Book",    font="Poppins", weight=LIGHT, font_size=18,
                         color=GREY).next_to(book_icon,  RIGHT, buff=0.15)
        staff_lbl = Text("Crozier", font="Poppins", weight=LIGHT, font_size=18,
                         color=GREY).next_to(staff_icon, RIGHT, buff=0.15)

        ship = make_longship(scale=1.0)
        ship.move_to(RIGHT*9.0)

        self.play(FadeIn(monk), run_time=0.5)
        for icon, lbl in [(bell_icon, bell_lbl), (book_icon, book_lbl),
                          (staff_icon, staff_lbl)]:
            self.play(FadeIn(icon), FadeIn(lbl), run_time=0.35)
            self.play(icon.animate.move_to(monk.get_center()),
                      FadeOut(lbl), run_time=0.5)
            self.play(FadeOut(icon), run_time=0.2)

        items_text = Text("Their bells. Their books. Their croziers.",
                          font="Poppins", weight=LIGHT, font_size=28,
                          color=GREY, slant=ITALIC).to_edge(UP, buff=V_PAD+0.3)
        self.play(FadeIn(items_text), run_time=0.5)

        self.add(ship)
        self.play(
            monk.animate.shift(LEFT*10.0),
            ship.animate.move_to(RIGHT*2.0),
            run_time=3.5, rate_func=linear,
        )

        left_lbl = Text("They left.", font="Poppins", weight=BOLD,
                        font_size=52, color=DARK).to_edge(DOWN, buff=V_PAD+0.5)
        self.play(FadeIn(left_lbl, shift=UP*0.1), run_time=0.5)
        self.wait(2.8)

        self.play(FadeOut(ship), FadeOut(items_text), FadeOut(left_lbl), run_time=0.5)
        self.remove(monk)

    def _a8_shared_instinct(self):
        self.camera.background_color = WHITE_BG
        monk_l = load_char("irish_monk_seated", height=2.8)
        if monk_l is None:
            monk_l = make_monk_geo(scale=0.8)
        monk_l.move_to(LEFT*2.8 + UP*0.3)

        cross_l   = make_cross(scale=0.7).move_to(LEFT*4.1 + DOWN*0.4)
        peace_lbl = Text("For peace.", font="Poppins", weight=LIGHT,
                         font_size=26, color=GREY, slant=ITALIC
                         ).move_to(LEFT*3.0 + DOWN*1.6)
        divider   = Line(UP*3.5, DOWN*3.5, stroke_color=L_GREY, stroke_width=1.5)
        ship_r    = make_longship(scale=0.8).move_to(RIGHT*2.5 + UP*0.2)
        opin_lbl  = Text("To escape opinions.", font="Poppins", weight=LIGHT,
                         font_size=26, color=GREY, slant=ITALIC
                         ).move_to(RIGHT*2.5 + DOWN*1.6)

        self.play(
            FadeIn(monk_l), FadeIn(cross_l), FadeIn(peace_lbl),
            FadeIn(divider),
            FadeIn(ship_r), FadeIn(opin_lbl),
            run_time=0.8,
        )
        self.wait(2.0)

        self.play(
            FadeOut(monk_l), FadeOut(cross_l), FadeOut(peace_lbl),
            FadeOut(divider), FadeOut(ship_r), FadeOut(opin_lbl),
            run_time=0.5,
        )

        q1 = Text("to get away from people", font="Poppins", weight=BOLD,
                  font_size=46, color=AMBER, slant=ITALIC).move_to(UP*1.3)
        q2 = Text("with opinions", font="Poppins", weight=BOLD,
                  font_size=46, color=AMBER, slant=ITALIC).move_to(UP*0.2)
        q3 = Text("about how they should live.", font="Poppins", weight=BOLD,
                  font_size=46, color=AMBER, slant=ITALIC).move_to(DOWN*0.9)

        self.play(AddTextLetterByLetter(q1, time_per_char=0.05), run_time=2.5)
        self.play(AddTextLetterByLetter(q2, time_per_char=0.06), run_time=1.8)
        self.play(AddTextLetterByLetter(q3, time_per_char=0.05), run_time=2.8)
        self.wait(5.0)

        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), run_time=0.5)

    # ── SECTION B ─────────────────────────────────────────────────────────────

    def _b1_the_man(self):
        self.camera.background_color = WHITE_BG
        ingolfr = load_char("ingolfr_arnarson", height=3.5)
        if ingolfr is None:
            body = Rectangle(width=0.7, height=1.6, fill_color="#2A4A2A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.3, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=1).move_to(body.get_top()+UP*0.32)
            ingolfr = VGroup(body, head)

        ingolfr.move_to(RIGHT*8.0)
        self.add(ingolfr)
        self.play(ingolfr.animate.move_to(ORIGIN), run_time=0.9)

        name_lbl = Text("Ingólfr Arnarson", font="Poppins", weight=BOLD,
                        font_size=36, color=DARK).to_edge(DOWN, buff=V_PAD+0.9)
        year_lbl = Text("874 AD", font="Poppins", weight=SEMIBOLD,
                        font_size=28, color=AMBER).next_to(name_lbl, DOWN, buff=0.2)
        self.play(FadeIn(name_lbl, shift=UP*0.1),
                  FadeIn(year_lbl, shift=UP*0.1), run_time=0.6)
        self.wait(8.5)

        self.play(FadeOut(ingolfr), FadeOut(name_lbl), FadeOut(year_lbl), run_time=0.5)

    def _b2_harald_problem(self):
        self.camera.background_color = WHITE_BG
        harald = load_char("king_harold_fairhair", height=3.5)
        if harald is None:
            body  = Rectangle(width=0.9, height=1.8, fill_color="#003090",
                              fill_opacity=1, stroke_width=0)
            head  = Circle(radius=0.32, fill_color="#D4B86A", fill_opacity=1,
                          stroke_width=0).move_to(body.get_top()+UP*0.34)
            cpts  = [[-0.45,0,0],[-0.45,0.4,0],[-0.22,0.25,0],
                     [0,0.55,0],[0.22,0.25,0],[0.45,0.4,0],[0.45,0,0]]
            crown = Polygon(*cpts, fill_color=AMBER, fill_opacity=1,
                            stroke_width=0).move_to(head.get_top()+UP*0.1)
            hl = Rectangle(width=0.15, height=2.2, fill_color=AMBER,
                           fill_opacity=0.9, stroke_width=0
                           ).move_to(body.get_center()+LEFT*0.62+DOWN*0.3)
            hr = Rectangle(width=0.15, height=2.2, fill_color=AMBER,
                           fill_opacity=0.9, stroke_width=0
                           ).move_to(body.get_center()+RIGHT*0.62+DOWN*0.3)
            harald = VGroup(hl, hr, body, head, crown)
        harald.move_to(RIGHT*2.8)

        spc_bg  = Ellipse(width=3.2, height=1.0, fill_color=WHITE_BG,
                          fill_opacity=1, stroke_color=L_GREY, stroke_width=1.5
                          ).move_to(RIGHT*2.8+UP*2.8)
        spc_txt = Text('"my kingdom. mine."', font="Poppins", weight=LIGHT,
                       font_size=22, color=DARK, slant=ITALIC
                       ).move_to(spc_bg.get_center())

        ingolfr_sm = load_char("ingolfr_arnarson", height=3.5*0.45)
        if ingolfr_sm is None:
            body = Rectangle(width=0.35, height=0.72, fill_color="#2A4A2A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.15, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=0).move_to(body.get_top()+UP*0.16)
            ingolfr_sm = VGroup(body, head)
        ingolfr_sm.move_to(LEFT*4.0+DOWN*0.8)

        self.play(GrowFromCenter(harald), run_time=0.7)
        self.play(FadeIn(VGroup(spc_bg, spc_txt), scale=0.9), run_time=0.5)
        self.play(FadeIn(ingolfr_sm), run_time=0.5)
        self.wait(1.3)

        boundary = Circle(radius=0.5, stroke_color=RED, stroke_width=2.5,
                         fill_opacity=0).move_to(RIGHT*2.8)
        bnd_lbl  = Text("radius of royal opinions", font="Poppins", weight=LIGHT,
                        font_size=18, color=RED).to_edge(DOWN, buff=V_PAD)
        self.play(GrowFromCenter(boundary), FadeIn(bnd_lbl), run_time=0.5)
        self.play(boundary.animate.scale(7.0).set_stroke(opacity=0.2), run_time=4.0)
        self.play(ingolfr_sm.animate.shift(LEFT*0.8), run_time=0.8)
        self.wait(7.2)

        self.play(
            FadeOut(harald), FadeOut(spc_bg), FadeOut(spc_txt),
            FadeOut(ingolfr_sm), FadeOut(boundary), FadeOut(bnd_lbl),
            run_time=0.6,
        )

    def _b3_he_left(self):
        self.camera.background_color = WHITE_BG
        t1 = Text("Ingólfr didn't disagree politely.", font="Poppins",
                  weight=NORMAL, font_size=46, color=DARK).move_to(UP*0.5)
        t2 = Text("He left.", font="Poppins", weight=BOLD,
                  font_size=72, color=RED).move_to(DOWN*0.6)
        self.play(FadeIn(t1, shift=DOWN*0.1), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(t2, shift=DOWN*0.15), run_time=0.45)
        self.wait(4.6)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

    def _b4_pillars(self):
        self.camera.background_color = SEA_DARK
        sea_bg = Rectangle(
            width=config.frame_width, height=config.frame_height,
            fill_color=SEA_DARK, fill_opacity=1, stroke_width=0,
        )
        self.add(sea_bg)

        ingolfr = load_char("ingolfr_releasing_pillars", height=3.4)
        if ingolfr is None:
            body = Rectangle(width=0.7, height=1.6, fill_color="#1A3A1A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.30, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=0).move_to(body.get_top()+UP*0.32)
            arm  = Line([0.35,0,0],[0.85,-0.4,0], stroke_color="#C8956A", stroke_width=6)
            ingolfr = VGroup(body, head, arm)
        ingolfr.move_to(LEFT*1.8+UP*0.3)

        p1 = make_pillar(scale=0.9).move_to(RIGHT*0.3+UP*0.3)
        p2 = make_pillar(scale=0.9).move_to(RIGHT*1.4+UP*0.3)

        self.play(FadeIn(ingolfr, shift=DOWN*0.15), run_time=0.7)
        self.play(GrowFromCenter(p1), GrowFromCenter(p2), run_time=0.7)

        lbl_p = Text("high-seat pillars", font="Poppins", weight=SEMIBOLD,
                     font_size=26, color=AMBER).move_to(RIGHT*3.0+UP*1.2)
        lbl_s = Text("central to Norse household\nand religious life",
                     font="Poppins", weight=LIGHT, font_size=19, color=L_GREY,
                     line_spacing=1.3).next_to(lbl_p, DOWN, buff=0.2)
        self.play(FadeIn(lbl_p), FadeIn(lbl_s), run_time=0.6)
        self.wait(1.0)

        # Pillars tip and drift right (floating)
        self.play(
            p1.animate.rotate(PI/2).shift(DOWN*0.7),
            p2.animate.rotate(PI/2).shift(DOWN*0.7),
            run_time=0.7,
        )
        # Drift right over 8s — use Group for both
        watching = Text("(he is still watching)", font="Poppins", weight=LIGHT,
                        font_size=22, color=L_GREY, slant=ITALIC
                        ).next_to(ingolfr, DR, buff=0.2)
        self.play(FadeIn(watching), run_time=0.4)
        self.play(
            p1.animate.shift(RIGHT*6.0),
            p2.animate.shift(RIGHT*6.0),
            run_time=8.0, rate_func=linear,
        )
        self.wait(3.5)

        self.play(
            FadeOut(ingolfr), FadeOut(lbl_p), FadeOut(lbl_s),
            FadeOut(watching), run_time=0.5,
        )
        self.remove(p1, p2, sea_bg)
        self.camera.background_color = WHITE_BG

    def _b5_three_years(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        # Three path segments around Iceland's coast
        seg1_pts = [[-0.5,-0.9,0],[0.5,-1.1,0],[1.8,-0.5,0],[2.2,0.3,0]]
        seg2_pts = [[2.2,0.3,0],[1.5,1.1,0],[0.0,1.3,0],[-1.5,1.0,0]]
        seg3_pts = [[-1.5,1.0,0],[-2.1,0.1,0],[-1.6,-0.7,0],[-0.5,-0.9,0]]

        def make_seg(pts):
            s = VMobject()
            s.set_points_smoothly(pts)
            s.set_stroke(color=AMBER, width=2.5, opacity=0.75)
            return s

        ship = make_longship(scale=0.35).move_to(seg1_pts[0])
        year_lbl = Text("YEAR 1", font="Poppins", weight=SEMIBOLD,
                        font_size=28, color=AMBER).to_corner(UR, buff=V_PAD)
        self.play(FadeIn(year_lbl), run_time=0.3)

        for seg_pts, yr in [(seg1_pts, "YEAR 2"), (seg2_pts, "YEAR 3"),
                            (seg3_pts, None)]:
            seg = make_seg(seg_pts)
            self.play(Create(seg), run_time=0.8)
            self.play(MoveAlongPath(ship, seg), run_time=3.0, rate_func=linear)
            if yr:
                new_lbl = Text(yr, font="Poppins", weight=SEMIBOLD,
                               font_size=28, color=AMBER).to_corner(UR, buff=V_PAD)
                self.play(Transform(year_lbl, new_lbl), run_time=0.35)

        watching = Text("(he is still watching)", font="Poppins", weight=LIGHT,
                        font_size=22, color=L_GREY, slant=ITALIC
                        ).to_edge(DOWN, buff=V_PAD*1.5)
        pillar_dot = Dot(point=[-0.5,-0.9,0], radius=0.14, color=AMBER)
        found_lbl  = Text("pillars found.", font="Poppins", weight=LIGHT,
                          font_size=22, color=AMBER, slant=ITALIC
                          ).move_to([-0.5,-1.4,0])
        self.play(FadeIn(watching), GrowFromCenter(pillar_dot),
                  FadeIn(found_lbl), run_time=0.5)
        self.wait(4.5)

        self.play(
            FadeOut(year_lbl), FadeOut(watching), FadeOut(ship),
            FadeOut(pillar_dot), FadeOut(found_lbl), run_time=0.5,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _b6_reykjavik(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        sw = [-0.3, -1.1, 0]
        dot = Dot(point=sw, radius=0.14, color=AMBER)
        self.play(GrowFromCenter(dot), run_time=0.5)
        for _ in range(2):
            self.play(dot.animate.scale(2.2).set_fill(opacity=0.25), run_time=0.35)
            self.play(dot.animate.scale(0.45).set_fill(opacity=1.0), run_time=0.28)

        steam = make_steam(n=3, scale=0.7).move_to([sw[0], sw[1]+0.15, 0])
        self.play(Create(steam), run_time=0.9)

        city_name = Text("REYKJAVÍK", font="Poppins", weight=BOLD,
                         font_size=52, color=AMBER).move_to(RIGHT*2.0+UP*0.8)
        city_sub  = Text("Smoky Bay", font="Poppins", weight=LIGHT,
                         font_size=28, color=GREY, slant=ITALIC
                         ).next_to(city_name, DOWN, buff=0.2)
        self.play(GrowFromCenter(city_name), run_time=0.5)
        self.play(FadeIn(city_sub, shift=UP*0.1), run_time=0.4)

        houses = VGroup(*[
            VGroup(
                Rectangle(width=0.3, height=0.24, fill_color=STONE,
                         fill_opacity=1, stroke_width=0),
                Triangle(fill_color=BROWN, fill_opacity=1,
                        stroke_width=0).scale(0.15).shift(UP*0.19),
            ).move_to([sw[0]+(i-1)*0.44, sw[1]+0.24, 0])
            for i in range(3)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(h) for h in houses], lag_ratio=0.3),
            run_time=0.8,
        )
        self.wait(7.0)

        self.play(
            FadeOut(dot), FadeOut(steam), FadeOut(city_name),
            FadeOut(city_sub), FadeOut(houses), run_time=0.6,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _b7_furniture(self):
        self.camera.background_color = WHITE_BG
        entries = [
            ("Iceland's capital:", GREY, LIGHT, 28),
            ("REYKJAVÍK", AMBER, BOLD, 56),
            ("Selected by: furniture delivery logistics.", GREY, LIGHT, 24),
            ("Est. 874 AD  ·  still going.", L_GREY, LIGHT, 22),
        ]
        mobs, y = [], 1.8
        for txt, col, wt, sz in entries:
            t = Text(txt, font="Poppins", weight=wt, font_size=sz, color=col)
            t.move_to(UP*y)
            mobs.append(t)
            y -= 0.78 if sz > 30 else 0.62

        for m in mobs:
            self.play(FadeIn(m, shift=DOWN*0.12), run_time=0.45)
            self.wait(0.28)
        self.wait(5.5)
        self.play(*[FadeOut(m) for m in mobs], run_time=0.5)

    # ── SECTION C ─────────────────────────────────────────────────────────────

    def _c1_numbers(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        random.seed(42)
        positions = [
            [random.uniform(-1.7, 1.7), random.uniform(-0.85, 0.6), 0]
            for _ in range(30)
        ]
        dots = VGroup(*[
            Dot(point=p, radius=0.08, color=AMBER, fill_opacity=0.85)
            for p in positions
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.06),
            run_time=4.0,
        )

        bar  = Line(LEFT*4.5+DOWN*3.0, RIGHT*4.5+DOWN*3.0,
                    stroke_color=DARK, stroke_width=2)
        l874 = Text("874 AD", font="Poppins", weight=LIGHT, font_size=20,
                    color=DARK).next_to(bar.get_start(), UP, buff=0.15)
        l930 = Text("930 AD", font="Poppins", weight=LIGHT, font_size=20,
                    color=DARK).next_to(bar.get_end(), UP, buff=0.15)
        cnt  = Text("8,000 – 20,000 settlers", font="Poppins", weight=BOLD,
                    font_size=32, color=AMBER).to_edge(DOWN, buff=V_PAD*0.4)

        self.play(Create(bar), FadeIn(l874), FadeIn(l930), run_time=0.6)
        self.play(FadeIn(cnt, shift=UP*0.1), run_time=0.5)
        self.wait(7.0)

        self.play(
            FadeOut(dots), FadeOut(bar), FadeOut(l874),
            FadeOut(l930), FadeOut(cnt), run_time=0.6,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _c2_who_they_were(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)

        iceland_pt = [-0.5, 0.6, 0]
        norway_pt  = [3.0, 1.8, 0]
        britain_pt = [1.6, -1.2, 0]
        ireland_pt = [0.3, -2.0, 0]

        target = Dot(point=iceland_pt, radius=0.12, color=RED)
        self.add(target)

        arr_nor = Arrow(norway_pt, iceland_pt, buff=0.15,
                       stroke_color=AMBER, stroke_width=4.5,
                       max_tip_length_to_length_ratio=0.08)
        arr_bri = Arrow(britain_pt, iceland_pt, buff=0.15,
                       stroke_color=BLUE, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.08)
        arr_ire = Arrow(ireland_pt, iceland_pt, buff=0.15,
                       stroke_color=GREEN, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.08)

        l_nor = Text("Norway (most)", font="Poppins", weight=SEMIBOLD,
                     font_size=20, color=AMBER).move_to([3.8,2.2,0])
        l_bri = Text("Britain",       font="Poppins", weight=LIGHT,
                     font_size=18, color=BLUE).move_to([2.5,-1.6,0])
        l_ire = Text("Ireland",       font="Poppins", weight=LIGHT,
                     font_size=18, color=GREEN).move_to([0.7,-2.6,0])

        self.play(Create(arr_nor), FadeIn(l_nor), run_time=1.0)
        self.play(Create(arr_bri), FadeIn(l_bri),
                  Create(arr_ire), FadeIn(l_ire), run_time=1.0)
        self.wait(3.0)

        dna = Text("Their DNA is still visible in Icelanders today.",
                   font="Poppins", weight=LIGHT, font_size=24,
                   color=GREY, slant=ITALIC).to_edge(DOWN, buff=V_PAD*0.8)
        self.play(FadeIn(dna, shift=UP*0.1), run_time=0.7)
        self.wait(11.0)

        self.play(
            FadeOut(arr_nor), FadeOut(arr_bri), FadeOut(arr_ire),
            FadeOut(l_nor), FadeOut(l_bri), FadeOut(l_ire),
            FadeOut(target), FadeOut(dna), run_time=0.6,
        )
        if map_img:
            self.remove(map_img)

    def _c3_why_they_came(self):
        self.camera.background_color = WHITE_BG
        r1 = Text("Norway was overcrowded.", font="Poppins", weight=NORMAL,
                  font_size=40, color=GREY).move_to(UP*1.8)
        r2 = Text("Harald was king.", font="Poppins", weight=NORMAL,
                  font_size=40, color=GREY).move_to(UP*0.9)
        r3a = Text("Some people would sail into a volcano",
                   font="Poppins", weight=BOLD, font_size=40, color=AMBER
                   ).move_to(DOWN*0.1)
        r3b = Text("before submitting to a monarch.",
                   font="Poppins", weight=BOLD, font_size=40, color=AMBER
                   ).move_to(DOWN*1.0)

        volcano = Triangle(fill_color="#5A3A1A", fill_opacity=1,
                          stroke_width=0).scale(0.5).move_to(RIGHT*1.2+DOWN*2.2)
        smoke1  = Line([1.0,-1.72,0],[0.75,-1.2,0],
                       stroke_color=GREY, stroke_width=3, stroke_opacity=0.7)
        smoke2  = Line([1.2,-1.72,0],[1.45,-1.2,0],
                       stroke_color=GREY, stroke_width=3, stroke_opacity=0.7)
        figure  = Triangle(fill_color=DARK, fill_opacity=1,
                           stroke_width=0).scale(0.14).move_to(LEFT*1.2+DOWN*2.2)

        self.play(FadeIn(r1, shift=DOWN*0.12), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(r2, shift=DOWN*0.12), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(r3a, shift=DOWN*0.10), FadeIn(r3b, shift=DOWN*0.10),
                  run_time=0.7)
        self.play(FadeIn(volcano), FadeIn(smoke1), FadeIn(smoke2),
                  FadeIn(figure), run_time=0.5)
        self.play(figure.animate.move_to(RIGHT*0.8+DOWN*2.2),
                  run_time=2.0, rate_func=linear)
        self.wait(13.0)

        self.play(
            FadeOut(r1), FadeOut(r2), FadeOut(r3a), FadeOut(r3b),
            FadeOut(volcano), FadeOut(smoke1), FadeOut(smoke2),
            FadeOut(figure), run_time=0.5,
        )

    def _c4_refuge(self):
        self.camera.background_color = WHITE_BG
        iceland_shape = make_iceland_outline().scale(2.5)
        iceland_shape.set_fill(color=AMBER, opacity=0.30)
        iceland_shape.set_stroke(color=AMBER, width=2)

        sub_lbl = Text("From its very first days", font="Poppins", weight=LIGHT,
                       font_size=26, color=GREY).to_edge(UP, buff=V_PAD+0.5)
        big_lbl = Text("A refuge.", font="Poppins", weight=BOLD,
                       font_size=72, color=DARK).move_to(DOWN*0.1)

        self.play(GrowFromCenter(iceland_shape), run_time=0.8)
        self.play(FadeIn(sub_lbl, shift=DOWN*0.1), run_time=0.5)
        self.play(GrowFromCenter(big_lbl), run_time=0.6)
        self.wait(7.6)

        self.play(FadeOut(iceland_shape), FadeOut(sub_lbl), FadeOut(big_lbl),
                  run_time=0.5)

    def _c5_built_government(self):
        self.camera.background_color = WHITE_BG
        t1 = Text("A refuge.", font="Poppins", weight=BOLD,
                  font_size=72, color=DARK).move_to(UP*0.8)
        t2 = Text("They built a government anyway.", font="Poppins", weight=BOLD,
                  font_size=42, color=RED).move_to(DOWN*0.5)
        self.play(FadeIn(t1), run_time=0.45)
        self.wait(0.5)
        self.play(FadeIn(t2, shift=DOWN*0.12), run_time=0.5)
        self.wait(5.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

    # ── SECTION D ─────────────────────────────────────────────────────────────

    def _d1_thingvellir(self):
        self.camera.background_color = WHITE_BG
        year_lbl = Text("930 AD", font="Poppins", weight=LIGHT,
                        font_size=32, color=GREY).to_corner(UR, buff=V_PAD)
        self.play(FadeIn(year_lbl), run_time=0.5)

        lp = Rectangle(width=3.8, height=5.0, fill_color="#C8B88A",
                       fill_opacity=1, stroke_color=DARK, stroke_width=2
                       ).move_to(LEFT*2.5)
        rp = Rectangle(width=3.8, height=5.0, fill_color="#C8B88A",
                       fill_opacity=1, stroke_color=DARK, stroke_width=2
                       ).move_to(RIGHT*2.5)
        lbl_na = Text("← North American\nPlate", font="Poppins", weight=LIGHT,
                      font_size=20, color=DARK, line_spacing=1.3
                      ).move_to(LEFT*3.0+UP*0.6)
        lbl_eu = Text("Eurasian\nPlate →", font="Poppins", weight=LIGHT,
                      font_size=20, color=DARK, line_spacing=1.3
                      ).move_to(RIGHT*3.0+UP*0.6)
        tv_lbl = Text("Þingvellir", font="Poppins", weight=SEMIBOLD,
                      font_size=28, color=AMBER).move_to(UP*1.5)

        self.play(FadeIn(lp), FadeIn(rp), run_time=0.7)
        self.play(FadeIn(lbl_na), FadeIn(lbl_eu), run_time=0.5)
        self.play(
            lp.animate.shift(LEFT*0.9), lbl_na.animate.shift(LEFT*0.9),
            rp.animate.shift(RIGHT*0.9), lbl_eu.animate.shift(RIGHT*0.9),
            run_time=4.0, rate_func=linear,
        )
        self.play(FadeIn(tv_lbl, shift=DOWN*0.1), run_time=0.5)

        quote = Text(
            '"as if the land itself was making a point about freedom."',
            font="Poppins", weight=LIGHT, font_size=22, color=AMBER, slant=ITALIC,
        ).to_edge(DOWN, buff=V_PAD*0.8)
        self.play(FadeIn(quote, shift=UP*0.1), run_time=0.6)
        self.wait(11.5)

        self.play(
            FadeOut(lp), FadeOut(rp), FadeOut(lbl_na), FadeOut(lbl_eu),
            FadeOut(tv_lbl), FadeOut(quote), FadeOut(year_lbl), run_time=0.6,
        )

    def _d2_no_king(self):
        self.camera.background_color = WHITE_BG
        # 36 chieftain icons in a wide arc
        figures = VGroup()
        n = 36
        for i in range(n):
            frac = i / (n - 1)
            x = (frac - 0.5) * 12.0
            y = -2.2 + 0.8 * (1 - (2*frac - 1)**2)
            fig = VGroup(
                Circle(radius=0.11, fill_color="#C8956A", fill_opacity=1,
                      stroke_width=0),
                Rectangle(width=0.15, height=0.28, fill_color=STONE,
                         fill_opacity=1, stroke_width=0).shift(DOWN*0.22),
            ).move_to([x, y, 0])
            figures.add(fig)

        self.play(
            LaggedStart(*[GrowFromCenter(f) for f in figures], lag_ratio=0.04),
            run_time=2.5,
        )
        self.wait(1.0)

        # Flash background + text slams
        flash = Rectangle(
            width=config.frame_width, height=config.frame_height,
            fill_color=RED, fill_opacity=0, stroke_width=0,
        )
        self.add(flash)
        texts  = [
            Text("No king.",         font="Poppins", weight=BOLD, font_size=52, color=RED).move_to(UP*2.0),
            Text("No standing army.",font="Poppins", weight=BOLD, font_size=52, color=RED).move_to(UP*0.9),
            Text("No central state.",font="Poppins", weight=BOLD, font_size=52, color=RED).move_to(DOWN*0.2),
        ]
        for t in texts:
            self.play(flash.animate.set_fill(opacity=0.07), run_time=0.08)
            self.play(flash.animate.set_fill(opacity=0.0),
                      FadeIn(t, shift=DOWN*0.08), run_time=0.35)
            self.wait(0.5)

        self.wait(13.0)
        self.play(FadeOut(figures), *[FadeOut(t) for t in texts],
                  FadeOut(flash), run_time=0.6)

    def _d3_just_laws(self):
        self.camera.background_color = WHITE_BG
        # Lawspeaker on rock
        ls_head = Circle(radius=0.28, fill_color="#C8956A", fill_opacity=1,
                        stroke_width=1, stroke_color=DARK)
        ls_body = Rectangle(width=0.55, height=1.2, fill_color=STONE,
                           fill_opacity=1, stroke_width=0).next_to(ls_head, DOWN, buff=0.05)
        ls_rock = Ellipse(width=1.0, height=0.3, fill_color="#8A7A6A",
                         fill_opacity=1, stroke_width=0
                         ).next_to(ls_body, DOWN, buff=0.0)
        lawspeaker = VGroup(ls_rock, ls_body, ls_head).move_to(UP*0.5)

        # Speech arcs from mouth
        mouth = ls_head.get_center() + RIGHT*0.22 + DOWN*0.08
        s_arcs = VGroup(*[
            Arc(radius=0.35*(i+1), start_angle=-PI*0.2, angle=PI*0.6,
                stroke_color=BLUE, stroke_width=max(1.0, 2.5-i),
                fill_opacity=0)
            .set_stroke(opacity=0.85-i*0.28)
            .move_arc_center_to(mouth)
            for i in range(3)
        ])

        self.play(FadeIn(lawspeaker), run_time=0.6)
        self.play(LaggedStart(*[Create(a) for a in s_arcs], lag_ratio=0.3),
                  run_time=1.0)

        facts = [
            ("Laws: spoken from memory.", DARK),
            ("Roads: none.",              DARK),
            ("Country: held together.",   AMBER),
        ]
        y_pos = [UP*1.8, UP*0.9, UP*0.0]
        fact_mobs = []
        for (txt, col), pos in zip(facts, y_pos):
            fm = Text(txt, font="Poppins", weight=SEMIBOLD,
                      font_size=30, color=col).move_to(RIGHT*2.5 + pos)
            fact_mobs.append(fm)
            self.play(FadeIn(fm, shift=LEFT*0.12), run_time=0.5)
            self.wait(0.35)

        self.wait(11.5)
        self.play(
            FadeOut(lawspeaker), FadeOut(s_arcs),
            *[FadeOut(f) for f in fact_mobs], run_time=0.6,
        )

    def _d4_it_worked(self):
        self.camera.background_color = WHITE_BG
        cols_data = [
            ("✓", "Deliberative", DARK,  False),
            ("✓", "Public",       DARK,  False),
            ("✓", "It worked.",   AMBER, True),
        ]
        x_pos = [-3.5, 0.0, 3.5]
        groups = []
        for (ck, lb, col, bold), x in zip(cols_data, x_pos):
            check = Text(ck, font="Poppins", weight=BOLD,
                        font_size=52, color=col).move_to([x, 0.6, 0])
            label = Text(lb, font="Poppins",
                        weight=BOLD if bold else NORMAL,
                        font_size=28, color=col).move_to([x, -0.3, 0])
            g = VGroup(check, label)
            if bold:
                uline = Line(
                    label.get_left()+DOWN*0.08, label.get_right()+DOWN*0.08,
                    stroke_color=col, stroke_width=2,
                )
                g.add(uline)
            groups.append(g)

        for g in groups:
            self.play(FadeIn(g, shift=UP*0.12), run_time=0.5)
            self.wait(0.28)

        self.wait(6.5)
        self.play(*[FadeOut(g) for g in groups], run_time=0.6)
