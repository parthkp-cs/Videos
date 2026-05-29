"""Iceland EP1 - Scene 04: IcelandEP1_S04_EmptyShelves
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_04.py IcelandEP1_S04_EmptyShelves
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


class IcelandEP1_S04_EmptyShelves(Scene):
    VD = 11.04  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003C9E"
        Text.set_default(font="Poppins")
        shelf_lines = VGroup(
            Line([-3.5, 0.6,0],[3.5, 0.6,0], color="#8B5E3C", stroke_width=8),
            Line([-3.5,-0.2,0],[3.5,-0.2,0], color="#8B5E3C", stroke_width=8),
            Line([-3.5,-1.0,0],[3.5,-1.0,0], color="#8B5E3C", stroke_width=8),
        )
        cols = ["#E05A2B","#3A7ABF","#E5C32E","#A0C050","#E05A2B","#3A7ABF","#E5C32E","#A0C050"]
        items = VGroup(*[
            Square(side_length=0.32, fill_color=cols[i%8], fill_opacity=0.9, stroke_width=0)
            .move_to([-3.0+i*0.46, 0.9-int(i/8)*0.8, 0])
            for i in range(16)
        ])
        self.play(FadeIn(shelf_lines), FadeIn(items), run_time=1.0)
        self.play(LaggedStart(*[FadeOut(it) for it in reversed(items)],
                              lag_ratio=0.25, run_time=6.0))
        pop_txt = Text("300,000 people", font_size=32, color="#FF4444").move_to([0, -1.5, 0])
        self.play(FadeIn(pop_txt), run_time=0.8)
        T = 7.8
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

