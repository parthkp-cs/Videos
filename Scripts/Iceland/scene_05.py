"""Iceland EP1 - Scene 05: IcelandEP1_S05_MostCountries
Intro text on dark → 3 full-screen editorial images (one per VO bullet) → puppet on white
VO: "Most countries, at that point, would have done what their creditors told them to do.
     Bail out the banks. Repay the foreign depositors.
     Take the austerity package. Smile for the IMF cameras."
Render: manim -qh scene_05.py IcelandEP1_S05_MostCountries
"""
from manim import *
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
BG   = SCRIPT_DIR / "../../Output/Iceland/backgrounds"
CHAR = SCRIPT_DIR / "../../Output/Iceland/characters"

sys.path.insert(0, str(SCRIPT_DIR))

STAT_RED = "#CC0000"
DARK_BG  = "#0D1B2A"


class IcelandEP1_S05_MostCountries(Scene):
    VD = 13.24   # 32 words / 145 wpm * 60

    VO_INTRO = 15 / 145 * 60   # 6.21s — "Most countries...told them to do"
    VO_BEAT1 =  4 / 145 * 60   # 1.66s — "Bail out the banks."
    VO_BEAT2 =  4 / 145 * 60   # 1.66s — "Repay the foreign depositors."
    VO_BEAT3 =  4 / 145 * 60   # 1.66s — "Take the austerity package."
    VO_BEAT4 =  5 / 145 * 60   # 2.07s — "Smile for the IMF cameras."

    def construct(self):
        FW = config.frame_width
        FH = config.frame_height
        Text.set_default(font="Poppins")

        # ══════════════════════════════════════════════════════
        # INTRO — dark background, punchy two-line text
        # ══════════════════════════════════════════════════════
        self.camera.background_color = DARK_BG

        line1 = Text("Most countries would have done",
                     font_size=42, color=WHITE)
        line2 = Text("what their creditors told them to do.",
                     font_size=42, color=WHITE)
        VGroup(line1, line2).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(line1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(line2, shift=UP * 0.2), run_time=0.5)
        self.wait(max(self.VO_INTRO - 2.0, 0))   # -1s shorter per user request
        self.play(FadeOut(VGroup(line1, line2)), run_time=0.3)

        # ══════════════════════════════════════════════════════
        # BEATS 1–3 — full-screen image + bottom label bar
        # ══════════════════════════════════════════════════════
        beats = [
            ("scene05_bailout.jpg",   "Bail out the banks.",           self.VO_BEAT1),
            ("scene05_paydebt.jpg",   "Repay the foreign depositors.", self.VO_BEAT2),
            ("scene05_austerity.jpg", "Take the austerity package.",   self.VO_BEAT3),
        ]

        CROSS = 0.35   # crossfade duration

        def make_beat_group(fname, label_text):
            img = ImageMobject(str(BG / fname))
            img.set_width(FW)
            img.move_to(ORIGIN)
            grad = Rectangle(width=FW, height=2.2,
                             fill_color=BLACK, fill_opacity=0.72, stroke_width=0)
            grad.move_to([0, -FH / 2 + 1.1, 0])
            label = Text(label_text, font="Poppins", weight=BOLD,
                         font_size=46, color=WHITE)
            label.move_to([0, -FH / 2 + 0.85, 0])
            return Group(img, grad, label)

        prev = None
        for fname, label_text, vo_dur in beats:
            grp = make_beat_group(fname, label_text)
            if prev is None:
                self.play(FadeIn(grp), run_time=CROSS)
            else:
                self.play(FadeOut(prev), FadeIn(grp), run_time=CROSS)
            self.wait(max(vo_dur - CROSS, 0))
            prev = grp

        # ══════════════════════════════════════════════════════
        # BEAT 4 — puppet on white + red label
        # ══════════════════════════════════════════════════════
        white = Rectangle(width=FW, height=FH,
                          fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.play(FadeOut(prev), FadeIn(white), run_time=0.35)
        self.remove(white)
        self.camera.background_color = WHITE

        puppet = ImageMobject(str(CHAR / "puppet_most_countries.png"))
        puppet.set_height(4.8)
        puppet.move_to([0, 0.4, 0])

        label4 = Text("Smile for the IMF cameras.", font="Poppins", weight=BOLD,
                      font_size=44, color=STAT_RED)
        label4.move_to([0, -3.1, 0])

        self.play(FadeIn(puppet, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(label4), run_time=0.3)

        T4 = 0.35 + 0.4 + 0.3
        self.wait(max(self.VO_BEAT4 - T4, 0) + 1.5)
        # NO FadeOut — scene 06 begins directly with puppet still on screen
