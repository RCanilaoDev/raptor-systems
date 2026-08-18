# Raptor Website Build 14

## Build 16.00 architecture realignment

- Rebuilt the public site around the approved 39-URL nested architecture.
- Moved Search, Commerce, and Web Operations beneath `/services/`.
- Moved evidence and operating methods beneath `/work/`.
- Added Services, Case Studies, Systems, HQCP, Web Production System, founder, Insights, privacy, and terms pages.
- Added a nested Services menu to the primary navigation.
- Updated canonicals, internal links, schema URLs, breadcrumbs, and the XML sitemap.
- Converted the former flat `.html` pages into temporary `noindex,follow` redirect documents for GitHub Pages.
- Added repeatable migration and architecture-validation scripts.

## Build 16.01 global technical foundation

- Standardized `index,follow,max-image-preview:large` directives on all 39 canonical pages.
- Added Open Graph and Twitter card metadata with canonical page URLs.
- Normalized the full favicon set and cache version.
- Standardized Google Tag Manager head and noscript placement.
- Connected every page to persistent Organization and WebSite entity IDs.
- Added the founder and Orange County relationships to the Organization entity.
- Added a branded, non-indexable `404.html` page.
- Expanded validation to enforce metadata, social cards, GTM, entity references, H1s, canonicals, and internal-link integrity.

## Build 16.02 Search Systems cluster

- Finalized the seven-page Search Systems cluster and preserved clear keyword ownership.
- Added the complete Services > Search Systems breadcrumb hierarchy to visible navigation and JSON-LD.
- Kept the Technical SEO System Audit as a child of the broader Technical SEO service.
- Added service categories, national service-area context, related-service entities, and a Search Systems offer catalog.
- Connected Technical SEO, Search Architecture, Local Search, Structured Data, Search Intelligence, HQCP, and relevant case-study evidence through deliberate contextual links.
- Added a dedicated Search Systems cluster validator.

## Build 16.03 Commerce Systems cluster

- Finalized the Commerce Systems hub and four child services.
- Added the complete Services > Commerce Systems breadcrumb hierarchy to visible navigation and JSON-LD.
- Preserved separate ownership for Shopify Development, Ecommerce Search Architecture, Ecommerce Technical Optimization, and Product & Commerce Operations.
- Added commerce service categories, national service-area context, related-service entities, and a Commerce Systems offer catalog.
- Connected commerce services to Search Architecture, Structured Data, Website Performance, and the WordPress + Shopify case study where those relationships are operationally relevant.
- Added a dedicated Commerce Systems cluster validator.

## Build 16.04 Web Operations cluster

- Finalized the Web Operations hub and five child services.
- Added the complete Services > Web Operations breadcrumb hierarchy to visible navigation and JSON-LD.
- Preserved separate ownership for Production Management, Portfolio Management, Website Development, Performance Optimization, and Migration & Infrastructure.
- Added Web Operations service categories, national service-area context, related-service entities, and a Web Operations offer catalog.
- Connected services to the Web Production System, high-volume production case, infrastructure migration case, WordPress + Shopify case, Technical SEO, and Commerce Systems where those relationships are supported by the work.
- Added a dedicated Web Operations cluster validator.

## Build 16.05 Evidence and Systems

- Finalized the Work hub, Case Studies hub, five case studies, Systems hub, Web Production System, and HQCP.
- Added complete Work > Case Studies and Work > Systems breadcrumb hierarchies to visible navigation and JSON-LD.
- Standardized each case study as an Article entity with Ricardo Canilao as author and Raptor Consulting Group as publisher.
- Connected each evidence record only to the services materially demonstrated by the work.
- Expanded the Work and Case Studies hubs to expose all five approved evidence records.
- Connected the Web Production System and HQCP to their relevant services and evidence.
- Added a dedicated Evidence and Systems validator.

## Build 16.06 Company and Founder

- Separated Raptor's company identity from Ricardo Canilao's professional profile.
- Added complete About, Founder, and Contact breadcrumb hierarchies.
- Added a persistent Person entity with Organization founder and works-for relationships.
- Added Orange County location context and verified professional disciplines.
- Connected experience statements to Search, Migration, Production, Commerce, HQCP, and System Audit evidence.
- Preserved direct call, text, and email paths without exposing the phone number in HTML.
- Omitted a résumé download action until an actual résumé file is provided.
- Added a dedicated Company and Founder validator.

## Build 16.07 Insights architecture

