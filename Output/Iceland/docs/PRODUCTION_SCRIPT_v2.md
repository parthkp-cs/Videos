# Iceland Episode 1: "How to Steal an Island"
## Production Script v2 — Scene-by-Scene with VO Sync
### Tools: Manim (visuals) · Cartopy/matplotlib (maps) · AUTOMATIC1111 SD (avatars)

---

## VISUAL SYSTEM

**Frame:** 1920×1080, Manim 14.22 × 8.0 units  
**Safe zone:** H_PAD = 1.5u left/right · V_PAD = 0.9u top/bottom  
**Font:** Poppins throughout (Regular/Bold/SemiBold/Light)  
**Color palette:**
- DARK_BG = `#0A0A0A` — cold open, Sturlung, close
- WHITE_BG = `#FFFFFF` — most historical scenes
- AMBER = `#D4821A` — warmth, settlement age, highlight
- RED = `#CC1B21` — danger, collapse, Norway pressure
- BLUE = `#004AAD` — Althing, law, structure
- COLD_GREY = `#5A5A60` — Sturlung age, exhaustion
- SKY_BLUE = `#A8C8E8` — Þingvellir backgrounds
- STONE_GREY = `#7A7060` — rock, tectonic plates

**Background texture rule:** Cold open = black. Historical (874–1000) = warm white with cartopy map backgrounds. Althing scenes = SKY_BLUE with rift valley illustration. Sturlung = desaturated/cold. Close = near-black fading to warm amber.

**Animation feel:** Not jittery. Each scene has one or two confident visual moves, not five small ones.

---

## CHARACTER AVATAR DEFINITIONS (for Stable Diffusion)
### Style base for all: `flat vector illustration, Kurzgesagt educational style, clean confident linework, character design sheet, white background, full body, expressive face, warm muted palette`

### NEG for all: `photorealistic, 3d render, dark background, text, watermark, multiple characters, cropped, deformed, blurry, nsfw`

---

### AVATAR 01: Irish Papar Monk
**Scenes:** 10, 11, 12, 13
```
irish_monk_seated: "Kurzgesagt flat vector illustration, Irish papar monk c. 800 AD, 
middle-aged man, round face with slight smile of deep contentment, simple brown 
undyed wool robe tied with hemp rope, Celtic tonsure (wide bald crown, fringe of 
brown hair around the sides), bare feet with leather sandals nearby, seated 
cross-legged on a grey basalt rock, holding a small brass handbell in right hand 
and a small vellum book in left, eyes half-closed in meditation, steam wisps 
rising from ground around him suggesting hot springs, absolute peaceful solitude, 
warm amber halo glow behind figure, full body portrait, white background"

irish_monk_packing: "same monk standing, expression shifted from serene to quietly 
resigned — eyebrows slightly raised, lips pressed, the look of a man thinking 
'of course', holding a small cloth bag, bell visible inside bag, book tucked under 
left arm, right hand reaching for a small wooden crozier, mid-motion of packing up"

irish_monk_walking: "same monk walking left, small packed bag over shoulder, 
looking forward with dignified resignation, not rushing, not looking back, 
sandals on feet now, silhouette moving away"
```

---

### AVATAR 02: Ingólfr Arnarson
**Scenes:** 14, 17, 19
```
ingolfr_arnarson: "Kurzgesagt flat vector illustration, Norse settler Ingólfr 
Arnarson c. 874 AD, broad-shouldered weathered man age 35, short thick auburn 
beard, deep-set determined eyes, wearing a thick dark green wool cloak with 
wide fur collar in grey-brown, leather belt with iron buckle, rough wool trousers 
tucked into leather boots, standing at ship prow — one hand gripping a carved 
wooden post, the other shading eyes looking toward horizon, expression: stubborn 
commitment mixed with slight apprehension, North Atlantic grey sea background, 
full body"

ingolfr_releasing_pillars: "same Ingólfr leaning over ship side, both hands 
releasing two tall ornately carved wooden pillars into grey sea water, pillars 
showing Viking knotwork carving, expression: resolute, watching them go, the 
pillars already floating on waves below"
```

---

### AVATAR 03: King Harald Fairhair
**Scenes:** 15
```
king_harald_fairhair: "Kurzgesagt flat vector illustration, caricature of King 
Harald Fairhair of Norway c. 865 AD, exaggeratedly large golden crown tilted 
slightly, absurdly long flowing blond-gold hair (reaching to knees), very smug 
self-satisfied expression with closed-eye smile, round face suggesting well-fed 
contentment, wearing elaborate deep blue royal robes with gold trim, right hand 
on hip, left hand holding ornamented sceptre casually, standing in a slight 
power-pose, small figure of Ingólfr walking away in far background, full body, 
slightly comedic proportions for humor effect, white background"
```

---

### AVATAR 04: Thorgeir Þorkelsson (Lawspeaker)
**Scenes:** 34, 35, 29
```
thorgeir_under_cloak: "Kurzgesagt flat vector illustration, Þorgeir Þorkelsson 
Norse lawspeaker c. 1000 AD, elderly man completely enveloped in a massive thick 
brown fur cloak, only weathered eyes visible over cloak edge, long grey eyebrow 
visible, seated cross-legged on a flat stone, completely still, Iceland grassland 
background, mysterious contemplative atmosphere, heavy fur cloak dominates 
composition, very different from monk — this is deliberate isolation, full body"

thorgeir_speaking: "same elderly man standing on a flat rock, cloak now open and 
draped back revealing dark wool tunic, long grey beard, arms slightly raised 
addressing a crowd, calm absolutely authoritative expression, eyes steady and 
clear, crowd of figures visible in background, midday light"
```

---

### AVATAR 05: Erik the Red
**Scenes:** 38, 39, 40, 41
```
erik_the_red: "Kurzgesagt flat vector illustration, Erik the Red Norse explorer 
c. 982 AD, imposing broad figure, massive bright red-orange beard (most distinctive 
feature), heavy brow, permanently defiant expression somewhere between aggression 
and amusement, wearing a battered fur cloak with hood down showing battle-worn 
edges, leather armor with iron studs visible beneath, wide leather belt, hands 
on hips in challenging stance, slight scar on chin, ship or sea background 
suggested, full body portrait, slightly larger proportions than other characters 
to suggest physical dominance"

erik_exile_walking: "same Erik walking right, carrying a bundle of belongings 
over shoulder, holding a small 'EXILED AGAIN' sign in other hand, expression: 
resigned exasperation mixed with 'fine, I'll find somewhere better anyway', 
stride purposeful not defeated, grey sea in background"
```

---

### AVATAR 06: Leif Eriksson
**Scenes:** 44, 45, 47
```
leif_eriksson: "Kurzgesagt flat vector illustration, Leif Eriksson Norse explorer 
c. 1000 AD, younger than Erik (late 20s), cleaner appearance, dark blond-brown 
hair with simple braided headband, clean-shaven with slight stubble, adventurous 
wide-eyed expression, wearing well-made blue-grey wool cloak over leather-reinforced 
tunic, holding a rolled vellum chart/map in left hand and pointing westward with 
right hand index finger, standing at ship stern, Greenland ice behind him to the 
east, open ocean ahead, full body portrait"
```

---

### AVATAR 07: Snorri Sturluson
**Scenes:** 50, 51, 52, 53, 54, 58, 59, 63, 64
```
snorri_writing: "Kurzgesagt flat vector illustration, Snorri Sturluson Icelandic 
scholar c. 1220 AD, age 40, slight-framed but intelligent-looking man, dark 
auburn hair beginning to grey at temples, slight shadows under eyes (works too 
hard), wearing dark grey-black medieval Icelandic coat with simple clasps, 
seated at a writing desk, holding large white goose-quill pen in right hand, 
left hand steadying a large vellum manuscript, expression: absorbed concentration 
with a hint of pride, bookshelves of scrolls in background, candlelight warm 
glow, full body"

snorri_afraid: "same Snorri standing, expression: frightened, cornered — eyes wide, 
quill still in hand out of habit, backing toward a stone wall, shadows dominant, 
cellar stone wall background, dark scene, candle has blown out, only moonlight 
from above, full body"
```

---

### AVATAR 08: Gissur Þorvaldsson
**Scenes:** 62, 63
```
gissur_thorvaldsson: "Kurzgesagt flat vector illustration, Gissur Þorvaldsson 
Norse chieftain c. 1241 AD, tall imposing figure, angular hard face, short dark 
beard, cold calculating expression — not angry, just coldly purposeful, wearing 
dark chainmail shirt over black wool tunic, fur-lined hood around shoulders, 
right hand resting on sword pommel at belt, left hand at side, night scene with 
torch shadows creating dramatic lighting, farmhouse stone walls behind, full 
body portrait, intimidating but controlled"
```

---

### AVATAR 09: Hákon IV of Norway
**Scenes:** 57, 58
```
hakon_iv: "Kurzgesagt flat vector illustration, King Hákon IV of Norway c. 1241 AD, 
seated on a carved wooden throne, patient chess-player expression — slight 
half-smile, one eyebrow raised, watching from a distance, wearing Norwegian royal 
robes in deep red with gold trim, moderate crown (not comically large like Harald, 
this one is restrained and real), elbows on armrests, fingers steepled in front 
of chest, Norwegian lion heraldic tapestry behind throne, deliberate composed 
stillness, full body portrait"
```

