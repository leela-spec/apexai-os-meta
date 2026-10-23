---
type: OperationalPatternCandidate
title: Source-Governed Execution Contract Candidate
description: Candidate pre-execution task contract that binds user input, source authority, transformation process, expected output, and source-coverage validation before complex AI work begins.
status: candidate_not_integrated
created: 2026-09-08
scope: operational_companion_cross_module
---

# Source-Governed Execution Contract Candidate

## 1. Problem

A recurring agent failure is not simply bad research or verbose communication. The operator can provide precise source material and still receive an answer that quietly prioritizes unrelated model knowledge, newly discovered sources, generic best practice, or whichever source the model happened to find easiest to use.

The missing control is a **pre-execution task contract** that makes four things explicit before substantial work begins:

1. **INPUT** — what material the task is actually based on;
2. **SOURCE AUTHORITY** — which inputs govern, which support, which may only be used for discovery, and which must not displace the requested basis;
3. **PROCESS** — what transformation or execution must be performed on that input;
4. **OUTPUT** — what concrete result will be produced, at roughly what depth and in what structure.

The contract must also make source usage auditable after execution so that a model cannot satisfy the prompt superficially while silently ignoring a required source.

This is **not primarily an A12 communication rule**. A12 controls user-facing information economy. This pattern composes A05, A08, A11, A12, A13, C01/C02, and the Human-AI Complex Task Execution guide into a task-level operating contract.

---

# 2. Existing proven basis

There is no single universal industry standard that exactly matches "input + ranked sources + process + output" for AI tasks. However, the requested behavior is strongly supported by several established and battle-tested patterns. The correct approach is to compose those patterns rather than invent an unrelated methodology.

## 2.1 OpenAI — outcome, evidence, constraints, output, stop rules

Current OpenAI model guidance recommends defining the expected outcome, success criteria, constraints, available evidence/context, output shape, and stopping conditions while avoiding unnecessary procedural micromanagement.

Relevant guidance:

- GPT-5.5: state expected outcome and success criteria; define constraints, available evidence, output, and stop rules; leave the exact path open unless the path itself matters.
- Current OpenAI model guidance: make instruction priority explicit where multiple instruction sources or Skills can conflict.
- OpenAI long-context prompting examples distinguish instructions from supplied external context and can explicitly constrain the model to the provided context where required.

Primary references:

- https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5
- https://developers.openai.com/api/docs/guides/latest-model
- https://learn.chatgpt.com/docs/prompting

## 2.2 Anthropic — structured prompt sections and source metadata

Anthropic explicitly recommends structuring complex prompts with descriptive XML tags so the model can distinguish instructions, context, inputs, examples, and outputs. For multi-document work, Anthropic recommends document-level metadata such as source identifiers and grounding the response in the supplied documents.

Portable lesson:

> distinguish the semantic role of each input instead of placing all material in one undifferentiated context block.

Primary reference:

- https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

## 2.3 Gemini — role / constraints / context / task / output structure

Gemini prompt guidance independently recommends consistent structured sections, prioritizing critical instructions, separating context from task instructions, and explicitly defining output format.

Primary reference:

- https://ai.google.dev/gemini-api/docs/prompting-strategies

## 2.4 GitHub Spec Kit — authoritative intent chain and traceability

GitHub Spec Kit operationalizes a comparable discipline for software work:

```text
constitution -> specification -> plan -> tasks -> implementation -> convergence
```

The constitution provides governing constraints; specification and plan define intent; tasks remain traceable to those artifacts; convergence checks implementation against the authoritative intent artifacts rather than treating code or tests as self-authenticating proof.

Spec Kit also uses explicit priorities such as P1/P2/P3 for user stories, but those are **work priorities**, not generic numerical source-confidence scores.

Primary references:

- https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md
- https://github.com/github/spec-kit/blob/main/templates/commands/converge.md
- https://github.com/github/spec-kit/blob/main/templates/commands/tasks.md

## 2.5 Established supporting concepts

The contract also reuses established non-AI vocabulary rather than introducing new semantics:

