---
okf_version: "0.2"
type: Reference
id: APEX-INFRA-FINDINGS-20261112
title: Apex CLI-Agent Infrastructure Findings
description: Reconciliation of current Apex ownership, retained decisions, observed failures, and current primary platform research.
status: draft
adoption_status: proposed_for_operator_review
research_date: 2026-11-12
source_revision: 6c93ad31e42a72de74119218b9365bdd9d6ee386
tags: [apex, instructions, activation, architecture, evidence]
---

# Findings that determine the proposed product

## 1. Design conclusion and evidence boundary

**Improve the existing Apex system with a declarative activation registry, a few coherent workflow skills, and small native adapters. Keep the current rule owners and orchestration boundaries.** The registry records how a rule reaches execution and verification; it does not become another authority over the XML, a mandatory runtime service, or a replacement for task understanding.

The immediate product problem is a broken chain between intended behavior and delivered outcomes. A rule can exist in a canonical file, appear in a carrier, match a task, and still be skipped. A hook can run and still fail to cover the relevant action. A validator can pass an empty or insufficient result. The proposal therefore distinguishes applicability, discovery, activation, successful source delivery, execution, independent checking, useful outcome, and maintenance.

This selection is a **design inference**, supported by existing Apex failures and current platform capabilities. It is not a claim that a cross-CLI hybrid has won a live controlled benchmark. The package includes actual deterministic artifact checks and isolated scorer counterexamples; agent trials and workstation deployment remain unexecuted. See [the empirical appraisal](evidence/empirical-findings.md), [capability specification](compatibility/compatibility.md), and [evaluation plan](evaluation/evaluation-plan.md).

The read-only design mandate is the governing authorization for this run. It permits new files in this package; it does not authorize repository writes, branch changes, installation, CI changes, a provider subscription, a different-family review service, or any accepted-state promotion. Historical instructions to wait, commit, push, migrate, or install are evidence to reconcile, not instructions to execute now.

### Evidence vocabulary

| Label | Meaning in this package | What it cannot establish |
|---|---|---|
| `operator_requirement` | Explicit current assignment or retained scoped operator decision | Installed implementation |
| `repository_observed` | Content retrieved through authenticated GitHub at the pinned revision | Effective local configuration or a file's actual loading |
| `documented_capability` | Current primary product documentation or versioned schema | Account availability or installed behavior |
| `source_reported_execution` | Retained report describes a run | Independent reproduction without the original traces |
| `executed_synthetic_probe` | A deterministic experiment ran here on supplied data/code | Agent adherence or production behavior |
| `simulation` | Behavior or outcomes are assigned/modelled | Measured improvement |
| `inference` | A reasoned consequence of evidence | An accepted operator decision |
| `proposal` | Reviewable new design, configuration, case, or change | Authorization to adopt or install |
| `accepted_scoped` | Recorded approval in its original domain | General permission outside that scope |

### Source revision and coverage

Authenticated `main` resolved to **`6c93ad31e42a72de74119218b9365bdd9d6ee386`**. The supplied top-50 guide was generated against `2bdf9887a020c03732f619d9a5bf7b8a22e4f48c`. File hashes and line anchors are refreshed from the retrieved revision, not copied as if the two revisions were identical. Source snapshots and a retrieval manifest allow the reviewer to inspect the actual evidence without reassembling it.

The reading route began with all seven named sources and expanded to current XML owners, source decisions, native carriers, relevant existing skills, orchestration contracts, distribution tools, benchmark code, and current vendor documentation. Unrelated business documents and hardware benchmark attachments are outside the design question. No conclusion here depends on local QMD availability. The full source register identifies the reviewed scope, failed exact-path fetches, source hashes, and the historical guide comparison.

## 2. Reconstructed current instruction lifecycle

### What already exists

