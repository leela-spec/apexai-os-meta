---
packet_id: "us-idea-01-sim-002"
role_accountability: knowledge_bank
lifecycle_stage: proposal
status: placement_recommended
target_surface: "apex-meta/fable-orchestrator/fable-execution-best-practices.md §3 (recommended durable home, NOT yet written); apex-meta/orchestration/simulations/US-IDEA-01-20260711/02-placement-packet.md (this file, only write of this stage)"
next_state: "Meta Ops holds a reviewed placement recommendation; operator (via Meta Ops) chooses A1 (place as §3 amendment) or A2 (keep as record only); any write to the durable home happens in a later, separate invocation"
prerequisites:
  - "apex-meta/orchestration/simulations/US-IDEA-01-20260711/00-intake-packet.md (immutable raw source)"
  - "apex-meta/orchestration/simulations/US-IDEA-01-20260711/01-candidate-entry.md (candidate idea record)"
expected_action: "Meta Ops: review this placement recommendation and route the A1/A2 choice to the operator; do not treat the recommendation as a promotion — the record stays candidate until independently reviewed"
sources_evidence:
  - "00-intake-packet.md L28 (verbatim raw operator note) — identity check basis"
  - "01-candidate-entry.md L30, L34-L38 (distilled core + claims) — traceability check basis"
  - "apex-meta/fable-orchestrator/fable-execution-best-practices.md L73-L85 (§3 universal_deep_research_prompt_frame: context rule L76, specificity_rule L79, perplexity_specific_rule L84), L87-L100 (§4 verification contract)"
  - "apex-meta/fable-orchestrator/prompts/PromptAnswers/research-integration-note.md L25 (§0 operator criticism recorded), L59 (§4 'Neither answer was repo-bound')"
  - ".claude/skills/PromptEngineer/ProviderStyleContract_ChatGPT.md L9 (style rules: avoid 'ambiguous_source_authority'), L27 (Deep Research Prompt Patterns), L59 (deep-research example prompt)"
  - "apex-meta/fable-orchestrator/prompts/external-research-pack-20260711.md L1-L26 (v2 pack frontmatter — confirms only v2 exists as a file)"
uncertainties:
  - "U1 (carried from 01): whether the rule binds ALL external-model prompts or only deep-research prompts — placement below works under either reading; scope decision stays with the operator"
  - "U2 (resolved as recommendation, not decision): primary home = fable-execution-best-practices.md §3; PromptEngineer surface demoted to optional cross-reference (see alternatives)"
  - "U3 (new): research-integration-note.md §0 and §4 claim 'v3 prompts' already fix repo-binding, but no v3 prompt file exists in apex-meta/fable-orchestrator/prompts/ — only the v2 pack (external-research-pack-20260711.md). The claimed fix is a missing source, reported as missing, not paraphrased. If v3 never materialized, the candidate rule is the only durable carrier of this requirement."
unresolved_risk:
  - "R1 (carried from 01): over-generalizing a context-specific complaint — mitigated by recommending an amendment inside existing §3 rather than a new section or new doc (honors the operator's 'I don't want to overengineer')"
  - "R2 (new): if A1 is executed as a broad rewrite of §3 instead of a minimal sharpening, it would duplicate specificity_rule (L79) and perplexity_specific_rule (L84) — the executing lane must merge, not append a near-duplicate"
stop_condition: "Stop after this file is written. If Meta Ops or Detective finds the identity check below wrong (distillation not traceable to L28 of the intake), route back to Meta Ops for re-distillation before any placement."
operator_validation: not_requested
authority:
  state: candidate
  basis_digest: null
  verification_ref: null
---

# Placement packet — US-IDEA-01 grounding rule (stage 3, Knowledge Bank)

## 1. Source identity check — PRESERVED

- The raw operator note in `00-intake-packet.md` L28 is present verbatim (typos preserved: "the to the", "knowledge base of for example"). No summary replaces it; the intake explicitly marks it immutable.
- `01-candidate-entry.md` L30 (distilled core) quotes the source verbatim where it matters ("random web searches that don't really understand what we're doing here") and every claim in L34-L38 maps to a sentence in L28 of the intake:
  - claim 1 → "really badly designed... could have been linked to the repos and to the actual orchestration systems"
  - claim 2 → "you do have all the information in the repo"
  - claim 3 → "naming the orchestration system, naming the folders where they're defined, and name the repo knowledge base"
  - claim 4 → "quite important to be precise, specifically in the beginning with the architecture"
  - claim 5 → "I don't want to overengineer"
- The evaluation-posture fragment ("be critical in understanding if we actually delivered") is kept separate in 01 (L42), not flattened into the rule. Identity preserved; no drift found.

