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

## 新電腦設定步驟

### 1. 安裝必要工具

```bash
# Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 工具
brew install fzf eza tmux lazygit sshpass

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
```

### 2. 複製設定檔

```bash
git clone https://github.com/wayneho219/dotfiles.git ~/dotfiles
mkdir -p ~/.config/git

cp ~/dotfiles/zsh/.zshrc ~/.zshrc
cp ~/dotfiles/zsh/.zprofile ~/.zprofile
cp ~/dotfiles/zsh/.bashrc ~/.bashrc
cp ~/dotfiles/zsh/.p10k.zsh ~/.p10k.zsh
cp ~/dotfiles/tmux/.tmux.conf.local ~/.tmux.conf.local
cp ~/dotfiles/git/.gitconfig ~/.gitconfig
cp ~/dotfiles/git/ignore ~/.config/git/ignore
```

### 3. 設定 SSH

自行建立 `~/.ssh/config`（不放在此 repo）。

---

> 更新設定後，把修改過的檔案重新複製回 `~/dotfiles` 對應資料夾再 push。
