"""Iceland EP1 - Scene 16: IcelandEP1_S16_ThreeYears
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_16.py IcelandEP1_S16_ThreeYears
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


class IcelandEP1_S16_ThreeYears(Scene):
    VD = 4.32  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F0F6FE"
        Text.set_default(font="Poppins")
        coast_map = load_map("iceland_coastline")
        self.add(coast_map)
        arc = Arc(radius=2.5, start_angle=-PI/2, angle=2*PI,
                  color="#C87941", stroke_width=2.5)
        self.play(Create(arc), run_time=4.5)
        for i, yr in enumerate(["Year 1", "Year 2", "Year 3"]):
            lbl = Text(yr, font="Poppins", weight=BOLD, font_size=40, color="#2B1A0E").move_to([0,-0.5,0])
            self.play(FadeIn(lbl), run_time=0.1)
            self.wait(0.2)
            if i < 2:
                self.play(FadeOut(lbl), run_time=0.1)
        self.wait(1.0)

