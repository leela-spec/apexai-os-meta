#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
DIR="apex-meta/Alpine/ImplementationPlans"
delete_files=(
  "$DIR/00-META-IMPLEMENTATION-PLAN.md"
  "$DIR/01-NGINX-IMPLEMENTATION-PLAN.md"
  "$DIR/02-POSTGRES-PGVECTOR-IMPLEMENTATION-PLAN.md"
  "$DIR/03-VALKEY-IMPLEMENTATION-PLAN.md"
  "$DIR/04-FIREFLY-IMPLEMENTATION-PLAN.md"
  "$DIR/05-PAPERLESS-NGX-IMPLEMENTATION-PLAN.md"
  "$DIR/06-OPENPROJECT-IMPLEMENTATION-PLAN.md"
  "$DIR/07-HERMES-IMPLEMENTATION-PLAN.md"
  "$DIR/08-INTEGRATION-ACCEPTANCE-CHECKLIST.md"
)
for f in "${delete_files[@]}"; do [[ -f "$f" ]] || { echo "ERROR expected generic plan missing: $f" >&2; exit 1; }; done
rm -- "${delete_files[@]}"
python3 - <<'PY'
from pathlib import Path
root=Path('apex-meta/Alpine/ImplementationPlans')
old='../antigravity-instruction-orchestrator/'
new='../../SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/'
for name in ['00-START-HERE.md','01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md']:
    p=root/name; s=p.read_text(encoding='utf-8-sig')
    if old not in s: raise SystemExit(f'Expected stale authority link not found in {p}')
    p.write_text(s.replace(old,new),encoding='utf-8')
(root/'README.md').write_text('''# Alpine / Docker Stack Implementation Plans\n\n## Execution authority\n\nFor Google Antigravity, start at `00-START-HERE.md`.\n\nCanonical execution files:\n- `01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md`\n- `02-NGINX-ANTIGRAVITY.md`\n- `03-POSTGRES-PGVECTOR-ANTIGRAVITY.md`\n- `04-VALKEY-ANTIGRAVITY.md`\n- `05-FIREFLY-ANTIGRAVITY.md`\n- `06-PAPERLESS-NGX-ANTIGRAVITY.md`\n- `07-OPENPROJECT-ANTIGRAVITY.md`\n- `08-HERMES-ANTIGRAVITY.md`\n- `09-INTEGRATION-ACCEPTANCE-ANTIGRAVITY.md`\n\nThe earlier generic implementation-plan family was removed after integration because it duplicated execution authority. Git history retains it for provenance.\n\nAlpine remains an image choice, not a requirement for every service.\n''',encoding='utf-8')
PY
! grep -R --line-number '../antigravity-instruction-orchestrator' "$DIR" >/dev/null 2>&1 || { echo "ERROR stale authority links remain" >&2; exit 1; }
git diff --check
echo "PATCH APPLIED LOCALLY. Review: git diff -- $DIR"
