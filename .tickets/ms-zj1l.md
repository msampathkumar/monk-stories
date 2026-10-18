---
id: ms-zj1l
status: closed
deps: []
links: []
created: 2026-10-18T00:11:41Z
type: task
priority: 2
assignee: Sampath Kumar
parent: ms-3lwv
---
# Fix small legacy validator failures (alt text, frontmatter)


## Notes

**2026-10-18T00:11:56Z**

Before: validate_story --all = 8 violations. Fixed smiling-snake alt ('Monk' -> 'Vedic Rishi ...', matches image which shows a Rishi); viduras-silence frontmatter normalized to standard keys (removed title/author, added authors: monk, Office Politics first, 3 tags) and alt text expanded. After: 2 violations (viduras-silence: 0 H2 sections, 236 words) -> needs content rewrite, tracked separately. mkdocs build OK.
