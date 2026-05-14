---
name: frontend-app-clone
description: Clone any web or mobile app UI from screenshots into a complete, runnable frontend project. Use this skill whenever the user provides a folder of app screenshots and wants to replicate the interface — even if they say "復刻介面", "根據截圖做前端", "仿照這個 App", "clone this UI", "copy this app's design", "幫我照這個截圖做出來", or simply hands you a directory of images and asks you to build a frontend. Also trigger when the user wants to recreate an existing app's look and feel without access to the source code. Works with both desktop web screenshots and mobile app screenshots.
---

# Frontend App Clone

從截圖資料夾分析現有應用程式的 UI，推薦最適合的技術框架，並產生完整可運行的純前端專案。

## 流程概覽

1. **分析截圖** — 讀取所有截圖，辨識頁面結構、設計系統、UI 元件模式
2. **框架選型** — 依複雜度與類型建議技術棧，向使用者說明並確認
3. **產生完整專案** — 設計 token、共用元件、頁面、路由、Mock 資料

---

## Step 1：分析截圖

讀取使用者提供目錄中的所有圖片（支援 PNG、JPG、WEBP）。

對每張截圖記錄以下資訊：

**版面類型判斷**
- 桌面版：寬版版面、側邊導覽列、多欄佈局
- 手機版：單欄、底部 Tab Bar、緊湊元素、大圓角按鈕

**設計系統提取**
- 主色、輔色、背景色（盡量精確，例如 `#00703C`）
- 字體風格（有襯線 / 無襯線 / 等寬，粗細感）
- 圓角程度（無圓角 / 小圓角 4px / 大圓角 12px+）
- 間距密度（緊密 / 標準 / 寬鬆）
- 陰影風格（扁平 / 輕微陰影 / 明顯立體）

**頁面識別**
- 為每張截圖命名，描述其用途（例：`首頁 / 個股詳情 / 登入 / 設定`）
- 標注哪些是主流程頁面、哪些是次要頁面

**重複出現的 UI 元件**
- 在多張截圖中出現的元件列表（卡片、表格、圖表、徽章、頂部導覽、底部導覽等）

分析完成後，輸出整理摘要給使用者確認，再進入下一步。

---

## Step 2：框架選型

依以下決策樹推薦技術棧，並向使用者說明理由後確認：

| 情境 | 建議技術棧 |
|------|-----------|
| 手機 App 截圖（單欄、底部導覽） | React + Vite + Tailwind CSS（Mobile-first 響應式） |
| 1–3 頁的靜態展示 | 純 HTML + CSS + Vanilla JS |
| 3–8 頁、含資料表格或圖表 | React + Vite + Tailwind + shadcn/ui |
| 後台 Dashboard / 管理系統 | React + Vite + Tailwind + shadcn/ui |
| 10 頁以上、多路由、SEO 需求 | Next.js App Router + Tailwind + shadcn/ui |
| 行銷官網 / 靜態內容為主 | Astro + Tailwind |

向使用者說明：
1. 選此框架的理由
2. 預計的目錄結構草圖
3. 需安裝的主要套件

**等使用者確認後，才進入 Step 3。**

---

## Step 3：產生完整專案

> **逐頁完成原則：每次只實作一個頁面，完成後向使用者回報，等確認後再繼續下一頁。**
>
> 回報格式（每頁完成後輸出）：
> - ✅ 已完成：`{頁面名稱}`（對應截圖：`{檔名}`）
> - 建立的檔案清單
> - 視覺還原說明（哪些細節有還原、哪些用了替代方案）
> - 詢問：「是否繼續下一頁：`{下一頁名稱}`？」
>
> 只有在使用者確認後，才開始下一個頁面。

### 3-1 初始化專案

執行對應的 scaffold 指令。以 React + Vite 為例：

```bash
npm create vite@latest <project-name> -- --template react-ts
cd <project-name>
npm install
npm install -D tailwindcss @tailwindcss/vite
npm install lucide-react clsx tailwind-merge
# 若需 shadcn/ui：
npx shadcn@latest init
```

### 3-2 設計 Token 設定

將 Step 1 提取的設計系統寫入設定檔：

**tailwind.config.ts 範例：**
```ts
theme: {
  extend: {
    colors: {
      primary: '#00703C',
      'primary-light': '#E8F5EE',
      'primary-border': '#E0EDE6',
      surface: '#FFFFFF',
      background: '#FAFBFA',
      'text-primary': '#1A1A1A',
      'text-secondary': '#888888',
      up: '#00703C',
      down: '#D32F2F',
    },
    fontFamily: {
      sans: ['Noto Sans TC', 'Microsoft JhengHei', 'sans-serif'],
    },
    borderRadius: {
      card: '4px',
    },
  },
}
```