- Finalized the Insights hub plus Search, Commerce, and Web Operations categories.
- Added complete category breadcrumb hierarchies to visible navigation and JSON-LD.
- Connected Ricardo Canilao as creator and Raptor Consulting Group as publisher.
- Connected each category to its supporting service, operating method, and evidence.
- Defined the boundary between informational article intent and commercial service-page intent.
- Added a governed article specification covering publication gates, required content, URL patterns, schema, authorship, and verification.
- Added a dedicated Insights validator.

## Build 16.08 unified entity graph

- Reconciled JSON-LD across all 39 canonical pages as one connected graph.
- Standardized Organization and WebSite definitions across every page.
- Kept the complete Ricardo Canilao Person definition on the founder ProfilePage and referenced it elsewhere through one persistent ID.
- Normalized page, service, article, breadcrumb, author, publisher, provider, founder, offer-catalog, and related-service relationships.
- Removed conflicting duplicate entity definitions and checked every internal `@id` reference.
- Generated machine-readable and human-readable entity graph registries.
- Added a dedicated whole-site entity graph validator.

## Build 16.09 responsive, accessibility, and interaction QA

- Audited all 39 canonical pages for language, main landmarks, H1 count, heading order, duplicate IDs, image alternatives, navigation labels, ARIA references, skip links, and positive tabindex use.
- Verified responsive breakpoints, reduced-motion handling, focus-visible treatments, and mobile navigation rules in the shared CSS.
- Corrected the Services disclosure so it closes on outside click, Escape, and mobile-menu close.
- Preserved focus return to the mobile menu toggle after Escape.
- Verified that phone actions remain runtime-generated and are not exposed as `tel:` or `sms:` values in HTML.
- Added repeatable accessibility/interaction validation and a Playwright visual-QA harness for an environment with an installed browser executable.

Build 14 adds the proof and case-study layer.

## New pages
- `proof.html`
- `case-study-search-structured-data.html`
- `case-study-wordpress-shopify.html`
- `case-study-website-migration.html`

## Site-wide changes
- Added `Proof` to the primary navigation.
- Added a proof teaser to the homepage.
- Added an earlier navigation collapse breakpoint so the expanded primary nav stays readable.
- Case studies are explicitly labeled as prior professional operating experience where appropriate.
- No invented ROI, ranking lifts, conversion percentages, or client names were added.

## Contact
- Phone: Call or text Raptor
- Email: raptorsystems.ai@gmail.com

## Logo
Place the approved Raptor logo at:
`assets/raptor-consulting-logo-img-stg.webp`


## Build 14.1 layout correction
- Standardized the Proof hub and all three case-study pages to one page rail.
- Standardized section headers to the established Raptor heading grid.
- Standardized narrative/result/evidence sections to the same `.82 / 1.18` split used by corrected About modules.
- Normalized bottom CTA panels and action alignment.
- Applied matching tablet/mobile collapse rules.
- No case-study content or evidence claims were changed.

## Build 15 footer system
- Replaced the minimal footer across the full site with a restrained global footer.
- Added Systems and Company navigation groups.
- Added direct phone and email access.
- Added a large centered Raptor logo treatment on Homepage and Contact only.
- Footer logo uses the approved asset path and retains a text fallback if the image is not yet present.
- No privacy/legal links were invented because those pages do not yet exist.

## Build 15.1 footer active states
- Exact footer destinations use `aria-current="page"` and a cyan active indicator.
- Child service pages highlight their parent system with `aria-current="location"`.
- Case-study pages highlight Proof contextually.
- Homepage remains neutral because Home is represented by the footer logo rather than a footer navigation link.

## Build 15.2 Commerce hero refinement
- Changed the Commerce Systems hero stack from centered/inset layers to a left-stepping diagonal path.
- Each successive system layer shifts farther left.
- Connector arrows follow the diagonal path.
- Added a very faint vertical interface trace in the newly exposed right-side negative space.
- Reduced the stagger on small screens to preserve readable module width.
- No Commerce Systems content was changed.

## Build 15.3 correction
- Reverted the Build 15.2 Commerce Systems hero stagger completely.
- Commerce Systems is back to its Build 15.1 centered/inset widget layout.
- Applied the intended left-stepping cascade to `WEB OPERATIONS // LIFECYCLE VIEW`.
- Build starts farthest right; each lifecycle stage shifts left through Improve.
- Connector arrows follow the diagonal lifecycle path.
- Mobile uses a reduced stagger to preserve text width.

## Build 15.4 list-direction standard
- Reversed the Web Operations lifecycle stagger.
- Item 01 is now left-justified.
- Each subsequent item steps progressively to the right.
- This is now the default Raptor visual pattern for staggered numbered lists.
- Mobile uses the same direction with reduced offsets.

