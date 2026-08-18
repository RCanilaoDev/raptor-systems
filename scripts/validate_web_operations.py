from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={
 "/services/web-operations/":["/","/services/","/services/web-operations/"],
 "/services/web-operations/website-production-management/":["/","/services/","/services/web-operations/","/services/web-operations/website-production-management/"],
 "/services/web-operations/website-portfolio-management/":["/","/services/","/services/web-operations/","/services/web-operations/website-portfolio-management/"],
 "/services/web-operations/website-development/":["/","/services/","/services/web-operations/","/services/web-operations/website-development/"],
 "/services/web-operations/website-performance-optimization/":["/","/services/","/services/web-operations/","/services/web-operations/website-performance-optimization/"],
 "/services/web-operations/website-migration-infrastructure/":["/","/services/","/services/web-operations/","/services/web-operations/website-migration-infrastructure/"],
}
RELATED={
 "/services/web-operations/website-production-management/":["/work/systems/web-production-system/","/work/case-studies/high-volume-website-production/","/services/web-operations/website-portfolio-management/"],
 "/services/web-operations/website-portfolio-management/":["/services/web-operations/website-production-management/","/services/web-operations/website-migration-infrastructure/","/work/case-studies/website-infrastructure-migration/"],
 "/services/web-operations/website-development/":["/services/web-operations/website-performance-optimization/","/services/commerce-systems/shopify-development/","/work/case-studies/wordpress-shopify-commerce-system/"],
 "/services/web-operations/website-performance-optimization/":["/services/search-systems/technical-seo/","/services/commerce-systems/ecommerce-technical-optimization/","/services/web-operations/website-development/"],
 "/services/web-operations/website-migration-infrastructure/":["/services/web-operations/website-portfolio-management/","/services/web-operations/website-performance-optimization/","/work/case-studies/website-infrastructure-migration/"],
}
errors=[]
for url,paths in PAGES.items():
 text=(ROOT/url.strip('/')/'index.html').read_text(encoding='utf-8'); m=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not m: errors.append(f"SCHEMA VERSION {url}"); continue
 graph=json.loads(m.group(1))['@graph']; bc=next((x for x in graph if x.get('@type')=='BreadcrumbList'),{}); actual=[x.get('item') for x in bc.get('itemListElement',[])]; expected=[BASE+x for x in paths]
 if actual!=expected: errors.append(f"BREADCRUMB {url}: {actual}")
 service=next((x for x in graph if x.get('@id')==BASE+url+'#service'),None)
 if not service or not service.get('serviceType'): errors.append(f"SERVICE {url}")
 for related in RELATED.get(url,[]):
  if f'href="{related}"' not in text: errors.append(f"RELATED {url} -> {related}")
print(f"Web Operations pages: {len(PAGES)}"); print(f"Errors: {len(errors)}")
for e in errors: print(e)
sys.exit(bool(errors))
