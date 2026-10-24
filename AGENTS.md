# AGENTS.md — Monk Stories

## Mission
Publish one parable per day from classical Indian and Buddhist lore about
power, loyalty, and rivalry, told fully inside its ancient world (the reader
draws the link to their own work), with one monochrome ink-wash illustration.
Static site: MkDocs Material (`mkdocs.yml`), posts in `docs/posts/`.

Audience: working professionals dealing with office politics; owner Sampath
Kumar (msampathkumar).

## Milestone and Definition of Done
**Milestone M1 (epic `ms-3lwv`): 30 daily posts that pass strict
validation**, starting 2026-10-18 (target proposed 2026-10-18; owner to confirm).
- DoD per day: `python3 scripts/validate_story.py <post>` exit 0,
  `python3 scripts/validate_image.py <image>` exit 0, visual audit 8/8,
  rubric 9/9, `mkdocs build` exit 0, commit pushed.
- Milestone count: number of `docs/posts/*.md` dated ≥ 2026-10-18 that pass
  `validate_story.py` — target 30.
- Legacy posts (before 2026-10-18) only need the `[all]` rules in
  `standards/story.md`.

## Workflow index
| Trigger | Workflow |
|---|---|
| Daily 04:00 IST automation, or "publish today's story" | `workflows/publish-daily-story.md` |
| Generate or replace one illustration | `workflows/generate-illustration.md` |
| `next_item.py` exit 11 or "fewer than 3 queue items" warning | `workflows/add-queue-items.md` |

## Single sources of truth
| Topic | File |
|---|---|
| Post format, word counts, naming, date rule, duplicates | `standards/story.md` |
| Lore categories → lineage → Rishi/Monk archetype | `standards/lineage.md` |
| Illustration style, prompts, forbidden artifacts, visual audit | `standards/art.md` |
| Next stories (ordered) | `standards/story-queue.md` |
| Post template / golden example | `templates/post.md` / `examples/2026-10-17-the-pious-predator.md` |

Skills (`skills/*/SKILL.md`) and personas (`agents/*.md`) link to these; they
never restate them. If a rule conflicts, the `standards/` file wins.

## Scripts (python3 stdlib; run from repo root)
| Command | Purpose | Exit codes |
|---|---|---|
| `python3 scripts/next_item.py` | Next story for today's UTC date | 0 item, 10 already published, 11 queue empty |
| `python3 scripts/validate_story.py <post>` / `--all` | Layer A gate for posts | 0 pass, 1 fail |
| `python3 scripts/validate_image.py <jpg>` | Layer A gate for images | 0 pass, 1 fail |
| `python3 scripts/check_duplicate.py <post>` | Duplicate-story check | 0 unique, 1 duplicate |
| `.venv/bin/mkdocs build -q` | Site build | 0 ok |
| `scripts/publish_daily_story.py` | Legacy helper: `generate_illustration()` Gemini call; `main()` only prints paths | — |

## Automation boundary
- Automation `daily-monk-story-publisher` (cron `0 4 * * *` Asia/Kolkata)
  runs **only** `workflows/publish-daily-story.md`, one post per run.
- Pause rule: the automation does nothing when `next_item.py` exits 10
  (already published) and stops BLOCKED when it exits 11 (queue empty).
- Owner review point: when 30 strict posts exist (M1 reached), report to the
  owner and keep publishing only if the owner confirms. UNVERIFIED: the owner
  has not yet set an end date for the series.
- The automation never edits `standards/`, `scripts/`, `mkdocs.yml`, or
  `AGENTS.md` (only the queue row status in `standards/story-queue.md`).

## Red lines (each testable)
1. Never call `pollinations.ai`, Unsplash, stock sites, or any non-Gemini image
   route. Test: `git grep -n -i "pollinations\|unsplash" -- scripts`
   prints nothing.
2. Never commit an image that has not passed the 8-question visual audit in
   `standards/art.md` §5; the tk note must contain the audit line.
3. Never commit a post that fails `validate_story.py`.
4. Never mix archetypes: rishi posts/images have no Buddhist monk; monk
   posts/images have no Rishi (`standards/lineage.md`).
5. One post per UTC date (`next_item.py` exit 10 enforces).
6. Every run starts with `tk create` + `tk start` and ends with `tk close` or a
   `BLOCKED:` note; `.tickets/` is committed with the change.
7. `git add <explicit paths>` only — never `git add .` or `-A`; never
   force-push; never commit `.env`, keys, or `site/`.
8. Max 2 fix loops per gate; then `BLOCKED:` note, ticket left open, no commit.
9. Use `trash`, never `rm`, for removals.

## Repo layout
```
AGENTS.md  standards/  workflows/  templates/  examples/  scripts/
skills/<name>/SKILL.md  agents/<persona>.md  docs/  mkdocs.yml  .tickets/
```
`docs/art-style.md` is a public site page, not a rule source.
