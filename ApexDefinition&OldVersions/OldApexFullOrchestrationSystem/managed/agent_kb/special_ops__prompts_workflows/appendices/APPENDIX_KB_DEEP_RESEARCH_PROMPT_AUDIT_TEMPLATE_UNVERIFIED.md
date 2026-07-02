# DEEP_RESEARCH_PROMPT_AUDIT_TEMPLATE

## Purpose

Use this template to evaluate whether a deep research prompt is strong enough to guide repo-grounded, high-reliability work without hallucination, drift, fake completion, or vague candidate output.

A prompt passes only if it is bounded, evidence-first, stage-gated, explicit about state and outputs, and verification-backed.

## Pass Standard

A strong deep research prompt is:

- evidence-first
- target-locked
- stage-gated
- artifact-centered
- explicit about state
- explicit about control signals
- verification-backed at closure

## Audit

### 1. Scope Lock

Check:

- exact objective is named
- exact repo or target scope is named
- non-goals are named
- stop condition is named
- completion criteria are named

Fail if:

- the prompt says “analyze everything” without boundaries
- the desired end-state is vague
- the model is allowed to broaden scope silently

### 2. Source Authority

Check:

- primary sources are named
- secondary sources are named
- forbidden or low-authority sources are named
- repo evidence outranks summaries and assumptions

Fail if:

- the prompt allows unsupported inference
- prior chat or summaries can override raw files
- the model can claim capabilities without evidence refs

### 3. State Discipline

Check:

- the prompt requires an explicit state or frame block
- current task state is defined in the prompt
- continuity does not depend on chat-history reconstruction

Fail if:

- the prompt assumes the model “remembers the context”
- active task state is implicit
- missing or stale state would not trigger a stop

### 4. Task Shape

Check:

- work is split into explicit stages
- each stage has a clear purpose
- large work is still bounded by stage
- synthesis is separated from verification

Fail if:

- research, design, writing, QA, and finalization are blended into one opaque pass
- the task is too broad to verify
- multiple hidden sub-goals are mixed together

### 5. Output Contract

Check:

- exact required outputs are named
- outputs are artifact-shaped, not just advisory
- final outputs are distinct from candidate ideas
- output order or sections are defined if needed

Fail if:

- the prompt asks for “thoughts,” “ideas,” or “recommendations” when files or structured outputs are required
- the prompt does not distinguish final from partial output
- the output shape is underspecified

### 6. Control Signals

Check:

- `HALT` conditions are defined
- `CLARIFY` conditions are defined
- unsupported claims trigger stop behavior
- ambiguity is treated as a control issue, not a prose note

Fail if:

- the model is expected to guess through ambiguity
- failure conditions are soft suggestions only
- there is no structured stop behavior

### 7. Verification

Check:

- the prompt requires a verification pass
- claims must be tied to evidence
- outputs must be checked before “done”
- completion depends on validation, not fluency

Fail if:

- the prompt allows completion after generation only
- routing, capability, or architecture claims are not checked
- verification is implied but not required

### 8. Drift Control

Check:

- the prompt blocks silent scope expansion
- out-of-scope improvements must be captured separately
- adjacent improvements are not auto-applied
- invented architecture is disallowed

Fail if:

- the prompt rewards “helpful extras”
- the model can mutate nearby concerns without approval
- the task can slide from evidence into generic theory

### 9. Finalization Discipline

Check:

- final statuses are defined
- candidate-only material cannot be labeled final
- unresolved blockers must be surfaced explicitly
- partial completion has a truthful status

Fail if:

- the prompt allows vague completion language
- the prompt hides missing evidence
- final and provisional outputs are blurred

### 10. Multi-Agent / Handoff Discipline

Check:

- handoff structure is defined if multiple agents or stages are involved
- settled state is passed forward
- exact next job is passed forward
- risks and success condition are passed forward

Fail if:

- handoffs depend on hidden reasoning
- downstream agents must reconstruct intent from chat
- ownership boundaries are unclear

## Quick Score

Score each area from 0 to 2:

- 0 = missing
- 1 = partial
- 2 = strong

Categories:

- Scope Lock
- Source Authority
- State Discipline
- Task Shape
- Output Contract
- Control Signals
- Verification
- Drift Control
- Finalization Discipline
- Handoff Discipline

### Rating

- 18-20: strong
- 14-17: usable but risky
- 10-13: weak
- under 10: not safe for serious deep research work

## Final Verdict

Use one of these:

- `PASS`
- `PASS_WITH_RISKS`
- `FAIL_REVISE_PROMPT`