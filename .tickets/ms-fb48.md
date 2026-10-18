---
id: ms-fb48
status: closed
deps: []
links: []
created: 2026-10-18T00:04:32Z
type: task
priority: 1
assignee: Sampath Kumar
parent: ms-3lwv
---
# Model-proof: workflows for daily story and art


## Notes

**2026-10-18T00:10:39Z**

Added workflows/publish-daily-story.md (13 steps covering every step of automation daily-monk-story-publisher: tk, next_item selection with exit codes, draft from template, duplicate pre-check, image sub-workflow, validator, 8-item rubric, mkdocs build, queue marking, tk note template, commit/push, 2-line notify; bounded 2 loops + BLOCKED path), workflows/generate-illustration.md (verbatim prompt, retries 30s/120s, max 2 regenerations, 8-question visual audit, standalone regenerate mode), workflows/add-queue-items.md (5-row batch, key dedupe, rubric).
