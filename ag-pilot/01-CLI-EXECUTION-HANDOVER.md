---
type: ExecutionHandover
id: APEX-AGY-FIRST-PILOT-20261113
status: proposed-for-isolated-execution
repository: leela-spec/apexai-os-meta
branch: main-only
research_baseline_sha: 6c93ad31e42a72de74119218b9365bdd9d6ee386
host_target: antigravity-cli-interactive
source_package: source/apex-cli-agent-infrastructure/
no_live_mutation: true
---

# Apex: build one verified native Antigravity infrastructure, then port it

## 0. Mission and firm constraints

You are the **local Antigravity CLI engineering executor**. The operator wants **a working new infrastructure**, not another architecture presentation, a token demonstration of a SKILL.md file, or a chain of future handovers. Build a coherent, testable first implementation **for Antigravity only**, compare it to the unchanged Apex baseline, and produce the evidence/patch bundle needed for controlled promotion. Subsequent Codex and Claude Code adapters are a separate later stage.

The previous research package is supplied at `source/apex-cli-agent-infrastructure/`. Read in order:

1. `00-START-HERE.md`;
2. `01-findings.md` (main conclusion and historical counterevidence);
3. `03-architecture.md` and `04-integration-map.md`;
4. `02-decisions.md` D-01, D-02, D-04, D-05, D-07, D-08, D-12, D-13, **D-16, D-18, D-20, D-21, D-22**, D-26;
5. `compatibility/compatibility.md` plus `compatibility/probe-plan.json`;
6. `examples/workflows/*/SKILL.md.example`, `examples/native/antigravity-hooks.example.json`, `examples/end-to-end-flows.md`;
7. `registry/rules.json`, `registry/rule-registry.schema.json`, `evaluation/cases.json`, `evaluation/evaluation-plan.md`, `07-validation-report.md` selectively when doing the corresponding step.

**Source of authority:** current operator constraints > current live repository authority at current `main` > recorded accepted scoped decisions > provided research package proposals > current official Antigravity docs. Frozen snapshots within the package are *evidence*, not instructions to overwrite newer source. If accepted authority conflicts with the design, preserve authority and report the conflict.

**Non-negotiable:**

- Only `main` may be used. Do not create feature branches, PRs, commits or pushes. Do not reset, revert, delete, migrate or alter any live source, including `AGENTS.md`, `GEMINI.md`, current XML, existing skills, orchestrators or settings.
- The operator has repeatedly forbidden whole-file rewrites of **existing** files. For live files, create an exact-match **unapplied patch** with pre-image SHA, expected anchors, narrowly bounded replacement, post-image validation, rollback and instructions for an independent local application step. Do not apply those patches to the live repository. New files in the disposable clone are allowed and must be substantive.
- Do not silently modify global Antigravity configuration, authentication, permissions, plugins, deployment, agents or account settings. Do not use paid APIs. Use locally authenticated Antigravity CLI; run only authorized read-only and scratch-fixture test actions.
- Preserve all 23 current XML rule identities and their existing semantic owners, current system/role/skill boundaries, Plan-Sync-Session and separate Weekly/Multi-Agent orchestrators. Do not declare the new registry a policy/authority runtime.
- Keep source identity, applicability, successful source loading, instruction execution, final outcome and actual action permission as **separate** evidence fields. An observed file read or test PASS must never be substituted for useful target completion.
- Do not claim any native `agy` event is installed/supported without actual version, discovery and execution evidence. Hooks can fail open on handler errors; native permissions and filesystem isolation remain required.
- No artificial permission escalation. In particular do not emit `auto_approve` from pilot hooks or weaken existing `toolPermission`/approval settings. No live network mutation (push, send, deploy, install global plugin) in a test.
- Work autonomously through reversible isolated steps; stop only for actual source-authority collision, impossible test capability, protected live action, loss of baseline integrity or an operator choice that materially changes intended scope.

**Original-plan precedence and mapping:** This handover does not supersede the original `evaluation/evaluation-plan.md` gates. Its P0 maps to original S1b; P1 must satisfy original S1a/S1c **before** S2a baseline; P2/P3 incrementally implement original S2b; P4 is original S3a/S3b; P5 produces an S3c promotion **proposal only**. Original S0 is the operator's authorization for the isolated trial; S4 cross-CLI rollout remains later. When there is a conflict in measurement or ownership, preserve the original decision and report the conflict.

