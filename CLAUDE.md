# History Channel — Project Context

## What this is
A YouTube channel producing one-episode-per-country history videos. 50 countries planned. Each episode covers the complete history of one nation from earliest origins to the present day.

## How to produce a new country

### Full pipeline (all 5 steps + Google Docs upload)
```bash
python3.12 "Scripts/run_country.py" "Finland"
```

### Skip Google Docs upload
```bash
python3.12 "Scripts/run_country.py" "Finland" --skip-docs
```

### Run specific steps only
```bash
python3.12 "Scripts/run_country.py" "Finland" --steps research,audio_script
```

### Re-run one step (e.g. rewrite the audio script)
```bash
python3.12 "Scripts/run_country.py" "Finland" --steps audio_script
```
Previous outputs (research, etc.) are automatically loaded as context.

## What the pipeline produces
All files saved to `Output/{Country}/`:

| File | Description |
|---|---|
| `research.md` | Full historical research dossier — dates, stats, sources, hook moments |
| `audio_script.md` | Clean narration only, ~1,400–1,600 words, ~10–12 min (voiceover-ready) |
| `production_script.md` | Full script with [VISUAL CUE] directions, ~2,000–2,500 words, ~16–20 min |
| `characters.md` | Design specs for every named character and archetype |
| `scene_breakdown.md` | Scene table + music brief + color palette reference |

Audio script is also uploaded to the Google Doc automatically.

## Agent prompts (reusable, country-agnostic)
Located in `Agents/prompts/`. Each prompt uses `{COUNTRY}` as the variable.

| File | Agent role |
|---|---|
| `01_research.md` | Researches full history, identifies hook moments, checks YouTube competition |
| `02_audio_script.md` | Writes clean narration script (~1,400–1,600 words) |
| `03_production_script.md` | Expands to full production script with visual direction |
| `04_characters.md` | Writes character design specs for all figures in the script |
| `05_scene_breakdown.md` | Produces scene table, music brief, and color palette reference |

## Series rules (apply to all countries)
- Cold open at the country's most dramatic modern moment → rewind to origins → close the loop
- Tone: light, warm, fun, punny — never sarcastic or mocking toward the country
- Runtime target: 14–18 min per video (sweet spot for YouTube mid-roll ads)
- All content historically accurate — real names, real dates, verified statistics

## Completed episodes
- **Iceland** — Output/Iceland/

## Google Doc
https://docs.google.com/document/d/1gG4r13LquXtl0VmfD1l3EDm-wrpurbIOs4Bm1KfgQy0/edit
Audio scripts are uploaded here. Formatting: Calibri, 11pt min, black.

## Credentials
Service account: `/Users/dishastark/Claude Projects/dp-drive-497206-c9107abb48b6.json`

---

## VIDEO PRODUCTION PIPELINE

Each episode is animated using Manim Community v0.20.1 + cartopy geographic maps + Stable Diffusion character avatars.

### Project structure (per episode)
```
Output/{Country}/Needed Final Files/   ← ALL production files live here
  iceland_ep1_full.mp4               ← final assembled episode
  scenes/                            ← Manim Python scene files
    iceland_60s.py                   ← cold open (approved, DO NOT MODIFY)
    iceland_part1.py                 ← Sections A–D (Monks → Althing)
    iceland_part2.py                 ← Sections E–H (Christianity → Sagas)
    iceland_part3.py                 ← Sections I–L (Sturlung → Close)
  renders/                           ← individual rendered MP4s (1080p60)
    Iceland60s.mp4 / IcelandPart1-3.mp4
  audio/
    Iceland Ep1 VO Part 1-3.mp3      ← voice-over narration
    piano_bg.mp3 + sfx_*.mp3         ← background music + SFX
  assets/
    characters/                      ← SD-generated avatar PNGs
    maps/                            ← cartopy PNG geographic maps
  scripts/                           ← all written scripts
    research.md / ep1_audio_script.md / ep1_production_script.md
    PRODUCTION_SCRIPT_v2.md / VISUAL_SCRIPT_EP1.md

Archive/Iceland/                     ← old versions, not needed for production
```

### Manim environment
Virtual env: `~/manim-env` — activate with `source ~/manim-env/bin/activate`
Render command: `manim -ql scenes/filename.py ClassName`
Quality flags: `-ql` (480p fast), `-qm` (720p), `-qh` (1080p final)

