---
name: monk-art-generator
description: "Use when generating, auditing, or regenerating a Monk Stories illustration (docs/assets/images/posts/*.jpg): monochrome ink-wash, full-bleed, Rishi for Hindu lore and shaved-head monk for Buddhist lore, Gemini image generation only."
---

# Monk Art Generator

## When to use
- Creating the image for a new post (`workflows/publish-daily-story.md` step 6).
- Replacing a defective existing image (`workflows/generate-illustration.md`, standalone mode).
- Auditing existing images against the visual audit.

## Procedure
1. Find the archetype: the post's lore category → `standards/lineage.md` table
   (`rishi` or `monk`).
2. Copy the matching prompt formula from `standards/art.md` §4 verbatim;
   replace only `[SCENE DETAILS]` (15–40 words, no colour words).
3. Generate with the OpenClaw `image_generate` tool at 16:9. Allowed
   alternative: `generate_illustration()` in `scripts/publish_daily_story.py`
   (needs `GEMINI_API_KEY`; never print the key).
4. Save to `docs/assets/images/posts/<post-stem>.jpg` (convert non-JPEG with
   `ffmpeg -i in.png -q:v 2 out.jpg`).
5. Run `python3 scripts/validate_image.py <jpg>`.
6. Open the image with `view_image`; answer the 8 questions in
   `standards/art.md` §5. Any NO → append `, absolutely no <item>` and
   regenerate. Max 2 regenerations, then BLOCKED.

## Standards referenced
- `standards/art.md` — palette, framing, forbidden artifacts, prompts, audit, retries.
- `standards/lineage.md` — Rishi / Monk / seeker appearance.

## Red lines
- Gemini models only; never pollinations.ai, Unsplash, stock, or scrapers.
- Never commit an image without the 8/8 visual audit recorded in the tk note.
- Never edit an image by hand to hide a defect (crop/paint over); regenerate.
