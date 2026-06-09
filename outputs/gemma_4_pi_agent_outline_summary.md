# How to run a local coding agent with Gemma 4 and Pi：簡報大綱摘要與學習指南

來源：Patrick Loeber〈How to run a local coding agent with Gemma 4 and Pi〉，2026-04-27。  
原文網址：https://patloeber.com/gemma-4-pi-agent/

## 一句話摘要

這篇文章示範如何用 LM Studio 在本機服務 Gemma 4 26B A4B，並把 Pi coding agent 連到本機 OpenAI-compatible API，建立一個不依賴雲端模型、可擴充 skills 與 extensions 的 terminal coding agent 工作流。

## 核心重點

1. **完整架構很簡單**  
   作者採用 `LM Studio + Pi agent + Gemma 4 26B A4B (Q4_K_M)`：LM Studio 負責下載與服務模型，Pi 作為 terminal coding harness。

2. **Gemma 4 26B A4B 是推薦選擇**  
   它是 MoE 架構，總參數 26B、每 token 啟用 4B，兼顧品質與推論速度；也支援文字、影像理解、function calling 與 thinking modes。

3. **量化選擇取決於 VRAM**  
   Q4_K_M 約 18GB、Q6_K 約 24GB、Q8_0 約 28GB。即使 MoE 每 token 只啟用部分參數，完整模型仍需載入記憶體。

4. **Context size 是主要資源旋鈕**  
   小修改可用 16K，一般 coding session 可用 64K，多檔重構可用 128K，完整 repo context 可到 256K；越大 context 會消耗更多 VRAM。

5. **Pi 的價值在輕量與可擴充**  
   Pi 提供 `read`、`write`、`edit`、`bash` 四個核心工具，系統 prompt 小、token efficient，並可用 skills、extensions、prompt templates 與 themes 擴充。

6. **本機 agent 也需要安全治理**  
   Pi 預設快速執行 shell 指令，搭配本機模型時仍可能產生破壞性命令；permission gate、container sandbox 與 extension 管理是必要保護層。

## 簡報敘事線

簡報以「把 coding agent 搬回自己的硬體」為主軸：

1. 先說明本機 agent 的價值：隱私、控制、離線與可調校。
2. 拆解三層架構：模型、OpenAI-compatible server、terminal agent。
3. 說明 Gemma 4 26B A4B、量化與 context size 的取捨。
4. 走過 LM Studio server 與 Pi `models.json` 設定。
5. 補上 skills、extensions 與安全治理，讓工作流可長期使用。

## 投影片大綱

### Slide 1：封面

**重點**：
- How to run a local coding agent with Gemma 4 and Pi。
- 視覺：Laptop、LM Studio、Gemma、Pi、terminal agent 的本機閉環。

### Slide 2：為什麼要跑本機 Coding Agent

**重點**：
- 自己掌控模型、資料與延遲。
- 適合實驗 coding agent、context engineering 與本機文件處理。
- 不代表零風險，仍需安全控制。

### Slide 3：整體架構

**重點**：
- LM Studio 服務 Gemma 4。
- OpenAI-compatible API 跑在 `localhost:1234`。
- Pi 透過設定檔連線並在 terminal 中使用工具。

### Slide 4：選擇 Gemma 4 26B A4B

**重點**：
- MoE：總參數 26B、每 token 啟用 4B。
- 支援 text、image、function calling、thinking modes。
- E4B 可作為低 VRAM 替代。

### Slide 5：量化與 VRAM 取捨

**重點**：
- Q4_K_M：18GB，平衡選擇。
- Q6_K：24GB，品質更高。
- Q8_0：28GB，接近原始品質。

### Slide 6：啟動 LM Studio Server

**重點**：
- Developer tab 選模型。
- Start Server。
- 用 `curl http://localhost:1234/v1/models` 驗證。

### Slide 7：Context Size 與 GPU Offload

**重點**：
- 16K、64K、128K、256K 對應不同任務規模。
- context 越大，額外 VRAM 越高。
- GPU offload 越多越快，但吃 VRAM。

### Slide 8：安裝與理解 Pi

**重點**：
- `npm install -g @mariozechner/pi-coding-agent`。
- Pi 核心工具是 `read`、`write`、`edit`、`bash`。
- 小系統 prompt 有利於本機模型。

### Slide 9：連接 Pi 到本機模型

**重點**：
- 編輯 `~/.pi/agent/models.json`。
- provider 指向 `http://localhost:1234/v1`。
- model id 要符合 LM Studio server tab。

### Slide 10：Skills 與 Extensions

**重點**：
- Skills 是 Markdown capability packages。
- Extensions 是 TypeScript 模組，可提供工具、命令、UI 與 permission gates。
- 兩者讓輕量 agent 具備專案能力。

### Slide 11：安全與治理

**重點**：
- Pi 預設 YOLO 執行 bash，速度快但有風險。
- 用 permission-gate、container sandbox、最小權限降低破壞性命令風險。
- 本機模型不等於可信模型。

### Slide 12：上手 Checklist

**重點**：
- 安裝 LM Studio。
- 下載 Gemma 4 26B A4B GGUF。
- 啟動 server、調 context、安裝 Pi、設定 models.json。
- 加入 skills/extensions，並建立安全邊界。

## 學習指南

### 入門順序

1. 先用 LM Studio 成功跑起 `localhost:1234`。
2. 用 `curl /v1/models` 確認 API 可用。
3. 安裝 Pi，先用簡單 repo 測 `read` 與 `edit`。
4. 再調高 context size 與 GPU offload。
5. 最後加入 skills 與 permission-related extensions。

### 推薦練習題

- 用 Pi 對一個小型 repo 做 README 改寫。
- 建立一個 project-level skill，要求 agent 固定使用繁中回覆。
- 比較 64K 與 128K context 在多檔重構時的差異。
- 加上 permission gate，測試危險 bash 指令是否會被攔截。

### 學習檢核問題

- 為什麼 MoE 模型仍需要載入完整參數？
- context size 與 VRAM 的關係是什麼？
- Pi 為什麼只提供四個核心工具？
- 本機 agent 在安全上有哪些誤解？
- 什麼情況適合用 skill，什麼情況適合用 extension？
