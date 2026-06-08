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


OUT = Path("outputs/iii_ai_agent_architecture_deck.pptx")
SOURCE = "資策會數轉院｜2026-03-06｜ideas-dtri.iii.org.tw/產業資訊/ai-agent-3/"


def cover(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    nodes = [
        (8.0, 1.25, "teal"),
        (10.3, 1.1, "gold"),
        (11.15, 2.65, "mint"),
        (9.4, 3.42, "coral"),
        (11.25, 5.2, "teal"),
        (8.35, 5.65, "gold"),
        (7.35, 3.85, "mint"),
    ]
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (0, 3), (6, 3), (6, 5)]:
        x1, y1, _ = nodes[a]
        x2, y2, _ = nodes[b]
        line(slide, theme, x1 + 0.13, y1 + 0.13, x2 + 0.13, y2 + 0.13, "mint", 1.15)
    for x, y, c in nodes:
        circle(slide, theme, x, y, 0.34 if c == "coral" else 0.26, c)

    add_text(slide, theme, "AI Agent\n架構全解析", 0.75, 1.1, 5.6, 1.35, size=36, color_name="white", bold=True, font=theme.heading_font)
    add_text(slide, theme, "從 Google 白皮書到企業落地的技術藍圖", 0.82, 2.8, 5.6, 0.3, size=16.5, color_name="cream")
    rect(slide, theme, 0.82, 3.55, 4.8, 0.92, "teal")
    add_text(slide, theme, "重點：模型之外，還要設計工具、協調層、部署與 Agent Ops", 1.07, 3.83, 4.25, 0.18, size=11.5, color_name="white", bold=True)
    add_footer(slide, theme, SOURCE, dark=True)


def shift_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "從「砌磚工」到「導演」", "開發重心從寫死邏輯，轉向設定目標、環境、工具與護欄")
    rect(slide, theme, 0.85, 1.75, 5.3, 3.7, "white", line="line")
    rect(slide, theme, 7.15, 1.75, 5.3, 3.7, "charcoal")
    add_text(slide, theme, "Predictive AI", 1.25, 2.12, 2.4, 0.28, size=18, bold=True)
    add_text(slide, theme, "開發者像砌磚工", 1.25, 2.72, 2.7, 0.25, size=15, color_name="teal", bold=True)
    add_bullets(slide, theme, ["明確定義每一步邏輯", "AI 主要負責預測與回覆", "適合邊界清楚的單點任務"], 1.28, 3.35, 4.2, size=13, gap=0.46)
    add_text(slide, theme, "Agentic AI", 7.55, 2.12, 2.4, 0.28, size=18, color_name="gold", bold=True)
    add_text(slide, theme, "開發者像導演", 7.55, 2.72, 2.7, 0.25, size=15, color_name="cream", bold=True)
    add_bullets(slide, theme, ["設定場景、工具與目標", "Agent 自主規劃與修正", "核心是上下文工程"], 7.58, 3.35, 4.1, dark=True, size=13, gap=0.46)
    line(slide, theme, 6.28, 3.58, 6.95, 3.58, "coral", 2.8)
    circle(slide, theme, 6.55, 3.4, 0.34, "coral")
    add_footer(slide, theme, SOURCE)