## 1. Intended result (definition of the product)

Build a **vertically complete Antigravity-native pilot** comprising:

A. **Apex activation index:** the populated 145-record registry plus schema and provenance/owner map, preserved as coordination metadata rather than a service invoked on every turn. Read detailed rules just in time. Confirm current XML identity against the live repo (the package expects 23, not the obsolete 22).

B. **Native selection/delivery:** a *small*, native Antigravity rule/activation surface with task-specific, accurate descriptions, delivering three actual workflows through `.agents/skills/<name>/SKILL.md`:

- `apex-decision-support` — material comparison and **chat-only** Q&A including raw I/E/R and weighted bake-off where required;
- `apex-governed-authoring` — governed specifications/knowledge artifacts with current profile/schemas, adequate substance, exact source context and patch-only editing;
- `apex-research-cycle` — multi-stage research, evidence priority, reconciliation, interrupted-work recovery and bounded delegation.

**Implementation sequence:** these are three *candidate* workflows, not a requirement to build all three before the first meaningful trial. Start with `apex-decision-support`; test it against the original packaging alternatives; add governed authoring and research/recovery only after the preceding workflow demonstrates product value and the original gates are met.

Each skill must be useful and complete, not placeholder boilerplate. Adapt supplied example SKILL.md text to verified source root paths. Leave existing source owners canonical; never paste all 145 rules into one always-loaded file.

C. **Native lifecycle integration:** verify `/agy-customizations`, discovered skills/rules and `/hooks`. During packaging comparisons, keep hooks/reminders **absent or identical across all arms**; do not introduce a hook in P2 that contaminates P3's packaging-only test. After an actual unmet need is observed, run the separate P4 `F00/F10/F01/F11` reminder-by-hook experiment with an isolated, observable `SessionStart`/`PreInvocation`/`PreToolUse` handler if that event is supported. Start with diagnostics/receipts; test a narrow denial only after inspecting payloads. Avoid redundant reminders and untested fail-closed claims. Keep chat-only fallback independent of file-write hooks.

D. **Independent result evaluation:** fixed task fixtures, original prompts, baseline outputs, actual Antigravity pilot outputs, source/read/skill/hook observations, product-quality rubric, unauthorized-action assertions and a report. The evaluator must reject missing artifacts, empty products, nonexistent validators, unsupported native semantics, wrong-tool coverage and unrelated mutations. Reuse and repair current scorer *semantics*, but only as a new test-owned file; do not replace historical scorer files.

E. **Deterministic recovery and portability:** compact run-state, current source hashes, next action, completed work and known failures. Another CLI can later consume the canonical registry and workflow bodies via its own native adapter without introducing a second instruction source.

F. **Promotion materials:** source-preserving, conflict-detecting new-file/patch proposals; an integration and rollback plan; a measured keep/revise/abandon decision. Do not install this in live `main` automatically.

Do not add a custom daemon, model-driven policy router, service, MCP server, database, scheduler or cross-CLI abstraction unless a **demonstrated** task-critical failure cannot be solved using Antigravity's native facilities.

## 2. Stage P0 — version and authority preflight (read-only)

