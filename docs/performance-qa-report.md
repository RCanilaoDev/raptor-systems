# Build 16.10 Performance and Technical QA Report

## Production payload changes

| Asset | Readable source | Production asset | Reduction |
|---|---:|---:|---:|
| CSS | 196,518 bytes | 152,107 bytes | 22.6% |
| JavaScript | 4,831 bytes | 3,937 bytes | 18.5% |

All 39 canonical pages reference `styles.min.css?v=16.10` and defer `script.min.js?v=16.10`. Readable source files remain in the repository for maintenance.

## Image delivery

- Every image on a canonical page has explicit width and height attributes.
- The header logo remains eager because it is above the fold.
- Footer logo components use native lazy loading and asynchronous decoding.
- Visible site graphics use WebP. Active favicon compatibility assets use ICO and PNG as required by browsers and devices.
- Two duplicate 239,690-byte favicon WebP source files are not referenced by the website and are excluded from the release package.

## Automated results

| Validation | Scope | Result |
|---|---:|---|
| Architecture and SEO | 39 canonical pages | 0 errors |
| Search Systems | 7 pages | 0 errors |
| Commerce Systems | 5 pages | 0 errors |
| Web Operations | 6 pages | 0 errors |
| Evidence and Systems | 10 pages | 0 errors |
| Company and Founder | 3 pages | 0 errors |
| Insights | 4 hubs | 0 errors |
| Entity graph | 103 definitions, 331 references | 0 errors |
| Accessibility and interactions | 39 canonical pages | 0 errors |
| Performance delivery | 39 canonical pages | 0 errors |

## Remaining live-environment checks

Browser rendering, HTTP status, CDN caching, Core Web Vitals, Google Search Console, GA4, and Tag Manager network behavior require the deployed site. Complete those checks using `docs/deployment-checklist.md` after approval to publish.
