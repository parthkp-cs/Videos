"""Iceland EP1 - Scene 40: IcelandEP1_S40_WentUnderground
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_40.py IcelandEP1_S40_WentUnderground
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


class IcelandEP1_S40_WentUnderground(Scene):
    VD = 5.42  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#D72828"
        Text.set_default(font="Poppins")
        plain = Rectangle(width=12, height=3, fill_color="#557755", fill_opacity=0.7, stroke_width=0).move_to([0,-0.5,0])
        self.play(FadeIn(plain), run_time=1.5)
        self.play(plain.animate.stretch(1.02, 1), run_time=1.0)
        self.play(plain.animate.stretch(1/1.02, 1), run_time=1.0)
        didnt = Text("It didn't disappear.", font_size=32, color="#C87941").move_to([0,0.8,0])
        under = Text("It went underground.", font="Poppins", weight=BOLD, font_size=36, color=WHITE).move_to([0,0.2,0])
        self.play(FadeIn(didnt), run_time=0.8)
        self.play(FadeIn(under), run_time=0.8)
        T = 5.1
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

