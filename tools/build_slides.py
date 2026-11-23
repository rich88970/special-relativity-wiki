"""把 slides/_content.html（各頁內容）套進 slides/_frame.html（外框、翻頁程式），輸出 slides/index.html。

內容裡的 Wiki 連結寫成 W/concepts/xxx.md，這裡換成同一個 GitHub Pages 網站上的 ../wiki/concepts/xxx.html
（GitHub Pages 會用 Jekyll 把 wiki/ 的 Markdown 轉成網頁，不依賴 github.com 的檔案瀏覽頁）。
用法：python tools/build_slides.py
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = "../wiki/"

frame = io.open(os.path.join(ROOT, "slides", "_frame.html"), encoding="utf-8").read()
body = io.open(os.path.join(ROOT, "slides", "_content.html"), encoding="utf-8").read()
body = re.sub(r'href="W/([^"]+)\.md"', lambda m: 'target="_blank" rel="noopener" href="' + WIKI + m.group(1) + '.html"', body)
out = frame.replace("<!--SLIDES-->", body)
io.open(os.path.join(ROOT, "slides", "index.html"), "w", encoding="utf-8").write(out)
print("slides/index.html：", out.count('<section class="slide"'), "頁")
