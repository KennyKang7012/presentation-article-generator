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


OUT = Path("outputs/91app_ai_agent_deck.pptx")
SOURCE = "91APP｜2026-03-11｜https://91app.com/blog/what-is-aiagent/"


def cover(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    # Search path turning into an agent workflow
    points = [(8.2, 1.1, "teal"), (10.2, 1.55, "gold"), (9.55, 3.0, "coral"), (11.3, 4.35, "mint"), (8.55, 5.0, "teal")]
    for x, y, c in points:
        circle(slide, theme, x, y, 0.34 if c == "coral" else 0.24, c)
    for a, b in [(points[0], points[1]), (points[1], points[2]), (points[2], points[3]), (points[2], points[4]), (points[0], points[2])]:
        line(slide, theme, a[0] + 0.12, a[1] + 0.12, b[0] + 0.12, b[1] + 0.12, "mint", 1.2)
    add_text(slide, theme, "AI Agent 與 AXO 時代", 0.78, 1.18, 6.8, 0.72, size=35, color_name="white", bold=True, font=theme.heading_font)
    add_text(slide, theme, "從自主代理、企業應用到搜尋體驗最佳化", 0.82, 2.1, 6.1, 0.32, size=17, color_name="cream")
    rect(slide, theme, 0.82, 3.02, 4.85, 0.9, "teal")
    add_text(slide, theme, "當搜尋被外包給 AI Agent，品牌要開始優化 AI 的體驗", 1.1, 3.29, 4.3, 0.25, size=12.8, color_name="white", bold=True)
    add_footer(slide, theme, SOURCE, dark=True)


def stage_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "為什麼現在談 AI Agent", "AI 正從推理者，走向可自主完成任務的代理")
    stages = [("Chatbot", "回覆問題"), ("Reasoner", "推理判斷"), ("Agent", "規劃行動"), ("Innovator", "創造方案"), ("Orchestrator", "組織協作")]
    for i, (name, desc) in enumerate(stages):
        x = 0.9 + i * 2.45
        y = 4.55 - i * 0.55
        rect(slide, theme, x, y, 1.8, 0.92, "charcoal" if name == "Agent" else "white", line=None if name == "Agent" else "line")
        add_text(slide, theme, name, x + 0.12, y + 0.2, 1.55, 0.18, size=12.5, color_name="gold" if name == "Agent" else "ink", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, desc, x + 0.12, y + 0.55, 1.55, 0.14, size=8.3, color_name="cream" if name == "Agent" else "muted", align=PP_ALIGN.CENTER)
        if i < 4:
            line(slide, theme, x + 1.8, y + 0.46, x + 2.45, y - 0.1, "teal", 1.6)
    add_text(slide, theme, "文章指出，產業共識正從「推理者」快速跨入「代理 Agent」爆發臨界點。企業導入重點也從工具試用，轉向流程重設。", 1.15, 1.8, 5.7, 0.82, size=17, color_name="ink", bold=True)
    add_text(slide, theme, "關鍵差異不是 AI 回答得更快，而是 AI 能否自己拆解任務、調用工具、觀察結果並修正策略。", 7.15, 1.9, 4.8, 0.72, size=15, color_name="muted")
    add_footer(slide, theme, SOURCE)


def compare_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "AI Agent、Chatbot、RPA 的差異", "從被動回覆，到目標導向的自主行動")
    cols = [
        ("Chatbot", "一問一答\n依腳本或 FAQ 回覆\n工具使用有限", "pale"),
        ("RPA", "固定 SOP\n流程穩定時效率高\n遇到例外易停機", "cream"),
        ("AI Agent", "理解目標\n自主規劃與調用工具\n失敗後可觀測並修正", "charcoal"),
    ]
    for i, (title, body, fill) in enumerate(cols):
        x = 0.95 + i * 4.1
        rect(slide, theme, x, 1.75, 3.45, 3.8, fill, line=None if fill == "charcoal" else "line")
        circle(slide, theme, x + 0.35, 2.15, 0.45, "coral" if i == 2 else "teal")
        add_text(slide, theme, title, x + 0.95, 2.18, 1.8, 0.22, size=17, color_name="gold" if fill == "charcoal" else "ink", bold=True)
        add_text(slide, theme, body, x + 0.38, 3.0, 2.65, 1.45, size=15, color_name="cream" if fill == "charcoal" else "muted")
    add_footer(slide, theme, SOURCE)


