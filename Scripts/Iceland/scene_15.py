"""Iceland EP1 - Scene 15: IcelandEP1_S15_PillarsOverboard
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_15.py IcelandEP1_S15_PillarsOverboard
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


class IcelandEP1_S15_PillarsOverboard(Scene):
    VD = 17.42  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F0F6FE"
        Text.set_default(font="Poppins")
        ocean = Rectangle(width=14.22, height=3, fill_color="#003060",
                          fill_opacity=0.5, stroke_width=0).move_to([0,-2.5,0])
        ship_body = Polygon([-1.5,0.3,0],[1.5,0.3,0],[1.0,-0.5,0],[-1.0,-0.5,0],
                            fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ingolfr = load_character("ingolfr_releasing_pillars", width=1.8).move_to([0, 0.6, 0])
        self.play(FadeIn(ocean), FadeIn(ship_body), FadeIn(ingolfr), run_time=0.5)
        p1 = Rectangle(width=0.2, height=1.2, fill_color="#C87941", fill_opacity=1, stroke_width=0).move_to([-0.4, 0.5, 0])
        p2 = Rectangle(width=0.2, height=1.2, fill_color="#C87941", fill_opacity=1, stroke_width=0).move_to([ 0.4, 0.5, 0])
        self.add(p1, p2)
        self.play(p1.animate.move_to([-2,-2,0]).set_opacity(0),
                  p2.animate.move_to([ 2,-2,0]).set_opacity(0), run_time=0.8)
        t1 = Text("Wherever they land...", font_size=30, color=WHITE).move_to([0,-1.5,0])
        t2 = Text("...that's home.", font="Poppins", weight=BOLD, font_size=36, color="#C87941").move_to([0, 0.3,0])
        self.play(FadeIn(t1), run_time=1.0)
        self.play(FadeIn(t2), run_time=1.0)
        T = 4.0
        self.wait(max(self.VD - T, 0) + 1.5)

