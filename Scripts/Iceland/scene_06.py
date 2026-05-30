"""Iceland EP1 - Scene 06: IcelandEP1_S06_IcelandAnswer
Extends Scene 05 — no transition. Puppet gets red X → bankers jailed →
Iceland flag shoves foreign flags off screen → "They Let the Banks Fail."
VO: "But, instead, Iceland jailed its bankers. Told the English and the Dutch
     to get lost. Let the banks fail."
Render: manim -qh scene_06.py IcelandEP1_S06_IcelandAnswer
"""
from manim import *
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
CHAR       = SCRIPT_DIR / "../../Output/Iceland/characters"
sys.path.insert(0, str(SCRIPT_DIR))

STAT_RED = "#CC0000"
IC_BLUE  = "#003897"
IC_RED   = "#D72828"
DARK_TXT = "#1A1A1A"


# ── helpers ────────────────────────────────────────────────────────────────

def make_red_x(size=1.3):
    d = size
    return VGroup(
        Line([-d, -d, 0], [d,  d, 0], color=STAT_RED, stroke_width=14),
        Line([-d,  d, 0], [d, -d, 0], color=STAT_RED, stroke_width=14),
    )


def make_jail_gate(cx):
    xs = np.linspace(cx - 1.5, cx + 1.5, 7)
    bars = VGroup(*[
        Line([x, -3.5, 0], [x, 3.5, 0], color="#777777", stroke_width=5)
        for x in xs
    ])
    top = Line([cx-1.5, 3.5, 0], [cx+1.5, 3.5, 0], color="#777777", stroke_width=8)
    bot = Line([cx-1.5, -3.5, 0], [cx+1.5, -3.5, 0], color="#777777", stroke_width=8)
    return VGroup(bars, top, bot)


def make_iceland_flag():
    w, h = 2.8, 1.85
    bg   = Rectangle(width=w, height=h, fill_color=IC_BLUE, fill_opacity=1, stroke_width=0)
    cw_v = Rectangle(width=w*0.12, height=h, fill_color=WHITE,   fill_opacity=1, stroke_width=0).shift(LEFT*w*0.11)
    cw_h = Rectangle(width=w, height=h*0.16,  fill_color=WHITE,   fill_opacity=1, stroke_width=0)
    cr_v = Rectangle(width=w*0.07, height=h, fill_color=IC_RED,  fill_opacity=1, stroke_width=0).shift(LEFT*w*0.11)
    cr_h = Rectangle(width=w, height=h*0.10,  fill_color=IC_RED,  fill_opacity=1, stroke_width=0)
    bdr  = SurroundingRectangle(bg, color="#AAAAAA", stroke_width=1.5, buff=0)
    return VGroup(bg, cw_h, cw_v, cr_h, cr_v, bdr)


def make_uk_flag():
    w, h = 1.4, 0.93
    bg  = Rectangle(width=w, height=h, fill_color="#012169", fill_opacity=1, stroke_width=0)
    d1w = Line([-w/2,-h/2,0], [w/2, h/2,0], color=WHITE,     stroke_width=5)
    d2w = Line([ w/2,-h/2,0], [-w/2,h/2,0], color=WHITE,     stroke_width=5)
    d1r = Line([-w/2,-h/2,0], [w/2, h/2,0], color="#C8102E", stroke_width=2.5)
    d2r = Line([ w/2,-h/2,0], [-w/2,h/2,0], color="#C8102E", stroke_width=2.5)
    ch  = Rectangle(width=w,      height=h*0.22, fill_color=WHITE,     fill_opacity=1, stroke_width=0)
    cv  = Rectangle(width=w*0.13, height=h,      fill_color=WHITE,     fill_opacity=1, stroke_width=0)
    rh  = Rectangle(width=w,      height=h*0.13, fill_color="#C8102E", fill_opacity=1, stroke_width=0)
    rv  = Rectangle(width=w*0.08, height=h,      fill_color="#C8102E", fill_opacity=1, stroke_width=0)
    bdr = SurroundingRectangle(bg, color="#AAAAAA", stroke_width=1.0, buff=0)
    lbl = Text("UK", font="Poppins", font_size=13, color=DARK_TXT).next_to(bg, DOWN, buff=0.08)
    return VGroup(bg, d1w, d2w, d1r, d2r, ch, cv, rh, rv, bdr, lbl)


