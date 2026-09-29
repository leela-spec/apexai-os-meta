# DRAFT — Antigravity OpenProject CLI pilot implementation plan

> **Status: non-authoritative working draft.** This preserves earlier planning work. The receiving AI must verify every claim against fresh local evidence and current primary sources, correct or replace the draft, obtain an independent review, and stop for operator acceptance before implementation.

## Outcome and execution rule

Produce a trustworthy, reproducible Antigravity-to-OpenProject path with the least irreversible work. Every phase is a separate evidence gate. Do not start a dependent phase merely because commands ran; start it only when its named prerequisites satisfy their handoff contracts.

Dependency route:

```text
A -> B -> C
C -> D (upgrade, when scheduled)
C + D if performed -> E
E -> F only for a required gap; otherwise F = not_needed
E + every required F result -> G
A-G evidence -> H
```

Phase D may be scheduled immediately after C or later, but must pass before any post-upgrade claim. Phase F is conditional and may return `not_needed`; it is not a mandatory rewrite stage.

The executor records for every step:

```yaml
step_evidence:
  phase:
  timestamp:
  inputs_and_versions:
  action:
  expected_result:
  observed_result:
  secret_redaction_checked:
  verdict: pass | fail | blocked | gap
  next_authorized_step:
```

Use temporary or ignored local files for command output. Do not commit credentials, instance data, or raw environment dumps.

## Evidence quality rules

- A tool being installed does not prove Antigravity discovers it.
- A skill being discovered does not prove its CLI commands match the installed binary.
- `--help` compatibility does not prove authentication or API compatibility.
- Authentication does not prove the endpoint is the intended instance.
- A successful write response does not prove the intended state; reread it.
- A missing upstream capability is a recorded gap, not permission to broaden scope.
- Open the full source behind a search result before making a conclusion.
- Reuse prior evidence when its relevant input has not changed.

## Phase A — minimum local and target baseline

### Question

Can this exact Antigravity surface host a project-scoped skill, and is there one unambiguous private OpenProject target for later access?

### Inputs

- `agy --version` and `agy --help` output.
- Official Antigravity Agent Skills documentation.
- prior environment evidence in the parent and evidence handovers.
- expected private endpoint supplied by the existing private stack configuration or operator-controlled configuration.

### Actions

1. Confirm `agy` resolves and record its version. Do not inventory unrelated agents.
2. Determine whether the pilot will run in Antigravity 2.0, Antigravity CLI, or the standalone IDE. Record the exact surface.
3. Confirm the workspace root and the officially documented project-scoped skill location: `.agents/skills/<skill-folder>/`.
4. Check whether a skill with the same name already exists. If it does, compare provenance and stop before overwriting it.
5. Record the expected private OpenProject endpoint and a non-secret identity fingerprint that can later distinguish it from the community and stopped duplicate instances.
6. Inspect whether `OP_CLI_HOST` or `OP_CLI_TOKEN` is set, recording presence and precedence only—never values.
7. Reuse the previous runtime inventory unless one of these checks contradicts it.

### Expected output

```yaml
baseline:
  antigravity_surface:
  agy_version:
  workspace_root:
  project_skill_path:
  existing_skill_collision: false
  expected_private_endpoint:
  instance_fingerprint_method:
  overriding_host_variable_present:
  overriding_token_variable_present:
```

### Handoff test

Pass when the Antigravity surface and skill destination are known and the future endpoint can be distinguished without guessing. An unavailable endpoint does not block offline installation; ambiguous identity blocks all live access.

### Stop conditions

- existing skill would be overwritten;
- target endpoint cannot be distinguished;
- a secret is printed or captured—redact the artifact and stop for review;
- the installed Antigravity surface does not support project skills as documented.

## Phase B — acquire and pin a compatible upstream pair offline

### Question

Can a specific CLI revision and Agent Skill revision be paired without credentials or network calls to OpenProject?

### Inputs

- official CLI README, release page, tags, and source revision;
- official Agent Skills README and `openproject-workpackage-crud/SKILL.md` revision;
- Node/npx availability;
- current absence or presence of `op`, `openproject-cli`, and Go.

### Required compatibility fact

