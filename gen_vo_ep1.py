"""
gen_vo_ep1.py
Generate VO audio for all 44 Iceland EP1 scenes using OpenAI TTS.

Voice: onyx (deep, authoritative narrator — best for history documentary)
Model: tts-1-hd (higher quality than tts-1)
Speed: 1.0

Reads:   Output/Iceland/vo_texts/scene_XX_vo.txt (44 files)
Outputs: Output/Iceland/vo/scene_XX_vo.mp3       (44 files)

Usage:
  python gen_vo_ep1.py                   # generate all 44 (skip existing)
  python gen_vo_ep1.py --force           # regenerate all even if exists
  python gen_vo_ep1.py --scene 07        # generate one scene only
  python gen_vo_ep1.py --dry-run         # list texts without generating
"""

import argparse
import os
import sys
import time
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE    = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland")
IN_DIR  = BASE / "vo_texts"
OUT_DIR = BASE / "vo"
OUT_DIR.mkdir(exist_ok=True)

# Load OpenAI API key from .env
ENV_FILE = Path(r"C:\Users\parth.pandya\Projects\.keys\.env")

def load_api_key() -> str:
    if not ENV_FILE.exists():
        sys.exit(f"ERROR: .env not found at {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("OPENAI_API_KEY=") and not line.startswith("OPENAI_API_KEY_PX"):
            return line.split("=", 1)[1].strip()
    sys.exit("ERROR: OPENAI_API_KEY not found in .env")


# ── Core generator ─────────────────────────────────────────────────────────────
def generate_scene(client, scene_id: str, force: bool = False) -> bool:
    """
    Generate VO for one scene.
    scene_id: zero-padded string like "01", "07", "44"
    Returns True on success.
    """
    in_path  = IN_DIR  / f"scene_{scene_id}_vo.txt"
    out_path = OUT_DIR / f"scene_{scene_id}_vo.mp3"

    if not in_path.exists():
        print(f"  [SKIP] scene_{scene_id}: vo_text not found ({in_path.name})")
        return False

    if out_path.exists() and not force:
        size_kb = out_path.stat().st_size // 1024
        print(f"  [SKIP] scene_{scene_id}_vo.mp3 exists ({size_kb} KB)")
        return True

    raw = in_path.read_text(encoding="utf-8")

    # Strip header block: everything up to and including the "---" separator line.
    # Format in each file:
    #   TTS SETTINGS: ...
    #   Voice: ...
    #   ---
    #   Scene XX | ...
    #   (blank line)
    #   <actual narration text>
    if "---" in raw:
        after_sep = raw.split("---", 1)[1]
        # Skip the "Scene XX | ..." meta line and any blank lines
        lines = after_sep.splitlines()
        narration_lines = []
        skip_meta = True
        for line in lines:
            stripped = line.strip()
            if skip_meta:
                # Skip blank lines and the "Scene XX |" meta line
                if stripped == "" or stripped.startswith("Scene "):
                    continue
                skip_meta = False
            narration_lines.append(line)
        text = "\n".join(narration_lines).strip()
    else:
        text = raw.strip()

    if not text:
        print(f"  [SKIP] scene_{scene_id}: empty text")
        return False

    word_count = len(text.split())
    print(f"  Generating scene_{scene_id}_vo.mp3  ({word_count}w)...")

    for attempt in range(3):
        try:
            response = client.audio.speech.create(
                model="tts-1-hd",
                voice="onyx",       # deep, authoritative narrator
                input=text,
                speed=1.0,
                response_format="mp3",
            )
            response.stream_to_file(str(out_path))
            size_kb = out_path.stat().st_size // 1024
            print(f"  [OK]   scene_{scene_id}_vo.mp3  ({size_kb} KB)")
            return True
        except Exception as e:
            print(f"  [attempt {attempt+1}/3 failed] {e}")
            if attempt < 2:
                time.sleep(3)

    print(f"  [FAIL] scene_{scene_id} after 3 attempts")
    return False


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Iceland EP1 VO generator — OpenAI TTS")
    parser.add_argument("--force",   action="store_true", help="Regenerate even if MP3 exists")
    parser.add_argument("--scene",   type=str,            help="Generate one scene, e.g. --scene 07")
    parser.add_argument("--dry-run", action="store_true", help="Print texts without generating")
    args = parser.parse_args()

    # Dry run: just print all texts
    if args.dry_run:
        txt_files = sorted(IN_DIR.glob("scene_*_vo.txt"))
        for f in txt_files:
            text = f.read_text(encoding="utf-8").strip()
            words = len(text.split())
            print(f"\n--- {f.name} ({words}w) ---")
            print(text)
        return

    # Load API key and initialise client
    api_key = load_api_key()
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("ERROR: openai package not installed. Run: pip install openai")

    client = OpenAI(api_key=api_key)

    if args.scene:
        # Single scene
        scene_id = args.scene.zfill(2)
        ok = generate_scene(client, scene_id, force=args.force)
        sys.exit(0 if ok else 1)

    # All 44 scenes
    all_ids = [f"{i:02d}" for i in range(1, 45)]
    ok_count, failed = 0, []

    print(f"Generating VO for {len(all_ids)} scenes -> {OUT_DIR}\n")
    for scene_id in all_ids:
        if generate_scene(client, scene_id, force=args.force):
            ok_count += 1
        else:
            # only count as failed if file doesn't exist (not just skipped)
            out_path = OUT_DIR / f"scene_{scene_id}_vo.mp3"
            if not out_path.exists():
                failed.append(f"scene_{scene_id}")
        time.sleep(0.3)   # light throttle — OpenAI TTS is fast

    print(f"\nDone. {ok_count}/{len(all_ids)} generated.")
    if failed:
        print(f"Failed: {failed}")
    else:
        print("All MP3s present in:", OUT_DIR)


if __name__ == "__main__":
    main()
