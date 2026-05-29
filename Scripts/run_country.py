#!/opt/homebrew/bin/python3.12
"""
History Channel — Country Video Generator
==========================================
Usage:
    python3 run_country.py "Finland"
    python3 run_country.py "Japan" --skip-docs
    python3 run_country.py "Finland" --steps research,audio_script

Outputs (saved to Output/{Country}/):
    research.md
    audio_script.md
    production_script.md
    characters.md
    scene_breakdown.md

Optionally uploads audio_script.md to the project Google Doc.
"""

import os
import sys
import re
import argparse
import anthropic
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
import warnings
warnings.filterwarnings("ignore")

# ── Config ────────────────────────────────────────────────────────────────────

BASE_DIR      = Path(__file__).parent.parent
AGENTS_DIR    = BASE_DIR / "Agents"
PROMPTS_DIR   = AGENTS_DIR / "prompts"
OUTPUT_DIR    = BASE_DIR / "Output"

SA_FILE       = Path("/Users/dishastark/Claude Projects/dp-drive-497206-c9107abb48b6.json")
GOOGLE_DOC_ID = "1gG4r13LquXtl0VmfD1l3EDm-wrpurbIOs4Bm1KfgQy0"
SCOPES        = ["https://www.googleapis.com/auth/documents"]

MODEL         = "claude-opus-4-5"