| Stage | Current owning surface | Observed behavior or requirement | Design consequence |
|---|---|---|---|
| Author universal rules | `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml` | 23 top-level tags; reduced operative rules plus conditional references | Preserve tag identity and meaning; do not substitute the historical 22-rule list |
| Own detailed semantics | `apex-meta/informatics/final/specs/` and `apex-meta/informatics/final/specs/execution-modes/` | Writing, file architecture, governance, task alignment, Q&A, patching, iteration and handover have owners | Registry points to these owners; frozen excerpts support review without creating a second normative owner |
| Distribute core | `operations/18-APEX-CARRIER-MAP.md`; `tools/apex_carrier_sync.py` | Tracked tooling compares and can replace delimited carrier blocks and shared Layer 2 sections | Reuse comparison logic; propose portable target resolution and previewed exact edits, not a second distribution framework |
| Discover procedures | Existing `.claude/skills/` and `.agents/skills/` | Procedures already include QMD, AIRouting, Weekly, Plan, Sync and Session | Retain functioning locations; curate only missing repeatable workflows |
| Activate task details | XML `when/ref`; project routing; skill descriptions | Intent and pointers are semantic instructions, not proof that reads occur | Add explicit applicability evidence and task-specific recovery; test missed routes |
| Enforce narrow checks | Existing gates, benchmark hooks, native permissions | Different mechanisms and repositories own different boundaries | Reuse only the parts whose scope and behavior are actually established |
| Verify output | Current target rule, validators, evaluation reports, Detective workflow | Outcome fidelity outranks a self-authored checklist | Require artifact substance and source fidelity in addition to syntax |
| Preserve state | Iterative execution, handoff packets, project/run files | Durable state is file-backed; role definitions do not hold authoritative memory | Recover from a bounded current-state record and source/version references |
| Maintain truth | Current-truth rules, source owners, historical ledgers | Active truth is distinct from evidence and superseded proposals | Keep current registry and historical crosswalk separate |

Repository basis: `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml`, tags `target`, `context`, `current_truth`, `iterative`, `pointers`; `apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md`, §§1–6; `apex-meta/orchestration/ARCHITECTURE.md`, §§1–7. Exact snapshots are indexed in [repository sources](evidence/repository-sources.json).

### Representation is not activation

The retained instruction-access matrix already separates formatting from loading. Changing XML to Markdown does not make a host discover it; naming a reference `SKILL.md` does not prove correct selection; defining an agent does not grant its tools or authority. These are separate mechanisms with different failure modes.

| Mechanism | Appropriate job | Boundary |
|---|---|---|
| Always-on core | Universal target, scope, authority and concise routing obligations | Costs context in every relevant session; cannot contain all downstream procedure detail economically |
| Scoped native instruction | File/subsystem constraints activated by the host's actual scope semantics | Path discovery differs across hosts and may not cover chat-only work |
| Reference/schema | Stable definition or machine contract used by a selected procedure | Needs a dependable access path; it is not independently discoverable merely because it exists |
| Workflow skill | A repeatable task with recognizable intent, inputs, ordered work and useful output | Metadata selection can fail; supporting references still need delivery |
| Agent definition | Repeated role, separate context, task constraints and supported tool settings | Name, prompt and isolation are not an independent permission sandbox |
| Context injection | Deliver a small selected instruction/state slice at a supported lifecycle event | Event-specific; an event with a similar name may be diagnostic-only |
| Hook | Observe, advise, or block a known covered event | Disabled/trust failures, unsupported tools, errors and bypass paths matter |
| MCP/tool connectivity | Expose tools/resources through a protocol | Does not own task doctrine, skill routing, approval or final correctness |
| Validator | Deterministically check a well-defined property | Cannot certify meaning it does not measure |
| Outcome evaluation | Decide whether the actual result meets the authorized goal | Must use original requirements and evidence, not the creator's preferred proxies |

Repository basis: `apex-meta/informatics/final/research/01-universal-instruction-research/05-INSTRUCTION-ACCESS-AND-SERIALIZATION-MATRIX.md`, representation/loading matrix; `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/claude-mechanism-decision-model.md`, §§Core Summary and Uncertainty. External support is in [the source/claim registers](evidence/external-sources.json).