- **Input-Process-Output (IPO):** explicit distinction between supplied material, transformation, and result.
- **Source authority / hierarchy:** not all sources have equal governing force.
- **Requirements traceability:** downstream work remains connected to originating requirements/sources.
- **Acceptance criteria / Definition of Done:** output is validated against the intended result rather than artifact existence.

---

# 3. Design decision: do not use 1-10 as the primary source authority mechanism

A free-form numerical score such as `8/10` versus `9/10` appears precise but creates a new ambiguity:

- Does 10 mean legally binding, user-preferred, current, highly trustworthy, or all of those?
- Can a large number of lower-ranked sources outweigh one higher-ranked source?
- Is the difference between 7 and 8 meaningful?
- Does a model have permission to override a user-designated 10 with an official source it considers newer?

The primary mechanism should therefore be **categorical authority + usage policy**.

A numeric rank may be retained only as a secondary ordering aid inside one tier when needed.

---

# 4. Source authority model

## 4.1 Authority tiers

| Tier | Name | Meaning | Default behavior |
|---|---|---|---|
| **P0** | Governing / Binding | Source explicitly designated by the operator or current project authority as controlling the task | MUST be used. Cannot be silently displaced by P1-P3 material. |
| **P1** | Primary / Authoritative | Current official, canonical, or directly observed source used to interpret, verify, or operationalize the task | Use for load-bearing claims when relevant. May challenge P0 only when the task explicitly asks for verification/correction. |
| **P2** | Supporting | Useful secondary material, prior research, examples, or complementary evidence | Use where it adds supported detail without changing P0/P1 intent. |
| **P3** | Discovery / Leads | Search results, community discussion, model suggestions, unverified leads | May identify what to inspect next; must not independently support a load-bearing conclusion. |
| **X** | Excluded | Material the operator explicitly does not want governing or entering the task | Do not use except to explain a requested contrast. |

## 4.2 Usage role

Authority and usage are separate fields.

Each source should also receive one of:

- `must-use` — omission is a task failure unless the source is inaccessible;
- `use-if-relevant` — use when its subject matter actually bears on the target;
- `verification-only` — may check/challenge a claim but must not silently redefine the task;
- `discovery-only` — may generate leads, not final claims;
- `background-only` — context, not governing evidence;
- `excluded` — must not be used as task support.

This prevents a common failure where an agent reads a requested source but then allows unrelated material to become the real basis of the answer.

---

# 5. Source conflict rules

1. **Explicit operator priority wins over default model preference.** If the operator says a document is the primary basis, the model may not silently substitute a source it personally considers more useful.
2. **P0 must be consumed before dependent reasoning.** A source marked P0/must-use cannot be skipped because another source appears easier or more detailed.
3. **Verification does not equal replacement.** If the task asks to verify P0 against external reality and a P1 source conflicts with it, expose the conflict. Do not silently rewrite P0 into the external source's position.
4. **Conflicting P0 sources require resolution.** Follow explicit internal precedence if provided; otherwise surface the conflict rather than synthesizing an invented compromise.
5. **P2/P3 cannot overrule P0/P1 by volume.** Ten weak sources do not automatically outrank one governing source.
6. **Unsupported gaps stay gaps unless expansion is authorized.** If required sources do not support a point, say so. Do not fill it with model knowledge unless the contract permits outside context.
7. **Freshness and authority are distinct.** Newer is not automatically more authoritative; more authoritative is not automatically current. When both matter, record both.

---

# 6. The Source-Governed Execution Contract

Use this only for tasks where source choice, transformation discipline, or output expectations materially affect correctness. Do not force it onto trivial rewrites or simple factual questions.

