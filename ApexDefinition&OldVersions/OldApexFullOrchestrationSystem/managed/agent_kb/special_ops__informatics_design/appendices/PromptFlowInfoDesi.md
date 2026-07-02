## Updated promptflow contract — corrected

```yaml
repo: MasterOfArts
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/
audit_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/KB_SYSTEM_RELIABILITY_AUDIT_V1
appendix_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/appendices/
mode: executable_unified_diff_patch
```

## Corrected scope

```yaml
target_files:
  scaffold:
    - ESSENCE.md
    - BEST_PRACTICES.md
    - MISTAKES.md
    - TEMPLATES.md
    - LEARNING_QUEUE.md
  appendices:
    - appendices/**
```

```yaml
write_scope:
  allowed:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/LEARNING_QUEUE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/appendices/**
  forbidden:
    - any Apex repo path
    - any apexai-os-meta path
    - any other MasterOfArts agent KB folder
    - runtime config
    - provider/model config
    - files outside target_root except audit_input read-only
```

```yaml
source_scope:
  read:
    - current_target_files
    - appendix_input
    - audit_input
  use_failure_files_as:
    - process_failure_patterns_only
  do_not_use_failure_files_as:
    - repo_reference
    - target_path_reference
    - content_source_for_informatics_kb
```

---

# Corrected core rule

```text
Update the MasterOfArts Informatics Design KB so the scaffold files and appendices become an excellent machine-readable KB base.

Use the current scaffold files, appendices, and KB_SYSTEM_RELIABILITY_AUDIT_V1 as the only substantive inputs.

Use the failure-analysis files only to prevent process drift, false completion, wrong-repo targeting, wrong-path targeting, filename trust, full invisible rewrites, and unsupported “done” claims.

Do not import Apex repo paths, Apex agent references, or apexai-os-meta target assumptions.
```

---

# Prime directive

```text
Create the best machine-readable Informatics Design KB base in the given MasterOfArts target path.

Integrate high-impact, proven, and operator-approved candidate content from appendices into the scaffold files.

After a strong candidate is integrated into the KB base, update the appendices so the candidate is no longer represented as unresolved future work.

Do not merely append prose. Convert both new and existing content into clear, agent-followable structure.
```

---

# Machine-readability rule

All updated KB content must be optimized for agent execution.

## Required forms

```text
Rule:
Constraint:
Decision:
Validation:
Stop:
Input:
Output:
Procedure:
Template:
Failure:
Candidate:
Status:
Owner:
Applies when:
Do not:
```

## Preferred structures

```text
compact sections
stable headings
tables for decision records
explicit status labels
single-purpose bullets
clear target-file roles
machine-checkable rules
```

## Reject

```text
long prose explanation
essay-style rationale
ambiguous “should” language
hidden rules inside paragraphs
duplicate concepts with unclear role
candidate content hardened without status
human-facing summary instead of executable rule
```

---

# Candidate handling rule

The executor must not decide silently whether a candidate is integrated.

Before applying diffs, it must produce a **Candidate Decision Table**.

```md
| candidate_id/source | candidate_summary | evidence_strength | target_option_A | target_option_B | recommendation | reason | operator_decision |
|---|---|---|---|---|---|---|---|
```

## Allowed recommendation values

```text
integrate_into_scaffold
integrate_into_appendix
split_between_scaffold_and_appendix
keep_as_candidate
reject_obsolete
needs_operator_decision
```

## Operator decision values

```text
approved
rejected
revise
defer
```

## Rule

```text
No candidate may be deleted from appendices unless the decision table shows it was approved and the final validation proves it was integrated into the KB base or otherwise dispositioned.
```

---

# Scaffold file role map

```yaml
ESSENCE.md:
  role: compact activation contract
  receives:
    - highest-priority rules
    - identity of Informatics Design
    - non-negotiable operating constraints
    - machine-readability doctrine

BEST_PRACTICES.md:
  role: execution practice layer
  receives:
    - procedures
    - operating patterns
    - recommended workflows
    - validation practices

MISTAKES.md:
  role: anti-drift and failure-prevention layer
  receives:
    - known failure modes
    - prohibited patterns
    - correction rules
    - process-drift warnings

TEMPLATES.md:
  role: reusable machine-facing schemas
  receives:
    - decision tables
    - audit templates
    - diff report formats
    - candidate evaluation schemas
    - validation output schemas

LEARNING_QUEUE.md:
  role: unresolved or deferred candidate queue
  receives:
    - useful but unapproved candidates
    - candidates needing more evidence
    - operator-deferred items
    - future improvement backlog
```

---

# Appendix update rule

Appendices are writable in this promptflow.

## Appendices must be updated when

```text
a strong candidate is integrated into scaffold files
a candidate is rejected
a candidate is deferred
a candidate is split into scaffold + appendix content
a TODO becomes obsolete
machine-readability status changes
audit status changes
```

## Appendix updates must preserve

```text
candidate IDs
source references
evidence notes
ranking logic
decision history
traceability
```

## Appendix updates may delete candidate rows only when

