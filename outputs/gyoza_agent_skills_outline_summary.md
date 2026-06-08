# Agent Skills 是什麼？超簡單入門與實作指南：簡報大綱摘要與學習指南

來源：閃電煎餃〈Agent Skills 是什麼？超簡單入門與實作指南〉，煎餃的調味實驗室，2026-03-24 發佈、2026-06-06 更新。  
原文網址：https://gyozalab.com/agent-skills-guide

## 一句話摘要

Agent Skills 是把重複 SOP 封裝成可攜帶、可版本控管、可漸進式載入的技能包，讓 AI Agent 在需要時讀取專業流程、使用工具並穩定產出指定結果，而不是每次都靠使用者重新貼 prompt。

## 核心重點

1. **Skills 解決「人肉 API」問題**  
   使用者不必每次重新貼格式、指令與脈絡；把工作規則定義一次，AI 之後就能自動套用。

2. **Agent、Skills、模型的角色不同**  
   模型像處理器，提供推理能力；Agent 像作業系統，提供能操作工具的環境；Skills 像應用程式，提供特定場景的專業流程。

3. **Skills 不只是 Prompt 升級版**  
   Prompt 是單次文字，GPTs/Gems 多半綁定平台；Agent Skills 是包含指令與資源的資料夾，可放在檔案系統、用 Git 管理，也可跨平台遷移。

4. **SKILL.md 是技能包核心**  
   每個 Skill 至少包含 `SKILL.md`。上半部 YAML frontmatter 是 AI 判斷是否觸發的名片，下半部 Markdown 是具體工作說明書。`references/`、`scripts/`、`assets/` 則視需求選配。

5. **漸進式載入維持效率**  
   AI 先看所有 Skill 的名稱與描述，相關時才讀完整 `SKILL.md`，真正需要時才開啟 references 或 scripts。這避免把大量資料一次塞進 context window。

6. **好用 Skill 的關鍵在描述與可推理指令**  
   description 要明確包含做什麼、何時觸發與關鍵能力；指令要說明 why，不只列 what；核心內容要控制篇幅；用範例校準比堆規則更有效。

7. **不用寫程式也能建立第一個 Skill**  
   可直接呼叫 Skill Creator，也可先跑通一次任務、從對話中提煉流程，再打包成技能。

8. **借用第三方 Skills 前要做安全查核**  
   先審核 `scripts/`、閱讀 `SKILL.md` 是否外傳資料，初學者優先選只包含文字指令的 Skill。

## 簡報敘事線

簡報以「把一次性 prompt 變成可攜帶的專業流程」為主軸：

1. 先用重複貼 prompt 的痛點建立需求。
2. 定義 Agent Skills，釐清它與 Agent、模型、Project、MCP 的關係。
3. 比較 Prompt、GPTs/Gems、Agent Skills 的生命週期與能力。
4. 拆解技能包資料夾與 `SKILL.md`。
5. 用漸進式載入說明為何 Skills 可以多而不慢。
6. 提煉四個寫作原則與兩種建立路徑。
7. 最後補上生態系、安全查核與第一步行動。

## 投影片大綱

### Slide 1：封面

**重點**：
- Agent Skills 是什麼？
- 從重複 prompt 到可攜帶的 AI 工作流程。
- 視覺：資料夾、名片、工具箱與工作流節點。

### Slide 2：痛點：我們一直在當人肉 API

**重點**：
- 每次開新對話都要重新貼指令、格式與脈絡。
- 小改動會造成格式跑掉。
- 真正需求是把規則定義一次、反覆穩定使用。

### Slide 3：Agent Skills 的一句話定義

**重點**：
- Skill 是可被機器理解、可跨平台遷移、包含背景知識的結構化工作指令集。
- 它不是聊天內容，而是 AI 在特定場景下啟動的專業模式。

### Slide 4：模型、Agent、Skills 的分工

**重點**：
- 模型：處理器，負責思考與推理。
- Agent：作業系統，能調動資源與工具。
- Skills：應用程式，教 AI 在特定任務中怎麼做。

### Slide 5：Prompt、GPTs/Gems、Agent Skills 差異

**重點**：
- Prompt：單次文字，關閉對話即消失。
- GPTs/Gems：平台角色設定，較難跨平台。
- Agent Skills：資料夾形式、可版本控管、可分享、可操作檔案與工具。

### Slide 6：Skills、Project、MCP 如何協作

**重點**：
- Project 提供持久脈絡。
- MCP 連接外部工具與資料。
- Skills 定義拿到工具與資料後要怎麼用。

### Slide 7：技能包長什麼樣

**重點**：
- 必要：`SKILL.md`。
- 選配：`references/`、`scripts/`、`assets/`。
- 優點：壓縮分享、放雲端、Git 版控，累積成專業邏輯庫。

### Slide 8：SKILL.md 的兩層結構

**重點**：
- YAML frontmatter：name 與 description，負責觸發與路由。
- Markdown body：具體流程、輸出格式、分類規則、模糊情境處理。

### Slide 9：漸進式載入三階段

**重點**：
- 第一層：看名片，只讀名稱與描述。
- 第二層：讀說明書，載入相關 Skill 的完整指令。
- 第三層：開工具箱，需要時才讀 references 或執行 scripts。

### Slide 10：四個寫出好 Skill 的原則

**重點**：
- description 決定觸發率。
- 指令要解釋 why。
- `SKILL.md` 控制篇幅，重資料放 references。
- 用 Before/After 範例校準輸出。

### Slide 11：不用寫程式，聊出第一個 Skill

**重點**：
- 方式一：需求清楚時直接呼叫 Skill Creator。
- 方式二：先跑通一次任務，再從對話提煉流程。
- 建立 Skill 是後設認知訓練：起點、終點、中間判斷標準。

### Slide 12：生態系與安全查核

**重點**：
- Skills 生態系包含基礎 Skills、第三方夥伴 Skills、社群分享 Skills。
- 下載前審核 scripts、閱讀 SKILL.md、優先選指令型 Skill。

### Slide 13：第一步行動

**重點**：
- 找一個每週至少重複三次的 AI 指令。
- 用 Skill Creator 打包成第一個 Skill。
- 測試觸發時機、輸出格式與安全邊界。

## 學習指南

### 入門順序

1. 先理解 Agent、模型、Skill 的分工。
2. 比較 Prompt、GPTs/Gems、Agent Skills 的生命週期差異。
3. 讀懂 `SKILL.md` 的 YAML frontmatter 與 Markdown body。
4. 用一個重複任務寫出最小可行 Skill。
5. 測試觸發條件、輸出格式與安全風險。

### 推薦練習題

1. 把你常用的一段 prompt 改寫成 Skill description。
2. 為「會議摘要」Skill 設計 `SKILL.md` 的輸出格式。
3. 畫出一個 Skill 的漸進式載入流程。
4. 檢查一個第三方 Skill，列出它的安全風險。

### 學習檢核問題

1. Skills 與 Prompt 最大差異是什麼？
2. 為什麼 description 會決定 Skill 能否被正確觸發？
3. 什麼內容適合放在 `references/` 而不是 `SKILL.md`？
4. 使用第三方 Skills 前應該先檢查哪些地方？
