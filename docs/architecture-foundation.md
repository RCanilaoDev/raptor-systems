# Raptor Website Architecture Foundation

Status: Proposed for approval  
Authority: Raptor Website Sitemap Phase 01, latest decisions supersede earlier decisions  
Implementation model: Static GitHub Pages using nested directories with `index.html`

## Governing Rules

- The approved nested architecture replaces the current flat `.html` architecture.
- Search Systems is the primary commercial discipline.
- Web Operations and Commerce Systems are supporting capabilities.
- Every indexable page has one defined purpose and one primary search-intent owner.
- Every child page links to its parent hub and relevant sibling, evidence, system, and Insight pages.
- Visible breadcrumbs and `BreadcrumbList` JSON-LD use the same hierarchy.
- Final JSON-LD describes visible, verified page content and uses persistent entity IDs.
- HQCP follows: Detect, Inspect, Reproduce, Corroborate, Verify.
- No doorway pages, cloned city pages, invented outcomes, unsupported expertise, or ranking guarantees.
- The preferred homepage URL is `/`; internal links must not use `/index.html`.

## Primary Navigation

1. Services
2. Work
3. Systems
4. About
5. Insights
6. Contact

The Services control opens the three-system architecture. Search Systems appears first and receives the strongest visual and internal-link emphasis.

## Approved URL Registry

| ID | Approved URL | Parent | Page role | Primary schema |
|---|---|---|---|---|
| CORE-001 | `/` | None | Company, positioning, proof, and primary conversion | `WebPage`, `Organization`, `WebSite` |
| CORE-002 | `/services/` | `/` | Complete services and systems hub | `CollectionPage`, `ItemList` |
| CORE-003 | `/work/` | `/` | Evidence and operating work hub | `CollectionPage`, `ItemList` |
| CORE-004 | `/about/` | `/` | Company identity and operating philosophy | `AboutPage` |
| CORE-005 | `/about/ricardo-canilao/` | `/about/` | Founder and professional authority profile | `ProfilePage`, `Person` |
| CORE-006 | `/insights/` | `/` | Firsthand technical publishing hub | `CollectionPage`, `ItemList` |
| CORE-007 | `/contact/` | `/` | Direct call and email conversion | `ContactPage` |
| CORE-008 | `/privacy-policy/` | `/` | Privacy disclosure | `WebPage` |
| CORE-009 | `/terms/` | `/` | Website terms | `WebPage` |
| SRCH-001 | `/services/search-systems/` | `/services/` | Search Systems hub | `Service`, `WebPage` |
| SRCH-002 | `/services/search-systems/technical-seo/` | `SRCH-001` | Broad Technical SEO service owner | `Service`, `WebPage` |
| SRCH-003 | `/services/search-systems/technical-seo/system-audit/` | `SRCH-002` | Defined audit and diagnostic engagement | `Service`, `WebPage` |
| SRCH-004 | `/services/search-systems/search-architecture/` | `SRCH-001` | Search architecture and intent alignment | `Service`, `WebPage` |
| SRCH-005 | `/services/search-systems/local-search/` | `SRCH-001` | Local search and website/GBP alignment | `Service`, `WebPage` |
| SRCH-006 | `/services/search-systems/structured-data-schema/` | `SRCH-001` | Entity and structured-data services | `Service`, `WebPage` |
| SRCH-007 | `/services/search-systems/analytics-search-intelligence/` | `SRCH-001` | GSC, GA4, GTM, indexation, and reporting | `Service`, `WebPage` |
| COMM-001 | `/services/commerce-systems/` | `/services/` | Commerce Systems hub | `Service`, `WebPage` |
| COMM-002 | `/services/commerce-systems/shopify-development/` | `COMM-001` | Shopify development and configuration | `Service`, `WebPage` |
| COMM-003 | `/services/commerce-systems/ecommerce-search-architecture/` | `COMM-001` | Ecommerce SEO and catalog relationships | `Service`, `WebPage` |
| COMM-004 | `/services/commerce-systems/ecommerce-technical-optimization/` | `COMM-001` | Storefront technical health and performance | `Service`, `WebPage` |
| COMM-005 | `/services/commerce-systems/product-commerce-operations/` | `COMM-001` | Product, catalog, and commerce operations | `Service`, `WebPage` |
| WEB-001 | `/services/web-operations/` | `/services/` | Web Operations hub | `Service`, `WebPage` |
| WEB-002 | `/services/web-operations/website-production-management/` | `WEB-001` | Website production lifecycle management | `Service`, `WebPage` |
| WEB-003 | `/services/web-operations/website-portfolio-management/` | `WEB-001` | Multi-site inventory and governance | `Service`, `WebPage` |
| WEB-004 | `/services/web-operations/website-development/` | `WEB-001` | Website development | `Service`, `WebPage` |
| WEB-005 | `/services/web-operations/website-performance-optimization/` | `WEB-001` | Performance and Core Web Vitals | `Service`, `WebPage` |
| WEB-006 | `/services/web-operations/website-migration-infrastructure/` | `WEB-001` | Migration, hosting, DNS, and infrastructure | `Service`, `WebPage` |
| CASE-000 | `/work/case-studies/` | `/work/` | Case-study collection | `CollectionPage`, `ItemList` |
| CASE-001 | `/work/case-studies/specialized-accounting-search-architecture/` | `CASE-000` | Verified accounting search-architecture evidence | `Article`, `WebPage` |
| CASE-002 | `/work/case-studies/complex-local-service-search-architecture/` | `CASE-000` | Local-service information-architecture evidence | `Article`, `WebPage` |
| CASE-003 | `/work/case-studies/website-infrastructure-migration/` | `CASE-000` | Multi-thousand-site migration evidence | `Article`, `WebPage` |
| CASE-004 | `/work/case-studies/wordpress-shopify-commerce-system/` | `CASE-000` | Hybrid WordPress and Shopify evidence | `Article`, `WebPage` |
| CASE-005 | `/work/case-studies/high-volume-website-production/` | `CASE-000` | Website production operations evidence | `Article`, `WebPage` |
| SYS-000 | `/work/systems/` | `/work/` | Raptor operating-systems hub | `CollectionPage`, `ItemList` |
| SYS-001 | `/work/systems/web-production-system/` | `SYS-000` | Production operating workflow | `WebPage` |
| SYS-002 | `/work/systems/hqcp/` | `SYS-000` | Human Quality Control Protocol | `WebPage` |
| INS-001 | `/insights/search/` | `/insights/` | Search Insights collection | `CollectionPage` |
| INS-002 | `/insights/commerce/` | `/insights/` | Commerce Insights collection | `CollectionPage` |
| INS-003 | `/insights/web-operations/` | `/insights/` | Web Operations Insights collection | `CollectionPage` |

