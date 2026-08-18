from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))


ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [node.text for node in ET.parse(ROOT / "sitemap.xml").findall("s:url/s:loc", ns)]
for absolute in urls:
    path = urlparse(absolute).path
    file = ROOT / ("index.html" if path == "/" else path.strip("/") + "/index.html")
    html = file.read_text(encoding="utf-8")
    if 'href="/styles.min.css?v=16.10"' not in html:
        errors.append(f"CSS ASSET {path}")
    if '<script defer src="/script.min.js?v=16.10"></script>' not in html:
        errors.append(f"JS ASSET {path}")
    parser = Parser()
    parser.feed(html)
    for image in parser.images:
        if not image.get("width") or not image.get("height"):
            errors.append(f"IMAGE DIMENSIONS {path}: {image.get('src')}")
        if image.get("src", "").endswith((".jpg", ".jpeg", ".png")) and "favicon" not in image.get("src", ""):
            errors.append(f"IMAGE FORMAT {path}: {image.get('src')}")
        if "footer-split-logo__part" in image.get("class", "") and image.get("loading") != "lazy":
            errors.append(f"LAZY IMAGE {path}: {image.get('src')}")

for required in ("styles.min.css", "script.min.js"):
    if not (ROOT / required).exists() or not (ROOT / required).stat().st_size:
        errors.append(f"MISSING ASSET {required}")
if (ROOT / "styles.min.css").stat().st_size >= (ROOT / "styles.css").stat().st_size:
    errors.append("CSS NOT REDUCED")
if (ROOT / "script.min.js").stat().st_size >= (ROOT / "script.js").stat().st_size:
    errors.append("JS NOT REDUCED")

print(f"Performance pages: {len(urls)}")
print(f"CSS: {(ROOT / 'styles.css').stat().st_size} -> {(ROOT / 'styles.min.css').stat().st_size} bytes")
print(f"JS: {(ROOT / 'script.js').stat().st_size} -> {(ROOT / 'script.min.js').stat().st_size} bytes")
print(f"Errors: {len(errors)}")
for error in errors:
    print(error)
sys.exit(bool(errors))
