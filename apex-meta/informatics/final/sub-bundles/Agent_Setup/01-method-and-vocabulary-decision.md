---
type: architecture-decision-research
status: decision_ready_not_applied
created: 2026-09-03
---

# Method and Vocabulary Decision

## Decision

Use a **thin established-method hybrid**.

Do not make `Macro / Meso / Micro` the primary execution vocabulary agents must learn. Preserve those terms as an operator-facing mental model/alias if useful, but map them to established concepts that models already recognize.

Do not copy GitHub Spec Kit wholesale into Apex. Reuse its lifecycle vocabulary and complexity-scaling concepts while keeping Apex state, authorization, and project records in their existing owners.

## Candidate comparison

| Candidate | Fit to operator intent | Reuse of established vocabulary | Complexity adaptation | Bottom-up V&V | Fit with Plan-Sync-Session | New-system risk | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Mostly adopt Spec Kit | High | Very high | Very high | Medium | Medium | Medium-high | Strong reference, too much ownership overlap if transplanted wholesale |
| Systems Engineering only | High for hierarchy/V&V | Very high | Medium | Very high | High | Low | Excellent semantic backbone, incomplete agent execution workflow alone |
| WBS only | Medium | Very high | Medium | Low | High | Low | Useful decomposition primitive only |
| Kiro-style spec modes | High | High | Very high | Medium | High | Low-medium | Strong corroborating pattern, vendor-specific implementation |
| New Apex Macro/Meso/Micro framework | High by definition | Low | Could be high | Could be high | High | **Very high** | Reject unless established vocabulary proves insufficient |
| **Thin hybrid** | **Very high** | **Very high** | **Very high** | **Very high** | **Very high** | **Low** | **RECOMMENDED** |

## Canonical vocabulary

### Preferred machine-facing terms

| Function | Canonical established term | Apex/operator alias |
|---|---|---|
| Whole-system purpose, value, boundaries, success | **System intent / stakeholder requirements / top-level specification** | Macro |
| Decomposition into capabilities/modules and interfaces | **Architecture / requirements allocation / subsystem specification** | Meso |
| Exact buildable/doable unit | **Detailed specification / work package / task** | Micro |
| Downward process | **Decomposition, derivation, allocation, requirements flowdown** | Macro -> Meso -> Micro |
| Upward process | **Integration, verification, validation, convergence** | Micro -> Meso -> Macro |
| Does output match its specification? | **Verification** | check realization against parent/requirements |
| Does realized system solve intended problem? | **Validation** | check final outcome against Macro/system intent |
| Parent-child scope completeness | **WBS 100% rule** | all and only parent scope represented |
| Iterative gap closure | **Convergence** | repeat until no material spec/implementation gap remains |

### Why not use Macro/Meso/Micro as primary agent terms

The three labels are compact and useful to the operator, but they are semantically overloaded across disciplines and already collide with historical Weekly artifacts in this repository. Agents gain more from explicit terms such as `system intent`, `architecture`, `detailed specification`, `verification`, and `validation` because those terms carry established prior meaning and reduce inference burden.

Recommended wording:

> Decompose top-down from system intent to architecture/work packages/tasks, preserving traceability and parent scope. Realize bottom-up: verify each implemented unit against its specification, integrate/verify parent units, then validate the realized system against intended outcomes. For the operator, this corresponds to Macro -> Meso -> Micro -> Meso -> Macro.

## Canonical lifecycle

```text
UNDERSTAND / CLARIFY
        ↓
SPECIFY INTENT + REQUIREMENTS
        ↓
PLAN / ARCHITECT / ALLOCATE
        ↓
DECOMPOSE INTO WORK PACKAGES / TASKS
        ↓
ANALYZE CONSISTENCY + DEPENDENCIES
        ↓
IMPLEMENT BOUNDED WORK
        ↓
VERIFY UNIT OUTPUTS
        ↓
INTEGRATE + VERIFY PARENT
        ↓
VALIDATE AGAINST SYSTEM INTENT
        ↓
CONVERGE / CORRECT IF GAPS REMAIN
```

This is a semantic composition, not a claim that NASA, PMI, Spec Kit, or Kiro defines this exact combined lifecycle.

## Complexity routing

Do not introduce a numerical complexity score unless evaluation proves it useful. Route by observable task properties instead.

