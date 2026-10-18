# Standard: Illustration (Monochrome Ink Wash)

Single source of truth for illustration style, prompts, file specs, and the
visual audit. Character archetypes come from `standards/lineage.md` — this
file does not restate them; the prompt formulas below embed them verbatim.
Layer A: `scripts/validate_image.py`. Layer B: the visual audit in §5.

## 1. File specification (Layer A, machine-checked)

| Property | Required |
|---|---|
| Path | `docs/assets/images/posts/<post-stem>.jpg` |
| Format | JPEG (bytes start `FF D8`) |
| Aspect ratio | 16:9, width/height within ±2% of 1.778 |
| Width | ≥ 1376 px (existing files: 1376×768 or 2752×1536) |
| Size | 200 KB – 8 MB |

## 2. Visual identity (Layer B, checked by eye with `view_image`)

| Attribute | Required |
|---|---|
| Medium | Indian ink-wash / brush painting on off-white paper |
| Palette | Black, grey washes, off-white only. **Zero** colour: no red, gold, yellow, saffron, green, blue |
| Framing | Full-bleed: painted content touches all four image edges; no margin, border, or frame |
| Figures | Exactly the archetype for the post's lineage (`standards/lineage.md`) |
| Rendering | Hand-brushed look; no 3D / CGI / photographic rendering |

## 3. Forbidden artifacts (any one present → reject and regenerate)

1. Paper-cut frames, torn-paper or deckle edges, mounting frames, white margins.
2. Red seals, hanko / chop marks, any coloured stamp or emblem.
3. Any text: calligraphy, Devanagari or pseudo-script, signatures, captions.
4. Watermarks or logos.
5. Colour accents of any hue.
6. Mixed archetypes (e.g. a shaved-head monk in a Rishi story).

## 4. Prompt formulas (copy verbatim; replace only `[SCENE DETAILS]`)

`[SCENE DETAILS]` = 15–40 words naming the story's central physical metaphor
(e.g. "a grey crane standing on one leg at the edge of a lotus pond, a crab
in the shallows"). No colour words in it.

### rishi (hindu lineage)

```text
A minimalist ink wash painting, black and white brush stroked artwork with authentic Indian aesthetic, an ancient Hindu sage (Rishi) with serene expression, long flowing beard, hair tied in a Vedic rishi jata topknot, wearing simple ascetic dhoti and natural rudraksha beads, subtle tilak on forehead, sitting under an ancient banyan tree outside a forest ashram hermitage, [SCENE DETAILS], traditional Indian brushwork, high contrast monochrome, full-bleed edge-to-edge composition, strictly no borders, no paper frames, no deckle edges, no artist seals, no stamps, no text, no color accents, contemplative and dignified atmosphere.
```

### monk (buddhist lineage)

```text
A minimalist ink wash painting, black and white brush stroked artwork with authentic ancient aesthetic, a serene Buddhist monk with clean shaved head and draped monastic robes, no beads, no topknot, sitting calmly in quiet contemplation in a bamboo grove, [SCENE DETAILS], traditional brushwork, high contrast monochrome, full-bleed edge-to-edge composition, strictly no borders, no paper frames, no deckle edges, no artist seals, no stamps, no text, no color accents, serene and dignified atmosphere.
```

Regeneration (after a failed audit): append to the prompt
`, absolutely no <failed item>` for each failed audit item, e.g.
`, absolutely no red seal, absolutely no border`.

## 5. Visual audit (Layer B — answer YES/NO after `view_image`)

1. Is the image entirely black/grey/off-white with no coloured pixels visible?
2. Does painted content reach all four edges (no border/margin/frame)?
3. Is there zero text, script, or signature anywhere?
4. Is there zero seal, stamp, chop, watermark, or logo?
5. Does the main figure match the lineage archetype (rishi: jata topknot +
   beard + beads; monk: shaved head + robe, no beads)?
6. Is only one archetype present, and does any seeker/disciple match the
   "Seeker" row for this lineage in `standards/lineage.md`?
7. Does the scene show the story's central metaphor from `[SCENE DETAILS]`?
8. Does it look hand-brushed (not 3D/CGI/photographic)?

All YES → accept. Any NO → regenerate (max 2 regenerations).

## 6. Generation route and red lines

- Allowed: Google Gemini image models only — via the OpenClaw
  `image_generate` tool, or `generate_illustration()` in
  `scripts/publish_daily_story.py` (model `gemini-3.1-flash-image`, 16:9, 2K,
  needs `GEMINI_API_KEY`). Which route the 04:00 automation uses is
  **UNVERIFIED** (not recorded in past tickets); both are allowed.
- Forbidden: `pollinations.ai`, Unsplash, stock photos, any scraper or
  non-Gemini fallback, synthetic 3D placeholders.
- On API error/timeout: retry at most 2 times (wait 30 s, then 120 s). Still
  failing → BLOCKED (see workflow). Never publish a post without its image.

## 7. Canonical reference

`docs/assets/images/posts/2026-10-07-the-smiling-snake.jpg` — rishi archetype
beneath a banyan tree, serpent by a lotus pond.