## Build 15.5 Website Lifecycle alignment
- Vertically centered the five `METHOD // WEBSITE LIFECYCLE` steps against the companion section copy.
- Vertically centered the number, title, and supporting text inside each step card.
- Preserved the five-step horizontal desktop layout.
- Single-column tablet/mobile flow returns to normal stacked alignment.

## Build 15.6 Technical SEO System Path
- Converted the Technical SEO `SYSTEM PATH` hero widget from a horizontal row to a vertical staggered sequence.
- `01 Discover` is flush left.
- `02 Index`, `03 Perform`, `04 Understand`, and `05 Measure` step progressively to the right.
- Horizontal arrows were visually converted to downward connectors.
- Mobile keeps the same Raptor direction with reduced offsets.

## Build 15.7 Technical SEO System Path sizing
- Preserved the staggered Technical SEO System Path.
- Restored the earlier 64px minimum box height.
- Reduced desktop module width to `calc(100% - 120px)`.
- Increased the stagger spacing to use the additional negative space.
- Tightened vertical gaps and restored the earlier compact internal text spacing.
- Mobile retains the 64px height with a less aggressive width reduction.

## Build 15.8 Homepage operating-problems section
- Fixed the right-side square modules under `Built for websites with real operating problems`.
- Rebuilt the modules as a clean 2-column grid with consistent gaps and equal visual height.
- Removed inherited positioning/transform behavior that allowed the cards to collide.
- Mobile collapses the modules to a single column.
- No homepage copy was changed.

## Build 15.9 Homepage operating-problems refinement
- Reduced the four operating-problem cards from 132px to 66px minimum height.
- Tightened card padding and spacing.
- Applied a blue Raptor button treatment to `ABOUT RAPTOR CONSULTING GROUP ↗`.
- Mobile keeps compact cards and expands the About CTA full width.

## Build 15.10 Homepage About CTA positioning fix
- Removed the legacy `.text-link` class from the About Raptor CTA.
- The legacy class used `position:absolute`, which caused the button to overlap the lower principle cards.
- Locked the blue CTA into normal document flow below the 2x2 card grid.
- Preserved the blue Raptor button styling and hover treatment.

## Build 15.11 shared Raptor hero stagger system
Applied the Raptor staggered-list styling to these hero widgets:

### Search Systems
- Search Architecture
- Local Search
- Structured Data & Schema
- Analytics & Search Intelligence

### Commerce Systems
- Shopify Development
- Ecommerce Search Architecture
- Ecommerce Technical Optimization
- Product & Commerce Operations

### Web Operations
- Website Production Management
- Website Portfolio Management
- Website Development
- Website Performance Optimization
- Website Migration & Infrastructure

### Company
- About // Operating Core

Default styling:
- Item 01 starts flush left.
- Each following item steps 30px farther right on desktop.
- Service System Path arrows now descend vertically.
- Modules use the compact 64px minimum height established on Technical SEO.
- Mobile keeps the same direction with reduced offsets.

## Build 15.12 About Operating Core box correction
- Preserved the existing 01-left-to-05-right stagger.
- Rebuilt the internal Operating Core card layout to match the System Path visual treatment.
- Numbers now sit in a dedicated left column with a vertical divider.
- Titles and descriptions align in the right content column.
- Restored the compact 64px minimum module height.
- Mobile retains the same number/divider/content anatomy.

## Build 15.13 Web Operations hero lifecycle refinement
- Changed only the `WEB OPERATIONS // LIFECYCLE VIEW` hero widget.
- Shortened desktop box width from `calc(100% - 64px)` to `calc(100% - 96px)`.
- Increased stagger travel while preserving 01 flush left and 05 farthest right.
- Increased connector arrow size from 12px to 17px.
- Increased connector height and padding to add vertical breathing room.
- Mobile uses a reduced version of the same spacing.

## Build 15.14 Commerce Systems hero connector refinement
- Changed only the Commerce Systems hero widget connectors.
- Increased arrow size to 17px on desktop.
- Increased connector height and vertical padding for more breathing room.
- Preserved the existing Commerce box widths, positions, and stack geometry.
- Mobile uses a slightly reduced 15px arrow and 24px connector height.

## Build 15.15 child-service connector direction
Updated the staggered hero connectors to point down-right (`↘`) on:

### Search Systems
- Search Architecture
- Local Search
- Structured Data & Schema
- Analytics & Search Intelligence

### Commerce Systems
- Shopify Development
- Ecommerce Search Architecture
- Ecommerce Technical Optimization
- Product & Commerce Operations

### Web Operations
- Website Production Management
- Website Portfolio Management
- Website Development
- Website Performance Optimization
- Website Migration & Infrastructure

