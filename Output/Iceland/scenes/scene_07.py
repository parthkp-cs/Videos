"""Iceland EP1 - Scene 07: IcelandEP1_S07_Recovered
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_07.py IcelandEP1_S07_Recovered
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


class IcelandEP1_S07_Recovered(Scene):
    VD = 2.23  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003897"
        Text.set_default(font="Poppins")
        flag_bg  = Rectangle(width=4.5, height=3.0,  fill_color="#003897", fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        cross_v  = Rectangle(width=0.62,height=3.0,  fill_color="#FFFFFF", fill_opacity=1, stroke_width=0).move_to([-0.7,0,0])
        cross_h  = Rectangle(width=4.5, height=0.55, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cross_vr = Rectangle(width=0.40,height=3.0,  fill_color="#D72828", fill_opacity=1, stroke_width=0).move_to([-0.7,0,0])
        cross_hr = Rectangle(width=4.5, height=0.35, fill_color="#D72828", fill_opacity=1, stroke_width=0)
        flag = VGroup(flag_bg, cross_h, cross_v, cross_hr, cross_vr)
        self.play(FadeIn(flag), run_time=0.8)
        self.play(flag.animate.scale(1.03), run_time=1.0)
        self.play(flag.animate.scale(1/1.03), run_time=1.0)
        T = 2.8
        self.wait(max(self.VD - T, 0) + 1.5)

