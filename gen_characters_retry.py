"""
gen_characters_retry.py
Retry 2 failed + add assassins_group + regenerate snorri_young (distorted face fix).
"""
import requests
import urllib.parse
import time
from pathlib import Path

OUT_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\characters")
BASE_URL = "https://image.pollinations.ai/prompt/{prompt}?width=1024&height=1024&nologo=true&model=flux&enhance=true&seed={seed}"

STYLE_PREFIX = (
    "flat illustrated character portrait, slightly textured illustration style, "
    "Kurzgesagt-adjacent warmth with hand-drawn rougher edges, strong readable silhouette, "
    "full body three-quarter shot, plain white background, "
    "NOT cartoonish, NOT stick figure, period-appropriate costume, "
    "well-proportioned face with correct anatomy, "
)

CHARACTERS = [
    # Regenerate snorri_young — better face quality with enhance=true
    (
        "snorri_young.png", True, 201,
        STYLE_PREFIX +
        "Snorri Sturluson young man age 28-35, medieval Icelandic scholar-chieftain, "
        "well-proportioned oval face, intelligent expressive brown eyes, slight knowing smile, "
        "dark brown medium-length slightly dishevelled hair, "
        "dark green Norse woollen tunic with simple collar embroidery, "
        "holding quill pen upright in right hand, rolled manuscript under left arm, "
        "upright confident posture, warm earth tones, full body illustration"
    ),
    # Retry ingolfr_small
    (
        "ingolfr_small.png", False, 105,
        STYLE_PREFIX +
        "Ingolfr Arnarson simplified icon version for map overlay use, "
        "Norse Viking settler man age 30-40, bearded, fur-lined cloak, "
        "simplified fewer lines same strong silhouette, "
        "designed as small icon immediately recognisable at thumbnail size, "
        "reduced detail level, white background"
    ),
    # Retry puppet_most_countries
    (
        "puppet_most_countries.png", False, 106,
        STYLE_PREFIX +
        "marionette puppet figure on visible strings, generic smiling figure, "
        "plain navy business suit, fixed cheerful smile, "
        "puppet strings attached to head shoulders and hands going upward off frame, "
        "text label on chest reading MOST COUNTRIES, "
        "arms slightly raised ready to comply, "
        "flat illustration humorous not grotesque, white background"
    ),
    # New: assassins group
    (
        "assassins_group.png", False, 107,
        STYLE_PREFIX +
        "group of five medieval Norse armed men advancing together as a unit, "
        "dark grey-brown cloaks and hoods, carrying swords or axes at sides, "
        "faces grim and resolute not cartoonishly evil, "
        "arranged in a tight cluster moving purposefully forward, "
        "dark muted palette to convey menace, "
        "medieval Icelandic 13th century warrior appearance, "
        "strong group silhouette readable as a threatening crowd, "
        "white background"
    ),
]


def generate(filename, force, seed, prompt):
    out_path = OUT_DIR / filename
    if out_path.exists() and not force:
        print(f"  [SKIP] {filename} already exists")
        return True

    encoded = urllib.parse.quote(prompt)
    url = BASE_URL.format(prompt=encoded, seed=seed)
    print(f"  Generating {filename} (seed={seed})...")
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=180)
            r.raise_for_status()
            with open(out_path, "wb") as f:
                f.write(r.content)
            size_kb = out_path.stat().st_size // 1024
            print(f"  [OK]   {filename} ({size_kb} KB)")
            return True
        except Exception as e:
            print(f"  [attempt {attempt+1}/3 failed] {e}")
            time.sleep(3)
    print(f"  [FAIL] {filename} after 3 attempts")
    return False


print(f"Generating/retrying {len(CHARACTERS)} characters...\n")
ok, failed = 0, []

for filename, force, seed, prompt in CHARACTERS:
    if generate(filename, force, seed, prompt):
        ok += 1
    else:
        failed.append(filename)
    time.sleep(2.0)

print(f"\nDone. {ok}/{len(CHARACTERS)} generated.")
if failed:
    print(f"Failed: {failed}")
