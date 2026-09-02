---
type: Review
title: Apex Informatics Post-W2 Wiring Verification
description: Adversarial static verification of routing, agent/Skill wiring, standards references, cross-client instruction surfaces, and representative cold-start requests after W0-W2/A1-A2 implementation.
tags: [apex, informatics, verification, agents, routing, okf]
generated: { by: openai/gpt-5.6-sol, at: 2026-09-02T07:02:00Z }
status: current
---

# Apex Informatics Post-W2 Wiring Verification

## Verification basis

```yaml
repository: leela-spec/apexai-os-meta
branch: main
verified_head: c140f3679107722e66b812320b62de5dc247ed3b
implementation_commit: 64b68f1bbac57a481c3178f32614c7d6cf8a3c70
mode: static_adversarial_verification
live_target_mutations: none
```

This review traces the current repository surfaces as a cold-start agent would encounter them. It does not claim to be an actual spawned Claude/Cursor/Kiro/Windsurf/Hermes session. Runtime-only behavior must still be confirmed in each host after the patches are applied.

# Executive verdict

**The canonical Apex routing architecture is substantially correct, but the post-W2 system is not fully wired across runtimes.**

The strongest parts are:

- `.claude/CLAUDE.md` correctly exposes exactly two orchestration systems plus the shared Plan-Sync-Session backbone.
- the seven live Multi-Agent Orchestration role definitions resolve and match `CURRENT-SYSTEM-MANIFEST.yaml`;
- `apex-plan`, `apex-sync`, and `apex-session` remain cleanly separated by proposal / deterministic computation / confirmed mutation;
- the Weekly Orchestrator controller points to the correct six stage Skills plus two retained reviewer agents;
- the Copilot repository-wide and informatics-scoped instruction split is structurally sound.

The highest-impact defects are:

| Priority | Defect | Consequence |
|---|---|---|
| **P0** | Six Weekly stage Skills describe forked execution only inside their Markdown bodies; they do not declare `context: fork` in Skill frontmatter. | Claude Code can run the stage inline even though the controller says stage isolation is mandatory. |
| **P0** | Cursor, Kiro, Windsurf, and `.agent/rules/obsidian-wiki.md` still load a false Obsidian-Wiki project identity globally. | A normal Apex request can begin from the wrong product model and wrong skill routes. |
| **P0** | `okf_validator.py` encodes non-OKF requirements as upstream OKF failures and skips nested directories containing `index.md`. | The validator can both reject valid OKF and miss invalid concepts below progressive-disclosure indexes. |
| **P1** | `.claude/rules/informatics.md` has no `paths:` frontmatter. | Informatics instructions load in every Claude session instead of only the governed paths. |
| **P1** | `standard.md` says `index.md`, `log.md`, `title`, `description`, and `okf_version` are universal OKF MUSTs. | The canonical Apex standard contradicts the upstream OKF spec and its own local conformance reference. |
| **P1** | Weekly Macro/Meso documents still describe six wrapper agents that no longer exist. | A cold-start maintenance agent can chase nonexistent `.claude/agents/apex-*` paths and conclude the working system is degraded. |
| **P1** | `.hermes.md` is a pre-informatics copy of the root operating rules. | Hermes can miss the canonical informatics route and diverge from current shared policy if this file is active in the Hermes host. |
| **P2** | Macro/Meso/Micro terminology is reused for three different meanings. | Unqualified requests such as “check the Meso file” are ambiguous to an agent. |
| **P2** | Root `CLAUDE.md` duplicates `AGENTS.md` byte-for-byte while `.claude/CLAUDE.md` is the actual Apex activation router. | Possible duplicate startup context and future drift; runtime `/memory` evidence is required before changing this surface. |
| **P2** | Three optional wrapper agents (`apex-plan-ops`, `apex-sync-ops`, `apex-kb-operator`) exist outside the live Multi-Agent manifest and have no repository references. | Directory discovery can make them look like normal/default routes even though current routers do not use them. |

# 1. Core routing and agent wiring

## 1.1 APEX OS activation router

Current `.claude/CLAUDE.md` correctly states:

```text
APEX OS
├── Weekly Orchestrator
├── Multi-Agent Orchestration
└── shared Plan-Sync-Session Backbone
```

It also explicitly forbids implicit cross-system activation. **PASS.**

