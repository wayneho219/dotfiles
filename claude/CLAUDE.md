# Claude Code — Global Rules

## Git

進行 git 相關操作（commit、branch、push、PR）時，使用 `git-workflow` skill 作為操作規範。與 git 無關的任務不要載入該 skill。

## Frontend
處理前端相關任務（新增或修改頁面、元件、樣式）時，使用 `frontend-design` skill 作為設計指引。與前端無關的任務（後端邏輯、資料處理、CLI 等）不要載入該 skill，以避免不必要的 context 消耗。

## Notes
撰寫筆記（「幫我做筆記」「整理成筆記」「記錄這個」「write notes」）時，使用 `note-taking` skill 作為格式規範。

## Language
- 與使用者溝通、撰寫計畫文件，一律用繁體中文。

## Boundaries
- 密鑰只能放環境變數或 `.env`，不要 inline 寫進程式碼或設定檔。

@RTK.md
