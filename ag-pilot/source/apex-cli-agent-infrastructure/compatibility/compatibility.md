---
type: Reference
id: APEX-CLI-COMPAT-20261112
title: Codex, Claude Code, Antigravity, and Gemini CLI compatibility
description: Current primary-source capability contracts by platform and surface, with explicit installed-version probes and inert examples.
status: proposed
retrieved_on: 2026-11-12
installed_verification: not_executed
---

# Cross-platform activation findings

## Design conclusion

Share rule identity, domain meaning, evidence, and skill resources. Adapt instruction discovery, invocation controls, native agent metadata, hook envelopes, permissions, and recovery for each platform **and surface**. A portable Markdown skill does not provide a portable execution contract.

This conclusion is a design inference from the opened official sources catalogued in `sources.json`; `claims.json` contains the individual capability claims and version conditions. No native adapter behavior, account capability, permission state, or adherence improvement was measured. A research-container Codex version fingerprint is recorded separately in `environment-observation.json`; it is not an operator-workstation observation. Current documentation was opened on 12 November 2026. Release notes are observations of published versions, not a claim that the workstation uses them.

The repository research brief already identifies the missing lifecycle as rule → trigger → activation → delivery → execution → verification. It explicitly keeps all-reference-as-skill packaging in the comparison. The proposed adapters below close platform-specific gaps; they do not resolve domain-rule meaning or authorize migration. Internal sources read: `apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md` §§1–4 and `apex-meta/informatics/final/research/11-infrastructure-evidence-index/07-current-web-research.md` §§Findings and Limits.

## Capability comparison

Every cell is **documented / installed-unverified** unless stated otherwise. Claim IDs refer to the machine-readable register, which resolves direct public URLs and precise reviewed sections.

| Mechanism | Codex local | Claude Code local | Antigravity | Gemini CLI |
|---|---|---|---|---|
| Guidance | Launch AGENTS chain, P-OAI-01 | CLAUDE plus conditional AGENTS, P-CLA-01/02 | Root/ancestor rules, P-AG-01/02 | GEMINI ancestry, P-GEM-01 |
| Procedure | `.agents/skills`, P-OAI-02 | `.claude/skills`, P-CLA-03 | `.agents/skills`, P-AG-04/05 | `.gemini/skills` / alias, P-GEM-02 |
| Chat delivery | Prompt event, P-OAI-03 | Prompt event, P-CLA-05 | Invocation event, P-AG-07 | BeforeAgent, P-GEM-03 |
| Tool checks | P-OAI-04/05 | P-CLA-06 | P-AG-06/07 | P-GEM-03 |
| Role definition | TOML, P-OAI-09 | Markdown, P-CLA-07 | Markdown, P-AG-08/09 | Markdown, P-GEM-04 |
| Policy | P-OAI-07/08/12 | P-CLA-08/09/10 | P-AG-10 | P-GEM-05 |
| Automation | P-OAI-10/11 | P-CLA-11/13/14 | P-AG-11/15 | Independent CLI profile |
| Version evidence | P-OAI-13 | P-CLA-15 | P-AG-14 | P-GEM-06 |

