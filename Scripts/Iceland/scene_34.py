"""Iceland EP1 - Scene 34: IcelandEP1_S34_HakonWatches
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_34.py IcelandEP1_S34_HakonWatches
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


class IcelandEP1_S34_HakonWatches(Scene):
    VD = 13.68  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#C42020"
        Text.set_default(font="Poppins")
        norway_map = load_map("norway_coast")
        norway_map.set_width(5).move_to([-2.5, 0, 0]).set_opacity(0.6)
        self.play(FadeIn(norway_map), run_time=1.0)
        hakon = load_character("hakon", width=2.5).move_to([2.0, 0, 0])
        self.play(FadeIn(hakon), run_time=0.5)
        lbl = Text("King Hakon IV  -  Norway", font_size=22, color=WHITE).next_to(hakon, DOWN, buff=0.2)
        self.play(FadeIn(lbl), run_time=0.5)
        for _ in range(3):
            self.play(hakon.animate.shift(RIGHT*0.05), run_time=0.4)
            self.play(hakon.animate.shift(LEFT*0.05),  run_time=0.4)
        patient = Text("Patient.",     font="Poppins", weight=BOLD, font_size=36, color="#5A4A8A").move_to([2.0,0.8,0])
        calc    = Text("Calculating.", font_size=36, color="#5A4A8A").move_to([2.0,0.2,0])
        self.play(FadeIn(patient), run_time=0.8)
        self.play(FadeIn(calc),    run_time=0.8)
        T = 6.6
        self.wait(max(self.VD - T, 0) + 1.5)

