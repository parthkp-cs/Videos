"""
gen_scene_backgrounds.py
Generate photographic-style background images for Iceland EP1 cold-open scenes.
Saves to Output/Iceland/backgrounds/
"""
import requests
import urllib.parse
import time
from pathlib import Path

OUT_DIR = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\backgrounds")
OUT_DIR.mkdir(exist_ok=True)

BASE_URL = "https://image.pollinations.ai/prompt/{prompt}?width=1920&height=1080&nologo=true&model=flux&enhance=true&seed={seed}"

IMAGES = [
    (
        "iceland_landscape_title.png", True, 301,
        "dramatic Icelandic landscape wide cinematic shot, "
        "black volcanic sand beach in foreground with dark grey basalt rocks, "
        "powerful steam rising from geothermal hot springs mid-ground, "
        "dark turbulent sky with faint aurora borealis greens and blues on the horizon, "
        "distant snow-capped volcanic mountains, "
        "cold deep blue-black ocean on the left, "
        "high contrast cinematic documentary atmosphere, very dark moody lighting, "
        "no people, no text, no logos, "
        "photorealistic illustration style, 16:9 widescreen, epic scale"
    ),
    (
        "financial_crash_2008.png", True, 302,
        "global financial crisis 2008 illustration, "
        "dark dramatic scene of financial district at night, "
        "glass skyscrapers reflecting red and orange stock ticker numbers, "
        "trading floor screens filled with plummeting red graphs and falling percentage numbers, "
        "newspapers with BANK COLLAPSE headlines scattered on ground, "
        "dark stormy sky over city skyline, "
        "red and charcoal color palette, deep shadows, dramatic underlit atmosphere, "
        "cinematic documentary illustration, high contrast, "
        "no specific brand logos, no people faces, no text except generic numbers on screens, "
        "16:9 widescreen cinematic composition"
    ),
    (
        "stock_market_crash.png", True, 303,
        "stock market crash data visualization scene, "
        "multiple large trading screens showing violently plummeting red line charts, "
        "currency exchange boards with ISK Icelandic Krona and USD EUR values, "
        "massive red downward arrows overlaid on charts, "
        "stock tickers scrolling with negative percentages, "
        "dark room atmosphere lit only by screen glow, "
        "trading terminal aesthetic, financial data everywhere, "
        "deep red and black color palette, high drama, "
        "cinematic illustration style, 16:9 widescreen, "
        "no faces or people visible, numbers and charts dominate the frame"
    ),
    (
        "empty_supermarket.png", True, 304,
        "empty supermarket shelves interior, "
        "long aisle with bare wooden shelves stripped of all products, "
        "a few scattered empty packages and price tags on floor, "
        "harsh fluorescent lighting overhead casting cold white light, "
        "slightly blurred background suggesting a large store, "
        "atmosphere of scarcity and crisis, "
        "desaturated muted color palette, shadows under shelves, "
        "photorealistic illustration, documentary style, "
        "no people, no text visible, 16:9 widescreen"
    ),
    (
        "iceland_flag_landscape.png", True, 305,
        "Iceland flag waving dramatically against a stormy dark sky, "
        "the blue white and red Nordic cross flag in full glory, "
        "flag billowing in strong wind, fabric folds and movement, "
        "dark grey storm clouds behind the flag, "
        "flag pole visible at left edge, "
        "below the flag glimpse of volcanic Icelandic landscape, "
        "cinematic lighting, dramatic atmosphere, "
        "high contrast, photorealistic illustration style, "
        "no text, 16:9 widescreen"
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
    print(f"  [FAIL] {filename}")
    return False


print(f"Generating {len(IMAGES)} background images -> {OUT_DIR}\n")
ok, failed = 0, []
for filename, force, seed, prompt in IMAGES:
    if generate(filename, force, seed, prompt):
        ok += 1
    else:
        failed.append(filename)
    time.sleep(2.0)

print(f"\nDone. {ok}/{len(IMAGES)} generated.")
if failed:
    print(f"Failed: {failed}")
