# Episode 2: "The Volcanoes and the Pirates"
## Production Script v2 — VO-Synced Director's Breakdown
### Iceland 3-Part Series | Aligned to Ep1 Production Learnings

---

## VISUAL SYSTEM

**Frame:** 1920x1080 | Manim 14.22 x 8.0 units
**Safe zone:** H_PAD = 1.5u left/right | V_PAD = 0.9u top/bottom

**Position shorthand used throughout:**
- `CTR` = [0, 0, 0]
- `L3` = [-3.0, 0, 0] | `R3` = [3.0, 0, 0]
- `L5` = [-5.0, 0, 0] | `R5` = [5.0, 0, 0] (near safe zone edge)
- `TC` = [0, 3.0, 0] | `BC` = [0, -3.0, 0]
- `TL` = [-4.5, 3.0, 0] | `TR` = [4.5, 3.0, 0]
- `BL` = [-4.5, -2.5, 0] | `BR` = [4.5, -2.5, 0]

**Color palette:**
- `DARK_BG` = `#0A0A0A` — cold open, Laki return, close
- `STONE_GREY` = `#4A4A4A` — colonial era (dominant)
- `SAGE_GREEN` = `#5C7A4E` — Commonwealth flashback only
- `DANISH_NAVY` = `#1C3A5E` — Danish rule marker
- `VOLCANIC_RED` = `#2D0000` — fissure glow, catastrophe
- `AMBER` = `#D4821A` — warmth, emphasis, survivor moments
- `CORSAIR_OCHRE` = `#C4782A` — Barbary raid section only
- `CRIMSON` = `#8B0000` — Jon Arason ONLY
- `COLD_WHITE` = `#F0EDE6` — captive Icelanders

**Font:** Poppins — all text elements without exception. Variants: Regular / Bold / SemiBold / Light.
**Manim implementation:** Every `Text()` object uses `font="Poppins"`. All scene TEXT directives are already annotated with `font="Poppins"` — do not override with default font.
**Animation feel:** One or two confident visual moves per scene. Not jittery.
**Duration formula:** `(word_count / 145) * 60 + 1.5s visual hold`

---

## SOUND ASSETS

### Reuse from Ep1:
- `sfx_bell.mp3` — single low tone. Reveals, dramatic beats.
- `sfx_collapse.mp3` — heavy impact. Deaths, catastrophe, stamping.
- `sfx_paper.mp3` — paper/parchment rustle. Documents, ledgers.
- `sfx_stamp.mp3` — ink stamp. Seals, dates, official markings.
- `sfx_whoosh.mp3` — movement sweep. Ships, map arrows, character entries.
- `piano_bg.mp3` — background ambient. Fade in/out per act.

### New SFX needed for Ep2:
- `sfx_crack.mp3` — deep earth crack/tear. Scene01 fissure opening.
- `sfx_tick.mp3` — dry single tick. Ledger checkmarks, tally marks.
- `sfx_clock.mp3` — year counter spinning. Scenes 06, 29.
- `sfx_crowd_murmur.mp3` — low crowd ambience. Scene07 Althing.

---

## AUDIO MIXING GUIDE

### Measured levels from Ep1 final mix (use as target for Ep2)

| Track | Measured LUFS | Implementation | Notes |
|-------|--------------|----------------|-------|
| VO (narration) | -26.20 LUFS | Reference. Do not compress. | VO sits quieter than the raw piano — this is expected. The mix brings them together. |
| Piano (raw, unattenuated) | -11.72 LUFS | Too loud by itself — drowns VO completely. | Never use piano at full volume against live VO. |
| Piano (Ep2 target: volume=0.05) | approx. -38 LUFS | ~12 dB below VO. Correct balance. | `volume=0.05` in ffmpeg/Manim audio mix is the calibrated value from Ep1 v2. |
| Final mix target | -19.24 LUFS | Ep1 v2 final assembled episode. | Aim to match this on Ep2. |

### Piano volume setting: volume=0.05

This is the single most important mix setting. In the Ep1 v2 final render, `volume=0.05` on the piano track produced the correct balance where VO sits clearly above music. Use this exact value for Ep2.

Relative to this baseline, adjust piano further per scene state:

| Scene state | Piano multiplier | Approx resulting LUFS |
|-------------|-----------------|----------------------|
| Active narration (default) | volume=0.05 | approx. -38 LUFS |
| Emotional hold / no VO | volume=0.07 | approx. -35 LUFS (music lifts slightly into silence) |
| Near-silence scenes (Scene04 counter, Scene08 cellar) | volume=0.02 | approx. -45 LUFS (barely present, creates dread) |
| Complete silence beats (Scenes 08 black, 11, 15, 19) | volume=0 (mute) | OFF — hard cut, not fade |

### SFX levels (relative to VO at -26.20 LUFS)

| SFX | dB offset vs VO | Notes |
|-----|----------------|-------|
| sfx_collapse, sfx_crack (heavy impact) | +8 dB above VO (-18 LUFS approx.) | Should physically land. Do not soften. |
| sfx_bell (reveal / death beat) | 0 to +2 dB above VO (-26 to -24 LUFS) | Use louder value for deaths, quieter for reveals. |
| sfx_tick, sfx_stamp (mechanical) | -2 dB below VO (-28 LUFS) | Each tick individually audible. Dry, no reverb tail. |
| sfx_crowd_murmur (ambient) | -10 dB below VO (-36 LUFS) | Texture only. Behind the scene, not on top of it. |
| sfx_whoosh (movement) | -2 dB below VO (-28 LUFS) | Punchy. Fade tail within 0.3s. |

### Ducking rules

- Piano does NOT duck under VO via sidechain. The `volume=0.05` baseline keeps it clear of VO naturally. The narration pacing has built-in breathing room.
- On heavy SFX hits (sfx_collapse, sfx_crack): duck piano by an additional -4 dB for 300ms, then restore. Attack: 50ms. Release: 300ms.
- On complete silence beats: mute piano AND all SFX with a hard cut, not a fade. The abruptness is the effect.

### Act-level music texture guide

| Act | Scenes | Music texture | Approx level |
|-----|--------|---------------|-------------|
| Cold open (Laki) | 01-05 | Solo cello drone, minimal | -18 to -10 dB, rising slowly |
| Rewind / Commonwealth | 06-07 | Light string texture | -14 dB |
| Sturlung / Snorri | 07-08 | Sparse piano only | -14 dB dropping to -20 dB |
| Old Covenant | 09-10 | Quiet piano, slightly warmer | -14 dB |
| Danish merger / Plague | 11-12 | Cold thin strings | -14 dB, silence on Scene11 |
| Reformation / Jon Arason | 13-15 | Sparse, tense. Silence on Scene15. | -14 dB, mute on Scene15 hold |
| Monopoly / Trade | 16-18 | Thin harpsichord texture (institutional, cold) | -14 dB |
| Barbary raid | 19-22 | Tense, low strings. Silence on Scene19 open. | -14 dB |
| Laki return | 23-26 | Cello drone returns, same as cold open | -10 to -14 dB |
| Jorgensen | 27-30 | Slightly wry string texture, light | -14 dB |
| Close | 31-34 | Full piano, warmest moment of episode | -12 dB |

---

## CHARACTER ASSETS

### Reused from Episode 1 — DO NOT RE-RENDER:

**Snorri Sturluson**
- `snorri_writing.png` — at desk, quill, confident expression (Ep1 Avatar 07)
- `snorri_afraid.png` — backed against stone wall, frightened (Ep1 Avatar 07)
- Used in: Scene08

**King Hakon IV of Norway**
- `hakon_iv.png` — seated, patient half-smile, cup in hand (Ep1 Avatar 09)
- Used in: Scene07, Scene08

---

### New Characters for Episode 2 — SD Prompts:

#### AVATAR EP2-01: Jon Arason
**Scenes:** 13, 14, 15

Style base: `flat vector illustration, Kurzgesagt educational style, clean confident linework, white background, full body, expressive face, warm muted palette`
NEG: `photorealistic, 3d render, dark background, text, watermark, multiple characters, cropped, deformed, blurry, nsfw`

```
jon_arason_defiant:
"Kurzgesagt flat vector illustration, Jon Arason Catholic Bishop of Holar
Iceland c.1540s, large physically imposing man, full grey-white beard, strong
jaw, bright direct eyes with slight amusement, wearing deep crimson chasuble
over cream alb (crimson is the ONLY warm color in this scene — make it vivid),
bishop mitre sitting noticeably askew on head as if just placed and not adjusted,
holding bishop crozier casually like a walking stick not ceremonially, rolled
parchment tucked under left arm (he was a poet), expression: cheerful defiance,
the look of someone who finds the situation slightly funny, nine very small
illustrated children figures visible in background row (tiny, simplified circles),
full body portrait, white background"

jon_arason_calm:
"same Jon Arason standing very still, expression shifted to absolute composure,
no longer amused, not afraid, the composure of a man who saw this coming and
prepared for it fully, mitre still askew, two slightly smaller male figures
flanking him (his sons Ari and Bjorn, same style, calm expressions), all three
facing forward, all three still, dark muted background, no props in hands,
full body portrait"
```

---

#### AVATAR EP2-02: Murat Reis the Younger
**Scenes:** 20, 21

```
murat_reis:
"Kurzgesagt flat vector illustration, Murat Reis the Younger Dutch-born
corsair captain c.1627, lean wiry build, light eyes fading blonde hair going
grey, visual collision of two worlds: Dutch-cut long dark navy coat with brass
buttons over Moroccan-style loose trousers, red sash at waist, loosely wrapped
flat Ottoman turban (not formal), horizontal scar along jaw from chin to ear,
holding an open navigation chart/map in both hands, expression: professional
assessment, the look of a logistics manager reviewing a delivery schedule,
no cruelty no drama — businesslike, full body, white background"
```

---

#### AVATAR EP2-03: Gudridur Simonardottir
**Scenes:** 22

```
gudridur:
"Kurzgesagt flat vector illustration, Gudridur Simonardottir Icelandic woman
c.1636, slight build medium height, very straight deliberate posture, permanent
dark circles under eyes (not distress — the mark of someone who has seen enough
and is still here), wearing traditional Icelandic dress: plain undyed wool
kyrtill tunic in cream-white, dark blue skaut headscarf, single strand of North
African beadwork visible at the edge of the headscarf where it meets the temple
(small but deliberate — she kept it), nothing in either hand, expression: absolute
unreadable composure, not blank not numb, fully present and decided, full body,
white background"
```

---

#### AVATAR EP2-04: Jorgen Jorgensen
**Scenes:** 28, 29, 30

```
jorgensen_confident:
"Kurzgesagt flat vector illustration, Jorgen Jorgensen Danish-born adventurer
c.1809, lean slightly underfed build, unkempt brown hair that has given up
on being styled, light beard neither intentional nor negligence, expression:
genuine manic enthusiasm — this man actually believes this is going to work,
wearing improvised semi-official uniform: dark green British naval-style coat
with mismatched brass buttons, Danish civilian trousers, wide-brimmed hat with
a strip of Icelandic cloth tucked into the band, always holding a large rolled
proclamation scroll in right hand, full body portrait, white background"

jorgensen_deflated:
"same Jorgen Jorgensen, same clothes, same hat (now slightly askew), rolled
proclamation scroll still in right hand but held limply at his side, expression:
the specific deflation of a man who has just remembered something important he
forgot, not angry not afraid, just the exact moment when enthusiasm becomes
recognition, full body, white background"
```

---

#### AVATAR EP2-05: Count Trampe
**Scenes:** 28

```
count_trampe:
"Kurzgesagt flat vector illustration, Count Trampe Danish Governor of Iceland
c.1809, medium slightly portly build, impeccably neat: every button fastened,
powdered wig slightly anachronistic but perfectly placed, clean-shaven, formal
Danish colonial governor dress: dark blue coat with gold epaulettes and silver
buttons, white cravat, always holding an open rulebook in both hands at chest
height, expression: affronted correctness — the look of a man who knows the
exact regulation and genuinely cannot comprehend why others do not follow it,
full body, white background"

count_trampe_jail:
"same Count Trampe, same clothes, same expression (affronted, correct), same
open rulebook still being read, but now standing inside a simple four-bar jail
cell (vertical bars visible left and right of him), he is still reading the book,
his expression has NOT changed, full body portrait"
```

---

---

## AUDIO SCRIPT (tightened | no em dashes | ~1,340 words)

---

June 1783. The ground in southern Iceland simply opens. Not a mountain. Not a crater. A crack. Twenty-seven kilometres of it, tearing across the landscape like the earth is trying to say something. And then it says it, for eight months straight.

The Laki fissure eruption, the Skaftareldar, is the largest lava-producing eruption in Iceland's recorded history. But the lava isn't the worst part. It's the gas. Approximately 120 million tonnes of sulphur dioxide pour into the atmosphere. Roughly three times the entire European industrial SO₂ output in 2006. In eight months. From one crack in the ground.

The gas kills the grass. The sheep eat the poisoned grass. Around eighty percent of Iceland's sheep die. About half the cattle and horses. Without livestock, there is no food.

A blue-grey haze rolls across Europe by midsummer. In England alone, an estimated twenty-three thousand people die from its effects. Harvests fail across France. The Northern Hemisphere cools by about 1.3 degrees.

In Iceland, approximately nine thousand people die. On an island of around forty thousand, that means one in every four or five.

That is not a statistic you absorb. That is every family, every village, everyone knowing exactly who didn't make it through the winter.

Iceland in 1783 has already been through five centuries of foreign rule, two waves of plague, a pirate raid, a trade monopoly that strangled it dry, and a Reformation enforced at sword point. And now this.

How did Iceland get here? Let's go back. Back to 1262, when the Icelanders handed themselves over. Voluntarily. Which is somehow the worst part.

...