def make_h_stripes(colors, label, w=1.4, h=0.93):
    n = len(colors)
    bh = h / n
    stripes = VGroup(*[
        Rectangle(width=w, height=bh, fill_color=c, fill_opacity=1, stroke_width=0)
        .shift(DOWN*(h/2 - bh/2 - i*bh))
        for i, c in enumerate(colors)
    ])
    bdr = SurroundingRectangle(stripes, color="#AAAAAA", stroke_width=1.0, buff=0)
    lbl = Text(label, font="Poppins", font_size=13, color=DARK_TXT).next_to(stripes, DOWN, buff=0.08)
    return VGroup(stripes, bdr, lbl)


def make_v_stripes(colors, label, w=1.4, h=0.93):
    n = len(colors)
    bw = w / n
    stripes = VGroup(*[
        Rectangle(width=bw, height=h, fill_color=c, fill_opacity=1, stroke_width=0)
        .shift(LEFT*(w/2 - bw/2 - i*bw))
        for i, c in enumerate(colors)
    ])
    bdr = SurroundingRectangle(stripes, color="#AAAAAA", stroke_width=1.0, buff=0)
    lbl = Text(label, font="Poppins", font_size=13, color=DARK_TXT).next_to(stripes, DOWN, buff=0.08)
    return VGroup(stripes, bdr, lbl)


def make_eu_flag():
    w, h = 1.4, 0.93
    bg   = Rectangle(width=w, height=h, fill_color="#003399", fill_opacity=1, stroke_width=0)
    ring = Text("★  ★  ★", font_size=14, color="#FFCC00").move_to([0, 0.12, 0])
    ring2= Text("★   ★   ★", font_size=11, color="#FFCC00").move_to([0, -0.12, 0])
    bdr  = SurroundingRectangle(bg, color="#AAAAAA", stroke_width=1.0, buff=0)
    lbl  = Text("EU", font="Poppins", font_size=13, color=DARK_TXT).next_to(bg, DOWN, buff=0.08)
    return VGroup(bg, ring, ring2, bdr, lbl)


def make_usa_flag():
    w, h = 1.4, 0.93
    stripes = VGroup(*[
        Rectangle(width=w, height=h/7, fill_color=["#B22234","#FFFFFF"][i%2],
                  fill_opacity=1, stroke_width=0)
        .shift(DOWN*(h/2 - h/14 - i*h/7))
        for i in range(7)
    ])
    canton = Rectangle(width=w*0.38, height=h*4/7, fill_color="#3C3B6E",
                       fill_opacity=1, stroke_width=0)
    canton.move_to([-w/2 + w*0.19, h/2 - h*2/7, 0])
    bdr = SurroundingRectangle(stripes, color="#AAAAAA", stroke_width=1.0, buff=0)
    lbl = Text("USA", font="Poppins", font_size=13, color=DARK_TXT).next_to(stripes, DOWN, buff=0.08)
    return VGroup(stripes, canton, bdr, lbl)


# ── scene ──────────────────────────────────────────────────────────────────

