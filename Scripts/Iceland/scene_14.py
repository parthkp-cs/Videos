"""Iceland EP1 - Scene 14: IcelandEP1_S14_IngoflrSetsOut
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_14.py IcelandEP1_S14_IngoflrSetsOut
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


class IcelandEP1_S14_IngoflrSetsOut(Scene):
    VD = 21.5  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EEF4FC"
        Text.set_default(font="Poppins")
        ingolfr = load_character("ingolfr_arnarson", width=2.5).move_to([4, 0, 0])
        self.play(ingolfr.animate.move_to([1.5, 0, 0]), run_time=1.0)
        name_lbl = Text("Ingolfr Arnarson", font_size=26, color="#2B1A0E")
        sub_lbl  = Text("874 AD", font_size=20, color="#888888")
        labels = VGroup(name_lbl, sub_lbl).arrange(DOWN, buff=0.1)
        labels.next_to(ingolfr, DOWN, buff=0.2)
        self.play(FadeIn(labels), run_time=0.5)
        norway_map = load_map("norway_coast")
        norway_map.set_width(6).move_to([-3, 0, 0]).set_opacity(0.7)
        self.play(FadeIn(norway_map), run_time=1.0)
        ship = Triangle(fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ship.set_width(0.8).rotate(-90*DEGREES).move_to([-4, -1.5, 0])
        self.add(ship)
        self.play(ship.animate.move_to([3, -1.5, 0]), run_time=5.0)
        corner_date = Text("874 AD", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.play(FadeIn(corner_date), run_time=0.5)
        T = 8.0
        self.wait(max(self.VD - T, 0) + 1.5)

