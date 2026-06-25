# Apex KB Hardening Patch Report

- mode: `verify`
- repo_head: `67a704ae09115a23de2bac6c66cb14a954a353af`
- repo_branch: `main`
- active_patch_count: `6`

## Changed Files
- none

## Active Patch Results

| ID | File | Status | Changed | Old matches | New matches |
|---|---|---:|---:|---:|---:|
| `G1-KB-CONTRACT-DATA-ROOT-REFLOW` | `.claude/skills/apex-kb/references/kb-contract.md` | `applied` | `False` | 0 | 1 |
| `G1-KB-CONTRACT-KB-SCHEMA-REFLOW` | `.claude/skills/apex-kb/references/kb-contract.md` | `applied` | `False` | 0 | 1 |
| `G1-KB-CONTRACT-SOURCE-POLICY-REFLOW` | `.claude/skills/apex-kb/references/kb-contract.md` | `applied` | `False` | 0 | 1 |
| `G2-PYTHON-CLAIM-LABEL-VOCABULARY` | `apex-meta/scripts/apex_kb.py` | `applied` | `False` | 0 | 1 |
| `G2-TEMPLATE-CLAIM-LABEL-FIELD` | `.claude/skills/apex-kb/templates/ingest-analysis-template.md` | `applied` | `False` | 0 | 1 |
| `G3-SCRIPT-CONTRACT-PARITY-MANIFEST-STATUS` | `.claude/skills/apex-kb/package-manifest.md` | `applied` | `False` | 0 | 1 |

## Deferred Patches

- `G4-DEFER-STALE-INDEX-HASH` — Stale-index behavior is a script-behavior change. This script records the gap but does not patch it until an explicit deterministic index freshness contract is approved. Current apex_kb.py reports stale_index=False and stale_index_hash=NA, so the weakness is real but should not be changed through an unreviewed broad code edit.
- `G5-DEFER-GOLDEN-FIXTURE` — The handover allows optional isolated tests/fixtures only if justified. This patch pass touches no optional fixture paths to keep unrelated changes out of the first hardening patch.
