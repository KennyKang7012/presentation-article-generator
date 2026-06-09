# Repository Guidelines

## Project Structure & Module Organization

This repository turns article outlines into reproducible PowerPoint decks.

- `scripts/`: Python generation scripts, one per article/deck, named `create_<topic>_deck.py`.
- `outputs/`: committed deliverables, including `<topic>_outline_summary.md` and generated `.pptx` files.
- `outputs/qa/`: local render/thumbnail checks; ignored by Git.
- `.codex/skills/`: local skill packages and helper scripts used for deck, PDF, DOCX, and article-to-presentation workflows.

When adding a new article, create the outline summary first, then add a matching deck script and generated deck under `outputs/`.

## Build, Test, and Development Commands

Run scripts with `uv` and declare dependencies inline:

```bash
uv run --with python-pptx python scripts/create_termdock_agent_skills_deck.py
```

Regenerate another deck by replacing the script path, for example:

```bash
uv run --with python-pptx python scripts/create_ai_agent_deck.py
```

Validate generated PPTX files before committing:

```bash
unzip -t outputs/<deck>.pptx
uv run --with defusedxml --with lxml python .codex/skills/pptx/scripts/office/validate.py outputs/<deck>.pptx
qlmanage -t -s 1400 -o outputs/qa outputs/<deck>.pptx
```

`unzip` checks package integrity, the XML validator catches Office-format issues, and `qlmanage` creates visual QA thumbnails.

## Coding Style & Naming Conventions

Use Python with 4-space indentation and small helper functions for repeated slide primitives. Keep deck constants near the top of each script, including `OUT`, `WIDE`, and `COLORS`. Prefer descriptive snake_case function names such as `add_footer`, `add_text`, and `create_timeline_slide`. Keep output filenames aligned with script names and topic slugs.

## Testing Guidelines

There is no formal unit-test suite yet. Treat PPTX regeneration plus the three validation commands above as the required test path. Inspect `outputs/qa/` thumbnails for layout regressions, clipped text, unreadable contrast, and inconsistent spacing before committing deck changes.

## Commit & Pull Request Guidelines

Use Taiwan Traditional Chinese for commit messages and repository-related conversation.
Recent commits use concise Traditional Chinese messages beginning with `新增`, for example `新增 README 說明文件` and `新增文章轉簡報技能包與簡報產物`. Follow that direct, outcome-focused style.

Pull requests should include the source article or outline used, the generated files changed, validation commands run, and screenshots or QA thumbnails when slide layout changed. Note any intentional visual style changes separately from content edits.

## Security & Configuration Tips

Do not commit macOS metadata, local virtual environments, temporary Office extraction folders, or `outputs/qa/` artifacts. Keep article sources and summaries in Markdown so deck generation remains reviewable and reproducible.
