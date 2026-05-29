"""Iceland EP1 - Scene 09: IcelandEP1_S09_BackUpFurther
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_09.py IcelandEP1_S09_BackUpFurther
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


class IcelandEP1_S09_BackUpFurther(Scene):
    VD = 6.19  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003897"
        Text.set_default(font="Poppins")
        yr_old = Text("874 AD",  font="Poppins", weight=BOLD, font_size=60, color="#C87941").move_to([0,1.2,0])
        yr_new = Text("c. 800s", font="Poppins", weight=BOLD, font_size=60, color="#C87941").move_to([0,1.2,0])
        self.add(yr_old)
        self.play(FadeTransform(yr_old, yr_new), run_time=1.0)
        iceland_map = load_map("iceland_blank")
        iceland_map.set_opacity(0.7).set_width(7)
        self.play(FadeIn(iceland_map), run_time=1.5)
        no_one = Text("No one home. Yet.", font_size=28, color="#888888").move_to([0,-1.5,0])
        self.play(FadeIn(no_one), run_time=0.8)
        T = 3.3
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

