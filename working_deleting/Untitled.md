# Apex KB Semantic-Value Closure Implementation Plan

## Summary

Update `apex-kb` so semantic compilation is complete only when compiled pages answer locked priority questions from actually reviewed evidence. Structural validity, file counts, headings, rankings, and drafter self-review remain necessary but cannot establish semantic completion.

Use `deterministic-markdown-patcher2` solely as the mutation control plane for existing Markdown and JSON contracts. The Apex KB skill remains the content being repaired. Prove the update through a browser/Git-connector Leela canary before merging to `main`.

## 1. Safe Patch Execution

- Create isolated worktrees for `apexai-os-meta` and the later Leela canary, preserving unrelated dirty files.
- Create temporary `patch_policy.v1` and `patch_intent.v1` artifacts outside the repositories.
- Apex policy will allow only the Apex KB skill package Markdown/JSON files; all other paths are protected and full-file rewrites are forbidden.
- Express each existing-file change as one `replace-heading-section` intent with a unique heading path, semantic hints, expected/forbidden phrases, and `max_files_touched: 1`.
- For every intent run: `validate-intent` → `locate` → `extract-span` → reviewed `apply-intent --allow-write` → executor `diff`.
- Stop on zero/multiple matches, ambiguous headings, validation failure, or unexpected diff paths.
- Create genuinely new files with `apply_patch` because the patcher executor has no create-file operation. Modify Python separately with `apply_patch`; never represent Python edits as Markdown-patcher work.
- Run `git diff --check` and an exact changed-path allowlist before staging.
- Produce separate commits for the Apex contract/runtime update and the Leela canary. Merge and push `main` only after their respective gates pass.

## 2. Apex KB Contract and Interface Changes

### Completion target and lifecycle

Update the Apex KB entrypoint and operating references to establish:

- `compiled_minimal` means the minimum useful page topology, never minimal content.
- Phase 0 rankings nominate candidate sources; they do not establish authority, evidence use, or topic completeness.
- A topic cannot begin semantic source selection until target questions and answer requirements are locked.
- A known readable canonical source that can answer a critical unresolved question is a continuation condition, not a reopen trigger.
- Connector cost, source length, context pressure, or write friction may cause `partial`; they cannot lower completion criteria.
- A clean-context semantic acceptance pass is required before `compiled_unvalidated`.
- `query_ready` still requires semantic acceptance, deterministic postflight, and fresh retrieval.
- Completion reports lead with question coverage, source-use coverage, acceptance verdicts, and unresolved blockers—not artifact counts.

Truthful states become:

- `analysis_complete_unvalidated`: Phase 1 complete without Phase 2 acceptance.
- `partial`: material query, evidence, page architecture, or semantic acceptance gaps remain.
- `compiled_unvalidated`: all critical/routine target questions pass semantic acceptance, but deterministic postflight has not run.
- `query_ready`: semantic acceptance passes and deterministic postflight/retrieval are current.

### Topic registry v2

Extend each topic entry with:

```
target_queries:
  - query_id: "<stable-topic-query-id>"
    question: "<question future AIs must answer>"
    priority: "critical | routine | supporting"
    answer_requirements: []
    expected_page: "wiki/..."
```

Rules:

- Registry entries remain backward-readable.
- Empty target queries remain valid for `source_only` and early `analysis_only`.
- Any compiled tier requires target queries for every in-scope topic.
- Query quantity is adaptive; broad topics must cover material definition, structure, workflow, ownership, rules, relationships, current/future state, examples, and edge cases where applicable.
- Topic `complete` is valid only when all critical/routine queries have accepted routes and semantic-pass evidence.

### Semantic run ledger

Define machine-readable per-topic ledgers under:

```
log/semantic-runs/<run-id>/topics/<topic-slug>.json
```

Each ledger records:

- stable target queries and answer status;
- candidate source, Phase 0 rank, duplicate status, authority class, and availability;
- `read_status: complete | targeted | blocked | unopened`;
- exact sections/passages reviewed;
- Phase 1 analysis reference;
- query IDs supported;
- claims/pages using the source;
- unanswered questions and next source/action;
- page architecture decisions;
- concept/entity candidate dispositions;
- completion blockers.