```xml
<execution_contract>
  <target>
    [One sentence: substantive useful outcome]
  </target>

  <input>
    <primary_request>
      [Operator request / problem statement]
    </primary_request>

    <sources>
      <source id="S1"
              authority="P0"
              use="must-use"
              role="governing-framework"
              freshness="current-or-specified-version">
        [Exact file, URL, repository path, dataset, or supplied document]
      </source>

      <source id="S2"
              authority="P1"
              use="verification-only"
              role="official-current-guidance">
        [Source]
      </source>

      <source id="S3"
              authority="P2"
              use="use-if-relevant"
              role="supporting-context">
        [Source]
      </source>
    </sources>

    <outside_context policy="forbidden|gap-only|verification-only|allowed">
      [What model knowledge/web research may and may not contribute]
    </outside_context>
  </input>

  <process>
    <operation>
      [summarize | compare | transform | synthesize | research | design | implement | audit]
    </operation>

    <source_use_rules>
      [How P0-P3 sources must be used; conflict behavior; citation/traceability needs]
    </source_use_rules>

    <required_steps>
      [Only steps whose order/completeness genuinely matters]
    </required_steps>

    <non_goals>
      [What must not be optimized, redesigned, introduced, or silently corrected]
    </non_goals>
  </process>

  <output>
    <artifact>
      [report | answer | implementation plan | patch | document | decision packet | etc.]
    </artifact>

    <structure>
      [Required sections / table / schema]
    </structure>

    <depth>
      [brief | standard | deep, plus approximate word/page/section range when useful]
    </depth>

    <evidence_visibility>
      [citations | source IDs | traceability table | no citations needed]
    </evidence_visibility>

    <audience>
      [operator | developer | executive | student | public reader | machine]
    </audience>
  </output>

  <validation>
    <source_coverage>
      Every must-use source is either materially used or explicitly reported inaccessible/not applicable.
    </source_coverage>

    <target_check>
      The produced artifact satisfies the substantive target, not merely the requested format.
    </target_check>

    <deviation_report>
      Report any material departure from source priority, process, scope, or output contract and why.
    </deviation_report>
  </validation>
</execution_contract>
```

---

# 7. Compact human-facing preflight

For complex work, the orchestrator should be able to show the resolved contract in a four-row summary before substantial execution begins.

This is **orientation, not a mandatory approval gate**. If the contract is clear and the work is authorized, continue. Ask only when unresolved ambiguity could materially change the outcome or authority boundary.

| Field | Preflight content |
|---|---|
| **Input** | What the task is based on |
| **Source order** | P0 governing → P1 primary/verification → P2 supporting → P3 discovery; note must-use sources |
| **Process** | What will be done to the input and what will not be done |
| **Output** | Artifact type, structure, approximate depth, evidence visibility |

Example:

```text
INPUT
- Learning framework v3 is the governing conceptual structure.
- Two supporting documents provide secondary detail.

SOURCE ORDER
- P0 / must-use: LearningHowToLearn vProcess_3
- P1 / must-use where relevant: Gliederung für Prozesssicht
- P2 / supporting: Meta Frame
- P2 / verification-only: current external learning-science evidence
- Model knowledge: gap-only; may not replace the P0 structure

PROCESS
- Preserve the P0 chapter logic.
- Map supporting concepts into that structure.
- Flag unsupported/conflicting claims rather than silently replacing them.
- Use external research only to verify or enrich identified gaps.

OUTPUT
- Publication-ready framework architecture
- Macro chapter map + meso concepts + micro claims/examples
- ~8-12 major sections
- source traceability for load-bearing claims
```

This gives the human a real model of what the AI is about to do before substantial execution starts.

---

# 8. Mandatory source-coverage check

The most important anti-drift mechanism is not the preflight itself. It is the **post-execution coverage check**.

For every `must-use` source, record:

| Source | Authority | Required use | Actually used? | Where it affected the result | Gap/deviation |
|---|---|---|---|---|---|
| S1 | P0 | governing framework | yes/no | sections/decisions | reason if no |
| S2 | P1 | verification | yes/no | claims/decisions | reason if no |

A final answer that ignores a `must-use` source fails the contract even if the prose sounds plausible.

This converts source adherence from an aspirational prompt instruction into an observable acceptance criterion.

---

# 9. Interaction with the Universal AI Instruction System

This pattern should not become another large always-loaded module.

