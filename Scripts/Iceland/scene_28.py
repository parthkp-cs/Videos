"""Iceland EP1 - Scene 28: IcelandEP1_S28_Greenland
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_28.py IcelandEP1_S28_Greenland
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


class IcelandEP1_S28_Greenland(Scene):
    VD = 20.98  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        atl_map = load_map("north_atlantic")
        self.play(FadeIn(atl_map), run_time=1.0)
        ship = Triangle(fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ship.set_width(0.5).rotate(-90*DEGREES).move_to([0.5,-0.3,0])
        self.add(ship)
        self.play(ship.animate.move_to([-2.5,-0.2,0]), run_time=3.0)
        gl_name = Text("Greenland", font="Poppins", weight=BOLD, font_size=40, color=WHITE).move_to([-2.5,1.0,0])
        self.play(FadeIn(gl_name), run_time=0.8)
        self.play(FadeOut(gl_name), run_time=0.3)
        ice_desc  = Text("Mostly covered in ice.",  font_size=28, color="#5A4A3A").move_to([0, 0.5,0])
        name_desc = Text("He named it Greenland.",  font_size=30, color="#888888").move_to([0,-0.1,0])
        arrow_lbl = Text("Iceland (the friendly name)", font_size=20, color=AMBER).move_to([2.5,-1.2,0])
        self.play(FadeIn(ice_desc), run_time=0.5)
        self.play(FadeIn(name_desc), run_time=0.5)
        self.play(FadeIn(arrow_lbl), run_time=1.0)
        T = 6.8
        self.wait(max(self.VD - T, 0) + 1.5)

