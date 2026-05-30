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
    VD = 7.2   # ffprobe confirmed actual TTS duration

    def construct(self):
        self.camera.background_color = "#B3CDE0"  # matches ocean colour of map
        Text.set_default(font="Poppins")
        MAP_PATH = Path(__file__).resolve().parents[2] / "Output/Iceland/maps/north_atlantic_clean.png"
        sea_map = ImageMobject(str(MAP_PATH))
        sea_map.set_height(config.frame_height)   # fill frame top-to-bottom, no black bars
        sea_map.move_to(ORIGIN)
        self.add(sea_map)
        # Year counter — hero of the scene, consistent size, paced to fill VO
        years = ["2008", "1944", "1874", "1262", "1000", "874"]
        FADE_IN   = 0.6
        N_TRANS   = len(years) - 1                           # 5 transitions
        PER_YEAR  = (self.VD - FADE_IN - 1.5) / N_TRANS     # ~1.7s each

        yr_txt = Text(years[0], font="Poppins", weight=BOLD,
                      font_size=120, color="#C87941").move_to(ORIGIN)
        self.play(FadeIn(yr_txt, scale=1.1), run_time=FADE_IN)

        for y in years[1:]:
            new_t = Text(y, font="Poppins", weight=BOLD,
                         font_size=120, color="#C87941").move_to(ORIGIN)
            self.play(FadeTransform(yr_txt, new_t), run_time=PER_YEAR)
            yr_txt = new_t

        # "874" holds as the final frame
        T = FADE_IN + N_TRANS * PER_YEAR
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)

