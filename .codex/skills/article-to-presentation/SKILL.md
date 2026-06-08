---
name: article-to-presentation
description: Turn a web article URL, pasted article text, or Markdown file into a polished presentation package with an outline-summary Markdown file and a professional PPTX deck. Use this skill whenever the user asks to make slides, a deck, a presentation, teaching material, learning guide, briefing, or executive summary from an online article or Markdown, even if they do not explicitly mention PowerPoint. This project-local skill should coordinate with the pptx skill and use uv for any Python work.
---

# Article to Presentation

Use this project-local skill to convert a source article into a reusable presentation deliverable:

1. A structured Markdown summary for slide production.
2. A professional `.pptx` deck.
3. Optional supporting images or diagrams.
4. QA artifacts proving the deck is readable and structurally valid.

This skill captures the workflow used in this project for producing the AI Agent article deck.

## Bundled Resources

This skill includes reusable scaffolding for frequent project use:

- `templates/outline_template.md` — starting structure for the outline-summary Markdown.
- `templates/theme.json` — default professional color/font theme.
- `scripts/deck_helpers.py` — reusable `python-pptx` helpers for shapes, text, footers, callouts, and simple visual motifs.
- `scripts/create_deck_from_outline.py` — generic generator that reads the slide outline Markdown and creates an initial PPTX deck.

Use these resources as the default starting point. For article-specific decks, copy the scripts into the project `scripts/` directory and customize them, or run them directly from the skill directory for a fast first draft.

## Trigger Context

Use this skill when the user provides any of these inputs and asks for a presentation-style output:

- A web article URL.
- A Markdown file.
- Pasted article text.
- A request such as "整理成簡報", "做成投影片", "產生教學簡報", "重點與大綱", "學習指南", "briefing deck", or "presentation from this article".

If the task involves producing or editing `.pptx`, also use the `pptx` skill. This skill defines the article-to-deck workflow; `pptx` defines the PowerPoint implementation and QA requirements.

## Required Outputs

Create these files unless the user asks for a different location:

- `outputs/<topic>_outline_summary.md`
- `outputs/<topic>_deck.pptx`
- `scripts/create_<topic>_deck.py` or another reproducible generation script when creating from scratch.
- Optional: `outputs/<topic>_diagram.png` for a standalone diagram.
- Optional QA files under `outputs/qa/`.

Use clear, stable filenames derived from the article topic. Avoid overwriting unrelated files. If an output already exists, update it only when it is part of the current task.

## Environment Rules

- If Python is needed, run it through `uv`:
  - `uv run --with python-pptx python scripts/create_<topic>_deck.py`
  - `uv run --with pillow python scripts/create_<topic>_diagram.py`
  - `uv run --with defusedxml --with lxml python .codex/skills/pptx/scripts/office/validate.py outputs/<deck>.pptx`
- Do not install Python packages globally.
- Prefer project-local scripts so the deck can be regenerated.
- If browser or web access is required to read a URL, browse the source and cite the URL in the summary.

## Workflow

### 1. Capture Source Content

For a URL:

1. Open or search the URL.
2. Extract the article title, author if available, publication/update date if available, section headings, and body content.
3. Use only relevant article content. Ignore comments, recommendations, navigation, ads, and unrelated sidebar content.
4. Preserve the source URL in the Markdown output and in a small deck footer or source note.

For Markdown or pasted text:

1. Read the file or pasted content.
2. Treat frontmatter, headings, tables, code blocks, and image references as part of the source structure.
3. Keep original terminology unless the user asks for translation or simplification.

When source access fails, ask for the article text or Markdown rather than inventing content.

### 2. Build the Outline Summary Markdown

The Markdown is the planning artifact. It should be useful even without the deck.

Use this structure:

```markdown
# [Source Title]: 簡報大綱摘要與學習指南

來源：[title/author/date/url]

## 一句話摘要

## 核心重點

## 簡報敘事線

## 投影片大綱

### Slide 1：[title]
**重點**：
- ...

## 學習指南

### 入門順序
### 推薦練習題
### 學習檢核問題
```

For business articles, replace `學習指南` with `行動建議` or `決策指南` when that better fits the audience. For technical or educational articles, keep the learning-guide framing.

### 3. Plan the Deck

Choose a deck structure based on the source:

- 8-12 slides for short articles.
- 12-18 slides for dense technical articles.
- Add section-divider slides only when they improve navigation.
- Include one clear visual idea per slide: diagram, process flow, comparison, callout, matrix, timeline, or icon-based layout.

