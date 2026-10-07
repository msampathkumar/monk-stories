#!/usr/bin/env python3
"""
Monk Stories Daily Publisher
Automates the drafting, illustration, and publication of daily wisdom parables.
"""

import os
import sys
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "docs" / "posts"
IMAGES_DIR = REPO_ROOT / "docs" / "assets" / "images" / "posts"
BOOKS_DIR = Path.home() / "books"

def ensure_directories():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)

def main():
    ensure_directories()
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"[monk-stories] Daily publisher initialized for {today}")
    print(f"[monk-stories] Reference books available in: {BOOKS_DIR}")
    print(f"[monk-stories] Blog posts directory: {POSTS_DIR}")

if __name__ == "__main__":
    main()
