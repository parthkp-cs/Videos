"""
Ep2 VO Generator — XTTS-v2 voice clone from Ep1 reference audio.
Run with Python 3.12 full path:
  "C:/Users/parth.pandya/AppData/Local/Programs/Python/Python312/python.exe" generate_vo.py

Outputs:
  Needed Final Files/audio/Iceland Ep2 VO Part 1.wav  (and .mp3)
  Needed Final Files/audio/Iceland Ep2 VO Part 2.wav  (and .mp3)
  Needed Final Files/audio/Iceland Ep2 VO Part 3.wav  (and .mp3)

Controls (edit vo_script_ep2.json to adjust per segment):
  speed       : float, 0.8–1.2. 1.0 = natural pace. 0.85 = 15% slower (dramatic).
  pause_after : seconds of silence inserted after this segment's audio ends.
  note        : director's instruction, not used by code — for human reference only.

Usage:
  python generate_vo.py                   # generate all 3 parts
  python generate_vo.py --test            # generate first 3 segments only (fast voice check)
  python generate_vo.py --part 2          # generate Part 2 only
  python generate_vo.py --segment 12      # regenerate a single segment (saves to temp/)
  python generate_vo.py --list            # list all segments with IDs
"""

import argparse
import json
import os
import struct
import subprocess
import sys
import wave
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
SCRIPT_JSON = BASE_DIR / "vo_script_ep2.json"
AUDIO_DIR = BASE_DIR / "Needed Final Files" / "audio"
TEMP_DIR = BASE_DIR / "vo_temp"
TEMP_DIR.mkdir(exist_ok=True)

# Ep1 reference audio — all 3 parts used together for best voice clone fidelity.
# XTTS-v2 averages the speaker embeddings across all reference files, giving
# a more accurate clone than a single file.
# NOTE: stored as MP3 paths; converted to WAV in prepare_voice_references() at startup.
VOICE_REFERENCE_MP3 = [
    AUDIO_DIR / "Iceland Ep1 VO Part 1.mp3",
    AUDIO_DIR / "Iceland Ep1 VO Part 2.mp3",
    AUDIO_DIR / "Iceland Ep1 VO Part 3.mp3",
]

# Output directory for per-scene VO files
SCENES_VO_DIR = AUDIO_DIR / "scenes"
SCENES_VO_DIR.mkdir(parents=True, exist_ok=True)
# Output filename pattern: scene_01_vo.mp3, scene_02_vo.mp3, …

SAMPLE_RATE = 22050  # XTTS-v2 default output sample rate


# ── Pre-convert reference MP3s to WAV ─────────────────────────────────────────
def prepare_voice_references() -> list:
    """
    Convert Ep1 reference MP3s to 22050 Hz mono WAV using ffmpeg.
    XTTS-v2's torchaudio.load() on Windows fails on MP3 due to torchcodec
    DLL issues. WAV files use a different (working) code path.
    Returns list of WAV path strings.
    """
    wav_refs = []
    for mp3 in VOICE_REFERENCE_MP3:
        wav_out = TEMP_DIR / (mp3.stem + "_ref.wav")
        if not wav_out.exists():
            print(f"  Converting reference: {mp3.name} -> {wav_out.name}")
            subprocess.run(
                [
                    "ffmpeg", "-y", "-i", str(mp3),
                    "-ar", "22050", "-ac", "1",
                    str(wav_out),
                ],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        wav_refs.append(str(wav_out))
    return wav_refs


# ── Load TTS ───────────────────────────────────────────────────────────────────
def load_tts_model():
    """Load XTTS-v2. Downloads model on first run (~1.8 GB)."""
    print("Loading XTTS-v2 model (first run downloads ~1.8 GB)...")
    # TOS_AGREED env var bypasses the interactive license prompt
    import os  # noqa: PLC0415
    os.environ["COQUI_TOS_AGREED"] = "1"
    from TTS.api import TTS  # noqa: PLC0415
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True, gpu=False)
    print("Model loaded.")
    return tts


# ── Silence generation ─────────────────────────────────────────────────────────
def make_silence_wav(duration_s: float, path: Path, sample_rate: int = SAMPLE_RATE):
    """Write a WAV file containing silence of given duration."""
    n_frames = int(sample_rate * duration_s)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(struct.pack("<" + "h" * n_frames, *([0] * n_frames)))