STEPS = [
    ("research",           "01_research.md",          "research.md"),
    ("audio_script",       "02_audio_script.md",       "audio_script.md"),
    ("production_script",  "03_production_script.md",  "production_script.md"),
    ("characters",         "04_characters.md",         "characters.md"),
    ("scene_breakdown",    "05_scene_breakdown.md",    "scene_breakdown.md"),
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_prompt(filename: str, country: str) -> str:
    path = PROMPTS_DIR / filename
    text = path.read_text()
    return text.replace("{COUNTRY}", country)


def load_context(country: str, output_dir: Path, steps_done: list[str]) -> str:
    """Build context string from previously generated outputs."""
    context_parts = []

    # Always include series concept and style guide
    for md in ["series_concept.md", "style_guide.md"]:
        p = AGENTS_DIR / md
        if p.exists():
            context_parts.append(f"## {md}\n\n{p.read_text()}")

    # Include already-generated outputs for this country
    labels = {
        "research":          "research.md",
        "audio_script":      "audio_script.md",
        "production_script": "production_script.md",
        "characters":        "characters.md",
    }
    for step in steps_done:
        if step in labels:
            p = output_dir / labels[step]
            if p.exists():
                context_parts.append(f"## Previously generated: {labels[step]}\n\n{p.read_text()}")

    return "\n\n---\n\n".join(context_parts)


def run_agent(client: anthropic.Anthropic, step_name: str, prompt_file: str,
              country: str, output_dir: Path, steps_done: list[str]) -> str:
    """Run a single agent step, stream output, save to file, return content."""

    output_file = output_dir / dict((s[0], s[2]) for s in STEPS)[step_name]

    print(f"\n{'─' * 60}")
    print(f"  Step: {step_name.replace('_', ' ').title()}  →  {output_file.name}")
    print(f"{'─' * 60}\n")

    prompt = load_prompt(prompt_file, country)
    context = load_context(country, output_dir, steps_done)

    system = (
        f"You are a specialist agent in a YouTube history channel pipeline. "
        f"You are producing content for a video about the complete history of {country}. "
        f"Follow the instructions in the user prompt exactly. "
        f"Output clean markdown only — no preamble, no 'here is your...' intro, no closing remarks. "
        f"Just the deliverable, starting immediately.\n\n"
        f"Context from the series and previous steps:\n\n{context}"
    )

    full_response = ""
    with client.messages.stream(
        model=MODEL,
        max_tokens=8096,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response += text

    print(f"\n\n✓  Saved to {output_file}\n")
    output_file.write_text(full_response)
    return full_response


def upload_to_google_doc(audio_script: str, country: str):
    """Upload audio script to the shared Google Doc."""
    print(f"\n{'─' * 60}")
    print(f"  Uploading to Google Doc...")
    print(f"{'─' * 60}\n")

    creds = service_account.Credentials.from_service_account_file(str(SA_FILE), scopes=SCOPES)
    service = build("docs", "v1", credentials=creds)

    doc = service.documents().get(documentId=GOOGLE_DOC_ID).execute()
    body = doc.get("body", {}).get("content", [])
    end_index = body[-1].get("endIndex", 2) if body else 2

    # Extract title and subtitle from script (first two non-empty lines)
    lines = [l for l in audio_script.split("\n") if l.strip()]
    title = lines[0].lstrip("#").strip() if lines else f"{country.upper()}: THE COMPLETE HISTORY"
    subtitle = lines[1].lstrip("#").strip() if len(lines) > 1 else "Audio Script — Single Episode"

    # Strip markdown headers from the full text for the doc
    clean_script = re.sub(r"^#{1,3}\s+", "", audio_script, flags=re.MULTILINE)
    full_text = f"{title}\n{subtitle}\n\n{clean_script.strip()}\n"

    title_end    = 1 + len(title) + 1
    subtitle_end = title_end + len(subtitle) + 1

    # Delete existing content and insert new
    requests = []
    if end_index > 2:
        requests.append({"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end_index - 1}}})
    requests.append({"insertText": {"location": {"index": 1}, "text": full_text}})
    service.documents().batchUpdate(documentId=GOOGLE_DOC_ID, body={"requests": requests}).execute()

    # Apply formatting
    doc2      = service.documents().get(documentId=GOOGLE_DOC_ID).execute()
    body2     = doc2.get("body", {}).get("content", [])
    new_end   = body2[-1].get("endIndex", 2)
    black     = {"color": {"rgbColor": {"red": 0, "green": 0, "blue": 0}}}

    fmt = [
        {"updateTextStyle": {
            "range": {"startIndex": 1, "endIndex": new_end - 1},
            "textStyle": {"weightedFontFamily": {"fontFamily": "Calibri", "weight": 400},
                          "fontSize": {"magnitude": 11, "unit": "PT"},
                          "foregroundColor": black, "bold": False, "italic": False},
            "fields": "weightedFontFamily,fontSize,foregroundColor,bold,italic"}},
        {"updateTextStyle": {
            "range": {"startIndex": 1, "endIndex": title_end},
            "textStyle": {"weightedFontFamily": {"fontFamily": "Calibri", "weight": 700},
                          "fontSize": {"magnitude": 18, "unit": "PT"},
                          "bold": True, "foregroundColor": black},
            "fields": "weightedFontFamily,fontSize,bold,foregroundColor"}},
        {"updateTextStyle": {
            "range": {"startIndex": title_end, "endIndex": subtitle_end},
            "textStyle": {"weightedFontFamily": {"fontFamily": "Calibri", "weight": 400},
                          "fontSize": {"magnitude": 12, "unit": "PT"},
                          "italic": True, "foregroundColor": black},
            "fields": "weightedFontFamily,fontSize,italic,foregroundColor"}},
        {"updateParagraphStyle": {
            "range": {"startIndex": 1, "endIndex": title_end},
            "paragraphStyle": {"alignment": "CENTER"}, "fields": "alignment"}},
        {"updateParagraphStyle": {
            "range": {"startIndex": title_end, "endIndex": subtitle_end},
            "paragraphStyle": {"alignment": "CENTER"}, "fields": "alignment"}},
    ]
    service.documents().batchUpdate(documentId=GOOGLE_DOC_ID, body={"requests": fmt}).execute()
    print(f"✓  Uploaded to Google Doc (ID: {GOOGLE_DOC_ID})\n")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate YouTube history video for a country.")
    parser.add_argument("country", help="Country name, e.g. 'Finland'")
    parser.add_argument("--skip-docs", action="store_true",
                        help="Skip uploading to Google Docs")
    parser.add_argument("--steps", default="all",
                        help="Comma-separated steps to run, e.g. 'research,audio_script'. Default: all")
    args = parser.parse_args()

    country     = args.country.strip()
    steps_to_run = [s.strip() for s in args.steps.split(",")] if args.steps != "all" \
                   else [s[0] for s in STEPS]

    output_dir = OUTPUT_DIR / country
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'═' * 60}")
    print(f"  History Channel — {country}")
    print(f"  Steps: {', '.join(steps_to_run)}")
    print(f"  Output: {output_dir}")
    print(f"{'═' * 60}")

    client      = anthropic.Anthropic()
    steps_done  = []
    audio_script = None

    for step_name, prompt_file, output_file in STEPS:
        if step_name not in steps_to_run:
            # Load existing output for context even if not re-running
            existing = output_dir / output_file
            if existing.exists():
                steps_done.append(step_name)
            continue

        result = run_agent(client, step_name, prompt_file, country, output_dir, steps_done)
        steps_done.append(step_name)

        if step_name == "audio_script":
            audio_script = result

    # Upload audio script to Google Docs
    if not args.skip_docs:
        if audio_script is None:
            # Try loading from file if audio_script step was skipped
            audio_path = output_dir / "audio_script.md"
            if audio_path.exists():
                audio_script = audio_path.read_text()

        if audio_script:
            upload_to_google_doc(audio_script, country)
        else:
            print("⚠  No audio script found to upload. Run with --steps audio_script or check Output folder.")

    print(f"\n{'═' * 60}")
    print(f"  Done. All files saved to:")
    print(f"  {output_dir}")
    print(f"{'═' * 60}\n")


if __name__ == "__main__":
    main()
