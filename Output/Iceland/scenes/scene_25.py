"""Iceland EP1 - Scene 25: IcelandEP1_S25_ThorgeIrDecides
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_25.py IcelandEP1_S25_ThorgeIrDecides
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


class IcelandEP1_S25_ThorgeIrDecides(Scene):
    VD = 15.89  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        thorgeir = load_character("thorgeir_under_cloak", width=2.5).move_to([0, 0, 0])
        self.play(FadeIn(thorgeir), run_time=1.0)
        lbl  = Text("Thorgeir Thorkelsson", font_size=22, color="#2B1A0E")
        sub  = Text("Lawspeaker - pagan",   font_size=18, color="#888888")
        lbls = VGroup(lbl, sub).arrange(DOWN, buff=0.1).next_to(thorgeir, DOWN, buff=0.2)
        self.play(FadeIn(lbls), run_time=0.5)
        t_hrs = Text("24 hours.",               font_size=36, color="#C87941").move_to([-2.5, 0.5,0])
        t_sil = Text("Silent. Under his cloak.", font_size=28, color="#5A4A3A").move_to([-2.5,-0.1,0])
        self.play(FadeIn(t_hrs), run_time=0.8)
        self.play(FadeIn(t_sil), run_time=0.8)
        clock_circle = Circle(radius=0.8, color=WHITE, stroke_width=2).move_to([2.5, 0, 0])
        clock_hand   = Line([2.5,0,0],[2.5,0.75,0], color=WHITE, stroke_width=3)
        self.play(Create(clock_circle), Create(clock_hand), run_time=0.5)
        self.play(Rotate(clock_hand, angle=-2*PI, about_point=[2.5,0,0]), run_time=4.0)
        stood = Text("Then he stood up.", font="Poppins", weight=BOLD, font_size=36, color="#2B1A0E").move_to([0,-1.5,0])
        self.play(FadeIn(stood), run_time=1.0)
        T = 8.1
        self.wait(max(self.VD - T, 0) + 1.5)

