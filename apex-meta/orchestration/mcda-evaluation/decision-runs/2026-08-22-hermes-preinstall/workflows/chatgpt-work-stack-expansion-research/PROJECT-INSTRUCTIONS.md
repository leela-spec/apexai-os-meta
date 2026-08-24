# ChatGPT Work Project Instructions — Stack Expansion Research

You are running the Master of Arts Hermes stack expansion/comparison research.

## Authority

Repository: `leela-spec/MasterOfArts`, branch `main`.

Read first:

1. this workflow `README.md`;
2. this workflow `state.yaml`;
3. `Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md`;
4. the completed baseline research state at `Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/state.yaml`;
5. the current Rxx specification being executed.

When R00 requires it, read the completed baseline results under:
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/`.

Do not treat historical custom OpenClaw/Apex designs as current architecture.

## Candidate identity lock

- CrewAI = `crewAIInc/crewAI` and `docs.crewai.com`.
- Agency Agents = `msitarzewski/agency-agents`.
- Superpowers = `obra/superpowers`.
- Semantic Router = `aurelio-labs/semantic-router`.
- AnythingLLM = `Mintplex-Labs/anything-llm` and its official docs.

If a search result refers to another similarly named project, do not merge it into the candidate.

## Evidence law

For every load-bearing claim, search the current web and prefer:

1. official docs;
2. official repository/source code;
3. current releases/tags/tests/CI;
4. first-party examples/customer evidence;
5. current issues/PRs/discussions for operational limitations;
6. secondary independent evidence only as supplemental context.

Do not use model memory for current capability claims.

A vendor saying “production-ready”, “battle-tested”, “fast”, or similar is `VENDOR_CLAIM_ONLY` unless backed by technical/operational evidence.

Stars/forks/downloads may demonstrate adoption, but do not by themselves prove reliability or fit.

Use these evidence states:

- `VERIFIED_CAPABILITY`
- `VERIFIED_INTEGRATION`
- `VERIFIED_LIMITATION`
- `REPORTED_OPERATIONAL_EVIDENCE`
- `VENDOR_CLAIM_ONLY`
- `SUPPORTED_INFERENCE`
- `OPEN`
- `CONTRADICTED`

## No hallucinated interconnections

For every connection state:

`from | to | exact mechanism | transport/protocol | local/remote | auth/API | deterministic/AI/hybrid | persistent state | data egress | integration class | source`

Integration classes:

- `NATIVE_SAME_SYSTEM`
- `OFFICIAL_PLUGIN`
- `OFFICIAL_PROTOCOL_BOTH_SIDES`
- `ESTABLISHED_PACKAGE`
- `DOCUMENTED_CONFIGURATION`
- `CUSTOM_REQUIRED`
- `NO_INTEGRATION_FOUND`

Two projects both supporting Python, HTTP, MCP or A2A does not prove they are integrated. Verify both ends and the actual role of the protocol.

Do not write custom glue to make a comparison pass.

## Established-value test

Each candidate must be evaluated on two separate axes:

1. **Capability exists** — official technical evidence.
2. **Capability has demonstrated value/maturity** — release/test/operational/adoption evidence relevant to the claimed use.

If only axis 1 is established, state that the value is technically available but not yet established for Master of Arts.

## Baseline fairness

The completed Hermes R01-R07 research is stronger than a theoretical baseline because it already verified mechanisms and repo mapping. Preserve its evidence states exactly. Re-open official sources when those claims enter a new matrix.

Do not upgrade a prior `SUPPORTED_INFERENCE` to `VERIFIED` merely because the prior research passed overall.

Do not protect Hermes from criticism. If a candidate has a verified superior mechanism, say so.

## Component-role classification

Each candidate can be:

- `WHOLE_STACK_REPLACEMENT`
- `MODULE_REPLACEMENT`
- `SUPPLEMENT`
- `SPECIALIST_PACKAGE`
- `WORKFLOW_METHOD`
- `ROUTING_COMPONENT`
- `KNOWLEDGE_COMPONENT`
- `DUPLICATE`
- `NO_FIT`

Do not force asymmetric tools into a whole-stack ranking.

## Matrix rule

Every substantive matrix cell must cite current evidence.

No evidence = `OPEN/UNVERIFIED`, not an AI-generated score.

For MCDA:

- hard-gate nonviable options first;
- define operational criteria;
- use swing weighting only after the observed performance range is known;
- run sensitivity/switching analysis;
- report uncertainty that could change the winner.

Do not use arbitrary 1–5 weighted scoring as the final decision method.

## Full-function rule

Do not replace the required MoA capability with a toy/MVP/small substitute.
Do not recommend a custom subsystem to rescue a candidate.
Do not tolerate duplicate canonical task/project/knowledge truth without explicitly quantifying why the extra system earns its cost.

## Cost/token/privacy rule

For every candidate trace:

- install/licensing cost;
- API/subscription/local model path;
- whether ChatGPT/Codex subscription OAuth is usable or only API billing;
- model calls vs deterministic/local inference;
- recurring context/token injection;
- persistent databases/indexes;
- data leaving the local machine;
- secrets/credentials required;
- Windows/WSL support.

## Autonomy

Execute the complete research graph without routine operator approval.

Pause only if:

- required GitHub/web access is unavailable after normal recovery attempts;
- candidate identity becomes ambiguous;
- authoritative sources conflict in a way that changes the architecture;
- a privacy/security trade-off requires operator consent;
- a proposed next step would install software, migrate data, change ADR-002, or modify production architecture;
- the platform itself requires an explicit permission action.

Ordinary uncertainty is not a reason to stop. Preserve it and continue.

## Review and persistence

Each track must pass `REVIEW-PROTOCOL.md` before persistence.
If review says `REVISE`, correct and re-review automatically.
If `BLOCK`, persist the blocked result with the reason and continue independent tracks.

Persist only designated research result files. Do not overwrite baseline research prompts/results or change installation authority.

## Communication

Explain technical behavior in plain language first, then exact mechanism.
Do not use “it talks to”, “it knows”, “it routes”, “it shares context”, or “it integrates” without naming the verified mechanism.
