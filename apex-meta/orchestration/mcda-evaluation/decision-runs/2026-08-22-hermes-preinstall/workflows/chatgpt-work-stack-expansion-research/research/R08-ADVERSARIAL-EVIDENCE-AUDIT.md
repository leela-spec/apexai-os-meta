# R08 — Adversarial Evidence Audit

Status: **RESEARCH REQUIRED**  
Depends on: R07

## Decision question

Which conclusions in R07 survive an independent, adversarial re-check of the current sources and integration mechanics, and which must be corrected before a V2 recommendation is allowed?

This track is designed to prevent a confident synthesis from laundering weak evidence into architecture.

## Operating stance

Assume every decision-changing R07 conclusion could be wrong until re-verified.

Do not optimize for agreement. Try to falsify:

- reasons to keep Hermes modules;
- reasons to add candidates;
- reasons to reject candidates;
- integration claims;
- maturity/reliability claims;
- API/subscription/local-cost claims;
- token/context claims;
- security/privacy claims;
- Windows/WSL claims;
- MCDA performance judgments.

## Research tasks

### 1. Re-open decision-changing sources

Create a list of every R07 claim that changes `KEEP/ADD/PILOT/REPLACE/DEFER/REJECT`.

For each:

- open the current official source again;
- locate exact supporting text/code/schema;
- check release/date/commit;
- inspect current issue/PR state when operational evidence matters;
- identify whether the source proves capability, integration, limitation or only marketing.

Do not rely on R02-R06 citations without re-opening them.

### 2. Attack all integration edges

For every claimed connection, answer independently:

- Is the sender role implemented?
- Is the receiver role implemented?
- Is the protocol/transport version compatible?
- Is authentication/config documented?
- What exact data moves?
- Who owns retry/state/recovery?
- Does current source show this connection, or only generic extensibility?
- Would a custom bridge still be needed?

Specific high-risk edges to challenge include, where R07 uses them:

- Hermes <-> CrewAI via A2A;
- Hermes <-> Agency Agents router;
- Hermes <-> Superpowers current plugin/skills path;
- Hermes <-> Semantic Router;
- Hermes <-> AnythingLLM;
- AnythingLLM <-> QMD via MCP;
- cross-runtime Agent Skills portability.

### 3. Attack established-value claims

For each candidate challenge:

- “production-ready” language;
- star/download/community metrics;
- release cadence;
- test coverage/CI;
- unresolved severe issues;
- first-party case studies;
- non-software fit.

Correct any claim that confuses adoption with reliability or technical capability with proven business value.

### 4. Attack baseline assumptions

Re-check whether R00/R07 over-credit Hermes because the previous research focused on it. Specifically verify:

- Kanban capability vs actual MoA needs;
- project-context mechanics;
- QMD Windows/WSL path;
- MarketingSkills multi-family path inference;
- learning/Curator governance;
- subscription provider path;
- gaps that a candidate genuinely solves better.

Do not preserve Hermes by default.

### 5. Attack matrix cells and MCDA

Audit every high-weight/high-impact cell:

- evidence ID present and valid;
- status correct;
- score/performance judgment traceable to evidence;
- hard filter correctly applied;
- swing weights reflect actual range;
- no double-counted criteria;
- no module candidate penalized for not being a whole stack;
- no whole stack gets credit twice for overlapping features.

Re-run sensitivity after corrections.

### 6. Contradiction ledger

Create:

| Claim | Source A | Source B | Type of conflict | Which source/version governs | Decision impact | Resolution |
|---|---|---|---|---|---|---|

Preserve unresolved contradictions rather than smoothing them over.

### 7. Correction packet

List exact R07 conclusions/cells that must change before R09.

The producing Work process should update its working V1 matrix/synthesis accordingly; do not overwrite source research reports unless they contain a demonstrable factual error and the workflow explicitly authorizes a corrected version.

## Required output

1. decision-changing claim audit;
2. integration-edge verification table;
3. operational-value challenge results;
4. baseline-bias audit;
5. matrix/MCDA audit;
6. contradiction ledger;
7. exact correction packet;
8. post-correction sensitivity result;
9. verdict `AUDIT_PASS | V1_REVISION_REQUIRED | DECISION_BLOCKED`;
10. source registry.

## Pass standard

`AUDIT_PASS` only when no unsupported or overstated claim remains that could plausibly change the V2 recommendation. Minor wording/source-format issues do not block; integration, maturity, cost/privacy or ranking-changing evidence issues do.
