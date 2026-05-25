"""
iceland_part2.py — Sections E–H: Christianity + Erik + Leif + Sagas (~270s)
VO Part 2 content.
"""
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

PROD  = Path("C:/Users/parth.pandya/Projects/YouTube/Output/Iceland/Needed Final Files")
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


def make_iceland_outline():
    pts = [
        [-1.8, 0.8, 0], [-2.1, 0.3, 0], [-2.4, -0.1, 0], [-2.2, -0.5, 0],
        [-1.6, -0.9, 0], [-0.8, -1.1, 0], [0.2, -1.0, 0], [0.9, -0.7, 0],
        [1.6, -0.3, 0], [2.0,  0.3, 0], [1.8,  0.8, 0], [1.2,  1.0, 0],
        [0.4,  1.1, 0], [-0.4, 1.2, 0], [-1.0, 1.0, 0], [-1.5, 0.9, 0],
    ]
    return Polygon(*pts, fill_color="#D4C8A8", fill_opacity=0.7,
                   stroke_color=DARK, stroke_width=2)


def make_small_figure(color=STONE, scale=1.0):
    head = Circle(radius=0.11*scale, fill_color="#C8956A", fill_opacity=1,
                 stroke_width=0)
    body = Rectangle(width=0.15*scale, height=0.28*scale,
                    fill_color=color, fill_opacity=1, stroke_width=0
                    ).next_to(head, DOWN, buff=0.02*scale)
    return VGroup(head, body)


def make_snorri_geo(scale=1.0):
    """Scholar character: robe, head, round glasses, quill."""
    body  = Rectangle(width=0.75*scale, height=1.5*scale, fill_color="#2A2A4A",
                      fill_opacity=1, stroke_width=0)
    head  = Circle(radius=0.28*scale, fill_color="#C8956A", fill_opacity=1,
                  stroke_color=DARK, stroke_width=1).move_to(body.get_top()+UP*0.30*scale)
    # Round glasses
    gl1   = Circle(radius=0.09*scale, fill_opacity=0, stroke_color=DARK,
                   stroke_width=1.5).move_to(head.get_center()+LEFT*0.10*scale+UP*0.02*scale)
    gl2   = Circle(radius=0.09*scale, fill_opacity=0, stroke_color=DARK,
                   stroke_width=1.5).move_to(head.get_center()+RIGHT*0.10*scale+UP*0.02*scale)
    gl_br = Line(gl1.get_right(), gl2.get_left(), stroke_color=DARK, stroke_width=1.5)
    # Quill
    quill = Line([0.5*scale, 0.5*scale, 0], [0.2*scale, -0.3*scale, 0],
                 stroke_color=AMBER, stroke_width=3)
    return VGroup(body, head, gl1, gl2, gl_br, quill)


