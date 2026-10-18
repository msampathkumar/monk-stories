# Standard: Story Lineage → Character Archetype

Single source of truth for (a) which lore categories are allowed, (b) which
lineage each belongs to, and (c) which character archetype the story text and
the illustration must use. `scripts/validate_story.py` and
`scripts/next_item.py` parse the table between the `LINEAGE-TABLE` markers —
keep its column order and spelling exact.

## Lineage table

<!-- LINEAGE-TABLE:BEGIN -->
| Lore category (frontmatter) | Lineage | Archetype |
|---|---|---|
| Mahabharata | hindu | rishi |
| Vidura Neeti | hindu | rishi |
| Ramayana | hindu | rishi |
| Puranas | hindu | rishi |
| Vedas & Upanishads | hindu | rishi |
| Panchatantra | hindu | rishi |
| Panchatantra & Chanakya | hindu | rishi |
| Chanakya Neeti | hindu | rishi |
| Vemana Satakam | hindu | rishi |
| Buddhist Parables | buddhist | monk |
| Jataka Tales | buddhist | monk |
| Dhammapada | buddhist | monk |
<!-- LINEAGE-TABLE:END -->

Rules:
1. Every post's `categories` list contains **at least one** lore category from
   the table. All lore categories in one post must share one lineage.
2. To add a new lore source, add a row here first (one commit), then use it.
3. "Telugu" stories (Vemana) are `hindu` lineage.

## Archetype: `rishi` (hindu lineage)

Used in story text **and** illustration.

| Element | Required value |
|---|---|
| Teacher's name in text | "the Rishi", "the Sage", or a named sage (e.g. Vidura) |
| Hair | Matted hair in a Vedic *rishi jata* topknot |
| Face | Flowing white or grey beard; subtle tilak / vibhuti on forehead |
| Ornaments | Natural rudraksha beads (neck and/or wrists) |
| Clothing | Unstitched cotton dhoti or ascetic wrap (*uttariya*) |
| Setting | Forest ashram / hermitage hut (*parnashala*), beneath a banyan or peepal tree |
| Seeker / disciple (if shown) | Courtier, minister, or householder in dhoti/kurta and uttariya, with hair or turban — **not** a shaved-head figure in monastic robes |

Forbidden for `rishi` posts: the words "Buddhist", "bhikkhu", "shaved head" in
the post or image alt text; the word "Monk" in image alt text.

## Archetype: `monk` (buddhist lineage)

| Element | Required value |
|---|---|
| Teacher's name in text | "the Monk", "the Master", "the Bhikkhu", or the Buddha |
| Hair | Clean shaved head; no topknot |
| Ornaments | None (no rudraksha, no tilak) |
| Clothing | Draped monastic robe (*kasaya* / *sanghati*) over one or both shoulders |
| Setting | Bamboo grove, mountain monastery, stone meditation platform, quiet stream |
| Seeker / disciple (if shown) | Indian layperson or merchant of the Buddha's era; no rudraksha, no tilak, no East-Asian script or lanterns |

Forbidden for `monk` posts: the words "Rishi", "rudraksha", "tilak", "jata" in
the post or image alt text.

Never mix archetypes in one post or one image.
