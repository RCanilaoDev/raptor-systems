from pathlib import Path
from urllib.parse import urlparse
import html, json, re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"
OG_IMAGE=BASE+"/assets/raptor-consulting-logo-img-header.webp"
GTM_HEAD="""<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-TZVZGCSP');</script>
<!-- End Google Tag Manager -->"""
GTM_BODY='''<!-- Google Tag Manager (noscript) --><noscript><iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-TZVZGCSP" style="display:none;visibility:hidden" title="Google Tag Manager" width="0"></iframe></noscript><!-- End Google Tag Manager (noscript) -->'''
FAVICONS='''<link href="/favicon.ico?v=16.01" rel="icon" sizes="any"/><link href="/assets/raptor-consulting-favicon-32.png?v=16.01" rel="icon" sizes="32x32" type="image/png"/><link href="/assets/raptor-consulting-favicon-16.png?v=16.01" rel="icon" sizes="16x16" type="image/png"/><link href="/assets/raptor-consulting-apple-touch-icon.png?v=16.01" rel="apple-touch-icon" sizes="180x180"/>'''

root=ET.parse(ROOT/"sitemap.xml").getroot(); ns={"s":"http://www.sitemaps.org/schemas/sitemap/0.9"}
urls=[n.text for n in root.findall("s:url/s:loc",ns)]
for canonical in urls:
    path=urlparse(canonical).path; file=ROOT/("index.html" if path=="/" else path.strip("/")+"/index.html")
    text=file.read_text(encoding="utf-8")
    title=html.unescape(re.search(r"<title>(.*?)</title>",text,re.S).group(1)).strip()
    description=html.unescape(re.search(r'<meta content="([^"]*)" name="description"',text).group(1)).strip()
    text=re.sub(r'<meta content="[^"]*" name="robots"\s*/?>','',text)
    social=(f'<meta content="index,follow,max-image-preview:large" name="robots"/>'
      f'<meta content="website" property="og:type"/><meta content="{html.escape(title)}" property="og:title"/>'
      f'<meta content="{html.escape(description)}" property="og:description"/><meta content="{canonical}" property="og:url"/>'
      f'<meta content="{OG_IMAGE}" property="og:image"/><meta content="Raptor Consulting Group" property="og:site_name"/>'
      f'<meta content="summary_large_image" name="twitter:card"/><meta content="{html.escape(title)}" name="twitter:title"/>'
      f'<meta content="{html.escape(description)}" name="twitter:description"/><meta content="{OG_IMAGE}" name="twitter:image"/>')
    text=text.replace('<meta content="#1A75C7" name="theme-color"/>', '<meta content="#1A75C7" name="theme-color"/>'+social)
    text=re.sub(r'(?:<link href="/?favicon\.ico[^>]*>|<link href="/?assets/raptor-consulting-(?:favicon-(?:32|16)|apple-touch-icon)[^>]*>)+',FAVICONS,text)
    if 'GTM-TZVZGCSP' not in text.split('</head>',1)[0]: text=text.replace('<head>','<head>\n'+GTM_HEAD,1)
    if 'googletagmanager.com/ns.html' not in text: text=text.replace('<body','<body',1).replace('>', '>'+GTM_BODY,1) if text.startswith('<body') else re.sub(r'(<body[^>]*>)',r'\1'+GTM_BODY,text,count=1)
    match=re.search(r'<script(?: data-raptor-schema="v1")? type="application/ld\+json">(.*?)</script>',text,re.S)
    if match:
      data=json.loads(match.group(1)); graph=data.setdefault('@graph',[])
      org=next((x for x in graph if x.get('@id')==BASE+'/#organization'),None)
      if org is None: org={"@type":"Organization","@id":BASE+"/#organization"}; graph.insert(0,org)
      org.update({"@type":"Organization","@id":BASE+"/#organization","name":"Raptor Consulting Group","url":BASE+"/","email":"raptorsystems.ai@gmail.com","founder":{"@id":BASE+"/about/ricardo-canilao/#person"},"areaServed":{"@type":"AdministrativeArea","name":"Orange County, California"},"logo":{"@type":"ImageObject","@id":BASE+"/#logo","url":OG_IMAGE,"contentUrl":OG_IMAGE}})
      website=next((x for x in graph if x.get('@id')==BASE+'/#website'),None)
      if website is None: graph.insert(1,{"@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":"Raptor Consulting Group","publisher":{"@id":BASE+"/#organization"},"inLanguage":"en-US"})
      for node in graph:
        if node.get('@id')==canonical+'#webpage': node.update({"url":canonical,"isPartOf":{"@id":BASE+"/#website"},"inLanguage":"en-US"})
      replacement='<script data-raptor-schema="v2" type="application/ld+json">'+json.dumps(data,separators=(',',':'))+'</script>'
      text=text[:match.start()]+replacement+text[match.end():]
    file.write_text(text,encoding="utf-8")

not_found=ROOT/"404.html"
not_found.write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1" name="viewport"/><title>Page Not Found | Raptor Consulting Group</title><meta content="noindex,follow" name="robots"/><link href="/styles.css" rel="stylesheet"/><link href="/favicon.ico?v=16.01" rel="icon"/></head><body><main class="section shell"><div class="eyebrow">SYSTEM // 404</div><h1>That page is outside the current system.</h1><p class="hero-lede">The address may have changed during Raptor's architecture realignment.</p><div class="hero-actions"><a class="button button-primary" href="/">Return Home</a><a class="button button-secondary" href="/services/">Explore Services</a></div></main></body></html>''',encoding="utf-8")
print(f"Finalized {len(urls)} canonical pages and 404.html")
