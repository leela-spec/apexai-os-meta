# R08 — Adversarial Evidence Audit — Result

Date: 2026-08-23  
Verdict: **AUDIT_PASS after recorded V1 corrections**  
Review: **PASS**

## Audit method

Every claim capable of changing a `KEEP/PILOT/DEFER/REJECT` action was re-opened in current first-party documentation, repository source or current issue state. Capability, integration, operational evidence and value were tested separately. The persisted R07 is the corrected V1; the correction packet below records changes made during this audit rather than hiding them.

## Decision-changing claim audit

| Claim attacked | Current evidence re-opened | Audit result | Decision impact |
|---|---|---|---|
| Hermes baseline owns orchestration, task state and provider path | current Hermes Kanban, provider and A2A docs plus accepted baseline | survives, but remains pre-install | KEEP, subject to existing QA |
| CrewAI can interoperate with Hermes over A2A | Hermes implements client/server v1.0; CrewAI implements client/server config with default 0.3.0 and auth/streaming | protocol roles verified; exact version negotiation/live behavior OPEN | no `ADD`; DEFER until named Flow and compatibility QA |
| CrewAI persistence is a better Kanban replacement | Flow persistence/human-feedback docs prove state features, not MoA task/review superiority | rejected as overstated | no replacement |
| Agency router avoids preloading 270 prompts | builder source loads JSON on disk and exposes four tool schemas; selected body loaded on inspect/load/delegate | survives | supports bounded PILOT |
| Agency delegation is fully verified | builder forwards optional `toolsets`; checker does not execute live `delegate_task`; current Hermes evidence uses `enabled_toolsets` | corrected to conditional limitation | pilot omits optional toolsets first; baseline fallback mandatory |
| Agency has superior MoA specialists | sample shows strong marketing/software/operations roles but weak workshop/general-review coverage | vendor breadth claim downgraded | PILOT, not ADD_NOW |
| Superpowers works on current Hermes | current plugin exists, but main and open issue #2157 show stale tool mappings/unqualified skill calls | contradicted for reliable as-shipped use | DEFER |
| Semantic Router could improve routing | library capability verified; no official selected-stack edge or measured defect | custom hypothetical rejected | REJECT |
| AnythingLLM can use QMD | AnythingLLM MCP client source plus QMD MCP server establish role compatibility | survives as protocol-backed edge, not product recipe | DEFER; possible UI pilot only |
| AnythingLLM native ingestion preserves fresh repo truth | beta sync docs describe file-only watches, cadence and moved/deleted behavior | contradicted as strong freshness claim | do not replace QMD |
| candidate popularity proves production value | repos/docs offer adoption and vendor claims, not exact MoA outcomes | rejected | no candidate receives ADD_NOW |

## Integration-edge verification

| Edge | Sender implemented | Receiver implemented | Version/auth/config | Data and state owner | Audit class |
|---|---|---|---|---|---|
| Hermes → CrewAI | Hermes A2A call/discovery | CrewAI A2A server | both document auth; v1.0 vs configurable/default 0.3.0 requires QA | explicit task/context/result; Hermes outer task, CrewAI inner Flow | OFFICIAL_PROTOCOL_BOTH_SIDES, C confidence |
| CrewAI → Hermes | CrewAI A2A client | Hermes A2A server/Agent Card | same version QA | caller retry; Hermes delegated session | OFFICIAL_PROTOCOL_BOTH_SIDES, C |
| Hermes → Agency router | Hermes plugin/tool dispatch | first-party router schemas | install/config documented | local roster; Hermes task/review | OFFICIAL_PLUGIN, B for search/load; C for delegate |
| Hermes → Superpowers | plugin bootstrap/skill registry | first-party plugin | current tool mapping conflict | Hermes session; no new DB | OFFICIAL_PLUGIN but CONTRADICTED reliability |
| Hermes ↔ Semantic Router | no sender adapter | no receiver plugin/protocol | none | would be bespoke | CUSTOM_REQUIRED |
| Hermes ↔ AnythingLLM | no product-specific edge | no product-specific edge | none | separate systems | NO_INTEGRATION_FOUND |
| AnythingLLM → QMD | generic MCP client | QMD MCP server | stdio is supported on both; exact config/tools require QA | QMD owns index, AnythingLLM owns chat/workspace | OFFICIAL_PROTOCOL_BOTH_SIDES, C |
| cross-runtime Agent Skills | formats/conventions differ by host | no full portability contract proved | OPEN | package/host-specific | OPEN |

## Operational-value challenge

| Candidate | Capability that survives | Operational evidence that survives | MoA value conclusion |
|---|---|---|---|
| CrewAI | Crews, Flows, persistence, knowledge/memory, MCP, A2A | active tested framework; no exact MoA case | possible bounded-flow value only |
| Agency Agents | current 270-role package, lazy router, first-party checker | checker coverage limited; vendor labels excluded | roster gaps require pilot sampling |
| Superpowers | coherent software methodology, first-party Hermes registration | current compatibility defect; no non-software outcome evidence | defer |
| Semantic Router | maintained semantic routing library | no selected-stack operation | reject custom insertion |
| AnythingLLM | mature UI/RAG/agent app and MCP client | broad product operation, but sync/security limits remain | separate UI only after a requirement |

