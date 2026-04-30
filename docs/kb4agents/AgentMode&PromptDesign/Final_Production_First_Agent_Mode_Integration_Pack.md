# Final Production-First Agent Mode Integration Pack

## 1. What changed

This integration pack closes the seven-step production-first update flow.

The key correction is now explicit:

> For subscription-browser Agent Mode runs that are meant to create files, KB updates, prompt artifacts, or unified diffs, the first active run must produce the requested artifact. Validation, plausibility review, second research, and learning documentation happen after a concrete artifact exists.

This directly corrects the repeated failure pattern where sophisticated prompt design produced control scaffolding, ledgers, audits, source gates, and “next action” reports while the actual requested KB files or diffs were not produced.

### Core shift

| Old failed pattern | New production-first pattern |
|---|---|
| Pre-analysis first | Target artifact first |
| Ledgers and control files as output | File/diff/KB artifact as output |
| Validation checklists defined but not run | Validation after artifact exists |
| Broad all-system audit | One selected agent / one target file group |
| “Recommended next action” as completion | Completion only when artifact exists |
| Iteration described conceptually | Continuation produces the next named artifact |
| Source gap blocks all production | Source gap becomes caveat/blocked claim inside target files when possible |

---

## 2. Files patched

| File | Purpose of patch | Status |
|---|---|---|
| `Production_First_Iteration_Learning_Record.md` | Captures the high-evidence learning that production-first iteration should be the default for file/diff/KB/prompt production runs. | Complete learning artifact |
| `GPT_Agent_Mode_Business_Playbook.md` | Adds the production-first rule to the Agent Mode business playbook and warns against governance-first prompt runs. | Patch artifact produced; needs raw patch validation before repo application |
| `agents/prompt_design/BEST_PRACTICES.md` | Adds target-artifact-first prompt design guidance and control-artifact-substitution prevention. | Patch artifact produced |
| `agents/prompt_design/MISTAKES_FAILURES.md` | Adds “control artifact substitution” and “validation theater” as prompt-design failure modes. | Patch artifact produced |
| `agents/prompt_design/LEARNING.md` | Promotes production-first artifact prompting as a supported learning pattern. | Patch artifact produced |
| `agents/prompt_design/AGENT_CARD.md` | Updates expected outputs and quality gates to enforce artifact-first prompt design. | Patch artifact produced |
| `agents/prompt_design/ESSENCE.md` | Compresses production-first doctrine into prompt-design activation behavior. | Patch artifact produced |
| `agents/workflow_process/BEST_PRACTICES.md` | Adds production-before-auxiliary-control and no-governance-as-deliverable rules. | Patch artifact produced; hunks need regeneration before direct application |
| `agents/workflow_process/MISTAKES_FAILURES.md` | Adds governance-first substitution and pre-analysis loop as workflow failures. | Patch artifact produced; hunks need regeneration before direct application |
| `agents/workflow_process/LEARNING.md` | Adds production-first iteration as a supported workflow learning pattern. | Patch artifact produced |
| `agents/workflow_process/AGENT_CARD.md` | Adds production-first continuation behavior and fixes metadata drift. | Patch artifact produced |
| `agents/workflow_process/ESSENCE.md` | Compresses workflow-level production-first sequence and fixes metadata drift. | Patch artifact produced |
| `OPERATING_SPINE_CANON.md` | Clarifies that OpenClaw remains operating-spine-first at system level while bounded artifact runs are production-first inside the file-production loop. | Patch artifact produced; path confirmed |
| `LEARNING_SYSTEM.md` | Adds production-first iteration as promoted learning. | Patch artifact produced; exact live path needs confirmation before application |
| `PROCESS_BLUEPRINT_SYSTEM.md` | Adds production-first blueprint rule. | Patch artifact produced; exact live path needs confirmation before application |
| `QA_HYGIENE_PROTOCOL.md` | Adds governance-first substitution as a hygiene finding class and closure rule. | Patch artifact produced; exact live path needs confirmation before application |
| `Production_First_Diff_Validation_Report.md` | Validates the produced artifacts after they exist. | Complete validation artifact |