def value_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "AI Agent 的企業價值", "不只是回答問題，而是把目標轉成可執行的工作流")
    steps = [
        ("目標", "使用者或流程提出任務"),
        ("規劃", "拆解步驟與選擇策略"),
        ("行動", "呼叫工具、API、資料庫"),
        ("觀察", "讀取結果並判斷是否修正"),
        ("完成", "交付工作成果與紀錄"),
    ]
    for i, (title, body) in enumerate(steps):
        x = 0.75 + i * 2.55
        fill = "charcoal" if i == 2 else "pale"
        rect(slide, theme, x, 2.05, 2.05, 2.55, fill, line=None if fill == "charcoal" else "line")
        add_text(slide, theme, f"{i+1:02}", x + 0.2, 2.32, 0.45, 0.2, size=14, color_name="gold" if fill == "charcoal" else "coral", bold=True)
        add_text(slide, theme, title, x + 0.2, 2.95, 1.45, 0.24, size=15, color_name="white" if fill == "charcoal" else "ink", bold=True)
        add_text(slide, theme, body, x + 0.2, 3.47, 1.55, 0.48, size=10.6, color_name="cream" if fill == "charcoal" else "muted")
        if i < 4:
            line(slide, theme, x + 2.05, 3.28, x + 2.55, 3.28, "teal", 2.1)
    add_text(slide, theme, "企業真正要設計的是可被 Agent 接手、可觀測、可回滾的流程，而不是另一個聊天視窗。", 1.2, 5.58, 10.9, 0.42, size=17, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def anatomy_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "Agent 的四大核心架構", "模型只是大腦；要完成工作，還需要雙手、神經系統與身體")
    items = [
        ("模型 Model", "推理、規劃、決策；依任務在成本與效能間取捨。", "teal"),
        ("工具 Tools", "搜尋網路、讀取資料庫、執行程式碼或操作 API。", "coral"),
        ("協調層 Orchestration", "管理記憶、任務步驟與「推理-行動-觀察」迴圈。", "gold"),
        ("部署 Infrastructure", "安全驗證、權限管理、擴展性與運行監控。", "mint"),
    ]
    for i, (title, body, accent) in enumerate(items):
        x = 0.85 + (i % 2) * 6.25
        y = 1.75 + (i // 2) * 2.25
        add_callout(slide, theme, title, body, x, y, 5.35, 1.65, accent)
    circle(slide, theme, 6.25, 3.2, 0.86, "charcoal")
    add_text(slide, theme, "Agent\nSystem", 6.47, 3.43, 0.44, 0.28, size=10.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def levels_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "代理系統的五級進化論", "用能力分類判斷企業目前在哪一級、下一步該補什麼")
    levels = [
        ("L0", "核心推理", "只能依訓練資料回答"),
        ("L1", "互聯問題解決", "能呼叫外部工具或檢索"),
        ("L2", "策略性問題解決", "能長期規劃與拆解步驟"),
        ("L3", "協作式多代理", "多個專精 Agent 組隊"),
        ("L4", "自我演化", "自我學習、生成工具或子 Agent"),
    ]
    for i, (lvl, title, desc) in enumerate(levels):
        x = 0.75 + i * 2.52
        h = 1.35 + i * 0.52
        y = 5.8 - h
        fill = "charcoal" if i == 3 else ("teal" if i == 2 else "pale")
        rect(slide, theme, x, y, 1.9, h, fill, line=None if fill != "pale" else "line")
        add_text(slide, theme, lvl, x + 0.18, y + 0.23, 0.48, 0.2, size=15, color_name="gold" if fill == "charcoal" else "coral", bold=True)
        add_text(slide, theme, title, x + 0.18, y + 0.72, 1.42, 0.24, size=12.2, color_name="white" if fill != "pale" else "ink", bold=True)
        add_text(slide, theme, desc, x + 0.18, y + 1.17, 1.42, 0.58, size=8.8, color_name="cream" if fill != "pale" else "muted")
    add_text(slide, theme, "文章指出：多數領先企業正在從 Level 2 邁向 Level 3，治理難度也同步上升。", 1.0, 6.35, 11.2, 0.28, size=13.5, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def maturity_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "企業成熟度定位", "Level 2 做流程，Level 3 做團隊；不要跳過可觀測性")
    columns = [
        ("Level 1", "工具接入", "查詢、摘要、檢索\n適合知識助理"),
        ("Level 2", "單流程 Agent", "拆解任務、調用工具\n適合客服、核銷、合規查詢"),
        ("Level 3", "多代理協作", "跨角色分工與互審\n適合複雜研究與營運決策"),
    ]
    for i, (level, title, body) in enumerate(columns):
        x = 0.9 + i * 4.15
        fill = "charcoal" if i == 1 else "white"
        rect(slide, theme, x, 1.8, 3.45, 3.9, fill, line=None if i == 1 else "line")
        add_text(slide, theme, level, x + 0.28, 2.18, 0.9, 0.22, size=12, color_name="gold" if i == 1 else "coral", bold=True)
        add_text(slide, theme, title, x + 0.28, 2.75, 2.5, 0.25, size=17, color_name="white" if i == 1 else "ink", bold=True)
        add_text(slide, theme, body, x + 0.28, 3.48, 2.6, 0.86, size=12.5, color_name="cream" if i == 1 else "muted")
    add_text(slide, theme, "升級前提：資料治理、權限邊界、工具穩定性、Eval 測試集與 Trace 可追蹤性。", 1.15, 6.25, 10.8, 0.28, size=13.5, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def multi_agent_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "為什麼一個 Agent 不夠用", "複雜任務需要專家團隊模式，降低認知過載並提升可除錯性")
    center = (5.65, 3.0)
    roles = [
        ("協調器", "拆解任務", 5.45, 1.35, "teal"),
        ("查詢分解", "產生搜尋策略", 2.1, 3.15, "gold"),
        ("評論", "審核準確性", 5.45, 4.95, "coral"),
        ("報告", "整合輸出", 8.8, 3.15, "mint"),
    ]
    for title, desc, x, y, accent in roles:
        line(slide, theme, x + 1.05, y + 0.38, center[0] + 1.08, center[1] + 0.5, "line", 1.3)
    rect(slide, theme, center[0], center[1], 2.15, 1.0, "charcoal")
    add_text(slide, theme, "合規查詢\n任務", center[0] + 0.42, center[1] + 0.32, 1.25, 0.32, size=14, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    for title, desc, x, y, accent in roles:
        rect(slide, theme, x, y, 2.1, 0.86, accent)
        add_text(slide, theme, title, x + 0.16, y + 0.18, 0.82, 0.18, size=12.5, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, desc, x + 0.98, y + 0.2, 0.92, 0.14, size=8.8, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "若報告品質不佳，可定位是報告 Agent、評論 Agent 或資料查詢環節的問題，而不是整個系統黑箱。", 1.1, 6.05, 11.1, 0.42, size=14.5, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def protocols_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "連接萬物的標準：MCP、A2A、AP2", "當企業有許多 Agent，互操作性會決定能否規模化")
    items = [
        ("MCP", "Model Context Protocol", "像 USB 標準，讓模型連接資料源與工具。", "teal"),
        ("A2A", "Agent2Agent", "Agent 交換 Agent Card，宣告能力並請求協作。", "coral"),
        ("AP2", "Agent Payments Protocol", "讓 Agent 進行訂票、採購等商業交易時具備授權與信任。", "gold"),
    ]
    for i, (tag, title, body, accent) in enumerate(items):
        x = 0.9 + i * 4.15
        rect(slide, theme, x, 1.85, 3.45, 3.75, "white", line="line")
        circle(slide, theme, x + 1.18, 2.28, 1.05, accent)
        add_text(slide, theme, tag, x + 1.43, 2.64, 0.55, 0.18, size=14, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, title, x + 0.38, 3.65, 2.65, 0.25, size=12.8, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, body, x + 0.38, 4.28, 2.65, 0.62, size=10.6, color_name="muted", align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def ops_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Agent Ops：駕馭不可預測性", "Agent 的輸出具有機率性，因此營運要看過程、看品質、看回饋")
    rect(slide, theme, 0.85, 1.8, 3.2, 3.95, "pale", line="line")
    rect(slide, theme, 5.05, 1.8, 3.2, 3.95, "charcoal")
    rect(slide, theme, 9.25, 1.8, 3.2, 3.95, "cream", line="line")
    blocks = [
        ("Evaluation", "AI 評 AI，評估答案是否準確、安全且符合任務。", 1.12, "ink"),
        ("Traces", "記錄思考過程、工具呼叫原因與中間觀察。", 5.32, "white"),
        ("Feedback Loop", "把錯誤案例與使用者回饋導回測試與改進。", 9.52, "ink"),
    ]
    for title, body, x, color in blocks:
        add_text(slide, theme, title, x, 2.35, 2.6, 0.3, size=18, color_name="gold" if color == "white" else "teal", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, body, x + 0.18, 3.25, 2.2, 0.82, size=12.6, color_name="cream" if color == "white" else "muted", align=PP_ALIGN.CENTER)
    line(slide, theme, 4.05, 3.78, 5.05, 3.78, "coral", 2.0)
    line(slide, theme, 8.25, 3.78, 9.25, 3.78, "coral", 2.0)
    add_text(slide, theme, "傳統測試：輸入 A 預期輸出 B。Agent Ops：同時治理輸出品質、推理軌跡與持續回饋。", 1.0, 6.32, 11.4, 0.28, size=13.2, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def scientist_slide(prs, theme):
    slide = blank_slide(prs, "cream", theme)
    add_title(slide, theme, "前瞻案例：AI 共同科學家", "多代理系統能把知識工作拆成探索、反思、生成與驗證")
    roles = [
        ("文獻探索", "整理研究脈絡與證據"),
        ("科學辯論", "從不同角度挑戰假設"),
        ("假設生成", "提出新穎研究方向"),
        ("驗證規劃", "設計後續實驗與評估"),
    ]
    for i, (title, body) in enumerate(roles):
        x = 1.05 + i * 3.05
        y = 2.1 + (0.35 if i % 2 else 0)
        rect(slide, theme, x, y, 2.4, 2.55, "white", line="line")
        circle(slide, theme, x + 0.88, y + 0.38, 0.64, ["teal", "gold", "coral", "mint"][i])
        add_text(slide, theme, title, x + 0.25, y + 1.35, 1.9, 0.22, size=13.5, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, body, x + 0.28, y + 1.88, 1.84, 0.42, size=10.3, color_name="muted", align=PP_ALIGN.CENTER)
        if i < 3:
            line(slide, theme, x + 2.4, y + 1.28, x + 3.05, 2.1 + (0.35 if (i + 1) % 2 else 0) + 1.28, "teal", 1.7)
    add_text(slide, theme, "價值不只在加速文獻回顧，而是創造「人類科學家可能忽略」的新假設。", 1.1, 5.85, 11.1, 0.32, size=14.8, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def taiwan_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "給台灣企業決策者的行動建議", "從流程、資料、治理三件事開始，不要只買聊天框")
    items = [
        ("重新思考工作流程", "優先盤點重複性高、規則清楚、錯誤成本可控的流程。", "teal"),
        ("資料治理是基本功", "Agent 能力取決於可取得、正確且有權限邊界的資料。", "gold"),
        ("建立人機協作治理", "用 Guardrails、審計、覆核與 Agent Ops 防止越權決策。", "coral"),
    ]
    for i, (title, body, accent) in enumerate(items):
        add_callout(slide, theme, title, body, 0.95 + i * 4.15, 2.05, 3.45, 3.4, accent)
    add_footer(slide, theme, SOURCE)


def roadmap_slide(prs, theme):
    slide = blank_slide(prs, "charcoal", theme)
    add_title(slide, theme, "導入路線圖", "先把單一流程做穩，再擴展成可治理的數位團隊", dark=True)
    steps = [
        ("01", "選流程", "高重複、規則清楚、資料可控"),
        ("02", "接工具", "API、資料庫、權限與回滾"),
        ("03", "建治理", "Eval、Trace、Feedback Loop"),
        ("04", "擴團隊", "從 Level 2 走向 Level 3 多代理"),
    ]
    for i, (num, title, body) in enumerate(steps):
        x = 0.95 + i * 3.1
        rect(slide, theme, x, 2.1, 2.45, 2.85, "white")
        add_text(slide, theme, num, x + 0.25, 2.43, 0.48, 0.2, size=15, color_name="coral", bold=True)
        add_text(slide, theme, title, x + 0.25, 3.05, 1.55, 0.25, size=16, color_name="ink", bold=True)
        add_text(slide, theme, body, x + 0.25, 3.72, 1.82, 0.52, size=10.5, color_name="muted")
        if i < 3:
            line(slide, theme, x + 2.45, 3.48, x + 3.1, 3.48, "gold", 2.0)
    add_text(slide, theme, "AI 不會取代所有人；能用 Agent 組建數位團隊的企業，會先取得效率與創新的複利。", 1.25, 5.95, 10.8, 0.3, size=15, color_name="gold", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def build():
    theme = load_theme(".codex/skills/article-to-presentation/templates/theme.json")
    prs = new_presentation()
    for maker in [
        cover,
        shift_slide,
        value_slide,
        anatomy_slide,
        levels_slide,
        maturity_slide,
        multi_agent_slide,
        protocols_slide,
        ops_slide,
        scientist_slide,
        taiwan_slide,
        roadmap_slide,
    ]:
        maker(prs, theme)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
