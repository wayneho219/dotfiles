# Claude Code — Global Rules

## Language
- 溝通與計畫文件一律用繁體中文。commit 訊息用英文；程式碼註解跟隨該專案現有語言。
- 答案中出現標準名稱、等級、縮寫時，順帶用一句話解釋具體內容。

## Skills
- git 操作（commit、branch、push、PR）→ `git-workflow`
- 前端頁面、元件、樣式 → `frontend-design`
- 寫筆記（「幫我做筆記」「整理成筆記」「記錄這個」）→ `note-taking`
- 碩論推到 Overleaf（「推到 overleaf」「同步 overleaf」）→ `overleaf-sync`；這是推到 Overleaf 專案的 git，不套用 `git-workflow` 的分支規則
- 其他任務不要載入以上 skill。

### 觸發原則（優先於 superpowers 的「有 1% 可能就必須載入」規則，該規則不採用）
- **直接用，不問**：使用者說出 skill 描述裡的觸發詞，或任務本身就是該 skill 的用途。
- **不載入**：只是沾到邊。例如回答問題、解釋概念、小幅修改、編輯既有檔案時，不因為「可能有幫助」就載入。
- **先問一句**：只有在兩個條件同時成立時才問：真的拿不準，而且用不用 skill 會明顯改變產出或成本（例如會做出 Artifact 網頁、跑多步驟流程、開 subagent）。只問一行「要用 X 嗎？」。差別不大時自己決定，不要問。
- 同一個 session 裡問過的 skill，照使用者的答案處理，不重複問。
- superpowers 的流程類 skill（brainstorming、writing-plans、TDD、subagent 等）只在使用者要求，或要從零開發一個有規模的新功能時使用；問答、論文編輯、小改動不用。

## Herdr（有 `$HC_TERMINAL_ID` 時）
- `hc ls`：列出終端機（含 `dgx_spark_ts/tN`）；`hc read <t> | tail -N`：讀畫面，只看錯誤用 `| grep -i -m 20 "error\|traceback"`
- `hc send <t> "文字"`：打字並按 Enter；送之前先 `hc read` 確認閒著、沒有草稿
- `hc wait <t>`：等 agent 講完（一般 shell 不要用，會一直等）；等特定輸出用 `--output "X"`，不要重複輪詢
- `hc exec --on dgx_spark_ts "<cmd>"`：在 DGX 跑短指令
- `hc run --bg --on dgx_spark_ts --cwd <dir> <cmd>`：在 DGX 跑長任務
- DGX 文字檔：`hc file read|edit|write --on dgx_spark_ts <path>`；二進位、資料夾、大檔用 scp／rsync（主機 `dgx_spark_ts`）
- `herdr-app do pane.split:right` / `tab.new`：開 pane、tab
- 其他用法才跑 `hc --skill`

## Boundaries
- 密碼、token、API key 只放環境變數或 `.env`，不寫進程式碼、alias、shell 設定檔或任何會被 commit 的檔案。

@RTK.md
