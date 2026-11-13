---
type: Reference
id: APEX-INFRA-DECISIONS-20261112
title: Apex Infrastructure Decision Matrix
description: Reviewable alternatives, evidence, estimates, selected approaches and failure modes for each material infrastructure choice.
status: draft
adoption_status: proposed_for_operator_review
tags: [apex, decisions, alternatives, evidence]
---

# Decision matrix

**Improve the current owners and native mechanisms incrementally. Do not install this proposal or change accepted domain meaning without subsequent approval.** [decisions.json](design/decisions.json) owns the machine-readable decision record; this document is its generated review view. Every material choice records alternatives, a mechanism, concrete Apex grounding, evidence, a recommendation, rejections, a trade-off, a failure mode, affected components and a reconsideration condition.

## Estimates, examples and depth

The tags below are **new coarse design estimates**, not source-authored values, measured probabilities or calibrated rankings. WP-07 owns their meanings: impact, empirical grounding/verification, and downside/complexity. Authority fidelity is not empirical efficacy. Documentation and accepted requirements establish what a mechanism supports or must preserve; they do not prove that the proposed composition improves outcomes. New E values stay in the established-standard range unless an executed narrow artifact/scorer diagnostic supplies stronger evidence. Each machine option records its evidence kind and basis. Original authored tags remain unchanged in [the registry](registry/rules.json) and [history](registry/history.json).

Raw I/E/R are **never combined**. The separate [architecture bake-off](examples/architecture-comparison.md) preserves EM-07/GS-13’s required weighted criterion rubric when its trigger applies. That rubric has its own explicitly estimated criteria and sensitivity limits; it does not score rule authority or empirical reliability.

Examples are illustrative applications of actual Apex surfaces unless expressly labelled source-reported or executed. They are not fabricated measurements. Reversal before installation is simply revision of the proposal; an approved isolated pilot rolls back only captured scoped files/profile settings. The JSON records this reversal boundary per option. The architecture comparison works through two real task families for the serious architectural alternatives.

This is an autonomous review presentation under the current continuous-run assignment, **not a completed interactive EM-06a session**. Each question has its own raw estimate. Cross-feature, lower-evidence and permission-sensitive decisions are flagged for deeper operator review before deployment. That later review may require the full L3 interaction and further trial evidence. The present assignment supplies authorization to complete the package and overrides blocking comprehension/letter rounds. No recommendation is accepted by silence.

Repository citations are root-relative at the pinned revision. External IDs resolve to direct primary URLs and reviewed sections in [external sources](evidence/external-sources.json). See [the adoption plan](evaluation/evaluation-plan.md) for stage dependencies and the concrete operator decision sheet.

## Navigation

