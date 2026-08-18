from pathlib import Path
from html.parser import HTMLParser
import json, re, sys, xml.etree.ElementTree as ET
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
class P(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.c=[]; self.h=[]; self.title=0; self.desc=0; self.metas={}; self.schema=[]; self._schema=None
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=="a" and d.get("href"): self.links.append(d["href"])
  if t=="link" and "canonical" in d.get("rel",""): self.c.append(d.get("href"))
  if re.fullmatch("h[1-6]",t): self.h.append(t)
  if t=="title": self.title+=1
  if t=="meta" and d.get("name")=="description": self.desc+=1
  if t=="meta" and (d.get("name") or d.get("property")): self.metas[d.get("name") or d.get("property")]=d.get("content")
  if t=="script" and d.get("type")=="application/ld+json": self._schema=""
 def handle_data(self,d):
  if self._schema is not None: self._schema+=d
 def handle_endtag(self,t):
  if t=="script" and self._schema is not None: self.schema.append(self._schema); self._schema=None

tree=ET.parse(ROOT/"sitemap.xml"); ns={"s":"http://www.sitemaps.org/schemas/sitemap/0.9"}
urls=[x.text for x in tree.findall("s:url/s:loc",ns)]; errors=[]
if len(urls)!=len(set(urls)): errors.append("DUPLICATE sitemap URLs")
for absolute in urls:
 path=urlparse(absolute).path; file=ROOT/("index.html" if path=="/" else path.strip("/")+"/index.html")
 if not file.exists(): errors.append(f"MISSING {path}"); continue
 text=file.read_text(encoding="utf-8"); p=P(); p.feed(text)
 if p.c!=[absolute]: errors.append(f"CANONICAL {path}: {p.c}")
 if p.title!=1 or p.desc!=1: errors.append(f"METADATA {path}: title={p.title} desc={p.desc}")
 if p.h.count("h1")!=1: errors.append(f"H1 {path}: {p.h.count('h1')}")
 for key in ("robots","twitter:card","twitter:title","twitter:description","twitter:image","og:type","og:title","og:description","og:url","og:image"):
  if not p.metas.get(key): errors.append(f"SOCIAL/ROBOTS {path}: missing {key}")
 if p.metas.get("og:url")!=absolute: errors.append(f"OG URL {path}: {p.metas.get('og:url')}")
 if "GTM-TZVZGCSP" not in text or "googletagmanager.com/ns.html" not in text: errors.append(f"GTM {path}")
 try:
  graph=json.loads(p.schema[0]).get("@graph",[])
  ids={x.get("@id") for x in graph}
  for required in (BASE+"/#organization",BASE+"/#website",absolute+"#webpage"):
   if required not in ids: errors.append(f"SCHEMA {path}: missing {required}")
 except Exception as exc: errors.append(f"SCHEMA JSON {path}: {exc}")
 for href in p.links:
  if href.startswith(("#","mailto:","tel:","sms:","http")): continue
  clean=href.split("#")[0].split("?")[0]
  target=ROOT/("index.html" if clean=="/" else clean.strip("/")+"/index.html" if clean.endswith("/") else clean.lstrip("/"))
  if clean and not target.exists(): errors.append(f"BROKEN {path} -> {href}")
 stale=re.findall(r'https://raptorconsultinggroup\.com/[^"< ]+\.html',text)
 if stale: errors.append(f"STALE URL {path}: {sorted(set(stale))[:3]}")
print(f"Canonical pages: {len(urls)}")
print("Errors:",len(errors))
for e in errors: print(e)
sys.exit(bool(errors))