Total approved launch URLs: 39.

## Current-to-Approved URL Map

| Current URL | Approved destination | Migration treatment |
|---|---|---|
| `/index.html` | `/` | Update all internal links; redirect stub if retained |
| `/search-systems.html` | `/services/search-systems/` | Move existing content; redirect stub |
| `/technical-seo.html` | `/services/search-systems/technical-seo/` | Move existing content; redirect stub |
| `/technical-seo-system-audit.html` | `/services/search-systems/technical-seo/system-audit/` | Move existing content; redirect stub |
| `/search-architecture.html` | `/services/search-systems/search-architecture/` | Move existing content; redirect stub |
| `/local-search.html` | `/services/search-systems/local-search/` | Move existing content; redirect stub |
| `/structured-data-schema.html` | `/services/search-systems/structured-data-schema/` | Move existing content; redirect stub |
| `/analytics-search-intelligence.html` | `/services/search-systems/analytics-search-intelligence/` | Move existing content; redirect stub |
| `/commerce-systems.html` | `/services/commerce-systems/` | Move existing content; redirect stub |
| `/shopify-development.html` | `/services/commerce-systems/shopify-development/` | Move existing content; redirect stub |
| `/ecommerce-search-architecture.html` | `/services/commerce-systems/ecommerce-search-architecture/` | Move existing content; redirect stub |
| `/ecommerce-technical-optimization.html` | `/services/commerce-systems/ecommerce-technical-optimization/` | Move existing content; redirect stub |
| `/product-commerce-operations.html` | `/services/commerce-systems/product-commerce-operations/` | Move existing content; redirect stub |
| `/web-operations.html` | `/services/web-operations/` | Move existing content; redirect stub |
| `/website-production-management.html` | `/services/web-operations/website-production-management/` | Move existing content; redirect stub |
| `/website-portfolio-management.html` | `/services/web-operations/website-portfolio-management/` | Move existing content; redirect stub |
| `/website-development.html` | `/services/web-operations/website-development/` | Move existing content; redirect stub |
| `/website-performance-optimization.html` | `/services/web-operations/website-performance-optimization/` | Move existing content; redirect stub |
| `/website-migration-infrastructure.html` | `/services/web-operations/website-migration-infrastructure/` | Move existing content; redirect stub |
| `/proof.html` | `/work/` | Rebuild as Work hub; redirect stub |
| `/case-study-search-structured-data.html` | `/work/case-studies/specialized-accounting-search-architecture/` | Move and realign existing case; redirect stub |
| `/case-study-website-migration.html` | `/work/case-studies/website-infrastructure-migration/` | Move and realign existing case; redirect stub |
| `/case-study-wordpress-shopify.html` | `/work/case-studies/wordpress-shopify-commerce-system/` | Move and realign existing case; redirect stub |
| `/about.html` | `/about/` | Separate company content from founder profile; redirect stub |
| `/contact.html` | `/contact/` | Move existing content; redirect stub |
| `/raptor-coming-soon.html` | None | Remove from the public build and all references |

