from pathlib import Path
import html, json, re

ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={
 "/services/search-systems/": ("Search Systems",[("Home","/"),("Services","/services/"),("Search Systems",None)]),
 "/services/search-systems/technical-seo/": ("Technical SEO",[("Home","/"),("Services","/services/"),("Search Systems","/services/search-systems/"),("Technical SEO",None)]),
 "/services/search-systems/technical-seo/system-audit/": ("Technical SEO System Audit",[("Home","/"),("Services","/services/"),("Search Systems","/services/search-systems/"),("Technical SEO","/services/search-systems/technical-seo/"),("System Audit",None)]),
 "/services/search-systems/search-architecture/": ("Search Architecture",[("Home","/"),("Services","/services/"),("Search Systems","/services/search-systems/"),("Search Architecture",None)]),
 "/services/search-systems/local-search/": ("Local Search",[("Home","/"),("Services","/services/"),("Search Systems","/services/search-systems/"),("Local Search",None)]),
 "/services/search-systems/structured-data-schema/": ("Structured Data & Schema",[("Home","/"),("Services","/services/"),("Search Systems","/services/search-systems/"),("Structured Data & Schema",None)]),
 "/services/search-systems/analytics-search-intelligence/": ("Analytics & Search Intelligence",[("Home","/"),("Services","/services/"),("Search Systems","/services/search-systems/"),("Search Intelligence",None)]),
}
RELATED={
 "/services/search-systems/technical-seo/": ["/services/search-systems/technical-seo/system-audit/","/services/search-systems/analytics-search-intelligence/","/work/systems/hqcp/"],
 "/services/search-systems/technical-seo/system-audit/": ["/services/search-systems/technical-seo/","/work/systems/hqcp/","/work/case-studies/"],
 "/services/search-systems/search-architecture/": ["/services/search-systems/structured-data-schema/","/work/case-studies/specialized-accounting-search-architecture/","/work/case-studies/complex-local-service-search-architecture/"],
 "/services/search-systems/local-search/": ["/services/search-systems/search-architecture/","/services/search-systems/structured-data-schema/","/work/case-studies/complex-local-service-search-architecture/"],
 "/services/search-systems/structured-data-schema/": ["/services/search-systems/search-architecture/","/work/case-studies/specialized-accounting-search-architecture/","/work/systems/hqcp/"],
 "/services/search-systems/analytics-search-intelligence/": ["/services/search-systems/technical-seo/system-audit/","/services/search-systems/technical-seo/","/work/systems/hqcp/"],
}
LABELS={"/services/search-systems/technical-seo/":"Technical SEO","/services/search-systems/technical-seo/system-audit/":"System Audit","/services/search-systems/search-architecture/":"Search Architecture","/services/search-systems/local-search/":"Local Search","/services/search-systems/structured-data-schema/":"Structured Data & Schema","/services/search-systems/analytics-search-intelligence/":"Search Intelligence","/work/systems/hqcp/":"HQCP","/work/case-studies/":"Case Studies","/work/case-studies/specialized-accounting-search-architecture/":"Accounting Case Study","/work/case-studies/complex-local-service-search-architecture/":"Local-Service Case Study"}

def visible_crumb(items):
 out=[]
 for label,url in items:
  if out: out.append('<span aria-hidden="true">//</span>')
  out.append(f'<a href="{url}">{html.escape(label)}</a>' if url else f'<span>{html.escape(label)}</span>')
 return '<nav aria-label="Breadcrumb" class="breadcrumb">'+''.join(out)+'</nav>'

for url,(name,crumbs) in PAGES.items():
 file=ROOT/url.strip("/")/"index.html"; text=file.read_text(encoding="utf-8"); canonical=BASE+url
 text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',visible_crumb(crumbs),text,count=1,flags=re.S)
 match=re.search(r'<script data-raptor-schema="v[23]" type="application/ld\+json">(.*?)</script>',text,re.S); data=json.loads(match.group(1)); graph=data['@graph']
 breadcrumb=next((x for x in graph if x.get('@type')=='BreadcrumbList'),None)
 if breadcrumb is None: breadcrumb={"@type":"BreadcrumbList","@id":canonical+"#breadcrumb"}; graph.append(breadcrumb)
 breadcrumb['itemListElement']=[{"@type":"ListItem","position":i,"name":label,"item":BASE+(dest or url)} for i,(label,dest) in enumerate(crumbs,1)]
 service=next((x for x in graph if x.get('@id')==canonical+'#service'),None)
 if service:
  service.update({"serviceType":name,"category":"Technical SEO and Search Architecture","areaServed":{"@type":"Country","name":"United States"}})
  service['isRelatedTo']=[{"@id":BASE+x+'#service'} for x in RELATED.get(url,[]) if x.startswith('/services/')]
 if url=="/services/search-systems/":
  service['hasOfferCatalog']={"@type":"OfferCatalog","name":"Search Systems Services","itemListElement":[{"@type":"Offer","itemOffered":{"@id":BASE+x+'#service'}} for x in LABELS if x.startswith('/services/search-systems/') and x.count('/')<=5]}
 replacement='<script data-raptor-schema="v3" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'; text=text[:match.start()]+replacement+text[match.end():]
 if url in RELATED and 'search-cluster-links' not in text:
  cards=''.join(f'<a class="button button-secondary" href="{x}">{html.escape(LABELS[x])}</a>' for x in RELATED[url])
  block=f'<section aria-labelledby="search-cluster-links-title" class="section shell search-cluster-links"><div class="section-label">Search Systems // Related Path</div><h2 id="search-cluster-links-title">Continue through the connected system.</h2><p>These pages provide the closest supporting method, evidence, or next diagnostic step.</p><div class="hero-actions">{cards}</div></section>'
  text=text.replace('<section aria-labelledby="contact-title"',block+'<section aria-labelledby="contact-title"',1)
 file.write_text(text,encoding="utf-8")
print(f"Finalized {len(PAGES)} Search Systems pages")
