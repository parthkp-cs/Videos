# Agent Prompt: Character Design Specs
## Step 4 of 5 — Character Design Document

**Variable:** `{COUNTRY}`
**Input:** Production script from Step 3 + Research dossier from Step 1

---

## Instructions for agent

Identify every named historical figure who appears in the production script and write a character design specification for each one. Also create any necessary archetypal/symbolic characters (e.g. "The Colonial Official", "The General") that represent groups or systems rather than specific individuals.

---

## For each character, provide

**Name & Role**
Full name and their role in the story. One sentence on why they matter to the narrative.

**Design**
Physical description suitable for a flat-illustration animator:
- Build and height relative to others
- Distinguishing features (hair, beard, scars, posture)
- Costume and era-appropriate clothing — be specific about materials and style
- Props they carry or are associated with
- Color palette for their design (must fit the era's color palette from the style guide)

**Expression & Personality**
What does their default expression communicate? What is the one thing their design must convey before a word is spoken?

**Key Scene**
The single most important moment this character appears. What are they doing? What should the viewer feel?

**Recurring visual**
If this character appears more than once, what visual element stays consistent so the viewer always recognises them instantly?

**Variants required**
List every pose/state variant this character needs across all scenes. Each variant becomes a separate PNG asset. Common variants:
- `seated` — at rest, meditating, or scholarly work
- `standing` — neutral upright pose, default
- `speaking` — gesturing, arm raised, commanding
- `packing` / `sailing` — in motion, carrying or aboard a vessel
- `under_cloak` — disguised, exiled, or concealed

---

## Archetype characters

For any unnamed archetype (e.g. "The Colonial Merchant", "The Soldier"), write the same spec but note explicitly:
- They are not a specific person
- What group or system they represent
- How many times they appear and in what contexts

For crowd scenes, the `make_small_figure(color, scale)` geometric pattern is used (not PNG assets). Specify:
- Which color (RED / AMBER / DARK / GREY) represents this group
- Whether they appear in crowds, rows, or solo
- Approximate count per scene

---

## Design rules (apply to all characters)

- Silhouette must be instantly recognisable at small size
- No two characters should have the same silhouette
- Expression tells personality before the label appears
- Costumes reflect era and role, not caricature
- Avoid making antagonists visually evil — historical figures who did harm should look like people, not villains

---

## Asset production (technical — for the production team)

### File naming convention
All character PNGs use **lowercase filenames** with underscores. No spaces.
- Format: `{firstname}_{lastname}.png` or `{role_description}.png`
- Located: `Output/{Country}/production/assets/characters/`
- Loaded in scene files via: `load_char("firstname_lastname", height=3.5)`
- Each variant is a separate file: `ingolfr_seated.png`, `ingolfr_standing.png`

### Geometric fallback (REQUIRED for every character)
Every character must have a `make_{name}_geo()` Python function defined as fallback in case the PNG does not exist. This function returns a `VGroup` using only Manim primitives (circles, rectangles, polygons). The fallback must:
- Approximate the character's silhouette
- Use the character's assigned color palette
- Be usable anywhere the PNG would be used

Example:
```python
def make_monk_geo(self):
    body = Rectangle(width=0.7, height=1.2, fill_color="#4A3728", fill_opacity=1)
    head = Circle(radius=0.25, fill_color="#D4A574", fill_opacity=1)
    head.next_to(body, UP, buff=0.05)
    return VGroup(body, head)
```

### Image generation (Stable Diffusion / Pollinations.ai)
Characters are generated as flat illustrations. Two approaches:
1. **Local SD:** WebUI at `~/AI-Tools/stable-diffusion-webui/` — start: `./webui.sh --api` — API at `http://127.0.0.1:7860`
2. **Pollinations.ai (free FLUX):** No API key required. POST to `https://image.pollinations.ai/prompt/{encoded_prompt}` — returns PNG directly. Use for quick generation without running local SD.

Prompt structure for character generation:
```
flat illustration, {character name}, {era} Norse/Viking/Medieval figure, 
{costume description from spec}, simple background, vector art style, 
high contrast, clean lines, suitable for animation overlay
```

### Character inventory format
At the end of the document, include a complete asset list in this format:
```
## Asset Inventory

| Character | File(s) | Variants | Geometric fallback |
|---|---|---|---|
| Ingólfr Arnarson | ingolfr_standing.png, ingolfr_seated.png | standing, seated | make_ingolfr_geo() |
| Irish Monk | monk_seated.png | seated | make_monk_geo() |
```
