---
name: mac-cleanup
description: 清理 macOS 上卸載後殘留的垃圾檔案。當使用者說「幫我清理」、「清除殘留」、「移除垃圾」、「卸載後還有東西」、「clean up」、「remove leftovers」、「清理廢物」、「有沒有殘留」，或是剛用 brew uninstall / 手動刪除 .app 時，立即啟用這個 skill。也適用於使用者說「我的 Mac 很慢，幫我清一下」這類模糊請求。
---

# Mac Cleanup Skill

目標：找出並安全地刪除 macOS 上多餘的殘留檔案，讓使用者清楚知道每個步驟。

---

## 流程概覽

```
確認目標 → 掃描殘留 → 顯示結果 → 等使用者確認 → 刪除 → 驗證
```

永遠不要跳過「等使用者確認」這步。

---

## Step 1：確認清理目標

分兩種情況：

**A. 指定 app 名稱**（例如「清理 iTerm2 的殘留」）
→ 直接進入 Step 2，針對該 app 掃描。

**B. 沒有指定**（例如「幫我清理一下」）
→ 詢問使用者：「要清理特定 app 的殘留，還是掃描常見垃圾？」
→ 選項：
  1. 特定 app（請告訴我 app 名稱）
  2. 一般掃描（Homebrew 快取、損毀的偏好設定、孤立的容器等）

---

## Step 2：掃描殘留

### 針對特定 app

用 app 名稱（大小寫不敏感）在以下位置搜尋，同時平行執行：

```bash
# 以 iTerm2 為例，APP_NAME=iterm2 或 iTerm2 或 iTerm
find ~/Library/Application\ Support -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Preferences -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Caches -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/HTTPStorages -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Logs -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Saved\ Application\ State -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Containers -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Group\ Containers -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
# Homebrew Cask 下載快取
find ~/Library/Caches/Homebrew -iname "*APP_NAME*" 2>/dev/null
find ~/Library/Caches/Homebrew/downloads -iname "*APP_NAME*" 2>/dev/null
# Homebrew Caskroom（安裝目錄）
find /opt/homebrew/Caskroom -maxdepth 1 -iname "*APP_NAME*" 2>/dev/null
```

對每個找到的路徑，用 `du -sh` 取得大小。

### 一般掃描

```bash
# Homebrew 快取（可用 brew cleanup 清）
du -sh ~/Library/Caches/Homebrew 2>/dev/null
# 損毀的偏好設定（macOS 無法讀取的 plist）
# 大型 Log 檔
du -sh ~/Library/Logs 2>/dev/null
# 孤立的 Saved Application State
ls ~/Library/Saved\ Application\ State 2>/dev/null
```

---

## Step 3：顯示結果

用清楚的格式列出所有找到的東西：

```
找到以下殘留：

  ~/Library/Application Support/iTerm2/    (2.3 MB)
  ~/Library/Preferences/com.googlecode.iterm2.plist    (48 KB)
  ~/Library/Caches/com.googlecode.iterm2/    (1.1 MB)
  ~/Library/HTTPStorages/com.googlecode.iterm2/    (8 KB)
  ~/Library/Caches/Homebrew/Cask/iTerm2-3_6_9.zip    (9.4 MB)

總計：~12.9 MB

要全部刪除嗎？（可以指定保留某幾個）
```

如果什麼都沒找到，直接告知「沒有找到殘留，系統很乾淨。」

### 例外：不要刪的東西

就算名稱匹配，這些**絕對不能刪**：
- 其他 app 快取目錄（例如 Cursor 裡面的 `iTermHelper.scpt` 不是 iTerm2 殘留）
- `/opt/homebrew/Library/` 下的東西
- 還在運行中的 app 相關檔案（先確認 app 是否還存在 `/Applications/`）

---

## Step 4：執行刪除

只在使用者確認後執行。

```bash
# 逐一刪除，用 rm -rf 針對目錄，rm -f 針對單一檔案
rm -rf "路徑"
rm -f "路徑"

# 如果有 Homebrew 快取，用官方指令
brew cleanup
```

刪完後驗證每個路徑是否確實消失：

```bash
ls "路徑" 2>/dev/null && echo "still exists" || echo "deleted"
```

---

## Step 5：回報結果

簡短告知哪些刪了、釋放了多少空間。若 `brew cleanup` 有警告（例如 `Operation not permitted`）但不影響結果，直接說明是無關的 Homebrew 內部問題。

---

## 注意事項

- **永遠先看，再刪**：不要在沒顯示結果就直接執行刪除。
- **不確定的東西**：若某個路徑不確定是否屬於目標 app，標記出來讓使用者決定。
- **Brew cleanup 的警告**：`brew cleanup` 的 `Warning: Skipping X` 是版本不符的正常警告，不是錯誤，不用特別解釋。
