from pathlib import Path
import sys

sys.path.append(str(Path(".codex/skills/article-to-presentation/scripts").resolve()))

from pptx.enum.text import PP_ALIGN

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


OUT = Path("outputs/termdock_agent_skills_deck.pptx")
SOURCE = "Termdock｜Danny Huang｜2026-03-16｜termdock.com/blog/agent-skills-guide/zh"


def cover(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    nodes = [
        (8.0, 1.1, "SKILL.md", "teal"),
        (10.15, 1.55, "490K+", "gold"),
        (9.25, 3.2, "Agent", "coral"),
        (11.1, 4.6, "Security", "mint"),
        (8.0, 5.25, "Team", "teal"),
    ]
    for a, b in [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (4, 3)]:
        x1, y1, _, _ = nodes[a]
        x2, y2, _, _ = nodes[b]
        line(slide, theme, x1 + 0.55, y1 + 0.28, x2 + 0.55, y2 + 0.28, "mint", 1.1)
    for x, y, label, fill in nodes:
        rect(slide, theme, x, y, 1.15, 0.56, fill)
        add_text(slide, theme, label, x + 0.08, y + 0.18, 0.98, 0.12, size=8.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "2026 Agent Skills\n完全指南", 0.78, 1.05, 6.2, 1.28, size=34, color_name="white", bold=True, font=theme.heading_font)
    add_text(slide, theme, "建立、分享與保護 AI Agent 能力", 0.82, 2.72, 5.5, 0.3, size=16.5, color_name="cream")
    rect(slide, theme, 0.82, 3.48, 4.95, 0.92, "teal")
    add_text(slide, theme, "從 SKILL.md 格式、跨 Agent 相容，到供應鏈安全與團隊治理", 1.08, 3.76, 4.42, 0.18, size=10.8, color_name="white", bold=True)
    add_footer(slide, theme, SOURCE, dark=True)


def why_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "為什麼需要 Skills", "強大的模型不知道你的 style guide、deploy pipeline 與合規要求")
    rect(slide, theme, 0.95, 1.75, 5.25, 3.8, "white", line="line")
    rect(slide, theme, 7.1, 1.75, 5.25, 3.8, "charcoal")
    add_text(slide, theme, "沒有 Skill", 1.28, 2.18, 1.7, 0.22, size=16.5, color_name="coral", bold=True)
    add_bullets(slide, theme, ["像沒讀過 style guide 的天才新人", "能力強，但每次即興產出", "不懂團隊規範與部署約束"], 1.35, 2.95, 4.1, size=12.2, gap=0.48)
    add_text(slide, theme, "有 Skill", 7.43, 2.18, 1.7, 0.22, size=16.5, color_name="gold", bold=True)
    add_bullets(slide, theme, ["把 context 編碼一次", "讓 agent 每次套用相同流程", "把通用智慧變成具體好用"], 7.5, 2.95, 4.1, dark=True, size=12.2, gap=0.48)
    add_footer(slide, theme, SOURCE)


def what_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Agent Skill 是什麼", "一個資料夾、一份 SKILL.md，加上可選的 scripts、參考資料與範例")
    rect(slide, theme, 1.0, 1.75, 3.15, 4.1, "charcoal")
    add_text(slide, theme, "skill-folder/", 1.3, 2.13, 1.6, 0.2, size=13.2, color_name="gold", bold=True)
    for i, (name, tag) in enumerate([("SKILL.md", "必要"), ("scripts/", "選配"), ("references/", "選配"), ("examples/", "選配")]):
        y = 2.85 + i * 0.62
        rect(slide, theme, 1.3, y, 2.1, 0.36, "white")
        add_text(slide, theme, name, 1.45, y + 0.11, 1.0, 0.08, size=8.4, color_name="ink", bold=True)
        add_text(slide, theme, tag, 2.67, y + 0.11, 0.45, 0.08, size=7.4, color_name="coral", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "AI agent 的 npm", 5.15, 2.0, 3.4, 0.35, size=22, color_name="teal", bold=True)
    add_bullets(slide, theme, ["npm 套件匯出可複用程式碼。", "Skill 匯出可複用流程、約束與領域知識。", "不需要編譯、runtime 或 dependency graph。"], 5.2, 3.0, 6.3, size=13.3, gap=0.58)
    add_footer(slide, theme, SOURCE)


