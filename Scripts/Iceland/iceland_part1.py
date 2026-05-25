"""
iceland_part1.py — Sections A-D: Monks + Ingolfr + Migration + Althing (~310s)
Rebuilt v3: richer visuals, more objects, all text in title case.
"""
import math
import random
from manim import *
from pathlib import Path

WHITE_BG = "#FFFFFF"
DARK     = "#1A1A1A"
RED      = "#CC1B21"
AMBER    = "#D4821A"
BLUE     = "#1E5FA8"
GREEN    = "#2A7A3A"
GREY     = "#5A5A5A"
L_GREY   = "#BBBBBB"
SEA_DARK = "#0F2030"
STONE    = "#7A7060"
BROWN    = "#5A3A1A"
AURORA_G = "#22FF88"
AURORA_T = "#00CCAA"
AURORA_B = "#44BBFF"
H_PAD = 1.5
V_PAD = 0.9

PROD  = Path("C:/Users/parth.pandya/Projects/YouTube/Output/Iceland/Needed Final Files")
MAPS  = PROD / "assets" / "maps"
CHARS = PROD / "assets" / "characters"


# ── Asset loaders ──────────────────────────────────────────────────────────────

def load_map(name, height=7.5):
    p = MAPS / f"{name}.png"
    if p.exists():
        img = ImageMobject(str(p))
        img.set_height(height)
        return img
    return None


def load_char(name, height=3.5):
    p = CHARS / f"{name}.png"
    if p.exists():
        img = ImageMobject(str(p))
        img.set_height(height)
        return img
    return None


# ── Geo stand-ins ──────────────────────────────────────────────────────────────

def make_monk_geo(scale=1.0):
    head = Circle(radius=0.32*scale, fill_color="#C8956A", fill_opacity=1,
                  stroke_color=DARK, stroke_width=1.5)
    robe = Triangle(fill_color=BROWN, fill_opacity=1, stroke_color=DARK,
                    stroke_width=1.5).scale(0.9*scale).next_to(head, DOWN, buff=0.04*scale)
    bald = Circle(radius=0.13*scale, fill_color="#8B6A4A", fill_opacity=0.7,
                  stroke_width=0).move_to(head.get_center() + UP*0.10*scale)
    return VGroup(robe, head, bald)


def make_cross(scale=1.0):
    v = Rectangle(width=0.12*scale, height=0.55*scale,
                  fill_color="#6B4A20", fill_opacity=1, stroke_width=0)
    h = Rectangle(width=0.38*scale, height=0.10*scale,
                  fill_color="#6B4A20", fill_opacity=1, stroke_width=0
                  ).move_to(v.get_center() + UP*0.12*scale)
    return VGroup(v, h)


def make_longship(scale=1.0):
    hull = Polygon(
        [-1.4*scale, 0, 0], [-1.0*scale, -0.35*scale, 0],
        [ 1.0*scale, -0.35*scale, 0], [ 1.4*scale, 0, 0],
        [ 0.8*scale,  0.08*scale, 0], [-0.8*scale,  0.08*scale, 0],
        fill_color="#3A2A1A", fill_opacity=1, stroke_width=0,
    )
    mast = Line(UP*1.2*scale, DOWN*0.05*scale, stroke_color=DARK, stroke_width=3*scale)
    sail = Polygon(
        [0, 1.15*scale, 0], [0.65*scale, 0.3*scale, 0], [-0.65*scale, 0.3*scale, 0],
        fill_color="#D4B88A", fill_opacity=0.9, stroke_width=0,
    )
    # Oar lines on hull
    oars = VGroup(*[
        Line(
            [-0.6*scale + i*0.28*scale, -0.35*scale, 0],
            [-0.7*scale + i*0.28*scale, -0.65*scale, 0],
            stroke_color="#5A3A1A", stroke_width=1.5*scale,
        )
        for i in range(5)
    ])
    return VGroup(hull, mast, sail, oars)


