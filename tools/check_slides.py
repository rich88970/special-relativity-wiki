"""檢查 C：簡報對 Wiki（AGENTS.md 第 5、6 節）。

檢查項目
1. 每一頁 <section class="slide"> 都有 data-wiki，列出的 Wiki 頁面都存在
2. 每一頁都有頁尾出處（class="src"）
3. 簡報裡出現的每個數字（10 以上的整數、所有小數、科學記號），都要出現在該頁 data-wiki 列的頁面裡
4. 每頁文字量（不含頁尾），超過 160 字提醒

用法：python tools/check_slides.py [--out checks/xxx.md]
結束碼：0＝沒有錯誤，1＝有錯誤
"""
import html
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDE = re.compile(r'<section class="slide"([^>]*)>(.*?)</section>', re.S)
NUM = re.compile(r"(?<![\w.])(\d+(?:[.,]\d+)*)(?![\w])")


def visible(fragment):
    fragment = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    fragment = re.sub(r'<(\w+)[^>]*class="[^"]*\bsrc\b[^"]*"[^>]*>.*?</\1>', " ", fragment, flags=re.S)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return html.unescape(fragment)


def norm(n):
    return n.replace(",", "")


def main():
    path = os.path.join(ROOT, "slides", "index.html")
    doc = io.open(path, encoding="utf-8").read()
    errors, warns = [], []
    slides = SLIDE.findall(doc)
    for k, (attrs, body) in enumerate(slides, 1):
        m = re.search(r'data-wiki="([^"]*)"', attrs)
        pages = (m.group(1).split() if m else [])
        if not pages:
            errors.append(f"第 {k} 頁沒有 data-wiki")
        wiki_text = ""
        for pg in pages:
            fp = os.path.join(ROOT, "wiki", pg)
            if not os.path.exists(fp):
                errors.append(f"第 {k} 頁 data-wiki 指到不存在的頁面：{pg}")
            else:
                wiki_text += io.open(fp, encoding="utf-8").read()
        if 'class="src"' not in body:
            errors.append(f"第 {k} 頁沒有頁尾出處（class=\"src\"）")
        text = visible(body)
        wiki_nums = {norm(x) for x in NUM.findall(wiki_text)}
        for n in NUM.findall(text):
            v = norm(n)
            if "." not in v and len(v) < 2:
                continue  # 個位數整數（步驟編號、「兩個」之類）不檢查
            if v not in wiki_nums:
                errors.append(f"第 {k} 頁的數字 {n} 不在引用的 Wiki 頁面裡（{' '.join(pages) or '無'}）")
        chars = len(re.sub(r"\s", "", text))
        if chars > 160:
            warns.append(f"第 {k} 頁文字 {chars} 字，超過 160 字")
    out = ["# 檢查 C：簡報對 Wiki\n", f"- 簡報共 {len(slides)} 頁", f"- 錯誤 {len(errors)} 個、提醒 {len(warns)} 個\n"]
    out += [f"- 錯誤：{e}" for e in errors] + [f"- 提醒：{w}" for w in warns]
    report = "\n".join(out) + "\n"
    print(report)
    if "--out" in sys.argv:
        dst = sys.argv[sys.argv.index("--out") + 1]
        io.open(os.path.join(ROOT, dst), "w", encoding="utf-8").write(report)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