---

---

## SCENE-BY-SCENE PRODUCTION SCRIPT

### Duration formula: target = (word_count ÷ 145wpm × 60) + 1.5s visual hold
### Durations marked as: `[TARGET: Xs]` = new target · `[WAS: Xs]` = previous version

---

## INTRO

---

### SceneIntro — Title Card | `[TARGET: 8s]`
**VO:** *(silent)*  
**VISUAL:** Full-screen Iceland flag (blue/white cross). Flag fills frame edge-to-edge. Manim's SVGMobject or Rectangle composition. Hold 3s then:  
Crossfade — title text fades in over flag: `"ICELAND"` large BOLD in white, subtitle `"How to Steal an Island"` in LIGHT below, sub-subtitle `"Episode 1 · 874 AD – 1262"` in LIGHT smaller. All centered. Text in safe zone.  
After 5s hold: white overlay rectangle fades in to white → transition to Scene01.  
**MANIM NOTE:** Use `ImageMobject` for the flag PNG if available, else build from rectangles. White fade overlay z_index=10.

---

## COLD OPEN

---

### Scene01 — The Number | `[TARGET: 9s]` `[WAS: 9.8s]`
**VO:** *"October 2008. Iceland's three biggest banks — Kaupthing, Landsbanki, Glitnir — collapsed in a single week."*  
**VISUAL:** Pure black background throughout. At 0s: `"11×"` appears centered — white text, fills ~65% of screen height (font_size ≈ 260). Animate with `GrowFromCenter` taking 0.5s. Hold 1.5s.  
At 2s: subtitle line fades in below: `"that's how many times larger the banks were than the entire economy"` — white, small (font_size=32), slightly grey. One line, centered.  
At 7s: single low pulse (visual only — add a brief Scale(1.05) then back on the `11×`).  
**NOTE:** No other elements. Maximum negative space. This is the hook.

---

### Scene02 — Banks Fall | `[TARGET: 6s]` `[WAS: 6.87s]`
**VO:** *"Their combined assets were eleven times the country's entire GDP."*  
**VISUAL:** Dark background. Left side: three bank building icons — each is a white Rectangle + Triangle roof, height ~2.5u, labeled "KAUPTHING" "LANDSBANKI" "GLITNIR" in small text below. They appear at 0s (`GrowFromCenter` staggered 0.2s apart).  
At 2s: the three buildings simultaneously tilt and fall — `rotate(-PI/2.3)` + `shift(DOWN*3)` with `run_time=1.2`. They fall *off screen*.  
Right side: tiny `"GDP"` bar (height 1u in AMBER) vs `"BANK ASSETS"` arrow pointing *off the top of screen* with label `"↑ still going"`. This punchline appears at 3s, hold 2s.  
**NOTE:** The GDP joke should be deadpan — small bar left, giant off-screen arrow right.

---

### Scene03 — The Graphs | `[TARGET: 8s]` `[WAS: 8.4s]`
**VO:** *"The currency lost more than half its value in days. The stock market shed over ninety percent."*  
**VISUAL:** White background, two graph axes side by side.  
LEFT GRAPH: labeled `"ISK (króna)"` — line starts top-left, drops 55% down then *falls off the right edge of frame*. Animate the line drawing with `Create`, run_time=2s.  
RIGHT GRAPH: labeled `"Stock Market"` — line starts top-left, drops 90% almost to bottom, then falls off bottom edge. Same animation, slight offset.  
Both use axes with `x_length=5.5, y_length=4.0`. After both lines fall: a small text label appears at fall point: `"−55%"` and `"−90%"` in RED.  
**NOTE:** Lines literally falling off the screen edge is the visual joke. Keep it clean — 2 graphs only, no extra clutter.

---

### Scene04 — Empty Shelves | `[TARGET: 10s]` `[WAS: 10.4s]`
**VO:** *"Grocery stores started running short on imported food. A country of three hundred thousand people was, by every measurable standard, bankrupt."*  
**VISUAL:** White background. A supermarket shelf — 3 horizontal shelf planks (brown rectangles, width=10u), 5 shelf spots per plank = 15 total item slots.  
At 0s: all 15 slots have simple coloured box-products (AMBER, BLUE, RED small rectangles with brand-dot labels).  
At 2s: items disappear one by one left-to-right, top shelf first — `FadeOut` staggered every 0.3s. By 6s: all gone except ONE tin can on the bottom-right shelf.  
At 7s: a hand/arm rectangle slides in from right, picks up the tin. The tin vanishes. Shelf completely empty.  
At 9s: text fades in top-right: `"300,000 people"` + `"bankrupt."` in BOLD.  
**NOTE:** The image of an *empty shelf* is instantly legible globally. Make the shelf realistic-looking with proper spacing.

---

### Scene05 — The Puppet | `[TARGET: 15s]` `[WAS: 5.73s — MAJOR EXTEND]`
**VO:** *"Most countries, at that point, would have done what their creditors told them to do. Bail out the banks. Repay the foreign depositors. Take the austerity package. Smile for the IMF cameras."*  
**VISUAL:** White background. A puppet figure (simplified human shape — circle head, rectangle body, stick arms/legs) appears center-screen. Chest label: `"MOST COUNTRIES"` in bold.  
Four strings rise from the puppet's shoulders and hands to a large Hand shape above labeled `"IMF"`.  
**Animation sequence (timed to VO):**  
- 0–3s: Puppet appears, strings draw upward  
- 3s: VO says "Bail out the banks" → puppet raises arm, waves cheerfully  
- 5s: VO says "Repay the foreign depositors" → puppet takes out wallet icon, hands it to the left  
- 7s: VO says "Take the austerity package" → puppet receives a LARGE PACKAGE labeled "AUSTERITY" and visibly bends under the weight  
- 10s: VO says "Smile for the IMF cameras" → puppet turns to face screen, big forced smile  
- 12s: Camera icon pops up, flash effect. Puppet's smile is extremely strained.  
**NOTE:** This scene needs all 15s — it's the comedic setup for Iceland's defiance. Each VO beat has a matching puppet action.

---

### Scene06 — Iceland's Answer | `[TARGET: 12s]` `[WAS: 6.6s — EXTEND]`
**VO:** *"But, instead, Iceland jailed its bankers. Told the English and the Dutch to get lost. Let the banks fail. And yet, recovered faster than anyone."*  
**VISUAL:** Dark background. Four beats, each 3s:  
**Beat 1** (0s): Prison bars slide down. A small suited-figure (banker silhouette) is behind them. Icelandic flag small top-right. Label: `"JAILED."` in AMBER.  
**Beat 2** (3s): UK flag + Netherlands flag appear left. Bold arrow pointing RIGHT → off screen. Label: `"GET LOST."` UK/NL flags exit right.  
**Beat 3** (6s): The three bank buildings from Scene02 appear again but smaller — and they simply COLLAPSE with no rescue. A `✗ NO BAILOUT` label stamps over them.  
**Beat 4** (9s): Simple upward-trending arrow in AMBER on dark bg. Label: `"Recovered. Faster than anyone."` The arrow is confident — not flashy, just right.  
**NOTE:** Four beats = four lines of VO. Each beat is exactly 3s. Punchy.

---

### Scene07 — Time Rewind | `[TARGET: 10s]` `[WAS: 10s]`
**VO:** *"To understand how a tiny island builds that kind of backbone, you have to go back to the very beginning. 874 AD."*  
**VISUAL:** Load cartopy `north_atlantic.png` map as background. Iceland visible center-left as a small island in a dark sea.  
Year counter appears top-right: starts at `"2008"` in RED, spins backward — `2008 → 1944 → 1800 → 1262 → 874`. Text blurs during spin (opacity flash), then lands hard on `"874"` in AMBER at 8s.  
Iceland outline on map pulses once (scale 1.05→1.0) as counter lands.  
**NOTE:** This is the transition moment. The year landing should feel like a *thud*. GrowFromCenter on the `874` landing.

---

### Scene08 — Title Card 874 | `[TARGET: 5.5s]` `[WAS: 5.47s]`
**VO:** *(brief hold — VO says "874 AD" in previous scene, this is visual emphasis)*  
**VISUAL:** Black background fades to warm AMBER-BROWN gradient. `"874"` in massive Poppins BOLD (font_size=220) centered, color: AMBER, burns in with `DrawBorderThenFill` run_time=1.5s.  
Below: `"AD"` in smaller SEMIBOLD fades in. Below that: dotted-line text label fades in: `"Iceland's founding year"` in LIGHT white.  
Hold 3s. Scene ends with image *still on screen* — cut directly to Scene09 (no fade needed).

---

## PART ONE: BEFORE THE VIKINGS, THERE WERE THE MONKS

---