The arrows now visually follow the 01-left-to-05-right stagger direction.
Technical SEO and parent-system hero widgets were not changed.

## Build 15.16 child-service arrow direction correction
- Fixed the staggered child-service arrows that visually appeared to point down-left.
- Cause: legacy `.service-path i { transform: rotate(90deg); }` was rotating the new `↘` glyph.
- Shared Raptor stagger connectors now explicitly use `transform: none`.
- The 13 requested Search, Commerce, and Web Operations child-page connectors now visibly point down-right.
- Technical SEO and parent-system widgets remain unchanged.

## Build 15.17 Technical SEO arrow fix
- Updated only the Technical SEO hero System Path connectors.
- Replaced the vertical down arrow with a down-right arrow (`↘`).
- Explicitly removed the inherited legacy rotation from the connector element.
- Box sizing, stagger offsets, spacing, and Technical SEO content remain unchanged.

## Build 15.18 Analytics & Search Intelligence refinement
- Vertically centered the five `METHOD // SEARCH INTELLIGENCE` steps against the section copy.
- Vertically centered the content inside each method card.
- Reduced Measurement Standard card minimum height from 150px to 112px.
- Increased Measurement Standard detail text from 12px to 13.5px.
- Vertically balanced the × marker with each measurement-standard statement.
- Mobile retains a compact stacked layout.

## Build 15.19 Structured Data & Schema refinement
Applied the same layout corrections used on Analytics & Search Intelligence:
- Vertically centered the five `METHOD // SCHEMA CONTROL` steps against the section copy.
- Vertically centered the content inside each Method card.
- Reduced `STRUCTURED DATA // QUALITY STANDARD` card minimum height to 112px.
- Increased Quality Standard detail text to 13.5px.
- Vertically centered the × marker with each statement.
- Mobile retains a compact stacked layout.

## Build 15.20 Search Architecture + Local Search refinement
Applied the same layout corrections used on Analytics & Search Intelligence and Structured Data & Schema:

### Search Architecture
- Vertically centered the five Method steps against the section copy.
- Vertically centered the content inside each Method card.
- Reduced standards/boundary card minimum height to 112px.
- Increased detail text to 13.5px.
- Vertically centered the marker with each statement.

### Local Search
- Vertically centered the five Method steps against the section copy.
- Vertically centered the content inside each Method card.
- Reduced standards/boundary card minimum height to 112px.
- Increased detail text to 13.5px.
- Vertically centered the marker with each statement.

## Build 15.21 Commerce child-page refinement
Applied the same Method and standards-card corrections to:
- Shopify Development
- Ecommerce Search Architecture
- Ecommerce Technical Optimization
- Product & Commerce Operations

Changes:
- Vertically centered each five-step Method flow against its section copy.
- Vertically centered content inside each Method card.
- Reduced standards/boundary card minimum height to 112px.
- Increased detail text to 13.5px.
- Vertically centered the × marker with each statement.
- Mobile retains a compact stacked layout.

## Build 15.22 Web Operations child-page refinement
Applied the same Method and standards-card corrections to:
- Website Production Management
- Website Portfolio Management
- Website Development
- Website Performance Optimization

Changes:
- Vertically centered each five-step Method flow against its section copy.
- Vertically centered content inside each Method card.
- Reduced standards/boundary card minimum height to 112px.
- Increased detail text to 13.5px.
- Vertically centered the marker with each statement.
- Mobile retains a compact stacked layout.

## Build 15.23 Production Management + Migration correction
- Fixed Website Production Management because its actual body class is `.production-management-page`, not `.website-production-management-page`.
- Applied the same Method vertical-centering and standards-card treatment to Website Migration & Infrastructure.
- Both pages now use 112px standards/boundary card minimum height and 13.5px detail text.
- Mobile retains the compact stacked layout.

## Build 15.24 Technical SEO System Audit refinement
- Redesigned the second row of `PRIORITY MODEL // DECISION LAYER` execution-order boxes.
- Each box now uses a dedicated number rail with divider, stronger title hierarchy, and cleaner supporting-question spacing.
- Made the `AUDIT OUTPUT // CLIENT DELIVERY` left-side explanation reliably sticky while the six deliverables scroll on the right.
- Removed the reveal transform from the sticky left column because transforms can interfere with sticky positioning.
- Sticky behavior returns to normal stacked flow below 860px.

