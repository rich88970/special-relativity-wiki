"""匯入來源 S1：把「讀懂物理」近代物理第 1 章（相對論）的講解文字轉成純文字，存進 raw/。

只取講解正文，略過題目卡（div.problem）、圖解、考試書寫側欄；數學式保留 LaTeX 原文（$...$）。
用法：python tools/ingest_site.py <study-site 的 subjects/modern/ch01 資料夾>
"""
import datetime
import html
import io
import os
import re
import sys
from html.parser import HTMLParser

SECTIONS = ["01-postulates", "02-time", "04-length", "05-twin", "08-energy", "11-lorentz"]
SKIP_CLASSES = {"problem", "anim", "video", "supp", "exam-only"}
BLOCKS = {"p", "h2", "h3", "h4", "li", "div", "section", "tr", "table", "ul", "ol"}


class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.skip_depth, self.out = [], 0, []

    def handle_starttag(self, tag, attrs):
        cls = set((dict(attrs).get("class") or "").split())
        skipping = self.skip_depth > 0 or bool(cls & SKIP_CLASSES)
        if tag in ("br", "img", "hr", "input", "meta", "link"):
            return
        self.stack.append(skipping)
        if skipping:
            self.skip_depth += 1
        elif tag in BLOCKS:
            self.out.append("\n")
        if not skipping and tag in ("h2", "h3", "h4"):
            self.out.append("## " if tag == "h2" else "### ")

    def handle_endtag(self, tag):
        if tag in ("br", "img", "hr", "input", "meta", "link") or not self.stack:
            return
        if self.stack.pop():
            self.skip_depth -= 1
        elif tag in BLOCKS:
            self.out.append("\n")

    def handle_data(self, data):
        if self.skip_depth == 0:
            self.out.append(data)


def main(src):
    today = datetime.date.today().isoformat()
    parts = [
        "---\nid: S1\ntitle: 讀懂物理｜近代物理第 1 章 相對論（講解正文）\nsource: 使用者自己的讀書網站（依 Beiser《Concepts of Modern Physics》第 1 章整理）\n"
        "url: https://rich88970.github.io/physics-study-site/chapter.html?s=modern&c=ch01\n"
        f"sections: {', '.join(SECTIONS)}\nfetched: {today}\n"
        "note: 只取講解正文，略過題目卡、圖解與考試側欄；LaTeX 原樣保留，匯入後不修改\n---\n"
    ]
    for name in SECTIONS:
        raw = io.open(os.path.join(src, "sections", name + ".html"), encoding="utf-8").read()
        p = TextOnly()
        p.feed(raw)
        text = html.unescape("".join(p.out))
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        parts.append(f"\n\n# 節 {name}\n\n{text}\n")
    out = "raw/S1-study-site-modern-ch01.md"
    io.open(out, "w", encoding="utf-8").write("".join(parts))
    print(out, sum(len(x) for x in parts), "字元")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1])
