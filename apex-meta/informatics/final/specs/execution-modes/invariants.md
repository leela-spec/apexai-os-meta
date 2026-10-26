---
type: Adapter
id: ADPT-EXEC-INVARIANTS-v0.2
title: Core Execution Invariants & Mode Dispatch
description: The EM-01..EM-05 always-apply invariants and the IF-routing table that dispatches to each adapter.
tags: [execution-modes, invariants, dispatch]
status: current
---

## 1. Core Execution Invariants (Top-Loaded Primacy)

The following invariants apply across all execution modes. Front-load these boundaries (aiming for roughly the first ~500 tokens):

- **EM-01 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition**: Never overwrite existing repository files via full-file rewrites. Modify existing files strictly using surgical exact-match patch blocks or verified AST patch intents.
- **EM-02 [P0 | I96/E95/R05] Handover Non-Paralysis Invariant**: Never write a handover to defer an action or ambiguity that available tools can resolve immediately. If a fact is checkable, invoke the tool and check it now.
- **EM-03 [P0 | I96/E95/R06] Step-by-Step Context & File Iteration Invariant**: Never front-load massive amounts of files or documentation at session start. Load context step-by-step per active stage and materialize each iteration's output into a dedicated file.
- **EM-04 [P0 | I95/E95/R08] Target Dominance**: Optimize for the most balanced, value-efficient, and effective path to the stated user outcome. Do not substitute process ceremony, secondary schemas, or self-verifying scripts for the required deliverable. Canonical: `AD-01`.
- **EM-05 [P0 | I94/E92/R10] Two-Strike Pivot Rule**: Stop repairing a failing subsystem if two consecutive fix attempts fail to advance the product. Reconsider the architecture and select an alternative approach. Canonical: `AD-02`; per-subsystem tracking mechanics in `AD-24`.

### Conditional Execution Mode Dispatch (`IF`-Routing)

Evaluate the active task against these conditional gates and load only the matching adapter section:

```xml
<execution_dispatch>
  IF task == "architectural_tradeoff_or_qa_alignment"  THEN apply="#2-adapter-1-qa-decision-matrix"          ELSE skip
  IF task == "multi_candidate_comparison_or_bakeoff"   THEN apply="#3-adapter-2-comparison--bake-off-rubric" ELSE skip
  IF task == "existing_file_mutation_or_patch"         THEN apply="#4-adapter-3-exact-match-patch-discipline" ELSE skip
  IF task == "session_handover_or_subagent_delegation" THEN apply="#5-adapter-4-handover--handoff-protocol"   ELSE skip
  IF task == "multi_step_iterative_or_mmm_execution"   THEN apply="#6-adapter-5-iterative-context--mmm-execution" ELSE skip
  IF task == "repository_sync_or_synch_request"        THEN apply="#7-adapter-6-git-sync--file-preservation"  ELSE skip
</execution_dispatch>
```

---
