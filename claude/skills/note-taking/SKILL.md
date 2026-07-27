---
name: note-taking
description: >
  撰寫筆記時的格式與內容規範。涵蓋 Obsidian 內建功能整合（Frontmatter、Callouts、Wikilinks）、
  視覺化優先順序、Mermaid 相容性限制、內容深度要求。
  觸發時機：使用者說「幫我做筆記」「整理成筆記」「記錄這個」「write notes」「summarize into notes」。
---

# 筆記撰寫規範

## 一、每份筆記的固定結構

### 1. Frontmatter（必填）

每份筆記開頭一律加 YAML frontmatter：

```yaml
---
date: YYYY-MM-DD
type: paper-review | tech-note | concept | course
tags: [主題tag, 子題tag]
output: paper | study | reference
status: draft | complete
---
```

- `type`：論文筆記用 `paper-review`、技術學習用 `tech-note`、概念解釋用 `concept`、課堂筆記用 `course`
- `output`：寫論文用 `paper`、考試複習用 `study`、快速查閱用 `reference`
- `output` 決定筆記的詳細程度與重點（見下方「輸出導向」）

### 2. TL;DR（必填）

Frontmatter 之後立刻放 1-2 句 callout 總結，讓讀者快速判斷要不要深讀：

```markdown
> [!abstract] TL;DR
> 這份筆記在說什麼，以及為什麼重要。一到兩句話。
```

### 3. 內文結構

每個概念依序涵蓋：
1. **背景脈絡** — 為什麼這個東西會存在？它解決了什麼前一個方法沒解決的問題？
2. **定義 / 核心貢獻** — 是什麼
3. **具體例子** — 最少一個，優先用真實場景

後面章節會涵蓋的內容，不在此展開，留一行 `→ 詳見 [[概念名稱]]`。

---

## 二、Obsidian 內建功能使用規範

### Callouts（視覺強調）

用 Obsidian 內建 callout 取代普通 blockquote，提高視覺層次：

| Callout | 用途 |
|---|---|
| `> [!abstract]` | TL;DR、摘要 |
| `> [!important]` | 核心貢獻、關鍵發現 |
| `> [!note]` | 背景脈絡、補充說明 |
| `> [!example]` | 具體例子 |
| `> [!warning]` | 限制、陷阱、注意事項 |
| `> [!tip]` | 實用技巧、在本研究的用途 |

範例：
```markdown
> [!important] 核心貢獻
> 定義了 Indirect Prompt Injection：攻擊者透過 LLM 讀取的外部資料注入惡意指令。

> [!warning] 侷限性
> 僅測試 GPT-3，未涵蓋間接注入場景。
```

### Wikilinks（跨筆記連結）

- 提到其他筆記中的概念時，一律用 `[[概念名稱]]` 而非純文字
- 後面章節會詳細說明的內容：`→ 詳見 [[概念名稱]]`
- 相關論文：`→ 參照 [[P2-Greshake-2023]]`
- Obsidian 的 Backlinks 面板和 Graph view 會自動追蹤這些連結

### Tags

- Frontmatter 的 `tags` 用於分類，格式：`[主題, 子題]`
- 範例：`tags: [prompt-injection, agent-security, benchmark]`
- 標籤盡量沿用已有的，不要每次都發明新標籤（保持搜尋一致性）

---

## 三、輸出導向（依 output 欄位調整重點）

| output | 重點調整 |
|---|---|
| `paper` | 強調論文的引用定位、與本研究的結構關係、引用建議位置（論文第幾節） |
| `study` | 強調例子和比較表，每節末尾附 1-3 個複習問題 |
| `reference` | 強調結構清晰、表格化、快速可查；背景脈絡可縮短 |

`study` 模式的複習問題範例：
```markdown
> [!tip] 複習問題
> 1. IPI 和直接 Prompt Injection 的差別是什麼？
> 2. 為什麼 LLM 整合應用天然容易受 IPI 影響？
```

---

## 四、視覺化規範

### 優先順序

```
ASCII（內容可完整用簡單英文表達）> Mermaid 圖 > Markdown 表格 > 純文字清單
```