| Existing owner | Contribution to the contract |
|---|---|
| A01 `<target>` | substantive outcome and anti-proxy completion |
| A05 `<intent>` | unresolved ambiguity threshold |
| A06 `<context>` | load only the sources needed for the current step |
| A08 `<evidence>` | claim-evidence traceability and uncertainty |
| A11 `<current_truth>` | source authority, precedence, and stale-state handling |
| A12 `<communication>` | compact preflight and useful final visibility |
| A13 `<grounding>` | when external reality must be consulted |
| C01 `<decision>` | material alternatives requiring operator choice |
| C02 `<research>` | deeper external research method |
| `13-HUMAN-AI-COMPLEX-TASK-EXECUTION.md` | natural operational owner for building the contract |

The likely long-term owner is therefore the **Human-AI Complex Task Execution guide / Execution Packet**, not the root constitution.

---

# 10. Proposed integration into the Human-AI Complex Task Execution guide

Do not edit the existing guide through a whole-file browser connector rewrite. When integration is authorized through a patch-capable executor, make two bounded changes.

## Change A — add Source Contract to complex-task preflight

After the current target/current-truth/scope preflight, add:

```text
SOURCE CONTRACT
- enumerate operator-provided and required project sources;
- assign authority tier and usage role;
- define whether outside knowledge/research may supplement, verify, or replace them;
- define conflict behavior;
- mark all must-use sources.
```

## Change B — extend the Execution Packet

Before `EXECUTION METHOD`, add:

```text
SOURCE AUTHORITY / INPUT CONTRACT
- P0 governing sources
- P1 authoritative/verification sources
- P2 supporting sources
- P3 discovery-only sources
- excluded sources
- outside-context policy
- conflict rules
- must-use source coverage requirement
```

Then add the source-coverage table to the final validation/report requirements.

---

# 11. Evaluation scenarios

The pattern should be tested before canonical integration.

## Scenario A — user gives three files with explicit priority

Expected:
- P0 structure governs;
- P1/P2 enrich it;
- model does not reorganize around generic external best practice;
- final coverage check proves all must-use inputs influenced the output.

## Scenario B — P0 source conflicts with current official evidence

If task = "transform based on P0": preserve P0 and flag the external conflict separately.

If task = "verify/correct P0": use P1 evidence to challenge it, expose the conflict, and recommend the correction without pretending P0 already said it.

## Scenario C — P0 lacks information needed for requested output

If outside context = forbidden: state the gap.

If outside context = gap-only: fill only the identified gap and label the addition.

## Scenario D — many attractive external sources appear

Expected:
- P2/P3 volume does not displace P0;
- external material is used only according to the contract;
- the agent does not optimize for novelty or source abundance.

## Scenario E — simple rewrite

Expected:
- no visible contract ceremony;
- supplied text is implicitly P0;
- task executes directly.

---

# 12. Acceptance criteria for this candidate

Keep this pattern only if controlled tests show that it materially improves:

1. use of explicitly supplied sources;
2. preservation of user-defined source priority;
3. resistance to unrelated-source drift;
4. transparency when sources conflict;
5. source-to-output traceability;
6. predictability of output scope and depth;
7. user understanding of what will happen before execution;

without causing:

1. unnecessary preflight ceremony on simple tasks;
2. false numerical precision;
3. excessive source loading;
4. suppression of useful external verification when the task explicitly asks for it;
5. rigid process sequencing where only the outcome matters.

---

# 13. Current recommendation

**Keep as an operational candidate and test it with the Human-AI Complex Task Execution guide. Do not add a new always-on A-module yet.**

The strongest practical form is:

```text
TARGET
  ↓
INPUT + SOURCE AUTHORITY
  ↓
PROCESS / TRANSFORMATION CONTRACT
  ↓
EXPECTED OUTPUT CONTRACT
  ↓
EXECUTION
  ↓
SOURCE-COVERAGE + TARGET VALIDATION
```

This directly addresses the operator failure mode: an AI should not be able to receive carefully selected sources, silently prefer something else, and still claim task completion merely because it produced a plausible-looking answer.
