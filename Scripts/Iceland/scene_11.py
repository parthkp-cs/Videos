"""Iceland EP1 - Scene 11: IcelandEP1_S11_PerfectExistence
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_11.py IcelandEP1_S11_PerfectExistence
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


class IcelandEP1_S11_PerfectExistence(Scene):
    VD = 7.51  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        self.play(FadeIn(iceland_map), run_time=1.5)
        date_lbl = Text("c. 800 AD", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        txt = Text("Perfectly good solitary existence.", font_size=30, color="#5A4A3A").move_to([0,-1.5,0])
        self.play(FadeIn(txt), run_time=1.0)
        T = 3.0
        self.wait(max(self.VD - T, 0) + 1.5)

