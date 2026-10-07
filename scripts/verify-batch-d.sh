#!/usr/bin/env bash
set -euo pipefail
URL="${1:-https://raptorconsultinggroup.com/}"
echo "Checking $URL"
html="$(curl -sL -A 'raptor-batch-d/1.0' "$URL")"
fail=0
for needle in 'beacon.min.js' 'cloudflareinsights.com' 'email-decode.min.js'; do
  if printf '%s' "$html" | rg -q "$needle"; then
    echo "FAIL still present: $needle"
    fail=1
  else
    echo "OK absent: $needle"
  fi
done
if printf '%s' "$html" | rg -q 'script\.min\.js\?v=16\.51'; then
  echo "OK script v=16.51"
else
  echo "WARN expected script.min.js?v=16.51"
fi
if printf '%s' "$html" | rg -q 'data-contact-action="email"'; then
  echo "OK email contact actions present"
else
  echo "FAIL missing data-contact-action=email"
  fail=1
fi
exit "$fail"
