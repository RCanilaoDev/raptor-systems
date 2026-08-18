from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={
 "/services/web-operations/":("Web Operations",[("Home","/"),("Services","/services/"),("Web Operations",None)]),
 "/services/web-operations/website-production-management/":("Website Production Management",[("Home","/"),("Services","/services/"),("Web Operations","/services/web-operations/"),("Production Management",None)]),
 "/services/web-operations/website-portfolio-management/":("Website Portfolio Management",[("Home","/"),("Services","/services/"),("Web Operations","/services/web-operations/"),("Portfolio Management",None)]),
 "/services/web-operations/website-development/":("Website Development",[("Home","/"),("Services","/services/"),("Web Operations","/services/web-operations/"),("Website Development",None)]),
 "/services/web-operations/website-performance-optimization/":("Website Performance Optimization",[("Home","/"),("Services","/services/"),("Web Operations","/services/web-operations/"),("Performance Optimization",None)]),
 "/services/web-operations/website-migration-infrastructure/":("Website Migration & Infrastructure",[("Home","/"),("Services","/services/"),("Web Operations","/services/web-operations/"),("Migration & Infrastructure",None)]),
}
RELATED={
 "/services/web-operations/website-production-management/":["/work/systems/web-production-system/","/work/case-studies/high-volume-website-production/","/services/web-operations/website-portfolio-management/"],
 "/services/web-operations/website-portfolio-management/":["/services/web-operations/website-production-management/","/services/web-operations/website-migration-infrastructure/","/work/case-studies/website-infrastructure-migration/"],
 "/services/web-operations/website-development/":["/services/web-operations/website-performance-optimization/","/services/commerce-systems/shopify-development/","/work/case-studies/wordpress-shopify-commerce-system/"],
 "/services/web-operations/website-performance-optimization/":["/services/search-systems/technical-seo/","/services/commerce-systems/ecommerce-technical-optimization/","/services/web-operations/website-development/"],
 "/services/web-operations/website-migration-infrastructure/":["/services/web-operations/website-portfolio-management/","/services/web-operations/website-performance-optimization/","/work/case-studies/website-infrastructure-migration/"],
}
LABELS={"/work/systems/web-production-system/":"Web Production System","/work/case-studies/high-volume-website-production/":"Production Case Study","/services/web-operations/website-production-management/":"Production Management","/services/web-operations/website-portfolio-management/":"Portfolio Management","/services/web-operations/website-development/":"Website Development","/services/web-operations/website-performance-optimization/":"Performance Optimization","/services/web-operations/website-migration-infrastructure/":"Migration & Infrastructure","/work/case-studies/website-infrastructure-migration/":"Migration Case Study","/services/commerce-systems/shopify-development/":"Shopify Development","/work/case-studies/wordpress-shopify-commerce-system/":"WordPress + Shopify Case Study","/services/search-systems/technical-seo/":"Technical SEO","/services/commerce-systems/ecommerce-technical-optimization/":"Ecommerce Technical Optimization"}
def breadcrumb(items):
 out=[]
 for label,url in items:
  if out: out.append('<span aria-hidden="true">//</span>')
  out.append(f'<a href="{url}">{html.escape(label)}</a>' if url else f'<span>{html.escape(label)}</span>')
 return '<nav aria-label="Breadcrumb" class="breadcrumb">'+''.join(out)+'</nav>'
for url,(name,items) in PAGES.items():
 file=ROOT/url.strip('/')/'index.html'; text=file.read_text(encoding='utf-8'); canonical=BASE+url
 text=re.sub(r'<nav aria-label="Breadcrumb" class="breadcrumb">.*?</nav>',breadcrumb(items),text,count=1,flags=re.S)
 m=re.search(r'<script data-raptor-schema="v[23]" type="application/ld\+json">(.*?)</script>',text,re.S); data=json.loads(m.group(1)); graph=data['@graph']
 bc=next((x for x in graph if x.get('@type')=='BreadcrumbList'),None)
 if bc is None: bc={"@type":"BreadcrumbList","@id":canonical+'#breadcrumb'}; graph.append(bc)
 bc['itemListElement']=[{"@type":"ListItem","position":i,"name":label,"item":BASE+(dest or url)} for i,(label,dest) in enumerate(items,1)]
 service=next((x for x in graph if x.get('@id')==canonical+'#service'),None)
 if service:
  service.update({"serviceType":name,"category":"Website Operations and Digital Infrastructure","areaServed":{"@type":"Country","name":"United States"}})
  service['isRelatedTo']=[{"@id":BASE+x+'#service'} for x in RELATED.get(url,[]) if x.startswith('/services/')]
  if url=="/services/web-operations/": service['hasOfferCatalog']={"@type":"OfferCatalog","name":"Web Operations Services","itemListElement":[{"@type":"Offer","itemOffered":{"@id":BASE+x+'#service'}} for x in PAGES if x!=url]}
 rep='<script data-raptor-schema="v3" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'; text=text[:m.start()]+rep+text[m.end():]
 if url in RELATED and 'webops-cluster-links' not in text:
  links=''.join(f'<a class="button button-secondary" href="{x}">{html.escape(LABELS[x])}</a>' for x in RELATED[url])
  block=f'<section aria-labelledby="webops-cluster-links-title" class="section shell webops-cluster-links"><div class="section-label">Web Operations // Related Path</div><h2 id="webops-cluster-links-title">Continue through the operating system.</h2><p>Move to the closest supporting capability, operating method, or evidence record.</p><div class="hero-actions">{links}</div></section>'
  text=text.replace('<section aria-labelledby="contact-title"',block+'<section aria-labelledby="contact-title"',1)
 file.write_text(text,encoding='utf-8')
print(f"Finalized {len(PAGES)} Web Operations pages")