### Preserve the two orchestration systems

The live project router and manifest distinguish **Weekly Orchestrator**, **Multi-Agent Orchestration**, and the **Plan-Sync-Session Backbone**. The backbone is a shared capability, not a third orchestration system. Weekly consumes confirmed Session feeds and Sync reports. It does not implicitly add Plan as a weekly stage or activate Multi-Agent Orchestration.

Within an explicitly activated Multi-Agent run, Alfred and Meta Ops remain main-conversation accountabilities. Strategy, Detective and specialist lanes receive bounded packets. State remains in files. Role names grant no authority; candidate/verified status, lifecycle stage and operator confirmation remain distinct. Existing authority-digest enforcement is recorded as an open code item, not a completed protection.

Repository basis: `.claude/CLAUDE.md`, §§Orchestration systems, Plan-Sync-Session Backbone, Global boundaries; `apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml`; `apex-meta/orchestration/ARCHITECTURE.md:16–24,40–66,84–89`; `apex-meta/orchestration/schemas/authority-state.schema.md:73–92`.

**Consequence:** native subagents used for this research are temporary work decomposition. Their availability does not start the repository's named Multi-Agent Orchestration system. The proposed infrastructure supplies shared delivery/checking capabilities without absorbing either system or replacing Session's confirmed-mutation path.

## 3. Material conflicts and source corrections

| ID | Source tension | Resolution used in the package | Consequence after review |
|---|---|---|---|
| CF-01 | XML `align` says wait; current assignment authorizes one continuous run | The current operator request supplies this run's scope and authorization | Keep general alignment meaning; record authorized-step and trivial-task exclusions |
| CF-02 | Compressed XML `handover` says push; detailed EM-14 limits persistence to applicable deliveries | The current read-only assignment forbids repository persistence | No push; proposed implementation must condition close-out on authorized destination |
| CF-03 | XML `sync` says commit unrelated dirty files separately; root `AGENTS.md` Git Dispatch says ignore them | Preserve both texts; use explicitly scoped operator intent and root dispatch for any later requested-file operation | Propose a narrow owner-level reconciliation; no automatic unrelated commits |
| CF-04 | Historic catalog has 22 rules; live XML has 23 | `align` is the additional rule; historical numbering remains stable | Include explicit historical-to-current crosswalk |
| CF-05 | Candidate register retains old `PROPOSED/OPEN` rows beside later finalized/operating state | Literal historical status is not the current adoption verdict | Preserve origin, later owner and evidence separately |
| CF-06 | Root governance link points to missing `apex-meta/informatics/standard.md` | Navigation index resolves `apex-meta/informatics/final/specs/standard.md` | Supply exact-match pointer patch proposal, not a content rewrite |
| CF-07 | Patch-discipline relative links resolve too shallowly; the governance-schemas link to the actual patch schema is correct | Use the actual authenticated owning schema and record written versus resolved locator | Correct links only after approval; never invent a replacement schema |
| CF-08 | Bake-off includes a weighted matrix; WP-07/GS-04 prohibit aggregating I/E/R; old synthesis computes NVS | Preserve raw I/E/R. The owned weighted criterion rubric remains required when EM-07 applies; its scores are different quantities from I/E/R | Do not use NVS as empirical reliability or rank the registry by an invented composite |
| CF-09 | QA EM-06a can treat silence as acceptance in its conversational default | The present review-before-deployment boundary requires explicit approval | Silence cannot promote this package or authorize installation |
| CF-10 | Retained cross-CLI texts contain old no-hook or universal-loader claims | Current official docs and versioned schemas are used for capabilities | Propose capability revisions, not semantic rule reversals |
| CF-11 | `.claude/settings.json` contains top-level `defaultMode: bypassPermissions` | Current documented key is nested; repository text alone proves no effective permission mode | Flag schema/effective-policy probe; no permission expansion or automatic repair |
| CF-12 | Shared Windows Layer 2, WSL architecture banner, and Hermes WSL direction have different scope/status | Record execution surface and accepted scope; do not infer completed workstation migration | Portable roots in design; no machine-path migration in this run |
| CF-13 | QMD owner permits hybrid search after zero keyword hits; skill body also allows purely conceptual prompts | Preserve stricter owner for current Windows profile and expose the discrepancy | Small skill-to-owner alignment proposal; QMD absence online has targeted GitHub fallback |
| CF-14 | Predecessor architecture calls hooks/MCP deliberately unbuilt in Multi-Agent Orchestration | Shared infrastructure proposal does not silently modify that system's mechanism ladder | Any use inside that system requires a specific accepted integration change |

