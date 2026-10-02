#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
python3 - <<'PY'
from pathlib import Path
import re
p=Path('apex-meta/Alpine/ARCHITEKTUR-BASIS.md'); s=p.read_text(encoding='utf-8-sig')
if 'AnythingLLM' not in s or 'Psono' not in s: raise SystemExit('Expected legacy architecture markers not found.')
intro='''# ki-basis — Current Platform Architecture\n\n> **Current runtime authority:** `ki-basis/compose.yaml`.  \n> This document describes the implemented local Docker stack. The older AnythingLLM/Psono/Authentik/Envoy/oMLX/Ollama/Speaches topology is superseded for the current runtime and remains available through Git history for provenance.\n'''
s=re.sub(r'\A# ki-basis — Platform-Architektur \(Startpunkt\)\n\n>.*?\n\n```mermaid', intro+'\n```mermaid', s, count=1, flags=re.S)
diagram='''```mermaid\nflowchart TB\n    subgraph edge [KI-BASIS — HTTP Edge]\n        NGX[nginx<br/>127.0.0.1:8084<br/>nginx:80]\n    end\n    subgraph control [KI-BASIS — AI Operating Surface]\n        HERMES[Hermes Agent<br/>host :8642 · :9119<br/>internal hermes:8642 · hermes:9119]\n    end\n    subgraph apps [KI-BASIS — Applications]\n        FIREFLY[Firefly III<br/>127.0.0.1:8086<br/>firefly:8080]\n        PAPERLESS[Paperless-ngx<br/>127.0.0.1:8010<br/>paperless:8000]\n        OPENPROJECT[OpenProject<br/>127.0.0.1:8082<br/>openproject:80]\n    end\n    subgraph data [KI-BASIS — Shared Data Services]\n        PG[(PostgreSQL + pgvector<br/>postgres:5432<br/>internal only)]\n        VALKEY[(Valkey<br/>valkey:6379<br/>internal only)]\n        DBF[(firefly DB)]\n        DBP[(paperless DB)]\n        DBO[(openproject DB)]\n    end\n    PG --> DBF\n    PG --> DBP\n    PG --> DBO\n    FIREFLY --> PG\n    PAPERLESS --> PG\n    PAPERLESS --> VALKEY\n    OPENPROJECT --> PG\n    HERMES -->|supported REST API| FIREFLY\n    HERMES -->|supported REST API| PAPERLESS\n    HERMES -->|API v3| OPENPROJECT\n    NGX --> FIREFLY\n    NGX --> PAPERLESS\n    NGX --> OPENPROJECT\n```'''
s=re.sub(r'```mermaid.*?```',diagram,s,count=1,flags=re.S)
idx=s.find('> **Kern-Service-Linie')
if idx<0: raise SystemExit('Expected legacy service-line block not found.')
replacement='''> **Current service line (`ki-basis/compose.yaml`):**\n> `postgres`, `valkey`, `firefly`, `paperless`, `openproject`, `nginx`, `hermes`.\n>\n> **Network:** all services join `ki-basis-net` and use Docker service-name DNS. PostgreSQL and Valkey are internal-only.\n>\n> **Persistence:** PostgreSQL, Valkey, Firefly uploads, Paperless data/media/export/consume, OpenProject assets, and Hermes `/opt/data` are persisted according to Compose.\n>\n> **Hermes role:** Hermes is the AI operating surface and reaches Firefly, Paperless and OpenProject through supported application APIs. It does not require direct database manipulation or a Docker socket.\n>\n> **Alpine policy:** Alpine is an image choice, not the platform architecture. nginx and Valkey use Alpine-compatible upstream images; complex vendor applications retain supported upstream images.\n\n### Current authority / evidence\n- Runtime: [`../../ki-basis/compose.yaml`](../../ki-basis/compose.yaml)\n- Stack environment template: [`../../ki-basis/.env.example`](../../ki-basis/.env.example)\n- Integration evidence: [`INTEGRATION-ACCEPTANCE-REPORT.md`](INTEGRATION-ACCEPTANCE-REPORT.md)\n- Antigravity implementation authority: [`ImplementationPlans/00-START-HERE.md`](ImplementationPlans/00-START-HERE.md)\n- Alpine image-build reference: [`2026-09-01-alpine-image-build.md`](2026-09-01-alpine-image-build.md)\n'''
p.write_text(s[:idx]+replacement+'\n',encoding='utf-8')
PY
git diff --check
echo "PATCH APPLIED LOCALLY. Review: git diff -- apex-meta/Alpine/ARCHITEKTUR-BASIS.md"

# > **Host boundary:** Windows 11 runs Docker Desktop. Docker Desktop uses its WSL-independent Hyper-V Linux-container backend.
