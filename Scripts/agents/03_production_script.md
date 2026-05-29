# Agent Prompt: Visual Production Script
## Step 3 of 5 — Scene-by-Scene Visual Direction

**Variable:** `{COUNTRY}`
**Input:** Audio script (Step 2) + Research dossier (Step 1) + Characters doc (Step 4, if already run)

---

## What this document is

A shot-by-shot visual script. Every line of narration gets a matching visual beat. This document is used directly to build Manim scene Python files — it is not a general creative brief. Every description must be concrete enough that a developer can implement it without asking a single question.

---

## Document structure

Divide the script into **lettered sections** (A, B, C…), one per narrative beat group. Within each section, number individual beats (A1, A2…).

For each beat, write:

```
**A1 — Beat Title** `[~Xs]`
**VO:** *"Exact narration line(s) for this beat."*
- Visual action 1 — what appears, how it moves, exact color and weight
- Visual action 2 — what changes, what text appears, in what order
- Visual action 3 — hold, transition, or final frame state
```

The `[~Xs]` timing estimate is calculated as:
> **Scene duration = (word count of VO for this beat ÷ 145) × 60 + 1.5 seconds visual hold**
> Beats with fewer than 5 VO words use dramatic timing: minimum 4–6 seconds.

Every beat must have at least one concrete visual action. No beat should have only a timing note and no description.

---

## Visual description standard — CRITICAL

The most common failure in this document is descriptions that tell the animator how something should *feel* instead of what should actually appear on screen.

**BAD — these will be rejected:**
- "Tone: deadpan. The humor is in the act."
- "Each 'No' hits like a drum."
- "Three silence dots appear — like a meditation breath."
- "Speed is the point."
- "Convey isolation."
- "The scene feels heavy."
- "Almost a compliment."

**GOOD — these are implementable:**
- `RED bold 72pt text slams in from the RIGHT edge of the frame in 0.45 seconds. Hard stop. No animation out.`
- `36 small figure icons fill a semicircle left to right. Then three lines hit one at a time: "No king." / "No standing army." / "No central state." — each RED, bold, 38pt, with a sharp pulse flash on arrival.`
- `Three concentric amber circles expand outward from the character's forehead — each ring fading as it grows, pulsing at breathing rhythm. This is the visual for meditation or inner stillness.`
- `The ship icon sits at Iceland's west coast, turns, and sails off the LEFT edge of the map entirely. The map pauses, then expands leftward.`

**The test:** Read your visual note aloud to someone who has not seen the script. They should be able to draw exactly what you described. If they would ask "but what does it look like?" — rewrite it.

### Required specifics for every visual note:
- **Text:** font size (pt), color (RED / AMBER / DARK / GREY / WHITE), weight (bold / semibold / light / italic), animation type (slams / fades / drops / grows letter-by-letter)
- **Characters:** which variant (seated / standing / packing / speaking / under cloak), position on frame (LEFT / RIGHT / CENTER), what they are doing
- **Maps:** which map asset, what is highlighted, what labels appear and when
- **Motion:** direction (LEFT / RIGHT / UP / DOWN), speed descriptor (fast / slow / deliberate), rate function if notable (linear / ease in-out)
- **Color meaning conventions to follow consistently:**
  - `RED (#CC1B21)` — bad news, confrontation, stamps, dramatic arrivals, death, exile
  - `AMBER (#D4821A)` — warmth, history, discovery, founding moments, positive resolution
  - `DARK (#1A1A1A)` — neutral narration text, standard labels
  - `GREY (#5A5A5A)` — secondary text, italic quotes, footnotes
  - `WHITE` — text on dark backgrounds only

---

## VO sync rule — REQUIRED

Each beat must map to a specific excerpt of the audio script. The cumulative timing of all beats within a Part must equal the duration of that VO Part (within ±10%). 

- Calculate VO Part duration: word count × (60/145) seconds
- Distribute that time across beats proportionally to their word counts
- If the visual beats total less than the VO, add hold time or extend transitions
- **Scenes cannot be shorter than their VO.** A narrator speaking over a blank or finished scene is a production failure.

---

## Character first-appearance rule

Every named character appearing for the first time gets a full introduction beat:

