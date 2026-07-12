# Weekly Orchestrator — Old-Apex Role Doctrine Migration Ledger

Status: executed 2026-07-12. Method: one evaluation worker per v1 role (PRC-MULTI-001 fan-out); every scaffold item (ESSENCE / BEST_PRACTICES / MISTAKES / TEMPLATES + appendices) evaluated against the current built system; only still-valid, non-duplicative, actionable doctrine migrated, each entry citing its source. LEARNING_QUEUE.md excluded everywhere (candidate learning never auto-promotes). Historical paths carried as evidence citations only, never as live instructions.

Source root: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/` (v1 KB stays intact per the standing do-not-delete resolution — this migration copies distilled doctrine out; it moves nothing).

## Migration map

| v1 role | kept | dropped | doctrine file (owning domain) | consumer wiring |
|---|---|---|---|---|
| alfred | 3 | 6 | `.claude/skills/weekly-orchestrator/references/roles/alfred-doctrine.md` | orchestrator references (read_when: presenting packets, recording gates) |
| meta_ops | 2 | 13 | `.claude/skills/weekly-orchestrator/references/roles/meta-ops-doctrine.md` | orchestrator references (read_when: sequencing, dispatch ambiguity) |
| meta_strategy | 7 | 7 | `.claude/skills/weekly-orchestrator/references/roles/meta-strategy-doctrine.md` | apex-precap-week startup read 1 |
| meta_detective | 17 | 15 | `.claude/skills/weekly-orchestrator/references/roles/meta-detective-doctrine.md` | both reviewer agents, pre-review read |
| special_ops__ai_handling_routing | 28 | 17 | `.claude/skills/AIRouting/old-apex-routing-doctrine.md` | AIRouting supporting_files |
| special_ops__prompts_workflows | 25 | 7 | `.claude/skills/PromptEngineer/references/old-apex-prompting-doctrine.md` + `.claude/skills/Workflow&Processes/old-apex-workflow-doctrine.md` | both skills' supporting_files |
| special_ops__knowledge_bank | 8 | 23 | `.claude/skills/apex-kb/references/old-apex-knowledge-bank-doctrine.md` | apex-kb supporting-files table |
| special_ops__informatics_design | 17 | 21 | `.claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md` | orchestrator references (read_when: file/packet design) |
| special_ops__hygiene_clean | 17 | 21 | `.claude/skills/weekly-orchestrator/references/roles/hygiene-clean-doctrine.md` | orchestrator references (read_when: structural QA sweeps) |
| **total** | **124** | **130** | 10 doctrine files | — |

## Drop-reason classes (evaluation record)

```yaml
drop_reasons:
  duplicate_of_current_system:      # largest class
    examples:
      - alfred owns/does-not-own boundaries — already in weekly-orchestrator SKILL.md + GLOSSARY
      - candidate-before-truth doctrine — already enforced by authority.state axis + G4/G5 candidate-only packets
      - typed-bullet signal words + scaffold/appendix split — already absorbed verbatim into D-M6
      - validator-never-implements-fixes — already a hard constraint in review-wiring + both reviewer definitions
  superseded_by_locked_architecture:
    examples:
      - meta_ops "owns execution control" — under the locked loop the operator executes flows (G3); main thread dispatches/gates/writes
      - detective pass/revise/hold/needs_input/escalate vocabulary — replaced by criterion-level pass/needs_revision/fail/blocked with deterministic aggregation
      - EVD/IMP/RSK promotion machinery + hand-maintained candidate ledgers — replaced by review wiring and apex-kb deterministic ownership
  bound_to_dead_surfaces:
    examples:
      - Hygiene-to-Night backlog routing, cross-agent lane ownership tables, old-repo execution locks (openclaw.json)
      - Codex bounded-execution preflight and edit-mode chooser — transport mechanics owned by deterministic-markdown-patcher skills
  stale_volatile_claims:
    examples:
      - provider-specific directive ceilings (gpt_4o 50, o3 100, ...) — non-provider-agnostic capability claims
  empty_state_only:
    examples:
      - alfred/meta_ops/meta_strategy BEST_PRACTICES/MISTAKES/TEMPLATES held EMPTY_STATE markers — nothing was ever promoted in v1
```

## Validation executed

```yaml
checks:
  lint_sweep: all 10 doctrine files — no changelog narrative, no LEARNING_QUEUE instructions, ≤120 lines each, source citation present (2 source-basis lines corrected to full repo paths)
  wiring: every doctrine file referenced by at least one consumer (orchestrator references list, agent startup reads, or skill supporting_files)
  source_preservation: v1 KB untouched (read-only evaluation)
```

Per-item verdicts live inside each doctrine file (kept items, with per-item source IDs); this ledger is the cross-role record.
