"""Iceland EP1 - Scene 35: IcelandEP1_S35_SeventyMen
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_35.py IcelandEP1_S35_SeventyMen
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


class IcelandEP1_S35_SeventyMen(Scene):
    VD = 6.7  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#0A0A14"
        Text.set_default(font="Poppins")

        # --- Background: farm map at full brightness ---
        farm_map = load_map("reykholt_farm")
        farm_map.set_opacity(1.0)

        # Warm torch-glow behind farmhouse window
        torch_outer = Circle(radius=2.2, fill_color="#C87941", fill_opacity=0.10, stroke_width=0).move_to([0.6, -0.4, 0])
        torch_inner = Circle(radius=0.9,  fill_color="#FF9A00", fill_opacity=0.22, stroke_width=0).move_to([0.6, -0.4, 0])
        self.play(FadeIn(farm_map), FadeIn(torch_outer), FadeIn(torch_inner), run_time=1.0)

        # --- Location label ---
        location_lbl = Text("Reykholt.  Night.", font_size=30, color="#FF6644").move_to([-2.4, 1.2, 0])
        self.play(FadeIn(location_lbl), run_time=0.5)

        # --- Snorri inside the farmhouse ---
        snorri = load_character("snorri_older", width=1.7).move_to([0.5, -0.2, 0])
        snorri_lbl = Text("Snorri", font_size=18, color="#DDDDDD").next_to(snorri, DOWN, buff=0.15)
        self.play(FadeIn(snorri), FadeIn(snorri_lbl), run_time=0.6)

        # --- Three assassin groups converging from left, right, and top ---
        # Each group uses assassins_group.png scaled small
        grp_left  = load_character("assassins_group", width=2.2).move_to([-6.5, -0.2, 0])
        grp_right = load_character("assassins_group", width=2.2).move_to([ 6.5, -0.5, 0])
        grp_top   = load_character("assassins_group", width=1.8).move_to([ 0.0,  3.8, 0])

        self.add(grp_left, grp_right, grp_top)

        # All converge toward Snorri simultaneously
        self.play(
            grp_left.animate.move_to([-2.0, -0.2, 0]),
            grp_right.animate.move_to([ 2.8, -0.2, 0]),
            grp_top.animate.move_to([0.5, 1.2, 0]),
            run_time=2.5,
            rate_func=linear,
        )

        # --- "70 men." stamp with shadow for legibility ---
        seventy_shadow = Text("70 men.", font="Poppins", weight=BOLD,
                               font_size=52, color="#000000").move_to([0.05, -1.55, 0])
        seventy = Text("70 men.", font="Poppins", weight=BOLD,
                       font_size=52, color="#FF2222").move_to([0, -1.5, 0])
        self.play(FadeIn(seventy_shadow), FadeIn(seventy), run_time=0.5)

        T = 4.5
        self.wait(max(self.VD - T, 0) + 1.5)
