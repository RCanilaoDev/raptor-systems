from pathlib import Path
import html, json, re, subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://raptorconsultinggroup.com"

MAPPING = {
 "search-systems.html":"/services/search-systems/", "technical-seo.html":"/services/search-systems/technical-seo/",
 "technical-seo-system-audit.html":"/services/search-systems/technical-seo/system-audit/",
 "search-architecture.html":"/services/search-systems/search-architecture/", "local-search.html":"/services/search-systems/local-search/",
 "structured-data-schema.html":"/services/search-systems/structured-data-schema/",
 "analytics-search-intelligence.html":"/services/search-systems/analytics-search-intelligence/",
 "commerce-systems.html":"/services/commerce-systems/", "shopify-development.html":"/services/commerce-systems/shopify-development/",
 "ecommerce-search-architecture.html":"/services/commerce-systems/ecommerce-search-architecture/",
 "ecommerce-technical-optimization.html":"/services/commerce-systems/ecommerce-technical-optimization/",
 "product-commerce-operations.html":"/services/commerce-systems/product-commerce-operations/",
 "web-operations.html":"/services/web-operations/", "website-production-management.html":"/services/web-operations/website-production-management/",
 "website-portfolio-management.html":"/services/web-operations/website-portfolio-management/",
 "website-development.html":"/services/web-operations/website-development/",
 "website-performance-optimization.html":"/services/web-operations/website-performance-optimization/",
 "website-migration-infrastructure.html":"/services/web-operations/website-migration-infrastructure/",
 "proof.html":"/work/", "case-study-search-structured-data.html":"/work/case-studies/specialized-accounting-search-architecture/",
 "case-study-website-migration.html":"/work/case-studies/website-infrastructure-migration/",
 "case-study-wordpress-shopify.html":"/work/case-studies/wordpress-shopify-commerce-system/",
 "about.html":"/about/", "contact.html":"/contact/",
}

NAV = '''<nav aria-label="Primary navigation" class="primary-nav" id="primary-nav">
<details class="nav-services"><summary>Services</summary><div class="services-menu"><div><b>Search Systems</b><a href="/services/search-systems/">Overview</a><a href="/services/search-systems/technical-seo/">Technical SEO</a><a href="/services/search-systems/technical-seo/system-audit/">System Audit</a><a href="/services/search-systems/search-architecture/">Search Architecture</a><a href="/services/search-systems/local-search/">Local Search</a><a href="/services/search-systems/structured-data-schema/">Structured Data</a><a href="/services/search-systems/analytics-search-intelligence/">Search Intelligence</a></div><div><b>Commerce Systems</b><a href="/services/commerce-systems/">Overview</a><a href="/services/commerce-systems/shopify-development/">Shopify Development</a><a href="/services/commerce-systems/ecommerce-search-architecture/">Ecommerce Search</a><a href="/services/commerce-systems/ecommerce-technical-optimization/">Technical Optimization</a><a href="/services/commerce-systems/product-commerce-operations/">Commerce Operations</a></div><div><b>Web Operations</b><a href="/services/web-operations/">Overview</a><a href="/services/web-operations/website-production-management/">Production Management</a><a href="/services/web-operations/website-portfolio-management/">Portfolio Management</a><a href="/services/web-operations/website-development/">Development</a><a href="/services/web-operations/website-performance-optimization/">Performance</a><a href="/services/web-operations/website-migration-infrastructure/">Migration</a></div></div></details><a href="/work/">Work</a><a href="/work/systems/">Systems</a><a href="/about/">About</a><a href="/insights/">Insights</a><a href="/contact/">Contact</a><a aria-label="Call Raptor" class="nav-cta" data-contact-action="call" href="#">Call Raptor</a>
</nav>'''

