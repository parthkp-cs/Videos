"""Iceland EP1 - Scene 05: IcelandEP1_S05_MostCountries
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_05.py IcelandEP1_S05_MostCountries
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


class IcelandEP1_S05_MostCountries(Scene):
    VD = 11.66  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003C9E"
        Text.set_default(font="Poppins")
        puppet = load_character("puppet_most_countries", width=3.0).move_to([0, 0.3, 0])
        strings = VGroup(*[
            Line([puppet.get_center()[0]+dx, puppet.get_top()[1]+0.05,0],
                 [puppet.get_center()[0]+dx, puppet.get_top()[1]+1.1, 0],
                 color="#888888", stroke_width=1.5)
            for dx in [-0.6, 0.0, 0.6]
        ])
        self.play(FadeIn(puppet), run_time=1.0)
        self.play(FadeIn(strings), run_time=0.5)
        for _ in range(3):
            self.play(Rotate(puppet, angle=5*DEGREES),  run_time=0.3)
            self.play(Rotate(puppet, angle=-5*DEGREES), run_time=0.3)
        bail  = Text("Bail out the banks.",     font_size=28, color=WHITE).move_to([0, -1.5, 0])
        repay = Text("Repay the foreign debt.", font_size=28, color=WHITE).move_to([0, -1.2, 0])
        self.play(FadeIn(bail),  run_time=0.8)
        self.play(FadeIn(repay), run_time=0.8)
        T = 5.1
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

