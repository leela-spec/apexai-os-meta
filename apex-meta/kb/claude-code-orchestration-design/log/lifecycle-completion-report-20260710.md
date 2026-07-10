# Apex KB Lifecycle Completion Report — 2026-07-10

```yaml
kb_slug: claude-code-orchestration-design
kb_root: apex-meta/kb/claude-code-orchestration-design
report_created_at: 2026-07-10
report_updated_at: 2026-07-10T20:30:00Z
predecessor_handover: log/handover-agent-run-20260710.md
run_mode: terminal_backed_autonomous_after_manual_permission_mode_disabled
update_reason: >
  Operator explicitly instructed that the deterministic-only pass was
  insufficient and that this run must also perform the LLM-owned Phase 2
  wiki-drafting step (SKILL.md: llm_owns.phase_2_wiki_drafting) rather than
  stopping at validation. Section 9 below documents that pass and its
  verified effect on the gates below.
final_status: fail_narrowed_to_max_run_20260709_only
compile_claimable: false
validation_claimable: false
evidence_complete: false
query_ready: false
```

## 1. Purpose

This resumes and closes out `log/handover-agent-run-20260710.md`. That
handover had already run source-payload-manifest generation, Phase 0, graph,
and `query-eval --init` (all exit 0). This report covers everything from
`quality` onward through postflight, the bounded semantic acceptance check,
and final status — and states plainly why `query_ready` is **not** reached.

## 2. Stages executed this run (all exit codes captured)

```yaml
stages:
  - step: quality (report-only)
    command: apex_kb.py --kb-root $KB quality --json
    exit_code: 0
    result: issue_count=89, 99 pages total (74 non-max-run, 25 max-run-20260709)
    status: ran_clean_findings_reported_below

  - step: quality --strict
    command: apex_kb.py --kb-root $KB quality --strict --json
    exit_code: 2
    result: status=fail, issue_count=89, shell_page_candidates=89
    status: fail

  - step: index rebuild
    command: apex_kb.py --kb-root $KB --allow-write --json index
    exit_code: 0
    result: page_count=99, wiki/index.md written/changed
    status: pass

  - step: retrieval build-index
    command: apex_kb_retrieval.py --kb-root $KB --allow-write --json build-index
    exit_code: 0
    result: chunk_count=298, page_count=98 (wiki/index.md intentionally excluded)
    status: pass

  - step: retrieval stale
    command: apex_kb_retrieval.py --kb-root $KB --json stale
    exit_code: 0
    result: added=[], deleted=[], modified=[], status=fresh
    status: pass

  - step: lint --strict
    command: apex_kb.py --kb-root $KB --json lint --strict
    exit_code: 2
    result: status=fail, issue_count=440 (365 report_only page_value_contract + 75 blocking frontmatter)
    status: fail

  - step: audit
    command: apex_kb.py --kb-root $KB --json audit
    exit_code: 0
    result: item_count=0, mutations=false
    status: pass

  - step: status
    command: apex_kb.py --kb-root $KB --json status
    exit_code: 0
    result: source_count=1, wiki_page_count=99, audit_item_count=0, phase0_artifacts_present=true, source_payload_manifest_status=fresh, wiki_index_status=fresh, retrieval_index_status=stale (see B5 — false positive), search_index_present=true
    status: pass_with_known_false_positive_field

  - step: postflight (dry-run)
    command: apex_kb.py --kb-root $KB --json postflight
    exit_code: 0
    result: status=planned, evidence_complete=false, 7 steps planned
    status: planned_clean

  - step: postflight (allow-write)
    command: apex_kb.py --kb-root $KB --allow-write --json postflight
    exit_code: 2
    result: status=fail, evidence_complete=false. Internal steps -- wiki_index: pass, retrieval_build: pass, lint_strict: fail, quality_strict: fail, audit: pass (non-blocking), status: pass, retrieval_stale: fresh/pass
    status: fail_driven_by_lint_and_quality_strict
```

## 3. Root-caused findings

### F1 — 25/25 max-run-20260709 pages have identical blocking frontmatter defects

