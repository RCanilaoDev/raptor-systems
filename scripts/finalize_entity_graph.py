from pathlib import Path
from urllib.parse import urlparse
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
ORG={"@type":"Organization","@id":BASE+"/#organization","name":"Raptor Consulting Group","url":BASE+"/","email":"raptorsystems.ai@gmail.com","description":"Raptor Consulting Group is a technical SEO and search architecture consultancy supported by commerce systems and web operations.","founder":{"@id":BASE+"/about/ricardo-canilao/#person"},"areaServed":{"@type":"AdministrativeArea","name":"Orange County, California"},"logo":{"@type":"ImageObject","@id":BASE+"/#logo","url":BASE+"/assets/raptor-consulting-logo-img-header.webp","contentUrl":BASE+"/assets/raptor-consulting-logo-img-header.webp"}}
WEBSITE={"@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":"Raptor Consulting Group","publisher":{"@id":BASE+"/#organization"},"inLanguage":"en-US"}
PERSON={"@type":"Person","@id":BASE+"/about/ricardo-canilao/#person","name":"Ricardo Canilao","url":BASE+"/about/ricardo-canilao/","jobTitle":"Senior Digital Consultant","worksFor":{"@id":BASE+"/#organization"},"homeLocation":{"@type":"AdministrativeArea","name":"Orange County, California"},"knowsAbout":["Technical SEO","Search architecture","Structured data","Web operations","Website production management","Shopify","Ecommerce systems","Website migration","Digital analytics"]}
root=ET.parse(ROOT/'sitemap.xml').getroot(); ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}; urls=[n.text for n in root.findall('s:url/s:loc',ns)]
records=[]
for canonical in urls:
 path=urlparse(canonical).path; f=ROOT/('index.html' if path=='/' else path.strip('/')+'/index.html'); text=f.read_text(encoding='utf-8')
 m=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S); data=json.loads(m.group(1)); graph=data['@graph']
 graph=[x for x in graph if x.get('@id') not in (ORG['@id'],WEBSITE['@id'],PERSON['@id'])]
 graph.insert(0,dict(ORG)); graph.insert(1,dict(WEBSITE))
 if canonical==PERSON['url']: graph.insert(2,dict(PERSON))
 page=next((x for x in graph if x.get('@id')==canonical+'#webpage'),None)
 if page:
  page.update({'url':canonical,'isPartOf':{'@id':WEBSITE['@id']},'inLanguage':'en-US'})
  if canonical==PERSON['url']: page.update({'@type':'ProfilePage','about':{'@id':PERSON['@id']},'mainEntity':{'@id':PERSON['@id']}})
  elif '/work/case-studies/' in canonical and canonical.rstrip('/')!=BASE+'/work/case-studies': page['@type']='WebPage'
 for node in graph:
  typ=node.get('@type'); types=typ if isinstance(typ,list) else [typ]
  if 'Service' in types: node.update({'provider':{'@id':ORG['@id']},'url':node.get('url',canonical)})
  if 'Article' in types: node.update({'author':{'@id':PERSON['@id']},'publisher':{'@id':ORG['@id']},'inLanguage':'en-US'})
 data['@graph']=graph; rep='<script data-raptor-schema="v7" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'; text=text[:m.start()]+rep+text[m.end():]; f.write_text(text,encoding='utf-8')
 records.append((canonical,graph))

nodes={}; edges=[]
def walk(value,source,parent=None):
 if isinstance(value,dict):
  current=value.get('@id',parent)
  if value.get('@id') and len(value)>1:
   entry=nodes.setdefault(value['@id'],{'id':value['@id'],'types':set(),'defined_on':set()}); typ=value.get('@type');
   if typ: entry['types'].update(typ if isinstance(typ,list) else [typ])
   entry['defined_on'].add(source)
  for k,v in value.items():
   if isinstance(v,dict) and v.get('@id') and current: edges.append({'source':current,'property':k,'target':v['@id'],'page':source})
   elif isinstance(v,list) and current:
    for item in v:
     if isinstance(item,dict) and item.get('@id'): edges.append({'source':current,'property':k,'target':item['@id'],'page':source})
   walk(v,source,current)
 elif isinstance(value,list):
  for v in value: walk(v,source,parent)
for source,graph in records: walk(graph,source)
registry={'version':'16.08','base_url':BASE+'/','canonical_page_count':len(urls),'nodes':[{'id':v['id'],'types':sorted(v['types']),'defined_on':sorted(v['defined_on'])} for v in sorted(nodes.values(),key=lambda x:x['id'])],'edges':edges}
(ROOT/'docs/entity-graph-registry.json').write_text(json.dumps(registry,indent=2),encoding='utf-8')
type_counts={}
for n in registry['nodes']:
 for t in n['types']: type_counts[t]=type_counts.get(t,0)+1
lines=['# Raptor Entity Graph Registry','','Version: 16.08  ',f'Canonical pages: {len(urls)}  ',f'Defined entity nodes: {len(nodes)}  ',f'Relationship edges: {len(edges)}','','## Persistent Entities','',f'- Organization: `{ORG["@id"]}`',f'- WebSite: `{WEBSITE["@id"]}`',f'- Person: `{PERSON["@id"]}`',f'- Logo: `{BASE}/#logo`','','## Entity Counts','']+[f'- {k}: {v}' for k,v in sorted(type_counts.items())]+['','## Governance','','- One canonical ID represents each entity across the site.','- Organization and WebSite definitions are identical wherever embedded.','- The full Person definition lives on Ricardo Canilao’s ProfilePage; other pages reference its ID.','- Service entities use their canonical service URL plus `#service`.','- Case studies use their canonical URL plus `#article`.','- Page and breadcrumb IDs use `#webpage` and `#breadcrumb`.','- Structured data must describe visible content and must not invent an entity, result, rating, review, or offer.','- Graph validation is required after any URL, navigation, content-role, or schema change.']
(ROOT/'docs/entity-graph-registry.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Normalized {len(urls)} page graphs: {len(nodes)} nodes, {len(edges)} edges')