Do not pair “latest” artifacts by name. The latest released CLI is v0.5.5 and uses verb-first commands, while the current skill requires noun-first commands. Select either:

1. a released CLI/skill pair whose documented command contracts match; or
2. a pinned CLI development commit and pinned skill commit whose contracts match.

If neither can be reproduced safely on Windows, record the pilot as blocked. Do not silently rewrite the skill or install an unpinned moving branch.

### Actions

1. Record the CLI tag or commit, skill commit, repository URLs, retrieval time, and integrity evidence.
2. Inspect the selected CLI's build requirements and Windows artifact availability. If building is required, present the toolchain addition and provenance before installing it.
3. Acquire the CLI into a user-local, reversible location. Do not replace another `op` executable.
4. Verify executable provenance with the resolved path, version output, and hash.
5. Install the skill project-locally under `.agents/skills/` using a pinned source. If using `npx skills`, first inspect its help and generated plan/output; confirm the selected Antigravity target and destination.
6. Review the installed skill diff against the pinned upstream source. Installation must not add unrelated agents, rules, plugins, or repository files.
7. Run offline help probes:

```text
op --version
op work-package inspect --help
op work-package update --help
op work-package list --help
```

8. Verify the flags required by the pinned skill, including JSON output, type/open inspection, supported update fields, actions, and parent filtering.
9. Do not configure credentials and do not contact OpenProject in this phase.

### Expected output

```yaml
pinned_pair:
  cli_revision:
  cli_path:
  cli_hash:
  skill_revision:
  skill_path:
  installer_and_version:
  command_contract_match:
  unsupported_skill_claims:
  files_added_or_changed:
```

### Handoff test

Pass only when the pinned skill's actual commands and flags match the pinned executable. Installer exit code alone is insufficient.

### Stop conditions

- verb-first CLI paired with noun-first skill;
- selected binary or source is unpinned;
- CLI provenance cannot be established;
- installation touches unrelated files;
- build requires an unapproved system-wide toolchain or elevation;
- any probe makes a live request unexpectedly.

### Rollback

Remove only the newly installed project skill folder and the newly acquired user-local executable after verifying their exact paths. Do not clean the repository or remove pre-existing tools.

## Phase C — prove discovery, target selection, and one read

### Question

Can a fresh Antigravity session discover the pinned skill and read one known Work Package from the intended private instance?

### Inputs

- passed Phase A baseline;
- passed Phase B pinned pair;
- operator-controlled private endpoint;
- dedicated read-capable credential or an explicitly approved temporary read credential;
- one known safe Work Package ID and expected non-secret attributes.

### Actions

1. Start a fresh Antigravity session so discovery does not rely on the installation session's memory.
2. Verify the skill is listed/discoverable from the project-scoped path. If not, diagnose path versus surface once, correct only the install path, and retry once.
3. Configure the CLI using its supported profile/token mechanism without putting the token in repository files or command arguments.
4. Check whether environment variables override the selected profile. If they do, resolve the ambiguity before connecting.
5. Make a non-mutating instance/API-root request and compare the observed host and fingerprint to Phase A.
6. Authenticate and identify the current user if supported by the selected CLI/API path.
7. Execute one deterministic read through the skill:

```text
op work-package inspect <known-id> --format json
```

8. Verify the returned ID, project, subject or another preselected stable attribute. Redact descriptions or user data not needed as evidence.
9. Repeat the read directly with the same pinned CLI command to distinguish skill-routing failure from CLI/API failure.

### Expected output

```yaml
read_proof:
  fresh_session_skill_discovered:
  resolved_endpoint:
  instance_fingerprint_match:
  authenticated_identity:
  work_package_id:
  expected_attributes_match:
  skill_read_result:
  direct_cli_read_result:
```

### Handoff test

The install/read pilot passes only when a fresh session discovers the skill and both the skill-mediated and direct CLI reads return the expected Work Package from the verified private instance.

### Stop conditions

- redirect or resolved host differs from the expected endpoint;
- instance fingerprint is absent or mismatched;
- environment override changes the intended target;
- authentication identity is broader or different than expected;
- the command attempts a mutation;
- skill and direct CLI results disagree.

### Failure routing

