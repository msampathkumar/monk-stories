# Monk Stories Art Style Guide

This document defines the strict visual identity, artistic principles, character guidelines, and prompt formulas for all illustrations in **Monk Stories**.

---

## 1. Visual & Aesthetic Identity

| Attribute | Specification |
| :--- | :--- |
| **Medium** | Traditional Indian ink wash painting / Kalamkari brushwork on textured off-white paper. |
| **Color Palette** | **Strictly 100% monochrome:** Deep Indian ink black, diluted charcoal washes, soft gray mid-tones, and off-white background. Absolutely NO color accents (no red, gold, yellow, saffron, or green). |
| **Framing** | **Full-bleed canvas from edge to edge.** The artwork must extend directly to all four borders of the image file without any artificial margins. |
| **Brushwork** | Expressive, fluid Indian brush strokes with visible ink bleed, organic bristle texture, and dynamic contrast (*shunya* / negative space). |
| **Tone** | Contemplative, dignified, austere, and timeless. |

---

## 2. Character Representation: Context-Aware Archetypes

Character depiction is strictly matched to the story's philosophical lineage:

### A. Hindu & Vedic Stories (Mahabharata, Ramayana, Puranas, Vedas, Satakams, Chanakya, Vidura)
Depict authentic **Vedic Hindu Sages (Rishis, Munis, Acharyas)**:
- **Hair**: Matted ascetic hair gathered into a traditional **Vedic Rishi Jata (topknot)**.
- **Beard**: Flowing, natural ascetic white/gray beard.
- **Attire**: Simple unstitched cotton **dhoti** or ascetic wrap (*uttariya*).
- **Sacred Ornaments**: Natural **Rudraksha beads** (*mala*) on neck and wrists.
- **Tilak**: Subtle sacred forehead markings (**Vibhuti / Bhasma** lines or sandalwood tilak).
- **Setting**: Forest hermitage (*Ashram / Tapovan*), beneath an ancient **Banyan** or **Peepal** tree, hermitage thatched huts (*parnashala*), river banks, stone steps.

### B. Buddhist & Zen Stories (Jataka Tales, Dhammapada, Akkosa Sutta)
Depict authentic **Buddhist Monks (Bhikkhus, Masters)**:
- **Appearance**: Clean shaved head, serene calm countenance, no beads or topknot.
- **Attire**: Simple monastic robe (*kasaya* / *sanghati*) draped over one or both shoulders.
- **Setting**: Bamboo groves, mountain monasteries, stone meditation platforms, quiet streams.

---

## 3. Standard AI Prompt Formulas (Gemini API)

### Base Formula for Vedic/Hindu Stories:
```text
A minimalist ink wash painting, black and white brush stroked artwork with authentic Indian aesthetic, an ancient Hindu sage (Rishi) with serene expression, long flowing beard, hair tied in a Vedic rishi jata topknot, wearing simple ascetic dhoti and natural rudraksha beads, subtle tilak on forehead, sitting under an ancient banyan tree outside a forest ashram hermitage, [SCENE DETAILS], traditional Indian brushwork, high contrast monochrome, full-bleed edge-to-edge composition, contemplative and dignified atmosphere.
```

### Base Formula for Buddhist/Zen Stories:
```text
A minimalist ink wash painting, black and white brush stroked artwork with authentic ancient aesthetic, a serene Buddhist monk with shaved head and draped monastic robes, sitting calmly in quiet contemplation, [SCENE DETAILS], traditional brushwork, high contrast monochrome, full-bleed edge-to-edge composition, serene and dignified atmosphere.
```

---

## 4. Absolute Invariant Negative Constraints (Hard Guardrails)

All prompt generation must explicitly enforce these negative rules:
- ❌ **NO Borders or Frames:** No paper-cut frames, torn paper borders, deckle edges, mounting frames, white borders, or margins around the art.
- ❌ **NO Stamps or Seals:** No red artist seal stamps, Chinese/Japanese Hanko chops, red square seals, or colored emblems.
- ❌ **NO Text or Typography:** No Devanagari text, calligraphy quotes, signatures, or inscriptions painted on the canvas.
- ❌ **NO Color Accents:** No colored dome washes (no gold/yellow), no red ink, strictly 100% monochrome black and white.
- ❌ **NO 3D or Watermarks:** No CGI rendering, plastic skin, 3D video game aesthetic, watermarks, or logos.
- ❌ **NO Scraper Fallbacks:** Never route image requests to external services like `pollinations.ai`. Use only official Gemini models.

---

## 5. Canonical Reference Image

- **Pilot Post Image:** `docs/assets/images/posts/2026-10-07-the-smiling-snake.jpg`
- Depicts: Full-bleed authentic Vedic Rishi seated peacefully beneath the banyan tree, observing the serpent by the lotus pond.
