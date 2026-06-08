from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path("outputs/ai_agent_architecture_diagram.png")
W, H = 1800, 1150

COLORS = {
    "bg": "#FFFFFF",
    "line": "#A9A9A9",
    "center": "#373076",
    "perception": "#F5A623",
    "planning": "#5A56C8",
    "action": "#D63E9F",
    "memory": "#009B7A",
    "top": "#F8DCA8",
    "left": "#DDD7FB",
    "right": "#CDEFE9",
    "bottom": "#F5C7EC",
    "text": "#333333",
    "muted": "#777777",
    "white": "#FFFFFF",
}


def font(size, bold=False):
    path = "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc"
    return ImageFont.truetype(path, size=size)


def rounded(draw, box, fill, radius=16):
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def text_center(draw, box, text, size=30, fill=COLORS["text"], bold=True, spacing=8):
    f = font(size, bold)
    lines = text.split("\n")
    heights = []
    widths = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=f)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    total_h = sum(heights) + spacing * (len(lines) - 1)
    x1, y1, x2, y2 = box
    y = y1 + (y2 - y1 - total_h) / 2
    for line, line_w, line_h in zip(lines, widths, heights):
        draw.text((x1 + (x2 - x1 - line_w) / 2, y), line, font=f, fill=fill)
        y += line_h + spacing


def box(draw, x, y, w, h, fill, label, size=30, color=COLORS["text"], bold=True):
    rounded(draw, (x, y, x + w, y + h), fill)
    text_center(draw, (x, y, x + w, y + h), label, size=size, fill=color, bold=bold)


def line(draw, p1, p2, width=4):
    draw.line([p1, p2], fill=COLORS["line"], width=width)


def main():
    img = Image.new("RGB", (W, H), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    # Main modules
    box(draw, 835, 400, 300, 280, COLORS["center"], "AI Agent", size=44, color=COLORS["white"])
    box(draw, 840, 270, 290, 72, COLORS["perception"], "1. Perception", size=32, color=COLORS["white"])
    box(draw, 500, 485, 280, 72, COLORS["planning"], "2. Planning", size=32, color=COLORS["white"])
    box(draw, 840, 750, 290, 72, COLORS["action"], "3. Action", size=32, color=COLORS["white"])
    box(draw, 1195, 485, 280, 72, COLORS["memory"], "4. Memory", size=32, color=COLORS["white"])

    line(draw, (985, 342), (985, 400))
    line(draw, (780, 521), (835, 521))
    line(draw, (1135, 521), (1195, 521))
    line(draw, (985, 680), (985, 750))

    # Perception inputs
    for x, label in [(520, "感測器"), (850, "處理單元\nGPU / CPU"), (1210, "多模態\nModel")]:
        box(draw, x, 90, 245, 118, COLORS["top"], label, size=30)
        line(draw, (x + 122, 208), (985, 270), width=3)

    # Planning stack
    planning = [
        ("規劃演算法\nPlanning Algorithm", 160, 250),
        ("大語言模型\nLLM", 160, 420),
        ("知識圖譜\nKnowledge Graph", 160, 590),
        ("推理引擎\nInference Engine", 160, 760),
    ]
    for label, x, y in planning:
        box(draw, x, y, 280, 105, COLORS["left"], label, size=26)
        line(draw, (440, y + 52), (500, 521), width=3)
    box(draw, 70, 265, 55, 105, "#ECE8FF", "複雜\n任務\n分解", size=20, color=COLORS["muted"])
    box(draw, 70, 790, 55, 105, "#ECE8FF", "制定\n行動\n計劃", size=20, color=COLORS["muted"])

    # Memory stack
    for label, y in [("原始知識庫\nKM", 151), ("短期記憶", 450), ("長期記憶", 680)]:
        box(draw, 1530, y, 230, 120, COLORS["right"], label, size=28)
        line(draw, (1530, y + 60), (1475, 521), width=3)
    line(draw, (1635, 570), (1635, 680), width=3)
    line(draw, (1675, 680), (1675, 570), width=3)
    text_center(draw, (1585, 595, 1640, 625), "構成", size=20, fill=COLORS["muted"])
    text_center(draw, (1675, 595, 1735, 625), "讀取", size=20, fill=COLORS["muted"])

    # Action stack
    actions = [
        ("外部工具\nTools", "API整合、數據分析、時程控管", 510),
        ("外部服務", "SQL、Cloud Service、Search", 840),
        ("反饋與決策機制", "評估、回饋、下一輪規劃", 1170),
    ]
    for label, caption, x in actions:
        box(draw, x, 920, 265, 105, COLORS["bottom"], label, size=27)
        rounded(draw, (x, 1042, x + 265, 1082), "#F9E4F5", radius=8)
        text_center(draw, (x + 8, 1048, x + 257, 1076), caption, size=17, fill=COLORS["muted"], bold=False)
        line(draw, (x + 132, 920), (985, 822), width=3)

    text_center(draw, (0, 1102, W, 1142), "AI Agent 參考架構圖", size=40, fill=COLORS["muted"], bold=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