All 25 pages under `wiki/*/max-run-20260709/` are missing `created_at` and
`updated_at` frontmatter fields (50 `missing_field` issues) and carry an
invalid `status: new_parallel_compile` value not in the recognized status
enum (25 `invalid_status` issues) = all 75 blocking lint issues. This is the
sole cause of the blocking half of the `lint --strict` failure. It is a
single, uniform, mechanically-repairable defect (looks like one templating
bug applied to the whole max-run batch) — but per the non-negotiables this
run does not edit max-run-20260709/ content without explicit operator
instruction. **Operator decision needed**: authorize a frontmatter-only
patch (add `created_at`/`updated_at`, correct `status`) across these 25
files, or explicitly accept the lint failure as known state.

### F2 — 73 of 74 non-max-run pages are empty scaffolds, corroborated two ways

Deterministically: `quality --strict` flags 73/74 non-max-run pages with
`no_key_claims`, `missing_phase2_value_sections` (all five Phase 2 sections
absent), and `thin_macro_meso_micro`; narrative word counts range 1-41
(median well under 10). Semantically: this run's bounded sample (Task #7)
read the two best-available non-max-run pages —
`wiki/summaries/minimal-claude-orchestration-architecture.md` (highest word
count, 41) verdicts `semantic_partial` (real, source-grounded prose, but
zero required structural sections); `wiki/entities/agent-skills-standard.md`
verdicts `semantic_fail` (one-line stub, no claim to evaluate). Both
confirm the deterministic signal rather than contradict it.

This is **not a new discovery** — `ingest-analysis/max-run-20260709/phase1-completion-report.md`
claim P1-COMP-001 already states the max-run should "focus on high-value
routing and value-contract pages, not blindly duplicate all 73 legacy
pages," confirming this was a known, intentional scoping decision carried
over from the prior run, not an omission from this one.

### F3 (B5, new) — `status`'s `retrieval_index_status` is a permanent false positive

`apex_kb.py`'s `retrieval_index_status()` (line ~1641) compares the file set
recorded in `derived/search/index-meta.json` against **all** `wiki_pages()`
(99, including `wiki/index.md`). The retrieval build intentionally excludes
`wiki/index.md` from chunking (98 pages), so the set comparison always
mismatches and this field will report `"stale"` on every run regardless of
actual freshness. Verified: `apex_kb_retrieval.py stale` (the authoritative
check) correctly returns `"fresh"` with no added/deleted/modified files
immediately after the same build. This is a script bug candidate, not
something this run fixed (script changes are out of scope for a lifecycle
run per the same precedent noted in B2 below).

### B1 — query-eval-pack queries still empty (carried over, confirmed)

`query-eval --init` (run in the predecessor session) left
`outputs/queries/evals/query-eval-pack.json` with `query_count: 0`
(re-verified from the captured output this run). `--init` only
scaffolds/validates the schema; it does not author target queries. This
still blocks true query-based blind evaluation per R03's minimum gate.
**Resolution requires operator-provided or Phase-1-derived target queries —
not a script bug.**

### B2 — shell-page heuristic false negative (partially resolved, updated finding)

The prior handover reported the deterministic shell-page heuristic does
**not** flag R03's five known-bad max-run-20260709 pages. Re-verified this
run: **4 of 5 now ARE flagged** as `shell_page_candidates`
(`claude-code-mechanism-decision-model.md`,
`production-agent-readiness-and-risk-model.md`,
`source-preserving-kb-compile.md`, `failure-analysis-and-feedback-loop.md`).
Only `wiki/entities/claude-code-subagents.md` (R03 verdict:
`semantic_partial`) still slips through undetected. This narrows but does
not close the R02-documented false-negative gap.

### B3 — pointer_only directory-scoped source (unchanged, cosmetic)

Unchanged from the handover: the single `pointer_only` source-manifest entry
points at the whole `raw/` directory, so Phase 0's per-file pointer resolver
reports it "unresolved" even though 1,732 files inside are still scanned
normally. Cosmetic only; not touched this run.

### B4 — repo hygiene (unchanged, not this run's scope)

37 direct commits to main, one file touched outside the KB root in the
compare window, and the leftover `log/max-run-20260709-write-probe.md` file
remain untouched. This run did not touch git history or delete the
write-probe file — that would be a content mutation outside this run's
authorized scope.

## 4. Bounded semantic acceptance summary