## 1.2 Multi-Agent Orchestration

Current manifest roles:

| Role | Runtime definition | Static wiring | Design judgement |
|---|---|---:|---|
| Alfred | `.claude/agents/alfred.md` | PASS | operator-facing intake/gates are separated from strategy and execution |
| Meta Strategy | `.claude/agents/meta-strategy.md` | PASS | bounded direction role; read-only |
| Meta Ops | `.claude/agents/meta-ops.md` | PASS | main-thread integration and sole run-scoped backbone invoker |
| Meta Detective | `.claude/agents/meta-detective.md` | PASS | independent review role |
| Knowledge Bank | `.claude/agents/knowledge-bank.md` | PASS | bounded specialist |
| Informatics Design | `.claude/agents/informatics-design.md` | PASS | bounded specialist |
| Prompts Workflows | `.claude/agents/prompts-workflows.md` | PASS | bounded specialist |

The doctrine manifest and `00-START-HERE.md` use progressive disclosure rather than preloading every doctrine file. **PASS.**

The optional `.claude/agents/apex-plan-ops.md`, `apex-sync-ops.md`, and `apex-kb-operator.md` are not referenced by the live manifest or current repository search. Treat them as optional compatibility/execution wrappers, not normal routing targets, until explicit use evidence proves otherwise.

## 1.3 Plan-Sync-Session backbone

| Capability | Owns | Must not own | Verdict |
|---|---|---|---|
| `apex-plan` | project capture, decomposition, proposal | deterministic exact-next computation, confirmed mutation | PASS |
| `apex-sync` | deterministic read-side reports/synchronization | planning authorship, confirmed mutation | PASS |
| `apex-session` | confirmed state/session mutation and handoff | planning decomposition, deterministic priority computation | PASS |

No material boundary collision was found.

## 1.4 Weekly Orchestrator

The live controller correctly names six stage Skills and two reviewer agents. The two reviewer definitions exist. The six stage Skills also exist.

**Runtime isolation FAIL:** the controller says each stage Skill declares `context: fork` on the Skill itself, but the six Skill frontmatter blocks currently contain only `name` and `description`. Their body-level `skill_contract.execution.context` fields are documentation, not Claude Code runtime configuration.

Affected Skills:

```text
.claude/skills/PrecapWeek/SKILL.md
.claude/skills/PrecapNextDay/SKILL.md
.claude/skills/raw-flow-dump-normalize/SKILL.md
.claude/skills/flow-recap/SKILL.md
.claude/skills/status-merge/SKILL.md
.claude/skills/ProjectStatus/SKILL.md
```

Patch: `PATCH-03-weekly-runtime-and-topology.md`.

# 2. Static request simulations

These simulations follow current routing documents and host rules. “Clarify” means the current architecture genuinely has more than one valid owner and one short clarification is preferable to guessing.

| Test request | Expected handoff | Current result | Clarification needed? |
|---|---|---|---|
| `Run the Weekly Orchestrator.` | `.claude/CLAUDE.md` → `weekly-orchestrator` → current stage Skill | **PARTIAL FAIL**: route correct; fork isolation not actually declared | only missing week/run scope required by selected stage |
| `Run Precap Week for next week.` | `PrecapWeek` | **PARTIAL FAIL**: correct owner; can execute inline today | week ID/date if not inferable from explicit run context |
| `Start Multi-Agent Orchestration for this architecture problem.` | `00-START-HERE.md` → Alfred/Meta Ops → bounded specialist/review | **PASS** | only source/task scope that cannot be inferred |
| `Create a project from these notes.` | `apex-plan` | **PASS** | only genuinely missing project identity/goal |
| `What is my exact next task?` | `apex-sync` | **PASS** | project/scope when multiple current scopes are possible |
| `Mark TASK-123 done and create the handoff.` | `apex-session` | **PASS** | required evidence/confirmation if absent |
| `Create an OKF concept in the informatics bundle.` | informatics route → authoring Skill → standard → validator | **PARTIAL FAIL**: right route; standard and validator overstate OKF requirements | target bundle if not named |
| `Fix this unrelated Python bug.` | normal repository/code path | **FAIL (context economy)**: `.claude/rules/informatics.md` currently loads globally | no |
| `Run the orchestration.` | exactly two orchestration systems are valid | **CORRECT STOP** | **yes: Weekly or Multi-Agent?** |
| `Plan this project and then tell me the exact next actions.` | `apex-plan` → after accepted state, `apex-sync` | **PASS** | project/scope if ambiguous |
| `Show the historical rationale for rule X.` | current owner first → evidence/history on demand | **PASS** | rule/source only if X is ambiguous |
| `Check the Meso file.` | multiple namespaces currently use “meso” | **AMBIGUOUS** | **yes: Weekly Meso architecture, Multi-Agent workflow integration, or document-level informatics analysis?** |
| `Apply the project principles.` | no canonical `PROJECT-PRINCIPLES.md` exists | **AMBIGUOUS** | **yes: repository-wide `AGENTS.md` invariants or a named system/project doctrine?** |
| `Update project status.` | could mean derived `ProjectStatus` overview or durable task mutation | **AMBIGUOUS** | **yes: overview only, or confirmed state mutation via Session?** |
| `Create an Apex knowledge base.` | `apex-kb` | **PASS** | normal Start-route inputs only |
| Cursor/Kiro/Windsurf: `Fix a normal code issue.` | shared Apex routing | **FAIL**: always-on rule says the whole repo is an Obsidian Wiki framework | no; this is configuration drift |

