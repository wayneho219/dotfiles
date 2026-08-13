# AI 語感病症清單

掃描完稿文件時比對此清單，命中就局部替換，不重寫整段。

## 中文

### 罐頭轉折/總結語
| 不要 | 替代 |
|---|---|
| 值得注意的是，X 會影響 Y | X 會影響 Y |
| 總的來說，這個方法... | 這個方法... |
| 綜上所述 | （直接刪掉，讓前文自己收尾） |
| 不難發現 | （直接刪掉，或改成具體的因果句） |
| 值得一提的是 | （直接刪掉） |

### 誇飾行銷詞彙
| 不要 | 替代 |
|---|---|
| 這個技術顛覆了整個產業 | 這個技術改變了 XX 的做法 |
| 幫助團隊賦能 | 讓團隊能夠自行 XX |
| 效能大幅提升 | 效能提升 3 倍（給具體數字） |
| 令人驚艷的結果 | （刪掉形容詞，直接給結果） |

### 制式排比句
| 不要 | 替代 |
|---|---|
| 這不僅是一個工具，更是一種方法論 | 這個工具改變了 XX 的做法（挑一個講清楚） |
| 這不只是 X，而是 Y | 直接講 Y，不用 X 陪襯 |
| 透過 A，藉此達成 B | A 帶來 B |
| 雖然 X 看似...，但實際上 Y | 直接講 Y，先讓步再反轉是同一招的隱藏版 |
| 乍看之下 X...，但 | 直接講重點，不用先立靶再打 |
| 大多數人認為 X，但其實 Y | 直接講 Y，除非「大多數人這樣想」本身是有根據的事實 |

### 空洞舖陳開場/結尾
| 不要 | 替代 |
|---|---|
| 在當今快速變化的時代 | （刪掉，直接進主題） |
| 本文旨在探討 X | 這篇在講 X（或直接開始講） |
| 總而言之 | （刪掉，讓結論句自己站住） |

### 過度條列化
| 不要 | 替代 |
|---|---|
| 用「首先、其次、最後」硬拆本可以一段講完的敘述 | 改成敘述文，用因果連接詞自然銜接 |
| 每個小節都刻意湊三點 | 該幾點就幾點，不硬湊 |

### 標點濫用
| 不要 | 替代 |
|---|---|
| 過度使用全形「——」補充說明 | 改用逗號、句號或括號 |
| 每個關鍵詞都加「」強調 | 只在真正需要強調時才加 |

### 讀者奉承語
| 不要 | 替代 |
|---|---|
| 這是個好問題 | （刪掉，直接回答） |
| 相信你會發現... | （刪掉） |

### 詞彙氾濫（單字層級）
公文/新聞稿語料訓練出來的高頻詞，出現一次沒問題，整篇重複出現才是病症。
| 不要 | 替代 |
|---|---|
| 賦能 | 讓...能夠 XX（講清楚實際做了什麼） |
| 抓手 | 具體做法、工具（直接講是什麼） |
| 閉環 | 完整流程（或直接刪，講結果） |
| 深耕 | 專注投入 XX（幾年、哪個領域，給具體範圍） |
| 打造 | 建立、做出（依語境挑一個具體動詞） |
| 蓬勃發展 | 快速成長（給具體數字或時間範圍） |
| 全面、高效、強大（同段重複堆疊） | 挑一個真正符合語境的形容詞，或直接換成數字 |

### 抽象名詞堆砌
| 不要 | 替代 |
|---|---|
| 自我的探索、認同感的建構、內在小孩的療癒 | 換成具體事件、對話、行動——誰、做了什麼、結果如何 |

### 模糊歸因
| 不要 | 替代 |
|---|---|
| 有人認為、研究顯示（不具名不附來源） | 講清楚是誰、哪份研究，找不到來源就直接刪掉這句 |

