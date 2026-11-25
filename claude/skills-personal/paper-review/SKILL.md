---
name: paper-review
description: >
  有系統地讀論文並整理成 Obsidian 筆記，存到 ~/paper-review。支援兩種模式：快速版
  （摘要/方法/結果，用於大量掃論文找重點）與深讀版（額外做批判分析：可攻擊點/延伸方向，
  並自動對照使用者的碩論進度筆記找出與現有研究方向的具體關聯）。輸入可以是 arXiv/期刊連結
  、本地 PDF 檔案，或 Zotero 庫裡的條目（用標題、關鍵字或 item key 指定）。觸發時機：使用者說
  「幫我整理這篇論文」「讀一下這篇 paper」「這篇論文在講什麼」「幫我深讀這篇」「這篇跟我的碩論
  有沒有關係」「讀 Zotero 裡的 XXX」，或貼上論文連結/PDF 路徑/Zotero key 要求摘要、重點整理、
  批判分析時，即使沒有明講「論文」兩個字（例如只丟一個 arXiv 連結加一句「這在講什麼」）也適用。
---

# 論文整理

## 第一步：確認模式

- 使用者明講模式就照做；沒講的話用這個規則猜，猜完告訴使用者猜的是哪個模式（一句話，不用問）：
  - 提到「碩論」「攻擊點」「漏洞」「延伸」「深讀」「精讀」→ **深讀版**
  - 只要「摘要」「重點」「這在講什麼」「掃過」→ **快速版**
  - 真的猜不出來才問使用者
- 使用者事後要求「幫我把這篇也深讀」：直接在原本的筆記檔案上補深讀版的章節，不要重開一份新檔案。

## 第二步：取得論文全文

- **arXiv/期刊連結**：用 WebFetch 抓取。arXiv 先抓 abstract page 拿到標題/作者/年份，再抓 PDF 或 HTML 全文版本讀取內容。
- **Zotero 條目**（使用者給標題/關鍵字/item key，或說「Zotero 裡的 XXX」）：
  1. 用 `zotero_search_items` 找到條目；多筆符合時列出來讓使用者選，不要自己猜。
  2. 用 `zotero_get_item_metadata` 取作者、年份、會議/期刊、DOI，這些直接用在筆記 frontmatter，不要再上網重查——使用者已在 Zotero 整理過正式出處，以 Zotero 為準。
  3. 用 `zotero_get_item_children` 找 PDF 附件的 key，讀 `~/Zotero/storage/<附件key>/` 底下的 PDF（照下面「本地 PDF」的規則讀全文）。
  4. 本機沒有 PDF（沒同步檔案或沒附件）時依序退回：`zotero_get_item_fulltext` → 用條目 `extra` 欄的 arXiv 編號或 DOI 走上面的連結流程。
  5. 記下 item key，第三、五步會用到。
- **本地 PDF**：用 Read tool 讀取；超過 20 頁時用 `pages` 參數分段讀完整本，不要只讀前 20 頁就當作讀完。
- **深讀版一律要讀全文**，不能只看摘要或搜尋引擎的片段拼湊——這是使用者碩論教授明確要求的做法（見下方「與研究的關聯」）,快速版可以視情況只讀摘要+結論。

## 第三步：套用筆記格式

在寫筆記前先用 Skill 工具呼叫 `note-taking` skill 取得完整的 Obsidian 格式規範（frontmatter、Callouts、Wikilinks、視覺化規則），本 skill 不重複定義這些，只在它的 `paper-review` 範本上疊加下面的模式差異。

論文在 Zotero 裡有條目時（不論輸入來源；連結/PDF 輸入就用標題搜一下 Zotero），frontmatter 加一行 `zotero: "zotero://select/library/items/<item key>"`，讓使用者從 Obsidian 一鍵跳回 Zotero。

### 快速版

套用 note-taking skill 的 `paper-review` 範本原樣：背景脈絡、核心貢獻、具體例子、侷限性、在本研究中的用途。`output: reference`。不做批判分析，讀完摘要/方法/結果就能寫完，目的是讓使用者一眼掃過大量論文。

### 深讀版

在快速版的基礎上多做兩件事，`output: paper`：

1. **可攻擊點/延伸方向**（`> [!danger]`）——找論文自己承認的限制、隱含假設、實驗設計的漏洞，具體回答「如果要挑戰這篇論文的方法、或延伸出新研究，縫隙在哪裡」。不是把侷限性再抄一遍，而是想清楚「這個限制可以怎麼被利用/延伸成研究貢獻」。

2. **與研究的關聯**（擴充 `> [!tip]`，自動對照）——讀取 `~/.claude/projects/-Users-wayneho/memory/project_llm_redteam_thesis.md`，把這篇論文對照到裡面現有的機制清單與盲區，具體寫出：這篇論文屬於哪個機制/作用階段、跟哪個盲區有沒有關係、能不能填補教授要求的「延伸點」。那份筆記內容會隨時間更動，以筆記裡當下寫的方向為準，不要用你記憶中的舊版本內容去對照。若那份筆記不存在或找不到明確關聯，老實說「目前看不出具體關聯」，不要硬掰。

## 第四步：存檔

- 位置：`~/paper-review/`，資料夾不存在就先建立。
- 檔名：`YYYY-MM-DD-論文標題縮寫.md`。標題縮寫規則：取論文標題轉成 kebab-case（全小寫、空格換成連字號、去掉冒號後的副標題與標點），過長時取前面能表意的幾個字，長度抓 3-6 個字左右（例如《Sealing the Audit-Runtime Gap for LLM Skills》→ `2026-08-03-sealing-audit-runtime-gap.md`；《VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills》→ `2026-08-03-vigil-runtime-enforcement.md`）。

## 第五步：寫回 Zotero（有 item key 時）

1. `zotero_create_note` 在該條目下建一則短 note：1–2 句重點 + 筆記完整路徑（`~/paper-review/<檔名>.md`）。已有本 skill 建的 note 時（例如快速版升級成深讀版）用 `zotero_update_note` 更新，不要再建一則。
2. 加標籤 `read/quick` 或 `read/deep`（深讀取代快速，不要兩個並存）。加標籤時保留原有標籤，只新增/替換這一個：用 `zotero_update_item` 寫入完整清單，例如 `{"tags": [{"tag": "cs.CR"}, {"tag": "read/deep"}]}`（原有標籤從第二步的 metadata 拿）。不要用 `zotero_batch_update_tags`——實測它回報成功卻沒寫入。寫完用 `zotero_get_item_metadata` 確認標籤真的在（不要用搜尋確認——搜尋索引有延遲，剛寫的標籤常常還搜不到；metadata 偶爾也會慢幾秒，第一次沒看到就再讀一次，兩次都沒有才重寫）。建 note 時 `note_text` 開頭放 `<h1>標題</h1>`，否則 Zotero 會顯示成 Untitled。
3. 論文不在 Zotero 裡時不要自動匯入，回報時問一句「要加進 Zotero 嗎？」。

## 第六步：回報

- 回報存檔路徑（有寫回 Zotero 就補一句「已在 Zotero 加 note 與 `read/*` 標籤」），並用 1-2 句話講這篇論文的重點（深讀版再加一句跟碩論的關係）。不要把整篇筆記內容貼在對話裡——使用者會自己開 Obsidian 或 Markdown 編輯器看。

## 多篇論文

使用者一次丟多篇（例如一串 arXiv 連結）時，每篇各自獨立存成一個檔案，全部存完後給一個簡短總表（篇名＋一句話重點，深讀版可加相關度），不要把多篇論文擠進同一個檔案。
