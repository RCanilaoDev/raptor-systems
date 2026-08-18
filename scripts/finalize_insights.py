from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={
 "/insights/":("Insights",[("Home","/"),("Insights",None)],["/insights/search/","/insights/commerce/","/insights/web-operations/"]),
 "/insights/search/":("Search Insights",[("Home","/"),("Insights","/insights/"),("Search",None)],["/services/search-systems/","/work/systems/hqcp/","/work/case-studies/specialized-accounting-search-architecture/"]),
 "/insights/commerce/":("Commerce Insights",[("Home","/"),("Insights","/insights/"),("Commerce",None)],["/services/commerce-systems/","/work/case-studies/wordpress-shopify-commerce-system/","/services/commerce-systems/ecommerce-search-architecture/"]),
 "/insights/web-operations/":("Web Operations Insights",[("Home","/"),("Insights","/insights/"),("Web Operations",None)],["/services/web-operations/","/work/systems/web-production-system/","/work/case-studies/website-infrastructure-migration/"]),
}
LABEL={"/insights/search/":"Search","/insights/commerce/":"Commerce","/insights/web-operations/":"Web Operations","/services/search-systems/":"Search Systems","/work/systems/hqcp/":"HQCP","/work/case-studies/specialized-accounting-search-architecture/":"Accounting Case Study","/services/commerce-systems/":"Commerce Systems","/work/case-studies/wordpress-shopify-commerce-system/":"Commerce Case Study","/services/commerce-systems/ecommerce-search-architecture/":"Ecommerce Search Architecture","/services/web-operations/":"Web Operations Services","/work/systems/web-production-system/":"Web Production System","/work/case-studies/website-infrastructure-migration/":"Migration Case Study"}
def breadcrumb(items):
 out=[]
 for label,url in items:
  if out: out.append('<span aria-hidden="true">//</span>')
  out.append(f'<a href="{url}">{html.escape(label)}</a>' if url else f'<span>{html.escape(label)}</span>')
 return '<nav aria-label="Breadcrumb" class="breadcrumb">'+''.join(out)+'</nav>'
for url,(name,items,related) in PAGES.items():
 f=ROOT/url.strip('/')/'index.html'; text=f.read_text(encoding='utf-8'); canonical=BASE+url
 text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',breadcrumb(items),text,count=1,flags=re.S)
 m=re.search(r'<script data-raptor-schema="v[2345]" type="application/ld\+json">(.*?)</script>',text,re.S); data=json.loads(m.group(1)); g=data['@graph']
 page=next(x for x in g if x.get('@id')==canonical+'#webpage'); page.update({"creator":{"@id":BASE+'/about/ricardo-canilao/#person'},"publisher":{"@id":BASE+'/#organization'}})
 bc=next((x for x in g if x.get('@type')=='BreadcrumbList'),None)
 if bc is None: bc={"@type":"BreadcrumbList","@id":canonical+'#breadcrumb'}; g.append(bc)
 bc['itemListElement']=[{"@type":"ListItem","position":i,"name":label,"item":BASE+(dest or url)} for i,(label,dest) in enumerate(items,1)]; page['breadcrumb']={"@id":bc['@id']}
 if url=='/insights/':
  listing={"@type":"ItemList","@id":canonical+'#categories',"name":"Raptor Insights Categories","itemListElement":[{"@type":"ListItem","position":i,"name":LABEL[x],"url":BASE+x} for i,x in enumerate(related,1)]}; g.append(listing); page['mainEntity']={"@id":listing['@id']}
 else: page['about']=[{"@id":BASE+x+('#service' if x.startswith('/services/') else '#webpage')} for x in related]
 rep='<script data-raptor-schema="v6" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'; text=text[:m.start()]+rep+text[m.end():]
 if 'insights-editorial-standard' not in text:
  links=''.join(f'<a class="button button-secondary" href="{x}">{html.escape(LABEL[x])}</a>' for x in related)
  block=f'''<section aria-labelledby="insights-editorial-title" class="section shell insights-editorial-standard"><div class="section-label">Insights // Publishing Standard</div><h2 id="insights-editorial-title">Experience first. Search intent second. Publication after verification.</h2><p>Insights begin with a real operating problem, decision, or lesson. They support the related commercial page with a narrower subject instead of competing for the same primary search intent.</p><div class="hero-actions">{links}</div></section>'''
  text=text.replace('<section class="section shell contact">',block+'<section class="section shell contact">',1)
 f.write_text(text,encoding='utf-8')
print('Finalized 4 Insights pages')