def make_steam(n=3, scale=1.0):
    wisps = []
    for i in range(n):
        x = (i - n//2) * 0.3 * scale
        path = VMobject()
        path.set_points_smoothly([
            [x, 0, 0], [x+0.15*scale, 0.3*scale, 0],
            [x-0.1*scale, 0.6*scale, 0], [x+0.05*scale, 0.9*scale, 0],
        ])
        path.set_stroke(color=GREY, width=2.5, opacity=0.5)
        wisps.append(path)
    return VGroup(*wisps)


def make_iceland_outline():
    pts = [
        [-1.8, 0.8, 0], [-2.1, 0.3, 0], [-2.4, -0.1, 0], [-2.2, -0.5, 0],
        [-1.6, -0.9, 0], [-0.8, -1.1, 0], [0.2, -1.0, 0], [0.9, -0.7, 0],
        [1.6, -0.3, 0], [2.0,  0.3, 0], [1.8,  0.8, 0], [1.2,  1.0, 0],
        [0.4,  1.1, 0], [-0.4, 1.2, 0], [-1.0, 1.0, 0], [-1.5, 0.9, 0],
    ]
    return Polygon(*pts, fill_color="#D4C8A8", fill_opacity=0.7,
                   stroke_color=DARK, stroke_width=2)


def make_pillar(scale=1.0):
    shaft = Rectangle(width=0.22*scale, height=1.4*scale,
                      fill_color="#6B4A20", fill_opacity=1, stroke_width=0)
    cap   = Rectangle(width=0.34*scale, height=0.14*scale,
                      fill_color="#5A3A10", fill_opacity=1, stroke_width=0
                      ).next_to(shaft, UP, buff=0)
    base  = Rectangle(width=0.34*scale, height=0.14*scale,
                      fill_color="#5A3A10", fill_opacity=1, stroke_width=0
                      ).next_to(shaft, DOWN, buff=0)
    knots = VGroup(*[
        Line(LEFT*0.08*scale, RIGHT*0.08*scale,
             stroke_color=AMBER, stroke_width=1.5
             ).move_to(shaft.get_center() + UP*(i*0.28 - 0.28)*scale)
        for i in range(4)
    ])
    return VGroup(base, shaft, cap, knots)


def make_bell(scale=1.0, fill_color=AMBER):
    dome = Arc(radius=0.3*scale, angle=PI, start_angle=0,
               fill_color=fill_color, fill_opacity=1,
               stroke_color=DARK, stroke_width=1.5*scale)
    body = Polygon(
        [-0.3*scale, 0, 0], [-0.44*scale, -0.32*scale, 0],
        [ 0.44*scale, -0.32*scale, 0], [ 0.3*scale, 0, 0],
        fill_color=fill_color, fill_opacity=1,
        stroke_color=DARK, stroke_width=1.5*scale,
    )
    rim = Line([-0.47*scale, -0.32*scale, 0], [0.47*scale, -0.32*scale, 0],
               stroke_color=DARK, stroke_width=3*scale)
    handle = Arc(radius=0.09*scale, angle=PI, start_angle=0,
                 stroke_color=DARK, stroke_width=2.5*scale,
                 fill_opacity=0).move_to([0, (0.3 + 0.09)*scale, 0])
    clapper_rod = Line([0, -0.06*scale, 0], [0, -0.24*scale, 0],
                       stroke_color=DARK, stroke_width=2*scale)
    clapper_ball = Circle(radius=0.07*scale, fill_color=DARK, fill_opacity=1,
                          stroke_width=0).move_to([0, -0.29*scale, 0])
    return VGroup(body, dome, rim, handle, clapper_rod, clapper_ball)


def make_book(scale=1.0, color=BROWN):
    cover = Rectangle(width=0.28*scale, height=0.40*scale, fill_color=color,
                      fill_opacity=1, stroke_color=DARK, stroke_width=1.2*scale)
    spine = Rectangle(width=0.06*scale, height=0.40*scale,
                      fill_color="#2A1A0A", fill_opacity=0.6,
                      stroke_width=0).next_to(cover, LEFT, buff=0)
    pages = Rectangle(width=0.04*scale, height=0.36*scale,
                      fill_color="#F5ECD7", fill_opacity=0.9,
                      stroke_width=0).move_to(cover.get_right() + LEFT*0.02*scale)
    return VGroup(spine, cover, pages)


def make_book_pile(n=14, seed=42):
    random.seed(seed)
    BOOK_COLORS = [BROWN, "#4A2A0A", "#1A3A5A", "#2A4A1A", "#5A1A1A",
                   "#3A3A1A", "#6B4A20", "#2A1A4A"]
    fw, fh = 14.22, 8.0
    books = VGroup()
    for _ in range(n):
        x = random.uniform(-fw/2 + 0.5, fw/2 - 0.5)
        y = random.uniform(-fh/2 + 0.4, fh/2 - 0.4)
        sc = random.uniform(0.7, 1.3)
        rot = random.uniform(-PI/3, PI/3)
        col = random.choice(BOOK_COLORS)
        b = make_book(scale=sc, color=col).move_to([x, y, 0]).rotate(rot)
        books.add(b)
    return books


def make_meditation_arcs(center, n=3, scale=1.0):
    circles = []
    for i in range(n):
        r = 0.45*(i+1)*scale
        c = Circle(radius=r, stroke_color=AMBER,
                   stroke_width=max(1.0, 3.0-i),
                   fill_opacity=0)
        c.set_stroke(opacity=0.75 - i*0.22)
        c.move_to(center)
        circles.append(c)
    return VGroup(*circles)


# ── New visual helpers ─────────────────────────────────────────────────────────

def make_wave_lines(n=3, y_base=-3.0, width=14.0, amplitude=0.18, color=BLUE):
    """Sinusoidal sea wave lines."""
    lines = VGroup()
    steps = 40
    for i in range(n):
        pts = []
        for j in range(steps + 1):
            x = -width/2 + j * (width / steps)
            y = y_base - i * 0.30 + amplitude * math.sin(j * PI / 4.5 + i * 1.3)
            pts.append([x, y, 0])
        wl = VMobject()
        wl.set_points_smoothly(pts)
        wl.set_stroke(color=color, width=max(0.8, 2.0 - i*0.4),
                      opacity=max(0.12, 0.40 - i*0.1))
        lines.add(wl)
    return lines


def make_star_field(n=24, seed=10, y_min=0.5, y_max=4.0):
    """White star dots scattered across upper frame."""
    random.seed(seed)
    stars = VGroup()
    for _ in range(n):
        x = random.uniform(-7.0, 7.0)
        y = random.uniform(y_min, y_max)
        r = random.uniform(0.022, 0.058)
        op = random.uniform(0.4, 1.0)
        stars.add(Dot(point=[x, y, 0], radius=r, color=WHITE, fill_opacity=op))
    return stars


def make_aurora_strips(y_top=3.5, n=4):
    """Horizontal colored strips simulating northern lights."""
    cols = [AURORA_G, AURORA_T, AURORA_B, AURORA_T]
    strips = VGroup()
    for i in range(n):
        h = 0.42 - i * 0.06
        s = Rectangle(
            width=14.22, height=h,
            fill_color=cols[i % len(cols)], fill_opacity=0.0, stroke_width=0,
        ).move_to([0, y_top - i * 0.42, 0])
        strips.add(s)
    return strips


def make_seagull(scale=1.0):
    """Simple V-shaped seagull silhouette."""
    l = Line([-0.22*scale, 0.09*scale, 0], [0, 0, 0],
             stroke_color=WHITE, stroke_width=1.8)
    r = Line([0, 0, 0], [0.22*scale, 0.09*scale, 0],
             stroke_color=WHITE, stroke_width=1.8)
    return VGroup(l, r)


def make_candle(scale=1.0):
    """Wax candle body + two-tone flame."""
    body = Rectangle(width=0.14*scale, height=0.55*scale,
                     fill_color="#FAEBD7", fill_opacity=1,
                     stroke_color="#C8A86A", stroke_width=0.8)
    flame_outer = Polygon(
        [-0.08*scale, 0, 0], [0.08*scale, 0, 0], [0, 0.26*scale, 0],
        fill_color="#FFB830", fill_opacity=0.9, stroke_width=0,
    ).move_to(body.get_top() + UP*0.12*scale)
    flame_inner = Polygon(
        [-0.04*scale, 0, 0], [0.04*scale, 0, 0], [0, 0.15*scale, 0],
        fill_color="#FFFF88", fill_opacity=0.95, stroke_width=0,
    ).move_to(body.get_top() + UP*0.12*scale)
    wax_drip = Rectangle(width=0.04*scale, height=0.12*scale,
                         fill_color="#FAEBD7", fill_opacity=0.85,
                         stroke_width=0).move_to(body.get_right() + DOWN*0.1*scale)
    return VGroup(body, wax_drip, flame_outer, flame_inner)


def make_sun_icon(scale=1.0, color=AMBER):
    """Disk + 8 rays."""
    disk = Circle(radius=0.26*scale, fill_color=color, fill_opacity=1, stroke_width=0)
    rays = VGroup(*[
        Line(
            [math.cos(i*PI/4)*0.32*scale, math.sin(i*PI/4)*0.32*scale, 0],
            [math.cos(i*PI/4)*0.50*scale, math.sin(i*PI/4)*0.50*scale, 0],
            stroke_color=color, stroke_width=2.5*scale,
        )
        for i in range(8)
    ])
    return VGroup(disk, rays)


def make_snowflake(scale=1.0):
    """Six-spoke snowflake from 3 crossed lines."""
    spokes = VGroup(*[
        Line(
            [math.cos(i*PI/3)*0.38*scale, math.sin(i*PI/3)*0.38*scale, 0],
            [-math.cos(i*PI/3)*0.38*scale, -math.sin(i*PI/3)*0.38*scale, 0],
            stroke_color=WHITE, stroke_width=2.2*scale,
        )
        for i in range(3)
    ])
    # Small crossbars
    bars = VGroup()
    for i in range(6):
        ang = i * PI / 3
        mid_x = math.cos(ang) * 0.22 * scale
        mid_y = math.sin(ang) * 0.22 * scale
        perp_ang = ang + PI/2
        b = Line(
            [mid_x + math.cos(perp_ang)*0.08*scale, mid_y + math.sin(perp_ang)*0.08*scale, 0],
            [mid_x - math.cos(perp_ang)*0.08*scale, mid_y - math.sin(perp_ang)*0.08*scale, 0],
            stroke_color=WHITE, stroke_width=1.5*scale,
        )
        bars.add(b)
    center_dot = Dot(ORIGIN, radius=0.04*scale, color=WHITE, fill_opacity=1)
    return VGroup(spokes, bars, center_dot)


def make_lightning_bolt(scale=1.0):
    """Dramatic zigzag lightning bolt."""
    pts = [
        [0.05*scale, 1.3*scale, 0],
        [-0.20*scale, 0.45*scale, 0],
        [0.10*scale, 0.45*scale, 0],
        [-0.18*scale, -0.55*scale, 0],
        [0.08*scale, -0.55*scale, 0],
        [-0.05*scale, -1.3*scale, 0],
    ]
    outer = VMobject()
    outer.set_points_as_corners(pts)
    outer.set_stroke(color="#FFFF88", width=6*scale, opacity=1.0)
    inner = VMobject()
    inner.set_points_as_corners(pts)
    inner.set_stroke(color=WHITE, width=2.5*scale, opacity=1.0)
    return VGroup(outer, inner)


def make_sword(scale=1.0):
    """Norse sword: blade + crossguard + handle + pommel."""
    blade = Polygon(
        [-0.055*scale, 0, 0], [0.055*scale, 0, 0], [0, 0.85*scale, 0],
        fill_color="#C8C8C8", fill_opacity=1, stroke_color="#888888", stroke_width=0.8,
    )
    guard = Rectangle(width=0.38*scale, height=0.09*scale,
                      fill_color="#8B6914", fill_opacity=1, stroke_width=0)
    handle = Rectangle(width=0.11*scale, height=0.34*scale,
                       fill_color=BROWN, fill_opacity=1, stroke_width=0
                       ).next_to(guard, DOWN, buff=0)
    pommel = Ellipse(width=0.22*scale, height=0.14*scale,
                     fill_color="#8B6914", fill_opacity=1,
                     stroke_width=0).next_to(handle, DOWN, buff=0)
    return VGroup(handle, guard, blade, pommel)


def make_throne(scale=1.0):
    """Simple wooden throne."""
    back = Rectangle(width=0.85*scale, height=1.0*scale,
                     fill_color="#7B5A14", fill_opacity=1, stroke_color=DARK, stroke_width=1)
    seat = Rectangle(width=0.85*scale, height=0.14*scale,
                     fill_color="#8B6A18", fill_opacity=1, stroke_color=DARK, stroke_width=1
                     ).next_to(back, DOWN, buff=0)
    leg_l = Rectangle(width=0.11*scale, height=0.48*scale,
                      fill_color="#6B4A10", fill_opacity=1, stroke_width=0
                      ).move_to(seat.get_left() + RIGHT*0.055*scale + DOWN*0.30*scale)
    leg_r = Rectangle(width=0.11*scale, height=0.48*scale,
                      fill_color="#6B4A10", fill_opacity=1, stroke_width=0
                      ).move_to(seat.get_right() + LEFT*0.055*scale + DOWN*0.30*scale)
    arm_l = Rectangle(width=0.09*scale, height=0.42*scale,
                      fill_color="#7B5A14", fill_opacity=1, stroke_width=0
                      ).move_to(seat.get_left() + RIGHT*0.045*scale + UP*0.24*scale)
    arm_r = Rectangle(width=0.09*scale, height=0.42*scale,
                      fill_color="#7B5A14", fill_opacity=1, stroke_width=0
                      ).move_to(seat.get_right() + LEFT*0.045*scale + UP*0.24*scale)
    return VGroup(leg_l, leg_r, arm_l, arm_r, seat, back)


def make_rune_stone(scale=1.0):
    """Carved stone slab with rune marks."""
    stone = RoundedRectangle(corner_radius=0.18*scale,
                             width=1.05*scale, height=1.65*scale,
                             fill_color="#8A7A6A", fill_opacity=1,
                             stroke_color=DARK, stroke_width=1.5)
    runes = VGroup(
        # X rune
        Line([-0.22*scale, 0.60*scale, 0], [0.22*scale, 0.78*scale, 0], stroke_color=DARK, stroke_width=1.5),
        Line([-0.22*scale, 0.78*scale, 0], [0.22*scale, 0.60*scale, 0], stroke_color=DARK, stroke_width=1.5),
        # vertical + cross
        Line([0, 0.42*scale, 0], [0, -0.02*scale, 0], stroke_color=DARK, stroke_width=1.5),
        Line([-0.18*scale, 0.22*scale, 0], [0.18*scale, 0.22*scale, 0], stroke_color=DARK, stroke_width=1.5),
        # arrow rune
        Line([-0.18*scale, -0.14*scale, 0], [0.18*scale, -0.14*scale, 0], stroke_color=DARK, stroke_width=1.5),
        Line([0.08*scale, -0.06*scale, 0], [0.18*scale, -0.14*scale, 0], stroke_color=DARK, stroke_width=1.5),
        Line([0.08*scale, -0.22*scale, 0], [0.18*scale, -0.14*scale, 0], stroke_color=DARK, stroke_width=1.5),
        # X rune 2
        Line([-0.18*scale, -0.34*scale, 0], [0.18*scale, -0.50*scale, 0], stroke_color=DARK, stroke_width=1.5),
        Line([-0.18*scale, -0.50*scale, 0], [0.18*scale, -0.34*scale, 0], stroke_color=DARK, stroke_width=1.5),
    )
    return VGroup(stone, runes)


def make_hot_spring(scale=1.0):
    """Glowing pool ellipse with ripple rings."""
    pool = Ellipse(width=1.4*scale, height=0.55*scale,
                   fill_color="#4A8A9A", fill_opacity=0.75,
                   stroke_color="#88CCDD", stroke_width=1.5)
    ring1 = Ellipse(width=1.7*scale, height=0.65*scale,
                    fill_opacity=0, stroke_color="#88CCDD", stroke_width=1.0,
                    ).set_stroke(opacity=0.5)
    ring2 = Ellipse(width=2.0*scale, height=0.75*scale,
                    fill_opacity=0, stroke_color="#88CCDD", stroke_width=0.6,
                    ).set_stroke(opacity=0.3)
    return VGroup(pool, ring1, ring2)


def make_viking_helmet(scale=1.0):
    """Simple bowl helmet + nose guard."""
    bowl = Ellipse(width=0.7*scale, height=0.45*scale,
                   fill_color="#7A7A7A", fill_opacity=1,
                   stroke_color=DARK, stroke_width=1)
    brim = Rectangle(width=0.75*scale, height=0.1*scale,
                     fill_color="#5A5A5A", fill_opacity=1,
                     stroke_width=0).next_to(bowl, DOWN, buff=-0.05*scale)
    nose = Rectangle(width=0.1*scale, height=0.25*scale,
                     fill_color="#5A5A5A", fill_opacity=1,
                     stroke_width=0).move_to(brim.get_center() + DOWN*0.17*scale)
    horn_l = Triangle(fill_color="#8A7A6A", fill_opacity=0.9,
                      stroke_width=0).scale(0.18*scale
                      ).rotate(-PI/6).move_to(bowl.get_left() + LEFT*0.12*scale + UP*0.04*scale)
    horn_r = Triangle(fill_color="#8A7A6A", fill_opacity=0.9,
                      stroke_width=0).scale(0.18*scale
                      ).rotate(PI/6).move_to(bowl.get_right() + RIGHT*0.12*scale + UP*0.04*scale)
    return VGroup(bowl, brim, nose, horn_l, horn_r)


def make_scroll(scale=1.0):
    """Unrolled parchment scroll."""
    body = Rectangle(width=2.4*scale, height=1.4*scale,
                     fill_color="#F5ECD7", fill_opacity=1,
                     stroke_color="#C8A86A", stroke_width=1.5)
    roll_l = Ellipse(width=0.22*scale, height=1.4*scale,
                     fill_color="#E8D8B0", fill_opacity=1,
                     stroke_color="#C8A86A", stroke_width=1.2
                     ).move_to(body.get_left())
    roll_r = Ellipse(width=0.22*scale, height=1.4*scale,
                     fill_color="#E8D8B0", fill_opacity=1,
                     stroke_color="#C8A86A", stroke_width=1.2
                     ).move_to(body.get_right())
    # Ruled lines on parchment
    lines = VGroup(*[
        Line(body.get_left() + RIGHT*0.2*scale + UP*(0.45 - i*0.22)*scale,
             body.get_right() + LEFT*0.2*scale + UP*(0.45 - i*0.22)*scale,
             stroke_color="#C8A86A", stroke_width=0.8, stroke_opacity=0.5)
        for i in range(5)
    ])
    return VGroup(body, roll_l, roll_r, lines)


def labeled(text_mob, bg_color="#FFFFFF", bg_opacity=0.72,
            pad_h=0.22, pad_v=0.14):
    """Wrap a positioned Text mob in a shaded pill background.
    Returns VGroup(bg_rect, text_mob) — use in FadeIn/FadeOut as one unit."""
    bg = RoundedRectangle(
        corner_radius=0.12,
        width=text_mob.width + pad_h * 2,
        height=text_mob.height + pad_v * 2,
        fill_color=bg_color, fill_opacity=bg_opacity, stroke_width=0,
    ).move_to(text_mob.get_center())
    return VGroup(bg, text_mob)


def make_checkmark(scale=1.0, color=GREEN):
    """Two-segment drawn checkmark. Returns VGroup."""
    stem = Line(
        [-0.18 * scale, 0.0 * scale, 0], [0.0, -0.22 * scale, 0],
        stroke_color=color, stroke_width=5 * scale,
    )
    tick = Line(
        [0.0, -0.22 * scale, 0], [0.34 * scale, 0.30 * scale, 0],
        stroke_color=color, stroke_width=5 * scale,
    )
    return VGroup(stem, tick)


class IcelandPart1(Scene):
    """Sections A-D: Monks + Ingolfr + Migration + Althing. ~310s total."""

    def construct(self):
        self.camera.background_color = WHITE_BG
        self._a2_the_papar()
        self._a3_sailing_to_edge()
        self._a4_they_found_it()
        self._a5_solitary_existence()
        self._a6_norse_arrived()
        self._a7_monks_pack_up()
        self._a8_shared_instinct()
        self._b1_the_man()
        self._b2_Harald_problem()
        self._b3_he_left()
        self._b4_pillars()
        self._b5_three_years()
        self._b6_reykjavik()
        self._b7_furniture()
        self._c1_numbers()
        self._c2_who_they_were()
        self._c3_why_they_came()
        self._c4_refuge()
        self._c5_built_government()
        self._d1_thingvellir()
        self._d2_no_king()
        self._d3_just_laws()
        self._d4_it_worked()

    # ── SECTION A ─────────────────────────────────────────────────────────────

    def _a2_the_papar(self):
        """A2 — Monk appears in first second, scene exits at ~4s.
        VO 'Actually, back up...' plays here; A3 covers the longer sailing VO."""
        self.camera.background_color = WHITE_BG

        parchment = Rectangle(width=14.22, height=8.0,
                              fill_color="#FAF5E8", fill_opacity=0.55,
                              stroke_width=0)
        self.add(parchment)
        self.wait(0.2)

        monk = load_char("irish_monk_seated", height=4.0)
        if monk is None:
            monk = make_monk_geo(scale=1.1)
        monk.move_to(ORIGIN + DOWN * 0.2)
        self.play(FadeIn(monk, shift=UP * 0.15), run_time=0.7)   # monk visible by t≈0.9s

        cross = make_cross(scale=1.4).move_to(LEFT * 2.5 + DOWN * 0.2)
        cross.set_opacity(0)
        self.add(cross)
        self.play(cross.animate.set_opacity(1).shift(UP * 0.25),
                  run_time=0.6, rate_func=smooth)                  # t≈1.5s

        forehead = monk.get_center() + UP * 0.72
        arcs = make_meditation_arcs(forehead, n=3, scale=1.1)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in arcs], lag_ratio=0.2),
            run_time=0.8,
        )                                                          # t≈2.3s

        name_card = Text("The Papar", font="Poppins", weight=BOLD,
                         font_size=38, color=DARK).to_edge(DOWN, buff=V_PAD + 1.0)
        sub_card  = Text("Irish Christian Hermits", font="Poppins", weight=LIGHT,
                         font_size=24, color=GREY, slant=ITALIC
                         ).next_to(name_card, DOWN, buff=0.15)
        self.play(
            FadeIn(name_card, shift=UP * 0.1),
            FadeIn(sub_card,  shift=UP * 0.1),
            run_time=0.4,
        )                                                          # t≈2.7s

        self.wait(0.8)                                             # t≈3.5s

        self.play(
            FadeOut(monk), FadeOut(cross), FadeOut(arcs),
            FadeOut(name_card), FadeOut(sub_card), FadeOut(parchment),
            run_time=0.5,
        )                                                          # exits at t≈4.0s

    def _a3_sailing_to_edge(self):
        """North Atlantic map. Boat sails Ireland → Iceland.
        Wave lines animate at bottom. Seagulls appear at arrival."""
        self.camera.background_color = WHITE_BG

        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(Rectangle(width=14.22, height=8.0,
                               fill_color="#0A1828", fill_opacity=1, stroke_width=0))

        # Wave lines at bottom of sea
        waves = make_wave_lines(n=3, y_base=-3.2, color="#2255AA")
        self.add(waves)

        ireland_pos = [3.0, -2.2, 0]
        iceland_pos = [-0.5, 0.6, 0]

        ire_dot = Dot(ireland_pos, radius=0.14, color=AMBER)
        ire_lbl = labeled(
            Text("Ireland", font="Poppins", weight=SEMIBOLD,
                 font_size=20, color=DARK).next_to(ire_dot, DOWN, buff=0.14),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        self.play(FadeIn(ire_dot), FadeIn(ire_lbl), run_time=0.5)
        self.wait(1.5)   # brief establishing hold before boat departs

        route = VMobject()
        route.set_points_smoothly([ireland_pos, [2.0, 0.5, 0], [0.8, 1.2, 0], iceland_pos])
        route.set_stroke(color=AMBER, width=2.5, opacity=0.85)

        b_hull = Polygon(
            [-0.35, 0, 0], [-0.25, -0.1, 0], [0.25, -0.1, 0], [0.35, 0, 0],
            [0.2, 0.04, 0], [-0.2, 0.04, 0],
            fill_color=BROWN, fill_opacity=1, stroke_width=0,
        )
        b_mast = Line([0, 0.3, 0], [0, -0.04, 0], stroke_color=DARK, stroke_width=2)
        b_sail = Triangle(fill_color="#D4B88A", fill_opacity=0.9,
                          stroke_width=0).scale(0.18).move_to([0, 0.18, 0])
        monk_boat = VGroup(b_hull, b_mast, b_sail).move_to(ireland_pos)

        # Wind streak lines along route
        wind1 = Line([2.2,0.4,0],[1.6,0.6,0], stroke_color=WHITE, stroke_width=1.0, stroke_opacity=0.4)
        wind2 = Line([1.5,0.9,0],[0.9,1.1,0], stroke_color=WHITE, stroke_width=1.0, stroke_opacity=0.35)
        wind3 = Line([0.6,1.0,0],[0.1,0.8,0], stroke_color=WHITE, stroke_width=1.0, stroke_opacity=0.3)

        quote = labeled(
            Text(
                "Somewhere Between The Known World\nAnd The Edge Of It.",
                font="Poppins", weight=LIGHT, font_size=24, color=DARK,
                slant=ITALIC, line_spacing=1.4,
            ).to_corner(UL, buff=V_PAD).shift(RIGHT * 0.3 + DOWN * 0.3),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )

        self.play(Create(route), run_time=2.0)
        self.play(FadeIn(quote, shift=RIGHT * 0.1),
                  FadeIn(wind1), FadeIn(wind2), FadeIn(wind3), run_time=0.6)
        self.play(MoveAlongPath(monk_boat, route), run_time=4.5, rate_func=linear)

        # Arrival: dot pulses, 3 seagulls appear, year tag
        ice_dot = Dot(iceland_pos, radius=0.14, color=GREEN)
        ice_lbl = labeled(
            Text("Iceland", font="Poppins", weight=SEMIBOLD,
                 font_size=20, color=DARK).next_to(ice_dot, UP, buff=0.14),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        self.play(GrowFromCenter(ice_dot), FadeIn(ice_lbl), run_time=0.5)
        for _ in range(2):
            self.play(ice_dot.animate.scale(2.0).set_fill(opacity=0.35), run_time=0.4)
            self.play(ice_dot.animate.scale(0.5).set_fill(opacity=1.0), run_time=0.35)

        # Seagulls at Iceland
        sg1 = make_seagull(0.55).move_to([iceland_pos[0]-1.0, iceland_pos[1]+0.7, 0])
        sg2 = make_seagull(0.42).move_to([iceland_pos[0]+0.7, iceland_pos[1]+1.0, 0])
        sg3 = make_seagull(0.38).move_to([iceland_pos[0]-0.2, iceland_pos[1]+1.3, 0])
        year_tag = labeled(
            Text("~800 AD", font="Poppins", weight=LIGHT,
                 font_size=22, color=DARK).next_to(ice_lbl, UP, buff=0.1),
            bg_color="#FFFDE8", bg_opacity=0.78,
        )
        arrival_txt = labeled(
            Text("First Arrival.", font="Poppins", weight=LIGHT,
                 font_size=22, color=DARK, slant=ITALIC
                 ).to_corner(UL, buff=V_PAD + 0.1).shift(RIGHT * 0.3),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        self.play(
            FadeIn(sg1), FadeIn(sg2), FadeIn(sg3),
            FadeIn(year_tag, shift=UP*0.1), run_time=0.5,
        )
        self.play(
            sg1.animate.shift([-0.3, 0.2, 0]), sg2.animate.shift([0.2, 0.25, 0]),
            sg3.animate.shift([-0.15, 0.18, 0]),
            FadeOut(quote), FadeIn(arrival_txt, shift=DOWN*0.1), run_time=0.8,
        )
        self.wait(5.0)   # hold for remaining VO "somewhere between the known world..."

        self.play(
            FadeOut(route), FadeOut(monk_boat), FadeOut(arrival_txt),
            FadeOut(ire_dot), FadeOut(ire_lbl),
            FadeOut(ice_dot), FadeOut(ice_lbl), FadeOut(year_tag),
            FadeOut(sg1), FadeOut(sg2), FadeOut(sg3),
            FadeOut(wind1), FadeOut(wind2), FadeOut(wind3),
            run_time=0.5,
        )
        self.remove(waves)
        if map_img:
            self.remove(map_img)

    def _a4_they_found_it(self):
        """Iceland highlighted on map. Aurora strips + expanding pulse rings."""
        self.camera.background_color = WHITE_BG

        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            map_bg = Rectangle(width=14.22, height=8.0,
                               fill_color="#0A1828", fill_opacity=1, stroke_width=0)
            self.add(map_bg)

        # Star field in sky
        stars = make_star_field(n=18, seed=5, y_min=1.5, y_max=4.0)
        self.add(stars)

        # Aurora strips at top
        aurora = make_aurora_strips(y_top=3.6, n=3)
        self.add(aurora)
        self.play(
            LaggedStart(*[s.animate.set_fill(opacity=0.12+i*0.03) for i, s in enumerate(aurora)],
                        lag_ratio=0.2),
            run_time=1.0,
        )

        iceland_pos = [-0.5, 0.6, 0]

        highlight = Ellipse(width=3.0, height=1.9,
                            fill_color=AMBER, fill_opacity=0.0,
                            stroke_color=AMBER, stroke_width=3.0).move_to(iceland_pos)
        # Expanding pulse rings
        pulse1 = Ellipse(width=3.4, height=2.2, fill_opacity=0,
                         stroke_color=AMBER, stroke_width=1.2
                         ).set_stroke(opacity=0.5).move_to(iceland_pos)
        pulse2 = Ellipse(width=3.9, height=2.6, fill_opacity=0,
                         stroke_color=AMBER, stroke_width=0.8
                         ).set_stroke(opacity=0.3).move_to(iceland_pos)

        self.add(highlight)
        self.play(
            highlight.animate.set_fill(opacity=0.28).set_stroke(opacity=1.0),
            GrowFromCenter(pulse1), run_time=0.8,
        )
        self.play(
            highlight.animate.set_fill(opacity=0.16).scale(1.06),
            GrowFromCenter(pulse2), run_time=0.7,
        )

        iceland_dot = Dot(point=iceland_pos, radius=0.14, color=AMBER)
        iceland_lbl = Text("Iceland", font="Poppins", weight=SEMIBOLD,
                           font_size=22, color=WHITE
                           ).next_to(highlight, UP, buff=0.18)
        self.play(GrowFromCenter(iceland_dot), FadeIn(iceland_lbl), run_time=0.5)

        text_color = WHITE if map_img else DARK
        t1 = Text("The Place They Found.", font="Poppins", weight=SEMIBOLD,
                  font_size=42, color=text_color).to_edge(DOWN, buff=V_PAD + 0.7)
        self.play(FadeIn(t1, shift=UP * 0.1), run_time=0.5)
        # Highlight breathes (replaces 1.8s dead wait)
        self.play(
            highlight.animate.scale(1.05).set_fill(opacity=0.28),
            pulse1.animate.scale(1.06).set_stroke(opacity=0.35),
            aurora[0].animate.set_fill(opacity=0.18),
            run_time=0.9,
        )
        self.play(
            highlight.animate.scale(1/1.05).set_fill(opacity=0.16),
            pulse1.animate.scale(1/1.06).set_stroke(opacity=0.25),
            aurora[0].animate.set_fill(opacity=0.12),
            run_time=0.9,
        )

        t2 = Text("Today We Call It Iceland.", font="Poppins", weight=SEMIBOLD,
                  font_size=42, color=AMBER).next_to(t1, DOWN, buff=0.22)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.5)
        self.play(
            highlight.animate.scale(1.04).set_fill(opacity=0.22),
            pulse2.animate.scale(1.05).set_stroke(opacity=0.2),
            run_time=1.2,
        )
        self.play(
            highlight.animate.scale(1/1.04).set_fill(opacity=0.16),
            pulse2.animate.scale(1/1.05).set_stroke(opacity=0.15),
            run_time=1.2,
        )
        self.wait(1.0)

        self.play(
            FadeOut(t1), FadeOut(t2), FadeOut(highlight),
            FadeOut(iceland_dot), FadeOut(iceland_lbl),
            FadeOut(pulse1), FadeOut(pulse2), FadeOut(aurora), FadeOut(stars),
            run_time=0.5,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.remove(map_bg)

        self._year_tracker = ValueTracker(800)
        self._year_label = always_redraw(
            lambda: Text(
                f"{int(self._year_tracker.get_value())} AD",
                font="Poppins", weight=BOLD, font_size=30, color=AMBER,
            ).to_corner(UR, buff=V_PAD)
        )
        self.add(self._year_label)

    def _a5_solitary_existence(self):
        """Monk meditating with bell, candle, hot spring, star field.
        Bell swings while year ticks 800 → 860."""
        self.camera.background_color = WHITE_BG

        # Night sky backdrop at top
        night_strip = Rectangle(width=14.22, height=2.8,
                                fill_color="#0A0A1A", fill_opacity=0.45, stroke_width=0
                                ).to_edge(UP, buff=0)
        self.add(night_strip)
        stars = make_star_field(n=20, seed=7, y_min=1.2, y_max=3.8)
        self.add(stars)

        # Aurora at top
        aurora = make_aurora_strips(y_top=3.8, n=3)
        self.add(aurora)
        self.play(
            LaggedStart(*[s.animate.set_fill(opacity=0.10+i*0.02) for i, s in enumerate(aurora)],
                        lag_ratio=0.15),
            run_time=0.8,
        )

        bg_books = make_book_pile(n=18, seed=7)
        for b in bg_books:
            b.set_opacity(0.18)
        self.add(bg_books)

        # Hot spring pool at bottom center
        hot_spring = make_hot_spring(scale=0.9).move_to(DOWN*2.8)
        self.add(hot_spring)

        monk = load_char("irish_monk_seated", height=3.8)
        if monk is None:
            monk = make_monk_geo(scale=1.0)
        monk.move_to(ORIGIN)

        bell = make_bell(scale=0.9, fill_color=AMBER)
        bell.move_to(monk.get_center() + LEFT * 1.8 + DOWN * 0.5)

        # Candle to right of monk
        candle = make_candle(scale=1.1).move_to(monk.get_center() + RIGHT*1.8 + DOWN*0.4)

        lap_book = make_book(scale=1.2, color="#3A5A2A")
        lap_book.move_to(monk.get_center() + DOWN * 0.5).rotate(-PI/6)

        steam = make_steam(n=4, scale=0.9).move_to(monk.get_center() + DOWN * 1.0)
        spring_steam = make_steam(n=3, scale=0.6).move_to(hot_spring.get_center() + UP*0.3)

        self.play(FadeIn(bg_books, run_time=0.6))
        self.play(FadeIn(hot_spring), FadeIn(spring_steam), run_time=0.5)
        self.play(FadeIn(monk), run_time=0.5)
        self.play(
            FadeIn(bell, shift=RIGHT*0.1), FadeIn(lap_book),
            FadeIn(candle, shift=LEFT*0.1), run_time=0.6,
        )
        self.play(Create(steam), run_time=0.7)

        forehead = monk.get_center() + UP * 0.65
        arcs = make_meditation_arcs(forehead, n=4, scale=1.0)
        self.play(LaggedStart(*[GrowFromCenter(a) for a in arcs], lag_ratio=0.35),
                  run_time=1.6)

        quote = Text("A Perfectly Good Solitary Existence.",
                     font="Poppins", weight=LIGHT, font_size=28, color=GREY,
                     slant=ITALIC).to_edge(DOWN, buff=V_PAD * 1.5)

        bell_top = bell.get_top()
        self.play(
            FadeIn(quote, shift=UP * 0.1),
            self._year_tracker.animate.set_value(830),
            bell.animate.rotate(PI/10, about_point=bell_top),
            aurora[0].animate.set_fill(opacity=0.15),
            run_time=2.5,
        )
        self.play(
            self._year_tracker.animate.set_value(860),
            bell.animate.rotate(-PI/10, about_point=bell_top),
            aurora[0].animate.set_fill(opacity=0.10),
            run_time=3.0,
        )

        self.play(
            FadeOut(monk), FadeOut(steam), FadeOut(spring_steam), FadeOut(bell),
            FadeOut(lap_book), FadeOut(candle), FadeOut(hot_spring),
            FadeOut(arcs), FadeOut(quote), FadeOut(bg_books),
            FadeOut(aurora), FadeOut(stars), FadeOut(night_strip),
            run_time=0.5,
        )

    def _a6_norse_arrived(self):
        """874 AD. Lightning bolt + Norse longship + monks depart.
        Year counter ticks 860 → 874."""
        self.camera.background_color = WHITE_BG

        monk = load_char("irish_monk_seated", height=3.0)
        if monk is None:
            monk = make_monk_geo(scale=0.85)
        monk.move_to(LEFT * 2.8 + DOWN * 0.2)
        forehead = monk.get_center() + UP * 0.5
        arcs = make_meditation_arcs(forehead, n=3, scale=0.8)
        self.play(FadeIn(monk), run_time=0.4)
        self.play(LaggedStart(*[GrowFromCenter(a) for a in arcs], lag_ratio=0.35),
                  run_time=1.0)
        self.wait(0.3)

        sea_bg = Rectangle(
            width=14.22, height=8.0,
            fill_color=SEA_DARK, fill_opacity=0, stroke_width=0,
        )
        self.add(sea_bg)

        # Wave lines rise with sea bg
        waves = make_wave_lines(n=3, y_base=-3.0, color="#2255AA")
        self.add(waves)

        ship = make_longship(scale=1.1)
        ship.move_to(RIGHT * 9.0)
        self.add(ship)
        self.play(
            sea_bg.animate.set_fill(opacity=0.60),
            ship.animate.move_to(RIGHT * 2.4),
            self._year_tracker.animate.set_value(874),
            run_time=1.5,
        )
        self.play(*[a.animate.set_stroke(opacity=0.0) for a in arcs], run_time=0.2)

        # Lightning bolt flash when ship arrives
        bolt = make_lightning_bolt(scale=0.85).move_to(RIGHT*2.4 + UP*2.0)
        flash_rect = Rectangle(width=14.22, height=8.0,
                               fill_color=WHITE, fill_opacity=0, stroke_width=0)
        self.add(flash_rect, bolt)
        self.play(flash_rect.animate.set_fill(opacity=0.35), run_time=0.07)
        self.play(flash_rect.animate.set_fill(opacity=0.0),
                  FadeOut(bolt), run_time=0.22)

        # Year label pulses at 874
        self.play(self._year_label.animate.scale(1.18), run_time=0.15, rate_func=rush_into)
        self.play(self._year_label.animate.scale(1/1.18), run_time=0.2)

        slam_text = Text("The Norse Arrived.", font="Poppins", weight=BOLD,
                         font_size=48, color=RED).to_edge(DOWN, buff=V_PAD + 0.3)
        slam_text.shift(RIGHT * 14)
        self.add(slam_text)
        self.play(slam_text.animate.shift(LEFT * 14), run_time=0.45)
        self.wait(1.0)

        flag_pole = Line([0, 0.6, 0], [0, -0.6, 0],
                         stroke_color=DARK, stroke_width=3).move_to(RIGHT * 4.5 + UP * 0.4)
        flag_rect = Rectangle(width=0.55, height=0.36, fill_color=RED,
                              fill_opacity=1, stroke_width=0
                              ).move_to(RIGHT * 4.83 + UP * 0.78)
        settle_lbl = Text("Norse Settle.", font="Poppins", weight=BOLD,
                          font_size=30, color=WHITE).move_to(RIGHT * 4.0 + DOWN * 0.8)
        self.play(Create(flag_pole), FadeIn(flag_rect), FadeIn(settle_lbl), run_time=0.7)
        self.wait(1.2)

        # Store state for A7 to continue with
        self._a6_monk   = monk
        self._a6_ship   = ship
        self._a6_arcs   = arcs
        self._a6_sea_bg = sea_bg
        self._a6_waves  = waves
        self._a6_objs   = (self._year_label, flash_rect, slam_text,
                           flag_pole, flag_rect, settle_lbl)

    def _a7_monks_pack_up(self):
        """A7 — Monks pack bells, books, croziers and leave. ~16s.
        Picks up directly from A6 state (monk left, ship right, sea bg)."""

        monk   = self._a6_monk
        ship   = self._a6_ship
        arcs   = self._a6_arcs
        sea_bg = self._a6_sea_bg
        waves  = self._a6_waves

        # Clear A6 text overlays immediately — they must not persist into A7
        year_label, flash_rect, slam_text, flag_pole, flag_rect, settle_lbl = self._a6_objs
        self.remove(year_label)
        self.play(
            FadeOut(slam_text), FadeOut(flag_pole),
            FadeOut(flag_rect), FadeOut(settle_lbl),
            FadeOut(flash_rect),
            run_time=0.3,
        )

        # Three objects beside the monk: bell, book, crozier (cross as staff)
        bell   = make_bell(scale=0.55, fill_color=AMBER
                           ).move_to(monk.get_center() + LEFT*1.2 + DOWN*0.55)
        book   = make_book(scale=1.1, color=BROWN
                           ).move_to(monk.get_center() + LEFT*0.35 + DOWN*1.0)
        crozier = make_cross(scale=0.8
                             ).move_to(monk.get_center() + RIGHT*0.6 + DOWN*0.4)

        self.play(
            FadeIn(bell, shift=UP*0.1),
            FadeIn(book, shift=UP*0.1),
            FadeIn(crozier, shift=UP*0.1),
            run_time=0.7,
        )

        # Pack each object — they fly into the monk's center (bag)
        bag_pos = monk.get_center() + DOWN * 0.3
        self.play(
            bell.animate.move_to(bag_pos).scale(0.2).set_opacity(0),
            run_time=0.55, rate_func=smooth,
        )
        self.play(
            book.animate.move_to(bag_pos).scale(0.2).set_opacity(0),
            run_time=0.55, rate_func=smooth,
        )
        self.play(
            crozier.animate.move_to(bag_pos).scale(0.2).set_opacity(0),
            run_time=0.55, rate_func=smooth,
        )

        # Text beats
        txt1 = Text("Their Bells. Their Books. Their Croziers.",
                    font="Poppins", weight=SEMIBOLD, font_size=30, color=AMBER
                    ).to_edge(DOWN, buff=V_PAD + 0.9)
        self.play(FadeIn(txt1, shift=UP*0.1), run_time=0.5)
        self.wait(0.6)

        txt2 = Text("They Left.", font="Poppins", weight=BOLD,
                    font_size=46, color=RED).next_to(txt1, DOWN, buff=0.2)
        self.play(FadeIn(txt2, shift=UP*0.1), run_time=0.4)

        # Monk walks left, crossing the ship
        self.play(
            monk.animate.shift(LEFT * 11.0),
            run_time=2.2, rate_func=smooth,
        )
        self.wait(0.6)

        # Full cleanup (A6 text already cleared at start of this method)
        self.play(
            FadeOut(arcs), FadeOut(sea_bg), FadeOut(ship), FadeOut(waves),
            FadeOut(txt1), FadeOut(txt2),
            FadeOut(bell), FadeOut(book), FadeOut(crozier),
            run_time=0.5,
        )
        self.remove(monk)
        self.camera.background_color = WHITE_BG

    def _a8_shared_instinct(self):
        self.camera.background_color = WHITE_BG
        monk_l = load_char("irish_monk_seated", height=2.8)
        if monk_l is None:
            monk_l = make_monk_geo(scale=0.8)
        monk_l.move_to(LEFT*2.8 + UP*0.3)

        cross_l   = make_cross(scale=0.7).move_to(LEFT*4.1 + DOWN*0.4)
        peace_lbl = Text("For Peace.", font="Poppins", weight=LIGHT,
                         font_size=26, color=GREY, slant=ITALIC
                         ).move_to(LEFT*3.0 + DOWN*1.6)

        # Chain-dash divider
        divider = VGroup(*[
            Rectangle(width=0.06, height=0.24, fill_color=L_GREY, fill_opacity=1,
                      stroke_width=0).move_to([0, 3.2 - i*0.35, 0])
            for i in range(18)
        ])

        ship_r    = make_longship(scale=0.8).move_to(RIGHT*2.5 + UP*0.2)
        opin_lbl  = Text("To Escape Opinions.", font="Poppins", weight=LIGHT,
                         font_size=26, color=GREY, slant=ITALIC
                         ).move_to(RIGHT*2.5 + DOWN*1.6)

        self.play(
            FadeIn(monk_l), FadeIn(cross_l), FadeIn(peace_lbl),
            LaggedStart(*[FadeIn(d) for d in divider], lag_ratio=0.04),
            FadeIn(ship_r), FadeIn(opin_lbl),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[d.animate.set_fill(opacity=0.5) for d in divider], lag_ratio=0.04),
            run_time=0.4,
        )
        self.play(
            LaggedStart(*[d.animate.set_fill(opacity=1.0) for d in divider], lag_ratio=0.04),
            run_time=0.4,
        )
        self.wait(0.4)

        self.play(
            FadeOut(monk_l), FadeOut(cross_l), FadeOut(peace_lbl),
            FadeOut(divider), FadeOut(ship_r), FadeOut(opin_lbl),
            run_time=0.5,
        )

        q1 = Text("To Get Away From People", font="Poppins", weight=BOLD,
                  font_size=46, color=AMBER).move_to(UP*1.3)
        q2 = Text("With Opinions", font="Poppins", weight=BOLD,
                  font_size=46, color=AMBER).move_to(UP*0.2)
        q3 = Text("About How They Should Live.", font="Poppins", weight=BOLD,
                  font_size=46, color=AMBER).move_to(DOWN*0.9)

        self.play(AddTextLetterByLetter(q1, time_per_char=0.05), run_time=2.5)
        self.play(AddTextLetterByLetter(q2, time_per_char=0.06), run_time=1.8)
        self.play(AddTextLetterByLetter(q3, time_per_char=0.05), run_time=2.8)

        punchline = Text("That Was Iceland's Founding Philosophy.",
                         font="Poppins", weight=LIGHT, font_size=26,
                         color=GREY, slant=ITALIC).to_edge(DOWN, buff=V_PAD)
        self.play(FadeIn(punchline, shift=UP*0.1), run_time=0.6)
        self.wait(1.8)

        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(punchline), run_time=0.5)

    # ── SECTION B ─────────────────────────────────────────────────────────────

    def _b1_the_man(self):
        self.camera.background_color = WHITE_BG

        # Norway silhouette in background right
        norway_blob = Polygon(
            [3.5,-1.0,0],[4.2,-0.4,0],[5.0,0.2,0],[5.5,1.0,0],[5.2,2.2,0],
            [4.8,2.8,0],[4.2,3.0,0],[3.8,2.6,0],[3.4,1.8,0],[3.2,0.8,0],
            fill_color="#C8B88A", fill_opacity=0.22, stroke_width=0,
        )
        norway_lbl = Text("Norway", font="Poppins", weight=LIGHT, font_size=18,
                          color=GREY).move_to([4.4, 1.0, 0])
        self.add(norway_blob, norway_lbl)

        # Compass rose bottom right
        compass_outer = Circle(radius=0.45, stroke_color=L_GREY, stroke_width=1.2, fill_opacity=0
                               ).move_to(RIGHT*5.5 + DOWN*3.0)
        compass_ticks = VGroup(*[
            Line(
                [5.5 + math.cos(i*PI/4)*0.32, -3.0 + math.sin(i*PI/4)*0.32, 0],
                [5.5 + math.cos(i*PI/4)*0.45, -3.0 + math.sin(i*PI/4)*0.45, 0],
                stroke_color=L_GREY, stroke_width=1.5,
            )
            for i in range(8)
        ])
        compass_n = Text("N", font="Poppins", weight=BOLD, font_size=14, color=GREY
                         ).move_to([5.5, -3.0+0.62, 0])
        compass_needle_n = Triangle(fill_color=RED, fill_opacity=1, stroke_width=0
                                    ).scale(0.10).move_to([5.5, -3.0+0.20, 0])
        compass_needle_s = Triangle(fill_color=GREY, fill_opacity=1, stroke_width=0
                                    ).scale(0.10).rotate(PI).move_to([5.5, -3.0-0.20, 0])
        compass = VGroup(compass_outer, compass_ticks, compass_n,
                         compass_needle_n, compass_needle_s)
        self.add(compass)

        ingolfr = load_char("ingolfr_arnarson", height=3.5)
        if ingolfr is None:
            body = Rectangle(width=0.7, height=1.6, fill_color="#2A4A2A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.3, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=1).move_to(body.get_top()+UP*0.32)
            ingolfr = VGroup(body, head)

        ingolfr.move_to(RIGHT*8.0)
        self.add(ingolfr)
        self.play(ingolfr.animate.move_to(ORIGIN), run_time=0.9)

        # Viking sword to right of Ingolfr
        sword = make_sword(scale=0.9).move_to(RIGHT*1.3 + DOWN*0.2)
        self.play(FadeIn(sword, shift=UP*0.15), run_time=0.5)

        name_lbl = Text("Ingólfr Arnarson", font="Poppins", weight=BOLD,
                        font_size=36, color=DARK).to_edge(DOWN, buff=V_PAD+0.9)
        year_lbl = Text("874 AD", font="Poppins", weight=SEMIBOLD,
                        font_size=28, color=AMBER).next_to(name_lbl, DOWN, buff=0.2)
        self.play(FadeIn(name_lbl, shift=UP*0.1),
                  FadeIn(year_lbl, shift=UP*0.1), run_time=0.6)

        facts = [
            ("Norway's First Exile.", GREY, LIGHT, 22),
            ("Norwegian Chieftain.\nNot A Refugee.", DARK, NORMAL, 22),
            ("A Man With A Plan...\nAnd Very Specific Furniture.", AMBER, LIGHT, 20),
        ]
        fact_mobs = []
        for i, (txt, col, wt, sz) in enumerate(facts):
            fm = Text(txt, font="Poppins", weight=wt, font_size=sz, color=col,
                      line_spacing=1.3)
            fm.to_edge(LEFT, buff=H_PAD).shift(UP * 1.2)
            fact_mobs.append(fm)
            if i > 0:
                self.play(FadeOut(fact_mobs[i-1]), FadeIn(fm, shift=DOWN*0.1), run_time=0.5)
            else:
                self.play(FadeIn(fm, shift=DOWN*0.1), run_time=0.5)
            self.wait(1.0)

        bg_ship = make_longship(scale=0.6)
        bg_ship.set_fill(opacity=0.18).move_to(RIGHT*3.8 + DOWN*0.3)
        self.play(FadeIn(bg_ship, shift=LEFT*0.2), run_time=0.6)
        self.wait(0.5)

        self.play(
            FadeOut(ingolfr), FadeOut(name_lbl), FadeOut(year_lbl),
            FadeOut(bg_ship), FadeOut(sword), FadeOut(norway_blob),
            FadeOut(norway_lbl), FadeOut(compass),
            FadeOut(fact_mobs[-1]),
            run_time=0.5,
        )

    def _b2_Harald_problem(self):
        self.camera.background_color = WHITE_BG
        Harald = load_char("king_Harald_fairhair", height=3.5)
        if Harald is None:
            body  = Rectangle(width=0.9, height=1.8, fill_color="#003090",
                              fill_opacity=1, stroke_width=0)
            head  = Circle(radius=0.32, fill_color="#D4B86A", fill_opacity=1,
                          stroke_width=0).move_to(body.get_top()+UP*0.34)
            cpts  = [[-0.45,0,0],[-0.45,0.4,0],[-0.22,0.25,0],
                     [0,0.55,0],[0.22,0.25,0],[0.45,0.4,0],[0.45,0,0]]
            crown = Polygon(*cpts, fill_color=AMBER, fill_opacity=1,
                            stroke_width=0).move_to(head.get_top()+UP*0.1)
            hl = Rectangle(width=0.15, height=2.2, fill_color=AMBER,
                           fill_opacity=0.9, stroke_width=0
                           ).move_to(body.get_center()+LEFT*0.62+DOWN*0.3)
            hr = Rectangle(width=0.15, height=2.2, fill_color=AMBER,
                           fill_opacity=0.9, stroke_width=0
                           ).move_to(body.get_center()+RIGHT*0.62+DOWN*0.3)
            Harald = VGroup(hl, hr, body, head, crown)
        Harald.move_to(RIGHT*2.8)

        spc_bg  = Ellipse(width=3.2, height=1.0, fill_color=WHITE_BG,
                          fill_opacity=1, stroke_color=L_GREY, stroke_width=1.5
                          ).move_to(RIGHT*2.8+UP*2.8)
        spc_txt = Text('"My Kingdom. Mine."', font="Poppins", weight=LIGHT,
                       font_size=22, color=DARK, slant=ITALIC
                       ).move_to(spc_bg.get_center())

        ingolfr_sm = load_char("ingolfr_arnarson", height=3.5*0.45)
        if ingolfr_sm is None:
            body = Rectangle(width=0.35, height=0.72, fill_color="#2A4A2A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.15, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=0).move_to(body.get_top()+UP*0.16)
            ingolfr_sm = VGroup(body, head)
        ingolfr_sm.move_to(LEFT*4.0+DOWN*0.8)

        # Fleeing figure silhouettes
        flee_figs = VGroup(*[
            VGroup(
                Circle(radius=0.11, fill_color="#C8956A", fill_opacity=1, stroke_width=0),
                Rectangle(width=0.15, height=0.32, fill_color=STONE,
                         fill_opacity=1, stroke_width=0).shift(DOWN*0.22),
            ).move_to(LEFT*(5.2+i*0.5) + DOWN*0.4)
            for i in range(3)
        ])

        self.play(GrowFromCenter(Harald), run_time=0.7)
        self.play(FadeIn(VGroup(spc_bg, spc_txt), scale=0.9), run_time=0.5)
        self.play(FadeIn(ingolfr_sm),
                  LaggedStart(*[FadeIn(f, shift=RIGHT*0.1) for f in flee_figs], lag_ratio=0.2),
                  run_time=0.6)
        self.wait(1.3)

        boundary = Circle(radius=0.5, stroke_color=RED, stroke_width=2.5,
                         fill_opacity=0).move_to(RIGHT*2.8)
        bnd_lbl  = Text("Radius Of Royal Opinions", font="Poppins", weight=LIGHT,
                        font_size=18, color=RED).to_edge(DOWN, buff=V_PAD)
        self.play(GrowFromCenter(boundary), FadeIn(bnd_lbl), run_time=0.5)
        self.play(boundary.animate.scale(7.0).set_stroke(opacity=0.2), run_time=4.0)

        # Tax scroll falls from Harald
        tax_scroll = Rectangle(width=0.4, height=0.6, fill_color="#F5ECD7", fill_opacity=1,
                               stroke_color="#C8A86A", stroke_width=1.0
                               ).move_to(RIGHT*2.8 + UP*0.3)
        tax_lbl = Text("Tax", font="Poppins", weight=BOLD, font_size=14, color=DARK
                       ).move_to(tax_scroll.get_center())
        self.play(FadeIn(VGroup(tax_scroll, tax_lbl)), run_time=0.3)
        self.play(VGroup(tax_scroll, tax_lbl).animate.move_to(RIGHT*1.5 + DOWN*1.5),
                  ingolfr_sm.animate.shift(LEFT*0.8),
                  run_time=0.8)

        shake = Text('"No."', font="Poppins", weight=BOLD,
                     font_size=28, color=AMBER, slant=ITALIC
                     ).next_to(ingolfr_sm, UL, buff=0.1)
        self.play(FadeIn(shake, shift=RIGHT*0.1), run_time=0.4)
        for _ in range(2):
            self.play(ingolfr_sm.animate.shift(RIGHT*0.15), run_time=0.12)
            self.play(ingolfr_sm.animate.shift(LEFT*0.15), run_time=0.12)

        boat_hint = make_longship(scale=0.4).move_to(LEFT*5.5 + DOWN*0.8)
        self.play(FadeIn(boat_hint, shift=RIGHT*0.3), run_time=0.5)

        depart_txt = Text("He Had A Different Plan.", font="Poppins",
                          weight=SEMIBOLD, font_size=26, color=DARK
                          ).next_to(ingolfr_sm, DOWN, buff=0.28)
        self.play(FadeIn(depart_txt, shift=DOWN*0.1), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(Harald), FadeOut(spc_bg), FadeOut(spc_txt),
            FadeOut(ingolfr_sm), FadeOut(boundary), FadeOut(bnd_lbl),
            FadeOut(shake), FadeOut(boat_hint), FadeOut(depart_txt),
            FadeOut(flee_figs), FadeOut(tax_scroll), FadeOut(tax_lbl),
            run_time=0.6,
        )

    def _b3_he_left(self):
        self.camera.background_color = WHITE_BG
        t1 = Text("Ingólfr Didn't Disagree Politely.", font="Poppins",
                  weight=NORMAL, font_size=46, color=DARK).move_to(UP*0.5)
        t2 = Text("He Left.", font="Poppins", weight=BOLD,
                  font_size=72, color=RED).move_to(DOWN*0.6)
        self.play(FadeIn(t1, shift=DOWN*0.1), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(t2, shift=DOWN*0.15), run_time=0.45)

        # Longship sails across bottom with wake trail behind
        exit_ship = make_longship(scale=0.7).move_to(RIGHT*9.0 + DOWN*2.2)
        self.add(exit_ship)

        # Wake trail — dotted line that follows ship
        wake_dots = VGroup(*[
            Dot(point=[9.0 - i*0.6, -2.2, 0], radius=0.04,
                color="#2255AA", fill_opacity=max(0.1, 0.5-i*0.08))
            for i in range(1, 12)
        ])
        self.add(wake_dots)

        # Spray at bow
        spray = VGroup(*[
            Line(
                [8.8 + i*0.08, -2.1 + i*0.06, 0],
                [8.6 + i*0.08, -1.85 + i*0.06, 0],
                stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.6,
            )
            for i in range(4)
        ])
        self.add(spray)

        self.play(
            exit_ship.animate.move_to(LEFT*9.0 + DOWN*2.2),
            wake_dots.animate.shift(LEFT*18.0),
            spray.animate.shift(LEFT*18.0),
            run_time=3.5, rate_func=linear,
        )
        self.wait(0.5)

        self.play(
            FadeOut(t1), FadeOut(t2), FadeOut(exit_ship),
            FadeOut(wake_dots), FadeOut(spray), run_time=0.5,
        )

    def _b4_pillars(self):
        self.camera.background_color = SEA_DARK
        sea_bg = Rectangle(
            width=14.22, height=8.0,
            fill_color=SEA_DARK, fill_opacity=1, stroke_width=0,
        )
        self.add(sea_bg)

        # Night sky: stars + moon
        stars = make_star_field(n=28, seed=3, y_min=0.0, y_max=4.0)
        self.add(stars)
        moon = Ellipse(width=0.7, height=0.75, fill_color="#FFFFC0", fill_opacity=0.92,
                       stroke_width=0).move_to(RIGHT*5.5 + UP*3.2)
        moon_shadow = Ellipse(width=0.5, height=0.75, fill_color=SEA_DARK, fill_opacity=1,
                              stroke_width=0).move_to(RIGHT*5.85 + UP*3.2)
        self.add(moon, moon_shadow)

        # Wave lines
        waves = make_wave_lines(n=4, y_base=-3.0, color="#2255AA")
        self.add(waves)

        ingolfr = load_char("ingolfr_releasing_pillars", height=3.4)
        if ingolfr is None:
            body = Rectangle(width=0.7, height=1.6, fill_color="#1A3A1A",
                             fill_opacity=1, stroke_width=0)
            head = Circle(radius=0.30, fill_color="#C8956A", fill_opacity=1,
                         stroke_width=0).move_to(body.get_top()+UP*0.32)
            arm  = Line([0.35,0,0],[0.85,-0.4,0], stroke_color="#C8956A", stroke_width=6)
            ingolfr = VGroup(body, head, arm)
        ingolfr.move_to(LEFT*1.8+UP*0.3)

        p1 = make_pillar(scale=0.9).move_to(RIGHT*0.3+UP*0.3)
        p2 = make_pillar(scale=0.9).move_to(RIGHT*1.4+UP*0.3)

        self.play(FadeIn(ingolfr, shift=DOWN*0.15), run_time=0.7)
        self.play(GrowFromCenter(p1), GrowFromCenter(p2), run_time=0.7)

        lbl_p = Text("High-Seat Pillars", font="Poppins", weight=SEMIBOLD,
                     font_size=26, color=AMBER).move_to(RIGHT*3.8+UP*1.2)
        lbl_s = Text("Central To Norse Household\nAnd Religious Life",
                     font="Poppins", weight=LIGHT, font_size=19, color=L_GREY,
                     line_spacing=1.3).next_to(lbl_p, DOWN, buff=0.2)
        self.play(FadeIn(lbl_p), FadeIn(lbl_s), run_time=0.6)
        self.wait(1.0)

        self.play(
            p1.animate.rotate(PI/2).shift(DOWN*0.7),
            p2.animate.rotate(PI/2).shift(DOWN*0.7),
            run_time=0.7,
        )
        watching = Text("(He Is Still Watching)", font="Poppins", weight=LIGHT,
                        font_size=22, color=L_GREY, slant=ITALIC
                        ).next_to(ingolfr, DR, buff=0.2)
        self.play(FadeIn(watching), run_time=0.4)
        self.play(
            p1.animate.shift(RIGHT*6.0),
            p2.animate.shift(RIGHT*6.0),
            run_time=8.0, rate_func=linear,
        )

        # Splash ripples + "Gods Will Decide"
        splash_center = [5.5, 0.3, 0]
        ripple1 = Circle(radius=0.3, stroke_color=AMBER, stroke_width=2.5,
                         fill_opacity=0).move_to(splash_center)
        ripple2 = Circle(radius=0.6, stroke_color=AMBER, stroke_width=1.5,
                         fill_opacity=0).move_to(splash_center)
        ripple3 = Circle(radius=1.0, stroke_color=AMBER, stroke_width=0.8,
                         fill_opacity=0).set_stroke(opacity=0.4).move_to(splash_center)
        gods_txt = Text("The Gods Will Decide.", font="Poppins",
                        weight=SEMIBOLD, font_size=30, color=AMBER, slant=ITALIC
                        ).to_edge(DOWN, buff=V_PAD + 0.3)
        self.play(
            GrowFromCenter(ripple1), GrowFromCenter(ripple2), GrowFromCenter(ripple3),
            FadeIn(gods_txt, shift=UP*0.1),
            run_time=0.8,
        )
        self.play(
            ripple1.animate.scale(2.8).set_stroke(opacity=0.0),
            ripple2.animate.scale(2.2).set_stroke(opacity=0.0),
            ripple3.animate.scale(1.8).set_stroke(opacity=0.0),
            run_time=1.4,
        )
        self.wait(0.5)

        self.play(
            FadeOut(ingolfr), FadeOut(lbl_p), FadeOut(lbl_s),
            FadeOut(watching), FadeOut(gods_txt),
            FadeOut(ripple1), FadeOut(ripple2), FadeOut(ripple3),
            FadeOut(stars), FadeOut(moon), FadeOut(moon_shadow),
            run_time=0.5,
        )
        self.remove(p1, p2, sea_bg, waves)
        self.camera.background_color = WHITE_BG

    def _b5_three_years(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        seg1_pts = [[-1.8,-0.8,0],[0.5,-1.1,0],[1.8,-0.5,0],[2.2,0.3,0]]
        seg2_pts = [[2.2,0.3,0],[1.5,1.1,0],[0.0,1.3,0],[-1.5,1.0,0]]
        seg3_pts = [[-1.5,1.0,0],[-2.1,0.1,0],[-1.9,-0.5,0],[-1.8,-0.8,0]]

        def make_seg(pts):
            s = VMobject()
            s.set_points_smoothly(pts)
            s.set_stroke(color=AMBER, width=2.5, opacity=0.75)
            return s

        ship = make_longship(scale=0.35).move_to(seg1_pts[0])

        # Seasonal icon in top-left, changes each year
        sun_icon  = make_sun_icon(scale=0.55).move_to(LEFT*5.5 + UP*3.0)
        snow_icon = make_snowflake(scale=0.55).move_to(LEFT*5.5 + UP*3.0)

        year_lbl = Text("Year 1", font="Poppins", weight=SEMIBOLD,
                        font_size=28, color=AMBER).to_corner(UR, buff=V_PAD)
        self.play(FadeIn(year_lbl), FadeIn(sun_icon), run_time=0.3)

        seg_data = [
            (seg1_pts, "Year 2", snow_icon),
            (seg2_pts, "Year 3", sun_icon),
            (seg3_pts, None,     None),
        ]
        current_season = sun_icon
        segs = []
        for seg_pts, yr, next_season in seg_data:
            seg = make_seg(seg_pts)
            segs.append(seg)
            self.play(Create(seg), run_time=0.8)
            self.play(MoveAlongPath(ship, seg), run_time=3.0, rate_func=linear)
            if yr:
                new_lbl = Text(yr, font="Poppins", weight=SEMIBOLD,
                               font_size=28, color=AMBER).to_corner(UR, buff=V_PAD)
                self.play(
                    Transform(year_lbl, new_lbl),
                    FadeOut(current_season), FadeIn(next_season), run_time=0.35,
                )
                current_season = next_season

        pillar_dot = Dot(point=[-1.8,-0.8,0], radius=0.14, color=AMBER)
        found_lbl  = Text("Pillars Found.", font="Poppins", weight=BOLD,
                          font_size=28, color=AMBER).move_to([-1.8,-1.4,0])
        settle_lbl = Text("This Is Home.", font="Poppins", weight=BOLD,
                          font_size=36, color=DARK).to_edge(DOWN, buff=V_PAD + 0.3)
        self.play(GrowFromCenter(pillar_dot), FadeIn(found_lbl), run_time=0.6)
        self.play(pillar_dot.animate.scale(2.0).set_fill(opacity=0.4), run_time=0.4)
        self.play(pillar_dot.animate.scale(0.5).set_fill(opacity=1.0), run_time=0.3)
        self.play(FadeIn(settle_lbl, shift=UP*0.1), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(year_lbl), FadeOut(ship), FadeOut(current_season),
            FadeOut(pillar_dot), FadeOut(found_lbl), FadeOut(settle_lbl),
            *[FadeOut(s) for s in segs],
            run_time=0.5,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _b6_reykjavik(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        # Aurora strips in sky
        aurora = make_aurora_strips(y_top=3.6, n=3)
        self.add(aurora)
        self.play(
            LaggedStart(*[s.animate.set_fill(opacity=0.10+i*0.03) for i, s in enumerate(aurora)],
                        lag_ratio=0.2),
            run_time=0.8,
        )

        sw = [-1.8, -0.8, 0]
        dot = Dot(point=sw, radius=0.14, color=AMBER)
        self.play(GrowFromCenter(dot), run_time=0.5)
        for _ in range(2):
            self.play(dot.animate.scale(2.2).set_fill(opacity=0.25), run_time=0.35)
            self.play(dot.animate.scale(0.45).set_fill(opacity=1.0), run_time=0.28)

        steam = make_steam(n=4, scale=0.8).move_to([sw[0], sw[1]+0.15, 0])
        self.play(Create(steam), run_time=0.9)

        city_name = Text("REYKJAVÍK", font="Poppins", weight=BOLD,
                         font_size=52, color=AMBER).move_to(RIGHT*2.0+UP*0.8)
        city_sub  = Text("Smoky Bay", font="Poppins", weight=LIGHT,
                         font_size=28, color=GREY, slant=ITALIC
                         ).next_to(city_name, DOWN, buff=0.2)
        self.play(GrowFromCenter(city_name), run_time=0.5)
        self.play(FadeIn(city_sub, shift=UP*0.1), run_time=0.4)

        houses = VGroup(*[
            VGroup(
                Rectangle(width=0.3, height=0.24, fill_color=STONE,
                         fill_opacity=1, stroke_width=0),
                Triangle(fill_color=BROWN, fill_opacity=1,
                        stroke_width=0).scale(0.15).shift(UP*0.19),
            ).move_to([sw[0]+(i-1)*0.44, sw[1]+0.24, 0])
            for i in range(3)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(h) for h in houses], lag_ratio=0.3),
            run_time=0.8,
        )

        # Second row of houses
        houses2 = VGroup(*[
            VGroup(
                Rectangle(width=0.3, height=0.24, fill_color="#5A6A50",
                         fill_opacity=1, stroke_width=0),
                Triangle(fill_color="#3A2A1A", fill_opacity=1,
                        stroke_width=0).scale(0.15).shift(UP*0.19),
            ).move_to([sw[0]+(i-2)*0.44, sw[1]+0.55, 0])
            for i in range(4)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(h) for h in houses2], lag_ratio=0.25),
            run_time=0.9,
        )

        # Small fishing boat in bay
        fish_boat = VGroup(
            Polygon([-0.24,0,0],[-0.16,-0.1,0],[0.16,-0.1,0],[0.24,0,0],
                    [0.14,0.04,0],[-0.14,0.04,0],
                    fill_color=BROWN, fill_opacity=0.85, stroke_width=0),
            Line([0,0.2,0],[0,-0.04,0], stroke_color=DARK, stroke_width=1.5),
        ).move_to([sw[0]-1.4, sw[1]-0.5, 0])
        self.play(FadeIn(fish_boat, shift=RIGHT*0.2), run_time=0.5)

        year_badge = Text("874 AD", font="Poppins", weight=SEMIBOLD,
                          font_size=24, color=AMBER).to_corner(UR, buff=V_PAD)
        pop_note   = Text("1 Family. Iceland's First City.", font="Poppins",
                          weight=LIGHT, font_size=22, color=GREY, slant=ITALIC
                          ).to_edge(DOWN, buff=V_PAD)
        self.play(FadeIn(year_badge), FadeIn(pop_note, shift=UP*0.1), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(dot), FadeOut(steam), FadeOut(city_name),
            FadeOut(city_sub), FadeOut(houses), FadeOut(houses2),
            FadeOut(year_badge), FadeOut(pop_note), FadeOut(fish_boat),
            FadeOut(aurora), run_time=0.6,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _b7_furniture(self):
        self.camera.background_color = WHITE_BG
        entries = [
            ("Iceland's Capital:", GREY, LIGHT, 28),
            ("REYKJAVÍK", AMBER, BOLD, 56),
            ("Selected By: Furniture Delivery Logistics.", GREY, LIGHT, 24),
            ("Est. 874 AD  ·  Still Going.", L_GREY, LIGHT, 22),
        ]
        mobs, y = [], 1.8
        for txt, col, wt, sz in entries:
            t = Text(txt, font="Poppins", weight=wt, font_size=sz, color=col)
            t.move_to(UP*y)
            mobs.append(t)
            y -= 0.78 if sz > 30 else 0.62

        for m in mobs:
            self.play(FadeIn(m, shift=DOWN*0.12), run_time=0.45)
            self.wait(0.28)

        # Pillars floating in water — pool + pillars + arrow
        water_pool = Ellipse(width=3.5, height=0.7, fill_color="#2255AA", fill_opacity=0.35,
                             stroke_color="#4488CC", stroke_width=1.2
                             ).move_to(RIGHT*4.2 + DOWN*1.2)
        pool_ripple = Ellipse(width=4.0, height=0.9, fill_opacity=0,
                              stroke_color="#4488CC", stroke_width=0.8
                              ).set_stroke(opacity=0.4).move_to(water_pool.get_center())
        pillar_pair = VGroup(
            make_pillar(scale=0.5).rotate(PI/2).move_to(RIGHT*3.8 + DOWN*1.15),
            make_pillar(scale=0.5).rotate(PI/2).move_to(RIGHT*4.7 + DOWN*1.15),
        )
        self.play(FadeIn(water_pool), GrowFromCenter(pool_ripple), run_time=0.6)
        self.play(
            LaggedStart(*[GrowFromCenter(p) for p in pillar_pair], lag_ratio=0.3),
            run_time=0.7,
        )

        arrow = Arrow(
            pillar_pair.get_center() + UP*0.5,
            mobs[2].get_right() + LEFT*0.1 + UP*0.08,
            buff=0.1, stroke_color=AMBER, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.12,
        )
        self.play(Create(arrow), run_time=0.5)
        self.wait(1.0)

        self.play(
            *[FadeOut(m) for m in mobs],
            FadeOut(pillar_pair), FadeOut(arrow),
            FadeOut(water_pool), FadeOut(pool_ripple), run_time=0.5,
        )

    # ── SECTION C ─────────────────────────────────────────────────────────────

    def _c1_numbers(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("iceland_overview", height=7.5)
        if map_img:
            self.add(map_img)
        else:
            self.add(make_iceland_outline().scale(2.5))

        random.seed(42)
        positions = [
            [random.uniform(-1.7, 1.7), random.uniform(-0.85, 0.6), 0]
            for _ in range(30)
        ]
        dots = VGroup(*[
            Dot(point=p, radius=0.08, color=AMBER, fill_opacity=0.85)
            for p in positions
        ])
        # Settlement rings (cluster markers)
        rings = VGroup(*[
            Circle(radius=0.2, stroke_color=AMBER, stroke_width=1.0, fill_opacity=0
                   ).set_stroke(opacity=0.35).move_to(p)
            for p in positions[::5]  # every 5th dot gets a ring
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.06),
            run_time=4.0,
        )
        self.play(
            LaggedStart(*[GrowFromCenter(r) for r in rings], lag_ratio=0.12),
            run_time=1.0,
        )

        bar  = Line(LEFT*4.5+DOWN*3.0, RIGHT*4.5+DOWN*3.0,
                    stroke_color=WHITE, stroke_width=2)
        l874 = labeled(
            Text("874 AD", font="Poppins", weight=LIGHT, font_size=20,
                 color=DARK).next_to(bar.get_start(), UP, buff=0.15),
            bg_opacity=0.80,
        )
        l930 = labeled(
            Text("930 AD", font="Poppins", weight=LIGHT, font_size=20,
                 color=DARK).next_to(bar.get_end(), UP, buff=0.15),
            bg_opacity=0.80,
        )
        cnt  = labeled(
            Text("8,000 – 20,000 Settlers", font="Poppins", weight=BOLD,
                 font_size=32, color="#D4821A").to_edge(DOWN, buff=V_PAD*0.4),
            bg_color="#FFFDE8", bg_opacity=0.85, pad_h=0.35, pad_v=0.18,
        )

        # Small longship icon on timeline
        timeline_ship = make_longship(scale=0.22).move_to(LEFT*4.5 + DOWN*3.35)

        self.play(Create(bar), FadeIn(l874), FadeIn(l930),
                  FadeIn(timeline_ship), run_time=0.6)
        self.play(FadeIn(cnt, shift=UP*0.1), run_time=0.5)
        self.play(timeline_ship.animate.move_to(ORIGIN + DOWN*3.35), run_time=2.0, rate_func=linear)

        random.seed(99)
        positions2 = [
            [random.uniform(-1.7, 1.7), random.uniform(-0.85, 0.6), 0]
            for _ in range(20)
        ]
        dots2 = VGroup(*[
            Dot(point=p, radius=0.07, color=GREEN, fill_opacity=0.7)
            for p in positions2
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots2], lag_ratio=0.05),
            run_time=2.0,
        )
        in_60 = labeled(
            Text("In 60 Years.", font="Poppins", weight=LIGHT,
                 font_size=24, color=GREY, slant=ITALIC
                 ).next_to(cnt, UP, buff=0.2),
            bg_opacity=0.78,
        )
        self.play(FadeIn(in_60, shift=DOWN*0.1), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(dots), FadeOut(dots2), FadeOut(rings),
            FadeOut(bar), FadeOut(l874), FadeOut(l930),
            FadeOut(cnt), FadeOut(in_60), FadeOut(timeline_ship), run_time=0.6,
        )
        if map_img:
            self.remove(map_img)
        else:
            self.clear()
            self.camera.background_color = WHITE_BG

    def _c2_who_they_were(self):
        self.camera.background_color = WHITE_BG
        map_img = load_map("north_atlantic", height=7.5)
        if map_img:
            self.add(map_img)

        iceland_pt = [-0.5, 0.6, 0]
        norway_pt  = [3.0, 1.8, 0]
        britain_pt = [1.6, -1.2, 0]
        ireland_pt = [0.3, -2.0, 0]

        target = Dot(point=iceland_pt, radius=0.12, color=RED)
        self.add(target)

        arr_nor = Arrow(norway_pt, iceland_pt, buff=0.15,
                       stroke_color=AMBER, stroke_width=4.5,
                       max_tip_length_to_length_ratio=0.08)
        arr_bri = Arrow(britain_pt, iceland_pt, buff=0.15,
                       stroke_color=BLUE, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.08)
        arr_ire = Arrow(ireland_pt, iceland_pt, buff=0.15,
                       stroke_color=GREEN, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.08)

        # Viking helmet over Norway
        helmet = make_viking_helmet(scale=0.55).move_to([4.0, 2.6, 0])
        # Celtic cross over Ireland/Britain
        celtic_cross = make_cross(scale=0.5).move_to([0.2, -2.7, 0])
        celtic_ring  = Circle(radius=0.22, stroke_color=GREEN, stroke_width=1.5,
                              fill_opacity=0).move_to([0.2, -2.5, 0])

        l_nor = labeled(
            Text("Norway (Most)", font="Poppins", weight=SEMIBOLD,
                 font_size=20, color=DARK).move_to([3.8, 2.2, 0]),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        l_bri = labeled(
            Text("Britain", font="Poppins", weight=LIGHT,
                 font_size=18, color=DARK).move_to([2.5, -1.6, 0]),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        l_ire = labeled(
            Text("Ireland", font="Poppins", weight=LIGHT,
                 font_size=18, color=DARK).move_to([0.7, -2.6, 0]),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )

        self.play(Create(arr_nor), FadeIn(l_nor), FadeIn(helmet), run_time=1.0)
        self.play(
            Create(arr_bri), FadeIn(l_bri),
            Create(arr_ire), FadeIn(l_ire),
            FadeIn(celtic_cross), GrowFromCenter(celtic_ring),
            run_time=1.0,
        )
        self.wait(3.0)

        dna = labeled(
            Text("Their DNA Is Still Visible In Icelanders Today.",
                 font="Poppins", weight=LIGHT, font_size=24,
                 color=DARK, slant=ITALIC).to_edge(DOWN, buff=V_PAD * 0.8),
            bg_color="#FFFDE8", bg_opacity=0.82, pad_h=0.3, pad_v=0.16,
        )
        self.play(FadeIn(dna, shift=UP*0.1), run_time=0.7)

        pct_nor = labeled(
            Text("~70% Norse", font="Poppins", weight=SEMIBOLD,
                 font_size=18, color=DARK).move_to([3.8, 1.7, 0]),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        pct_cel = labeled(
            Text("~30% Celtic", font="Poppins", weight=SEMIBOLD,
                 font_size=18, color=DARK).move_to([1.8, -3.0, 0]),
            bg_color="#FFFDE8", bg_opacity=0.82,
        )
        self.play(arr_nor.animate.set_stroke(width=6.5),
                  FadeIn(pct_nor, shift=DOWN*0.1), run_time=0.8)
        self.play(arr_nor.animate.set_stroke(width=4.5), run_time=0.4)
        self.play(
            arr_bri.animate.set_stroke(width=4.0),
            arr_ire.animate.set_stroke(width=4.0),
            FadeIn(pct_cel, shift=DOWN*0.1), run_time=0.8,
        )
        self.play(
            arr_bri.animate.set_stroke(width=2.5),
            arr_ire.animate.set_stroke(width=2.5), run_time=0.4,
        )
        self.wait(1.5)

        self.play(
            FadeOut(arr_nor), FadeOut(arr_bri), FadeOut(arr_ire),
            FadeOut(l_nor), FadeOut(l_bri), FadeOut(l_ire),
            FadeOut(target), FadeOut(dna), FadeOut(pct_nor), FadeOut(pct_cel),
            FadeOut(helmet), FadeOut(celtic_cross), FadeOut(celtic_ring),
            run_time=0.6,
        )
        if map_img:
            self.remove(map_img)

    def _c3_why_they_came(self):
        self.camera.background_color = WHITE_BG
        r1 = Text("Harald Unified Norway.", font="Poppins", weight=LIGHT,
                  font_size=40, color=GREY).move_to(UP*1.8)
        r2 = Text("Harald Was King.", font="Poppins", weight=NORMAL,
                  font_size=40, color=GREY).move_to(UP*0.9)
        r3a = Text("Some People Would Sail Into A Volcano",
                   font="Poppins", weight=BOLD, font_size=40, color=AMBER
                   ).move_to(DOWN*0.1)
        r3b = Text("Before Submitting To A Monarch.",
                   font="Poppins", weight=BOLD, font_size=40, color=AMBER
                   ).move_to(DOWN*1.0)

        volcano = Triangle(fill_color="#5A3A1A", fill_opacity=1,
                          stroke_width=0).scale(0.5).move_to(RIGHT*1.2+DOWN*2.2)
        # Lava glow at volcano base
        lava_glow = Ellipse(width=1.2, height=0.35, fill_color="#FF4400", fill_opacity=0.55,
                            stroke_width=0).move_to(RIGHT*1.2+DOWN*2.58)
        smoke1  = Line([1.0,-1.72,0],[0.75,-1.2,0],
                       stroke_color=GREY, stroke_width=3, stroke_opacity=0.7)
        smoke2  = Line([1.2,-1.72,0],[1.45,-1.2,0],
                       stroke_color=GREY, stroke_width=3, stroke_opacity=0.7)
        figure  = Triangle(fill_color=DARK, fill_opacity=1,
                           stroke_width=0).scale(0.14).move_to(LEFT*1.2+DOWN*2.2)

        self.play(FadeIn(r1, shift=DOWN*0.12), run_time=0.6)
        self.wait(0.3)
        self.play(FadeOut(r1), FadeIn(r2, shift=DOWN*0.12), run_time=0.6)
        self.wait(0.3)
        self.play(FadeOut(r2), FadeIn(r3a, shift=DOWN*0.10), FadeIn(r3b, shift=DOWN*0.10),
                  run_time=0.7)
        self.play(
            FadeIn(volcano), FadeIn(lava_glow),
            FadeIn(smoke1), FadeIn(smoke2), FadeIn(figure),
            run_time=0.5,
        )
        # Lava pulses as figure walks toward it
        self.play(
            figure.animate.move_to(RIGHT*0.8+DOWN*2.2),
            lava_glow.animate.scale(1.3).set_fill(opacity=0.75),
            run_time=2.0, rate_func=linear,
        )
        self.play(lava_glow.animate.scale(1/1.3).set_fill(opacity=0.55), run_time=0.4)

        extra_figs = VGroup(*[
            Triangle(fill_color=DARK, fill_opacity=1, stroke_width=0
                     ).scale(0.11).move_to(LEFT*(1.2+i*0.35)+DOWN*2.4)
            for i in range(1, 7)
        ])
        self.play(
            LaggedStart(*[FadeIn(f, shift=RIGHT*0.1) for f in extra_figs],
                        lag_ratio=0.15),
            run_time=1.5,
        )
        not_just = Text("Not Just Ingólfr.", font="Poppins", weight=SEMIBOLD,
                        font_size=26, color=DARK).to_corner(UL, buff=V_PAD)
        hundreds = Text("Hundreds Of Families.", font="Poppins", weight=BOLD,
                        font_size=26, color=AMBER).next_to(not_just, DOWN, buff=0.2)
        self.play(FadeIn(not_just, shift=DOWN*0.1), run_time=0.5)
        self.play(FadeIn(hundreds, shift=DOWN*0.1), run_time=0.5)
        all_figs = VGroup(figure, *extra_figs)
        self.play(all_figs.animate.shift(RIGHT*1.5), run_time=2.0, rate_func=linear)
        self.wait(1.0)

        self.play(
            FadeOut(r3a), FadeOut(r3b),
            FadeOut(volcano), FadeOut(lava_glow), FadeOut(smoke1), FadeOut(smoke2),
            FadeOut(all_figs),
            FadeOut(not_just), FadeOut(hundreds), run_time=0.5,
        )

    def _c4_refuge(self):
        self.camera.background_color = WHITE_BG
        iceland_shape = make_iceland_outline().scale(2.5)
        iceland_shape.set_fill(color=AMBER, opacity=0.30)
        iceland_shape.set_stroke(color=AMBER, width=2)

        sub_lbl = Text("From Its Very First Days", font="Poppins", weight=LIGHT,
                       font_size=26, color=GREY).to_edge(UP, buff=V_PAD+0.5)
        big_lbl = Text("A Refuge.", font="Poppins", weight=BOLD,
                       font_size=72, color=DARK).move_to(DOWN*0.1)

        # People silhouettes arriving from the sea
        arrivals = VGroup(*[
            VGroup(
                Circle(radius=0.08, fill_color="#C8956A", fill_opacity=1, stroke_width=0),
                Rectangle(width=0.10, height=0.22, fill_color=STONE,
                         fill_opacity=1, stroke_width=0).shift(DOWN*0.17),
            ).move_to([-3.0 + i*0.8, -2.0, 0])
            for i in range(5)
        ])
        arrival_ship = make_longship(scale=0.4).move_to([-4.5, -1.8, 0])
        # Shield icon
        shield = VGroup(
            Polygon([0,0.5,0],[-0.35,0.2,0],[-0.35,-0.2,0],[0,-0.5,0],
                    [0.35,-0.2,0],[0.35,0.2,0],
                    fill_color=BLUE, fill_opacity=0.55,
                    stroke_color=DARK, stroke_width=1.5),
            Line([0,0.5,0],[0,-0.5,0], stroke_color=DARK, stroke_width=1.5),
            Line([-0.35,0,0],[0.35,0,0], stroke_color=DARK, stroke_width=1.5),
        ).scale(0.7).move_to(RIGHT*4.5 + UP*1.5)

        self.play(GrowFromCenter(iceland_shape), run_time=0.8)
        self.play(FadeIn(sub_lbl, shift=DOWN*0.1), run_time=0.5)
        self.play(GrowFromCenter(big_lbl), run_time=0.6)
        self.play(
            FadeIn(arrival_ship, shift=RIGHT*0.3),
            LaggedStart(*[FadeIn(a, shift=UP*0.1) for a in arrivals], lag_ratio=0.15),
            FadeIn(shield, shift=LEFT*0.1),
            run_time=1.0,
        )

        for _ in range(2):
            self.play(iceland_shape.animate.scale(1.04).set_fill(opacity=0.42),
                      shield.animate.scale(1.08), run_time=0.9)
            self.play(iceland_shape.animate.scale(1/1.04).set_fill(opacity=0.30),
                      shield.animate.scale(1/1.08), run_time=0.9)
        self.wait(0.5)

        self.play(
            FadeOut(iceland_shape), FadeOut(sub_lbl), FadeOut(big_lbl),
            FadeOut(arrivals), FadeOut(arrival_ship), FadeOut(shield),
            run_time=0.5,
        )

    def _c5_built_government(self):
        self.camera.background_color = WHITE_BG
        t1 = Text("A Refuge.", font="Poppins", weight=BOLD,
                  font_size=72, color=DARK).move_to(UP*0.8)
        t2 = Text("They Built A Government Anyway.", font="Poppins", weight=BOLD,
                  font_size=42, color=RED).move_to(DOWN*0.5)
        self.play(FadeIn(t1), run_time=0.45)
        self.wait(0.5)
        self.play(FadeIn(t2, shift=DOWN*0.12), run_time=0.5)

        # Scroll unrolling on right side
        scroll = make_scroll(scale=0.85).move_to(RIGHT*4.2 + DOWN*0.3)
        scroll.set_opacity(0)
        self.add(scroll)
        self.play(scroll.animate.set_opacity(1.0).shift(UP*0.15), run_time=0.8)

        law_txt = Text("Law", font="Poppins", weight=BOLD,
                       font_size=22, color=DARK).move_to(scroll.get_center() + UP*0.45)
        # Quill marks
        quill_lines = VGroup(*[
            Line(
                scroll.get_center() + [-0.7, 0.1 - i*0.22, 0],
                scroll.get_center() + [-0.1 + random.uniform(-0.1,0.2), 0.1 - i*0.22, 0],
                stroke_color=DARK, stroke_width=1.2, stroke_opacity=0.6,
            )
            for i in range(4)
        ])
        self.play(FadeIn(law_txt, shift=DOWN*0.08), run_time=0.4)
        self.play(
            LaggedStart(*[Create(ql) for ql in quill_lines], lag_ratio=0.25),
            run_time=1.0,
        )

        checkmark = make_checkmark(scale=0.65, color=GREEN).next_to(scroll, UP, buff=0.2)
        self.play(FadeIn(checkmark, shift=DOWN*0.1), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(t1), FadeOut(t2), FadeOut(scroll),
            FadeOut(law_txt), FadeOut(quill_lines), FadeOut(checkmark),
            run_time=0.5,
        )

    # ── SECTION D ─────────────────────────────────────────────────────────────

    def _d1_thingvellir(self):
        self.camera.background_color = WHITE_BG

        # Real Þingvellir map as full-screen background
        tv_map = load_map("thingvellir", height=8.0)
        if tv_map:
            self.add(tv_map)
        else:
            self.camera.background_color = "#C8B88A"

        year_lbl = labeled(
            Text("930 AD", font="Poppins", weight=LIGHT,
                 font_size=32, color=DARK).to_corner(UR, buff=V_PAD),
            bg_opacity=0.80,
        )
        self.play(FadeIn(year_lbl), run_time=0.5)

        # Semi-transparent plate overlays on top of the map
        lp = Rectangle(width=5.2, height=8.0, fill_color=BLUE,
                       fill_opacity=0.22, stroke_width=0).move_to(LEFT*3.1)
        rp = Rectangle(width=5.2, height=8.0, fill_color=RED,
                       fill_opacity=0.22, stroke_width=0).move_to(RIGHT*3.1)

        lbl_na = labeled(
            Text("North American\nPlate", font="Poppins", weight=SEMIBOLD,
                 font_size=22, color=WHITE, line_spacing=1.3
                 ).move_to(LEFT*3.8 + UP*2.8),
            bg_color="#1E5FA8", bg_opacity=0.75,
        )
        lbl_eu = labeled(
            Text("Eurasian\nPlate", font="Poppins", weight=SEMIBOLD,
                 font_size=22, color=WHITE, line_spacing=1.3
                 ).move_to(RIGHT*3.8 + UP*2.8),
            bg_color="#CC1B21", bg_opacity=0.75,
        )
        tv_lbl = labeled(
            Text("Þingvellir", font="Poppins", weight=BOLD,
                 font_size=34, color=DARK).move_to(UP*3.2),
            bg_color="#FFFDE8", bg_opacity=0.88,
        )

        self.play(FadeIn(lp), FadeIn(rp), run_time=0.7)
        self.play(FadeIn(lbl_na), FadeIn(lbl_eu), run_time=0.5)
        # Plates drift apart over 4s — labels drift with them
        self.play(
            lp.animate.shift(LEFT*0.9), lbl_na.animate.shift(LEFT*0.9),
            rp.animate.shift(RIGHT*0.9), lbl_eu.animate.shift(RIGHT*0.9),
            run_time=4.0, rate_func=linear,
        )
        self.play(FadeIn(tv_lbl, shift=DOWN*0.1), run_time=0.5)

        quote = labeled(
            Text(
                '"As If The Land Itself Was\nMaking A Point About Freedom."',
                font="Poppins", weight=LIGHT, font_size=22,
                color=DARK, slant=ITALIC, line_spacing=1.3,
            ).to_edge(DOWN, buff=V_PAD * 0.8),
            bg_color="#FFFDE8", bg_opacity=0.85, pad_h=0.3, pad_v=0.16,
        )
        self.play(FadeIn(quote, shift=UP*0.1), run_time=0.6)

        # Crack forms in rift + aurora glow
        crack = VMobject()
        crack.set_points_smoothly([
            [0, 4.0, 0], [0.12, 2.0, 0], [-0.10, 0.0, 0],
            [0.08, -2.0, 0], [0, -4.0, 0]
        ])
        crack.set_stroke(color="#FFFF88", width=5.0, opacity=0.95)
        self.play(Create(crack), run_time=2.5)
        rift_glow = Rectangle(width=0.5, height=8.0, fill_color=AURORA_G,
                              fill_opacity=0.0, stroke_width=0)
        self.add(rift_glow)
        self.play(rift_glow.animate.set_fill(opacity=0.30), run_time=0.6)
        self.play(rift_glow.animate.set_fill(opacity=0.18), run_time=0.4)

        # Assembly figures on left (North American) side
        figs_left = VGroup(*[
            VGroup(
                Circle(radius=0.07, fill_color="#C8956A", fill_opacity=1, stroke_width=0),
                Rectangle(width=0.09, height=0.2, fill_color=STONE,
                         fill_opacity=1, stroke_width=0).shift(DOWN*0.17),
            ).move_to(LEFT*2.5 + UP*(0.4 - i*0.5))
            for i in range(5)
        ])
        speaker_pos = figs_left[2].get_center() + RIGHT*0.1
        speak_arcs = VGroup(*[
            Arc(radius=0.2*(i+1), start_angle=-PI*0.1, angle=PI*0.5,
                stroke_color=AMBER, stroke_width=max(0.8, 2.0-i),
                fill_opacity=0).set_stroke(opacity=0.7-i*0.25).move_arc_center_to(speaker_pos)
            for i in range(3)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(f) for f in figs_left], lag_ratio=0.15),
            run_time=1.0,
        )
        self.play(LaggedStart(*[Create(a) for a in speak_arcs], lag_ratio=0.25), run_time=0.8)
        assemble_lbl = labeled(
            Text("First Assembly. 930 AD.", font="Poppins", weight=BOLD,
                 font_size=22, color=DARK).move_to(LEFT*2.5 + DOWN*2.2),
            bg_color="#FFFDE8", bg_opacity=0.85,
        )
        self.play(FadeIn(assemble_lbl, shift=UP*0.1), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(lp), FadeOut(rp), FadeOut(lbl_na), FadeOut(lbl_eu),
            FadeOut(tv_lbl), FadeOut(quote), FadeOut(year_lbl),
            FadeOut(crack), FadeOut(rift_glow),
            FadeOut(figs_left), FadeOut(speak_arcs), FadeOut(assemble_lbl),
            run_time=0.6,
        )
        if tv_map:
            self.remove(tv_map)
        self.camera.background_color = WHITE_BG

    def _d2_no_king(self):
        self.camera.background_color = WHITE_BG

        # Empty throne in center before figures appear — then crown descends and no one sits
        throne = make_throne(scale=1.2).move_to(ORIGIN + UP*0.2)
        crown_pts = [[-0.38,0,0],[-0.38,0.38,0],[-0.20,0.22,0],
                     [0,0.50,0],[0.20,0.22,0],[0.38,0.38,0],[0.38,0,0]]
        crown = Polygon(*crown_pts, fill_color=AMBER, fill_opacity=1,
                        stroke_width=0).scale(0.85).move_to(throne.get_top() + UP*0.55)

        self.play(FadeIn(throne, shift=UP*0.2), run_time=0.7)
        self.play(FadeIn(crown), run_time=0.4)
        # Crown hovers and descends, then throne fades — nobody sits
        self.play(crown.animate.move_to(throne.get_top() + UP*0.15), run_time=0.6)
        self.play(crown.animate.move_to(throne.get_top() + UP*0.55), run_time=0.5)
        empty = Text("(Empty.)", font="Poppins", weight=LIGHT, font_size=22,
                     color=GREY, slant=ITALIC).next_to(throne, DOWN, buff=0.2)
        self.play(FadeIn(empty, shift=UP*0.1), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(throne), FadeOut(crown), FadeOut(empty), run_time=0.5)

        figures = VGroup()
        n = 36
        for i in range(n):
            frac = i / (n - 1)
            x = (frac - 0.5) * 12.0
            y = -2.2 + 0.8 * (1 - (2*frac - 1)**2)
            fig = VGroup(
                Circle(radius=0.11, fill_color="#C8956A", fill_opacity=1,
                      stroke_width=0),
                Rectangle(width=0.15, height=0.28, fill_color=STONE,
                         fill_opacity=1, stroke_width=0).shift(DOWN*0.22),
            ).move_to([x, y, 0])
            figures.add(fig)

        self.play(
            LaggedStart(*[GrowFromCenter(f) for f in figures], lag_ratio=0.04),
            run_time=2.5,
        )
        self.wait(1.0)

        flash = Rectangle(
            width=14.22, height=8.0,
            fill_color=RED, fill_opacity=0, stroke_width=0,
        )
        self.add(flash)
        texts = [
            Text("No King.",          font="Poppins", weight=BOLD, font_size=52, color=RED).move_to(UP*2.0),
            Text("No Standing Army.", font="Poppins", weight=BOLD, font_size=52, color=RED).move_to(UP*0.9),
            Text("No Central State.", font="Poppins", weight=BOLD, font_size=52, color=RED).move_to(DOWN*0.2),
        ]
        for t in texts:
            self.play(flash.animate.set_fill(opacity=0.07), run_time=0.08)
            self.play(flash.animate.set_fill(opacity=0.0),
                      FadeIn(t, shift=DOWN*0.08), run_time=0.35)
            self.wait(0.5)

        wave_idxs = [3, 8, 15, 22, 29, 33]
        self.play(
            LaggedStart(*[
                figures[i].animate.scale(1.5).set_fill(opacity=0.5)
                for i in wave_idxs
            ], lag_ratio=0.12),
            run_time=1.0,
        )
        self.play(
            LaggedStart(*[
                figures[i].animate.scale(1/1.5).set_fill(opacity=1.0)
                for i in wave_idxs
            ], lag_ratio=0.12),
            run_time=0.8,
        )
        eq_text = Text("= Direct Democracy.", font="Poppins", weight=BOLD,
                       font_size=36, color=AMBER).move_to(UP*1.0)
        first_lbl = Text("The World's First.", font="Poppins", weight=LIGHT,
                         font_size=26, color=GREY, slant=ITALIC
                         ).next_to(eq_text, DOWN, buff=0.2)
        # Fade out red texts first, then reveal
        self.play(*[FadeOut(t) for t in texts], run_time=0.4)
        self.play(FadeIn(eq_text, shift=UP*0.15), run_time=0.6)
        self.play(FadeIn(first_lbl, shift=UP*0.1), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(figures),
            FadeOut(flash), FadeOut(eq_text), FadeOut(first_lbl),
            run_time=0.6,
        )

    def _d3_just_laws(self):
        self.camera.background_color = WHITE_BG

        # Rune stone on left
        rune_stone = make_rune_stone(scale=1.0).move_to(LEFT*4.8 + UP*0.5)

        ls_head = Circle(radius=0.28, fill_color="#C8956A", fill_opacity=1,
                        stroke_width=1, stroke_color=DARK)
        ls_body = Rectangle(width=0.55, height=1.2, fill_color=STONE,
                           fill_opacity=1, stroke_width=0).next_to(ls_head, DOWN, buff=0.05)
        ls_rock = Ellipse(width=1.0, height=0.3, fill_color="#8A7A6A",
                         fill_opacity=1, stroke_width=0
                         ).next_to(ls_body, DOWN, buff=0.0)
        lawspeaker = VGroup(ls_rock, ls_body, ls_head).move_to(UP*0.5)

        mouth = ls_head.get_center() + RIGHT*0.22 + DOWN*0.08
        s_arcs = VGroup(*[
            Arc(radius=0.35*(i+1), start_angle=-PI*0.2, angle=PI*0.6,
                stroke_color=BLUE, stroke_width=max(1.0, 2.5-i),
                fill_opacity=0)
            .set_stroke(opacity=0.85-i*0.28)
            .move_arc_center_to(mouth)
            for i in range(3)
        ])

        self.play(FadeIn(rune_stone, shift=RIGHT*0.15), run_time=0.7)
        self.play(FadeIn(lawspeaker), run_time=0.6)
        self.play(LaggedStart(*[Create(a) for a in s_arcs], lag_ratio=0.3),
                  run_time=1.0)

        facts = [
            ("Laws: Spoken From Memory.", DARK),
            ("Roads: None.",              DARK),
            ("Country: Held Together.",   AMBER),
        ]
        y_pos = [UP*1.8, UP*0.9, UP*0.0]
        fact_mobs = []
        for (txt, col), pos in zip(facts, y_pos):
            fm = Text(txt, font="Poppins", weight=SEMIBOLD,
                      font_size=30, color=col).move_to(RIGHT*2.5 + pos)
            fact_mobs.append(fm)
            self.play(FadeIn(fm, shift=LEFT*0.12), run_time=0.5)
            self.wait(0.35)

        # Second arc wave
        s_arcs2 = VGroup(*[
            Arc(radius=0.35*(i+1)*1.5, start_angle=-PI*0.2, angle=PI*0.6,
                stroke_color=BLUE, stroke_width=max(0.8, 2.0-i),
                fill_opacity=0)
            .set_stroke(opacity=0.55-i*0.18)
            .move_arc_center_to(mouth)
            for i in range(3)
        ])
        self.play(
            LaggedStart(*[Create(a) for a in s_arcs2], lag_ratio=0.3),
            run_time=1.2,
        )

        # Word-propagation dots from lawspeaker to audience
        prop_dots = VGroup(*[
            Dot(point=[mouth[0]+i*0.9, mouth[1]+0.3, 0], radius=0.06,
                color=AMBER, fill_opacity=max(0.2, 1.0-i*0.2))
            for i in range(1, 6)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in prop_dots], lag_ratio=0.15),
            run_time=0.8,
        )

        audience_lbl = Text("Audience: All Of Iceland.", font="Poppins",
                            weight=SEMIBOLD, font_size=26, color=BLUE
                            ).move_to(RIGHT*2.5 + DOWN*1.0)
        self.play(FadeIn(audience_lbl, shift=LEFT*0.12), run_time=0.5)

        # Listener chain on right edge
        audience = VGroup(*[
            VGroup(
                Circle(radius=0.07, fill_color="#C8956A", fill_opacity=1, stroke_width=0),
                Rectangle(width=0.09, height=0.2, fill_color=STONE,
                         fill_opacity=1, stroke_width=0).shift(DOWN*0.17),
            ).move_to(RIGHT*5.5 + UP*(0.7 - i*0.55))
            for i in range(5)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(f) for f in audience], lag_ratio=0.15),
            run_time=0.8,
        )
        self.wait(1.0)

        self.play(
            FadeOut(rune_stone), FadeOut(lawspeaker),
            FadeOut(s_arcs), FadeOut(s_arcs2), FadeOut(prop_dots),
            *[FadeOut(f) for f in fact_mobs],
            FadeOut(audience_lbl), FadeOut(audience),
            run_time=0.6,
        )

    def _d4_it_worked(self):
        self.camera.background_color = WHITE_BG
        cols_data = [
            ("Deliberative", DARK,  False),
            ("Public",       DARK,  False),
            ("It Worked.",   AMBER, True),
        ]
        x_pos = [-3.5, 0.0, 3.5]
        groups = []
        for (lb, col, bold), x in zip(cols_data, x_pos):
            check = make_checkmark(scale=0.60, color=col).move_to([x, 0.6, 0])
            label = Text(lb, font="Poppins",
                        weight=BOLD if bold else NORMAL,
                        font_size=28, color=col).move_to([x, -0.3, 0])
            g = VGroup(check, label)
            if bold:
                uline = Line(
                    label.get_corner(DL) + DOWN*0.06,
                    label.get_corner(DR) + DOWN*0.06,
                    stroke_color=col, stroke_width=2,
                )
                g.add(uline)
            groups.append(g)

        for g in groups:
            self.play(FadeIn(g, shift=UP*0.12), run_time=0.5)
            self.wait(0.28)

        # Timeline from 930 AD to present with milestone markers
        timeline = Line(LEFT*5.5+DOWN*2.0, RIGHT*5.5+DOWN*2.0,
                        stroke_color=DARK, stroke_width=2)
        milestones = [
            ("930 AD", -5.5),
            ("1000", -3.5),
            ("1262", -1.0),
            ("1944", 2.5),
            ("Today", 5.5),
        ]
        self.play(Create(timeline), run_time=0.8)
        mile_mobs = []
        for label, x in milestones:
            tick = Line([x, -1.85, 0], [x, -2.15, 0], stroke_color=DARK, stroke_width=2)
            lbl  = Text(label, font="Poppins", weight=LIGHT, font_size=16, color=DARK
                        ).move_to([x, -2.42, 0])
            self.play(FadeIn(tick), FadeIn(lbl), run_time=0.2)
            mile_mobs.extend([tick, lbl])

        still_going = Text("930 AD: Still Going.", font="Poppins",
                           weight=SEMIBOLD, font_size=26, color=DARK
                           ).to_edge(UP, buff=V_PAD)
        note = Text("Oldest Parliament In Continuous Operation.",
                    font="Poppins", weight=LIGHT, font_size=19, color=GREY
                    ).next_to(still_going, DOWN, buff=0.15)
        self.play(FadeIn(still_going, shift=UP*0.1), run_time=0.5)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(1.0)

        self.play(
            *[FadeOut(g) for g in groups],
            FadeOut(still_going), FadeOut(note),
            FadeOut(timeline), *[FadeOut(m) for m in mile_mobs],
            run_time=0.6,
        )
