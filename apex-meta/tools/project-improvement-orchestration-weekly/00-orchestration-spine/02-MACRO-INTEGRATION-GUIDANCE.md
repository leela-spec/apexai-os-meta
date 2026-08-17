# Macro Guidance — Integrate the Validated Operator Design into the Real Weekly Runtime

## Why this file exists

The validated operator-facing design already exists, but the production Weekly Orchestration does not reliably execute it.

The failure is not primarily that the templates are missing. The Step 5 promotion copied J1-J12 templates into owning packages, but Step 6 activation validation explicitly reports:

- `contracts_changed: 0`
- `entrypoints_changed: 0`
- `runtime_changes: 0`

while declaring the design `active_and_ready`.

The current PreCapWeek and PreCapNextDay entrypoints still instruct the runtime to create schema-first planning packets, numeric rating structures, per-flow packets, and per-flow prompt packs. Therefore the design was **promoted as files but not integrated as runtime behavior**.

This project must correct that at the source.

---

## Objective

Make the **actual production Weekly Orchestration runtime** express the already validated operator experience while removing or archiving stale active instructions that cause the old schema-centric behavior to reappear.

The desired result is not a presentation overlay on top of the current packets. It is a runtime in which:

1. the Weekly Orchestrator defines a simple, coherent lifecycle;
2. each stage has one clear owner and bounded interface;
3. operator-facing artifacts are the primary stage outputs where an operator must understand, decide, execute, or review;
4. machine payloads are retained only when a named consumer needs them;
5. stale contracts cannot remain discoverable as competing active authority;
6. a fresh runtime invocation produces the intended behavior without prior design-chat memory.

---

## Validated design authority to integrate

Use these as the current design intent unless the operator explicitly changes them:

- `apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml`
- Step 4 templates and worked examples
- operator decisions recorded in this project folder

### Locked presentation behavior

Primary outputs must be:

- human first;
- result-card first;
- decision/action before implementation detail;
- progressively disclosed;
- one primary operator job per artifact;
- concise in machine handoff;
- free of duplicated human/machine surfaces;
- explicit about candidate versus confirmed state;
- resilient to partial context without inventing certainty.

### Locked output relationships

The intended operator sequence is:

```text
confirmed project reality
    -> Weekly Command Brief
    -> PreCap Next Day Brief
    -> Flow Execution Card(s)
    -> directly usable prompt file(s)
    -> operator execution
    -> truthful evidence capture
    -> FlowRecap / candidate changes
    -> only necessary review/approval
    -> confirmed canonical state update
```

The full flow execution workspace contains three sprints. The day brief summarizes them. Prompt content is linked, not duplicated into the flow card. Large repetitive operator-facing Flow Prompt Packs are rejected by the validated prompt-file design.

---

## Macro problem diagnosis

### P1 — Presentation files were promoted without changing the behavior that creates outputs

The promotion map placed human-facing templates into owning skill packages but declared entrypoint updates unnecessary. The later activation run validated files/links/fixtures while changing no entrypoints, contracts, or runtime.

**Implication:** template existence is not activation. The owning skill entrypoint and/or runtime stage contract must explicitly require the intended operator artifact.

### P2 — Current stage entrypoints still encode stale output authority

Examples already verified:

- `PrecapWeek/SKILL.md` still centers `precap_week_output`, `first_precap_next_day_seed`, fixed project/rating structures, and schema validation; it does not make the promoted Weekly Command Brief template the primary operator output.
- `PrecapNextDay/SKILL.md` still makes `next_day_plan`, `flow_packet`, and `flow_prompt_pack` schema authorities and requires represented flows to have flow-prompt-pack references.
- degraded prompt behavior can create generic/placeholder prompt-pack structures when actual prompt generation is unavailable.

**Implication:** the stale behavior must be removed or subordinated. Adding more references to the human templates without removing conflicting requirements will preserve drift.

### P3 — Global Weekly Orchestrator contracts can force stale complexity downstream

The central Weekly Orchestrator currently routes G1-G5, validates a common handoff envelope, reads Session/Sync, and requires multiple packet-level authority/gate fields. Some of these may be valuable; others may be legacy architecture that causes every stage to serialize orchestration plumbing.

**Implication:** Module 00 must validate the central lifecycle first. Stage cleanup alone is insufficient if the central contract still requires stale packet machinery.

### P4 — Active stale files are dangerous even when a new design exists

Claude can discover and read project files dynamically. If old and new contracts remain adjacent and both look authoritative, a fresh session can reconstruct the wrong behavior.

