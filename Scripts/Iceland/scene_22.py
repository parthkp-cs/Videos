"""Iceland EP1 - Scene 22: IcelandEP1_S22_ThirtyChieftains
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_22.py IcelandEP1_S22_ThirtyChieftains
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


class IcelandEP1_S22_ThirtyChieftains(Scene):
    VD = 23.98  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
        import math
        chieftains = VGroup(*[
            Dot(point=[2.5*math.cos(i*2*PI/36), 2.5*math.sin(i*2*PI/36), 0],
                radius=0.12, color="#C87941")
            for i in range(36)
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in chieftains], lag_ratio=0.06, run_time=1.5))
        count_lbl  = Text("36 chieftains", font_size=30, color="#2B1A0E").move_to([0,0,0])
        self.play(FadeIn(count_lbl), run_time=0.5)
        self.play(chieftains.animate.scale(1.15), run_time=6.0)
        parl_txt  = Text("World's oldest surviving parliament", font_size=28, color="#8A9A6A").move_to([0,-1.2,0])
        still_txt = Text("930 AD  -  still active today",        font_size=24, color="#888888").move_to([0,-1.7,0])
        self.play(FadeIn(parl_txt),  run_time=1.0)
        self.play(FadeIn(still_txt), run_time=0.8)
        cta = make_subscribe_cta()
        self.play(FadeIn(cta), run_time=0.5)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(cta), run_time=0.5)
        T = 9.8
        self.wait(max(self.VD - T, 0) + 1.5)

