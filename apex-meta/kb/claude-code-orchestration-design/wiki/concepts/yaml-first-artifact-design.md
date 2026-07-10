---
title: "YAML-First Artifact Design"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "yaml-first-artifact-design"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; yaml-first artifact design"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C011, B04-C014; state blocks and proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# YAML-First Artifact Design

## Definition

YAML-first artifact design is the convention of encoding an artifact's identity, state, authority, reads, writes, and gates as concise, fenced YAML blocks before any explanatory prose, so a future agent can parse and route the artifact without re-reading narrative text. This concept directly answers the compile plan's `token_economy_and_information_design_index` core question `yaml_first_artifact_design`, and it is evidenced not only by Phase 1 claims about state blocks and proof contracts (B04-C011, B04-C014) but by the plain physical structure of the Phase 1 batch files themselves — including the very batch file this KB used to ingest this claim.

## Operating Rules

```yaml
rules:
  - "Give every artifact a machine-parseable identity/state block (frontmatter or an equivalent leading yaml block) before any prose explanation."
  - "Put required fields (source refs, status, confidence, gates) in yaml, not buried in sentences, so a downstream agent can check them without full-text comprehension."
  - "Keep narrative prose for judgment and synthesis; keep structured facts, lists, and state in yaml."
  - "Do not treat yaml-first shape as a hard lint gate by default; it is presently a soft, low-risk documentation convention rather than an enforced high-risk gate."
reads:
  - "frontmatter and other fenced yaml blocks"
writes:
  - "structured fields plus short clarifying prose"
token_efficiency: "Predictable, uniform fields reduce repeated interpretation overhead for any agent that later reads the artifact."
drift_controls: "Required fields make missing authority, status, or source pointers immediately visible instead of silently absent from prose."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names yaml_first_artifact_design as an explicit core question inside token_economy_and_information_design_index, alongside packet_size_budget and smallest_useful_file_shape."
    coverage: "Frames why file/packet design choices (including yaml-first shape) matter for token cost and drift."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies claims about explicit state frames, atomic task packets, and file-output/task-closure proof — all of which are represented as structured fields rather than prose."
    coverage: "Claims B04-C011 (state frames/atomic task packets) and B04-C014 (file-output and task-closure contracts require explicit fields, not narrative claims of success)."
  - source_id: "phase1-batch04-apex-application-patterns (self-evidence, structural)"
    rationale: "The batch file itself is the clearest available evidence: its own frontmatter and every major section (source_files_read, claims, concepts_extracted, entities_extracted, contradictions_or_tensions, open_questions, proposed_phase_2_wiki_targets) is a separately fenced yaml block."
    coverage: "Direct structural example of yaml-first design already in productive use across this KB's Phase 1 output."
  - source_id: "phase1-process-retrospective-20260702"
    rationale: "Confirms this is not a one-off shape: the retrospective's structural-validation table shows all four Phase 1 batch files share the identical required-section, yaml-block-per-section pattern."
    coverage: "Section 2, validated_batches; corroborates the convention is KB-wide, not particular to one file."
```

## Macro / Meso / Micro

### Macro

The `token_economy_and_information_design_index` treats file and packet design as a lever for reducing token cost, drift, hallucination, and context overload, and it names `yaml_first_artifact_design` as one of its explicit core questions alongside `smallest_useful_file_shape`, `packet_size_budget`, and `refs_not_copies`. Read together, the index is asking: what shape should an artifact take so an agent can act on it cheaply and correctly? YAML-first design is this KB's compiled answer for the identity/state/authority layer of that shape — put the parseable facts in yaml, keep prose for synthesis and judgment.

### Meso

