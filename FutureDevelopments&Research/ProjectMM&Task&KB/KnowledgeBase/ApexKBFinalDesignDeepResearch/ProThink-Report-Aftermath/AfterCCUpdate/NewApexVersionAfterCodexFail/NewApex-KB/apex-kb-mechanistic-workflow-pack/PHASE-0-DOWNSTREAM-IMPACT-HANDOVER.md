# Apex KB Phase 0 Downstream Impact Handover

```yaml
schema: apex.kb.phase0-downstream-impact-handover.v1
status: operator_decisions_locked_patch_required
scope: phase_0_setup_to_later_modules
repository: leela-spec/apexai-os-meta
baseline_commit: 9bb240a122e6f0a1e6f167201b8d6abeaf941bcc
patch_instructions: patches/PHASE-0-SEMANTIC-DEPTH-AND-GIT-SYNC.exact-match.md
```

## 1. Locked Phase 0 decisions

1. The compact Q&A is the operator frontend.
2. The Start adapter transforms it into the existing run-intent, topic-registry, and run-state inputs.
3. Deterministic corpus intelligence must always run at full configured capability.
4. `quick`, `standard`, and `deep` are semantic-execution depth profiles only.
5. The temporary 40/60/80 candidate-coverage mapping is not the semantic-depth model and must be retired.
6. Non-text policy is captured in Setup and consumed by the deterministic corpus-intelligence module.
7. Dirty and untracked files are informational; Apex KB must not rewrite, reset, clean, or stash them.
8. Apex KB must never create or combine worktrees.
9. Start should prefer an updated primary `main` through fetch plus fast-forward-only synchronization. Synchronization failure must remain visible but should not automatically block a new non-overlapping KB destination.

## 2. Semantic-depth handover

All three profiles receive the same deterministic inventory, structure maps, topic maps, duplicate/version facts, and work packs.

| Profile | Semantic behavior |
|---|---|
| `quick` | Use the strongest evidence first, answer locked questions concisely, disposition every candidate, and avoid optional expansion. |
| `standard` | Review the complete bounded work pack with normal authority, contradiction, version, and source-atlas treatment. |
| `deep` | Perform the maximum bounded cross-source reconciliation, evolution analysis, uncertainty treatment, and Macro/Meso/Micro synthesis. |

The semantic module must define concrete token, read, retry, and output expectations. It must not reduce deterministic discovery.

## 3. Output-tier handover

| Operator option | Current runtime route | New module interpretation |
|---|---|---|
| `analysis_only` | Deterministic corpus processing, then semantic Phase 1, then stop | Phase 1 Deterministic + semantic-analysis part of Phase 2 |
| `compiled_kb` | Above plus semantic Phase 2 and independent semantic acceptance | Complete Phase 2 plus acceptance portion of Phase 3 |
| `query_ready` | Above plus postflight and retrieval/index verification | Complete Phase 3 Finish and Prove |

`compiled_kb` maps to the current runtime value `compiled_full`. The legacy `compiled_minimal` tier remains low-level only and is not exposed in the standard Start form.

## 4. Non-text handover

Phase 0 Setup validates and preserves one policy:

| Policy | Required deterministic-module behavior |
|---|---|
| `inventory_and_report` | Inventory every non-text file, do not claim its contents were read, and report extraction gaps. |
| `extract_when_supported` | Use approved available extractors and record extractor identity, output pointers, and failures. |
| `block_on_unsupported` | Block corpus completion when an in-scope file lacks an approved extraction route. |

Required downstream result fields:

```yaml
non_text_policy: ""
non_text_inventory_count: 0
extracted_count: 0
unsupported_count: 0
failed_extractions: []
extraction_artifact_paths: []
blocking_reason: null
```

## 5. Variables removed from the operator surface

The operator no longer supplies:

- KB ID, title, or purpose;
- run ID or KB slug;
- branch/ref or target commit;
- execution route;
- runtime mode;
- success definition;
- output rationale;
- corpus breadth;
- topic or query IDs;
- expected page paths;
- repeated target repository;
- timestamps or schema metadata;
- free-form special constraints.

These values remain internal where current consumers still require them. The Start adapter must derive them deterministically and expose material values in the operator readback.

## 6. Downstream impact by module

### Phase 1 — Deterministic Corpus Intelligence

Must consume:

- repository and source folders;
- structured exclusions;
- KB destination exclusion;
- topics, phrases, and negative terms;
- source-handling policy;
- non-text policy.

Must not consume semantic depth as a reason to truncate inventory, topic maps, duplicate analysis, or structural extraction.

### Phase 2 — Semantic Compilation

Must consume:

- semantic depth;
- locked questions;
- deterministic work packs;
- complete candidate and extraction-gap records;
- source pointers and fingerprints.

It must define how `quick`, `standard`, and `deep` alter semantic effort without changing the locked corpus or questions.

### Phase 3 — Finish and Prove

Must consume:

- selected output tier;
- compiled artifacts;
- independent semantic-acceptance records;
- extraction gaps and blockers;
- deterministic postflight/retrieval status.

It must not mark `query_ready` when required non-text evidence remains blocked or retrieval is stale.

## 7. Git and worktree policy

- Identify the primary worktree through `git worktree list --porcelain`.
- Never create, remove, prune, or combine worktrees.
- Prefer the primary `main` worktree for the run.
- Fetch `origin/main` when possible.
- Use fast-forward-only synchronization when possible.
- Never perform an automatic non-fast-forward merge, rebase, reset, clean, or stash.
- Preserve dirty and untracked files.
- When synchronization cannot complete safely, continue from current local `main` with an explicit warning and resolved commit, provided the configured source and destination remain valid and non-overlapping.

## 8. Required implementation status

The decisions above are not fully installed merely because this handover exists.

Use the exact-match patch file for the proposed live changes. The executor must read every target, prove one exact match per block, apply changes individually, run tests, and report failures without guessing.

## 9. First real test

Use `PHASE-0-FIRST-REAL-TEST-HANDOVER.md` in a new orchestrator chat.

The test target is:

```yaml
repository: leela-spec/leela
source_folder: LeelaAppDevelopment
kb_destination: operator_confirmation_required
stop_after: phase_0_setup
```

The test must stop before deterministic corpus intelligence begins and return the exact Setup artifacts, Git/worktree evidence, test results, blockers, and Phase 1 handover readiness.
