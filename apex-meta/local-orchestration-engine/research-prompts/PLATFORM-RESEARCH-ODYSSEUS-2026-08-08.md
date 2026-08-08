---
title: "Platform Research Prompt — Odysseus"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
candidate: Odysseus
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md
---

# Deep Research Prompt — Odysseus

## Mission

Evaluate **Odysseus AI** as a candidate runtime component behind the APEX/FEE bounded local execution architecture. Do not assume Odysseus is the executor merely because earlier hypotheses considered it. Determine what it actually executes today, how much autonomous/orchestration authority it imports, and whether its browser/tool/local-model capabilities can be subordinated to externally frozen APEX/FEE work packets and evidence contracts.

Locked architecture:

```text
Layer 4 subscription/deep-reasoning AI -> strategy, planning, research, synthesis, judgement
Layer 3 Claude Code/Codex -> scarce difficult coding/architecture/debugging/verification
Layer 2 local LLM execution operator -> bounded operations, small recovery, evidence, escalation
Layer 1 deterministic execution -> Python/PowerShell/Git/validators/ledgers/exact transforms
```

APEX/FEE remains the default hypothesis for authority, work-packet state, capabilities, checkpoints, evidence and escalation.

## Evidence requirements

Use current primary evidence wherever possible:

1. official Odysseus repository/source code;
2. official documentation and current releases;
3. relevant official issues/discussions for verified deployment limitations;
4. direct executed tests where available.

For every consequential claim, classify the evidence as source-code verified, officially documented, measured, inferred, or unknown.

## Locked architecture decisions to respect

- FEE/custom deterministic spine remains the authority/evidence/state hypothesis;
- fresh vs persistent subscription sessions are declared in work packets;
- browser adapters may be provider-specific behind a common bounded execution contract;
- low-risk UI recovery may occur locally, but auth/CAPTCHA/account/payment/security ambiguity stops;
- local file/code edits are bounded/mechanical unless a later authority decision says otherwise;
- tools should be action IDs + externally validated arguments rather than arbitrary shell from model text;
- jobs need multiple explicit roots/repositories with distinct permissions;
- Git is capability-based and destructive history operations prohibited/escalated;
- project and personal automation need separate trust profiles;
- model backend must remain swappable;
- blocked overnight work checkpoints while independent safe jobs may continue;
- structured evidence/action logging is mandatory;
- captured web/model/source content has zero execution authority.

## Mandatory user-flow corpus

### UF-A — Subscription research executor
Evaluate authenticated browser/session control, work-packet-selected fresh/persistent conversation, prompt submission, upload/download, deep-research waiting, exact capture/provenance, logout/challenge handling, resume and hostile-content containment.

### UF-B — Script failure recovery
Evaluate declared Python/PowerShell/process execution, bounded log/exit inspection, allowlisted recovery actions, argument validation outside model reasoning, one-safe-retry behavior, arbitrary-command containment and compact escalation packets.

### UF-C — Detective evidence collection
Evaluate Git/filesystem inspection, tests, hashes, file presence, timestamps, source references, contradiction candidates and structured evidence packaging while avoiding final authority/validity judgement.

### UF-D — Database / knowledge hygiene
Evaluate constrained file/data operations, schema adherence, dry-run/transaction support, bounded formatting anomaly recovery, unknown-field preservation and semantic ambiguity escalation.

### UF-E — Multi-repo / multi-folder execution
Evaluate per-job roots with read/write distinctions, several repositories per job, Windows paths, provenance, Git capabilities and ability to delegate enforcement to a thin external FEE broker if native controls are incomplete.

### UF-F — Personal weekly execution
Evaluate separate profiles/credentials/roots/capabilities, sensitive-action gating, auditability, resumable unattended execution and whether Odysseus can avoid mixing personal and project trust zones.

## Hard gates

Return `PASS`, `PASS_WITH_EXTERNAL_BROKER`, `FAIL`, or `UNKNOWN` for:

