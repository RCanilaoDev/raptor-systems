# Batch C — long-lived cache for versioned static assets

## Why this is required

GitHub Pages (behind Fastly) always sends:

```http
Cache-Control: max-age=600
```

That applies to HTML, CSS, JS, and images. There is no in-repo setting that
overrides it. Lighthouse flags this as “Use efficient cache lifetimes.”

Assets are already cache-busted with `?v=16.49` (CSS/JS/logos/favicons), so
long browser/CDN TTLs are safe: a new deploy bumps `v=` and fetches fresh files.

## Recommended activation: Cloudflare Free (proxy GitHub Pages)

Keeps same-origin URLs (best for LCP). Orange-cloud the domain, then override
cache TTLs at the edge.

### 1. Add the site to Cloudflare

1. Create/sign in to a free Cloudflare account.
2. **Add site** → `raptorconsultinggroup.com`.
3. Choose the **Free** plan.
4. Cloudflare will show two nameservers (e.g. `*.ns.cloudflare.com`).

### 2. Point Namecheap DNS to Cloudflare

1. Namecheap → Domain List → `raptorconsultinggroup.com` → **Nameservers**.
2. Select **Custom DNS**.
3. Enter the two Cloudflare nameservers → save.
4. Wait until Cloudflare shows the zone as **Active** (often 5–30 minutes).

### 3. DNS records in Cloudflare

Keep GitHub Pages reachability:

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | `@` | `185.199.108.153` | Proxied (orange) |
| A | `@` | `185.199.109.153` | Proxied (orange) |
| A | `@` | `185.199.110.153` | Proxied (orange) |
| A | `@` | `185.199.111.153` | Proxied (orange) |
| CNAME | `www` | `RCanilaoDev.github.io` | Proxied (orange) |

SSL/TLS mode: **Full** (GitHub Pages serves HTTPS).

### 4. Cache Rule (Batch C)

**Caching → Cache Rules → Create rule**

**Rule name:** `Raptor versioned static assets`

**If incoming requests match** — Custom filter expression:

```txt
(http.request.uri.path.extension in {"css" "js" "webp" "png" "jpg" "jpeg" "svg" "ico" "woff" "woff2"})
```

**Then:**

- **Eligible for cache:** Yes  
- **Edge TTL:** Override → **1 month** (or 1 year)  
- **Browser TTL:** Override → **1 year**  
- **Cache key:** Include query string (so `?v=16.49` busts correctly) — default is fine if query string is part of the cache key

Optional second rule for HTML (keep short):

**If:**

```txt
(http.request.uri.path.extension eq "html") or (http.request.uri.path eq "/")
```

**Then:** Browser TTL Override → **Respect origin** (or a few minutes). Do **not** long-cache HTML.

### 5. Verify

```bash
curl -sI "https://raptorconsultinggroup.com/styles.min.css?v=16.49" | rg -i 'cache-control|cf-cache|age|server'
curl -sI "https://raptorconsultinggroup.com/" | rg -i 'cache-control|cf-cache|age|server'
```

Expect static assets roughly like:

```http
cache-control: public, max-age=31536000
cf-cache-status: HIT   # after first request
server: cloudflare
```

HTML may still be short-lived; that is intentional.

## Alternative: Cloudflare Pages / Netlify

Deploy this repo to a host that honors the root `_headers` file. Same policy,
no Cache Rule UI required. Custom domain cuts over when you are ready.

## What not to do

- Do not long-cache HTML without a purge/version strategy.
- Do not remove `?v=` query busting while using year-long asset TTLs.
