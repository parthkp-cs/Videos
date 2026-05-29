# Agent Prompt: Scene Breakdown & Music Brief
## Step 5 of 5 — Production Tables

**Variable:** `{COUNTRY}`
**Input:** Production script from Step 3

---

## Instructions for agent

Produce three production reference tables from the production script. These are used by the director, animator, and composer to plan and execute the video.

---

### Table 1: Scene-by-Scene Breakdown

A table with one row per scene covering:

| Column | Description |
|---|---|
| # | Scene number (matches beat ID from production script, e.g. A1, B3) |
| Scene name | Short descriptive title |
| Part / File | Which VO part and Manim Python file this scene lives in (e.g. Part 1 / `{country}_part1.py`) |
| Manim class | The Python class name that renders this section (e.g. `{Country}Part1`) |
| Setting / Era | Location and time period |
| Key visual | The most important single image in this scene — concrete description (object, character, map) |
| Narration start | First 5–8 words of narration in this scene |
| Duration (s) | Estimated runtime in seconds using the formula: `(word_count ÷ 145) × 60 + 1.5` |

**Note on timing:** Cold open = separate file (`{country}_60s.py`). Parts 1–3 each map to one Python file and one VO audio file.

---

### Table 2: Music Brief

A table with one row per major segment (not per scene — group scenes with the same emotional arc):

| Column | Description |
|---|---|
| Segment | Name of the segment or era |
| Tone | 2–4 words describing the emotional tone |
| Instrumentation | Suggested instruments or sound palette |
| Key rule | One specific instruction for the composer (e.g. "stop all music when X happens", "must not feel triumphant here") |

**Global music rules to always include:**
- No comedy music stings — tone is carried by words, not music
- Music shifts with each major era
- The cold open theme should return at the close
- Piano background runs throughout at `volume=0.08` — any scoring must work over this

---

### Table 3: Color Palette Reference

A table mapping each historical era to a color palette:

| Column | Description |
|---|---|
| Era / Period | Name and approximate dates |
| Primary colors | 2–3 hex codes or plain color names |
| Mood | One word |
| Notes | Any specific color rules for this era (e.g. "red accent only for this scene") |

**Standard palette (always applies — these override era colors):**
- `RED #CC1B21` — bad news, confrontation, stamps, dramatic arrivals, death, exile
- `AMBER #D4821A` — warmth, history, discovery, founding moments, positive resolution
- `DARK #1A1A1A` — neutral narration text, standard labels
- `GREY #5A5A5A` — secondary text, italic quotes, footnotes
- `WHITE` — text on dark backgrounds only (cold/night/death scenes)

---

### Output format
All three tables in clean markdown. No prose. Tables only, with a one-line header above each.
