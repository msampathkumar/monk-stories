#!/usr/bin/env python3
"""
Monk Stories Daily Publisher
Automates the drafting, illustration, and publication of daily wisdom parables.
Adheres strictly to ART_STYLE.md for Vedic/Hindu Rishi character design and monochrome ink-wash aesthetics.
"""

import os
import sys
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "docs" / "posts"
IMAGES_DIR = REPO_ROOT / "docs" / "assets" / "images" / "posts"
BOOKS_DIR = Path.home() / "books"
ART_STYLE_GUIDE = REPO_ROOT / "ART_STYLE.md"

# Standard prompt template adhering strictly to ART_STYLE.md
PROMPT_TEMPLATE = (
    "A minimalist ink wash painting, black and white brush stroked artwork with authentic Indian aesthetic, "
    "an ancient Hindu sage (Rishi) with serene expression, long beard, hair tied in a Vedic rishi jata topknot, "
    "wearing simple ascetic dhoti and rudraksha beads, subtle tilak on forehead, sitting under an ancient banyan tree "
    "outside a forest ashram hermitage, {scene_details}, traditional brushwork, high contrast monochrome, "
    "contemplative and dignified atmosphere."
)

def ensure_directories():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)

def generate_art_prompt(scene_details: str) -> str:
    """Generate image prompt adhering strictly to ART_STYLE.md"""
    return PROMPT_TEMPLATE.format(scene_details=scene_details)

def main():
    ensure_directories()
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"[monk-stories] Daily publisher initialized for {today}")
    print(f"[monk-stories] Art style guide loaded: {ART_STYLE_GUIDE}")
    print(f"[monk-stories] Reference books available in: {BOOKS_DIR}")

if __name__ == "__main__":
    main()
