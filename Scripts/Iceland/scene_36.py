"""Iceland EP1 - Scene 36: IcelandEP1_S36_LastWords
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_36.py IcelandEP1_S36_LastWords
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


class IcelandEP1_S36_LastWords(Scene):
    VD = 6.43  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#8B1010"
        Text.set_default(font="Poppins")
        torch_glow = Circle(radius=2.0, fill_color="#C87941", fill_opacity=0.15, stroke_width=0).move_to([3.0,-1.5,0])
        self.play(FadeIn(torch_glow), run_time=0.5)
        snorri = load_character("snorri_older", width=2.0).move_to([-1.5,-0.3,0])
        self.play(FadeIn(snorri), run_time=0.8)
        words_ic = Text("Eigi skal hoggva.", font="Poppins", weight=BOLD, font_size=36, color=WHITE).move_to([0,0.8,0])
        words_en = Text("Do not strike.",    font_size=28, color="#AAAAAA").move_to([0,0.2,0])
        self.play(FadeIn(words_ic), run_time=1.0)
        self.play(FadeIn(words_en), run_time=0.8)
        T = 3.1
        self.wait(max(self.VD - T, 0) + 1.5)

