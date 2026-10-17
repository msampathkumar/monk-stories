---
name: monk-art-generator
description: "Generates authentic, full-bleed monochrome ink wash illustrations for Monk Stories using the Google Gemini image generation API, strictly eliminating paper frames, seals, stamps, text, and foreign artifacts."
---

# Monk Stories Art Generator Skill

Use this skill when generating, inspecting, or regenerating wisdom parable illustrations for the `monk-stories` repository.

## 1. Visual Directives & Aesthetic Rules

- **Medium:** Minimalist monochrome ink wash painting with authentic Indian Kalamkari and brush-stroke aesthetic.
- **Palette:** Strictly 100% black and white. Deep Indian ink black, diluted grayscale washes, clean off-white negative space. Absolutely zero color accents (no red, gold, saffron, or yellow).
- **Composition:** Full-bleed canvas from edge to edge. The artwork must extend directly to the border of the image file.
- **Negative Invariants (Zero Tolerance):**
  - ❌ NO paper-cut frames, deckle edges, torn parchment borders, or mounting margins.
  - ❌ NO red artist seals, Hanko stamps, Chinese/Japanese chop marks, or colored emblems.
  - ❌ NO text, calligraphy quotes, signatures, or pseudo-Devanagari inscriptions.
  - ❌ NO watermarks, logos, or third-party branding.
  - ❌ NO 3D rendering, CGI gloss, plastic skin, or Western medieval backdrops.

## 2. Character Archetypes by Cultural Lineage

- **Hindu / Vedic / Telugu Lore (Mahabharata, Ramayana, Puranas, Vemana, Chanakya, Vidura):**
  - Authentic Hindu Sage (Rishi / Muni).
  - Matted hair gathered in a Vedic *rishi jata* topknot.
  - Flowing ascetic beard, serene and dignified expression.
  - Simple cotton ascetic *dhoti* and natural *rudraksha* beads.
  - Subtle *tilak* / *vibhuti* on forehead.
  - Setting: Beneath an ancient Banyan or Peepal tree outside an ashram hermitage (*parnashala*).

- **Buddhist / Zen Lore (Jataka Tales, Dhammapada, Akkosa Sutta):**
  - Authentic Buddhist Monk (Bhikkhu).
  - Shaved head, serene calm countenance, no beads or topknot.
  - Simple monastic robe (*sanghati* / *kasaya*) draped over shoulder.
  - Setting: Bamboo grove, stone meditation slab, quiet stream.

## 3. Gemini Generation Protocol

Always generate using the official Google Gemini image API (`gemini-3.1-flash-image` or configured Gemini image model) with `aspectRatio: '16:9'` and `imageSize: '2K'`.

```python
import os, requests, base64

def generate_monk_art(prompt: str, output_path: str):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is required.")
        
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent?key={key}"
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "2K"
            }
        }
    }
    
    res = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=120)
    res.raise_for_status()
    data = res.json()
    
    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline:
                b64 = inline.get("data")
                with open(output_path, "wb") as f:
                    f.write(base64.b64decode(b64))
                return output_path
    raise RuntimeError("No image returned from Gemini API")
```

## 4. Mandatory Post-Generation Verification

Every generated image MUST be visually inspected with `view_image` before committing:
1. Verify character archetype matches lineage.
2. Confirm canvas is full-bleed with no white/parchment border margin.
3. Confirm absence of red stamps, watermarks, and text.
4. If defective, re-roll immediately with strengthened negative constraints.