```yaml
semantic_acceptance:
  carried_over_from_R03_not_relitigated:
    - path: wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
      verdict: semantic_fail
    - path: wiki/summaries/max-run-20260709/production-agent-readiness-and-risk-model.md
      verdict: semantic_partial
    - path: wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
      verdict: semantic_partial
    - path: wiki/entities/max-run-20260709/claude-code-subagents.md
      verdict: semantic_partial
    - path: wiki/summaries/max-run-20260709/failure-analysis-and-feedback-loop.md
      verdict: semantic_partial
  new_this_run_non_max_run_sample:
    - path: wiki/summaries/minimal-claude-orchestration-architecture.md
      verdict: semantic_partial
      reason: >
        Real, source-grounded prose (verified against
        log/phase2-specialized-index-compile-plan-20260702.md lines 38-137);
        answers a plausible "how should orchestration mechanism choice work"
        query; but has zero Key Claims, Macro/Meso/Micro, Routes Here, or
        Uncertainty sections -- cannot support the KB's own query-routing
        contract.
    - path: wiki/entities/agent-skills-standard.md
      verdict: semantic_fail
      reason: >
        One-line role tag only; no claim to entail against sources; cannot
        answer even a basic blind query about tension with Claude Code
        native skill behavior (a tension documented elsewhere as
        P1-CONTRA-001 but absent from this page).
  generalization_basis: >
    Deterministic quality metrics show 73/74 non-max-run pages score in the
    same range (1-41 narrative words, 0 key claims) as the two sampled
    pages, so this bounded sample is treated as representative rather than
    exhaustive verification.
```

## 5. Phase 1 completion status confirmed (Task #6)

```yaml
phase1_status:
  original_07-02:
    status: phase_1_complete_operator_review_needed
    phase2_gate_original: hard_enforced (operator decision Q002, log/operator-phase1-review-decisions-20260702.md)
    phase2_gate_reinterpreted_later: >
      log/R01-executor-capability-and-process-feasibility.md and
      log/R04-process-simplification-and-guardrail-deletion-audit.md (both
      already in this KB, not new research from this run) reclassify the
      "approve ingest" phrase as "not a capability or quality gate," an
      optional resume mechanism only. R04 explicitly flags this as one of
      three incompatible interpretations across SKILL.md, acceptance tests,
      and the original operator decision log. This is a pre-existing,
      already-documented governance ambiguity -- surfaced here for
      completeness, not re-litigated or resolved by this run.
  max_run_07-09:
    status: complete_with_baseline_warning
    scoping_confirmed: >
      P1-COMP-001 explicitly scoped the max-run to avoid duplicating the 73
      legacy pages -- consistent with and explaining F2 above.
```

## 6. Final verdicts (per non-negotiables: do not claim what did not pass)

```yaml
final_verdicts:
  compile: not_claimable  # quality --strict and lint --strict both fail
  validation: fail        # lint --strict fail, quality --strict fail, postflight allow-write fail
  evidence_complete: false  # returned directly by postflight
  query_ready: not_reached
  reasons:
    - B1 query-eval-pack has zero authored target queries
    - F1 all 25 max-run-20260709 pages fail frontmatter lint (blocking)
    - F2 73/74 non-max-run pages are semantically empty (deterministic + sampled semantic confirmation)
    - postflight allow-write returns status=fail, evidence_complete=false directly
```

## 7. Artifacts created/updated this run

```yaml
artifacts:
  - path: wiki/index.md
    action: rewritten (index --allow-write), page_count=99
  - path: derived/search/index.sqlite
    action: rebuilt (retrieval build-index --allow-write), chunk_count=298
  - path: derived/search/index-meta.json
    action: rewritten alongside sqlite rebuild
  - path: log/lifecycle-completion-report-20260710.md
    action: created (this report)
```

## 9. Phase 2 wiki-drafting pass (added after operator instruction)

The initial pass through this report (sections 1-8) treated the 73 empty
non-max-run pages as an already-known, out-of-scope legacy condition and
stopped at deterministic validation. The operator correctly pointed out that
`SKILL.md`'s `llm_owns: phase_2_wiki_drafting` makes authoring those pages
this assistant's job, not an optional extra — the deterministic scripts
were never going to write semantic content themselves. This section records
that follow-up work.

