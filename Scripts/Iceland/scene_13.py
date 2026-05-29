"""Iceland EP1 - Scene 13: IcelandEP1_S13_FirstInstinct
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_13.py IcelandEP1_S13_FirstInstinct
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


class IcelandEP1_S13_FirstInstinct(Scene):
    VD = 12.26  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
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