| Observation | Classification | Next action |
|---|---|---|
| skill not discovered, files correct | Antigravity discovery gap | verify documented surface path once; then block |
| skill command rejected by CLI | pinned-pair defect | return to Phase B; no live workaround |
| CLI reads, skill fails | skill routing defect | record minimal upstream issue or patch candidate |
| CLI cannot read API root | endpoint/auth/API defect | diagnose only that boundary |
| wrong instance answers | identity safety failure | stop all live work |

## Phase D — prepare the OpenProject upgrade as an independent change

### Question

Can the private installation be moved from its exact current version to the selected current stable Community release with a tested recovery boundary?

This phase begins only after Phase C or when the operator explicitly prioritizes the upgrade. It is not needed to prove CLI installation or an initial read against the current instance.

### Inputs

- exact running OpenProject version and image digest;
- exact Compose files and overrides used by the private stack;
- PostgreSQL version and database topology;
- attachment storage, configuration, plugins/add-ons, and secrets inventory;
- official current upgrade documentation and each intervening major's notes;
- maintenance window and operator approval for runtime changes.

### Actions

1. Re-check the current stable release and pin exact images; never use a floating `latest` tag.
2. Derive the supported major sequence. For a 14.x source and 17.x target, plan sequential transitions `14 -> 15 -> 16 -> 17` unless current official tooling explicitly performs and verifies those migrations on a restored copy.
3. Check each major's PostgreSQL, Redis, worker, plugin, configuration, and Compose requirements. Include the official pre-17 background-worker handling where applicable.
4. Produce backups of database, attachments, configuration, and secrets metadata sufficient to restore the previous image and state together.
5. Test restore into an isolated target before touching the private instance. Verify login, Work Package count/sample, attachments, projects, and API access.
6. For each hop, state image/digest, prerequisite, migration command/behavior, health criteria, data checks, and rollback boundary.
7. Execute only after the runbook and recovery test are reviewed. Stop after each major and verify before advancing.
8. Leave irreversible optional conversions disabled unless separately approved.

### Expected output

```yaml
upgrade_runbook:
  source_version_and_digest:
  target_version_and_digest:
  major_hops:
  database_compatibility:
  compose_changes:
  backup_set:
  restore_test_result:
  per_hop_checks:
  rollback_boundary:
  irreversible_options_disabled:
```

### Handoff test

Pass when the target instance is healthy on the pinned target version, data/API smoke checks pass, and the prior version can be restored from the tested backup set. Re-run the Phase C read proof after the upgrade.

### Stop conditions

- no exact source version or image identity;
- backup omits database, attachments, or required configuration;
- restore was not tested;
- unsupported major jump;
- failed migration, health check, or sample-data comparison;
- rollback would restore only an image but not matching migrated data.

## Phase E — dedicated identity and bounded write proof

### Question

Can a least-privilege Leela agent identity perform only the approved pilot writes in an isolated test project?

### Inputs

- passed Phase C against the current target and, if performed, passed Phase D;
- administrator access for one bounded setup action;
- proposed dedicated Leela test-project name and identifier;
- proposed non-admin agent role and permissions;
- explicit operator authorization for the listed test mutations;
- known exact workflow action names where a transition is tested.

### Actions

1. As the administrator, create or select one dedicated Leela integration-test project. Record and verify its numeric ID, identifier, name, URL, and cleanup/archive policy before granting agent access.
2. Create or select the dedicated non-admin identity and token outside the repository.
3. Grant membership only to Leela and the verified integration-test project, with the smallest permissions needed for the chosen tests.
4. Re-run identity, project, and endpoint checks using the dedicated token.
5. Start with one reversible write: create one clearly named test Work Package in the test project.
6. Reread and compare project, type, subject, author, and timestamps.
7. Perform only individually approved operations supported by the pinned upstream contract: update a safe field, attach a test file, or run an exact named workflow action.
8. After every mutation, reread before the next mutation.
9. Archive or otherwise handle test artifacts according to the selected cleanup policy; do not assume delete permission.

### Expected output

