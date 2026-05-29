"""Iceland EP1 - Scene 18: IcelandEP1_S18_GreatMigration
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_18.py IcelandEP1_S18_GreatMigration
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


class IcelandEP1_S18_GreatMigration(Scene):
    VD = 18.31  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#F5F8FD"
        Text.set_default(font="Poppins")
        import random; random.seed(42)
        iceland_map = load_map("iceland_overview")
        self.play(FadeIn(iceland_map), run_time=1.0)
        dots = VGroup(*[
            Dot(point=[random.uniform(-3.5,3.5), random.uniform(-1.5,1.5), 0],
                radius=0.08, color="#C87941")
            for _ in range(40)
        ])
        pop_lbl = Text("0", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.add(pop_lbl)
        groups = [dots[i:i+8] for i in range(0,40,8)]
        pop_vals = ["8,000","12,000","16,000","20,000","20,000"]
        for grp, pop in zip(groups, pop_vals):
            self.play(LaggedStart(*[FadeIn(d) for d in grp], lag_ratio=0.1, run_time=1.2))
            new_lbl = Text(pop, font_size=24, color="#888888").move_to([-2.4,1.2,0])
            self.play(FadeTransform(pop_lbl, new_lbl), run_time=0.2)
            pop_lbl = new_lbl
        date_lbl = Text("874 - 930 AD", font_size=24, color="#888888").move_to([-2.4,1.2,0])
        self.play(FadeTransform(pop_lbl, date_lbl), run_time=0.5)
        T = 7.5
        self.wait(max(self.VD - T, 0) + 1.5)

