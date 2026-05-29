# History Channel — Project Context

## What this is
A YouTube channel producing one-episode-per-country history videos. 50 countries planned.
Each episode covers the complete history of one nation from earliest origins to the present day.

---

## Folder structure

```
Scripts/
  agents/                    <- parent pipeline prompts (country-agnostic, reusable)
    01_research.md
    02_audio_script.md
    03_production_script.md
    04_characters.md
    05_scene_breakdown.md
    series_concept.md
    style_guide.md
  {Country}/                 <- all .py files for that episode
    helpers.py
    scene_01.py ... scene_44.py
    gen_atlantic_map.py
    gen_characters.py
    gen_vo_ep1.py
    render_ep1.py
  run_country.py             <- pipeline runner (research through scene breakdown)

Output/
  {Country}/
    renders/                 <- final approved MP4s (YouTube codec, no audio)
    vo/                      <- VO MP3s per scene
    sfx/                     <- sound effects
    maps/                    <- cartopy PNG geographic maps
    characters/              <- character PNGs (Pollinations.ai)
    backgrounds/             <- background photo assets
    vo_texts/                <- scene_XX_vo.txt files (word count + VO text)
    ep1_research.md          <- episode production docs (country-specific)
    ep1_audio_script.md
    ep1_production_script.md
    ep1_characters.md
    ep1_scene_breakdown.md
```

---

## Generating a new country (research through scene breakdown)

```bash
# Full pipeline — research, audio script, production script, characters, scene breakdown
python Scripts/run_country.py "Norway"

# Skip Google Docs upload
python Scripts/run_country.py "Norway" --skip-docs

# Run specific steps only
python Scripts/run_country.py "Norway" --steps research,audio_script

# Re-run one step with prior outputs as context
python Scripts/run_country.py "Norway" --steps audio_script
```

**What each step produces** (saved to `Output/{Country}/`):

| Step | File | What it is |
|------|------|------------|
| research | `research.md` | Full historical research dossier, dates, stats, hook moments |
| audio_script | `audio_script.md` | Clean narration, ~1,400-1,600 words, ~10-12 min |
| production_script | `production_script.md` | Full script with [VISUAL CUE] directions |
| characters | `characters.md` | Design specs for every named character |
| scene_breakdown | `scene_breakdown.md` | Scene table, music brief, color palette |

Audio script is also uploaded to the shared Google Doc automatically.

---

## Agent prompts (parent templates — live in Scripts/agents/)

Each prompt uses `{COUNTRY}` as the variable placeholder.

| File | Role |
|------|------|
| `01_research.md` | Historical research, hook moments, YouTube competition check |
| `02_audio_script.md` | Narration script (~1,400-1,600 words) |
| `03_production_script.md` | Full production script with visual direction |
| `04_characters.md` | Character design specs |
| `05_scene_breakdown.md` | Scene table, music brief, color palette |
| `series_concept.md` | Series-level rules and format |
| `style_guide.md` | Visual and writing style reference |

---

## Series rules (apply to all countries)
- Cold open at the country's most dramatic modern moment, rewind to origins, close the loop
- Tone: light, warm, fun, punny — never sarcastic or mocking toward the country
- Runtime target: 14-18 min per video (sweet spot for YouTube mid-roll ads)
- All content historically accurate — real names, real dates, verified statistics

---

## Video production (Manim animation)

Tech: Manim Community v0.20.1, Python 3.12, cartopy geographic maps, Pollinations.ai characters.

### Render commands

```bash
# Preview (480p, fast)
cd Scripts/Iceland
py -3.12 -m manim -ql scene_03.py IcelandEP1_S03_TheNumbers

# Batch render all 44 scenes (1080p60, YouTube codec)
py -3.12 Scripts/Iceland/render_ep1.py

# Single scene
py -3.12 Scripts/Iceland/render_ep1.py --scene 3

# From scene N onwards
py -3.12 Scripts/Iceland/render_ep1.py --from 4
```

### Visual system
- Frame: 1920x1080, Manim 14.22 x 8.0 units
- Font: Poppins Bold for titles, Poppins Regular for body
- White background unless a real photograph meaningfully adds context
- Use cartopy-generated maps (not hand-drawn) for geographic scenes
- Use Group() (not VGroup()) when mixing ImageMobject with VMobject
- When background photos are used: add all images at opacity=0 FIRST, then overlay, then text

### YouTube codec (applied by render_ep1.py)
- libx264, CRF 16, preset slow, High 4.1, yuv420p, movflags +faststart, no audio (-an)
- Audio added only at final stitch stage

### VO loudnorm
- OpenAI TTS outputs at ~-25.6 LUFS
- Apply: `loudnorm=I=-14:TP=-2:LRA=11` to normalize to -14 LUFS before mixing
- Piano underscore: `volume=0.05` (~-38 LUFS, ~12 dB below VO)

### Scene duration formula
Target duration = (VO word count / 145wpm x 60) + 1.5s visual hold
Scenes with <5 VO words: use dramatic timing, not the word formula.

---

## Completed episodes

| Country | Status | Scene files | Production docs |
|---------|--------|-------------|-----------------|
| Iceland | In production (scenes 01-03 approved) | Scripts/Iceland/ | Output/Iceland/ |

---

## Credentials
- Google service account: `C:\Users\parth.pandya\Projects\.keys\` (see project_keys_store memory)
- Google Doc (audio scripts): https://docs.google.com/document/d/1gG4r13LquXtl0VmfD1l3EDm-wrpurbIOs4Bm1KfgQy0/edit