```yaml
write_proof:
  target_identity_match:
  test_project_id:
  test_project_identifier:
  test_project_cleanup_policy:
  agent_identity:
  effective_project_membership:
  permissions_tested:
  mutations_authorized:
  mutation_results:
  reread_results:
  unexpected_side_effects:
  test_artifact_disposition:
```

### Handoff test

Pass when every authorized mutation has matching reread evidence, no unapproved project is accessible for writing, and no unexpected side effect remains unresolved.

### Stop conditions

- target or user identity mismatch;
- unexpected access outside the allowed projects;
- rejected or ambiguous workflow action;
- partial or multi-field update not predicted by the command;
- operation needs a capability absent from upstream—record a gap and stop that operation;
- operator has not authorized the concrete mutation.

### Required-capability matrix

Before handing off to the real-task phase, classify each required program outcome. Test only the smallest representative operation and route an unsupported required outcome to Phase F.

| Outcome | Minimum proof | Route if upstream lacks it |
|---|---|---|
| Work Package read/create/update | response plus reread of stable fields | Phase F |
| hierarchy | read direct children; create/link a child only if required and authorized | Phase F |
| relation/dependency | create in test scope and read the relation back | Phase F |
| workflow/status | execute an exact allowed action and reread status | Phase F |
| evidence/comment | add bounded test evidence and reread activity | Phase F |
| Kanban representation | after upgrade, confirm the test status appears in the intended board view | record UI/config blocker |
| Gantt/dependency representation | after upgrade, confirm the test dependency appears in the intended Gantt view | record UI/config blocker |

An outcome may be `not_required_for_pilot`, but anything retained in the parent runtime definition of done must eventually be `pass` or explicitly deferred with that broader completion marked incomplete.

## Phase F — resolve only required capability gaps

### Question

Does an accepted pilot outcome require a capability the pinned upstream pair cannot perform?

### Inputs

- one concrete failed or unsupported operation from Phase E or the real-task design;
- exact desired outcome and risk class;
- upstream CLI/skill evidence;
- the smallest relevant subset of the preserved 58-handler package;
- the selected instance's exact version, API root/schema or HAL capability responses, and matching official API documentation for that operation.

### Actions

1. Describe the gap as input, desired transformation, expected output, and why existing upstream commands cannot achieve it.
2. Check current upstream issues/source for the one operation; do not repeat the whole architecture comparison.
3. Retrieve only candidate handlers relevant to that operation. Open their full source before conclusions.
4. Compare their HTTP method, endpoint, payload, auth, confirmation behavior, and assumptions with the selected instance's actual API capabilities and the matching official documentation. Do not assume the newest online documentation describes an older instance.
5. Audit Windows/macOS differences only on this selected execution path. API semantics are generally platform-neutral; paths, shelling, executable lookup, temporary files, permissions, and quoting are not.
6. Choose the least change: wait for upstream, contribute upstream, add a narrow wrapper, or patch one retained path.
7. Produce a contextual patch proposal with exact files, tests, rollback, and operator gate. Do not refactor or catalog unrelated handlers.
8. If the operator authorizes that exact patch, apply it, run the named focused tests, exercise the operation in the integration-test project, and verify the result by reread. If authorization is not granted, mark the operation deferred and the dependent outcome incomplete.

### Expected output

```yaml
required_gap:
  operation:
  upstream_limit:
  api_contract:
  candidate_local_handlers:
  platform_specific_risks:
  selected_resolution:
  exact_patch_scope:
  operator_authority:
  implementation_result:
  verification:
  rollback:
```

### Handoff test

Pass when the required operation is proven safely after its exact authority gate. A deferred operation is a truthful phase result but does not satisfy a dependent required outcome. “All handlers reviewed” is not a handoff requirement.

### Stop conditions

- no accepted outcome requires the operation;
- proposed change expands beyond the selected path;
- API contract is inferred from old handler code rather than current documentation;
- more than ten tracked files would change without a blast-radius review;
- solution creates a second PM database or always-running custom orchestrator.

## Phase G — one real Leela task and fresh-session resume

### Question

Can OpenProject route one real task into repository truth and receive evidence back without becoming a duplicate semantic authority?

### Inputs

- passed read proof and any write capabilities actually required;
- one operator-selected Leela Work Package;
- qualified repository references in that Work Package;
- accepted write policy for evidence/status updates;
- repository authority rules and task-specific source artifacts.

