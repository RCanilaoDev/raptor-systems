from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
PAGES={
 "/services/commerce-systems/":["/","/services/","/services/commerce-systems/"],
 "/services/commerce-systems/shopify-development/":["/","/services/","/services/commerce-systems/","/services/commerce-systems/shopify-development/"],
 "/services/commerce-systems/ecommerce-search-architecture/":["/","/services/","/services/commerce-systems/","/services/commerce-systems/ecommerce-search-architecture/"],
 "/services/commerce-systems/ecommerce-technical-optimization/":["/","/services/","/services/commerce-systems/","/services/commerce-systems/ecommerce-technical-optimization/"],
 "/services/commerce-systems/product-commerce-operations/":["/","/services/","/services/commerce-systems/","/services/commerce-systems/product-commerce-operations/"],
}
RELATED={
 "/services/commerce-systems/shopify-development/":["/services/commerce-systems/ecommerce-search-architecture/","/services/commerce-systems/ecommerce-technical-optimization/","/work/case-studies/wordpress-shopify-commerce-system/"],
 "/services/commerce-systems/ecommerce-search-architecture/":["/services/search-systems/search-architecture/","/services/search-systems/structured-data-schema/","/services/commerce-systems/shopify-development/"],
 "/services/commerce-systems/ecommerce-technical-optimization/":["/services/web-operations/website-performance-optimization/","/services/commerce-systems/shopify-development/","/work/case-studies/wordpress-shopify-commerce-system/"],
 "/services/commerce-systems/product-commerce-operations/":["/services/commerce-systems/shopify-development/","/services/commerce-systems/ecommerce-search-architecture/","/work/case-studies/wordpress-shopify-commerce-system/"],
}
errors=[]
for url,expected_paths in PAGES.items():
 text=(ROOT/url.strip('/')/'index.html').read_text(encoding='utf-8'); m=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not m: errors.append(f"SCHEMA VERSION {url}"); continue
 graph=json.loads(m.group(1))['@graph']; bc=next((x for x in graph if x.get('@type')=='BreadcrumbList'),{}); actual=[x.get('item') for x in bc.get('itemListElement',[])]
 expected=[BASE+x for x in expected_paths]
 if actual!=expected: errors.append(f"BREADCRUMB {url}: {actual}")
 service=next((x for x in graph if x.get('@id')==BASE+url+'#service'),None)
 if not service or not service.get('serviceType'): errors.append(f"SERVICE {url}")
 for related in RELATED.get(url,[]):
  if f'href="{related}"' not in text: errors.append(f"RELATED {url} -> {related}")
print(f"Commerce Systems pages: {len(PAGES)}"); print(f"Errors: {len(errors)}")
for e in errors: print(e)
sys.exit(bool(errors))