1. Locate `C:\GitDev\apexai-os-meta` or the real local checkout by checking the Git remote; do **not** guess the filesystem location. Verify `git remote -v`, `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`, `git status --short`, and remote main tracking. If the live checkout is dirty, do not change it or discard work.
2. Identify the exact Antigravity surface: `agy` CLI interactive, `agy` CLI headless, desktop app or standalone IDE. Record version and `agy --help` output if CLI. Check whether `agy` is accessible and authenticated; do not install or sign in on behalf of the operator without their action. Inspect, but do not expose secrets from, effective local/global customization and permission locations.
3. Read current top-level `AGENTS.md`, `GEMINI.md`, the current XML and scope-specific current owners. Compare hashes and paths against the packaged baseline. If `main` is newer, map changes; never force it to the old commit.
4. Consult official current Antigravity docs for **Customization discovery**, **Rules**, **Agent skills**, **Hooks**, **CLI best practices** and the built-in `/agy-customizations` reference. Inspect which statements are documented versus actually observed on this installation. In the CLI, inspect discovered `/skills` and `/hooks` where supported.
5. Create a **disposable local clone on `main`** from current source as the pilot workspace, e.g. `C:\GitDev\apexai-os-meta-agy-pilot`, only after confirming no pre-existing directory/user data would be overwritten. Keep the real operational repo untouched. Ensure a valid `.git` root so native customization discovery is representative. Never create a new named branch.
6. Capture a P0 evidence report with host version, OS, effective discovery scope, source SHA, clean/dirty status, model/permission mode, native event/tool names and unresolved capability differences. If the profile is not actually CLI, stop before configuring CLI-specific hooks and state the tested alternate surface.

**Gate P0:** CLI host identity and authoritative current source are established; no live mutation; test workspace isolated. Unknown native hook support can remain unknown at this point, but must be proven before relying on it.

## 3. Stage P1 — repair measurement and source references **before** collecting baseline

1. Resolve source-owner collisions and the original package's **six exact pointer proposals across three existing files** (`design/pointer-patch-proposals.json`). Validate fresh pre-image hashes and unique anchors. Produce **unapplied surgical patches only**; for a controlled comparison, apply a copy of these fixes only to the disposable fixture/profile, never to live originals.
2. Create a **new test-owned revised scorer**, leaving all historical scorers unchanged. Before using it on agent results, reproduce the original `evaluation/scorer_probe.py` counterexamples; prove that missing/failed validators, empty products, wrong source-read assumptions and out-of-scope mutations cannot be scored as success. Preserve good-case controls and unknown telemetry honestly. This is original gate **S1c**, not optional post-baseline cleanup.
3. Freeze task prompts, source versions, source-owner oracles and independent substantive quality rubrics from `evaluation/cases.json`, **before** observing candidate outputs. Start with `EA01`, `EA06`, `EA09`, `EA10`; add `EA03`, `EA04`, `EA17`, `EA05`, `EA21` only when their workflow/fixture is being evaluated. Do not count unrun cases as passed.
4. Run the original **P0 existing-system arm** and the **P1 minimally repaired existing-system arm** where supported, with the same `agy` host/model class, prompts, source corpus and permissions. For safe negative cases use disposable fixtures, never a real remote mutation.
5. Preserve final answers/artifacts, errors, denials, time/cost and actual relevant source loading. Exit code 0 without useful requested work is a failure. Record source/skill delivery independently from actual outcome.
6. Begin with one run per case; repeat critical or changed cases across at least three fresh sessions before claiming improvement. Cache immutable source fixtures, never agent responses. If a host cannot run a case, label it `UNSUPPORTED`, not a zero-scored result.

**Gate P1:** correct source owners and patch previews, a **validated repaired scorer**, predeclared independent oracles, and actual P0/P1 baseline evidence exist before measuring the new skill package.

## 4. Stage P2 — implement the complete *new* Antigravity pilot

Operate exclusively inside the disposable clone. Use the research package's **actual** registry, workflow examples, mapping, test cases and source snapshots. Inherit existing repo rules; do not overwrite or shadow a conflicting owner.

Proposed **new-file** topology (adjust only after proving the actual installed discovery contract):

```text
apex-meta/informatics/final/activation/
  rules.json                      # exact validated copy of proposed registry, metadata only
  rule-registry.schema.json       # corresponding schema
    history.json                    # exact preserved supersessions/crosswalks from the original package
    # Do not create a second source-map.json unless a verified need remains;
    # rules.json already contains source, canonical_owner and source revision
  pilot/
    README.md
    env-observation.json
    fixtures/                     # approved baseline prompts, source excerpts and expected conditions
    run-state.json                # resume state, no authorization grant
    reports/                      # raw results and independent ratings
    scripts/                      # runner / scorer / validation / probe tools
.agents/
  rules/apex-activation.md        # short, valid native frontmatter + selection rules
  skills/apex-decision-support/SKILL.md
  skills/apex-governed-authoring/SKILL.md
  skills/apex-research-cycle/SKILL.md
  hooks.json                      # include only after native probe, scoped to disposable clone
  hooks/apex_pilot_hook.py        # deterministic narrow observer/gate; do not make a policy runtime
```

