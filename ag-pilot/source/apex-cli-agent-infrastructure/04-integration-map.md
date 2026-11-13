---
type: Reference
id: APEX-INFRA-INTEGRATION-20261112
title: Existing File to Target Integration Map
description: Concrete retain, reference, adapt and add decisions with exact source and target locations.
status: draft
adoption_status: proposed_for_operator_review
tags: [integration, files, approval, ownership]
---

# Integration map

**Keep all existing semantic owners in place.** The canonical [machine map](design/integration-map.json) covers every retrieved source used for the design plus proposed new target artifacts. It records source hashes, action, decision, stage, validation, rollback and approval status. All live changes are unapplied.

The [pointer proposals](design/pointer-patch-proposals.json) contain exact old/new text for six bounded corrections across three existing files. They are review data, not a new mutation schema or an executable installer. Fresh hash and unique-match checks are mandatory before any later application. The correct link in `governance-schemas.md` is retained. The existing `git-sync.md` is reused, not recreated.

## Proposed changes and retained operating surfaces

| Existing path → target | Action | Stage / decision | Reason |
|---|---|---|---|
| `.agents/skills/qmd/SKILL.md` → same path | adapt_after_owner_resolution | S1 / D-19 | Align the conceptual-query exception with the owner’s keyword-zero-result rule for the current profile; do not reindex or change daemon settings. |
| `.claude/CLAUDE.md` → same path | retain_and_reference | S1 / D-14 | Preserve explicit system activation, Weekly separation and Plan-Sync-Session ownership. |
| `.claude/agents/meta-detective.md` → same path | retain_and_reference | S2 / D-12 | Reuse role doctrine when that system is explicitly active; native illustrative verifier wrappers are not a replacement. |
| `.claude/settings.json` → same path | inspect_effective_policy_before_any_change | S1 / D-15, D-09 | Top-level defaultMode is not proof of effective bypass. No automatic permission expansion or config rewrite is proposed. After S1 profile inspection, a separately approved S3 change may add only the tested hook entries, preserving permission fields and unrelated settings. |
| `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json` → same path | retain_and_reference | S1 / D-18 | Retain the actual canonical patch_intent.v1 schema; exact-match proposals do not replace or restate this machine owner. |
| `.github/copilot-instructions.md` → same path | retain_and_reference | S4 / D-07 | Retain observed carrier; Copilot runtime parity was not audited. Expansion requires an explicit separate supported-profile probe. |
| `AGENTS.md` → same path | adapt_after_approval | S1 / D-18 | Correct the verified standard pointer only; preserve Git Dispatch and the live core. Further carrier simplification needs D-07 probes. |
| `CLAUDE.md` → same path | retain_then_conditional_adapter | S3 / D-07 | Keep the current carrier; test native AGENTS/CLAUDE precedence and one-copy loading before any exact projection replacement. |
| `GEMINI.md` → same path | retain_then_conditional_adapter | S3 / D-07 | Keep the carrier while actual Gemini versus Antigravity profile use is resolved; migration is not inferred. |
| `apex-meta/informatics/final/research/08-read-trace-routing-experiments/artifacts/stage1/score_stage1_corrected.py` → same path | reference_and_selective_reuse | S1 / D-20 | Retain historical semantics and mixed results. Reuse exact mutation-scope check; replace attempted-read and invalid-validator proxies. |
| `apex-meta/informatics/final/research/10-ultra-upgrade-validation/fixtures/armB_hook_agy.py` → same path | reference_only_do_not_install | S3 / D-09 | Benchmark-specific hooks inform failure cases and payload leads; do not promote them to production policy. |
| `apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py` → same path | retain_frozen_then_new_scoring_revision | S1 / D-20 | Keep historical scorer exact. An approved future revised scorer must reject demonstrated counterexamples and retain reproducible version identity. |
| `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml` → same path | retain_and_reference | S1 / D-02 | Keep all 23 tags and seven explicit refs. A new sync ref or wording reconciliation is an owner-level proposal requiring separate review. |
| `apex-meta/informatics/final/specs/execution-modes.md` → same path | retain_pending_owner_resolution | S1 / D-02 | Preserve current aggregate definitions. Do not silently delete EM-12 or other delegated views; record ownership consolidation separately. |
| `apex-meta/informatics/final/specs/execution-modes/git-sync.md` → same path | retain_and_reference | S1 / D-23 | Existing standalone EM-12 adapter; no file creation needed. Its relation to the duplicate general EM-12 owner is RC-11. |
| `apex-meta/informatics/final/specs/execution-modes/patch-discipline.md` → same path | adapt_after_approval | S1 / D-18 | Correct two too-shallow relative links; retain the actual authoritative patch schema and worked example. |
| `apex-meta/informatics/final/specs/general-informatics-router.md` → same path | retain_as_portable_artifact | S1 / D-02 | Preserve the source-owned portable artifact; do not introduce it as another mandatory runtime hop. |
| `apex-meta/informatics/final/specs/governance-schemas.md` → same path | retain_and_reference | S1 / D-02 | Correct patch-schema relative link already resolves; do not apply the initially suspected unnecessary correction. |
| `apex-meta/informatics/final/specs/standard.md` → same path | adapt_after_approval | S1 / D-18 | Correct unique index/migration links and the diagnostic rule locator; preserve substantive text. |
| `apex-meta/informatics/final/tools/agent_eval_runner.py` → same path | retain_as_simulation_evidence | S1 / D-20 | Do not use assigned outcomes as agent measurements. Preserve historical script; reuse only source-grounded fixture ideas. |
| `apex-meta/informatics/final/tools/apex_carrier_sync.py` → same path | adapt_after_approval | S3 / D-17 | Reuse block comparison. Parameterize selected roots and explicit preview; retain backups and avoid uncontrolled cross-repository writes. |
| `apex-meta/informatics/final/tools/check_vendor_drift.py` → same path | adapt_after_approval | S3 / D-17 | Separate unknown/skipped from in-sync, include selected non-Markdown adapter assets, and separate manifest refresh from comparison. |
| `apex-meta/informatics/final/tools/okf_validator.py` → same path | reuse_with_bounded_validation | S1 / D-20 | Use existing supported structural diagnostics; add independent rule identity/semantic checks outside its current coverage. |
| `apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml` → same path | retain_and_reference | S1 / D-14 | Retain the live manifest of system, role and skill boundaries; infrastructure does not create a new orchestration system. |
| `apex-meta/orchestration/agents/meta-ops/INTEGRATION-apex-plan-sync-session.md` → same path | retain_and_reference | S1 / D-14 | Retain the scoped Meta Ops/backbone integration contract, with Plan, Sync and Session responsibilities distinct. |
| `apex-meta/orchestration/schemas/authority-state.schema.md` → same path | retain_and_reference | S1 / D-12 | Retain candidate/verified/invalidated authority, basis digest and confirmation boundaries. Automatic digest enforcement remains an open code item. |
| `apex-meta/orchestration/schemas/handoff-packet.schema.md` → same path | retain_and_reference | S1 / D-14 | Retain the named-system handoff_packet owner; activation and evaluation sidecars do not add fields to it. |
| `apex-meta/orchestration/schemas/review-verdict.schema.md` → same path | retain_and_reference | S1 / D-12 | Retain the scoped independent-review verdict owner. This package does not claim that the live Detective workflow ran. |
| `apex-meta/orchestration/workflows/detective-review.md` → same path | retain_and_reference | S1 / D-12 | Reuse independent validity/alignment lenses inside the explicitly activated named system; no new reviewer fleet or automatic promotion. |
| new → `apex-meta/informatics/final/activation/rules.json` | add_after_approval | S1 / D-02 | Add the proposed activation metadata index. It does not become the semantic owner. |
| new → `apex-meta/informatics/final/activation/rule-registry.schema.json` | add_after_approval | S1 / D-02 | Add the exact proposed metadata schema with registry. |
| new → `apex-meta/informatics/final/activation/history.json` | add_after_approval | S1 / D-02 | Keep historical crosswalks and candidate decisions outside the active view. |
| new → `.agents/skills/apex-decision-support/SKILL.md` | add_after_approval | S2 / D-04 | Pilot a task-centered decision procedure with source references; target root is conditional on D05/native discovery. |
| new → `.agents/skills/apex-governed-authoring/SKILL.md` | add_after_approval | S2 / D-04 | Pilot governed artifact authoring with actual FA/EM owners. |
| new → `.agents/skills/apex-research-cycle/SKILL.md` | add_after_approval | S2 / D-13 | Pilot sustained research/recovery; current state remains in existing run files. |
| new → `.agents/hooks/apex_hook.py` | add_after_approval | S3 / D-09 | Conditional production predicate interface from retained design. Canary scripts are not a completed production enforcement engine. |
| new → `.codex/hooks.json` | add_after_approval | S3 / D-09 | Proposed native Codex configuration; exact-path fetch at pinned Apex revision returned 404; workstation remains unknown. |
| new → `.agents/hooks.json` | add_after_approval | S3 / D-09 | Proposed native Antigravity configuration; exact-path fetch at pinned Apex revision returned 404; workstation remains unknown. |
| new → `.codex/agents/apex-verifier.toml` | add_after_approval | S2 / D-12 | Optional bounded native role wrapper only when useful; inherited permissions are not a new sandbox. |
| new → `<existing-run-dir>/activation-state.json` | add_after_approval | S2 / D-11 | Optional proposed coverage/receipt sidecar. It grants no authority and is not an existing domain schema. |
| new → `<approved-profile>/native-adapter-configuration` | add_after_approval | S3 / D-24 | Host-specific configuration projection; choose one actual scope after the read-only probe. No universal global path is asserted. |

## Review boundaries

The source-only entries retain research, accepted scoped decisions and implementation evidence without making them active runtime instructions. No historical candidate, experiment or remote snapshot is promoted by inclusion. The map’s “reference only” action means evidence is used here; it does not mean that agents must load that source on every task.

Current roots and account profiles must be read before adding native configuration. A repository 404 for `.codex/hooks.json` or `.agents/hooks.json` does not establish absence on a workstation. No entry can replace global settings or broaden permissions. The top-level Claude `defaultMode` defect is a probe item; this package deliberately supplies no bypass-enabling patch.

Later exact carrier-block replacement is permitted only after the selected native profile proves equivalent loading and a scoped operator approval names the target. Full-file rewrites remain prohibited. Existing Plan, Sync, Session, Weekly and AIRouting owners are not relocated or merged. Copilot and other retained infrastructure remain provenance unless a later approved profile is actually audited.

**Failure guard:** resolve a missing or changed source before applying a proposal, preserve unrelated bytes, and never treat this map’s target paths as installed or accepted state.
