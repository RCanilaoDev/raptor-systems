# Raptor Build 16.10 Deployment Checklist

## Before deployment

- Confirm the deployment commit contains all 39 canonical pages, `404.html`, `robots.txt`, `sitemap.xml`, `CNAME`, and the versioned production assets.
- Create a recoverable Git tag or release before replacing the live build.
- Confirm the custom domain remains `raptorconsultinggroup.com` and HTTPS enforcement remains enabled in GitHub Pages.
- Keep the 24 legacy flat HTML redirect stubs. GitHub Pages cannot send server-side 301 responses, so these remain noindex client redirects until hosting supports managed redirects.

## Release verification

- Open the homepage and representative Search, Commerce, Web Operations, Work, About, Founder, Insights, Contact, Privacy, and Terms URLs.
- Verify the desktop services disclosure, mobile menu, outside-click closing, Escape closing, keyboard focus, Call Raptor action, and footer reveal.
- Verify `/404.html`, one intentionally invalid URL, all legacy flat URLs, and trailing-slash canonical URLs.
- Confirm `styles.min.css?v=16.10` and `script.min.js?v=16.10` return HTTP 200 and the JavaScript loads with `defer`.
- Confirm all images return HTTP 200, retain their dimensions, and footer graphics lazy-load.
- Confirm Google Tag Manager container `GTM-TZVZGCSP` loads once and GA4 real-time traffic is visible.

## Search verification

- Confirm `https://raptorconsultinggroup.com/robots.txt` and `https://raptorconsultinggroup.com/sitemap.xml` return HTTP 200.
- Submit the sitemap in Google Search Console.
- Inspect the homepage plus one URL from each primary site section and request indexing only after the live checks pass.
- Validate representative JSON-LD with Google Rich Results Test and Schema.org Validator.
- Confirm canonical, robots, Open Graph, Twitter, title, description, one H1, breadcrumb markup, and internal links on representative pages.

## Monitoring

- Run PageSpeed Insights on representative desktop and mobile URLs after CDN caches settle.
- Crawl all sitemap URLs and check status, canonical targets, indexability, headings, schema, and broken internal links.
- Review Search Console indexing and enhancement reports after 24 hours, 7 days, and 30 days.
- Review GA4 and Tag Manager after 24 hours to confirm traffic and contact interactions are recorded as intended.