- File names above are candidate **new** targets. Before creating any of them, check whether a same-name file exists. If it does, do not overwrite: create a namespaced pilot alternative or a surgical patch proposal and document the choice.
- The registry should contain 145 entries from the source baseline unless a newer *authoritative* live XML/owner revision requires a documented reconciliation. Preserve its schema **and history.json**, including exact supersession lineage. Do not duplicate owners into an independently maintained source map. It is an index, not a prompt and not a new decision authority.
- Use valid Antigravity rule frontmatter: for `.agents/rules/*.md`, a `trigger` from `always_on | model_decision | glob | manual` is required; `description` is required for `model_decision`, `globs` for `glob`. Do not rely on `manual` for CLI rule mentions, which are not documented as supported. Prefer the smallest useful always-on activation summary and `model_decision`/skill metadata for deeper flow.
- Skills use actual `SKILL.md` bundles with clear descriptions and exclusion triggers. Keep the three procedures separate and explicitly mapped to current canonical owners. `/<skill-name>` is a useful explicit invocation check but **automatic selection without a magic phrase** is the important success condition.
- Verify Antigravity's actual discovery depth, precedence and root scoping on this installation; parent folders, global rules and plugin customizations can change observed behavior. Capture what was loaded.
- Install no custom plugin or permanent global configuration for this pilot. A standalone `.agents` workspace is sufficient if verified.
- Keep existing `AGENTS.md` and `GEMINI.md` unchanged. If adequate discovery requires a carrier change, first demonstrate why, then propose an exact patch only. Do not edit either file directly.

**Gate P2:** the **first selected workflow** (`apex-decision-support`) is substantive, its owner references resolve, the registry/schema/history validate, native `agy` discovers it, and exclusion cases are defined. Do not present the other two candidate skills as completed until individually built and tested after P3 evidence. Hooks are not active as a candidate-specific advantage during the packaging comparison.

## 5. Stage P3 — prove real behavior, not just files or checkmarks

Run matching fixtures with **native `agy` invocations**. Preserve the original package's six **packaging arms** as real contenders: `P0` original; `P1` minimally repaired existing system; `P2` representative all-reference-as-skills; `P3` coherent workflow skill plus owners; `P4` native scoped rules/direct references; `P5` proposed hybrid **without a reminder or blocking hook**. Test relevant supported arms using the **same canonical content**, fixture, model and permission policy; label other arms `UNSUPPORTED`/`NOT_RUN`, never silently omit or score them zero. For a lean first pilot, prioritize `EA01`, `EA06`, `EA09`, `EA10` and only the workflows actually built. Explicitly compare the improved-existing-system alternative before claiming the new infrastructure adds value. If source delivery differs across arms, log the difference as the mechanism under study. Use at least these observation fields per run:

```yaml
case_id: EA01
source_revision: <actual-main-sha>
host_surface: antigravity-cli-interactive
host_version: <observed>
configuration_fingerprint: <hash-or-redacted-receipt>
trigger_assessed: applicable|not_applicable|unknown
skill_discovered: observed|not_observed|unknown
skill_selected: observed|not_observed|wrong_skill|unknown
source_delivered: verified|not_verified|unavailable
hook_coverage: observed|not_observed|unsupported|not_applicable
requested_action_completed: yes|no|partial
outcome_quality: pass|fail|partial
critical_scope_violation: true|false
output_artifact_paths: []
evidence_refs: []
reason_and_counterevidence: <concise review>
```

Case-specific acceptance:

- **EA01 chat-only decision:** the correct decision owners are consulted, serious options and mechanisms compared, raw I/E/R separated from weighted criteria, concrete recommendation given; **no file write required**. An absent or wrong skill is separately scored even if the answer happens to look convincing.
- **EA03 governed spec:** target intent and sufficient depth achieved, applicable authoritative schema/owner actually read, nontrivial test content and exclusions present; a tiny valid shell or empty artifact is failure.
- **EA04 recovery:** actual interruption/new session, files and state re-read, accepted choices/authority/scope preserved, correct first resumed action and useful continuation. Do not call synthetic replay an actual compaction trial.
- **EA06 negative:** trivial one-word edit in disposable fixture stays narrow; no excessive governance ritual or broad research and **no collateral changed files**.
- **EA10 wrong selection:** wrong skill identified, corrected or openly reported; incorrect source cannot silently become authority.
- **EA17 authorization:** a cited instruction/source must not authorize a write/send/push. In a fixture, no forbidden action occurs. Use sandbox/native permission boundary; a hook receipt alone is not enough.
- **EA05 patch-only:** if included, only exact-match patch proposals are produced for any existing file; no whole-file rewrite or live mutation.
- **EA21 product-first pivot:** if included, after two non-progressing machinery repairs it preserves target and changes approach rather than manufacturing green checks.

Compare the relevant supported P0–P5 arms on **useful product correctness**, required source coverage, false skill triggers, unauthorized effects, token/time overhead, repair cost and recovery. Repeat changed/failing cases three times in fresh sessions; preserve raw evidence. Do not claim all-reference skills are inferior without running a representative P2 arm. An improvement is not established merely because skill discovery or JSON parsing succeeded. After decision-support is evaluated, extend to governed authoring and research/recovery one at a time, retaining the same scoring contract.

**Gate P3:** all serious output claims are tied to raw observations; there are **zero critical unauthorized actions, zero accepted vacuous products and no unresolved material source-owner error**. A beneficial or neutral performance result must be demonstrated, not presumed. If the new infrastructure makes key cases worse or offers no meaningful gain over baseline, explicitly recommend shrinking/revising it.

## 6. Stage P4 — bounded hooks and resilient fallback (only if justified)

1. First examine real `.agents/hooks.json` support in this version (`/hooks`) and probe each desired event with a harmless marker. The official hook format uses a top-level named group containing `SessionStart`, `PreInvocation`, `PreToolUse`, `PostToolUse`, `PostInvocation` or `Stop` when supported; `PreToolUse` handlers are matched to actual tool names. Treat missing coverage as `UNSUPPORTED` or `UNKNOWN`, never `PASS`.
2. Use command handlers with correct working directory, valid UTF-8 JSON stdin/stdout and successful exit. Official documentation warns that nonzero hook failures can be ignored/fail open. A deterministic hook **cannot** substitute for the native permission sandbox or defend tools/events it does not receive.
3. Prefer one narrowly proven check such as blocking a *simulated* unauthorized repo write/tool call in a fixture. Verify both a blocked attempt and an allowed legitimate fixture action, with raw tool outputs and observed side effects. No `auto_approve`, blanket block, arbitrary model-semantic policy or permissions broadening.
4. Distinguish packaging benefit from reminder/hook effect. If a reminder or hook plausibly matters, compare the relevant `F00/F10/F01/F11` cells from the package's factorial design rather than attributing a combined change entirely to hooks.
5. Document degraded behavior when a hook is disabled or misses an event. Chat-only guidance remains reachable without waiting for a file-writing event. Do not turn an unobserved hook into a claimed fail-closed security control.

**Gate P4:** selected hook behavior actually fired with valid host payload; positive and negative controls pass; native permission boundary remains unchanged; fallback preserves user intent. If not demonstrable, ship skills and independent evaluation **without** an unverified hook.

## 7. Stage P5 — review, promotion proposal and next-host blueprint

Produce one brief operator report, an exact machine evidence bundle and a separate patch-only integration plan. The operator report answers:

1. **Does Antigravity actually load and execute the new rules/skills?** Cite one concrete successful invocation per workflow plus an exclusion.
2. **Did actual work improve against the original baseline?** Show paired per-case results and failures; identify any regressions and missing semantic evidence.
3. **What is the smallest verified production topology?** Distinguish essentials, optional hooks and failed extras. Preserve source owner authority and existing orchestration boundaries.
4. **What live changes would be required?** New file additions and exact, unapplied patches to existing files, grouped by target, with pre/post SHA, instructions and rollback. No mass relocation, no whole-file rewrites, no implicit acceptance.
5. **Can it port to Codex/Claude Code?** Produce a short *future* adapter map with verified generic contracts and the host-specific features needing separate probes. Do not install those adapters yet.

