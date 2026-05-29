"""Iceland EP1 - Scene 26: IcelandEP1_S26_HorsemeatExemption
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_26.py IcelandEP1_S26_HorsemeatExemption
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


class IcelandEP1_S26_HorsemeatExemption(Scene):
    VD = 27.46  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        christianity = Text("Christianity.", font="Poppins", weight=BOLD, font_size=48, color="#2B1A0E").move_to([0,0.5,0])
        self.play(FadeIn(christianity), run_time=1.0)
        hammer_icon = Text("Hammer gone.", font_size=24, color="#888888").move_to([2.5,-0.5,0])
        self.add(hammer_icon)
        self.play(FadeOut(hammer_icon), run_time=1.5)
        cross_v = Rectangle(width=0.3, height=1.8, fill_color=AMBER, fill_opacity=0.8, stroke_width=0)
        cross_h = Rectangle(width=1.2, height=0.3, fill_color=AMBER, fill_opacity=0.8, stroke_width=0).shift(UP*0.5)
        cross = VGroup(cross_v, cross_h).move_to([-3.0, 0, 0])
        self.play(FadeIn(cross), run_time=1.0)
        exceptions = Text("...with exceptions.", font_size=34, color="#C87941").move_to([0,-0.3,0])
        self.play(FadeIn(exceptions), run_time=0.8)
        self.play(FadeOut(christianity), run_time=0.3)
        ex1 = Text("Horsemeat at home: still fine.",    font_size=28, color="#888888").move_to([0, 0.3,0])
        ex2 = Text("Private pagan ritual: still fine.", font_size=28, color="#888888").move_to([0,-0.3,0])
        ex3 = Text("This is peak Iceland.", font="Poppins", weight=BOLD, font_size=30, color="#C87941").move_to([0,-1.0,0])
        self.play(FadeIn(ex1), run_time=0.8)
        self.play(FadeIn(ex2), run_time=0.8)
        self.play(FadeIn(ex3), run_time=1.0)
        T = 6.9
        self.wait(max(self.VD - T, 0) + 1.5)

