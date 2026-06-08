# 2026 Agent Skills 完全指南：簡報大綱摘要與開發者決策指南

來源：Danny Huang〈2026 Agent Skills 完全指南：建立、分享與保護 AI Agent 能力〉，Termdock，2026-03-16。  
原文網址：https://www.termdock.com/blog/agent-skills-guide/zh

## 一句話摘要

Agent Skills 是以 `SKILL.md` 為核心的開放標準，把團隊規範、流程、約束與領域知識封裝成 AI Agent 可按需載入的能力；它已快速形成近五十萬技能的生態系，但也帶來供應鏈與 prompt injection 安全風險，必須以版本治理、最小工具權限與持續測試來管理。

## 核心重點

1. **Skill 填補通用智慧與具體好用之間的落差**  
   強大的模型不知道團隊 style guide、deploy pipeline 或合規要求。Skill 把這些 context 編碼一次，讓 agent 每次執行任務時都能套用。

2. **SKILL.md 格式刻意簡單**  
   每個 skill 從 `SKILL.md` 開始：YAML frontmatter 提供機器可讀 metadata，Markdown body 提供人類可讀指令。必填欄位是 `name` 與 `description`。

3. **Description 是觸發器，也是最高槓桿優化點**  
   Agent 讀 description 來判斷 skill 是否相關。寫得太泛會不觸發；寫得具體才能提高可靠性。

4. **漸進式揭露降低 context 成本**  
   Frontmatter 永遠載入，完整 body 只在相關時載入，外部參考檔與 scripts 則按需讀取或執行。這讓安裝多個 skill 仍能維持 context window 經濟性。

5. **生態系已快速規模化**  
   截至 2026 年 3 月，三大 marketplace 合計超過 490K 個 skill。SkillsMP 主打數量，Skills.sh 主打策展與 Snyk 掃描，ClawHub 則因惡意 skill 事件成為風險案例。

6. **跨 Agent 相容性來自核心規範**  
   Claude Code、Codex CLI、GitHub Copilot 都支援 `SKILL.md`。若需跨平台，應堅持 `name`、`description`、Markdown body，避免 agent 專屬 frontmatter。

7. **安全風險已成為一級議題**  
   Snyk 掃描 3,984 個 skill，36.8% 至少有漏洞，13.4% 有重大問題；惡意 skill 可透過 shell 執行、檔案讀取與 prompt injection 造成資料外洩。

8. **團隊治理要把 skill 當程式碼看**  
   專案 skill 應進入 code review、版本 pinning、代表性任務測試與定期安全稽核。Skill 是隨專案演進的活文件。

## 簡報敘事線

簡報以「讓 AI Agent 從聰明新人變成遵守團隊規範的工程師」為主軸：

1. 用新人與食譜比喻說明為何需要 skill。
2. 拆解 `SKILL.md` 格式、description、漸進式揭露。
3. 看生態系與三大 marketplace 的成長。
4. 說明如何建立第一個 skill 與跨 Claude/Codex/Copilot 使用。
5. 導入 Superpowers 作為方法論框架。
6. 用安全數據與 ClawHavoc 事件說明治理必要性。
7. 以最佳實踐、團隊共享、context engineering 與上手 checklist 收束。

## 投影片大綱

### Slide 1：封面

**重點**：
- 2026 Agent Skills 完全指南。
- 建立、分享與保護 AI Agent 能力。
- 視覺：SKILL.md、marketplace、agent、security shield 節點。

### Slide 2：為什麼需要 Skills

**重點**：
- 沒有 skill 的 AI coding agent 像沒讀過 style guide 的天才新人。
- 通用智慧不等於具體好用。
- Skill 把團隊 context 編碼一次，讓 agent 每次套用。

### Slide 3：Agent Skill 是什麼

**重點**：
- 一個資料夾，加上 `SKILL.md`、可選 scripts、參考資料和範例。
- 不需要編譯、runtime 或 dependency graph。
- 像 AI agent 的 npm：可複用知識、流程與約束。

### Slide 4：SKILL.md 格式

