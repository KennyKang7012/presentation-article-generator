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


OUT = Path("outputs/gyoza_agent_skills_deck.pptx")
SOURCE = "煎餃的調味實驗室｜2026-03-24 發佈／2026-06-06 更新｜gyozalab.com/agent-skills-guide"


def cover(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    # Reusable workflow motif: file, card, toolbox, output.
    blocks = [(8.0, 1.15, "SKILL.md", "teal"), (10.25, 1.65, "YAML", "gold"), (9.15, 3.22, "Agent", "coral"), (11.1, 4.85, "Tools", "mint"), (8.15, 5.35, "Output", "teal")]
    for a, b in [(0, 1), (1, 2), (0, 2), (2, 3), (2, 4), (4, 3)]:
        x1, y1, _, _ = blocks[a]
        x2, y2, _, _ = blocks[b]
        line(slide, theme, x1 + 0.5, y1 + 0.28, x2 + 0.5, y2 + 0.28, "mint", 1.15)
    for x, y, label, fill in blocks:
        rect(slide, theme, x, y, 1.0, 0.56, fill)
        add_text(slide, theme, label, x + 0.08, y + 0.18, 0.84, 0.12, size=8.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)

    add_text(slide, theme, "Agent Skills\n是什麼？", 0.78, 1.08, 5.6, 1.25, size=36, color_name="white", bold=True, font=theme.heading_font)
    add_text(slide, theme, "從重複 prompt 到可攜帶的 AI 工作流程", 0.82, 2.7, 5.8, 0.3, size=16.5, color_name="cream")
    rect(slide, theme, 0.82, 3.48, 4.95, 0.92, "teal")
    add_text(slide, theme, "把一次性指令變成可觸發、可分享、可版本控管的專業流程", 1.08, 3.76, 4.42, 0.18, size=11.5, color_name="white", bold=True)
    add_footer(slide, theme, SOURCE, dark=True)


def pain_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "痛點：我們一直在當人肉 API", "重複貼 prompt，其實是在手動搬運脈絡、格式與判斷標準")
    items = [
        ("重貼指令", "每次開新視窗，都要重新描述格式與規則。"),
        ("格式漂移", "改一個字，整段輸出結構可能跟著跑掉。"),
        ("對齊成本", "花時間修 prompt，卻不是在完成真正任務。"),
    ]
    for i, (title, body) in enumerate(items):
        add_callout(slide, theme, title, body, 0.92 + i * 4.15, 2.02, 3.45, 3.3, ["teal", "coral", "gold"][i])
    add_text(slide, theme, "Skills 的出發點：把規則定義一次，讓 AI 之後每次自動套用。", 1.15, 6.05, 10.8, 0.28, size=14.5, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def definition_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Agent Skills 的一句話定義", "可被機器理解、可跨平台遷移、包含背景知識的結構化工作指令集")
    rect(slide, theme, 1.1, 1.65, 11.1, 2.05, "charcoal")
    add_text(slide, theme, "Skill 不是一段聊天內容，而是一份標準化的能力說明書。", 1.55, 2.22, 10.2, 0.32, size=22, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    labels = [("特定場景", "何時觸發"), ("專業流程", "怎麼執行"), ("輸出規格", "交付什麼"), ("可攜帶", "如何分享")]
    for i, (head, sub) in enumerate(labels):
        x = 1.05 + i * 3.05
        rect(slide, theme, x, 4.42, 2.4, 1.05, ["teal", "gold", "coral", "mint"][i])
        add_text(slide, theme, head, x + 0.22, 4.68, 1.95, 0.2, size=13.2, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, sub, x + 0.22, 5.08, 1.95, 0.12, size=8.2, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def roles_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "模型、Agent、Skills 的分工", "能力、環境與專業流程各司其職")
    roles = [
        ("AI 模型", "處理器", "提供運算能力與推理邏輯。", "teal"),
        ("Agent", "作業系統", "提供穩定環境，讓 AI 能調動資源與工具。", "coral"),
        ("Skills", "應用程式", "安裝在 Agent 上，教 AI 特定任務怎麼做。", "gold"),
    ]
    for i, (title, metaphor, body, accent) in enumerate(roles):
        x = 0.9 + i * 4.15
        rect(slide, theme, x, 1.85, 3.45, 3.65, "white", line="line")
        circle(slide, theme, x + 1.21, 2.25, 1.02, accent)
        add_text(slide, theme, title, x + 0.38, 3.72, 2.65, 0.24, size=15, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, metaphor, x + 0.38, 4.14, 2.65, 0.18, size=10.6, color_name="teal", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, body, x + 0.42, 4.58, 2.55, 0.4, size=9.8, color_name="muted", align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def compare_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Prompt、GPTs/Gems、Agent Skills 差異", "關鍵差異在生命週期、載入方式、工具能力與可攜帶性")
    cols = [
        ("Prompt", "單次文字\n關閉對話就消失\n每次手動貼上", "pale"),
        ("GPTs / Gems", "平台角色設定\n啟動時整體載入\n多半綁定單一平台", "cream"),
        ("Agent Skills", "資料夾技能包\n需要時才載入\n可用 Git 管理與分享", "charcoal"),
    ]
    for i, (title, body, fill) in enumerate(cols):
        x = 0.95 + i * 4.1
        rect(slide, theme, x, 1.75, 3.45, 3.8, fill, line=None if fill == "charcoal" else "line")
        circle(slide, theme, x + 0.35, 2.15, 0.45, "coral" if i == 2 else "teal")
        add_text(slide, theme, title, x + 0.95, 2.18, 1.85, 0.22, size=15.5, color_name="gold" if fill == "charcoal" else "ink", bold=True)
        add_text(slide, theme, body, x + 0.38, 3.0, 2.65, 1.2, size=13.5, color_name="cream" if fill == "charcoal" else "muted")
    add_text(slide, theme, "文章強調：Agent Skills 是包含指令與資源的資料夾，不只是更長的 prompt。", 1.2, 6.12, 10.9, 0.25, size=13.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def ecosystem_stack_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "Project、MCP、Skills 如何協作", "脈絡、工具與流程要分層設計")
    layers = [
        ("Project", "固定工作桌", "共享長期背景資料與指令", 1.3, "teal"),
        ("MCP", "工具橋樑", "連接外部服務、資料庫與檔案", 2.65, "gold"),
        ("Skills", "專業流程", "定義拿到工具與資料後怎麼用", 4.0, "coral"),
    ]
    for name, label, body, y, color in layers:
        rect(slide, theme, 2.15, y, 8.95, 0.9, color)
        add_text(slide, theme, name, 2.45, y + 0.25, 1.28, 0.16, size=13, color_name="white", bold=True)
        add_text(slide, theme, label, 4.2, y + 0.25, 1.8, 0.16, size=11.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, body, 6.45, y + 0.25, 3.85, 0.16, size=10.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "設計重點：不要把所有知識塞進一段 prompt，該持久的放 Project，該連接的交給 MCP，該執行的寫成 Skill。", 1.05, 5.92, 11.25, 0.36, size=13.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def package_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "技能包長什麼樣", "最小可行 Skill 只需要 SKILL.md，進階需求再加資料夾")
    rect(slide, theme, 0.95, 1.75, 3.1, 4.0, "charcoal")
    add_text(slide, theme, "agent-skill/", 1.28, 2.12, 1.8, 0.22, size=14.5, color_name="gold", bold=True)
    entries = [("SKILL.md", "必要"), ("references/", "選配"), ("scripts/", "選配"), ("assets/", "選配")]
    for i, (name, tag) in enumerate(entries):
        y = 2.85 + i * 0.62
        rect(slide, theme, 1.28, y, 2.08, 0.36, "white")
        add_text(slide, theme, name, 1.42, y + 0.11, 1.05, 0.08, size=8.5, color_name="ink", bold=True)
        add_text(slide, theme, tag, 2.63, y + 0.11, 0.45, 0.08, size=7.5, color_name="coral", bold=True, align=PP_ALIGN.CENTER)
    bullets = [
        "references/ 放靜態參考文件，例如品牌指南或 API 文件。",
        "scripts/ 放自動化腳本，適合複雜運算或外部工具操作。",
        "assets/ 放範本、圖片、數據清單等靜態資源。",
        "資料夾形式方便 zip 分享、雲端保存與 Git 版控。",
    ]
    add_bullets(slide, theme, bullets, 5.0, 2.02, 6.7, size=13.2, gap=0.58)
    add_footer(slide, theme, SOURCE)


def skillmd_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "SKILL.md 的兩層結構", "名片負責觸發，說明書負責執行")
    rect(slide, theme, 0.95, 1.65, 5.45, 4.5, "white", line="line")
    rect(slide, theme, 6.92, 1.65, 5.45, 4.5, "charcoal")
    add_text(slide, theme, "YAML Frontmatter", 1.25, 2.08, 2.6, 0.22, size=17, color_name="teal", bold=True)
    add_text(slide, theme, "AI 啟動時先看這段，用來判斷這次任務要不要派這個 Skill 出場。", 1.25, 2.72, 4.35, 0.46, size=12.2, color_name="muted")
    rect(slide, theme, 1.25, 3.55, 4.45, 1.32, "pale", line="line")
    add_text(slide, theme, "name: meeting-summary", 1.48, 3.86, 3.6, 0.12, size=8.8, color_name="ink")
    add_text(slide, theme, "description: 建立會議摘要，使用者提到逐字稿或會議錄音時觸發", 1.48, 4.18, 3.85, 0.18, size=8.2, color_name="ink")
    add_text(slide, theme, "Markdown Body", 7.22, 2.08, 2.6, 0.22, size=17, color_name="gold", bold=True)
    add_text(slide, theme, "告訴 AI 具體怎麼做：輸出格式、分類規則、例外處理與品質標準。", 7.22, 2.72, 4.35, 0.46, size=12.2, color_name="cream")
    add_bullets(slide, theme, ["工作流程", "輸出格式", "判斷標準", "模糊情境處理"], 7.28, 3.65, 3.5, dark=True, size=12.5, gap=0.42)
    add_footer(slide, theme, SOURCE)


def progressive_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "漸進式載入三階段", "Skill 可以裝很多，但每次只讀真正需要的部分")
    steps = [
        ("01", "找名片", "只讀 name 與 description"),
        ("02", "翻說明書", "任務相關時才載入完整 SKILL.md"),
        ("03", "開工具箱", "需要時才讀 references 或執行 scripts"),
    ]
    for i, (num, title, body) in enumerate(steps):
        x = 1.0 + i * 4.1
        fill = "charcoal" if i == 1 else "pale"
        rect(slide, theme, x, 2.0, 3.3, 3.3, fill, line=None if i == 1 else "line")
        add_text(slide, theme, num, x + 0.28, 2.35, 0.52, 0.22, size=15, color_name="gold" if i == 1 else "coral", bold=True)
        add_text(slide, theme, title, x + 0.28, 3.0, 1.7, 0.25, size=17, color_name="white" if i == 1 else "ink", bold=True)
        add_text(slide, theme, body, x + 0.28, 3.7, 2.35, 0.58, size=11.5, color_name="cream" if i == 1 else "muted")
        if i < 2:
            line(slide, theme, x + 3.3, 3.66, x + 4.1, 3.66, "teal", 2.0)
    add_text(slide, theme, "這個設計保護 context window：避免專業手冊一次全塞進來，讓速度、成本與品質保持穩定。", 1.1, 6.15, 11.1, 0.28, size=13.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def principles_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "四個寫出好 Skill 的原則", "真正影響品質的是觸發、理由、篇幅與範例")
    items = [
        ("Description", "包含做什麼、何時觸發、關鍵能力。", "teal"),
        ("Why", "說明目的，讓 AI 能依情境變通。", "gold"),
        ("Scope", "SKILL.md 控制篇幅，重資料放 references。", "coral"),
        ("Examples", "用 Before/After 校準，比堆規則更有效。", "mint"),
    ]
    for i, (title, body, accent) in enumerate(items):
        x = 0.9 + (i % 2) * 6.25
        y = 1.75 + (i // 2) * 2.1
        add_callout(slide, theme, title, body, x, y, 5.35, 1.5, accent)
    add_footer(slide, theme, SOURCE)


def creator_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "不用寫程式，聊出第一個 Skill", "兩種路徑：需求清楚就直接打包，需求模糊就先跑通一次")
    rect(slide, theme, 0.95, 1.85, 5.2, 3.75, "pale", line="line")
    rect(slide, theme, 7.15, 1.85, 5.2, 3.75, "charcoal")
    add_text(slide, theme, "方式一：直接呼叫 Skill Creator", 1.28, 2.32, 3.8, 0.24, size=15.8, color_name="teal", bold=True)
    add_bullets(slide, theme, ["描述目標", "回答觸發條件與格式問題", "檢查 SKILL.md 初版", "測試並迭代"], 1.35, 3.0, 4.0, size=11.8, gap=0.42)
    add_text(slide, theme, "方式二：先聊再打包", 7.48, 2.32, 3.8, 0.24, size=15.8, color_name="gold", bold=True)
    add_bullets(slide, theme, ["先完整跑通一次任務", "記錄不滿與調整", "提煉工作邏輯與踩坑", "再交給 Skill Creator 打包"], 7.55, 3.0, 4.0, dark=True, size=11.8, gap=0.42)
    add_text(slide, theme, "建立 Skill 是後設認知：起點是什麼、終點要什麼、中間靠哪些判斷標準。", 1.15, 6.18, 10.9, 0.28, size=13.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def safety_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "生態系與安全查核", "Skills 可以借用專家流程，但下載前要先自我防衛")
    rect(slide, theme, 0.9, 1.75, 5.3, 4.2, "white", line="line")
    add_text(slide, theme, "三類來源", 1.25, 2.15, 1.3, 0.22, size=16, color_name="teal", bold=True)
    add_bullets(slide, theme, ["基礎 Skills：文件處理、網頁瀏覽、研究等通用能力。", "第三方夥伴 Skills：由軟體公司開發的專業模組。", "社群分享 Skills：使用者整理的流程包。"], 1.25, 2.82, 4.3, size=11.5, gap=0.55)
    rect(slide, theme, 7.1, 1.75, 5.3, 4.2, "charcoal")
    add_text(slide, theme, "安全三查", 7.45, 2.15, 1.3, 0.22, size=16, color_name="gold", bold=True)
    add_bullets(slide, theme, ["審核 scripts/ 是否包含看不懂或來源不明的程式。", "閱讀 SKILL.md 是否要求外傳資料到不明網址。", "新手優先選只包含文字指令的 Skill。"], 7.45, 2.82, 4.3, dark=True, size=11.5, gap=0.55)
    add_footer(slide, theme, SOURCE)


def action_slide(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, "第一步行動", "找一個每週重複三次的 AI 指令，今天就打包成 Skill", dark=True)
    steps = [
        ("01", "挑任務", "每週重複、格式固定、容易驗證"),
        ("02", "寫名片", "description 說清楚何時觸發"),
        ("03", "定流程", "輸入、判斷、輸出與例外處理"),
        ("04", "測試", "檢查觸發、品質與安全邊界"),
    ]
    for i, (num, title, body) in enumerate(steps):
        x = 0.95 + i * 3.1
        rect(slide, theme, x, 2.1, 2.45, 2.85, "white")
        add_text(slide, theme, num, x + 0.25, 2.42, 0.48, 0.2, size=15, color_name="coral", bold=True)
        add_text(slide, theme, title, x + 0.25, 3.05, 1.55, 0.25, size=16, color_name="ink", bold=True)
        add_text(slide, theme, body, x + 0.25, 3.72, 1.85, 0.52, size=10.5, color_name="muted")
        if i < 3:
            line(slide, theme, x + 2.45, 3.48, x + 3.1, 3.48, "gold", 2.0)
    add_text(slide, theme, "你累積的不再是混亂對話紀錄，而是一套可帶走、可複用的專業邏輯庫。", 1.25, 5.95, 10.8, 0.3, size=15, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def build():
    theme = load_theme(".codex/skills/article-to-presentation/templates/theme.json")
    prs = new_presentation()
    for maker in [
        cover,
        pain_slide,
        definition_slide,
        roles_slide,
        compare_slide,
        ecosystem_stack_slide,
        package_slide,
        skillmd_slide,
        progressive_slide,
        principles_slide,
        creator_slide,
        safety_slide,
        action_slide,
    ]:
        maker(prs, theme)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
