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


OUT = Path("outputs/gemma_4_pi_agent_deck.pptx")
SOURCE = "Patrick Loeber｜2026-04-27｜patloeber.com/gemma-4-pi-agent/"


def customize(theme):
    theme.colors.update(
        {
            "graphite": "20252B",
            "green": "2E8B57",
            "lime": "B6E35D",
            "blue": "3F7CAC",
            "orange": "F29E4C",
            "rose": "D1495B",
            "mist": "EEF4F2",
            "panel": "FAFAF7",
        }
    )
    return theme


def cover(prs, theme):
    slide = blank_slide(prs, "graphite", theme)
    nodes = [
        (7.5, 1.0, "LM Studio", "blue"),
        (10.2, 1.2, "Gemma 4", "green"),
        (9.15, 3.0, "localhost:1234", "lime"),
        (7.65, 5.0, "Pi", "orange"),
        (10.35, 5.15, "Terminal", "rose"),
    ]
    for a, b in [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)]:
        x1, y1, _, _ = nodes[a]
        x2, y2, _, _ = nodes[b]
        line(slide, theme, x1 + 0.62, y1 + 0.28, x2 + 0.62, y2 + 0.28, "mint", 1.2)
    for x, y, label, fill in nodes:
        rect(slide, theme, x, y, 1.35, 0.58, fill)
        add_text(slide, theme, label, x + 0.09, y + 0.19, 1.15, 0.12, size=8.3, color_name="white", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "Gemma 4 + Pi\n本機 Coding Agent", 0.78, 1.05, 6.1, 1.35, size=32, color_name="white", bold=True, font=theme.heading_font)
    add_text(slide, theme, "用 LM Studio 把開放模型接到 terminal agent", 0.82, 2.78, 5.9, 0.32, size=15.5, color_name="cream")
    rect(slide, theme, 0.82, 3.55, 5.35, 0.95, "green")
    add_text(slide, theme, "模型在本機、API 在 localhost、工具在 terminal", 1.08, 3.86, 4.8, 0.2, size=10.8, color_name="white", bold=True)
    add_footer(slide, theme, SOURCE, dark=True)