判斷 ASCII 是否適合：
- **圖框內**的標籤、內容可以用簡單英文表達（圖外的標題、說明可以是中文）
- ASCII 本身的視覺結構（方框、箭頭、線條）比 Mermaid flowchart 更直觀呈現該概念
- 否則用 Mermaid

### Mermaid 使用限制（Obsidian 相容性）

**可用：**
- `flowchart TD` / `flowchart LR`
- `flowchart` subgraph（避免過寬時改用 TD）

**禁用（Obsidian Mermaid 版本不支援 / 中文相容性差）：**
- `timeline` — Obsidian 版本過舊，不支援
- `mindmap` — 中文節點解析失敗
- `quadrantChart` — 中文標籤解析失敗

**節點換行：**
- node label 內換行一律用 `<br/>`，**不可用 `\n`**
- `\n` 在 Obsidian 的 Mermaid 渲染器中顯示為字面文字，不會換行
- 範例：`L1["Layer 1<br/>P1 Perez 2022"]`

**方向選擇：**
- 節點多、內容長的流程圖（如時間軸、多層架構）一律用 `flowchart TD`
- `flowchart LR` 只用在節點少且寬度可控的情況（如 2–3 個節點的步驟圖）
- 判斷標準：預覽時若圖寬超出螢幕或需要橫向捲動，改用 `TD`

**樣式規則：**
- 不加自訂 `fill` 顏色（dark theme 下對比度會出問題）
- 讓 Mermaid 使用預設主題配色

### ASCII 圖

- 圖框內標籤可用英文表達時，**優先選用**（比 Mermaid 更輕量、更直觀）
- **中文只允許出現在以下兩種位置**：
  1. 框右邊界 `│` 之後的同行說明：`│ content │  ← 中文說明`
  2. 完全不參與框線結構的獨立行（標題行、段落說明），例如 `flash.h（公開介面）:` 單獨一行
- **其餘位置一律英文**：框內內容、兩框之間的間隔、任何會影響後續欄位對齊的位置
- 原因：中文字寬 = 2 格，英文 = 1 格，混入框結構會讓邊框對不齊

**框間標籤的間距規則：**
- 兩框之間放文字標籤時，間距 = 標籤長度 + 左右各 1 空格（`API` 3字元 → 間距 5）
- 確定間距後，該圖**所有行的框間距必須統一**（含 `┌─┐` 行與箭頭行）

**暫存器 bit 標籤行規則（4-char slot）：**
- 2位數 pair（如 `31 30`）：格式 `XX YY`（5 chars），可略微溢出到相鄰 ┬ 位置
- 1位數 pair（如 `9 8`）：格式 `X  Y`（4 chars，兩空格），恰好填滿 slot interior
- 2位數→1位數的過渡（如 `10` 後接 `9`）：中間保留 1 空格（┬ 位置天然分隔），不會造成 `109` 視覺混淆
- 範例：`... 11 10 9  8 7  6 5  4 3  2 1  0`（`10` 在 slot 右半，`9` 在下一 slot 起點）

**對齊問題排查（修改前必做）：**
- 先數每行字元寬度，找出與 `┌─...─┐` 長度不一致的行
- 只改那一行，不要整張圖重寫或大範圍刪中文

---

## 五、筆記類型快速參照

### paper-review（論文筆記）

```markdown
---
date: ...
type: paper-review
tags: [...]
output: paper
status: draft
---

> [!abstract] TL;DR
> 一句話說這篇論文是什麼、為什麼重要。

| 欄位 | 內容 |
|---|---|
| 作者 | |
| 年份 / 會議 | |
| arXiv | |
| 相關度 | ★★★★☆ |

**背景脈絡**（前一個研究沒解決什麼）

**核心貢獻**

> [!example] 具體例子

> [!warning] 侷限性

> [!tip] 在本研究中的用途（引用位置建議）
```

### tech-note（技術學習）

```markdown
---
date: ...
type: tech-note
tags: [...]
output: study
status: draft
---

> [!abstract] TL;DR
> 這個技術是什麼、解決什麼問題。

**為什麼需要它**（背景）

**怎麼運作**

> [!example] 範例

> [!warning] 常見陷阱

> [!tip] 複習問題
```
