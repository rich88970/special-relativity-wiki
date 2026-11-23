"""把 slides/_content.html（各頁內容）套進 slides/_frame.html（外框、翻頁程式），輸出 slides/index.html。

內容裡的 Wiki 連結寫成 W/concepts/xxx.md，這裡換成 GitHub 上的頁面網址（GitHub 會把 Markdown 排好版）。
用法：python tools/build_slides.py
"""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = "https://github.com/rich88970/special-relativity-wiki/blob/main/wiki/"

frame = io.open(os.path.join(ROOT, "slides", "_frame.html"), encoding="utf-8").read()
body = io.open(os.path.join(ROOT, "slides", "_content.html"), encoding="utf-8").read()
body = body.replace('href="W/', 'target="_blank" rel="noopener" href="' + WIKI)
out = frame.replace("<!--SLIDES-->", body)
io.open(os.path.join(ROOT, "slides", "index.html"), "w", encoding="utf-8").write(out)
print("slides/index.html：", out.count('<section class="slide"'), "頁")
