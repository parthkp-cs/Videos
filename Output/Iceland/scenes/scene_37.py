"""Iceland EP1 - Scene 37: IcelandEP1_S37_TheyStruck
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_37.py IcelandEP1_S37_TheyStruck
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


class IcelandEP1_S37_TheyStruck(Scene):
    VD = 0.7  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#000000"
        Text.set_default(font="Poppins")
        self.wait(0.2)
        struck = Text("They struck.", font="Poppins", weight=BOLD, font_size=56, color=WHITE).move_to([0,0,0])
        self.play(FadeIn(struck), run_time=1.5)
        T = 2.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(struck), run_time=1.0)

