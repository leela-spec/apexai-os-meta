# Apex KB implementation handover

## Evaluation identity

- Intended repository: `leela-spec/apexai-os-meta`
- Intended branch: `agent/apex-kb-python-cli`
- Package: `apex-kb` 1.0.0
- Primary donor sdist SHA-256: `68ab9b5a12dc63c3e4b196122ddfdec75a8d89c84cdef672407361767d865308`
- Supplied wheel SHA-256: `83602eeb6be5fce87654c4e4e122ede9955e2264b902c13e1dbc1cee3fced786`
- Evaluated branch base: `ee69b2d366193ca4d89323cd65731acb776fe960`
- Final published commit: recorded by Git and draft PR #10 when this handover is committed

This document describes the applied implementation tree. Repository-byte compilation and all 49 tests passed. Rebuilt wheel and source-distribution artifacts installed cleanly, and their CLI/template/schema/FTS5/`pypdf` probes passed. Branch CI, push, and PR update remain publication steps.

## Public surface and lifecycle

The console entry point is `apex-kb = apex_kb.cli:main`. Normal commands are `start`, `continue`, `status`, `query`, and `update`; `doctor` is diagnostic. The CLI owns normalized configuration, frozen manifests, atomic state, task packets, validation, postflight, retrieval, updates, migration, and completion.

The lifecycle performs whole-corpus deterministic intelligence, bounded Phase 1 review, Phase 2 dossier/atlas compilation, fresh-context semantic acceptance, postflight, retrieval for `query_ready`, and durable completion. Semantic workers write only declared incoming results and never control transitions.

## Source layout and ownership

- `src/apex_kb/config.py`: normalization, schema validation, canonical Start/readback.
- `src/apex_kb/lifecycle.py`: state transitions, recovery, update/migration, completion.
- `src/apex_kb/corpus/`: deterministic inventory, extraction coordination, topic and impact maps.
- `src/apex_kb/semantic/`: bounded packets, result validation, deterministic rendering.
- `src/apex_kb/retrieval/`: accepted-page chunking, SQLite FTS5, health, query evidence.
- `src/apex_kb/schemas/`: runtime JSON contracts.
- `src/apex_kb/templates/`: packaged operator and semantic task templates.
- `tests/`: lifecycle, corpus, formats, contracts, update, product, and retrieval integrity.

Canonical knowledge remains Markdown and source-preserving evidence. SQLite is derived and rebuildable. Run manifests/state and stage results have distinct ownership; no chat or Skill is a parallel authority.

## Retrieval hardening in the prepared tree

Retrieval accepts only exact frontmatter `status: accepted`, excluding `accepted_pending_evaluation`. Health combines accepted-page hashes, current run/config identity, database SHA-256, embedded metadata equality, SQLite `PRAGMA integrity_check`, an FTS5 table/runtime probe, and exact row count. Focused tests cover each boundary and repeated-build identity.

## Evidence and limitations

The supplied synthetic and connector-backed subset evidence is preserved unchanged under `evidence/canaries/`. The synthetic canary proves lifecycle mechanics and contracts with a deterministic fixture worker, not independent semantic quality. Its absolute `/mnt/data/work/...` package path is historical and nonportable.

The connector-backed evidence is a one-file excerpt projection, not the full Leela corpus. It records a full-corpus export blocker and must not be represented as completion of the required local real canary.

The committed `evidence/canaries/light-smoke/` packet records a one-source, one-candidate, two-query public-CLI run that reached `query_ready` after independent acceptance, postflight, retrieval, and completion. It is lifecycle proof only, not a Leela semantic-quality claim. A full Leela run was invalidated when the corpus changed during execution and is not committed.

## Pending final work

1. Commit only the intended Apex KB implementation, documentation, tests, and evidence.
2. Push `agent/apex-kb-python-cli` and update draft PR #10 without merging it.
3. Confirm branch CI passes.
4. Run a fresh full Leela Skill Tree canary only after the source corpus is stable and its pre-run fingerprint is locked.
