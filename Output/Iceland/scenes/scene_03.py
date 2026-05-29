"""Iceland EP1 - Scene 03: IcelandEP1_S03_TheNumbers
Auto-generated. Update VO_DURATION_ACTUAL after TTS + ffprobe.
Render: manim -qh scene_03.py IcelandEP1_S03_TheNumbers
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


class IcelandEP1_S03_TheNumbers(Scene):
    VD = 11.3  # VO_DURATION_ACTUAL — replace with ffprobe result after TTS

    def construct(self):
        self.camera.background_color = "#003C9E"
        Text.set_default(font="Poppins")
        # Axes
        axes = Axes(x_range=[0,3,1], y_range=[0,12,2],
                    x_length=5, y_length=5,
                    axis_config={"color":WHITE,"stroke_width":2}, tips=False)
        axes.move_to([0, -0.3, 0])
        xl1 = Text("GDP",         font_size=20, color=WHITE).next_to(axes.x_axis.n2p(1), DOWN, buff=0.2)
        xl2 = Text("Bank Assets", font_size=20, color=WHITE).next_to(axes.x_axis.n2p(2), DOWN, buff=0.2)
        self.play(Create(axes), Create(xl1), Create(xl2), run_time=1.0)

        unit = axes.y_axis.unit_size
        bar_gdp = Rectangle(width=0.7, height=unit*1.0,
                            fill_color="#4A90D9", fill_opacity=1, stroke_width=0)
        bar_gdp.align_to(axes.x_axis.n2p(1), DOWN)
        bar_gdp.move_to([axes.x_axis.n2p(1)[0], axes.c2p(0,0.5)[1], 0])
        bar_ast = Rectangle(width=0.7, height=unit*11.0,
                            fill_color="#FF4444", fill_opacity=1, stroke_width=0)
        bar_ast.move_to([axes.x_axis.n2p(2)[0], axes.c2p(0,5.5)[1], 0])

        self.play(DrawBorderThenFill(bar_gdp), run_time=1.0)
        self.play(DrawBorderThenFill(bar_ast), run_time=0.5)
        self.play(bar_ast.animate.shift(UP*1.5).stretch(1.3, 1), run_time=1.0)
        mult = Text("11x", font="Poppins", weight=BOLD, font_size=64, color="#FF4444").move_to([2.2, 1.2, 0])
        self.play(FadeIn(mult), run_time=0.5)
        T = 4.0
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