**重點**：
- YAML frontmatter：name、description、allowed-tools、metadata、license。
- Markdown body：Instructions、Conventions、Example。
- `name` 小寫連字號，最長 64 字元；`description` 最長 1,024 字元。

### Slide 5：Description 決定觸發率

**重點**：
- Description 是反向搜尋查詢。
- Agent 用它搜尋 skill 庫的相關性。
- 最佳化方式是明確寫出任務、方法與輸出格式。

### Slide 6：漸進式揭露

**重點**：
- Frontmatter 永遠載入。
- Body 只在 skill 相關時載入。
- 大型 skill 透過外部檔案與 scripts 按需讀取。

### Slide 7：490K+ 生態系

**重點**：
- SkillsMP：400K+，數量霸主。
- Skills.sh：83K+、8M+ 安裝，主打 CLI 原生安裝與 Snyk 掃描。
- ClawHub：~10K+，但遭 ClawHavoc 惡意攻擊。

### Slide 8：建立第一個 Skill

**重點**：
- 建目錄：個人或專案 skill 位置。
- 寫 SKILL.md：定義 review 流程與輸出格式。
- 測試：用應該觸發的 prompt 驗證。
- 優化 description：讓觸發更穩。

### Slide 9：跨 Agent 使用

**重點**：
- Claude Code：`~/.claude/skills/`、`.claude/skills/`、Marketplace。
- Codex CLI：`.agents/skills/` 或 `.codex/skills/`。
- GitHub Copilot：`.github/skills/`。
- 核心規範可無修改跨 agent 運作。

### Slide 10：Superpowers 與 Skills 框架

**重點**：
- Superpowers 是以 skill 組合成的軟體開發方法論。
- 涵蓋 Brainstorming、Planning、TDD、Code Review、Debugging、Documentation。
- 強制機制讓 agent 先規劃、先測試，再實作。

### Slide 11：安全性：13.4% 重大問題

**重點**：
- Snyk 掃描 3,984 個 skill。
- 36.8% 至少有漏洞。
- 13.4% 包含重大問題。
- 76 個確認為惡意載荷，91% 結合 prompt injection 和惡意軟體。

### Slide 12：威脅模型與防禦

**重點**：
- 攻擊向量：shell 執行、檔案系統存取、prompt injection。
- 防禦：驗證來源、閱讀 SKILL.md、使用 allowed-tools、拒絕系統密碼要求、定期掃描。

### Slide 13：架構最佳實踐與團隊治理

**重點**：
- SKILL.md 保持 500 行以內。
- 確定性任務用 scripts。
- 一個 skill，一個動詞。
- 專案 skill 像程式碼一樣 review、pin、測試。

### Slide 14：Context Engineering 與上手 Checklist

**重點**：
- CLAUDE.md / AGENTS.md：專案憲法，永遠載入。
- SKILL.md：任務能力，按需載入。
- MCP Server：外部即時資料與工具。
- 上手：理解規範、建個人 skill、建專案 skill、測觸發、掃安全、每週迭代。

## 開發者決策指南

### 入門順序

1. 先讀懂 `SKILL.md` 核心欄位：`name`、`description`、Markdown body。
2. 用 code review、PR description 或 component creation 建第一個個人 skill。
3. 用 5 種不同 phrasing 測試 description 觸發可靠性。
4. 把專案規範封裝成 `.claude/skills/`、`.codex/skills/` 或 `.github/skills/`。
5. 對 marketplace skill 做版本 pinning、SKILL.md review 與安全掃描。

### 推薦練習題

1. 將團隊 code review checklist 轉成一份 `SKILL.md`。
2. 將一個超過 500 字的 CLAUDE.md 拆出任務型 skill。
3. 設計一個只允許讀檔、不允許 shell 的 `allowed-tools` 策略。
4. 比較 Claude Code、Codex CLI、Copilot 的 skill 目錄慣例，設計 symlink 共享方案。

### 檢核問題

1. 為什麼 description 是 skill 中最高槓桿的欄位？
2. 什麼內容應放在 references 而不是 SKILL.md body？
3. 為什麼 marketplace skill 應該 pin 版本？
4. Shell 執行、檔案系統存取與 prompt injection 分別會造成什麼風險？
