# Batch D — Remove Cloudflare scripts from the critical path

PSI called out two Cloudflare-injected scripts on `https://raptorconsultinggroup.com/`:

1. `static.cloudflareinsights.com/beacon.min.js` (Web Analytics)
2. `/cdn-cgi/scripts/.../email-decode.min.js` (Email Address Obfuscation)

Both add third-party / utility JS on first load. First-party pages no longer use
raw `mailto:` or visible email addresses in HTML body copy (JSON-LD Organization
`email` remains for SEO). Contact uses `data-contact-action="email"` in
`script.min.js?v=16.51`.

## Cloudflare dashboard steps (required)

### 1. Disable Web Analytics (stops beacon + `/cdn-cgi/rum`)

1. Cloudflare Dashboard → select **raptorconsultinggroup.com**
2. **Analytics & Logs** → **Web Analytics**
3. Find this site / beacon → **Disable** or remove the site from Web Analytics  
   (wording varies; goal is no automatic beacon injection)

Optional: if a Web Analytics JS snippet was pasted into HTML, remove it. This
repo does not include one — injection was zone-level.

### 2. Disable Email Address Obfuscation (stops email-decode.min.js)

1. **Security** → **Settings** (or **Scrape Shield**, depending on dashboard UI)
2. **Email Address Obfuscation** → **Off**

Safe now because visible/body emails and `mailto:` links were replaced with
runtime `data-contact-action="email"` handlers.

## Verify

```bash
curl -sL 'https://raptorconsultinggroup.com/' | rg -n 'beacon\.min|cloudflareinsights|email-decode|mailto:raptorsystems'
```

Expect:

- No `beacon.min.js` / `cloudflareinsights.com`
- No `email-decode.min.js`
- No body `mailto:raptorsystems...` (JSON-LD email may still appear in schema)

Then re-run PageSpeed Insights on `https://raptorconsultinggroup.com/`.
