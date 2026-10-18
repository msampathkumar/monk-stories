# Workflow: generate illustration

**Produces:** `docs/assets/images/posts/<post-stem>.jpg` for one existing or in-progress post
**Runs per invocation:** 1 image
**Skill(s):** `skills/monk-art-generator`
**Standards:** `standards/art.md`, `standards/lineage.md`

Called from `workflows/publish-daily-story.md` step 6, or standalone to
replace a defective image (then create your own ticket:
`tk create "Regenerate image: <stem>" -t task --parent ms-3lwv`; `tk start <id>`).

## Preconditions
- [ ] Post file exists: `test -f docs/posts/<stem>.md`.
- [ ] Archetype known: from `scripts/next_item.py` output, or look up the post's lore category in `standards/lineage.md`.

## Inputs
| Input | Path / Command |
|---|---|
| Post | `docs/posts/<stem>.md` |
| Prompt formula | `standards/art.md` §4 (`rishi` or `monk` block) |
| Visual audit | `standards/art.md` §5 |
| Golden image (rishi) | `docs/assets/images/posts/2026-10-17-the-pious-predator.jpg` |

## Steps
1. **Scene details.** Read the post's ancient-story section. Write `[SCENE DETAILS]`: 15–40 words naming the central creature/object and the setting; no colour words; no text/sign/scroll with writing.
2. **Prompt.** Copy the `<archetype>` formula from `standards/art.md` §4 verbatim; replace only `[SCENE DETAILS]`.
3. **Generate (attempt 1).** Use the OpenClaw `image_generate` tool with the prompt, aspect ratio 16:9, highest available resolution (2K). Never use any non-Gemini/scraper route (`standards/art.md` §6).
   - API error/timeout → wait 30 s, retry; wait 120 s, retry. Third failure → BLOCKED "image API: <error>".
4. **Save.** Write the result to `docs/assets/images/posts/<stem>.jpg`. If the tool returned PNG/WEBP: `ffmpeg -loglevel error -y -i <tmpfile> -q:v 2 docs/assets/images/posts/<stem>.jpg`.
5. **Validate (Layer A).** `python3 scripts/validate_image.py docs/assets/images/posts/<stem>.jpg` → exit 0. Aspect/size FAIL → regenerate (step 7).
6. **Visual audit (Layer B).** Open the file with `view_image`. Answer the 8 questions in `standards/art.md` §5 YES/NO.
7. **Regenerate if needed.** Any NO → append `, absolutely no <failed item>` per NO to the prompt and go to step 3. Max **2 regenerations** (3 images total). Still any NO → BLOCKED "visual audit: Q<n> <reason>".
8. **Record.** Note in the ticket: prompt used, number of generations, audit 8/8. (Standalone run: `tk add-note`, `tk close`, then `git add docs/assets/images/posts/<stem>.jpg .tickets/ && git commit -m "fix(art): regenerate <stem> (ticket: <id>)" && git push origin master`.)

## Rubric
The 8 visual-audit questions in `standards/art.md` §5 — all YES.

## Failure handling
- Image shows text or a seal → regenerate with `, absolutely no text, absolutely no red seal`.
- Border/paper frame → regenerate with `, absolutely no border, painted to all four edges`.
- Wrong archetype (e.g. shaved-head disciple in a rishi story) → regenerate with the "Seeker" row from `standards/lineage.md` appended.
- BLOCKED → `tk add-note <id> "BLOCKED: <reason>"`; leave ticket open; do not commit the image; return BLOCKED to the caller.

## Definition of Done
- `validate_image.py` exit 0; visual audit 8/8 YES; file at the exact path; (standalone) ticket closed and commit pushed.
