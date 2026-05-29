"""Iceland EP1 - Scene 24: IcelandEP1_S24_ConversionCrisis
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_24.py IcelandEP1_S24_ConversionCrisis
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


class IcelandEP1_S24_ConversionCrisis(Scene):
    VD = 18.6  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        cross_v = Rectangle(width=0.28,height=1.6, fill_color=WHITE, fill_opacity=0.9, stroke_width=0).move_to([-3.0,0.0,0])
        cross_h = Rectangle(width=1.2, height=0.28,fill_color=WHITE, fill_opacity=0.9, stroke_width=0).move_to([-3.0,0.3,0])
        cross = VGroup(cross_v, cross_h)
        hammer_head = Rectangle(width=1.0,height=0.4, fill_color="#C87941", fill_opacity=0.9, stroke_width=0).move_to([3.0, 0.3,0])
        hammer_hndl = Rectangle(width=0.3,height=0.9, fill_color="#C87941", fill_opacity=0.9, stroke_width=0).move_to([3.0,-0.2,0])
        hammer = VGroup(hammer_head, hammer_hndl)
        divider = DashedLine([0,-2.5,0],[0,2.5,0], dash_length=0.2, color="#888888", stroke_width=1.5)
        self.play(FadeIn(cross), FadeIn(hammer), Create(divider), run_time=1.5)
        date_lbl = Text("c. Year 1000", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        title_txt = Text("The Conversion Question", font="Poppins", weight=BOLD, font_size=34, color="#2B1A0E").move_to([0,-1.5,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        self.play(FadeIn(title_txt), run_time=1.0)
        c1 = Text("Christianity", font_size=30, color="#4A90D9").move_to([-1.8,0.0,0])
        c2 = Text("Old Ways",     font_size=30, color="#C87941").move_to([ 1.8,0.0,0])
        self.play(FadeIn(c1), FadeIn(c2), run_time=0.8)
        T = 6.8
        self.wait(max(self.VD - T, 0) + 1.5)