## Build 15.25 Audit Client Delivery sticky Safari correction
- Rechecked the `AUDIT OUTPUT // CLIENT DELIVERY` sticky behavior.
- Identified the global `overflow-x: hidden` on the root elements as a Safari sticky blocker.
- Added an audit-page-only root hook and changed horizontal overflow to `clip` on this page.
- Added `position: -webkit-sticky` plus standard `position: sticky`.
- Explicitly keeps the Deliverables section/grid overflow visible.
- Left copy now sticks 32px from the viewport top while the right deliverable stack continues scrolling.
- Sticky remains disabled below 860px for the stacked mobile/tablet layout.

## Build 15.26 Homepage section-head alignment
- Corrected the top alignment of `CORE SYSTEMS`.
- Corrected the top alignment of `FLAGSHIP OFFER // SEARCH SYSTEMS`.
- Both homepage two-column heading areas now align from the top instead of the bottom.
- Removed the first Flagship Offer copy paragraph's top margin so its right column begins flush with the left section label.
- No other homepage sections were changed.

## Build 15.27 Technical SEO System Audit section alignment
- Top-aligned the two-column intro area in Audit Definition.
- Top-aligned the two-column intro area in Audit Scope // 8 Systems.
- Top-aligned the two-column intro area in Priority Model // Decision Layer.
- Removed any right-column paragraph top offset in those three sections.
- Existing top-aligned Verification, Client Delivery, What This Audit Is Not, and Good Fit layouts remain unchanged.
- Existing Client Delivery sticky behavior remains unchanged.

## Build 15.28 SMS contact path
- Added `Text Raptor` buttons using `sms:Call or text Raptor` to all existing site `.contact-actions` conversion panels.
- Updated 24 pages and 24 contact CTA panels.
- Contact page hero now offers Email, Call, and Text.
- Contact page `Direct Contact // Two Paths` is now `Direct Contact // Three Paths`.
- Added a dedicated SMS contact card between Call and Email.
- Contact page final CTA now includes Text Raptor.
- Mobile contact buttons remain full-width and the three contact-method cards collapse to one column below 820px.
- Main navigation remains Call-only; SMS was added to contact sections, not global navigation.

## Build 15.29 Home + Contact footer logo fade
- Added a viewport-triggered fade-in to the large centered footer logo treatment used on Home and Contact.
- The treatment begins at 0 opacity with an 18px downward offset, then settles upward over 1.15 seconds.
- Reveal begins when roughly 18% of the logo stage enters the viewport.
- The animation runs once per page view.
- `prefers-reduced-motion` disables the motion and displays the logo immediately.
- Progressive enhancement keeps the logo visible if JavaScript is unavailable.

## Build 15.30 Top navigation Call Raptor wrap fix
- Prevented the top-navigation `Call Raptor` button from breaking onto two lines.
- Added `white-space: nowrap` and `flex-shrink: 0` to the navigation phone CTA.
- No other navigation spacing or layout changes were made.

## Build 15.31 Top navigation Call Raptor rollover
- Added a blue hover/focus rollover to the top-navigation `Call Raptor` button.
- Hover state uses deep Raptor blue, cyan border, white text, restrained blue glow, and a 1px lift.
- Existing one-line nowrap behavior remains intact.

## Build 15.32 Global header logo + navigation update
- Added the supplied `raptor-consulting-logo-img-header.webp` logo to the global website header.
- Updated the header logo on all 25 HTML pages.
- Footer logo assets and large Home/Contact footer treatment remain unchanged.
- Header brand width is now responsive, up to 282px on full desktop.
- Reduced desktop nav gap slightly to accommodate the wider logo.
- Kept all primary navigation labels on one line at desktop sizes.
- Preserved the one-line `Call Raptor` CTA and its blue rollover effect.
- Existing mobile menu behavior begins at the current 940px breakpoint.
- Added intrinsic 420×111 image dimensions to reduce layout shift.


## Build 15.33 Footer split-logo animation
- Replaced the large footer logo on `index.html` and `contact.html`.
- Added three new footer logo assets:
  - `assets/raptor-consulting-logo-img-birdup.webp`
  - `assets/raptor-consulting-logo-img-text.webp`
  - `assets/raptor-consulting-logo-img-text-cg.webp`
- Animation sequence:
  1. RAPTOR main text fades in
  2. Bird head fades up into position
  3. CONSULTING GROUP subtext fades down into position
- Triggered on viewport entry using IntersectionObserver.
- Header logo remains unchanged.


## Build 15.34 footer logo alignment refinement
- Reduced the footer bird head by about 30%.
- Refined the composite alignment for the Home and Contact footer logo.
- Tightened footer brand stage spacing so the three-piece mark sits more cleanly in the footer.

