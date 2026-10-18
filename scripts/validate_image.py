#!/usr/bin/env python3
"""Layer A check for a post illustration (standards/art.md §1).

Usage: python3 scripts/validate_image.py docs/assets/images/posts/<stem>.jpg [...]
Exit 0 = all pass; 1 = violations (one line each). Stdlib only.
Colour, framing, text and archetype are NOT machine-checked: run the visual
audit in standards/art.md §5 with view_image.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from storylib import POST_NAME_RE, jpeg_size  # noqa: E402

MIN_W, RATIO, TOL = 1376, 16 / 9, 0.02
MIN_BYTES, MAX_BYTES = 200 * 1024, 8 * 1024 * 1024


def check(path):
    p = Path(path)
    errs = []
    if not p.is_file():
        return [f"{p}: file not found"]
    if p.suffix != ".jpg" or not POST_NAME_RE.match(p.stem + ".md"):
        errs.append(f"{p}: name must be YYYY-MM-DD-<slug>.jpg")
    size = p.stat().st_size
    if not MIN_BYTES <= size <= MAX_BYTES:
        errs.append(f"{p}: size {size} bytes outside {MIN_BYTES}-{MAX_BYTES}")
    dims = jpeg_size(p)
    if dims is None:
        errs.append(f"{p}: not a readable JPEG")
        return errs
    w, h = dims
    if w < MIN_W:
        errs.append(f"{p}: width {w} < {MIN_W}")
    if h == 0 or abs((w / h) / RATIO - 1) > TOL:
        errs.append(f"{p}: aspect {w}x{h} is not 16:9 (±2%)")
    return errs


def main(argv):
    if not argv:
        print(__doc__.strip().splitlines()[2])
        return 2
    errs = [e for a in argv for e in check(a)]
    for e in errs:
        print("FAIL", e)
    if not errs:
        print(f"PASS {len(argv)} image(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
