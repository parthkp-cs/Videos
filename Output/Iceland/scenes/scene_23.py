"""Iceland EP1 - Scene 23: IcelandEP1_S23_ItWorked
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_23.py IcelandEP1_S23_ItWorked
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


class IcelandEP1_S23_ItWorked(Scene):
    VD = 7.9  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
        timeline  = Line([-4.5,0.5,0],[4.5,0.5,0], color="#8A9A6A", stroke_width=3)
        left_lbl  = Text("930 AD", font_size=22, color="#8A9A6A").move_to([-4.5,0.9,0])
        right_lbl = Text("Today",  font_size=22, color="#8A9A6A").move_to([ 4.5,0.9,0])
        self.play(Create(timeline), FadeIn(left_lbl), FadeIn(right_lbl), run_time=1.5)
        tick = Dot([-4.3,0.5,0], radius=0.12, color="#C87941")
        self.play(tick.animate.move_to([4.3,0.5,0]), run_time=0.5)
        not_perfect = Text("Not a perfect democracy.", font_size=28, color="#5A4A3A").move_to([0,-0.3,0])
        but_worked  = Text("But it worked.", font="Poppins", weight=BOLD, font_size=40, color="#8A9A6A").move_to([0,-1.0,0])
        self.play(FadeIn(not_perfect), run_time=0.8)
        self.play(FadeIn(but_worked),  run_time=1.0)
        T = 3.8
        self.wait(max(self.VD - T, 0) + 1.5)

