from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
CASES={
 "/work/case-studies/specialized-accounting-search-architecture/":["/services/search-systems/search-architecture/","/services/search-systems/structured-data-schema/","/services/search-systems/local-search/","/services/search-systems/technical-seo/"],
 "/work/case-studies/complex-local-service-search-architecture/":["/services/search-systems/search-architecture/","/services/search-systems/local-search/","/services/search-systems/structured-data-schema/"],
 "/work/case-studies/website-infrastructure-migration/":["/services/web-operations/website-portfolio-management/","/services/web-operations/website-migration-infrastructure/","/services/web-operations/website-performance-optimization/"],
 "/work/case-studies/wordpress-shopify-commerce-system/":["/services/commerce-systems/","/services/commerce-systems/shopify-development/","/services/web-operations/website-development/","/services/commerce-systems/ecommerce-search-architecture/"],
 "/work/case-studies/high-volume-website-production/":["/services/web-operations/website-production-management/","/services/web-operations/website-portfolio-management/"],
}
SYSTEMS=["/work/systems/web-production-system/","/work/systems/hqcp/"]; errors=[]
for url,related in CASES.items():
 text=(ROOT/url.strip('/')/'index.html').read_text(encoding='utf-8'); m=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not m: errors.append(f"SCHEMA VERSION {url}"); continue
 graph=json.loads(m.group(1))['@graph']; article=next((x for x in graph if x.get('@id')==BASE+url+'#article'),None); bc=next((x for x in graph if x.get('@type')=='BreadcrumbList'),{})
 if not article or article.get('author',{}).get('@id')!=BASE+'/about/ricardo-canilao/#person': errors.append(f"ARTICLE {url}")
 if len(bc.get('itemListElement',[]))!=4: errors.append(f"BREADCRUMB {url}")
 for dest in related:
  if f'href="{dest}"' not in text: errors.append(f"EVIDENCE LINK {url} -> {dest}")
for url in SYSTEMS:
 text=(ROOT/url.strip('/')/'index.html').read_text(encoding='utf-8')
 if 'system-relationships' not in text: errors.append(f"SYSTEM LINKS {url}")
print("Evidence and Systems pages: 10"); print(f"Errors: {len(errors)}")
for e in errors: print(e)
sys.exit(bool(errors))