```text
candidate was approved for integration
integration location is recorded
diff proof exists
final validation confirms the scaffold contains the integrated content
appendix deletion/update is represented in a unified diff
```

Better default than hard deletion:

```text
move candidate from active/future section to integrated/resolved section
```

Only delete if the appendix design clearly expects deletion instead of status transition.

---

# Unified diff rule

All writes must happen through unified diffs.

```yaml
diff_requirements:
  - create one unified diff per changed file
  - include scaffold diffs and appendix diffs
  - validate each diff before applying
  - apply only after candidate decisions are approved
  - fetch back every changed file
  - report exact changed_file_set
```

## Important correction

The previous “minimal patch” framing is removed.

New framing:

```text
Use the smallest safe diff that produces the correct high-quality KB result.

Small is preferred only when it does not reduce quality, coherence, machine-readability, or candidate integration completeness.

Do not rewrite blindly. But do restructure existing content when needed to make the KB machine-readable and internally coherent.
```

---

# Required execution phases

## Phase 1 — Verify target

```text
confirm repo == MasterOfArts
confirm target_root exists
confirm audit_input exists
confirm appendix_input exists
list target files
list appendix files
STOP if any path resolves to Apex/apexai-os-meta
```

## Phase 2 — Read and classify inputs

```text
read current scaffold files
read appendix files
read KB_SYSTEM_RELIABILITY_AUDIT_V1
extract:
  - proven high-impact candidates
  - future research candidates
  - TODOs
  - machine-readability gaps
  - reliability/audit constraints
  - existing scaffold weaknesses
```

## Phase 3 — Candidate decision table

Produce:

```md
| candidate_id/source | candidate_summary | evidence_strength | possible_targets | recommendation | reason | operator_decision |
|---|---|---|---|---|---|---|
```

Stop for operator decision unless the operator has already provided approval rules.

## Phase 4 — Design target updates

For each scaffold and appendix file:

```md
| file | current_role | needed_update | source_candidate | update_type | risk | expected_diff |
|---|---|---|---|---|---|---|
```

Update types:

```text
machine_readability_refactor
candidate_integration
candidate_status_update
todo_resolution
audit_rule_integration
appendix_cleanup
template_addition
failure_rule_addition
```

## Phase 5 — Generate unified diffs

Create diffs for:

```text
scaffold files changed
appendix files changed
```

Each diff must include only the intended file.

## Phase 6 — Validate diffs before applying

```text
diff target path inside allowed write scope
no Apex path
no other agent folder
candidate decisions respected
appendix statuses updated
machine-readable structure improved
no unsupported deletion
no false completion
```

## Phase 7 — Apply diffs

Only apply validated diffs.

## Phase 8 — Fetch-back and final proof

Fetch back every changed file and return:

```yaml
repo:
target_root:
audit_read:
appendices_read:
candidate_decision_table:
operator_decisions_used:
files_changed:
scaffold_files_changed:
appendix_files_changed:
diffs_created:
diffs_applied:
changed_file_set:
forbidden_paths_changed:
fetch_back_verified:
candidates_integrated:
candidates_deleted_or_resolved:
candidates_deferred:
remaining_operator_decisions:
status:
```

---

# Stop conditions

```yaml
stop_if:
  - repo_is_not_MasterOfArts
  - target_root_is_not_exact_path
  - audit_input_missing
  - appendix_input_missing
  - Apex_or_apexai_os_path_detected_as_target
  - candidate_needs_operator_decision
  - deletion_without_integration_proof
  - diff_changes_forbidden_path
  - final_response_lacks_changed_file_set
  - fetch_back_missing_for_changed_file
  - executor_claims_completion_from_prior_summary
```

---

# Final compact promptflow

```text
You are executing the Informatics Design KB update in MasterOfArts only.

Target root:
MasterOfArts/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/

Audit input:
MasterOfArts/OpenClaw/07_finalopenclawsystem/managed/agent_kb/KB_SYSTEM_RELIABILITY_AUDIT_V1

Appendix input:
MasterOfArts/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/appendices/

Goal:
Create an excellent machine-readable Informatics Design KB base by updating the five scaffold files and appendices.

Use:
- current scaffold files
- appendix TODOs
- future research candidates
- machine-readability findings
- KB_SYSTEM_RELIABILITY_AUDIT_V1

Do not use:
- Apex repo paths
- apexai-os-meta target assumptions
- other agent KB folders
- prior execution summaries as completion proof

Failure-analysis files are process-warning inputs only.

Required behavior:
1. Verify exact repo and paths.
2. Read scaffold, appendix, and audit inputs.
3. Extract high-impact and proven candidates.
4. Produce candidate decision table with context, options, recommendation, and operator decision field.
5. Stop for operator decision where needed.
6. Convert both existing and new content into machine-readable structure.
7. Update scaffold files where high-impact approved content belongs.
8. Update appendices after integration, rejection, or deferral.
9. Use unified diffs for every changed file.
10. Validate diffs before applying.
11. Apply diffs only inside target root.
12. Fetch back every changed file.
13. Report changed_file_set and proof.

Core rule:
Make the KB excellent and machine-readable, not merely minimally patched. Preserve traceability. Do not drift target repo or path.
```