The Icelandic Commonwealth had worked for three hundred years without a king, without an army. Held together by the Althing (the world's oldest surviving parliament) and the stubbornness of a population who had sailed to the edge of the world specifically to avoid being governed. Then the Sturlung Age happened. Forty years of clan warfare. Iceland's great families tore into each other while Norway's King Hakon IV watched and applied pressure.

Snorri Sturluson, Iceland's greatest writer and historian, ended up in his cellar at Reykholt in 1241. Seventy of Hakon's men outside. His last recorded words: "Eigi skal hoggva." Do not strike. They struck.

Twenty years later, the surviving chieftains signed the Old Covenant and became Norwegian subjects. They kept their laws, in theory. They kept the Althing, in form. But sovereignty was gone. And once you hand that over, getting it back turns out to take about seven hundred years.

...

In 1380, Norway merged with Denmark. Iceland came along. Whether Icelanders were formally informed is not entirely clear. They were simply Danish now. Not through conquest, but through a dynastic reshuffling in which no one thought to ask Iceland.

It got worse before it got worse.

The Black Death arrived in 1402, carried on a ship. It killed somewhere between a quarter and half the population. Scholars argue the exact figure. The people who died found the academic debate less interesting. It came back in 1494. Iceland's medieval population never fully recovered from either wave.

Then came the Reformation. King Christian III of Denmark decided his entire kingdom was Lutheran now. In Iceland, one man stood in the way: Jon Arason, the Catholic bishop of Holar. Poet, nationalist, father of at least nine children. (The bishop apparently kept busy.) He understood the Reformation for exactly what it was: foreign cultural control wearing a clerical collar.

He resisted for decades.

On the seventh of November, 1550, he was beheaded alongside two of his sons, Ari and Bjorn. Catholic properties were seized by Danish administrators. Iceland's spiritual life was changed by royal decree. The island took the blow and kept going.

...

The trade monopoly landed in 1602 and it landed hard. The Danish crown carved Iceland into trading districts, each handed to a licensed merchant. Icelanders sold to them and bought from them at prices the merchants set. Fish went out cheap. Consumer goods came in expensive. Economic diversification was impossible by design. The monopoly ran until 1787. Its damage ran considerably longer.

The monopoly didn't just impoverish Iceland. It made it defenceless. No surplus meant no investment, no infrastructure, no capacity to respond when things went catastrophically wrong.

Barbary corsairs.

In 1627, ships from Algiers (commanded by Murat Reis the Younger, a Dutchman who had converted to Islam and gone into the raiding business) arrived on the coast of Iceland. They hit the East Fjords, then Grindevik, then spent three days on the Vestmannaeyjar islands. They killed approximately fifty people. They kidnapped approximately four hundred.

Four hundred Icelanders were loaded onto ships and transported to North Africa to be sold into slavery. The event entered memory as Tyrkjaranid, the Turkish Raid. Because "Algerian raid by a Dutch convert" apparently lacked the necessary ring.

The monopoly meant no money to ransom them quickly. Most spent the rest of their lives in Algiers. About fifty eventually returned. The most famous was Gudridur Simonardottir, nine years in North Africa before coming home to marry the great poet Hallgrimur Petursson. She endured. She rebuilt. She made a life. That pattern will keep coming up.

...

And then 1783. Now you know how Iceland got there.

The fissure opens. Eight months of lava and sulphur. Eighty percent of the sheep, gone. A quarter of the people, gone.

The haze drifts south and fails the harvests of France. Historians have argued, carefully and with caveats, that Laki's agricultural disruption contributed to the conditions that produced the French Revolution six years later. Iceland did not plan this. Iceland was simply having a routine geological episode and accidentally destabilising Western Europe. It is, in some ways, the most Icelandic thing Iceland has ever done.

The trade monopoly was still in place. Relief supplies could not be freely imported. The island was starving and the mechanism designed to help was the same mechanism that had been bleeding it dry for eighty years.

By 1800, the Althing itself was gone. Abolished by royal decree. A High Court in Reykjavik took its place. Iceland was no longer a nation in any practical sense. A remote administrative district, periodically devastated by geology, locked into a system designed to extract what little it could produce.

Then June 1809. A Danish-born adventurer named Jorgen Jorgensen arrived in Reykjavik. He found the Danish governor Count Trampe blocking all trade per monopoly rules and responded by arresting him. He declared Iceland independent from Denmark, proclaimed himself Protector of Iceland, Commander in Chief by Land and Sea, and issued proclamations in English. He seemed genuinely enthusiastic about the whole project.

His reign lasted sixty-two days.

In August, HMS Talbot sailed into Reykjavik harbour. Its captain noted Jorgensen was in violation of his parole from a prior arrest in Britain. He was taken aboard, transported to London, and eventually transported again as a convict to Tasmania. Icelanders remember him as Jorundur hundadagakonungur. Jorgen the Dog-Days King. Collected by a passing warship, gone before autumn. The whole affair has the quality of elaborate farce. But underneath it, something real: even in 1809, an outsider could see Iceland deserved to govern itself. He was just not quite the right outsider.

...

Plague, twice. Piracy from a direction that makes no geographical sense. A Reformation enforced by beheading. A monopoly designed to keep the island poor. A volcanic catastrophe that killed a quarter of the population and accidentally destabilised France. The parliament abolished. A sixty-two-day king collected by the Navy. Six centuries of foreign rule. Six centuries of endurance.

Go back to Laki. 1783. Forty thousand people, decimated, isolated, locked into a system designed to bleed them dry. No rescue. No cavalry. What there was: people who stayed, who rebuilt, who remembered the sagas, who kept speaking a language barely changed in a thousand years, who held onto the memory of what Iceland had once been. Self-governing. Beholden to no king.

Those people's grandchildren's grandchildren looked at six centuries of this and decided enough was enough.

That is Episode 3.

---

---

## SCENE-BY-SCENE PRODUCTION SCRIPT

### Format per scene:
- `[TARGET: Xs]` = total scene duration from formula + holds
- `| VO ~Xw, ~Xs |` = word count and VO time within the scene
- Timestamps are scene-relative (T+0:00 = start of THIS scene)
- All Manim positions in scene-relative coordinates

---

## TITLE CARD

---

### SceneIntro — Title Card | `[TARGET: 8s]`

**VO:** *(silent)*

**VISUAL:** Full-screen Iceland flag (blue/white cross). Flag fills frame edge-to-edge. Manim's SVGMobject or Rectangle composition. Hold 3s then:
Crossfade — title text fades in over flag: `"ICELAND"` large BOLD in white, subtitle `"The Volcanoes and the Pirates"` in LIGHT below, sub-subtitle `"Episode 2 · 1262–1830"` in LIGHT smaller. All centered. Text in safe zone.
After 5s hold: white overlay rectangle fades in to white → transition to Scene01.

**MANIM NOTE:** Use `ImageMobject` for the flag PNG if available, else build from rectangles. White fade overlay z_index=10. Identical implementation to Ep1 SceneIntro — only the subtitle and sub-subtitle text strings change.
**SOUND NOTE:** piano_bg.mp3 at volume=0.05. No VO. No SFX.

---

## COLD OPEN

---

### Scene01 — Ground Zero | `[TARGET: 25s]` | VO ~35w, ~14.5s

**VO:** *"June 1783. The ground in southern Iceland simply opens. Not a mountain. Not a crater. A crack. Twenty-seven kilometres of it, tearing across the landscape like the earth is trying to say something. And then it says it, for eight months straight."*

---

**T+0:00**
- BG: `DARK_BG` — full frame, no elements
- MAP: none yet
- CHARACTER: none
- AUDIO: Silence. Music: single cello note fades in from nothing (piano_bg.mp3 at -18dB, very low)

**T+0:01** | VO: *"June 1783."*
- TEXT: `"June 1783."` at `TC` offset [0, 2.5, 0], WHITE SEMIBOLD font="Poppins" font_size=36, `FadeIn` run_time=0.8s
- SFX: none

**T+0:03** | VO: *"The ground in southern Iceland simply opens."*
- VISUAL: Extreme close-up of dark soil. Draw a jagged `VMobject` crack — NOT a straight line. Use these waypoints (approximate, the irregularity is the point):
  `[-7, -0.3, 0] → [-5.2, -0.6, 0] → [-3.8, -0.1, 0] → [-2.4, -0.7, 0] → [-1.1, -0.2, 0] → [0, -0.5, 0] → [1.2, -0.8, 0] → [2.5, -0.3, 0] → [3.9, -0.9, 0] → [5.1, -0.4, 0] → [7, -0.6, 0]`
  stroke_width=2, color=`VOLCANIC_RED`, no fill
- ANIMATE: `Create` the VMobject from center outward — split it at the midpoint [0, -0.5, 0] and animate both halves simultaneously tearing left and right. run_time=2.5s
- SFX: `sfx_crack.mp3` fires at T+0:03, -5dB, stereo spread (left channel slightly ahead of right — mimics a tear propagating)

**T+0:05** | VO: *"Not a mountain. Not a crater. A crack."*
- VISUAL: Crack is now fully visible across the frame
- TEXT: `"Not a mountain."` at [-3.5, -1.5, 0], STONE_GREY LIGHT font="Poppins" font_size=24, `FadeIn` 0.5s
- TEXT: `"Not a crater."` at [0, -1.5, 0], STONE_GREY LIGHT font="Poppins" font_size=24, `FadeIn` 0.5s after first
- TEXT: `"A crack."` at [3.5, -1.5, 0], WHITE BOLD font="Poppins" font_size=28, `FadeIn` 0.5s after second

**T+0:09** | VO: *"Twenty-seven kilometres of it..."*
- VISUAL: Crack glows — add a second VMobject tracing the same waypoints but offset ±0.12u vertically, `VOLCANIC_RED` opacity=0.3, stroke_width=3. Creates a hot-edge glow effect without making it look neat.
- TEXT: `"27 KILOMETRES"` at `BC` (= [0, -2.8, 0] — bottom-centre safe zone), WHITE BOLD font="Poppins" font_size=40, `GrowFromCenter` run_time=0.8s
- SFX: `sfx_bell.mp3` at T+0:09, -10dB (low, single tone)

**T+0:14** | VO: *"And then it says it, for eight months straight."*
- VISUAL: All prior text fades out. Only the glowing crack line remains. Hold.
- AUDIO: Cello note deepens/sustains

**T+0:16** | Title card begins building (over the crack, not replacing it):
- TEXT line 1: `"THE VOLCANOES AND THE PIRATES"` at [0, 2.0, 0], WHITE BOLD font="Poppins" font_size=40, `Write` run_time=1.2s
- TEXT line 2: `"The Crisis (1262-1830)"` at [0, 1.2, 0], WHITE LIGHT font="Poppins" font_size=24, `FadeIn` 0.5s after line 1
- TEXT line 3: `"Episode 2 of 3"` at [0, 0.6, 0], STONE_GREY font="Poppins" font_size=20, `FadeIn` 0.5s after line 2

**T+0:22** | Hold. Title over glowing crack. No movement. Music sustains.

**T+0:25** | Scene end. All elements hold into Scene02 (no transition — continue directly).

**MANIM NOTE:** The crack VMobject is the entire visual. It must look like geology, not geometry — use the waypoints as a guide but feel free to add 1–2 more micro-jags between them. No smooth curves (`make_smooth()` off). No lava, no volcano shape, no steam. The irregularity IS the drama. Title card layers ON TOP of the crack — do not replace it. Use z_index=10 for text. The glow pass at T+0:09 uses the same waypoints — do not re-randomise them or the two paths won't align.
**SOUND NOTE:** sfx_crack is the only hard SFX. Cello drone starts at -18dB and slowly rises to -12dB by T+0:25. Do not fade out — continues under Scene02.

---

### Scene02 — The Haze Famine | `[TARGET: 37s]` | VO ~95w, ~39s

**VO:** *"The Laki fissure eruption, the Skaftareldar, is the largest lava-producing eruption in Iceland's recorded history. But the lava isn't the worst part. It's the gas. Approximately 120 million tonnes of sulphur dioxide pour into the atmosphere. Roughly three times the entire European industrial SO₂ output in 2006. In eight months. From one crack in the ground. The gas kills the grass. The sheep eat the poisoned grass. Around eighty percent of Iceland's sheep die. About half the cattle and horses. Without livestock, there is no food."*

---

**T+0:00**
- BG: white (`WHITE_BG`), transition from Scene01 via `FadeToColor` run_time=0.5s
- MAP: load `iceland_overview.png` at `CTR`, scale to fill frame width, `FadeIn` run_time=0.8s
- CHARACTER: none
- AUDIO: Music transitions from cello drone to slightly fuller string texture, -10dB

**T+0:02** | VO: *"The Laki fissure eruption, the Skaftareldar..."*
- VISUAL: A `Rectangle` (fill_color=#BFD000, fill_opacity=0.0, no stroke) sits at the southern coast of Iceland
- ANIMATE: `fill_opacity` animates to 0.65 over 3s (haze cloud materialises over Iceland)

**T+0:08** | VO: *"...Approximately 120 million tonnes of sulphur dioxide..."*
- VISUAL: Haze cloud `Rectangle` expands upward: `animate.shift(UP*1.5)` run_time=5s (cloud rises over island)

**T+0:10** | VO: *"Roughly three times the entire European industrial SO₂ output in 2006..."*
- VISUAL: Bar chart appears at `R3` area, right of map:
  - Two `Rectangle` bars side by side, base at [3.5, -2.5, 0]
  - LEFT bar: width=0.8u, height=1.0u, `STONE_GREY`, label `"EU SO₂\n2006"` font="Poppins" font_size=14 below
  - RIGHT bar: width=0.8u, height=3.0u, `VOLCANIC_RED`, label `"Laki\n1783"` font="Poppins" font_size=14 below
  - Both bars `GrowFromBase` (animate height from 0), staggered 0.5s
  - Label under red bar: `"(one crack)"` ITALIC STONE_GREY font="Poppins" font_size=12
- SFX: none

**T+0:18** | VO: *"The gas kills the grass."*
- VISUAL: Bar chart remains. On map, a tally list appears at `TL` = [-4.5, 2.8, 0]:

**T+0:20** | VO: *"Around eighty percent of Iceland's sheep die."*
- TALLY LINE 1: small sheep icon + `"Sheep: 80% dead"` at [-4.5, 2.5, 0], RED BOLD font="Poppins" font_size=20, `FadeIn`
- SFX: `sfx_tick.mp3` at T+0:20, -8dB

**T+0:23** | VO: *"About half the cattle and horses."*
- TALLY LINE 2: cattle icon + `"Cattle: ~50% dead"` at [-4.5, 1.9, 0], RED font="Poppins" font_size=20, `FadeIn`
- TALLY LINE 3: horse icon + `"Horses: ~50% dead"` at [-4.5, 1.3, 0], RED font="Poppins" font_size=20, `FadeIn` 0.5s after
- SFX: `sfx_tick.mp3` at each line, -8dB

**T+0:29** | VO: *"Without livestock, there is no food."*
- TEXT: `"Without livestock, there is no food."` at `BC` = [0, -3.0, 0], WHITE BOLD font="Poppins" font_size=28, `GrowFromCenter`
- SFX: `sfx_bell.mp3` at T+0:29, -8dB (low tone — weight)

**T+0:34** | Hold. Map with haze, tally lines, bold text. No new elements.

**T+0:37** | Scene end. All elements HOLD into Scene03 (map persists — do not transition).

**MANIM NOTE:** Map is loaded once and shared with Scene03. Do not reload. Bar chart and tally list are the two visual moves — they do not animate simultaneously. Bar chart first (right), then tally list (left) as VO progresses.
**SOUND NOTE:** Music stays at -10dB. Three sfx_tick hits staggered. sfx_bell on final line. No other SFX.

---

### Scene03 — Europe Poisoned | `[TARGET: 18s]` | VO ~38w, ~15.7s

**VO:** *"A blue-grey haze rolls across Europe by midsummer. In England alone, an estimated twenty-three thousand people die from its effects. Harvests fail across France. The Northern Hemisphere cools by about 1.3 degrees."*

---

**T+0:00**
- MAP: transition to `north_atlantic.png` — `Transform` or `ReplacementTransform` from `iceland_overview.png`, run_time=1.0s. Both Iceland and UK/France/Europe visible.
- BG: `WHITE_BG` continues
- The haze cloud Rectangle from Scene02 persists and begins moving EAST: `animate.shift(RIGHT*5)` run_time=7s (cloud sweeps across the map toward Europe)

**T+0:03** | VO: *"In England alone, an estimated twenty-three thousand people die..."*
- WHEN CLOUD REACHES UK on map (approx T+0:03):
  - LABEL: `"~23,000 deaths (est.)"` at UK position on map = approx [-0.5, 1.5, 0], STONE_GREY font="Poppins" font_size=20, `FadeIn`
  - SFX: `sfx_bell.mp3`, -10dB

**T+0:07** | VO: *"Harvests fail across France."*
- WHEN CLOUD REACHES FRANCE on map (approx T+0:06):
  - LABEL: `"harvest failures"` at France position = approx [0.5, 0.5, 0], STONE_GREY font="Poppins" font_size=20, `FadeIn`

**T+0:10** | VO: *"The Northern Hemisphere cools by about 1.3 degrees."*
- VISUAL: Thermometer appears at `R5` = [5.0, 0, 0]:
  - Tall `Rectangle` stroke outline + filled mercury column (WHITE stroke, AMBER fill initially)
  - Mercury fill height drops from 60% to 47% of total thermometer height, `animate.scale` on fill, run_time=2s
  - LABEL: `"-1.3°C"` at [5.5, -0.5, 0], DANISH_NAVY BOLD font="Poppins" font_size=24, `FadeIn` as mercury drops
- SFX: none

**T+0:16** | Hold. Map with cloud over Europe, two labels, thermometer.

**T+0:18** | Scene end. Transition: `FadeOut` all map elements. Scene04 begins on same BG.

**MANIM NOTE:** Cloud Rectangle from Scene02 is the SAME object — do not recreate. Its motion from Iceland east to Europe is one continuous `animate.shift`. Thermometer is a simple composed VGroup (two Rectangles + Line). Do not use complex Manim thermometer class.
**SOUND NOTE:** Two sfx_bell hits, quiet. Music continues at -10dB. No other SFX.

---

### Scene04 — One in Four | `[TARGET: 20s]` | VO ~47w, ~19.4s

**VO:** *"In Iceland, approximately nine thousand people die. On an island of around forty thousand, that means one in every four or five. That is not a statistic you absorb. That is every family, every village, everyone knowing exactly who didn't make it through the winter."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: load `iceland_overview.png` at `CTR`, scale to 80% of frame height, `FadeIn` run_time=0.5s
- CHARACTER: none
- AUDIO: Music drops to near-silence, -20dB. Let the counter be heard.

**T+0:01** | VO: *"In Iceland, approximately nine thousand people die."*
- TEXT: `"~40,000"` at `TC` = [0, 2.8, 0], WHITE BOLD font="Poppins" font_size=80, `GrowFromCenter` run_time=0.5s
- LABEL: `"population of Iceland, 1783"` at [0, 2.0, 0], STONE_GREY LIGHT font="Poppins" font_size=18, `FadeIn`

**T+0:04** | VO: *"On an island of around forty thousand, that means one in every four or five."*
- ANIMATE: Counter `"~40,000"` begins ticking down, number updates every 0.3s, takes 7s to reach `"~31,000"`
- AUDIO: Each tick: `sfx_tick.mp3` at -15dB (quiet, metronomic)
- Counter animation should feel SLOW and deliberate — not fast. Viewer reads each change.

**T+0:11** | Counter reaches `"~31,000"` — STOPS.
- SFX: `sfx_collapse.mp3` at T+0:11, -8dB (heavy, single impact — the weight of the number)
- TEXT: `"1 in 4"` at `CTR` = [0, 0, 0], VOLCANIC_RED BOLD font="Poppins" font_size=96, `GrowFromCenter` run_time=0.6s
- TEXT: `"or 5"` at [2.0, 0, 0], VOLCANIC_RED LIGHT font="Poppins" font_size=48, `FadeIn` 0.3s after

**T+0:13** | VO: *"That is not a statistic you absorb."*
- VISUAL: HOLD. No new elements. Counter remains at ~31,000. The big `"1 in 4"` holds.
- AUDIO: Music silence continues.

**T+0:17** | VO: *"That is every family, every village, everyone knowing exactly who didn't make it through the winter."*
- VISUAL: Still holding. No movement.

**T+0:20** | Scene end. `FadeOut` all elements. Hold one beat of black before Scene05.

**MANIM NOTE:** The counter slowness is essential. `run_time=7s` for the number to drop from 40,000 to 31,000 means the viewer watches it happen. Do NOT speed it up. The silence + slow counter + sudden stop + "1 in 4" stamp is the entire emotional sequence. Three moments, nothing else.
**SOUND NOTE:** Music nearly silent (-20dB) during counter. sfx_tick at -15dB per tick. sfx_collapse fires ONCE when counter stops. No other SFX. Music does not resume until Scene05.

---

### Scene05 — The Ledger | `[TARGET: 20s]` | VO ~40w, ~16.6s

**VO:** *"Iceland in 1783 has already been through five centuries of foreign rule, two waves of plague, a pirate raid, a trade monopoly that strangled it dry, and a Reformation enforced at sword point. And now this."*

---

**T+0:00**
- BG: `WHITE_BG`
- VISUAL: A lined ledger page fills the center 60% of frame. `Rectangle` outline (STONE_GREY stroke_width=1), interior has 7 horizontal `Line` rules spaced 0.7u apart. `FadeIn` run_time=0.5s.
- CHARACTER: none
- AUDIO: Music resumes at -14dB, quiet string texture

**T+0:02** | VO: *"...five centuries of foreign rule..."*
- LINE 1 appears: `"Five centuries of foreign rule .................. [✓]"` at top ruled line, LEFT-aligned, font="Poppins" font_size=22
  - Text LEFT: STONE_GREY | Tick RIGHT: green `"[✓]"` at end of dotted leaders
  - `FadeIn` run_time=0.4s for text, then `GrowFromCenter` for tick 0.2s later
  - SFX: `sfx_tick.mp3` -8dB when tick appears

**T+0:05** | VO: *"...two waves of plague..."*
- LINE 2: `"Two waves of plague ..................................... [✓]"` same format, row 2
- SFX: `sfx_tick.mp3` -8dB

**T+0:07** | VO: *"...a pirate raid..."*
- LINE 3: `"Pirate raid .................................................... [✓]"` row 3
- SFX: `sfx_tick.mp3` -8dB

**T+0:09** | VO: *"...a trade monopoly that strangled it dry..."*
- LINE 4: `"Trade monopoly (strangled it dry) ........... [✓]"` row 4
- SFX: `sfx_tick.mp3` -8dB

**T+0:11** | VO: *"...and a Reformation enforced at sword point."*
- LINE 5: `"Reformation (enforced at sword point) ... [✓]"` row 5
- SFX: `sfx_tick.mp3` -8dB

**T+0:14** | VO: *"And now this."*
- LINE 6 appears in SHAKIER lettering (use a different font weight or slight rotation on each character):
  `"Geological catastrophe ............................. [✓]"` row 6
  - Text: VOLCANIC_RED instead of STONE_GREY
  - Tick: VOLCANIC_RED instead of green
  - SFX: `sfx_stamp.mp3` -5dB (heavier than the ticks)

**T+0:16**
- TEXT: `"And now this."` at `BC` = [0, -3.0, 0], AMBER BOLD font="Poppins" font_size=36, `GrowFromCenter`
- SFX: `sfx_bell.mp3` -8dB

**T+0:18** | Hold. Full ledger visible. `"And now this."` at bottom.

**T+0:20** | Scene end. `FadeOut` ledger. `"And now this."` holds slightly longer, fades last.

**MANIM NOTE:** Each ledger row: text body is STONE_GREY LEFT-aligned, dotted leaders are STONE_GREY, tick is right-aligned. All 6 lines use the same Row VGroup template. Row 6 (volcanic) uses `VOLCANIC_RED` throughout. "Shakier lettering" = apply `Rotate(0.5 * DEGREES)` individually to random characters in the string, or just a slightly heavier stroke. Keep it subtle.
**SOUND NOTE:** Five sfx_tick hits (one per checkmark). sfx_stamp on row 6. sfx_bell on final text. Staggered as noted.

---

### Scene06 — The Rewind | `[TARGET: 15s]` | VO ~28w, ~11.6s

**VO:** *"How did Iceland get here? Let's go back. Back to 1262, when the Icelanders handed themselves over. Voluntarily. Which is somehow the worst part."*

---

**T+0:00**
- BG: `DARK_BG`, `FadeToColor` from previous scene run_time=0.5s
- VISUAL: Large year counter `"1783"` at `CTR`, AMBER BOLD font="Poppins" font_size=120, `GrowFromCenter` run_time=0.5s
- CHARACTER: none
- AUDIO: Music builds slightly

**T+0:02** | VO: *"Let's go back."*
- ANIMATE: `"1783"` begins spinning backward — rapid intermediate values flash: `"1750"` ... `"1700"` ... `"1627"` ... `"1550"` ... `"1402"` ... `"1380"` ... `"1262"`
  - Each intermediate: hold 0.15s, slight blur (`opacity` flicker between 0.6-1.0)
  - run_time=5s total for spin
  - SFX: `sfx_clock.mp3` starts at T+0:02, -8dB, plays until T+0:07

**T+0:07** | Counter LANDS on `"1262"`:
- Text: `"1262"` color transitions from AMBER to STONE_GREY in 0.3s
- ANIMATE: `Scale(1.1)` then `Scale(1.0)` run_time=0.4s (thud on landing)
- SFX: `sfx_collapse.mp3` -8dB (single heavy thud)

**T+0:08** | VO: *"...when the Icelanders handed themselves over."*
- TEXT: `"The Icelanders handed themselves over."` at [0, -1.5, 0], WHITE LIGHT font="Poppins" font_size=28, `FadeIn` run_time=0.5s

**T+0:10** | VO: *"Voluntarily."*
- TEXT: `"Voluntarily."` at [0, -2.3, 0], AMBER BOLD font="Poppins" font_size=36, `GrowFromCenter` run_time=0.4s
- SFX: `sfx_bell.mp3` -10dB

**T+0:12** | VO: *"Which is somehow the worst part."*
- TEXT: `"(Which is somehow the worst part.)"` at [0, -3.0, 0], STONE_GREY ITALIC font="Poppins" font_size=22, `FadeIn`

**T+0:14** | Hold. `"1262"` + three text lines all visible.

**T+0:15** | Scene end. `FadeOut` all elements. Transition to Act One.

**MANIM NOTE:** Year counter reuse pattern matches Ep1 Scene07. Same behavior. The landing "thud" (scale bounce) is critical — it tells the viewer: we've arrived. Use same VGroup structure as Ep1.
**SOUND NOTE:** sfx_clock during spin (a mechanical tick-through sound). sfx_collapse on landing. sfx_bell on "Voluntarily." Three distinct SFX moments. Music fades slightly during spin, returns at T+0:08.

---

## ACT ONE — THE OLD COVENANT

---

### Scene07 — The Commonwealth | `[TARGET: 25s]` | VO ~70w, ~29s

**VO:** *"The Icelandic Commonwealth had worked for three hundred years without a king, without an army. Held together by the Althing (the world's oldest surviving parliament) and the stubbornness of a population who had sailed to the edge of the world specifically to avoid being governed. Then the Sturlung Age happened. Forty years of clan warfare. Iceland's great families tore into each other while Norway's King Hakon IV watched and applied pressure."*

---

**T+0:00**
- BG: `SAGE_GREEN` (#5C7A4E) — the ONLY warm-toned scene in this act. Signals "what was lost."
- MAP: Simplified Thingvellir valley: two STONE_GREY plate Rectangles at L5 and R5, slide in from off-screen (LEFT plate from far left, RIGHT plate from far right), run_time=1.5s
- Floor: GREEN Rectangle at bottom third of frame
- Law Rock: small STONE_GREY Ellipse at `CTR` bottom
- 30 small figures (Circle r=0.12 + Rectangle body 0.12x0.28, AMBER/brown tones) appear in a circle around the Law Rock, staggered `FadeIn` lag_ratio=0.05, run_time=1.5s
- LABEL: `"THE ALTHING"` at `TC` = [0, 3.0, 0], STONE_GREY BOLD font="Poppins" font_size=32, `FadeIn`
- LABEL: `"working fine, for 300 years"` at [0, 2.4, 0], STONE_GREY ITALIC font="Poppins" font_size=18, `FadeIn` 0.5s after
- AUDIO: `sfx_crowd_murmur.mp3` at -14dB (low background ambience)

**T+0:08** | VO: *"Then the Sturlung Age happened."*
- BG: `SAGE_GREEN` begins transitioning to `STONE_GREY` — `animate.set_fill(STONE_GREY, opacity=1)` on BG Rectangle, run_time=6s (slow drain of warmth across this and next beat)
- VISUAL: Three jagged crack VMobjects appear across the Thingvellir valley floor — same organic waypoint method as Scene01, NOT straight Lines:
  - CRACK A: `[-5, -1.8, 0] → [-3.6, -2.1, 0] → [-2.3, -1.6, 0] → [-0.8, -2.2, 0] → [0.5, -1.7, 0]` — short, left half
  - CRACK B: `[-1.5, -0.8, 0] → [0.2, -1.2, 0] → [1.8, -0.7, 0] → [3.1, -1.3, 0] → [4.8, -0.9, 0]` — longer, right half
  - CRACK C: `[-0.5, -2.5, 0] → [0.8, -2.9, 0] → [2.0, -2.4, 0]` — small, center-bottom
  - All: stroke_width=1.5, color=`VOLCANIC_RED`, `Create` staggered with lag_ratio=0.4, total run_time=2.5s
- SFX: `sfx_crack.mp3` -10dB, quieter than Scene01

**T+0:12** | VO: *"Forty years of clan warfare."*
- TEXT: `"Forty years."` at `BC` = [0, -3.0, 0], STONE_GREY BOLD font="Poppins" font_size=40, `GrowFromCenter` run_time=0.4s
- Lands exactly on *"Forty years."* — the two words in the VO. No other visual added. The cracked, draining scene speaks for itself.
- NOTE: Clan labels (STURLUNGS / ODDS) removed — VO names no clans, it says "great families." The cracks and BG drain already show the breakdown. Labels at this moment would compete with three simultaneous animations (BG drain, cracks still fading in, stamp) and give the viewer nothing the VO doesn't already cover.

**T+0:18** | VO: *"...while Norway's King Hakon IV watched and applied pressure."*
- CHARACTER: `hakon_iv.png` enters from `R5` (far right), slides in `animate.shift(LEFT*1.5)` run_time=1.0s, settles at `R3` = [3.0, 0, 0], height=2.5u
- LABEL: `"King Hakon IV"` at [3.0, -1.8, 0], WHITE BOLD font="Poppins" font_size=20, `FadeIn`
- LABEL: `"(watching)"` at [3.0, -2.3, 0], STONE_GREY ITALIC font="Poppins" font_size=16, `FadeIn` 0.3s after
- SFX: `sfx_whoosh.mp3` -12dB as character enters (subtle)
- Hakon holds his cup. He does not move further.

**T+0:22** | Hold. Cracked Thingvellir + "Forty years." stamp + Hakon watching. BG fully STONE_GREY.

**T+0:25** | Scene end. Hakon stays on screen into Scene08 (reuse object — do not recreate).

**MANIM NOTE:** Three VO-anchored beats: (1) Commonwealth reveal at *"three hundred years"*, (2) BG drain + cracks + "Forty years." stamp at *"Then the Sturlung Age happened...Forty years."*, (3) Hakon enters at *"King Hakon IV watched."* The BG drain runs for 6s across beats 2 and 3 — it is background state change, not a competing visual move. Hakon is the punchline and must feel late — the last thing that appears before scene end.
**SOUND NOTE:** sfx_crowd_murmur at scene open (-14dB). sfx_crack when cracks appear (-10dB). sfx_whoosh when Hakon enters (-12dB). Music continues at -12dB throughout.

---

### Scene08 — Snorri's Cellar | `[TARGET: 22s]` | VO ~38w, ~15.7s

**VO:** *"Snorri Sturluson, Iceland's greatest writer and historian, ended up in his cellar at Reykholt in 1241. Seventy of Hakon's men outside. His last recorded words: 'Eigi skal hoggva.' Do not strike. They struck."*

---

**T+0:00**
- BG: `DARK_BG`. Quick cut from Scene07 (no transition fade — hard cut)
- CHARACTER: `hakon_iv.png` from Scene07 EXITS RIGHT: `animate.shift(RIGHT*8)` run_time=0.5s, then `FadeOut`
- AUDIO: Music drops to near-silence, -20dB

**T+0:00** | CHARACTER: `snorri_writing.png` (REUSE from Ep1 Avatar 07) enters at `CTR`, `GrowFromCenter` run_time=0.8s, height=3.5u
- LABEL: `"Snorri Sturluson"` at [0, -2.2, 0], WHITE BOLD font="Poppins" font_size=32, `FadeIn`
- LABEL: `"Iceland's greatest writer"` at [0, -2.8, 0], WHITE LIGHT font="Poppins" font_size=22, `FadeIn` 0.3s after

**T+0:05** | VO: *"...ended up in his cellar at Reykholt in 1241."*
- TEXT: `"1241"` at `TR` = [4.5, 3.0, 0], AMBER BOLD font="Poppins" font_size=48, `GrowFromCenter`
- TEXT: `"Reykholt cellar"` at [4.5, 2.3, 0], STONE_GREY font="Poppins" font_size=18, `FadeIn` 0.3s after
- SFX: `sfx_bell.mp3` -10dB

**T+0:08** | VO: *"Seventy of Hakon's men outside."*
- TEXT: `"70 men outside."` at `TL` = [-4.5, 3.0, 0], WHITE BOLD font="Poppins" font_size=26, `FadeIn`
- VISUAL: `snorri_writing.png` dims (opacity 0.7) — swap or overlay a shadow Rectangle (DARK_BG at 0.3 opacity) over avatar
- BG: Floor darkens — add shadow Rectangle at bottom of frame, `FadeIn`

**T+0:12** | VO: *"His last recorded words: 'Eigi skal hoggva.'"*
- ANIMATE: snorri_writing.png exits via `FadeOut` run_time=0.3s
- CHARACTER: `snorri_afraid.png` (REUSE from Ep1 Avatar 07) enters at `CTR`, `FadeIn` run_time=0.5s, height=3.5u
- TEXT: `"Eigi skal hoggva."` at [0, 1.8, 0], WHITE ITALIC BOLD font="Poppins" font_size=52, `GrowFromCenter` run_time=0.5s
- TEXT: `"(Do not strike.)"` at [0, 1.0, 0], WHITE LIGHT font="Poppins" font_size=28, `FadeIn` 0.3s after
- SFX: `sfx_bell.mp3` -8dB

**T+0:15** | VO: *"They struck."*
- ANIMATE: All elements `FadeOut` over 1.5s — avatar, labels, "Eigi skal hoggva" text
- BG: transitions to pure black

**T+0:17** | Pure black. 1.5s of silence.

**T+0:18** | SFX: `sfx_collapse.mp3` -5dB (heavy single impact)
- TEXT: `"They struck."` at `CTR`, WHITE BOLD font="Poppins" font_size=64, `GrowFromCenter` run_time=0.3s

**T+0:19** | Hold. `"They struck."` on black. 3 seconds. Do not add anything.

**T+0:22** | `FadeOut` text. Scene end.

**MANIM NOTE:** Four VO-anchored beats — no floating visuals: (1) *"Snorri...cellar...1241"* → Hakon exits and Snorri enters simultaneously, labels and "1241" appear as one reveal; (2) *"Seventy of Hakon's men outside"* → "70 men outside" text + avatar dims; (3) *"Eigi skal hoggva"* → avatar swap + quote text; (4) *"They struck."* → black + stamp text. Hakon exit and Snorri entry happen in the same moment — run them as parallel animations (`AnimationGroup`), not sequentially. Two separate avatar states: `snorri_writing.png` FadeOut → `snorri_afraid.png` FadeIn. Use the SAME SD-generated assets from Ep1 — do NOT regenerate. The 1.5s of black before "They struck." is complete silence — no music, no SFX.
**SOUND NOTE:** sfx_bell at T+0:05 and T+0:12. COMPLETE SILENCE from T+0:15 to T+0:18 (kill music AND SFX). sfx_collapse at T+0:18 exactly. Music does not return until Scene09.

---

### Scene09 — The Old Covenant | `[TARGET: 22s]` | VO ~50w, ~20.7s

**VO:** *"Twenty years later, the surviving chieftains signed the Old Covenant and became Norwegian subjects. They kept their laws, in theory. They kept the Althing, in form. But sovereignty was gone. And once you hand that over, getting it back turns out to take about seven hundred years."*

---

**T+0:00**
- BG: `WHITE_BG`
- VISUAL: A formal contract scroll unfurls vertically from top to bottom — `Rectangle` reveal (height animates from 0 to 4.5u), STONE_GREY border, cream interior (`#F5F0E8`), run_time=1.5s
- Position: `CTR`, width=7u
- AUDIO: `sfx_paper.mp3` -8dB as scroll unfurls
- Music returns at -14dB, quiet

**T+0:01** | LABEL inside scroll at top: `"GAMLI SATTMALI"` STONE_GREY BOLD font="Poppins" font_size=24 centered
- LABEL: `"The Old Covenant — 1262"` STONE_GREY LIGHT font="Poppins" font_size=18 below title

**T+0:04** | VO: *"They kept their laws, in theory."*
- TEXT inside scroll, line 1: `"You keep your laws."` at [-1.0, 0.5, 0] relative to scroll, STONE_GREY font="Poppins" font_size=20, `FadeIn`
- TEXT footnote: `"          (in theory)"` immediately right of line 1, STONE_GREY ITALIC font="Poppins" font_size=14 — appears 0.5s after, like fine print being added

**T+0:07** | VO: *"They kept the Althing, in form."*
- TEXT inside scroll, line 2: `"You keep the Althing."` at [-1.0, -0.1, 0] relative to scroll, font="Poppins" font_size=20, `FadeIn`
- TEXT footnote: `"         (in form)"` ITALIC font="Poppins" font_size=14 — 0.5s after
- SFX: `sfx_paper.mp3` -12dB (subtle second rustle)

**T+0:10** | VO: *"But sovereignty was gone."*
- TEXT inside scroll, line 3: `"Norway keeps everything else."` at [-1.0, -0.7, 0], STONE_GREY BOLD font="Poppins" font_size=20, `FadeIn`

**T+0:12** | Four red wax seals stamp onto bottom of scroll, staggered 0.4s each:
- Each seal: `Circle(radius=0.25)` in `VOLCANIC_RED` with small `"X"` center, at positions bottom of scroll
- SFX: `sfx_stamp.mp3` -6dB for EACH stamp (4 hits, 0.4s apart)

**T+0:14** | Norwegian flag icon (small, Rectangle composition in Norwegian colors) rises over tiny Iceland outline at `TR` corner:
- `animate.shift(UP*1.5)` run_time=1.0s
- SFX: `sfx_whoosh.mp3` -12dB

**T+0:16** | VO: *"...getting it back turns out to take about seven hundred years."*
- TEXT below scroll: `"~700 years to get it back."` at [0, -3.2, 0], AMBER BOLD font="Poppins" font_size=36, `GrowFromCenter`
- SFX: `sfx_bell.mp3` -8dB

**T+0:20** | Hold. Scroll with text + seals + flag + verdict label.

**T+0:22** | Scene end. `FadeOut` all. Transition to Act Two.

**MANIM NOTE:** Contract scroll is a `Rectangle` with cream fill and STONE_GREY border. Text appears INSIDE it using relative positioning. The footnotes `"(in theory)"` and `"(in form)"` are the visual jokes — they must appear AFTER the main text, as if added reluctantly. Four stamp SFX, timed exactly 0.4s apart — they should feel like the deliberate weight of a decision being made.
**SOUND NOTE:** sfx_paper on scroll unfurl. sfx_paper again at T+0:07. Four sfx_stamp hits at T+0:12. sfx_whoosh for flag. sfx_bell for verdict. Music at -14dB throughout.

---

## ACT TWO — THE LONG SQUEEZE

---

### Scene10 — Denmark Inherits Iceland | `[TARGET: 17s]` | VO ~43w, ~17.8s

**VO:** *"In 1380, Norway merged with Denmark. Iceland came along. Whether Icelanders were formally informed is not entirely clear. They were simply Danish now. Not through conquest, but through a dynastic reshuffling in which no one thought to ask Iceland."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: `north_atlantic.png` at `CTR`, scale to fill frame, `FadeIn` run_time=0.5s. Norway and Iceland visible.
- AUDIO: Music at -14dB, institutional feel (thin harpsichord if available, else string pizzicato)

**T+0:02** | VO: *"In 1380, Norway merged with Denmark."*
- VISUAL: A small marriage icon at Norway-Denmark border on map: two `Circle` crown icons + a Ring linking them, `GrowFromCenter`
- LABEL: `"1380 — dynastic union"` at Norway-Denmark position, STONE_GREY font="Poppins" font_size=18, `FadeIn`

**T+0:05** | VO: *"Iceland came along."*
- VISUAL: Danish crown icon (simple: `Circle` with small points) slides from Denmark position toward Iceland on map: `animate.shift` along map path, run_time=1.5s
- SFX: `sfx_whoosh.mp3` -12dB
- Crown settles over Iceland. Norwegian crown icon fades out from Iceland.

**T+0:08** | VO: *"Whether Icelanders were formally informed is not entirely clear."*
- VISUAL: A posted-proclamation note appears OVER Iceland on map — `Rectangle` (cream fill, STONE_GREY border), tilted 3 degrees, `GrowFromCenter`:
  ```
  NOTICE TO ICELANDERS:
  You are now Danish.
  — Regards, Denmark

  P.S. No reply necessary.
  ```
  Font_size=16 inside note. Note appears water-stained (corner opacity at 0.6)

**T+0:12** | VO: *"...no one thought to ask Iceland."*
- CHARACTER: A small Icelandic figure (Circle head + Rectangle body, COLD_WHITE, scale=0.5) appears at `BL` area of Iceland on map, `GrowFromCenter`
- ANIMATE: Figure looks at the notice (slight `Rotate(15*DEGREES)` on head circle)
- ANIMATE: Figure shrugs — head shifts UP 0.1u then returns, run_time=0.5s
- LABEL: `"(not asked)"` at figure position, STONE_GREY ITALIC font="Poppins" font_size=14, `FadeIn`

**T+0:15** | Hold. Map with crown, notice, shrugging Icelander.

**T+0:17** | Scene end. Map `FadeOut`. Notice holds slightly longer then fades.

**MANIM NOTE:** The shrug is ONE small movement: head shifts up 0.1u then returns. Do not animate arms or body. A small figure with one small motion. The notice text must be readable — font="Poppins" font_size=16 inside the note is minimum.
**SOUND NOTE:** sfx_whoosh when crown slides. No other SFX. Music continues at -14dB throughout.

---

### Scene11 — It Got Worse | `[TARGET: 8s]` | VO ~8w, ~3.3s

**VO:** *"It got worse before it got worse."*

---

**T+0:00**
- BG: `DARK_BG`. Hard cut from Scene10.
- CHARACTER: none
- MAP: none
- AUDIO: Music CUTS to silence at T+0:00. Complete audio silence.

**T+0:01** | VO: *"It got worse"*
- TEXT: `"IT GOT WORSE"` at [0, 0.6, 0], WHITE BOLD font="Poppins" font_size=72, `GrowFromCenter` run_time=0.5s

**T+0:02** | VO: *"before it got worse."*
- TEXT: `"BEFORE IT GOT WORSE"` at [0, -0.6, 0], WHITE BOLD font="Poppins" font_size=72, `GrowFromCenter` run_time=0.5s

**T+0:03** | Both lines on screen. Hold 5 seconds. No animation. No music. No SFX. Nothing moves.

**T+0:08** | Scene end. `FadeOut` text. 0.5s fade.

**MANIM NOTE:** This is a pure title card. Two lines, full screen, no other elements whatsoever. The power is in the lack of embellishment and the silence. Do NOT add a background texture or color gradient. Pure black with white text.
**SOUND NOTE:** Complete silence for the entire 8s including any ambient music. Silence is the sound design here.

---

### Scene12 — The Black Death | `[TARGET: 25s]` | VO ~52w, ~21.5s

**VO:** *"The Black Death arrived in 1402, carried on a ship. It killed somewhere between a quarter and half the population. Scholars argue the exact figure. The people who died found the academic debate less interesting. It came back in 1494. Iceland's medieval population never fully recovered from either wave."*

---

**T+0:00**
- BG: `STONE_GREY` — full desaturation. No warmth.
- MAP: `iceland_overview.png` at `CTR`, opacity=0.4 (map visible but dim), `FadeIn` run_time=0.5s
- AUDIO: Music resumes at -16dB, low, institutional

**T+0:02** | VO: *"The Black Death arrived in 1402, carried on a ship."*
- VISUAL: A ship silhouette enters from RIGHT edge — simple hull polygon + mast `Line` in `DARK_BG` color, moves LEFT: `animate.shift(LEFT*3)` run_time=2.0s, settling at northwest coast of Iceland on map
- SFX: `sfx_whoosh.mp3` -12dB as ship arrives

**T+0:04** | As ship arrives:
- VISUAL: A small rat icon (Circle r=0.15 + curved tail Line) appears at the ship, `GrowFromCenter`, then `animate.shift(DOWN*0.5)` — walking off the gangplank
- SFX: `sfx_bell.mp3` -10dB (ominous low tone)

**T+0:07** | VO: *"It killed somewhere between a quarter and half the population."*
- TEXT: Population counter `"~50,000"` at `TC` = [0, 2.8, 0], WHITE BOLD font="Poppins" font_size=60, `GrowFromCenter`
- ANIMATE: Counter drops steadily to `"~37,000"` (25% loss) over 5s
- Each tick: `sfx_tick.mp3` -15dB

**T+0:12** | Counter reaches `"~37,000"`. Stops.
- SFX: `sfx_collapse.mp3` -10dB

**T+0:13** | VO: *"Scholars argue the exact figure. The people who died found the academic debate less interesting."*
- TEXT: Academic footnote box at `BR` = [4.0, -2.0, 0], `Rectangle` (STONE_GREY border, WHITE fill, width=3.5u, height=1.8u), `FadeIn`:
  ```
  "[SCHOLARS ARGUE: 25% to two-thirds]
  The people who died found this
  less interesting."
  ```
  Font_size=14, STONE_GREY text

**T+0:18** | VO: *"It came back in 1494."*
- STAMP: `"1494 — IT CAME BACK"` text at `CTR`, VOLCANIC_RED BOLD font="Poppins" font_size=32, `GrowFromCenter`
- SFX: `sfx_stamp.mp3` -6dB

**T+0:20** | VO: *"Iceland's medieval population never fully recovered from either wave."*
- TEXT: `"Never fully recovered."` at `BC` = [0, -3.0, 0], WHITE ITALIC font="Poppins" font_size=28, `FadeIn`

**T+0:23** | Hold. Dimmed map, counter, footnote, 1494 stamp, verdict text.

**T+0:25** | Scene end. All elements `FadeOut`. 0.5s fade.

**MANIM NOTE:** Ship enters from RIGHT — map's northwest coast is on the left side of the Iceland silhouette. So ship enters RIGHT, crosses to LEFT where it docks. Rat icon is tiny (r=0.15) — visible but not detailed. The footnote box is the only moment of dark comedy in an otherwise bleak scene. Keep it small, bottom right, like a footnote literally placed on the page.
**SOUND NOTE:** sfx_whoosh for ship. sfx_bell when rat appears. sfx_tick during counter drop (quiet, -15dB). sfx_collapse when counter stops. sfx_stamp for 1494. Music at -16dB (darker, thinner than normal).

---

### Scene13 — Jon Arason Introduced | `[TARGET: 28s]` | VO ~62w, ~25.7s

**VO:** *"Then came the Reformation. King Christian III of Denmark decided his entire kingdom was Lutheran now. In Iceland, one man stood in the way: Jon Arason, the Catholic bishop of Holar. Poet, nationalist, father of at least nine children. (The bishop apparently kept busy.) He understood the Reformation for exactly what it was: foreign cultural control wearing a clerical collar."*

---

**T+0:00**
- BG: `STONE_GREY` continues from Scene12
- CHARACTER: none yet
- MAP: none
- AUDIO: Music continues at -14dB

**T+0:02** | VO: *"Then came the Reformation."*
- TEXT: `"THE REFORMATION"` at `TC` = [0, 3.0, 0], DANISH_NAVY BOLD font="Poppins" font_size=36, `FadeIn`
- TEXT: `"1519-1550"` at [0, 2.3, 0], DANISH_NAVY font="Poppins" font_size=22, `FadeIn` 0.3s after

**T+0:05** | VO: *"In Iceland, one man stood in the way: Jon Arason, the Catholic bishop of Holar."*
- CHARACTER: `jon_arason_defiant.png` enters at `CTR` from bottom: `animate.shift(UP*8)` starting at [0, -8, 0], run_time=1.2s, settles at [0, 0.2, 0], height=3.8u
- SFX: `sfx_whoosh.mp3` -8dB (confident entry)
- LABEL: `"Jon Arason"` at [0, -2.2, 0], WHITE BOLD font="Poppins" font_size=32, `FadeIn`
- LABEL: `"Bishop of Holar"` at [0, -2.8, 0], WHITE LIGHT font="Poppins" font_size=22, `FadeIn` 0.3s after
- His crimson chasuble is visually prominent against the grey background

**T+0:09** | VO: *"Poet, nationalist, father of at least nine children."*
- DESCRIPTOR TAG 1: `"Poet"` — small `RoundedRectangle` background (AMBER), text WHITE BOLD font="Poppins" font_size=20, at [-3.0, 2.0, 0], `GrowFromCenter`
- DESCRIPTOR TAG 2: `"Nationalist"` — at [0, 2.5, 0], `GrowFromCenter` 0.8s after
- DESCRIPTOR TAG 3: `"Father of at least 9"` — at [3.0, 2.0, 0], `GrowFromCenter` 0.8s after

**T+0:13** | VO: *"(The bishop apparently kept busy.)"*
- VISUAL: Nine tiny circle figures (r=0.08 each, COLD_WHITE) appear in a row behind/below the avatar at [0, -3.4, 0], staggered `GrowFromCenter` lag_ratio=0.1, run_time=1.5s
- LABEL: `"(apparently kept busy)"` at [0, -3.8, 0], STONE_GREY ITALIC font="Poppins" font_size=16, `FadeIn` after children appear
- SFX: gentle `sfx_tick.mp3` x9 in rapid succession as each child appears, -15dB

**T+0:18** | VO: *"He understood the Reformation for exactly what it was: foreign cultural control wearing a clerical collar."*
- TEXT builds word by word at `BC` area [0, -4.2, 0] — but wait, that's outside safe zone. Place at [0, -3.0, 0]:
  `"Foreign cultural control"` appears, WHITE ITALIC font="Poppins" font_size=24, `Write` run_time=1.5s
- TEXT continues: `"wearing a clerical collar."` at [0, -3.6, 0], CRIMSON ITALIC font="Poppins" font_size=24, `Write` run_time=1.0s — the CRIMSON matches his vestments

**T+0:25** | Hold. Avatar in center + 3 tags + 9 children + final line.

**T+0:28** | Scene end. Avatar and tags remain visible — HOLD into Scene14 (do not exit Jon Arason).

**MANIM NOTE:** Jon Arason's CRIMSON is the only warm color in this entire grey section. The moment he enters, the color contrast is the visual statement. Three descriptor tags appear around him — these are small `RoundedRectangle` VGroups with text inside. Nine children are nine `Circle` objects in a row — they are tiny, decorative, and appear rapidly (the joke is the number, not the detail).
**SOUND NOTE:** sfx_whoosh on Jon Arason's entry (-8dB, confident). Nine rapid-fire sfx_tick hits when children appear (-15dB). Music at -14dB throughout.

---

### Scene14 — Decades of Resistance | `[TARGET: 15s]` | VO ~5w, ~2.1s

**VO:** *"He resisted for decades."*

---

**T+0:00**
- BG: `WHITE_BG`, fade from Scene13's STONE_GREY, run_time=0.5s
- CHARACTER: `jon_arason_defiant.png` scales down to 0.3 height and moves to `L5` = [-5.0, 0, 0] (becomes small icon on left of timeline)
- AUDIO: Music at -12dB

**T+0:00** | VISUAL: Horizontal timeline bar appears at `CTR`:
- `Rectangle` bar: width=10u, height=0.15u, `STONE_GREY`, at [0, 0, 0]
- LEFT label `"1519"` at [-5.0, 0.5, 0], STONE_GREY font="Poppins" font_size=18, `FadeIn`
- RIGHT label `"1550"` at [5.0, 0.5, 0], STONE_GREY font="Poppins" font_size=18, `FadeIn`
- Label above bar: `"DECADES OF RESISTANCE"` at [0, 1.0, 0], STONE_GREY BOLD font="Poppins" font_size=22, `FadeIn`

**T+0:02** | VO: *"He resisted for decades."*
- ANIMATE: Jon Arason icon moves RIGHT along bar to 25% point (x=-2.5u): `animate.shift(RIGHT*2.5)` run_time=0.8s
- Lutheran official figure (Circle r=0.12 + cross icon DANISH_NAVY, scale=0.25) enters from RIGHT at x=+5.0: `animate.shift(LEFT*2.5)` run_time=0.8s — they meet at x=0.0
- Jon Arason does NOT move backward. Lutheran figure retreats: `animate.shift(LEFT*3)` run_time=0.5s then `FadeOut`
- `"RESISTED"` Text (GREEN, font="Poppins" font_size=16) stamps at meeting point [−2.5, 0.8, 0]: `GrowFromCenter` run_time=0.3s
- SFX: `sfx_stamp.mp3` -8dB

**T+0:05** | Repeat at 50% point (x=0.0u):
- Jon Arason icon: `animate.shift(RIGHT*2.5)` run_time=0.8s
- New Lutheran figure enters from RIGHT x=+5.0, moves to meet: `animate.shift(LEFT*2.5)` run_time=0.8s
- Retreats: `animate.shift(LEFT*3)` run_time=0.5s then `FadeOut`
- `"RESISTED"` Text at [0, 0.8, 0]: `GrowFromCenter` run_time=0.3s
- SFX: `sfx_stamp.mp3` -8dB

**T+0:08** | Repeat at 75% point (x=+2.5u):
- Jon Arason icon: `animate.shift(RIGHT*2.5)` run_time=0.8s
- New Lutheran figure enters, retreats same pattern
- `"RESISTED"` Text at [+2.5, 0.8, 0]: `GrowFromCenter` run_time=0.3s
- SFX: `sfx_stamp.mp3` -8dB
- Three `"RESISTED"` labels now line the timeline in green.

**T+0:11** | Jon Arason reaches the `"1550"` end point.
- A single RED `"X"` stamp appears over the `"1550"` marker: `GrowFromCenter` run_time=0.3s
- SFX: `sfx_collapse.mp3` -8dB
- Jon Arason icon fades slightly at this moment (opacity 0.5)

**T+0:13** | Hold. Full timeline with three `"RESISTED"` labels + red X at end.

**T+0:15** | Scene end. Timeline stays visible — Jon Arason exits: `FadeOut` at `L5`.

**MANIM NOTE:** Jon Arason's icon (scaled-down version of the avatar, scale=0.3) moves along the timeline in THREE beats. Each beat: he moves RIGHT, a Lutheran figure enters from RIGHT, they meet, Lutheran retreats, "RESISTED" stamps. The timing of each beat is ~3s. The final red X is heavier than the stamps — use sfx_collapse, not sfx_stamp.
**SOUND NOTE:** Three sfx_stamp hits (evenly spaced at T+0:02, T+0:05, T+0:08). sfx_collapse at T+0:11. Music at -12dB throughout.

---

### Scene15 — The Execution | `[TARGET: 17s]` | VO ~40w, ~16.6s

**VO:** *"On the seventh of November, 1550, he was beheaded alongside two of his sons, Ari and Bjorn. Catholic properties were seized by Danish administrators. Iceland's spiritual life was changed by royal decree. The island took the blow and kept going."*

---

**T+0:00**
- BG: `DARK_BG`. Hard cut from Scene14.
- AUDIO: Music CUTS to silence. Complete.

**T+0:00** | TEXT: `"7 November 1550"` at [0, 2.5, 0], AMBER BOLD font="Poppins" font_size=52, `GrowFromCenter` run_time=0.5s
- SFX: `sfx_stamp.mp3` -5dB (hard, final)

**T+0:02** | CHARACTER: `jon_arason_calm.png` enters at `CTR`, `FadeIn` run_time=1.0s, height=4.0u
- Avatar shows Jon Arason + two sons flanking, all calm, all still, all facing forward
- No labels. No movement. Just the three figures.
- AUDIO: Silence continues.

**T+0:06** | VO: *"...he was beheaded alongside two of his sons, Ari and Bjorn."*
- VISUAL: No new elements. Hold on three calm figures.

**T+0:10** | VO: *"Catholic properties were seized..."*
- ANIMATE: Three figures dim to opacity=0.4 over 3s (`animate.set_opacity(0.4)` run_time=3.0s — slow, deliberate)

**T+0:12** | VO: *"Iceland's spiritual life was changed by royal decree."*
- TEXT stacked at `BC`, three lines fading in 1.5s apart:
  - `"Catholic properties: seized."` WHITE LIGHT font="Poppins" font_size=24 at [0, -2.0, 0], `FadeIn`
  - `"Spiritual life: changed by decree."` WHITE LIGHT font="Poppins" font_size=24 at [0, -2.6, 0], `FadeIn` 1.5s after
  - `"The island took the blow and kept going."` AMBER ITALIC font="Poppins" font_size=24 at [0, -3.2, 0], `FadeIn` 1.5s after

**T+0:16** | Hold. Three dimmed figures + three text lines. Silence continues.

**T+0:17** | Scene end. All `FadeOut`. Music resumes at -14dB from silence.

**MANIM NOTE:** `jon_arason_calm.png` shows all three figures (Arason + two sons) in one image. The figures dimming slowly IS the death — do not use a graphic representation. The stacked text below them is the epilogue. The silence throughout this scene is essential — music returns AFTER the scene ends, not during.
**SOUND NOTE:** sfx_stamp at T+0:00 (date stamp — hard). Complete silence from T+0:00 to T+0:17. Music resumes at start of Scene16. No exceptions to the silence.

---

## ACT THREE — THE MONOPOLY AND THE PIRATES

---

### Scene16 — Trade Monopoly | `[TARGET: 25s]` | VO ~65w, ~26.9s

**VO:** *"The trade monopoly landed in 1602 and it landed hard. The Danish crown carved Iceland into trading districts, each handed to a licensed merchant. Icelanders sold to them and bought from them at prices the merchants set. Fish went out cheap. Consumer goods came in expensive. Economic diversification was impossible by design. The monopoly ran until 1787. Its damage ran considerably longer."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: `iceland_overview.png` at `CTR`, `FadeIn` run_time=0.5s
- AUDIO: Music at -12dB, harpsichord texture (thin, mechanical — institutional feel)

**T+0:02** | VO: *"The Danish crown carved Iceland into trading districts..."*
- VISUAL: A grid of `Rectangle` borders (thick DANISH_NAVY stroke_width=2, no fill) divides the map into 7-8 trading districts. Grid `Create`s outward from center, run_time=2s.
- SFX: `sfx_stamp.mp3` -8dB as grid appears

**T+0:05** | VO: *"...each handed to a licensed merchant."*
- VISUAL: In each district, a small merchant figure (Circle head + Rectangle body in dark coat, arms-crossed pose) appears: staggered `GrowFromCenter` lag_ratio=0.15, run_time=2s
- Each merchant: arms crossed, looking smug
- COUNT: 7-8 merchants, one per district

**T+0:10** | VO: *"Icelanders sold to them and bought from them at prices the merchants set."*
- VISUAL: A simple flowchart appears RIGHT of map at [5.5, 0, 0]:
  Title: `"THE MONOPOLY"` STONE_GREY BOLD font="Poppins" font_size=16
  Lines build downward:
  ```
  ICELANDERS catch fish
       |
  sell to merchant
  (at merchant's price)
       |
  merchant sells back
  (at merchant's price)
       |
  ICELANDERS save money...
       |
  (oh. they can't.)
  ```
  Each text line: `FadeIn` run_time=0.4s. Each `|` connector: `Text("|", font="Poppins", font_size=14, color=STONE_GREY)`, `FadeIn` run_time=0.2s. Text line appears first, connector 0.3s after, then next text line 1.2s after connector. Total cascade: 1.5s per link.

**T+0:20** | VO: *"The monopoly ran until 1787. Its damage ran considerably longer."*
- TEXT: `"1602 — 1787. 185 years."` at `BC` = [0, -3.0, 0], STONE_GREY BOLD font="Poppins" font_size=28, `FadeIn`
- TEXT: `"Its damage ran considerably longer."` at [0, -3.5, 0], WHITE ITALIC font="Poppins" font_size=22, `FadeIn` 1s after

**T+0:23** | Hold. Map with grid + merchants + flowchart + verdict text.

**T+0:25** | Scene end. Map and merchants HOLD into Scene17 (same map, do not reload).

**MANIM NOTE:** The flowchart is placed RIGHT of the map frame. It must use font="Poppins" font_size=14-16 — small enough to be a sidebar, large enough to read. The `"(oh. they can't.)"` final line is the punchline. It appears LAST, after a 1.5s beat. The harpsichord music texture is intentional for this section — institutional, cold, slightly annoying. If unavailable, use thin pizzicato strings.
**SOUND NOTE:** sfx_stamp when grid appears. No other SFX. Music at -12dB, harpsichord texture throughout Acts 3 and partial Act 4.

---

### Scene17 — The Scales | `[TARGET: 12s]` | VO ~10w, ~4.1s

**VO:** *"Fish went out cheap. Consumer goods came in expensive."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: `iceland_overview.png` from Scene16 `FadeOut` while balance scale `FadeIn` at `CTR`
- VISUAL: Balance scale at `CTR` — build as a single `VGroup` so rotation works correctly:
  - Triangle fulcrum: `Polygon([-0.4,-1.5,0], [0.4,-1.5,0], [0,-0.5,0])`, fill=STONE_GREY — NOT a `Triangle()` (use `Polygon` for explicit vertex control)
  - Vertical post: `Line([0,-1.5,0],[0,-0.5,0])`, stroke_width=2, STONE_GREY
  - Horizontal beam: `Line([-3.0,-0.5,0],[3.0,-0.5,0])`, stroke_width=2, STONE_GREY — beam has slight natural sag: add midpoint [0,-0.55,0] via VMobject waypoints so it bows very slightly downward (not a straight Line)
  - LEFT pan suspension: `Line([-3.0,-0.5,0],[-3.0,0.2,0])`, stroke_width=1.5, STONE_GREY
  - RIGHT pan suspension: `Line([3.0,-0.5,0],[3.0,0.2,0])`, stroke_width=1.5, STONE_GREY
  - LEFT pan: `Arc` (flat-bottomed half-circle), radius=0.7, centered at [-3.0, 0.2, 0], STONE_GREY stroke_width=2 — curved pan, not a circle
  - RIGHT pan: same `Arc` at [3.0, 0.2, 0]
  - Assemble all above into `VGroup(fulcrum, post, beam, left_susp, right_susp, left_pan, right_pan)` — rotation pivot at [0,-0.5,0]
- Scale appears in balanced position. `FadeIn` run_time=0.8s.
- AUDIO: Music continues at -12dB

**T+0:02** | VO: *"Fish went out cheap."*
- LEFT pan: Fish icon stack — 5 fish shapes, each built as: `VMobject` with waypoints tracing a simple fish body (oval body + V tail): body approx `[(-0.15,0,0),(-0.05,0.06,0),(0.1,0.06,0),(0.15,0,0),(0.1,-0.06,0),(-0.05,-0.06,0),(-0.15,0,0)]` + tail `[(0.1,0.06,0),(0.2,0.1,0),(0.18,0,0),(0.2,-0.1,0),(0.1,-0.06,0)]`, fill=STONE_GREY. Stack 5 of these at slightly different y offsets inside the LEFT pan VGroup. `FadeIn`.
- LABEL above left pan: `"FISH — out"` STONE_GREY font="Poppins" font_size=18, arrow pointing LEFT
- LABEL below left pan: `"price: very low"` STONE_GREY ITALIC font="Poppins" font_size=14

**T+0:04** | VO: *"Consumer goods came in expensive."*
- RIGHT pan: Single small goods Rectangle (nearly empty), `FadeIn`
- LABEL above right pan: `"GOODS — in"` STONE_GREY font="Poppins" font_size=18, arrow pointing RIGHT from off-screen
- LABEL below right pan: `"price: very high"` RED font="Poppins" font_size=14

**T+0:05** | ANIMATE: The scale TIPS:
- Beam `Rotate(-25*DEGREES)` around center fulcrum, run_time=1.0s (left drops, right rises)
- LEFT pan swings DOWN dramatically
- RIGHT pan swings UP
- SFX: `sfx_collapse.mp3` -8dB as scale tips (weight of fish dropping)

**T+0:06** | Hold. Scale wildly unbalanced. Fish side nearly touching the ground.

**T+0:10** | Hold continues. No new elements.

**T+0:12** | Scene end. `FadeOut` scale. Hard cut to Scene18.

**MANIM NOTE:** The scale rotation is ONE animation — the entire beam rotates around its center point. This is a single `Rotate` call on a `VGroup` containing the beam + both pan-connection Lines + both pan circles. It should feel sudden and final (run_time=1.0s, not slower). Hold 6s on the tipped scale — let the imbalance be visually obvious.
**SOUND NOTE:** sfx_collapse when scale tips (-8dB). No other SFX in this scene. Music at -12dB.

---

### Scene18 — Defenceless | `[TARGET: 15s]` | VO ~30w, ~12.4s

**VO:** *"The monopoly didn't just impoverish Iceland. It made it defenceless. No surplus meant no investment, no infrastructure, no capacity to respond when things went catastrophically wrong."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: `iceland_overview.png` `FadeIn` at `CTR`, opacity=0.7
- VISUAL: Merchant district grid from Scene16 fades back in over map at 30% opacity (semi-transparent, serves as visual reminder)
- AUDIO: Music at -12dB

**T+0:02** | VO: *"It made it defenceless."*
- TEXT: `"Defenceless."` at `TC` = [0, 3.0, 0], WHITE BOLD font="Poppins" font_size=48, `GrowFromCenter`
- SFX: `sfx_bell.mp3` -8dB

**T+0:04** | VO: *"No surplus..."*
- LABEL 1: Empty bag icon (Rectangle outline, no fill) + `"No surplus"` at Iceland's west coast on map, STONE_GREY font="Poppins" font_size=18, `FadeIn`

**T+0:06** | VO: *"...no investment..."*
- LABEL 2: Empty building outline (Rectangle outline) + `"No investment"` at Iceland's south coast, `FadeIn`

**T+0:08** | VO: *"...no capacity to respond when things went catastrophically wrong."*
- LABEL 3: `"No capacity to respond"` at Iceland's north coast, `FadeIn`

**T+0:10** | VO: *"...when things went catastrophically wrong."*
- VISUAL: A ship silhouette enters from off-screen RIGHT at [8.5, -1.2, 0] (fully off-frame), `animate.shift(LEFT*1.5)` run_time=4s — ends at [7.0, -1.2, 0], still barely in frame. opacity=0.35 (faint silhouette, not a clear ship). Build as VMobject:
  - Hull: curved bottom path `[(-0.8,-0.2,0),(-0.6,-0.35,0),(0,-0.4,0),(0.6,-0.35,0),(0.8,-0.2,0)]` closed, fill=STONE_GREY opacity=0.35
  - Mast: `Line([0,-0.2,0],[0,0.4,0])`, stroke_width=1.5, STONE_GREY opacity=0.35
  - Scale entire VGroup to 0.6u height
  - This is NOT a rectangular hull — the curved keel reads as a warship profile, not a merchant vessel
- SFX: `sfx_whoosh.mp3` -15dB (barely audible — ominous)

**T+0:13** | Hold. Map with three labels + mystery ship on horizon edge.

**T+0:14** | TEXT: `"Things went catastrophically wrong."` at `BC` = [0, -3.0, 0], WHITE BOLD font="Poppins" font_size=28, `FadeIn`

**T+0:15** | Scene end. Map fades. Mystery ship holds into Scene19 momentarily.

**MANIM NOTE:** The mystery ship at T+0:10 is a setup for Scene19's reveal. It should be barely visible — a shape at the edge of frame, not labeled, not explained. The viewer may notice it or may not. Do not draw attention to it. The three "No X" labels are placed at different coastal positions on the actual Iceland map — use the real geography.
**SOUND NOTE:** sfx_bell at T+0:02. sfx_whoosh at T+0:10 (very quiet, -15dB). Music at -12dB.

---

### Scene19 — Barbary Corsairs | `[TARGET: 10s]` | VO ~2w, ~0.8s

**VO:** *"Barbary corsairs."*

---

**T+0:00**
- BG: `DARK_BG`. Hard cut from Scene18. All map elements gone.
- AUDIO: Music CUTS to silence. Complete.
- CHARACTER: none
- MAP: none

**T+0:01** | VO: *"Barbary corsairs."*
- TEXT: `"Barbary corsairs."` at [0, 0.5, 0], WHITE BOLD font="Poppins" font_size=72, `GrowFromCenter` run_time=0.4s

**T+0:03** | TEXT: `"(This will sound made up."` at [0, -0.8, 0], STONE_GREY ITALIC font="Poppins" font_size=26, `FadeIn` run_time=0.4s

**T+0:05** | TEXT: `"It is not made up.)"` continues on same line or line below, STONE_GREY ITALIC font="Poppins" font_size=26, `FadeIn` run_time=0.4s

**T+0:06** | Hold. Two lines. Black background. Silence.

**T+0:10** | Scene end. Text `FadeOut`. Music does NOT return yet — Scene20 opens in silence briefly.

**MANIM NOTE:** Two words and a disclaimer. This is the shortest scene in the episode. Its power is complete nakedness — nothing on screen but the text, no sound at all. Do not add any graphical element. Do not add ambient music. Two lines of text on black.
**SOUND NOTE:** Complete silence for all 10s. No music, no SFX, no ambient. Silence is the sound design.

---

### Scene20 — The Raid | `[TARGET: 28s]` | VO ~60w, ~24.8s

**VO:** *"In 1627, ships from Algiers (commanded by Murat Reis the Younger, a Dutchman who had converted to Islam and gone into the raiding business) arrived on the coast of Iceland. They hit the East Fjords, then Grindevik, then spent three days on the Vestmannaeyjar islands. They killed approximately fifty people. They kidnapped approximately four hundred."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: Wide view of `north_atlantic.png` showing both Iceland (top) and North Africa/Algeria (bottom), `FadeIn` run_time=0.5s
- AUDIO: Music returns at -10dB — SUDDEN shift to `oud` or plucked string texture (audibly different from prior harpsichord). This musical shift IS the scene transition. Jarring. Intentional.
- CHARACTER: `murat_reis.png` enters at `L3` = [-3.0, 0.5, 0], `GrowFromCenter` run_time=0.6s, height=2.8u

**T+0:02** | VO: *"In 1627, ships from Algiers..."*
- LABEL: `"Murat Reis the Younger"` at [-3.0, -1.5, 0], WHITE BOLD font="Poppins" font_size=22, `FadeIn`
- LABEL: `"Born: Dutch. Converted. Career: raiding."` at [-3.0, -2.1, 0], STONE_GREY LIGHT font="Poppins" font_size=16, `FadeIn`
- VISUAL: The long arrow begins animating from Algeria on the map — `Create` of a curved `CurvedArrow` from bottom of map to top (Algeria to Iceland), run_time=5s, CORSAIR_OCHRE color, stroke_width=2

**T+0:04** | VO: *"...commanded by Murat Reis the Younger, a Dutchman who had converted to Islam..."*
- As arrow curves upward, a label tracks along the path midway: `"(yes, this far)"` STONE_GREY ITALIC font="Poppins" font_size=18, `FadeIn` at midpoint of arrow

**T+0:10** | VO: *"...arrived on the coast of Iceland."*
- Arrow reaches Iceland. Map zooms in: Iceland fills the frame (`north_atlantic.png` scales up, Iceland becomes dominant), run_time=1.5s
- `murat_reis.png` exits LEFT: `animate.shift(LEFT*8)` + `FadeOut` run_time=0.8s
- SFX: `sfx_whoosh.mp3` -8dB as arrow completes and map zooms

**T+0:13** | VO: *"They hit the East Fjords..."*
- Three raid location dots appear on Iceland map in sequence:
  - DOT 1: RED `Circle(r=0.15)` at East Fjords position on map + label `"East Fjords"`, `GrowFromCenter`
  - SFX: `sfx_stamp.mp3` -6dB

**T+0:16** | VO: *"...then Grindevik..."*
  - DOT 2: RED `Circle(r=0.15)` at Grindevik position + label `"Grindevik"`, `GrowFromCenter`
  - SFX: `sfx_stamp.mp3` -6dB

**T+0:18** | VO: *"...then spent three days on the Vestmannaeyjar islands."*
  - DOT 3: RED `Circle(r=0.25)` — LARGER — at Vestmannaeyjar position + label `"Vestmannaeyjar"` + sub-label `"3 days"`, `GrowFromCenter` with pulse animation (scale 1.0 to 1.3 to 1.0)
  - SFX: `sfx_stamp.mp3` -4dB (louder — more weight)

**T+0:21** | VO: *"They killed approximately fifty people."*
- COUNTER: `"~50 killed"` at `TL` = [-4.5, 2.8, 0], RED BOLD font="Poppins" font_size=32, `GrowFromCenter`
- SFX: `sfx_collapse.mp3` -10dB

**T+0:23** | VO: *"They kidnapped approximately four hundred."*
- COUNTER: `"~400 kidnapped"` at [-4.5, 1.8, 0], RED BOLD font="Poppins" font_size=32, `GrowFromCenter` 1.5s after previous
- SFX: `sfx_collapse.mp3` -8dB

**T+0:26** | Hold. Map with three dots + two counters.

**T+0:28** | Scene end. Map holds into Scene21 (same Iceland close-up map, do not reload).

**MANIM NOTE:** The long arrow from Algeria to Iceland is the scene's visual anchor. `CurvedArrow` in `CORSAIR_OCHRE` — the warm color intrudes into the map's grey-blue palette, visually telling the story before VO explains it. The musical shift from harpsichord to oud/plucked strings at T+0:00 is the audio equivalent of the visual intrusion. The map zoom at T+0:10 is one confident move — Iceland fills the frame as the ships arrive.
**SOUND NOTE:** Music texture shifts to `oud`/plucked at T+0:00 (-10dB). sfx_whoosh at T+0:10 (-8dB). Three sfx_stamp hits (-6dB, -6dB, -4dB escalating). Two sfx_collapse hits for the counters. Silence between stamp hits for weight.

---

### Scene21 — The Procession | `[TARGET: 18s]` | VO ~42w, ~17.4s

**VO:** *"Four hundred Icelanders were loaded onto ships and transported to North Africa to be sold into slavery. The event entered memory as Tyrkjaranid, the Turkish Raid. Because 'Algerian raid by a Dutch convert' apparently lacked the necessary ring."*

---

**T+0:00**
- MAP: Iceland close-up from Scene20 remains. `FadeOut` raid dots and counters from Scene20 over 0.5s.
- AUDIO: Music drops to -15dB. Quieter.

**T+0:01** | VO: *"Four hundred Icelanders were loaded onto ships..."*
- VISUAL: 400 tiny figure icons arranged in column formation at Iceland's south coast. Appear in groups of 20, staggered `FadeIn`, run_time=2s total.
  - Each figure: Circle r=0.06 (head) + Rectangle 0.06x0.12 (body), base color COLD_WHITE
  - Add variation — figures are NOT identical. In `tiny_figure()` factory function, apply per-figure:
    - `Rotate(random.uniform(-8, 8) * DEGREES)` on the whole figure (slight lean)
    - Random scale: `scale(random.uniform(0.85, 1.15))` (slight height variation)
    - Random opacity: `set_opacity(random.uniform(0.7, 1.0))` (some slightly fainter, further away)
    - Use `random.seed(42)` before the loop for reproducible randomness across re-renders

**T+0:03** | ANIMATE: The entire column of 400 figures `animate.shift(RIGHT*5)` — moving toward ship icons at Iceland's southern coast. run_time=4s.
- SFX: `sfx_crowd_murmur.mp3` -14dB (low ambience of many people moving)

**T+0:07** | Figures reach ships. Ships depart south: `animate.shift(DOWN*6)` (off the map toward North Africa), run_time=3s.
- The reversed long arrow from Scene20 reactivates: `Create` from Iceland DOWN toward Algeria, COLD_WHITE color (figures going the other direction now)
- Figures scale down as they travel: entire VGroup starts at scale=1.0, animate to scale=0.55 over the 3s departure (`animate.scale(0.55)` run_time=3s concurrent with ship movement) — simulates distance/receding from view
- Music drops to -20dB. Near silence.

**T+0:10** | STOP all animation. Silence. 2 seconds.

**T+0:12** | VO: *"The event entered memory as Tyrkjaranid, the Turkish Raid."*
- TEXT: `"TYRKJARANID"` at `TC` = [0, 2.8, 0], WHITE BOLD font="Poppins" font_size=40, `Write` run_time=0.8s
- TEXT: `"The Turkish Raid"` at [0, 2.1, 0], WHITE LIGHT font="Poppins" font_size=28, `FadeIn`

**T+0:15** | VO: *"Because 'Algerian raid by a Dutch convert' apparently lacked the necessary ring."*
- TEXT: `"(Algiers is not in Turkey."` at [0, -2.5, 0], STONE_GREY ITALIC font="Poppins" font_size=18, `FadeIn`
- TEXT: `"The commander was Dutch."` at [0, -3.0, 0], STONE_GREY ITALIC font="Poppins" font_size=18, `FadeIn` 0.5s after
- TEXT: `"'Algerian Raid by a Dutch Convert' lacked the ring.)"` at [0, -3.1, 0], STONE_GREY ITALIC font="Poppins" font_size=13, `FadeIn` 0.5s after — font_size=13 keeps this within safe zone Y bound at -3.1

**T+0:17** | Hold.

**T+0:18** | Scene end. `FadeOut` all. Transition to Scene22.

**MANIM NOTE:** 400 figures is a VGroup of 400 small composed shapes. Use `VGroup(*[tiny_figure() for _ in range(400)])` created in a 20-column grid. The column-formation moving toward ships is ONE `animate.shift` on the entire VGroup. Do not animate individual figures. The silence at T+0:10 (2s) is the weight of the procession completing — let it sit before the title card.
**SOUND NOTE:** sfx_crowd_murmur at -14dB during procession. Music drops to -20dB at T+0:07. Two seconds of near-complete silence at T+0:10. Music does not return until Scene22.

---

### Scene22 — Gudridur | `[TARGET: 22s]` | VO ~55w, ~22.8s

**VO:** *"The monopoly meant no money to ransom them quickly. Most spent the rest of their lives in Algiers. About fifty eventually returned. The most famous was Gudridur Simonardottir, nine years in North Africa before coming home to marry the great poet Hallgrimur Petursson. She endured. She rebuilt. She made a life. That pattern will keep coming up."*

---

**T+0:00**
- BG: `WHITE_BG`
- MAP: none
- CHARACTER: `gudridur.png` enters at `CTR` from position [0, -8, 0], slides up to [0, 0.2, 0], height=3.8u, `animate.shift(UP*8)` run_time=1.0s
- SFX: `sfx_whoosh.mp3` -12dB (quiet entry)
- AUDIO: Music returns at -12dB, quiet, single string thread

**T+0:02** | CHARACTER is now visible at CTR, standing still, composed.
- LABEL: `"Gudridur Simonardottir"` at [0, -2.2, 0], WHITE BOLD font="Poppins" font_size=28, `FadeIn`
- LABEL: `"Nine years in North Africa"` at [0, -2.8, 0], STONE_GREY LIGHT font="Poppins" font_size=20, `FadeIn` 0.3s after

**T+0:05** | VO: *"About fifty eventually returned. The most famous was Gudridur Simonardottir..."*
- VISUAL: A small arrow indicator points to the beadwork detail at her cap edge (a tiny `Arrow` pointing to the bead area on the right side of her headscarf)
- LABEL: `"(she kept it)"` at [2.5, 1.8, 0], STONE_GREY ITALIC font="Poppins" font_size=16, `FadeIn` — small, easy to miss

**T+0:12** | VO: *"She endured."*
- TEXT: `"She endured."` at [0, -2.2, 0], WHITE BOLD font="Poppins" font_size=28, `FadeIn`
- SFX: `sfx_bell.mp3` -12dB

**T+0:15** | VO: *"She rebuilt."*
- TEXT: `"She rebuilt."` at [0, -2.7, 0], WHITE BOLD font="Poppins" font_size=28, `FadeIn`

**T+0:17** | VO: *"She made a life."*
- TEXT: `"She made a life."` at [0, -3.2, 0], WHITE BOLD font="Poppins" font_size=28, `FadeIn`
- NOTE: Three lines stacked from Y=-2.2 to Y=-3.2. All within safe zone (floor -3.1 at 28pt; this is tight — if rendering clips, reduce to font_size=24 and start at Y=-2.0 with 0.5u spacing)

**T+0:19** | VO: *"That pattern will keep coming up."*
- ANIMATE: The three lines above `FadeOut` run_time=0.5s, replaced immediately by:
- TEXT: `"That pattern will keep coming up."` at [0, -2.7, 0], AMBER ITALIC font="Poppins" font_size=26, `FadeIn` run_time=0.5s
- SFX: `sfx_bell.mp3` -10dB

**T+0:21** | Hold. Gudridur at center. Bead arrow. Three lines + final pattern line.

**T+0:22** | Scene end. Gudridur `FadeOut` downward: `animate.shift(DOWN*8)` + `FadeOut` run_time=0.8s.

**MANIM NOTE:** Stack the three "She endured/rebuilt/made a life" lines BELOW the character label area. They accumulate — each new line appears below the previous, so all three are visible when the pattern line appears. Gudridur NEVER moves during the scene. She enters (one motion), then stands completely still. Her stillness IS the character.
**SOUND NOTE:** sfx_whoosh on entry (-12dB, quiet). sfx_bell at "She endured" (-12dB) and "That pattern will keep coming up" (-10dB). Music at -12dB throughout, single thread.

---

## ACT FOUR — THE RECKONING

---

### Scene23 — Return to Laki | `[TARGET: 12s]` | VO ~11w, ~4.5s

**VO:** *"And then 1783. Now you know how Iceland got there."*

---

**T+0:00**
- BG: `DARK_BG`. Hard cut.
- VISUAL: The SAME glowing crack VMobject from Scene01 reappears — recreate with IDENTICAL waypoints: `[-7,-0.3,0]→[-5.2,-0.6,0]→[-3.8,-0.1,0]→[-2.4,-0.7,0]→[-1.1,-0.2,0]→[0,-0.5,0]→[1.2,-0.8,0]→[2.5,-0.3,0]→[3.9,-0.9,0]→[5.1,-0.4,0]→[7,-0.6,0]`, VOLCANIC_RED stroke_width=2, plus the same glow pass (second VMobject same waypoints ±0.12u offset, opacity=0.3, stroke_width=3). Must be pixel-identical to Scene01 — use the same function/class to build it.
- AUDIO: The SAME single cello note from Scene01 returns from silence, -18dB, immediate

**T+0:01** | VO: *"And then 1783."*
- TEXT: `"1783"` at [0, 1.5, 0], AMBER BOLD font="Poppins" font_size=80, `GrowFromCenter` run_time=0.4s
- SFX: `sfx_bell.mp3` -8dB

**T+0:04** | VO: *"Now you know how Iceland got there."*
- TEXT: `"Now you know how Iceland got there."` at [0, -2.0, 0], WHITE LIGHT font="Poppins" font_size=28, `FadeIn` run_time=0.5s

**T+0:06** | Hold. Glowing crack + `"1783"` + recognition text. Music sustains.

**T+0:10** | Hold continues.

**T+0:12** | Scene end. Elements hold into Scene24.

**MANIM NOTE:** This is a callback. The crack must be IDENTICAL to Scene01 — same position, same VOLCANIC_RED, same glow effect. The cello note must be the SAME note and same audio treatment. The audience recognition is the entire emotional beat. Do not add anything new.
**SOUND NOTE:** Cello drone returns immediately at T+0:00 (-18dB), same as Scene01. sfx_bell at T+0:01 (-8dB). No other SFX. Music stays at cello drone level.

---

### Scene24 — The Fissure Returns | `[TARGET: 12s]` | VO ~23w, ~9.5s

**VO:** *"The fissure opens. Eight months of lava and sulphur. Eighty percent of the sheep, gone. A quarter of the people, gone."*

---

**T+0:00**
- All Scene23 elements continue. Crack still glowing.
- VISUAL: The ledger page from Scene05 materialises as a semi-transparent overlay over the crack (opacity=0.45), `FadeIn` run_time=1.0s
- The five prior green ticks are visible through the overlay

**T+0:02** | VO: *"Eighty percent of the sheep, gone."*
- NEW LEDGER LINE appears at the bottom of the overlay: `"Eighty percent of sheep"` ... `"[GONE]"` — VOLCANIC_RED text, `FadeIn`
- SFX: `sfx_tick.mp3` -6dB (heavier than previous ticks — this is a GONE not a check)

**T+0:05** | VO: *"A quarter of the people, gone."*
- NEW LEDGER LINE: `"A quarter of the people"` ... `"[GONE]"` — VOLCANIC_RED text, `FadeIn`
- SFX: `sfx_collapse.mp3` -8dB (heavier — people dying, not livestock)

**T+0:08** | Ledger overlay holds. Crack glows beneath it. Two GONE lines visible.

**T+0:10** | Ledger overlay `FadeOut`. Just the crack remains.

**T+0:12** | Scene end. Crack continues into Scene25.

**MANIM NOTE:** The ledger overlay laid OVER the glowing crack creates a layered visual — all the prior disasters (seen in Scene05) plus the current two new losses. The opacity of the overlay (0.45) means the crack glow shows through it. This layering is the point: nothing happened in isolation, everything accumulated.
**SOUND NOTE:** sfx_tick for sheep line (-6dB). sfx_collapse for people line (-8dB). Cello drone continues throughout.

---

### Scene25 — The French Revolution Link | `[TARGET: 26s]` | VO ~65w, ~26.9s

**VO:** *"The haze drifts south and fails the harvests of France. Historians have argued, carefully and with caveats, that Laki's agricultural disruption contributed to the conditions that produced the French Revolution six years later. Iceland did not plan this. Iceland was simply having a routine geological episode and accidentally destabilising Western Europe. It is, in some ways, the most Icelandic thing Iceland has ever done."*

---

**T+0:00**
- BG: `WHITE_BG`, transition from DARK_BG run_time=0.5s
- MAP: `north_atlantic.png` at `CTR`, `FadeIn` run_time=0.5s
- AUDIO: Music returns at -12dB. Cello drone fades out. String texture resumes.

**T+0:02** | VO: *"The haze drifts south and fails the harvests of France."*
- VISUAL: Yellow-green haze `Rectangle` (from Scene02/03 visual language) appears over Iceland on the map, opacity=0.6, then `animate.shift(RIGHT*3 + DOWN*2)` over 5s (drifting south toward France)

**T+0:07** | Haze reaches France.
- LABEL: `"France — harvest failures"` at France position on map, STONE_GREY font="Poppins" font_size=18, `FadeIn`
- LABEL: `"6 years before the French Revolution"` at France position below previous, AMBER font="Poppins" font_size=16, `FadeIn` 0.5s after

**T+0:10** | VO: *"Historians have argued, carefully and with caveats, that Laki's disruption contributed..."*
- VISUAL: Cause-and-effect chain builds RIGHT of map at [5.5, 1.5, 0], building downward:
  ```
  Iceland
      |
  volcanic eruption
      |
  European harvest failure
      |
  French bread prices spike
      |
  French Revolution
      |
  Napoleon
      |
  most of modern Europe
  ```
  Each line + arrow appears every 1.2s, cascading downward. font="Poppins" font_size=14, STONE_GREY.
- SFX: `sfx_tick.mp3` -14dB for each new line in chain

**T+0:22** | Chain complete. Last line: `"most of modern Europe"` visible.
- ASTERISK: `"* Iceland did not plan this."` at [5.5, -2.8, 0], STONE_GREY ITALIC font="Poppins" font_size=12, `FadeIn`

**T+0:23** | VO: *"The most Icelandic thing Iceland has ever done."*
- TEXT: `"The most Icelandic thing Iceland has ever done."` at `BC` = [0, -3.0, 0], AMBER ITALIC font="Poppins" font_size=26, `FadeIn`

**T+0:25** | Hold.

**T+0:26** | Scene end. `FadeOut` all. Keep map visible into Scene26.

**MANIM NOTE:** The cause-and-effect chain appears on the RIGHT side of the map — it's a sidebar infographic. Each link is simple: a short line of text + a `|` connector. The chain keeps going FURTHER than the viewer expects (from volcanic eruption all the way to "most of modern Europe") — that is the joke. The asterisk footnote at the bottom is tiny and appears last, almost as a whisper.
**SOUND NOTE:** sfx_tick for each chain link (-14dB, quiet). No other SFX. Music at -12dB.

---

### Scene26 — Monopoly Blocks Relief | `[TARGET: 15s]` | VO ~38w, ~15.7s

**VO:** *"The trade monopoly was still in place. Relief supplies could not be freely imported. The island was starving and the mechanism designed to help was the same mechanism that had been bleeding it dry for eighty years."*

---

**T+0:00**
- MAP: `iceland_overview.png` at `CTR`, `FadeIn` run_time=0.5s
- VISUAL: Merchant district grid from Scene16 reappears over map — `FadeIn` at opacity=0.5. Merchants still in their districts, arms crossed.
- AUDIO: Music at -12dB, harpsichord texture returns briefly

**T+0:02** | VO: *"Relief supplies could not be freely imported."*
- VISUAL: Three supply ships appear approaching Iceland from different directions (LEFT, RIGHT, BOTTOM of map), each labeled `"RELIEF"` — `FadeIn` then `animate.shift` toward Iceland coast, run_time=2s

**T+0:05** | Ships reach the merchant district grid borders and STOP.
- VISUAL: A `"NO ENTRY"` symbol (Circle with diagonal Line, `VOLCANIC_RED`) appears over each ship's path at the grid border, `GrowFromCenter` staggered 0.3s
- SFX: `sfx_stamp.mp3` -6dB x3 (one per blocked ship, rapid)
- Ships animate slightly backward (small recoil `animate.shift(LEFT*0.3)` etc.)

**T+0:10** | VO: *"The mechanism designed to help was the same mechanism bleeding it dry."*
- VISUAL: Inside the grid, one merchant figure (arms still crossed) visible. Does not move. Does not help.
- TEXT: `"The mechanism designed to help"` at `TC` = [0, 3.0, 0], WHITE ITALIC font="Poppins" font_size=22, `FadeIn`
- TEXT: `"was the mechanism bleeding it dry."` at [0, 2.4, 0], AMBER BOLD font="Poppins" font_size=24, `FadeIn` 0.5s after

**T+0:13** | Hold. Blocked ships + merchant grid + verdict text.

**T+0:15** | Scene end. `FadeOut` all.

**MANIM NOTE:** Three supply ships blocked at the grid border is the visual. Three `NO ENTRY` stamps appear in rapid succession (staggered 0.3s). The merchant standing inside the grid, unmoved and arms-crossed, is the moral — he is not evil, he is following procedure. That is what makes the system indictable.
**SOUND NOTE:** Three sfx_stamp hits (-6dB, rapid). No other SFX. Music at -12dB.

---

### Scene27 — Althing Abolished | `[TARGET: 19s]` | VO ~50w, ~20.7s

**VO:** *"By 1800, the Althing itself was gone. Abolished by royal decree. A High Court in Reykjavik took its place. Iceland was no longer a nation in any practical sense. A remote administrative district, periodically devastated by geology, locked into a system designed to extract what little it could produce."*

---

**T+0:00**
- BG: `WHITE_BG`
- VISUAL: Vertical `Line` divider appears at `CTR`, `Create` run_time=0.3s. Both halves of the comparison build SIMULTANEOUSLY — viewer reads during the 3s before VO begins:
  - LEFT header: `"THE ALTHING (930–1800)"` at [-3.5, 3.0, 0], `SAGE_GREEN` BOLD font="Poppins" font_size=20, `FadeIn` run_time=0.4s
  - RIGHT header: `"A HIGH COURT (1800)"` at [3.5, 3.0, 0], DANISH_NAVY BOLD font="Poppins" font_size=20, `FadeIn` run_time=0.4s — both headers appear together
  - LEFT four lines `FadeIn` as a single `VGroup` (all four at once) run_time=0.5s:
    `"World's oldest parliament"` / `"Annual democratic assembly"` / `"Held in the open air"` / `"The people govern themselves"` — STONE_GREY font="Poppins" font_size=18, LEFT-aligned at [-5.5, 2.2, 0], spacing 0.55u
  - RIGHT four lines `FadeIn` as a single `VGroup` simultaneously with LEFT lines:
    `"Run by Denmark"` / `"In Reykjavik"` / `"Not elected"` / `"Handles disputes only"` — STONE_GREY font="Poppins" font_size=18, LEFT-aligned at [1.5, 2.2, 0], spacing 0.55u
- AUDIO: Music at -12dB
- NOTE: Both sides fully readable before VO begins. This is the SETUP move — viewer sees what was lost before the VO declares it gone.

**T+0:03** | VO: *"By 1800, the Althing itself was gone. Abolished by royal decree."*
- STAMP: `"ABOLISHED"` VOLCANIC_RED BOLD font="Poppins" font_size=64 slams down over the LEFT half at *"Abolished"*, `GrowFromCenter` run_time=0.4s with `Rotate(-3*DEGREES)`
- SFX: `sfx_stamp.mp3` -4dB simultaneously with stamp (loudest stamp in the episode)
- LEFT half dims at the same moment: DARK_BG Rectangle overlay opacity=0.5 over left half, `FadeIn` run_time=0.3s
- Stamp + dim happen as one simultaneous beat — `AnimationGroup`

**T+0:07** | VO: *"Iceland was no longer a nation in any practical sense."*
- TEXT: `"Iceland: a remote administrative district."` at `BC` = [0, -3.0, 0], WHITE LIGHT font="Poppins" font_size=22, `FadeIn`

**T+0:12** | Hold. Split frame: dimmed left with ABOLISHED stamp + right column + verdict text.

**T+0:19** | Scene end. `FadeOut` all. Hard cut.

**MANIM NOTE:** Three VO-anchored beats: (1) Both comparison columns appear simultaneously at T+0:00 — BEFORE VO starts, so the viewer reads the contrast first, then hears it confirmed. This order matters: see what was lost, then hear it called gone. (2) ABOLISHED stamp fires on *"Abolished by royal decree"* — stamp + dim are one `AnimationGroup`. (3) Verdict text on *"no longer a nation."* The staggered-line approach was removed because 8 lines building over 8 seconds while VO announces abolition creates a mismatch — viewer is still reading "Annual democratic assembly" while hearing "Abolished."
**SOUND NOTE:** sfx_stamp at T+0:03 at -4dB (loudest stamp). No other SFX. Music at -12dB, drops to -15dB after stamp.

---

## ACT FIVE — THE DOG-DAYS KING

---

### Scene28 — Jorgensen Arrives | `[TARGET: 28s]` | VO ~65w, ~26.9s

**VO:** *"Then June 1809. A Danish-born adventurer named Jorgen Jorgensen arrived in Reykjavik. He found the Danish governor Count Trampe blocking all trade per monopoly rules and responded by arresting him. He declared Iceland independent from Denmark, proclaimed himself Protector of Iceland, Commander in Chief by Land and Sea, and issued proclamations in English. He seemed genuinely enthusiastic about the whole project."*

---

**T+0:00**
- BG: `WHITE_BG`
- AUDIO: Music shifts — lighter pizzicato strings, slightly wry. -12dB. Not comedic stings — just lighter in tone.

**T+0:02** | VO: *"A Danish-born adventurer named Jorgen Jorgensen arrived in Reykjavik."*
- CHARACTER: `jorgensen_confident.png` enters from BOTTOM: `animate.shift(UP*8)` starting at [0, -8, 0], arrives at `CTR` = [0, 0.3, 0], height=3.5u, run_time=1.0s
- SFX: `sfx_whoosh.mp3` -10dB
- LABEL: `"Jorgen Jorgensen"` at [0, -2.2, 0], WHITE BOLD font="Poppins" font_size=30, `FadeIn`
- LABEL: `"Status: absolutely not supposed to be here"` at [0, -2.9, 0], RED ITALIC font="Poppins" font_size=18, `FadeIn` 0.5s after

**T+0:06** | VO: *"He found the Danish governor Count Trampe blocking all trade..."*
- CHARACTER: `count_trampe.png` enters from RIGHT: `animate.shift(LEFT*3)` from [7, 0, 0], settles at `R3` = [3.0, 0.3, 0], height=2.5u (slightly smaller than Jorgensen), run_time=0.8s
- SFX: `sfx_whoosh.mp3` -12dB
- LABEL: `"Count Trampe"` at [3.0, -1.8, 0], STONE_GREY BOLD font="Poppins" font_size=20, `FadeIn`
- LABEL: `"Danish Governor"` at [3.0, -2.3, 0], STONE_GREY LIGHT font="Poppins" font_size=16, `FadeIn`
- Trampe holds his rulebook open, facing Jorgensen

**T+0:10** | VO: *"...and responded by arresting him."*
- ANIMATE: `count_trampe.png` scales to 0.3x and is "picked up" — `animate.shift(LEFT*1.5 + UP*0.5)` run_time=0.8s — moves toward Jorgensen and past him to `L3` = [-3.0, 0, 0]
- A simple jail cell appears at `L3` area: four vertical `Line` objects as bars (STONE_GREY, height=1.5u, spaced 0.3u apart), `GrowFromBase` run_time=0.5s
- `count_trampe_jail.png` appears inside the bars (replaces the scale-down Trampe)
- LABEL over jail: `"ARRESTED"` at [-3.0, 1.5, 0], RED BOLD font="Poppins" font_size=24, `GrowFromCenter`
- SFX: `sfx_stamp.mp3` -6dB

**T+0:14** | VO: *"He declared Iceland independent from Denmark..."*
- Three proclamation scrolls enter from LEFT, moving RIGHT across the frame:
  - SCROLL 1: `Rectangle` (cream fill, STONE_GREY border, width=3.5u, height=2.0u), appears at `L5`, `animate.shift(RIGHT*12)` run_time=3s
  - Text inside: `"ICELAND: INDEPENDENT"` BOLD font="Poppins" font_size=14
  - Language tag at bottom: `"Issued in: ENGLISH"` STONE_GREY ITALIC font="Poppins" font_size=11
  
  - SCROLL 2: Appears 1s after SCROLL 1, same motion, text: `"I, JORGENSEN: PROTECTOR"`
  
  - SCROLL 3: Appears 1s after SCROLL 2, text: `"COMMANDER IN CHIEF"`

**T+0:20** | VO: *"...and issued proclamations in English."*
- A small Icelandic figure (Circle head r=0.15 + Rectangle body 0.15x0.3, COLD_WHITE) at [0, -2.8, 0] `GrowFromCenter` run_time=0.3s
- A scroll object (tiny Rectangle 0.4x0.25, cream fill) falls into figure's hands at T+0:20: `FadeIn`
- Figure "reads" — head circle `Rotate(20*DEGREES)` run_time=0.3s (tilts to look at it), then `Rotate(-20*DEGREES)` run_time=0.3s (tilts other way)
- Figure shrugs — head circle `animate.shift(UP*0.1)` run_time=0.2s then `animate.shift(DOWN*0.1)` run_time=0.2s
- LABEL: `"(reads: English)"` at [0, -3.1, 0], STONE_GREY ITALIC font="Poppins" font_size=13, `FadeIn` 0.5s after shrug — font_size=13 keeps within safe zone at Y=-3.1

**T+0:24** | VO: *"He seemed genuinely enthusiastic about the whole project."*
- TEXT: `"Genuinely enthusiastic."` at `TC` = [0, 3.0, 0], AMBER ITALIC font="Poppins" font_size=30, `FadeIn`
- `jorgensen_confident.png` at CTR still visible, still has the rolled proclamation raised

**T+0:26** | Hold.

**T+0:28** | Scene end. Count Trampe in jail stays in frame until Scene30. `jorgensen_confident.png` at CTR holds.

**MANIM NOTE:** Four VO-anchored beats — no floating visuals: (1) *"Jorgensen arrived"* → Jorgensen enters; (2) *"found Trampe...responded by arresting him"* → Trampe enters then immediately arrested (both within one VO sentence — enter at start of sentence, jail cell appears at *"arresting"*); (3) *"issued proclamations in English"* → scrolls float past + Icelander shrug (concurrent); (4) *"genuinely enthusiastic"* → enthusiasm text. Trampe entering and being arrested are cause-effect within one sentence — run them rapid-sequence (0.8s entry, 0.8s arrest) not as separate scene beats. Scrolls float continuously — they do not stop — implying the proclamations just keep coming.
**SOUND NOTE:** sfx_whoosh for Jorgensen entry (-10dB). sfx_whoosh for Trampe entry (-12dB). sfx_stamp when Trampe is jailed (-6dB). Music at -12dB, lighter pizzicato tone throughout this act.

---

### Scene29 — Sixty-Two Days | `[TARGET: 12s]` | VO ~6w, ~2.5s

**VO:** *"His reign lasted sixty-two days."*

---

**T+0:00**
- BG: `WHITE_BG`
- `jorgensen_confident.png` from Scene28 at `CTR` dims to opacity=0.3 (fades to background)
- MAP: none
- AUDIO: Music drops to -18dB (near silence)

**T+0:01** | VISUAL: Large horizontal timeline bar appears at `CTR`:
- `Rectangle` bar: width=11u (full safe width), height=0.3u, STONE_GREY, at [0, 0.5, 0]
- LEFT label: `"Jorgen Jorgensen's reign"` at [-5.5, 1.2, 0], STONE_GREY font="Poppins" font_size=18

**T+0:02** | Three comparison bars appear stacked vertically (ABOVE the Jorgensen bar), filling from left:

- BAR A (top): STONE_GREY, full frame width, fills in over 0.5s. Label: `"British Monarchy: ~1,000 years"` at right end
- BAR B (middle): STONE_GREY, full frame width, fills in 0.5s. Label: `"Roman Empire: ~500 years"`
- BAR C (bottom, Jorgensen): The timeline bar FILLS only a tiny VOLCANIC_RED sliver — approximately 0.06u of the 11u bar, starting from the left: `animate.set_fill(VOLCANIC_RED)` on a tiny inner Rectangle, `GrowFromBase`

- LABEL over the tiny sliver: `"62 DAYS"` RED BOLD font="Poppins" font_size=24, `GrowFromCenter` pointing down to the sliver

**T+0:05** | VO: *"His reign lasted sixty-two days."*
- SFX: `sfx_clock.mp3` -10dB (a quick tick-down, 3 ticks only)

**T+0:07** | Hold. Three comparison bars visible. The proportions ARE the joke. No other elements.

**T+0:11** | `jorgensen_confident.png` (still dimmed at 0.3) — changes to `jorgensen_deflated.png` (swap, `FadeOut` then `FadeIn` 0.3s)

**T+0:12** | Scene end. `jorgensen_deflated.png` at `CTR` (dimmed) holds into Scene30.

**MANIM NOTE:** Three bars are the visual. The proportion speaks for itself: two bars spanning full frame, one bar that is barely a line. Font_size for comparison labels should be 16-18, readable. The `"62 DAYS"` label above the tiny sliver should be large enough to be ironic (font="Poppins" font_size=24). Avatar swap at T+0:11 (confident → deflated) is silent and quick — the transition to Scene30.
**SOUND NOTE:** sfx_clock at T+0:05 (-10dB, 3 ticks only — not a full clock sound). Music at -18dB. Very quiet.

---

### Scene30 — HMS Talbot | `[TARGET: 30s]` | VO ~95w, ~39.3s

**VO:** *"In August, HMS Talbot sailed into Reykjavik harbour. Its captain noted Jorgensen was in violation of his parole from a prior arrest in Britain. He was taken aboard, transported to London, and eventually transported again as a convict to Tasmania. Icelanders remember him as Jorundur hundadagakonungur. Jorgen the Dog-Days King. Collected by a passing warship, gone before autumn. The whole affair has the quality of elaborate farce. But underneath it, something real: even in 1809, an outsider could see Iceland deserved to govern itself. He was just not quite the right outsider."*
*(VO compresses to 30s — increase delivery pace for this section)*

---

**T+0:00**
- BG: `WHITE_BG`
- `jorgensen_deflated.png` at `CTR` still at opacity=0.3 from Scene29
- AUDIO: Music returns slightly at -12dB

**T+0:01** | VO: *"In August, HMS Talbot sailed into Reykjavik harbour."*
- VISUAL: HMS Talbot ship silhouette enters from RIGHT at [9, -0.5, 0]: organic hull (same curved VMobject method as Scene18 mystery ship but larger — scale to 1.4u height, full opacity=1.0):
  - Hull: `[(-1.2,-0.3,0),(-0.9,-0.55,0),(0,-0.6,0),(0.9,-0.55,0),(1.2,-0.3,0),(1.0,0,0),(-1.0,0,0)]` closed, fill=DANISH_NAVY
  - Mast: `Line([0,0,0],[0,1.1,0])`, stroke_width=2, STONE_GREY
  - Crossbeam: `Line([-0.5,0.7,0],[0.5,0.7,0])`, stroke_width=1.5, STONE_GREY
  - Small Union Jack: `Rectangle(width=0.4, height=0.25)` at [0.5, 0.9, 0], fill with red+blue cross Lines inside (VOLCANIC_RED + DANISH_NAVY)
  - `animate.shift(LEFT*6)` run_time=2s, settles at `R3` = [3.0, -0.5, 0]
- SFX: `sfx_whoosh.mp3` -8dB
- LABEL above ship: `"HMS TALBOT"` STONE_GREY BOLD font="Poppins" font_size=18, `FadeIn`
- LABEL: `"August 1809"` at [3.0, -1.5, 0], STONE_GREY font="Poppins" font_size=14, `FadeIn`

**T+0:04** | VO: *"Its captain noted Jorgensen was in violation of his parole..."*
- VISUAL: A Naval officer figure (Circle head + dark blue Rectangle body with epaulette indicator, scale=0.6) steps off ship at R3: `animate.shift(LEFT*1.5)` run_time=0.8s
- Officer holds a small paper (Rectangle with lines) — `FadeIn`
- Officer consults paper: head tilts slightly (small `Rotate` on head circle), then head tilts back up, looking toward Jorgensen at CTR

**T+0:08** | VO: *"He was taken aboard..."*
- ANIMATE: Officer extends arm toward Jorgensen — build as two-segment composite (NOT a straight Line):
  - Upper arm: `Line([3.2, 0.3, 0],[2.4, 0.1, 0])` stroke_width=3, DANISH_NAVY (angled downward from shoulder)
  - Forearm: `Line([2.4, 0.1, 0],[1.6, 0.2, 0])` stroke_width=3, DANISH_NAVY (slight angle back up — elbow bend)
  - Both appear simultaneously via `Create` run_time=0.4s
  - Small `Circle(r=0.06, fill=DARK_BG)` at fingertip [1.6, 0.2, 0] for pointing gesture
- SFX: `sfx_bell.mp3` -12dB (the simple, bureaucratic finality of a single note)
- `jorgensen_deflated.png` opacity rises to 1.0 (fully visible for this beat — the spotlight is on him now)

**T+0:11** | VO: *"...transported to London, and eventually transported again as a convict to Tasmania."*
- VISUAL: Map appears as background at reduced opacity (0.4): simplified world map showing Iceland → London → Tasmania
- Dotted arrow traces: Iceland → London → Tasmania, `Create` run_time=3s in STONE_GREY
- Labels at each destination: `"London"`, `"Tasmania"` STONE_GREY font="Poppins" font_size=16
- `jorgensen_deflated.png` moves along the path at small scale (0.25) — `MoveAlongPath`, run_time=3s
- SFX: `sfx_whoosh.mp3` -10dB

**T+0:16** | Map and travel path fade. Title card builds:
- `"JORUNDUR HUNDADAGAKONUNGUR"` at [0, 2.0, 0], WHITE BOLD font="Poppins" font_size=34, `Write` run_time=0.8s
- `"Jorgen the Dog-Days King."` at [0, 1.3, 0], WHITE LIGHT font="Poppins" font_size=26, `FadeIn`
- `"Collected by a passing warship."` at [0, 0.6, 0], STONE_GREY font="Poppins" font_size=22, `FadeIn` 1s after
- `"Gone before autumn."` at [0, -0.1, 0], STONE_GREY font="Poppins" font_size=22, `FadeIn` 1s after

**T+0:22** | VO: *"But underneath it, something real: even in 1809, an outsider could see Iceland deserved to govern itself."*
- TEXT: `"Even in 1809 — an outsider could see it."` at [0, -1.5, 0], WHITE ITALIC font="Poppins" font_size=24, `FadeIn`
- TEXT: `"Iceland deserved to govern itself."` at [0, -2.2, 0], AMBER BOLD font="Poppins" font_size=26, `FadeIn` 1s after

**T+0:27** | VO: *"He was just not quite the right outsider."*
- TEXT: `"He was just not quite the right outsider."` at [0, -3.0, 0], STONE_GREY ITALIC font="Poppins" font_size=22, `FadeIn`

**T+0:29** | Hold.

**T+0:30** | Scene end:
- Naval officer arm Lines `FadeOut` run_time=0.3s
- Officer figure `animate.shift(RIGHT*6)` + `FadeOut` run_time=0.8s (returns to ship, exits RIGHT)
- HMS Talbot silhouette `animate.shift(RIGHT*8)` run_time=1.0s (ship departs)
- All remaining text elements `FadeOut` run_time=0.5s
- Transition to Close.

**MANIM NOTE:** Six beats across 30s, every one VO-anchored — this scene is correctly structured and does NOT need trimming: (1) T+0:01 *"HMS Talbot sailed in"* → ship + officer; (2) T+0:04 *"captain noted Jorgensen in violation"* → officer reads paper; (3) T+0:08 *"He was taken aboard"* → officer points; (4) T+0:11 *"transported to London...Tasmania"* → travel path; (5) T+0:16 *"Icelanders remember him...Dog-Days King"* → title card; (6) T+0:22 *"something real...deserved to govern itself"* → verdict lines. At 95 words / ~30s, the beat density is ~5s per visual beat — comfortable pacing. The pointing arm (T+0:08) is the visual joke. The title card (T+0:16) is the payoff. The two sincere verdict lines are the emotional turn.
**SOUND NOTE:** sfx_whoosh for ship arrival (-8dB). sfx_bell when officer points (-12dB, very quiet — almost delicate). sfx_whoosh for travel path (-10dB). Music at -12dB, returning to warmer string texture for the close section.

---

## CLOSE

---

### Scene31 — The Final Ledger | `[TARGET: 28s]` | VO ~65w, ~26.9s

**VO:** *"Plague, twice. Piracy from a direction that makes no geographical sense. A Reformation enforced by beheading. A monopoly designed to keep the island poor. A volcanic catastrophe that killed a quarter of the population and accidentally destabilised France. The parliament abolished. A sixty-two-day king collected by the Navy. Six centuries of foreign rule. Six centuries of endurance."*

---

**T+0:00**
- BG: `WHITE_BG`
- VISUAL: The ledger page from Scenes 05 and 24 returns — full page, all prior items visible with their green ticks. `FadeIn` run_time=0.8s.
- AUDIO: Music at -12dB, fuller string texture — building slightly

**T+0:02** | New items appear at the bottom of the ledger, one per VO beat (staggered 2.5s each):

**T+0:02** | VO: *"Plague, twice."*
- `"Plague, twice ................................................ [✓]"` — STONE_GREY, `FadeIn` + `sfx_tick.mp3` -8dB

**T+0:04** | VO: *"Piracy from a direction that makes no geographical sense."*
- `"Piracy (wrong direction entirely) ......... [✓]"` — `FadeIn` + `sfx_tick.mp3`

**T+0:07** | VO: *"A Reformation enforced by beheading."*
- `"Reformation, enforced by beheading ..... [✓]"` — `FadeIn` + `sfx_tick.mp3`

**T+0:09** | VO: *"A monopoly designed to keep the island poor."*
- `"Monopoly (185 years) ............................ [✓]"` — `FadeIn` + `sfx_tick.mp3`

**T+0:12** | VO: *"A volcanic catastrophe..."*
- `"Volcanic catastrophe .............................. [✓]"` — VOLCANIC_RED, `FadeIn` + `sfx_stamp.mp3` -6dB

**T+0:15** | VO: *"The parliament abolished."*
- `"Parliament: abolished .............................. [✓]"` — DANISH_NAVY, `FadeIn` + `sfx_stamp.mp3` -6dB

**T+0:17** | VO: *"A sixty-two-day king collected by the Navy."*
- `"62-day king (collected by Royal Navy) .. [✓]"` — STONE_GREY ITALIC, `FadeIn` + `sfx_tick.mp3`

**T+0:20** | Ledger fills with all items. A ruled final line appears below all entries.

**T+0:21** | VO: *"Six centuries of foreign rule."*
- TEXT: `"Six centuries of foreign rule."` at [0, -2.5, 0], STONE_GREY BOLD font="Poppins" font_size=30, `GrowFromCenter`

**T+0:23** | VO: *"Six centuries of endurance."*
- TEXT: `"Six centuries of endurance."` at [0, -3.1, 0], AMBER BOLD font="Poppins" font_size=30, `GrowFromCenter`
- NOTE: Y=-3.1 is the safe zone floor at this font size. Do not move lower.
- SFX: `sfx_bell.mp3` -6dB

**T+0:25** | Hold. Full ledger + two contrasting final lines. STONE_GREY vs AMBER.

**T+0:28** | Scene end. Ledger `FadeOut`. Two bottom lines hold slightly longer before fading.

**MANIM NOTE:** The two final lines — `"foreign rule"` in STONE_GREY and `"endurance"` in AMBER — are the emotional axis of the entire episode. They must appear at the same font size, same weight, but opposite colors. They are equals in historical weight. The color contrast (grey vs gold) makes one feel like burden and the other like dignity. The ledger above them is context; these two lines are the conclusion.
**SOUND NOTE:** sfx_tick x5 for regular items. sfx_stamp x2 for volcanic catastrophe and parliament (heavier). sfx_bell at "Six centuries of endurance." Music builds from -12dB to -9dB during the two final lines.

---

### Scene32 — Lights across Iceland | `[TARGET: 28s]` | VO ~70w, ~29s

**VO:** *"Go back to Laki. 1783. Forty thousand people, decimated, isolated, locked into a system designed to bleed them dry. No rescue. No cavalry. What there was: people who stayed, who rebuilt, who remembered the sagas, who kept speaking a language barely changed in a thousand years, who held onto the memory of what Iceland had once been. Self-governing. Beholden to no king."*

---

**T+0:00**
- BG: `DARK_BG` — transition from Scene31's `WHITE_BG`, hard cut
- MAP: `iceland_overview.png` at `CTR`, full opacity, `FadeIn` run_time=0.5s. Dark map on dark background. The Laki fissure crack glows faintly (VOLCANIC_RED line at low intensity) at south coast — same Line from Scenes01/23.
- CHARACTER: none
- AUDIO: Music drops to -18dB. Cello drone returns from nothing. Very quiet.

**T+0:02** | VO: *"Forty thousand people, decimated, isolated..."*
- VISUAL: The map is nearly dark. No labels visible. Empty. Quiet.

**T+0:06** | VO: *"...people who stayed, who rebuilt..."*
- First amber dot appears: `Circle(r=0.07, fill_color=AMBER, fill_opacity=1.0)` at a northern coast position on the map. `GrowFromCenter` run_time=0.4s.
- SFX: `sfx_tick.mp3` -15dB (very quiet, gentle)

**T+0:08** | Second amber dot at a different position.
- SFX: `sfx_tick.mp3` -15dB

**T+0:10** | VO: *"...who remembered the sagas..."*
- Third, fourth dots appear. Each 1.5s apart, irregular positions across the island.
- SFX: `sfx_tick.mp3` -15dB per dot

**T+0:13** | Fifth, sixth dots.

**T+0:16** | VO: *"...who kept speaking a language barely changed in a thousand years..."*
- Seventh, eighth, ninth, tenth dots. Each 1.2s apart. By now 10 dots visible.
- Cello deepens slightly

**T+0:20** | VO: *"...who held onto the memory of what Iceland had once been."*
- Three more dots — 13 total by T+0:23.
- Dots are irregular — no grid pattern. Some near coast, some inland.

**T+0:23** | All 13+ dots visible. They do not go out. They hold.

**T+0:24** | VO: *"Self-governing."*
- TEXT: `"Self-governing."` at `L3` = [-3.0, -2.5, 0], WHITE BOLD font="Poppins" font_size=30, `FadeIn`

**T+0:26** | VO: *"Beholden to no king."*
- TEXT: `"Beholden to no king."` at `R3` = [3.0, -2.5, 0], WHITE BOLD font="Poppins" font_size=30, `FadeIn`

**T+0:28** | Hold. Dark map. Amber dots. Two phrases.

**T+0:28** | Scene end. Map and dots hold into Scene33.

**MANIM NOTE:** EACH amber dot appears individually — use a loop with `play(GrowFromCenter(dot), run_time=0.4)` and `wait(1.2)` between iterations. Do NOT create all dots simultaneously. The gradual appearance — one by one, irregular positions, over 20+ seconds — IS the meaning. They represent people and communities that survived and persisted. The dots do not go out. They are still there when the episode ends.
**SOUND NOTE:** sfx_tick at -15dB for each dot appearance (very quiet, almost subliminal). Cello drone at -18dB deepening toward -14dB by end of scene. No other SFX. Let the quietness of the dot sounds contrast with all prior SFX.

---

### Scene33 — Those People | `[TARGET: 10s]` | VO ~18w, ~7.4s

**VO:** *"Those people's grandchildren's grandchildren looked at six centuries of this and decided enough was enough."*

---

**T+0:00**
- MAP and amber dots from Scene32 all continue. No transition.
- AUDIO: Music rises slightly to -12dB. A thread of resolution.

**T+0:01** | ONE amber dot — select one in the center-ish of the island — pulses:
- `Circle` scales 1.0 → 1.5 → 1.0, opacity fades from 1.0 to 0.0 at peak (like a ripple)
- run_time=1.5s
- SFX: `sfx_bell.mp3` -12dB (single quiet note — not dramatic, just present)

**T+0:04** | VO: *"Those people's grandchildren's grandchildren..."*
- TEXT: `"Those people's grandchildren's grandchildren"` at [0, 2.0, 0], WHITE BOLD font="Poppins" font_size=26, `FadeIn`

**T+0:06** | VO: *"...decided enough was enough."*
- TEXT: `"decided enough was enough."` at [0, 1.3, 0], AMBER BOLD font="Poppins" font_size=32, `FadeIn`

**T+0:08** | Hold. All dots. Both lines. One faded pulse ring visible.

**T+0:10** | Scene end. Gentle `FadeOut` of text. Dots continue to Scene34.

**MANIM NOTE:** ONE dot pulses. One. Not all of them. The specificity of a single dot pulsing feels like choosing one family, one person, one line of descent. The scale-up + fade (like a ripple) is a 1.5s animation. After it's gone, the dot is still there (opacity returns to 1.0 — the circle body doesn't disappear, only the expanding ring fades). The pulse is a ring that expands and fades, not the dot itself disappearing.
**SOUND NOTE:** sfx_bell at T+0:01 (-12dB, single note, quiet). Music resolving toward major at -12dB. One note at the right moment.

---

### Scene34 — Episode Card | `[TARGET: 15s]` | VO ~4w, ~1.7s

**VO:** *"That is Episode 3."*

---

**T+0:00**
- ANIMATE: `DARK_BG` with amber dots → `WHITE_BG` crossfade, run_time=1.5s. Dots fade as BG brightens.
- AUDIO: Music resolves to a warm chord at -10dB. Unresolved — open fifth, not full major. The story is not finished.

**T+0:01** | VO: *"That is Episode 3."*
- TEXT: `"That is Episode 3."` delivered with VO. No visual sync needed here — the episode card is building.

**T+0:02** | Clean white card builds. All elements centered. Safe zone respected:

- TEXT: `"ICELAND: THE VOLCANOES AND THE PIRATES"` at [0, 2.0, 0], STONE_GREY SEMIBOLD font="Poppins" font_size=28, `FadeIn`
- TEXT: `"Episode 2 of 3"` at [0, 1.3, 0], AMBER font="Poppins" font_size=22, `FadeIn` 0.5s after
- `Line` divider: from [-4.0, 0.9, 0] to [4.0, 0.9, 0], STONE_GREY stroke_width=0.5, `Create`

- TEXT: `"Episode 3: 'The Republic'"` at [0, 0.4, 0], DANISH_NAVY BOLD font="Poppins" font_size=28, `FadeIn` 1s after divider
- TEXT: `"How Iceland Got Its Country Back"` at [0, -0.3, 0], STONE_GREY LIGHT font="Poppins" font_size=20, `FadeIn` 0.5s after

- `Line` divider at [0, -0.7, 0] same style, `Create`

- PROGRESS BAR: Three `Rectangle` segments at [0, -1.2, 0] centered, width=9u total:
  - Ep1 segment: width=3u, STONE_GREY fill — already done
  - Ep2 segment: width=3u, AMBER fill — current episode
  - Ep3 segment: width=3u, outline only (STONE_GREY stroke, no fill) — upcoming; a faint pulse animation (opacity 0.3 to 0.7 cycle, run_time=2s loop)

- SMALL: Iceland outline icon (simplified coastline SVG at 0.4u height) + `"Subscribe"` text + bell icon: at [0, -2.5, 0], STONE_GREY font="Poppins" font_size=14

**T+0:06** | All episode card elements visible.

**T+0:07** | Hold. 8 seconds.

**T+0:15** | Scene end. Gentle `FadeOut` all elements.

**MANIM NOTE:** Clean white card. No animations after T+0:06 except the Ep3 segment pulse. The open/unresolved musical chord is the final audio instruction — do not resolve it to a full major chord. An open fifth or a suspension. The episode is complete, not finished.
**SOUND NOTE:** Music resolves to open chord at -10dB at T+0:00. Chord sustains through the card. Fades to silence at T+0:14. No SFX on the episode card.

---

---

## SUMMARY TABLE

| # | Scene | VO (w) | Target | Map | Character(s) | Key Move | Key SFX |
|---|---|---|---|---|---|---|---|
| 01 | Ground Zero | 35 | 25s | none | none | Crack Line + glow + title | sfx_crack, sfx_bell |
| 02 | Haze Famine | 95 | 37s | iceland_overview | none | SO₂ cloud + tally + bar chart | sfx_tick x3, sfx_bell |
| 03 | Europe Poisoned | 38 | 18s | north_atlantic | none | Cloud drifts east + thermometer | sfx_bell x2 |
| 04 | One in Four | 47 | 20s | iceland_overview | none | Counter drops, stops, "1 in 4" | sfx_tick, sfx_collapse |
| 05 | The Ledger | 40 | 20s | none | none | 6-row ledger builds + "And now this" | sfx_tick x5, sfx_stamp, sfx_bell |
| 06 | The Rewind | 28 | 15s | none | none | Year spins to 1262 + 3-line reveal | sfx_clock, sfx_collapse, sfx_bell |
| 07 | The Commonwealth | 70 | 25s | Thingvellir (built) | hakon_iv (enters R, T+0:18) | BG green-to-grey + cracks + Hakon | sfx_crack, sfx_whoosh |
| 08 | Snorri's Cellar | 38 | 22s | none | snorri_writing (CTR) → snorri_afraid (CTR, T+0:12) | "Eigi skal hoggva" + 2s black + "They struck." | sfx_bell x2, sfx_collapse |
| 09 | The Old Covenant | 50 | 22s | none (Norway flag) | none | Contract unfurls + footnotes + 4 seals | sfx_paper x2, sfx_stamp x4, sfx_whoosh, sfx_bell |
| 10 | Denmark Inherits | 43 | 17s | north_atlantic | small Icelander figure (BC, T+0:12) | Crown slides + notice posted + shrug | sfx_whoosh |
| 11 | It Got Worse | 8 | 8s | none | none | Title card only. SILENCE. | none |
| 12 | The Black Death | 52 | 25s | iceland_overview | none | Ship + rat + counter + footnote | sfx_whoosh, sfx_bell, sfx_tick, sfx_collapse, sfx_stamp |
| 13 | Jon Arason Intro | 62 | 28s | none | jon_arason_defiant (CTR, T+0:05) | Avatar enters + 3 tags + 9 children | sfx_whoosh, sfx_tick x9 |
| 14 | Decades of Resistance | 5 | 15s | none | jon_arason icon (L5→timeline, exits L5 at end) | Timeline + 3 RESISTED + red X | sfx_stamp x3, sfx_collapse |
| 15 | The Execution | 40 | 17s | none | jon_arason_calm (CTR, T+0:02) dims and exits | Date stamp + 3 calm figures dim + text coda | sfx_stamp, SILENCE |
| 16 | Trade Monopoly | 65 | 25s | iceland_overview | none | District grid + merchants + flowchart | sfx_stamp |
| 17 | The Scales | 10 | 12s | none | none | Balance scale tips | sfx_collapse |
| 18 | Defenceless | 30 | 15s | iceland_overview | mystery ship silhouette (R edge, T+0:10) | 3 labels + mystery ship | sfx_bell, sfx_whoosh |
| 19 | Barbary Corsairs | 2 | 10s | none | none | 2 words + disclaimer. SILENCE. | none |
| 20 | The Raid | 60 | 28s | north_atlantic → iceland zoom | murat_reis (L3, T+0:02; exits L at T+0:10) | Long arrow + map zoom + 3 dots + 2 counters | sfx_whoosh x2, sfx_stamp x3, sfx_collapse x2 |
| 21 | The Procession | 42 | 18s | iceland_overview | 400 figure VGroup | 400 figures march + ships depart + title card | sfx_crowd, sfx_tick, sfx_stamp |
| 22 | Gudridur | 55 | 22s | none | gudridur (CTR) | Avatar still + bead arrow + 3 lines + pattern | sfx_whoosh, sfx_bell x2 |
| 23 | Return to Laki | 11 | 12s | none | none | Same crack callback + 1783 + recognition | sfx_bell |
| 24 | Fissure Returns | 23 | 12s | none (ledger overlay) | none | Ledger over crack + 2 GONE lines | sfx_tick, sfx_collapse |
| 25 | French Revolution | 65 | 26s | north_atlantic | none | Haze drifts + cause-effect chain + asterisk | sfx_tick x7 |
| 26 | Monopoly Blocks | 38 | 15s | iceland_overview | none | 3 relief ships blocked by grid + verdict | sfx_stamp x3 |
| 27 | Althing Abolished | 50 | 19s | none | none | Before/after split + ABOLISHED stamp | sfx_stamp (loudest) |
| 28 | Jorgensen Arrives | 65 | 28s | none | jorgensen_confident (CTR, T+0:02), count_trampe (R3, T+0:06 → L3 jail T+0:10), small Icelander (BC, T+0:20) | Trampe jailed + 3 scrolls + Icelander shrugs | sfx_whoosh x2, sfx_stamp |
| 29 | Sixty-Two Days | 6 | 12s | none | jorgensen_deflated (CTR dimmed, swap at T+0:11) | 3 comparison bars + 62-day sliver | sfx_clock |
| 30 | HMS Talbot | 95 | 30s | simplified world map (T+0:11) | jorgensen_deflated (CTR), Naval officer figure (R3, T+0:04) | Ship arrives + officer points + travel path + title card | sfx_whoosh x2, sfx_bell |
| 31 | The Final Ledger | 65 | 28s | none | none | Full ledger + STONE_GREY vs AMBER final lines | sfx_tick x5, sfx_stamp x2, sfx_bell |
| 32 | Lights across Iceland | 70 | 28s | iceland_overview (dark) | 13+ amber dot objects (appearing one by one) | Dots appear individually over 20s + 2 phrases | sfx_tick x13 (quiet) |
| 33 | Those People | 18 | 10s | iceland_overview (continues) | none (dots continue) | One dot pulses + 2-line verdict | sfx_bell |
| 34 | Episode Card | 4 | 15s | none | none | White card + progress bar + Ep3 pulse | none |

**Total scenes: 34**
**Estimated total runtime: ~670s (~11.2 min)**
**VO word count: ~1,340 words**
**Target range: 10-14 min — within range**

---

## CHANGES VS ORIGINAL EP2 DOCUMENT

| Change | Original | v2 | Reason |
|---|---|---|---|
| Scene count | 43 | 34 | VO-driven formula; merged short scenes |
| Duration formula | Not applied | Every scene calibrated | Ep1 v2 discipline |
| Em dashes | 30+ in audio + production | 0 | Writing rule |
| Visual moves per scene | Up to 8 concurrent | Max 2-3 per scene | Ep1 "not jittery" principle |
| Timestamp direction | None | T+XX:XX per beat | User requirement |
| Character positions | Vague | Manim position notation | User requirement |
| Enter/exit direction | Missing | Explicit per character | User requirement |
| Sound effects | Not noted | Per scene, with file name + dB | User requirement |
| Ep1 character reuse | Not noted | Snorri + Hakon explicitly called out | User requirement |
| SD prompts format | Separate doc | Embedded at top | Matches Ep1 format |
| "Barbary corsairs" | Buried in paragraph | Scene19: standalone 10s silence | Let absurdity land |
| Snorri death | Mixed in long scene | Scene08: silence discipline from Ep1 | Match Ep1 "They struck." weight |
| "It got worse" | Inline phrase | Scene11: title card + complete silence | Ep1 deadpan discipline |
| Gudridur | Part of Tyrkjaranid block | Scene22: dedicated scene, own entry | She deserves her moment |
| Silence as sound design | Not used | Scenes 08, 11, 15, 19 | Ep1's most powerful tool |

---

*File: EP2_Production_v2.md*
*Version: 2.0*
*Audio: tightened, no em dashes, ~1,340 words*
*Production: VO-synced, timestamped, SFX-noted, position-specific*
*Character assets: 5 new SD prompts + 2 Ep1 reuses noted*
*Ready for Python scene file generation*
