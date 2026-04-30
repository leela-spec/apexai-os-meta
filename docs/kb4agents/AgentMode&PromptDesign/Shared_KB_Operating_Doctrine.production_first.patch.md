# Shared KB / Operating Doctrine — Production-First Patch Artifact

## Phase

`CONTINUE 5`

## Target

Shared OpenClaw / Special Ops operating doctrine surfaces.

## Files patched

1. `OPERATING_SPINE_CANON.md`
2. `LEARNING_SYSTEM.md`
3. `PROCESS_BLUEPRINT_SYSTEM.md`
4. `QA_HYGIENE_PROTOCOL.md`

## Patch purpose

Integrate the core production-first learning into shared doctrine without turning OpenClaw itself into a file-production-first architecture.

The distinction is:

- **System authority remains operating-spine-first.**
- **Artifact manufacturing runs are production-first inside the bounded file-production loop.**
- **Validation, plausibility checks, and second research happen after a concrete artifact exists.**
- **Pre-analysis, ledgers, and control surfaces must not substitute for the requested output.**

## Unified diff

```diff
diff --git a/OpenClaw/07_finalopenclawsystem/managed/rules/OPERATING_SPINE_CANON.md b/OpenClaw/07_finalopenclawsystem/managed/rules/OPERATING_SPINE_CANON.md
--- a/OpenClaw/07_finalopenclawsystem/managed/rules/OPERATING_SPINE_CANON.md
+++ b/OpenClaw/07_finalopenclawsystem/managed/rules/OPERATING_SPINE_CANON.md
@@
 - Docs may explain, exemplify, freeze, or reconcile, but they may not be the sole runtime authority for load-bearing behavior.

 - File production is subordinate manufacturing work. It may be required by the operating spine, but it must not become the master process of the system.
+
+- Within an already-authorized artifact-manufacturing run, production is first inside the bounded file-production loop: create the requested target artifact, then validate, plausibility-check, research further, and improve it. This does not invert runtime authority; it prevents governance scaffolding from substituting for the requested file, diff, or KB output.
@@
 ## Boundaries and anti-drift rules

 - Do not reinstall a file-production-first architecture under new terminology.
+
+- Do not confuse system-level operating-spine-first authority with artifact-run sequencing. The system stays operating-spine-first, but a bounded production pass must still produce the requested artifact before broad audit/control expansion.
+
+- Do not let scope contracts, source ledgers, claim caches, acceptance-test files, or other control surfaces become substitute deliverables when the user asked for a concrete file, diff, KB update, or prompt artifact.

 - Do not treat README files, docs, or rituals as substitute hosts for constitutional runtime law.
diff --git a/OpenClaw/07_finalopenclawsystem/managed/processes/LEARNING_SYSTEM.md b/OpenClaw/07_finalopenclawsystem/managed/processes/LEARNING_SYSTEM.md
--- a/OpenClaw/07_finalopenclawsystem/managed/processes/LEARNING_SYSTEM.md
+++ b/OpenClaw/07_finalopenclawsystem/managed/processes/LEARNING_SYSTEM.md
@@
 ## Learning intake

 Lessons may be captured from observed successes, observed failures, audits, user corrections, source changes, or implementation results when they are tied to a concrete workflow or artifact.
+
+### Production-first iteration learning
+
+When repeated prompt/workflow runs produce control surfaces instead of the requested artifact, record the failure as **governance-first substitution**.
+
+This learning is high-evidence, high-impact, and low-risk when all of the following are true:
+
+- the user asked for concrete production such as files, diffs, KB updates, or prompt artifacts;
+- the run instead produced pre-analysis, ledgers, broad audits, or acceptance-test scaffolds;
+- the missing output could have been produced first and validated afterward;
+- later validation, plausibility review, or second research can safely operate on the produced artifact.
+
+The promoted lesson is:
+
+> For artifact-production work, use `produce -> validate -> improve -> document learning`. Do not use `pre-analyze -> create control surfaces -> maybe produce`.
+
+This lesson must be stored as workflow and prompt-design doctrine, not merely as a one-off anecdote.
@@
 ## Promotion criteria

 A learning may be promoted when it is supported by evidence, has a clear operational effect, does not conflict with stronger authority, and can be expressed as a bounded rule or process change.
+
+Production-first iteration may be promoted without waiting for many additional examples when the risk of applying it is low and the impact is high: it narrows the first pass to the requested target artifact while preserving validation and research as follow-up passes.
diff --git a/OpenClaw/07_finalopenclawsystem/managed/processes/PROCESS_BLUEPRINT_SYSTEM.md b/OpenClaw/07_finalopenclawsystem/managed/processes/PROCESS_BLUEPRINT_SYSTEM.md
--- a/OpenClaw/07_finalopenclawsystem/managed/processes/PROCESS_BLUEPRINT_SYSTEM.md
+++ b/OpenClaw/07_finalopenclawsystem/managed/processes/PROCESS_BLUEPRINT_SYSTEM.md
@@
 ## Process blueprint rules

 A process blueprint defines a repeatable sequence for bounded work. It must name the objective, target artifact, authority, allowed scope, stop condition, and verification method.
+
+### Production-first blueprint rule
+
+For subscription-browser Agent Mode runs that create or modify files, diffs, KB artifacts, prompts, playbooks, or agent documents, the blueprint must make the **first active production phase** create the target artifact.
+
+Use this default sequence:
+
+1. **Produce:** create the requested file, diff, patch, KB update, or prompt artifact.
+2. **Validate:** check the artifact against target, source, structure, patchability, and user intent.
+3. **Improve:** make a second-pass correction based on validation findings.
+4. **Document learning:** capture only the reusable lesson that changed future behavior.
+
+Do not begin these runs with broad governance surfaces unless the user explicitly requested audit-only or planning-only work.
@@
 ## Anti-patterns

 - Do not design a process that hides the actual deliverable behind unbounded preparation.
+- Do not let pre-analysis become the deliverable.
+- Do not let ledgers, scope contracts, claim caches, acceptance tests, or control reports substitute for the requested artifact.
+- Do not call a run iterative unless it has explicit stop points and each continuation produces the next named artifact.
 - Do not combine unrelated work types unless the user explicitly authorizes a mixed pass.
diff --git a/OpenClaw/07_finalopenclawsystem/managed/rules/QA_HYGIENE_PROTOCOL.md b/OpenClaw/07_finalopenclawsystem/managed/rules/QA_HYGIENE_PROTOCOL.md
--- a/OpenClaw/07_finalopenclawsystem/managed/rules/QA_HYGIENE_PROTOCOL.md
+++ b/OpenClaw/07_finalopenclawsystem/managed/rules/QA_HYGIENE_PROTOCOL.md
@@
 ## Hygiene finding classes

 Hygiene findings identify structural risks, source gaps, drift, stale state, broken dependencies, unsafe scope expansion, and verification failures.
+
+### Governance-first substitution
+
+**Definition:** A run is asked to create or patch a concrete artifact, but instead produces planning, source ledgers, claim caches, acceptance-test scaffolds, broad audit reports, or other control surfaces while the target artifact remains missing, unvalidated, or unusable.
+
+**Severity:** P1 when the run is presented as successful or blocks downstream work; P2 when clearly labeled as a partial diagnostic.
+
+**Evidence signals:**
+
+- requested file/diff/KB artifact is absent;
+- output contains many control artifacts but no usable target artifact;
+- validation says `not_checked`, `not_yet_run`, or equivalent while claiming readiness;
+- continuation steps redesign the process instead of producing the next named artifact;
+- the first phase expands into all-system audit when a one-agent or one-file target was requested.
+
+**Required correction:**
+
+1. Stop the control-first expansion.
+2. Restate the target artifact.
+3. Produce the artifact in the next pass.
+4. Validate the produced artifact.
+5. Only then add broader audit, research, or learning documentation.
@@
 ## Closure rule

 A hygiene finding may close only when the affected artifact or control surface has been corrected, verified, and linked to the durable output that resolves the issue.
+
+For governance-first substitution, closure requires the concrete target artifact to exist. A better plan, broader ledger, or cleaner audit does not close the finding by itself.
```

## Notes

- This patch keeps the OpenClaw authority model intact: **operating spine remains above file production**.
- The production-first rule is scoped to **artifact-manufacturing runs**, especially subscription-browser Agent Mode workflows.
- The shared doctrine now has a named failure class: **governance-first substitution**.
- The closure rule prevents future runs from treating better control scaffolding as a successful substitute for target output.