### Mechanical status

The flow succeeded at the behavior level: it produced concrete artifacts before validation. It did **not** fully succeed at repo-application readiness. Several patch artifacts are Markdown-wrapped and some hunks are not valid raw unified diffs. Before repo application, the patches should be regenerated or converted into raw `.patch` files and checked with `git apply --check`.

---

## 3. Core doctrine now added

### Production-first doctrine

- **Rule:** For artifact-producing tasks, create the requested target artifact first.
- **Rule:** Validate after the artifact exists; do not let validation scaffolds replace production.
- **Rule:** Improve the produced artifact in a second pass if validation finds concrete defects.
- **Rule:** Document learning only after there is a produced artifact to learn from.
- **Rule:** “Recommended next action” is not completion when the user asked for a file, diff, KB update, or prompt artifact.

### Named anti-pattern

**Governance-first substitution**

A run is asked to create a concrete artifact, but instead produces planning, source ledgers, claim caches, acceptance-test scaffolds, broad audit reports, or other control surfaces while the requested target artifact remains missing, unvalidated, or unusable.

### Severity rule

- **P1:** The run is presented as successful or blocks downstream work while the target artifact is absent or unusable.
- **P2:** The run is clearly labeled as a partial diagnostic and not as the requested production result.

### Closure rule

A governance-first substitution finding closes only when the concrete target artifact exists and has been validated. A better plan, broader ledger, cleaner audit, or next-step recommendation does not close it.

---

## 4. Future Agent Mode prompt template

Use this template for the next subscription-browser Agent Mode run when the goal is to patch one Special Ops agent KB folder.

```text
/agent

Use this prompt as the controlling instruction.

REPOSITORY:
leela-spec/MasterOfArts

MODE:
production_first_one_agent_diff

SELECTED_AGENT:
<agent_slug>

TARGET_FOLDER:
docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/agents/<agent_slug>/

TARGET_FILES:
1. BEST_PRACTICES.md
2. MISTAKES_FAILURES.md
3. LEARNING.md
4. AGENT_CARD.md
5. ESSENCE.md

SOURCE_INDEX:
SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

PRIMARY OBJECTIVE:
Read the selected agent’s indexed source files and the five existing target files, then produce one review-ready unified diff that patches exactly those five target files.

SUCCESS CONDITION:
The run is successful only when a concrete unified diff exists for the selected agent’s five target files.

NON-GOALS:
- Do not create batch scope contracts.
- Do not create source ledgers.
- Do not create claim caches.
- Do not create acceptance-test files.
- Do not create group-level control artifacts.
- Do not audit all agents.
- Do not patch other agent folders.
- Do not produce a recommendation-only answer.
- Do not browse the web.
- Do not commit, push, apply changes, or open a pull request.

SOURCE RULES:
1. Read the source index only enough to identify sources assigned to SELECTED_AGENT.
2. Read only sources assigned to SELECTED_AGENT, plus direct target preimages.
3. Use primary sources for doctrine.
4. Use supporting sources only to clarify or extend primary doctrine.
5. Use evidence-only sources only for failure examples, not positive doctrine.
6. If a required source is missing, do not switch into audit/control mode. Instead:
   - still patch the five target files if possible;
   - mark affected claims as provisional or blocked inside those files;
   - record the source limit in metadata/body text;
   - continue producing the unified diff unless the target files themselves are unavailable.

PRODUCTION-FIRST RULE:
Create the target diff before broad validation or learning documentation. Minimal source/target reading is allowed, but the first substantive output must be the five-file patch.

PATCH RULES:
1. Treat the live target files as the only valid preimages.
2. Preserve unrelated text exactly.
3. Patch only the smallest sections needed to integrate the selected improvement.
4. Keep the five-file structure intact.
5. Do not rewrite whole files unless the target file is structurally unusable.
6. Use valid unified diff format with real hunk ranges.
7. Do not include Markdown commentary inside the raw patch.
8. If you also provide a Markdown review wrapper, include the raw patch separately.

REQUIRED OUTPUT ARTIFACT:
Create one downloadable artifact named:

<agent_slug>.production_first.ALL_CHANGES.patch

The artifact must contain only the raw unified diff.

VALIDATION AFTER PATCH CREATION:
After creating the raw patch:
1. Run or simulate a strict patch-format check.
2. Run `git apply --check <agent_slug>.production_first.ALL_CHANGES.patch` if the environment supports it.
3. If the check fails, repair the patch once and rerun the check.
4. If the check still fails, return the patch plus the exact failure reason. Do not pretend validation passed.

FINAL RESPONSE FORMAT:
Return only:

- selected_agent:
- target_folder:
- source_files_read:
- target_files_read:
- files_changed:
- files_unchanged:
- raw_patch_artifact:
- git_apply_status: check_passes | check_fails | not_available
- blockers:
- next_agent_recommendation:

STOP CONDITION:
Stop immediately after returning the patch artifact and validation status. Do not create additional control files, audits, manifests, or future plans.
```

