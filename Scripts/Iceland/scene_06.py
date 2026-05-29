"""Iceland EP1 - Scene 06: IcelandEP1_S06_IcelandAnswer
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_06.py IcelandEP1_S06_IcelandAnswer
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


class IcelandEP1_S06_IcelandAnswer(Scene):
    VD = 6.43  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003897"
        Text.set_default(font="Poppins")
        bars = VGroup(*[
            Line([x,-2.0,0],[x,2.0,0], color=GREY, stroke_width=6)
            for x in [-1.0,-0.6,-0.2,0.2,0.6,1.0]
        ]).move_to([-1.5, 0, 0])
        cross_bar = Line([-2.0, 0.8,0],[0.2, 0.8,0], color=GREY, stroke_width=6)
        door = VGroup(bars, cross_bar)
        banker = Text("Banker", font_size=26, color="#FF4444").move_to([-1.5, -0.3, 0])
        self.play(FadeIn(door), run_time=0.8)
        self.play(FadeIn(banker), run_time=0.5)

        flag_bg  = Rectangle(width=1.8,  height=1.2, fill_color="#003897", fill_opacity=1, stroke_color=WHITE, stroke_width=1.5)
        cross_v  = Rectangle(width=0.25, height=1.2, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cross_h  = Rectangle(width=1.8,  height=0.22,fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cross_vr = Rectangle(width=0.16, height=1.2, fill_color="#D72828", fill_opacity=1, stroke_width=0)
        cross_hr = Rectangle(width=1.8,  height=0.14,fill_color="#D72828", fill_opacity=1, stroke_width=0)
        cross_v.move_to([-0.3, 0, 0]); cross_vr.move_to([-0.3, 0, 0])
        flag = VGroup(flag_bg, cross_h, cross_v, cross_hr, cross_vr).move_to([2.2, 0, 0])
        self.play(FadeIn(flag), run_time=0.8)
        self.play(Rotate(flag, angle=2*DEGREES,  about_point=flag.get_left()), run_time=0.5)
        self.play(Rotate(flag, angle=-2*DEGREES, about_point=flag.get_left()), run_time=0.5)
        T = 3.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