## Build 15.35 Footer split-logo specificity correction
- Fixed the reason Build 15.34 visually appeared unchanged.
- Legacy `.footer-brand-mark img` styling was overriding the three-piece logo dimensions.
- Added higher-specificity rules for RAPTOR text, bird head, and CONSULTING GROUP subtext.
- Bird head now actually renders about 30% smaller than the previous composite.
- Rebalanced the bird/text/subtext positions at desktop, tablet, and mobile sizes.

## Build 15.36 narrow header logo + nav spacing
- Replaced the global header logo asset with the new narrower logo.
- Updated header logo intrinsic dimensions to 378x106 across all pages.
- Reduced the header logo footprint to free more horizontal room.
- Increased spacing between top navigation items while preserving no-wrap desktop behavior.
- Slightly reduced desktop nav font size and CTA padding to keep the nav on one line.

## Build 15.37 Global compact sticky header
- Made the global site header sticky.
- Full utility strip + navigation remain visible at the top of the page.
- At 96px of scroll, the header transitions into a compact state.
- Compact state hides the utility strip, tightens nav-shell padding, and slightly reduces the Raptor logo.
- Added a dark translucent glass treatment, subtle blur, blue lower edge, and restrained shadow while sticky.
- Desktop navigation remains one line and preserves the blue `Call Raptor` rollover.
- At the existing <=1220px menu breakpoint, the compact sticky state resolves to logo + Menu.
- Added reduced-motion support.
- Switched root horizontal overflow from `hidden` to `clip` to keep sticky behavior reliable in Safari.

## Build 15.38 Sticky header blue edge
- Replaced the light sticky-header divider with a clearer Raptor blue line.
- Increased the compact header bottom border to `rgba(63,155,233,.58)`.
- Matched the compact nav-shell border and inset edge to the same blue family.
- Sticky behavior, spacing, logo sizing, and navigation remain unchanged.

## Build 15.39 Sticky header Safari seam correction
- Removed the compact sticky header's physical bottom border.
- Added a dedicated 2px Raptor-blue pseudo-element across the bottom of the sticky header.
- The blue edge sits over the Safari `backdrop-filter` compositing seam that could appear white even when the border itself was blue.
- Preserved the translucent sticky treatment, shadow, nav spacing, logo sizing, and Call Raptor rollover.

## Build 15.40 Footer logo layer order
- Corrected the composite footer logo stacking order on Home and Contact.
- RAPTOR wordmark is now the foreground layer (`z-index: 3`).
- Bird head sits behind the wordmark (`z-index: 1`).
- CONSULTING GROUP remains above the base layer (`z-index: 2`).
- No size, position, or animation timing changes in this build.

## Build 15.41 Footer logo alignment
- Reworked the Home and Contact footer split-logo layout to match the centered guide image.
- Centered all three logo assets on a shared vertical axis.
- Increased and repositioned the bird head so it sits centered above and behind the RAPTOR wordmark.
- Centered the CONSULTING GROUP subtext beneath the wordmark.
- Preserved the current reveal order and z-index order.

## Build 15.42 footer logo size reduction
- Reduced the footer RAPTOR wordmark, bird head, and CONSULTING GROUP subtext by 10%.
- Slightly tightened the footer logo stage height and offsets so the centered stacked composition stays aligned.

## Build 15.43 footer logo reduction
- Reduced all three footer logo images by an additional 12%.
- Adjusted container heights and vertical offsets so the centered stacked layout stays aligned across desktop, tablet, and mobile.

## Build 15.44 footer top spacing
- Added more top padding above the footer logo composition on Home and Contact.
- Included a slightly smaller top-padding adjustment on smaller screens.

## Build 15.45 Sticky header opacity refinement
- Reduced the compact sticky-header background opacity by approximately 25%.
- Header gradient alpha changed from .96/.91 to .72/.68.
- Compact nav-shell background alpha changed from .88 to .66.
- Reduced the bottom blue edge opacity by approximately 15%, from .82 to .70.
- Softened the blue edge glow proportionally.
- Blur, spacing, logo sizing, navigation, and sticky behavior remain unchanged.

## Build 15.46 Sticky opacity layering correction
- Double-checked why Build 15.45 looked nearly unchanged.
- The compact header and compact nav-shell backgrounds were compositing together, producing roughly 90% effective darkness.
- Removed the compact nav-shell background so the reduced-opacity outer sticky header is now the only translucent background layer.
- Removed the nav-shell inset shadow that visually reinforced the bottom edge.
- Kept the dedicated blue bottom line at approximately 15% lower visible intensity.
- Sticky behavior, blur, spacing, logo size, and navigation remain unchanged.

