"""Shared helpers for monk-stories validators (python3 stdlib only)."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "docs" / "posts"
IMAGES_DIR = REPO_ROOT / "docs" / "assets" / "images" / "posts"
LINEAGE_MD = REPO_ROOT / "standards" / "lineage.md"
QUEUE_MD = REPO_ROOT / "standards" / "story-queue.md"

STRICT_CUTOFF = "2026-10-18"  # posts dated on/after this pass all rules
IN_WORLD_CUTOFF = "2026-10-13"  # posts dated on/after this get the modern-term scan
POST_NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")


def list_posts():
    """All dated post files, sorted by name."""
    return sorted(p for p in POSTS_DIR.glob("*.md") if POST_NAME_RE.match(p.name))


def split_frontmatter(text):
    """Return (frontmatter_text or None, body_text)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def parse_frontmatter(fm):
    """Minimal YAML subset: `key: value`, `key: [a, b]`, and `- item` lists.

    Returns (dict, ordered_keys)."""
    data, keys, current = {}, [], None
    for raw in fm.splitlines():
        line = raw.split(" #", 1)[0].rstrip()
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and not raw.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            keys.append(key)
            current = key
            if val.startswith("[") and val.endswith("]"):
                data[key] = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            elif val == "":
                data[key] = []
            else:
                data[key] = val.strip("'\"")
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and current is not None and isinstance(data.get(current), list):
            data[current].append(m.group(1).strip().strip("'\""))
    return data, keys


def load_lineage_table():
    """{lore category: (lineage, archetype)} parsed from standards/lineage.md."""
    text = LINEAGE_MD.read_text(encoding="utf-8")
    block = text.split("<!-- LINEAGE-TABLE:BEGIN -->", 1)[1].split("<!-- LINEAGE-TABLE:END -->", 1)[0]
    table = {}
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0].startswith("Lore") or set(cells[0]) <= set("-"):
            continue
        table[cells[0]] = (cells[1], cells[2])
    return table


def load_queue():
    """List of dicts from standards/story-queue.md."""
    text = QUEUE_MD.read_text(encoding="utf-8")
    block = text.split("<!-- QUEUE:BEGIN -->", 1)[1].split("<!-- QUEUE:END -->", 1)[0]
    cols = ["status", "slug", "story", "lore", "source", "locator", "key", "theme"]
    rows = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8 or cells[0] == "Status" or set(cells[0]) <= set("-"):
            continue
        rows.append(dict(zip(cols, cells)))
    return rows


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9\u2019']+", text))


def title_of(body):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def source_line_of(body):
    for line in body.splitlines():
        if line.startswith("**Source:**"):
            return line[len("**Source:**"):].strip()
    return ""


def jpeg_size(path):
    """Return (width, height) of a JPEG using SOF markers, or None."""
    data = Path(path).read_bytes()
    if data[:2] != b"\xff\xd8":
        return None
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = int.from_bytes(data[i + 2:i + 4], "big")
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h = int.from_bytes(data[i + 5:i + 7], "big")
            w = int.from_bytes(data[i + 7:i + 9], "big")
            return w, h
        i += 2 + seg_len
    return None
