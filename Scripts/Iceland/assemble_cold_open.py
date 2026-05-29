"""
assemble_cold_open.py  — v3 (Whisper-driven shot list)
Assembles Iceland EP1 Cold Open from cold_open_shots.json

Usage:
  python assemble_cold_open.py              # build changed shots, stitch
  python assemble_cold_open.py --force      # re-render all
  python assemble_cold_open.py --stitch     # stitch only (use cache)
  python assemble_cold_open.py --shot s12_jailed  # re-render one shot
"""

import os, sys, argparse, subprocess, hashlib, json
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from moviepy import VideoFileClip, ImageSequenceClip, AudioFileClip, CompositeAudioClip
from moviepy.audio.fx import AudioLoop, MultiplyVolume

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT      = Path(r'C:/Users/parth.pandya/Projects/YouTube')
ASSETS    = ROOT / 'Alternative Approach/Iceland EP 1'
AUDIO_DIR = ROOT / 'Output/Iceland/Needed Final Files/audio'
PIANO     = AUDIO_DIR / 'piano_bg.mp3'
VO_PART1  = AUDIO_DIR / 'Iceland Ep1 VO Part 1.mp3'
CACHE     = ROOT / 'Scripts/Iceland/scene_cache'
OUT_FILE  = ASSETS / 'cold_open.mp4'
SHOTS_F   = ROOT / 'Scripts/Iceland/cold_open_shots.json'
MANIFEST_F= ROOT / 'Scripts/Iceland/asset_manifest.json'
HASH_F    = CACHE / 'hashes_v3.json'
CACHE.mkdir(exist_ok=True)

FPS = 24
W, H = 1920, 1080
VO_OFFSET     = 3.0    # flag plays first, then VO starts
COLD_OPEN_END = 58.5   # seconds into Part 1 where cold open ends

# ── Args ──────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument('--force',  action='store_true')
parser.add_argument('--stitch', action='store_true')
parser.add_argument('--shot',   type=str, default=None)
args = parser.parse_args()

shots    = json.loads(SHOTS_F.read_text())
manifest = json.loads(MANIFEST_F.read_text())

# ── Fonts ─────────────────────────────────────────────────────────────────────
FONT_PATHS = [
    r'C:/Windows/Fonts/georgiab.ttf', r'C:/Windows/Fonts/georgia.ttf',
    r'C:/Windows/Fonts/arialbd.ttf',  r'C:/Windows/Fonts/arial.ttf',
]
def get_font(size):
    for fp in FONT_PATHS:
        if os.path.exists(fp): return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

