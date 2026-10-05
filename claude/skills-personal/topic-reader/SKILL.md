---
name: topic-reader
description: Use when converting a whole topic folder of the stm32mp215f knowledge base (c-language/, arm-architecture/, trustzone/, yocto/, cryptography/, stm32mp2/, networking/ …) into a reading-version Artifact, or when the user says 「把 X 主題做成 artifact」「做閱讀版」「主題閱讀器」. Not for a single concept or flow — that is visual-explainer.
---

# Topic Reader：主題閱讀版 Artifact

讀者是**還沒讀完這些筆記、記不住專有名詞**的使用者。目標：讀完整個主題不必離開頁面查任何詞。

設計規格：`docs/superpowers/specs/2026-10-02-topic-reader-design.md`
全部主題是**同一個多頁 artifact**（網址記在專案記憶裡，或用 Artifact `action: "list"` 找標題「STM32MP215F 知識庫」）
- `artifacts/index.html`：首頁（學習路線＋名詞總表），是發布時的 `file_path`
- `artifacts/<slug>.html`：各主題頁，由建置腳本產生
- `artifacts/glossary.js`：唯一一份共用名詞庫，只增不重複定義
- 範本：`artifacts/boot-flow.html`（手寫、使用者已確認），CSS 與 `<script>` 引擎所有主題共用

## 流程

1. 讀完該資料夾所有 `.md`（含 README）。
2. 查證關鍵事實（位址、順序、編號、函式名）：TF-A／Linux／U-Boot 原始碼與官方文件 > ST wiki > 其他。wiki.st.com 常逾時，改查原始碼或 WebSearch 摘要。查不到標 `<span class="unv">未查證</span>`。
3. 規劃章節：沿用 `.md` 的 01、02…；最前面「導讀」、最後「速查」。
4. 寫內文到 `artifacts/src/<slug>-body.html`（只寫 `<article>` 們，不含 head 與 script），每章用 block 組成，依下表選形式。
   重複性高的 SVG（bit 格子、暫存器陣列）在 `scripts/topic_gens.py` 寫產生器，內文用 `%%NAME%%` 佔位。範本已有 `.cell`／`.cell.chg` 樣式。
   建置：`python3 scripts/build_topic.py <slug> "<頁面標題>"` → `artifacts/<slug>.html`。
5. 新名詞加進 `glossary.js`（JSON 格式，`d` 白話一句、`e` 具體例子、可選 `full`、`alias`）。
6. `python3 scripts/glossary_check.py artifacts/<topic>.html` 必須 OK（同時檢查內文縮寫、名詞庫解釋、圖上零件的 `data-term`）；再用 node 檢查 `<script>` 能 parse；有程式碼面板時印出行號，對一次 `data-lines`。
7. 在 `artifacts/index.html` 的 `TOPICS` 給該主題加上 `file`（卡片才會變成可點的「可閱讀」）。
8. 發布到同一個 URL：`file_path` = `artifacts/index.html`，`files` 列出 `glossary.js` 和每一個主題頁（新增的頁也要列）。有 `url` 時帶上；同一個 session 內直接用同一個 `file_path` 重發即可。
9. 回報連結、查證來源、未查證項目、「與筆記不同」清單。`.md` 不改，commit 交給使用者。

## 多頁 artifact 的限制

- 只有 `index.html` 會被套上 skeleton；其他 HTML 要自帶 `<!doctype html>`、charset、viewport、`[hidden]{display:none!important}` 與 body 樣式。範本已經有，用建置腳本產生就不用管。
- 頁面之間用相對連結（`href="index.html"`），範本的章節列左側已有「← 知識庫」。
- 頁面執行時不能讀別的 artifact 的檔案；共用的東西都要放在同一個 artifact 裡。

## 選 block 形式

判斷：**這段文字會不會反覆回頭參照同一個東西？** 會 → split block（左側固定）；不會 → plain block。

| 內容形狀 | 形式 | 標記 |
|---|---|---|
| 流程／順序 | split + SVG，零件逐段亮起 | `.beat[data-focus="零件id…" data-flows="f-…" data-labels="l-…"]` |
| 層級／結構 | split + 堆疊 SVG | 同上 |
| 程式碼 | split + `<pre class="code">` | `.beat[data-lines="3 4 5"]` |
| 比較 | plain + 表格 | — |
| 純概念 | plain 單欄 | — |

SVG 零件：`<g class="part" id="p-xxx" data-term="名詞庫主鍵">` 內含 `rect.body`；`data-term` 必須是 `glossary.js` 的鍵。

## 頁面規則

- 畫面簡潔：**不放「怎麼讀這一頁」之類的使用說明**、不放頁首大標，打開就是導讀內容。
- 每章結尾：`.quiz` 5 題左右 `<details class="q">`，再接 `.src` 來源列表。
- 筆記有錯：`<div class="fix"><b class="h">與筆記不同</b>…</div>`，寫清楚筆記怎麼寫、正確是什麼、依據哪個來源。
- 程式碼裡的 `<`、`>`、`&` 要寫成 entity。
- 名詞小卡是 stack（點小卡內的詞 push、「← 回到」與 Esc pop、點空白全關），範本已實作，不要改回單層。

## 常見錯誤

| 錯誤 | 結果 | 正確做法 |
|---|---|---|
| 會被插入名詞按鈕的元素用 grid／flex | 一句話被拆成好幾格（`summary` 曾經這樣壞掉） | 用 block + 絕對定位裝飾 |
| `glossary.js` 的 `d`／`e` 用了沒收錄的縮寫 | 用不懂的詞解釋不懂的詞 | 跑 glossary_check，它也檢查名詞庫自己 |
| 大寫識別字（暫存器欄位、巨集）寫在一般文字 | check 失敗或被誤當名詞 | 包進 `<code>`；數值欄用 `<td class="m">` |
| 照抄筆記的位址／編號 | 把筆記的錯誤搬進頁面 | 每個數字都對一次一手來源 |
