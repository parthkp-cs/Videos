"""Iceland EP1 - Scene 09: IcelandEP1_S09_BackUpFurther
Map continues from scene 08. "874" gets strikethrough → wiped → "800" arrives.
Monk (left/800) and Viking (right/874) appear. Year labels zoom in continuously.
VO: "Actually, back up slightly further. Because Iceland didn't start with Vikings. It started with monks."
Render: manim -qh scene_09.py IcelandEP1_S09_BackUpFurther
"""
from manim import *
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
MAPS  = SCRIPT_DIR / "../../Output/Iceland/maps"
CHAR  = SCRIPT_DIR / "../../Output/Iceland/characters"
sys.path.insert(0, str(SCRIPT_DIR))

AMBER    = "#C87941"
DARK_TXT = "#1A1A1A"


class IcelandEP1_S09_BackUpFurther(Scene):
    VD = 6.19

    def construct(self):
        self.camera.background_color = "#D6E8F5"
        Text.set_default(font="Poppins")

        # ── Map background — north_atlantic_wide (same as scene 02) ──────
        sea_map = ImageMobject(str(MAPS / "north_atlantic_wide.png"))
        sea_map.set_width(config.frame_width).move_to(ORIGIN)
        self.add(sea_map)

        # ══════════════════════════════════════════════════════
        # BEAT 1 — "874" with strikethrough, then wiped
        # ══════════════════════════════════════════════════════
        yr874 = Text("874", font="Poppins", weight=BOLD,
                     font_size=120, color=AMBER).move_to(ORIGIN)
        self.add(yr874)   # seamless from scene 08 — "874" already on screen

        # Red strikethrough draws across the text
        strike = Line(
            yr874.get_left()  + LEFT  * 0.1,
            yr874.get_right() + RIGHT * 0.1,
            color="#CC0000", stroke_width=10,
        )
        self.play(Create(strike), run_time=0.4)
        self.wait(0.25)

        # Wipe both off to the left
        self.play(
            yr874.animate.shift(LEFT * 14),
            strike.animate.shift(LEFT * 14),
            run_time=0.3, rate_func=rush_into,
        )
        self.remove(yr874, strike)

        # ══════════════════════════════════════════════════════
        # BEAT 2 — "800" slides in
        # ══════════════════════════════════════════════════════
        yr800 = Text("800", font="Poppins", weight=BOLD,
                     font_size=120, color=AMBER).move_to(RIGHT * 14)
        self.add(yr800)
        self.play(yr800.animate.move_to(ORIGIN), run_time=0.4, rate_func=rush_from)
        self.wait(0.15)

        # ══════════════════════════════════════════════════════
        # BEAT 3 — Monk (left) + Viking (right) drop in
        # ══════════════════════════════════════════════════════
        monk   = ImageMobject(str(CHAR / "irish_monk_seated_nobg.png"))
        viking = ImageMobject(str(CHAR / "viking_settler_nobg.png"))
        monk.set_height(4.94)
        viking.set_height(5.2)

        # Base-align both characters at y = -1.5 (bottom edge)
        BASE_Y = -1.5
        monk.move_to([-2.8,  BASE_Y + monk.height / 2,  0])
        viking.move_to([ 2.8, BASE_Y + viking.height / 2, 0])

        # Shift both above frame, then drop
        monk.shift(UP * 9)
        viking.shift(UP * 9)
        self.play(
            monk.animate.shift(DOWN * 9),
            viking.animate.shift(DOWN * 9),
            run_time=0.5, rate_func=rush_into,
        )

        # "800" slides left to sit under monk; "874" appears under viking
        lbl_800 = Text("800", font="Poppins", weight=BOLD,
                       font_size=52, color=AMBER).move_to([-2.8, -2.2, 0])
        lbl_874 = Text("874", font="Poppins", weight=BOLD,
                       font_size=52, color=AMBER).move_to([ 2.8, -2.2, 0])

        self.play(
            yr800.animate.move_to([-2.8, -2.4, 0]).scale(52 / 120),
            FadeIn(lbl_874),
            run_time=0.4,
        )
        self.remove(yr800)
        self.add(lbl_800)

        # ══════════════════════════════════════════════════════
        # BEAT 4 — Breath zoom during VO hold
        # ══════════════════════════════════════════════════════
        T_setup = 0.4 + 0.25 + 0.3 + 0.4 + 0.15 + 0.5 + 0.4   # no fadein for 874
        zoom_dur = max(self.VD - T_setup, 0)

        self.play(
            lbl_800.animate.scale(1.12),
            lbl_874.animate.scale(1.12),
            run_time=zoom_dur, rate_func=linear,
        )

        # ══════════════════════════════════════════════════════
        # ENDING — Viking exits right, 874 fades, 800 fades,
        # monk shrinks to tiny avatar (continuous into scene 10)
        # ══════════════════════════════════════════════════════
        self.play(
            viking.animate.shift(RIGHT * 12),
            FadeOut(lbl_874),
            run_time=0.5, rate_func=rush_into,
        )
        self.play(FadeOut(lbl_800), run_time=0.3)

        # Monk shrinks to tiny avatar at Ireland position
        # north_atlantic_iceland extent lon -50..25, lat 45..72
        # Ireland lon=-8, lat=53 → x=0.85, y=-1.63
        # north_atlantic_wide extent: lon -100..30, lat 20..75
        # Ireland lon=-8, lat=53 → x=2.95, y=0.8
        IRELAND_POS = np.array([2.95, 0.8, 0])
        self.play(
            monk.animate.set_height(0.75).move_to(IRELAND_POS),
            run_time=0.6,
        )
        # Scene 10 picks up from here — no fadeout
