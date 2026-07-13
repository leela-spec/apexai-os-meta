# Browser Git Connector Semantic Runbook

## Capability boundary

Use this route only when complete repository-file reads and reliable whole-file writes are available but terminal execution is not. Account-level Skills are optional. Repository-local `semantic-contract/` files are sufficient authority. Never run or claim scaffold, intake, hashing, manifest mutation, Phase 0 regeneration, index/retrieval rebuild, lint, quality, postflight, or deterministic validation from this route.

## Startup target lock

1. Read every repository-local semantic contract file, the topic registry, Phase 0 rankings, and any existing ledger for the selected topic.
2. Confirm stable target-query IDs, priorities, answer requirements, and expected page routes before selecting sources.
3. If a compiled topic has no target queries, stop semantic drafting and report `partial: missing_target_queries`.

## One-topic compilation

1. Use Phase 0 rankings only to nominate candidates.
2. Prefer canonical specifications; then implementation evidence for current-state questions; current contracts/updates; user stories and examples; then historical or proposed material.
3. Open the complete source or every relevant section needed for the locked questions. Never infer from filenames, snippets, rankings, or prior summaries.
4. Update the topic ledger after every source and before context ends. Distinguish `unopened`, `targeted`, `complete`, and `blocked`; distinguish candidate, reviewed, and materially used.
5. Continue source reading while a known readable source can answer an unresolved critical/routine query.
6. Write Phase 1 analysis with query linkage and explicit concept/entity dispositions. Read it back in full.
7. Choose page topology by recurring retrieval value and duplication reduction. Draft complete answer-bearing pages, not boundary notices. Read every written page back in full.
8. Classify reopen triggers as `evidence_unavailable`, `evidence_conflict`, `future_change`, or `readable_unopened`; the last blocks completion for critical/routine queries.
9. Report `partial` if connector reliability, context, or evidence access prevents completion.

## Interrupted-context recovery prompt

```text
Resume one Apex KB semantic topic from repository files only. Read the repository-local semantic contract, topic registry entry, complete topic ledger, referenced Phase 1 analyses, and current compiled pages. Treat the ledger as navigation, not evidence. Reopen every source whose exact passage is needed before making a claim. Continue from the first unresolved critical/routine query. Do not certify your own output or perform deterministic work.
```

## Clean-context page-only evaluator prompt

```text
Evaluate one topic without drafting context. Read its target queries and compiled pages first. For each query, answer only from compiled pages, cite the exact page section, and return answerable, partial, not_answerable, or blocked. Then identify any answer requirement absent from the pages. Do not inspect raw sources until the page-only verdicts are fixed. Afterward inspect only the resolved evidence passages supplied for verification. Return reason-coded repairs and a semantic verdict. No numeric score, file-count proxy, or self-report may establish a pass.
```

## Claim-entailment evaluator prompt

```text
Independently select at least two material claims from each page, or all claims when fewer exist. Compare each claim with its resolved source passage. Return supported, partially_supported, contradicted, or unresolvable, with page and source pointers. A semantic pass requires all sampled material claims to be supported.
```

## Deterministic handoff

Provide the run ID, topic ledgers, created/updated Phase 1 and Phase 2 files, semantic-acceptance artifacts, unresolved blockers, and truthful state. Stop at `compiled_unvalidated`. A terminal-backed executor must validate schemas, lint/quality wiring, index/retrieval freshness, and postflight before `query_ready`.
