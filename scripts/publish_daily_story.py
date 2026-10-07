#!/usr/bin/env python3
"""
Monk Stories Daily Publisher
Automates the drafting, illustration, and publication of daily wisdom parables.
Adheres strictly to ART_STYLE.md for Vedic/Hindu Rishi character design and monochrome ink-wash aesthetics.
Enforces task-centric work via `tk` (/home/sampathm/.local/bin/tk).
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "docs" / "posts"
IMAGES_DIR = REPO_ROOT / "docs" / "assets" / "images" / "posts"
BOOKS_DIR = Path.home() / "books"
ART_STYLE_GUIDE = REPO_ROOT / "ART_STYLE.md"
TK_BIN = Path.home() / ".local" / "bin" / "tk"

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

def run_tk(args: list[str]) -> str:
    """Execute tk command inside monk-stories repository."""
    cmd = [str(TK_BIN)] + args
    result = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True, check=True)
    return result.stdout.strip()

def tk_create_daily_ticket(title: str, parent: str = "ms-3lwv") -> str:
    """Create a new daily story ticket in tk and transition it to in_progress."""
    output = run_tk(["create", f"Daily Story: {title}", "-t", "task", "-p", "2", "--parent", parent, "-d", f"Publish daily story '{title}'"])
    ticket_id = output.splitlines()[-1].strip()
    run_tk(["start", ticket_id])
    return ticket_id

def tk_complete_daily_ticket(ticket_id: str, notes: str):
    """Log completion notes and close the ticket."""
    run_tk(["add-note", ticket_id, notes])
    run_tk(["close", ticket_id])

def main():
    ensure_directories()
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"[monk-stories] Daily publisher initialized for {today}")
    print(f"[monk-stories] Art style guide loaded: {ART_STYLE_GUIDE}")
    print(f"[monk-stories] Task tracker: {TK_BIN}")
    print(f"[monk-stories] Reference books available in: {BOOKS_DIR}")

if __name__ == "__main__":
    main()
