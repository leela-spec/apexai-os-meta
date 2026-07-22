# Testing and canary evidence

## Required final validation

Run these commands from the final committed package bytes:

```powershell
python -m compileall -q src
python -m pytest tests -q
python -m build .
```

Use clean installations of the resulting wheel and source distribution to verify CLI help, all public commands, packaged schemas/templates, FTS5, PDF extraction when `pypdf` is installed, drift rejection, atomic interruption recovery, fresh-process resume, deterministic Phase 0 rerun, deterministic retrieval rebuild, and selective update invalidation.

Repository-byte validation on 2026-07-21 passed `compileall` and all 49 tests. Rebuilt wheel and source-distribution artifacts installed cleanly; CLI help, packaged schemas/templates, FTS5, and `pypdf` probes passed. These results test the implementation tree applied to `agent/apex-kb-python-cli`; final branch CI remains authoritative after publication.

## Focused retrieval checks

`tests/test_retrieval_integrity.py` covers exact accepted-page status, SQLite integrity, FTS5 runtime health, embedded metadata/database identity, manifest drift rejection, and repeated-build database identity.

## Supplied evidence boundaries

`evidence/canaries/synthetic-nine-topic-canary.json` records a 650-file, nine-topic lifecycle and contract canary. Its own `semantic_claim_limit` states that it does not prove independent semantic quality. Its `semantic_executor` is a deterministic fixture worker. The `package_artifact` value is a historical, nonportable build-container path (`/mnt/data/work/...`), retained unchanged as provenance rather than presented as a current local path.

`evidence/canaries/connector-backed-leela-subset.json` records a connector-backed projection from one Leela source file. It identifies repository, ref, blob SHA, source path, and fetched line ranges. Its `projection_limit` states that it is not a complete byte-identical repository file; its semantic prose is fixture-generated; and the full-corpus canary is explicitly `blocked_external_repository_export`. Its `query_ready` status applies only to the excerpt projection.

Neither supplied JSON file is evidence that the required final local Leela Skill Tree canary passed. Preserve both files unchanged and keep their limitation fields visible.

## Lightweight end-to-end smoke canary

`evidence/canaries/light-smoke/` records a deliberately tiny public-CLI run with one synthetic Markdown source, one topic, one candidate, and two target questions. Bounded Phase 1 and Phase 2 workers ran in separate contexts, and a third fresh context returned `semantic_pass` after page-only evaluation and four material-claim checks. Postflight, SQLite FTS5 retrieval, completion certification, and both target queries passed. The run reached `query_ready` with database SHA-256 `78bb2c1d58c3c4c5a07762789b4785c316ce5109987e546845d1a6158186ca99`.

This smoke canary proves the complete local lifecycle and its fail-closed repair path on a minimal fixture. It does not prove semantic quality or coverage for the changing Leela corpus.

## Real canary truthfulness

Before and after a real canary, record the Leela repository commit and status. Use `pointer_only` and an external destination. Preserve source inventory, candidate counts, dispositions, compiled pages, independent acceptance, retrieval identity, target-question query results, warnings, and source-tree immutability proof. If independent acceptance cannot run in a genuinely fresh context, stop at the handoff packet and report that state.

A full local Leela run was intentionally not accepted as evidence on 2026-07-21 because the source corpus changed materially while it was running. The operator narrowed validation to the lightweight smoke canary. No output from the interrupted Leela run is committed here.