```yaml
phase2_authoring_pass:
  method: >
    9 parallel subagents, each assigned a cluster of 7-9 pages, each required
    to read the actual Phase 1 batch files (ingest-analysis/phase1-batch01
    through 04), the specialized-index compile plan, the operator decision
    log, and the completion report before writing -- grounding every Key
    Claim in a real claim ID (e.g. B01-C001) or concepts_extracted/
    entities_extracted entry, and explicitly downgrading confidence to
    medium/working_hypothesis (rather than high/source_backed_summary)
    wherever content was synthesized from the specialized-index question
    framework instead of quoting a direct Phase 1 claim.
  pages_authored: 73
  pages_touched_outside_assignment: 0
  honesty_notes:
    - scheduler.md and scheduler-boundary-and-deferment.md were correctly
      left thin/low-confidence -- Phase 1 never deep-dived scheduling, and
      the agents said so explicitly instead of inventing scheduler mechanics.
    - the persistent/production-agent-roster cluster (persistent-agent-boundary,
      production-agent-readiness-gate, production-agent-roster-candidate-boundary,
      productive-agent-redundancy, production-agent-readiness-and-roster-boundary)
      was correctly framed as an open architectural question per the compile
      plan, not resolved doctrine.
    - wiki/entities/claude-code-subagents.md (the one page that survived the
      earlier B2 false-negative narrowing, R03 verdict semantic_partial) was
      specifically re-verified by its assigned agent as now genuinely strong:
      full Macro/Meso/Micro narrative, 4 real Key Claims, Evidence, Routes
      Here, and Uncertainty triggers pulled from actual open questions.
```

### 9.1 Verified before/after (rerun of the full deterministic pipeline)

```yaml
before_after:
  quality_strict:
    before: {status: fail, issue_count: 89}
    after: {status: fail, issue_count: 16}
    note: all 16 remaining issues are exclusively in wiki/*/max-run-20260709/ -- zero non-max-run pages remain flagged
  lint_strict:
    before: {status: fail, issue_count: 440, report_only: 365, blocking: 75}
    after: {status: fail, issue_count: 76, report_only: 0, blocking: 75}
    note: >
      report_only page_value_contract issues dropped from 365 to 0 -- every
      one of them was a non-max-run page, now cleared. The 75 blocking
      frontmatter issues are unchanged because they belong exclusively to
      the 25 max-run-20260709/ pages, which this run still does not modify
      without explicit operator instruction (see F1 / OD1 below). One
      residual orphan-link issue exists for a pre-existing, previously
      uncommitted-to-this-run trial-20260710-status-merge/ page pair
      (confirmed via git log to predate this session -- not introduced by
      the authoring pass).
  index_and_retrieval:
    wiki_page_count: 101 (was reported as 99 earlier in this same log; the
      2-page difference is wiki/*/trial-20260710-status-merge/*.md, which
      were already committed before this session and were picked up once
      wiki/index.md was rebuilt against current disk state)
    retrieval_stale_check: fresh, 0 added/deleted/modified
  postflight_allow_write:
    before: {status: fail, evidence_complete: false}
    after: {status: fail, evidence_complete: false}
    note: >
      Still fails -- and correctly so. lint_strict and quality_strict are
      still blocking steps, and both still fail because of the 25
      max-run-20260709/ pages' frontmatter defect (F1) and the same pages'
      remaining shell-page flags. This is the accurate state: the
      non-max-run backlog is closed; the max-run-20260709/ backlog is
      untouched pending an explicit operator decision (OD1).
```

### 9.2 What this changes about the operator decisions in section 8

OD3 (fate of the 73 empty legacy pages) is **resolved** -- they are authored
now, not backfilled-later or archived. OD1 (max-run-20260709/ frontmatter
patch) is now the *only* remaining blocker standing between this KB and a
clean `quality --strict` / `lint --strict` pass. OD2 (query-eval-pack target
queries) and OD4/OD5 are unchanged and still open.

## 10. Operator decisions required before this KB can claim query_ready

```yaml
operator_decisions_needed:
  - id: OD1
    question: Authorize a frontmatter-only patch (created_at, updated_at, valid status) across the 25 max-run-20260709/ pages to clear the blocking lint failure (F1)?
  - id: OD2
    question: Author or commission target queries for outputs/queries/evals/query-eval-pack.json (B1) so true query-based blind evaluation can run?
  - id: OD3
    question: Decide the fate of the 73 empty legacy (non-max-run) pages (F2) -- backfill Phase 2 content, explicitly deprecate/archive them, or scope query_ready claims to the max-run-20260709 subset only?
  - id: OD4
    question: Authorize a script patch to apex_kb.py's retrieval_index_status() (F3/B5) to exclude wiki/index.md from the wiki_pages() comparison set, removing the permanent false-positive stale reading?
  - id: OD5
    question: Repo hygiene items from B4 (37 direct commits, stray out-of-root file touch, leftover write-probe.md) -- any action wanted, or accepted as-is?
```
