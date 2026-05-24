"""
iceland_part3.py — Sections I–L: Sturlung Age + Old Covenant + Long Middle + Close (~255s)
VO Part 3 content.
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
COLD_GREY = "#2E2E3A"
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


def make_small_figure(color=STONE, scale=1.0):
    head = Circle(radius=0.15*scale, fill_color=color, fill_opacity=1, stroke_width=0)
    body = Rectangle(width=0.22*scale, height=0.38*scale,
                     fill_color=color, fill_opacity=1, stroke_width=0
                     ).next_to(head, DOWN, buff=0.02*scale)
    return VGroup(head, body)


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


def make_iceland_outline(fill="#D4C8A8"):
    pts = [
        [-1.8, 0.8, 0], [-2.1, 0.3, 0], [-2.4, -0.1, 0], [-2.2, -0.5, 0],
        [-1.6, -0.9, 0], [-0.8, -1.1, 0], [0.2, -1.0, 0], [0.9, -0.7, 0],
        [1.6, -0.3, 0], [2.0,  0.3, 0], [1.8,  0.8, 0], [1.2,  1.0, 0],
        [0.4,  1.1, 0], [-0.4, 1.2, 0], [-1.0, 1.0, 0], [-1.5, 0.9, 0],
    ]
    return Polygon(*pts, fill_color=fill, fill_opacity=0.7,
                   stroke_color=DARK, stroke_width=2)


def make_chieftain_row(n=36, scale=0.55):
    group = VGroup()
    cols = 12
    rows = 3
    for i in range(min(n, cols * rows)):
        fig = make_small_figure(color=STONE, scale=scale)
        col = i % cols
        row = i // cols
        fig.move_to([col * 0.9 - 4.9, row * -0.7 + 0.6, 0])
        group.add(fig)
    return group


def make_king_geo(scale=1.0):
    head = Circle(radius=0.32*scale, fill_color="#C8956A", fill_opacity=1,
                  stroke_color=DARK, stroke_width=1.5)
    body = Rectangle(width=0.7*scale, height=0.9*scale,
                     fill_color="#4A2080", fill_opacity=1, stroke_width=0
                     ).next_to(head, DOWN, buff=0.04*scale)
    crown_pts = [
        [-0.32*scale, 0.12*scale, 0], [-0.32*scale, 0.4*scale, 0],
        [-0.16*scale, 0.2*scale, 0], [0, 0.45*scale, 0],
        [0.16*scale, 0.2*scale, 0], [0.32*scale, 0.4*scale, 0],
        [0.32*scale, 0.12*scale, 0],
    ]
    crown = Polygon(*crown_pts, fill_color="#D4A800", fill_opacity=1, stroke_width=0)
    crown.move_to(head.get_center() + UP*0.28*scale)
    return VGroup(body, head, crown)


def make_farmhouse(scale=1.0):
    walls = Rectangle(width=2.0*scale, height=1.2*scale,
                      fill_color="#7A6050", fill_opacity=1, stroke_color=DARK, stroke_width=2)
    roof_pts = [
        [-1.2*scale, 0.6*scale, 0], [0, 1.4*scale, 0], [1.2*scale, 0.6*scale, 0],
    ]
    roof = Polygon(*roof_pts, fill_color="#4A3020", fill_opacity=1,
                   stroke_color=DARK, stroke_width=2)
    door = Rectangle(width=0.3*scale, height=0.5*scale,
                     fill_color=DARK, fill_opacity=0.8, stroke_width=0
                     ).move_to(walls.get_center() + DOWN*0.35*scale)
    return VGroup(walls, roof, door)


def make_cross(scale=1.0):
    v = Rectangle(width=0.12*scale, height=0.55*scale,
                  fill_color="#6B4A20", fill_opacity=1, stroke_width=0)
    h = Rectangle(width=0.38*scale, height=0.10*scale,
                  fill_color="#6B4A20", fill_opacity=1, stroke_width=0
                  ).move_to(v.get_center() + UP*0.12*scale)
    return VGroup(v, h)


def make_scroll(scale=1.0):
    body = Rectangle(width=2.4*scale, height=1.6*scale,
                     fill_color="#F5EAC8", fill_opacity=1,
                     stroke_color="#8B6A30", stroke_width=3)
    top_roll = Ellipse(width=2.6*scale, height=0.3*scale,
                       fill_color="#E8D8A0", fill_opacity=1,
                       stroke_color="#8B6A30", stroke_width=2
                       ).next_to(body, UP, buff=-0.1*scale)
    bot_roll = Ellipse(width=2.6*scale, height=0.3*scale,
                       fill_color="#E8D8A0", fill_opacity=1,
                       stroke_color="#8B6A30", stroke_width=2
                       ).next_to(body, DOWN, buff=-0.1*scale)
    return VGroup(body, top_roll, bot_roll)


class IcelandPart3(Scene):
    def construct(self):
        self.camera.background_color = WHITE_BG
        self._i1_dark_turns()
        self._i2_forty_years()
        self._i3_norway_watches()
        self._i4_seventy_men()
        self._i5_last_words()
        self._i6_they_struck()
        self._j1_commonwealth_falls()
        self._j2_the_signature()
        self._j3_not_conquest()
        self._j4_what_they_built()
        self._j5_underground()
        self._k1_the_catalogue()
        self._k2_original_instinct()
        self._l1_return()
        self._l2_the_foundation()
        self._end_card()

    # ── SECTION I — THE STURLUNG AGE ─────────────────────────────────────

    def _i1_dark_turns(self):
        # Background bleeds from warm white to cold grey
        bg = Rectangle(width=15, height=9, fill_color=WHITE_BG,
                       fill_opacity=1, stroke_width=0)
        self.add(bg)

        date_bar = Rectangle(width=5.5, height=0.65,
                             fill_color=COLD_GREY, fill_opacity=1, stroke_width=0)
        date_bar.move_to([0, 2.6, 0])
        date_txt = Text("1220 – 1262", font="Poppins", weight=BOLD,
                        font_size=28, color=WHITE)
        date_txt.move_to(date_bar.get_center())

        title = Text("The Sturlung Age.", font="Poppins", weight=BOLD,
                     font_size=46, color=COLD_GREY)
        title.move_to([0, 1.4, 0])

        chieftains = make_chieftain_row(36, scale=0.52)
        chieftains.move_to([0, -0.8, 0])

        self.play(
            bg.animate.set_fill(color="#D8D8E0"),
            run_time=2.5
        )
        self.play(
            FadeIn(date_bar, date_txt),
            run_time=0.7
        )
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(chieftains), run_time=0.8)

        # Chieftains topple one by one
        for i, fig in enumerate(chieftains):
            self.play(
                Rotate(fig, angle=PI/2, about_point=fig.get_bottom()),
                run_time=0.18,
            )
        self.wait(1.5)
        self.clear()

    def _i2_forty_years(self):
        self.camera.background_color = "#D8D8E0"

        iceland = make_iceland_outline(fill="#A8A8B8")
        iceland.scale(2.0).move_to([0, 0.3, 0])
        self.add(iceland)

        # Flash red zones — irregular points across the map
        zone_positions = [
            [-2.0, 0.5, 0], [0.5, -0.8, 0], [1.5, 0.2, 0],
            [-1.0, -0.5, 0], [0.0, 0.8, 0], [2.0, -0.2, 0],
        ]
        for pos in zone_positions:
            flash = Circle(radius=0.45, fill_color=RED,
                           fill_opacity=0.0, stroke_width=0)
            flash.move_to(pos)
            self.play(
                flash.animate.set_fill(opacity=0.7),
                run_time=0.25,
            )
            self.play(
                flash.animate.set_fill(opacity=0.0),
                run_time=0.35,
            )

        years_txt = Text("40 years.", font="Poppins", weight=BOLD,
                         font_size=60, color=COLD_GREY)
        years_txt.move_to([0, -2.6, 0])
        self.play(FadeIn(years_txt, shift=UP*0.3), run_time=0.5)

        for word in ["Raids.", "Assassinations.", "Revenge."]:
            w = Text(word, font="Poppins", weight=BOLD,
                     font_size=38, color=RED)
            w.next_to(years_txt, RIGHT, buff=0.5)
            self.play(FadeIn(w, shift=UP*0.15), run_time=0.3)
            self.wait(0.6)
        self.wait(1.5)
        self.clear()

    def _i3_norway_watches(self):
        self.camera.background_color = "#D8D8E0"

        iceland = make_iceland_outline(fill="#A8A8B8")
        iceland.scale(1.6).move_to([-2.5, 0.2, 0])
        self.add(iceland)

        king = make_king_geo(scale=1.1)
        king.move_to([4.0, 0.0, 0])
        king_lbl = Text("Hákon IV", font="Poppins", weight=SEMIBOLD,
                        font_size=22, color=DARK)
        king_lbl.next_to(king, DOWN, buff=0.2)

        self.play(FadeIn(king, king_lbl), run_time=0.8)

        chess_positions = [
            [-3.5, 0.4, 0], [-1.8, -0.5, 0], [-2.8, -0.3, 0],
        ]
        chess_pieces = VGroup()
        for pos in chess_positions:
            piece = RegularPolygon(n=6, radius=0.22,
                                   fill_color=COLD_GREY, fill_opacity=1, stroke_width=0)
            piece.move_to(pos)
            chess_pieces.add(piece)

        self.play(FadeIn(chess_pieces), run_time=0.6)

        eye_line = Line(king.get_left(), [-0.9, 0.2, 0],
                        stroke_color=AMBER, stroke_width=1.5, stroke_opacity=0.5)
        self.play(Create(eye_line), run_time=0.8)

        for beat in ["Hákon IV watched.", "He waited.", "He picked his moment."]:
            t = Text(beat, font="Poppins", weight=NORMAL,
                     font_size=28, color=DARK, slant=ITALIC)
            t.move_to([0, -3.0, 0])
            self.play(FadeIn(t, shift=UP*0.15), run_time=0.5)
            self.wait(0.9)
            self.play(FadeOut(t), run_time=0.25)
        self.wait(1.0)
        self.clear()

    def _i4_seventy_men(self):
        self.camera.background_color = "#0A0A0A"

        farmhouse = make_farmhouse(scale=1.2)
        farmhouse.move_to([0, 0.5, 0])
        self.add(farmhouse)

        # 70 silhouettes approach from the right in rows
        silhouettes = VGroup()
        for i in range(70):
            fig = make_small_figure(color="#303030", scale=0.38)
            col = i % 14
            row = i // 14
            fig.move_to([col * 0.45 - 3.1, row * -0.55 - 1.5, 0])
            silhouettes.add(fig)

        silhouettes.shift(RIGHT * 8)
        self.play(FadeIn(farmhouse), run_time=0.5)
        self.play(silhouettes.animate.shift(LEFT * 8), run_time=2.8)

        for line in ["September 1241.", "70 men.", "Middle of the night."]:
            t = Text(line, font="Poppins", weight=BOLD,
                     font_size=36, color=WHITE)
            t.move_to([0, 3.1, 0])
            self.play(FadeIn(t, shift=DOWN*0.2), run_time=0.5)
            self.wait(1.2)
            self.play(FadeOut(t), run_time=0.25)
        self.wait(1.5)
        self.clear()

    def _i5_last_words(self):
        self.camera.background_color = "#0A0A0A"

        norse = Text("Eigi skal höggva.", font="Poppins", weight=BOLD,
                     font_size=52, color=WHITE)
        norse.move_to([0, 0.6, 0])

        english = Text("Do not strike.", font="Poppins", weight=LIGHT,
                       font_size=32, color=L_GREY)
        english.next_to(norse, DOWN, buff=0.5)

        self.play(FadeIn(norse), run_time=1.2)
        self.play(FadeIn(english), run_time=0.8)
        self.wait(3.5)
        self.clear()

    def _i6_they_struck(self):
        self.camera.background_color = "#0A0A0A"

        they_struck = Text("They struck.", font="Poppins", weight=BOLD,
                           font_size=60, color=RED)
        they_struck.move_to([0, 0, 0])

        self.play(FadeIn(they_struck, shift=DOWN*0.2), run_time=0.4)
        self.wait(3.5)
        self.clear()

    # ── SECTION J — THE OLD COVENANT ─────────────────────────────────────

    def _j1_commonwealth_falls(self):
        self.camera.background_color = "#D8D8E0"

        chieftains = make_chieftain_row(36, scale=0.52)
        chieftains.move_to([0, 0.2, 0])
        self.add(chieftains)

        year_txt = Text("1262.", font="Poppins", weight=BOLD,
                        font_size=50, color=COLD_GREY)
        year_txt.move_to([0, -2.5, 0])
        self.play(FadeIn(year_txt, shift=UP*0.2), run_time=0.6)

        for fig in chieftains:
            self.play(fig.animate.set_color(L_GREY).set_opacity(0.3),
                      run_time=0.12)

        for word in ["Exhausted.", "Too broken."]:
            t = Text(word, font="Poppins", weight=NORMAL,
                     font_size=36, color=GREY, slant=ITALIC)
            t.next_to(year_txt, RIGHT, buff=0.7)
            self.play(FadeIn(t, shift=UP*0.1), run_time=0.45)
            self.wait(0.9)
            self.play(FadeOut(t), run_time=0.2)
        self.wait(1.5)
        self.clear()

    def _j2_the_signature(self):
        self.camera.background_color = WHITE_BG

        scroll = make_scroll(scale=1.2)
        scroll.move_to([0, -0.3, 0])

        quill_line = Text("~~~~~", font="Poppins", weight=NORMAL,
                          font_size=20, color=DARK)
        quill_line.move_to([0, -0.4, 0])

        seal = Circle(radius=0.4, fill_color="#8B2020",
                      fill_opacity=1, stroke_color="#5A0000", stroke_width=3)
        seal.move_to([0.9, -1.15, 0])

        lbl1 = Text("Gamli sáttmáli", font="Poppins", weight=BOLD,
                    font_size=30, color=DARK)
        lbl2 = Text("The Old Covenant · 1262", font="Poppins", weight=LIGHT,
                    font_size=22, color=GREY, slant=ITALIC)
        lbl1.move_to([0, 1.6, 0])
        lbl2.next_to(lbl1, DOWN, buff=0.25)

        above_txt = Text("Handed to Norway.", font="Poppins", weight=BOLD,
                         font_size=40, color=COLD_GREY)
        above_txt.move_to([0, 2.7, 0])

        self.play(FadeIn(scroll), run_time=0.7)
        self.play(Write(quill_line), run_time=1.5)
        self.play(FadeIn(seal, scale=0.3), run_time=0.5)
        self.play(FadeIn(lbl1, lbl2), run_time=0.7)
        self.play(FadeIn(above_txt, shift=DOWN*0.2), run_time=0.6)
        self.wait(2.0)
        self.clear()

    def _j3_not_conquest(self):
        self.camera.background_color = WHITE_BG

        line1 = Text("Not conquest.", font="Poppins", weight=NORMAL,
                     font_size=48, color=DARK, slant=ITALIC)
        line1.move_to([0, 1.0, 0])

        strikethrough = Line(
            line1.get_left() + LEFT*0.1,
            line1.get_right() + RIGHT*0.1,
            stroke_color=RED, stroke_width=5
        )

        line2 = Text("Surrender by choice.", font="Poppins", weight=BOLD,
                     font_size=48, color=AMBER)
        line2.move_to([0, -0.2, 0])

        line3 = Text("Somehow more Icelandic.", font="Poppins", weight=LIGHT,
                     font_size=28, color=GREY, slant=ITALIC)
        line3.move_to([0, -1.4, 0])

        self.play(FadeIn(line1), run_time=0.7)
        self.play(GrowFromPoint(strikethrough, strikethrough.get_left()), run_time=0.5)
        self.play(FadeIn(line2, shift=UP*0.15), run_time=0.6)
        self.play(FadeIn(line3), run_time=0.6)
        self.wait(2.5)
        self.clear()

    def _j4_what_they_built(self):
        self.camera.background_color = WHITE_BG

        icons_data = [
            (make_chieftain_row(7, scale=0.6), "Parliament",       [-4.5, 0.5, 0]),
            (make_scroll(scale=0.7),           "Legal tradition",   [-1.5, 0.3, 0]),
            (make_scroll(scale=0.7),           "Literary culture",  [1.5,  0.3, 0]),
            (make_small_figure(STONE, 1.0),    "Stubbornness",      [4.5,  0.3, 0]),
        ]

        for icon, label, pos in icons_data:
            icon.move_to(pos)
            lbl = Text(label, font="Poppins", weight=SEMIBOLD,
                       font_size=22, color=DARK)
            lbl.next_to(icon, DOWN, buff=0.3)
            self.play(GrowFromPoint(icon, [pos[0], pos[1]-0.8, 0]), run_time=0.6)
            self.play(FadeIn(lbl), run_time=0.35)

        footer1 = Text("Three centuries.", font="Poppins", weight=BOLD,
                       font_size=36, color=AMBER)
        footer2 = Text("Something extraordinary.", font="Poppins", weight=BOLD,
                       font_size=36, color=DARK)
        footer1.move_to([0, -2.5, 0])
        footer2.next_to(footer1, RIGHT, buff=0.5)
        self.play(FadeIn(footer1, footer2), run_time=0.7)
        self.wait(2.5)
        self.clear()

    def _j5_underground(self):
        self.camera.background_color = WHITE_BG

        icons = VGroup(
            make_chieftain_row(5, scale=0.55).move_to([-4.0, 1.2, 0]),
            make_scroll(scale=0.6).move_to([-1.3, 1.0, 0]),
            make_scroll(scale=0.6).move_to([1.3,  1.0, 0]),
            make_small_figure(STONE, 0.9).move_to([4.0, 1.2, 0]),
        )
        self.add(icons)

        ground = Line([-7.5, -0.5, 0], [7.5, -0.5, 0],
                      stroke_color=STONE, stroke_width=4)
        self.play(Create(ground), run_time=0.6)

        self.play(icons.animate.shift(DOWN * 2.4).set_opacity(0.25), run_time=1.8)

        t1 = Text("It didn't disappear.", font="Poppins", weight=BOLD,
                  font_size=38, color=DARK)
        t2 = Text("It went underground.", font="Poppins", weight=BOLD,
                  font_size=38, color=AMBER)
        t1.move_to([0, 2.5, 0])
        t2.next_to(t1, DOWN, buff=0.45)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, shift=DOWN*0.15), run_time=0.6)
        self.wait(2.5)
        self.clear()

    # ── SECTION K — THE LONG MIDDLE ──────────────────────────────────────

    def _k1_the_catalogue(self):
        self.camera.background_color = WHITE_BG

        items = [
            ("Althing: abolished.",              GREY,     NORMAL,  34),
            ("Althing: restored.",               GREY,     NORMAL,  34),
            ("Sold to Denmark.",                 GREY,     NORMAL,  34),
            ("Plagues.",                         DARK,     BOLD,    42),
            ("Famines.",                         DARK,     BOLD,    42),
            ("North African pirates raided the coast.", RED, BOLD, 38),
            ("Occupied by Britain.",             GREY,     NORMAL,  34),
            ("Then America.",                    GREY,     NORMAL,  34),
            ("Banks: exploded.",                 RED,      BOLD,    44),
            ("Volcano: shut down European airspace.", DARK, SEMIBOLD, 36),
        ]

        for text, color, weight, size in items:
            t = Text(text, font="Poppins", weight=weight,
                     font_size=size, color=color)
            t.move_to([0, 0, 0])
            hold = 1.8 if "pirates" in text else 1.3
            self.play(FadeIn(t), run_time=0.3)
            self.wait(hold)
            self.play(FadeOut(t), run_time=0.2)
        self.wait(0.5)
        self.clear()

    def _k2_original_instinct(self):
        self.camera.background_color = WHITE_BG

        # Monk boat — same tiny vessel from Section A
        hull = Polygon(
            [-0.7, 0, 0], [-0.5, -0.18, 0], [0.5, -0.18, 0], [0.7, 0, 0],
            [0.4, 0.04, 0], [-0.4, 0.04, 0],
            fill_color="#3A2A1A", fill_opacity=1, stroke_width=0,
        )
        mast = Line([0, 0.0, 0], [0, 0.6, 0], stroke_color=DARK, stroke_width=2)
        sail = Polygon(
            [0, 0.58, 0], [0.32, 0.15, 0], [-0.32, 0.15, 0],
            fill_color="#D4B88A", fill_opacity=0.9, stroke_width=0,
        )
        boat = VGroup(hull, mast, sail)
        boat.move_to([-4.5, 0.5, 0])

        sea = Rectangle(width=15, height=0.06,
                        fill_color=AMBER, fill_opacity=0.3, stroke_width=0)
        sea.move_to([0, 0.3, 0])

        self.add(sea, boat)
        self.play(boat.animate.shift(RIGHT * 9.0), run_time=5.0,
                  rate_func=linear)

        self.play(FadeIn(sea), run_time=0.01)

        for i, line in enumerate([
            "The stubbornness.",
            "The pragmatism.",
            "The willingness to refuse.",
        ]):
            t = Text(line, font="Poppins", weight=BOLD,
                     font_size=38, color=AMBER)
            t.move_to([0, -0.8 - i * 0.95, 0])
            self.play(FadeIn(t, shift=UP*0.15), run_time=0.6)
            self.wait(1.2)
        self.wait(2.0)
        self.clear()

    # ── SECTION L — THE CLOSE ─────────────────────────────────────────────

    def _l1_return(self):
        self.camera.background_color = WHITE_BG

        # Iceland map with the October 2008 visual language returning
        iceland = make_iceland_outline(fill="#D4C8A8")
        iceland.scale(2.1).move_to([0, 0.3, 0])

        date_txt = Text("October 2008.", font="Poppins", weight=BOLD,
                        font_size=54, color=DARK)
        date_txt.move_to([0, 2.9, 0])

        bank_towers = VGroup()
        for i, (x, h) in enumerate([(-1.0, 2.0), (0.0, 2.6), (1.0, 1.8)]):
            tower = Rectangle(width=0.55, height=h,
                              fill_color="#4A5060", fill_opacity=0.85,
                              stroke_color=DARK, stroke_width=1.5)
            tower.move_to([x, h/2 - 1.1, 0])
            bank_towers.add(tower)

        crack = Line([0, 1.3, 0], [0, -1.3, 0],
                     stroke_color=RED, stroke_width=3, stroke_opacity=0.7)

        self.play(FadeIn(iceland), run_time=0.7)
        self.play(FadeIn(bank_towers), run_time=0.5)
        self.play(GrowFromPoint(crack, [0, 1.3, 0]), run_time=0.8)
        self.play(FadeIn(date_txt, shift=DOWN*0.2), run_time=0.6)
        self.wait(3.5)
        self.clear()

    def _l2_the_foundation(self):
        self.camera.background_color = WHITE_BG

        iceland = make_iceland_outline(fill="#D4C8A8")
        iceland.scale(1.6).move_to([0, 0.9, 0])
        self.add(iceland)

        timeline = Line([-5.5, -1.8, 0], [5.5, -1.8, 0],
                        stroke_color=DARK, stroke_width=2)

        dot_left = Dot([- 5.5, -1.8, 0], radius=0.12,
                       color=AMBER, fill_opacity=1)
        lbl_left = Text("874 AD", font="Poppins", weight=SEMIBOLD,
                        font_size=22, color=AMBER)
        lbl_left.next_to(dot_left, DOWN, buff=0.2)

        dot_right = Dot([5.5, -1.8, 0], radius=0.12,
                        color=DARK, fill_opacity=1)
        lbl_right = Text("2008 AD", font="Poppins", weight=SEMIBOLD,
                         font_size=22, color=DARK)
        lbl_right.next_to(dot_right, DOWN, buff=0.2)

        connector = Line([-5.5, -1.8, 0], [5.5, -1.8, 0],
                         stroke_color=AMBER, stroke_width=3)

        title = Text("The foundation", font="Poppins", weight=BOLD,
                     font_size=46, color=DARK)
        sub = Text("was laid in 874.", font="Poppins", weight=BOLD,
                   font_size=46, color=AMBER)
        title.move_to([0, -3.0, 0])
        sub.next_to(title, RIGHT, buff=0.35)

        self.play(Create(timeline), run_time=0.6)
        self.play(FadeIn(dot_left, lbl_left), run_time=0.5)
        self.play(FadeIn(dot_right, lbl_right), run_time=0.5)
        self.play(Create(connector), run_time=1.5)
        self.play(
            iceland.animate.set_fill(color=AMBER, opacity=0.5),
            run_time=0.7,
        )
        self.play(FadeIn(title, sub), run_time=0.8)
        self.wait(3.0)
        self.clear()

    def _end_card(self):
        self.camera.background_color = WHITE_BG

        # Iceland flag colours
        flag_bg = Rectangle(width=5.4, height=3.4,
                            fill_color="#003897", fill_opacity=1, stroke_width=0)
        flag_h = Rectangle(width=5.4, height=0.55,
                           fill_color=WHITE, fill_opacity=1, stroke_width=0)
        flag_v = Rectangle(width=0.55, height=3.4,
                           fill_color=WHITE, fill_opacity=1, stroke_width=0)
        flag_h_red = Rectangle(width=5.4, height=0.28,
                               fill_color=RED, fill_opacity=1, stroke_width=0)
        flag_v_red = Rectangle(width=0.28, height=3.4,
                               fill_color=RED, fill_opacity=1, stroke_width=0)
        flag_v.move_to([-0.75, 0, 0])
        flag_h.move_to([0, 0, 0])
        flag_v_red.move_to([-0.75, 0, 0])
        flag_h_red.move_to([0, 0, 0])
        flag = VGroup(flag_bg, flag_h, flag_v, flag_h_red, flag_v_red)
        flag.move_to([0, 0.8, 0])

        title = Text("How to Steal an Island", font="Poppins", weight=BOLD,
                     font_size=44, color=DARK)
        title.move_to([0, -1.4, 0])

        next_ep = Text(
            "Next: The Althing, the Sagas, and how Iceland\n"
            "built the rules it still lives by.",
            font="Poppins", weight=LIGHT, font_size=26, color=GREY,
            line_spacing=1.3,
        )
        next_ep.move_to([0, -2.8, 0])

        self.play(FadeIn(flag, shift=DOWN*0.2), run_time=0.8)
        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(next_ep), run_time=0.6)
        self.wait(4.0)
        self.play(FadeOut(VGroup(flag, title, next_ep)), run_time=1.0)
