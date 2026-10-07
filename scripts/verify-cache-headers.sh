#!/usr/bin/env bash
# Verify Batch C cache headers on production.
set -euo pipefail
BASE="${1:-https://raptorconsultinggroup.com}"
V="${2:-16.49}"

check() {
  local url="$1"
  echo ""
  echo "==> $url"
  curl -sI -A "raptor-cache-check/1.0" "$url" | rg -i 'HTTP/|cache-control|cf-cache-status|age|server:|x-cache|expires' || true
}

check "$BASE/"
check "$BASE/styles.critical.min.css?v=$V"
check "$BASE/styles.min.css?v=$V"
check "$BASE/script.min.js?v=$V"
check "$BASE/assets/raptor-consulting-logo-img-header.webp?v=$V"

echo ""
echo "GitHub Pages origin alone always shows max-age=600."
echo "After Cloudflare Batch C, static assets should show long max-age and cf-cache-status."
