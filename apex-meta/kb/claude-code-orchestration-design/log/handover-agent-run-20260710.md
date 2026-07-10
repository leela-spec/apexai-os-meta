# Apex KB Handover — Agentic Terminal Lifecycle Run

```yaml
kb_slug: claude-code-orchestration-design
kb_root: apex-meta/kb/claude-code-orchestration-design
handover_created_at: 2026-07-10
handover_reason: operator_switching_from_manual_permission_mode_to_autonomous_mode
execution_route: terminal_backed
skill_authority: .claude/skills/apex-kb/SKILL.md
purpose: >
  Resume the in-progress terminal-backed Apex KB lifecycle run autonomously
  after the operator turns off manual tool-permission mode. This file is the
  single source of truth for what has run, what passed, and what is left.
```

## Operator instruction on record

Run the full lifecycle in one pass, autonomously, without asking for
permission at each step, until the lifecycle reaches its terminal state
(`postflight` + bounded semantic acceptance + final report). Do not claim
`compile`, `validation`, `evidence_complete`, or `query_ready` unless the
corresponding checks actually pass. Preserve source custody, provenance,
hashes, manifests, and existing KB content. Do not write outside this KB
root. Do not hardcode another KB slug.

## Why this KB needed a real terminal run

Prior runs (`log/max-run-20260709-execution-audit.md`,
`log/max-run-20260709-phase2-quality-failure-root-cause.md`) used a GitHub
connector for semantic writes and only did connector read-back — no
deterministic postflight (`index`, `build-index`, `lint --strict`,
`quality --strict`, `status`, `stale`) was actually executed after those
writes. That is the gap this run is closing.

## Steps already executed and confirmed (exit code 0, JSON captured)

```yaml
completed_steps:
  - step: generate-source-payload-manifest
    command: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design generate-source-payload-manifest --allow-write --json
    result: file_count=2647, group_count=6, root_sha256=0eecb21a458560373b8f41d1d2824db6e4643c9a8ddc28589caa88a4f5d01a29, total_size_bytes=389803331
    status: pass

  - step: phase0
    command: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design phase0 --allow-write --json
    result: artifact_count=8 (all 8 deterministic phase0 artifacts present), source_file_count=1732
    caveat: >
      pointer_only_warning_count=1. The single pointer_only source in
      manifests/source-manifest.json points at the whole `raw/` directory
      (not a file), so Phase 0's per-file pointer resolver reports it
      "unresolved" with reason "not_a_file" even though phase0 still scans
      1732 files inside raw/ through its normal directory walk. This is a
      cosmetic/known mismatch between a directory-scoped pointer_only entry
      and a file-scoped pointer resolver — not a missing-source problem.
      Do not "fix" this by inventing per-file source-manifest entries unless
      the operator asks for finer-grained custody; report it as-is.
    status: pass_with_reported_caveat

  - step: graph
    command: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design graph --allow-write --json
    result: exit 0, wrote/confirmed manifests/phase0/process-flow-graph.json (output JSON was captured to scratchpad but not yet summarized in chat — reread it on resume)
    status: pass_exit_code_confirmed_summary_pending

  - step: query-eval --init
    command: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design query-eval --init --allow-write --json
    result: exit 0 (output JSON captured to scratchpad but not yet summarized in chat — reread it on resume)
    known_prior_state: >
      outputs/queries/evals/query-eval-pack.json previously had queries: [].
      R03 flagged this as blocking query-based blind evaluation. Check
      whether --init populated real queries or only validated/left it empty;
      if still empty, target-query authorship is a required follow-up before
      any semantic acceptance pass that needs query trials.
    status: exit_code_confirmed_content_verification_pending
```

## Baseline status captured before this run (for comparison)

```yaml
baseline_status_snapshot:
  command: python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design --json status
  result:
    source_count: 1
    wiki_page_count: 99
    audit_item_count: 0
    phase0_artifacts_present: true
    source_payload_manifest_status: stale   # now regenerated above, expect fresh on rerun
    wiki_index_status: stale
    retrieval_index_status: stale
```