## GitHub Pages Redirect Constraint

GitHub Pages does not provide project-controlled server-side rewrite rules for this static deployment. The repository therefore cannot guarantee true HTTP 301 responses for the old `.html` URLs.

Recommended launch treatment for this young site:

1. Build all approved URLs as nested directories with `index.html`.
2. Update all internal links, canonicals, schema IDs, breadcrumbs, and sitemap entries to the approved URLs.
3. Keep each old `.html` file temporarily as a minimal redirect document containing:
   - canonical pointing to the approved destination;
   - `noindex,follow`;
   - immediate meta refresh;
   - JavaScript `location.replace` enhancement;
   - visible fallback link.
4. Exclude old redirect documents from the XML sitemap.
5. If true 301 control becomes important, place Cloudflare, Netlify, Vercel, or another redirect-capable edge/host in front of the static build.

## Breadcrumb Registry

The breadcrumb is derived from the registry rather than written independently on each page.

- Service example: Home > Services > Search Systems > Technical SEO > System Audit
- Case example: Home > Work > Case Studies > Specialized Accounting Search Architecture
- System example: Home > Work > Systems > HQCP
- Founder example: Home > About > Ricardo Canilao
- Insight category example: Home > Insights > Search

## Internal-Link Rules

Every service child page links to:

- its parent system hub;
- at least one genuinely related sibling service;
- its most relevant case study when evidence exists;
- HQCP or the Web Production System when the operating method is relevant;
- the Technical SEO System Audit when diagnosis is the appropriate next step;
- a contextual Contact action.

Every case study links to:

- the Case Studies hub;
- every service materially demonstrated by the case;
- the relevant system or methodology;
- Ricardo's profile where authorship or direct role is discussed;
- a contextual Contact action.

Insights pages and future articles must not compete with commercial service pages for the same primary intent. They support the service owner through narrower problem-based subjects and contextual links.

## Persistent Entity IDs

- Organization: `https://raptorconsultinggroup.com/#organization`
- WebSite: `https://raptorconsultinggroup.com/#website`
- Logo: `https://raptorconsultinggroup.com/#logo`
- Person: `https://raptorconsultinggroup.com/about/ricardo-canilao/#person`
- Each page: `{canonical-url}#webpage`
- Each service: `{canonical-url}#service`
- Each breadcrumb: `{canonical-url}#breadcrumb`
- Each case study or Insight article: `{canonical-url}#article`

## Content Disposition

### Reuse and realign

- Homepage
- Three system hubs
- Fourteen current child service pages
- Technical SEO System Audit
- Contact
- Three current case studies
- Most company-level About content

### New pages or materially new content

- Services hub
- Work hub realignment and Case Studies hub
- Systems hub
- Web Production System
- Dedicated HQCP page
- Ricardo Canilao profile
- Complex Local-Service Search Architecture case study
- High-Volume Website Production case study
- Insights hub and three category pages
- Privacy Policy
- Terms

## Module 01 Acceptance Criteria

- All 39 approved URLs are represented.
- Every page has a single parent except the homepage.
- Current URLs have explicit dispositions.
- Navigation, breadcrumbs, internal linking, and entity IDs share the same hierarchy.
- Search Systems retains primary prominence.
- Current verified content is preserved for reuse.
- No implementation begins until this registry is approved.
