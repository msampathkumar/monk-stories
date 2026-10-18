---
id: ms-ke6i
status: open
deps: []
links: []
created: 2026-10-18T00:11:57Z
type: bug
priority: 1
assignee: Sampath Kumar
parent: ms-3lwv
---
# Owner decision: site not deployed; notification URLs 404

As of 2026-10-18: https://msampathkumar.github.io/monk-stories/posts/2026-10-17-the-pious-predator/ returns HTTP 404; no gh-pages branch and no .github/workflows deploy. Daily Telegram links point at a non-existent page. Also: blog plugin has blog_dir: posts but posts live in docs/posts/ not docs/posts/posts/, so they render as plain pages (site/posts/<stem>/), not blog posts with yyyy/MM/dd URLs. Owner to choose deploy method (GitHub Actions + Pages, or mkdocs gh-deploy) and whether to move posts into docs/posts/posts/ (changes URLs). Not done in review: no deploys allowed.

