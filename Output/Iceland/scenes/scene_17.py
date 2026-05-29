"""Iceland EP1 - Scene 17: IcelandEP1_S17_ReykjavikFounded
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_17.py IcelandEP1_S17_ReykjavikFounded
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


class IcelandEP1_S17_ReykjavikFounded(Scene):
    VD = 13.75  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        self.add(iceland_map)
        self.play(iceland_map.animate.set_width(10).move_to([0.5,-0.3,0]), run_time=1.5)
        steam = VGroup(*[
            Triangle(fill_color="#AADDFF", fill_opacity=0.5-0.1*i, stroke_width=0)
            .scale(0.4).move_to([-1.5+i*0.3, -0.5+i*0.5, 0])
            for i in range(4)
        ])
        self.play(FadeIn(steam), run_time=1.0)
        self.play(steam.animate.shift(UP*1.0).set_opacity(0), run_time=1.0)
        city_name = Text("Reykjavik", font="Poppins", weight=BOLD, font_size=40, color="#2B1A0E").move_to([0,1.0,0])
        self.play(FadeIn(city_name), run_time=1.0)
        meaning = Text("Smoky Bay.", font_size=28, color="#5A4A3A").next_to(city_name, DOWN, buff=0.3)
        self.play(FadeIn(meaning), run_time=0.8)
        footer = Text("Iceland's capital. Day one.", font_size=26, color="#888888").move_to([0,-1.5,0])
        self.play(FadeIn(footer), run_time=0.8)
        T = 6.4
        self.wait(max(self.VD - T, 0) + 1.5)

