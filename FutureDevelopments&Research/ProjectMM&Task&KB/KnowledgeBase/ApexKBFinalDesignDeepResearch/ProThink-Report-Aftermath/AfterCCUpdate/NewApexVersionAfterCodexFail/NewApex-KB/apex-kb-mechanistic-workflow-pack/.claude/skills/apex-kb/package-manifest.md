# Apex KB Package Manifest v2

## Entry point

- `.claude/skills/apex-kb/SKILL.md` — manual-only thin launcher.

## Runtime scripts outside this package

- `apex-meta/scripts/apex_kb.py` — public CLI and deterministic domain stages.
- `apex-meta/scripts/apex_kb_control.py` — state machine, manifest lock, stage transitions, packet/instruction rendering, and reconciliation.
- `apex-meta/scripts/apex_kb_retrieval.py` — derived retrieval build/query.

The skill folder is not executable by itself.

## Canonical v2 contracts

- `references/run-config.schema.json`
- `references/preflight-report.schema.json`
- `references/run-manifest.schema.json`
- `references/run-state.schema.json`
- `references/stage-result.schema.json`
- `references/semantic-task-instructions.schema.json`
- `references/semantic-handoff-packet.schema.json`
- `references/phase0-stats.schema.json`
- `references/semantic-value-contract.md`
- `references/script-command-contract.md`
- `references/phase0-ranking-and-stats-contract.okf.md`

## Stable templates

- `templates/welcome-intake.okf.md`
- `templates/run-config-template.okf.json`
- `templates/topic-registry-template.okf.json`
- `templates/phase0-stats-report.okf.md`
- `templates/phase1-prompt-template.okf.md`
- `templates/phase1-run-instructions.okf.yaml`
- `templates/phase2-prompt-template.okf.md`
- `templates/phase2-run-instructions.okf.yaml`
- `templates/ingest-analysis-template.md`
- `templates/wiki-page-templates.md`
- `templates/semantic-handoff-packet-template.md`

## Loading policy

- The skill body contains only launcher behavior.
- Deterministic scripts read schemas/templates by exact path.
- Semantic executors receive only the generated instruction file, named stable prompt, batch guide, and named evidence.
- No runtime stage reads this manifest to decide business logic; it is packaging and consistency-test input only.