The IDs resolve precise facts, scopes and probes in `claims.json`. Every platform uses the same proposed rule identities and evaluation oracle; none shares an unqualified hook or permission schema.
Sources: [Codex guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex hooks](https://learn.chatgpt.com/docs/hooks), [Claude memory](https://code.claude.com/docs/en/memory), [Claude skills](https://code.claude.com/docs/en/skills), [Antigravity discovery](https://antigravity.google/docs/customization-discovery), [Antigravity hooks](https://antigravity.google/docs/hooks), [Gemini memory](https://geminicli.com/docs/cli/gemini-md/), [Gemini hooks](https://geminicli.com/docs/hooks/reference/).

## Codex support contract

The current reference is published CLI **0.167.2**; the research container reports **0.167.0-alpha.4**. Neither establishes the operator installation. Source version, observed runtime version and tested adapter version are separate fields. [Changelog](https://learn.chatgpt.com/docs/changelog).

| Component | Proposed treatment | Authoritative detail |
|---|---|---|
| Instruction and skill discovery | Native entrypoint plus bounded route descriptions; catalog omissions are observable failures | EXT-OAI-02/03, P-OAI-01/02 |
| Lifecycle delivery | Use supported events; diagnostic events are not a fallback delivery path | EXT-OAI-01, P-OAI-03 |
| Hook enforcement | Declare event/tool coverage and degraded mode; keep host controls independent | P-OAI-04/05/06 |
| Configuration | Inspect effective layers and migrate obsolete syntax only after approval | [Config](https://learn.chatgpt.com/docs/config-file/config-basic), [profiles](https://learn.chatgpt.com/docs/config-file/config-advanced), [reference](https://learn.chatgpt.com/docs/config-file/config-reference) |
| Agent isolation | Separate reviewer role from actual inherited authority | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) |
| SDK and automation | Optional native harness integration; capture invocation and outcomes | [Headless](https://learn.chatgpt.com/docs/non-interactive-mode), [SDK](https://learn.chatgpt.com/docs/codex-sdk) |
| Execution policy | Keep command approval logic outside the Apex domain registry | [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules), [security](https://learn.chatgpt.com/docs/agent-approvals-security) |

`native-schemas/codex/` preserves five release-specific wire schemas and blob provenance. The offline fixtures demonstrate a consequential distinction: JSON validity alone cannot certify a hook's intended effect. Review the semantic negatives beside the valid delivery/denial samples in `../examples/native/codex-hook-fixtures.json`. These are package checks, not Codex execution measurements.

## Material release and interpretation changes

| Issue | Earlier assumption or misleading evidence | Current disposition | Package consequence |
|---|---|---|---|
| Codex historical configs | Legacy profiles, untrusted approval value, full-auto or MCP-server recipes | P-OAI-07/08/10/11 record current migrations | Flag existing recipes; do not auto-migrate live policy |
| Claude AGENTS support | A legacy bridge is always required, or root AGENTS always loads | Version, ancestor files and built-in plugin policy determine loading (P-CLA-02) | Retain a minimal explicit `@AGENTS.md` import where compatibility requires it; remove duplicate hook injection only after probe |
| Claude repository bypass setting | Repository text proves bypass mode | Key nesting and allowed scope matter (P-CLA-09) | Record source text separately; inspect effective runtime settings before any proposed permission change |
| Claude headless equivalence | All `-p` invocations load the same customizations | Bare mode explicitly changes discovery and authentication (P-CLA-11) | Invocation flags belong in the compatibility fingerprint |
| Antigravity descendant rules | Cached search excerpt says rules load while descendant files are touched | Opened rules/discovery pages state otherwise (P-AG-01) | Root-discovered glob rules or explicit reference route; descendant canary probe mandatory |
| Antigravity old CLI skill shape | Old search result describes loose Markdown skill files | Opened current skills page uses bundles (P-AG-04) | Use `SKILL.md` bundles; preserve old assets until mapping succeeds |
| Antigravity hook location | Old CLI search result says hooks in settings.json | Opened dedicated hook reference explicitly rejects that location (P-AG-06) | Separate hooks.json adapter; permissions still have a settings scope |
| Workflow cutoff | Cached old page names 19 October 2026 | Both opened current IDE workflow and migration pages say existing workflows still work for now | Record deprecation, not an inferred outage; App command does not imply CLI/IDE command parity |
| Gemini to Antigravity | Migration guide broadly calls rules identical | Specific current discovery and schema documentation establishes important differences | Component mapping and probes, not blind folder rename/import |
| Antigravity hook handler types | Current general plugin page mentions prompt evaluations | Dedicated hooks reference documents command handlers only | Ship command-handler examples; prompt handlers remain unsupported by this package pending exact schema proof |
| Process exit success | Exit 0 proves requested action occurred | Antigravity headless may soft-deny actions and exit 0 (P-AG-11) | Score artifact evidence and denials separately |

Primary support: [Claude settings reference](https://code.claude.com/docs/en/settings-reference#permissions-defaultmode), [Claude headless](https://code.claude.com/docs/en/headless), [Antigravity rules](https://antigravity.google/docs/rules), [Antigravity discovery](https://antigravity.google/docs/customization-discovery), [Antigravity skills](https://antigravity.google/docs/skills), [Antigravity hooks](https://antigravity.google/docs/hooks), [IDE workflows](https://antigravity.google/docs/ide/workflows/), [migration](https://antigravity.google/docs/migration/workflows-to-skills/), [plugins](https://antigravity.google/docs/plugins?tab=cli).

### Repository-observed configuration conflict

The pinned repository file `.claude/settings.json`:1 contains `{"defaultMode":"bypassPermissions"}`. This is **repository-observed configuration text**, not measured host behavior. Current documentation describes `permissions.defaultMode`, and current project-scope acceptance is restricted. Therefore this package must not label the workstation as running bypass mode, nor silently “fix” the key into an active permission escalation. The integration proposal should retain the source, flag the mismatch, and request the operator’s intended local policy as a later deployment decision. A diagnostic is useful immediately; permission mutation is outside this run. [Official setting definition](https://code.claude.com/docs/en/settings-reference#permissions-defaultmode).

## Surface contracts

| Surface | Proposed support posture | Verification required before enabling |
|---|---|---|
| Codex interactive CLI | Primary candidate | Actual binary, cwd chain, catalog, trusted hooks, host permissions |
| Codex IDE / Desktop local | Separate local profiles | Backend version and host settings; do not inherit CLI test results |
| Codex exec / TypeScript SDK | Optional automation profiles | Invocation, dependencies, traces and outcome oracle |
| Work Cloud / local computer access | Separate managed integration | P-OAI-06, account eligibility and policy scope; local adapter ineligible without supported transport |
| Claude interactive CLI | Primary candidate | Version, instruction selection, discovery, hooks, effective permissions, Windows tool IDs |
| Claude normal print mode | Candidate with explicit flags | Discovered catalog, configured hooks, streamed result and refusal handling |
| Claude bare print mode | Separate explicit-input profile | Supply intended inputs; do not assume ambient instruction/skill loading |
| Claude VS Code / Desktop local | Candidate, separate fingerprint | Launch working directory, extension/app version, settings sources, account policy and tool list |
| Claude hosted single-repo outside project threads | Separate cloud profile | Repository settings and server-managed policy actually reaching that session |
| Claude hosted project threads / multi-repo | Limited until per-surface probe | Hook/permission configuration cannot be assumed to transfer from repository or workstation |
| Claude Python / TypeScript SDK | Optional adapter, not required adoption | SDK version plus underlying CLI, setting sources, skill list, callback contracts |
| Antigravity CLI interactive | Primary candidate | Actual `agy` binary/version, customizations, supported events, exact tool list |
| Antigravity CLI headless | Candidate with outcome checks | stderr/refusal capture, machine-readable terminal status, requested artifact existence |
| Antigravity App | Independent candidate | App version, active workspace, customization toggles and permission preset |
| Antigravity standalone IDE | Partial profile | Rules/skills/hooks documented; custom subagent parity requires direct proof |
| Antigravity IDE extensions | Distinct host identity | Identify which backend/session executes work; do not inherit standalone IDE assumptions |
| Antigravity Python SDK | Optional, separate runtime | SDK decorators/state contracts; no assumed hooks.json parity |
| Antigravity managed cloud / remote agent | Unverified deployment profile | Remote environment, mounted files, account policy and available events |
| Gemini CLI | Retained compatibility/migration profile | Actual version, settings trust, enabled skills/hooks and current policies |

Support posture is a **proposal**, not an assertion of current Apex deployment. Official surface evidence: [Claude cloud](https://code.claude.com/docs/en/claude-code-on-the-web), [Claude settings scopes](https://code.claude.com/docs/en/settings), [Claude SDK skills](https://code.claude.com/docs/en/agent-sdk/skills), [Antigravity SDK](https://antigravity.google/docs/sdk/overview/), [Antigravity headless](https://antigravity.google/docs/cli/headless/).

## Proposed lifecycle adapter responsibilities

1. **Discovery:** expose short rule/skill descriptions and a stable route to canonical source. Do not ingest the registry wholesale.
2. **Applicability:** resolve a task’s intent, scope, exclusions and explicit operator correction into selected rule IDs. An exact keyword can support routing but cannot establish task meaning.
3. **Delivery:** encode the selected bounded text and state pointer using the host’s supported context channel. Receipt identifies rule/source hashes, delivery channel and epoch. Receipt is observational, never an authority grant.
4. **Execution:** use the existing CLI harness. A workflow skill controls its procedure; native settings/permissions control tool access. Connectors supply data/actions but do not become domain-rule owners.
5. **Verification:** validate deterministic constraints mechanically; review semantic usefulness independently against original intent. Correlate activation, source-read evidence, result adherence and outcome separately.
6. **Recovery:** compare task identity, source revision, active rules, unresolved decisions and remaining work after resumption or delegation. Re-read changed owners; do not replay old mutation authorization.
7. **Maintenance:** preserve accepted meanings and change adapter mappings only with version evidence. A drift report should identify which capability claim or probe has gone stale.

For Antigravity, repeated pre-invocation reminders need a task/turn hash or equivalent idempotency key. Otherwise the “reliable” mechanism can become an unbounded injection loop. For Claude, a separate check after compaction must not depend on an older skill still being present. Gemini’s pre-compression hook is useful for checkpointing, but cannot prove an interruption checkpoint completed. These are design consequences of P-CLA-04/05, P-AG-07 and P-GEM-03.

### Hook coverage and fallback

A hook adapter owns **a specific event/tool set**, not all agent behavior. Shell wrappers, hosted tools, file mentions, native attachment loading, SDK callbacks and GUI actions can bypass a presumed hook path. A failed or disabled adapter must produce a visible degraded-capability record. Do not continue describing the run as mechanically enforced.

The fallback for a conversational answer is a short native routing instruction plus explicit invocation when needed, followed by result evaluation. The fallback for a critical mutation is existing host permissions and an independently runnable precondition/postcondition check; where the precondition cannot be enforced, that surface is not eligible for that mutation profile. Narrow correction requests should replace only the corrected rule selection, not restart the full workflow. Trivial greetings and explanations of quoted trigger words should produce no workflow activation.

## Native examples and boundaries

The `../examples/native/` files are inert candidates under this package, not in any active customization directory. They deliberately avoid broad permission grants, API harness adoption, shell-command execution, network access and auto-installation. The Python encoders only transform fixture input to documented hook response shapes; it cannot validate a real task’s semantic compliance. `probe-plan.json` supplies executable conditions for later authorized host testing. Offline encoder checks must be labelled **simulation / shape-only**, never measured platform adherence.

The operator may choose the all-reference-as-skills alternative, native-rules-first alternative, or minimal existing-system improvement. This research does not pre-approve a hybrid. Its contribution is a precise compatibility constraint: whichever packaging wins, delivery and verification require platform-specific implementation and outcome evidence.

## Access and evidence limitations

- No operator Windows host, installed-version inventory, effective configuration stack, account settings or live transcript was available. The separate research-container fingerprint is not operator evidence.
- Vendor docs describe current behavior; minima are recorded only when explicitly documented. No release number was inferred for a feature with no minimum stated.
- Search cache contradictions were resolved by opening canonical pages. The older claims remain discovery history, not current support.
- Latest visible release notes do not prove latest distributable binaries or account availability. Gradual rollout can produce mixed installations.
- No benchmark or ablation of activation quality was run here. The findings and evaluation artifacts own retained experiment appraisal and empirical evaluation design.
- Source references are public URLs. Internal references remain repository-root-relative; the package source inventory pins their common revision.
