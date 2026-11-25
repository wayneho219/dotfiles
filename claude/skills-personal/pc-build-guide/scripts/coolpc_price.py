#!/usr/bin/env python3
"""原價屋 (coolpc) 估價單現價查詢。

原價屋沒有官方 API，但整站報價集中在 evaluate.php 這一頁：所有商品都放在
<OPTION> 裡，文字格式固定為「名稱/規格, $價格 符號」。抓一次就有全部。

用法:
    coolpc_price.py 9700X                 # 名稱含 9700X 的品項
    coolpc_price.py 990 PRO 2TB           # 多個關鍵字 = 全部都要命中 (AND)
    coolpc_price.py B650M WIFI --max 4000 # 加價格上限
    coolpc_price.py --selftest            # 解析器自我測試 (不連網)

輸出: [分類] 名稱  $價格，依價格排序。價格為現金價，符號 ◆=熱賣 ★=有圖 等。
資料每個工作日更新，僅供參考，下單前請以原價屋網站/現場為準。
"""
import os
import sys
import re
import time
import tempfile
import http.client
import urllib.request

URL = "https://www.coolpc.com.tw/evaluate.php"
CACHE = os.path.join(tempfile.gettempdir(), "coolpc_evaluate.html")
CACHE_TTL = 6 * 3600  # ponytail: 同一天多次查詢共用快取，別狂打小店家的站

ROW_RE = re.compile(
    r"<OPTGROUP[^>]*LABEL=['\"]([^'\"]+)['\"]"      # group 1: 分類標籤
    r"|<OPTION[^>]*>\s*([^<\n]+)",                   # group 2: 選項文字
    re.I,
)
PRICE_RE = re.compile(r"^(.*?),\s*\$([\d,]+)")


def fetch(fresh=False):
    try:
        if not fresh and time.time() - _mtime(CACHE) < CACHE_TTL:
            return open(CACHE, "rb").read()
    except OSError:
        pass
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, timeout=30)
    try:
        data = resp.read()
    except http.client.IncompleteRead as e:
        data = e.partial  # coolpc 常提早關閉連線，實際內容已收完
    try:
        open(CACHE, "wb").write(data)
    except OSError:
        pass
    return data


def _mtime(path):
    import os
    return os.path.getmtime(path)


def parse(html_bytes):
    """回傳 [(分類, 名稱, 價格int), ...]，保持頁面順序。"""
    text = html_bytes.decode("big5", errors="ignore")  # 頁面是 Big5，且有少數壞位元組
    rows = []
    cur = ""
    for m in ROW_RE.finditer(text):
        if m.group(1):
            cur = m.group(1).strip()
            continue
        pm = PRICE_RE.match(m.group(2).strip())
        if pm:
            rows.append((cur, pm.group(1).strip(), int(pm.group(2).replace(",", ""))))
    return rows


def page_date(html_bytes):
    text = html_bytes.decode("big5", errors="ignore")
    m = re.search(r"id=Mdy>\s*(20\d\d/\d{1,2}/\d{1,2}(?:\s+\d{1,2}:\d{2})?)", text)
    return m.group(1) if m else "未知"


def selftest():
    sample = (
        b"<SELECT><OPTGROUP LABEL='AMD AM5 9000'>"
        b"<OPTION value=1>{AMD R7 9700X} \xa5N\xb2z\xac\xd5\xb8\xcb, $11450 \xa1\xb6</OPTION>"
        b"<OPTGROUP LABEL='SSD'>"
        b"<OPTION value=2>Samsung 990 PRO 2TB /Gen4, $17,999</OPTION>"
        b"<OPTION value=3>\xa6\xb9\xa6C\xb5L\xbb\xf9\xae\xe6</OPTION></SELECT>"
    )
    rows = parse(sample)
    assert len(rows) == 2, rows
    assert rows[0][0] == "AMD AM5 9000" and rows[0][2] == 11450, rows[0]
    assert rows[1][0] == "SSD" and rows[1][2] == 17999, rows[1]
    print("selftest ok")


def main(argv):
    if "--selftest" in argv:
        return selftest()
    fresh = "--fresh" in argv
    argv = [a for a in argv if a != "--fresh"]
    price_max = price_min = None
    out = []
    i = 0
    while i < len(argv):
        if argv[i] == "--max":
            price_max = int(argv[i + 1]); i += 2
        elif argv[i] == "--min":
            price_min = int(argv[i + 1]); i += 2
        else:
            out.append(argv[i]); i += 1
    keywords = [k.lower() for k in out]
    if not keywords:
        print(__doc__)
        return 1

    html = fetch(fresh=fresh)
    rows = parse(html)
    hits = []
    for cat, name, price in rows:
        hay = (cat + " " + name).lower()
        if all(k in hay for k in keywords):
            if price_max is not None and price > price_max:
                continue
            if price_min is not None and price < price_min:
                continue
            hits.append((price, cat, name))
    hits.sort()
    print(f"# 原價屋 evaluate.php  頁面日期 {page_date(html)}  命中 {len(hits)} 筆  (現金價，僅供參考)")
    for price, cat, name in hits:
        print(f"  [{cat}] {name}  ${price:,}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) or 0)
