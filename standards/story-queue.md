# Story Queue

Ordered backlog of classical stories for the daily post.
`scripts/next_item.py` returns the **first** row with status `[ ]` whose `Key`
does not already appear (case-insensitive) in any `docs/posts/*.md`.

Rules:
- Status `[ ]` = available. After publishing, change it to `[x] YYYY-MM-DD`
  (the post date) in the same commit as the post.
- `Lore category` must be a value from `standards/lineage.md`.
- `Locator` is where the story sits in the source text. Values marked
  `UNVERIFIED` must be checked or kept as `UNVERIFIED` in the post's Source line.
- `Key` = a distinctive term that will appear in the post; used for dedupe.
- Columns are parsed by script: keep 8 columns and the `|` separators.
- When fewer than 3 `[ ]` rows remain, run `workflows/add-queue-items.md`.

<!-- QUEUE:BEGIN -->
| Status | Slug | Story | Lore category | Source text | Locator | Key | Workplace theme |
|---|---|---|---|---|---|---|---|
| [x] 2026-10-18 | the-monkey-and-the-crocodile | The Monkey and the Crocodile | Panchatantra | Panchatantra | Book 4 (Labdhapranasham) | Crocodile | Presence of mind when a trusted ally turns on you |
| [x] 2026-10-19 | the-talkative-tortoise | The Talkative Tortoise | Jataka Tales | Jataka Tales | Kacchapa Jataka, No. 215 (UNVERIFIED) | Tortoise | Speaking at the wrong moment destroys a rescue plan |
| [x] 2026-10-20 | the-blue-jackal | The Blue Jackal | Panchatantra | Panchatantra | Book 1 (Mitra-bheda) | Blue Jackal | Impostor leaders exposed by their own nature |
| [x] 2026-10-21 | manthara-whisper | Manthara's Whisper to Kaikeyi | Ramayana | Valmiki Ramayana | Ayodhya Kanda | Manthara | The confidant who poisons a leader's judgment |
| [x] 2026-10-22 | the-parable-of-the-arrow | The Parable of the Poisoned Arrow | Buddhist Parables | Majjhima Nikaya | Cula-Malunkyovada Sutta, MN 63 | Malunkyaputta | Analysis paralysis while the incident burns |
| [x] 2026-10-23 | the-brahmin-and-the-three-thieves | The Brahmin and the Three Thieves | Panchatantra | Panchatantra | Book 3 (Kakolukiyam) | Three Thieves | Manufactured consensus and gaslighting |
| [x] 2026-10-25 | ekalavyas-thumb | Ekalavya's Thumb | Mahabharata | Mahabharata | Adi Parva | Ekalavya | Gatekeepers who demand your edge as tribute |
| [x] 2026-10-26 | the-parable-of-the-raft | The Parable of the Raft | Buddhist Parables | Majjhima Nikaya | Alagaddupama Sutta, MN 22 | Raft | Clinging to processes after they stop serving |
| [x] 2026-10-27 | the-yakshas-questions | The Yaksha's Questions | Mahabharata | Mahabharata | Vana Parva (Yaksha Prashna) | Yaksha | Answering hard questions under pressure |
| [x] 2026-10-28 | the-monkey-kings-bridge | The Monkey King's Bridge | Jataka Tales | Jataka Tales | Mahakapi Jataka, No. 407 (UNVERIFIED) | Mahakapi | The leader who becomes the bridge for the team |
| [x] 2026-10-29 | the-lion-and-the-hare | The Lion and the Hare | Panchatantra | Panchatantra | Book 1 (Mitra-bheda) | Bhasuraka | Outwitting a tyrant without open confrontation |
| [x] 2026-10-30 | the-lion-makers | The Lion Makers | Panchatantra | Panchatantra | Book 5 (Aparikshitakarakam) | Lion Makers | Brilliance without judgment builds the beast that eats you |
| [x] 2026-10-31 | angulimala-stops | Angulimala: "I Have Stopped" | Buddhist Parables | Majjhima Nikaya | Angulimala Sutta, MN 86 | Angulimala | Stopping a destructive pattern mid-career |
| [x] 2026-11-01 | karnas-armour | Karna's Armour and Indra's Request | Mahabharata | Mahabharata | Vana Parva (UNVERIFIED) | Kavacha | Generosity exploited by a calculated request |
| [x] 2026-11-02 | the-golden-geese | The Golden Geese | Jataka Tales | Jataka Tales | Suvarna Hansa Jataka, No. 136 (UNVERIFIED) | Golden Goose | Greed that turns a sustainable asset into a barren loss |
| [x] 2026-11-06 | vidura-and-dhritarashtra | Vidura's Counsel to Dhritarashtra | Mahabharata | Mahabharata | Udyoga Parva (UNVERIFIED) | ViduraCounsel | Speaking hard truths to a ruler blinded by affection |
| [x] 2026-11-03 | the-pigeon-and-the-hunter | The Pigeon and the Hunter | Panchatantra | Panchatantra | Book 1 (Mitra-bheda) (UNVERIFIED) | Pigeon | Mutual loyalty that defeats a trap |
| [x] 2026-11-05 | the-blind-men-and-the-elephant | The Blind Men and the Elephant | Buddhist Parables | Udana | Udana 6.4 (UNVERIFIED) | Blind Men | Partial perspectives presented as absolute truth |
| [x] 2026-11-04 | shvetaketu-and-aruni | Shvetaketu's Pride Humbled | Vedas & Upanishads | Chandogya Upanishad | Chapter 6 (UNVERIFIED) | Shvetaketu | Academic arrogance humbled by deeper reality |
| [x] 2026-11-07 | sibi-and-the-dove | Sibi and the Dove | Mahabharata | Mahabharata | Vana Parva (UNVERIFIED) | Sibi | Protecting a dependent at personal cost |
| [x] 2026-11-08 | the-potter-and-the-ass | The Potter and the Ass | Panchatantra | Panchatantra | Book 3 (UNVERIFIED) | PotterAss | Imitating a leader's style without understanding its mechanics |
| [x] 2026-11-09 | the-blind-turtle | The Blind Turtle and the Golden Yoke | Buddhist Parables | Majjhima Nikaya | Bala-Pandita Sutta, MN 129 (UNVERIFIED) | BlindTurtle | The extreme rarity of a rare service window |
| [x] 2026-11-10 | the-merchant-and-two-wives | The Merchant and the Two Wives | Panchatantra | Panchatantra | Book 1 (UNVERIFIED) | TwoWives | Trying to please conflicting stakeholders splits your focus |
| [x] 2026-11-11 | the-quail-and-the-fowler | The Quail and the Fowler | Jataka Tales | Jataka Tales | Vattaka Jataka, No. 35 (UNVERIFIED) | Quail | Solidarity among peers when hunted by a predator |

<!-- QUEUE:END -->