class IcelandEP1_S06_IcelandAnswer(Scene):
    VD = 9.4

    VO_BEAT1 =  3 / 145 * 60   # 1.24s — "But, instead,"
    VO_BEAT2 =  4 / 145 * 60   # 1.66s — "Iceland jailed its bankers."
    VO_BEAT3 =  9 / 145 * 60   # 3.72s — "Told the English and the Dutch to get lost."
    VO_BEAT4 =  4 / 145 * 60   # 1.66s — "Let the banks fail."

    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(font="Poppins")

        # ══════════════════════════════════════════════════════
        # BEAT 1 — "But, instead" — Red X on puppet (scene 05 state)
        # ══════════════════════════════════════════════════════
        puppet = ImageMobject(str(CHAR / "puppet_most_countries.png"))
        puppet.set_height(4.8).move_to([0, 0.4, 0])
        lbl05 = Text("Smile for the IMF cameras.", font="Poppins", weight=BOLD,
                     font_size=44, color=STAT_RED).move_to([0, -3.1, 0])

        # No fade-in — scene 06 begins mid-action extending scene 05
        self.add(puppet, lbl05)

        red_x = make_red_x(1.3).move_to(puppet.get_center() + UP * 0.4)
        self.play(FadeIn(red_x, scale=2.5), run_time=0.35, rate_func=rush_into)

        T1 = 0.35
        self.wait(max(self.VO_BEAT1 - T1, 0))
        self.play(FadeOut(Group(puppet, lbl05, red_x)), run_time=0.3)

        # ══════════════════════════════════════════════════════
        # BEAT 2 — "Iceland jailed its bankers"
        # 3 bankers appear, jail bars drop on each
        # ══════════════════════════════════════════════════════
        chars_info = [
            (-4.2, "banker_woman.png"),
            ( 0.0, "banker_bald.png"),
            ( 4.2, "banker_man.png"),
        ]
        bankers = []
        for cx, fname in chars_info:
            img = ImageMobject(str(CHAR / fname))
            img.set_height(4.5).move_to([cx, 0.2, 0])
            bankers.append(img)

        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in bankers], lag_ratio=0.3),
            run_time=0.5,
        )

        gates = [make_jail_gate(cx) for cx, _ in chars_info]
        for g in gates:
            g.shift(UP * 9)

        self.play(
            LaggedStart(
                gates[0].animate.shift(DOWN * 9),
                gates[1].animate.shift(DOWN * 9),
                gates[2].animate.shift(DOWN * 9),
                lag_ratio=0.3,
            ),
            run_time=0.75, rate_func=rush_into,
        )

        T2 = 0.3 + 0.5 + 0.75
        self.wait(max(self.VO_BEAT2 - T2, 0) + 0.25)
        self.play(FadeOut(Group(*bankers, *gates)), run_time=0.3)

        # ══════════════════════════════════════════════════════
        # BEAT 3 — "Told the English and the Dutch to get lost"
        # Iceland flag shoves foreign flags off screen
        # ══════════════════════════════════════════════════════
        iceland = make_iceland_flag().move_to(ORIGIN)

        # Left flags: UK, Germany, France
        left_flags = VGroup(
            make_uk_flag(),
            make_h_stripes(["#000000","#DD0000","#FFCE00"], "Germany"),
            make_v_stripes(["#002395","#FFFFFF","#ED2939"], "France"),
        ).arrange(DOWN, buff=0.2).move_to([-5.2, 0.3, 0])

        # Right flags: Netherlands, USA, EU, Canada
        right_flags = VGroup(
            make_h_stripes(["#AE1C28","#FFFFFF","#21468B"], "Netherlands"),
            make_usa_flag(),
            make_eu_flag(),
            make_v_stripes(["#FF0000","#FFFFFF","#FF0000"], "Canada"),
        ).arrange(DOWN, buff=0.12).move_to([5.2, 0.1, 0])

        # Start off-screen on each side
        left_flags.shift(LEFT * 9)
        right_flags.shift(RIGHT * 9)

        self.play(FadeIn(iceland, scale=0.6), run_time=0.4)

        # Foreign flags rush in from both sides
        self.play(
            left_flags.animate.shift(RIGHT * 9),
            right_flags.animate.shift(LEFT * 9),
            run_time=0.7,
        )
        self.wait(0.4)

        # Iceland flag shakes — then shoves everyone off
        self.play(iceland.animate.shift(RIGHT * 0.3), run_time=0.1)
        self.play(iceland.animate.shift(LEFT  * 0.3), run_time=0.1)
        self.play(
            left_flags.animate.shift(LEFT  * 18),
            right_flags.animate.shift(RIGHT * 18),
            run_time=0.5, rate_func=rush_into,
        )

        T3 = 0.3 + 0.4 + 0.7 + 0.4 + 0.2 + 0.5
        self.wait(max(self.VO_BEAT3 - T3, 0))
        self.play(FadeOut(iceland), run_time=0.3)

        # ══════════════════════════════════════════════════════
        # BEAT 4 — "Let the banks fail" — title card
        # ══════════════════════════════════════════════════════
        line1 = Text("They Let the", font="Poppins", font_size=66, color=DARK_TXT)
        line2 = Text("Banks Fail.", font="Poppins", weight=BOLD, font_size=82, color=STAT_RED)
        slide = VGroup(line1, line2).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        slide.shift(RIGHT * 16)

        self.play(slide.animate.shift(LEFT * 16), run_time=0.45, rate_func=rush_into)

        T4 = 0.3 + 0.45
        self.wait(max(self.VO_BEAT4 - T4, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
