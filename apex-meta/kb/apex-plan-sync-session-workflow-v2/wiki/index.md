---
title: "Apex Plan Sync Session Workflow v2 — Wiki Index"
page_type: "index"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T10:15:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# Apex Plan Sync Session Workflow v2 — Wiki Index

This KB documents the `apex-plan` / `apex-sync` / `apex-session` skill package trio: what each
package owns, how they hand work to each other, and why the design is isolated-yet-overlapping by
intent rather than by accident. It also tracks two adjacent Master-of-Arts workflow-research
documents at the operator's explicit request. This page is the entry point for a reader — human
or LLM — who has no prior context on this repository's Apex orchestration work.

## Start here, in order

1. [Apex Plan Sync Session Workflow Summary](summaries/apex-plan-sync-session-workflow-summary.md)
   — one-page overview of what the three packages are and how they relate. Read this first.
2. [Isolation With Overlap](concepts/isolation-with-overlap.md) — the resilience argument: why
   disjoint ownership plus deliberate, repeated overlap (not either alone) is what makes the
   three-package design robust to drift.
3. [Three Package Boundary](concepts/three-package-boundary.md) — the precise ownership partition
   (which package owns which process_scope items) that Isolation With Overlap's argument depends on.
4. [Proposal Computation Mutation Split](concepts/proposal-computation-mutation-split.md) — the
   three epistemic states (qualitative proposal / exact computed fact / confirmed mutation) that
   map onto apex-plan / apex-sync / apex-session respectively.
5. [Operator-Gated Phase Boundary](concepts/operator-gated-phase-boundary.md) — the three
   different gate mechanisms (a required field, a dry-run CLI default, a four-state validation
   enum) that all implement "nothing consequential happens by default," including this KB's own
   `approve ingest` gate.

## Entity pages (per-package full contracts)

- [apex-plan](entities/apex-plan.md) — project capture, decomposition, dependency/priority/urgency
  proposal; zero script execution surface; produces the `apex_plan_packet`.
- [apex-sync](entities/apex-sync.md) — deterministic read-side computation via
  `scripts/apex_sync.py`; dry-run by default; one narrow registry-write exception; documented
  single-point-of-failure risk if the script fails.
- [apex-session](entities/apex-session.md) — gated status mutation, state-delta extraction, entity
  maintenance, and the four persistent H6 handoff artifacts; the only package with an explicit
  cross-package routing step in its own procedure.

## Master of Arts workflow research (adjacent, separate lineage)

- [Master of Arts Workflow Research](concepts/master-of-arts-workflow-research.md) and its
  [summary](summaries/master-of-arts-workflow-research-summary.md) — two operator-supplied draft
  research documents (a process-ranking document and a draft workflow example database) tracked
  in this KB at the operator's explicit request. **This is a separate research thread, not a
  description of the apex-plan/apex-sync/apex-session skill package** — read the summary page's
  Core Summary for the scope boundary before assuming any connection.

## What this KB run found and fixed (detective findings)

This KB run was explicitly framed as a "detective" pass over a prior, untrusted run of this same
KB. Everything below was independently verified against live repository files during this session,
not carried forward from the prior run's claims.

1. **Source custody was broken.** All three skill packages' sources were recorded as
   `pointer_only` against Windows local paths (`C:\GitDev\...`), with no durable content actually
   stored in the KB — confirmed by this KB's own prior audit,
   `audit/FailureReport_HighImpact_CC_Testrun.md`. This run re-intook all 31 canonical files
   (9 apex-plan, 12 apex-session, 8 apex-sync, plus the 2 Master-of-Arts files) as durable,
   SHA-256-hashed, `copy_into_kb` sources. Every hash was independently re-verified against the
   live repository files during this session (see `manifests/source-manifest.json`).

2. **A source-intake destination collision was found and fixed mid-run.** `apex_kb.py`'s
   `source-intake --source-root` mode (and single-file `--source-path` mode) computes destination
   paths from the file's basename/relative-path alone, with no per-source-root prefix. Because all
   three skill packages have their own `SKILL.md` and `package-manifest.md`, the first intake
   attempt silently overwrote apex-plan's stored `SKILL.md` content with apex-session's, and so on.
   This was caught by an immediate hash cross-check (not by the tool itself), reverted via
   `git checkout`, and re-run using distinct `raw/other/` (apex-plan), `raw/refs/` (apex-session),
   `raw/notes/` (apex-sync), and `raw/papers/` (Master-of-Arts extras) buckets. All 31 sources are
   now independently confirmed to contain the correct originating file's content.

3. **The "wrong signal words" suspicion is confirmed, with a precise mechanism.** The operator who
   commissioned this run suspected a prior KB pass "ran on previously wrong signal words." This KB
   run found the concrete cause: `apex_kb.py`'s `rank_topic_sources()` function
   (`scripts/apex_kb.py` line 1038) reads topic entries by `slug`/`name`, but
   `old-apex-full-orchestration-agent-kb-v2/manifests/topic-registry.json` — and this KB's own
   first-draft `topic-registry.json` in this session, before the bug was caught — used
   `topic_id`/`title` instead. Every topic missing a `name` field silently falls back to the
   literal string `"unnamed"`, so all topics collapse into one ranking bucket keyed by whichever
   topic was processed last. Confirmed directly: `old-apex-full-orchestration-agent-kb-v2`'s
   `manifests/phase0/topic-source-rankings.json` contains exactly one key, `"unnamed"`, despite
   that KB declaring 3 distinct topics — meaning two of its three wiki summary pages
   (`agent-architecture`, `resilient-iterative-workflows`) were never backed by their own
   correctly-computed Adaptive Ranked Source Set. This KB's own `topic-registry.json` was corrected
   to the `slug`/`name` schema and re-run, producing 5 correctly separated topic rankings (see
   `manifests/phase0/topic-source-rankings.json` in this KB). **The deterministic script itself is
   correct** — the defect was in the hand-authored registry input file's field names, in both KBs.

