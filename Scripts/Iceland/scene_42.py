"""Iceland EP1 - Scene 42: IcelandEP1_S42_OriginalInstinct
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_42.py IcelandEP1_S42_OriginalInstinct
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


class IcelandEP1_S42_OriginalInstinct(Scene):
    VD = 16.61  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
        modern_map = load_map("iceland_modern")
        self.play(FadeIn(modern_map), run_time=2.0)
        ingolfr_sm = load_character("ingolfr_arnarson", width=1.2).move_to([-0.5, 0, 0])
        self.play(FadeIn(ingolfr_sm), run_time=0.8)
        instinct_txt = Text("That original instinct.", font="Poppins", weight=BOLD,
                            font_size=36, color="#C87941").move_to([0,0.8,0])
        self.play(FadeIn(instinct_txt), run_time=1.0)
        t_sail  = Text("Sail into the unknown.",  font_size=28, color="#5A4A3A").move_to([0, 0.0,0])
        self.play(FadeIn(t_sail), run_time=0.8)
        self.play(FadeOut(t_sail), run_time=0.3)
        t_rules = Text("Build your own rules.",   font_size=28, color="#5A4A3A").move_to([0,-0.7,0])
        self.play(FadeIn(t_rules), run_time=0.8)
        self.play(FadeOut(t_rules), run_time=0.3)
        t_hold  = Text("Hold the line.",           font_size=28, color="#5A4A3A").move_to([0,-0.7,0])
        self.play(FadeIn(t_hold), run_time=0.8)
        T = 6.2
        self.wait(max(self.VD - T, 0) + 1.5)