若使用 CSS Variables，寫入 `src/styles/tokens.css`。

### 3-3 共用元件

在 `src/components/` 下，為截圖中重複出現的 UI 元件各建一個檔案：

| 截圖中出現 | 建立的元件 |
|----------|-----------|
| 頂部導覽列 | `Navbar.tsx` |
| 側邊選單 | `Sidebar.tsx` |
| 底部 Tab（手機） | `BottomNav.tsx` |
| 資料卡片 | `Card.tsx` |
| 數字摘要卡 | `KpiCard.tsx` |
| 資料表格 | `DataTable.tsx` |
| 圖表容器 | `ChartCard.tsx` |
| 按鈕、徽章 | `Button.tsx`、`Badge.tsx` |

每個元件規格：
- 使用 TypeScript interface 定義 props
- 使用設計 token（Tailwind class 或 CSS variable）
- 手機版元件需包含觸控友善的尺寸（`min-h-[44px]`）

### 3-4 頁面元件（逐頁實作，每頁完成後等確認）

依截圖順序，一次只實作一個頁面：

1. 在 `src/pages/` 建立該頁面的元件檔案（命名對應截圖，例：`MarketPage.tsx`）
2. 使用共用元件組合，還原截圖的版面結構
3. 動態區域使用 Mock 資料（來自 Step 3-5）
4. 圖片佔位使用 `https://placehold.co/{W}x{H}/{bg}/{text}?text={label}`
5. 截圖中無法判斷的細節，依常見 UX 模式補全

**頁面完成後立即回報**（見 Step 3 開頭的回報格式），等使用者確認再繼續下一頁。

### 3-5 Mock 資料層

建立 `src/data/mock.ts`，提供每個頁面所需的假資料：

```ts
// 同時定義 TypeScript interface
export interface StockItem {
  id: string
  name: string
  changePercent: number
  articleCount: number
}

export const mockStocks: StockItem[] = [
  { id: '2330', name: '台積電', changePercent: 2.5, articleCount: 42 },
  { id: '2317', name: '鴻海', changePercent: -1.2, articleCount: 28 },
]
```

在需要替換成真實 API 的地方加上標記：
```ts
// TODO: replace with GET /api/stocks
```

### 3-6 路由設定

依框架建立路由：

**React Router（react-router-dom）：**
```tsx
<Routes>
  <Route path="/" element={<HomePage />} />
  <Route path="/stocks/:id" element={<StockDetailPage />} />
</Routes>
```

**Next.js App Router：**
直接在 `app/` 下建立對應的 `page.tsx` 目錄結構。

### 3-7 收尾

- 更新入口檔案（`App.tsx` 或 `layout.tsx`）整合所有路由與全域樣式
- 確認 `npm run dev` 可正常啟動且無 TypeScript 錯誤
- 在 `README.md` 記錄：
  - 啟動方式（`npm install && npm run dev`）
  - 截圖 → 路由對應表
  - 後端整合說明（哪些 Mock 需換成 API、建議的 API 結構）

---

## 輸出品質標準

> **節奏提醒**：頁面數 = 回報次數，不可跳過確認環節一次做完所有頁面。

完成後自我檢查：

- [ ] `npm install && npm run dev` 不報錯、可在瀏覽器看到頁面
- [ ] 每張截圖都有對應的頁面路由
- [ ] 主色、背景色與截圖一致
- [ ] 重複 UI 元件已抽取為共用元件（不在多個頁面重複寫相同 JSX）
- [ ] 每個頁面都有 Mock 資料填充，不是空白頁
- [ ] TypeScript 無 `any`（除必要情況）
- [ ] 手機截圖的版面有 Mobile-first 響應式處理

---

## 常見限制與處理方式

| 限制 | 處理方式 |
|------|---------|
| 無法從截圖取得精確字體名稱 | 選外觀相近的 Google Fonts 替代，在程式碼加 `// TODO: confirm font` |
| 截圖中的 Logo / 圖示無法取出 | 用 `lucide-react` icon 或 `placehold.co` 替代，標記 TODO |
| 截圖無法顯示動畫與 hover 效果 | 依常見 UX 模式補全（hover 變色、按鈕 active、transition）|
| 顏色數值只能目測估算 | 選色後在程式碼標記 `// TODO: verify exact hex from design spec` |
| 表格資料欄位未知 | 依截圖中可見的欄標題設計 interface，其餘欄位留 TODO |
