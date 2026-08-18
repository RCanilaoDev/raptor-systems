from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; errors=[]
class P(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[]; self.headings=[]; self.links=[]; self.buttons=[]; self.images=[]; self.nav=[]; self.aria=[]; self.controls=[]; self.main=0; self.lang=''
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='html': self.lang=d.get('lang','')
  if d.get('id'): self.ids.append(d['id'])
  if re.fullmatch(r'h[1-6]',t): self.headings.append(int(t[1]))
  if t=='a': self.links.append(d)
  if t=='button': self.buttons.append(d)
  if t=='img': self.images.append(d)
  if t=='nav': self.nav.append(d)
  if t=='main': self.main+=1
  if d.get('aria-labelledby'): self.aria.extend(d['aria-labelledby'].split())
  if d.get('aria-controls'): self.controls.extend(d['aria-controls'].split())
root=ET.parse(ROOT/'sitemap.xml').getroot(); ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}; urls=[n.text for n in root.findall('s:url/s:loc',ns)]
for absolute in urls:
 path=urlparse(absolute).path; f=ROOT/('index.html' if path=='/' else path.strip('/')+'/index.html'); text=f.read_text(encoding='utf-8'); p=P(); p.feed(text)
 if p.lang!='en': errors.append(f'LANG {path}')
 if p.main!=1: errors.append(f'MAIN {path}: {p.main}')
 dup={x for x in p.ids if p.ids.count(x)>1}
 if dup: errors.append(f'DUPLICATE ID {path}: {dup}')
 if p.headings.count(1)!=1: errors.append(f'H1 {path}')
 if any(b-a>1 for a,b in zip(p.headings,p.headings[1:])): errors.append(f'HEADING JUMP {path}: {p.headings}')
 if any('alt' not in x for x in p.images): errors.append(f'IMAGE ALT {path}')
 if any(not x.get('aria-label') for x in p.nav): errors.append(f'NAV LABEL {path}')
 if any(x not in p.ids for x in p.aria): errors.append(f'ARIA LABELLEDBY {path}')
 if any(x not in p.ids for x in p.controls): errors.append(f'ARIA CONTROLS {path}')
 if 'href="#main-content"' not in text or 'id="main-content"' not in text: errors.append(f'SKIP LINK {path}')
 if re.search(r'tabindex="[1-9]',text): errors.append(f'POSITIVE TABINDEX {path}')
css=(ROOT/'styles.css').read_text(); js=(ROOT/'script.js').read_text()
for token in ('@media (prefers-reduced-motion: reduce)','@media (max-width: 560px)','.menu-toggle','.services-menu','focus-visible'):
 if token not in css: errors.append(f'CSS REQUIREMENT {token}')
for token in ("event.key === 'Escape'","toggle.focus()","servicesDisclosure.open = false","aria-expanded"):
 if token not in js: errors.append(f'INTERACTION REQUIREMENT {token}')
if re.search(r'(?:tel:|sms:)\+?\d','\n'.join((ROOT/urlparse(u).path.strip('/')/'index.html').read_text() if urlparse(u).path!='/' else (ROOT/'index.html').read_text() for u in urls)): errors.append('HARDCODED PHONE')
print(f'Accessibility pages: {len(urls)}'); print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
