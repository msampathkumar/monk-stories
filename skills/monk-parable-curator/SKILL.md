---
name: monk-parable-curator
description: "Use when drafting, editing, or reviewing a Monk Stories parable post (docs/posts/*.md) or adding stories to the queue. Covers retelling a classical Indian or Buddhist story and drawing its lesson fully inside the ancient world, following the repo's story standard and validator."
---

# Monk Parable Curator

## When to use
- Writing a new daily post (called from `workflows/publish-daily-story.md` step 4).
- Fixing a post that fails `scripts/validate_story.py` or the story rubric.
- Choosing stories for `standards/story-queue.md` (`workflows/add-queue-items.md`).

## Procedure
1. Get the unit: `python3 scripts/next_item.py` (never choose a story freely).
2. Read `standards/story.md` (format and limits) and the archetype section of
   `standards/lineage.md` named by `archetype:`.
3. Copy `templates/post.md` to the `post:` path. Fill slots in order; match the
   section rhythm of `examples/2026-10-17-the-pious-predator.md`.
   - **Approach (Part 1):** Ground the named seeker naturally in the ancient/timeless world (guild-master, caravan leader, court treasurer, minister, physician, royal counselor, master artisan).
   - **Fully in-world:** every section, heading, and closing line stays in the
     story's era. No modern words (validator `MODERN_TERMS`), no "in modern
     times" pivot. The reader makes the link to their own life.
4. Retelling (Part 2): include only events you can attribute to the named
   source. If a detail is uncertain, omit it. Never invent verse numbers; write
   `UNVERIFIED` in the Source line instead.
5. Teaching (Part 3): one pattern per story beat, shown in the seeker's own
   world (court, guild, caravan, council); give each a short bold name and one
   line such a person might say.
6. Counsel (Part 4): ≥ 3 `### N.` rules; each names an action the seeker can
   take tomorrow, in-world (e.g. "write the terms on a palm leaf and have both
   parties seal it").
7. Close with the Source line, 1–3 sentences of the seeker's changed state,
   then the blockquote aphorism using the story's central image.
8. Run `python3 scripts/validate_story.py <post>`; fix each FAIL line (max 2
   loops), then answer the rubric in the workflow.

## Standards referenced
- `standards/story.md` — structure, word counts, banned phrases, Source line, duplicates.
- `standards/lineage.md` — allowed lore categories; Rishi vs Monk teacher.
- `standards/story-queue.md` — the ordered backlog.

## Red lines
- Never pick a story outside the queue during a daily run.
- Never present an invented quote as a verbatim verse.
- Never mix a Rishi teacher into a Buddhist story or a Buddhist monk into a Hindu story.
- Never step out of the ancient setting anywhere in the post, headings included.
- Never commit a post with validator FAILs.
