# dotfiles

Wayne 的終端設定檔備份。

## 檔案對照表

| 檔案 | 複製到 |
|---|---|
| `zsh/.zshrc` | `~/.zshrc` |
| `zsh/.zprofile` | `~/.zprofile` |
| `zsh/.bashrc` | `~/.bashrc` |
| `zsh/.p10k.zsh` | `~/.p10k.zsh` |
| `tmux/.tmux.conf.local` | `~/.tmux.conf.local` |
| `git/.gitconfig` | `~/.gitconfig` |
| `git/ignore` | `~/.config/git/ignore` |
| `ghostty/config` | `~/.config/ghostty/config` |
| `claude/CLAUDE.md` | `~/.claude/CLAUDE.md` |
| `claude/settings.json` | `~/.claude/settings.json`（合併，勿直接覆蓋） |
| `claude/commands/` | `~/.claude/commands/` |
| `claude/skills/` | `~/.claude/plugins/cache/user-skills/user-skills/1.0.0/skills/` |
| `claude/plugins/claude-hud/config.json` | `~/.claude/plugins/claude-hud/config.json` |
| `claude/TROUBLESHOOTING.md` | 參考文件，無需複製 |

## 新電腦設定步驟

### 1. 安裝必要工具

```bash
# Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 工具
brew install fzf eza tmux lazygit sshpass node

# RTK（Token-optimized CLI proxy for Claude Code）
brew install rtk                          # macOS
# Linux：
# curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
# echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc

# Nerd Font（Powerlevel10k 和 eza 圖示必要）
brew install --cask font-jetbrains-mono-nerd-font
# 安裝後到 Ghostty 設定中指定字型：font-family = "JetBrainsMono Nerd Font"

# oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# zsh plugins
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# oh-my-tmux
git clone https://github.com/gpakosz/.tmux.git ~/.tmux
ln -s ~/.tmux/.tmux.conf ~/.tmux.conf

# Ghostty（從官網下載 .dmg 安裝）
# https://ghostty.org
```

### 2. 複製設定檔

```bash
git clone https://github.com/wayneho219/dotfiles.git ~/dotfiles
mkdir -p ~/.config/git ~/.config/ghostty ~/.claude/commands

cp ~/dotfiles/zsh/.zshrc ~/.zshrc
cp ~/dotfiles/zsh/.zprofile ~/.zprofile
cp ~/dotfiles/zsh/.bashrc ~/.bashrc
cp ~/dotfiles/zsh/.p10k.zsh ~/.p10k.zsh
cp ~/dotfiles/tmux/.tmux.conf.local ~/.tmux.conf.local
cp ~/dotfiles/git/.gitconfig ~/.gitconfig
git config --global user.email "your@email.com"  # 填入自己的 email（repo 內不存放）
cp ~/dotfiles/git/ignore ~/.config/git/ignore
cp ~/dotfiles/ghostty/config ~/.config/ghostty/config
cp ~/dotfiles/claude/CLAUDE.md ~/.claude/CLAUDE.md
cp ~/dotfiles/claude/commands/* ~/.claude/commands/
mkdir -p ~/.claude/plugins/claude-hud
cp ~/dotfiles/claude/plugins/claude-hud/config.json ~/.claude/plugins/claude-hud/config.json
```

### 3. 設定 Claude Code

```bash
# 安裝 Claude Code
npm install -g @anthropic-ai/claude-code

# 安裝 plugins（公開 marketplace）
claude plugins install superpowers
claude plugins install skill-creator
claude plugins install frontend-design
claude plugins install pyright-lsp
claude plugins install claude-md-management
claude plugins install clangd-lsp

# 安裝 ponytail（自訂 marketplace，GitHub: DietrichGebert/ponytail）
# 先在 Claude Code 裡執行 /update-config 加入 ponytail marketplace，再安裝

# 安裝 claude-hud（自訂 marketplace，GitHub: jarrodwatts/claude-hud）
# 先在 Claude Code 裡執行 /update-config 加入 claude-hud marketplace，再安裝

# 安裝 user-skills（本機目錄 plugin）
# 把 claude/skills/ 複製到目標路徑後，在 Claude Code 設定中指向該目錄
mkdir -p ~/.claude/plugins/cache/user-skills/user-skills/1.0.0
cp -r ~/dotfiles/claude/skills ~/.claude/plugins/cache/user-skills/user-skills/1.0.0/

# settings.json：手動將 enabledPlugins / extraKnownMarketplaces / statusLine / hooks 合併進去
# 不要直接覆蓋，會清掉 Claude Code 自動管理的欄位
# hooks 欄位包含 RTK PreToolUse hook，合併時一併帶入
```

### 4. 設定 SSH

自行建立 `~/.ssh/config`（不放在此 repo）。

---

> 更新設定後，把修改過的檔案重新複製回 `~/dotfiles` 對應資料夾再 push。
