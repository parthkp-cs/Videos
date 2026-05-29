"""
gen_characters.py
Generate 6 missing Iceland EP1 characters using Pollinations.ai (flux model).
Same method as fetch_assets.py. Saves PNGs to Output/Iceland/characters/
"""
import requests
import urllib.parse
import time
from pathlib import Path

OUT_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\characters")
OUT_DIR.mkdir(exist_ok=True)

BASE_URL = "https://image.pollinations.ai/prompt/{prompt}?width=1024&height=1024&nologo=true&model=flux&seed={seed}"

STYLE_PREFIX = (
    "flat illustrated character portrait, slightly textured illustration style, "
    "Kurzgesagt-adjacent warmth with hand-drawn rougher edges, strong readable silhouette, "
    "full body three-quarter shot, plain white background, "
    "NOT cartoonish, NOT stick figure, period-appropriate costume, "
)

CHARACTERS = [
    (
        "snorri_young.png", 101,
        STYLE_PREFIX +
        "Snorri Sturluson young man age 25-35, medieval Icelandic chieftain-scholar, "
        "round face intelligent bright eyes slight knowing smile, dark brown medium-length "
        "slightly dishevelled hair, dark green Norse woollen tunic simple embroidery at collar, "
        "holding quill pen upright in right hand, rolled manuscript under left arm, "
        "posture upright confident slightly self-satisfied, warm earth tones, full body"
    ),
    (
        "snorri_older.png", 102,
        STYLE_PREFIX +
        "Snorri Sturluson older man age 55-60, same round face now lined and sunken-eyed, "
        "intelligent but wary and tired expression, grey-streaked dark hair thin on top, "
        "heavier dark cloak over tunic suggesting high status and cold weather, "
        "no quill hands slightly open and tense, look of man who has made political enemies "
        "and cannot escape them, shoulders slightly inward guarded posture, "
        "must look like same character as snorri_young aged 30 years"
    ),
    (
        "hakon.png", 103,
        STYLE_PREFIX +
        "King Hakon IV of Norway age 45-55, tall composed regal Nordic man, "
        "sharp jaw pale calculating eyes, short blond-grey well-groomed hair, "
        "dark navy blue royal cloak trimmed with fur at collar gold clasp at throat, "
        "simple understated gold circlet crown, expression patient calculating completely still, "
        "face of someone who has been waiting a long time and knows he will win, "
        "arms relaxed one hand on armrest, more formal and polished than Icelandic characters, "
        "distinctly Norwegian royalty"
    ),
    (
        "gissur.png", 104,
        STYLE_PREFIX +
        "Gissur Thorvaldsson age 35-45 Icelandic chieftain, medium build dark hair short practical, "
        "dark grey-brown travelling cloak with hood pushed back, "
        "expression NOT villainous — resolute tired doing something necessary but not enjoying it, "
        "instrument not a monster, slight tension around eyes, "
        "purposeful slightly forward-leaning posture, "
        "visually distinct from other chieftains but not caricatured as evil"
    ),
    (
        "ingolfr_small.png", 105,
        STYLE_PREFIX +
        "Ingolfr Arnarson simplified small icon version, same character as full version, "
        "simplified detail fewer lines same silhouette same colours, "
        "Norse Viking settler age 30-40, bearded, fur-lined cloak, "
        "designed to be placed as small icon on map overlay, "
        "immediately recognisable simplified silhouette, transparent or white background, "
        "reduced detail level suitable for thumbnail size display"
    ),
    (
        "puppet_most_countries.png", 106,
        STYLE_PREFIX +
        "marionette puppet on strings representing Most Countries, "
        "generic figure no nationality, plain navy business suit, "
        "big fixed smile slightly blank eyes, "
        "visible marionette strings going upward out of frame attached to head shoulders and hands, "
        "chest label text MOST COUNTRIES in clean sans-serif font, "
        "arms slightly out ready to comply, "
        "flat illustration slightly humorous not grotesque, "
        "cheerfully compliant puppet visual joke, white background"
    ),
]


def generate(filename, seed, prompt):
    out_path = OUT_DIR / filename
    if out_path.exists():
        print(f"  [SKIP] {filename} already exists")
        return True

    encoded = urllib.parse.quote(prompt)
    url = BASE_URL.format(prompt=encoded, seed=seed)
    print(f"  Generating {filename}...")
    try:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(r.content)
        size_kb = out_path.stat().st_size // 1024
        print(f"  [OK]   {filename} ({size_kb} KB)")
        return True
    except Exception as e:
        print(f"  [FAIL] {filename}: {e}")
        return False


print(f"Generating {len(CHARACTERS)} characters to {OUT_DIR}\n")
ok, failed = 0, []

for filename, seed, prompt in CHARACTERS:
    if generate(filename, seed, prompt):
        ok += 1
    else:
        failed.append(filename)
    time.sleep(1.0)

print(f"\nDone. {ok}/{len(CHARACTERS)} generated.")
if failed:
    print(f"Failed: {failed}")