# 3. Standard reference audit

The four current references at the end of `apex-meta/informatics/standard.md` are not equivalent authorities.

| Reference | Alignment with adopted architecture | Disposition |
|---|---|---|
| `SmallSkills/OKF_Format/conformance-rules.md` | **High.** It correctly states the minimal upstream OKF conformance bar and consumer tolerances. | Retain, but the standard must stop contradicting it. |
| `informatics-design-formats-practice-guide.md` | **Useful but scoped.** It explicitly says its source rules originated in Skill-package authoring and may not universally apply to KB pages. | Retain as supporting synthesis, not normative foundation. |
| `token-efficient-information-design.md` | **High.** Its catalog-first / refs-not-copies / load-on-demand conclusions match the new profile. | Retain as supporting synthesis. |
| Weekly `informatics-design-doctrine.md` | **Wrong dependency direction for the base standard.** It is an authoritative doctrine for one Weekly role, not an Apex-wide source. | Remove from base-standard references; make Weekly doctrine conform to/reference the canonical informatics standard instead. |

The reference section should distinguish:

```text
normative upstream standards
→ runtime/vendor specifications
→ local grounded references
→ supporting research/synthesis
```

Patch: `PATCH-01-informatics-scope-and-standard.md`.

# 4. Macro / Meso / Micro and “project principles”

## 4.1 Weekly Macro and Meso

The Weekly architecture files are understandable as historical decision artifacts, but their topology is stale:

- Macro says every stage is a named `.claude/agents/` subagent that preloads a Skill.
- Meso lists six nonexistent stage-agent files and declares path failure to mean the system is degraded.
- The live controller now intentionally uses six direct forked stage Skills and only two named reviewer agents.

The correct repair is to update Macro/Meso to the live topology. **Do not recreate the removed wrapper agents.**

## 4.2 “Micro”

No canonical Weekly `Micro` execution file was found. The word also appears in a separate informatics summary where Macro/Meso/Micro mean package/document/rule granularity. Treating “Micro” as a global Apex tier would therefore be invented semantics.

## 4.3 Multi-Agent usage of macro/meso

`meta-strategy.md` calls itself “macro-direction” and `meta-ops.md` calls itself “meso-workflow.” Those labels are understandable to a human who knows the history but collide with the Weekly artifact names and the informatics guide.

Recommended vocabulary:

```text
Meta Strategy → strategic direction
Meta Ops      → workflow integration
Informatics   → package / document / rule levels
Weekly        → Weekly Macro / Weekly Meso (proper artifact names)
```

## 4.4 Project principles

No canonical `PROJECT-PRINCIPLES.md`, `Project Principles`, or equivalent current owner was found.

Do not create another principle document merely because the phrase is convenient. Current durable principles already have owners:

- repository-wide execution/scope/safety → `AGENTS.md`;
- orchestration-system topology/authority → selected orchestration entrypoint/architecture;
- role doctrine → selected role domain;
- informatics rules → `apex-meta/informatics/standard.md`.