### Scene09 — Blank Island | `[TARGET: 8s]` `[WAS: 11.73s — TRIM]`
**VO:** *"Actually, back up slightly further. Because Iceland didn't start with Vikings. It started with monks."*  
**VISUAL:** Load `iceland_overview.png` cartopy map. The map has the island labeled. At 0s: all labels FADE OUT — only the blank coastline silhouette remains. The island looks truly empty.  
Counter ticks back slightly from 874 → blurred `"c. 800s"` label appears top-left.  
`"No settlers."` label appears bottom-center in LIGHT grey.  
The emptiness IS the point. Hold 5s then cut.  
**NOTE:** Keep it short — this is a quick setup for the big reveal.

---

### Scene10 — The Papar Monk | `[TARGET: 29s]` `[WAS: 16.13s — MAJOR EXTEND]`
**VO:** *"Before any Norse settler set foot on the island, a small group of Irish Christian hermits — the papar, as the old texts call them — had already been living there. They had sailed north deliberately, looking for the most remote, God-soaked silence they could find, somewhere between the known world and the edge of it. The place they found is what we call today, Iceland."*  
**VISUAL:** White background (warm). Load `irish_monk_seated.png` avatar (SD generated) centered, height=3.5u. If SD not available: circle head + triangle robe + bell in hand (geometric fallback, radius=0.55, robe scale=1.4).  
Avatar `GrowFromCenter` entrance at 0s, run_time=1.0.  
Label appears below: `"The Papar"` in Poppins BOLD + `"Irish Christian hermits, c.800 AD"` in LIGHT — both in safe zone, anchored to bottom.  
At 8s: three small `"..."` text icons appear around the monk suggesting absolute silence.  
At 15s: a small cross icon `✝` plants itself left of monk (FadeIn).  
At 20s: Steam wisps (3 thin curved lines, animated `CurvedArrow`) appear at monk's feet — hot springs suggestion.  
At 25s: Pull-quote fades in top-left area (in safe zone): `"looking for the most remote,\nGod-soaked silence they could find"` — Poppins LIGHT ITALIC, font_size=28, AMBER color.  
Hold through 29s.  
**NOTE:** This is the longest single scene in Part 1. Give it weight — the monk just sits there and that IS the scene.

---

### Scene11 — The Tiny Boat | `[TARGET: 9s]` `[WAS: 9.13s]`
**VO:** *"They settled in. They were having a perfectly good solitary existence."*  
**VISUAL:** Dark grey-blue sea background (gradient Rectangle). A tiny boat center-frame — hull polygon + single mast line. One monk figure inside (tiny, load `irish_monk_seated` at scale 0.6).  
Left side of sea: label `"The Known World →"` in LIGHT grey.  
Right side: label `"← Probably Fine"` in LIGHT grey, slight italic.  
Boat bobs gently (up/down 0.1u, run_time=4s linear loop).  
At 5s: `"settled in."` text appears top-center in BOLD AMBER. `"perfectly good solitary existence."` fades in below in LIGHT.  
**NOTE:** The two labels are the entire joke. The scene is otherwise completely calm.

---

### Scene12 — The Monk Departs | `[TARGET: 9.5s]` `[WAS: 10.87s]`
**VO:** *"Then the Norse arrived, and the monks packed up their bells and their books and their croziers, and left."*  
**VISUAL:** White background. Split screen.  
RIGHT: A longship silhouette appears on the horizon — simple hull profile, square sail. It moves slowly LEFT from off-screen right. `FadeIn`, then `animate.shift(LEFT * 2)`.  
LEFT/CENTER: Load `irish_monk_packing.png` avatar OR geometric monk with expression change. Expression label appears as text: `"...of course."` in italic GREY nearby.  
The monk figure then `animate.shift(LEFT * 4)` — walking off screen — while the longship moves in from right. They pass each other going opposite directions.  
Final frame: empty center, longship on right.  
**NOTE:** The direction of travel is the scene. Monk exits left, ship enters right. Needs no additional explanation.

---

### Scene13 — First Instinct | `[TARGET: 16s]` `[WAS: 8.47s — EXTEND]`
**VO:** *"They had come all this way specifically to be alone. Iceland's very first residents chose it for the same reason its founders would: to get away from people with opinions about how they should live."*  
**VISUAL:** Load `iceland_overview.png` as background at half-opacity (desaturated). Empty shoreline visible.  
A small wooden cross stands in sand/rock (Rectangle + Line, simple). Longship silhouettes appear on the horizon right.  
This scene is a HOLD with text overlay. The key element is a pull-quote that builds word by word:  
`"to get away from people with opinions"` — appears word by word, Poppins BOLD ITALIC, font_size=44, AMBER, centered on screen. Each word fades in with 0.5s gap.  
`"about how they should live."` — continues on next line, same treatment.  
Hold 4s after full quote appears.  
**NOTE:** The quote IS the scene. The visual hold builds weight. This is 16s because the VO is 35 words — give it time.

---

## PART TWO: THE FOUNDING — FURNITURE DELIVERY LOGISTICS

---

### Scene14 — Ingólfr Sets Out | `[TARGET: 10s]` `[WAS: 9.47s]`
**VO:** *"The man credited with the first permanent Norse settlement was Ingólfr Arnarson, who arrived in 874 AD. He was fleeing Norway —"*  
**VISUAL:** Load `north_atlantic.png` cartopy map as background. Norway visible right, Iceland visible left-center.  
A small ship icon appears on Norway's coast at 0s (`GrowFromCenter`). A dotted arrow path animates from Norway westward toward Iceland (`Create`, run_time=3s).  
At 4s: Load `ingolfr_arnarson.png` avatar (SD) left-of-center, height=3.0u. `GrowFromCenter` entrance.  
Label below: `"Ingólfr Arnarson"` BOLD + `"874 AD"` SEMIBOLD AMBER.  
Ship continues moving along dotted path in background.  
**NOTE:** Map provides geographic grounding. Avatar appears mid-scene as character is named.

---

### Scene15 — Harald Fairhair | `[TARGET: 15s]` `[WAS: 6.67s — MAJOR EXTEND]`
**VO:** *"King Harald Fairhair was busy consolidating power back home, which is a polite way of saying he was making life unpleasant for anyone who disagreed with him. Ingólfr didn't disagree politely. He left."*  
**VISUAL:** White background. Load `king_harald_fairhair.png` avatar right-side, height=3.0u. Harald fills the right half. `GrowFromCenter`.  
Label appears: `"Harald Fairhair"` + `"(consolidating power)"` in parentheses, GREY ITALIC.  
At 4s: tiny Ingólfr (load `ingolfr_arnarson.png` at scale 0.5) appears far left, holding a small bag.  
A large thought-bubble from Harald's head contains `"my kingdom. mine."` in cheerful font.  
At 8s: An expanding boundary indicator (growing circle/rectangle from Harald outward) moves left. Small label: `"radius of royal opinions"`.  
At 11s: Ingólfr takes one look, turns, and `animate.shift(LEFT * 5)` — walks off screen left. Does not look back.  
At 13s: Harald waves goodbye cheerfully. He doesn't notice Ingólfr is gone. He looks pleased with himself regardless.  
**NOTE:** This needs the full 15s — it's a comedic beat with 3 distinct movements.

---

### Scene16 — The Sailing Route | `[TARGET: 9s]` `[WAS: 10.13s]`
**VO:** *"His method for choosing where to build his home is one of history's great examples of logistical commitment."*  
**VISUAL:** Load `ingolfr_route.png` cartopy map (Iceland coastline with route annotations). The pre-rendered map shows the 3-year route circling the island.  
On top: animate a small ship icon tracing the route path — `MoveAlongPath` on the route line, run_time=5s.  
Route has three marker notes (pre-rendered in map or overlaid):  
- `"not here"` — northwest coast  
- `"checked this already"` — south coast  
- `"3 years"` label in a box — route duration  
**NOTE:** The cartopy map does the heavy lifting here. Only the ship icon moves in Manim.

---

### Scene17 — The Pillars Overboard | `[TARGET: 14s]` `[WAS: 9s — EXTEND]`
**VO:** *"He threw his high-seat pillars overboard — these were ornately carved wooden posts, central to Norse household and religious life — and pledged to settle wherever they washed ashore."*  
**VISUAL:** Dark grey ocean background. Load `ingolfr_releasing_pillars.png` (SD) center, height=3.2u. Avatar shows Ingólfr leaning over ship side releasing pillars.  
At 0s: avatar appears. Two carved wooden post objects (Rectangles with decorative VGroup knotwork detail) floating in the water below.  
At 4s: pillars begin drifting right (`animate.shift(RIGHT)` slowly, run_time=8s linear).  
Text label appears at 4s: `"high-seat pillars"` with sub-label `"(central to Norse household and\nreligious life)"` in LIGHT grey.  
At 10s: Ingólfr is still watching. Add label: `"(he is still watching)"` in parentheses, italic, gentle humor.  
At 12s: pillars float further. Ingólfr continues watching. Nothing else happens.  
**NOTE:** The comedy is in the *commitment* to watching. The pillars just... float. He keeps watching. Hold on this.

---

