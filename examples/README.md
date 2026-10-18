# Golden examples

Each example passes its Layer A gate. Copy their structure; do not copy their text.

| Artifact | Golden example | Gate command |
|---|---|---|
| Story post | `examples/2026-10-17-the-pious-predator.md` | `python3 scripts/validate_story.py --strict examples/2026-10-17-the-pious-predator.md` |
| Illustration (rishi) | `docs/assets/images/posts/2026-10-17-the-pious-predator.jpg` | `python3 scripts/validate_image.py docs/assets/images/posts/2026-10-17-the-pious-predator.jpg` + visual audit 8/8 YES (checked 2026-10-18) |
| Illustration (monk) | none passes yet — `2026-10-10-the-unaccepted-gift.jpg` has East-Asian text and a red seal. Use the monk prompt in `standards/art.md` §4. | — |

The example post is a copy of the live post; its image path resolves to the
live image. Keep it in sync only if the live post is edited.
