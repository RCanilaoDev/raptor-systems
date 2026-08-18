from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
CASES={
 "/work/case-studies/specialized-accounting-search-architecture/":("Specialized Accounting Search Architecture",["/services/search-systems/search-architecture/","/services/search-systems/structured-data-schema/","/services/search-systems/local-search/","/services/search-systems/technical-seo/"]),
 "/work/case-studies/complex-local-service-search-architecture/":("Complex Local-Service Search Architecture",["/services/search-systems/search-architecture/","/services/search-systems/local-search/","/services/search-systems/structured-data-schema/"]),
 "/work/case-studies/website-infrastructure-migration/":("Website Infrastructure Migration",["/services/web-operations/website-portfolio-management/","/services/web-operations/website-migration-infrastructure/","/services/web-operations/website-performance-optimization/"]),
 "/work/case-studies/wordpress-shopify-commerce-system/":("WordPress + Shopify Commerce System",["/services/commerce-systems/","/services/commerce-systems/shopify-development/","/services/web-operations/website-development/","/services/commerce-systems/ecommerce-search-architecture/"]),
 "/work/case-studies/high-volume-website-production/":("High-Volume Website Production",["/services/web-operations/website-production-management/","/services/web-operations/website-portfolio-management/"]),
}
SYSTEMS={"/work/systems/web-production-system/":("Web Production System",["/services/web-operations/website-production-management/","/work/case-studies/high-volume-website-production/"]),"/work/systems/hqcp/":("HQCP",["/services/search-systems/technical-seo/system-audit/","/services/search-systems/technical-seo/","/work/case-studies/"])}
LABEL={u:n for u,(n,_) in CASES.items()}|{u:n for u,(n,_) in SYSTEMS.items()}|{"/services/search-systems/search-architecture/":"Search Architecture","/services/search-systems/structured-data-schema/":"Structured Data & Schema","/services/search-systems/local-search/":"Local Search","/services/search-systems/technical-seo/":"Technical SEO","/services/web-operations/website-portfolio-management/":"Portfolio Management","/services/web-operations/website-migration-infrastructure/":"Migration & Infrastructure","/services/web-operations/website-performance-optimization/":"Performance Optimization","/services/commerce-systems/":"Commerce Systems","/services/commerce-systems/shopify-development/":"Shopify Development","/services/web-operations/website-development/":"Website Development","/services/commerce-systems/ecommerce-search-architecture/":"Ecommerce Search Architecture","/services/web-operations/website-production-management/":"Production Management","/services/search-systems/technical-seo/system-audit/":"Technical SEO System Audit","/work/case-studies/":"Case Studies"}
def crumbs(items):
 out=[]
 for label,url in items:
  if out: out.append('<span aria-hidden="true">//</span>')
  out.append(f'<a href="{url}">{html.escape(label)}</a>' if url else f'<span>{html.escape(label)}</span>')
 return '<nav aria-label="Breadcrumb" class="breadcrumb">'+''.join(out)+'</nav>'
def schema(text,canonical,items,article=False,name=""):
 m=re.search(r'<script data-raptor-schema="v[234]" type="application/ld\+json">(.*?)</script>',text,re.S); data=json.loads(m.group(1)); graph=data['@graph']
 bc=next((x for x in graph if x.get('@type')=='BreadcrumbList'),None)
 if bc is None: bc={"@type":"BreadcrumbList","@id":canonical+'#breadcrumb'}; graph.append(bc)
 bc['itemListElement']=[{"@type":"ListItem","position":i,"name":label,"item":BASE+(dest or canonical.removeprefix(BASE))} for i,(label,dest) in enumerate(items,1)]
 page=next((x for x in graph if x.get('@id')==canonical+'#webpage'),None)
 if article:
  art=next((x for x in graph if x.get('@id')==canonical+'#article'),None)
  if art is None: art={"@type":"Article","@id":canonical+'#article'}; graph.append(art)
  art.update({"headline":name,"url":canonical,"mainEntityOfPage":{"@id":canonical+'#webpage'},"author":{"@id":BASE+'/about/ricardo-canilao/#person'},"publisher":{"@id":BASE+'/#organization'},"isPartOf":{"@id":BASE+'/work/case-studies/#webpage'},"inLanguage":"en-US"})
  if page: page['mainEntity']={"@id":canonical+'#article'}
 rep='<script data-raptor-schema="v4" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'; return text[:m.start()]+rep+text[m.end():]

