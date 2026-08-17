# Process — Macro / Meso Weekly Orchestration Improvement

## Macro process

### Phase A — Reconstruct and repair the orchestration spine

**Why:** Individual module fixes will drift if the global lifecycle, ownership, state rules and transactions remain stale or contradictory.

**Goal:** Make the production Weekly Orchestrator the clear, minimal runtime architectural spine.

**Method:** Inspect current weekly-orchestrator skill, stage agents/skills, shared contracts, deterministic helpers, state interfaces and recovered operator design. Challenge all current assumptions. Update global production contracts where required. Archive superseded material.

**Exit:** Master can state the intended lifecycle, every stage owner, every data transition, every gate, every persistence boundary and every AI/deterministic/operator role without contradictions.

### Phase B — Improve one output/module at a time

**Why:** Detailed human-facing outputs require focused operator discussion and should not flood the Master context.

**Goal:** Land one module's intended behavior in its real production skill/agent/template.

**Method:** Master generates a bounded handover from the module README + current global architecture. A fresh module chat discusses only the unresolved detailed design with the operator, implements it in production and returns evidence.

**Exit:** Module implementation exists in active production files and the module chat returns a concise implementation summary, changed paths, interface implications and unresolved issues.

### Phase C — Master integration verification

**Why:** A locally good module can still break downstream contracts, duplicate state or violate global authority.

**Goal:** Verify the module against the whole infrastructure before runtime testing.

**Method:** Master reads the actual changed files/diff and relevant upstream/downstream contracts. It checks ownership, transactions, state authority, gates, human/machine layering and stale references.

**Exit:** PASS -> fresh runtime test. FAIL -> bounded correction handover back to module chat.

### Phase D — Fresh runtime test

**Why:** A design chat contains hidden context and can accidentally make a weak implementation appear correct.

**Goal:** Test only what the repository actually encodes.

**Method:** Start a fresh test context. Invoke the real production skill/agent path with the frozen W34/example inputs. Do not explain desired output shape in the test prompt.

**Exit:** Produced artifact and execution evidence are returned to operator and Master.

### Phase E — Operator acceptance and iteration

**Why:** Architectural correctness does not prove operator usefulness.

**Goal:** Confirm the actual generated output is useful for real work.

**Method:** Operator reviews the production-generated example. Rejected -> return to module design/implementation. Accepted -> Master records module complete and opens next dependency-ready module.

---

## Meso process — Master cycle for every module

1. **Orient:** read `CURRENT-STATE.md`, `DECISIONS.md`, active module README and required production references.
2. **Define boundary:** state module input, owner, output, consumer, authority, persistence, operator interaction and known design intent.
3. **Create bounded handover:** include only global rules relevant to this module, exact active paths, known defects, desired output function, test fixture references and decisions still requiring operator input.
4. **Delegate to fresh chat:** module chat does not redesign the whole loop.
5. **Receive implementation evidence:** changed paths, summary, unresolved questions, interface changes, commit/ref.
6. **Verify:** inspect production files; validate upstream/downstream compatibility and global invariants.
7. **Update project state:** record verification outcome, decisions and next action in `CURRENT-STATE.md` / `DECISIONS.md`.
8. **Test fresh:** run `TEST-PROTOCOL.md` for the module.
9. **Accept or iterate:** operator verdict controls closure.
10. **Advance:** choose next dependency-ready module and create its handover.

## Named-consumer test

For every persistent file, major section, field, score, gate, validation object, review or deterministic computation:

1. Who consumes it?
2. What concrete capability does it enable or failure does it prevent?
3. What breaks if it disappears?
4. Can it be derived cheaply instead of persisted?
5. Is the same truth authoritative somewhere else?

If no concrete answer exists, it is a removal/archive candidate.

## Change policy

- Global contradictions may be fixed during Module 00 even when they touch stage files.
- Detailed layout/wording/output behavior belongs to the owning module chat.
- No unrelated cleanup during module work.
- When an active file becomes obsolete, apply `ARCHIVE-POLICY.md`.
- The Master may reorder unfinished modules only after recording a dependency reason.
