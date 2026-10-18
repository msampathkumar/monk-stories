# Workflow: publish daily story

**Produces:** `docs/posts/YYYY-MM-DD-<slug>.md` + `docs/assets/images/posts/YYYY-MM-DD-<slug>.jpg` (one story unit)
**Runs per invocation:** 1 unit
**Skill(s):** `skills/monk-parable-curator`, `skills/monk-art-generator`
**Standards:** `standards/story.md`, `standards/lineage.md`, `standards/art.md`, `standards/story-queue.md`
**Run by:** automation `daily-monk-story-publisher` (04:00 IST = 22:30 UTC). Epic: `ms-3lwv`.

All commands run from `/home/sampathm/github/monk-stories`.

## Preconditions
- [ ] Clean tree: `git status --porcelain` prints nothing. Else → STOP, `tk` note BLOCKED "dirty tree".
- [ ] Up to date: `git pull --rebase` exits 0.
- [ ] Tools exist: `test -x .venv/bin/mkdocs && test -x ~/.local/bin/tk`.

## Inputs
| Input | Path / Command |
|---|---|
| Next story | `python3 scripts/next_item.py` |
| Post template | `templates/post.md` |
| Golden post | `examples/2026-10-17-the-pious-predator.md` |
| Optional source notes | `~/books/*.md` (4 files; read only if they mention the story) |

## Steps
1. **Select unit.** Run `python3 scripts/next_item.py`.
   - Exit 10 (`STOP: post already exists`) → nothing to do. Reply `NO_REPLY`. STOP.
   - Exit 11 (`BLOCKED`) → `tk create "BLOCKED: story queue empty" -t task --parent ms-3lwv`; reply "Monk Stories: queue empty, run workflows/add-queue-items.md". STOP.
   - Exit 0 → record every printed value (`date`, `slug`, `post`, `image`, `story`, `lore`, `archetype`, `source`, `locator`, `key`, `theme`).
2. **Ticket.** `tk create "Daily Story: <story>" -t task --parent ms-3lwv -d "<theme>"` → `<id>`; `tk start <id>`.
3. **Read context.** Read exactly: `standards/story.md`, the `<archetype>` section of `standards/lineage.md`, `templates/post.md`, `examples/2026-10-17-the-pious-predator.md`. `grep -il "<key>" ~/books/*.md` and read any match.
4. **Draft post.** Copy `templates/post.md` to `<post>`. Fill every `{{slot}}`:
   - `{{DATE}}` = `<date>`, `{{SLUG}}` = `<slug>`, `{{LORE_CATEGORY}}` = `<lore>`.
   - Teacher = archetype `<archetype>` (rishi → "the Rishi"; monk → "the Monk").
   - `**Source:**` line = `<source>, <locator>` (keep `UNVERIFIED` if the queue says so).
   - Must include the queue `<key>` word at least once (dedupe depends on it).
5. **Pre-check duplicates.** `python3 scripts/check_duplicate.py <post>` → must print `PASS`. If FAIL on title → change the main title (text before `:`) and re-run.
6. **Generate image.** Follow `workflows/generate-illustration.md` with `<post>` and `<archetype>`. It must end with the image at `<image>` and visual audit 8/8 YES. If it ends BLOCKED → `trash <post>` (never `rm`, never `git clean`), `tk add-note <id> "BLOCKED: image: <reason>"`, leave ticket open, reply "Monk Stories BLOCKED: <reason>". STOP.
7. **Validate (Layer A).** `python3 scripts/validate_story.py <post>` → fix each `FAIL` line, re-run. Max 2 fix loops. Still failing → BLOCKED as in step 6.
8. **Rubric (Layer B).** Answer each rubric question YES/NO with a quote from the post. Any NO → fix, re-run step 7 (counts toward the 2 loops).
9. **Build.** `.venv/bin/mkdocs build -q` → exit 0. Non-zero → read the error, fix the post (not `mkdocs.yml`), max 2 loops, else BLOCKED.
10. **Mark queue.** In `standards/story-queue.md` change that row's `[ ]` to `[x] <date>`.
11. **Record.** `tk add-note <id> "<filled templates/publish-note.md block>"`; `tk close <id>`.
12. **Commit.** `git add <post> <image> standards/story-queue.md .tickets/ && git commit -m "feat(daily-story): publish '<Title>' (ticket: <id>)" && git push origin master`. Push rejected → `git pull --rebase` once, push again; still failing → note BLOCKED (commit stays local).
13. **Notify.** Final reply = exactly two lines: `<Title>` and `https://msampathkumar.github.io/monk-stories/posts/<date>-<slug>/` (URL is **UNVERIFIED** — site not deployed as of 2026-10-18; see `standards/story.md` §7).

## Rubric (all must be YES; quote evidence)
1. The seeker is named and the opening states one concrete workplace incident (who did what, and the cost)?
2. The teacher is the `<archetype>` throughout (no Rishi in a monk post, no monk in a rishi post)?
3. Every event in the ancient-story section belongs to the named source; no invented verse numbers or quotes presented as exact?
4. Each beat of the ancient story is mapped to a named workplace behaviour in the mirror section?
5. Every `### N.` rule contains an action the reader can do this week? (quote one per rule)
6. No first-person narrator outside quoted dialogue?
7. The closing blockquote uses the story's central image (the `<key>` creature/object)?
8. `<theme>` differs from the themes of the last 3 posts (`ls docs/posts/2026-* | tail -3`, read their H1s)?

## Failure handling
- `next_item.py` exit 10 → already published today; do nothing.
- Image API error/timeout → retries and limits in `workflows/generate-illustration.md`; never publish without an image.
- Validator FAIL on word count → expand/trim Part 2 or Part 3 only.
- Validator FAIL on lineage word → replace the word with the archetype's term from `standards/lineage.md`.
- mkdocs warning about `blog` / MkDocs 2.0 banner → informational; ignore if exit code is 0.
- Any step still failing after 2 loops → `tk add-note <id> "BLOCKED: <step>: <last FAIL line>"`, leave ticket open, do not commit, reply "Monk Stories BLOCKED: <reason>". STOP.

## Definition of Done
- `validate_story.py <post>` exit 0; `validate_image.py <image>` exit 0; visual audit 8/8; rubric 8/8.
- `mkdocs build` exit 0; queue row marked; ticket closed; commit pushed to `origin/master`; two-line notification sent.
