"""Iceland EP1 - Scene 10: IcelandEP1_S10_TheMonks
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_10.py IcelandEP1_S10_TheMonks
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


class IcelandEP1_S10_TheMonks(Scene):
    VD = 19.56  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
        route_map = load_map("ireland_to_iceland_route")
        self.play(FadeIn(route_map), run_time=1.5)
        monk = load_character("irish_monk_packing", width=2.5).move_to([-2.0, 0, 0])
        self.play(FadeIn(monk), run_time=1.0)
        lbl  = Text("The Papar", font_size=24, color="#5A4A3A").next_to(monk, DOWN, buff=0.2)
        desc = Text("Irish Christian hermits", font_size=26, color="#5A4A3A").move_to([0,-1.2,0])
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(FadeIn(desc), run_time=0.8)
        route_line = DashedLine([-4.5,-1.0,0],[1.5,1.5,0],
                                dash_length=0.15, dashed_ratio=0.6,
                                color="#C87941", stroke_width=2.5)
        self.play(Create(route_line), run_time=3.0)
        T = 6.8
        self.wait(max(self.VD - T, 0) + 1.5)