## Build 15.47 Safari sticky glass correction
- Reworked the compact header so there is exactly one translucent glass layer.
- The full-width `.site-header.is-compact` is now transparent with no backdrop filter.
- The actual `.nav-shell` now carries the glass background at `.47` alpha, approximately 25% lower than the original `.62` nav-shell alpha.
- Added both `-webkit-backdrop-filter` and standard `backdrop-filter` to the compact nav-shell for Safari/WebKit.
- Added mild saturation with a 14px blur so underlying page content remains perceptible through the menu.
- Kept the single blue bottom line at `.70` visible intensity.

## Build 15.48 Footer/header logo handoff
- On the Homepage and Contact page, the sticky-header logo now fades out when the large footer logo section enters the viewport.
- The header navigation stays fixed in place because the brand element keeps its width; only opacity changes.
- The header logo fades back in when the footer brand section leaves the viewport.
- Other pages are unaffected because they do not contain the large `.footer-brand-stage` treatment.
- Reduced-motion users get the same state change without animation.

## Build 15.49 Safari overscroll background
- Set the root `html` canvas to Raptor blue (`#1A75C7`) so Safari rubber-band overscroll no longer reveals white.
- Kept the visible page body on the existing dark background (`#03060B`).
- Added `theme-color: #1A75C7` as a browser UI fallback.

## Build 15.50 Google Tag Manager
- Extracted the live Raptor Consulting Group Google Tag Manager container: `GTM-TZVZGCSP`.
- Installed the standard GTM script immediately after the opening `<head>` on all 25 HTML pages.
- Installed the standard GTM `<noscript>` iframe immediately after the opening `<body>` on all 25 HTML pages.
- No separate hard-coded GA4 measurement ID or Search Console verification meta tag was added because neither was verified from the current live page.
- Existing site design, sticky-header behavior, footer behavior, routes, and JavaScript remain unchanged.

## Build 15.51 XML sitemap + robots.txt
- Added `sitemap.xml` with all 25 public HTML pages.
- Homepage is represented as `https://raptorconsultinggroup.com/`.
- Added `<lastmod>2026-08-17</lastmod>` for the current build.
- Added `robots.txt` allowing crawling and pointing to `https://raptorconsultinggroup.com/sitemap.xml`.
- No `priority` or `changefreq` values were added because modern search engines do not need them.

## Build 15.52 Canonicals + governed JSON-LD schema
- Added one self-referencing canonical URL to all 25 public HTML pages.
- Added a connected Schema.org JSON-LD `@graph` to all 25 pages.
- Shared `Organization` entity uses `https://raptorconsultinggroup.com/#organization` so page-level entities resolve to one Raptor identity.
- Homepage defines the `WebSite` entity and connects it to the Organization.
- Added `Service` entities to 18 Search, Commerce, Web Operations, and Technical SEO service pages.
- Added `AboutPage` to About and `ContactPage` to Contact.
- Added `CollectionPage` + `ItemList` to Proof without presenting prior work as reviews or testimonials.
- Case studies use conservative `WebPage` markup with `genre: Case Study`.
- Added `BreadcrumbList` only on pages where a visible breadcrumb trail exists.
- No LocalBusiness, Review, AggregateRating, Offer, price, founder, address, or unsupported claims were added.

## Build 15.53 Homepage Proof CTA alignment
- Centered the `Explore Proof & Case Studies` button at the bottom of the Homepage `PROOF // SELECTED OPERATING EXPERIENCE` section.
- Proof cards, section heading, copy alignment, and spacing remain unchanged.

## Build 15.54 Site-wide favicon
- Added the provided Raptor bird-head favicon asset at `assets/raptor-consulting-favicon.webp`.
- Installed it as the favicon on all 25 HTML pages.
- Source favicon dimensions: 1000×1000.
- Removed any older icon declarations before installing the new site-wide favicon.

## Build 15.55 Title + meta description optimization
- Refined titles and meta descriptions across all 25 public pages.
- Strengthened the Homepage title around Technical SEO while retaining Commerce and Web Operations.
- Kept service-page targeting distinct to reduce internal keyphrase competition.
- Added natural commercial phrases such as Technical SEO Services, Local SEO, Shopify Development Services, Website Migration Services, and Website Development Services where they fit the page.
- Meta descriptions are now concise, unique, and written for click-through rather than keyword density.
- No obsolete `meta keywords` tag was added.
- Synchronized governed JSON-LD WebPage and Service descriptions with the updated metadata.
- H1s, visible page copy, canonicals, GTM, sitemap, robots.txt, favicon, and site design remain unchanged.

