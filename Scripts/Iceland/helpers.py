"""Iceland EP1 shared helpers imported by every scene file."""
from manim import *
from pathlib import Path

BASE = Path(__file__).resolve().parents[2] / "Output" / "Iceland"
SFX  = BASE / "sfx"
VO   = BASE / "vo"

def load_map(name: str) -> ImageMobject:
    img = ImageMobject(str(BASE / "maps" / f"{name}.png"))
    img.set_width(config.frame_width)
    return img

def load_character(name: str, width: float = 2.5) -> ImageMobject:
    img = ImageMobject(str(BASE / "characters" / f"{name}.png"))
    img.set_width(width)
    return img

def make_subscribe_cta() -> VGroup:
    box   = RoundedRectangle(corner_radius=0.12, width=3.2, height=0.65,
                              fill_color="#CC0000", fill_opacity=0.92,
                              stroke_color=WHITE, stroke_width=1.5)
    label = Text("\U0001f514  Subscribe", font="Poppins", font_size=22, color=WHITE)
    label.move_to(box)
    cta = VGroup(box, label)
    cta.move_to([2.2, -1.2, 0])
    return cta

ICELAND_BLUE  = "#003897"
ICELAND_WHITE = "#FFFFFF"
ICELAND_RED   = "#D72828"
AMBER         = "#C87941"
DARK_TXT      = "#2B1A0E"
WARM_TXT      = "#5A4A3A"
GREY_TXT      = "#888888"
MID_TXT       = "#AAAAAA"
GREEN_ACC     = "#8A9A6A"
DARK_RED      = "#8B1A1A"
RED_ACC       = "#FF4444"
BLUE_ACC      = "#4A90D9"
PURPLE_TXT    = "#5A4A8A"
ORANGE_ACC    = "#FF812E"
CORNER_TL     = [-2.4,  1.2, 0]
BODY_LEFT     = [-1.8,  0.0, 0]
BODY_RIGHT    = [ 1.8,  0.0, 0]
BODY_CTR      = [ 0.0,  0.0, 0]