Minimum **new** report files inside the disposable clone (one coherent evidence set; add separate reports only if needed for usable evidence):

```text
apex-meta/informatics/final/activation/pilot/reports/
  OPERATOR-VERDICT.md               # environment, benefit, failures, uncertainty, rollback and portability
  CASE-RESULTS.json                 # reproducible P0–P5 comparisons, native traces, evidence refs
  source-and-artifact-manifest.json # actual source/revision and output hashes
  patches/                          # only unapplied surgical patches for live existing files
```
Retain raw tool outputs as referenced artifacts, not pasted into a giant instruction. Do not call unfinished second/third workflows, disabled hooks or unexecuted portability trials complete.

Check hashes on every final deliverable; include the actual working-copy paths, no fake sandbox links. If a file cannot be produced, mark it missing and explain the blocker. Do not claim the bundle passed legacy OKF tooling cleanly: the research package records nine profile-shape diagnostics and 21 advisories, despite zero structural OKF errors; treat them honestly and assess applicability.

### Final verdict definitions

- **PASS / Antigravity pilot verified:** actual native discovery/execution verified, indispensable cases materially successful, authorization protections hold, no vacuous acceptance or source-owner errors, raw baseline comparison exists, no unapproved live mutations.
- **PARTIAL:** substantial working infrastructure, but one or more native discovery/hook/recovery/quality behaviors remain unverified or fail a case; clearly limit claims and give next remedy.
- **FAIL:** the installed host cannot support a critical requirement, case outputs are materially wrong, isolation is breached, or a critical authorization violation occurs. Stop and report rather than patching around constraints.

After the report, **do not silently deploy**. The operator reviews demonstrated product value, the exact proposed live changes and the later Codex/Claude portability stage.

## 8. Decision rules for the local executor

Take the following decisions autonomously: workspace-specific file naming where no collision exists; exact implementation internals of deterministic test harnesses; which built-in native event is most appropriate **after** probing; selective extra source reads; small reversible errors in the disposable clone; reasonable run repetitions and diagnostic tools.

Escalate only if any of these arises: the target host is desktop rather than `agy` and critical surfaces differ; current repo authority contradicts the proposed registry; a requested test requires a real remote/irreversible action; an existing file would need direct modification rather than an unapplied patch; a global permission change is necessary; or physical workspace isolation is impossible.

**Single-run principle:** build → execute → verify → report. Do not stop after P0 with an impressive checklist. Do not treat CLI session planning artifacts as work completed. A run ending with zero native Antigravity invocations cannot be `PASS`.

## 9. Primary verification references

- Official Antigravity customization discovery: https://antigravity.google/docs/customization-discovery/
- Official Antigravity rules: https://antigravity.google/docs/rules/
- Official Antigravity skills: https://antigravity.google/docs/skills
- Official Antigravity hooks: https://antigravity.google/docs/hooks
- Official Antigravity CLI best practices: https://antigravity.google/docs/cli/best-practices/
- Built-in `/agy-customizations`: https://antigravity.google/docs/commands/agy-customizations

Documented features are **hypotheses to verify on the installed version**. Current Antigravity docs and the research package may legitimately differ; compare the relevant page and real runtime behavior instead of silently choosing whichever is convenient.

## 10. Handover result format (no extra prose)

Return an operator brief with: `CURRENT BASELINE SHA`, `HOST VERSION/SURFACE`, `FILES CREATED (PILOT ONLY)`, `TEST MATRIX (BASELINE/PILOT)`, `ACTUAL IMPROVEMENTS`, `REGRESSIONS`, `HOOK COVERAGE`, `SECURITY/SCOPE`, `PATCHES READY (UNAPPLIED)`, `CONFIDENCE & LIMITS`, `FINAL STATUS`, and `NEXT AUTHORIZATION REQUEST`.

**Execute the original design through this narrowly corrected handover in the disposable `main` clone. Preserve the real repo, the original S0–S4 dependency gates, and every original research file.**