## Build 15.56 Primary positioning hierarchy
- Repositioned Raptor publicly around one primary discipline: `Technical SEO & Search Architecture`.
- Kept `Raptor Search Systems` as internal methodology language on the primary discipline page.
- Reframed `Commerce Systems` and `Web Operations` as supporting technical capabilities rather than equal primary pillars.
- Updated global navigation to `Technical SEO & Search | Commerce Systems | Web Operations | SEO Audit`.
- Updated footer hierarchy, footer positioning statement, and generic system labels across the site.
- Reworked the Homepage hero and service architecture messaging around the primary/secondary hierarchy.
- Visually strengthened the primary Search card on Homepage and About while preserving responsive behavior.
- Repositioned Commerce Systems as ecommerce technical expertise and Web Operations as development/infrastructure expertise.
- Updated public Search breadcrumbs from `Search Systems` to `Technical SEO & Search`.
- Updated Homepage/Search/About metadata and synchronized governed JSON-LD.
- Added an Organization description to the site-wide schema graph reflecting the new positioning.
- URLs, child service pages, sitemap, robots.txt, GTM, favicon, HQCP, Priority Model, and Technical SEO System Audit remain intact.

## Build 15.57 Homepage hero distinction
- Replaced the Homepage H1 `Technical SEO & Search Architecture.` with the outcome-driven headline:
  `Pinpoint the technical issues holding back your search performance.`
- Kept the Homepage eyebrow `Raptor // Technical SEO & Search Architecture` so the primary discipline remains explicit.
- Kept the Technical SEO & Search page H1 as `Technical SEO & Search Architecture`.
- Tightened the Homepage supporting paragraph to reinforce diagnosis, verification, and prioritization.
- Metadata, schema, GTM, sitemap, robots.txt, favicon, navigation, and service architecture remain unchanged.

## Build 15.58 Homepage H1 size refinement
- Reduced only the Homepage `#hero-title` size.
- Desktop: `clamp(40px, 5vw, 64px)`.
- Mobile <=560px: `clamp(38px, 12.5vw, 54px)`.
- Homepage headline wording, spacing, and all other page H1 sizes remain unchanged.

## Build 15.59 Mobile menu + footer bird position
- Fixed the hamburger dropdown being clipped by the angular `.nav-shell` `clip-path`.
- Desktop header keeps its angular geometry; clipping is disabled only at the <=1220px hamburger breakpoint.
- Added explicit mobile menu z-index, touch behavior, outside-click closing, Escape handling, and desktop-resize reset.
- Raised only the footer bird-head image by 30% on Homepage and Contact.
- RAPTOR wordmark and CONSULTING GROUP subtext size/position remain unchanged.

## Build 15.60 Favicon compatibility fix
- Replaced the single WebP-only favicon declaration with a full favicon set.
- Added root `favicon.ico` containing 16×16, 32×32, and 48×48 sizes.
- Added explicit 16×16 and 32×32 PNG favicons.
- Added a 180×180 Apple touch icon.
- Added `?v=15.60` versioning to favicon URLs to help bypass stale browser favicon caches after deployment.
- Original 1000×1000 WebP source remains in `assets/`.
- Applied the favicon set to all 25 HTML pages.

## Build 15.61 Mobile footer bird true 30% lift
- Corrected the prior mobile bird adjustment.
- The bird is now moved upward by approximately 30% of its rendered image height, rather than increasing its bottom offset by 30%.
- <=700px: `bottom: clamp(69px, 13.79vw, 123px)`.
- <=520px: `bottom: 53px`.
- Applies only where the split footer logo exists: Homepage and Contact.
- RAPTOR wordmark and CONSULTING GROUP subtext remain fixed.
- Desktop bird position remains unchanged.

## Build 15.62 Contact privacy cleanup
- Replaced the previous Gmail address site-wide with `raptorsystems.ai@gmail.com`.
- Removed the public phone number from visible page text.
- Removed direct phone-number `tel:` and `sms:` URLs from HTML source.
- Removed the `telephone` property from Organization JSON-LD.
- Preserved Call Raptor / Text Raptor behavior through runtime-generated links using an encoded contact value in JavaScript.
- The literal phone number is no longer present in text-based source files in this build.

## Build 16.10 Performance and final technical QA
- Added repeatable production finalization in `scripts/finalize_performance.py`.
- Added `styles.min.css` and `script.min.js` while retaining the readable source assets.
- Versioned production asset references with `?v=16.10` and deferred the site JavaScript.
- Verified all canonical-page images have explicit dimensions and footer graphics lazy-load.
- Added `scripts/validate_performance.py` and a complete release checklist at `docs/deployment-checklist.md`.
- Verified-unused duplicate favicon WebP source files are excluded from the deployment package; active ICO, PNG, and Apple touch icons remain.