### 翻譯腔／公文贅詞
中文技術與學術文件常見的臃腫結構，本身不誇張也不空洞，但整篇堆疊就顯得生硬。
| 不要 | 替代 |
|---|---|
| 進行了 + N（進行了測試、進行了分析） | 直接用動詞：測試了、分析了 |
| 通過 + N（通過導入自動化流程） | 用「A 帶來 B」或直接講做了什麼 |
| 顯著（顯著提升、顯著影響） | 給具體數字或程度，或換成明顯、大幅 |
| 均、上述、能夠（同段重複出現） | 都、這些／以上、能——換成白話對應詞 |
| 這說明、從而、以提高 | 說明、（可刪）、用來 |

### 格式濫用
不是用詞問題，是排版留下的痕跡。
| 不要 | 替代 |
|---|---|
| 正式文件裡殘留 Markdown 語法（##、**）沒轉換 | 轉成該格式該有的標題/粗體樣式，不留原始符號 |
| 每個標題都套用英文式 Title Case | 依文件語言與場合的慣例大小寫 |
| 正式文件裡加 emoji | 刪掉，除非文件性質本來就輕鬆（如內部聊天記錄） |

## English

### Filler Transitions
| Avoid | Replace with |
|---|---|
| Furthermore, X affects Y | X affects Y |
| It's worth noting that X | X |
| In conclusion, ... | (cut — let the last point stand) |
| Overall, this approach... | This approach... |

### Marketing / Hype Words
| Avoid | Replace with |
|---|---|
| unlock the power of X | use X |
| leverage the platform | use the platform |
| a game-changing feature | a feature that does Y (name the actual effect) |
| seamless integration | integration that does Y (drop the adjective) |

### Rule-of-Three / False Parallelism
| Avoid | Replace with |
|---|---|
| It's not just X, it's Y | Y (drop the X setup) |
| A robust, scalable, and efficient solution | pick the one property that actually matters here |
| While X may seem..., it's actually Y | Y (the hedge-then-reframe is the same trick in a softer coat) |
| At first glance, X... | Cut the setup, state the point |
| Most people think X, but actually Y | Y — unless "most people think X" is itself a sourced claim |

### Bloated Verbs
| Avoid | Replace with |
|---|---|
| serves as, stands as, marks a, represents a | is |
| boasts a, features a, offers a | has, gives |
| plays a role in | affects, causes, shapes — name the actual relationship |
| aims to, seeks to | wants to, tries to, will (if the outcome is known) |

### Empty Framing
| Avoid | Replace with |
|---|---|
| In today's fast-paced world | (cut, start with the point) |
| This article aims to explore X | This is about X |

### Over-Bulleting
| Avoid | Replace with |
|---|---|
| Forcing flowing prose into a 3-point bullet list | Prose with natural connectives, unless the content is genuinely enumerable |

### Em Dash Overuse
| Avoid | Replace with |
|---|---|
| Repeated "—" as a crutch for every aside | Comma, period, or parentheses depending on the relationship |

### Sycophantic Openers
| Avoid | Replace with |
|---|---|
| Great question! | (cut, answer directly) |
| Absolutely, here's... | (cut) |

### Overused Single Words
Frequency of these words spiked sharply post-ChatGPT (e.g. "delve" usage up 654% in biomedical abstracts, 2020-2023, per Max Planck Institute research). One use is fine — the tell is repetition across a document.
| Avoid | Replace with |
|---|---|
| delve, boast, underscore, foster, harness, leverage, navigate | dig into, has, show, build, use, deal with — a plain verb |
| robust, pivotal, comprehensive, intricate, nuanced, vibrant | pick the one specific quality that's actually true here |
| tapestry, landscape, realm, journey (as metaphor) | name the actual thing instead of the metaphor |
| testament to | proof of, shows |

### False Range / Vague Attribution
| Avoid | Replace with |
|---|---|
| From [extreme A] to [extreme B] spanning an implausibly wide, loosely-connected set | Name the actual two things being compared, only if the span is real |
| Critics argue / Some believe (no named source) | Name the source, or cut the claim |

### Formatting Tells
Not a wording problem — leftover artifacts from generation.
| Avoid | Replace with |
|---|---|
| Leftover Markdown syntax (##, **) in prose meant to render as plain text | Convert to actual formatting, or plain text |
| Title Case on every heading regardless of house style | Follow the target document's convention |
| Emoji in formal documents | Cut, unless the register genuinely calls for it |
