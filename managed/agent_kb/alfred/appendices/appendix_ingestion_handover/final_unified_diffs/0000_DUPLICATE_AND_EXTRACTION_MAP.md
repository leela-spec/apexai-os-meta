# Duplicate and Extraction Map

## Scope lock

This file is reference-only for the final unified diff package. It does not patch scaffold files.

Allowed write surface for this pass:

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs/
```

No scaffold target file is modified by this map.

## Baseline inventory read

Target scaffold files checked:

- `managed/agent_kb/alfred/ESSENCE.md`
- `managed/agent_kb/alfred/BEST_PRACTICES.md`
- `managed/agent_kb/alfred/MISTAKES.md`
- `managed/agent_kb/alfred/TEMPLATES.md`
- `managed/agent_kb/alfred/LEARNING_QUEUE.md`
- `managed/agent_kb/alfred/SOURCE_MANIFEST.md`
- `managed/agent_kb/alfred/COVERAGE_AUDIT.md`
- `managed/agent_kb/alfred/README.md`

Proposal/control diffs checked:

- `managed/agent_kb/alfred/appendices/appendix_ingestion_handover/0001_TEMPLATES.diff`
- `managed/agent_kb/alfred/appendices/appendix_ingestion_handover/0003_MISTAKES.diff`
- `managed/agent_kb/alfred/appendices/appendix_ingestion_handover/0004_BEST_PRACTICES.diff`
- `managed/agent_kb/alfred/appendices/appendix_ingestion_handover/0005_ESSENCE.diff`
- `managed/agent_kb/alfred/appendices/appendix_ingestion_handover/0002_0006_0007_0008_RESIDUAL_DIFFS.md`

## Existing ID ranges

| ID family | Existing current range observed | Proposal range observed | Final handling |
|---|---:|---:|---|
| `ALFRED-BP-*` | `001-023` | `024-028` | Merge/add only where not already semantically present. Omit cleanup-artifact doctrine as permanent practice. |
| `ALFRED-MF-*` | `001-023` | `024-028` | Merge/add only where not already semantically present. Omit cleanup-artifact-as-doctrine as permanent failure. |
| `ALFRED-TPL-*` | `001-019` | `020-030` | Split into compact index plus grouped files; preserve existing IDs where possible. |
| `ALFRED-LQ-*` | `001-005` | residual additions | Add candidate-only deferred/source-extension items without promoting runtime truth. |

## Semantic overlap map

| Proposed item | Decision | Target final owner | Notes |
|---|---|---|---|
| Verified direct-route boundary | merge | `ESSENCE.md` | Existing route boundary remains; add compact non-verified-specialist rule only. |
| Daily Command Board boundary | merge | `ESSENCE.md` | Board is Alfred-owned planning model; not downstream execution or silent mutation. |
| Trace/state/pattern boundary | merge | `ESSENCE.md` | Session Export trace, OpState delta candidates, pattern candidate-first. |
| Route-by-function practice | merge | `BEST_PRACTICES.md` | Already partly covered by BP-007/BP-008; refine without duplicate doctrine. |
| Board lock/revision discipline | merge | `BEST_PRACTICES.md` | Already partly covered by BP-017 and MF-018; add compact accepted practice if needed. |
| Priority from trace through packets | merge | `BEST_PRACTICES.md` | Already partly covered by BP-019; add no raw trace priority mutation. |
| Rejected pattern archive practice | add | `BEST_PRACTICES.md` / templates group | Candidate rejection trace is not permanent doctrine beyond general practice. |
| Cleanup-artifact practice | omit | none | Cleanup artifacts are temporary; do not promote permanent scaffold practice. |
| Unverified direct-route drift | add/merge | `MISTAKES.md` | Countermeasure: route through `meta_ops` unless verified. |
| Raw project dump to MetaOps | add/merge | `MISTAKES.md` | Countermeasure: bounded craft-flow handoff. |
| Session trace pollution | merge | `MISTAKES.md` | Existing MF-019 covers direct OpState mutation; final diff refines trace pollution. |
| Rejected candidate trace loss | add | `MISTAKES.md` | Countermeasure: archive rejected candidates. |
| Cleanup artifact as doctrine | omit | none | Do not preserve temporary cleanup history as permanent failure doctrine. |
| `TPL-020` route decision card | merge | grouped routing templates | Merge with existing `TPL-005` and `TPL-007`. |
| `TPL-021` process handover priority card | merge | grouped project packet templates | Merge with existing `TPL-011`. |
| `TPL-022` Daily Command Board compact | merge | grouped daily board templates | Merge with existing `TPL-012`. |
| `TPL-023` Project Packet | merge | grouped project packet templates | Merge with existing `TPL-011`. |
| `TPL-024` MetaOps craft-flow handoff | merge | grouped project packet templates | Merge with existing `TPL-013`. |
| `TPL-025` Session Export correction | merge | grouped trace/state/tracking templates | Merge with existing `TPL-014`. |
| `TPL-026` OpState delta candidate | merge | grouped trace/state/tracking templates | Merge with existing `TPL-015`. |
| `TPL-027` Tracking Record | merge | grouped trace/state/tracking templates | Merge with existing `TPL-016`; keep Alfred-v1 minimal. |
| `TPL-028` Pattern Candidate | merge | grouped pattern-learning templates | Merge with existing `TPL-017`. |
| `TPL-029` Rejected Pattern Archive | add | grouped pattern-learning templates | Keep as reusable archive form unless already present. |
| `TPL-030` Alfred escalation hold | merge | grouped routing templates | Merge with existing escalation/route material. |
| Weekly Preview | defer | `LEARNING_QUEUE.md` | Remove from accepted template index; keep candidate-only. |
| Monthly Direction Map | defer | `LEARNING_QUEUE.md` | Remove from accepted template index; keep candidate-only. |

## Extraction map for template split

| Group file | Source blocks to preserve / merge |
|---|---|
| `templates/routing_templates.md` | Existing `ALFRED-TPL-005`, `ALFRED-TPL-006`, `ALFRED-TPL-007`, `ALFRED-TPL-008`, `ALFRED-TPL-009`, `ALFRED-TPL-030` proposal material. |
| `templates/daily_board_templates.md` | Existing `ALFRED-TPL-012` plus compact board lock controls from proposal `ALFRED-TPL-022`. |
| `templates/project_packet_templates.md` | Existing `ALFRED-TPL-011`, `ALFRED-TPL-013`, proposal `ALFRED-TPL-021`, `ALFRED-TPL-023`, `ALFRED-TPL-024`. |
| `templates/trace_state_tracking_templates.md` | Existing `ALFRED-TPL-014`, `ALFRED-TPL-015`, `ALFRED-TPL-016`, proposal `ALFRED-TPL-025`, `ALFRED-TPL-026`, `ALFRED-TPL-027`. |
| `templates/pattern_learning_templates.md` | Existing `ALFRED-TPL-017`, proposal `ALFRED-TPL-028`, `ALFRED-TPL-029`. |

## Metric cleanup decision

Final accepted signal fields remain:

- `EVD`
- `IMP`
- `RSK`
- scoped `URG` for process handovers, Daily Command Board routing, and time-sensitive handoff priority only.

All non-final metric language from proposal/control artifacts is classified as delete/replace in final scaffold wording, not preserve.

## Validation result

- Duplicate IDs: classified.
- Proposed templates: merge/add/defer/omit classified.
- Metric cleanup: classified.
- Cleanup artifacts: cleanup-bound, not permanent doctrine.
