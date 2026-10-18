---
id: ms-ise2
status: closed
deps: []
links: []
created: 2026-10-18T00:04:32Z
type: task
priority: 1
assignee: Sampath Kumar
parent: ms-3lwv
---
# Model-proof: validators, duplicate check, next_item


## Notes

**2026-10-18T00:08:59Z**

Added scripts/storylib.py (shared parsing, lineage/queue table parsers, JPEG SOF size reader), scripts/validate_story.py (frontmatter, H1, image embed+file, sections, numbered rules, words, opening>=120w, Source line, closing blockquote, banned phrases, lineage-forbidden words, duplicates; strict for date>=2026-10-18, --strict flag for goldens), scripts/validate_image.py (JPEG, 16:9 ±2%, width>=1376, 200KB-8MB), scripts/check_duplicate.py (slug, same-date strict, main-title overlap>=0.5, identical Source line; pre-write --title mode), scripts/next_item.py (UTC date, exit 10 STOP if post exists, exit 11 BLOCKED if queue empty, first [ ] row whose Key not in any post). All stdlib. Results: validate_image PASS 12/12; validate_story --all: 8 violations (smiling-snake alt contains 'Monk'; viduras-silence 7 legacy violations); check_duplicate PASS (2026-10-13 double-post tolerated as legacy). Negative test on a bad file produced 14 FAIL lines. mkdocs build still OK. publish_daily_story.py untouched.
