# MISTAKES

## Purpose

Accepted validated AI Handling Routing failure patterns and countermeasures.

This scaffold is compact. Detailed drift evidence lives in `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

## Entry schema

```yaml
mistake_entry:
  id:
  status: accepted | deprecated
  pattern:
  trigger_conditions:
  countermeasure:
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

## Accepted mistake patterns

### AIHR-MISTAKE-001 — Routing before objective freeze

- **Status:** accepted
- **Pattern:** Agent chooses model, tool, specialist, or execution surface before task, non-task, target output, and success criteria are explicit.
- **Trigger conditions:** broad prompt; multi-part request; unclear target surface; user asks to "execute" without a bounded mode.
- **Countermeasure:** freeze objective and classify overload before routing.
- **Evidence refs:** `SingleGuide_Claude.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-001`.
- **Scores:** EVD 5 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-002 — Silent source-authority substitution

- **Status:** accepted
- **Pattern:** Agent treats summary, prior chat, memory, or speculative reasoning as stronger than the current authoritative source.
- **Trigger conditions:** summarized handoff exists; current file is available but not read; multiple sources conflict.
- **Countermeasure:** select authority tier first; prefer current direct source; flag primary-source conflict explicitly.
- **Evidence refs:** `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-003`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-003 — Verification theater

- **Status:** accepted
- **Pattern:** Agent approves, forwards, commits, or routes output because it is fluent and structured, without evidence, read-back, diff, source check, or test.
- **Trigger conditions:** output looks complete; no explicit verification artifact exists; downstream reuse is expected.
- **Countermeasure:** use confidence states; require evidence for `VERIFIED`; mark unverified outputs `PROBABLE`, `WEAK`, or `UNSAFE`.
- **Evidence refs:** `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-004`.
- **Scores:** EVD 5 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-004 — Advisory routing collapses into repo execution

- **Status:** accepted
- **Pattern:** Browser-chat advisory work becomes direct file mutation or repo execution without mode lock, exact target paths, or post-write verification.
- **Trigger conditions:** user says "execute"; connector write tools are available; promptflow includes target paths.
- **Countermeasure:** require explicit execution surface, operation class, exact repo-relative paths, closed target set, and fetch-back verification.
- **Evidence refs:** `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-005`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-005 — Rewrite reflex for bounded repair

- **Status:** accepted
- **Pattern:** Agent routes a small defect, path fix, or local update into a broad rewrite or cleanup pass.
- **Trigger conditions:** long file; stale references; desire to make surrounding content coherent; ambiguous repair boundary.
- **Countermeasure:** patch before rewrite; preserve untouched content; stop if a semantic rewrite is required but not authorized.
- **Evidence refs:** `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-006`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-006 — Path drift

- **Status:** accepted
- **Pattern:** Agent uses a vague filename, guessed repository, Windows locator path, or stale path as execution authority.
- **Trigger conditions:** local path and repo path both appear; same filename exists in multiple places; target repo is ambiguous.
- **Countermeasure:** use exact repo-relative paths; verify repo context; stop on ambiguity.
- **Evidence refs:** `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-007`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-007 — Premature specialist or Codex handoff

- **Status:** accepted
- **Pattern:** Agent hands off work before objective, scope, source authority, constraints, expected output, fallback posture, and validator are explicit.
- **Trigger conditions:** high-complexity request; long promptflow; multiple agents named; user wants speed.
- **Countermeasure:** use a routing card or handoff note before delegation.
- **Evidence refs:** `HARMONIZATION_RISK_REGISTER.md`; `SingleGuide_Claude.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-008`.
- **Scores:** EVD 4 / IMP 5 / RSK 4.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-008 — Config-authority overreach

- **Status:** accepted
- **Pattern:** Advisory model/tool guidance becomes a recommendation to mutate runtime config, provider policy, or permission authority.
- **Trigger conditions:** `openclaw.json`, model registry, provider settings, tool permissions, or runtime authority are implicated.
- **Countermeasure:** stop and route to manual/governance review; do not self-authorize config mutation.
- **Evidence refs:** `PROMPTFLOW_KB_BASE_BUILD.md`; current seed boundary.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-010`.
- **Scores:** EVD 5 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

### AIHR-MISTAKE-009 — Stale model/provider claim

- **Status:** accepted
- **Pattern:** Agent routes based on outdated model names, pricing, capability claims, or provider availability.
- **Trigger conditions:** model/provider choice is material; no current source has been checked; claim could have changed recently.
- **Countermeasure:** mark `needs_current_verification`; verify live/current source before recommending.
- **Evidence refs:** source manifest gap-risk note.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-011`.
- **Scores:** EVD 4 / IMP 5 / RSK 5.
- **Owner:** `special_ops__ai_handling_routing`.
- **Validator:** `meta_ops`.

## Stop pattern summary

- **Stop:** missing source authority.
- **Stop:** execution surface unclear.
- **Stop:** route implies config mutation.
- **Stop:** repo path or target repo ambiguous.
- **Stop:** current model/provider claim is material but unverified.
- **Stop:** handoff lacks acceptance criteria or validator.
