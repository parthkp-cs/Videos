"""Iceland EP1 - Scene 41: IcelandEP1_S41_RapidMontage
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_41.py IcelandEP1_S41_RapidMontage
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


class IcelandEP1_S41_RapidMontage(Scene):
    VD = 20.21  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
        segments = [
            ("Althing abolished",                   "#003897", 1.5),
            ("Danish rule begins\n1397",            "#555555", 1.5),
            ("Plague and famine\nPopulation halved","#D72828", 1.5),
            ("Laki eruption\n1783",                 "#8B1010", 2.0),
            ("Althing restored\n1845",              "#003897", 1.5),
            ("Independence\n1944",                  "#003897", 2.0),
            ("2008 crisis\nThey chose differently", "#003C9E", 2.0),
        ]
        for label, bg_col, duration in segments:
            self.camera.background_color = bg_col
            overlay = Rectangle(width=14.22, height=8.0, fill_color=bg_col, fill_opacity=1, stroke_width=0)
            txt = Text(label, font_size=36, color=WHITE, line_spacing=1.2).move_to([0,0,0])
            self.play(FadeIn(overlay), FadeIn(txt), run_time=0.3)
            self.wait(duration - 0.6)
            self.play(FadeOut(overlay), FadeOut(txt), run_time=0.3)
        self.camera.background_color = "#EEF4FC"
        T = 13.0
        self.wait(max(self.VD - T, 0) + 1.5)

