from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from deck_helpers import (
    add_bullets,
    add_callout,
    add_footer,
    add_text,
    add_title,
    blank_slide,
    circle,
    line,
    load_theme,
    new_presentation,
    rect,
)


@dataclass
class SlideSpec:
    number: int
    title: str
    bullets: list[str]
    visual: str = ""


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text.strip()


def find_source(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("來源"):
            return strip_md(line.replace("來源：", "").replace("來源:", "")).strip()
    return ""


def find_summary(markdown: str) -> str:
    match = re.search(r"## 一句話摘要\s+(.+?)(?=\n## |\Z)", markdown, re.S)
    if not match:
        return ""
    lines = [strip_md(line) for line in match.group(1).splitlines() if strip_md(line)]
    return lines[0] if lines else ""


def parse_slides(markdown: str) -> list[SlideSpec]:
    pattern = re.compile(r"^### Slide\s+(\d+)[：:]\s*(.+?)\s*$", re.M)
    matches = list(pattern.finditer(markdown))
    slides: list[SlideSpec] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
        body = markdown[start:end]
        title = strip_md(match.group(2))
        bullets = []
        visual = ""
        for raw in body.splitlines():
            line_text = raw.strip()
            if line_text.startswith("- "):
                bullets.append(strip_md(line_text[2:]))
            elif line_text.startswith("**視覺**"):
                visual = strip_md(line_text.split("：", 1)[-1].split(":", 1)[-1])
            elif line_text.startswith("**標題**"):
                title_value = strip_md(line_text.split("：", 1)[-1].split(":", 1)[-1])
                if title_value:
                    title = title_value
            elif line_text.startswith("**副標**") and not bullets:
                bullets.append(strip_md(line_text.split("：", 1)[-1].split(":", 1)[-1]))
        slides.append(SlideSpec(int(match.group(1)), title, bullets[:6], visual))
    return slides


def add_cover(prs, theme, spec: SlideSpec, summary: str, source: str):
    slide = blank_slide(prs, "charcoal", theme)
    for x, y, d, c in [(8.6, 1.1, 0.28, "mint"), (10.9, 1.65, 0.2, "gold"), (9.65, 3.1, 0.34, "coral"), (11.2, 4.3, 0.23, "mint"), (8.2, 4.85, 0.18, "gold")]:
        circle(slide, theme, x, y, d, c)
    for a, b in [((8.74, 1.24), (11.0, 1.75)), ((11.0, 1.75), (9.82, 3.27)), ((9.82, 3.27), (11.31, 4.41)), ((9.82, 3.27), (8.29, 4.94)), ((8.74, 1.24), (9.82, 3.27))]:
        line(slide, theme, a[0], a[1], b[0], b[1], "mint", 1)
    add_text(slide, theme, spec.title, 0.78, 1.25, 6.9, 0.72, size=36, color_name="white", bold=True, font=theme.heading_font)
    subtitle = spec.bullets[0] if spec.bullets else summary
    add_text(slide, theme, subtitle[:70], 0.82, 2.15, 5.9, 0.4, size=17, color_name="cream")
    rect(slide, theme, 0.82, 3.08, 4.75, 0.9, "teal")
    add_text(slide, theme, (summary or "專業簡報摘要")[:42], 1.1, 3.35, 4.2, 0.28, size=13.5, color_name="white", bold=True)
    add_footer(slide, theme, source, dark=True)


def add_standard_slide(prs, theme, spec: SlideSpec, source: str, idx: int):
    dark = idx % 5 == 0
    slide = blank_slide(prs, "charcoal" if dark else "cream" if idx % 2 == 0 else "white", theme)
    add_title(slide, theme, spec.title, spec.visual, dark=dark)
    if len(spec.bullets) <= 3:
        colors = ["teal", "coral", "gold"]
        for i, bullet in enumerate(spec.bullets or ["補充重點待整理"]):
            add_callout(slide, theme, f"{i + 1:02}", bullet, 0.95 + i * 4.1, 1.85, 3.45, 2.95, colors[i % len(colors)])
    else:
        rect(slide, theme, 0.95, 1.65, 5.15, 4.85, "white" if not dark else "teal", line=None if dark else "line")
        add_bullets(slide, theme, spec.bullets, 1.3, 2.05, 4.3, dark=dark)
        rect(slide, theme, 7.0, 1.65, 4.9, 4.85, "pale" if not dark else "charcoal", line=None if dark else "line")
        add_text(slide, theme, "Visual Cue", 7.45, 2.0, 1.5, 0.25, size=15, color_name="teal" if not dark else "mint", bold=True)
        add_text(slide, theme, spec.visual or "用流程圖、比較圖或重點 callout 呈現", 7.45, 2.55, 3.7, 1.2, size=16, color_name="ink" if not dark else "cream")
        for i, c in enumerate(["teal", "gold", "coral", "mint"]):
            circle(slide, theme, 7.55 + i * 0.75, 4.55, 0.42, c)
            if i:
                line(slide, theme, 7.55 + (i - 1) * 0.75 + 0.42, 4.76, 7.55 + i * 0.75, 4.76, "line", 1.5)
    add_footer(slide, theme, source, dark=dark)


def add_closing(prs, theme, spec: SlideSpec, source: str):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, spec.title or "結論", "把文章轉成可行動的理解", dark=True)
    bullets = spec.bullets or ["掌握核心概念", "辨識應用場景", "規劃下一步行動"]
    add_bullets(slide, theme, bullets, 1.0, 2.1, 6.8, dark=True, size=15, gap=0.65)
    for i, (label, c) in enumerate([("理解", "teal"), ("整理", "gold"), ("應用", "coral"), ("行動", "mint")]):
        x = 8.1 + (i % 2) * 2.1
        y = 2.0 + (i // 2) * 1.75
        circle(slide, theme, x, y, 1.12, c)
        add_text(slide, theme, label, x + 0.35, y + 0.44, 0.45, 0.14, size=11.5, color_name="white", bold=True)
    add_footer(slide, theme, source, dark=True)


def build(input_md: Path, output_pptx: Path, theme_path: Path | None):
    markdown = input_md.read_text(encoding="utf-8")
    specs = parse_slides(markdown)
    if not specs:
        raise SystemExit("No slide outline found. Expected headings like: ### Slide 1：封面")
    theme = load_theme(theme_path)
    prs = new_presentation()
    source = find_source(markdown)
    summary = find_summary(markdown)
    for idx, spec in enumerate(specs):
        if idx == 0:
            add_cover(prs, theme, spec, summary, source)
        elif idx == len(specs) - 1 or "結論" in spec.title:
            add_closing(prs, theme, spec, source)
        else:
            add_standard_slide(prs, theme, spec, source, idx)
    prs.core_properties.title = specs[0].title
    prs.core_properties.subject = "Generated from article outline Markdown"
    prs.core_properties.author = "Codex article-to-presentation skill"
    output_pptx.parent.mkdir(parents=True, exist_ok=True)
    prs.save(output_pptx)
    print(output_pptx)


def main():
    parser = argparse.ArgumentParser(description="Create a PPTX deck from article outline-summary Markdown.")
    parser.add_argument("input_md", type=Path)
    parser.add_argument("output_pptx", type=Path)
    parser.add_argument("--theme", type=Path, default=None)
    args = parser.parse_args()
    build(args.input_md, args.output_pptx, args.theme)


if __name__ == "__main__":
    main()