def format_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "SKILL.md 格式", "YAML 給機器判斷，Markdown 給 Agent 執行")
    rect(slide, theme, 0.95, 1.65, 5.45, 4.55, "white", line="line")
    rect(slide, theme, 6.92, 1.65, 5.45, 4.55, "charcoal")
    add_text(slide, theme, "YAML Frontmatter", 1.25, 2.08, 2.55, 0.22, size=16.5, color_name="teal", bold=True)
    add_bullets(slide, theme, ["name：小寫連字號，最長 64 字元", "description：觸發器，最長 1,024 字元", "allowed-tools / metadata / license：選配"], 1.28, 2.9, 4.3, size=11.2, gap=0.52)
    add_text(slide, theme, "Markdown Body", 7.22, 2.08, 2.45, 0.22, size=16.5, color_name="gold", bold=True)
    add_bullets(slide, theme, ["Instructions：任務流程", "Conventions：團隊規範", "Example：可複製的範例", "Rules：不可違反的約束"], 7.25, 2.9, 4.0, dark=True, size=11.2, gap=0.52)
    add_footer(slide, theme, SOURCE)


def description_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Description 決定觸發率", "它是反向搜尋查詢：agent 在 skill 庫中搜尋相關性")
    rect(slide, theme, 0.95, 1.9, 5.25, 3.55, "pale", line="line")
    rect(slide, theme, 7.1, 1.9, 5.25, 3.55, "charcoal")
    add_text(slide, theme, "太泛", 1.28, 2.35, 1.0, 0.22, size=16, color_name="coral", bold=True)
    add_text(slide, theme, '"code review"', 1.45, 3.2, 3.5, 0.2, size=16, color_name="muted", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "問題：觸發意圖模糊，agent 不知道哪些請求該匹配。", 1.42, 4.05, 3.55, 0.38, size=11, color_name="muted", align=PP_ALIGN.CENTER)
    add_text(slide, theme, "具體", 7.43, 2.35, 1.0, 0.22, size=16, color_name="gold", bold=True)
    add_text(slide, theme, "Perform thorough code review with focus on security, performance, and maintainability.", 7.55, 3.0, 4.3, 0.42, size=11.4, color_name="cream", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "方向：任務、方法、輸出格式越清楚，觸發越穩。", 7.55, 4.16, 4.3, 0.28, size=11, color_name="cream", align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def progressive_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "漸進式揭露", "把初始 context window 成本壓到最低")
    steps = [
        ("01", "Frontmatter", "永遠載入，成本極低"),
        ("02", "SKILL.md Body", "相關時才載入完整指令"),
        ("03", "外部檔案 / Scripts", "需要時才讀取或執行"),
    ]
    for i, (num, title, body) in enumerate(steps):
        x = 1.0 + i * 4.1
        fill = "charcoal" if i == 1 else "white"
        rect(slide, theme, x, 2.0, 3.3, 3.25, fill, line=None if i == 1 else "line")
        add_text(slide, theme, num, x + 0.28, 2.35, 0.55, 0.2, size=15, color_name="gold" if i == 1 else "coral", bold=True)
        add_text(slide, theme, title, x + 0.28, 3.0, 2.0, 0.25, size=15.5, color_name="white" if i == 1 else "ink", bold=True)
        add_text(slide, theme, body, x + 0.28, 3.72, 2.35, 0.42, size=11.2, color_name="cream" if i == 1 else "muted")
        if i < 2:
            line(slide, theme, x + 3.3, 3.6, x + 4.1, 3.6, "teal", 2.0)
    add_text(slide, theme, "安裝數十個 skill 時，只有匹配任務的少數 skill 進入完整 context。", 1.1, 6.1, 11.1, 0.25, size=13.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def ecosystem_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "490K+ Skill 生態系", "從概念到標準基礎設施，時間以月計")
    cards = [
        ("SkillsMP", "400K+", "數量霸主；爬取 GitHub SKILL.md 並做語意搜尋。", "teal"),
        ("Skills.sh", "83K+ / 8M+", "Vercel 推出；CLI 原生安裝、排行榜、Snyk 掃描。", "gold"),
        ("ClawHub", "~10K+", "開放平台；ClawHavoc 事件成為安全反例。", "coral"),
    ]
    for i, (name, stat, body, accent) in enumerate(cards):
        x = 0.9 + i * 4.15
        rect(slide, theme, x, 1.95, 3.45, 3.55, "charcoal" if i == 1 else "pale", line=None if i == 1 else "line")
        add_text(slide, theme, stat, x + 0.3, 2.35, 2.4, 0.32, size=22, color_name="gold" if i == 1 else "coral", bold=True)
        add_text(slide, theme, name, x + 0.3, 3.1, 2.4, 0.22, size=16, color_name="white" if i == 1 else "ink", bold=True)
        add_text(slide, theme, body, x + 0.3, 3.85, 2.55, 0.68, size=10.4, color_name="cream" if i == 1 else "muted")
    add_footer(slide, theme, SOURCE)