| ID | Decision | Selected approach | Stage |
|---|---|---|---|
| [D-01](#d-01) | Improve the existing system without a new runtime framework | Selective native composition | S2 |
| [D-02](#d-02) | Preserve the live XML and canonical detailed owners | Registry owns activation metadata | S1 |
| [D-03](#d-03) | Keep universal context selection outside optional skills | Always-on sufficient-context invariant | S1 |
| [D-04](#d-04) | Package coherent procedures, retain references and schemas | Three workflow candidates with owner references | S2 |
| [D-05](#d-05) | Recognize task intent, including chat-only decisions | Semantic native selection plus explicit override | S2 |
| [D-06](#d-06) | Use native scope as a signal, not universal policy coverage | Per-surface scope plus task fallback | S1 |
| [D-07](#d-07) | Revisit physical carrier duplication only after exact loader probes | Retain current carriers; pilot one verified projection | S3 |
| [D-08](#d-08) | Separate semantic guidance from enforceable hook preconditions | Narrow covered preconditions; soft semantic reminders | S3 |
| [D-09](#d-09) | Share policy inputs, adapt native events separately | Pure bounded policy plus thin native adapters | S3 |
| [D-10](#d-10) | Treat missing or failed hooks as unavailable coverage | Expose coverage state and choose task-specific fallback | S3 |
| [D-11](#d-11) | Count observed delivery separately from source access attempts | Successful delivered source/version/section before action | S3 |
| [D-12](#d-12) | Keep independent semantic review proportionate | Independent check using original requirements and artifact | S2 |
| [D-13](#d-13) | Persist task state in files, recover at the next supported boundary | Existing run state plus optional activation sidecar | S2 |
| [D-14](#d-14) | Reuse roles and preserve orchestration boundaries | Shared delivery capability, separate systems | S1 |
| [D-15](#d-15) | Preserve permission boundaries and probe effective configuration | Record the defect and inspect effective mode later | S1 |
| [D-16](#d-16) | Pilot shared skill sources without mass relocation | Keep current owners; pilot one new portable workflow | S2 |
| [D-17](#d-17) | Extend existing distribution checks with honest status | Bounded extensions to current tools | S3 |
| [D-18](#d-18) | Resolve missing pointers with exact scoped patches | Pinned exact-match proposal per file | S1 |
| [D-19](#d-19) | Use current retrieval policy with authenticated fallback | Owner-scoped retrieval, direct source validation | S1 |
| [D-20](#d-20) | Repair evaluator meaning before measuring adoption | Keep useful fixtures, replace insufficient predicates | S1 |
| [D-21](#d-21) | Separate packaging comparisons from hook/reminder causality | Architecture arms plus a separate factorial | S2 |
| [D-22](#d-22) | Preserve raw priorities and separate all scoring concepts | Separate preserved and estimated dimensions | S1 |
| [D-23](#d-23) | Resolve authorization conflicts without automatic persistence | Current scoped authorization controls actions | S0 |
| [D-24](#d-24) | Keep SDK, hosted and bare surfaces as explicit profiles | Separate capability profiles and boot contracts | S1 |
| [D-25](#d-25) | Defer plugins, MCP policy services and model/hardware selection | Define interfaces; defer unproven infrastructure | S4 |
| [D-26](#d-26) | Adopt by dependency-aware stages and rollback evidence | Scoped approval and evidence gates | S0 |

<a id="d-01"></a>

## D-01 — Improve the existing system without a new runtime framework

**Question:** Which composition closes activation and verification gaps with proportionate maintenance? **New question estimate:** (I95/E60/R50).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** DEC-08 rejects a tiny shared abstraction; DEC-12/13 retain reduced core; handover14 asks that all-reference skills remain a serious option.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Improved existing files only | Repair pointers and metadata; use current carriers and direct source reads without new activation components. **Example:** A chat ranking loads EM-06 only when the model recognizes the existing XML condition. | [P1 \| I80/E70/R10] | Retain as baseline and full degraded mode; alone it leaves important missed-read cases unresolved. |
| B — Selective native composition | Keep owners and core; add a design-time activation index, three workflow candidates, optional bounded hook adapters, and independent outcome checks. **Example:** A governed test spec selects one workflow, loads FA/EM owners, and validates the resulting spec. | [P1 \| I90/E70/R30] | Selected; pilot before claiming reliable adoption. |
| C — Registry router service | Run a separate semantic classifier/service on every request and return an active-rule bundle. **Example:** Every typo, chat answer and engineering turn incurs routing and service dependencies. | [P1 \| I80/E45/R75] | Defer: no measured routing-scale problem justifies another service or model dependency. |
| D — All reference files as skills | Wrap each reference in skill metadata and expose all through native discovery. **Example:** QA, file architecture, governance schemas and each small adapter become independent selectable units. | [P1 \| I85/E60/R50] | Retain as evaluation arm; definitions and overlapping triggers create selection and ownership costs. |
| E — One Apex skill | Use one explicit entrypoint that branches internally into every reference. **Example:** The operator invokes the same skill for a ranking, typo and long research task. | [P1 \| I70/E55/R40] | Reject as universal default; a thin orientation index can still be useful. |
| F — All rules always loaded | Inline the detailed owner corpus into every session. **Example:** The typo task receives governance and Q&A requirements it does not need. | [P1 \| I65/E60/R60] | Reject globally; preserve only the current universal core and justified critical slices. |
| G — Native scoped rules only | Use native path scopes and direct references without new workflow packages. **Example:** A governed specification path can load formatting constraints, while a conversational ranking has no file event. | [P1 \| I70/E65/R35] | Retain as a packaging arm and component; insufficient alone for chat-only activation. |

**Recommendation: B.** This composition addresses conversational routing and narrow preconditions while preserving the proven file owners. Vendor documentation establishes mechanisms; retained failures and studies establish why they need separate evaluation. No study proves this whole composition wins in Apex.

**Reasoning and trade-off:** More metadata and per-surface maintenance than native-only; less runtime complexity than a central service. **Primary failure:** The optional skill is selected incorrectly or an uncovered action is mistaken for enforced execution.

**Evidence:** `apex-meta/informatics/final/candidates/01-decision-register.md §§DEC-08,12,13`; `apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/HANDOVER-14-APEX-RULE-REGISTRY-AND-ACTIVATION-INTEGRATION.md §§3,7`; `apex-meta/informatics/final/operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md Executive verdict`. External: EEMP-02, EEMP-03, EEMP-05, EXT-OAI-01, EXT-CLAUDE-02.

**Affected components:** `03-architecture.md`, `registry/rules.json`, `examples/workflows/`, `evaluation/evaluation-plan.md`. **Stage:** S2.

**What would change this choice:** A controlled same-content trial finds no outcome benefit over improved existing files, or selection failures persist enough to justify a different packaging strategy.

<a id="d-02"></a>

## D-02 — Preserve the live XML and canonical detailed owners

**Question:** Where does rule meaning live, and what may the registry own? **New question estimate:** (I95/E70/R25).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** DEC-01/02/03 preserve single owners; DEC-17 selects named tags; current ultra XML supersedes 22-rule candidates.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Registry becomes the policy master | Move normative definitions into JSON and generate every source. **Example:** Editing XML.authoring in JSON would rewrite the established authoring contract. | [P1 \| I80/E45/R70] | Reject: would silently change accepted ownership and require a separate migration decision. |
| B — Registry owns activation metadata | Keep canonical text in current owners; record identities, source hashes, trigger/delivery/verification metadata and frozen evidence excerpts. **Example:** WP-07 remains in writing-profile.md; its registry record points to that section and preserves authored metrics. | [P1 \| I95/E70/R15] | Selected. |
| C — Only prose cross-references | Keep all routing relationships in prose and native files with no structured coverage view. **Example:** A new tag can appear in XML without an obvious unmapped activation/verification row. | [P1 \| I65/E70/R20] | Insufficient for the requested populated lifecycle registry. |

**Recommendation: B.** The registry fills a coordination gap without overruling the domain contract. Snapshot quotes make review self-contained but never become a second normative source.

**Reasoning and trade-off:** Metadata can drift even when definitions do not; source change requires a targeted registry update. **Primary failure:** A reviewer treats a frozen excerpt or proposed activation as accepted current policy.

**Evidence:** `apex-meta/informatics/final/candidates/01-decision-register.md §§DEC-01..09,17`; `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml`; `apex-meta/informatics/final/specs/writing-profile.md WP-23`. External: EEMP-13.

**Affected components:** `registry/rules.json`, `registry/rule-registry.schema.json`, `registry/history.json`, `evidence/repository-sources.json`. **Stage:** S1.

**What would change this choice:** The operator explicitly authorizes a new canonical serialization and a source-preserving migration plan.

<a id="d-03"></a>

## D-03 — Keep universal context selection outside optional skills

**Question:** Should the context rule itself require skill activation or a hard token budget? **New question estimate:** (I90/E65/R25).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** A06 selected sufficiency over smallest context and rejected a dedicated deeper artifact; live XML context/recovery are current.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Hard universal token ceiling | Refuse deeper context after one fixed limit on every task. **Example:** A long research task drops a load-bearing source to meet a token target. | [P1 \| I55/E40/R65] | Reject: the Codex skill-list budget is not a universal correctness ceiling. |
| B — Always-on sufficient-context invariant | Keep the live compact rule; retrieve the next needed owner/source and use durable state for long work. **Example:** A short typo stays short; an architecture study expands when an actual conflict requires another owner. | [P1 \| I95/E70/R20] | Selected. |
| C — Optional context-management skill | Make context selection itself depend on selecting a separate skill. **Example:** The same routing miss that hides a rule also hides the rule for restoring it. | [P1 \| I60/E45/R45] | Reject as the universal mechanism; a separate context-audit task may later justify a skill. |

**Recommendation: B.** The invariant governs whether deeper procedures are loaded; placing it behind optional selection is circular. Current native budget facts inform testing, not doctrine.

**Reasoning and trade-off:** Sufficiency requires judgment and cannot be guaranteed by a numerical ceiling. **Primary failure:** Excessively narrow retrieval omits a constraint while appearing efficient.

**Evidence:** `apex-meta/informatics/final/research/01-universal-instruction-research/module-deepening/A06-context-engineering-progressive-disclosure/README.md §§7,9,10`; `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml <context>,<recovery>`. External: EEMP-01, EEMP-08, EEMP-12, EXT-OAI-02.

**Affected components:** `03-architecture.md`, `examples/workflows/apex-research-cycle/SKILL.md.example`, `evaluation/cases.json`. **Stage:** S1.

**What would change this choice:** Measured context pressure identifies a repeatable domain-specific budget or audit need without dropping material constraints.

<a id="d-04"></a>

## D-04 — Package coherent procedures, retain references and schemas

**Question:** Which existing material deserves a separately discoverable skill? **New question estimate:** (I90/E60/R40).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** The retained brief explicitly asks to compare all references as skills; Hermes D05 accepts shared-source direction with a pilot, not a mass conversion.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Every reference independently selectable | Add a SKILL.md wrapper to each owner and small subrule. **Example:** A decision task must choose among QA, bake-off, metrics and evidence fragments. | [P1 \| I85/E60/R50] | Evaluation contender; reject as the default until retrieval benefit exceeds metadata and fragmentation costs. |
| B — Three workflow candidates with owner references | Provide decision-support, governed-authoring and long-research workflows; retain definition files and machine schemas in place. **Example:** Test-spec creation reads the task-spec owner and the actual frontmatter/patch schemas as needed. | [P1 \| I95/E70/R25] | Selected as a bounded pilot, not a mandatory final skill count. |
| C — Direct references only | Use XML cues plus explicit reads; expose no new skills. **Example:** The operator can still request EM-06 directly on an unsupported host. | [P1 \| I75/E70/R10] | Keep as fallback and baseline. |

**Recommendation: B.** Each candidate has a recognizable task, ordered work and useful result. File schemas and isolated constraints are inputs to those workflows rather than independent user jobs.

**Reasoning and trade-off:** A workflow can be too broad or fail to open its references; metadata tuning is still necessary. **Primary failure:** Selection of a similarly named skill loads the wrong owner or skips a dependency.

**Evidence:** `apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md §2`; `apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D05-SHARED-SKILL-SOURCE.md Promotion gate`; `apex-meta/informatics/final/specs/file-architecture.md FA-03`. External: EEMP-02, EEMP-03, EEMP-04, EEMP-13, EXT-OAI-02, EXT-CLAUDE-02.

**Affected components:** `examples/workflows/`, `registry/rules.json`, `evaluation/cases.json`. **Stage:** S2.

**What would change this choice:** Same-content trials show finer-grained or direct-reference packaging has better useful outcomes and acceptable maintenance cost.

<a id="d-05"></a>

## D-05 — Recognize task intent, including chat-only decisions

**Question:** How do rankings and Q&A activate without any file event? **New question estimate:** (I90/E60/R35).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** EM-06 excludes routine reversible choices; the current brief explicitly includes conversational answers and misleading triggers.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Keyword-only trigger | Match compare/rank/Q&A tokens and inject a matrix. **Example:** A request to fix a typo in the word ranking accidentally starts a decision workflow. | [P1 \| I60/E50/R60] | Reject as sole selector; keywords may provide hints only. |
| B — Semantic native selection plus explicit override | Match the requested outcome and exclusions; use native skill descriptions and an explicit invocation path; material uncertainty is resolved in context. **Example:** Which CLI architecture fits Apex? selects decision support even when no file is created. | [P1 \| I90/E70/R30] | Selected. |
| C — Write-hook activation only | Wait for a file write to select downstream rules. **Example:** A complete conversational architecture recommendation has no trigger event. | [P1 \| I45/E70/R40] | Reject for answers; retain as an additional signal for governed file operations. |

**Recommendation: B.** The task is the requested decision, not a vocabulary item or file extension. The existing XML obligation remains active when automatic selection fails.

**Reasoning and trade-off:** Native selection is probabilistic; explicit invocation improves recoverability but adds operator effort when needed. **Primary failure:** A negative or quoted trigger is treated as user intent.

**Evidence:** `apex-meta/informatics/final/specs/execution-modes/qa-decision-matrix.md §§2,2.1,2.3`; `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml <trade_off>`. External: EXT-OAI-02, EXT-CLAUDE-02, EXT-AGY-03, EEMP-03, EEMP-04.

**Affected components:** `examples/workflows/apex-decision-support/SKILL.md.example`, `examples/end-to-end-flows.md`, `evaluation/cases.json`. **Stage:** S2.

**What would change this choice:** Measured false positives or misses justify changed descriptions, smaller procedure boundaries, or a bounded router after simpler repairs fail.

<a id="d-06"></a>

## D-06 — Use native scope as a signal, not universal policy coverage

**Question:** Which rule scopes can safely be delegated to native loaders? **New question estimate:** (I90/E70/R40).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** Five-plane path-scoping is intent; historical claims about descendants and AGENTS behavior are surface-specific.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — One path rule copied everywhere | Assume every native loader reads nested instructions when a file is touched. **Example:** An Antigravity descendant rule is assumed to apply despite its workspace/ancestor discovery boundary. | [P1 \| I65/E35/R60] | Reject: documented loading semantics differ. |
| B — Per-surface scope plus task fallback | Project path constraints through each verified loader; preserve intent-based source reads for new paths, chat and unverified profiles. **Example:** A governed spec outside the discovered ancestor chain still loads its owner through the workflow. | [P1 \| I90/E70/R25] | Selected. |
| C — Always load all scoped rules | Eliminate path uncertainty by loading every subtree rule into the core. **Example:** A code typo inherits unrelated documentation requirements. | [P1 \| I55/E65/R55] | Reject as blanket solution. |

**Recommendation: B.** The shared layer owns meaning, while the native adapter owns actual scope and limitations. A declared path pattern is never logged as successful loading without evidence.

**Reasoning and trade-off:** Each surface needs an explicit discovery probe and documented fallback. **Primary failure:** A newly created path or alternate working directory bypasses the expected scope.

**Evidence:** `apex-meta/informatics/final/specs/file-architecture.md §§2,FA-03`; `apex-meta/informatics/final/research/01-universal-instruction-research/07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md §§4.3,6`. External: EXT-OAI-03, EXT-CLAUDE-01, EXT-AGY-01, EXT-AGY-02.

**Affected components:** `compatibility/compatibility.md`, `compatibility/probe-plan.json`, `03-architecture.md`. **Stage:** S1.

**What would change this choice:** A native loader change establishes broader reliable scope and the same negative tests still pass.

<a id="d-07"></a>

## D-07 — Revisit physical carrier duplication only after exact loader probes

**Question:** Can newer native AGENTS support replace byte-identical vendor copies? **New question estimate:** (I90/E65/R50).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** DEC-21/22 selected physical copies because standalone loaders and imports differed; named-tag and equal-behavior intent remain.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Immediately replace all carriers with stubs | Convert every vendor file into a pointer/import to AGENTS.md. **Example:** A host whose import or fallback rule differs silently loses core constraints. | [P1 \| I80/E45/R70] | Reject before probes; a prose pointer is not an import. |
| B — Keep copies forever | Preserve the old physical pattern regardless of new support. **Example:** A current native AGENTS loader may inject duplicate contract copies. | [P1 \| I70/E70/R30] | Safe interim only; permanent duplication misses a real simplification opportunity. |
| C — Retain current carriers; pilot one verified projection | Test precedence, one-copy loading, exact semantic parity and recovery per profile; replace only redundant tested copies after approval. **Example:** Claude v2.1.277+ support is evaluated alongside CLAUDE precedence and configuration IDs rather than assumed from its version. | [P1 \| I95/E70/R25] | Selected. |

**Recommendation: C.** New primary evidence invalidates the universal no-native-AGENTS premise, not the original equal-behavior requirement. This is a conditional capability revision to DEC-21/22, not an authorized rewrite.

**Reasoning and trade-off:** Temporary duplication persists until native behavior is measured. **Primary failure:** Both carriers load, or neither does, despite matching disk hashes.

**Evidence:** `apex-meta/informatics/final/candidates/01-decision-register.md §§DEC-21,22; Standalone CLI Loader Behavior`; `apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md`. External: EXT-OAI-03, EXT-CLAUDE-01, EXT-AGY-01.

**Affected components:** `design/integration-map.json`, `compatibility/probe-plan.json`, `03-architecture.md`. **Stage:** S3.

**What would change this choice:** The exact target loader demonstrates one canonical discovery path under startup, nested cwd, resume and delegation conditions.

<a id="d-08"></a>

## D-08 — Separate semantic guidance from enforceable hook preconditions

**Question:** Which rules should a hook block, advise about, or leave to review? **New question estimate:** (I95/E60/R55).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Q002 favors hard gates for high-risk cases; current Multi-Agent architecture deliberately has no hook layer; Round2 intervention is confounded.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Block on all semantic rules | Translate each requirement into a regex or model judgment gate. **Example:** An answer is blocked because a lexical phrase is missing although the required reasoning is present. | [P1 \| I80/E40/R75] | Reject: imprecise gates create false denials and a second semantic policy. |
| B — Narrow covered preconditions; soft semantic reminders | Gate only explicit, measurable preconditions on verified events; use brief context and independent review for judgment rules. **Example:** A confirmed patch target outside the authorized set is denied; an architecture answer is checked against EM-06 after composition. | [P1 \| I95/E70/R30] | Selected; exact candidate gate requires later approval and probe. |
| C — No hooks anywhere | Rely on prompts, skills and final evaluation for every action. **Example:** A covered premature write cannot be interrupted by the shared layer. | [P1 \| I70/E70/R15] | Baseline and unsupported-surface fallback; insufficient where a demonstrated hard boundary is valuable. |

**Recommendation: B.** Hooks can enforce only the action and condition they observe. They cannot establish correct intent, comprehension or useful output merely by firing.

**Reasoning and trade-off:** Coverage is intentionally incomplete and must be visible. **Primary failure:** A tool bypass, disabled hook or ambiguous parser is logged as a successful guard.

**Evidence:** `apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md Q002`; `apex-meta/orchestration/ARCHITECTURE.md §6`; `apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md`. External: EXT-OAI-01, EXT-CLAUDE-03, EXT-AGY-04, EEMP-14.

**Affected components:** `03-architecture.md`, `examples/native/`, `evaluation/evaluation-plan.md`. **Stage:** S3.

**What would change this choice:** A predicate lacks a reliable normalized event or incurs material false denials; then keep it advisory or remove it.

<a id="d-09"></a>

## D-09 — Share policy inputs, adapt native events separately

**Question:** How much hook implementation should be cross-CLI? **New question estimate:** (I90/E65/R45).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Handover13 proposed shared Python/thin adapters; the proposal snapshot is not installed and its capability claims need refresh.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — One universal event envelope | Accept identical event names, payload keys and decision responses on all hosts. **Example:** Claude hookSpecificOutput is sent to an Antigravity hook with different response fields. | [P1 \| I45/E25/R75] | Reject: concrete schemas and event effects differ. |
| B — Pure bounded policy plus thin native adapters | Keep source IDs, authorized target/state and predicates shared; parse and emit native formats in separate adapters with fixtures. **Example:** The same read-receipt requirement is mapped to a covered Codex PreToolUse or supported Antigravity pre-tool event. | [P1 \| I90/E70/R30] | Selected design boundary; supplied canary is illustrative, not the production guard. |
| C — Independent full implementations | Each host owns separate rule text and policy logic. **Example:** Updating a source-read condition requires three policy edits. | [P1 \| I75/E70/R50] | Reject as default because semantic drift becomes routine. |

**Recommendation: B.** Only the small common policy data is portable. Native adapters own lifecycle, trust, denial semantics, tool names and unsupported paths.

**Reasoning and trade-off:** Adapter fixtures and documentation must track native releases. **Primary failure:** Schema-valid output has unsupported runtime meaning, such as Codex ask or continue:false in PreToolUse.

**Evidence:** `apex-meta/informatics/final/operations/handovers/HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md`; `apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/cross-cli-hook-architecture.md`. External: EXT-OAI-01, EXT-OAI-13, EXT-CLAUDE-03, EXT-AGY-04, EXT-GEMINI-03.

**Affected components:** `examples/native/`, `compatibility/compatibility.md`, `design/integration-map.json`. **Stage:** S3.

**What would change this choice:** A host cannot expose the required event or reliable identity, in which case use the direct-reference fallback and report the missing coverage.

<a id="d-10"></a>

## D-10 — Treat missing or failed hooks as unavailable coverage

**Question:** What happens when a guard is disabled, untrusted, malformed or misses a tool? **New question estimate:** (I95/E65/R50).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Retained benchmark fixture fails open for some errors and unknown tools; hosted/local enforcement differ.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Assume no denial means pass | Treat a missing hook result as successful policy approval. **Example:** A disabled handler yields the same green status as a validated receipt. | [P1 \| I30/E25/R90] | Reject. |
| B — Force all failures closed globally | Deny every tool when any optional hook is unavailable. **Example:** A read-only typo explanation is blocked by a missing optional post-tool observer. | [P1 \| I65/E40/R70] | Reject globally; fail-closed can be correct for a narrowly approved mandatory gate with a reliable host contract. |
| C — Expose coverage state and choose task-specific fallback | Mark covered_verified, unavailable, bypassed, or unknown; use native permissions and explicit procedure/review; stop only the action that lacks a required precondition. **Example:** A high-risk canonical mutation waits for its actual authority predicate, while safe source reading continues. | [P1 \| I95/E70/R25] | Selected. |

**Recommendation: C.** The hook is not the permission system. A meaningful missing guarantee must constrain the specific dependent action without imposing ritual on unrelated work.

**Reasoning and trade-off:** The orchestrating agent must understand unknown versus deny and communicate the material limitation. **Primary failure:** A fail-open native path is concealed behind a generic success flag.

**Evidence:** `apex-meta/informatics/final/research/10-ultra-upgrade-validation/fixtures/armB_hook_agy.py`; `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml <ground>,<recovery>`. External: EXT-OAI-01, EXT-CLAUDE-03, EXT-AGY-04.

**Affected components:** `03-architecture.md`, `evaluation/cases.json`, `compatibility/probe-plan.json`. **Stage:** S3.

**What would change this choice:** Runtime evidence proves a stronger native guarantee for a specific event and approved action class.

<a id="d-11"></a>

## D-11 — Count observed delivery separately from source access attempts

**Question:** What is a valid source-read receipt? **New question estimate:** (I90/E70/R35).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** Routing pilots and trace scorers show that search hits, basenames and failed tools can be miscounted as reads.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Presence or attempted read | Check whether the source path appears in text, a Glob or an issued command. **Example:** An unsuccessful Glob with no delivered content gets credit. | [P1 \| I20/E30/R80] | Reject; synthetic counterexample executed. |
| B — Successful delivered source/version/section before action | Observe content delivery and success; bind receipt to source hash, task, session epoch and relevant section; invalidate on source/task changes. **Example:** A successful read of the governing authoring section precedes the governed write. | [P1 \| I95/E70/R25] | Selected; native auto-load evidence uses host trace where available. |
| C — Require full-file read every time | Always reload all owners before each write. **Example:** The second paragraph edit repeats the entire governance corpus. | [P1 \| I60/E65/R50] | Reject as default; expand a slice only when needed for sufficient context. |

**Recommendation: B.** A receipt proves access to known bytes. Independent checks still determine adherence and outcome. Unknown native loading remains unknown, not fabricated from directory presence.

**Reasoning and trade-off:** Some hosts cannot expose exact delivered bytes, so receipt quality differs by profile. **Primary failure:** A stale receipt survives compaction, hash changes or delegation and is reused for a different task.

**Evidence:** `apex-meta/informatics/final/research/08-read-trace-routing-experiments/artifacts/stage1/score_stage1_corrected.py read detection`; `apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py §§trace parsing,deterministic_checks`. External: EEMP-14.

**Affected components:** `03-architecture.md`, `examples/activation-state.schema.json`, `evaluation/evaluation-plan.md`. **Stage:** S3.

**What would change this choice:** A cheaper observable can be shown to preserve delivery fidelity on the same adversarial traces.

<a id="d-12"></a>

## D-12 — Keep independent semantic review proportionate

**Question:** Who verifies correctness beyond syntax and the author’s own rubric? **New question estimate:** (I90/E65/R35).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** XML target rejects self-authored criteria as substitutes; Detective validity and alignment are separate blind lenses.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Author checklist only | Let the creator declare its artifact complete using chosen checks. **Example:** An empty report passes a line-count test and is called useful. | [P1 \| I45/E45/R75] | Reject for material outcomes. |
| B — Independent check using original requirements and artifact | Give a reviewer original task, source owners and actual output without the creator’s verdict; use separate validity/alignment lenses when the named system is active. **Example:** The reviewer detects a correct JSON registry whose workflow ignores chat rankings. | [P1 \| I95/E70/R25] | Selected; ordinary typo work needs bounded inspection, not a new review fleet. |
| C — Always invoke a different external model family | Treat provider diversity as required independence for every task. **Example:** A trivial edit requires another provider account and unapproved data transfer. | [P1 \| I70/E50/R65] | Reject as blanket rule; contrary to current scoped system boundaries without approval. |

**Recommendation: B.** Evidence and task separation are necessary; model identity alone is insufficient. This package’s independent artifact review is bounded and is not a claim that the repository Detective workflow ran.

**Reasoning and trade-off:** Review can still share blind spots and adds cost on material work. **Primary failure:** The reviewer sees only the author’s rationale or tests and ratifies the same mistake.

**Evidence:** `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml <target>`; `apex-meta/orchestration/workflows/detective-review.md`; `apex-meta/orchestration/schemas/review-verdict.schema.md`. External: EEMP-14, EEMP-10.

**Affected components:** `evaluation/evaluation-plan.md`, `07-validation-report.md`, `03-architecture.md`. **Stage:** S2.

**What would change this choice:** Repeated misses identify a specific missing lens or evidence source, not merely a desire for more agents.

<a id="d-13"></a>

## D-13 — Persist task state in files, recover at the next supported boundary

**Question:** How do constraints survive long research, compaction, interruption and delegation? **New question estimate:** (I95/E60/R45).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Current recovery/iterative rules and local-engine lock use durable files; Hermes D09 defers shared external memory.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Transcript or memory only | Rely on the model’s retained summary or vendor history. **Example:** After interruption, a rejected option reappears as accepted. | [P1 \| I50/E55/R70] | Reject as sole authoritative state. |
| B — Existing run state plus optional activation sidecar | Persist target, authorization, decisions, unresolved sources, next action and hashes in the owning run files; use a small proposed sidecar only for coverage receipts. **Example:** After compaction, reload the current task record and the one owner needed for the next action. | [P1 \| I95/E70/R25] | Selected; no new database or scheduler. |
| C — New universal memory service | Centralize all histories, state and rule decisions in a service. **Example:** Two project boards are mirrored into a new cross-repository authority. | [P1 \| I75/E45/R75] | Defer: violates the intended project-truth separation without a proven need and approval. |

**Recommendation: B.** Recovery is an idempotent work step. Native compaction events can assist but are not required; Antigravity can use the next supported invocation or explicit restart.

**Reasoning and trade-off:** Checkpoints need deliberate updates and can still contain misleading summaries. **Primary failure:** The first resumed action uses stale authorization or promotes an unverified candidate.

**Evidence:** `apex-meta/informatics/final/specs/execution-modes/iterative-execution.md`; `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md §§8,13`; `apex-meta/epics/hermes-multi-repo-orchestration-v2/DECISIONS.md D09`. External: EEMP-08, EEMP-09, EEMP-15, EXT-OAI-01, EXT-CLAUDE-01, EXT-AGY-04, EXT-CLAUDE-03.

**Affected components:** `03-architecture.md`, `examples/activation-state.schema.json`, `examples/workflows/apex-research-cycle/SKILL.md.example`, `evaluation/cases.json`. **Stage:** S2.

**What would change this choice:** File-based recovery fails reproducibly at required scale and an approved store offers a measurable advantage without changing authority.

<a id="d-14"></a>

## D-14 — Reuse roles and preserve orchestration boundaries

**Question:** Does shared infrastructure create a new agent system? **New question estimate:** (I95/E70/R40).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Weekly and Multi-Agent are separate; Plan-Sync-Session is shared backbone; Alfred and Meta Ops remain main accountabilities.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Merge orchestration into one dispatcher | A new runtime automatically selects Weekly, Multi-Agent and Plan from task text. **Example:** Mentioning a weekly report starts the named system without operator activation. | [P1 \| I70/E35/R85] | Reject: changes accepted system meaning and authorization. |
| B — Shared delivery capability, separate systems | Reuse current role doctrine and bounded native adapters only within the explicitly selected system; ad hoc research delegation remains distinct. **Example:** Weekly consumes its existing confirmed Session feed and Sync output; it does not acquire a new Plan stage. | [P1 \| I95/E70/R15] | Selected. |
| C — Create dedicated rule agents for every layer | Add a routing agent, registry agent, hook agent and recovery agent to ordinary work. **Example:** A simple governed document passes through a new multi-agent chain. | [P1 \| I65/E35/R65] | Reject absent a repeated accountability gap. |

**Recommendation: B.** A capability can serve two systems without becoming either system’s orchestrator. File authority and explicit activation remain independent of role labels.

**Reasoning and trade-off:** Platform-native role fields differ; thin wrappers may still be necessary. **Primary failure:** A helpful skill invocation is mistaken for activation of the named orchestration system.

**Evidence:** `.claude/CLAUDE.md Orchestration systems`; `apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml`; `apex-meta/orchestration/ARCHITECTURE.md §§2..7`; `.claude/skills/weekly-orchestrator/SKILL.md`. External: EXT-OAI-04, EXT-CLAUDE-04, EXT-AGY-05.

**Affected components:** `03-architecture.md`, `design/integration-map.json`, `examples/native/`. **Stage:** S1.

**What would change this choice:** The operator explicitly approves changed orchestration doctrine and associated handoff/authority contracts.

<a id="d-15"></a>

## D-15 — Preserve permission boundaries and probe effective configuration

**Question:** How should the malformed or ineffective Claude permission setting be handled? **New question estimate:** (I95/E70/R60).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Repository has top-level defaultMode; project intent and effective runtime policy are distinct.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Move bypassPermissions to a current key automatically | Repair the syntax to make the apparent bypass setting effective. **Example:** The design run expands a project’s permission posture while claiming a harmless config cleanup. | [P1 \| I20/E20/R95] | Reject: unauthorized and potentially disallowed by current scope rules. |
| B — Record the defect and inspect effective mode later | Provide a read-only probe for version, setting precedence and actual permission behavior; prepare a least-privilege task profile only after explicit approval. **Example:** An operator reviews the effective mode rather than inferring it from one JSON field. | [P1 \| I95/E70/R15] | Selected. |
| C — Assume project file is authoritative | Document bypass as the installed state. **Example:** An agent tries an action under permissions the runtime does not grant. | [P1 \| I35/E15/R80] | Reject: source text does not establish loaded policy. |

**Recommendation: B.** Current Claude docs place defaultMode under permissions and restrict project/local auto/bypass settings. Codex subagent prompts likewise cannot supply an independent sandbox.

**Reasoning and trade-off:** The package cannot certify installed permission behavior without workstation access. **Primary failure:** A schema cleanup inadvertently broadens permissions or a read-only role is treated as sandbox enforcement.

**Evidence:** `.claude/settings.json`; `.claude/CLAUDE.md Global boundaries`; `AGENTS.md Git Dispatch`. External: EXT-CLAUDE-07, EXT-CLAUDE-05, EXT-OAI-09, EXT-OAI-04.

**Affected components:** `compatibility/probe-plan.json`, `design/integration-map.json`, `examples/native/`. **Stage:** S1.

**What would change this choice:** An authorized installed-profile audit establishes the precise effective setting and desired posture.

<a id="d-16"></a>

## D-16 — Pilot shared skill sources without mass relocation

**Question:** Where should portable skills and platform wrappers live? **New question estimate:** (I85/E65/R40).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Hermes D05 accepts shared-source direction conditional on a pilot; existing .claude skills and .agents QMD remain live.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Relocate all skills to .agents immediately | Move existing sources and symlink every vendor root. **Example:** A functioning Session procedure changes its path on three hosts at once. | [P1 \| I85/E50/R70] | Reject before D05 pilot and loader verification. |
| B — Keep current owners; pilot one new portable workflow | Use .agents/skills as a proposed canonical location only for the new pilot; deliver a supported adapter/copy where needed and track its origin/hash. **Example:** Decision-support is tested in one isolated project while existing Plan/Sync/Session paths remain unchanged. | [P1 \| I90/E70/R25] | Selected. |
| C — Independent vendor-owned copies | Author separate task semantics in each native root. **Example:** Three QA skills diverge when EM-06 changes. | [P1 \| I60/E65/R55] | Reject as default; generated/scoped projections are allowed without redefining ownership. |

**Recommendation: B.** This makes D05 concrete without pretending its promotion gate is complete. Symlinks, plugins and copies have different host support and trust implications.

**Reasoning and trade-off:** A temporary projection may duplicate bytes; discovery and drift still need checking. **Primary failure:** Same-name skills resolve ambiguously, or a supported symlink is mistaken for universal support.

**Evidence:** `apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D05-SHARED-SKILL-SOURCE.md`; `.claude/skills/apex-plan/SKILL.md`; `.agents/skills/qmd/SKILL.md`. External: EXT-OAI-02, EXT-CLAUDE-02, EXT-AGY-03, EEMP-13.

**Affected components:** `03-architecture.md`, `design/integration-map.json`, `examples/workflows/`. **Stage:** S2.

**What would change this choice:** The shared-source pilot proves a supported distribution method for each selected profile and no domain owner changes.

<a id="d-17"></a>

## D-17 — Extend existing distribution checks with honest status

**Question:** How are carriers, native adapters and source versions kept aligned? **New question estimate:** (I85/E70/R40).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Existing carrier sync and vendor drift tools already own comparisons; some roots are workstation-specific and unavailable master can exit zero.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — New distribution framework | Replace existing tools with a universal installer and daemon. **Example:** Every source change triggers an autonomous multi-repository deployment. | [P1 \| I65/E35/R80] | Reject absent demonstrated benefit and explicit deployment authorization. |
| B — Bounded extensions to current tools | Parameterize selected roots, include adapter/schema assets, separate skipped/unknown/drift/in-sync, preview exact scoped changes and preserve rollback bytes. **Example:** Unavailable master produces unknown, while a hook config hash mismatch is a review item. | [P1 \| I90/E70/R25] | Selected; implementation remains a proposal. |
| C — Keep checks unchanged | Only compare today’s Markdown/vendor manifests and infer success from exit code. **Example:** A changed JSON hook configuration escapes the Markdown-only check. | [P1 \| I55/E70/R50] | Insufficient for new adapter assets. |

**Recommendation: B.** Reuse comparison logic and make its boundaries explicit. Refreshing a manifest is not evidence that drift is correct, and matching bytes is not proof of activation.

**Reasoning and trade-off:** Native parsing and hash scopes add maintenance to existing scripts. **Primary failure:** An automatic manifest rewrite blesses unintended drift or normalizes a missing source as synchronized.

**Evidence:** `apex-meta/informatics/final/tools/apex_carrier_sync.py`; `apex-meta/informatics/final/tools/check_vendor_drift.py`; `apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md`. External: EXT-OAI-01, EEMP-07.

**Affected components:** `design/integration-map.json`, `03-architecture.md`, `evaluation/cases.json`. **Stage:** S3.

**What would change this choice:** A bounded extension becomes more complex than its value, or a platform-supported distribution unit removes the same failure with less infrastructure.

<a id="d-18"></a>

## D-18 — Resolve missing pointers with exact scoped patches

**Question:** How should known navigation defects be made reviewable without rewriting owners? **New question estimate:** (I85/E85/R10).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** GS-02/EM-01 prohibit whole-file rewrites; DEC-03 preserves the actual patch schema; source audit identifies exact defects.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Rewrite and consolidate documents | Regenerate affected files to remove broken links and simplify layout. **Example:** A one-link fix changes unrelated rules and formatting. | [P1 \| I50/E30/R85] | Reject; unnecessary scope and loss of byte-preserving review. |
| B — Pinned exact-match proposal per file | Record original hash, unique old/new text, purpose and constraints; require a fresh preflight before any later application. **Example:** The AGENTS governance link is corrected to final/specs/standard.md without changing its surrounding instructions. | [P1 \| I95/E85/R10] | Selected; no proposal is applied by this package. |
| C — Only document the defect | Leave the implementer to reconstruct every link correction. **Example:** Operator approval still requires another design pass to determine the replacement path. | [P1 \| I45/E70/R10] | Insufficiently concrete for this assignment. |

**Recommendation: B.** Each correction is reviewable, bounded and anchored to authenticated current bytes. The correct governance-schemas relative link is explicitly retained.

**Reasoning and trade-off:** A changed source hash invalidates the exact proposal and requires reinspection. **Primary failure:** A stale patch matches unintended text or introduces a link based on a guessed owner.

**Evidence:** `AGENTS.md Informatics & Knowledge Routing`; `apex-meta/informatics/final/specs/standard.md`; `apex-meta/informatics/final/specs/execution-modes/patch-discipline.md`; `apex-meta/informatics/final/specs/governance-schemas.md GS-02,GS-09`. Current scoped source/assignment evidence applies; no external capability claim is needed.

**Affected components:** `design/pointer-patch-proposals.json`, `design/integration-map.json`. **Stage:** S1.

**What would change this choice:** A later revision has already fixed the pointer, or new source authority changes the intended destination.

<a id="d-19"></a>

## D-19 — Use current retrieval policy with authenticated fallback

**Question:** What if QMD is absent, stale or semantically over-triggered? **New question estimate:** (I85/E70/R25).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** DEC-QMD-01..06 own current Windows search behavior; the skill body adds a conceptual-query exception not present in the stricter owner.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Require QMD for every task | Block online processors or load all indexed material by default. **Example:** An authenticated GitHub source is available but work stops because local search is missing. | [P1 \| I30/E30/R60] | Reject; user explicitly permits targeted online retrieval. |
| B — Owner-scoped retrieval, direct source validation | For the current Windows profile, keyword first and hybrid only after zero hits; otherwise use authorized targeted repository search/read. Verify the actual owner revision. **Example:** A source discovered in an old QMD index is re-read at the pinned GitHub revision before it enters the registry. | [P1 \| I90/E70/R20] | Selected; propose only a narrow skill/owner alignment after approval. |
| C — Semantic search as authority | Treat the highest-ranked retrieved passage as current policy. **Example:** A historical candidate outranks the live 23-rule XML in search. | [P1 \| I45/E25/R80] | Reject: retrieval rank is not source authority. |

**Recommendation: B.** QMD is a discovery aid with documented scope and freshness limits. No daemon, new collection or indexing change is needed for this package.

**Reasoning and trade-off:** Direct retrieval can be slower than local search, but avoids claiming unverified local state. **Primary failure:** A plausible historical excerpt is promoted into current truth.

**Evidence:** `apex-meta/informatics/final/operations/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md §2`; `.agents/skills/qmd/SKILL.md §1`; `apex-meta/informatics/final/research/11-infrastructure-evidence-index/03-retrieval-and-gaps.md`. Current scoped source/assignment evidence applies; no external capability claim is needed.

**Affected components:** `03-architecture.md`, `design/integration-map.json`, `evidence/repository-sources.json`. **Stage:** S1.

**What would change this choice:** The owning QMD policy is explicitly changed for a verified WSL or other profile and its trade-offs are accepted.

<a id="d-20"></a>

## D-20 — Repair evaluator meaning before measuring adoption

**Question:** Can the retained evaluators certify activation and useful outcomes? **New question estimate:** (I95/E85/R25).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** DEC-06 requires replacement tests to cover more; target rule distinguishes useful output from shape; retained runner is simulation.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Reuse reported pass flags unchanged | Run the existing graders and accept their total score as adherence. **Example:** A failed validator or empty artifact still receives deterministic pass. | [P1 \| I30/E25/R85] | Reject; executed counterexamples show the proxy is unsound. |
| B — Keep useful fixtures, replace insufficient predicates | Separate applicability, delivery, adherence and outcome; require successful checker execution, nonempty meaningful artifacts and scoped mutation diffs. **Example:** The same typo case fails if an unrelated file changes even when the typo is corrected. | [P1 \| I95/E85/R20] | Selected; new native trials remain unexecuted. |
| C — Manual judgment only | Discard all structural and trace checks. **Example:** A reviewer must manually find a failed JSON parse in every run. | [P1 \| I70/E65/R40] | Reject alone; deterministic evidence remains useful within its measured scope. |

**Recommendation: B.** Synthetic probes establish failure possibility, not invalid historical scores. Existing cases are valuable once their observation contracts are made honest.

**Reasoning and trade-off:** Historical results are not directly comparable to a revised scorer without re-scoring available traces. **Primary failure:** Unknown/missing validator evidence is converted to zero errors.

**Evidence:** `apex-meta/informatics/final/candidates/01-decision-register.md DEC-06`; `apex-meta/informatics/final/tools/agent_eval_runner.py`; `apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py`; `apex-meta/informatics/final/research/08-read-trace-routing-experiments/artifacts/stage1/score_stage1_corrected.py`. External: EEMP-10, EEMP-14.

**Affected components:** `evaluation/scorer_probe.py`, `evaluation/evaluation-plan.md`, `evaluation/cases.json`. **Stage:** S1.

**What would change this choice:** A predicate is independently shown to measure the intended property on positive and adversarial fixtures.

<a id="d-21"></a>

## D-21 — Separate packaging comparisons from hook/reminder causality

**Question:** Which evaluation design can support a mechanism claim? **New question estimate:** (I90/E70/R35).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** Round2 B-AGY combines hooks and reminders; baseline and deliberation arms do not isolate the effect.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — One challenger versus old baseline | Compare the whole new stack against an older configuration and attribute gains to hooks. **Example:** A better reminder is credited to a tool gate. | [P1 \| I50/E40/R65] | Reject for causal attribution; end-to-end comparison may still show package-level usefulness. |
| B — Architecture arms plus a separate factorial | Hold task, model, content, permissions and scoring constant for packaging arms; within the selected packaging vary hook on/off and reminder on/off. **Example:** The same chat ranking and governed spec are observed in all four reminder/hook cells. | [P1 \| I95/E70/R30] | Selected. |
| C — Only token and latency benchmarks | Choose the cheapest configuration without semantic outcomes. **Example:** A concise but incorrect recommendation wins. | [P1 \| I30/E35/R75] | Reject: cost is a separate reported outcome, not the target. |

**Recommendation: B.** This preserves the combined-intervention limitation and distinguishes selection benefit from source-content and enforcement benefit. Balanced ordering and repeated fresh sessions limit carryover.

**Reasoning and trade-off:** More trials are required; no sample count alone guarantees external validity. **Primary failure:** Model drift, unbalanced context or shared state confounds the apparent treatment effect.

**Evidence:** `apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md`; `apex-meta/informatics/final/research/10-ultra-upgrade-validation/preregistration.md`; `apex-meta/informatics/final/research/08-read-trace-routing-experiments/01-findings-and-protocol.md`. External: EEMP-02, EEMP-05, EEMP-06, EEMP-14.

**Affected components:** `evaluation/evaluation-plan.md`, `evaluation/cases.json`, `examples/architecture-comparison.md`. **Stage:** S2.

**What would change this choice:** The operator chooses a narrower practical outcome question, in which case report package-level association without mechanism attribution.

<a id="d-22"></a>

## D-22 — Preserve raw priorities and separate all scoring concepts

**Question:** How are original priorities, new estimates, reading ranks and empirical reliability represented? **New question estimate:** (I90/E70/R15).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** WP-07 owns unaggregated I/E/R; GS-04 delegates; old NVS and bake-off criterion weights have distinct provenance.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — One composite rank | Aggregate I/E/R, source count and reading rank into a single confidence score. **Example:** An easy-to-read source with many citations outranks a contradictory live owner. | [P1 \| I35/E20/R75] | Reject: violates raw metric meaning and creates false precision. |
| B — Separate preserved and estimated dimensions | Retain exact authored tags; store null for unscored source rules; label this matrix’s values as new judgments; report empirical counts separately. **Example:** XML.authoring inherits no invented WP-07 score; WP-07 retains its original raw tag. | [P1 \| I95/E70/R10] | Selected. |
| C — Discard all numeric tags | Replace recorded values with vague high/medium/low confidence. **Example:** The operator loses original I/E/R distinctions and historical comparability. | [P1 \| I50/E45/R35] | Reject for source fidelity. |

**Recommendation: B.** Never aggregate I/E/R into a sum, weighted product or NVS. When the EM-07/GS-13 bake-off trigger applies, retain its four phases and separate weighted criterion matrix. The architecture comparison supplies that rubric with explicitly estimated criterion values; it does not convert them into empirical reliability or rule authority.

**Reasoning and trade-off:** Reviewers must interpret multiple dimensions instead of one seductive number. **Primary failure:** A new estimate is mistaken for a source-authored value or measured probability.

**Evidence:** `apex-meta/informatics/final/specs/writing-profile.md WP-07`; `apex-meta/informatics/final/specs/governance-schemas.md GS-04`; `apex-meta/informatics/final/specs/execution-modes/bake-off.md §§3.1,3.2`; `apex-meta/informatics/final/research/09-ultra-contract-and-layers-synthesis/index.md`. External: EEMP-06.

**Affected components:** `registry/rules.json`, `registry/history.json`, `design/decisions.json`, `02-decisions.md`, `examples/architecture-comparison.md`. **Stage:** S1.

**What would change this choice:** The operator approves a change to the owning bake-off rubric or a distinct criterion model. Current mandatory criterion comparison and original raw I/E/R remain separate until then.

<a id="d-23"></a>

## D-23 — Resolve authorization conflicts without automatic persistence

**Question:** How do align, sync and handover apply to this read-only continuous run? **New question estimate:** (I95/E70/R20).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** Current operator authorization outranks source prompts; EM-14 scopes persistence; root Git Dispatch ignores unrelated dirty files.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Literal isolated command execution | Wait, stage unrelated files, push or install because a quoted source says to do so. **Example:** A research task modifies main despite the operator’s explicit prohibition. | [P1 \| I10/E10/R100] | Reject. |
| B — Current scoped authorization controls actions | Complete the requested package; record conflicts; make later repository mutations contingent on specific approval and fresh scope verification. **Example:** Deliver one ZIP without a branch, commit or deployment. | [P1 \| I100/E70/R5] | Selected. |
| C — Treat every ambiguity as a stop | Pause for confirmation on routine file grouping and research choices. **Example:** The package stops after an inventory instead of creating reviewable artifacts. | [P1 \| I35/E25/R50] | Reject: current assignment authorizes autonomous routine design work. |

**Recommendation: B.** The original domain meaning is preserved while the operator’s present task boundary determines what may execute. Silence is not deployment approval.

**Reasoning and trade-off:** Some compressed owner wording still needs explicit reconciliation in a later authorized change. **Primary failure:** Historical execution prose is promoted to current authorization.

**Evidence:** `AGENTS.md Git Dispatch`; `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml <align>,<sync>,<handover>`; `apex-meta/informatics/final/specs/execution-modes/handover.md EM-14`; `apex-meta/informatics/final/specs/execution-modes/qa-decision-matrix.md EM-06a`. Current scoped source/assignment evidence applies; no external capability claim is needed.

**Affected components:** `00-START-HERE.md`, `design/integration-map.json`, `evaluation/evaluation-plan.md`. **Stage:** S0.

**What would change this choice:** The operator explicitly authorizes a subsequent scoped installation or repository persistence task.

<a id="d-24"></a>

## D-24 — Keep SDK, hosted and bare surfaces as explicit profiles

**Question:** Can local interactive capability claims be reused in automation and cloud? **New question estimate:** (I90/E70/R45).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Retained audits mix surfaces; current Codex profiles, MCP server removal and Claude bare mode change automation assumptions.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Assume CLI parity | Use one invocation recipe for local, cloud, SDK and bare operation. **Example:** A Claude --bare job is expected to discover the same hooks and skills as normal print mode. | [P1 \| I30/E25/R80] | Reject. |
| B — Separate capability profiles and boot contracts | Declare surface, version, roots, settings, trust, permission mode, event coverage and durable-history behavior before interpreting traces. **Example:** Codex exec --json gives event evidence but structured output alone does not prove correct behavior. | [P1 \| I95/E70/R20] | Selected. |
| C — Exclude all automation surfaces | Limit the package to interactive CLI forever. **Example:** A future approved headless run has no reproducible startup contract. | [P1 \| I55/E70/R25] | Too narrow; supply unexecuted probes rather than unsupported parity claims. |

**Recommendation: B.** Documented migrations and scope differences change concrete configuration. They do not imply the operator upgraded or migrated a profile.

**Reasoning and trade-off:** The compatibility matrix is larger and must be maintained by surface. **Primary failure:** A successful exit code masks a soft-denied action or an unloaded customization.

**Evidence:** `apex-meta/informatics/final/research/01-universal-instruction-research/05-INSTRUCTION-ACCESS-AND-SERIALIZATION-MATRIX.md`; `apex-meta/informatics/final/research/11-infrastructure-evidence-index/07-current-web-research.md`. External: EXT-OAI-05, EXT-OAI-06, EXT-OAI-08, EXT-OAI-10, EXT-CLAUDE-09, EXT-AGY-07, EXT-CLAUDE-11, EXT-CLAUDE-12, EXT-CLAUDE-13, EXT-AGY-12, EXT-AGY-13.

**Affected components:** `compatibility/compatibility.md`, `compatibility/probe-plan.json`, `examples/native/`. **Stage:** S1.

**What would change this choice:** A provider documents and a probe confirms a common contract for the relevant profiles.

<a id="d-25"></a>

## D-25 — Defer plugins, MCP policy services and model/hardware selection

**Question:** Which adjacent infrastructure choices are material now? **New question estimate:** (I85/E65/R30).

**Review depth:** L2-style autonomous review presentation; not a claim of a completed interactive EM-06a session.

**Original position and scope:** Q003/Q005 stage project skills before plugins/MCP policy; Hermes D06/D09/D10 and local LM decisions retain separate scope and deferrals.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Adopt a platform plugin and memory/model stack now | Bundle routing, connectivity, state and provider choice into one deployment. **Example:** A rule activation improvement turns into a new local-model and scheduler project. | [P1 \| I65/E35/R80] | Reject for this package’s implementation scope. |
| B — Define interfaces; defer unproven infrastructure | Use files/native skills and existing tools; revisit plugins for distribution only after a shared-source pilot, and model/runtime choices under their own locks. **Example:** A later plugin may carry the same verified workflow without becoming its semantic owner. | [P1 \| I95/E70/R15] | Selected. |
| C — Prohibit plugins or MCP permanently | Freeze a file-only design even if supported distribution becomes simpler. **Example:** A future maintained native package cannot replace manual copies. | [P1 \| I50/E35/R30] | Reject as unnecessary rigidity. |

**Recommendation: B.** Connectivity is not doctrine, a plugin is not evaluation, and local hardware does not determine rule authority. Keeping these choices separate prevents accidental scope expansion.

**Reasoning and trade-off:** Potential distribution conveniences are postponed until justified by actual friction. **Primary failure:** The infrastructure design is used as implicit approval for an unrelated platform migration.

**Evidence:** `apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md Q003,Q005`; `apex-meta/epics/hermes-multi-repo-orchestration-v2/DECISIONS.md D06,D09,D10`; `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`. External: EEMP-07, EEMP-13, EXT-OAI-02.

**Affected components:** `03-architecture.md`, `design/integration-map.json`, `evaluation/evaluation-plan.md`. **Stage:** S4.

**What would change this choice:** A measured deployment problem and explicit operator authorization justify a separate bounded integration.

<a id="d-26"></a>

## D-26 — Adopt by dependency-aware stages and rollback evidence

**Question:** What can be approved next without approving the whole architecture at once? **New question estimate:** (I95/E65/R45).

**Review depth:** L3 deployment review flagged; this continuous-run artifact is an autonomous decision presentation, not a completed interactive EM-06a session.

**Original position and scope:** Current assignment is review-only; D05 requires pilot/promotion gates; existing authority-state code enforcement remains open.

| Option | Mechanism and illustrative Apex grounding | New raw estimate | Disposition |
|---|---|---|---|
| A — Deploy the complete proposal in one pass | Install registry, skills, hooks and new carriers across repositories together. **Example:** A failure cannot be isolated to routing, loading, permissions or source drift. | [P1 \| I55/E30/R90] | Reject. |
| B — Scoped approval and evidence gates | Repair source/measurement defects, probe one profile, pilot one workflow, then add a justified guard and expand only after outcome evidence. **Example:** A pilot can be removed by restoring captured pre-change bytes without touching unrelated skills. | [P1 \| I95/E70/R20] | Selected. |
| C — Another abstract research handover | Ask for a new design run before producing concrete changes or cases. **Example:** The operator must reconstruct integration choices again. | [P1 \| I20/E20/R45] | Reject: this package provides the concrete design and review decisions now. |

**Recommendation: B.** Stages expose dependencies and isolate failures. The next operator action is to approve a concrete bounded slice, not to authorize an unknown universal installer.

**Reasoning and trade-off:** Full rollout is slower than a single broad change, but rollback and attribution remain tractable. **Primary failure:** A completed structural check is treated as installation acceptance or authority promotion.

**Evidence:** `apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D05-SHARED-SKILL-SOURCE.md`; `apex-meta/orchestration/schemas/authority-state.schema.md §§8,9`; `apex-meta/informatics/final/specs/execution-modes/task-specification.md`. External: EXT-OAI-01, EEMP-14.

**Affected components:** `evaluation/evaluation-plan.md`, `design/integration-map.json`, `00-START-HERE.md`, `07-validation-report.md`. **Stage:** S0.

**What would change this choice:** A stage lacks a material risk or adds no information; remove that ceremony rather than adding another gate.

## Failure guard

Do not promote a proposal on the strength of a score. Preserve original source meaning, review the actual outcome, and authorize the specific implementation slice before live changes.
