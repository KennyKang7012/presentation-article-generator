# presentation-article-generator

把文章整理成可重跑的簡報產生器。這個專案會把來源文章轉成兩份主要產物：

1. `outputs/<topic>_outline_summary.md`
2. `outputs/<topic>_deck.pptx`

同時也保留對應的生成腳本，方便之後重新產生或微調版型。

## 目前產物

- `outputs/ai_agent_outline_summary.md`
- `outputs/ai_agent_intro_deck.pptx`
- `outputs/91app_ai_agent_outline_summary.md`
- `outputs/91app_ai_agent_deck.pptx`
- `outputs/iii_ai_agent_architecture_outline_summary.md`
- `outputs/iii_ai_agent_architecture_deck.pptx`
- `outputs/gyoza_agent_skills_outline_summary.md`
- `outputs/gyoza_agent_skills_deck.pptx`
- `outputs/termdock_agent_skills_outline_summary.md`
- `outputs/termdock_agent_skills_deck.pptx`

QA 縮圖與單頁檢查檔會放在 `outputs/qa/`，這個資料夾已加入 `.gitignore`。

## 專案結構

```text
outputs/    文章大綱、PPTX、QA 產物
scripts/    各文章對應的簡報生成腳本
.codex/     專案內使用的技能與模板
AGENTS.md   貢獻者指南與協作規範
```

## 如何重新產生簡報

以 `uv` 執行對應腳本即可：

```bash
uv run --with python-pptx python scripts/create_termdock_agent_skills_deck.py
```

其他文章也可以替換成對應腳本：

```bash
uv run --with python-pptx python scripts/create_iii_ai_agent_architecture_deck.py
uv run --with python-pptx python scripts/create_gyoza_agent_skills_deck.py
uv run --with python-pptx python scripts/create_91app_ai_agent_deck.py
uv run --with python-pptx python scripts/create_ai_agent_deck.py
```

## 驗證方式

產生完 PPTX 後，建議做三個檢查：

1. 壓縮結構檢查

```bash
unzip -t outputs/<deck>.pptx
```

2. Office XML 驗證

```bash
uv run --with defusedxml --with lxml python .codex/skills/pptx/scripts/office/validate.py outputs/<deck>.pptx
```

3. 視覺檢查

```bash
qlmanage -t -s 1400 -o outputs/qa outputs/<deck>.pptx
```

## 備註

- 這些簡報是由文章內容整理而來，不是直接截圖。
- 來源文章與摘要會保留在各自的 `outline_summary.md` 裡。
- 若要新增新文章，建議先建立對應的 outline summary，再補生成腳本與 PPTX。