```
- [CHARACTER NAME] enters frame from [direction]. [Which image variant]. 
  Name card appears below: **"Full Name"** (bold, DARK, 30pt) / *"Role or era"* (light, GREY, 22pt, italic).
  [One sentence on what their presence/expression communicates before any label appears.]
```

Reference the Characters document (Step 4) for physical description and which image asset to use. If a character appears in multiple contexts (e.g. seated meditating vs. standing speaking), note which variant is used in each scene.

---

## Cold open specification

The cold open is a **separate scene file** rendered independently. It must:
- Stand alone without needing prior context
- Run 60–90 seconds
- End on a freeze-frame or title card that transitions cleanly into the main episode
- Use the same visual standards as the main script

Mark the cold open section clearly:
```
## COLD OPEN (separate scene file — DO NOT MERGE WITH PART 1)
```

---

## VO part boundary markers

Mark where each audio Part ends and the next begins:

```
---
*[VO PART 1 ENDS — next section is VO Part 2]*
---
```

The scene file for each Part must visually complete before the next Part's VO begins. No visual should rely on VO from a different Part file.

---

## Technical environment (how this script becomes video)

This visual script is implemented in:

**Animation:** Manim Community v0.19–v0.20.1
- Virtual env: `~/manim-env` — activate: `source ~/manim-env/bin/activate`
- Render: `manim -qh --media_dir media filename.py ClassName`
- Quality flags: `-ql` (480p draft), `-qm` (720p), `-qh` (1080p60 final)
- Frame: 1920×1080, Manim coordinate space 14.22 × 8.0 units
- Safe zone: H_PAD = 1.5u left/right, V_PAD = 0.9u top/bottom
- Background: white (`#FFFFFF`) unless a scene requires dark (cold/night/death scenes use `#0A0A0A` or `#2E2E3A`)

**Python rules for scene files (enforce in visual descriptions):**
- NO numpy — all coordinates as plain Python lists: `[x, y, 0]` not `np.array([x, y, 0])`
- Use `VMobject().set_points_smoothly([...])` for curves and motion paths — NOT `CubicBezier` or `set_points_smooth`
- Use `Group()` when mixing `ImageMobject` with other objects — NOT `VGroup()`
- Font: Poppins — valid weights: `BOLD`, `SEMIBOLD`, `NORMAL`, `LIGHT` (REGULAR does not exist)
- `self.wait()` must always be positive — never `self.wait(0)`
- `self.clear()` between major sections; reset `self.camera.background_color` if it changed

**Character assets:**
- Located: `Output/{Country}/production/assets/characters/` — PNG files, lowercase filenames
- Loaded via: `load_char("character_name", height=3.5)` helper in scene file
- Always provide a geometric fallback for any character whose PNG may be missing

**Map assets:**
- Located: `Output/{Country}/production/assets/maps/` — PNG files
- Loaded via: `load_map("map_name", height=7.5)` helper in scene file
- Always provide a polygon fallback using `Polygon(*pts)` if map PNG does not exist

**Video assembly (ffmpeg):**
- Clips stitched with: `xfade=transition=fade:duration=0.5:offset={clip_end - 0.5}`
- VO audio mixed with: `adelay={ms}|{ms}` per track, `volume=2.2` for VO, `volume=0.08` for piano background
- Final render: H.264, `-crf 18`, `-preset fast`, `-r 60`

---

## Required visual moments (checklist)

Every production script must include:

- [ ] Cold open that establishes scale or stakes in the first 10 seconds
- [ ] Explicit time-rewind moment (spinning clock, calendar, or equivalent)
- [ ] Name card for every named character on first appearance
- [ ] Map for every geographical claim (settlement, route, territory)
- [ ] VO Part 1 / Part 2 / Part 3 boundary markers
- [ ] Visual for every text-only dramatic moment (no blank screen with narration only)
- [ ] Final frame that closes the loop to the cold open
- [ ] End card with episode title and next-episode teaser

---

## What to avoid

- Visual notes that describe tone or emotion instead of what is on screen
- Abstract stand-ins for physical visuals ("silence", "heaviness", "the weight of history")
- Scenes that end before their VO ends
- Characters appearing without introduction on first use
- Map labels that are not historically accurate
- Pacing notes masquerading as visual descriptions ("fast-paced montage" is not a visual)
- Reusing the exact same visual for two different narrative beats in the same section