**Implication:** superseded active contracts must be either:

- rewritten as the new authority;
- reduced to a compatibility-only internal contract with a named consumer; or
- moved to an explicit archive/history location.

Do not leave obsolete authoritative-looking files in active skill paths merely for history; Git plus the archive area preserves history.

---

## Macro target architecture

The project should aim for the smallest composition that satisfies the real workflow. The pending architecture research determines whether each custom stage agent remains necessary, but the authority model is independent of that choice.

### Canonical ownership model

**Weekly Orchestrator:** owns the lifecycle composition, stage routing, transaction boundaries, state/evidence distinction, persistence rules, real gate/review triggers, and recovery behavior.

**Stage/module owner:** owns how its stage transforms accepted inputs into its output and the detailed operator-facing artifact for that stage.

**Template/example:** demonstrates the required operator result and acts as an acceptance target; it does not independently define lifecycle authority.

**Deterministic helper:** computes reproducible evidence or validation only when that computation creates concrete value; it does not create a parallel operator workflow.

**Session/state authority:** owns confirmed durable state mutation.

### Single-authority rule

For every rule, identify one canonical active owner. Other files may reference that owner but must not restate an independently editable duplicate.

Examples:

- lifecycle order -> Weekly Orchestrator;
- Weekly Command Brief behavior -> PrecapWeek;
- Next Day Brief / Flow Execution preparation -> PrecapNextDay or whatever owner Module 00 confirms;
- prompt body creation -> PromptEngineer;
- AI surface routing -> AIRouting where actually required;
- FlowRecap interpretation -> flow-recap;
- durable mutation -> apex-session;
- deterministic blocker/dependency computation -> apex-sync only where retained.

---

## Macro migration strategy

### Phase A — Establish one corrected global spine

Before detailed output-module work, the Master must inspect and simplify:

- Weekly Orchestrator stage sequence;
- gate/review conditions;
- common handoff requirements;
- Session/Sync/ProjectStatus relationships;
- persistent versus ephemeral artifacts;
- agent/skill composition after the architecture research.

Do not perfect individual output layouts here. Establish only the interfaces needed for the intended lifecycle.

### Phase B — Make design authority executable, not decorative

For every operator-output module:

1. update the owning active entrypoint so the validated operator artifact is an explicit required runtime result;
2. make the approved template/example discoverable through that entrypoint;
3. remove or rewrite conflicting stale output requirements;
4. keep only the minimum machine contract required by the next consumer;
5. ensure the stage return presents the operator artifact first rather than only an envelope/summary;
6. make validation check the rendered/operator result and downstream contract, not merely file/link presence.

### Phase C — Retire stale authority

When a current active file conflicts with the corrected runtime:

1. identify its current consumers;
2. migrate any real required fields/behavior to the new owner;
3. update those consumers;
4. move the superseded file into the designated archive/history area with source path/date/replacement reference;
5. search the repo for remaining active references to the archived path;
6. fail the migration if an active runtime still treats it as authority.

### Phase D — Integrate production before testing

The operator has explicitly chosen:

```text
define -> integrate into production -> Master integration verification -> fresh runtime test -> operator review -> iterate
```

Do not substitute an isolated mock/example for the actual production implementation.

### Phase E — Fresh-context acceptance

After each module is integrated and independently verified by the Master, a fresh test session invokes the real production entrypoint against the existing W34 regression data.

The test prompt should contain only the normal runtime trigger and fixture/input references. It must not explain the intended output design. If the fresh runtime cannot produce the approved behavior without design-chat context, the implementation is not complete.

---

## Non-goals

Do not:

- build a second permanent master control plane above Weekly Orchestrator;
- create a new universal schema to replace the old universal schema;
- preserve every current packet for compatibility without finding a current consumer;
- add numeric scoring/ratings unless a real retained consumer requires them;
- use templates as passive documentation only;
- keep stale files in active paths because they might be useful later;
- redesign all output details inside Module 00;
- treat successful link/schema validation as proof that the intended user experience is active.

---

## Macro completion condition

Macro integration is conceptually complete when the repository has:

1. one coherent production lifecycle authority;
2. explicit module ownership and transaction boundaries;
3. the validated human-facing design encoded as active runtime requirements, not unused templates;
4. no known stale active contract that can reproduce the superseded schema-first operator experience;
5. a clear archive trail for removed architecture;
6. a fresh-context test path for each module;
7. bounded module handovers for detailed implementation.

The next file, `03-MESO-INTEGRATION-GUIDANCE.md`, translates this target into the concrete component-by-component migration map.
