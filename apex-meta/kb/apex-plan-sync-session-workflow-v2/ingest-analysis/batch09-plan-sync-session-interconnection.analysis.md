---
analysis_id: "apex-plan-sync-session-workflow-v2-interconnection-analysis"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_slug: "plan-sync-session-interconnection"
run_profile:
  output_tier: "compiled_full"
  safe_mode: "none"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "fresh"
created_at: "2026-07-11T09:46:00Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
supersedes: "ingest-analysis/batch05-handoffs-and-gates.analysis.md (pointer_only, unverifiable; content cross-checked and confirmed below)"
---

# Phase 1 Ingest Analysis — plan/sync/session interconnection (isolation-with-overlap)

## 1. Source Identity

```yaml
source_identity:
  title: "Cross-cutting synthesis across apex-plan, apex-sync, apex-session SKILL.md contracts"
  author_or_origin: "Derived from the three primary sources analyzed in batch06-08, not a new raw source."
  source_authority_level: "secondary"
  source_authority_rationale: "This is an LLM-authored synthesis of primary-source claims already established in batch06/07/08; every cross-cutting claim below cites the specific primary-source line ranges it is built from."
  source_scope: "How the three packages divide work, where they deliberately overlap (shared vocabulary, shared gate concepts), and why that overlap makes the system resilient rather than redundant-as-waste."
  source_limitations:
    - "No direct evidence of a live multi-turn conversation exercising all three skills together; this synthesis is contract-level, not runtime-observed (see U001 in batch08)."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: >
    apex-plan, apex-sync, and apex-session are isolated by exclusive ownership of distinct
    process-scope items, but deliberately overlap on a shared vocabulary (the H1 status enum),
    a shared boundary-declaration pattern (each names the others' territory as explicitly
    forbidden to itself), and a shared gate discipline (nothing consequential happens without
    an explicit operator/gate signal) — and it is exactly that overlap that lets any one
    package's failure be caught by the other two's boundary checks instead of propagating silently.
  compact_summary: >
    Isolation: each package owns a disjoint process_scope (apex-plan: PM1-3/PD1-2/PD4;
    apex-sync: 8 deterministic reports; apex-session: PM6/KB1-3/KB6/PD5-6). No process_scope
    item appears twice.
    Overlap #1 - shared vocabulary: the H1 status enum (open/in-progress/blocked/done/deferred)
    is defined identically in all three SKILL.md files, so any package can validate a status
    value without depending on another package's code.
    Overlap #2 - mirrored boundary declarations: apex-plan's hands_off_to_apex_sync/
    hands_off_to_apex_session lists are the same operations apex-sync's and apex-session's own
    boundary/scope-routing sections claim as their own -- the boundary is asserted from both
    sides, so a drift in one file's boundary list is independently checkable against the other
    two.
    Overlap #3 - shared gate discipline: apex-plan's operator_gate, apex-sync's dry-run default,
    and apex-session's operator_validation gate are three separate implementations of the same
    principle -- nothing consequential happens by default; a human or an explicit flag must
    confirm it.
    This is resilience-by-redundant-cross-check, not accidental duplication: if apex-plan's
    boundary list ever silently expanded to include, say, status mutation, apex-session's own
    "no_new_project_decomposition"-style self-declared boundary would not itself catch that
    (each package only self-declares its own forbidden list), but a KB or reviewer diffing the
    three contracts against each other would immediately see the mismatch -- which is precisely
    the kind of cross-file consistency check this KB is built to support for a future reader
    or LLM.
  relevant_to_kb_because:
    - "Directly answers the operator's stated goal: understanding how the three skills are isolated but have redundant overlaps so the system stays resilient."
  likely_not_relevant_for:
    - "Runtime/operational evidence (no transcripts of live multi-skill sessions were available to this KB run)."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "apex-plan SKILL.md lines 32-44 vs apex-sync SKILL.md lines 43-54,111-152 vs apex-session SKILL.md line 188"
      reason: "The three-way cross-reference proving the handoff triangle is consistent: what apex-plan says it hands off to apex-sync/apex-session matches what apex-sync's Required Outputs and apex-session's routing step 1 claim to receive."
      extraction_priority: high
    - section_ref: "apex-plan SKILL.md lines 73-76 vs apex-sync SKILL.md lines 78-109 vs apex-session SKILL.md line 259 (no_script_execution)"
      reason: "All three independently forbid themselves from arbitrary script execution except apex-sync's one narrow, explicitly-named script path -- the 'no ambient scripting' norm is enforced three times, not once."
      extraction_priority: high
  reusable_definitions: []
  reusable_processes:
    - "Macro-to-micro reading order for a new LLM: read all three frontmatter descriptions first (macro: what does each package do and NOT do) -> read each Skill Contract yaml block (meso: exact owned/handed-off/forbidden operations) -> read each Procedure and Failure Modes section (micro: step-by-step behavior and exact trigger/correction pairs) -> re-read the three frontmatter descriptions once more with the micro detail in mind to confirm the macro boundary actually holds end-to-end."
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "isolation-with-overlap"
    concept_label: "Isolation with deliberate, resilience-producing overlap"
    source_pointer: "synthesis of apex-plan SKILL.md lines 32-44/78-90, apex-sync SKILL.md lines 45-54/193-208, apex-session SKILL.md lines 248-261"
    summary: "Each package's process_scope is disjoint (isolation), but the boundary between packages is asserted redundantly from both sides and the shared H1 vocabulary and gate discipline are repeated in all three files -- overlap that exists specifically to make drift detectable rather than to duplicate work."
    confidence: high
  - concept_slug: "macro-meso-micro-reading-order"
    concept_label: "Macro -> meso -> micro -> meso -> macro comprehension loop"
    source_pointer: "derived from the structural layering common to all three SKILL.md files: frontmatter (macro) -> Skill Contract yaml (meso) -> Procedure/Failure Modes (micro)"
    summary: "Each SKILL.md is itself already organized macro-to-micro (one-paragraph description, then structured contract, then step-by-step procedure); understanding the three-package system requires the same loop applied across all three files, then back up to confirm the macro claims (the frontmatter 'does not' clauses) actually hold once the micro detail (failure modes, exact forbidden operations) is checked."
    confidence: medium
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "handoff-triangle"
    entity_label: "apex-plan <-> apex-sync <-> apex-session handoff triangle"
    entity_type: other
    source_pointer: "apex-plan SKILL.md lines 32-44, 231-241; apex-session SKILL.md line 188"
    summary: "apex-plan hands proposals to apex-sync (computation) and apex-session (mutation); apex-session routes decomposition asks back to apex-plan and ranking/blocker/registry/drift/score asks to apex-sync; apex-sync stays strictly read-side except the registry write exception. Three one-directional handoff edges plus two routing-back edges from apex-session complete the triangle."
    confidence: high
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The 6 operations apex-plan hands off to apex-sync (SKILL.md lines 32-38) exactly match the semantic content of apex-sync's own Required Outputs list (next_action, blocker, registry, stall, drift, score/focus_candidate/dependency_validation), with no operation named by apex-plan as 'apex-sync's job' that apex-sync's own SKILL.md fails to claim as its output."
    source_pointer: "apex-plan raw/other/SKILL.md lines 32-38 vs apex-sync raw/notes/SKILL.md lines 45-54"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-session is the only package whose SKILL.md contains an explicit routing step (step 1) that reads live operator input and dispatches part of a mixed request to the other two packages before doing its own work -- apex-plan and apex-sync do not have an equivalent explicit dispatch step in their own procedures, they only declare what they refuse to do."
    source_pointer: "apex-session raw/refs/SKILL.md line 188; apex-plan raw/other/SKILL.md lines 139-153 (no equivalent dispatch step); apex-sync raw/notes/SKILL.md lines 111-152 (step 2 is a boundary check, not a dispatch to a named package)"
    confidence: medium
    claim_label: source_backed_summary
```

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      C002's claim that apex-session is uniquely the "dispatcher" package is a structural
      observation from static text comparison, not confirmed against a runtime trace where a
      mixed request actually got split three ways. Medium confidence is intentional; a future
      session-transcript source could raise or lower this.
    source_pointer: "apex-session raw/refs/SKILL.md line 188"
    proposed_handling: revisit_source
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  concepts:
    - "concepts/three-package-boundary.md (update with C001, add isolation-with-overlap framing)"
    - "concepts/isolation-with-overlap.md (new page)"
  summaries:
    - "summaries/apex-plan-sync-session-workflow-summary.md (update source_refs to real hashes)"
audit_items: []
manifest_updates: []
```

## 9. Compile Decision

Output tier is `compiled_full`. Continue into Phase 2 wiki compile once the operator issues `approve ingest`.
