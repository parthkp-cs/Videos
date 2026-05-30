"""Iceland EP1 - Scene 04: IcelandEP1_S04_EmptyShelves
60% — 3 empty shelf photos cycling with dark overlay
40% — bold red text on white: 300,000 people / BANKRUPT
VO: "In days, Iceland's Grocery stores started running short on imported food.
     In a literal sense, country of three hundred thousand people was,
     by every measurable standard, bankrupt."
Render: manim -qh scene_04.py IcelandEP1_S04_EmptyShelves
"""
from manim import *
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
BG = SCRIPT_DIR / "../../Output/Iceland/backgrounds"

sys.path.insert(0, str(SCRIPT_DIR))

STAT_RED = "#CC0000"
DARK_TXT = "#1A1A1A"
GREY_TXT = "#888888"


class IcelandEP1_S04_EmptyShelves(Scene):
    VD = 11.04

    # VO split at the 60/40 mark
    VO_PART1 = 16 / 145 * 60   # 6.62s — "...running short on imported food. In a literal sense, country"
    VO_PART2 = 11 / 145 * 60   # 4.55s — "of three hundred thousand people was...bankrupt."

    def construct(self):
        self.camera.background_color = "#000000"
        Text.set_default(font="Poppins")

        FW = config.frame_width    # 14.222
        FH = config.frame_height   # 8.0

        # ══════════════════════════════════════════════════════
        # PART 1 — Images (60% of scene)
        # 3 photos, ~2s each, smooth crossfade between them
        # ══════════════════════════════════════════════════════
        img_paths = [
            BG / "empty_shelf_01.jpg",
            BG / "empty_shelf_02.jpg",
            BG / "empty_shelf_03.jpg",
        ]

        def make_img(path):
            img = ImageMobject(str(path))
            img.set_width(FW)
            img.move_to(ORIGIN)
            return img

        # Dark overlay — sits above images, stays throughout Part 1
        overlay = Rectangle(width=FW, height=FH,
                            fill_color=BLACK, fill_opacity=0.42, stroke_width=0)

        # Caption strip at bottom
        caption = Text("October 2008 — Reykjavík", font="Poppins",
                       font_size=22, color=WHITE, slant=ITALIC)
        caption.move_to([0, -3.5, 0])

        imgs   = [make_img(p) for p in img_paths]
        HOLD   = 1.6   # hold time per image after it's fully visible
        FADE   = 0.4   # crossfade duration

        # Image 1 fade in
        self.play(FadeIn(imgs[0]), FadeIn(overlay), FadeIn(caption), run_time=0.6)
        self.wait(HOLD)

        # Images 2 and 3 — crossfade
        for i in range(1, 3):
            self.play(FadeOut(imgs[i - 1]), FadeIn(imgs[i]), run_time=FADE)
            self.wait(HOLD)

        # Sync remaining Part 1 VO time
        T1 = 0.6 + 2 * (FADE + HOLD) + HOLD
        self.wait(max(self.VO_PART1 - T1, 0))

        # ── Wipe to white ──────────────────────────────────
        white = Rectangle(width=FW, height=FH,
                          fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.play(FadeIn(white), run_time=0.45)
        self.clear()

        # ══════════════════════════════════════════════════════
        # PART 2 — Red text on white (40% of scene)
        # ══════════════════════════════════════════════════════
        self.camera.background_color = WHITE

        stat = Text("300,000 people.", font="Poppins", weight=BOLD,
                    font_size=54, color=STAT_RED)
        sub  = Text("by every measurable standard,", font="Poppins",
                    font_size=34, color=DARK_TXT)
        bang = Text("BANKRUPT.", font="Poppins", weight=BOLD,
                    font_size=88, color=STAT_RED)

        VGroup(stat, sub, bang).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(stat,  shift=UP * 0.25), run_time=0.4)
        self.play(FadeIn(sub),                    run_time=0.3)
        self.play(FadeIn(bang,  scale=1.6),        run_time=0.45, rate_func=rush_into)

        T2 = 0.45 + 0.4 + 0.3 + 0.45   # wipe + text animations
        self.wait(max(self.VO_PART2 - T2, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
