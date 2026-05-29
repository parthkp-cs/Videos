"""Iceland EP1 - Scene 31: IcelandEP1_S31_SnorriAndMarvel
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_31.py IcelandEP1_S31_SnorriAndMarvel
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


class IcelandEP1_S31_SnorriAndMarvel(Scene):
    VD = 28.73  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#EAF0F8"
        Text.set_default(font="Poppins")
        snorri_y = load_character("snorri_young", width=2.5).move_to([-1.5, 0, 0])
        self.play(FadeIn(snorri_y), run_time=1.0)
        lbl = Text("Snorri Sturluson  -  born 1179", font_size=22, color="#2B1A0E").next_to(snorri_y, DOWN, buff=0.2)
        self.play(FadeIn(lbl), run_time=0.5)
        book_bg    = Rectangle(width=1.5, height=2.0, fill_color="#8A6030", fill_opacity=0.9, stroke_width=0).move_to([2.5,0,0])
        book_title = Text("Prose Edda", font_size=16, color=WHITE).move_to(book_bg.get_center())
        self.play(FadeIn(book_bg), FadeIn(book_title), run_time=1.0)
        for name, pos in [("Odin",[-3.5,0.8,0]),("Thor",[-3.5,0.0,0]),("Loki",[-3.5,-0.8,0])]:
            g = Text(name, font_size=24, color="#C87941").move_to(pos)
            self.play(FadeIn(g), run_time=0.5)
        if_we      = Text("If we know Norse mythology today...", font_size=28, color="#5A4A3A").move_to([0,-1.5,0])
        its_snorri = Text("it's because Snorri wrote it down.", font="Poppins", weight=BOLD, font_size=34, color="#8A9A6A").move_to([0,-2.0,0])
        self.play(FadeIn(if_we),     run_time=0.8)
        self.play(FadeIn(its_snorri), run_time=1.0)
        snorri_o = load_character("snorri_older", width=2.5).move_to([-1.5, 0, 0])
        self.play(FadeTransform(snorri_y, snorri_o), run_time=2.0)
        T = 10.3
        self.wait(max(self.VD - T, 0) + 1.5)