## Baseline-bias audit

The baseline was not preserved by default. Its weak points remain explicit: context files are unconfigured; QMD schema/WSL behavior needs live QA; MarketingSkills family-relative loading is an inference; memory/Curator governance is untested; subscription quota semantics are open. No candidate proves a better one-owner solution to those weaknesses today:

- CrewAI and AnythingLLM add rather than remove state owners.
- Agency adds roster breadth but does not fix project truth, recovery or learning.
- Superpowers adds method overlap and a current defect.
- Semantic Router does not address the uninstalled baseline and requires custom infrastructure.

If baseline QA fails a required capability, the associated candidate decision must be reopened rather than protecting Hermes.

## Matrix and MCDA audit

- All 20 schema rows and six columns are present in corrected R07.
- No unsupported capability is scored as verified; vendor claims are D confidence.
- Hard filters are applied to proposed module uses, not entire products.
- Agency is not scored as a knowledge/runtime product; Semantic Router is not penalized for lacking RAG, but fails its actual integration use.
- The MCDA ranks optional **pilot opportunities**, not whole stacks, preventing double-credit for broad feature sets.
- Scores are anchored bands and swing weights follow the observed range; they are not a preselected 1–5 feature score.
- The 72.50/49.25/47.25 ordering does not authorize adoption because operational-value uncertainty and requirement gates remain.

## Contradiction ledger

| Claim | Source A | Source B | Conflict | Governing evidence | Impact | Resolution |
|---|---|---|---|---|---|---|
| current Hermes delegation toolset key | Agency builder forwards `toolsets` | current Hermes/Superpowers issue evidence names `enabled_toolsets` | schema/name drift | live current Hermes schema governs | Agency delegate options may fail | pilot without optional key; no patch; upstream/live QA |
| Superpowers Hermes readiness | plugin README/install path | issue #2157 and audited mapping source | documented support vs current execution drift | current source + open issue | cannot rely on plugin | DEFER |
| CrewAI/Hermes A2A compatibility | both implement A2A roles | documented/default protocol versions differ | capability vs exact compatibility | live negotiated test governs | no current integration guarantee | DEFER until named need + QA |
| AnythingLLM document freshness | “live sync” feature | beta limitations on cadence/delete/move | feature label vs semantics | detailed beta docs | cannot replace QMD on freshness | DEFER/reject replacement |
| Agency “production-ready” | repository marketing language | checker omits delegation and no MoA outcomes | vendor claim vs operational proof | tests/source govern | no ADD_NOW | PILOT |

## Correction packet applied to R07

1. CrewAI A2A changed from unqualified verified integration to `OFFICIAL_PROTOCOL_BOTH_SIDES`, confidence C, with explicit protocol-version QA.
2. Agency delegation changed from fully verified to `VERIFIED_LIMITATION`; search/inspect/load remain verified. Pilot scope now omits optional toolsets first.
3. Superpowers Hermes path changed from usable plugin to official plugin with `CONTRADICTED` current reliability.
4. AnythingLLM → QMD retained only as generic protocol-backed MCP edge; no Hermes/AnythingLLM edge is inferred.
5. AnythingLLM native ingestion downgraded for beta freshness/delete behavior.
6. Vendor production/adoption language removed from operational-value scoring.
7. MCDA reframed as pilot-priority module analysis; no cross-category “winner.”

## Post-correction sensitivity

The corrected order remains Agency pilot opportunity 72.50, AnythingLLM UI opportunity 49.25, CrewAI Flow opportunity 47.25. Simplicity, privacy and subscription scenarios choose baseline-only. Specialist-first chooses Agency pilot. Knowledge-first does **not** choose AnythingLLM until a human UI is an explicit requirement. Autonomy-first does **not** choose CrewAI until a named Flow need and A2A/recovery QA exist. Superpowers and Semantic Router cannot enter through reweighting while hard filters fail.

## Source registry

- All R00–R07 source IDs were re-opened at their recorded commits.
- [Hermes A2A](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
- [CrewAI A2A source](https://github.com/crewAIInc/crewAI/blob/f4731f5025f861c78e3af0487cc80bf5e7c64782/docs/edge/en/learn/a2a-agent-delegation.mdx)
- [Agency builder](https://github.com/msitarzewski/agency-agents/blob/ebe9c99acb5c96f9468de368d8bead775387d1a7/scripts/build-hermes-plugin.py)
- [Superpowers issue #2157](https://github.com/obra/superpowers/issues/2157)
- [AnythingLLM live sync](https://docs.anythingllm.com/beta-preview/active-features/live-document-sync)

No unresolved contradiction changes the V2 action set; open items are explicitly gated pilots. **AUDIT_PASS**.
