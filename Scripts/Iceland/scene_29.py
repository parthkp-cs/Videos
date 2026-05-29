"""Iceland EP1 - Scene 29: IcelandEP1_S29_LeifNorthAmerica
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_29.py IcelandEP1_S29_LeifNorthAmerica
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


class IcelandEP1_S29_LeifNorthAmerica(Scene):
    VD = 28.15  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        atl_map = load_map("north_atlantic")
        leif = load_character("leif_eriksson", width=2.5).move_to([3.0, 0, 0])
        self.play(FadeIn(atl_map), FadeIn(leif), run_time=1.0)
        lbl = Text("Leif Eriksson  -  c. 1000 AD", font_size=22, color="#2B1A0E").next_to(leif, DOWN, buff=0.2)
        self.play(FadeIn(lbl), run_time=0.5)
        ship = Triangle(fill_color="#5A3010", fill_opacity=0.9, stroke_width=0)
        ship.set_width(0.5).rotate(-90*DEGREES).move_to([-2.0,-0.5,0])
        self.add(ship)
        self.play(ship.animate.move_to([-5.0,-0.8,0]), run_time=4.0)
        site_lbl = Text("L'Anse aux Meadows", font_size=28, color=WHITE).move_to([-4.5,-0.2,0])
        self.play(FadeIn(site_lbl), run_time=0.5)
        columbus = Text("500 years before Columbus.", font="Poppins", weight=BOLD, font_size=34, color="#C87941").move_to([0,1.2,0])
        evidence = Text("Tree-ring evidence. 1021 AD. Confirmed.", font_size=24, color="#888888").move_to([0,0.6,0])
        self.play(FadeIn(columbus),  run_time=1.0)
        self.play(FadeIn(evidence),  run_time=0.8)
        T = 7.8
        self.wait(max(self.VD - T, 0) + 1.5)

