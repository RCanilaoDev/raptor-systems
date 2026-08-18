from pathlib import Path
import json,re,sys
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

errors=[]
for url,(name,crumbs) in PAGES.items():
 text=(ROOT/url.strip("/")/"index.html").read_text(encoding="utf-8")
 match=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not match: errors.append(f"SCHEMA VERSION {url}"); continue
 graph=json.loads(match.group(1))['@graph']; crumb=next((x for x in graph if x.get('@type')=='BreadcrumbList'),{})
 expected=[BASE+(dest or url) for _,dest in crumbs]; actual=[x.get('item') for x in crumb.get('itemListElement',[])]
 if actual!=expected: errors.append(f"BREADCRUMB {url}: {actual}")
 service=next((x for x in graph if x.get('@id')==BASE+url+'#service'),None)
 if not service or not service.get('serviceType'): errors.append(f"SERVICE {url}")
 for related in RELATED.get(url,[]):
  if f'href="{related}"' not in text: errors.append(f"RELATED {url} -> {related}")
print(f"Search Systems pages: {len(PAGES)}")
print(f"Errors: {len(errors)}")
for error in errors: print(error)
sys.exit(bool(errors))
