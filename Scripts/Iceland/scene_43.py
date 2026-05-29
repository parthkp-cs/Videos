"""Iceland EP1 - Scene 43: IcelandEP1_S43_FoundationWasLaid
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_43.py IcelandEP1_S43_FoundationWasLaid
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


class IcelandEP1_S43_FoundationWasLaid(Scene):
    VD = 10.75  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003897"
        Text.set_default(font="Poppins")
        atl_map = load_map("north_atlantic_dark")
        atl_map.set_opacity(0.8)
        self.play(FadeIn(atl_map), run_time=1.0)
        oct_lbl = Text("October 2008.", font_size=36, color="#FF4444").move_to([0,0.8,0])
        self.play(FadeIn(oct_lbl), run_time=0.8)
        self.play(FadeOut(oct_lbl), run_time=0.3)
        foundation = Text("The foundation was already there.", font="Poppins", weight=BOLD,
                          font_size=34, color="#C87941").move_to([0,0.5,0])
        since_930  = Text("It had been there since 930.", font_size=28, color="#888888").move_to([0,-0.1,0])
        self.play(FadeIn(foundation), run_time=1.0)
        self.play(FadeIn(since_930),  run_time=0.8)
        T = 3.6
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

