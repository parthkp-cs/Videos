"""Iceland EP1 - Scene 10: IcelandEP1_S10_TheMonks
Begins exactly where scene 09 ends — same map (north_atlantic_iceland),
same monk avatar (irish_monk_seated_nobg) already at Ireland.
Monk sails from Ireland to Iceland with dashed route line drawing ahead of it.
VO: "Before any Norse settler set foot on the island, a small group of Irish
Christian hermits — the papar — had already been living there. They sailed
north deliberately, looking for the most remote, God-soaked silence..."
Render: manim -qh scene_10.py IcelandEP1_S10_TheMonks
"""
from manim import *
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
MAPS = SCRIPT_DIR / "../../Output/Iceland/maps"
CHAR = SCRIPT_DIR / "../../Output/Iceland/characters"
sys.path.insert(0, str(SCRIPT_DIR))

AMBER    = "#C87941"
DARK_TXT = "#1A1A1A"

# Positions on north_atlantic_wide (extent lon -100..30, lat 20..75)
# x = (lon+100)/130 * 14.22 - 7.11   y = (lat-20)/55 * 8.0 - 4.0
IRELAND_POS = np.array([2.95, 0.80, 0])
ICELAND_POS = np.array([1.86, 2.55, 0])


class IcelandEP1_S10_TheMonks(Scene):
    VD = 19.56

    def construct(self):
        self.camera.background_color = "#D6E8F5"
        Text.set_default(font="Poppins")

        # ── Same map as scenes 02 and 09 ────────────────────────
        sea_map = ImageMobject(str(MAPS / "north_atlantic_wide.png"))
        sea_map.set_width(config.frame_width).move_to(ORIGIN)
        self.add(sea_map)

        # ── Same monk, same size, at Ireland — scene begins mid-action ──
        monk = ImageMobject(str(CHAR / "irish_monk_seated_nobg.png"))
        monk.set_height(0.75).move_to(IRELAND_POS)
        self.add(monk)

        # ── "The Papar" label appears ───────────────────────────
        papar_lbl = Text("The Papar", font="Poppins", weight=BOLD,
                         font_size=26, color=AMBER)
        papar_lbl.next_to(monk, DOWN, buff=0.12)
        desc_lbl = Text("Irish Christian hermits", font="Poppins",
                        font_size=18, color=DARK_TXT)
        desc_lbl.next_to(papar_lbl, DOWN, buff=0.08)

        self.play(FadeIn(papar_lbl), FadeIn(desc_lbl), run_time=0.5)
        self.wait(0.8)

        # ── Dashed route line draws ahead of the monk ──────────
        # Route: straight line Ireland → Iceland (slight northwestward arc)
        route = DashedLine(
            IRELAND_POS, ICELAND_POS,
            color=AMBER, stroke_width=2.5, dash_length=0.18, dashed_ratio=0.55,
        )

        # Labels travel with monk
        ship_grp = Group(monk, papar_lbl, desc_lbl)

        T_intro = 0.5 + 0.8
        sail_time = max(self.VD - T_intro - 2.5, 5.0)

        # Route draws and monk sails simultaneously
        self.play(
            Create(route, run_time=sail_time, rate_func=linear),
            ship_grp.animate(run_time=sail_time, rate_func=linear).move_to(ICELAND_POS),
        )

        # ── Arrived at Iceland — clear travel labels, show arrival ─
        self.play(FadeOut(papar_lbl), FadeOut(desc_lbl), run_time=0.3)

        arrive = Text("c. 800", font="Poppins", weight=BOLD,
                      font_size=26, color=AMBER)
        arrive.next_to(monk, DOWN, buff=0.15)
        self.play(FadeIn(arrive, scale=1.3), run_time=0.3, rate_func=rush_into)
        self.wait(0.4)

        # ── Quote — centred, nothing overlapping ────────────────
        self.play(FadeOut(Group(monk, arrive, route)), run_time=0.4)

        quote = VGroup(
            Text('"...the most remote,', font="Poppins", font_size=32,
                 color=DARK_TXT, slant=ITALIC),
            Text('God-soaked silence."', font="Poppins", weight=BOLD,
                 font_size=36, color=AMBER, slant=ITALIC),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(quote, shift=UP * 0.2), run_time=0.6)

        T = T_intro + sail_time + 0.3 + 0.3 + 0.4 + 0.4 + 0.6
        self.wait(max(self.VD - T, 0) + 1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
