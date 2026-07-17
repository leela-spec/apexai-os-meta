# Apex KB Semantic Value Contract v3

## Canonical authority

| Concern | Owner |
|---|---|
| Operator choices before confirmation | `manifests/run-config.okf.json` |
| Confirmed immutable configuration | `manifests/run-manifest.json` |
| Lifecycle progress and next stage | `manifests/run-state.json` |
| Topic vocabulary and target questions | `manifests/topic-registry.json` |
| Phase 0 source routing | `manifests/phase0/topic-source-rankings.json` and work pack |
| Semantic task scope | generated instruction file |
| Semantic procedure | stable Phase 1/2 prompt template plus batch guide |
| Completion | independent semantic acceptance plus deterministic postflight |

Chat memory is never a canonical owner.

## Intake and lock

1. The start command renders the fixed welcome and input shape.
2. The operator saves `run-config.okf.json`.
3. Schema validation and read-only preflight run before source intake.
4. The operator confirms the compact preflight readback.
5. The control plane writes `run-manifest.json`, computes the canonical configuration SHA-256, and initializes state.
6. Every later stage checks that hash. A mismatch blocks and invalidates from the earliest affected stage.

The lock is logical workflow custody. It is not encryption or an operating-system file lock.

## Question contract

- The operator locks the primary topic, intent, strong vocabulary, and priority questions at the beginning.
- A fixed coverage matrix adds predictable checks for definition, structure, workflow, ownership, rules, relationships, present/proposed/open state, examples/edge cases, and source landscape where material.
- Phase 0 may report missing evidence signals but cannot rewrite or invent target questions.
- New target questions require a new operator-confirmed configuration/registry revision.
- The standard new-KB run contains one primary topic. Additional topics belong in another run or the future update lifecycle.

## Phase 0 contract

Phase 0 is deterministic. It inventories every in-scope file, extracts path/title/H1/heading/body/link/date/duplicate signals, emits exhaustive candidate rankings without top-N truncation, creates one bounded work pack, and writes a corpus/topic statistics report. Signals guide reading only; they never establish semantic authority.

## Phase 1 contract

- One generated instruction file controls each bounded source batch.
- The AI sees one topic, locked questions, at most four ordinary sources, exact pointers, exact writes, and exact validation rules.
- The AI may judge meaning, relevance, authority, contradiction, and source value only inside that boundary.
- Each batch updates the cumulative topic analysis and semantic ledger.
- The control plane reconciles outputs and either emits a next batch, a reason-coded repair instruction, or a topic-finalization instruction.
- Source count and rank are never completion criteria.

## Phase 2 contract

- Phase 2 receives validated Phase 1, not the raw corpus by default.
- The generated instruction file declares the exact dossier, source atlas, and any explicitly approved concept/entity pages.
- Claims, present/proposed/open state, source hashes, pointers, candidate dispositions, contradictions, and uncertainty carry forward.
- The AI may not invent pages, paths, topics, questions, or next stages.

## Acceptance contract

A fresh evaluator receives compiled pages, locked questions, and evidence—but not drafting rationale. `semantic_pass` requires every critical/routine question to be answerable and every sampled material claim to be supported. Structural checks can reject an artifact but cannot manufacture a semantic pass.

## Truthful states

- `analysis_complete_unvalidated`: Phase 1 complete; accepted Phase 2 absent.
- `partial`: material evidence, question, output, or acceptance gap remains.
- `compiled_unvalidated`: semantic acceptance passes; deterministic postflight pending.
- `query_ready`: semantic acceptance, postflight, and retrieval freshness pass.