An unopened source never appears as supporting evidence. Targeted reading is acceptable only when all relevant sections and remaining question coverage are recorded.

### Phase 1 contract

Extend the analysis template with:

- target-query linkage;
- source-read and authority record;
- questions answered, partially answered, contradicted, blocked, or not covered;
- additional evidence required;
- concept/entity disposition:
    - `promote`;
    - `embed_in_summary`;
    - `defer_blocked`;
    - `reject_no_independent_value`;
- disposition rationale, affected query IDs, and destination page;
- explicit topic completion effect: `supports`, `partial`, or `blocks`.

No candidate may disappear between Phase 1 and Phase 2 without a disposition.

### Phase 2 contract

Add `semantic_contract_version`, `semantic_run_id`, and `target_query_ids` to v2 page frontmatter.

Add a required `Target Questions Answered` section containing direct answer routes and page pointers.

Adaptive Ranked Source Set entries must include:

- source ID and path;
- original Phase 0 rank when available;
- analysis reference;
- reviewed status;
- supported query IDs;
- claim IDs using the source;
- rationale and coverage.

Only reviewed and materially used sources belong in that section. Unreviewed candidates remain in the semantic ledger.

Retain Macro/Meso/Micro, Key Claims, Routes Here, and uncertainty sections, but:

- prohibit duplicated YAML/prose copies of the same claims and source lists;
- require pages to answer their declared questions directly;
- prohibit boundary-only orientation pages from satisfying broad domain topics;
- classify every reopen trigger by evidence availability and completion effect;
- make `readable_unopened` a completion blocker for critical/routine questions.

Remove the rule that a generic pointer-only concept/entity page can be considered complete. If no independent project-specific retrieval value exists, record a rejection disposition and do not create the page.

## 3. Browser Connector and Semantic Acceptance

Add an authoritative browser/Git-connector runbook plus repository-local contract assets containing:

- target-lock startup prompt;
- one-topic-at-a-time compilation procedure;
- durable ledger update protocol;
- interrupted-context recovery prompt;
- source-read/source-use distinction;
- page architecture decision rules;
- page-only evaluator prompt;
- claim-entailment evaluator prompt;
- deterministic handoff prompt.

Connector workflow:

1. Lock topic questions before reading sources.
2. Use rankings only to find candidates.
3. Prioritize canonical specifications, implementation evidence where current state matters, current updates/contracts, user stories/examples, then historical/proposal material.
4. Update the topic ledger after each source and before context ends.
5. Draft complete pages only after critical evidence coverage is resolved.
6. Run semantic acceptance in a fresh context that does not receive drafting rationale or self-assessment.
7. Report `partial` when connector limitations prevent completion.

Semantic acceptance artifacts live under:

```
audit/semantic-acceptance/<run-id>/<topic-slug>.json
```

They record:

- evaluator context and contract version;
- page-only results per target query:
    - `answerable`;
    - `partial`;
    - `not_answerable`;
    - `blocked`;
- independently selected material claims;
- entailment result:
    - `supported`;
    - `partially_supported`;
    - `contradicted`;
    - `unresolvable`;
- page/source pointers;
- reason-coded repairs;
- final `semantic_pass`, `semantic_partial`, `semantic_fail`, or `insufficient_evidence`.

Do not use a numeric average as an acceptance authority. Every critical/routine query must be answerable and every sampled material claim supported for `semantic_pass`.

Update scaffolding so new KBs receive the repository-local semantic contract and browser instructions automatically. Existing KBs receive a migration warning rather than a crash.

## 4. Deterministic Runtime Enforcement

Update the Apex KB runtime while preserving the LLM/deterministic boundary.

### Quality checks

Add reason-coded structural findings for:

