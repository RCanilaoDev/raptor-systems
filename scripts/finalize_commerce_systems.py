from pathlib import Path
import html,json,re

ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={
 "/services/commerce-systems/":("Commerce Systems",[("Home","/"),("Services","/services/"),("Commerce Systems",None)]),
 "/services/commerce-systems/shopify-development/":("Shopify Development",[("Home","/"),("Services","/services/"),("Commerce Systems","/services/commerce-systems/"),("Shopify Development",None)]),
 "/services/commerce-systems/ecommerce-search-architecture/":("Ecommerce Search Architecture",[("Home","/"),("Services","/services/"),("Commerce Systems","/services/commerce-systems/"),("Ecommerce Search Architecture",None)]),
 "/services/commerce-systems/ecommerce-technical-optimization/":("Ecommerce Technical Optimization",[("Home","/"),("Services","/services/"),("Commerce Systems","/services/commerce-systems/"),("Technical Optimization",None)]),
 "/services/commerce-systems/product-commerce-operations/":("Product & Commerce Operations",[("Home","/"),("Services","/services/"),("Commerce Systems","/services/commerce-systems/"),("Commerce Operations",None)]),
}
RELATED={
 "/services/commerce-systems/shopify-development/":["/services/commerce-systems/ecommerce-search-architecture/","/services/commerce-systems/ecommerce-technical-optimization/","/work/case-studies/wordpress-shopify-commerce-system/"],
 "/services/commerce-systems/ecommerce-search-architecture/":["/services/search-systems/search-architecture/","/services/search-systems/structured-data-schema/","/services/commerce-systems/shopify-development/"],
 "/services/commerce-systems/ecommerce-technical-optimization/":["/services/web-operations/website-performance-optimization/","/services/commerce-systems/shopify-development/","/work/case-studies/wordpress-shopify-commerce-system/"],
 "/services/commerce-systems/product-commerce-operations/":["/services/commerce-systems/shopify-development/","/services/commerce-systems/ecommerce-search-architecture/","/work/case-studies/wordpress-shopify-commerce-system/"],
}
LABELS={"/services/commerce-systems/shopify-development/":"Shopify Development","/services/commerce-systems/ecommerce-search-architecture/":"Ecommerce Search Architecture","/services/commerce-systems/ecommerce-technical-optimization/":"Technical Optimization","/services/commerce-systems/product-commerce-operations/":"Commerce Operations","/services/search-systems/search-architecture/":"Search Architecture","/services/search-systems/structured-data-schema/":"Structured Data & Schema","/services/web-operations/website-performance-optimization/":"Website Performance","/work/case-studies/wordpress-shopify-commerce-system/":"WordPress + Shopify Case Study"}
def crumb(items):
 out=[]
 for label,url in items:
  if out: out.append('<span aria-hidden="true">//</span>')
  out.append(f'<a href="{url}">{html.escape(label)}</a>' if url else f'<span>{html.escape(label)}</span>')
 return '<nav aria-label="Breadcrumb" class="breadcrumb">'+''.join(out)+'</nav>'
for url,(name,items) in PAGES.items():
 file=ROOT/url.strip('/')/'index.html'; text=file.read_text(encoding='utf-8'); canonical=BASE+url
 text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',crumb(items),text,count=1,flags=re.S)
 m=re.search(r'<script data-raptor-schema="v[23]" type="application/ld\+json">(.*?)</script>',text,re.S); data=json.loads(m.group(1)); graph=data['@graph']
 bc=next((x for x in graph if x.get('@type')=='BreadcrumbList'),None)
 if bc is None: bc={"@type":"BreadcrumbList","@id":canonical+'#breadcrumb'}; graph.append(bc)
 bc['itemListElement']=[{"@type":"ListItem","position":i,"name":label,"item":BASE+(dest or url)} for i,(label,dest) in enumerate(items,1)]
 service=next((x for x in graph if x.get('@id')==canonical+'#service'),None)
 if service:
  service.update({"serviceType":name,"category":"Ecommerce and Commerce Systems","areaServed":{"@type":"Country","name":"United States"}})
  service['isRelatedTo']=[{"@id":BASE+x+'#service'} for x in RELATED.get(url,[]) if x.startswith('/services/')]
  if url=="/services/commerce-systems/": service['hasOfferCatalog']={"@type":"OfferCatalog","name":"Commerce Systems Services","itemListElement":[{"@type":"Offer","itemOffered":{"@id":BASE+x+'#service'}} for x in PAGES if x!=url]}
 rep='<script data-raptor-schema="v3" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'; text=text[:m.start()]+rep+text[m.end():]
 if url in RELATED and 'commerce-cluster-links' not in text:
  links=''.join(f'<a class="button button-secondary" href="{x}">{html.escape(LABELS[x])}</a>' for x in RELATED[url])
  block=f'<section aria-labelledby="commerce-cluster-links-title" class="section shell commerce-cluster-links"><div class="section-label">Commerce Systems // Related Path</div><h2 id="commerce-cluster-links-title">Continue through the connected commerce system.</h2><p>Move to the closest supporting service, technical discipline, or operating evidence.</p><div class="hero-actions">{links}</div></section>'
  text=text.replace('<section aria-labelledby="contact-title"',block+'<section aria-labelledby="contact-title"',1)
 file.write_text(text,encoding='utf-8')
print(f"Finalized {len(PAGES)} Commerce Systems pages")
