"""Iceland EP1 - Scene 39: IcelandEP1_S39_SurrenderByChoice
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_39.py IcelandEP1_S39_SurrenderByChoice
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


class IcelandEP1_S39_SurrenderByChoice(Scene):
    VD = 26.95  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#B82020"
        Text.set_default(font="Poppins")
        table = Rectangle(width=4, height=0.5, fill_color="#8B6030", fill_opacity=0.9, stroke_width=0).move_to([0,-0.5,0])
        doc   = Rectangle(width=1.5, height=2.0, fill_color="#FFFDE7", fill_opacity=0.9,
                          stroke_color="#888888", stroke_width=1).move_to([0,0.5,0])
        self.play(FadeIn(table), FadeIn(doc), run_time=1.0)
        reps = VGroup(*[Dot([-5+i*0.3,-0.2,0], radius=0.12, color="#EEE") for i in range(5)])
        self.add(reps)
        self.play(reps.animate.shift(RIGHT*4.5), run_time=2.0)
        not_conquest = Text("Not conquest.", font="Poppins", weight=BOLD, font_size=36, color=WHITE).move_to([0,1.2,0])
        surrender    = Text("A surrender by choice.",              font_size=36, color="#C87941").move_to([0,0.6,0])
        iceland_way  = Text("Which is somehow more Icelandic.",    font_size=28, color="#888888").move_to([0,0.0,0])
        self.play(FadeIn(not_conquest), run_time=0.8)
        self.play(FadeIn(surrender),    run_time=0.8)
        self.play(FadeIn(iceland_way),  run_time=0.8)
        T = 8.4
        self.wait(max(self.VD - T, 0) + 1.5)

