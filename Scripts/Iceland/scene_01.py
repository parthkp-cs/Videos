"""Iceland EP1 - Scene 01: IcelandEP1_S01_TitleCard
Iceland landscape cycling background + flag + title text.
Render: manim -qh scene_01.py IcelandEP1_S01_TitleCard
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from helpers import (ICELAND_BLUE, ICELAND_WHITE, ICELAND_RED)

BG_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\backgrounds")


def make_flag(scale=1.0) -> VGroup:
    """Iceland flag as Manim VGroup. Nordic cross, correct proportions."""
    w, h = 4.0 * scale, 2.67 * scale
    bg      = Rectangle(width=w, height=h, fill_color=ICELAND_BLUE,  fill_opacity=1, stroke_width=0)
    cross_h = Rectangle(width=w, height=h*0.22, fill_color=ICELAND_WHITE, fill_opacity=1, stroke_width=0)
    cross_v = Rectangle(width=w*0.11, height=h, fill_color=ICELAND_WHITE, fill_opacity=1, stroke_width=0).shift(LEFT*w*0.15)
    red_h   = Rectangle(width=w, height=h*0.13, fill_color=ICELAND_RED,   fill_opacity=1, stroke_width=0)
    red_v   = Rectangle(width=w*0.065, height=h, fill_color=ICELAND_RED,  fill_opacity=1, stroke_width=0).shift(LEFT*w*0.15)
    return VGroup(bg, cross_h, cross_v, red_h, red_v)


class IcelandEP1_S01_TitleCard(Scene):
    VD = 15.86

    def construct(self):
        self.camera.background_color = "#000000"
        Text.set_default(font="Poppins")

        # ── Load 3 landscape photos ──────────────────────────────────────────
        imgs = []
        for n in [1, 3, 5]:
            img = ImageMobject(str(BG_DIR / f"iceland_bg_{n:02d}.jpg"))
            img.set_width(config.frame_width)
            # height-fit: ensure full frame coverage
            if img.height < config.frame_height:
                img.set_height(config.frame_height)
            imgs.append(img)

        # ── Dark overlay — sits on top of every photo for text legibility ──
        overlay = Rectangle(
            width=config.frame_width, height=config.frame_height,
            fill_color="#000000", fill_opacity=0.52, stroke_width=0
        )

        # ── Iceland flag (top-right corner) ─────────────────────────────────
        flag = make_flag(scale=0.32)
        flag.move_to([5.5, 3.3, 0])

        # ── Title text ───────────────────────────────────────────────────────
        title = Text("ICELAND", font="Poppins", weight=BOLD,
                     font_size=96, color=WHITE).move_to([0, 0.6, 0])
        subtitle = Text("Forged in Fire. Frozen in Principle.",
                        font_size=34, color="#DDDDDD").next_to(title, DOWN, buff=0.45)
        tagline = Text("The world's first direct democracy",
                       font_size=22, color="#AAAAAA").next_to(subtitle, DOWN, buff=0.25)

        # ── Layer order: photos FIRST, then overlay + text on top ───────────
        # All photos added at once; img2 and img3 start invisible.
        # Overlay and text are added AFTER — they always sit on top.
        imgs[1].set_opacity(0)
        imgs[2].set_opacity(0)
        self.add(imgs[0], imgs[1], imgs[2])  # bottom layers
        self.add(overlay, flag)              # mid layer — always on top of photos

        # Text appears once, holds 5s, then fades out
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(subtitle), run_time=0.8)
        self.play(FadeIn(tagline), run_time=0.6)
        self.wait(5.0)
        self.play(FadeOut(VGroup(title, subtitle, tagline)), run_time=0.8)

        # Crossfade photo 1 → 2 (overlay stays, text gone)
        self.wait(1.0)
        self.play(imgs[1].animate.set_opacity(1),
                  imgs[0].animate.set_opacity(0), run_time=2.0)

        # Crossfade photo 2 → 3
        self.wait(3.0)
        self.play(imgs[2].animate.set_opacity(1),
                  imgs[1].animate.set_opacity(0), run_time=2.0)

        # Hold to fill VO duration
        T = 12.0
        self.wait(max(self.VD - T, 0) + 1.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
