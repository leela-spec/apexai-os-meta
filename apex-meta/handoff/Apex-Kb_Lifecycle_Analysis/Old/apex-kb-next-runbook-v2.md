# Apex KB Next Runbook v2

## 0. Inputs

- `kb_slug`
- source root(s)
- source authority policy
- risk domain
- desired language
- operator constraints

## 1. Deterministic preparation

1. Load installed `apex-kb` skill.
2. Resolve one KB root: `apex-meta/kb/<kb-slug>/`.
3. Scaffold if needed.
4. Intake or point to sources.
5. Hash sources and update manifest.
6. Run Phase 0 corpus intelligence.
7. Produce or verify:
   - corpus profile
   - heading/frontmatter/link maps
   - topic-file map
   - source-priority candidates
   - noisy-source report
   - table-heavy/PDF risk report

## 2. Phase 1 semantic ingest

1. Read Phase 0 navigation first.
2. Select high-signal sources.
3. Use source-specific analysis for high-risk legal, tax, medical, financial, or operational claims.
4. Use grouped analysis only for low-risk homogeneous sources.
5. Every Phase 1 report includes:
   - source coverage ledger
   - source paths and hashes/no-hash reasons
   - key claims with pointers
   - contradictions
   - open questions
   - proposed summary/concept/entity pages
6. Halt after Phase 1.

## 3. Approval gate

Proceed to Phase 2 only after the exact separate operator phrase:

```text
approve ingest
```

## 4. Phase 2 compile

Generate in this order:

1. Summary pages.
2. Concept pages.
3. Entity pages.
4. Wiki semantic index section.
5. Audit/risk items.
6. Query packets if useful.

Each page must expose:

- source refs
- source path
- source hash or no-hash reason
- source pointer
- confidence
- claim label
- open questions
- review flags

## 5. Postflight

1. Rebuild deterministic index.
2. Rebuild retrieval index.
3. Run lint.
4. Run audit.
5. Run status/stale checks.
6. Run 5-10 query simulations.
7. Save reusable query packets for common future questions.

## 6. Final report

Report only what is verified:

- what exists
- what is source-grounded
- what is semantically reliable
- what is risky
- what is missing
- what must happen next

## Compact operator prompt template

```text
Run Apex KB for <kb_slug>.
Mode: <phase0 | phase1 | phase2 | postflight | query-test>.
Target root: apex-meta/kb/<kb_slug>/.
Boundaries: repo-local only; do not mutate Apex Plan/Sync/Session/PreCap/FlowRecap/APSU; no PRs/issues/comments/reviewers/assignees/external sharing.
Stop condition: <exact stop condition>.
Use the installed apex-kb skill and do not duplicate its script details in this prompt.
```
