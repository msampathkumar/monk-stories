#!/usr/bin/env python3
"""Print the next daily story to produce (deterministic).

Usage: python3 scripts/next_item.py [--date YYYY-MM-DD]
  --date defaults to today's UTC date (`date -u +%F`), per standards/story.md.

Output (key: value lines) and exit codes:
  0  next item printed (date, slug, post, image, story, lore, lineage,
     archetype, source, locator, key, theme)
  10 a post for this date already exists  -> STOP, nothing to do
  11 queue has no available item          -> BLOCKED: run workflows/add-queue-items.md
Selection rule: first queue row with status '[ ]' whose Key does not appear
as a whole word (case-insensitive) in any docs/posts/*.md and whose slug is
not already used. Stdlib only.
"""

import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import storylib as sl  # noqa: E402


def main(argv):
    date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    if len(argv) == 2 and argv[0] == "--date":
        date = argv[1]
    elif argv:
        print(__doc__.strip())
        return 2

    posts = sl.list_posts()
    existing = [p for p in posts if p.name.startswith(date + "-")]
    if existing:
        print(f"STOP: post already exists for {date}: {existing[0].relative_to(sl.REPO_ROOT)}")
        return 10

    corpus = "\n".join(p.read_text(encoding="utf-8").lower() for p in posts)
    used_slugs = {sl.POST_NAME_RE.match(p.name).group(2) for p in posts}
    table = sl.load_lineage_table()
    remaining = 0
    chosen = None
    for row in sl.load_queue():
        if row["status"] != "[ ]":
            continue
        if re.search(r"\b" + re.escape(row["key"].lower()) + r"\b", corpus) or row["slug"] in used_slugs:
            continue
        remaining += 1
        if chosen is None:
            chosen = row
    if chosen is None:
        print("BLOCKED: no available story in standards/story-queue.md; run workflows/add-queue-items.md")
        return 11
    if chosen["lore"] not in table:
        print(f"BLOCKED: queue lore category '{chosen['lore']}' not in standards/lineage.md")
        return 11
    lineage, archetype = table[chosen["lore"]]
    stem = f"{date}-{chosen['slug']}"
    out = {
        "date": date,
        "slug": chosen["slug"],
        "post": f"docs/posts/{stem}.md",
        "image": f"docs/assets/images/posts/{stem}.jpg",
        "story": chosen["story"],
        "lore": chosen["lore"],
        "lineage": lineage,
        "archetype": archetype,
        "source": chosen["source"],
        "locator": chosen["locator"],
        "key": chosen["key"],
        "theme": chosen["theme"],
        "queue_remaining": remaining,
    }
    for k, v in out.items():
        print(f"{k}: {v}")
    if remaining < 3:
        print("WARNING: fewer than 3 queue items left; run workflows/add-queue-items.md after publishing")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