If “project principles” is used without a named project/system and those owners would yield different answers, the agent should ask one clarification rather than invent a global artifact.

Patch: `PATCH-04-terminology-and-ambiguity.md`.

# 5. Cross-client instruction audit

| Surface | Current state | Verdict |
|---|---|---|
| `AGENTS.md` | current shared Apex invariants + informatics route | PASS, though Apex-KB patch procedure is still heavier than ideal for a universal file |
| `.claude/CLAUDE.md` | current Apex activation router | PASS |
| `.claude/rules/informatics.md` | correct content, missing path scope | FAIL |
| `.github/copilot-instructions.md` | compact current adapter | PASS |
| `.github/instructions/informatics.instructions.md` | correct `applyTo` path scope | PASS |
| `.cursor/rules/obsidian-wiki.mdc` | always-on obsolete project identity | FAIL |
| `.kiro/steering/obsidian-wiki.md` | always-on obsolete project identity | FAIL |
| `.windsurf/rules/obsidian-wiki.md` | always-on obsolete project identity | FAIL |
| `.agent/rules/obsidian-wiki.md` | always-on obsolete project identity | FAIL |
| `.hermes.md` | old root rule copy; lacks informatics routing | FAIL/CONDITIONAL on Hermes host loading this file |
| root `CLAUDE.md` | byte-copy of `AGENTS.md` | CONDITIONAL improvement; inspect `/memory` before changing |

Patch: `PATCH-05-cross-client-instruction-drift.md`.

# 6. Validator correctness

The current validator has four architectural failures:

1. It calls missing root `index.md` and missing `okf_version` upstream `OKF_ERROR`s even though OKF v0.2 makes both optional.
2. Its hand-written colon-splitter is not a YAML parser and cannot verify arbitrary parseable YAML frontmatter.
3. It treats every nested directory containing `index.md` as a separate bundle and skips the whole subtree. OKF explicitly permits nested `index.md` files for progressive disclosure inside one bundle.
4. It skips `log.md` and nested `index.md` structural validation entirely.

The current tests encode the first defect (`test_red_missing_root_index`) and lack regressions for nested indexed subdirectories and reserved log files.

Patch: `PATCH-02-okf-validator-correctness.md`.

# 7. High-impact improvement order

```yaml
apply_first:
  - PATCH-03-weekly-runtime-and-topology.md
  - PATCH-05-cross-client-instruction-drift.md
  - PATCH-02-okf-validator-correctness.md
then:
  - PATCH-01-informatics-scope-and-standard.md
  - PATCH-04-terminology-and-ambiguity.md
conditional_after_runtime_evidence:
  - root_CLAUDE_deduplication
later_not_now:
  - skill_directory_case_normalization
  - cross-client_skill_canonicalization
  - broad historical_OKF_retrofit
  - RAG_or_vector_retrieval
```

# 8. Acceptance checks after applying the patch pack

1. In Claude Code, `/memory` shows `informatics.md` only when a matching governed path is active, not on unrelated work.
2. Invoke each of the six Weekly stage Skills and confirm it opens an isolated fork rather than doing stage work in the main thread.
3. Run one Weekly flow through stage dispatch → return envelope → gate without any reference to the removed wrapper agents.
4. Run the OKF validator against a bundle with no index; upstream OKF conformance must remain valid, while Apex Profile may flag the local missing-index policy if the target is governed.
5. Put a valid concept beneath `subdir/index.md`; the validator must inspect it.
6. Put malformed real YAML in a concept; a real YAML parser must reject it.
7. Open Cursor, Kiro, Windsurf, the generic `.agent` host, and Hermes on an unrelated Apex task; none should introduce the repo as an Obsidian Wiki product.
8. Ask `run the orchestration`; the agent asks Weekly vs Multi-Agent rather than guessing.
9. Ask `check the Meso file`; the agent disambiguates or uses an explicitly named Weekly context.
10. Ask `apply project principles`; the agent resolves a named owner or asks which project/system rather than inventing a `Project Principles` authority.

# Scope guard

This verification does not recommend:

- recreating the six removed Weekly wrapper agents;
- adding a global Macro/Meso/Micro framework;
- adding a new Project Principles SSOT;
- migrating archives/history;
- introducing RAG or embeddings;
- normalizing every mirrored Skill name in this pass.
