# Claude Code 排障筆記

## claude-hud 設定問題（2026-05-23）

### 環境背景

| 項目 | 說明 |
|------|------|
| 啟動方式 | 從 WSL 終端執行 `claude` |
| 實際執行檔 | Windows 的 `claude.exe`（npm wrapper script 呼叫） |
| StatusLine shell | Git Bash（**非** WSL bash） |
| `$HOME` in statusLine | `/c/Users/Wayne`（Windows home） |
| plugin 路徑 | `/c/Users/Wayne/.claude/plugins/cache/...` |

### 問題一：WSL settings.json 有殘留測試指令

`~/.claude/settings.json`（WSL 路徑）裡有舊的測試指令蓋掉了正確設定：

```json
"statusLine": {
  "type": "command",
  "command": "while true; do echo HUD_ALIVE; sleep 2; done"
}
```

**修法**：直接更新該檔案為正確指令。

### 問題二：`stty size </dev/tty` 在 Git Bash 子行程失敗

claude-hud setup skill 生成的 Linux 指令範本使用了：

```bash
cols=$(stty size </dev/tty 2>/dev/null | awk '{print $2}')
```

這個指令在 Git Bash 子行程（無 TTY）中會靜默中斷整個指令，導致 HUD 完全不啟動。

**修法**：改用 `${COLUMNS:-116}` fallback，完全跳過 `stty`。

### 正確的 statusLine 指令

寫入 `~/.claude/settings.json`（即 `\\wsl.localhost\Ubuntu\home\wayne\.claude\settings.json`）：

```json
"statusLine": {
  "type": "command",
  "command": "export COLUMNS=${COLUMNS:-116}; plugin_dir=$(ls -d \"${CLAUDE_CONFIG_DIR:-$HOME/.claude}\"/plugins/cache/*/claude-hud/*/ 2>/dev/null | sort -V | tail -1); exec \"$(command -v node)\" \"${plugin_dir}dist/index.js\""
}
```

### 診斷指令

想確認 statusLine 的 shell 環境，可以暫時設：

```json
"command": "echo \"SHELL:$0 HOME:$HOME NODE:$(command -v node 2>/dev/null)\""
```

重啟後會在 HUD 位置顯示環境資訊。

### 關鍵認知

從 WSL 終端執行 `claude` 時，`claude` script 呼叫的是 Windows `claude.exe`。
Windows process 產生 statusLine 子行程時使用的是 **Git Bash**，而非 WSL bash。
因此 statusLine 指令必須在 Git Bash 環境下能正常執行。
