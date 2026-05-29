"""Iceland EP1 - Scene 30: IcelandEP1_S30_IcelandWasWriting
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_30.py IcelandEP1_S30_IcelandWasWriting
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


class IcelandEP1_S30_IcelandWasWriting(Scene):
    VD = 22.27  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        self.play(FadeIn(iceland_map), run_time=1.5)
        quill_trail = Line([-3,0,0],[3,0,0], color=AMBER, stroke_width=2.5)
        self.play(Create(quill_trail), run_time=2.0)
        sagas = VGroup(*[
            Text("Saga", font="Poppins", weight=BOLD, font_size=20, color="#5A4A3A")
            .move_to([2.5, -0.5+i*0.45, 0])
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(s) for s in sagas], lag_ratio=0.5, run_time=2.0))
        while_txt   = Text("While others were exploring...", font_size=28, color="#5A4A3A").move_to([0,-1.2,0])
        writing_txt = Text("Iceland was writing everything down.", font="Poppins", weight=BOLD, font_size=34, color="#2B1A0E").move_to([0,-1.8,0])
        self.play(FadeIn(while_txt),   run_time=0.8)
        self.play(FadeIn(writing_txt), run_time=1.0)
        T = 7.3
        self.wait(max(self.VD - T, 0) + 1.5)