- `missing_target_queries`;
- `unknown_target_query_id`;
- `target_query_route_missing`;
- `ranked_source_not_in_source_refs`;
- `ranked_source_not_analyzed`;
- `ranked_source_without_claim_use`;
- `source_ref_without_phase1_evidence`;
- `candidate_promotion_disposition_missing`;
- `readable_unopened_source_blocks_completion`;
- `semantic_acceptance_missing`;
- `semantic_acceptance_incomplete`;
- `topic_status_inconsistent`;
- `legacy_semantic_contract`.

Strict quality blocks v2 compiled pages on these reasons. It validates contracts and evidence wiring only; it does not claim to grade semantic meaning.

### Query evaluation

Introduce `apex.query_eval_pack.v2` with:

- query ID;
- priority;
- answer requirements;
- expected pages/routes;
- expected raw-source requirement.

`query-eval --init` derives entries from registry target queries when present. Existing v1 packs remain readable and receive a migration report.

### Semantic acceptance status

Add a read-only semantic-acceptance validation/status surface that:

- validates acceptance artifact shape;
- verifies query/page IDs against registry and wiki files;
- checks that all critical/routine queries have a verdict;
- reports `missing`, `partial`, `pass`, or `fail`;
- never runs an LLM or invents a semantic verdict.

`status` and postflight evidence expose this value. Deterministic postflight cannot promote a semantically incomplete KB.

### Compatibility

- Existing source-only and analysis-only KBs continue working.
- Legacy pages are reported without being silently relabeled v2.
- A legacy KB cannot newly claim `query_ready` until it migrates the in-scope compiled pages and acceptance artifacts.
- Deprecated lifecycle-state documentation remains untouched; `SKILL.md` stays the single operational authority.

## 5. Validation and Leela Canary

### Patcher and package validation

Run:

- patch executor self-test;
- intent and policy schema validation;
- unique target-location checks;
- executor diff reports;
- package inventory validation;
- JSON parsing for all new schemas/templates;
- Python compile checks;
- exact diff-scope verification.

Replace placeholder-positive acceptance examples with substantive fixtures.

Add fixtures for:

- valid v2 summary with locked queries, reviewed sources, linked claims, and semantic pass;
- structurally complete page with no target queries;
- unopened source included as evidence;
- readable canonical source deferred through a reopen trigger;
- missing concept/entity disposition;
- source reference without Phase 1 evidence;
- semantic acceptance missing or incomplete;
- topic marked complete despite failed acceptance;
- legacy v1 KB compatibility;
- query-eval v2 initialization from registry;
- deterministic postflight passing while still refusing a semantic/query-ready claim when acceptance is absent.

### Leela canary

After the Apex update passes:

1. Sync the new repository-local semantic contract into the Leela KB.
2. Lock target questions for all nine registered topics.
3. Create topic ledgers and classify canonical, implementation, update, example, historical, and proposal sources.
4. Rewrite the nine summaries from sufficient canonical evidence.
5. Promote concept/entity pages where objects have independent fields, rules, lifecycle, or repeated direct queries.
6. Run clean-context page-only and claim-entailment acceptance for every topic.
7. Repair only reason-coded failures.
8. Run deterministic index, retrieval, strict lint, strict quality, semantic-acceptance status, and postflight.
9. Repeat the six known failed queries plus the three remaining topic query sets.

Canary acceptance requires:

- every critical/routine query answered from compiled pages;
- no routine answer requiring a readable raw source;
- answer-bearing retrieval results rather than uncertainty-only chunks;
- every evidence source actually reviewed and used;
- explicit disposition for all Phase 1 candidates;
- sampled claims supported by resolved passages;
- no duplicated filler added merely to satisfy deterministic parsing;
- semantic acceptance pass and deterministic postflight pass before `query_ready`.

## Assumptions

- Full closure includes both the Apex KB repair and the Leela canary.
- The browser connector remains semantic-only; local tooling owns deterministic validation and Git integration.
- Existing Markdown/JSON sections are mutated only through `deterministic-markdown-patcher2`.
- New files and Python changes use bounded `apply_patch` because the Markdown executor does not support those operations.
- Unrelated dirty files remain untouched.
- Apex and Leela are merged and pushed to `main` only after all scoped validation succeeds.