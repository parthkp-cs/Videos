"""
render_ep1.py
Render all 44 Iceland EP1 Manim scenes at high quality (-qh, 1080p60).
Outputs each video to Output/Iceland/renders/scene_XX_ClassName.mp4

Usage:
  py -3.12 render_ep1.py                  # render all (skip existing)
  py -3.12 render_ep1.py --force          # re-render all
  py -3.12 render_ep1.py --scene 07       # render one scene
  py -3.12 render_ep1.py --quality ql     # override quality (ql/qm/qh)
  py -3.12 render_ep1.py --from 10        # start from scene 10
"""

import argparse
import subprocess
import sys
import time
import shutil
from pathlib import Path

SCENES_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Scripts\Iceland")
RENDERS_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\renders")
RENDERS_DIR.mkdir(exist_ok=True)

SCENES = [
    ( 1, "IcelandEP1_S01_TitleCard"),
    ( 2, "IcelandEP1_S02_BanksCollapse"),
    ( 3, "IcelandEP1_S03_TheNumbers"),
    ( 4, "IcelandEP1_S04_EmptyShelves"),
    ( 5, "IcelandEP1_S05_MostCountries"),
    ( 6, "IcelandEP1_S06_IcelandAnswer"),
    ( 7, "IcelandEP1_S07_Recovered"),
    ( 8, "IcelandEP1_S08_TimeRewind"),
    ( 9, "IcelandEP1_S09_BackUpFurther"),
    (10, "IcelandEP1_S10_TheMonks"),
    (11, "IcelandEP1_S11_PerfectExistence"),
    (12, "IcelandEP1_S12_MonkDeparts"),
    (13, "IcelandEP1_S13_FirstInstinct"),
    (14, "IcelandEP1_S14_IngoflrSetsOut"),
    (15, "IcelandEP1_S15_PillarsOverboard"),
    (16, "IcelandEP1_S16_ThreeYears"),
    (17, "IcelandEP1_S17_ReykjavikFounded"),
    (18, "IcelandEP1_S18_GreatMigration"),
    (19, "IcelandEP1_S19_WhyTheyCame"),
    (20, "IcelandEP1_S20_BuiltGovernment"),
    (21, "IcelandEP1_S21_AlthingConvenes"),
    (22, "IcelandEP1_S22_ThirtyChieftains"),
    (23, "IcelandEP1_S23_ItWorked"),
    (24, "IcelandEP1_S24_ConversionCrisis"),
    (25, "IcelandEP1_S25_ThorgeIrDecides"),
    (26, "IcelandEP1_S26_HorsemeatExemption"),
    (27, "IcelandEP1_S27_ErikExiled"),
    (28, "IcelandEP1_S28_Greenland"),
    (29, "IcelandEP1_S29_LeifNorthAmerica"),
    (30, "IcelandEP1_S30_IcelandWasWriting"),
    (31, "IcelandEP1_S31_SnorriAndMarvel"),
    (32, "IcelandEP1_S32_SnorriPolitician"),
    (33, "IcelandEP1_S33_SturlungAge"),
    (34, "IcelandEP1_S34_HakonWatches"),
    (35, "IcelandEP1_S35_SeventyMen"),
    (36, "IcelandEP1_S36_LastWords"),
    (37, "IcelandEP1_S37_TheyStruck"),
    (38, "IcelandEP1_S38_OldCovenant"),
    (39, "IcelandEP1_S39_SurrenderByChoice"),
    (40, "IcelandEP1_S40_WentUnderground"),
    (41, "IcelandEP1_S41_RapidMontage"),
    (42, "IcelandEP1_S42_OriginalInstinct"),
    (43, "IcelandEP1_S43_FoundationWasLaid"),
    (44, "IcelandEP1_S44_EndCard"),
]

# Quality flag -> subfolder name Manim uses
QUALITY_SUBDIR = {
    "ql": "480p15",
    "qm": "720p30",
    "qh": "1080p60",
}


def find_rendered_mp4(scene_num: int, classname: str, quality: str) -> Path | None:
    """Find the MP4 Manim wrote under scenes/media/videos/."""
    subdir = QUALITY_SUBDIR.get(quality, "1080p60")
    mp4 = SCENES_DIR / "media" / "videos" / f"scene_{scene_num:02d}" / subdir / f"{classname}.mp4"
    return mp4 if mp4.exists() else None


