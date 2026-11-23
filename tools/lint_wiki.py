"""檢查 A：Wiki 格式與出處（AGENTS.md 第 3、6 節）。

檢查項目
1. 概念頁每一段、每一條清單都有出處標記〔S#…〕或〔計算：…〕（標題、空行、「相關概念」除外）
2. 出處標記裡的 S# 都有對應的來源頁 wiki/sources/S#.md
3. 來源頁「重點」「數字與例子」每條都有（raw 第 N–M 行），而且行號在原始檔範圍內
4. 所有相對連結指到存在的檔案
5. index.md 列出所有來源頁與概念頁

用法：python tools/lint_wiki.py [--out checks/xxx.md]
結束碼：0＝沒有錯誤，1＝有錯誤
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r"〔([^〕]*)〕")
LINK = re.compile(r"\]\(([^)\s]+)\)")
RAWREF = re.compile(r"raw\s*第\s*([\d\s、,，–\-~～]+?)\s*行")  # 可寫「第 12 行」「第 12–15 行」「第 98、121–127 行」


def ranges(spec):
    """把「98、121–127」拆成 [(98, 98), (121, 127)]。"""
    out = []
    for part in re.split(r"[、,，]", spec):
        nums = [int(x) for x in re.findall(r"\d+", part)]
        if nums:
            out.append((nums[0], nums[-1]))
    return out


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def read(p):
    return io.open(p, encoding="utf-8").read()


def main():
    errors, warns = [], []
    src_pages = sorted(glob.glob(os.path.join(ROOT, "wiki", "sources", "S*.md")))
    con_pages = sorted(glob.glob(os.path.join(ROOT, "wiki", "concepts", "*.md")))
    src_ids = {os.path.basename(p)[:-3] for p in src_pages}

    # 1、2 概念頁出處
    for p in con_pages:
        section = ""
        lines = read(p).split("\n")
        for i, line in enumerate(lines, 1):
            s = line.strip()
            if s.startswith("#"):
                section = s.lstrip("# ").strip()
                continue
            if not s or section.startswith("相關概念") or s.startswith("|---") or s.startswith("| ---"):
                continue
            nxt = lines[i].strip() if i < len(lines) else ""
            if s.startswith("|") and (nxt.startswith("|---") or nxt.startswith("| ---")):
                continue  # 表頭不用出處；表格內容列仍要有
            tags = TAG.findall(s)
            if not tags:
                errors.append(f"{rel(p)} 第 {i} 行沒有出處標記：{s[:50]}")
                continue
            for t in tags:
                if t.startswith("計算"):
                    continue
                ids = re.findall(r"S\d+", t)
                if not ids:
                    errors.append(f"{rel(p)} 第 {i} 行出處格式不對：〔{t}〕")
                for sid in ids:
                    if sid not in src_ids:
                        errors.append(f"{rel(p)} 第 {i} 行引用不存在的來源 {sid}")

    # 3 來源頁行號
    for p in src_pages:
        text = read(p)
        m = re.search(r"\((\.\./\.\./raw/[^)]+)\)", text)
        if not m:
            errors.append(f"{rel(p)} 找不到原始檔連結（../../raw/…）")
            continue
        raw = os.path.normpath(os.path.join(os.path.dirname(p), m.group(1)))
        if not os.path.exists(raw):
            errors.append(f"{rel(p)} 原始檔不存在：{m.group(1)}")
            continue
        n_lines = len(read(raw).split("\n"))
        section = ""
        for i, line in enumerate(text.split("\n"), 1):
            s = line.strip()
            if s.startswith("#"):
                section = s.lstrip("# ").strip()
                continue
            if section in ("重點", "數字與例子") and s.startswith(("-", "*")):
                refs = RAWREF.findall(s)
                if not refs:
                    errors.append(f"{rel(p)} 第 {i} 行沒有標 raw 行號：{s[:50]}")
                for a, b in (r for spec in refs for r in ranges(spec)):
                    if not (1 <= a <= b <= n_lines):
                        errors.append(f"{rel(p)} 第 {i} 行行號超出範圍（原始檔 {n_lines} 行）：raw 第 {a}–{b} 行")

    # 4 連結
    for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True):
        for i, line in enumerate(read(p).split("\n"), 1):
            for target in LINK.findall(line):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                path = os.path.normpath(os.path.join(os.path.dirname(p), target.split("#")[0]))
                if not os.path.exists(path):
                    errors.append(f"{rel(p)} 第 {i} 行連結失效：{target}")

    # 5 index
    idx = os.path.join(ROOT, "wiki", "index.md")
    if not os.path.exists(idx):
        errors.append("wiki/index.md 不存在")
    else:
        itext = read(idx)
        for p in src_pages + con_pages:
            name = rel(p)[len("wiki/"):]
            if name not in itext:
                errors.append(f"index.md 沒有列出 {name}")

    out = [f"# 檢查 A：Wiki 格式與出處\n", f"- 來源頁 {len(src_pages)} 頁、概念頁 {len(con_pages)} 頁",
           f"- 錯誤 {len(errors)} 個、提醒 {len(warns)} 個\n"]
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