### Scene18 — Missing Poster | `[TARGET: 7s]` `[WAS: 7.73s]`
**VO:** *"Then he spent three years sailing along the coast looking for them."*  
**VISUAL:** White background. A simple "MISSING" poster — like a lost pet poster — appears center. Poster shows: a rough drawing of two wooden pillars, title `"MISSING"` in RED, description: `"Two carved high-seat pillars"` `"Last seen: somewhere in the North Atlantic"` `"Contact: Ingólfr Arnarson"` `"(currently sailing nearby)"`.  
`"3 YEARS"` stamp appears bottom of poster in big RED ink.  
**NOTE:** Pure deadpan visual gag. No animations needed — just `FadeIn` the poster, stamp appears, hold.

---

### Scene19 — Reykjavík Founded | `[TARGET: 11s]` `[WAS: 9.47s]`
**VO:** *"They eventually turned up at a bay where steam rose from hot springs in the ground. He named it Reykjavík. Smoky Bay."*  
**VISUAL:** Load `iceland_overview.png` map as background. Southwest coast of Iceland marked with a glowing dot.  
Load `ingolfr_arnarson.png` at scale 0.8, left of center, pointing at the ground.  
Steam wisps (3 CurvedArrow lines, white, stroke_opacity=0.6) animate rising from ground beneath his feet.  
At 5s: City name label animates in: `"REYKJAVÍK"` in large AMBER BOLD, placed at SW coast on map.  
Sub-label below: `"Smoky Bay"` in LIGHT italic.  
At 8s: A tiny settlement icon (3 small rectangle houses) appears next to the dot.  
**NOTE:** The steam is critical — Reykjavík literally means "Smoky Bay". Make the steam prominent.

---

### Scene20 — Capital Label | `[TARGET: 8s]` `[WAS: 8.4s]`
**VO:** *"Iceland's capital was chosen by furniture delivery logistics, and it has been the capital ever since."*  
**VISUAL:** White background, large centered text treatment.  
`"Reykjavík"` appears in large BOLD (font_size=72) AMBER.  
Below: `"Capital of Iceland"` in SEMIBOLD BLUE.  
Below: `"Chosen by: furniture delivery logistics"` in LIGHT GREY ITALIC font_size=28.  
Below: `"Est. 874 AD — still going."` in LIGHT font_size=22.  
Each line fades in 0.7s after the previous. Hold last line 3s.  
**NOTE:** This is a visual pause/joke beat. Clean typography only.

---

## PART THREE: THE GREAT MIGRATION

---

### Scene21 — Great Migration | `[TARGET: 7s]` `[WAS: 16.67s — MAJOR TRIM]`
**VO:** *"Between 874 and 930, somewhere between eight thousand and twenty thousand settlers followed."*  
**VISUAL:** Load `settlement_migration.png` cartopy map showing migration arrows from Norway/Britain to Iceland.  
Population counter animates: starts at `"0"` → counts up to `"8,000–20,000"` over 4s.  
Date bar shows `"874 AD"` → `"930 AD"` with animated fill.  
**NOTE:** This scene is SHORT because the VO is short. Don't pad it. The map explains it.

---

### Scene22 — Where They Came From | `[TARGET: 13s]` `[WAS: 7.67s — EXTEND]`
**VO:** *"Most came from western Norway. Some came from Norse-settled communities in Britain and Ireland, bringing Irish wives and Irish slaves whose DNA is still visible in Icelanders today."*  
**VISUAL:** Load `settlement_migration.png` map persists. Highlight western Norway in AMBER (Rectangle overlay semi-transparent). Arrow from Norway → Iceland labeled `"Most settlers"`.  
Second arrow from Britain/Ireland → Iceland labeled `"Some settlers"` in a slightly different tone.  
At 7s: DNA helix icon (two intertwined curves) appears with label:  
`"their DNA: still in Icelanders today"` — in AMBER ITALIC font_size=24, placed in Iceland on map.  
**NOTE:** The DNA line is emotionally resonant — emphasize it.

---

### Scene23 — Choosing the Volcano | `[TARGET: 13s]` `[WAS: 8.13s — EXTEND]`
**VO:** *"They came because Norway was overcrowded, because Harald was king, and because some people would sail into an active volcanic field before they'd submit to a monarch."*  
**VISUAL:** White background. Three-column visual:  
Column 1 `"Norway: overcrowded"` — many small figures packed together (VGroup of 20+ tiny stick figures)  
Column 2 `"Harald: king"` — small caricature crown icon, smug expression  
Column 3 `"Iceland: active volcanic field"` — a volcano shape with lava (RED) erupting  
An arrow points FROM columns 1&2 TOWARD column 3 with label: `"preferred option"`.  
This should be slightly absurdist — the volcano is clearly worse by any normal metric, but these settlers chose it.  
At 9s: Pull-quote below: `"some people would sail into a volcano\nbefore they'd submit to a monarch."` — BOLD, font_size=32.

---

### Scene24 — Refuge Hold | `[TARGET: 9s]` `[WAS: 10.47s]`
**VO:** *"Iceland was, from its very first days, a refuge for people who did not want to be ruled."*  
**VISUAL:** Load `iceland_overview.png` map. Iceland glows in warm AMBER — `set_fill(opacity=0.7)` on the island outline.  
Large centered text over map: `"A refuge"` in BOLD AMBER font_size=64.  
Below: `"for people who did not want to be ruled."` in LIGHT white font_size=34.  
The word `"did not want to be ruled"` underlines itself (DrawUnderline animation).  
**NOTE:** This is the thesis statement for the whole episode. Give it gravitas.

---

### Scene25 — Transition to Althing | `[TARGET: 11s]` `[WAS: 8.07s — EXTEND]`
**VO:** *"Which made it all the more remarkable that they built their own way to govern themselves — by building their own government."*  
**VISUAL:** White background. A text beat — builds the irony:  
First: `"People who refused to be governed by anyone"` — fades in, BOLD, DARK.  
Then: `"...built a government."` — appears after 4s, BOLD AMBER, slightly larger.  
Then: `"930 AD"` timestamp fades in, top-right, SEMIBOLD BLUE.  
At 8s: A small silhouette of Þingvellir rift valley (the tectonic plates) fades in at bottom as transition hint.  
**NOTE:** The irony of this moment deserves the 11s. Let the two text lines breathe.

---

## PART FOUR: THE ALTHING — THE OLDEST PARLIAMENT

---

### Scene26 — Þingvellir Landscape | `[TARGET: 8s]` `[WAS: 8.27s]`
**VO:** *"In 930, the Althing convened for the first time at Þingvellir —"*  
**VISUAL:** SKY_BLUE background. Full Þingvellir rift valley illustration — two stone plate walls (STONE_GREY Rectangles, width=2.5u height=7u) on left and right, green plain (GREEN_FLOOR Rectangle) at bottom, sky blue above.  
The scene builds: plates appear first from off-screen (slide in), then plain fills in, then Law Rock (STONE_GREY Ellipse) appears center.  
Year label: `"930 AD"` burns in top-right in AMBER.  
**NOTE:** This is an establishing shot. Give it space to breathe. No characters yet.

---

### Scene27 — Tectonic Comedy | `[TARGET: 13s]` `[WAS: 7.8s — EXTEND]`
**VO:** *"a dramatic rift valley where the North American and Eurasian tectonic plates are slowly pulling apart, as if the land itself was making a point about freedom."*  
**VISUAL:** Continue Þingvellir background. Add two plate labels:  
LEFT plate: `"NORTH AMERICAN\nPLATE"` label in BLUE  
RIGHT plate: `"EURASIAN\nPLATE"` label in AMBER  
At 3s: Plates begin to slowly pull apart — `plate_left.animate.shift(LEFT*0.25)`, `plate_right.animate.shift(RIGHT*0.25)`, run_time=8s linear.  
At 5s: A speech bubble appears from the ground between plates: `"a point about freedom"` in ITALIC.  
At 10s: Small geology textbook icon appears with label `"happening since 60 million years ago"` in tiny GREY text — deadpan footnote.  
**NOTE:** The 13s gives the tectonic movement time to feel slow and inevitable — which is the point.

---

### Scene28 — Thirty-Six Chieftains | `[TARGET: 8s]` `[WAS: 10.53s]`
**VO:** *"Thirty-six chieftains gathered for what was, by any serious assessment, the world's oldest surviving parliamentary institution."*  
**VISUAL:** Continue Þingvellir. 36 figure silhouettes appear on the plain — arranged in 2 rows of 18. Each figure: circle head (radius=0.13) + rectangle body (0.14 × 0.30) in varied brown/ochre tones. Staggered `FadeIn` (lag_ratio=0.06), run_time=1.5s.  
Counter appears: `"36 chieftains"` in BOLD AMBER top-center.  
Label below: `"World's oldest parliamentary institution"` in BLUE SEMIBOLD font_size=22.  
At 6s: `"No king."` appears bottom-left, BOLD.

---