# ── Single segment synthesis ───────────────────────────────────────────────────
def synthesize_segment(tts, segment: dict, out_wav: Path, voice_refs: list) -> bool:
    """
    Synthesize one segment to WAV using XTTS-v2 voice cloning.
    voice_refs: list of WAV path strings (pre-converted from Ep1 MP3s).
    Returns True on success.
    """
    text = segment["text"]
    speed = float(segment.get("speed", 1.0))
    seg_id = segment["id"]

    print(f"  Segment {seg_id:02d} | speed={speed} | {len(text.split())}w | {text[:60]}...")

    try:
        # XTTS-v2 tts_to_file accepts speed= parameter in coqui-tts >= 0.25
        # speaker_wav accepts a list of paths for multi-file voice averaging
        tts.tts_to_file(
            text=text,
            speaker_wav=voice_refs,
            language="en",
            file_path=str(out_wav),
            speed=speed,
        )
        return True
    except TypeError:
        # Older API: no speed parameter — fall back, then time-stretch with ffmpeg
        print(f"    [speed param not supported — synthesizing at 1.0, then stretching to {speed}]")
        raw_wav = out_wav.with_suffix(".raw.wav")
        tts.tts_to_file(
            text=text,
            speaker_wav=voice_refs,
            language="en",
            file_path=str(raw_wav),
        )
        # ffmpeg atempo: range 0.5–2.0; speed<1 = slower = atempo must be reciprocal
        atempo = 1.0 / speed  # e.g. speed=0.9 -> atempo=1.111 -> 11% longer
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(raw_wav),
                "-filter:a", f"atempo={atempo:.4f}",
                str(out_wav),
            ],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        raw_wav.unlink(missing_ok=True)
        return True


# ── Scene assembly ─────────────────────────────────────────────────────────────
def assemble_scene(scene_id: str, segments: list, tts, voice_refs: list, skip_existing: bool = False):
    """
    Synthesize all VO segments for one scene and concatenate into a single MP3.
    Output: Needed Final Files/audio/scenes/scene_{id}_vo.mp3

    The MP3 starts at T+0:00 of the scene. Pauses between segments are baked in.
    Manim plays this file at scene start — no offset math needed.
    """
    out_mp3 = SCENES_VO_DIR / f"scene_{scene_id}_vo.mp3"
    if skip_existing and out_mp3.exists():
        print(f"  Scene {scene_id} | [cached] {out_mp3.name}")
        return

    print(f"\n  Scene {scene_id} — {len(segments)} segment(s)")
    wav_files = []

    for seg in segments:
        seg_wav = TEMP_DIR / f"seg_{seg['id']:03d}.wav"
        sil_wav = TEMP_DIR / f"sil_{seg['id']:03d}.wav"

        # Synthesize segment (use cached WAV if already done)
        if seg_wav.exists() and skip_existing:
            print(f"    Segment {seg['id']:02d} | [cached]")
        else:
            ok = synthesize_segment(tts, seg, seg_wav, voice_refs)
            if not ok:
                print(f"    ERROR: segment {seg['id']} failed. Skipping.")
                continue

        wav_files.append(str(seg_wav))

        # Silence after this segment (inter-beat pause, baked into the file)
        pause = float(seg.get("pause_after", 0.3))
        if pause > 0.01:
            make_silence_wav(pause, sil_wav)
            wav_files.append(str(sil_wav))

    if not wav_files:
        print(f"    No audio for scene {scene_id}.")
        return

    # ffmpeg concat
    concat_file = TEMP_DIR / f"concat_scene{scene_id}.txt"
    with open(concat_file, "w") as f:
        for w in wav_files:
            f.write(f"file '{w}'\n")

    combined_wav = TEMP_DIR / f"scene{scene_id}_combined.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file), str(combined_wav)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(combined_wav), "-codec:a", "libmp3lame", "-qscale:a", "2", str(out_mp3)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    combined_wav.unlink(missing_ok=True)

    # Report duration
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(out_mp3)],
        capture_output=True, text=True,
    )
    duration = float(result.stdout.strip()) if result.stdout.strip() else 0
    print(f"    => {out_mp3.name} ({duration:.1f}s)")


