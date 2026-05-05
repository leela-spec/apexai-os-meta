# Safe Unified Diff Creation Plan

## Purpose

Create final unified diffs for Alfred KB finalization through small, context-safe iterations.

This plan covers only the creation of final unified diff proposals. It does not apply scaffold patches, move files, delete files, or perform final cleanup.

## Validated decisions used as input

Source decision register: `NewIntegration.md` / validated operator decision set from the Alfred KB finalization discussion.

Validated posture:

- Proposal/control diffs are temporary execution artifacts.
- Execute validated diffs first, then delete proposal/control artifacts in a later cleanup pass.
- Before creating final diffs, check overlap and merge instead of duplicating.
- Remove all superseded metric vocabulary from final scaffold wording.
- Use only `EVD`, `IMP`, `RSK`, and scoped `URG`.
- If templates become too large, create a template index plus grouped template files.
- Daily Command Board is an Alfred-owned operating model.
- CF1-CF4 are canonical enough for compact scaffold constraints.
- Non-verified specialists route through `meta_ops`.
- Weekly Preview is deferred.
- Monthly Direction Map is deferred.
- Cleanup-artifact doctrine/practice entries are omitted as permanent scaffold content because cleanup artifacts will be deleted.

## Hard constraints

- Produce unified diffs only.
- Do not patch target scaffold files during this planning phase.
- Do not rewrite entire files when a smaller context patch is possible.
- Do not introduce duplicate IDs.
- Preserve existing IDs where possible and merge new content into existing entries.
- Do not keep references to superseded metrics as historical notes, mappings, or examples.
- Do not create permanent README entries for proposal folders that will be deleted.
- Do not move files by rewrite. When a split is needed, create new files by exact content extraction or explicitly generated new grouped-template content.
- Every diff must be reviewable as a standalone patch.
- Every diff must include enough surrounding context to avoid unsafe application.

## Target outputs