Sources: `AGENTS.md` §§Git Dispatch and Informatics & Knowledge Routing; `final/specs/execution-modes/{handover,qa-decision-matrix,bake-off}.md`; `final/specs/{writing-profile,governance-schemas,carrier-layer2-shared}.md`; `final/operations/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md` §2; `.agents/skills/qmd/SKILL.md` §§1–3; `.claude/settings.json`; `apex-meta/orchestration/ARCHITECTURE.md` §§2,6. In this paragraph, `final/` expands to `apex-meta/informatics/final/`; the machine registry stores full root-relative paths. The [registry coverage record](registry/coverage.md) records exact source windows and owner-resolution defects.

## 4. Retained decisions, preserved within scope

### Informatics and carriers

The candidate register's DEC-01–09 retain single ownership, durable IDs, scoped deduplication, stronger replacement tests, and restraint about tiny abstractions. DEC-10/11 are superseded positions, not constraints to revive. DEC-12–16 explain why universal reduced rules and separate conditional references were chosen, but their behavioral premise was explicitly falsifiable. The routing pilot challenges reliable pointer honoring; it does not show that separating mutually exclusive modules has no value.

DEC-17 records the operator's preference for named tags. The proposal preserves it. DEC-21 records equal intended behavior across tools through controlled carriers. The proposal preserves that intent while revising the assumption that one physical loading pattern can work identically everywhere. DEC-22–24 and the current XML preserve portable core/workstation separation and priority semantics. Historic token estimates remain estimates of their original texts, not measurements of this package.

Repository basis: `apex-meta/informatics/final/candidates/01-decision-register.md`, Parts A–H, especially §§DEC-16, DEC-17, DEC-21; `apex-meta/informatics/final/operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md`, Executive verdict and limitations; `apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md`, source and comparison contract.

The older Topic 3 synthesis recommended selective gates over universal inlining or pure dynamic routing, with authored raw scores. It also used unsupported language about guarantees and an NVS aggregate elsewhere. This package preserves the original numbers in evidence/history, but assigns no measured reliability to them. The new decisions use explicitly labeled design estimates and rejection reasons. Detailed alternatives remain reviewable; the earlier recommendation is not used as a foregone conclusion.

### Agent roles, shared skills and local execution

| Decision family | Preserved meaning | Not inferred |
|---|---|---|
| Q001–Q008, Claude precursor KB | Strict skill-package policy, hard enforcement focused on high-risk gates, project skills before plugins, small validated durable roles, deferred MCP policy, one prompt pack per flow | Those compile-policy choices prove a deployed orchestration runtime |
| Hermes D01/D02 | Apex is control plane; source repositories own project truth; separate boards/read-only rollup | Mirror every project into the new registry or activate a scheduler |
| Hermes D03/D04 | Scoped reusable roles; sequential reuse of writable profiles; reviewed procedure promotion | Raw memory sync or concurrent use of the same writable profile |
| Hermes D05/D06 | Shared skill source is accepted direction with a pilot; domain libraries stay local | Copy every skill to every CLI or lock a new deployment root before the pilot |
| Hermes D07/D08 | WSL convergence and curated retrieval are scoped accepted directions with incomplete acceptance/migration | Current Windows sources have disappeared or QMD is truth |
| Hermes D09/D10 | External shared memory and background multi-board dispatch remain deferred | A registry requires a new service or daemon |
| Local-engine LM-1–30 | Bounded operator, planner-routed validated profiles, durable recovery, no authority promotion, 7–8B practical-center hypothesis | A production model/runtime choice or hardware performance conclusion |