1. Authority containment.
2. Job-scoped permissions.
3. Resumability after runtime/browser/model interruption.
4. Evidence capture sufficient for APEX/FEE.
5. Safe escalation instead of uncontrolled autonomous continuation.
6. Practical Windows viability on Intel Core Ultra 7 258V / ~32 GB RAM / Intel Arc 140V with browser/local-model/dev-tool coexistence.

Hard-gate failure overrides aggregate score.

## Odysseus-specific questions

1. What is the current Odysseus runtime architecture and execution model?
2. Which local-model backends/formats/providers are supported today?
3. What is the real Windows deployment path: native, WSL, containers or other?
4. What browser/web capabilities exist and do they work with authenticated subscription sessions?
5. How are tasks/workspaces/sessions persisted and resumed?
6. What shell/filesystem/Git/process tools exist?
7. How are tool permissions defined? Can individual tools and roots be restricted per job?
8. Can all dangerous tool arguments be externally validated by FEE before execution?
9. Can arbitrary model-generated commands be disabled or replaced by bounded action schemas?
10. How does Odysseus represent tool failures, partial completion, retries and continuation?
11. Can it consume an externally frozen state machine/work packet without inventing its own goal hierarchy?
12. What autonomous planning/orchestration concepts might conflict with Weekly Orchestrator or Multi-Agent Orchestration?
13. Can those overlapping control-plane features be disabled, ignored or placed below FEE?
14. What action/event logs exist, and can they deterministically feed APEX evidence artifacts?
15. How are browser/model/source prompt-injection attacks handled?
16. Can failures stop and route to a closed set of escalation destinations?
17. What state isolation exists across jobs, projects and personal profiles?
18. What runtime overhead exists before local model/browser load?
19. What update/release cadence and integration breakage risk exists?
20. What licensing/security/data-handling constraints matter?

## Role hypotheses to test

1. Odysseus as **primary bounded executor behind FEE**.
2. Odysseus as **local-model/tool workspace behind FEE** with its own orchestration disabled/minimized.
3. Odysseus as **browser/session capability provider for selected flows**.
4. Odysseus as **specialized executor for a subset of UF-A..UF-F**.
5. Odysseus excluded because it imports too much overlapping control plane or lacks containment/Windows fit.

## Scoring

0–100 scores with confidence 0–100:

| Dimension | Weight |
|---|---:|
| FIT | 18 |
| BOUND | 15 |
| BROWSER | 14 |
| TOOLS | 12 |
| RECOVERY | 10 |
| AUDIT | 9 |
| MULTIROOT | 8 |
| LOCALMODEL | 5 |
| WINDOWS | 4 |
| RESOURCE | 3 |
| MAINT | 2 |

Also score UF-A..UF-F separately.

## Required output

1. Executive finding.
2. Current-runtime reality map with versions/commit SHAs.
3. UF-A..UF-F evidence table.
4. Hard-gate table.
5. Weighted score + confidence.
6. Windows/runtime/local-model assessment.
7. Browser/session assessment.
8. Tool/root/permission containment assessment.
9. State/resume/evidence assessment.
10. Control-plane overlap analysis versus APEX Weekly + Multi-Agent Orchestration.
11. Strongest Odysseus role in a hybrid architecture.
12. External FEE wrappers/brokers required.
13. Unknowns requiring local bake-off.
14. Concrete benchmark fixtures.
15. Rejected roles and reversal triggers.
16. Evidence appendix.

End with:

```yaml
platform_research_result:
  candidate: Odysseus
  evidence_date: null
  versions_or_commits_reviewed: []
  runtime_reality: {}
  per_user_flow_scores: {}
  weighted_scores: {}
  score_confidence: {}
  hard_gate_results: {}
  windows_fit: {}
  browser_fit: {}
  local_model_fit: {}
  permission_model: {}
  state_and_resumability: {}
  audit_and_evidence: {}
  duplicated_orchestration_risk: {}
  strongest_role: null
  required_external_brokers: []
  unresolved_unknowns: []
  benchmark_tests_required: []
  rejected_roles: []
  reversal_triggers: []
  overall_confidence_0_to_100: null
```