class IcelandPart2(Scene):
    """Sections E–H: Christianity Decision + Erik + Leif + Sagas. ~270s total."""

    def construct(self):
        self.camera.background_color = WHITE_BG
        self._e1_the_question()
        self._e2_half_and_half()
        self._e3_one_man_decides()
        self._e4_under_the_cloak()
        self._e5_the_verdict()
        self._e6_exemptions()
        self._f1_most_famous_export()
        self._f2_exiled_twice()
        self._f3_sailed_west()
        self._f4_greenland()
        self._g1_his_son()
        self._g2_the_continent()
        self._g3_five_hundred_years()
        self._g4_filed_no_paperwork()
        self._h1_iceland_was_writing()
        self._h2_the_three_things()
        self._h3_snorri()
        self._h4_thor_odin()
        self._h5_welcome_marvel()
        self._h6_the_pivot()

    # ── SECTION E ─────────────────────────────────────────────────────────────

    def _e1_the_question(self):
        self.camera.background_color = WHITE_BG
        year_lbl = Text("1000 AD", font="Poppins", weight=LIGHT,
                        font_size=32, color=GREY).to_corner(UR, buff=V_PAD)
        self.play(FadeIn(year_lbl), run_time=0.5)

        cross = make_cross(scale=1.2).move_to(LEFT*2.5)
        # Norse hammer — geometric
        h_head = Rectangle(width=0.7, height=0.55, fill_color=STONE,
                           fill_opacity=1, stroke_width=0).move_to(RIGHT*2.5+UP*0.05)
        h_haft = Rectangle(width=0.15, height=1.0, fill_color=BROWN,
                           fill_opacity=1, stroke_width=0
                           ).move_to(RIGHT*2.5+DOWN*0.75)
        hammer = VGroup(h_head, h_haft)

        self.play(cross.animate.move_to(LEFT*9), run_time=0.01)
        self.remove(cross)
        cross.move_to(LEFT*9)
        self.add(cross)
        self.play(
            cross.animate.move_to(LEFT*2.5),
            hammer.animate.move_to(RIGHT*2.5),
            run_time=1.2,
        )

        question = Text("Christianity or paganism?", font="Poppins", weight=BOLD,
                        font_size=42, color=DARK).to_edge(DOWN, buff=V_PAD+0.6)
        self.play(FadeIn(question, shift=UP*0.12), run_time=0.6)
        self.wait(9.7)

        self.play(FadeOut(cross), FadeOut(hammer), FadeOut(question),
                  FadeOut(year_lbl), run_time=0.5)

    def _e2_half_and_half(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        # Left half overlay (BLUE = Christian) and right half (AMBER = Norse)
        lh = Rectangle(width=config.frame_width/2, height=config.frame_height,
                       fill_color=BLUE, fill_opacity=0.28, stroke_width=0
                       ).move_to(LEFT*config.frame_width/4)
        rh = Rectangle(width=config.frame_width/2, height=config.frame_height,
                       fill_color=AMBER, fill_opacity=0.28, stroke_width=0
                       ).move_to(RIGHT*config.frame_width/4)
        divline = Line(UP*4.0, DOWN*4.0, stroke_color=DARK, stroke_width=2)

        self.play(FadeIn(lh), FadeIn(rh), Create(divline), run_time=0.8)

        t1 = Text("Half Christian. Half not.", font="Poppins", weight=SEMIBOLD,
                  font_size=36, color=DARK).to_edge(UP, buff=V_PAD+0.4)
        self.play(FadeIn(t1, shift=DOWN*0.1), run_time=0.6)
        self.wait(2.0)

        t2 = Text("Civil war: a real possibility.", font="Poppins", weight=BOLD,
                  font_size=40, color=RED).to_edge(DOWN, buff=V_PAD+0.5)
        self.play(FadeIn(t2, shift=UP*0.12), run_time=0.5)
        self.wait(5.5)

        self.play(FadeOut(lh), FadeOut(rh), FadeOut(divline),
                  FadeOut(t1), FadeOut(t2), run_time=0.5)
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _e3_one_man_decides(self):
        self.camera.background_color = WHITE_BG
        # Central figure: Þorgeir on rock
        th_head = Circle(radius=0.26, fill_color="#C8956A", fill_opacity=1,
                        stroke_width=1, stroke_color=DARK)
        th_body = Rectangle(width=0.5, height=1.1, fill_color=BROWN,
                           fill_opacity=1, stroke_width=0).next_to(th_head, DOWN, buff=0.05)
        th_rock = Ellipse(width=0.9, height=0.28, fill_color="#8A7A6A",
                         fill_opacity=1, stroke_width=0).next_to(th_body, DOWN, buff=0.0)
        thorgeir_center = VGroup(th_rock, th_body, th_head).move_to(ORIGIN)

        # 12 small figures converging from left and right
        left_figs  = VGroup(*[make_small_figure(BLUE, scale=0.7).move_to(
            LEFT*(4.5-i*0.3)+DOWN*(1.0-abs(i-3)*0.3)) for i in range(6)])
        right_figs = VGroup(*[make_small_figure(AMBER, scale=0.7).move_to(
            RIGHT*(4.5-i*0.3)+DOWN*(1.0-abs(i-3)*0.3)) for i in range(6)])

        self.play(FadeIn(left_figs), FadeIn(right_figs), run_time=0.6)
        self.play(
            left_figs.animate.shift(RIGHT*2.5),
            right_figs.animate.shift(LEFT*2.5),
            run_time=1.5,
        )
        self.play(GrowFromCenter(thorgeir_center), run_time=0.6)

        decision_t = Text("They let one man decide.", font="Poppins", weight=BOLD,
                          font_size=40, color=DARK).to_edge(UP, buff=V_PAD+0.4)
        name_t     = Text("Þorgeir Þorkelsson", font="Poppins", weight=SEMIBOLD,
                          font_size=28, color=AMBER).to_edge(DOWN, buff=V_PAD+0.7)
        sub_t      = Text("Lawspeaker  ·  1000 AD", font="Poppins", weight=LIGHT,
                          font_size=22, color=GREY).next_to(name_t, DOWN, buff=0.15)
        self.play(FadeIn(decision_t, shift=DOWN*0.1), run_time=0.6)
        self.play(FadeIn(name_t), FadeIn(sub_t), run_time=0.5)
        self.wait(4.5)

        self.play(
            FadeOut(left_figs), FadeOut(right_figs),
            FadeOut(thorgeir_center), FadeOut(decision_t),
            FadeOut(name_t), FadeOut(sub_t), run_time=0.5,
        )

    def _e4_under_the_cloak(self):
        self.camera.background_color = WHITE_BG
        thorgeir = load_char("thorgeir_under_cloak", height=4.0)
        if thorgeir is None:
            # Geometric: just a big fur-cloak blob with eyes
            cloak = Ellipse(width=2.8, height=3.5, fill_color="#6B4A20",
                           fill_opacity=1, stroke_color=DARK, stroke_width=2)
            eye_l = Ellipse(width=0.22, height=0.15, fill_color=DARK,
                           fill_opacity=1, stroke_width=0).move_to(LEFT*0.28+UP*0.4)
            eye_r = Ellipse(width=0.22, height=0.15, fill_color=DARK,
                           fill_opacity=1, stroke_width=0).move_to(RIGHT*0.28+UP*0.4)
            thorgeir = VGroup(cloak, eye_l, eye_r)
        thorgeir.move_to(ORIGIN)

        self.play(GrowFromCenter(thorgeir), run_time=1.0)

        # Day / night cycle icons
        sun  = Circle(radius=0.3, fill_color="#FFD700", fill_opacity=1,
                     stroke_width=0).move_to(RIGHT*5.5+UP*2.5)
        moon = Circle(radius=0.28, fill_color="#D0D0D0", fill_opacity=1,
                     stroke_width=0).move_to(RIGHT*5.5+UP*2.5)
        # Day arc
        day_arc = Arc(radius=1.2, start_angle=PI, angle=-PI,
                     stroke_color=AMBER, stroke_width=2, fill_opacity=0
                     ).move_arc_center_to(RIGHT*5.5+UP*1.5)

        self.play(FadeIn(sun), run_time=0.4)
        self.play(MoveAlongPath(sun, day_arc), run_time=2.0, rate_func=linear)
        self.play(FadeOut(sun), FadeIn(moon), run_time=0.4)
        night_arc = Arc(radius=1.2, start_angle=PI, angle=-PI,
                       stroke_color=BLUE, stroke_width=2, fill_opacity=0
                       ).move_arc_center_to(RIGHT*5.5+UP*1.5)
        self.play(MoveAlongPath(moon, night_arc), run_time=2.0, rate_func=linear)
        self.play(FadeOut(moon), run_time=0.3)

        day_t  = Text("A full day.", font="Poppins", weight=LIGHT,
                      font_size=32, color=GREY).to_edge(DOWN, buff=V_PAD+0.9)
        ngt_t  = Text("A full night.", font="Poppins", weight=LIGHT,
                      font_size=32, color=GREY).next_to(day_t, DOWN, buff=0.22)
        self.play(FadeIn(day_t, shift=UP*0.1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(ngt_t, shift=UP*0.1), run_time=0.5)
        self.wait(5.0)

        self.play(FadeOut(thorgeir), FadeOut(day_t), FadeOut(ngt_t),
                  FadeOut(day_arc), FadeOut(night_arc), run_time=0.5)

    def _e5_the_verdict(self):
        self.camera.background_color = WHITE_BG
        # Þorgeir standing — use speaking variant
        thorgeir = load_char("thorgeir_speaking", height=3.5)
        if thorgeir is None:
            th_head = Circle(radius=0.28, fill_color="#C8956A", fill_opacity=1,
                            stroke_width=1, stroke_color=DARK)
            th_body = Rectangle(width=0.55, height=1.3, fill_color=BROWN,
                               fill_opacity=1, stroke_width=0
                               ).next_to(th_head, DOWN, buff=0.05)
            thorgeir = VGroup(th_body, th_head)
        thorgeir.move_to(LEFT*2.5)

        # Cross rises behind
        cross = make_cross(scale=1.4)
        cross_start = cross.copy().move_to(RIGHT*1.5+DOWN*2.0)
        cross_end   = cross.copy().move_to(RIGHT*1.5+UP*0.2)

        self.play(GrowFromCenter(thorgeir), run_time=0.8)
        self.play(GrowFromPoint(cross_start, cross_start.get_bottom()), run_time=0.6)
        self.play(cross_start.animate.move_to(cross_end.get_center()), run_time=0.6)

        verdict = Text("Iceland would be Christian.", font="Poppins", weight=BOLD,
                       font_size=46, color=DARK).to_edge(DOWN, buff=V_PAD+0.6)
        self.play(FadeIn(verdict, shift=UP*0.12), run_time=0.6)
        self.wait(6.5)

        self.play(FadeOut(thorgeir), FadeOut(cross_start), FadeOut(verdict),
                  run_time=0.5)

    def _e6_exemptions(self):
        self.camera.background_color = WHITE_BG
        cross_sm = make_cross(scale=1.0).move_to(LEFT*3.5)
        self.play(GrowFromCenter(cross_sm), run_time=0.5)

        # Exemption list
        exemptions = [
            ("Horsemeat: still permitted",  "✓"),
            ("Infant exposure: still allowed", "✓"),
            ("Faith: adopted",              "✓  (on Icelandic terms)"),
        ]
        mobs = []
        y = 1.5
        for txt, chk in exemptions:
            line = Text(f"{chk}  {txt}", font="Poppins", weight=LIGHT,
                       font_size=28, color=DARK).move_to(RIGHT*0.8+UP*y)
            mobs.append(line)
            self.play(FadeIn(line, shift=LEFT*0.15), run_time=0.5)
            self.wait(0.4)
            y -= 0.85

        self.wait(1.5)
        horsemeat_t = Text('"Christianity came with a horsemeat exemption."',
                           font="Poppins", weight=LIGHT, font_size=26,
                           color=AMBER, slant=ITALIC
                           ).to_edge(DOWN, buff=V_PAD+0.7)
        self.play(FadeIn(horsemeat_t, shift=UP*0.1), run_time=0.6)
        self.wait(2.0)

        pragmatism_t = Text("Pragmatism dressed up as theology.", font="Poppins",
                            weight=LIGHT, font_size=24, color=GREY, slant=ITALIC
                            ).next_to(horsemeat_t, DOWN, buff=0.22)
        self.play(FadeIn(pragmatism_t, shift=UP*0.1), run_time=0.5)
        self.wait(12.0)

        self.play(
            FadeOut(cross_sm), *[FadeOut(m) for m in mobs],
            FadeOut(horsemeat_t), FadeOut(pragmatism_t), run_time=0.5,
        )

    # ── SECTION F ─────────────────────────────────────────────────────────────

    def _f1_most_famous_export(self):
        self.camera.background_color = WHITE_BG
        year_lbl = Text("982 AD", font="Poppins", weight=LIGHT,
                        font_size=32, color=GREY).to_corner(UR, buff=V_PAD)
        self.play(FadeIn(year_lbl), run_time=0.4)

        erik = load_char("erik_the_red", height=3.5)
        if erik is None:
            body = Rectangle(width=0.8, height=1.7, fill_color="#4A1A1A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.3, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=1).move_to(body.get_top()+UP*0.32)
            beard = Ellipse(width=0.5, height=0.6, fill_color=RED,
                           fill_opacity=0.9, stroke_width=0
                           ).move_to(head.get_center()+DOWN*0.22)
            erik = VGroup(body, head, beard)
        erik.move_to(RIGHT*1.5)

        t1 = Text("Iceland's most famous export:", font="Poppins", weight=LIGHT,
                  font_size=28, color=GREY).move_to(LEFT*1.5+UP*1.0)
        t2 = Text("A man too violent\neven for Iceland.", font="Poppins",
                  weight=BOLD, font_size=44, color=RED, line_spacing=1.3
                  ).move_to(LEFT*1.5+DOWN*0.3)

        self.play(GrowFromCenter(erik), run_time=0.7)
        self.play(FadeIn(t1, shift=DOWN*0.1), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(t2, shift=DOWN*0.12), run_time=0.5)
        self.wait(9.0)

        self.play(FadeOut(erik), FadeOut(t1), FadeOut(t2), FadeOut(year_lbl),
                  run_time=0.5)

    def _f2_exiled_twice(self):
        self.camera.background_color = WHITE_BG
        # Two EXILE stamps slamming down
        stamp1_bg = Rectangle(width=3.5, height=2.2, fill_color="#F5F0E8",
                              fill_opacity=1, stroke_color=DARK, stroke_width=2
                              ).move_to(LEFT*2.5+UP*0.5)
        stamp1_t  = Text("EXILE", font="Poppins", weight=BOLD,
                         font_size=56, color=RED
                         ).move_to(stamp1_bg.get_center())
        stamp1_lbl = Text("Norway", font="Poppins", weight=LIGHT,
                          font_size=22, color=GREY
                          ).next_to(stamp1_bg, DOWN, buff=0.2)
        stamp1 = VGroup(stamp1_bg, stamp1_t)
        stamp1.rotate(-12*DEGREES)

        stamp2_bg = Rectangle(width=3.5, height=2.2, fill_color="#F5F0E8",
                              fill_opacity=1, stroke_color=DARK, stroke_width=2
                              ).move_to(RIGHT*2.5+UP*0.5)
        stamp2_t  = Text("EXILE", font="Poppins", weight=BOLD,
                         font_size=56, color=RED
                         ).move_to(stamp2_bg.get_center())
        stamp2_lbl = Text("Iceland", font="Poppins", weight=LIGHT,
                          font_size=22, color=GREY
                          ).next_to(stamp2_bg, DOWN, buff=0.2)
        stamp2 = VGroup(stamp2_bg, stamp2_t)
        stamp2.rotate(8*DEGREES)

        # Stamps start high, slam down
        s1_start = stamp1.copy().shift(UP*5.0)
        s2_start = stamp2.copy().shift(UP*5.0)
        self.add(s1_start, s2_start)

        self.play(s1_start.animate.move_to(stamp1.get_center()), run_time=0.35)
        self.play(FadeIn(stamp1_lbl), run_time=0.3)
        self.wait(0.4)
        self.play(s2_start.animate.move_to(stamp2.get_center()), run_time=0.35)
        self.play(FadeIn(stamp2_lbl), run_time=0.3)
        self.wait(1.0)

        man_t = Text("Manslaughter × 2", font="Poppins", weight=BOLD,
                     font_size=38, color=DARK).to_edge(DOWN, buff=V_PAD+0.5)
        self.play(FadeIn(man_t, shift=UP*0.1), run_time=0.5)
        self.wait(8.5)

        self.play(
            FadeOut(s1_start), FadeOut(s2_start),
            FadeOut(stamp1_lbl), FadeOut(stamp2_lbl),
            FadeOut(man_t), run_time=0.5,
        )

    def _f3_sailed_west(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)

        # Ship at Iceland's west coast
        ship = make_longship(scale=0.5).move_to(LEFT*0.5+DOWN*0.5)
        self.add(ship)

        t1 = Text("Sensing a pattern in his reviews,", font="Poppins",
                  weight=LIGHT, font_size=26, color=GREY, slant=ITALIC
                  ).to_edge(UP, buff=V_PAD+0.5)
        t2 = Text("Erik sailed west.", font="Poppins", weight=BOLD,
                  font_size=46, color=DARK).to_edge(DOWN, buff=V_PAD+0.5)

        self.play(FadeIn(t1), run_time=0.5)

        # Ship sails off left edge, map expands west
        self.play(
            ship.animate.move_to(LEFT*8.5),
            run_time=2.2, rate_func=linear,
        )
        self.play(FadeIn(t2, shift=UP*0.12), run_time=0.5)

        # Expand map westward — arrow pointing west
        west_arrow = Arrow(LEFT*2.0, LEFT*5.5, stroke_color=AMBER,
                          stroke_width=3, max_tip_length_to_length_ratio=0.1)
        self.play(Create(west_arrow), run_time=0.6)
        self.wait(4.5)

        self.play(FadeOut(t1), FadeOut(t2), FadeOut(ship),
                  FadeOut(west_arrow), run_time=0.5)
        if map_img:
            self.remove(map_img)

    def _f4_greenland(self):
        self.camera.background_color = WHITE_BG
        # Iceland shape on right, Greenland on left — side-by-side comparison
        iceland_shape = Polygon(
            [-0.9, 0.4, 0], [-1.1, 0.15, 0], [-1.2, -0.05, 0], [-1.1, -0.25, 0],
            [-0.8, -0.45, 0], [-0.4, -0.55, 0], [0.1, -0.5, 0], [0.45, -0.35, 0],
            [0.8, -0.15, 0], [1.0, 0.15, 0], [0.9, 0.4, 0], [0.6, 0.5, 0],
            fill_color="#7ABF6A", fill_opacity=0.85, stroke_color=DARK, stroke_width=1.5
        ).scale(0.9).move_to(RIGHT*3.0)

        greenland_shape = Polygon(
            [-1.2, 2.0, 0], [-1.8, 1.2, 0], [-2.2, 0.2, 0], [-2.0, -0.8, 0],
            [-1.4, -1.6, 0], [-0.5, -2.0, 0], [0.5, -1.8, 0], [1.2, -1.0, 0],
            [1.6, 0.2, 0], [1.2, 1.2, 0], [0.5, 1.8, 0],
            fill_color="#A8C8E0", fill_opacity=0.5, stroke_color=DARK, stroke_width=1.5
        ).scale(0.7).move_to(LEFT*2.8)

        ice_overlay = Polygon(
            [-1.2, 2.0, 0], [-1.8, 1.2, 0], [-2.2, 0.2, 0], [-2.0, -0.8, 0],
            [-1.4, -1.6, 0], [-0.5, -2.0, 0], [0.5, -1.8, 0], [1.2, -1.0, 0],
            [1.6, 0.2, 0], [1.2, 1.2, 0], [0.5, 1.8, 0],
            fill_color=WHITE, fill_opacity=0.65, stroke_width=0
        ).scale(0.7).move_to(LEFT*2.8)

        gl_label = Text("GREENLAND", font="Poppins", weight=BOLD,
                        font_size=36, color=GREEN).move_to(LEFT*2.8+UP*3.0)
        gl_sub   = Text("(mostly ice)", font="Poppins", weight=LIGHT,
                        font_size=20, color=GREY, slant=ITALIC
                        ).next_to(gl_label, DOWN, buff=0.15)
        ic_label = Text("Iceland", font="Poppins", weight=SEMIBOLD,
                        font_size=28, color=DARK).move_to(RIGHT*3.0+UP*1.8)
        ic_sub   = Text("(mostly green)", font="Poppins", weight=LIGHT,
                        font_size=18, color=GREY, slant=ITALIC
                        ).next_to(ic_label, DOWN, buff=0.12)

        self.play(FadeIn(iceland_shape), FadeIn(ic_label), FadeIn(ic_sub), run_time=0.7)
        self.wait(0.4)
        self.play(GrowFromCenter(greenland_shape), GrowFromCenter(ice_overlay),
                  run_time=0.7)
        self.play(FadeIn(gl_label), FadeIn(gl_sub), run_time=0.5)
        self.wait(2.5)

        named_t = Text("Named to attract settlers.", font="Poppins", weight=LIGHT,
                       font_size=26, color=AMBER, slant=ITALIC
                       ).to_edge(DOWN, buff=V_PAD+0.5)
        self.play(FadeIn(named_t, shift=UP*0.1), run_time=0.6)
        self.wait(10.0)

        self.play(
            FadeOut(iceland_shape), FadeOut(greenland_shape), FadeOut(ice_overlay),
            FadeOut(gl_label), FadeOut(gl_sub), FadeOut(ic_label),
            FadeOut(ic_sub), FadeOut(named_t), run_time=0.5,
        )

    # ── SECTION G ─────────────────────────────────────────────────────────────

    def _g1_his_son(self):
        self.camera.background_color = WHITE_BG
        erik_sm = load_char("erik_the_red", height=3.5*0.5)
        if erik_sm is None:
            body = Rectangle(width=0.4, height=0.85, fill_color="#4A1A1A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.15, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=0).move_to(body.get_top()+UP*0.17)
            erik_sm = VGroup(body, head)
        erik_sm.move_to(LEFT*2.5+DOWN*0.5)

        leif = load_char("leif_eriksson", height=3.5)
        if leif is None:
            body = Rectangle(width=0.75, height=1.65, fill_color="#2A3A5A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.29, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=1).move_to(body.get_top()+UP*0.31)
            leif = VGroup(body, head)
        leif.move_to(RIGHT*1.5)

        t1 = Text("Erik's son.", font="Poppins", weight=LIGHT,
                  font_size=28, color=GREY).to_edge(UP, buff=V_PAD+0.5)
        t2 = Text("Leif Eriksson.", font="Poppins", weight=BOLD,
                  font_size=36, color=DARK).next_to(t1, DOWN, buff=0.25)

        self.play(FadeIn(erik_sm), run_time=0.5)
        self.play(GrowFromCenter(leif), run_time=0.6)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.5)
        self.wait(4.5)

        self.play(FadeOut(erik_sm), FadeOut(leif), FadeOut(t1), FadeOut(t2),
                  run_time=0.5)

    def _g2_the_continent(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)

        # Greenland dot
        gl_dot = Dot(point=LEFT*2.0+UP*1.0, radius=0.12, color=GREEN)
        gl_lbl = Text("Greenland", font="Poppins", weight=LIGHT, font_size=20,
                      color=GREEN).next_to(gl_dot, UP, buff=0.15)
        self.add(gl_dot, gl_lbl)

        # North America landmass — simple polygon off left edge
        na_shape = Polygon(
            [-4.5, -2.5, 0], [-4.5, 2.0, 0], [-5.5, 2.5, 0], [-6.5, 1.5, 0],
            [-6.8, 0.0, 0], [-6.0, -1.5, 0], [-5.0, -2.5, 0],
            fill_color="#C8B88A", fill_opacity=0.7, stroke_color=DARK, stroke_width=1.5
        )
        na_lbl = Text("North America", font="Poppins", weight=LIGHT,
                      font_size=18, color=DARK).move_to([-5.5, 0.3, 0])

        # Ship sailing from Greenland to North America
        ship = make_longship(scale=0.45).move_to(LEFT*2.0+UP*1.0)
        route = VMobject()
        route.set_points_smoothly([[-2.0, 1.0, 0], [-3.2, 0.8, 0], [-4.0, 0.2, 0], [-4.5, -0.5, 0]])
        route.set_stroke(color=AMBER, width=2, opacity=0.7)

        self.play(Create(route), run_time=1.2)
        self.play(MoveAlongPath(ship, route), run_time=3.0, rate_func=linear)

        self.play(GrowFromCenter(na_shape), FadeIn(na_lbl), run_time=0.7)

        # Settlement dot
        settle_dot = Dot(point=[-4.5, -0.5, 0], radius=0.12, color=AMBER)
        settle_lbl = Text("Leifsbuðir", font="Poppins", weight=LIGHT,
                          font_size=20, color=AMBER).next_to(settle_dot, DR, buff=0.12)
        self.play(GrowFromCenter(settle_dot), FadeIn(settle_lbl), run_time=0.5)

        tree_ring = Text("1021 CE  ·  Tree-ring confirmed.", font="Poppins",
                         weight=LIGHT, font_size=20, color=GREY, slant=ITALIC
                         ).to_edge(DOWN, buff=V_PAD*0.7)
        self.play(FadeIn(tree_ring), run_time=0.5)
        self.wait(11.0)

        self.play(
            FadeOut(gl_dot), FadeOut(gl_lbl), FadeOut(na_shape), FadeOut(na_lbl),
            FadeOut(ship), FadeOut(route), FadeOut(settle_dot),
            FadeOut(settle_lbl), FadeOut(tree_ring), run_time=0.5,
        )
        if map_img:
            self.remove(map_img)

    def _g3_five_hundred_years(self):
        self.camera.background_color = WHITE_BG
        timeline = Line(LEFT*5.5+DOWN*0.5, RIGHT*5.5+DOWN*0.5,
                       stroke_color=DARK, stroke_width=2)

        dot_leif   = Dot(point=LEFT*5.5+DOWN*0.5, radius=0.12, color=AMBER)
        dot_col    = Dot(point=RIGHT*5.5+DOWN*0.5, radius=0.12, color=GREY)
        lbl_leif   = Text("1021 CE", font="Poppins", weight=SEMIBOLD,
                          font_size=22, color=AMBER).next_to(dot_leif, UP, buff=0.2)
        lbl_leif2  = Text("Leif Eriksson", font="Poppins", weight=LIGHT,
                          font_size=18, color=AMBER).next_to(lbl_leif, UP, buff=0.1)
        lbl_col    = Text("1492 CE", font="Poppins", weight=LIGHT,
                          font_size=22, color=GREY).next_to(dot_col, UP, buff=0.2)
        lbl_col2   = Text("Columbus", font="Poppins", weight=LIGHT,
                          font_size=18, color=GREY).next_to(lbl_col, UP, buff=0.1)
        gap_lbl    = Text("500 years", font="Poppins", weight=LIGHT,
                          font_size=22, color=L_GREY, slant=ITALIC
                          ).move_to(DOWN*0.5)

        self.play(Create(timeline), run_time=0.7)
        self.play(
            GrowFromCenter(dot_leif), FadeIn(lbl_leif), FadeIn(lbl_leif2),
            GrowFromCenter(dot_col), FadeIn(lbl_col), FadeIn(lbl_col2),
            run_time=0.6,
        )
        self.play(FadeIn(gap_lbl), run_time=0.4)

        big_t = Text("Five hundred years before Columbus.", font="Poppins",
                     weight=BOLD, font_size=40, color=AMBER).to_edge(DOWN, buff=V_PAD+0.5)
        self.play(FadeIn(big_t, shift=UP*0.12), run_time=0.6)
        self.wait(5.5)

        self.play(
            FadeOut(timeline), FadeOut(dot_leif), FadeOut(dot_col),
            FadeOut(lbl_leif), FadeOut(lbl_leif2), FadeOut(lbl_col), FadeOut(lbl_col2),
            FadeOut(gap_lbl), FadeOut(big_t), run_time=0.5,
        )

    def _g4_filed_no_paperwork(self):
        self.camera.background_color = WHITE_BG
        # Settlement dot that quietly vanishes
        dot = Dot(point=ORIGIN, radius=0.18, color=AMBER)
        lbl = Text("Leifsbuðir", font="Poppins", weight=LIGHT,
                   font_size=26, color=AMBER).next_to(dot, UP, buff=0.3)
        self.add(dot, lbl)
        self.wait(0.5)

        # Dot vanishes — no drama
        self.play(FadeOut(dot), FadeOut(lbl), run_time=0.8)

        lines = [
            ("Filed no paperwork.", GREY),
            ("Left.", GREY),
            ("History moved on without him.", L_GREY),
        ]
        y = 1.2
        mobs = []
        for txt, col in lines:
            t = Text(txt, font="Poppins", weight=LIGHT, font_size=34,
                     color=col, slant=ITALIC).move_to(UP*y)
            mobs.append(t)
            self.play(FadeIn(t, shift=DOWN*0.1), run_time=0.5)
            self.wait(0.5)
            y -= 0.9

        self.wait(5.0)
        self.play(*[FadeOut(m) for m in mobs], run_time=0.5)

    # ── SECTION H ─────────────────────────────────────────────────────────────

    def _h1_iceland_was_writing(self):
        self.camera.background_color = WHITE_BG
        # Quill appears — ink spreads
        quill = Line([-0.08, 0.5, 0], [0.08, -0.5, 0],
                     stroke_color=AMBER, stroke_width=4).move_to(ORIGIN)
        quill_tip = Dot(point=[0, -0.5, 0], radius=0.06, color=AMBER)

        # "Ink" spreading: multiple short text fragments appearing randomly
        fragment_data = [
            ("saga", LEFT*3.0+UP*1.5), ("law", RIGHT*2.5+UP*2.0),
            ("rune", LEFT*1.5+UP*2.5), ("myth", RIGHT*3.5+DOWN*1.0),
            ("skald", LEFT*3.5+DOWN*1.5), ("thing", RIGHT*1.0+DOWN*2.0),
        ]
        fragments = [
            Text(t, font="Poppins", weight=LIGHT, font_size=18,
                 color="#CCCCCC").move_to(pos)
            for t, pos in fragment_data
        ]

        self.play(GrowFromCenter(quill), GrowFromCenter(quill_tip), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(f) for f in fragments], lag_ratio=0.15),
            run_time=2.0,
        )

        big_t = Text("Iceland was writing.", font="Poppins", weight=BOLD,
                     font_size=58, color=DARK).move_to(ORIGIN)
        self.play(
            *[FadeOut(f) for f in fragments],
            FadeOut(quill), FadeOut(quill_tip),
            run_time=0.5,
        )
        self.play(GrowFromCenter(big_t), run_time=0.7)
        self.wait(7.5)

        self.play(FadeOut(big_t), run_time=0.5)

    def _h2_the_three_things(self):
        self.camera.background_color = WHITE_BG
        # Three scroll/book icons
        scroll1 = VGroup(
            Rectangle(width=1.5, height=2.0, fill_color="#F5F0E0",
                     fill_opacity=1, stroke_color=BROWN, stroke_width=2),
            Ellipse(width=1.5, height=0.3, fill_color="#D4B870",
                   fill_opacity=1, stroke_width=0).shift(UP*1.0),
            Ellipse(width=1.5, height=0.3, fill_color="#D4B870",
                   fill_opacity=1, stroke_width=0).shift(DOWN*1.0),
        ).move_to(LEFT*4.0)
        lbl1 = Text("Family Sagas", font="Poppins", weight=SEMIBOLD,
                    font_size=22, color=DARK).next_to(scroll1, DOWN, buff=0.3)

        book2 = VGroup(
            Rectangle(width=1.4, height=1.9, fill_color="#D4C8A8",
                     fill_opacity=1, stroke_color=DARK, stroke_width=2),
            Rectangle(width=0.12, height=1.9, fill_color=BROWN,
                     fill_opacity=1, stroke_width=0).move_to(LEFT*0.64),
        ).move_to(ORIGIN)
        lbl2 = Text("Kings' Histories", font="Poppins", weight=SEMIBOLD,
                    font_size=22, color=DARK).next_to(book2, DOWN, buff=0.3)

        tome3 = VGroup(
            Rectangle(width=1.4, height=2.0, fill_color="#8A6A20",
                     fill_opacity=1, stroke_color=DARK, stroke_width=2),
            Rectangle(width=0.12, height=2.0, fill_color="#5A4010",
                     fill_opacity=1, stroke_width=0).move_to(LEFT*0.64),
            Text("✦", font="Poppins", weight=BOLD, font_size=28, color=AMBER
                ).move_to(ORIGIN),
        ).move_to(RIGHT*4.0)
        lbl3 = Text("Mythology", font="Poppins", weight=SEMIBOLD,
                    font_size=22, color=DARK).next_to(tome3, DOWN, buff=0.3)

        for icon, lbl in [(scroll1, lbl1), (book2, lbl2), (tome3, lbl3)]:
            self.play(GrowFromCenter(icon), FadeIn(lbl), run_time=0.6)
            self.wait(0.3)

        sub = Text("The most sophisticated prose literature of medieval Europe.",
                   font="Poppins", weight=LIGHT, font_size=22,
                   color=GREY, slant=ITALIC).to_edge(DOWN, buff=V_PAD+0.4)
        self.play(FadeIn(sub, shift=UP*0.1), run_time=0.6)
        self.wait(10.5)

        self.play(
            FadeOut(scroll1), FadeOut(book2), FadeOut(tome3),
            FadeOut(lbl1), FadeOut(lbl2), FadeOut(lbl3),
            FadeOut(sub), run_time=0.5,
        )

    def _h3_snorri(self):
        self.camera.background_color = WHITE_BG
        snorri = load_char("snorri_sturluson", height=3.5)
        if snorri is None:
            snorri = make_snorri_geo(scale=1.0)
        snorri.move_to(RIGHT*1.0)

        # Desk
        desk = Rectangle(width=3.0, height=0.18, fill_color=BROWN,
                        fill_opacity=1, stroke_width=0
                        ).next_to(snorri, DOWN, buff=-0.1)

        name_t = Text("Snorri Sturluson", font="Poppins", weight=BOLD,
                      font_size=36, color=DARK).to_edge(DOWN, buff=V_PAD+0.8)
        born_t = Text("Born 1179 AD", font="Poppins", weight=LIGHT,
                      font_size=24, color=AMBER).next_to(name_t, DOWN, buff=0.18)

        self.play(GrowFromCenter(snorri), FadeIn(desk), run_time=0.8)
        self.play(FadeIn(name_t, shift=UP*0.1), FadeIn(born_t, shift=UP*0.1),
                  run_time=0.6)
        self.wait(9.5)

        self.play(FadeOut(snorri), FadeOut(desk), FadeOut(name_t), FadeOut(born_t),
                  run_time=0.5)

    def _h4_thor_odin(self):
        self.camera.background_color = WHITE_BG
        # Four mythology icons
        # Thor's hammer
        thor_h  = VGroup(
            Rectangle(width=0.6, height=0.5, fill_color=STONE,
                     fill_opacity=1, stroke_color=DARK, stroke_width=1.5),
            Rectangle(width=0.18, height=0.8, fill_color=BROWN,
                     fill_opacity=1, stroke_width=0).shift(DOWN*0.65),
        ).move_to(LEFT*4.5+UP*0.5)
        thor_l  = Text("Thor", font="Poppins", weight=BOLD, font_size=26,
                       color=DARK).next_to(thor_h, DOWN, buff=0.3)

        # Odin's ravens (two circles as bird heads)
        raven1  = Ellipse(width=0.35, height=0.28, fill_color=DARK, fill_opacity=1,
                         stroke_width=0).move_to(LEFT*1.5+UP*0.7)
        raven2  = Ellipse(width=0.35, height=0.28, fill_color=DARK, fill_opacity=1,
                         stroke_width=0).move_to(LEFT*1.0+UP*0.4)
        odin_g  = VGroup(raven1, raven2)
        odin_l  = Text("Odin", font="Poppins", weight=BOLD, font_size=26,
                       color=DARK).next_to(odin_g, DOWN, buff=0.3)

        # Loki's serpent — zigzag
        loki_pts = [[0.5,0.6,0],[0.7,0.2,0],[0.5,-0.2,0],[0.7,-0.6,0]]
        loki_g   = VMobject()
        loki_g.set_points_as_corners(loki_pts)
        loki_g.set_stroke(color=GREEN, width=4)
        loki_l   = Text("Loki", font="Poppins", weight=BOLD, font_size=26,
                        color=DARK).move_to([0.6,-1.1,0])

        # Ragnarök — flame
        rag_flame = VGroup(*[
            Triangle(fill_color=RED if i % 2 == 0 else AMBER,
                    fill_opacity=0.85, stroke_width=0
                    ).scale(0.3+i*0.08).move_to([3.5+i*0.15, 0.2+i*0.4, 0])
            for i in range(4)
        ])
        rag_l    = Text("Ragnarök", font="Poppins", weight=BOLD, font_size=26,
                        color=DARK).move_to(RIGHT*3.5+DOWN*0.8)

        icons_lbls = [
            (thor_h,   thor_l),
            (odin_g,   odin_l),
            (VGroup(loki_g), loki_l),
            (rag_flame, rag_l),
        ]
        all_icons = []
        for icon, lbl in icons_lbls:
            self.play(GrowFromCenter(icon), FadeIn(lbl), run_time=0.55)
            self.wait(0.25)
            all_icons += [icon, lbl]

        self.wait(1.5)
        wrote_t = Text("A 13th-century Icelander wrote it down.", font="Poppins",
                       weight=BOLD, font_size=38, color=AMBER
                       ).to_edge(DOWN, buff=V_PAD+0.4)
        self.play(FadeIn(wrote_t, shift=UP*0.12), run_time=0.6)
        self.wait(12.5)

        self.play(*[FadeOut(m) for m in all_icons], FadeOut(wrote_t), run_time=0.5)

    def _h5_welcome_marvel(self):
        self.camera.background_color = WHITE_BG
        forgot_t = Text("Without Snorri: forgotten.", font="Poppins",
                        weight=LIGHT, font_size=36, color=GREY).move_to(UP*0.5)
        # Icon silhouettes fade in grey
        icons_grey = VGroup(*[
            Circle(radius=0.25, fill_color=L_GREY, fill_opacity=0.6, stroke_width=0
                  ).move_to(LEFT*3.0+(i-1.5)*1.5+UP*0.5)
            for i in range(4)
        ])
        self.play(FadeIn(icons_grey), run_time=0.5)
        self.play(FadeIn(forgot_t), run_time=0.5)
        self.wait(1.5)

        # Snap back — icons become AMBER
        self.play(icons_grey.animate.set_fill(color=AMBER, opacity=0.9), run_time=0.4)

        marvel_t = Text("You're welcome, Marvel.", font="Poppins", weight=BOLD,
                        font_size=46, color=RED).move_to(DOWN*0.6)
        self.play(FadeIn(marvel_t, shift=DOWN*0.12), run_time=0.5)
        self.wait(5.5)

        self.play(FadeOut(icons_grey), FadeOut(forgot_t), FadeOut(marvel_t),
                  run_time=0.5)

    def _h6_the_pivot(self):
        self.camera.background_color = WHITE_BG
        t1 = Text("Snorri was also a politician.", font="Poppins",
                  weight=NORMAL, font_size=40, color=DARK).move_to(UP*0.5)
        t2 = Text("This eventually got him killed.", font="Poppins",
                  weight=BOLD, font_size=40, color=RED).move_to(DOWN*0.5)

        self.play(FadeIn(t1, shift=DOWN*0.1), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(t2, shift=DOWN*0.1), run_time=0.5)
        self.wait(5.0)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)
