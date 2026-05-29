"""Iceland EP1 - Scene 27: IcelandEP1_S27_ErikExiled
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_27.py IcelandEP1_S27_ErikExiled
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


class IcelandEP1_S27_ErikExiled(Scene):
    VD = 18.41  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        erik = load_character("erik_the_red", width=2.5).move_to([-5.0, 0, 0])
        self.play(erik.animate.move_to([0.0, 0, 0]), run_time=1.0)
        lbl  = Text("Erik the Red",             font_size=26, color="#2B1A0E")
        sub  = Text("982 AD  -  twice exiled",  font_size=20, color="#888888")
        lbls = VGroup(lbl, sub).arrange(DOWN, buff=0.1).next_to(erik, DOWN, buff=0.2)
        self.play(FadeIn(lbls), run_time=0.5)
        exile_txt = Text("EXILE", font="Poppins", weight=BOLD, font_size=36, color="#FF4444").next_to(erik, UP, buff=0.3)
        self.play(FadeIn(exile_txt), run_time=0.8)
        map_lbl = Text("3 years exile.", font_size=28, color="#888888").move_to([2.5, 0, 0])
        self.play(FadeIn(map_lbl), run_time=0.5)
        ocean = Rectangle(width=14.22, height=8.0, fill_color="#003060", fill_opacity=0.7, stroke_width=0)
        self.play(FadeOut(map_lbl), FadeIn(ocean), run_time=1.5)
        west = Text("He went west anyway.", font_size=34, color="#C87941").move_to([0, 0, 0])
        self.play(FadeIn(west), run_time=0.8)
        T = 6.1
        self.wait(max(self.VD - T, 0) + 1.5)