# ── Helpers ───────────────────────────────────────────────────────────────────
def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def fit_frame(img):
    """Crop + resize PIL image to 1920x1080."""
    iw, ih = img.size
    if iw / ih > W / H:
        nw = int(ih * W / H)
        img = img.crop(((iw-nw)//2, 0, (iw-nw)//2+nw, ih))
    else:
        nh = int(iw * H / W)
        img = img.crop((0, (ih-nh)//2, iw, (ih-nh)//2+nh))
    return img.resize((W, H), Image.LANCZOS)

def add_text_overlay(frames, text, style, color_hex='#FFFFFF'):
    """Burn text overlay onto every frame."""
    color = hex_to_rgb(color_hex)
    lines = text.split('\n')

    if style == 'center_large':
        font = get_font(88)
        y_base = H // 2 - 50
        bg_alpha = 180
    elif style == 'stat_slam':
        font = get_font(120)
        y_base = H // 2 - 60
        bg_alpha = 200
    elif style == 'impact':
        font = get_font(96)
        y_base = H // 2 - 60
        bg_alpha = 210
    else:
        font = get_font(72)
        y_base = H - 160
        bg_alpha = 160

    result = []
    n = len(frames)
    for i, frame in enumerate(frames):
        # Fade in over first 20% of shot
        t = i / max(n-1, 1)
        alpha = int(255 * min(1.0, t / 0.2)) if style != 'stat_slam' else 255

        img = Image.fromarray(frame).convert('RGBA')
        ov  = Image.new('RGBA', img.size, (0,0,0,0))
        d   = ImageDraw.Draw(ov)

        total_h = sum(d.textbbox((0,0), l, font=font)[3] - d.textbbox((0,0), l, font=font)[1] + 12 for l in lines)
        y = y_base - total_h // 2

        for line in lines:
            bb = d.textbbox((0,0), line, font=font)
            tw, th = bb[2]-bb[0], bb[3]-bb[1]
            tx = (W - tw) // 2
            pad = 20
            d.rectangle([tx-pad, y-pad//2, tx+tw+pad, y+th+pad//2], fill=(0,0,0,min(bg_alpha, alpha)))
            d.text((tx+3, y+3), line, font=font, fill=(0,0,0,alpha))
            d.text((tx, y),     line, font=font, fill=(*color, alpha))
            y += th + 12

        result.append(np.array(Image.alpha_composite(img, ov).convert('RGB')))
    return result

# ── Text card builder ─────────────────────────────────────────────────────────
def build_text_card(shot):
    """Build a punchy text card (bank names, etc.)"""
    text    = shot['text']
    style   = shot.get('style', 'bank_name')
    dur     = shot['vo_end'] - shot['vo_start']
    n       = max(int(dur * FPS), 1)

    if style == 'bank_name':
        bg_color = (8, 12, 28)      # deep navy
        font = get_font(140)
        accent = (220, 60, 60)      # red
    else:
        bg_color = (5, 5, 5)
        font = get_font(100)
        accent = (255, 255, 255)

    frames = []
    for i in range(n):
        t = i / max(n-1, 1)
        # Slam in: scale from 1.15 → 1.0 over first 25%
        scale_t = max(0.0, 1.0 - t / 0.25) if t < 0.25 else 0.0
        scale   = 1.0 + scale_t * 0.15

        img = Image.new('RGB', (W, H), bg_color)
        ov  = Image.new('RGBA', img.size, (0,0,0,0))
        d   = ImageDraw.Draw(ov)

        # Alpha: instant on, fade out last 15%
        alpha = 255 if t < 0.85 else int(255 * (1.0 - t) / 0.15)

        bb = d.textbbox((0,0), text, font=font)
        tw, th = bb[2]-bb[0], bb[3]-bb[1]

        # Scale effect
        scaled_font = get_font(int(140 * scale)) if style == 'bank_name' else get_font(int(100 * scale))
        bb2 = d.textbbox((0,0), text, font=scaled_font)
        tw2, th2 = bb2[2]-bb2[0], bb2[3]-bb2[1]
        tx, ty = (W-tw2)//2, (H-th2)//2

        # Accent underline
        line_y = ty + th2 + 18
        d.rectangle([tx, line_y, tx+tw2, line_y+4], fill=(*accent, alpha))
        # Shadow
        d.text((tx+4, ty+4), text, font=scaled_font, fill=(0,0,0,alpha))
        d.text((tx, ty),     text, font=scaled_font, fill=(*accent, alpha))

        final = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
        frames.append(np.array(final))

    return ImageSequenceClip(frames, fps=FPS)

# ── 874 AD title card ─────────────────────────────────────────────────────────
def build_874_card(dur):
    n = max(int(dur * FPS), 1)
    amber, dark = (212, 130, 26), (10, 10, 10)
    f874, fsub = get_font(160), get_font(48)
    frames = []
    for i in range(n):
        t = i / max(n-1, 1)
        alpha = int(255 * min(1.0, t / 0.35))
        img = Image.new('RGB', (W, H), dark).convert('RGBA')
        ov  = Image.new('RGBA', (W, H), (0,0,0,0))
        d   = ImageDraw.Draw(ov)
        bb  = d.textbbox((0,0), '874', font=f874)
        tw, th = bb[2]-bb[0], bb[3]-bb[1]
        tx, ty = (W-tw)//2, (H-th)//2 - 20
        d.text((tx+4, ty+4), '874', font=f874, fill=(0,0,0,alpha))
        d.text((tx, ty),     '874', font=f874, fill=(*amber, alpha))
        bb2 = d.textbbox((0,0), 'AD', font=fsub)
        d.text(((W-(bb2[2]-bb2[0]))//2, ty+th+12), 'AD', font=fsub, fill=(200,180,140,alpha))
        frames.append(np.array(Image.alpha_composite(img, ov).convert('RGB')))
    return ImageSequenceClip(frames, fps=FPS)

# ── Stock video shot builder ───────────────────────────────────────────────────
def build_stock_shot(shot, asset_path):
    dur = shot.get('duration') or (shot['vo_end'] - shot['vo_start'])
    dur = max(dur, 2.0)

    clip = VideoFileClip(str(asset_path))
    # Loop if clip is shorter than needed
    if clip.duration < dur:
        from moviepy import concatenate_videoclips as ccv
        repeats = int(np.ceil(dur / clip.duration))
        clip = ccv([clip] * repeats)
    clip = clip.subclipped(0, dur).resized((W, H))

    # Apply text overlay if specified
    overlay = shot.get('text_overlay')
    if overlay:
        frames = [np.array(clip.get_frame(i / FPS)) for i in range(int(dur * FPS))]
        frames = add_text_overlay(frames, overlay['text'], overlay['style'], overlay.get('color', '#FFFFFF'))
        clip.close()
        return ImageSequenceClip(frames, fps=FPS)

    return clip

# ── Cache helpers ─────────────────────────────────────────────────────────────
def file_hash(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''): h.update(chunk)
    return h.hexdigest()

def shot_hash(shot):
    asset = manifest.get(shot['id'])
    base = json.dumps({k: v for k, v in shot.items() if k != 'note'}, sort_keys=True)
    if asset and Path(asset).exists():
        base += file_hash(asset)
    return hashlib.md5(base.encode()).hexdigest()

stored_hashes = json.loads(HASH_F.read_text()) if HASH_F.exists() else {}
new_hashes = {}

def export_shot(clip, sid):
    out = CACHE / f'{sid}.mp4'
    clip.write_videofile(str(out), fps=FPS, codec='libx264', audio_codec=None,
        preset='fast', logger=None,
        ffmpeg_params=['-crf', '18', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0'])
    return out

# ── Render loop ───────────────────────────────────────────────────────────────
if not args.stitch:
    for shot in shots:
        sid   = shot['id']
        stype = shot['type']
        h     = shot_hash(shot)
        new_hashes[sid] = h
        cache_mp4 = CACHE / f'{sid}.mp4'

        force_this = args.force or (args.shot == sid)
        cache_hit  = cache_mp4.exists() and stored_hashes.get(sid) == h

        if not force_this and cache_hit:
            print(f'{sid}: cached')
            continue

        reason = 'forced' if force_this else ('changed' if cache_mp4.exists() else 'new')
        print(f'{sid} [{stype}]: rendering ({reason})...')

        if stype == 'text_card':
            clip = build_text_card(shot)
        elif stype == 'title_card':
            clip = build_874_card(shot['vo_end'] - shot['vo_start'])
        elif stype == 'stock_video':
            asset = manifest.get(sid)
            if not asset:
                print(f'  WARNING: no asset for {sid}, skipping')
                continue
            clip = build_stock_shot(shot, asset)
        else:
            continue

        export_shot(clip, sid)
        if hasattr(clip, 'close'): clip.close()
        print(f'  Done.')

    stored_hashes.update(new_hashes)
    HASH_F.write_text(json.dumps(stored_hashes, indent=2))
else:
    print('--stitch: using cached shots.')

# ── Stitch ────────────────────────────────────────────────────────────────────
print('\nStitching...')
concat_list = CACHE / 'concat_v3.txt'
with open(concat_list, 'w') as f:
    for shot in shots:
        mp4 = CACHE / f'{shot["id"]}.mp4'
        if mp4.exists():
            f.write(f"file '{mp4.as_posix()}'\n")
        else:
            print(f'  WARNING: missing cache for {shot["id"]}')

silent_mp4 = CACHE / 'cold_open_v3_silent.mp4'
subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0',
    '-i', str(concat_list), '-c', 'copy', str(silent_mp4)], check=True)

# ── Audio mix ─────────────────────────────────────────────────────────────────
print('Mixing audio...')
total_dur = sum(
    shot.get('duration') or (shot['vo_end'] - shot['vo_start'])
    for shot in shots
)
print(f'Total video duration: {total_dur:.1f}s')

vo    = AudioFileClip(str(VO_PART1)).subclipped(0, COLD_OPEN_END).with_start(VO_OFFSET)
piano = AudioFileClip(str(PIANO)).with_effects([AudioLoop(duration=total_dur), MultiplyVolume(0.05)])
audio = CompositeAudioClip([vo, piano])
audio_out = CACHE / 'cold_open_v3_audio.mp3'
audio.write_audiofile(str(audio_out), fps=44100, codec='libmp3lame', logger=None)

# ── Mux + loudnorm to -14 LUFS (YouTube standard) ────────────────────────────
print(f'Muxing + normalising to -14 LUFS...')
# Two-pass loudnorm: pass 1 measures, pass 2 applies precisely
pass1 = subprocess.run([
    'ffmpeg', '-y',
    '-i', str(silent_mp4), '-i', str(audio_out),
    '-filter_complex', '[1:a]loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json[aout]',
    '-map', '0:v:0', '-map', '[aout]',
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
    '-movflags', '+faststart',
    str(OUT_FILE)
], capture_output=True, text=True)

if pass1.returncode != 0:
    print('loudnorm failed, falling back to direct mux')
    print(pass1.stderr[-500:])
    subprocess.run(['ffmpeg', '-y',
        '-i', str(silent_mp4), '-i', str(audio_out),
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
        '-map', '0:v:0', '-map', '1:a:0',
        '-movflags', '+faststart',
        str(OUT_FILE)], check=True)

print(f'\nDone. Output: {OUT_FILE}')
