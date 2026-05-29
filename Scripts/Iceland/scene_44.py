"""Iceland EP1 - Scene 44: IcelandEP1_S44_EndCard
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_44.py IcelandEP1_S44_EndCard
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


class IcelandEP1_S44_EndCard(Scene):
    VD = 14.16  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#000000"
        Text.set_default(font="Poppins")
        channel_txt = Text("History in Minutes", font="Poppins", weight=BOLD,
                           font_size=42, color=WHITE).move_to([0,1.5,0])
        self.play(FadeIn(channel_txt), run_time=1.0)
        next_ep = Text("Part 2: The World Takes Notice", font_size=36, color="#FF812E").move_to([0,0.3,0])
        self.play(FadeIn(next_ep), run_time=1.0)
        sub_btn = RoundedRectangle(corner_radius=0.2, width=3.5, height=0.8,
                                   fill_color="#CC0000", fill_opacity=1, stroke_width=0).move_to([0,-1.0,0])
        sub_txt = Text("Subscribe", font="Poppins", weight=BOLD, font_size=28, color=WHITE).move_to(sub_btn)
        self.play(FadeIn(sub_btn), FadeIn(sub_txt), run_time=0.8)
        self.wait(15.1)