Final diff files should be created under:

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs/
```

Recommended final diff package:

```text
0001_ESSENCE_FINAL.diff
0002_BEST_PRACTICES_FINAL.diff
0003_MISTAKES_FINAL.diff
0004_TEMPLATES_INDEX_FINAL.diff
0005_TEMPLATE_GROUPS_FINAL.diff
0006_LEARNING_QUEUE_FINAL.diff
0007_SOURCE_MANIFEST_FINAL.diff
0008_COVERAGE_AUDIT_FINAL.diff
0009_README_FINAL.diff
0010_CLEANUP_PLAN_FINAL.diff
```

`0010_CLEANUP_PLAN_FINAL.diff` should be a diff proposal only if cleanup artifacts are represented in tracked files. If cleanup is a deletion-only repo operation with no lasting file content, keep cleanup as an executor note rather than scaffold doctrine.

## File move / split policy

### Required split

The template surface should be split if the final template set remains larger than a compact index.

Recommended target structure:

```text
managed/agent_kb/alfred/TEMPLATES.md
managed/agent_kb/alfred/templates/routing_templates.md
managed/agent_kb/alfred/templates/daily_board_templates.md
managed/agent_kb/alfred/templates/project_packet_templates.md
managed/agent_kb/alfred/templates/trace_state_tracking_templates.md
managed/agent_kb/alfred/templates/pattern_learning_templates.md
```

### Drift guard

Do not simulate a move by rewriting existing template content from memory.

For each extracted template group:

1. Fetch current `TEMPLATES.md`.
2. Identify exact existing template blocks to keep.
3. Copy exact blocks into grouped files where preservation is required.
4. Apply only intentional edits from the validated decision register.
5. Keep a block-level extraction map in the diff package notes.

### Template split decision

Use a split if all of the following are true:

- routing, board, project packet, trace/state/tracking, and pattern templates all remain accepted;
- `TEMPLATES.md` would otherwise be a long mixed-purpose file;
- grouped files can be named by function and referenced from the index.

## Iteration model

Each iteration creates one or more final unified diffs and includes its own validation checklist.

### Iteration 0 - Baseline inventory and duplicate map

Create no scaffold diff yet.

Actions:

1. Fetch current target files:
   - `ESSENCE.md`
   - `BEST_PRACTICES.md`
   - `MISTAKES.md`
   - `TEMPLATES.md`
   - `LEARNING_QUEUE.md`
   - `SOURCE_MANIFEST.md`
   - `COVERAGE_AUDIT.md`
   - `README.md`
2. Fetch current proposal diffs:
   - `0001_TEMPLATES.diff`
   - `0003_MISTAKES.diff`
   - `0004_BEST_PRACTICES.diff`
   - `0005_ESSENCE.diff`
   - `0002_0006_0007_0008_RESIDUAL_DIFFS.md`
3. Build an ID map:
   - existing `ALFRED-BP-*`
   - existing `ALFRED-MF-*`
   - existing `ALFRED-TPL-*`
   - existing `ALFRED-LQ-*`
   - proposed new IDs
4. Build a semantic overlap map.
5. Mark each proposed addition as:
   - merge into existing ID
   - add as new ID
   - defer
   - omit

Output:

```text
final_unified_diffs/0000_DUPLICATE_AND_EXTRACTION_MAP.md
```

Validation:

- No duplicate IDs remain unclassified.
- Every proposed template has a merge/add/defer/omit decision.
- Every old metric term occurrence has a delete/replace decision.

### Iteration 1 - ESSENCE final diff

Create:

```text
final_unified_diffs/0001_ESSENCE_FINAL.diff
```

Scope:

- Add or refine compact canonical boundary doctrine for:
  - verified direct-route boundary;
  - Daily Command Board boundary;
  - trace/state/pattern boundary;
  - Alfred-owned board, not downstream execution;
  - CF1-CF4 compact constraints only;
  - non-verified specialists route through `meta_ops`.
- Remove superseded metric mapping table and all historical references to old metric vocabulary.
- Keep only `EVD`, `IMP`, `RSK`, and scoped `URG`.
- Preserve existing ESSENCE structure where possible.

Do not include:

- full appendix schemas;
- detailed Sequencing implementation;
- XP/min ranking as an Alfred metric;
- exact 5V workflow;
- mobile voice-to-markdown workflow;
- permanent cleanup-artifact doctrine.

Validation:

- Search diff result for banned terms:
  - `value / urgency / leverage / fit` as a metric system;
  - old mapping table language;
  - cleanup artifact as permanent doctrine.
- Confirm `URG` appears only in process-handover / Daily Board / craft-flow priority scope.

### Iteration 2 - BEST_PRACTICES final diff

Create:

```text
final_unified_diffs/0002_BEST_PRACTICES_FINAL.diff
```

Scope:

- Merge route-by-function practice without duplicating ESSENCE.
- Add or merge board lock/revision discipline.
- Add or merge priority-from-trace-through-planning-packets rule.
- Add or merge rejected pattern archive practice.
- Add compact workflow selection matrix if not already covered.
- Omit permanent cleanup-artifact practice entry unless generalized and not tied to temporary folders.

Validation:

- No duplicate best-practice IDs.
- No practice restates ESSENCE verbatim.
- No old metric vocabulary remains.
- Every practice has owner, validator, source basis, and stop condition if machine-contract style is used.

### Iteration 3 - MISTAKES final diff

Create:

```text
final_unified_diffs/0003_MISTAKES_FINAL.diff
```

Scope:

- Add or merge:
  - unverified direct-route drift;
  - raw project dump to MetaOps;
  - Session trace pollution;
  - rejected candidate trace loss.
- Omit permanent cleanup-artifact-as-doctrine failure unless rewritten as a general temporary-artifact failure not tied to folders that will be deleted.

Validation:

- No mistake pattern without countermeasure.
- No duplicate mistake IDs.
- No failure entry exists only to preserve temporary cleanup process history.

### Iteration 4 - Template architecture final diffs

Create:

```text
final_unified_diffs/0004_TEMPLATES_INDEX_FINAL.diff
final_unified_diffs/0005_TEMPLATE_GROUPS_FINAL.diff
```

Scope for `0004_TEMPLATES_INDEX_FINAL.diff`:

- Convert `TEMPLATES.md` into compact canonical template index if split is used.
- Keep template posture and invalid-use rules.
- Reference grouped files by function.
- Preserve only the smallest always-used forms in the index if necessary.

Scope for `0005_TEMPLATE_GROUPS_FINAL.diff`:

Create grouped files under:

```text
managed/agent_kb/alfred/templates/
```

Grouped file allocation:

| Group file | Contains |
|---|---|
| `routing_templates.md` | route decision card, compact route brief, escalation hold / route decision |
| `daily_board_templates.md` | Daily Command Board compact, CF1-CF4 board fields, board lock controls |
| `project_packet_templates.md` | process handover priority card, Project Packet, MetaOps craft-flow handoff |
| `trace_state_tracking_templates.md` | Session Export correction, OpState delta candidate, Tracking Record |
| `pattern_learning_templates.md` | Pattern Candidate, Rejected Pattern Archive |

Merge rules:

- Existing TPL-005 and TPL-007 merge with proposed TPL-020.
- Existing TPL-011 merges with proposed TPL-021 and TPL-023.
- Existing TPL-012 merges with proposed TPL-022.
- Existing TPL-013 merges with proposed TPL-024.
- Existing TPL-014 merges with proposed TPL-025.
- Existing TPL-015 merges with proposed TPL-026.
- Existing TPL-016 merges with proposed TPL-027 and remains Alfred-v1 minimal.
- Existing TPL-017 merges with proposed TPL-028.
- Proposed TPL-029 is kept as rejected pattern archive unless already present.
- Proposed TPL-030 merges with existing escalation material.
- Weekly Preview is deferred.
- Monthly Direction Map is deferred.

Validation:

- No duplicate template IDs.
- No duplicated template titles.
- `TEMPLATES.md` links to every grouped file.
- Grouped files do not define governance.
- No old metric vocabulary remains.
- Any copied content is copied exactly unless listed as an intentional edit.

### Iteration 5 - LEARNING_QUEUE final diff

Create:

```text
final_unified_diffs/0006_LEARNING_QUEUE_FINAL.diff
```

Scope:

- Add candidate-only future items:
  - process-priority calibration from real boards;
  - exact day-start/day-close protocol;
  - exact 5V workflow;
  - mobile voice-to-markdown intake;
  - detailed Leela workflow surface split into scaffold-high-level vs appendix/deferred product mechanics.
- Ensure weekly preview and monthly direction map are deferred if not already represented.

Validation:

- All entries are candidate-only.
- No learning item is described as runtime truth.
- No source-gap item is hardened as accepted doctrine.

### Iteration 6 - SOURCE_MANIFEST final diff

Create:

```text
final_unified_diffs/0007_SOURCE_MANIFEST_FINAL.diff
```

Scope:

- Record appendix source classes and source-extension inputs.
- Treat uploaded Alfred/Leela source files as finalization-source input if directly represented in the source/audit plan.
- Separate source/content appendices from temporary process-control artifacts.
- Do not add permanent doctrine claims.

Must classify:

- Alfred role docs;
- Sequencing SSOT update;
- Daily Flows;
- Craft Flows;
- Sequencing science/rationale;
- Sequence builder/settings examples;
- KB base build index;
- existing appendix source files;
- temporary proposal/control folders as cleanup-bound, not doctrine.

Validation:

- No `not_accessible` status remains for attached/read source material that was used in finalization.
- No process-control folder is listed as doctrine source.
- README references align with final cleanup lifecycle.

### Iteration 7 - COVERAGE_AUDIT final diff

Create:

```text
final_unified_diffs/0008_COVERAGE_AUDIT_FINAL.diff
```

Scope:

- Record coverage outcomes from the validated decision register.
- Mark scaffold-now, appendix-now, appendix-deferred, delete-after-ingestion, and omitted areas.
- Include clear status for:
  - Daily Command Board;
  - CF1-CF4;
  - template split;
  - metric-system cleanup;
  - Sequencing high-level vs detailed implementation;
  - 5V deferred;
  - mobile intake deferred;
  - weekly preview deferred;
  - monthly direction map deferred.

Validation:

- Coverage audit mirrors validated decisions.
- No deferred item appears as accepted scaffold.
- No deleted artifact appears as final source authority.

### Iteration 8 - README final diff

Create:

```text
final_unified_diffs/0009_README_FINAL.diff
```

Scope:

- Update README to point to final scaffold and template group structure if template split is used.
- Do not add permanent handover-folder navigation for folders that will be deleted.
- If needed, add a short statement that final template groups live under `managed/agent_kb/alfred/templates/`.

Validation:

- No references to final-deleted proposal folders.
- No README doctrine beyond navigation.
- All listed scaffold files exist in the final diff package.

### Iteration 9 - Cleanup diff / cleanup note

Create only if needed:

```text
final_unified_diffs/0010_CLEANUP_PLAN_FINAL.diff
```

Scope:

- If cleanup requires tracked-file changes, prepare deletion diffs or README/source-manifest adjustments.
- If cleanup is simply deleting temporary proposal/control folders after successful ingestion, create an executor note instead of permanent scaffold content.

Deletion candidates after successful ingestion:

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/
managed/agent_kb/alfred/appendices/cleanup_patch_proposals/
```