def architecture_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "拆解 AI Agent 的大腦：7 大核心架構", "成熟 Agent 是一組可觀測、可行動、可學習的系統")
    center_x, center_y = 5.9, 3.23
    nodes = [
        ("感知", "Perception", 5.85, 1.25, "teal"),
        ("Core LLM", "目標編碼", 8.45, 2.0, "gold"),
        ("記憶", "Memory / RAG", 8.55, 4.15, "mint"),
        ("規劃", "Reasoning", 5.85, 5.15, "coral"),
        ("行動", "Tools", 3.15, 4.2, "teal"),
        ("觀測", "Feedback", 3.0, 2.0, "gold"),
        ("學習", "Learning Loop", 1.0, 3.15, "mint"),
    ]
    for _title, _sub, x, y, _c in nodes:
        line(slide, theme, x + 1.0, y + 0.36, center_x + 0.6, center_y + 0.6, "line", 1.1)
    circle(slide, theme, center_x, center_y, 1.2, "charcoal")
    add_text(slide, theme, "AI\nAgent", center_x + 0.34, center_y + 0.36, 0.52, 0.38, size=14, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    for title, sub, x, y, c in nodes:
        rect(slide, theme, x, y, 2.0, 0.72, c)
        add_text(slide, theme, title, x + 0.12, y + 0.18, 0.62, 0.18, size=12, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, sub, x + 0.72, y + 0.2, 1.05, 0.14, size=8.7, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def flow_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "運作閉環：東京機票與行程案例", "Agent 的價值在於遇到例外時能觀測、調整、再行動")
    steps = [
        ("感知", "目的地、時間、預算、任務類型"),
        ("規劃", "航班、飯店、景點、交通、日曆"),
        ("行動", "Skyscanner、Booking、Maps、Calendar"),
        ("觀測調整", "客滿或失敗時回到規劃層"),
        ("學習", "記住住宿與航班偏好"),
    ]
    for i, (title, body) in enumerate(steps):
        x = 0.75 + i * 2.55
        rect(slide, theme, x, 2.1, 2.05, 2.4, "charcoal" if i == 3 else "pale", line=None if i == 3 else "line")
        add_text(slide, theme, f"{i+1:02}", x + 0.2, 2.38, 0.45, 0.2, size=15, color_name="gold" if i == 3 else "coral", bold=True)
        add_text(slide, theme, title, x + 0.2, 2.95, 1.45, 0.24, size=15, color_name="white" if i == 3 else "ink", bold=True)
        add_text(slide, theme, body, x + 0.2, 3.5, 1.55, 0.5, size=10.4, color_name="cream" if i == 3 else "muted")
        if i < 4:
            line(slide, theme, x + 2.05, 3.3, x + 2.55, 3.3, "teal", 2.2)
    add_footer(slide, theme, SOURCE)


def applications_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "三類實際應用場景", "從個人數位分身、企業流程，到多代理協作")
    cards = [
        ("B2C 個人分身", "自動比價、表單填寫、行事曆整合、收件匣管理、研究助理。", "teal"),
        ("B2B 營運代理", "Lead Scoring、客製化開發信、HR 審批、客服退換貨。", "coral"),
        ("Developer 多代理", "LangChain / LangGraph、AutoGen、CrewAI、Google A2A。", "gold"),
    ]
    for i, (title, body, accent) in enumerate(cards):
        add_callout(slide, theme, title, body, 0.9 + i * 4.15, 1.9, 3.45, 3.55, accent)
    add_footer(slide, theme, SOURCE)


