# Standard: Daily Story Post

Single source of truth for post format. Enforced by
`scripts/validate_story.py` (Layer A) and the rubric in
`workflows/publish-daily-story.md` (Layer B). Lineage and archetype rules live
in `standards/lineage.md`; illustration rules live in `standards/art.md`.

**Strict-mode cutoff:** posts dated **2026-10-18 or later** must pass every rule
below. Posts dated earlier ("legacy") are checked only for rules marked
**[all]**.

## 1. File naming and date [all]

- Path: `docs/posts/YYYY-MM-DD-<slug>.md`.
- `<slug>`: lowercase ASCII letters, digits, single hyphens; 2–6 words;
  no leading article required.
- `YYYY-MM-DD` = the **UTC date at run time**: `date -u +%F`. (The 04:00 IST
  run is 22:30 UTC the previous day; all existing posts follow this.)
- Exactly one post per date (strict mode). Legacy exception: 2026-10-13 has two.
- Image path: `docs/assets/images/posts/YYYY-MM-DD-<slug>.jpg` — same stem as
  the post.

## 2. Frontmatter [all]

Exactly these keys, in this order. No `title:` or `author:` keys.

```yaml
---
date: YYYY-MM-DD          # equals the filename date
authors:
  - monk                  # only author id defined in docs/posts/.authors.yml
categories:
  - Office Politics       # always first
  - <Lore category>       # from standards/lineage.md table
  - <optional third>      # e.g. Power & Strategy
tags:                     # 3–6 tags
  - <specific theme>
  - <...>
---
```

## 3. Body structure

| # | Element | Rule |
|---|---|---|
| 1 | H1 [all] | Exactly one `# ` line; it is the first body line. Format `# <Title>: <Subtitle>`; ≤ 110 characters (strict). |
| 2 | Image [all] | First non-blank line after H1 is `![<alt>](../assets/images/posts/<stem>.jpg)`; alt text ≥ 3 words; file exists. |
| 3 | Part 1 — The Approach (strict) | Prose before the first `## `; ≥ 120 words; a **named** seeker brings a workplace-mirroring problem to the teacher (archetype per lineage). |
| 4 | Part 2 — The Ancient Story (strict) | A `## ` section that retells the classical story or verse. |
| 5 | Part 3 — The Workplace Mirror (strict) | A `## ` section mapping the story to modern work. |
| 6 | Part 4 — Practical Rules (strict) | A `## ` section with **≥ 3** numbered `### 1. …`, `### 2. …`, `### 3. …` sub-headings. |
| 7 | Source line (strict) | A line `**Source:** <Text>, <locator>` after the last `### ` heading. `<Text>` names the classical work (e.g. *Panchatantra*, *Jataka Tales*); `<locator>` = book / parva / kanda / verse / Jataka number. Write `locator UNVERIFIED` if you cannot confirm it. |
| 8 | Part 5 — The Provocation (strict) | The **last non-blank line** of the file is a blockquote `> *"…"*`, ≤ 45 words. |

Section count: ≥ 3 `## ` headings [all]; ≥ 3 numbered `### N.` headings (strict).

## 4. Length

- Body words (everything after frontmatter, counted by
  `scripts/storylib.py:word_count`): strict posts **900–2200**; legacy posts
  **500–2200**.

## 5. Language (binary tests)

- Banned phrases [all] (case-insensitive; validator list is authoritative):
  "delve", "tapestry", "testament to", "in today's fast-paced",
  "ever-evolving", "game-changer", "game changer", "synergy",
  "navigate the complexities", "at the end of the day", "unlock your potential".
- No first-person narrator ("I" outside quoted dialogue is allowed only
  inside quotation marks) — Layer B rubric item.
- Every practical rule (`### N.`) contains at least one concrete action verb
  phrase the reader can do this week (e.g. "email a written summary",
  "decline the meeting") — Layer B rubric item.
- Quoted verses: attribute to the work named in the Source line; never invent
  verse numbers (use `UNVERIFIED`).

## 6. Duplicates

Checked by `scripts/check_duplicate.py <post>`:
- slug not used by another post;
- date not used by another post (strict);
- main-title overlap (text before `:`; words ≥ 4 letters minus stopwords;
  overlap = shared / smaller set) with any other post < 0.5;
- normalized `**Source:**` line not identical to another post's.

Selection-time duplicate avoidance: `scripts/next_item.py` skips queue items
whose `Key` already appears in any post (see `standards/story-queue.md`).

## 7. Publication URL

`https://msampathkumar.github.io/monk-stories/posts/<stem>/` —
**UNVERIFIED**: as of 2026-10-18 this returns HTTP 404 (no gh-pages branch or
deploy workflow exists). See ticket for owner decision.
