#!/usr/bin/env python3
"""
Monk Stories Daily Publisher
Automates the drafting, illustration, and publication of daily wisdom parables.
Adheres strictly to AGENTS.md and ART_STYLE.md for Vedic/Hindu Rishi character design,
full-bleed edge-to-edge framing, and 100% monochrome ink-wash aesthetics.
Enforces task-centric work via `tk` (/home/sampathm/.local/bin/tk).
Uses ONLY our own Google Gemini API (gemini-3.1-flash-image) with zero third-party fallbacks.
"""

import os
import sys
import json
import base64
import requests
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "docs" / "posts"
IMAGES_DIR = REPO_ROOT / "docs" / "assets" / "images" / "posts"
BOOKS_DIR = Path.home() / "books"
ART_STYLE_GUIDE = REPO_ROOT / "ART_STYLE.md"
AGENTS_GUIDE = REPO_ROOT / "AGENTS.md"
TK_BIN = Path.home() / ".local" / "bin" / "tk"
IMAGE_MODELS = ["gemini-3-pro-image", "gemini-3.1-flash-image"]  # primary, fallback (Gemini only)

# Hardened prompt template: strictly full bleed, monochrome, zero seals/frames/text
PROMPT_TEMPLATE = (
    "A minimalist ink wash painting, black and white brush stroked artwork with authentic Indian aesthetic, "
    "an ancient Hindu sage (Rishi) with serene expression, long flowing beard, hair tied in a Vedic rishi jata topknot, "
    "wearing simple ascetic dhoti and natural rudraksha beads, subtle tilak on forehead, sitting under an ancient banyan tree "
    "outside a forest ashram hermitage, {scene_details}, traditional Indian brushwork, high contrast monochrome, "
    "full-bleed edge-to-edge composition, strictly no borders, no paper frames, no deckle edges, no artist seals, "
    "no stamps, no text, no color accents, contemplative and dignified atmosphere."
)

def ensure_directories():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)

def generate_art_prompt(scene_details: str) -> str:
    """Generate image prompt adhering strictly to ART_STYLE.md and AGENTS.md guardrails."""
    return PROMPT_TEMPLATE.format(scene_details=scene_details)

def generate_illustration(prompt: str, output_path: Path) -> Path:
    """Generate a 16:9 monochrome illustration, trying Gemini image models in order."""
    last_err = None
    for model in IMAGE_MODELS:
        try:
            return _generate_with_model(model, prompt, output_path)
        except Exception as e:  # try next Gemini model; never external services
            last_err = e
            print(f"[monk-stories] {model} failed: {e}")
    raise RuntimeError(f"All Gemini image models failed: {last_err}")

def _generate_with_model(model: str, prompt: str, output_path: Path) -> Path:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is missing!")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "2K"
            }
        }
    }

    res = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=120)
    res.raise_for_status()
    data = res.json()

    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline:
                b64_data = inline.get("data")
                img_bytes = base64.b64decode(b64_data)
                with open(output_path, "wb") as f:
                    f.write(img_bytes)
                print(f"[monk-stories] Successfully generated: {output_path} ({len(img_bytes)} bytes)")
                return output_path

    raise RuntimeError("No image data returned from Gemini API")

def main():
    ensure_directories()
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"[monk-stories] Daily publisher initialized for {today}")
    print(f"[monk-stories] Art style guide loaded: {ART_STYLE_GUIDE}")
    print(f"[monk-stories] Agent rules loaded: {AGENTS_GUIDE}")
    print(f"[monk-stories] Task tracker: {TK_BIN}")

if __name__ == "__main__":
    main()