def governance_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "企業導入挑戰與治理解法", "Agent 會執行動作，因此治理要比聊天工具更嚴格")
    rows = [
        ("幻覺與決策失控", "Human-in-the-loop", "金流、法律、敏感資料操作要有人確認"),
        ("資料外洩與權限過大", "RBAC / 地端部署", "用最小權限與本地模型降低外洩風險"),
        ("Prompt Injection", "輸入過濾 / 指令隔離", "防止惡意指令混入 Agent 執行流程"),
        ("責任與可追蹤性", "Audit Log", "完整記錄每次 Agent 操作與結果"),
    ]
    for i, (risk, control, note) in enumerate(rows):
        y = 1.65 + i * 1.12
        rect(slide, theme, 0.95, y, 3.15, 0.72, "pale", line="line")
        rect(slide, theme, 4.65, y, 2.75, 0.72, "charcoal")
        rect(slide, theme, 7.95, y, 4.15, 0.72, "cream", line="line")
        add_text(slide, theme, risk, 1.18, y + 0.24, 2.55, 0.14, size=10.8, bold=True)
        add_text(slide, theme, control, 4.85, y + 0.24, 2.25, 0.14, size=10.6, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, note, 8.18, y + 0.22, 3.45, 0.16, size=9.5, color_name="muted")
    add_footer(slide, theme, SOURCE)