def render_scene(scene_num: int, classname: str, quality: str, force: bool) -> bool:
    dest = RENDERS_DIR / f"scene_{scene_num:02d}_{classname}.mp4"

    if dest.exists() and not force:
        print(f"  [SKIP] scene_{scene_num:02d} — {dest.name} already in renders/")
        return True

    scene_file = SCENES_DIR / f"scene_{scene_num:02d}.py"
    print(f"\n[{scene_num:02d}/44] Rendering {classname} ...")
    t0 = time.time()

    result = subprocess.run(
        [
            "py", "-3.12", "-m", "manim",
            f"-{quality}",
            str(scene_file),
            classname,
        ],
        cwd=str(SCENES_DIR),
        capture_output=True,
        text=True,
    )

    elapsed = time.time() - t0

    if result.returncode != 0:
        print(f"  [FAIL] scene_{scene_num:02d} after {elapsed:.0f}s")
        print("  --- stderr (last 20 lines) ---")
        for line in result.stderr.strip().splitlines()[-20:]:
            print("  " + line)
        return False

    # Transcode Manim output to YouTube-compatible H.264
    # - yuv420p:           required by YouTube (Manim can output yuv444p)
    # - profile:high 4.1: broadest device compatibility
    # - crf 16:           near-lossless for intermediate clip quality
    # - preset slow:      better compression at same quality vs fast
    # - movflags +faststart: progressive download / upload
    # - no audio stream:  scenes are silent; audio added at stitch stage
    src = find_rendered_mp4(scene_num, classname, quality)
    if src is None:
        print(f"  [FAIL] scene_{scene_num:02d} — MP4 not found after render")
        return False

    ff = subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", str(src),
            "-c:v", "libx264",
            "-preset", "slow",
            "-crf", "16",
            "-profile:v", "high",
            "-level:v", "4.1",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-an",                      # no audio
            str(dest),
        ],
        capture_output=True, text=True,
    )

    if ff.returncode != 0:
        print(f"  [FAIL] ffmpeg transcode for scene_{scene_num:02d}")
        for line in ff.stderr.strip().splitlines()[-10:]:
            print("  " + line)
        return False

    size_mb = dest.stat().st_size / (1024 * 1024)
    print(f"  [OK]   scene_{scene_num:02d}  {elapsed:.0f}s  {size_mb:.1f} MB  -> {dest.name}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Iceland EP1 batch renderer")
    parser.add_argument("--force",   action="store_true", help="Re-render even if output exists")
    parser.add_argument("--scene",   type=int,            help="Render one scene number only")
    parser.add_argument("--quality", default="qh",        choices=["ql", "qm", "qh"],
                        help="Manim quality flag (default: qh = 1080p60)")
    parser.add_argument("--from",    dest="start_from", type=int, default=1,
                        help="Start from scene N (skip earlier scenes)")
    args = parser.parse_args()

    if args.scene:
        matches = [(n, c) for n, c in SCENES if n == args.scene]
        if not matches:
            sys.exit(f"ERROR: scene {args.scene} not in list")
        n, c = matches[0]
        ok = render_scene(n, c, args.quality, args.force)
        sys.exit(0 if ok else 1)

    to_render = [(n, c) for n, c in SCENES if n >= args.start_from]
    print(f"Rendering {len(to_render)} scenes at -{args.quality} -> {RENDERS_DIR}\n")

    done, failed = 0, []
    total_t0 = time.time()

    for scene_num, classname in to_render:
        ok = render_scene(scene_num, classname, args.quality, args.force)
        if ok:
            done += 1
        else:
            failed.append(scene_num)

    total_elapsed = time.time() - total_t0
    print(f"\n{'='*50}")
    print(f"Done. {done}/{len(to_render)} rendered in {total_elapsed/60:.1f} min.")
    if failed:
        print(f"Failed scenes: {failed}")
        print(f"Re-run with: py -3.12 render_ep1.py --scene <N>  to retry individually")
    else:
        print("All renders successful. Ready to stitch.")
        print(f"Output: {RENDERS_DIR}")


if __name__ == "__main__":
    main()
