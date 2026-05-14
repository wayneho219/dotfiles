---
name: session-cleanup
description: Review and clean up old Claude Code sessions. Use this skill whenever the user wants to manage, review, delete, or organize their Claude conversation history. Trigger on phrases like "清理 session", "整理對話", "刪掉舊的 session", "clean up sessions", "review my sessions", "哪些 session 可以刪", or any mention of having too many sessions or wanting to free up space in Claude.
---

# Session Cleanup

幫使用者審視並清理 Claude Code 的舊 session 紀錄。

## 流程概覽

1. 執行腳本取得所有 session 的 metadata 與對話片段
2. 為每個 session 寫一行中文摘要
3. 以表格列出，讓使用者選擇要刪哪些
4. 確認後刪除（`.jsonl` + 同名資料夾）

---

## Step 1：掃描所有 sessions

執行：

```bash
python3 ~/.claude/plugins/cache/user-skills/user-skills/1.0.0/skills/session-cleanup/scripts/list_sessions.py
```

這個腳本會輸出 JSON，每筆包含：
- `uuid`、`project`（所在 project 目錄名）
- `file`（`.jsonl` 的完整路徑）
- `dir`（同名資料夾路徑，若存在）
- `size_kb`、`modified`（最後修改時間）
- `messages`：前 4 條有意義的對話（role + text 前 400 字）

---

## Step 2：為每個 session 寫摘要

讀取每筆 session 的 `messages`，用**一句中文**概括這個 session 在做什麼。

摘要原則：
- 重點是「做了什麼」，例如「除錯 FastAPI 認證問題」、「建立 dotfiles GitHub repo」
- 如果訊息看不出內容（空的或只有系統訊息），寫「(無法辨識內容)」
- 保持簡短，不超過 20 個字

---

## Step 3：呈現清單

依 project 分組，按最後修改時間由新到舊排列，格式如下：

```
📁 Project: ~/.claude/projects/-Users-wayneho  (18 個 sessions)

 #   日期              大小    摘要
 1   2026-04-21 18:05   45 KB  整理終端設定並建立 dotfiles GitHub repo
 2   2026-04-21 14:12   12 KB  執行 Pokemon champions Task 8 與 9
 3   2026-04-19 09:33    8 KB  除錯 FastAPI 登入認證問題
...

📁 Project: ~/.claude/projects/-Users-wayneho-Desktop  (5 個 sessions)
...
```

顯示完後問：
> 請輸入要**刪除**的編號（例如：`1 3 5`、`all`、`all except 2 4`）
> 或輸入 `cancel` 取消。

---

## Step 4：解析使用者輸入

支援以下格式：
- `1 3 5` — 刪除編號 1、3、5
- `1-5` — 刪除編號 1 到 5
- `all` — 刪除全部
- `all except 2 4` — 保留 2、4，其餘全刪
- `cancel` — 取消，不做任何事

解析後，**顯示確認清單**：

```
即將刪除以下 3 個 sessions：
  #1  2026-04-21  整理終端設定並建立 dotfiles GitHub repo
  #3  2026-04-19  除錯 FastAPI 登入認證問題
  #5  2026-04-18  (無法辨識內容)

確認刪除？(yes/no)
```

---

## Step 5：執行刪除

使用者確認後：

```bash
rm -f <session.file>
rm -rf <session.dir>   # 若同名資料夾存在才執行
```

每刪一個輸出一行確認。全部刪完後：

```
✓ 已刪除 3 個 sessions，釋放約 XX KB 空間。
```

---

## 注意事項

- **永遠不要在沒有確認的情況下刪除**
- 目前正在進行的 session（即這個對話）不在清單裡，不會被刪到
- 如果使用者輸入 `cancel` 或確認時回答 `no`，直接結束，不做任何刪除
