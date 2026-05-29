"""
fetch_assets.py
Downloads all images and stock videos for Iceland EP1 Cold Open (Scenes 1-8)
Sources: Pexels (photos + videos) + Pollinations.ai (AI-generated specifics)
Output: C:/Users/parth.pandya/Projects/YouTube/Alternative Approach/Iceland EP 1/
"""

import os
import requests
import time
import urllib.parse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(r'C:/Users/parth.pandya/Projects/.keys/.env')

PEXELS_KEY = os.getenv('PEXELS_API_KEY')
OUT_DIR = Path(r'C:/Users/parth.pandya/Projects/YouTube/Alternative Approach/Iceland EP 1')
OUT_DIR.mkdir(parents=True, exist_ok=True)

PEXELS_PHOTO_URL = 'https://api.pexels.com/v1/search'
PEXELS_VIDEO_URL = 'https://api.pexels.com/videos/search'
HEADERS = {'Authorization': PEXELS_KEY}

# ── Asset manifest ────────────────────────────────────────────────────────────
# Each entry: (filename, type, query_or_prompt)
# type: 'pexels_video' | 'pexels_photo' | 'pollinations'

ASSETS = [
    # Scene 1 -- Iceland cover, banking crisis begins
    ('scene_01a_iceland_aerial.mp4',     'pexels_video', 'Iceland aerial coastline dramatic'),
    ('scene_01b_iceland_map.jpg',        'pollinations', 'Top-down satellite map of Iceland island surrounded by dark North Atlantic ocean, minimal cinematic style, cold blue tones, island clearly visible, dramatic lighting from above'),

    # Scene 2 -- Three banks collapsing (real bank exterior photos + name overlay later)
    ('scene_02a_kaupthing.jpg',          'pexels_photo', 'modern bank building glass exterior corporate'),
    ('scene_02b_landsbanki.jpg',         'pexels_photo', 'financial institution building exterior urban'),
    ('scene_02c_glitnir.jpg',            'pexels_photo', 'contemporary office tower glass facade city'),

    # Scene 3 -- Currency and stock market crash
    ('scene_03a_krona_currency.jpg',     'pexels_photo', 'euro currency banknotes close up money'),
    ('scene_03b_stock_crash.jpg',        'pexels_photo', 'stock market crash red falling chart financial crisis'),
    ('scene_03c_trading_screen.jpg',     'pexels_photo', 'stock exchange trading screen red numbers panic'),

    # Scene 4 -- Empty grocery store
    ('scene_04a_empty_store.jpg',        'pollinations', 'Photorealistic image of a blonde Caucasian woman in her 30s standing in a grocery store aisle with nearly empty shelves, looking worried and confused, fluorescent lighting, realistic documentary photography style'),
    ('scene_04b_empty_shelf.jpg',        'pollinations', 'Close-up photorealistic image of empty grocery store shelves with only one or two items remaining, harsh fluorescent overhead lighting, sense of scarcity and crisis'),

    # Scene 5 -- People on streets, IMF pressure
    ('scene_05a_people_street.jpg',      'pexels_photo', 'people walking city street winter overcast worried crowd'),
    ('scene_05b_government_building.jpg','pexels_photo', 'government building exterior official architecture'),
    ('scene_05c_press_conference.jpg',   'pexels_photo', 'politicians press conference podium microphones signing'),

    # Scene 6 -- Iceland jails bankers
    ('scene_06a_prison_door.jpg',        'pexels_photo', 'prison cell door metal bars close up'),
    ('scene_06b_iceland_flag.jpg',       'pexels_photo', 'Iceland flag waving blue sky'),

    # Scene 7 -- Time rewind, zoom out on Iceland
    ('scene_07a_iceland_above.jpg',      'pexels_photo', 'Iceland landscape aerial view volcanic island ocean'),

    # Scene 8 -- 874 AD title card (programmatic, no image needed -- skipped here)
]


def download_pexels_photo(query, out_path):
    r = requests.get(PEXELS_PHOTO_URL, headers=HEADERS, params={
        'query': query, 'per_page': 1, 'orientation': 'landscape', 'size': 'large'
    })
    r.raise_for_status()
    photos = r.json().get('photos', [])
    if not photos:
        print(f'  [WARN] No Pexels photo found for: {query}')
        return False
    url = photos[0]['src']['large2x']
    img_data = requests.get(url).content
    with open(out_path, 'wb') as f:
        f.write(img_data)
    return True


def download_pexels_video(query, out_path):
    r = requests.get(PEXELS_VIDEO_URL, headers=HEADERS, params={
        'query': query, 'per_page': 3, 'orientation': 'landscape'
    })
    r.raise_for_status()
    videos = r.json().get('videos', [])
    if not videos:
        print(f'  [WARN] No Pexels video found for: {query}')
        return False
    # Pick best quality video file (prefer HD)
    video = videos[0]
    files = sorted(video['video_files'], key=lambda x: x.get('width', 0), reverse=True)
    # Pick highest resolution that is <= 1920 wide
    chosen = next((f for f in files if f.get('width', 0) <= 1920), files[0])
    vid_data = requests.get(chosen['link'], stream=True)
    with open(out_path, 'wb') as f:
        for chunk in vid_data.iter_content(chunk_size=8192):
            f.write(chunk)
    return True


def download_pollinations(prompt, out_path):
    encoded = urllib.parse.quote(prompt)
    url = f'https://image.pollinations.ai/prompt/{encoded}?width=1920&height=1080&nologo=true&model=flux'
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    with open(out_path, 'wb') as f:
        f.write(r.content)
    return True


# ── Main ──────────────────────────────────────────────────────────────────────
print(f'Output folder: {OUT_DIR}')
print(f'Assets to fetch: {len(ASSETS)}\n')

success, failed = 0, []

for filename, asset_type, query in ASSETS:
    out_path = OUT_DIR / filename
    if out_path.exists():
        print(f'  [SKIP] {filename} already exists')
        success += 1
        continue

    print(f'  Fetching {filename} ({asset_type})...')
    try:
        if asset_type == 'pexels_photo':
            ok = download_pexels_photo(query, out_path)
        elif asset_type == 'pexels_video':
            ok = download_pexels_video(query, out_path)
        elif asset_type == 'pollinations':
            ok = download_pollinations(query, out_path)
        else:
            ok = False

        if ok:
            size_kb = out_path.stat().st_size // 1024
            print(f'  [OK]   {filename} ({size_kb} KB)')
            success += 1
        else:
            failed.append(filename)

    except Exception as e:
        print(f'  [FAIL] {filename}: {e}')
        failed.append(filename)

    time.sleep(0.5)  # be polite to APIs

print(f'\nDone. {success}/{len(ASSETS)} fetched.')
if failed:
    print(f'Failed: {failed}')
