"""Iceland EP1 - Scene 32: IcelandEP1_S32_SnorriPolitician
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_32.py IcelandEP1_S32_SnorriPolitician
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


class IcelandEP1_S32_SnorriPolitician(Scene):
    VD = 6.79  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#D0E0F0"
        Text.set_default(font="Poppins")
        snorri_o = load_character("snorri_older", width=2.5).move_to([0, 0.3, 0])
        self.play(FadeIn(snorri_o), run_time=1.0)
        shadow = Triangle(fill_color="#000000", fill_opacity=0.55, stroke_width=0)
        shadow.set_width(5).rotate(180*DEGREES).move_to([5, 3, 0])
        self.add(shadow)
        self.play(shadow.animate.move_to([3.5, 1.5, 0]), run_time=1.5)
        pol_txt  = Text("Snorri was also a politician.",     font_size=32, color="#2B1A0E").move_to([0,-1.3,0])
        kill_txt = Text("This eventually got him killed.", font_size=32, color="#8B1A1A").move_to([0,-1.9,0])
        self.play(FadeIn(pol_txt),  run_time=0.8)
        self.play(FadeIn(kill_txt), run_time=0.8)
        T = 4.1
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