def build_first_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "建立第一個 Skill", "五分鐘版本：建目錄、寫 SKILL.md、測試、優化 description")
    steps = [
        ("01", "建目錄", "~/.claude/skills/ 或專案 .claude/skills/"),
        ("02", "寫 SKILL.md", "定義流程、輸出格式與規則"),
        ("03", "測試觸發", '例如：claude "review the changes"'),
        ("04", "優化描述", "用測試 query 驗證觸發可靠性"),
    ]
    for i, (num, title, body) in enumerate(steps):
        x = 0.95 + i * 3.1
        rect(slide, theme, x, 2.05, 2.45, 2.85, "white", line="line")
        add_text(slide, theme, num, x + 0.25, 2.38, 0.5, 0.18, size=14.5, color_name="coral", bold=True)
        add_text(slide, theme, title, x + 0.25, 3.0, 1.55, 0.2, size=14.8, color_name="ink", bold=True)
        add_text(slide, theme, body, x + 0.25, 3.65, 1.8, 0.5, size=9.7, color_name="muted")
        if i < 3:
            line(slide, theme, x + 2.45, 3.45, x + 3.1, 3.45, "teal", 2.0)
    add_footer(slide, theme, SOURCE)


def cross_agent_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "跨 Agent 使用 Skill", "同一份核心 SKILL.md，可在 Claude Code、Codex CLI、Copilot 間流動")
    rows = [
        ("Claude Code", "~/.claude/skills/\n.claude/skills/", "個人、專案、Marketplace"),
        ("Codex CLI", ".agents/skills/\n.codex/skills/", "$skill-installer 與官方 catalog"),
        ("GitHub Copilot", ".github/skills/", "Copilot coding agent / CLI / VS Code agent mode"),
    ]
    for i, (name, paths, note) in enumerate(rows):
        y = 1.65 + i * 1.45
        rect(slide, theme, 0.95, y, 3.0, 0.9, "pale", line="line")
        rect(slide, theme, 4.4, y, 3.2, 0.9, "charcoal")
        rect(slide, theme, 8.05, y, 4.15, 0.9, "cream", line="line")
        add_text(slide, theme, name, 1.2, y + 0.32, 2.25, 0.12, size=11.5, bold=True)
        add_text(slide, theme, paths, 4.65, y + 0.22, 2.45, 0.22, size=9.4, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, note, 8.3, y + 0.32, 3.3, 0.12, size=9.6, color_name="muted")
    add_text(slide, theme, "跨平台原則：堅持 name、description、Markdown body；避免 agent 專屬 frontmatter。", 1.1, 6.25, 11.1, 0.25, size=12.8, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def superpowers_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "Superpowers 與 Skills 框架", "一份 skill 是食譜；Superpowers 是一整本食譜書與廚房流程")
    skills = ["Brainstorming", "Planning", "TDD", "Code Review", "Debugging", "Documentation"]
    for i, label in enumerate(skills):
        x = 1.0 + (i % 3) * 4.1
        y = 1.85 + (i // 3) * 1.6
        rect(slide, theme, x, y, 3.25, 0.88, ["teal", "gold", "coral", "mint", "teal", "gold"][i])
        add_text(slide, theme, label, x + 0.18, y + 0.29, 2.85, 0.12, size=11.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "強制機制是核心：沒有測試就拒絕實作；未規劃前不碰檔案，把通用 LLM 變成有紀律的開發者。", 1.0, 5.45, 11.2, 0.45, size=14.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def security_numbers_slide(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, "安全性：13.4% 的 Skill 存在重大問題", "Snyk ToxicSkills 研究揭示快速生態系的供應鏈風險", dark=True)
    stats = [
        ("3,984", "掃描 skill 數量"),
        ("36.8%", "至少有一個漏洞"),
        ("13.4%", "包含重大等級問題"),
        ("76", "確認為惡意載荷"),
    ]
    for i, (num, label) in enumerate(stats):
        x = 0.95 + i * 3.1
        rect(slide, theme, x, 2.15, 2.45, 2.6, "white")
        add_text(slide, theme, num, x + 0.22, 2.78, 1.95, 0.38, size=28, color_name="coral", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, label, x + 0.22, 3.72, 1.95, 0.22, size=10.5, color_name="muted", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "91% 的惡意 skill 結合 prompt injection 和傳統惡意軟體。", 1.1, 5.85, 11.2, 0.28, size=15, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def threat_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "威脅模型與防禦", "讓 skill 強大的同一個機制，也讓它們危險")
    threats = [
        ("Shell 執行", "下載並執行惡意載荷"),
        ("檔案系統存取", "讀取 .env、SSH key、credentials 並外洩"),
        ("Prompt Injection", "覆蓋安全準則並社交工程使用者"),
    ]
    for i, (title, body) in enumerate(threats):
        x = 0.9 + i * 4.15
        add_callout(slide, theme, title, body, x, 1.75, 3.45, 1.7, ["coral", "gold", "teal"][i])
    defenses = ["只從驗證來源安裝", "安裝前閱讀 SKILL.md", "用 allowed-tools 最小化工具權限", "Agent 要求系統密碼時拒絕", "定期執行 Snyk Agent Scan"]
    add_text(slide, theme, "防禦清單", 1.05, 4.2, 1.4, 0.22, size=16, color_name="teal", bold=True)
    add_bullets(slide, theme, defenses, 1.05, 4.75, 10.6, size=11.3, gap=0.36)
    add_footer(slide, theme, SOURCE)


def governance_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "架構最佳實踐與團隊治理", "把 skill 當程式碼看：小、可測、可 review、可追蹤")
    items = [
        ("500 行以內", "主檔聚焦指令與約束，大量參考資料移到外部檔案。", "teal"),
        ("確定任務用 Script", "Lint、format、test、build 不交給 LLM 自行詮釋。", "gold"),
        ("一個動詞", "Review、Test、Document、Deploy 分成不同 skill。", "coral"),
        ("團隊治理", "Review 變更、pin marketplace 版本、測試代表性任務。", "mint"),
    ]
    for i, (title, body, accent) in enumerate(items):
        x = 0.9 + (i % 2) * 6.25
        y = 1.75 + (i // 2) * 2.1
        add_callout(slide, theme, title, body, x, y, 5.35, 1.5, accent)
    add_footer(slide, theme, SOURCE)


def context_slide(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, "Context Engineering 與上手 Checklist", "Scope 決定該用 CLAUDE.md、AGENTS.md、SKILL.md 還是 MCP", dark=True)
    rows = [
        ("CLAUDE.md / AGENTS.md", "專案憲法", "永遠載入；架構、規範、硬性約束"),
        ("SKILL.md", "任務能力", "按需載入；流程、模板、checklist"),
        ("MCP Servers", "外部工具", "工具呼叫時；資料庫、API、服務"),
    ]
    for i, (name, role, note) in enumerate(rows):
        y = 1.65 + i * 1.05
        rect(slide, theme, 0.95, y, 3.3, 0.68, "white")
        rect(slide, theme, 4.6, y, 2.4, 0.68, "teal")
        rect(slide, theme, 7.35, y, 4.85, 0.68, "white")
        add_text(slide, theme, name, 1.18, y + 0.22, 2.7, 0.1, size=9.5, color_name="ink", bold=True)
        add_text(slide, theme, role, 4.82, y + 0.22, 1.85, 0.1, size=9.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, note, 7.58, y + 0.22, 4.1, 0.1, size=9.2, color_name="muted")
    add_text(slide, theme, "上手：讀規範 → 建個人 skill → 建專案 skill → 測 5 種觸發語句 → 掃安全 → 每週迭代。", 1.0, 5.75, 11.3, 0.32, size=13.5, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def build():
    theme = load_theme(".codex/skills/article-to-presentation/templates/theme.json")
    prs = new_presentation()
    for maker in [
        cover,
        why_slide,
        what_slide,
        format_slide,
        description_slide,
        progressive_slide,
        ecosystem_slide,
        build_first_slide,
        cross_agent_slide,
        superpowers_slide,
        security_numbers_slide,
        threat_slide,
        governance_slide,
        context_slide,
    ]:
        maker(prs, theme)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
