Below are the **relevant working + validation file paths** you should use alongside the prompt flow for reference, grounding, and verification.

I’ve grouped them by function so you can quickly navigate the system during execution.

---

# 1. Core working decision locks (PRIMARY CONTEXT)

These define the **truth you are integrating**.

```text
managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md
```

**Use for:**

- Ground truth validation

- Conflict resolution (newer overrides older)

- Ensuring no drift in logic or naming


---

# 2. Integration control file (YOU JUST CREATED)

```text
managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md
```

**Use for:**

- Executing the full integration process

- Driving staged patching + audits


---

# 3. Process + system backbone (VALIDATION OF CORRECTNESS)

These ensure your integration aligns with **Apex OS operating principles**.

```text
managed/processes/AGENT_HANDOFF_CONTRACTS.md
managed/rules/OPERATING_SPINE_CANON.md
managed/rituals/NIGHT_PLANNING_PROTOCOL.md
managed/rituals/SESSION_EXPORT_PROTOCOL.md
```

**Use for:**

- Verifying:

    - Handoff integrity

    - Trace vs state separation

    - Night loop correctness

- Preventing:

    - Metric collision (V/U/L/F vs EVD/IMP/RSK)

    - Invalid workflow assumptions


---

# 4. Informatics design layer (STRUCTURE + SIMPLIFICATION)

```text
managed/agents/special_ops__informatics_design.md
```

**Use for:**

- Structure decisions

- Naming consistency

- Avoiding:

    - Over-engineering

    - Redundant schemas

    - Poor retrieval structure


---

# 5. Alfred KB canonical files (TARGETS FOR PATCHING)

These are the **final surfaces where logic must land cleanly**.

```text
managed/agent_kb/alfred/ESSENCE.md
managed/agent_kb/alfred/BEST_PRACTICES.md
managed/agent_kb/alfred/MISTAKES.md
managed/agent_kb/alfred/TEMPLATES.md
managed/agent_kb/alfred/README.md
```

**Use for:**

- Ensuring:

    - Doctrine is compact

    - No schema bloat leaks into canonical layer

- Final validation surface


---

# 6. Learning + future system evolution (NON-CANONICAL)

```text
managed/agent_kb/alfred/LEARNING_QUEUE.md
```

**Use for:**

- Capturing:

    - v1.1 ideas

    - Algorithm evolution

    - Rhythm expansion

- Preventing premature complexity in v1


---

# 7. Source + audit layer (VALIDATION + TRACEABILITY)

```text
managed/agent_kb/alfred/SOURCE_MANIFEST.md
managed/agent_kb/alfred/COVERAGE_AUDIT.md
managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
managed/knowledge/AGENT_KB_LANES.md
```

**Use for:**

- Verifying:

    - What is source-backed vs derived

    - What is canonical vs working

- Ensuring:

    - No accidental promotion

    - Proper audit trail


---

# 8. Future appendices (TO BE CREATED BY FLOW)

These will become the **operational core**:

```text
managed/agent_kb/alfred/appendices/APPENDIX_APEX_ORIENTATION_AND_ROUTING.md
managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md
```

**Use for:**

- Housing all detailed schemas + mechanics

- Keeping canonical files clean


---

# 9. Validation strategy (how to use these together)

## Minimal validation loop

When executing any prompt in the flow:

1. **Check decision locks**
    → Are you aligned with latest rules?

2. **Check process files**
    → Are you violating Apex OS mechanics?

3. **Check informatics design**
    → Is structure clean and minimal?

4. **Check canonical targets**
    → Would this pollute ESSENCE/BEST_PRACTICES?

5. **Check audit layer**
    → Are you accidentally promoting non-canonical logic?


---

## High-risk drift indicators

Watch for these during integration:

- Mixing:

    - `V/U/L/F` ↔ `EVD/IMP/RSK`

- Reintroducing:

    - Sid vs Alfred confusion

- Inflating:

    - Daily Command Board into dashboard

- Violating:

    - Trace vs State separation

- Prematurely adding:

    - Weekly automation

    - Monthly planning

    - Mood/energy tracking

- Promoting:

    - Patterns too early


---

# 10. Condensed reference set (fast execution)

If you want the **minimum viable set during execution**:

```text
CORE:
- ALFRED_WORKFLOW_DECISION_LOCK.md
- APEX_VARIABLES_HANDOFF_DECISION_LOCK.md

CONTROL:
- APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md

VALIDATION:
- AGENT_HANDOFF_CONTRACTS.md
- special_ops__informatics_design.md

TARGET:
- ESSENCE.md
- BEST_PRACTICES.md
```

---

If you want, next step I can:

- Turn this into a **formal “Integration Checklist Artifact” file in repo**

- Or run a **pre-flight validation before you execute Prompt 0 in the new chat**