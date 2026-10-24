Template for the final `tk add-note <id> "..."` of workflows/publish-daily-story.md.
Copy the block, fill every {{slot}}, pass it as one quoted argument.

```
PUBLISHED {{DATE}} {{SLUG}}
post: docs/posts/{{DATE}}-{{SLUG}}.md ({{WORDS}} words)
image: docs/assets/images/posts/{{DATE}}-{{SLUG}}.jpg ({{W}}x{{H}}, generations: {{N}})
queue item: {{STORY}} | lore: {{LORE}} | archetype: {{ARCHETYPE}}
Layer A: validate_story PASS; validate_image PASS; check_duplicate PASS; mkdocs build OK
Visual audit (standards/art.md §5): 1 {{Y}} 2 {{Y}} 3 {{Y}} 4 {{Y}} 5 {{Y}} 6 {{Y}} 7 {{Y}} 8 {{Y}}
Story rubric: 1 {{Y}} "{{quote}}" | 2 {{Y}} "{{quote}}" | 3 {{Y}} | 4 {{Y}} | 5 {{Y}} | 6 {{Y}} | 7 {{Y}} | 8 {{Y}} | 9 {{Y}}
```
