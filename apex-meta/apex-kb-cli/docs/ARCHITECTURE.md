# Apex KB architecture

## Authority and boundaries

The `apex-kb` Python application is the lifecycle authority. Configuration, manifests, atomic state, legal next actions, task packets, imported semantic results, postflight, retrieval, and completion are owned by the application. The optional Codex Skill launches public commands or executes one generated semantic packet; it does not derive paths or transitions.

Configured source repositories are read-only. Source custody is explicit: `pointer_only` records identity without copying, while `copy_into_kb` and `snapshot_copy` preserve relative paths and verify hashes before accepting bytes.

## Control plane

`run-config.yaml` is the normalized operator input. `run-manifest.json` freezes run identity, canonical configuration hash, corpus scope, topic contracts, and artifact routes. `run-state.json` is atomically replaced and records the current durable transition. Stage results and completion certificates are evidence, not alternate state authorities.

`continue` derives one action from these files and referenced artifacts. It fails closed on schema, identity, source-drift, route, completeness, or lifecycle mismatches. Bounded repair instructions do not advance state.

## Data plane

Deterministic corpus intelligence inventories every discovered file or explicit exclusion and publishes field-separated match evidence, duplicate relationships, exhaustive topic candidates, and extraction status. Deterministic scoring and path rules are navigation hints, never semantic authority.

Phase 1 reviews every candidate and produces reusable content-hash source capsules plus a topic analysis. Phase 2 produces a structured dossier and source atlas. Independent acceptance evaluates page-only answerability and sampled material claims before the application promotes page frontmatter from `accepted_pending_evaluation` to the exact status `accepted`.

## Retrieval

Only pages with exact frontmatter `status: accepted` enter retrieval. Pages are split on headings with page/chunk hashes, source IDs, and exact line spans. SQLite FTS5 is a rebuildable derivative; Markdown remains canonical.

Retrieval health verifies:

- current run/config identity and unchanged accepted-page hashes;
- the recorded database SHA-256;
- exact equality between embedded database metadata and the index manifest;
- `PRAGMA integrity_check` returning only `ok`;
- the expected FTS5 table and a live `MATCH` probe;
- exact indexed-row count.

Queries fail closed on a stale or unhealthy index unless the operator explicitly requests stale access.

## Updates and completion

An update archives prior control evidence, rebuilds deterministic intelligence, classifies additions, changes, deletions, identical-content moves, and unreadable files, and invalidates only affected semantic work. Unchanged capsules and accepted topic outputs may be reused when their contracts remain valid.

`query_ready` requires semantic acceptance, deterministic postflight, healthy retrieval, and durable completion certificates. It is not inferred from file counts, package metadata, or the presence of a database.