4. **A new, previously-undocumented data-integrity gap was found in apex-plan.** All four
   `.pro.md` files in `.claude/skills/apex-plan/` are 0 bytes on disk, despite
   `extraction-report.md` documenting 7 extracted blocks from a Prothinking-sourced extraction.
   The prior audit's finding P3 flagged `.v1.md` files as byte-identical duplicates of their
   canonical twins (confirmed accurate by this run) but did not separately notice the `.pro.md`
   files were empty — this is a new finding, recorded as an audit item, not a KB defect (apex-kb
   must not modify skill package files).

5. **The apex-sync single-point-of-failure risk (prior audit finding P2) is independently
   reconfirmed**, not resolved: `apex-sync`'s own `SKILL.md` (lines 145-147, 191) requires
   returning the script failure report and stopping inference if `scripts/apex_sync.py` fails,
   with no fallback computation path defined anywhere in its contract.

6. **The three stale `pointer_only` manifest entries were not deleted.** `apex_kb.py` has no
   source-removal subcommand, and hand-editing the manifest would violate `apex-kb`'s
   `python_owns: source_manifest_shape` rule. They remain in `manifests/source-manifest.json` as
   `source_id: apex-plan / apex-sync / apex-session`, explicitly superseded by the file-level
   `apex-plan-skill` / `apex-sync-skill` / `apex-session-skill` entries (and the rest of the 31)
   added in this run — kept intentionally as an audit trail of the original broken intake, not as
   active sources.

## Related KBs and logs referenced by this run (not modified)

- `apex-meta/kb/apex-plan-sync-session-workflow-v2/audit/FailureReport_HighImpact_CC_Testrun.md`
  — this KB's own prior failure audit; findings P2 (apex-sync SPOF) and P3 (`.v1.md` duplication)
  were independently reconfirmed above; P1 (`project-kb-manager` completion_gate) and P4/P5 were
  read but are out of this run's remediation scope (they concern a different package,
  `project-kb-manager`, not apex-plan/apex-sync/apex-session directly).
- `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/` — a separate, larger KB (agent
  architecture, failure patterns, resilient iterative workflows, plus the same OperatorResearch
  dropbox the two Master-of-Arts extras were pulled from). Out of scope for remediation in this
  run; its own `topic-registry.json` schema bug is documented above as a cross-KB finding, but its
  files were not modified.
- `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/log/previous-run-and-signal-comparison.md`
  — that KB's own prior documentation of a v1→v2 "signal-word reassessment" (raw noisy term
  frequency replaced with semantic clusters). That fix addressed a different problem (noisy raw
  terms) than the schema bug found in finding 3 above (which silently defeats *any* topic
  registry, noisy or not, regardless of keyword quality).

## Source basis

This wiki layer is compiled from ingest-analysis batches 06-10 (this run), which supersede
batches 01-05 (the prior, pointer_only, untrusted run) — their claims were cross-checked against
live repository files rather than assumed. See `ingest-analysis/batch06-apex-plan-contract.analysis.md`
through `batch10-master-of-arts-workflow-research.analysis.md` for full source-identity,
extraction-candidate, and uncertainty-trigger detail behind every claim summarized on this page.

## Next deterministic step

Run `lint --strict`, `audit`, `index --allow-write`, `postflight --allow-write`, and
`apex_kb_retrieval.py build-index` to confirm `query_ready` state (in progress in this session).

<!-- BEGIN AUTO-GENERATED INDEX -->

Generated: `2026-07-11T09:57:18Z`

Compiled page count: `10`

## Topic Guides

- How apex-plan, apex-sync, and apex-session hand off work to each other and stay isolated-but-overlapping - `compiled` / `operator` (no page yet)
- Master of Arts workflow example database and process ranking research (Hermes/Alfred lineage) - `compiled` / `operator` (no page yet)
- apex-plan skill: capture, decomposition, dependency/priority rationale, and its does-not boundary - `compiled` / `operator` (no page yet)
- apex-session skill: session state mutation, handoff, and its does-not boundary - `compiled` / `operator` (no page yet)
- apex-sync skill: deterministic read-side computation via apex_sync.py, and its does-not boundary - `compiled` / `operator` (no page yet)

## Concept Pages

- [Isolation With Overlap](concepts/isolation-with-overlap.md) - `active` / `high`
- [Master of Arts Workflow Research](concepts/master-of-arts-workflow-research.md) - `active` / `medium`
- [Operator-Gated Phase Boundary](concepts/operator-gated-phase-boundary.md) - `active` / `high`
- [Proposal Computation Mutation Split](concepts/proposal-computation-mutation-split.md) - `active` / `high`
- [Three Package Boundary](concepts/three-package-boundary.md) - `active` / `high`

## Entity Pages

- [apex-plan](entities/apex-plan.md) - `active` / `high`
- [apex-session](entities/apex-session.md) - `active` / `high`
- [apex-sync](entities/apex-sync.md) - `active` / `high`

## Summary Pages

- [Apex Plan Sync Session Workflow Summary](summaries/apex-plan-sync-session-workflow-summary.md) - `active` / `high`
- [Master of Arts Workflow Research Summary](summaries/master-of-arts-workflow-research-summary.md) - `active` / `medium`

<!-- END AUTO-GENERATED INDEX -->