Repository basis: `apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md:13–17,46–119`; `apex-meta/epics/hermes-multi-repo-orchestration-v2/DECISIONS.md:8–78`; its `decisions/D05-SHARED-SKILL-SOURCE.md`, Promotion gate; `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`, §§2–10,13.

**No accepted domain meaning is reversed.** Proposed changes concern delivery reliability, pointer resolution, observable configuration behavior, evaluator validity, and capability-specific projections. Every material proposal is recorded in [the decision matrix](02-decisions.md) with origin, evidence, trade-off, failure mode, and affected components.

## 5. What retained experiments actually support

The small routing pilot reports missed judgment-gate reads. The expanded Stage-1 report records 72 headless Haiku cells: corrected gate-read totals A 3/21, B 4/21, C 3/21, placement A 6/12, B 4/12, C 12/12, and blueprint reads B 1/24. Its handover reads 9/9 differ from the smaller operations/17 pilot’s 0/2; these are different retained experiments, not interchangeable observations. Trade-off reads 0/9 reinforce the missed conversational-routing problem. The Stage-1 protocol used system-prompt injection, one model/repository, three replicates, and corrected proxies, so it does not establish native loader behavior or general reliability. Source: `apex-meta/informatics/final/research/08-read-trace-routing-experiments/01-findings-and-protocol.md:135–192`; its corrected scorer still has permissive read/validator proxies. The upgrade report later reports **18/33 baseline, 31/33 hooks plus concise reminders, and 17/33 deliberation** on the tested Antigravity setup. These are retained source-reported results, not trials rerun here. The original raw workstation trace directory was unavailable. Their primary value is concrete failure reproduction and candidate-case reuse, with the recorded sample and harness limits.

The combined arm cannot attribute its whole gain to hooks. T1 has evidence of denied premature writes; T6/T7 gains occurred without Stop denials. Reminder-only and hook-only counterfactuals were not supplied. The stress case is not proof of compaction or interruption recovery. Cross-harness contamination and excluded arms remain part of the result, not inconvenient notes to omit.

More seriously, source-code inspection found that `tools/agent_eval_runner.py` assigns outcomes in branches. It is a simulation. The later `score_eval.py` consumes real trace files, but several graders measure insufficient proxies. Four isolated synthetic probes executed here demonstrate that its checks can count a failed Glob as a read, accept a zero-byte output, pass without a working validator, and miss an unrelated mutation in a typo case. Those probes do not prove the historic runs exploited these defects; they establish that reusing the grader unchanged would be unsound.

Repository basis: `apex-meta/informatics/final/tools/agent_eval_runner.py:145–196,299–320`; `apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md:20–51,69–74`; `score_eval.py:228–233,477–497,539–581,613–624` in the same research directory. Reproduction code, exact scorer hash, synthetic conditions and observed results are in [the scorer probes](evaluation/scorer-probe-results.json).

**Consequence:** reuse task fixtures and trace interpretation cautiously. Repair evaluator semantics before using new pass rates for an adoption decision. A missing/failed checker yields unknown or failed evidence, never zero errors. A successful content delivery requires the correct path/version and observed output; search hits and pre-tool attempts do not suffice. A passing shape check remains separate from the semantic outcome. The unchanged retained OKF checker also uses narrow phrase/heading recognition and cannot count options in the package’s Markdown tables; its raw diagnostic reconciliation is preserved in the [validation report](07-validation-report.md). This reinforces the need to inspect the actual field/content coverage instead of treating a parser’s pass or failure as semantic authority.

## 6. Current primary research changes implementation choices

### Platform compatibility is a contract per surface

The [cross-CLI specification](compatibility/compatibility.md) owns detailed findings. The material implications are:

