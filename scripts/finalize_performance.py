from pathlib import Path
from urllib.parse import urlparse
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BUILD = "16.10"


def strip_css_comments(source: str) -> str:
    out, i, quote = [], 0, None
    while i < len(source):
        char = source[i]
        if quote:
            out.append(char)
            if char == "\\" and i + 1 < len(source):
                i += 1
                out.append(source[i])
            elif char == quote:
                quote = None
        elif char in ("'", '"'):
            quote = char
            out.append(char)
        elif source.startswith("/*", i):
            end = source.find("*/", i + 2)
            i = len(source) if end < 0 else end + 2
            continue
        else:
            out.append(char)
        i += 1
    return "".join(out)


def minify_css(source: str) -> str:
    strings = []

    def protect(match):
        strings.append(match.group(0))
        return f"___RAPTOR_STRING_{len(strings) - 1}___"

    cleaned = strip_css_comments(source)
    cleaned = re.sub(r"(?:'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\")", protect, cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"\s*([{}:;,>~])\s*", r"\1", cleaned)
    cleaned = cleaned.replace(";}" , "}")
    for index, value in enumerate(strings):
        cleaned = cleaned.replace(f"___RAPTOR_STRING_{index}___", value)
    return cleaned + "\n"


def optimize_js(source: str) -> str:
    # Preserve line boundaries for automatic semicolon insertion. This removes
    # block comments, indentation, trailing space, and empty lines only.
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    lines = [line.strip() for line in source.splitlines() if line.strip()]
    return "\n".join(lines) + "\n"


def canonical_files():
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(ROOT / "sitemap.xml")
    for node in tree.findall("s:url/s:loc", ns):
        path = urlparse(node.text).path
        yield ROOT / ("index.html" if path == "/" else path.strip("/") + "/index.html")


(ROOT / "styles.min.css").write_text(minify_css((ROOT / "styles.css").read_text(encoding="utf-8")), encoding="utf-8")
(ROOT / "script.min.js").write_text(optimize_js((ROOT / "script.js").read_text(encoding="utf-8")), encoding="utf-8")

files = list(canonical_files())
if (ROOT / "404.html").exists():
    files.append(ROOT / "404.html")
for file in files:
    html = file.read_text(encoding="utf-8")
    html = re.sub(r'href="/(?:styles|styles\.min)\.css(?:\?v=[^"]+)?"', f'href="/styles.min.css?v={BUILD}"', html)
    html = re.sub(r'<script(?: defer)? src="/(?:script|script\.min)\.js(?:\?v=[^"]+)?"></script>', f'<script defer src="/script.min.js?v={BUILD}"></script>', html)
    file.write_text(html, encoding="utf-8")

print(f"Performance finalization complete: {len(files)} HTML files, build {BUILD}")
