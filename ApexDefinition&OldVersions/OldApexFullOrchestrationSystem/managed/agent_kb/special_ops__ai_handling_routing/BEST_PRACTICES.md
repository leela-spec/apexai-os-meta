# BEST_PRACTICES

## Purpose

Accepted compact practices for Special Ops AI Handling Routing.

This scaffold is navigational. Detailed source evidence lives in `appendices/`.

## Entry schema

```yaml
practice_entry:
  id:
  status: accepted | deprecated
  practice:
  context_conditions:
  evidence_refs:
  appendix_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due:
```

## Accepted practices

### AIHR-BP-001 — Freeze the routing objective before selecting mode, tool, or handoff

- **Status:** accepted
- **Practice:** State what the task is, what it is not, the target output, and the non-goals before recommending an execution path.
- **Context conditions:** Use for every non-trivial model/tool/handoff decision.
- **Evidence refs:** `SingleGuide_Claude.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-001`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-001`.
- **Scores:** EVD 5 / IMP 5 / RSK 3.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-002 — Route ambiguity to one focused clarification or explicit `NEEDS_INPUT`

- **Status:** accepted
- **Practice:** If objective, authority, target surface, success criteria, or tool capability is materially unclear, ask one focused question or mark the route `NEEDS_INPUT`.
- **Context conditions:** Use when missing information changes the route or risk level.
- **Evidence refs:** `SingleGuide_Claude.md`; `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-002`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-002`.
- **Scores:** EVD 5 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-003 — Decide source authority before verification or handoff

- **Status:** accepted
- **Practice:** Identify the governing source tier before deciding whether an output, route, or handoff is safe to trust.
- **Context conditions:** Use whenever current files, summaries, prior chat, external docs, or assumptions compete.
- **Evidence refs:** `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-004`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-003`.
- **Scores:** EVD 5 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-004 — Classify overload before routing execution

- **Status:** accepted
- **Practice:** Classify the request as `one_pass_safe`, `decompose_first`, or `unsafe_in_one_pass` before sending it to an agent, model, tool, or repo execution surface.
- **Context conditions:** Use for multi-objective, multi-file, multi-tool, long-context, or high-risk work.
- **Evidence refs:** `WORKFLOW_BEST_PRACTICES_RESEARCH.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-012`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-001`.
- **Scores:** EVD 5 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-005 — Separate advisory chat routing from repo execution

- **Status:** accepted
- **Practice:** For repo-affecting work, require an execution surface, operation mode, exact repo-relative path, closed target set, and verification path before execution.
- **Context conditions:** Use when the route might involve Codex, GitHub connector writes, commits, patches, or file mutations.
- **Evidence refs:** `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-007`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-005`.
- **Scores:** EVD 5 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-006 — Prefer exact path and patch discipline over broad rewrite

- **Status:** accepted
- **Practice:** Route bounded file fixes to exact-path, minimal-patch handling; require explicit rewrite authority before whole-file or semantic rewrite work.
- **Context conditions:** Use for repo or file work where preservation matters.
- **Evidence refs:** `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-008`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-006`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-007 — Treat specific model/provider/cost claims as `needs_current_verification`

- **Status:** accepted
- **Practice:** Do not make current model, provider, pricing, performance, or availability recommendations unless the claim is verified in the current execution context.
- **Context conditions:** Use for model selection, tool selection, API/provider recommendations, cost-quality tradeoffs, or capability claims.
- **Evidence refs:** promptflow source-gap check; source manifest gap-risk note.
- **Appendix refs:** `APPENDIX_KB_SOURCE_MANIFEST.md#Ranking-plausibility-check`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-011`.
- **Scores:** EVD 4 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-BP-008 — Stop for manual review on config-impacting recommendations

- **Status:** accepted
- **Practice:** If a routing recommendation would modify or imply modification of `openclaw.json`, model registry, runtime config, provider policy, or permission authority, stop and route to manual/governance review.
- **Context conditions:** Use whenever advisory routing touches runtime authority.
- **Evidence refs:** promptflow target lock; seed boundary.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-015`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-010`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

## Reading path

1. Read `ESSENCE.md` for the lane boundary.
2. Use this file for compact practices.
3. Use `TEMPLATES.md` when a routing/handoff card is needed.
4. Use `MISTAKES.md` when routing risk is suspected.
5. Use appendices for evidence and candidate history.