## Remaining steps to execute, in exact order, on resume

Run from repo root `C:\GitDev\apexai-os-meta`. All commands are already
approved in spirit by the operator's "no permission prompts, run the whole
lifecycle" instruction — execute them without pausing for confirmation.

```bash
KB="apex-meta/kb/claude-code-orchestration-design"

# 1. Re-summarize graph + query-eval output already captured (scratchpad JSON files:
#    graph_out.json, queryeval_out.json) before moving on — do not rerun unless stale.

# 2. Quality / coverage (report-only first, then strict)
python apex-meta/scripts/apex_kb.py --kb-root "$KB" quality --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" quality --strict --json

# 3. Deterministic index rebuild
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --allow-write --json index

# 4. Retrieval rebuild + stale check
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --allow-write --json build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --json stale

# 5. Lint (strict), audit, status
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json lint --strict
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json audit
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json status

# 6. Postflight as the bounded deterministic completion interface
#    (dry-run first for a clean planned-state record, then allow-write)
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json postflight
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --allow-write --json postflight
```

After postflight, run the **bounded semantic acceptance check** required by
`references/ingest-query-lint-audit-rules.md` ("Phase 2 acceptance and
repair loop") and `log/research-r03-independent-semantic-quality-gate.md`
before claiming `query_ready`:

```yaml
semantic_acceptance_plan:
  scope: bounded sample, not every page (99 wiki pages exist; this KB has
    already been diagnosed with a known thin-page failure mode in the
    max-run-20260709/ pages — see below)
  method_per_r03:
    - blind_query_trial: attempt 1-2 plausible target queries per sampled page using only page content
    - material_claim_selection: pick 2-3 claims carrying the page's main conclusion
    - source_entailment_check: compare each claim against its cited source pointer/excerpt
    - synthesis_and_uncertainty_check: verify Macro/Meso/Micro add distinct value and uncertainty is preserved
    - verdict: semantic_pass | semantic_partial | semantic_fail | insufficient_evidence, reason-coded
  known_already_diagnosed_failures_do_not_rediscover_from_scratch:
    - path: wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
      prior_verdict: semantic_fail (see log/research-r03-independent-semantic-quality-gate.md)
    - path: wiki/summaries/max-run-20260709/production-agent-readiness-and-risk-model.md
      prior_verdict: semantic_partial
    - path: wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
      prior_verdict: semantic_partial
    - path: wiki/entities/max-run-20260709/claude-code-subagents.md
      prior_verdict: semantic_partial
    - path: wiki/summaries/max-run-20260709/failure-analysis-and-feedback-loop.md
      prior_verdict: semantic_partial
  action_on_resume: >
    Treat these five prior verdicts as already-established bounded semantic
    acceptance evidence (R03 report). Do not re-claim query_ready for the
    max-run-20260709/ page set — R03 already found a blocking semantic_fail
    and four semantic_partial results there. Extend the same method to a
    small sample of the *original* (non-max-run) wiki/summaries, concepts,
    entities pages (the ones without a max-run-20260709/ subfolder), since
    those have not yet been through this bounded semantic gate at all.
```

## Known outstanding blockers (do not silently resolve; surface these)

```yaml
outstanding_blockers:
  - id: B1
    description: query-eval-pack.json queries array may still be empty after --init (init only scaffolds/validates schema, it does not author target queries)
    impact: blocks true query-based blind evaluation required by R03 minimum gate
    resolution: requires operator-provided or Phase-1-derived target queries per page/topic; not a script bug

  - id: B2
    description: max-run-20260709/ Phase 2 pages are known thin (single claim, one-sentence Macro/Meso/Micro layers, file-level-only pointers) per log/max-run-20260709-phase2-quality-failure-root-cause.md and log/research-r02-deterministic-quality-metrics-20260710.md
    impact: current deterministic quality/shell-page heuristic in apex_kb.py does NOT flag these as repair candidates (documented false-negative in R02) — quality --strict may report clean even though R03's independent semantic read found one semantic_fail and four semantic_partial pages
    resolution: >
      Do not let a passing `quality --strict` alone justify `query_ready`.
      Report deterministic quality result AND the R03 semantic findings
      side by side. The R02 report recommends a script patch
      (apex-meta/scripts/apex_kb.py: extract_source_refs, is_shell_page_candidate,
      quality_report, cmd_quality) to catch this — that patch has NOT been
      applied. Applying it is an operator decision (it changes the script,
      which is out of scope for "run the lifecycle" unless explicitly
      requested).

  - id: B3
    description: pointer_only source-manifest entry for raw/ is directory-scoped; Phase 0's pointer resolver expects file-scoped pointers, so it reports 1 unresolved/1 warning every run
    impact: cosmetic only — 1732 files are still scanned; does not block any gate
    resolution: report as known caveat unless operator wants finer per-file source-manifest entries

  - id: B4
    description: F1/F2/F5 from log/max-run-20260709-execution-audit.md (37 direct commits to main, one unrelated file touched outside KB root in the compare window, a leftover log/max-run-20260709-write-probe.md debris file)
    impact: repo hygiene / git history, not a KB lifecycle gate failure
    resolution: operator decision — this run has not touched git history or deleted the write-probe file; flag both in the final report, do not delete anything without explicit operator instruction (deleting log/max-run-20260709-write-probe.md would be a content mutation outside this run's asked scope)
```

## Task tracker state at handover time

```yaml
task_list_state:
  "#1 Inspect current KB state": completed
  "#2 Run source intake / payload manifest stage": in_progress -> should be marked completed on resume (payload manifest regenerated successfully; source-manifest.json already had the one pointer_only entry, no new raw sources needed intake)
  "#3 Run Phase 0 deterministic corpus intelligence": effectively done (phase0 ran, 8/8 artifacts present) -> mark completed on resume, note the pointer caveat
  "#3b (implicit) graph / query-eval": ran, exit 0 both, needs output summarization on resume
  "#4 Assess Phase 1/Phase 2 semantic compile state": not started — on resume, read ingest-analysis/max-run-20260709/phase1-completion-report.md and ingest-analysis/phase1-completion-report.md to confirm Phase 1 completion status, then proceed (no new Phase 1/2 authoring is planned in this run — extensive Phase 1/2 content already exists; this run's job is deterministic validation + bounded semantic acceptance, not a rewrite)
  "#5 Run deterministic index + retrieval build": pending
  "#6 Run lint, quality, audit, status checks": pending
  "#7 Run postflight as final completion interface": pending
  "#8 Run bounded semantic acceptance check": pending (plan above)
  "#9 Compile final lifecycle report": pending — must honestly reflect B1-B4 and R02/R03 findings, must not claim query_ready if quality --strict, lint --strict, or the semantic sample surface a semantic_fail/blocking finding
```

## Explicit non-negotiables carried over from the operator's original request

```yaml
non_negotiables:
  - use exactly this KB root, nothing else: apex-meta/kb/claude-code-orchestration-design
  - do not write outside the KB root
  - do not hardcode another KB slug
  - preserve source custody, provenance, hashes, manifests, existing KB content (never overwrite max-run-20260709/ or original wiki content; this run only adds deterministic artifacts, a query-eval pack fill-in if applicable, and this log/report)
  - use postflight as the final bounded deterministic completion interface
  - run the bounded semantic acceptance check before claiming query_ready
  - do not claim compile / validation / evidence completeness / query_ready unless checks actually pass
  - report stages completed; artifacts created/updated; command results and exit codes; postflight status and evidence completeness; retrieval freshness; quality/lint/audit/semantic acceptance results; remaining blockers or required operator decisions
```

## Resume instruction

On resume, re-read this file first, then continue directly from "Remaining
steps to execute, in exact order, on resume" above. Do not restart from
scaffold/source-intake — those are already done and verified. Do not pause
to ask permission for any of the listed commands; the operator has already
authorized the full run.
