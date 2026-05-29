"""Iceland EP1 - Scene 33: IcelandEP1_S33_SturlungAge
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_33.py IcelandEP1_S33_SturlungAge
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


class IcelandEP1_S33_SturlungAge(Scene):
    VD = 12.7  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#D72828"
        Text.set_default(font="Poppins")
        clan_map = load_map("iceland_clans")
        self.play(FadeIn(clan_map), run_time=1.5)
        date_lbl = Text("1220 - 1262", font_size=28, color="#FF4444").move_to([-2.4,1.2,0])
        self.play(FadeIn(date_lbl), run_time=0.5)
        sturlung = Text("The Sturlung Age", font="Poppins", weight=BOLD, font_size=40, color="#8B1A1A").move_to([0,0.5,0])
        self.play(FadeIn(sturlung), run_time=1.0)
        arrows = VGroup(*[
            Arrow(start, end, color="#FF4444", stroke_width=3)
            for start, end in [([-2.0,1.0,0],[1.5,-0.5,0]),
                               ([ 1.8,0.8,0],[-1.0,-1.0,0]),
                               ([-0.5,-1.2,0],[2.5,0.5,0])]
        ])
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.4, run_time=3.0))
        civil_war = Text("Iceland's civil war.", font_size=32, color="#FF4444").move_to([0,-1.5,0])
        self.play(FadeIn(civil_war), run_time=0.5)
        T = 6.5
        self.wait(max(self.VD - T, 0) + 1.5)