### Stable Diffusion
WebUI at `~/AI-Tools/stable-diffusion-webui/`
Start: `cd ~/AI-Tools/stable-diffusion-webui && ./webui.sh --api`
API: `http://127.0.0.1:7860`

### Visual system (all episodes)
- Frame: 1920×1080, Manim 14.22 × 8.0 units
- Safe zone: H_PAD=1.5u left/right, V_PAD=0.9u top/bottom
- Font: Poppins (installed at ~/Library/Fonts/)
- NO numpy — plain Python lists `[x, y, 0]` for all coordinates
- `load_map(name)` and `load_character(name)` helpers in every scene file

### Scene duration rule
**Target duration = (VO word count ÷ 145wpm × 60) + 1.5s visual hold**
Scenes with <5 VO words = hold/transition: use dramatic timing, not word formula.

### Audio mix constants (DO NOT CHANGE)
| Track | Setting | LUFS | Notes |
|-------|---------|------|-------|
| VO (narration) | Reference — no compression | -26.20 LUFS | Do not alter |
| Piano (raw) | Never use unattenuated | -11.72 LUFS | Drowns VO completely |
| Piano (mixed) | `volume=0.05` | ~-38 LUFS | ~12 dB below VO — calibrated from Ep1 v2 |
| Final mix target | — | -19.24 LUFS | |

### ffmpeg stitch constants (DO NOT CHANGE)
```bash
ffmpeg -y \
  -i Iceland60s.mp4 -i IcelandPart1.mp4 -i IcelandPart2.mp4 -i IcelandPart3.mp4 \
  -i "Iceland Ep1 VO Part 1.mp3" -i "Iceland Ep1 VO Part 2.mp3" -i "Iceland Ep1 VO Part 3.mp3" \
  -i piano_bg.mp3 \
  -filter_complex "
    [0:v][1:v][2:v][3:v]concat=n=4:v=1:a=0[vout];
    [4:a]adelay=VO1_MS|VO1_MS[vo1];
    [5:a]adelay=VO2_MS|VO2_MS[vo2];
    [6:a]adelay=VO3_MS|VO3_MS[vo3];
    [7:a]aloop=loop=-1:size=2e+09,volume=0.05[bg];
    [vo1][vo2][vo3][bg]amix=inputs=4:duration=first:dropout_transition=2[aout]
  " \
  -map "[vout]" -map "[aout]" \
  -c:v libx264 -preset fast -crf 18 \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  output.mp4
```
- `VO1_MS` = 5300 (VO1 always starts 5.3s into cold open)
- `VO2_MS` = Iceland60s duration + Part1 duration, in milliseconds
- `VO3_MS` = Iceland60s duration + Part1 duration + Part2 duration, in milliseconds
- Piano `volume=0.05` is the single most important constant — never change without re-calibrating

### VO audio structure (3-part split)
- Part 1: intro → cold open → founding → Althing establishment
- Part 2: conversion → exploration → literary age
- Part 3: civil war → collapse → modern resolution → close
Audio placed with ffmpeg `adelay` at exact scene boundary timestamps.

### Slash commands
- `/episode-rebuild` — rewrite all scene Python files from production script
- `/video-render` — render + stitch + audio mix
- `/new-episode` — full pipeline for a new country

### Iceland episode notes
- All files: `Output/Iceland/Needed Final Files/`
- Final video: `iceland_ep1_full.mp4` (12m43s, 4 parts stitched with xfade)
- Scene files: `scenes/iceland_60s.py` (cold open, DO NOT MODIFY) + `iceland_part1–3.py`
- Individual renders: `renders/Iceland60s.mp4` (80s) + `IcelandPart1.mp4` (311s) + `IcelandPart2.mp4` (237s) + `IcelandPart3.mp4` (135s)
- VO placement: VO1 at 5.3s, VO2 at 391s (Part2 visual start), VO3 at 628s (Part3 visual start)
- Maps: iceland_overview, north_atlantic, ingolfr_route, erik_route, leif_route, thingvellir, settlement_migration
- Known issue: Reykjavík story overlaps at ~4:12 (cold open beat 8 + Part1 section B6) — needs edit pass
