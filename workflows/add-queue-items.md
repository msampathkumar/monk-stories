# Workflow: add queue items

**Produces:** 5 new rows in `standards/story-queue.md`
**Runs per invocation:** 1 batch of exactly 5 rows
**Skill(s):** `skills/monk-parable-curator`
**Standards:** `standards/story-queue.md`, `standards/lineage.md`

Trigger: `scripts/next_item.py` exits 11 or prints `WARNING: fewer than 3 queue items left`.

## Preconditions
- [ ] `git status --porcelain` is empty; `git pull --rebase` exits 0.

## Inputs
| Input | Path / Command |
|---|---|
| Queue | `standards/story-queue.md` |
| Lore categories | `standards/lineage.md` table |
| Used stories | `grep -h '^# ' docs/posts/2026-*.md` |

## Steps
1. **Ticket.** `tk create "Add 5 story queue items" -t task --parent ms-3lwv`; `tk start <id>`.
2. **Pick 5 stories.** Rules: well-known classical stories with a named source text; at least 2 of the 5 from a different lineage than the last 3 queue rows; no story already in a post H1 or the queue.
3. **Fill rows.** Append 5 rows inside the `QUEUE` markers, status `[ ]`, 8 columns. `Lore category` must be a table value. `Locator` = book/parva/kanda/sutta/Jataka number; add `(UNVERIFIED)` if you cannot confirm it from a source you read.
4. **Key check.** For each `Key`: `grep -ilw "<key>" docs/posts/*.md` must print nothing; else choose a more distinctive key (a proper name works best).
5. **Validate.** `python3 scripts/next_item.py --date 2099-01-01` exits 0 and shows `queue_remaining` ≥ 5.
6. **Record & commit.** `tk add-note <id> "added: <5 slugs>"`; `tk close <id>`; `git add standards/story-queue.md .tickets/ && git commit -m "docs(queue): add 5 stories (<id>)" && git push origin master`.

## Rubric (all YES)
1. Each story exists in the named source (you can name the book/section)?
2. Each row's lineage matches its source (Buddhist texts → Buddhist lore category)?
3. Each workplace theme is one sentence naming a specific behaviour?
4. No duplicate of an existing post or queue row?
5. Every unverified locator is marked `(UNVERIFIED)`?

## Failure handling
- `next_item.py` exit 2 or parse error → a row does not have 8 cells; fix the `|` separators.
- Unsure a story exists in the source → do not add it.

## Definition of Done
- 5 rows added, `next_item.py` exit 0, ticket closed, commit pushed.
