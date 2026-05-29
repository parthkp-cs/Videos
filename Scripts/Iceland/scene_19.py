"""Iceland EP1 - Scene 19: IcelandEP1_S19_WhyTheyCame
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_19.py IcelandEP1_S19_WhyTheyCame
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


class IcelandEP1_S19_WhyTheyCame(Scene):
    VD = 15.7  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
        norway_map = load_map("norway_coast")
        norway_map.set_width(6).move_to([-2, 0, 0]).set_opacity(0.7)
        self.play(FadeIn(norway_map), run_time=1.5)
        king = load_character("king_Harald_Fairhair", width=2.2).move_to([1.5, 0, 0])
        king_lbl = Text("Harald Fairhair", font_size=22, color="#2B1A0E").next_to(king, DOWN, buff=0.2)
        self.play(FadeIn(king), FadeIn(king_lbl), run_time=1.0)
        arrows = VGroup(*[
            Arrow([-1.0, y, 0],[1.5, y+0.3, 0], color="#FF4444", stroke_width=3)
            for y in [-0.5, 0, 0.5]
        ])
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.3, run_time=1.5))
        t1 = Text("Too crowded.",          font_size=30, color="#2B1A0E").move_to([0, 0.5, 0])
        t2 = Text("Bad king.",             font_size=30, color="#2B1A0E").move_to([0,-0.1, 0])
        t3 = Text("Active volcano? Fine.", font_size=30, color="#C87941").move_to([0,-0.7, 0])
        self.play(FadeIn(t1), run_time=0.5)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), run_time=0.8)
        T = 5.8
        self.wait(max(self.VD - T, 0) + 1.5)

