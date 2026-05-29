"""Iceland EP1 - Scene 12: IcelandEP1_S12_MonkDeparts
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_12.py IcelandEP1_S12_MonkDeparts
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


class IcelandEP1_S12_MonkDeparts(Scene):
    VD = 6.53  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
        ship = Polygon([3.0,-0.5,0],[5.5,-0.5,0],[4.5,0.5,0],
                       fill_color="#5A4A3A", fill_opacity=0.8, stroke_width=0)
        self.play(FadeIn(ship), run_time=1.0)
        monk = load_character("irish_monk_seated", width=2.0).move_to([-1.0, 0, 0])
        self.play(FadeIn(monk), run_time=0.8)
        self.play(monk.animate.move_to([-8, 0, 0]), run_time=2.0)
        farewell = Text("They were never coming back.", font_size=28, color="#5A4A3A").move_to([0,-0.5,0])
        self.play(FadeIn(farewell), run_time=0.8)
        T = 4.6
        self.wait(max(self.VD - T, 0) + 1.5)

