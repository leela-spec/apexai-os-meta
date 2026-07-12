---
packet_id: "us-idea-01-sim-001"
role_accountability: meta_ops
lifecycle_stage: proposal
status: candidate_entry_drafted
target_surface: "apex-meta/fable-orchestrator/fable-execution-best-practices.md (proposed durable home, NOT yet written)"
next_state: "placement packet exists (02-placement-packet.md)"
prerequisites: ["00-intake-packet.md"]
expected_action: "Knowledge Bank: check placement, duplicates, lane, candidate status; do NOT promote or create a project"
sources_evidence:
  - "00-intake-packet.md (raw source, verbatim)"
  - "apex-meta/fable-orchestrator/prompts/PromptAnswers/research-integration-note.md §0 (the delivered-vs-wanted assessment the operator asked for)"
uncertainties:
  - "U1: whether the rule should bind ALL external-model prompts or only deep-research prompts (source says 'these prompts'; confidence: medium that it generalizes)"
  - "U2: durable home — fable-execution-best-practices.md vs. PromptEngineer skill references (placement question for Knowledge Bank)"
unresolved_risk:
  - "R1: over-generalizing a context-specific complaint into a blanket rule (operator explicitly said 'I don't want to overengineer')"
stop_condition: "stop if Detective finds the distillation replaced distinctive wording with generic advice"
operator_validation: not_requested
authority:
  state: candidate
  basis_digest: null
  verification_ref: null
---

# Candidate idea record

## Distilled core (near-source)

**When this repo delegates research to an external model, the prompt must carry the repo's identity into the question**: name the orchestration system under design, name the exact folders where its parts are defined, and name the specific knowledge base(s) that already hold the information (e.g. `apex-meta/kb/claude-code-orchestration-design`). Otherwise the answers come back as "random web searches that don't really understand what we're doing here" (operator's words) — generically argued, needing full re-grounding before they can be trusted.

## Explicit claims (from source, confidence-marked)

1. **[high]** The delivered deep-research prompts were badly designed *because* they were not linked to the repos and actual orchestration systems.
2. **[high]** The repo already has the information externally researched ("you do have all the information in the repo") — external research must be additive to, not ignorant of, it.
3. **[high]** Requirement, verbatim intent: name (a) the orchestration system, (b) the folders where its parts are defined, (c) the relevant repo KB(s), inside any such prompt.
4. **[medium]** Precision matters most "specifically in the beginning with the architecture" — early-phase prompts carry the highest grounding burden.
5. **[high]** Counter-principle stated in the same breath: do not overengineer — this is one precise rule, not a new prompt bureaucracy.

## Preserved roughness / unresolved fragments

- "be critical in understanding if we actually delivered what we wanted to get delivered" — an instruction about *evaluation posture* toward external results, not only about prompt authoring; kept as its own fragment, not merged into the rule.

## Candidate tags and links (tentative)

- tags: `prompt-design`, `external-research`, `grounding`, `fable-orchestrator-lessons` (confidence: high)
- related existing records: `fable-execution-best-practices.md` (execution lessons; §7 holds a similar "check before deleting" lesson → likely lane), `prompts/PromptAnswers/research-integration-note.md` §4 ("Neither answer was repo-bound") — same finding from the artifact side (confidence: high)
- project links: PromptEngineer skill (`provider-style-contract-chatgpt.md`, deep-research section) as a *candidate* second surface (confidence: low — see R1)

## Candidate next actions (bounded, operator chooses zero or more)

- A1: add the rule as a numbered lesson to `fable-execution-best-practices.md` (effort: small; stop: one section, no restructure)
- A2: nothing further (record kept as knowledge only)