---

## 5. Operator checklist

Use this before starting the Agent Mode run.

| Check | Pass condition |
|---|---|
| **One selected agent** | The prompt contains exactly one `SELECTED_AGENT`. |
| **Exactly five target files** | Only `BEST_PRACTICES.md`, `MISTAKES_FAILURES.md`, `LEARNING.md`, `AGENT_CARD.md`, and `ESSENCE.md` are in scope. |
| **Target artifact named** | The required output is a raw `.patch` file, not a report. |
| **No control artifacts** | The prompt forbids scope contracts, ledgers, claim caches, acceptance-test files, and group artifacts. |
| **No all-system audit** | The prompt forbids auditing all agents or broad package-level review. |
| **Production-first wording** | The prompt says the first substantive output must be the five-file patch. |
| **Source gaps bounded** | Missing sources become source-limit caveats inside the five target files when possible. |
| **Validation after output** | `git apply --check` appears only after patch creation. |
| **Stop condition** | The run stops after patch artifact and validation status. |
| **No recommendation-only completion** | The run cannot finish with “next steps” instead of the patch. |

---

## 6. Anti-pattern checklist

Reject or stop the run if any of these appear.

| Anti-pattern | Why it is unsafe |
|---|---|
| **“Before producing the patch, create a source ledger.”** | Reopens governance-first substitution. |
| **“Create acceptance tests first.”** | Validation scaffolding can replace artifact creation. |
| **“Audit the whole package before patching.”** | Converts one-agent production into all-system audit. |
| **“Mark blockers and recommend next run.”** | Can become recommendation-only completion. |
| **“Produce a Markdown patch summary only.”** | Not mechanically usable; raw patch must exist. |
| **“Use bare `@@` hunk headers.”** | Not valid unified diff for application. |
| **“Use generated KB files as source truth.”** | Generated files are targets/preimages, not doctrine authority. |
| **“Continue through all agents.”** | Violates one-agent/one-diff discipline. |
| **“Validation not checked, but conclusion says validated.”** | Validation theater. |
| **“More guardrails instead of target output.”** | The exact failure pattern being corrected. |

---

## 7. Promotion recommendation

### Recommendation

Promote the production-first doctrine into the playbook, Prompt Design agent KB, Workflow / Process agent KB, and shared operating doctrine after converting the produced Markdown patch artifacts into mechanically valid raw patches.

### Promotion state

`promote_after_patch_validation`

### Required pre-promotion actions

1. Convert each `.patch.md` artifact into a raw `.patch` file or regenerate the patch from live repo files.
2. Confirm exact live repo paths for shared doctrine targets.
3. Run `git apply --check` for each raw patch.
4. Fix invalid hunks, especially bare `@@` hunks in Phase 4 and Phase 5.
5. Only then apply or submit the patch set for human review.

### Immediate next production run

Use the template in section 4 for the next selected agent.

Recommended next target:

```text
SELECTED_AGENT:
information_design
```

Reason:

- It is foundational for KB structure and source/status visibility.
- It is less source-blocked than routing/hygiene agents.
- It provides a clean test of the production-first one-agent/five-file template.