def transform(text, destination):
    for old, new in sorted(MAPPING.items(), key=lambda x: -len(x[0])):
        text = text.replace(f'"{old}', f'"{new}').replace(f"'{old}", f"'{new}")
        text = text.replace(f'{BASE}/{old}', f'{BASE}{new}')
    text = text.replace('href="index.html"', 'href="/"').replace('href="#top"', 'href="/#top"')
    text = re.sub(r'(href|src)="(styles\.css|script\.js|favicon\.ico|assets/)', lambda m: f'{m.group(1)}="/{m.group(2)}', text)
    text = re.sub(r'<nav aria-label="Primary navigation" class="primary-nav" id="primary-nav">.*?</nav>', NAV, text, flags=re.S)
    text = re.sub(r'<link href="https://raptorconsultinggroup\.com/[^"]*" rel="canonical"/>', f'<link href="{BASE}{destination}" rel="canonical"/>', text, count=1)
    return text

def committed(name):
    return subprocess.check_output(["git","show",f"HEAD:{name}"],cwd=ROOT,text=True)

for old, destination in MAPPING.items():
    target = ROOT / destination.strip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(transform(committed(old), destination), encoding="utf-8")

home = committed("index.html")
(ROOT / "index.html").write_text(transform(home, "/"), encoding="utf-8")

def page(url, title, description, eyebrow, heading, lead, sections, schema_type="WebPage"):
    canonical = BASE + url
    section_html = "".join(f'<article class="service-card"><h2>{html.escape(h)}</h2><p>{html.escape(p)}</p></article>' for h,p in sections)
    graph = {"@context":"https://schema.org","@graph":[
      {"@type":"Organization","@id":BASE+"/#organization","name":"Raptor Consulting Group","url":BASE+"/"},
      {"@type":schema_type,"@id":canonical+"#webpage","url":canonical,"name":title,"description":description,"isPartOf":{"@id":BASE+"/#website"},"about":{"@id":BASE+"/#organization"}}
    ]}
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/><title>{html.escape(title)}</title><meta content="{html.escape(description)}" name="description"/><meta content="#1A75C7" name="theme-color"/><link href="/styles.css" rel="stylesheet"/><link href="{canonical}" rel="canonical"/><script type="application/ld+json">{json.dumps(graph,separators=(',',':'))}</script><link href="/favicon.ico?v=15.60" rel="icon" sizes="any"/></head><body><a class="skip-link" href="#main-content">Skip to content</a><div class="site-frame"><header class="site-header" id="top"><div class="utility-bar shell"><div class="status"><span aria-hidden="true" class="status-dot"></span> Raptor Systems // Operational</div><div class="utility-label">Technical SEO &amp; Search // Commerce // Web Operations</div></div><div class="nav-shell shell"><a aria-label="Raptor Consulting Group home" class="brand" href="/"><img alt="Raptor Consulting Group" height="106" src="/assets/raptor-consulting-logo-img-header.webp" width="378"/></a><button aria-controls="primary-nav" aria-expanded="false" class="menu-toggle" type="button"><span>Menu</span></button>{NAV}</div></header><main id="main-content"><section class="service-hero section shell"><div class="eyebrow">{html.escape(eyebrow)}</div><h1>{html.escape(heading)}</h1><p class="service-hero-lede">{html.escape(lead)}</p></section><div class="divider shell"></div><section class="section shell"><div class="service-card-grid">{section_html}</div></section><section class="section shell contact"><div class="contact-panel"><div><div class="section-label">Start a Conversation</div><h2>Discuss the system with Raptor.</h2><p>Call or email Raptor directly. No intake form required.</p></div><div class="contact-actions"><a class="button button-primary" data-contact-action="call" href="#">Call Raptor</a><a class="button button-secondary" href="mailto:raptorsystems.ai@gmail.com">Email Raptor</a></div></div></section></main><footer class="site-footer"><div class="shell footer-bottom"><div>© 2026 Raptor Consulting Group</div><a href="/privacy-policy/">Privacy</a><a href="/terms/">Terms</a><a href="#top">Return to top ↑</a></div></footer></div><script src="/script.js"></script></body></html>'''