def why_local(prs, theme):
    slide = blank_slide(prs, "panel", theme)
    add_title(slide, theme, "為什麼要跑本機 Coding Agent", "不是取代雲端模型，而是取得控制權與實驗空間")
    items = [
        ("資料控制", "程式碼與文件留在自己的機器，適合敏感 repo 與離線實驗。", "green"),
        ("可調校", "模型、量化、context size、GPU offload 都能自己調。", "blue"),
        ("低延遲迭代", "terminal agent 可直接讀寫檔案、執行指令、快速修正。", "orange"),
    ]
    for i, (title, body, accent) in enumerate(items):
        add_callout(slide, theme, title, body, 0.9 + i * 4.15, 1.9, 3.45, 2.15, accent)
    rect(slide, theme, 1.25, 5.0, 10.85, 0.78, "graphite")
    add_text(slide, theme, "提醒：本機模型不等於可信模型；它仍可能 hallucinate、誤用工具或產生危險 shell 指令。", 1.58, 5.27, 10.2, 0.18, size=11.8, color_name="cream", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def architecture(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "三層架構", "模型服務、OpenAI-compatible API、terminal coding harness")
    boxes = [
        (0.9, "LM Studio", "下載 GGUF、設定量化、啟動 local server", "blue"),
        (4.95, "Gemma 4 26B A4B", "本機推論，支援 function calling 與 thinking modes", "green"),
        (9.0, "Pi Agent", "在 terminal 中使用 read/write/edit/bash", "orange"),
    ]
    for x, title, body, accent in boxes:
        rect(slide, theme, x, 2.0, 3.25, 2.55, "mist", line="line")
        circle(slide, theme, x + 0.28, 2.32, 0.36, accent)
        add_text(slide, theme, title, x + 0.78, 2.34, 2.1, 0.2, size=14.5, color_name="ink", bold=True)
        add_text(slide, theme, body, x + 0.34, 3.2, 2.55, 0.55, size=10.6, color_name="muted")
    line(slide, theme, 4.15, 3.2, 4.9, 3.2, "green", 2.2)
    line(slide, theme, 8.2, 3.2, 8.95, 3.2, "green", 2.2)
    rect(slide, theme, 4.75, 5.45, 3.85, 0.52, "graphite")
    add_text(slide, theme, "http://localhost:1234/v1", 4.98, 5.63, 3.35, 0.12, size=10.5, color_name="lime", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def model_choice(prs, theme):
    slide = blank_slide(prs, "mist", theme)
    add_title(slide, theme, "為什麼選 Gemma 4 26B A4B", "MoE 讓本機 coding agent 在品質與速度之間取得甜蜜點")
    rect(slide, theme, 0.95, 1.8, 5.2, 3.9, "graphite")
    add_text(slide, theme, "26B total\n4B active", 1.45, 2.35, 3.7, 0.8, size=30, color_name="lime", bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, theme, "Mixture-of-Experts：每個 token 只啟用部分參數，但完整權重仍要載入記憶體。", 1.35, 4.28, 3.85, 0.42, size=11.3, color_name="cream", align=PP_ALIGN.CENTER)
    add_bullets(slide, theme, ["文字與影像理解", "Function calling", "System prompt support", "Thinking modes"], 7.0, 2.0, 4.7, size=13.2, gap=0.58)
    rect(slide, theme, 7.0, 5.35, 4.45, 0.6, "white", line="line")
    add_text(slide, theme, "低 VRAM 可試 E4B，但需要更明確的提示與任務拆解。", 7.25, 5.56, 3.9, 0.12, size=9.6, color_name="muted", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def quantization(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "量化與 VRAM 取捨", "先讓模型穩定跑起來，再追求品質")
    rows = [
        ("Q4_K_M", "18 GB", "Good balance", "green"),
        ("Q6_K", "24 GB", "Higher quality", "blue"),
        ("Q8_0", "28 GB", "Near-original", "orange"),
    ]
    for i, (q, size, quality, accent) in enumerate(rows):
        y = 1.75 + i * 1.25
        rect(slide, theme, 1.05, y, 2.25, 0.72, accent)
        rect(slide, theme, 3.55, y, 2.5, 0.72, "mist", line="line")
        rect(slide, theme, 6.35, y, 4.9, 0.72, "mist", line="line")
        add_text(slide, theme, q, 1.3, y + 0.26, 1.7, 0.12, size=12, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, size, 3.82, y + 0.26, 1.85, 0.12, size=12, color_name="ink", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, quality, 6.65, y + 0.26, 4.15, 0.12, size=11.6, color_name="muted", align=PP_ALIGN.CENTER)
    rect(slide, theme, 1.05, 5.75, 10.2, 0.62, "graphite")
    add_text(slide, theme, "推薦起點：Q4_K_M。若還有 VRAM，再往 Q6_K 或 Q8_0 測試。", 1.38, 5.98, 9.5, 0.12, size=11.2, color_name="cream", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def lm_studio(prs, theme):
    slide = blank_slide(prs, "panel", theme)
    add_title(slide, theme, "啟動 LM Studio Server", "把本機模型變成 OpenAI-compatible endpoint")
    steps = [
        ("1", "Developer tab", "進入 LM Studio 的 Developer 頁籤。"),
        ("2", "Select model", "選擇已下載的 Gemma 4 GGUF。"),
        ("3", "Start Server", "啟動預設 localhost:1234 server。"),
        ("4", "Verify", "curl http://localhost:1234/v1/models"),
    ]
    for i, (num, title, body) in enumerate(steps):
        x = 0.85 + i * 3.05
        rect(slide, theme, x, 2.0, 2.45, 2.6, "white", line="line")
        circle(slide, theme, x + 0.3, 2.32, 0.42, ["blue", "green", "orange", "rose"][i])
        add_text(slide, theme, num, x + 0.42, 2.45, 0.18, 0.1, size=10, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, title, x + 0.32, 3.05, 1.8, 0.2, size=12.5, color_name="ink", bold=True)
        add_text(slide, theme, body, x + 0.32, 3.68, 1.75, 0.45, size=9.5, color_name="muted")
        if i < 3:
            line(slide, theme, x + 2.45, 3.28, x + 3.05, 3.28, "green", 1.8)
    add_footer(slide, theme, SOURCE)


def context_slide(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Context Size 與 GPU Offload", "最大 context 不一定是最佳 context")
    rows = [
        ("16K", "小修改、單檔任務", "~1 GB"),
        ("64K", "一般 coding session", "~4 GB"),
        ("128K", "多檔重構", "~8 GB"),
        ("256K", "完整 repo context", "~16 GB"),
    ]
    for i, (ctx, use, vram) in enumerate(rows):
        y = 1.42 + i * 0.78
        rect(slide, theme, 0.95, y, 1.5, 0.54, "green" if i == 2 else "mist", line=None if i == 2 else "line")
        rect(slide, theme, 2.8, y, 5.1, 0.54, "mist", line="line")
        rect(slide, theme, 8.25, y, 2.05, 0.54, "mist", line="line")
        add_text(slide, theme, ctx, 1.18, y + 0.2, 1.0, 0.1, size=10.5, color_name="white" if i == 2 else "ink", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, use, 3.1, y + 0.2, 4.4, 0.1, size=10.3, color_name="ink")
        add_text(slide, theme, vram, 8.55, y + 0.2, 1.4, 0.1, size=10.3, color_name="muted", bold=True, align=PP_ALIGN.CENTER)
    for x, title, body, accent in [
        (1.05, "實務建議", "作者偏好 128K：coding agent 會累積檔案、工具輸出與對話歷史；若 OOM，先降低 context size。", "orange"),
        (6.95, "GPU Offload", "GPU layers 越多越快，但需要更多 VRAM；放不下時會分到 CPU，仍可用但較慢。", "blue"),
    ]:
        rect(slide, theme, x, 5.28, 5.05, 1.2, "white", line="line")
        circle(slide, theme, x + 0.25, 5.55, 0.26, accent)
        add_text(slide, theme, title, x + 0.65, 5.54, 3.8, 0.18, size=12.8, color_name="ink", bold=True)
        add_text(slide, theme, body, x + 0.25, 6.02, 4.55, 0.32, size=9.2, color_name="muted")
    add_footer(slide, theme, SOURCE)


def pi_install(prs, theme):
    slide = blank_slide(prs, "graphite", theme)
    add_title(slide, theme, "安裝與理解 Pi", "小而清楚的 terminal coding harness", dark=True)
    rect(slide, theme, 0.95, 1.8, 5.05, 1.05, "white")
    add_text(slide, theme, "npm install -g @mariozechner/pi-coding-agent", 1.28, 2.22, 4.35, 0.12, size=10, color_name="ink", bold=True)
    tools = [("read", "讀檔"), ("write", "寫檔"), ("edit", "修改"), ("bash", "執行")]
    for i, (tool, label) in enumerate(tools):
        x = 1.05 + i * 2.85
        rect(slide, theme, x, 4.15, 2.1, 0.82, ["blue", "green", "orange", "rose"][i])
        add_text(slide, theme, tool, x + 0.18, 4.38, 0.8, 0.12, size=12.5, color_name="white", bold=True)
        add_text(slide, theme, label, x + 1.1, 4.4, 0.6, 0.1, size=8.5, color_name="white", align=PP_ALIGN.CENTER)
    add_text(slide, theme, "Pi 的核心刻意小：少工具、少 system prompt、少 token 成本，適合本機模型做 context engineering。", 1.05, 5.9, 10.8, 0.28, size=12.2, color_name="cream", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def model_config(prs, theme):
    slide = blank_slide(prs, "panel", theme)
    add_title(slide, theme, "把 Pi 連到本機模型", "models.json 指向 LM Studio 的 localhost server")
    rect(slide, theme, 0.95, 1.65, 5.6, 4.9, "graphite")
    code = '{\n  "providers": {\n    "lmstudio": {\n      "baseUrl": "http://localhost:1234/v1",\n      "api": "openai-completions",\n      "apiKey": "lm-studio"\n    }\n  }\n}'
    add_text(slide, theme, code, 1.25, 2.0, 4.9, 3.6, size=10.2, color_name="lime", font="Consolas")
    add_bullets(
        slide,
        theme,
        ["檔案位置：~/.pi/agent/models.json", "model id 必須符合 LM Studio server tab", "啟動 pi 後用 /model 切換到本機模型", "設定完成後 agent 全程走 localhost"],
        7.15,
        2.0,
        4.8,
        size=12.2,
        gap=0.62,
    )
    add_footer(slide, theme, SOURCE)


def skills_extensions(prs, theme):
    slide = blank_slide(prs, "white", theme)
    add_title(slide, theme, "Skills 與 Extensions", "讓輕量 agent 取得專案能力與安全控制")
    rect(slide, theme, 0.95, 1.8, 5.3, 3.75, "mist", line="line")
    rect(slide, theme, 7.05, 1.8, 5.3, 3.75, "graphite")
    add_text(slide, theme, "Skills", 1.3, 2.25, 1.5, 0.24, size=17, color_name="green", bold=True)
    add_bullets(slide, theme, ["Markdown capability packages", "可安裝 user-level 或 project-level", "適合流程、規範、文件解析與簡報生成"], 1.35, 3.0, 4.2, size=11.4, gap=0.54)
    add_text(slide, theme, "Extensions", 7.4, 2.25, 1.8, 0.24, size=17, color_name="orange", bold=True)
    add_bullets(slide, theme, ["TypeScript modules", "可加入工具、命令、UI、permission gates", "適合更深的 agent 行為客製"], 7.45, 3.0, 4.2, dark=True, size=11.4, gap=0.54)
    add_footer(slide, theme, SOURCE)


def security(prs, theme):
    slide = blank_slide(prs, "mist", theme)
    add_title(slide, theme, "安全與治理", "本機執行降低資料外流，但放大 shell 風險")
    risks = [
        ("YOLO Bash", "Pi 預設會快速執行 bash；效率高，也可能執行錯誤或破壞性命令。", "rose"),
        ("Permission Gate", "對高風險操作加確認步驟，避免模型自行越權。", "orange"),
        ("Sandbox", "需要更強隔離時，把命令放進 container 或受控環境。", "blue"),
    ]
    for i, (title, body, accent) in enumerate(risks):
        add_callout(slide, theme, title, body, 0.9 + i * 4.15, 1.85, 3.45, 2.2, accent)
    rect(slide, theme, 1.2, 5.15, 10.85, 0.78, "graphite")
    add_text(slide, theme, "原則：模型可以在本機跑，但工具權限仍要最小化、可審查、可中止。", 1.55, 5.43, 10.1, 0.15, size=12.1, color_name="cream", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE)


def checklist(prs, theme):
    slide = blank_slide(prs, "graphite", theme)
    add_title(slide, theme, "上手 Checklist", "先跑通最小閉環，再加入能力與保護層", dark=True)
    steps = [
        ("01", "安裝 LM Studio"),
        ("02", "下載 Gemma 4 26B A4B Q4_K_M"),
        ("03", "Start Server 並 curl /v1/models"),
        ("04", "調 context size 與 GPU offload"),
        ("05", "安裝 Pi 並設定 models.json"),
        ("06", "加入 skills、extensions、permission gate"),
    ]
    for i, (num, text) in enumerate(steps):
        x = 0.95 + (i % 2) * 6.0
        y = 1.65 + (i // 2) * 1.38
        rect(slide, theme, x, y, 5.25, 0.82, "white")
        circle(slide, theme, x + 0.32, y + 0.22, 0.38, ["green", "blue", "orange", "rose", "green", "blue"][i])
        add_text(slide, theme, num, x + 0.41, y + 0.35, 0.18, 0.1, size=8, color_name="white", bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, theme, text, x + 0.9, y + 0.31, 3.95, 0.12, size=11, color_name="ink", bold=True)
    add_text(slide, theme, "完成後，你就有一個模型、資料與工具鏈都在自己機器上的 coding agent workflow。", 1.1, 6.25, 11.1, 0.28, size=12.5, color_name="lime", bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, theme, SOURCE, dark=True)


def build():
    theme = customize(load_theme(".codex/skills/article-to-presentation/templates/theme.json"))
    prs = new_presentation()
    for maker in [
        cover,
        why_local,
        architecture,
        model_choice,
        quantization,
        lm_studio,
        context_slide,
        pi_install,
        model_config,
        skills_extensions,
        security,
        checklist,
    ]:
        maker(prs, theme)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
