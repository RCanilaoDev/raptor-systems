from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={"/insights/":2,"/insights/search/":3,"/insights/commerce/":3,"/insights/web-operations/":3}; errors=[]
for url,depth in PAGES.items():
 text=(ROOT/url.strip('/')/'index.html').read_text(encoding='utf-8'); m=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not m: errors.append(f"SCHEMA VERSION {url}"); continue
 g=json.loads(m.group(1))['@graph']; page=next(x for x in g if x.get('@id')==BASE+url+'#webpage'); bc=next((x for x in g if x.get('@type')=='BreadcrumbList'),{})
 if page.get('creator',{}).get('@id')!=BASE+'/about/ricardo-canilao/#person': errors.append(f"CREATOR {url}")
 if page.get('publisher',{}).get('@id')!=BASE+'/#organization': errors.append(f"PUBLISHER {url}")
 if len(bc.get('itemListElement',[]))!=depth: errors.append(f"BREADCRUMB {url}")
 if 'insights-editorial-standard' not in text: errors.append(f"EDITORIAL STANDARD {url}")
if not (ROOT/'docs/insights-article-specification.md').exists(): errors.append('ARTICLE SPECIFICATION')
print('Insights pages: 4'); print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
