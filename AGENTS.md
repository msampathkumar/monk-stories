# AGENTS.md — Monk Stories Operational Rules & Workflows

## 1. Repository Mission & Identity
**Monk Stories** publishes daily timeless philosophical parables grounded in classical Indian traditions (Mahabharata, Ramayana, Puranas, Vemana Satakam, Chanakya Neeti, Vidura Neeti, and Buddhist Akkosa Sutta/Jatakas), adapted to modern organizational psychology and executive presence.

Publications run daily at **04:00 AM IST (22:30 UTC)** via MkDocs Material.

---

## 2. Dedicated Agent Roles
- **Katha (Parable Curator & Scribe):** Researches classical lore from `~/books/`, extracts psychological mechanisms, and authors structured Markdown parables following the `monk-parable-curator` skill.
- **Chitra (Monochrome Art Director & Quality Gatekeeper):** Translates the story's core metaphor into authentic Indian brushwork prompts, invokes our Gemini image generation engine, audits the output against visual invariants, and enforces zero-defect quality before publication.

---

## 3. Strict Rules & Red Lines

### Rule 1: Zero External Fallback Scrapers (Hard Red Line)
- **NEVER** call `pollinations.ai`, Unsplash, or any unauthorized external generation/scraping endpoint.
- **ALWAYS** use our own Google Gemini API (`gemini-3.1-flash-image` via `GEMINI_API_KEY`).
- If an API call fails or times out, retry with exponential backoff or alert the operator. Do not substitute synthetic 3D fallbacks.

### Rule 2: Pure Monochrome Full-Bleed Aesthetics
- All illustrations must be **100% black and white ink wash**. No red stamps, no yellow/gold dome washes, no color accents.
- All illustrations must be **full-bleed edge-to-edge**.
- **Forbidden Artifacts:**
  - ❌ Paper-cut frames, torn paper, deckle edges, border margins, or mounting frames.
  - ❌ Chinese/Japanese Hanko chop marks, red artist seal stamps, or red square seals.
  - ❌ Devanagari calligraphy text, inscriptions, signatures, or quotes painted on the canvas.
  - ❌ Third-party watermarks or logos.

### Rule 3: Character Lineage Alignment
- **Hindu, Vedic, and Telugu Stories:** Depict authentic **Vedic Hindu Sages (Rishis/Munis)** with ascetic matted hair (*rishi jata* topknot), flowing beard, natural rudraksha beads, subtle forehead tilak/vibhuti, unstitched cotton dhoti, seated beneath an ancient Banyan or Peepal tree outside a forest ashram hermitage (*parnashala*).
- **Buddhist & Zen Stories:** Depict authentic **Buddhist Monks (Bhikkhus)** with clean shaved heads and draped monastic robes (*kasaya*). Never mix traditions.

### Rule 4: Mandatory Pre-Commit Visual Verification
- Every generated image MUST be inspected via `view_image` before being committed to Git.
- Confirm full-bleed framing, authentic archetype, absence of seals/frames/text, and pure monochrome palette.

### Rule 5: Task-Centric Execution (`tk`)
- Every daily run and maintenance task must begin with `tk create`, proceed with `tk start`, log progress with `tk add-note`, and finish with `tk close`, committing `.tickets/` with the changes.

---

## 4. Layered Workflows

```
[1. Katha Sourcing] 
     ↓ Read classical wisdom from ~/books/ (Vemana, Chanakya, Vidura, Ramayana)
[2. Katha Drafting]
     ↓ Draft 5-part parable in docs/posts/YYYY-MM-DD-<slug>.md
[3. Chitra Art Direction]
     ↓ Compose hardened prompt with explicit negative constraints
[4. Gemini Generation]
     ↓ Call gemini-3.1-flash-image (16:9 widescreen, 2K resolution)
[5. Quality Audit]
     ↓ Inspect via view_image: verify full-bleed, monochrome, zero seals/frames
[6. Site Build & DR]
     ↓ .venv/bin/mkdocs build → tk close → git commit & push to origin master
```
