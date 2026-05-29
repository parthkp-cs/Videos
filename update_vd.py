"""
update_vd.py
Patch VD = X.X  in all 44 Iceland EP1 scene files with measured ffprobe durations.
Run once after VO generation. Idempotent — safe to re-run.
"""
from pathlib import Path
import re

SCENES_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\scenes")

# Measured durations from ffprobe (seconds, rounded to 2dp)
VD_VALUES = {
     1: 15.86,
     2: 18.50,
     3: 11.30,
     4: 11.04,
     5: 11.66,
     6:  6.43,
     7:  2.23,
     8:  7.20,
     9:  6.19,
    10: 19.56,
    11:  7.51,
    12:  6.53,
    13: 12.26,
    14: 21.50,
    15: 17.42,
    16:  4.32,
    17: 13.75,
    18: 18.31,
    19: 15.70,
    20:  7.78,
    21: 14.04,
    22: 23.98,
    23:  7.90,
    24: 18.60,
    25: 15.89,
    26: 27.46,
    27: 18.41,
    28: 20.98,
    29: 28.15,
    30: 22.27,
    31: 28.73,
    32:  6.79,
    33: 12.70,
    34: 13.68,
    35:  6.70,
    36:  6.43,
    37:  0.70,
    38: 21.34,
    39: 26.95,
    40:  5.42,
    41: 20.21,
    42: 16.61,
    43: 10.75,
    44: 14.16,
}

updated, skipped = 0, 0

for scene_num, vd in VD_VALUES.items():
    scene_file = SCENES_DIR / f"scene_{scene_num:02d}.py"
    if not scene_file.exists():
        print(f"  [MISSING] {scene_file.name}")
        continue

    src = scene_file.read_text(encoding="utf-8")

    # Match: VD = <number>  (with optional comment)
    pattern = r"(VD\s*=\s*)[\d.]+(\s*(?:#.*)?)$"
    new_src, count = re.subn(pattern, rf"\g<1>{vd}\2", src, flags=re.MULTILINE)

    if count == 0:
        print(f"  [NO MATCH] scene_{scene_num:02d}.py — VD line not found")
        skipped += 1
        continue

    if new_src == src:
        print(f"  [UNCHANGED] scene_{scene_num:02d}.py  VD={vd}")
        skipped += 1
        continue

    scene_file.write_text(new_src, encoding="utf-8")
    print(f"  [UPDATED]  scene_{scene_num:02d}.py  VD={vd}")
    updated += 1

print(f"\nDone. {updated} updated, {skipped} unchanged/skipped.")
