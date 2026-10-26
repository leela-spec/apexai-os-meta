#!/usr/bin/env bash
set -euo pipefail
echo "==> Putting Paperless, Firefly, and Nginx back to sleep..."
docker update --restart=no ki-basis-paperless ki-basis-firefly ki-basis-nginx >/dev/null
docker stop ki-basis-paperless ki-basis-firefly ki-basis-nginx
echo "==> Tools are SLEEPING (restart=no). ~840 MB RAM released."
