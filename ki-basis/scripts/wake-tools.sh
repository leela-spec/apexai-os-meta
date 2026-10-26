#!/usr/bin/env bash
set -euo pipefail
echo "==> Waking up Paperless and Firefly..."
docker start ki-basis-valkey ki-basis-paperless ki-basis-firefly ki-basis-nginx
echo "==> Paperless (http://127.0.0.1:8010) and Firefly (http://127.0.0.1:8086) are ACTIVE."
