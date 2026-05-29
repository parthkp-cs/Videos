"""Iceland EP1 - Scene 08: IcelandEP1_S08_TimeRewind
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_08.py IcelandEP1_S08_TimeRewind
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


class IcelandEP1_S08_TimeRewind(Scene):
    VD = 7.2  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003897"
        Text.set_default(font="Poppins")
        sea_map = load_map("north_atlantic_dark")
        sea_map.set_opacity(0.8)
        self.add(sea_map)
        self.play(sea_map.animate.scale(0.15), run_time=3.0)
        years = ["2008","1944","1874","1262","1000","874"]
        yr_txt = Text(years[0], font_size=40, color="#C87941").move_to([0,-0.5,0])
        self.play(FadeIn(yr_txt), run_time=0.2)
        for y in years[1:]:
            new_t = Text(y, font_size=40, color="#C87941").move_to([0,-0.5,0])
            self.play(FadeTransform(yr_txt, new_t), run_time=0.15)
            yr_txt = new_t
        self.play(FadeOut(yr_txt), run_time=0.3)
        year_lbl = Text("874 AD", font="Poppins", weight=BOLD, font_size=80, color="#C87941").move_to([0,0,0])
        self.play(FadeIn(year_lbl), run_time=1.5)
        glow = Rectangle(width=5, height=1.8, fill_color="#C87941", fill_opacity=0, stroke_width=0).move_to(year_lbl)
        self.add(glow)
        self.play(glow.animate.set_fill(opacity=0.12), run_time=2.0)
        T = 7.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