Validation:

- Cleanup is not encoded as permanent Alfred doctrine.
- Final README and source/audit files do not point to deleted temporary artifacts.

## Global validation after all final diffs are created

Run these checks before applying any final diff package:

1. Duplicate ID scan:
   - `ALFRED-BP-`
   - `ALFRED-MF-`
   - `ALFRED-TPL-`
   - `ALFRED-LQ-`
2. Banned metric vocabulary scan:
   - old four-field metric model;
   - historical mapping table;
   - metric use of value, urgency, leverage, or fit.
3. Template index link check.
4. Deleted-folder reference check.
5. Source-status consistency check.
6. Weekly Preview and Monthly Direction Map deferred-status check.
7. Scaffold-vs-appendix boundary check.
8. Unified diff apply dry-run in order.

## Final diff apply order, after review

When the final diff package is approved, apply in this order:

```text
0000_DUPLICATE_AND_EXTRACTION_MAP.md      # reference only
0001_ESSENCE_FINAL.diff
0002_BEST_PRACTICES_FINAL.diff
0003_MISTAKES_FINAL.diff
0004_TEMPLATES_INDEX_FINAL.diff
0005_TEMPLATE_GROUPS_FINAL.diff
0006_LEARNING_QUEUE_FINAL.diff
0007_SOURCE_MANIFEST_FINAL.diff
0008_COVERAGE_AUDIT_FINAL.diff
0009_README_FINAL.diff
0010_CLEANUP_PLAN_FINAL.diff or cleanup note
```

Reasoning:

- ESSENCE first locks boundaries.
- Practices and mistakes then align to boundaries.
- Templates then split/merge under those boundaries.
- Learning queue captures deferred items after scaffold scope is clear.
- Source/audit files record final coverage.
- README updates only after final structure is known.
- Cleanup happens last.
