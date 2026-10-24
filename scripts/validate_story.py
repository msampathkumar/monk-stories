#!/usr/bin/env python3
"""Layer A validator for a daily story post (standards/story.md).

Usage:
  python3 scripts/validate_story.py docs/posts/YYYY-MM-DD-<slug>.md [...]
  python3 scripts/validate_story.py --all        # every dated post
  python3 scripts/validate_story.py --strict F   # force strict rules on F
                                                 # (e.g. a golden example)
Exit 0 = pass; 1 = violations (one line each, prefixed FAIL). Stdlib only.
Posts dated >= STRICT_CUTOFF get every rule; older (legacy) posts get the
[all] rules only. Duplicate checks run via check_duplicate.py (also invoked
here for files inside docs/posts/).
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import storylib as sl  # noqa: E402
import validate_image  # noqa: E402
import check_duplicate  # noqa: E402

BANNED = [
    "delve", "tapestry", "testament to", "in today's fast-paced",
    "ever-evolving", "game-changer", "game changer", "synergy",
    "navigate the complexities", "at the end of the day",
    "unlock your potential",
]
# Modern words that pull the reader out of the ancient setting. Single source
# of truth (standards/story.md section 5). Regexes, matched case-insensitively
# with word boundaries against the WHOLE body (headings included) of strict
# posts and posts dated >= sl.IN_WORLD_CUTOFF. Some natural words are banned
# only in their modern sense ("the board" yes, a ship's board no; "cloud"
# only in tech phrases) so ancient imagery stays usable.
MODERN_TERMS = [
    r"managers?", r"management", r"directors?", r"vice[- ]presidents?", r"vps?",
    r"executives?", r"corporate", r"corporations?", r"compan(?:y|ies)",
    r"offices?", r"e-?mails?", r"meetings?", r"slides?", r"slide decks?",
    r"decks?", r"stakeholders?", r"kpis?", r"deadlines?", r"quarterly",
    r"promotions?", r"hr", r"boss(?:es)?", r"team leads?", r"engineers?",
    r"engineering", r"software", r"the cloud", r"cloud (?:computing|provider|platform|service)s?",
    r"platforms?", r"infrastructure", r"sprints?", r"roadmaps?", r"start-?ups?",
    r"ceos?", r"ctos?", r"cfos?", r"the board", r"board meetings?", r"board of",
    r"boardrooms?", r"organi[sz]ations?", r"organi[sz]ational(?:ly)?",
    r"workplaces?", r"colleagues?", r"careers?", r"professionals?",
    r"professionally", r"modern", r"chief of staff", r"memo(?:randum|randa|s)?",
    r"employees?", r"spreadsheets?", r"dashboards?", r"deliverables?",
    r"inbox(?:es)?", r"pull requests?", r"microservices?", r"blast radius",
    r"database", r"failover", r"runbooks?", r"pipelines?", r"1:1", r"one-on-ones?",
    r"slack", r"scrum", r"high performers?", r"audit methodology", r"rail corridor",
]
MODERN_RE = re.compile(r"\b(?:" + "|".join(MODERN_TERMS) + r")\b", re.IGNORECASE)


def modern_terms_in(text):
    """Sorted unique modern terms found in text (lowercased)."""
    return sorted({m.group(0).lower() for m in MODERN_RE.finditer(text)})
FORBIDDEN_BY_ARCHETYPE = {
    "rishi": {"text": ["buddhist", "bhikkhu", "shaved head"], "alt": ["monk"]},
    "monk": {"text": ["rishi", "rudraksha", "tilak", "jata"], "alt": []},
}
EXPECTED_KEYS = ["date", "authors", "categories", "tags"]


def validate(path, force_strict=False, repo_check=True):
    p = Path(path)
    errs = []

    def fail(msg):
        errs.append(f"{p.name}: {msg}")

    if not p.is_file():
        return [f"{p}: file not found"]
    m = sl.POST_NAME_RE.match(p.name)
    if not m:
        fail("filename must be YYYY-MM-DD-<slug>.md (lowercase, hyphens)")
        return errs
    date, slug = m.group(1), m.group(2)
    stem = p.stem
    strict = force_strict or date >= sl.STRICT_CUTOFF
    text = p.read_text(encoding="utf-8")

    # --- frontmatter [all]
    fm_text, body = sl.split_frontmatter(text)
    if fm_text is None:
        fail("missing YAML frontmatter delimited by '---' lines")
        return errs
    fm, keys = sl.parse_frontmatter(fm_text)
    if keys != EXPECTED_KEYS:
        fail(f"frontmatter keys must be exactly {EXPECTED_KEYS} in order; got {keys}")
    if fm.get("date") != date:
        fail(f"frontmatter date '{fm.get('date')}' != filename date '{date}'")
    if fm.get("authors") != ["monk"]:
        fail("authors must be exactly ['monk']")
    cats = fm.get("categories") or []
    if not isinstance(cats, list) or not cats or cats[0] != "Office Politics":
        fail("categories[0] must be 'Office Politics'")
        cats = cats if isinstance(cats, list) else []
    table = sl.load_lineage_table()
    lore = [c for c in cats if c in table]
    archetype = None
    if not lore:
        fail(f"categories need >=1 lore category from standards/lineage.md; got {cats}")
    else:
        lineages = {table[c][0] for c in lore}
        if len(lineages) > 1:
            fail(f"lore categories mix lineages {sorted(lineages)}")
        archetype = table[lore[0]][1]
    tags = fm.get("tags") or []
    if not isinstance(tags, list) or not 3 <= len(tags) <= 6:
        fail(f"tags must be a list of 3-6 items; got {len(tags) if isinstance(tags, list) else tags}")

    # --- H1 + image [all]
    lines = body.splitlines()
    nonblank = [(i, ln) for i, ln in enumerate(lines) if ln.strip()]
    h1 = [ln for ln in lines if ln.startswith("# ")]
    if len(h1) != 1:
        fail(f"need exactly one H1 ('# '), found {len(h1)}")
    if not nonblank or not nonblank[0][1].startswith("# "):
        fail("first body line must be the H1")
    title = sl.title_of(body)
    if strict:
        if ":" not in title:
            fail("H1 must be '<Title>: <Subtitle>'")
        if len(title) > 110:
            fail(f"H1 is {len(title)} chars (> 110)")
    alt = ""
    if len(nonblank) >= 2:
        img = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", nonblank[1][1])
        want = f"../assets/images/posts/{stem}.jpg"
        if not img:
            fail("first non-blank line after H1 must be the image embed ![alt](...)")
        else:
            alt = img.group(1)
            if img.group(2) != want:
                fail(f"image path must be '{want}', got '{img.group(2)}'")
            if len(alt.split()) < 3:
                fail(f"image alt text needs >=3 words: '{alt}'")
            img_errs = validate_image.check(sl.IMAGES_DIR / f"{stem}.jpg")
            errs.extend(f"{p.name}: image: {e}" for e in img_errs)

    # --- sections
    h2 = [ln for ln in lines if ln.startswith("## ")]
    if len(h2) < 3:
        fail(f"need >=3 '## ' sections, found {len(h2)}")
    numbered_h3 = [ln for ln in lines if re.match(r"^### \d+\. \S", ln)]
    if strict and len(numbered_h3) < 3:
        fail(f"need >=3 numbered '### N. ' practical rules, found {len(numbered_h3)}")

    # --- length
    words = sl.word_count(body)
    lo = 900 if strict else 500
    if not lo <= words <= 2200:
        fail(f"body word count {words} outside {lo}-2200")

    # --- strict-only structure
    if strict:
        first_h2 = next((i for i, ln in enumerate(lines) if ln.startswith("## ")), len(lines))
        start = nonblank[1][0] + 1 if len(nonblank) >= 2 else 0
        opening = "\n".join(lines[start:first_h2])
        if sl.word_count(opening) < 120:
            fail(f"opening scene before first '## ' has {sl.word_count(opening)} words (< 120)")
        src_idx = next((i for i, ln in enumerate(lines) if ln.startswith("**Source:**")), None)
        last_h3 = max((i for i, ln in enumerate(lines) if ln.startswith("### ")), default=-1)
        if src_idx is None:
            fail("missing '**Source:** <Text>, <locator>' line")
        else:
            if src_idx < last_h3:
                fail("'**Source:**' line must come after the last '### ' heading")
            if "," not in lines[src_idx]:
                fail("Source line must be '<Text>, <locator>' (comma missing)")
        last = nonblank[-1][1] if nonblank else ""
        if not re.match(r'^> \*".+"\*\s*$', last):
            fail('last non-blank line must be a closing blockquote: > *"..."*')
        elif sl.word_count(last) > 45:
            fail(f"closing blockquote has {sl.word_count(last)} words (> 45)")

    # --- fully in-world (strict, or dated >= IN_WORLD_CUTOFF): whole body
    if strict or date >= sl.IN_WORLD_CUTOFF:
        for i, ln in enumerate(lines, 1):
            found = modern_terms_in(ln)
            if found:
                fail(f"body line {i}: modern term(s) {found} break the ancient setting")

    # --- language [all]
    if "{{" in text or "}}" in text:
        fail("unfilled template slot '{{...}}' remains")
    low = body.lower()
    for phrase in BANNED:
        if phrase in low:
            fail(f"banned phrase: '{phrase}'")
    if archetype:
        rules = FORBIDDEN_BY_ARCHETYPE[archetype]
        for w in rules["text"]:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                fail(f"lineage '{archetype}': forbidden word in text: '{w}'")
        for w in rules["alt"]:
            if re.search(r"\b" + re.escape(w) + r"\b", alt.lower()):
                fail(f"lineage '{archetype}': forbidden word in image alt: '{w}'")

    # --- duplicates
    if repo_check and p.resolve().parent == sl.POSTS_DIR.resolve():
        errs.extend(check_duplicate.check(p, strict=strict))
    return errs


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    force = False
    if argv[0] == "--strict":
        force, argv = True, argv[1:]
    files = sl.list_posts() if argv == ["--all"] else [Path(a) for a in argv]
    errs = []
    for f in files:
        errs.extend(validate(f, force_strict=force))
    for e in errs:
        print("FAIL", e)
    print(f"{'PASS' if not errs else 'FAILED'}: {len(files)} file(s), {len(errs)} violation(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
