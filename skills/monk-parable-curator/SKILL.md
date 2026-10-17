---
name: monk-parable-curator
description: "Curates, drafts, and formats daily wisdom parables for Monk Stories, extracting high-leverage lessons from classical Indian lore and adapting them to modern organizational dynamics."
---

# Monk Stories Parable Curator Skill

Use this skill when researching, drafting, structuring, or updating parables for the `monk-stories` repository.

## 1. Wisdom Sources & Philosophical Roots

Draw exclusively from authentic classical sources available in `~/books/` or established Indian philosophical literature:
- **Vidura Neeti / Mahabharata:** Navigating toxic courts, corrupted boards, sycophancy, silent boundaries, Shalya-vritti (demoralization).
- **Chanakya Neeti / Arthashastra:** Power dynamics, strategic realism, poison in the milk (sweet saboteurs), containment.
- **Vemana Satakam:** Moral directness, the scorpion's tail (innate malice), empty boasters vs quiet competence.
- **Ramayana (Vibhishana, Hanuman, Sugriva):** Ethical thresholds, knowing when to walk away from toxic leadership, unwavering service.
- **Buddhist Parables (Akkosa Sutta, Jatakas, Dhammapada):** Deflecting insults (the unaccepted gift), non-reactive composure, quiet detachment.

## 2. Narrative Structure

Every post must follow the five-part architecture:
1. **The Tension / The Approach:** A courtier, counselor, or minister arrives at the hermitage burdened by a modern-mirroring crisis.
2. **The Rishi's / Monk's Observation:** A grounded physical metaphor in the hermitage (a banyan root, a clay pot, milk, a scorpion, a stone pillar).
3. **The Ancient Doctrine:** The verse or aphorism explained through timeless psychological realism.
4. **The Corporate / Workplace Mirror:** Direct, actionable translation into modern engineering, executive leadership, or organizational politics.
5. **The Provocation:** A sharp, unforgettable closing aphorism or question that lingers with the reader.

## 3. Formatting & Metadata Rules

- **Location:** `docs/posts/YYYY-MM-DD-slug.md`
- **Frontmatter:**
```yaml
---
date: YYYY-MM-DD
authors:
  - monk
categories:
  - Office Politics
  - <Lore Source, e.g. Mahabharata / Chanakya Neeti>
  - Power & Strategy
tags:
  - <Specific theme, e.g. Toxic Leadership>
  - Emotional Intelligence
  - Ancient Wisdom
---
```
- **Image Embed:** Must immediately follow the title header:
```markdown
# Title of the Story

![Alt Text describing the scene](../assets/images/posts/YYYY-MM-DD-slug.jpg)
```
- **Language & Tone:** Serious, dignified, psychologically astute. Strictly no corporate clichés, no buzzwords, and zero AI slop.