### Scene29 — The Lawspeaker Speaks | `[TARGET: 10s]` `[WAS: 8.73s]`
**VO:** *"No king. No standing army. No central state. Just laws, spoken aloud from memory by the Lawspeaker over his three-year term,"*  
**VISUAL:** Load `thorgeir_speaking.png` avatar (SD) standing on Law Rock center-stage, height=3.0u. GrowFromCenter.  
Three "NO" labels appear and then CROSS OUT themselves staggered:  
`"✗ No King"` · `"✗ No Army"` · `"✗ No Central State"`  
Each appears with FadeIn then a RED strikethrough line draws across it.  
At 6s: `"JUST LAWS."` appears large in AMBER BOLD, all caps.  
The Lawspeaker figure has a small text label: `"Memorized every law.\n3-year term.\nSpoken aloud."` in small LIGHT grey.

---

### Scene30 — The Gov Org Chart | `[TARGET: 10s]` `[WAS: 7.07s — EXTEND]`
**VO:** *"and a system of public dispute resolution that somehow held together a population scattered across a volcanic island with no roads."*  
**VISUAL:** White background. A simple organizational diagram builds:  
Top: `"THE ALTHING"` box in BLUE BOLD  
Below: three boxes: `"Public Laws"` · `"Dispute Resolution"` · `"No Roads Needed"`  
Connection lines `Create` from top to each. Under `"No Roads Needed"` box: a small sub-label: `"(a feature, apparently)"` in GREY ITALIC.  
At 7s: Pull-quote bottom: `"somehow held together a population\nscattered across a volcanic island"` — ITALIC AMBER.

---

### Scene31 — Althing Wide Shot | `[TARGET: 11.5s]` `[WAS: 9.73s]`
**VO:** *"It was not a democracy in any modern sense. The chieftains held the power. But it was deliberative, it was public, and it worked."*  
**VISUAL:** Return to full Þingvellir — all 36 figures visible, plates slowly pulling apart in background.  
At 3s: Three labels appear one after another: `"deliberative."` `"public."` `"worked."` — each in BOLD AMBER, appear sequentially with 1.5s gap each, placed center-frame.  
At 9s: Final text hold: `"For 330 years."` in large BLUE BOLD. This is the summary statement.  
`"— VO Part 1 ends —"` marker (for production only, not rendered).

---

## PART FIVE: CHRISTIANITY — THE PRAGMATIC CONVERSION

---

### Scene32 — Conversion Crisis | `[TARGET: 9s]` `[WAS: 7.8s]`
**VO:** *"The Althing's finest hour came around the year 1000, when Iceland faced its most consequential decision: Christianity or Paganism?"*  
**VISUAL:** White background. Large split — left half: AMBER (Pagan sun/Thor's hammer symbol), right half: BLUE (Christian cross).  
Label center: `"c. 1000 AD"` BOLD.  
The dividing line between them vibrates slightly — tension.  
`"Christianity or Paganism?"` appears as question mark in large font_size=60 centered.  
`"Civil war: a real possibility."` small label below in RED.

---

### Scene33 — Óláfr's Pressure | `[TARGET: 11s]` `[WAS: 10.27s]`
**VO:** *"Norway's King Óláfr Tryggvason was pressuring conversion. Half of Iceland was already Christian. The other half was not. Civil war was a real possibility."*  
**VISUAL:** Load `north_atlantic.png` map. Norway highlighted. Large arrow pointing FROM Norway TO Iceland labeled `"'Convert. Please.'\n— King Óláfr"` (in quotes, with please being slightly sarcastic).  
Iceland split in two — LEFT half AMBER (pagan), RIGHT half BLUE (Christian). A crack line runs down the middle of Iceland.  
Population counter: `"½ Christian  ½ Pagan"` — shown as split bar.  
`"Civil war brewing."` in RED, bottom-center.

---

### Scene34 — Thorgeir Appears | `[TARGET: 8s]` `[WAS: 7.73s]`
**VO:** *"The two factions agreed to let the lawspeaker, Þorgeir Þorkelsson, decide."*  
**VISUAL:** White background. LEFT side: AMBER crowd (pagan figures). RIGHT side: BLUE crowd (Christian figures). Both crowds face center.  
Center stage: A glowing spotlight area on the Law Rock. `"?"` blinks there.  
`"they agreed to let one man decide"` label top.  
Then: Load `thorgeir_under_cloak.png` avatar (SD) walks in from off-screen center. `GrowFromCenter`. He stands on the rock.  
Label: `"Þorgeir Þorkelsson"` BOLD + `"The Lawspeaker"` LIGHT.

---

### Scene35 — Under the Cloak | `[TARGET: 14s]` `[WAS: 17.67s — TRIM]`
**VO:** *"Þorgeir, himself a pagan, disappeared under his fur cloak for a full day and a full night. He meditated. He thought. He emerged and announced his verdict: Iceland would be Christian."*  
**VISUAL:** `thorgeir_under_cloak.png` fully enveloped. The ENTIRE scene is this figure, still, wrapped, on a rock.  
Time indicators appear: `"Day 1 — dawn"` → `"Day 1 — noon"` → `"Day 1 — dusk"` → `"Night"` → `"Day 2 — dawn"` — each fades in/out in top-left, creating time passage.  
At 10s: Cloak OPENS — dramatic moment. Avatar changes to `thorgeir_speaking.png`. He emerges.  
At 12s: His verdict text burns in: `"Iceland will be Christian."` — BOLD BLUE font_size=52, center screen. GrowFromCenter.  
**NOTE:** Trim 3s from current. The cloak-hold is evocative but 17s is too long — 14s is right.

---

### Scene36 — Terms and Conditions | `[TARGET: 12s]` `[WAS: 9.87s — EXTEND]`
**VO:** *"But — and this is the part that tells you everything about Iceland. Christianity came with a horsemeat exemption. Private consumption of horse was still permitted."*  
**VISUAL:** A terms & conditions scroll unfurls (Rectangle revealing animation). Title: `"New Terms and Conditions"` `"Re: Christianity, Iceland Branch"`.  
Body text appears line by line (Poppins font_size=22):  
`"1. Iceland officially Christian. (✓)"` — BLUE  
`"2. Horsemeat: still fine in private. (✓)"` — AMBER  
`"3. Horse worshipping in public: not fine. (✗)"` — strikethrough  
`"4. Signed by: a Pagan. (✓)"` — AMBER  
Legal-style fine print at bottom: `"Christianity accepted on Icelandic terms."` ITALIC.  
Each line appears with 1.5s gap, giving time to read.

---

### Scene37 — Compromise Achieved | `[TARGET: 19s]` `[WAS: 11.4s — MAJOR EXTEND]`
**VO:** *"Exposure of unwanted infants was still allowed. The new faith was adopted on Icelandic terms, negotiated by a pagan who understood that the alternative was bloodshed. Pragmatism dressed up as theology. It would not be the last time Iceland repackaged necessity as principle."*  
**VISUAL:** Continue the T&C scroll. More items appear:  
`"5. Infant exposure in private: still permitted. (complex)"` — in an uncomfortable yellow-grey  
`"6. Signed by: a Pagan who understood bloodshed."` — RED  
`"7. Effective: immediately."` — BLUE  
At 8s: Scroll rolls up. Large centered text replaces it:  
`"Pragmatism dressed up as theology."` — BOLD AMBER font_size=44, italic.  
At 13s: A small timer / recurring stamp: `"(not the last time)"` pops in bottom-right — GREY ITALIC, small.  
At 15s: Pull-quote: `"It would not be the last time\nIceland repackaged necessity as principle."` — Poppins LIGHT ITALIC.  
**NOTE:** This is the editorial heart of Part 5. Give it 19s. The T&C format is the conceit — use it fully.

---

## PART SIX: ERIK, LEIF, AND THE DISCOVERIES

---

### Scene38 — Erik Introduced | `[TARGET: 9s]` `[WAS: 7.4s]`
**VO:** *"Around 982, Iceland produced its most famous export of the era: a man too violent even for Iceland."*  
**VISUAL:** White background. A job-posting style frame:  
`"EXPORT OF THE ERA — 982 AD"` title bar in RED.  
Below: `"Product:"` with description: `"One (1) Man."` `"Too violent even for Iceland."` `"Available immediately."` `"Reasons: manslaughter × 2"`  
Load `erik_the_red.png` avatar right side, height=3.2u. GrowFromCenter.  
`"Erik the Red"` label under avatar, BOLD.  
**NOTE:** The "export" framing is the joke. Visual punch.

---

### Scene39 — Two Exile Notices | `[TARGET: 14s]` `[WAS: 7.4s — MAJOR EXTEND]`
**VO:** *"Erik the Red had already been exiled from Norway for manslaughter before arriving here. Iceland exiled him too — also for manslaughter. Sensing a pattern in his reviews, Erik sailed west."*  
**VISUAL:** White background. Two formal "NOTICE OF EXILE" documents appear side by side:  
LEFT DOCUMENT: `"NOTICE OF EXILE"` header with Norway flag icon.  
Body: `"Name: Erik Þorvaldsson"` `"Reason: manslaughter"` `"Duration: 3 years"` `"Signed: King of Norway"`  
Official stamp: `"EXILED"` in red.  
RIGHT DOCUMENT: Same format with Iceland flag icon.  
Body: `"Name: Erik the Red"` `"Reason: also manslaughter"` `"Duration: 3 years"` `"Signed: Althing"`  
Official stamp: `"EXILED (again)"` in red.  
The RIGHT document appears 3s after the left — recognition beat.  
At 10s: A THIRD document template appears but is BLANK except for: `"Destination: TBD. Sailing west."` And Erik's silhouette walking right with a bag.  
`"Sensing a pattern in his reviews."` bottom label, ITALIC GREY.  
**NOTE:** THREE documents. This needs the 14s — it's a comedy-of-escalation.

---

### Scene40 — Erik Sails West | `[TARGET: 5s]` `[WAS: 5.13s]`
**VO:** *(visual pause — "Erik sailed west" already spoken in Scene39)*  
**VISUAL:** Load `erik_route.png` cartopy map. One ship icon animates westward from Iceland → Greenland. Clean, simple, fast.

---

### Scene41 — Greenland Named | `[TARGET: 7s]` `[WAS: 9.93s — TRIM]`
**VO:** *"He found a large island, mostly covered in ice. He named it Greenland."*  
**VISUAL:** Load `erik_route.png` map. Greenland visible. A `"GREENLAND"` label appears on the map in AMBER animated text.  
Underneath: `"(mostly ice)"` in small grey parentheses.  
An ice cap overlay on Greenland (light blue rectangle, semi-transparent) fills most of the island.  
A small `"🤔"` or thought-bubble from the `"GREENLAND"` label: `"green?"` in italic.

---

### Scene42 — The Name Swap Map | `[TARGET: 20s]` `[WAS: 7.87s — MAJOR EXTEND]`
**VO:** *"The Eiríks saga is essentially candid about this: he chose the name specifically to attract settlers. Iceland, the island with the friendly name, has comparatively little ice on its surface. Whereas, Greenland, the island with the aspirational name, is nearly buried under the largest ice sheet in the Northern Hemisphere."*  
**VISUAL:** Load `erik_route.png` map (shows both Iceland and Greenland). TWO-PANEL comparison:  
LEFT PANEL label: `"ICELAND"` with arrow pointing at actual Iceland. Below: `"ice coverage: ~11%"` and a small snow icon.  
RIGHT PANEL label: `"GREENLAND"` with arrow pointing at Greenland. Below: `"ice coverage: ~79%"` and a massive blue glacier covering most of it.  
At 4s: Arrows appear swapping the NAMES between islands — an animated swap. `"ICELAND"` label slides right toward Greenland, `"GREENLAND"` label slides left toward Iceland, then both land on the WRONG island... but stay there.  
At 12s: Source citation: `"— Eiríks saga rauða (it's literally in the text)"` in ITALIC GREY font_size=20, bottom-right.  
At 15s: Big verdict label: `"Real estate has never been the same."` in AMBER BOLD.  
**NOTE:** This is the most complex single graphic in the exploration section. The NAME SWAP animation is the key moment — names sliding and landing on wrong islands is visually satisfying.

---

### Scene43 — Fourteen Ships | `[TARGET: 8.5s]` `[WAS: 8.67s]`
**VO:** *"The naming worked. Fourteen ships of settlers followed him back. Real estate has never been the same."*  
**VISUAL:** Load `erik_route.png` map. Fourteen ship icons animate from Iceland westward toward Greenland — each slightly different size, staggered departure, run_time=4s.  
Counter appears: `"14 ships"` → animates each ship icon appearing. Label: `"The naming worked."` in BOLD AMBER.

---

### Scene44 — Leif Appears | `[TARGET: 5s]` `[WAS: 6.4s]`
**VO:** *"Erik's son Leif did one better."*  
**VISUAL:** Load `leif_eriksson.png` (SD) avatar center, height=3.0u. GrowFromCenter. Label: `"Leif Eriksson"` + `"Erik's son"`. He's pointing west. Short beat.

---

### Scene45 — Leif Sails West | `[TARGET: 19s]` `[WAS: 12.2s — EXTEND]`
**VO:** *"Around the year 1000 — we know from tree-ring evidence that Norse settlers occupied L'Anse aux Meadows in exactly 1021 CE — Leif Eriksson sailed west from Greenland, found an entire continent, established a settlement he called Leifsbuðir, and then went home."*  
**VISUAL:** Load `leif_route.png` cartopy map (shows Greenland + North Atlantic + tip of Newfoundland/North America). A dotted route animates from Greenland → L'Anse aux Meadows, run_time=5s.  
At 5s: Landing marker appears at L'Anse aux Meadows with label: `"Leifsbuðir"` + `"(L'Anse aux Meadows, Newfoundland)"`.  
At 8s: Scientific callout box: `"tree-ring evidence:"` `"exact date: 1021 CE"` `"confirmed by: dendrochronology"` — appearing in a small academic-footnote style box, GREY.  
At 12s: `"1021 CE"` label burns in on the marker in AMBER.  
At 15s: Leif avatar (scale 0.6) appears at the landing site, plants a flag-stick. But then immediately picks up his belongings.  
**NOTE:** The "went home" part is key — visually show him turning around and leaving.