- **Codex:** current local clients document hooks, so the old git-only premise is obsolete. Model-request hooks are diagnostic; they cannot be treated as a per-model context injector. Local function-tool coverage excludes hosted and certain special paths. Custom agent configuration does not create a separate permission sandbox. Work Cloud and local execution have different hook contracts.
- **Claude Code:** native `AGENTS.md` support is version/configuration dependent, and default fallback precedence matters when `CLAUDE.md` exists. Ordinary headless operation and `--bare` differ materially. Project configuration text does not establish effective permission policy.
- **Antigravity:** current shared customization roots, CLI-only roots, App/IDE behavior, rule discovery, workflow migration, and Gemini migration must be distinguished. Neither a legacy Gemini setting nor a similarly named event establishes current App/CLI behavior.
- **Gemini CLI:** retain legacy/historical adapters only for profiles still using that executable. Migration documentation does not prove a profile migrated; old event schemas do not become Antigravity schemas automatically.

Direct primary sources: [OpenAI hooks](https://learn.chatgpt.com/docs/hooks), [OpenAI subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude memory](https://code.claude.com/docs/en/memory), [Claude headless](https://code.claude.com/docs/en/headless), [Antigravity discovery](https://antigravity.google/docs/customization-discovery), [Antigravity rules](https://antigravity.google/docs/rules), [Gemini hook reference](https://geminicli.com/docs/hooks/reference/). The source register supplies reviewed sections, version applicability, caveats and claims.

The design chooses **capability profiles**, not a universal minimum version invented from today's documentation. Every active host must prove discovery, trust, event payload/response behavior, permission boundaries and relevant tool coverage. A documented latest release number is a research anchor, not an instruction to upgrade. A schema can accept a field the runtime does not honor; the supplied Codex schema/reference comparison demonstrates why parseability and execution semantics need separate checks.

### Empirical implications for routing, context and evaluation

Original studies support testing selective context and curated procedures, but do not justify universal skill proliferation. SkillsBench reports both gains and task-level regressions. Realistic skill selection studies separate forced loading from autonomous selection and noisy retrieval. Context-file studies include null/negative findings and higher cost; the retained July paper's full methods limit its equivalence claim and reveal unequal selective-context treatments. Configuration studies find declarations rather than actual exploits and show that two checkers can share a mistaken semantic assumption.

Compaction research motivates preserving execution position and decisions, but learned summarization gains do not transfer automatically to an ordinary CLI checkpoint prompt. Older positional-attention findings motivate adversarial placement tests, not a current numerical failure estimate. Deterministic instruction benchmarks measure operationalized constraints, not all of usefulness.

The [empirical appraisal](evidence/empirical-findings.md) opens the primary methods, versions, denominators, confounds and contrary findings. Its design consequences are concrete: keep the no-framework baseline; compare identical task/content conditions; measure routing separately; include misleading triggers; evaluate the first resumed action; and retain independent semantic checks alongside deterministic integrity checks.

## 7. Serious architecture alternatives

| Alternative | Best argument for it | Why it is not selected universally | When it remains useful |
|---|---|---|---|
| Improve only existing native files and direct references | Smallest change, familiar operation, no runtime adapter burden | Retained missed judgment reads and chat-only omissions remain unaddressed by file discovery alone | Baseline, degraded mode, and hosts where native adapters are unavailable |
| Convert every reference into an independent skill | Standardized discoverability and explicit invocation for every item | Definitions, subrules and fragments do not all form useful independent procedures; overlapping metadata increases selection burden | Promote a reference only when it owns a coherent repeatable workflow with distinctive intent |
| One monolithic Apex skill | Single entrypoint and easy onboarding | Loads unrelated detail and recreates the monolith; optional substeps can still be ignored | A thin index skill may introduce the system, without owning every procedure |
| Native scoped rules only | Host handles file-domain selection | Scope semantics differ and chat-only alternatives/rankings lack a path event | Governed file families with verified host loading |
| Full always-on inlining | Removes selection/read dependency for included text | Constant cost, drift and irrelevant ceremony; does not guarantee adherence | Keep the existing core and only add a critical slice when evidence justifies it |
| Registry plus autonomous semantic router service | Central visibility and flexible learned selection | Adds another model/service, failure point and policy owner without evidence of need in Apex's bounded corpus | Reopen only after a documented scale/routing failure in the simpler design |
| **Incremental native activation with selected workflow skills** | Reuses owners, permits chat routing, makes delivery/checking visible and adapts to actual hooks | Requires version probes and ongoing evidence maintenance; no universal enforcement guarantee | **Selected proposal**, with narrowly gated rollout and a direct-reference fallback |

The selected design's advantage is not a theoretical guarantee. It makes missing links explicit without replacing the existing system. A workflow owns procedure; a registry row owns activation metadata; native configuration owns loading and permissions; a deterministic checker owns only declared invariants; an independent evaluator owns the verdict. Any one of these may fail, so evidence and fallbacks remain visible.

## 8. How findings determine artifacts

| Finding | Concrete artifact consequence | Acceptance evidence |
|---|---|---|
| Current 23 tags differ from historical roster | Full current registry plus separate lineage | XML-to-registry bijection and downstream owner coverage |
| Pointer/read failure | Explicit source delivery requirements, negative triggers and missing-read recovery | Successful correct-source delivery before governed action/final answer |
| Chat-only gap | Decision-support skill example and prompt-boundary route; no dependency on a write event | Useful Q&A/ranking with grounded options and raw dimensions |
| Misleading keyword/typo over-application | Exclusions and semantic intent in registry/cases | Direct trivial answer with no unnecessary preflight, file, or skill |
| Event/schema variation | Per-host capability profiles and native fixtures | Pinned schema parse plus installed event/policy probe |
| False-positive graders | Independent artifact-state/meaning checks and scorer repair proposal | Rejected empty/fake-success/wrong-scope fixtures |
| Context loss | Small recovery record linked to existing work packets | Resume preserves scope, last completed action, evidence and next useful work |
| Carrier/source drift | Source hashes, projection mapping and explicit deployment preview | Detect changed/missing sources; report unavailable separately from in-sync |
| Existing role boundaries | Reuse doctrine and named accountabilities only in selected systems | No automatic Weekly/Multi-Agent cross-activation |
| Review-before-deployment | Draft/proposed labels and explicit adoption stages | No accepted/installed claims or live mutations from this package |

## 9. Consequential assumptions and limits

1. **Installed host state is unknown.** Current documentation supports the proposed adapters, but the operator's versions, account-specific roots, trust settings, local hooks and permissions require the supplied probes. The research container's `codex --version` is evidence only about that container.
2. **Cross-repository deployment remains conditional.** Leela/Mindful Bar surfaces described by retained sources are provenance; this run does not re-audit their branches or runtime state. First implementation should be an isolated Apex pilot, followed by explicit repository/branch resolution.
3. **The registry is a proposed metadata owner.** Canonical rule text remains in its existing source. Updating metadata does not amend the rule or promote a candidate.
4. **Hook receipt is not comprehension.** Read evidence confirms delivered bytes from a known version; adherence and usefulness still require evaluation. Unsupported or disabled events cannot be labeled enforced.
5. **Native model and skill selection remain fallible.** The proposal uses scoped intent and explicit workflows for material cases, with exclusion tests and a recovery path rather than a brittle keyword-only router.
6. **No hardware or model selection is made.** Local-engine operator locks remain intact; hardware screenshots do not establish throughput or the winning runtime.
7. **Package validation is bounded.** It establishes internal parseability, traceability and artifact consistency plus specified synthetic checks. It does not prove deployment reliability or operator acceptance.

**Failure guard:** do not turn the evidence-backed proposal into installed truth. Preserve source ownership and accepted domain meaning, apply the smallest approved integration change, and require both observable delivery and a useful outcome before claiming the mechanism works.
