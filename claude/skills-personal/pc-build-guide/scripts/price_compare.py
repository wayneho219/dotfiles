#!/usr/bin/env python3
"""跨通路現價比對：原價屋 + PChome 24h + 欣亞。

三家都沒有官方 API，用的是各站搜尋頁背後的未公開 JSON / 報價頁：
    原價屋   evaluate.php（見 coolpc_price.py）
    PChome   ecshweb.pchome.com.tw/search/v3.3/all/results
    欣亞     www.sinya.com.tw/api/search/getdata/

蝦皮沒有納入：API 直接擋反爬（403），且賣場報價賣家眾多、水貨/整新品/代購混雜，
單一「蝦皮價」參考價值低。要看蝦皮請自己開連結。

用法:
    price_compare.py 9700X
    price_compare.py 990 PRO --max 20000              # 關鍵字全部命中(AND)，可加 --min/--max
    price_compare.py 9700X --exclude 主機板 --exclude 組合  # 濾掉搭售/組合包，可重複
    price_compare.py --selftest

各家商品命名不一致（2TB vs 2T、含不含「代理盒裝」、PChome 常是主機板+CPU 組合包），
關鍵字用「最短能辨識的字串」就好，不要疊太多，再用 --exclude 清雜訊、自己看清單。
每家各列出命中品項（依價格排序）與最低價。單一通路報價僅供參考，
下單前仍請到各站/PTT 電蝦版核對，並注意組合包、水貨、福利品。
"""
import os
import re
import sys
import json
import subprocess
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import coolpc_price  # 重用 fetch() / parse()

UA = "Mozilla/5.0"
PRICE_NUM = re.compile(r"[\d,]+")


def _get(url, headers=None, timeout=25):
    # 用 curl：欣亞 nginx 會提早關連線，Python urllib 會 IncompleteRead 拿到截斷的 JSON，curl 不會
    cmd = ["curl", "-sS", "--compressed", "-m", str(timeout), "-A", UA]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True, timeout=timeout + 5).stdout


def to_int(s):
    m = PRICE_NUM.search(str(s) or "")
    return int(m.group(0).replace(",", "")) if m else None


def from_coolpc(kw):
    rows = coolpc_price.parse(coolpc_price.fetch())
    return [(name, price, "https://www.coolpc.com.tw/evaluate.php")
            for cat, name, price in rows]


def from_pchome(kw):
    url = ("https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="
           + urllib.parse.quote(kw) + "&page=1&sort=sale/dc")
    d = json.loads(_get(url))
    out = []
    for p in d.get("prods", []):
        price = to_int(p.get("price"))
        if price:
            out.append((p.get("name", ""), price,
                        "https://24h.pchome.com.tw/prod/" + p.get("Id", "")))
    return out


def from_sinya(kw):
    url = ("https://www.sinya.com.tw/api/search/getdata/?keyword="
           + urllib.parse.quote(kw))
    d = json.loads(_get(url, headers={"X-Requested-With": "XMLHttpRequest"}))
    out = []
    for p in d.get("results", []):
        price = to_int(p.get("new_price") or p.get("old_price"))
        if price:
            href = p.get("href") or ""
            if href and not href.startswith("http"):
                href = "https://www.sinya.com.tw" + href
            out.append((p.get("prod_title", ""), price, href))
    return out


SOURCES = [("原價屋", from_coolpc), ("PChome", from_pchome), ("欣亞", from_sinya)]


def selftest():
    assert to_int("$10,550元") == 10550
    assert to_int("16490") == 16490
    assert to_int("") is None
    assert to_int(None) is None
    print("selftest ok")


def main(argv):
    if "--selftest" in argv:
        return selftest()
    price_max = price_min = None
    kws, excl = [], []
    i = 0
    while i < len(argv):
        if argv[i] == "--max":
            price_max = int(argv[i + 1]); i += 2
        elif argv[i] == "--min":
            price_min = int(argv[i + 1]); i += 2
        elif argv[i] == "--exclude":  # 排除含此字的品項，可重複；濾組合包/主機板搭售用
            excl.append(argv[i + 1].lower()); i += 2
        else:
            kws.append(argv[i]); i += 1
    if not kws:
        print(__doc__)
        return 1
    low = [k.lower() for k in kws]

    for label, fn in SOURCES:
        try:
            rows = fn(kws[0])
        except Exception as e:  # 一家掛掉不影響其他家
            print(f"\n== {label} ==  查詢失敗：{e}")
            continue
        hits = []
        for name, price, url in rows:
            nl = name.lower()
            if not all(k in nl for k in low):
                continue
            if any(x in nl for x in excl):
                continue
            if price_max is not None and price > price_max:
                continue
            if price_min is not None and price < price_min:
                continue
            hits.append((price, name, url))
        hits.sort()
        print(f"\n== {label} ==  命中 {len(hits)} 筆"
              + (f"，最低 ${hits[0][0]:,}" if hits else ""))
        for price, name, url in hits[:12]:
            print(f"  ${price:>7,}  {name[:58]}  {url}")
    print("\n（單一通路報價，僅供參考；注意組合包/水貨/福利品，重要採購請再自行核對）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) or 0)