def search_shift_slide(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, "搜尋行為典範轉移", "從人類搜尋點擊，走向 Agent 代搜尋、代比較、代交易", dark=True)
    rect(slide, theme, 0.95, 1.85, 5.15, 3.65, "white")
    add_text(slide, theme, "傳統 SEO", 1.25, 2.2, 1.5, 0.24, size=16, bold=True)
    old = ["人類輸入關鍵字", "瀏覽搜尋結果", "點擊進站", "自行比較與下單"]
    for i, item in enumerate(old):
        add_text(slide, theme, item, 1.55 + i * 0.9, 3.0 + i * 0.38, 2.2, 0.16, size=10.5, color_name="muted")
        circle(slide, theme, 1.22 + i * 0.9, 3.02 + i * 0.38, 0.13, "teal")
    rect(slide, theme, 7.2, 1.85, 5.15, 3.65, "teal")
    add_text(slide, theme, "Agent 時代", 7.5, 2.2, 1.7, 0.24, size=16, color_name="white", bold=True)
    new = ["使用者交付目標", "Agent 搜尋與篩選", "比較可信來源", "直接預約或交易"]
    for i, item in enumerate(new):
        add_text(slide, theme, item, 7.8 + i * 0.9, 3.0 + i * 0.38, 2.25, 0.16, size=10.5, color_name="white")
        circle(slide, theme, 7.47 + i * 0.9, 3.02 + i * 0.38, 0.13, "gold")
    add_text(slide, theme, "新競爭關鍵：被 Agent 找到、信任、引用、操作", 3.25, 6.15, 6.8, 0.22, size=14, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def aao_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "AAO 四大優化方向", "AI Agent Optimization：讓代理找得到、信任你、能操作，也能被控管")
    items = [
        ("找得到", "Schema.org、語義化 HTML、乾淨 API", "teal"),
        ("願意引用", "E-E-A-T、作者、數據來源、第三方背書", "gold"),
        ("能行動", "預約 API、查詢端點、交易介面", "coral"),
        ("保護自己", "robots.txt、AI 爬蟲協議、版權聲明", "mint"),
    ]
    for i, (title, body, c) in enumerate(items):
        x = 1.0 + (i % 2) * 5.65
        y = 1.65 + (i // 2) * 2.25
        rect(slide, theme, x, y, 4.8, 1.55, "white", line="line")
        circle(slide, theme, x + 0.32, y + 0.42, 0.48, c)
        add_text(slide, theme, title, x + 1.05, y + 0.36, 1.4, 0.22, size=16, bold=True)
        add_text(slide, theme, body, x + 1.05, y + 0.85, 3.25, 0.26, size=10.8, color_name="muted")
    add_footer(slide, theme, SOURCE)


def axo_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "從 SEO 走向 AXO", "SEO 沒有死，但需要服務新的使用者：AI 代理")
    steps = [("SEO", "人類搜尋體驗"), ("AAO", "Agent 找到、引用、行動"), ("AXO", "AI eXperience Optimization")]
    for i, (title, desc) in enumerate(steps):
        x = 1.2 + i * 3.9
        rect(slide, theme, x, 2.25, 2.7, 1.5, "charcoal" if i == 2 else "pale", line=None if i == 2 else "line")
        add_text(slide, theme, title, x + 0.25, 2.65, 2.15, 0.26, size=22, color_name="gold" if i == 2 else "teal", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, desc, x + 0.25, 3.18, 2.15, 0.18, size=9.5, color_name="cream" if i == 2 else "muted", align=PP_ALIGN.CENTER)
        if i < 2:
            line(slide, theme, x + 2.7, 3.0, x + 3.9, 3.0, "coral", 2.4)
    add_text(slide, theme, "未來品牌網站不只要讓人看懂，也要讓 AI Agent 能解析、信任、引用並完成任務。", 2.1, 5.25, 8.8, 0.42, size=17, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def roadmap_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "導入行動指南", "從單一高價值流程開始，逐步建立可治理的 Agent 工作流")
    roadmap = [
        ("0-30 天", "選定流程\n盤點資料與工具"),
        ("31-60 天", "建立 PoC\n加入人工審核"),
        ("61-90 天", "串接 API\n建立稽核與回饋"),
        ("90 天後", "擴展到多流程\n佈局 AAO / AXO"),
    ]
    for i, (time, body) in enumerate(roadmap):
        x = 0.95 + i * 3.05
        rect(slide, theme, x, 2.0, 2.45, 2.6, "white", line="line")
        add_text(slide, theme, time, x + 0.25, 2.35, 1.65, 0.2, size=15, color_name="coral", bold=True)
        add_text(slide, theme, body, x + 0.25, 3.05, 1.75, 0.7, size=13, color_name="ink")
        if i < 3:
            line(slide, theme, x + 2.45, 3.25, x + 3.05, 3.25, "teal", 2)
    add_text(slide, theme, "先小規模驗證效益，再逐步擴展；治理與網站可操作性要同步設計。", 2.1, 5.75, 8.8, 0.28, size=14, color_name="teal", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def conclusion_slide(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, "結論", "AI Agent 改變的不只是 AI 工具，而是企業流程與數位行銷入口", dark=True)
    add_text(slide, theme, "AI Agent 是會行動的 AI", 0.95, 1.75, 5.8, 0.42, size=28, color_name="white", bold=True, font=theme.heading_font)
    add_bullets(
        slide,
        theme,
        [
            "企業價值來自流程重設，而不是單點工具導入。",
            "安全可控的 Agent 需要權限、審核、稽核與回饋設計。",
            "SEO 的下一步，是讓品牌被人類與 AI Agent 同時理解、信任並操作。",
        ],
        1.05,
        2.65,
        6.2,
        dark=True,
        size=14.5,
        gap=0.68,
    )
    for i, (label, c) in enumerate([("Human", "teal"), ("Agent", "gold"), ("Brand", "coral")]):
        x = 8.1 + i * 1.45
        circle(slide, theme, x, 3.1, 1.0, c)
        add_text(slide, theme, label, x + 0.2, 3.48, 0.6, 0.12, size=9.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        if i < 2:
            line(slide, theme, x + 1.0, 3.6, x + 1.45, 3.6, "cream", 1.4)
    add_footer(slide, theme, SOURCE, dark=True)


def build():
    theme = load_theme(".codex/skills/article-to-presentation/templates/theme.json")
    prs = new_presentation()
    for fn in [
        cover,
        stage_slide,
        compare_slide,
        architecture_slide,
        flow_slide,
        applications_slide,
        governance_slide,
        search_shift_slide,
        aao_slide,
        axo_slide,
        roadmap_slide,
        conclusion_slide,
    ]:
        fn(prs, theme)
    prs.core_properties.title = "AI Agent 與 AXO 時代"
    prs.core_properties.subject = "91APP AI Agent 文章摘要簡報"
    prs.core_properties.author = "Codex"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