Two independent lines of Phase 1 evidence converge on this answer. First, the apex-application-patterns claims: high-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction (B04-C011), and file-output/task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed (B04-C014) — all of these are naturally expressed as structured fields, not as narrative assertions of "it worked." Second, and more directly, this very KB's own Phase 1 batch files are built exactly this way: a yaml frontmatter block up top (title, source_batch_id, kb_slug, phase, status, gate policy), followed by one fenced yaml block per section for source files read, claims, concepts, entities, contradictions, open questions, and proposed Phase 2 targets. The Phase 1 process retrospective independently validates that all four batch files share this identical required-section shape, so this is a demonstrated, repeated authoring convention rather than an incidental choice in one file.

### Micro

- Compile plan `token_economy_and_information_design_index` core question `yaml_first_artifact_design`, alongside `smallest_useful_file_shape` and `packet_size_budget` (compile plan lines ~122-134).
- B04-C011: explicit state frames and atomic task packets for high-risk execution, instead of chat-history reconstruction.
- B04-C014: file-output/task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status.
- Self-evidence: `phase1-batch04-apex-application-patterns.md` lines 3-23 (frontmatter yaml block) and lines 33-103, 107-277, 281-342, 346-383, 387-425, 429-460, 464-487 (one fenced yaml block per required section).
- `phase1-process-retrospective-20260702.md` lines 19-73: structural validation confirming all four batch files (01-04) share the same required-section, yaml-block shape.
- Operational note (not a Phase 1 ingested claim): the operator decision log treats "style" and "low-risk documentation conventions" as soft-enforced rather than hard-enforced (`operator-phase1-review-decisions-20260702.md`, Q002 soft_enforce list), which is why yaml-first shape is stated here as a strong convention, not a hard gate.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "token_economy_and_information_design_index names yaml_first_artifact_design as a core question for reducing token cost, drift, and context overload through file/packet design."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, token_economy_and_information_design_index core_questions"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction, and file-output/task-closure contracts require explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns.md, claims B04-C011, B04-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "This KB's own Phase 1 batch files (including phase1-batch04-apex-application-patterns.md) are themselves built as a leading yaml frontmatter block followed by one fenced yaml block per required section, giving direct self-evidence that yaml-first design is already in productive, repeated use across this KB."
    source_pointer: "phase1-batch04-apex-application-patterns.md lines 3-23, 107-277; corroborated by phase1-process-retrospective-20260702.md lines 19-73"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "How should artifact packets be shaped to stay small and machine-checkable?"
    leads_to: "claude-code-orchestration-design/concepts/packet-size-budget.md"
    rationale: "Packet-size-budget is the sibling token_economy_and_information_design_index question about size limits for the same kind of structured artifact."
  - question: "Should a downstream agent read the full raw source or a compiled reference?"
    leads_to: "claude-code-orchestration-design/concepts/refs-not-copies.md"
    rationale: "Refs-not-copies is the adjacent token_economy_and_information_design_index answer about pointing to sources instead of duplicating them; both concepts reduce token cost through file shape."
  - related_page: "claude-code-orchestration-design/concepts/compiled-kb-before-raw-source.md"
    relation: "Both concepts come from the same specialized index and both use this KB's own compiled artifacts as self-evidence."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "token_economy_and_information_design_index core_questions, yaml_first_artifact_design"
    supports: "Definition and Macro section."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claims B04-C011, B04-C014"
    supports: "Meso section: structured state/proof requirements."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "file structure lines 3-23, 107-277"
    supports: "Micro section: direct structural self-evidence of yaml-first design."
  - source_id: "phase1-process-retrospective-20260702"
    source_pointer: "lines 19-73, validated_batches"
    supports: "Corroboration that yaml-block-per-section is a KB-wide, not single-file, convention."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Whether yaml-first shape should become a hard-enforced lint rule (a later S7+ deterministic index/lint concern) versus remain a soft documentation convention is not yet decided; the operator decision log currently treats 'style' and low-risk documentation conventions as soft-enforced only."
    source_pointer: "operator-phase1-review-decisions-20260702.md, Q002 soft_enforce list"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Exact required-field schemas per page type are a deterministic S7+ lint concern; S6/Phase 2 supplies source-grounded content, not the final lint rule set."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, section 8 next_action"
    proposed_handling: "leave_as_gap"
```