NEW = {
 "/services/": ("Digital Consulting Services | Raptor Consulting Group","Technical SEO and search architecture supported by commerce systems and web operations.","Services // System Architecture","Three connected systems. One operating view.","Raptor organizes its work around the systems that affect search, commerce, and website operations.",[("Search Systems","Technical SEO, search architecture, local search, structured data, and measurement."),("Commerce Systems","Shopify development, ecommerce search architecture, technical optimization, and product operations."),("Web Operations","Production, portfolio management, development, performance, migration, and infrastructure.")],"CollectionPage"),
 "/work/case-studies/": ("Case Studies | Raptor Consulting Group","Firsthand operating evidence across search, commerce, and web operations.","Work // Case Studies","Show the work. Label the evidence.","Each case separates context, role, decisions, implementation, and observed outcomes.",[("Search Architecture","Business understanding translated into clearer service structure and machine-readable context."),("Commerce Architecture","WordPress and Shopify connected around different technical requirements."),("Web Operations","Large-scale migrations and production systems managed through controlled operating records.")],"CollectionPage"),
 "/work/systems/": ("Operating Systems | Raptor Consulting Group","Raptor operating systems for production control and human verification.","Work // Systems","Methods that control how the work moves.","Systems explain how Raptor makes decisions, verifies findings, and moves work into production.",[("Web Production System","Intake, discovery, production, quality control, deployment, and post-launch monitoring."),("HQCP","A documented verification protocol built on the rule that detection is not diagnosis.")],"CollectionPage"),
 "/work/systems/web-production-system/": ("Web Production System | Raptor","A controlled website production workflow from intake through post-launch verification.","Systems // Web Production","Move website work through a controlled production lifecycle.","The production system gives each request a defined state, owner, review path, and verification step.",[("Intake and Discovery","Define the request, business context, access, dependencies, and acceptance conditions."),("Production and QC","Build, inspect, correct, and prepare the work for client review."),("Deployment and Monitoring","Launch carefully, connect search and analytics, then verify the production result.")],"WebPage"),
 "/work/systems/hqcp/": ("HQCP | Human Quality Control Protocol | Raptor","Raptor's Human Quality Control Protocol for verified technical findings.","Systems // HQCP","Detection is not diagnosis.","Automated tools can detect a condition. HQCP determines whether it is real, important, and ready for action.",[("V0 to V2","Detect the potential issue, inspect it, and reproduce the condition directly."),("V3 to V4","Corroborate through an independent source, then verify the evidence and business context."),("Decision","Prioritize, sequence, implement, and measure only after the finding can support action.")],"WebPage"),
 "/about/ricardo-canilao/": ("Ricardo Canilao | Founder of Raptor Consulting Group","Professional profile for Ricardo Canilao, founder of Raptor Consulting Group.","Personnel // Founder","Ricardo Canilao","Technical SEO, web operations, ecommerce systems, production management, and digital infrastructure informed by firsthand operating experience.",[("Technical SEO","Diagnosis, search architecture, structured data, analytics, and implementation."),("Web Operations","High-volume production, multi-site management, migrations, hosting, and QA."),("Ecommerce","Shopify development, product operations, merchant systems, and ongoing store work.")],"ProfilePage"),
 "/insights/": ("Technical Insights | Raptor Consulting Group","Firsthand insights about search, commerce, and web operations.","Insights // Field Notes","Technical lessons from real operating work.","Raptor Insights documents problems, decisions, and lessons grounded in firsthand professional experience.",[("Search","Technical SEO, structured data, local search, and information architecture."),("Commerce","Shopify, catalog structure, ecommerce search, and technical store operations."),("Web Operations","Production systems, website portfolios, performance, migrations, and infrastructure.")],"CollectionPage"),
 "/insights/search/": ("Search Insights | Raptor","Technical SEO and search architecture insights from Raptor Consulting Group.","Insights // Search","Search systems explained through real technical problems.","Articles in this collection will focus on diagnosis, indexation, performance, structured data, and search architecture.",[("Diagnosis","Why a crawler warning must be inspected before it becomes a recommendation."),("Structure","Why business understanding comes before content, entities, and structured data."),("Measurement","How Search Console, analytics, and direct inspection support technical decisions.")],"CollectionPage"),
 "/insights/commerce/": ("Commerce Insights | Raptor","Ecommerce systems and Shopify technical insights from Raptor Consulting Group.","Insights // Commerce","Commerce systems beyond the storefront.","This collection covers product structure, Shopify implementation, ecommerce search, measurement, and operating work.",[("Store Architecture","Connect products, collections, content, navigation, and search intent."),("Platform Decisions","Choose technology based on business and operational requirements."),("Operations","Keep product information, merchandising, measurement, and storefront behavior accurate.")],"CollectionPage"),
 "/insights/web-operations/": ("Web Operations Insights | Raptor","Website production, performance, migration, and infrastructure insights.","Insights // Web Operations","What operating websites at scale teaches you.","This collection documents production systems, portfolio control, performance, migration, and infrastructure lessons.",[("Production","Control intake, QA, launch, and post-production rather than relying on memory."),("Portfolios","Inventory and prioritize multiple websites as one operating environment."),("Infrastructure","Evaluate hosting and migration decisions against real requirements and costs.")],"CollectionPage"),
 "/privacy-policy/": ("Privacy Policy | Raptor Consulting Group","Privacy information for the Raptor Consulting Group website.","Company // Privacy","Privacy Policy","Raptor limits website data collection to the systems needed to operate, measure, and improve the site.",[("Information Collected","The site may collect standard analytics, device, browser, and interaction information through configured measurement tools."),("How Information Is Used","Information supports website operation, measurement, security, and responses to direct inquiries."),("Contact","Privacy questions may be sent to raptorsystems.ai@gmail.com.")],"WebPage"),
 "/terms/": ("Website Terms | Raptor Consulting Group","Terms governing use of the Raptor Consulting Group website.","Company // Terms","Website Terms","These terms apply to use of the public Raptor Consulting Group website and its informational content.",[("Informational Content","Website content does not create a consulting engagement or guarantee a particular search or business outcome."),("Intellectual Property","Raptor branding, original content, diagrams, and operating methods may not be republished without permission."),("External Systems","Third-party platforms and links remain subject to their own availability, policies, and terms.")],"WebPage"),
}

