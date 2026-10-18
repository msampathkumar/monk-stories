#!/usr/bin/env python3
"""Duplicate-story check (standards/story.md §6).

Usage:
  python3 scripts/check_duplicate.py docs/posts/YYYY-MM-DD-<slug>.md
  python3 scripts/check_duplicate.py --title "<Title>" --slug <slug> [--date YYYY-MM-DD]
      (pre-check before writing the file)
Exit 0 = unique; 1 = duplicate found (one FAIL line each). Stdlib only.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import storylib as sl  # noqa: E402

OVERLAP_MAX = 0.5
STOP = {"with", "from", "that", "this", "when", "your", "into", "over", "lesson", "warning"}


def sig_words(title):
    """Significant words (>= 4 letters, not stopwords) of the main title (before ':')."""
    main = title.split(":", 1)[0]
    return {w for w in re.findall(r"[a-z]+", main.lower()) if len(w) >= 4 and w not in STOP}


def overlap(a, b):
    """Overlap coefficient |a & b| / min(|a|, |b|)."""
    return len(a & b) / min(len(a), len(b)) if a and b else 0.0


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def compare(name, date, slug, title, source, strict=True):
    errs = []
    tw = sig_words(title)
    for other in sl.list_posts():
        if other.name == name:
            continue
        om = sl.POST_NAME_RE.match(other.name)
        o_date, o_slug = om.group(1), om.group(2)
        _, obody = sl.split_frontmatter(other.read_text(encoding="utf-8"))
        if o_slug == slug:
            errs.append(f"{name}: slug '{slug}' already used by {other.name}")
        if strict and o_date == date:
            errs.append(f"{name}: date {date} already has a post: {other.name}")
        j = overlap(tw, sig_words(sl.title_of(obody)))
        if j >= OVERLAP_MAX:
            errs.append(f"{name}: main title overlaps {other.name} (overlap {j:.2f} >= {OVERLAP_MAX})")
        osrc = sl.source_line_of(obody)
        if source and osrc and norm(source) == norm(osrc):
            errs.append(f"{name}: Source line identical to {other.name}")
    return errs


def check(path, strict=None):
    """strict=None -> strict for posts dated >= STRICT_CUTOFF (one post per date)."""
    p = Path(path)
    m = sl.POST_NAME_RE.match(p.name)
    if not m:
        return [f"{p.name}: filename must be YYYY-MM-DD-<slug>.md"]
    if strict is None:
        strict = m.group(1) >= sl.STRICT_CUTOFF
    _, body = sl.split_frontmatter(p.read_text(encoding="utf-8"))
    return compare(p.name, m.group(1), m.group(2), sl.title_of(body), sl.source_line_of(body), strict)


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    if argv[0] == "--title":
        args = dict(zip(argv[0::2], argv[1::2]))
        import datetime
        date = args.get("--date") or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        slug = args.get("--slug", "")
        errs = compare(f"{date}-{slug}.md", date, slug, args["--title"], "")
    else:
        errs = [e for a in argv for e in check(a)]
    for e in errs:
        print("FAIL", e)
    print("PASS: no duplicates" if not errs else f"FAILED: {len(errs)} duplicate signal(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