---

### Scene46 — Empty Filing Cabinet | `[TARGET: 6s]` `[WAS: 10.07s — TRIM]`
**VO:** *"Five hundred years before Columbus, Leif found North America,"*  
**VISUAL:** White background. A filing cabinet drawer opens. Inside: completely empty except for one file labeled `"NORTH AMERICA - DISCOVERY PAPERWORK"` — which is blank/empty.  
Label: `"paperwork filed: 0"` in GREY.

---

### Scene47 — Mournful Hold | `[TARGET: 6s]` `[WAS: 8.73s — TRIM]`
**VO:** *"filed no paperwork, and left. History moved on without him."*  
**VISUAL:** A small Leif figure walks off screen RIGHT. The continent shape (simplified North America polygon) sits in the background, empty, labeled `"(no claim filed)"`.  
`"History moved on without him."` fades in center, ITALIC, GREY, font_size=32.

---

## PART SEVEN: SNORRI AND THE PROSE EDDA

---

### Scene48 — Iceland Is Writing | `[TARGET: 11s]` `[WAS: 11.27s]`
**VO:** *"Back in Iceland, something else was happening that would matter far more to the world than a temporary camp in Newfoundland. Iceland was writing."*  
**VISUAL:** Load `iceland_overview.png` map as background. Multiple quill-pen icons appear across Iceland, animated one after another. Each quill "writes" a squiggly line on the map.  
Counter: `"12th – 13th century"` top-left.  
Large centered label builds: `"ICELAND WAS WRITING."` — each word appears separately, BOLD AMBER, font_size=52.

---

### Scene49 — The Saga Mosaic | `[TARGET: 14s]` `[WAS: 9.33s — EXTEND]`
**VO:** *"In the 12th and 13th centuries, Icelanders produced the most sophisticated prose literature of medieval Europe: the family sagas, the histories of Norse kings, and — most consequentially — the mythology."*  
**VISUAL:** White background. A mosaic/grid of manuscript-style tiles appears — each is a small rectangle with faint rune-like squiggles (simulated manuscript). 3×4 grid = 12 tiles.  
Three tiles glow in sequence, highlighted in AMBER, BLUE, RED:  
`"Family Sagas"` (AMBER tile, appears 2s)  
`"Histories of Kings"` (BLUE tile, appears 5s)  
`"The Mythology"` (RED tile, appears 8s) — this last one glows BRIGHTER  
At 11s: `"most consequentially:"` label above the RED tile. `"THE MYTHOLOGY"` subtitle below.

---

### Scene50 — Snorri Introduced | `[TARGET: 7s]` `[WAS: 7.4s]`
**VO:** *"The man who synthesised it all was Snorri Sturluson, born in 1179."*  
**VISUAL:** White background. Load `snorri_writing.png` (SD) avatar center, height=3.2u. GrowFromCenter.  
Label: `"Snorri Sturluson"` BOLD + `"born 1179"` AMBER + `"scholar, historian, politician"` LIGHT.

---

### Scene51 — The Gods Named | `[TARGET: 10s]` `[WAS: 11.2s]`
**VO:** *"His Prose Edda is, quite simply, the reason we know what we know about Norse mythology. Thor, Odin, Loki, Ragnarök —"*  
**VISUAL:** White background. Snorri avatar left side. Right side: Norse deity names appear one by one in large bold text, staggered, falling from top:  
`"THOR"` (RED, font_size=64)  
`"ODIN"` (BLUE, font_size=64)  
`"LOKI"` (DARK, font_size=64)  
`"RAGNARÖK"` (AMBER, font_size=64)  
Each crashes in with GrowFromCenter, 1.2s apart. By scene end: all 4 names fill the right side.

---

