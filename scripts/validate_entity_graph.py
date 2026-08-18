from pathlib import Path
from urllib.parse import urlparse
import json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; BASE='https://raptorconsultinggroup.com'; errors=[]
root=ET.parse(ROOT/'sitemap.xml').getroot(); ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}; urls=[n.text for n in root.findall('s:url/s:loc',ns)]
definitions={}; references=[]; stable={BASE+'/#organization':[],BASE+'/#website':[]}; person_pages=[]; articles=[]; services=[]
def walk(v,page,parent=None):
 if isinstance(v,dict):
  current=v.get('@id',parent)
  if v.get('@id') and len(v)>1:
   definitions.setdefault(v['@id'],[]).append((page,v))
  if v.get('@id') and len(v)==1: references.append((page,parent,v['@id']))
  for x in v.values(): walk(x,page,current)
 elif isinstance(v,list):
  for x in v: walk(x,page,parent)
for url in urls:
 path=urlparse(url).path; f=ROOT/('index.html' if path=='/' else path.strip('/')+'/index.html'); text=f.read_text(encoding='utf-8'); m=re.search(r'<script data-raptor-schema="v7" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not m: errors.append(f'SCHEMA VERSION {url}'); continue
 data=json.loads(m.group(1)); graph=data.get('@graph',[]); walk(graph,url)
 for sid in stable:
  node=next((x for x in graph if x.get('@id')==sid),None)
  if not node: errors.append(f'STABLE ENTITY {url} missing {sid}')
  else: stable[sid].append(json.dumps(node,sort_keys=True))
 for node in graph:
  t=node.get('@type'); ts=t if isinstance(t,list) else [t]
  if node.get('@id')==BASE+'/about/ricardo-canilao/#person': person_pages.append(url)
  if 'Article' in ts: articles.append(node.get('@id'))
  if 'Service' in ts: services.append(node.get('@id'))
for sid,versions in stable.items():
 if len(set(versions))!=1: errors.append(f'CONFLICTING DEFINITION {sid}')
for page,parent,target in references:
 if target.startswith(BASE) and target not in definitions: errors.append(f'UNRESOLVED {page}: {target}')
for entity in definitions:
 if '.html' in entity: errors.append(f'STALE ENTITY ID {entity}')
if person_pages!=[BASE+'/about/ricardo-canilao/']: errors.append(f'PERSON DEFINITION PAGES {person_pages}')
if len(set(articles))!=5: errors.append(f'ARTICLE COUNT {len(set(articles))}')
if len(set(services))!=18: errors.append(f'SERVICE COUNT {len(set(services))}')
registry=json.loads((ROOT/'docs/entity-graph-registry.json').read_text())
if registry.get('canonical_page_count')!=39: errors.append('REGISTRY PAGE COUNT')
print(f'Entity definitions: {len(definitions)}'); print(f'References checked: {len(references)}'); print(f'Unique services: {len(set(services))}'); print(f'Unique articles: {len(set(articles))}'); print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
