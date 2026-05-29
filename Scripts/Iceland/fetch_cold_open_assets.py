"""
fetch_cold_open_assets.py
Fetches stock videos for each shot in cold_open_shots.json.
Sources: Pexels (primary) → Coverr (fallback for cinematic/aerial)
Output: Alternative Approach/Iceland EP 1/assets/
"""

import os, json, requests, time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(r'C:/Users/parth.pandya/Projects/.keys/.env')

PEXELS_KEY = os.getenv('PEXELS_API_KEY')
COVERR_KEY = os.getenv('COVERR_API_KEY')

SHOTS_FILE = Path(r'C:/Users/parth.pandya/Projects/YouTube/Scripts/Iceland/cold_open_shots.json')
ASSETS_DIR = Path(r'C:/Users/parth.pandya/Projects/YouTube/Alternative Approach/Iceland EP 1/assets')
ASSETS_DIR.mkdir(exist_ok=True)

shots = json.loads(SHOTS_FILE.read_text())

# ── Pexels video search ───────────────────────────────────────────────────────
def search_pexels_video(query, per_page=5):
    r = requests.get('https://api.pexels.com/videos/search',
        headers={'Authorization': PEXELS_KEY},
        params={'query': query, 'per_page': per_page, 'orientation': 'landscape', 'size': 'large'})
    if r.status_code != 200:
        return []
    results = []
    for v in r.json().get('videos', []):
        # Prefer 1080p
        files = [f for f in v['video_files'] if f['width'] == 1920 and f['height'] == 1080]
        if not files:
            files = sorted([f for f in v['video_files'] if f['width'] >= 1280], key=lambda x: -x['width'])
        if files:
            results.append({
                'id': v['id'],
                'title': v.get('url', ''),
                'duration': v['duration'],
                'url': files[0]['link'],
                'width': files[0]['width'],
                'height': files[0]['height'],
                'source': 'pexels'
            })
    return results

# ── Coverr video search ───────────────────────────────────────────────────────
def search_coverr(query, per_page=5):
    r = requests.get('https://api.coverr.co/videos',
        headers={'Authorization': f'Bearer {COVERR_KEY}'},
        params={'query': query, 'page': 1, 'per_page': per_page})
    if r.status_code != 200:
        return []
    results = []
    for v in r.json().get('hits', []):
        if v.get('is_premium'):
            continue
        # Fetch full video details to get download URL
        detail = requests.get(f"https://api.coverr.co/videos/{v['id']}",
            headers={'Authorization': f'Bearer {COVERR_KEY}'}).json()
        renditions = detail.get('default_variant', {}).get('renditions', [])
        # Pick 1080p free
        url_1080 = next((r['url'] for r in renditions if r['height'] == 1080 and not r.get('is_plus')), None)
        url_720  = next((r['url'] for r in renditions if r['height'] == 720  and not r.get('is_plus')), None)
        url = url_1080 or url_720
        if url:
            results.append({
                'id': v['id'],
                'title': v.get('title', ''),
                'duration': float(v.get('duration', 0)),
                'url': url,
                'width': 1920 if url_1080 else 1280,
                'height': 1080 if url_1080 else 720,
                'source': 'coverr'
            })
        time.sleep(0.2)  # be polite to Coverr API
    return results

# ── Download a video ──────────────────────────────────────────────────────────
def download(url, out_path, source):
    headers = {}
    if source == 'pexels':
        headers['Authorization'] = PEXELS_KEY
    r = requests.get(url, stream=True, headers=headers, timeout=60)
    r.raise_for_status()
    with open(out_path, 'wb') as f:
        for chunk in r.iter_content(65536):
            f.write(chunk)

# ── Main fetch loop ───────────────────────────────────────────────────────────
manifest = {}  # shot_id -> local file path

for shot in shots:
    sid = shot['id']

    # Skip shots that don't need fetching
    if shot['type'] in ('text_card', 'title_card'):
        print(f'{sid}: text/title card — no fetch needed')
        manifest[sid] = None
        continue

    # Already have this asset
    if 'asset' in shot:
        existing = Path(r'C:/Users/parth.pandya/Projects/YouTube/Alternative Approach/Iceland EP 1') / shot['asset']
        if existing.exists():
            print(f'{sid}: using existing {shot["asset"]}')
            manifest[sid] = str(existing)
            continue

    query = shot.get('query', '')
    sources = shot.get('sources', ['pexels_video', 'coverr'])
    out_file = ASSETS_DIR / f'{sid}.mp4'

    if out_file.exists():
        print(f'{sid}: already downloaded')
        manifest[sid] = str(out_file)
        continue

    print(f'\n{sid}: searching for "{query}"...')
    candidates = []

    for src in sources:
        if src == 'pexels_video' and not candidates:
            results = search_pexels_video(query)
            if results:
                print(f'  Pexels: {len(results)} results')
                for r in results[:3]:
                    print(f'    [{r["source"]}] {r["duration"]}s {r["width"]}x{r["height"]} {r["url"][:60]}')
                candidates = results
        elif src == 'coverr' and not candidates:
            results = search_coverr(query)
            if results:
                print(f'  Coverr: {len(results)} results')
                for r in results[:3]:
                    print(f'    [{r["source"]}] {r["duration"]}s {r["width"]}x{r["height"]} {r["title"]}')
                candidates = results
        time.sleep(0.3)

    if not candidates:
        print(f'  WARNING: no results found for "{query}"')
        manifest[sid] = None
        continue

    # Pick best: prefer duration >= needed shot duration, then longest
    needed = (shot.get('vo_end', 0) or 0) - (shot.get('vo_start', 0) or 0)
    needed = max(needed, 3.0)
    best = next((c for c in candidates if c['duration'] >= needed), candidates[0])

    print(f'  Downloading: {best["source"]} | {best["duration"]}s | {best["width"]}x{best["height"]}')
    download(best['url'], out_file, best['source'])
    size_mb = out_file.stat().st_size // (1024*1024)
    print(f'  Saved: {out_file.name} ({size_mb}MB)')
    manifest[sid] = str(out_file)
    time.sleep(0.5)

# Save manifest
manifest_file = Path(r'C:/Users/parth.pandya/Projects/YouTube/Scripts/Iceland/asset_manifest.json')
manifest_file.write_text(json.dumps(manifest, indent=2))
print(f'\nManifest saved: {manifest_file}')
print('Done.')