### Scene52 — Marvel Banner | `[TARGET: 12s]` `[WAS: 7.73s — EXTEND]`
**VO:** *"the entire cosmology that has since spawned films, comics, and theme park rides — exists in its current form because a 13th-century Icelander wrote it down."*  
**VISUAL:** The 4 god names from Scene51 persist. A timeline appears:  
`"Snorri writes Prose Edda: c.1220 CE"` → arrow → `"Films, comics, theme parks: 2011+"` → arrow → `"Billions of $$"`  
In between the timeline entries: tiny icons (simplified movie camera, comic book, rollercoaster).  
At 8s: Snorri's writing-figure appears bottom-left, quill still in hand, looking confused at the rollercoaster icon.

---

### Scene53 — Gods Acknowledge | `[TARGET: 8s]` `[WAS: 6.93s]`
**VO:** *"Without Snorri, those gods would be as obscure as the gods of the Angles and Saxons. You're welcome, Marvel."*  
**VISUAL:** LEFT side: Thor/Odin/Loki names large and bright.  
RIGHT side: `"Angle Gods?"` and `"Saxon Gods?"` labels — each is a ? mark icon with no name beneath — just blank outlines.  
Comparison line between them: `"Snorri's gods: you know them. Others: you don't."` in BOLD.  
At 5s: Small Snorri figure bottom-right waves nonchalantly at the bright Thor/Odin/Loki text. `"You're welcome, Marvel."` in ITALIC AMBER.

---

### Scene54 — Snorri's Attention Shifts | `[TARGET: 9s]` `[WAS: 9s]`
**VO:** *"Snorri was also a politician. And like most Icelandic politicians of his era, this eventually got him killed."*  
**VISUAL:** Snorri avatar center. He has two labels — LEFT: `"Scholar"` (bright, glowing) RIGHT: `"Politician"` (dark, slightly ominous red glow).  
At 3s: The `"Scholar"` label dims. The `"Politician"` label grows larger, pulsing RED.  
At 6s: A clock appears above — speeds forward. Then STOPS abruptly.  
At 7s: Ominous single text appears: `"1241."` — BOLD RED, center screen.  
`"— VO Part 2 ends —"` production marker.

---

## PART EIGHT: THE STURLUNG AGE

---

### Scene55 — Sturlung Age Opens | `[TARGET: 7s]` `[WAS: 11.67s — TRIM]`
**VO:** *"The Sturlung Age — roughly 1220 to 1262 — was Iceland's civil war."*  
**VISUAL:** Load `iceland_overview.png` map as background at low opacity (0.5). Cold grey rectangle overlay desaturates the map.  
Large text center: `"THE STURLUNG AGE"` in BOLD COLD_GREY font_size=64. Below: `"1220 – 1262"` in SEMIBOLD RED. Below: `"Iceland's civil war."` in BOLD RED.  
**NOTE:** Trim to 7s — the VO says this quickly and bluntly. Match that energy.

---

### Scene56 — Timeline of Violence | `[TARGET: 9s]` `[WAS: 10.87s]`
**VO:** *"The great family clans tore the island apart in a forty-year cycle of raids, assassinations, and revenge killings."*  
**VISUAL:** Dark background. A horizontal timeline bar `"1220"` → `"1262"` in COLD_GREY. On this timeline: 12 red dots appear staggered — each labeled with a small icon (sword/fire/X). They accumulate over 5s.  
The dots don't get slower — they maintain pace, suggesting relentlessness.  
Counter: `"40 years"` label above bar. `"Raids · Assassinations · Revenge"` below bar in small caps.

---

### Scene57 — The Map Fragments | `[TARGET: 7.5s]` `[WAS: 9.07s]`
**VO:** *"Norway's King Hákon IV watched, and waited, and quietly backed different factions in turn."*  
**VISUAL:** Load `iceland_overview.png` map. Map appears to crack/fragment into 4-5 pieces (draw crack lines with `Line`, stroke_width=2, animate `Create`). Each fragment gets a different pale color — different clan regions.  
Off to the right: Load `hakon_iv.png` avatar (SD) at scale 0.7, watching from a distance. Label: `"King Hákon IV"` + `"(watching, waiting)"`.

---

### Scene58 — Hákon Watches | `[TARGET: 7s]` `[WAS: 8.8s]`
**VO:** *"Snorri himself had become a vassal of Hákon, then fallen out of favour."*  
**VISUAL:** Two avatars facing each other. LEFT: Load `hakon_iv.png` at height=2.8u. RIGHT: Load `snorri_writing.png` at height=2.8u, smaller/deferential posture.  
A dotted line connects them labeled `"vassal"` in AMBER.  
At 4s: The line color shifts RED and a `"✗ OUT OF FAVOUR"` stamp appears over Snorri's avatar.  
Snorri's figure dims (opacity 0.5).

---

### Scene59 — Snorri Exposed | `[TARGET: 5s]` `[WAS: 8.67s — TRIM]`
**VO:** *"In September 1241, Hákon ordered him killed."*  
**VISUAL:** Hákon's figure. He raises one hand. An ORDER document appears: `"ORDER TO EXECUTE"` `"Target: Snorri Sturluson"` `"Date: September 1241"` `"Signed: King Hákon IV"`.  
Official seal stamps onto document. Fast, hard, decisive.  
**NOTE:** 5 seconds. Short and brutal. This is a kill order — match the coldness.

---

### Scene60 — The Date | `[TARGET: 9s]` `[WAS: 8.6s]`
**VO:** *"Gissur Þorvaldsson arrived at Snorri's farmhouse at Reykholt with seventy men in the middle of the night."*  
**VISUAL:** Near-black background. Single candle flame (circle + teardrop, AMBER glow). Farmhouse silhouette in background.  
Date stamp burns in: `"September 1241"` — BOLD AMBER, GrowFromCenter, font_size=72. Then dims back.  
At 5s: `"70 men"` appears. `"middle of the night."` below it. Both in cold white, small.  
Shadows lengthen across the scene.

---

### Scene61 — Seventy Men | `[TARGET: 5s]` `[WAS: 11.13s — TRIM]`
**VO:** *"Snorri was found hiding in his cellar."*  
**VISUAL:** Dark background. 70 dot figures appear in the dark — small, menacing, silent. They don't move. The *number* is the visual.  
Counter appears: `"70"` in RED BOLD, large. Below: `"armed men"`.  
Then: single figure (Snorri) shown smaller, alone, in a cellar outline below.  
**NOTE:** Cut to 5s. This scene is about the number 70 vs. one man. Keep it stark.

---

### Scene62 — Gissur's Face | `[TARGET: 5s]` `[WAS: 7.2s]`
**VO:** *"His last recorded words were: Eigi skal höggva."*  
**VISUAL:** Load `gissur_thorvaldsson.png` (SD) avatar, large, near-full screen height, in shadow. His expression: cold, decided.  
No label. No text. Just the face.  
At 3s: Snorri's voice — text appears: `"Eigi skal höggva."` in ITALIC white, font_size=48, bottom of screen.

---

### Scene63 — The Cellar | `[TARGET: 10s]` `[WAS: 10.47s]`
**VO:** *"Do not strike."*  
**VISUAL:** Stone cellar walls (dark grey). Load `snorri_afraid.png` (SD) avatar backed against wall. Torchlight from above. Gissur's shadow visible at top of scene.  
The text `"Eigi skal höggva."` — center screen — in BOLD WHITE, ITALIC, font_size=96. Fills most of the frame.  
Below: `"(Do not strike.)"` in translation, smaller LIGHT ITALIC.  
Below: attribution `"— Snorri's last recorded words"` in tiny GREY.  
This is a full visual hold. The text IS the scene.

---

### Scene64 — Last Words | `[TARGET: 11.5s]` `[WAS: 11.47s]`
**VO:** *(visual hold)*  
**VISUAL:** Near-black. The last words from Scene63 persist:  
`"Eigi skal höggva."` — enormous, white, italic.  
After 4s: it begins to fade. Very slowly. Lasts the entire 11.5s.  
At 9s: as the text fades, a faint outline of Iceland map appears beneath it — just the coastline, barely visible, in pale grey. As if to say: this happened here.

---

### Scene65 — They Struck | `[TARGET: 10.5s]` `[WAS: 10.53s]`
**VO:** *"They struck."*  
**VISUAL:** Pure black for 3s. Complete silence / darkness.  
Then: `"They struck."` in BOLD WHITE, font_size=64, simple FadeIn. Holds 5s.  
Then fades out.  
**NOTE:** Two words. The scene is the pause before and after. Do not add graphics. Do not animate. This is the most important 10s in the episode.

---

## PART NINE: THE COVENANT

---