### Route 0 — Direct execution

Use when all are true:

- target is explicit and bounded;
- expected output is obvious;
- no material ambiguity;
- no meaningful cross-component dependency reasoning;
- reversible/low-risk or existing mutation gate already covers it;
- can be completed coherently in one bounded context.

Behavior: execute directly, verify result exists, report.

Examples: push known files; rename one file; answer from a supplied artifact; make one small approved edit.

### Route 1 — Compact preflight / Quick-Spec-like

Use when work is nontrivial but still fits one coherent implementation cycle.

Triggers include one or more:

- multiple meaningful subtasks;
- scope could be misunderstood;
- output structure matters;
- dependencies/sources materially affect execution;
- mutation spans several files/components;
- success requires explicit acceptance conditions.

Behavior:

1. expose compact understanding/preflight;
2. clarify only material ambiguity;
3. produce a bounded spec/plan/tasks representation;
4. implement;
5. verify + validate outcome;
6. converge once if needed.

### Route 2 — Full specification flow

Use when:

- requirements/design choices are consequential;
- multiple modules/interfaces must coordinate;
- operator review between definition and implementation has material value;
- there is significant uncertainty, dependency risk, or costly rework potential;
- execution cannot safely be represented as one bounded task list.

Behavior: requirements/specification -> design/architecture -> tasks/work packages -> cross-artifact analysis -> implementation phases -> integration verification -> system validation.

### Route 3 — Recursive/bounded program

Use only when Route 2 still exceeds manageable context or one implementation run.

Typical evidence:

- large epic/program with independently valuable slices;
- many modules with partial ordering;
- context would contain substantial irrelevant detail for each worker;
- a phase/slice itself remains too large after ordinary decomposition;
- long-horizon work needs durable checkpoints and independent bounded contexts.

Behavior:

- create a roadmap/spec-of-specs-like decomposition;
- each slice has explicit intent, scope boundary, dependencies, status, and link to its own specification;
- execute one bounded slice/phase at a time;
- verify each slice before integration;
- recursively decompose only a slice that still fails boundedness.

## Complexity anti-patterns

Reject these behaviors:

- forcing requirements/design/tasks documents onto trivial work;
- creating an epic because a task has several steps;
- using recursive decomposition before one bounded plan has actually failed context/manageability;
- using agents/subagents merely because a task is long;
- treating output length as complexity;
- treating irreversible action risk as planning complexity (risk belongs to authorization/mutation policy, not this method);
- inventing a numeric complexity model and thresholds without evaluation evidence.

## Hierarchical correctness rules

1. **Traceability:** every child work unit must map to a parent requirement/capability/outcome or be explicitly marked derived/new scope.
2. **100% accounting:** child scope should cover all required parent scope and should not silently introduce unrelated scope.
3. **Validate before deeper flowdown:** if a derived architecture/subsystem requirement materially changes intent or constraints, reconcile it against its parent before further decomposition.
4. **Verify before upward integration:** a unit should satisfy its own acceptance/specification before being treated as complete input to parent integration.
5. **Validate at system boundary:** a fully integrated result can pass verification yet still fail the intended outcome; final validation is separate.
6. **Converge from evidence:** if verification/validation finds a gap, update the appropriate upstream artifact/assumption rather than patching only the visible symptom.

## Source-backed conclusions vs local adaptation

### Directly source-backed

- Spec Kit uses an agentic SDD lifecycle and documents bounded implementation, subagents, and spec-of-specs for increasingly large work.
- Kiro distinguishes Quick Spec and Full Spec modes and uses Requirements -> Design -> Tasks in its structured flow.
- NASA guidance uses hierarchical requirements decomposition/flowdown, traceability, verification, and validation.
- PMI WBS is deliverable-oriented hierarchical decomposition and uses the 100% rule.
- Anthropic Agent Skills uses progressive disclosure from metadata to `SKILL.md` to deeper resources.

### Apex-specific composition/inference

- The exact lifecycle above is a local integration of those established concepts.
- Mapping operator Macro/Meso/Micro to system intent/architecture/work packages is an Apex aliasing decision.
- The four route model is an Apex routing design inspired by Spec Kit/Kiro complexity behavior; it is not an external standard.
- Keeping Plan-Sync-Session as the state owner is based on current repository architecture, not an external framework recommendation.