Use this default sequence for educational/technical articles:

1. Cover.
2. Why the topic matters now.
3. Core definition or concept.
4. Main principles or capabilities.
5. Architecture/process overview.
6. Detailed breakdown slides.
7. Example or use case.
8. Tools/frameworks/methods.
9. Challenges/risks.
10. Learning guide or action plan.
11. Conclusion.

### 4. Design the Deck

Follow the `pptx` skill design guidance. In this project, prefer:

- 16:9 layout.
- A distinctive visual motif tied to the article, such as loops, networks, workflows, architecture maps, or decision paths.
- A palette with one dominant dark or light base, 1-2 supporting colors, and one accent.
- Strong contrast and generous margins.
- No plain text-only slides.
- No copied screenshots as the only visual when a diagram can be redrawn as editable shapes.

For Chinese decks, use readable system fonts such as `Aptos`, `Aptos Display`, `PingFang TC`, `Heiti TC`, or available project fonts. Keep body text concise enough to avoid wrapping into cramped boxes.

### 5. Create Reproducible PPTX

When creating from scratch:

1. Start from the bundled generator when the outline Markdown follows this skill's format:
   `uv run --with python-pptx python .codex/skills/article-to-presentation/scripts/create_deck_from_outline.py outputs/<topic>_outline_summary.md outputs/<topic>_deck.pptx --theme .codex/skills/article-to-presentation/templates/theme.json`
2. If the deck needs a richer custom design, copy the bundled scripts into project `scripts/` and customize:
   - `.codex/skills/article-to-presentation/scripts/deck_helpers.py`
   - `.codex/skills/article-to-presentation/scripts/create_deck_from_outline.py`
3. Use `python-pptx` via `uv` when Node/PptxGenJS is unavailable.
4. Keep helper functions for repeated shapes, text boxes, footers, colors, and diagrams.
5. Use editable shapes for architecture diagrams and flows when possible.
6. Store generated deck in `outputs/`.

The bundled generator is intended to produce a strong first draft, not the final ceiling. After generation, inspect the deck and customize dense slides, architecture diagrams, and article-specific visuals as needed.

When the user provides a template deck:

1. Use the `pptx` skill editing workflow.
2. Analyze the template visually before editing.
3. Preserve template styling unless the user asks for a redesign.

### 6. Add Article-Specific Diagrams

If the source article includes an important diagram or screenshot:

- Recreate a similar diagram as a new visual, unless the user explicitly asks to preserve the screenshot.
- Keep the structure and teaching intent, but do not simply paste or trace the source image.
- Export a standalone PNG when useful, and include the diagram in the deck as editable shapes or a generated image.
- Add 1-3 explanatory slides if the diagram contains multiple concepts.

### 7. QA Requirements

Run at least these checks before final response:

1. Content check:
   - Confirm slide count and slide titles.
   - Check there are no placeholder strings such as `lorem`, `ipsum`, `xxxx`, `placeholder`.
   - Confirm the source is cited in the Markdown and deck.

2. Structure check:
   - Run `unzip -t outputs/<deck>.pptx`.
   - Run the pptx skill validator when possible:
     `uv run --with defusedxml --with lxml python .codex/skills/pptx/scripts/office/validate.py outputs/<deck>.pptx`

3. Visual check:
   - Prefer full slide rendering with LibreOffice/soffice and `pdftoppm` when available.
   - If LibreOffice is unavailable on macOS, use `qlmanage -t` for thumbnail sanity checks.
   - Inspect at least the cover, the densest content slide, and any newly added diagram slide.
   - If a visual issue is found, fix and re-check the affected slide.

Report any QA limitation plainly, for example: "LibreOffice was not available, so I used Quick Look thumbnails instead of full per-slide rendering."

## Final Response

Keep the final response concise and include:

- The Markdown path.
- The PPTX path.
- Any standalone diagram/image path.
- A short QA summary.
- Any limitation, such as inability to render full slide images.

Use clickable local file links when possible.

## Example Prompts

**URL input**

> 請把這篇文章 https://example.com/article 的重點、大綱、學習指南整理成 Markdown，並做成專業簡報。

**Markdown input**

> 請把 `notes/agent-overview.md` 做成一份給主管看的 12 頁簡報，保留一份簡報大綱摘要。

**Diagram expansion**

> 這張截圖是文章裡的架構圖，請重畫一張相似圖，並新增 3 頁說明到簡報裡。
