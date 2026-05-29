"""
new_episode.py — Scaffold a new country episode

Creates all required folders and placeholder files so the episode is
immediately ready for the pipeline (run_country.py) and production.

Usage:
    python Scripts/new_episode.py Norway
    python Scripts/new_episode.py "New Zealand"
    python Scripts/new_episode.py Norway --list       # just show what would be created
"""

import argparse
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent   # YouTube/


def scaffold(country: str, dry_run: bool = False) -> None:
    slug = country.replace(" ", "_")  # "New Zealand" -> "New_Zealand"
    print(f"\nScaffolding episode: {country}  (slug: {slug})\n")

    # ── Folders ─────────────────────────────────────────────────────────────
    folders = [
        f"Scripts/{slug}",
        f"Output/{country}/renders",
        f"Output/{country}/vo",
        f"Output/{country}/sfx",
        f"Output/{country}/maps",
        f"Output/{country}/characters",
        f"Output/{country}/backgrounds",
        f"Output/{country}/vo_texts",
    ]

    for f in folders:
        path = BASE / f
        if dry_run:
            print(f"  [DIR]  {f}/")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"  [OK]   {f}/")

    # ── Starter scripts in Scripts/{slug}/ ──────────────────────────────────
    helpers_content = f'''"""Shared helpers for {country} episode."""
from manim import *
from pathlib import Path

BASE = Path(r"{BASE / f"Output/{country}"}")
SFX  = BASE / "sfx"
VO   = BASE / "vo"

def load_map(name: str) -> ImageMobject:
    img = ImageMobject(str(BASE / "maps" / f"{{name}}.png"))
    img.set_width(config.frame_width)
    return img

def load_character(name: str, width: float = 2.5) -> ImageMobject:
    img = ImageMobject(str(BASE / "characters" / f"{{name}}.png"))
    img.set_width(width)
    return img

# Brand colors
RED     = "#CC0000"
DARK    = "#1A1A1A"
WHITE   = "#FFFFFF"
GREY    = "#888888"
BLUE    = "#4A6FA5"
'''

    render_content = f'''"""
render_{slug.lower()}.py
Batch render all scenes for {country} episode.

Usage:
    py -3.12 Scripts/{slug}/render_{slug.lower()}.py
    py -3.12 Scripts/{slug}/render_{slug.lower()}.py --scene 1
    py -3.12 Scripts/{slug}/render_{slug.lower()}.py --from 5 --quality ql
"""
import argparse, subprocess, sys, time
from pathlib import Path

SCENES_DIR  = Path(r"{BASE / f"Scripts/{slug}"}")
RENDERS_DIR = Path(r"{BASE / f"Output/{country}/renders"}")
RENDERS_DIR.mkdir(exist_ok=True)

SCENES = [
    # (scene_number, "ClassName"),
    # Fill in as scenes are built:
    # ( 1, "{country.replace(" ", "")}EP1_S01_TitleCard"),
]

QUALITY_SUBDIR = {{"ql": "480p15", "qm": "720p30", "qh": "1080p60"}}


def render_scene(n: int, cls: str, quality: str, force: bool) -> bool:
    dest = RENDERS_DIR / f"scene_{{n:02d}}_{{cls}}.mp4"
    if dest.exists() and not force:
        print(f"  [SKIP] scene_{{n:02d}} already in renders/")
        return True

    scene_file = SCENES_DIR / f"scene_{{n:02d}}.py"
    print(f"\\n[{{n:02d}}] Rendering {{cls}} ...")
    t0 = time.time()

    result = subprocess.run(
        ["py", "-3.12", "-m", "manim", f"-{{quality}}", str(scene_file), cls],
        cwd=str(SCENES_DIR), capture_output=True, text=True,
    )
    elapsed = time.time() - t0

    if result.returncode != 0:
        print(f"  [FAIL] after {{elapsed:.0f}}s")
        for line in result.stderr.strip().splitlines()[-15:]:
            print("  " + line)
        return False

    subdir = QUALITY_SUBDIR.get(quality, "1080p60")
    src = SCENES_DIR / "media" / "videos" / f"scene_{{n:02d}}" / subdir / f"{{cls}}.mp4"
    if not src.exists():
        print(f"  [FAIL] MP4 not found after render")
        return False

    subprocess.run([
        "ffmpeg", "-y", "-i", str(src),
        "-c:v", "libx264", "-preset", "slow", "-crf", "16",
        "-profile:v", "high", "-level:v", "4.1",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
        str(dest),
    ], capture_output=True)

    print(f"  [OK]   scene_{{n:02d}}  {{elapsed:.0f}}s  -> {{dest.name}}")
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--force",   action="store_true")
    p.add_argument("--scene",   type=int)
    p.add_argument("--quality", default="qh", choices=["ql", "qm", "qh"])
    p.add_argument("--from",    dest="start_from", type=int, default=1)
    args = p.parse_args()

    todo = [(n, c) for n, c in SCENES if n >= args.start_from]
    if args.scene:
        todo = [(n, c) for n, c in SCENES if n == args.scene]

    ok, failed = 0, []
    for n, c in todo:
        if render_scene(n, c, args.quality, args.force):
            ok += 1
        else:
            failed.append(n)

    print(f"\\nDone. {{ok}}/{{len(todo)}} rendered.")
    if failed:
        print(f"Failed: {{failed}}")

if __name__ == "__main__":
    main()
'''

    scene01_stub = f'''"""
{country} EP1 - Scene 01: Title Card
Render: manim -qh scene_01.py {country.replace(" ", "")}EP1_S01_TitleCard
"""
from manim import *
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from helpers import *


class {country.replace(" ", "")}EP1_S01_TitleCard(Scene):
    VD = 15.0   # update after TTS

    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Text.set_default(font="Poppins")

        title = Text("{country.upper()}", font="Poppins", weight=BOLD,
                     font_size=96, color=DARK)
        self.play(Write(title), run_time=1.2)
        self.wait(self.VD - 2.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
'''

    stubs = {
        f"Scripts/{slug}/helpers.py": helpers_content,
        f"Scripts/{slug}/render_{slug.lower()}.py": render_content,
        f"Scripts/{slug}/scene_01.py": scene01_stub,
    }

    for rel_path, content in stubs.items():
        path = BASE / rel_path
        if dry_run:
            print(f"  [FILE] {rel_path}")
        else:
            if path.exists():
                print(f"  [SKIP] {rel_path} (already exists)")
            else:
                path.write_text(content, encoding="utf-8")
                print(f"  [OK]   {rel_path}")

    # ── vo_texts placeholder ─────────────────────────────────────────────────
    manifest = BASE / f"Output/{country}/vo_texts/!EP1_VO_MANIFEST.txt"
    if not dry_run and not manifest.exists():
        manifest.write_text(
            f"{country} EP1 — VO Manifest\n"
            f"Generated by new_episode.py\n\n"
            f"Add scene_XX_vo.txt files here as scenes are written.\n"
            f"Format:\n"
            f"  TTS SETTINGS: Speed=1, Stability=55%, Similarity=75%, Style=25%\n"
            f"  ---\n"
            f"  Scene XX | ~Xs | N words\n\n"
            f"  [VO text here]\n",
            encoding="utf-8",
        )
        print(f"  [OK]   Output/{country}/vo_texts/!EP1_VO_MANIFEST.txt")

    print(f"\n{'=' * 50}")
    if dry_run:
        print(f"  Dry run complete. No files written.")
    else:
        print(f"  {country} scaffolded.")
        print(f"\n  Next steps:")
        print(f"  1. python Scripts/run_country.py \"{country}\"")
        print(f"     -> produces research, audio script, production script,")
        print(f"        characters, scene breakdown in Output/{country}/")
        print(f"  2. Build scene_01.py onward in Scripts/{slug}/")
        print(f"  3. py -3.12 Scripts/{slug}/render_{slug.lower()}.py --scene 1 --quality ql")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new country episode.")
    parser.add_argument("country", help="Country name, e.g. Norway")
    parser.add_argument("--list", action="store_true",
                        help="Show what would be created without writing files")
    args = parser.parse_args()
    scaffold(args.country.strip(), dry_run=args.list)