## 2. Duplicate / related records (found by search, exact files + sections)

| Record | Location | Relation to candidate |
|---|---|---|
| §3 `universal_deep_research_prompt_frame` — `context` rule | `apex-meta/fable-orchestrator/fable-execution-best-practices.md` L76 | Related: "paste the specific repo files/KB excerpts needed" — content-carrying, but does not require *naming* the system/folders/KB |
| §3 `specificity_rule` | same file, L79 | **Closest existing record**: "State the exact repo path, KB name, or decision this prompt's output will feed into." Partial overlap — it names *one* path/KB as target, the candidate requires naming (a) the orchestration system, (b) the defining folders, (c) the KB(s), as *identity carried into the question*, with operator authority behind it |
| §3 `perplexity_specific_rule` | same file, L84 | Related, provider-scoped: "name the exact repo/path" for Perplexity's GitHub connector only |
| §4 `verification_contract` | same file, L87-L100 | Covers the candidate's *evaluation-posture* fragment ("be critical... delivered what we wanted") — cross-check every claim against real repo state, downgrade ungroundable claims |
| Integration note §0 | `apex-meta/fable-orchestrator/prompts/PromptAnswers/research-integration-note.md` L25 | Same finding from the artifact side: "the answers argue mostly from generic framework surveys... the re-run prompts (v3) are rewritten to name the systems, folders, and KB explicitly" — a dated assessment, not durable doctrine |
| Integration note §4 | same file, L59 | "Neither answer was repo-bound" — the empirical evidence for the candidate rule |
| PromptEngineer deep-research patterns | `.claude/skills/PromptEngineer/ProviderStyleContract_ChatGPT.md` — "Deep Research Prompt Patterns" (L27) and style rules (L9: avoid `ambiguous_source_authority`, `unbounded_research_scope`) | Related but generic: requires source grounding and scope, contains **no** repo-identity naming rule; the file's ownership block restricts it to provider-style adaptation, so a repo-specific grounding rule does not belong there as primary |
| Missing: "v3 prompts" | claimed at research-integration-note.md L25/L59; **no file found** in `apex-meta/fable-orchestrator/prompts/` (only the v2 pack `external-research-pack-20260711.md`) | Reported missing per KB rule — not paraphrased from memory |

**Classification: EXTENSION** — not a duplicate (no existing record carries the full three-part naming requirement with operator authority), not wholly new (§3 `specificity_rule` and the integration note already point the same direction). The candidate sharpens an existing rule and gives it the operator's explicit backing.

## 3. Recommended primary durable home — ONE

**`apex-meta/fable-orchestrator/fable-execution-best-practices.md` §3** — amend/sharpen the `universal_deep_research_prompt_frame` (strengthen `specificity_rule` or add one adjacent `repo_identity_rule` line inside the same YAML block; alternatively a numbered lesson section per A1 of the candidate entry, but the in-§3 amendment is smaller and honors R1).

Reasoning:
- §3 is *the* operating rule surface for authoring external research prompts — exactly the activity the operator's rule governs; placing it anywhere else splits doctrine from its enforcement point.
- The closest existing record lives there (L79); merging avoids a near-duplicate rule in a second file (R2).
- The file already holds lane-matched lessons (§7 deliverable-over-process, §8 check-before-delete) — 01-candidate-entry.md L47 identified this lane correctly.
- Given U3 (no v3 prompt file exists), this is the only surface where the rule would durably bind future prompt authoring.

Alternatives considered and rejected as primary:
- `research-integration-note.md` — a dated, status-"drafted" assessment artifact tied to one research pack; evidence, not doctrine. Keep as citation.
- `.claude/skills/PromptEngineer/ProviderStyleContract_ChatGPT.md` — provider-generic style contract; its ownership boundaries exclude repo-specific content; at most an optional cross-reference later (matches 01's low confidence on this surface).
- New standalone rule file — rejected outright; violates claim 5 ("don't overengineer") and R1.

## 4. Candidate status — CONFIRMED, NOT PROMOTED

`authority.state: candidate` on 00, 01, and this packet. Knowledge Bank records this status; it does not promote. Promotion requires independent review plus the operator-gated path (schema rule 2). No durable home has been written; A1 remains a proposed action.

## 5. Project membership

This belongs to the **existing fable-orchestrator initiative** (`apex-meta/fable-orchestrator/`), not a new project. It is feedback on that initiative's own external-research prompt practice, its evidence lives in that folder's artifacts, and its recommended home is that folder's operating doc. No new project, epic, or KB scaffold is warranted.