### Scene66 — After Snorri | `[TARGET: 8s]` `[WAS: 11.93s — TRIM]`
**VO:** *"The Icelandic Commonwealth outlived him by barely twenty years. By 1262, the chieftains were exhausted."*  
**VISUAL:** Timeline bar `"1241"` (Snorri's death) → `"1262"` (covenant). Short bar — barely 20 years.  
`"barely 20 years"` label above. `"exhausted"` label at 1262 end, in COLD_GREY italic.

---

### Scene67 — Exhausted Chieftains | `[TARGET: 11s]` `[WAS: 14.27s — TRIM]`
**VO:** *"The bloodshed had gone on too long, the clans were too broken, and Hákon's Norway was offering peace in exchange for submission."*  
**VISUAL:** Þingvellir background, now muted/desaturated. Only 20 figures (not 36 — fewer now). They are shorter, darker grey, some semi-transparent (ghost versions of dead chieftains).  
Hákon avatar right side, offering something (a scroll/olive branch).  
Label on scroll: `"Peace."` Label below: `"(terms: your sovereignty)"` — in small cold text.

---

### Scene68 — Old Covenant Signed | `[TARGET: 9s]` `[WAS: 11.53s — TRIM]`
**VO:** *"They signed the Old Covenant — the Gamli sáttmáli — and handed themselves to the Norwegian king."*  
**VISUAL:** A scroll/document (`"Gamli sáttmáli"` header, `"The Old Covenant — 1262"`) unfurls in the center.  
Four red wax seals stamp onto it — staggered, each one heavy-sounding (visual weight).  
Norwegian flag rises over Iceland map in background.

---

### Scene69 — Surrender Scoreboard | `[TARGET: 8s]` `[WAS: 12.8s — TRIM]`
**VO:** *"It was not conquest. It was a surrender by choice, which is somehow more Icelandic."*  
**VISUAL:** Dark scoreboard (sports-style). Two columns:  
LEFT: `"Conquered by force"` — `"—"` score in grey.  
RIGHT: `"Chose to submit, own terms"` — `"✓"` score in AMBER.  
At 5s: Small footnote text: `"(presented without comment)"` GREY ITALIC.  
**NOTE:** Trimmed to 8s. Short and deadpan.

---

### Scene70 — Þingvellir Breathing | `[TARGET: 21s]` `[WAS: 21.2s]`
**VO:** *"People who had settled on the edge of the world rather than accept a king had spent three centuries building something extraordinary: a parliament, a legal tradition, a literary culture, and a very specific stubbornness about doing things their own way."*  
**VISUAL:** Load `thingvellir.png` cartopy map as background. Full Þingvellir valley — EMPTY. No people.  
The Law Rock still there, center. Plates slowly pulling apart (6s animation).  
Text builds word by word:  
`"A parliament."` → `"A legal tradition."` → `"A literary culture."` → `"A stubbornness."` — each line in AMBER, fades in every 4s.  
Dusk overlay gradually darkens.

---

### Scene71 — Something Still Alive | `[TARGET: 14s]` `[WAS: 13.67s]`
**VO:** *"They handed it over when the alternative was more of their own neighbours killing each other. What they built in those three centuries didn't disappear. It went underground."*  
**VISUAL:** Near-dark Þingvellir. Empty. Plates still.  
At 4s: A single amber pulse radiates from the Law Rock — `Circle` expanding, opacity fading, like a heartbeat.  
At 8s: Pull-quote: `"What they built didn't disappear."` in BOLD WHITE, center.  
At 11s: `"It went underground."` in ITALIC AMBER, below.  
The pulse repeats once more, faint.

---

## CLOSE: THE LONG VIEW

---

### Scene72 — Rapid Montage | `[TARGET: 14s]` `[WAS: 19.4s — TRIM]`
**VO:** *"The Althing would be abolished, restored, abolished again. Foreign kings would trade Iceland like a ledger item. Plagues would come. Famines would come. Pirates from North Africa would raid the coast."*  
**VISUAL:** Dark background. RAPID SEQUENCE — each beat ~2.5s:  
1. Althing symbol (scales/columns) appears → strikethrough → reappears → strikethrough again  
2. Iceland as a ledger row: `"Iceland . . . . . . . . [price]"` in a bookkeeping register  
3. Skull icon on ship silhouette labeled `"1402 — Black Death"` 
4. Empty shelf (echo of Scene04) — quick  
5. Corsair ship labeled `"1627 — Barbary Pirates"` 
**NOTE:** Trim 5s from current. Fast montage — 5 images × 2.5s each. Keep moving.

---

### Scene73 — Roots Showing | `[TARGET: 13s]` `[WAS: 9.13s — EXTEND]`
**VO:** *"And through all of it, that original instinct — the one that made people sail to the edge of the world in the first place — kept surfacing."*  
**VISUAL:** Three-column visual. DARK BACKGROUND.  
Each column: a modern image (RED/grey) with an ancient echo (AMBER glow) beneath it:  
Column 1: Bank collapse (2008) → AMBER glow: monks sailing to escape (echo)  
Column 2: Ash cloud (2010) → AMBER glow: Ingólfr following pillars (echo)  
Column 3: Modern Iceland outline → AMBER glow: Þingvellir Law Rock (echo)  
The amber echoes literally glow through the modern images. Time collapse visual.  
At 9s: `"that original instinct"` center text in AMBER BOLD.  
`"kept surfacing."` below in ITALIC.

---

### Scene74 — Return to Cold Open | `[TARGET: 9s]` `[WAS: 9.13s]`
**VO:** *"The stubbornness. The pragmatism. The willingness to do something nobody else thought was rational and simply refuse to back down."*  
**VISUAL:** Dark background. Iceland map small on dark North Atlantic (echoes Scene07). Three words appear sequentially in AMBER BOLD:  
`"Stubbornness."` (4s) · `"Pragmatism."` (6s) · `"Backbone."` (8s)  
Each word GrowFromCenter, holds 1s, then the next appears.  
Below the map: three bank buildings from Scene02 — visible again, toppling.

---

### Scene75 — Final Hold | `[TARGET: 13s]` `[WAS: 17.27s — TRIM]`
**VO:** *"October 2008. A tiny island. Eleven times its GDP in collapsing bank assets. The IMF at the door. The foundation for what happened next was laid in 874."*  
**VISUAL:** Iceland outline in AMBER on near-black sea. Glowing. Tectonic plates visible either side, slowly separating.  
Steam rising from the island (CurvedArrow lines, white, slow).  
At 6s: `"874"` appears in AMBER center. Small, then grows.  
At 10s: `"2008"` appears beside it. Two dates, side by side. `"874 ← → 2008"` with a connecting arrow.  
At 12s: Fade to black.

---

### Scene76 — End Card | `[TARGET: 8.5s]` `[WAS: 8.6s]`
**VO:** *(no VO — optional call-to-action voice)*  
**VISUAL:** Clean WHITE background. Center layout:  
`"ICELAND: HOW TO STEAL AN ISLAND"` — series title, BLUE SEMIBOLD font_size=36  
`"Episode 1 of 3"` — AMBER, font_size=24  
Divider line.  
`"Episode 2 →"` in BLUE BOLD font_size=32. `"The Long Dark: Plague, Monopoly & a Man\nWho Ruled Iceland for Two Months"` in LIGHT font_size=22.  
Bottom: Small Iceland outline icon (AMBER) + `"Subscribe"` with a bell icon (simplified).  
All elements in safe zone. Fade in gently, hold 7s.

---

## SUMMARY: REQUIRED DURATION CHANGES

| Scene | Old | New | Change |
|-------|-----|-----|--------|
| Scene05 — Puppet | 5.7s | 15s | **+9.3s** |
| Scene06 — Iceland's Answer | 6.6s | 12s | **+5.4s** |
| Scene10 — Papar Monk | 16.1s | 29s | **+12.9s** |
| Scene13 — First Instinct | 8.5s | 16s | **+7.5s** |
| Scene15 — Harald Fairhair | 6.7s | 15s | **+8.3s** |
| Scene17 — Pillars Overboard | 9.0s | 14s | **+5.0s** |
| Scene21 — Great Migration | 16.7s | 7s | **−9.7s** |
| Scene22 — Where They Came | 7.7s | 13s | **+5.3s** |
| Scene23 — Volcano Choice | 8.1s | 13s | **+4.9s** |
| Scene27 — Tectonic Comedy | 7.8s | 13s | **+5.2s** |
| Scene37 — Compromise | 11.4s | 19s | **+7.6s** |
| Scene39 — Two Exiles | 7.4s | 14s | **+6.6s** |
| Scene42 — Name Swap Map | 7.9s | 20s | **+12.1s** |
| Scene45 — Leif Sails | 12.2s | 19s | **+6.8s** |
| Scene49 — Saga Mosaic | 9.3s | 14s | **+4.7s** |
| Scene52 — Marvel Banner | 7.7s | 12s | **+4.3s** |
| Scene55 — Sturlung Opens | 11.7s | 7s | **−4.7s** |
| Scene59 — Snorri Exposed | 8.7s | 5s | **−3.7s** |
| Scene61 — Seventy Men | 11.1s | 5s | **−6.1s** |
| Scene66 — After Snorri | 11.9s | 8s | **−3.9s** |
| Scene67 — Exhausted Chieftains | 14.3s | 11s | **−3.3s** |
| Scene69 — Scoreboard | 12.8s | 8s | **−4.8s** |
| Scene72 — Montage | 19.4s | 14s | **−5.4s** |
| Scene73 — Roots Showing | 9.1s | 13s | **+3.9s** |
| Scene75 — Final Hold | 17.3s | 13s | **−4.3s** |

**New estimated total: ~800s (13m 20s)**

---

*Document ready for review. Approve → rebuild all scene Python files.*
