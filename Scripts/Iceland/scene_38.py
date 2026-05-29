"""Iceland EP1 - Scene 38: IcelandEP1_S38_OldCovenant
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_38.py IcelandEP1_S38_OldCovenant
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


class IcelandEP1_S38_OldCovenant(Scene):
    VD = 21.34  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#A01818"
        Text.set_default(font="Poppins")
        iceland_map = load_map("iceland_overview")
        iceland_map.set_opacity(0.5)
        self.play(FadeIn(iceland_map), run_time=2.0)
        year_lbl = Text("1262", font_size=40, color="#8B1A1A").move_to([-2.4,1.2,0])
        over_lbl = Text("The Commonwealth: over.", font_size=32, color="#5A4A3A").move_to([0,0.5,0])
        self.play(FadeIn(year_lbl), run_time=0.8)
        self.play(FadeIn(over_lbl), run_time=0.8)
        seal_rect = Rectangle(width=2.5, height=1.5, fill_color="#C42020", fill_opacity=0.85,
                              stroke_color=WHITE, stroke_width=1.5)
        seal_txt  = Text("NORWAY", font_size=22, color=WHITE).move_to(seal_rect)
        seal = VGroup(seal_rect, seal_txt).move_to([1.5,-0.5,0])
        self.play(FadeIn(seal), run_time=1.5)
        self.play(FadeOut(over_lbl), run_time=0.3)
        exhausted = Text("Chieftains: exhausted.", font_size=28, color="#888888").move_to([0,-0.3,0])
        bloodshed = Text("Bloodshed: too high.",   font_size=28, color="#888888").move_to([0,-0.8,0])
        self.play(FadeIn(exhausted), run_time=0.8)
        self.play(FadeIn(bloodshed), run_time=0.8)
        cta = make_subscribe_cta()
        self.play(FadeIn(cta), run_time=0.5)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.play(ScaleInPlace(cta, 1.05, rate_func=there_and_back), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(cta), run_time=0.5)
        T = 6.7
        self.wait(max(self.VD - T, 0) + 1.5)

