# Tier 0 KB Validation — Deterministic Addendum

This addendum continues `tier0-kb-validation-and-extension-packet.okf.md` at repository commit `b66cab13f10019a8760bd31135d78cae08f58ed8`.

It records the terminal-backed KB validation results supplied by the deterministic executor and closes the decision-critical Claude Code activation-path and compaction questions against current official documentation.

No semantic wiki page, generated KB artifact, Tier 0 runtime file, or source-custody artifact was modified.

```okf
continuation:
  repository:
    baseline_commit: "b66cab13f10019a8760bd31135d78cae08f58ed8"
    tested_commit: "b66cab13f10019a8760bd31135d78cae08f58ed8"
    branch: "main"
    deterministic_run_changed_files: []
    deterministic_run_repository_unchanged: true

  executive_decision:
    overall_status: "supported_with_qualification"
    safe_to_plan: true
    safe_to_patch: true
    safe_to_apply: false
    safe_to_patch_scope:
      - "Case-correct the project activation file from .claude/Claude.md to .claude/CLAUDE.md."
      - "Compact the activation file by retaining durable global constraints, identity, canonical routing pointers, and recovery-critical instructions."
      - "Remove the duplicated weekly-loop procedure rather than repairing its stale G5/APSU copy."
      - "Keep detailed weekly stages, gates, routing, packet validation, and artifact handling in .claude/skills/weekly-orchestrator/SKILL.md and its references."
    excluded_from_safe_patch_scope:
      - "Semantic KB page repairs or extensions."
      - "KB index or retrieval rebuilds."
      - "Mass skill-description rewrites."
      - "Mass agent-description rewrites."
      - "Arbitrary token or word targets."
      - "A new orchestration skill, registry, state machine, or general map."
    highest_value_change: "Create a recognized, compact .claude/CLAUDE.md and eliminate its stale duplicate weekly-loop ownership."
    unresolved_blockers_to_application:
      - "The bounded runtime patch has not been generated or reviewed."
      - "No before/after InstructionsLoaded or /memory proof exists for the renamed activation file."
      - "No no-loss validation has proved every removed global constraint has one canonical destination."
      - "No orchestration regression fixture has run against the proposed runtime patch."

  deterministic_preflight:
    - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb"
      repository_ref: "b66cab13f10019a8760bd31135d78cae08f58ed8"
      preflight: "pass"
      health: "pass"
      lint: "fail: 73 issues"
      quality: "fail: 16 findings"
      audit: "pass"
      status: "pass; wiki and retrieval indexes stale"
      retrieval_health: "pass"
      retrieval_index: "stale"
      source_custody: "inconsistent or incomplete under the current contract"
      blocking_for_query_ready:
        - "strict lint failure"
        - "strict quality failure"
        - "stale wiki index"
        - "stale retrieval index"
      effect_on_tier0_runtime_decision: "does_not_reverse_decision"
      rationale: "The failures concern historical KB maintenance and query readiness; the Tier 0 ownership decision is independently supported by direct current-repository evidence and raw-source verification."

    - kb_root: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2"
      repository_ref: "b66cab13f10019a8760bd31135d78cae08f58ed8"
      preflight: "pass"
      health: "pass"
      lint: "fail"
      quality: "pass"
      audit: "pass: zero audit items"
      status: "pass; wiki and retrieval indexes stale"
      retrieval_health: "pass"
      retrieval_index: "stale"
      source_custody: "payload manifest fresh"
      blocking_for_query_ready:
        - "strict lint failure"
        - "stale wiki index"
        - "stale retrieval index"
      effect_on_tier0_runtime_decision: "does_not_reverse_decision"
      rationale: "The failures prevent current KB certification but do not contradict the current runtime ownership and duplication findings."

  deterministic_interpretation:
    confirmed:
      - "Both KB roots exist and their command surfaces execute successfully."
      - "Required tools and SQLite FTS5 are available."
      - "Neither historical KB is currently query-ready."
      - "Stored retrieval/index artifacts cannot be treated as fresh evidence."
      - "KB v1 requires substantial lifecycle repair before certification."
      - "KB v2 is structurally healthier than KB v1 but still fails strict lint and freshness."
    contradicted_or_corrected:
      - prior_claim: "No deterministic preflight or retrieval-staleness execution has run."
        corrected_status: "closed"
      - prior_claim: "The activation filename and case remain unverified."
        corrected_status: "closed"
        finding: "Claude Code recognizes ./CLAUDE.md or ./.claude/CLAUDE.md. The repository contains .claude/Claude.md instead."
      - prior_claim: "An explicit custom compaction reread procedure may be required."
        corrected_status: "qualified"
        finding: "A recognized project-root CLAUDE.md is reread and reinjected automatically after /compact. Custom recovery instructions should address Apex state/artifact recovery, not reimplement CLAUDE.md reinjection."

  decision_critical_platform_evidence:
    activation_file:
      verified_behavior: "Project instructions are loaded from ./CLAUDE.md or ./.claude/CLAUDE.md."
      repository_observation: "The only active repository candidate found is .claude/Claude.md."
      implication: "Case-correct rename is a prerequisite to relying on the activation file across case-sensitive environments."
      claim_status: "directly_supported"
      evidence: 99
      risk: 91
      impact: 99
      basis: "Current official Claude Code documentation specifies the uppercase filename and current repository search finds only the mixed-case candidate."

    compaction:
      verified_behavior: "Project-root CLAUDE.md is reread from disk and reinjected after /compact."
      implication: "Do not add a redundant instruction telling Claude to reload CLAUDE.md itself. Add only Apex-specific recovery pointers needed to rediscover active state and canonical artifacts."
      claim_status: "directly_supported"
      evidence: 98
      risk: 32
      impact: 84
      basis: "Current official Claude Code troubleshooting documentation explicitly states the project-root reinjection behavior."

  tier0_implementation_candidates:
    - candidate_id: "T0-001"
      current_path: ".claude/Claude.md"
      target_path: ".claude/CLAUDE.md"
      current_owner: "project activation surface"
      problem: "The filename does not match the documented Claude Code project-instruction filename on case-sensitive filesystems."
      smallest_safe_change: "Perform a case-correct Git rename without changing content in the same step."
      content_to_retain: "all current bytes during the rename-only step"
      content_to_relocate_or_replace_with_pointer: "none during rename-only step"
      canonical_destination: ".claude/CLAUDE.md"
      dependencies: []
      required_validation:
        - "git diff --summary proves rename"
        - "git status shows no duplicate mixed-case file"
        - "Claude Code /memory or InstructionsLoaded proof lists .claude/CLAUDE.md"
      claim_status: "directly_supported"
      evidence: 99
      risk: 28
      impact: 99
      safe_to_plan: true
      safe_to_patch: true

    - candidate_id: "T0-002"
      current_path: ".claude/CLAUDE.md after T0-001"
      current_owner: "project activation surface"
      problem: "The file duplicates detailed weekly-loop procedure and contains a stale G5/APSU copy."
      smallest_safe_change: "Retain identity, durable global constraints, canonical pointers, and recovery-critical navigation; remove detailed weekly stages, gates, agent/skill tables, and artifact procedure already owned elsewhere."
      content_to_retain:
        - "identity and global mission"
        - "hard cross-system constraints"
        - "independent-review invariant"
        - "pointers to the final orchestration map"
        - "pointer to weekly-orchestrator for weekly execution"
        - "Apex-specific active-state and artifact recovery pointers"
      content_to_relocate_or_replace_with_pointer:
        - "weekly loop stages and G1-G5 procedure"
        - "detailed skill routing table"
        - "detailed agent routing table"
        - "weekly artifact-handling procedure"
      canonical_destination:
        weekly_runtime: ".claude/skills/weekly-orchestrator/SKILL.md and references"
        system_law: "apex-meta/orchestration/00-START-HERE.md"
        cross_system_map: "apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md"
      dependencies:
        - "T0-001"
        - "exact no-loss mapping ledger"
      required_validation:
        - "before/after line, byte, and token estimate"
        - "structured proof that every removed global rule is retained or has exactly one canonical owner"
        - "grep or schema checks for G1-G5 ownership"
        - "orchestration routing regression fixture"
        - "Claude Code /memory or InstructionsLoaded proof"
      claim_status: "directly_supported"
      evidence: 98
      risk: 54
      impact: 97
      safe_to_plan: true
      safe_to_patch: true

    - candidate_id: "T0-003"
      current_path: ".claude/skills/weekly-orchestrator/SKILL.md"
      current_owner: "weekly orchestration runtime"
      problem: "Apex-specific session recovery may require a compact state/artifact reread sequence, but CLAUDE.md reinjection itself is automatic."
      smallest_safe_change: "Add only a short Apex recovery rule if current weekly state discovery does not already cover context loss."
      content_to_retain: "all current routing, gates, packet validation, and mutation boundaries"
      content_to_relocate_or_replace_with_pointer: "none"
      canonical_destination: ".claude/skills/weekly-orchestrator/SKILL.md or an existing owned reference"
      dependencies:
        - "inspect current state-discovery and resume instructions"
      required_validation:
        - "prove the rule is not duplicate"
        - "simulate missing conversational context with durable artifacts present"
      claim_status: "supported_with_qualification"
      evidence: 82
      risk: 43
      impact: 76
      safe_to_plan: true
      safe_to_patch: false

    - candidate_id: "T0-004"
      current_path: ".claude/skills/*/SKILL.md and .claude/agents/*.md"
      current_owner: "individual skill and agent packages"
      problem: "Only measured description offenders may create material routing or startup-context cost."
      smallest_safe_change: "Generate inventory and nominate offenders; make no blanket edits."
      dependencies:
        - "active-package inventory"
        - "description byte, word, and token estimates"
        - "trigger regression tests"
      required_validation:
        - "literal trigger retention"
        - "input/output/boundary retention"
        - "invocation-mode retention"
      claim_status: "requires_execution_validation"
      evidence: 86
      risk: 78
      impact: 83
      safe_to_plan: true
      safe_to_patch: false

  rejected_already_fixed_and_deferred:
    already_fixed:
      - "precap-week preload name"
      - "precap-next-day preload name"
      - "project-status-overview preload name"
    rejected:
      - "repair the stale weekly loop inside the activation file"
      - "create another orchestration skill"
      - "create another general registry"
      - "adopt BUILD/VERIFY/LOCK as a Tier 0 runtime state machine"
      - "mass-rewrite descriptions"
      - "use an arbitrary numeric token or word target"
    deferred:
      - "semantic KB extensions until exact phrase approve ingest"
      - "KB v1 lifecycle repair"
      - "KB v2 lint and index repair"
      - "description optimization until inventory and regression evidence exist"

  exact_changed_file_ledger:
    deterministic_executor_run: []
    this_orchestrator_continuation:
      - path: "tier0-kb-validation-deterministic-addendum.okf.md"
        change: "created"
        artifact_class: "validation_and_implementation_handoff"
    semantic_wiki_files: []
    tier0_runtime_files: []
    generated_kb_files: []

  final_boundary:
    semantic_wiki_gate_respected: true
    approve_ingest_received: false
    runtime_patch_implemented: false
    safe_to_apply: false
```

## Final interpretation

The deterministic failures prevent either historical KB from being represented as current, lint-clean, fresh, or query-ready. They do not invalidate the Tier 0 runtime recommendation because that recommendation is supported by direct inspection of the current activation surface, current weekly-orchestrator ownership, raw historical sources, and current Claude Code platform behavior.

The safest implementation order is now explicit:

1. rename `.claude/Claude.md` to `.claude/CLAUDE.md` without content edits;
2. prove Claude Code loads the corrected file;
3. compact it by subtraction and canonical pointers;
4. run no-loss, routing, and orchestration regression checks;
5. keep description work and semantic KB repairs outside the Tier 0 patch.
