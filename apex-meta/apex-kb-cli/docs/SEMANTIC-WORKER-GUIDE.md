# Apex KB semantic worker guide

## Worker contract

A semantic worker receives one bounded task directory. Read every control file before starting:

```text
TASK.md
task.json
source-allowlist.json
output.schema.json
expected-output-path.txt
```

The packet fixes run identity, configuration hash, task identity, topic, allowed sources, required routes, target questions, output schema, and incoming path. Stop on any disagreement among these files.

The worker may read only allowlisted evidence and must write one JSON result only to the declared incoming path. It must not select the next lifecycle stage, edit control state, change manifests, widen the source set, render canonical pages, build retrieval, or modify source files.

## Phase 1

Review every deterministic candidate exactly once. Preserve source ID, repository path, content hash, read status, disposition, evidence pointers, authority/freshness assessment, duplicate or supersession relationship, questions supported, and uncertainty. Unsupported or unreadable candidates remain visible with an honest blocked disposition.

Candidate rank is a navigation aid, not permission to omit low-ranked, ambiguous, contradictory, historical, prototype, duplicate, or incidental sources. Produce reusable source capsules only as permitted by the packet.

## Phase 2

Return the structured dossier and source atlas required by the packet. The dossier must provide distinct Macro (why), Meso (what it is), and Micro (how) value and answer every locked target question with source pointers. The atlas must preserve every reviewed candidate and disposition exactly once.

The application validates routes and renders Markdown; the worker does not write wiki files directly.

## Independent acceptance

Acceptance must run in a fresh evaluator context that did not draft the pages. Evaluate critical and routine questions from compiled pages, sample material claims against resolved evidence passages, record contradictions and uncertainty, and state whether raw sources still need reopening.

If an independent context is unavailable, return or preserve the exact acceptance handoff and stop before claiming semantic acceptance or `query_ready`. A drafting context must never certify its own work as independent.

## Repair

Invalid output does not advance lifecycle state. Follow the generated bounded repair instruction, preserve packet identity, and replace only the declared incoming result. Do not reinterpret a schema error as authority to change the packet.
