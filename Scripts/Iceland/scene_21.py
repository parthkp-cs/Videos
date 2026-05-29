"""Iceland EP1 - Scene 21: IcelandEP1_S21_AlthingConvenes
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_21.py IcelandEP1_S21_AlthingConvenes
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


class IcelandEP1_S21_AlthingConvenes(Scene):
    VD = 14.04  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
        valley_map = load_map("thingvellir")
        self.play(FadeIn(valley_map), run_time=1.5)
        date_lbl   = Text("930 AD", font_size=32, color="#C87941").move_to([-2.4,1.2,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        place_name = Text("Thingvellir", font="Poppins", weight=BOLD, font_size=36, color="#2B1A0E").move_to([0,0.5,0])
        self.play(FadeIn(place_name), run_time=0.8)
        rift = DashedLine([-5.0,-0.5,0],[5.0,-0.5,0], dash_length=0.3, dashed_ratio=0.5,
                          color="#888888", stroke_width=2)
        self.play(Create(rift), run_time=2.0)
        althing_txt = Text("The Althing", font="Poppins", weight=BOLD, font_size=40, color="#8A9A6A").move_to([0,-1.2,0])
        self.play(FadeIn(althing_txt), run_time=1.0)
        T = 8.8
        self.wait(max(self.VD - T, 0) + 1.5)