for url,(name,related) in CASES.items():
 f=ROOT/url.strip('/')/'index.html'; text=f.read_text(encoding='utf-8'); canonical=BASE+url
 items=[("Home","/"),("Work","/work/"),("Case Studies","/work/case-studies/"),(name,None)]
 text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',crumbs(items),text,count=1,flags=re.S)
 text=schema(text,canonical,items,True,name)
 if 'evidence-relationships' not in text:
  links=''.join(f'<a class="button button-secondary" href="{x}">{html.escape(LABEL[x])}</a>' for x in related)
  block=f'<section aria-labelledby="evidence-relationships-title" class="section shell evidence-relationships"><div class="section-label">Evidence // Demonstrated Systems</div><h2 id="evidence-relationships-title">What this case supports.</h2><p>The links below identify the services materially demonstrated by the work. They do not turn an observed result into a broader performance guarantee.</p><div class="hero-actions">{links}</div></section>'
  text=text.replace('<section aria-labelledby="contact-title"',block+'<section aria-labelledby="contact-title"',1).replace('<section aria-labelledby="proof-contact-title"',block+'<section aria-labelledby="proof-contact-title"',1).replace('<section class="section shell contact">',block+'<section class="section shell contact">',1)
 f.write_text(text,encoding='utf-8')

for url,(name,related) in SYSTEMS.items():
 f=ROOT/url.strip('/')/'index.html'; text=f.read_text(encoding='utf-8'); canonical=BASE+url; items=[("Home","/"),("Work","/work/"),("Systems","/work/systems/"),(name,None)]
 text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',crumbs(items),text,count=1,flags=re.S); text=schema(text,canonical,items,False,name)
 if 'system-relationships' not in text:
  links=''.join(f'<a class="button button-secondary" href="{x}">{html.escape(LABEL[x])}</a>' for x in related)
  text=text.replace('<section class="section shell contact">',f'<section aria-labelledby="system-relationships-title" class="section shell system-relationships"><div class="section-label">System // Applied Through</div><h2 id="system-relationships-title">See the method in context.</h2><div class="hero-actions">{links}</div></section><section class="section shell contact">',1)
 f.write_text(text,encoding='utf-8')

for url,label,parent in [("/work/","Work",[("Home","/"),("Work",None)]),("/work/case-studies/","Case Studies",[("Home","/"),("Work","/work/"),("Case Studies",None)]),("/work/systems/","Systems",[("Home","/"),("Work","/work/"),("Systems",None)])]:
 f=ROOT/url.strip('/')/'index.html'; text=f.read_text(encoding='utf-8'); text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',crumbs(parent),text,count=1,flags=re.S); text=schema(text,BASE+url,parent,False,label)
 if url=="/work/case-studies/" and 'case-registry' not in text:
  cards=''.join(f'<article class="service-card"><h2>{html.escape(n)}</h2><p><a class="button button-secondary" href="{u}">View Case Study</a></p></article>' for u,(n,_) in CASES.items())
  text=text.replace('<section class="section shell"><div class="service-card-grid">','<section aria-labelledby="case-registry-title" class="section shell case-registry"><h2 id="case-registry-title">Five evidence records.</h2><div class="service-card-grid">'+cards,1)
 if url=="/work/" and 'all-evidence-paths' not in text:
  text=text.replace('<section aria-labelledby="proof-method-title"',f'<section class="section shell all-evidence-paths"><div class="hero-actions"><a class="button button-primary" href="/work/case-studies/">View All Five Case Studies</a><a class="button button-secondary" href="/work/systems/">Explore Operating Systems</a></div></section><section aria-labelledby="proof-method-title"',1)
 f.write_text(text,encoding='utf-8')
print("Finalized 10 Evidence and Systems pages")
