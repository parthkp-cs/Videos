"""Iceland EP1 - Scene 20: IcelandEP1_S20_BuiltGovernment
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_20.py IcelandEP1_S20_BuiltGovernment
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


class IcelandEP1_S20_BuiltGovernment(Scene):
    VD = 7.78  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
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

