from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]; BASE="https://raptorconsultinggroup.com"; errors=[]
for url in ('/about/','/about/ricardo-canilao/','/contact/'):
 text=(ROOT/url.strip('/')/'index.html').read_text(encoding='utf-8'); m=re.search(r'<script data-raptor-schema="v\d+" type="application/ld\+json">(.*?)</script>',text,re.S)
 if not m: errors.append(f"SCHEMA VERSION {url}"); continue
 g=json.loads(m.group(1))['@graph']; ids={x.get('@id') for x in g}
 if url=='/about/ricardo-canilao/' and BASE+'/about/ricardo-canilao/#person' not in ids: errors.append(f"PERSON {url}")
 org=next(x for x in g if x.get('@id')==BASE+'/#organization')
 if org.get('founder',{}).get('@id')!=BASE+'/about/ricardo-canilao/#person': errors.append(f"FOUNDER {url}")
if 'founder-profile-bridge' not in (ROOT/'about/index.html').read_text(): errors.append('ABOUT FOUNDER BRIDGE')
profile=(ROOT/'about/ricardo-canilao/index.html').read_text()
for path in ('/work/case-studies/specialized-accounting-search-architecture/','/work/case-studies/website-infrastructure-migration/','/work/case-studies/high-volume-website-production/','/work/case-studies/wordpress-shopify-commerce-system/','/work/systems/hqcp/'):
 if f'href="{path}"' not in profile: errors.append(f"PROFILE EVIDENCE {path}")
source='\n'.join(p.read_text(errors='ignore') for p in ROOT.rglob('*.html'))
if re.search(r'(?:tel:|sms:)\+?\d',source): errors.append('HARDCODED PHONE URI')
if 'DOWNLOAD RÉSUMÉ' in profile.upper() or 'DOWNLOAD RESUME' in profile.upper(): errors.append('UNSUPPORTED RESUME LINK')
print('Company and Founder pages: 3'); print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