### Actions

1. Start from the Work Package and retrieve its explicit identifiers and repository references.
2. Validate that every referenced repository path exists and that semantic claims are grounded in their owning artifacts.
3. State readiness/blockers before implementation. Do not copy full semantic documents into OpenProject.
4. Perform the repository task under normal repository instructions. Do not invoke an optional framework unless the operator explicitly selected it for this task.
5. Record concise evidence: commit or diff identity, validations, outcome, blockers, and exact repository references.
6. Write back only the fields/actions allowed by the accepted policy, rereading after each write.
7. End the session. In a fresh Antigravity session, start only from the Work Package and qualified repository references, then state the correct current status and next action.

### Expected output

```yaml
real_task_proof:
  work_package:
  repository_sources_grounded:
  readiness_decision:
  implementation_evidence:
  openproject_updates:
  post_write_reread:
  fresh_session_resume:
  semantic_duplication_detected: false
```

### Handoff test

Pass when the fresh session resumes accurately without chat history and OpenProject contains operational state plus references—not copied semantic authority.

### Stop conditions

- Work Package contradicts higher-authority repository truth;
- references are absent, stale, or ambiguous;
- the write policy does not authorize the needed update;
- fresh session requires hidden chat context;
- OpenProject content is being used to overwrite accepted product semantics.

## Phase H — production-policy decision and generalization

### Question

Which mutations may run without per-action confirmation, and is the proven Antigravity route ready to generalize?

### Inputs

- evidence from Phases A–G;
- observed failure modes and reversibility;
- the still-unresolved write-autonomy choices.

### Decision presentation

Present concrete options rather than an abstract yes/no:

| Class | Examples | Recommended temporary treatment |
|---|---|---|
| Read-only | inspect Work Package, list children | automatic after target verification |
| Low-impact reversible | add comment, update a clearly scoped test subject | explicit task authorization; verify by reread |
| Workflow/structure | change status, create child, create dependency, change priority | per-action confirmation until operator decides |
| High-impact | close/archive work, bulk edits, project settings, membership | explicit operator confirmation |
| Destructive | delete or irreversible conversion | separate approval and recovery plan |

### Actions

1. Ask the operator to select or modify the classes using examples from the actual pilot.
2. Record the decision in the existing program owner; do not change repository-wide agent rules unless explicitly requested.
3. Decide whether to generalize to another agent using the same pinned contract. Do not duplicate the integration before the Antigravity evidence is green.
4. Reassess pinned upstream revisions before generalization; upstream is a moving target.

### Expected output

```yaml
production_policy:
  read_policy:
  low_impact_write_policy:
  workflow_and_structure_policy:
  high_impact_policy:
  destructive_policy:
  decision_owner:
  decision_reference:
  generalization_authorized:
```

### Handoff test

Pass when the operator's selected policy is recorded in the existing program owner and the generalization decision is explicit. Unresolved autonomy blocks unattended production writes, but does not invalidate approved reads or completed test-scope evidence.

### Stop conditions

- no operator decision for an unattended production-write class;
- proposed policy grants broader authority than the pilot exercised;
- decision would require repository-wide rule changes that were not explicitly requested;
- upstream revisions changed without repeating the compatibility probes.

## Final verification checklist

- [ ] Every phase records its exact inputs and versions.
- [ ] Every command has an expected result and observed result.
- [ ] Each transformation has a postcondition, not only an exit code.
- [ ] Each phase names the artifact passed to the next phase.
- [ ] Every live call verifies target instance and identity.
- [ ] Every write is authorized and reread.
- [ ] Secrets are absent from repository diff and evidence.
- [ ] CLI and skill revisions are pinned and command-compatible.
- [ ] Fresh-session skill discovery is proven.
- [ ] Upgrade is separated from install/read and has a tested restore boundary.
- [ ] Only required handler paths are inspected or patched.
- [ ] Windows audit is limited to the selected execution path.
- [ ] The write-autonomy decision remains explicit rather than inferred.
- [ ] No optional framework is invoked automatically.
- [ ] `git diff --check` and repository-prescribed scoped gates pass for any repository documentation change.
