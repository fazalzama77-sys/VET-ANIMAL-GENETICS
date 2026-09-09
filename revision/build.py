"""Inline _revision.css into each rapid-revision sheet.

The sheets are meant to be self-contained single files (a student may copy just
one of them to a phone or email it), so the shared stylesheet is baked in.
_revision.css stays the single source of truth -- edit it, then re-run this.

    python build.py
"""
import io
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SHEETS = [
    "unit1-rapid-revision.html",
    "unit2-rapid-revision.html",
    "unit3-rapid-revision.html",
]

css = io.open(os.path.join(HERE, "_revision.css"), encoding="utf-8").read()
block = "<style>\n" + css + "\n</style>"

for name in SHEETS:
    path = os.path.join(HERE, name)
    html = io.open(path, encoding="utf-8").read()
    if "<style>" in html:
        html = re.sub(r"<style>.*?</style>", lambda m: block, html, count=1, flags=re.S)
    else:
        html = html.replace('<link rel="stylesheet" href="_revision.css">', block, 1)
    io.open(path, "w", encoding="utf-8").write(html)
    print("built", name)