# ── CLI ────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Ep2 VO generator — XTTS-v2 voice clone, per-scene output")
    parser.add_argument("--test", action="store_true",
                        help="Generate segments 1-3 only (fast voice check)")
    parser.add_argument("--scene", type=str,
                        help="Generate one scene only by scene ID, e.g. --scene 07")
    parser.add_argument("--segment", type=int,
                        help="Regenerate a single segment by ID (saves to vo_temp/)")
    parser.add_argument("--list", action="store_true",
                        help="List all segments with their scene assignments")
    parser.add_argument("--skip-existing", action="store_true",
                        help="Skip scenes already assembled in audio/scenes/")
    args = parser.parse_args()

    # Verify all reference audio files exist
    missing = [r for r in VOICE_REFERENCE_MP3 if not r.exists()]
    if missing:
        for m in missing:
            print(f"ERROR: Voice reference not found: {m}")
        sys.exit(1)
    print(f"Voice reference: {len(VOICE_REFERENCE_MP3)} Ep1 VO files - converting to WAV...")
    voice_refs = prepare_voice_references()
    print(f"  Ready: {[Path(r).name for r in voice_refs]}")

    # Load script
    with open(SCRIPT_JSON, encoding="utf-8") as f:
        script = json.load(f)
    segments = script["segments"]

    # --list
    if args.list:
        # Group by scene for display
        from collections import defaultdict  # noqa: PLC0415
        by_scene = defaultdict(list)
        for s in segments:
            by_scene[s["scene"]].append(s)
        print(f"\n{'Scene':>7}  {'Segs':>5}  {'Words':>6}  Segments")
        print("-" * 70)
        for scene_id in sorted(by_scene):
            segs = by_scene[scene_id]
            words = sum(len(s["text"].split()) for s in segs)
            seg_ids = [str(s["id"]) for s in segs]
            print(f"  {scene_id:>5}  {len(segs):>5}  {words:>6}w  IDs: {', '.join(seg_ids)}")
        return

    # Load model (skip for --list)
    tts = load_tts_model()

    # --segment: single segment regen into vo_temp/
    if args.segment is not None:
        match = [s for s in segments if s["id"] == args.segment]
        if not match:
            print(f"ERROR: segment ID {args.segment} not found.")
            sys.exit(1)
        seg = match[0]
        out = TEMP_DIR / f"seg_{seg['id']:03d}.wav"
        synthesize_segment(tts, seg, out, voice_refs)
        print(f"Saved to: {out}")
        return

    # --test: first 3 segments only
    if args.test:
        test_segs = segments[:3]
        print(f"\nTest run: segments {[s['id'] for s in test_segs]}")
        for seg in test_segs:
            out = TEMP_DIR / f"seg_{seg['id']:03d}.wav"
            synthesize_segment(tts, seg, out, voice_refs)
        print("\nTest complete. Listen to vo_temp/seg_001.wav, 002.wav, 003.wav.")
        print("If the voice matches Ep1, run without --test to generate all scenes.")
        return

    # Group all segments by scene
    from collections import defaultdict  # noqa: PLC0415
    by_scene = defaultdict(list)
    for s in segments:
        by_scene[s["scene"]].append(s)

    # --scene: one scene only
    if args.scene is not None:
        scene_id = args.scene.zfill(2)
        if scene_id not in by_scene:
            print(f"ERROR: scene '{scene_id}' not found. Use --list to see available scenes.")
            sys.exit(1)
        assemble_scene(scene_id, by_scene[scene_id], tts, voice_refs, skip_existing=args.skip_existing)
        return

    # Full generation — all scenes in order
    print(f"\nGenerating VO for {len(by_scene)} scenes...")
    for scene_id in sorted(by_scene):
        assemble_scene(scene_id, by_scene[scene_id], tts, voice_refs, skip_existing=args.skip_existing)

    print("\nAll done. Output:")
    for f in sorted(SCENES_VO_DIR.glob("scene_*_vo.mp3")):
        size_kb = f.stat().st_size / 1024
        print(f"  {f.name} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