for url, args in NEW.items():
    target = ROOT / url.strip("/") / "index.html"; target.parent.mkdir(parents=True, exist_ok=True); target.write_text(page(url,*args),encoding="utf-8")

# Two complete evidence pages added from the approved operating record.
for url,title,lead,items in [
 ("/work/case-studies/complex-local-service-search-architecture/","Complex Local-Service Search Architecture","A combined property-management and cleaning business needed its unusual service model translated into a structure customers and search systems could understand.",[("Context","The business combined service lines that generic website templates failed to explain accurately."),("Work","Business discovery, customer-language analysis, service relationships, content structure, headings, metadata, and structured-data planning."),("Evidence boundary","The case demonstrates the operating method and delivered architecture. It does not claim unmeasured ranking or revenue outcomes.")]),
 ("/work/case-studies/high-volume-website-production/","High-Volume Website Production","A production environment moving roughly 30 websites per week required intake control, two quality checks, client review, launch coordination, and escalation handling.",[("Context","High project volume created dependencies across clients, production resources, domains, infrastructure, and launch schedules."),("Role","Directly handled higher-touch ecommerce and special projects while supporting production escalation and quality control."),("Operating lesson","A visible production record, clear states, defined ownership, and post-launch checks reduce preventable delivery failures.")])]:
    target=ROOT/url.strip("/")/"index.html"; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(page(url,f"{title} | Raptor",lead,"Work // Case Study",title,lead,items,"Article"),encoding="utf-8")

# Old paths remain as temporary GitHub Pages redirect documents.
redirect_template='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url={dest}"><link rel="canonical" href="{absolute}"><title>Page moved | Raptor Consulting Group</title><script>location.replace({js});</script></head><body><p>This page moved to <a href="{dest}">{dest}</a>.</p></body></html>'''
for old,dest in MAPPING.items():
    (ROOT/old).write_text(redirect_template.format(dest=dest,absolute=BASE+dest,js=json.dumps(dest)),encoding="utf-8")
(ROOT/"raptor-coming-soon.html").unlink(missing_ok=True)

urls=["/"]+list(MAPPING.values())+list(NEW.keys())+["/work/case-studies/complex-local-service-search-architecture/","/work/case-studies/high-volume-website-production/"]
urls=list(dict.fromkeys(urls))
(ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{BASE}{u}</loc></url>\n' for u in urls)+'</urlset>\n',encoding="utf-8")
print(f"Built {len(urls)} canonical pages and {len(MAPPING)} redirect documents")
