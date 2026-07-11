# APEX Operator Template System - Research Findings

## 1. Executive synthesis

The accepted APEX architecture is not a chain of generic status cards. It is a controlled sequence of operator jobs that progressively transforms project truth into plans, execution context, evidence, interpretation, durable state, and advisory routing. The template system must therefore do two things at once:

1. create a recognizable human interface across the family; and
2. keep each artifact's authority, state vocabulary, and lifecycle boundary distinct.

The strongest design conclusion is that **consistency should live in presentation anatomy, not in a universal domain schema**. Every primary artifact can lead with result, next action, review need, material warning, provenance, and a minimal handoff. It cannot safely share one lifecycle enum, one approval meaning, or one generic content layout.

The repository evidence, operator user stories, prior research, and current external guidance all support a result-first, action-oriented, progressively disclosed Markdown system. They also support explicit uncertainty, direct links instead of duplication, a visible human decision before consequential transitions, and compact machine payloads placed after the human view.

## 2. Research method and authority handling

### 2.1 Evidence hierarchy used

1. Live owning skills and reference contracts for domain meaning and valid states.
2. Step 3 operator-output design package for presentation intent and cross-artifact relationships.
3. Step 2 user stories for operator problems and desired value.
4. Named project research and workflow examples for failure patterns and realistic stress tests.
5. Current web research for contemporary prompt and interface design, never to override APEX ownership.

### 2.2 Repository review strategy

The review began with the system foundations, Round 6 lifecycle and consistency resolutions, and the Step 4 handoff. It then moved by artifact group: planning, execution and evidence, recap and usage, and durable state and routing. Owning contracts were inspected where they affected state values, required handoffs, write boundaries, or forbidden claims.

The repository remained read only. No branch, patch, commit, issue, pull request, runtime file, skill package, calendar event, or durable state was created or changed.

### 2.3 Evidence identifiers used below

- `Rxx`: live repository sources.
- `Uxx`: Step 2 user-story sources.
- `Pxx`: named project sources.
- `Wxx`: current external sources.

## 3. Reconstructed APEX operating loop

```text
Project state
  -> weekly direction
  -> next-day outline
  -> executable flow
  -> prompt access
  -> execution evidence
  -> result interpretation
  -> usage learning
  -> status review
  -> durable KB update
  -> confirmed project overview
  -> advisory routing into later execution
```

### 3.1 Planning is not execution

J1 establishes planning-safe context. J2 sets weekly direction. J3 creates a compact day outline. None of these executes project work. J4 is the first complete single-flow execution workspace, but even J4 only prepares and guides operator execution. `R03`, `R06`, `R07`, `U02`.

**Template implication:** planning artifacts use outcome, sequence, and review language. J4 alone receives full tasks, inputs, dependencies, conditions, and resume point.

### 3.2 A summary is not a workspace

Round 6 explicitly corrects the J3/J4 depth boundary. J3 must keep three sprints visible but summarize them. J4 must make the same flow executable without requiring the operator to reconstruct details. `R06`, `R07`, `R17`.

**Template implication:** J3 has a short flow block with one line per sprint and a J4 link. J4 has three complete sprint workspaces. This is the most visible proof that the family is specialized rather than generic.

### 3.3 Evidence is not interpretation

J6 may organize, normalize, and assess readiness of evidence. J7 interprets that evidence into a flow result and candidate changes. `R09`, `R12`, `R18`.

**Template implication:** J6 contains no recommendation, recap judgment, or project-state conclusion. It presents planned versus actual facts, source references, gaps, conflicts, and readiness. J7 contains the interpretive result and labels any project change as candidate.

### 3.4 Candidate, approved, written, and confirmed are different

The durable-state path is deliberately four-stage:

```text
J7 candidate project-state change
  -> J9 operator merge decision
  -> J10 durable write and result
  -> J11 confirmed accepted project truth
```

Round 6 rejects shortcuts from completion to merge, approval to confirmed write, and prepared update to overview truth. `R04`, `R05`, `R13`, `R14`, `R15`, `R16`.

**Template implication:** each artifact displays both its own state and the next gate. J9 has a separate durable confirmation area. J10 requires a result reference before `executed` can feed J11. J11 excludes candidate entries.

### 3.5 Learning and routing remain advisory

J8 can extract a reusable, evidence-bound usage signal. J12 weighs that signal with current context and records an operator route decision. Neither can override routing automatically, and J12 recommendation alone does not authorize execution. `R04`, `R11`, `R16`.

**Template implication:** recommendation and operator decision are separate sections. Exact volatile model names are conditional on current verification; stable surface classes are the default.

## 4. Repository findings translated into design

### Finding 1: The first screen is an operator contract

The Step 3 principles require every primary output to answer what changed or is current, what happens next, what needs review, and any material warning within roughly ten seconds. `R01`, `R02`.

**Selected design:** a four-line blockquote result card at the top of every J1-J12 template. It is compact, renders consistently in common Markdown viewers, and is readable as plain text. J6a is exempt because its accepted design calls for one to three lines only.

### Finding 2: The result card reports value, not build status

Internal validation success is not the operator result. `R01`.

**Selected design:** `Outcome` describes planning readiness, work direction, evidence meaning, or durable effect. Technical validation appears at the end or only when failure changes the next action.

### Finding 3: Human-readable content must precede machine handoff

The shared anatomy makes the human layer the decision interface and the machine layer a minimum state-preserving projection. `R02`.

**Selected design:** each template ends with one compact YAML `presentation_handoff` and one static `template_authority` block. No template begins with YAML front matter or a schema dump.

### Finding 4: A universal state enum would erase ownership

Round 6 explicitly rejects one shared state enum. Execution result, candidate state, merge approval, durable write, overview truth, and route decision have different owners and meanings. `R04`.

**Selected design:** shared labels are limited to neutral result-card prompts. Each artifact supplies its own lifecycle language in the body and handoff.

### Finding 5: Links are the main anti-duplication mechanism

The execution design requires direct prompt links and visible path fallbacks. The wider architecture repeatedly says to reference upstream context rather than reprint it. `R07`, `R08`, `R12`.

**Selected design:** J3 links to J4; J4 links to J5 prompt files and routing references; J6 links to evidence; downstream cards link to source packets and result receipts. Related content is summarized in one line, not copied.

### Finding 6: J2 needs variable depth, not a fixed dashboard quota

The weekly design forbids arbitrary global caps and permits complexity to follow active projects, capacity, deadlines, and dependencies. `R06`, `U01`.

**Selected design:** repeatable project sections with compact bullets; no fixed number of projects or priorities in the template. The result card carries counts, while detail expands only as work requires.

### Finding 7: J3 must preserve all three sprints without becoming J4

The accepted day design requires S1, S2, and S3 visibility for each full active flow, but moves complete execution detail into J4. `R06`, `R17`.

**Selected design:** each J3 flow block contains a flow purpose, expected output, J4 reference, and three concise intent lines. No task lists, full input inventories, prompt bodies, or done/stop criteria appear.

### Finding 8: J4 needs an interruption-safe re-entry point

J4 is the primary operator workspace. A returning operator should not need to infer where to resume from completion notes scattered across the document. This follows the operator need to reduce re-reading and the design requirement for an exact next action. `R07`, `U02`, `P06`.

**Selected design:** `Start or resume here` sits immediately after the result card. Each sprint has a status and explicit completion and review conditions.

### Finding 9: J5 is an access layer, not a second execution plan

The accepted J5 design rejects the large repetitive Flow Prompt Pack as the operator surface. It retains one prompt per file plus a lightweight mapping. `R08`, `R12`.

**Selected design:** one J5 template contains a narrow prompt index and a reusable single-prompt-file skeleton. It omits full flow context, task sequence, expected outputs already owned by J4, and routing reasoning.

### Finding 10: Evidence normalization is conditional

J6 should use the lightest handoff that preserves evidence quality. Simple structured evidence can pass directly; fragmented or conflicting evidence is normalized first. `R09`.

**Selected design:** the first decision in J6 is `direct`, `normalize`, or `review/insufficient`. The remainder is the same evidence shape, avoiding two parallel artifact types.

### Finding 11: A skip is not partial or blocked execution

The Skip Marker exists only for a planned flow that was not executed and where downstream work needs the reason. `R10`.

**Selected design:** J6a has exactly flow identity, reason, handling, and optional review. It tells the author to use J6 instead when any execution evidence, artifact, decision, or blocker needs preservation.

### Finding 12: J7 must show interpretation without implying acceptance

The FlowRecap card interprets planned versus actual work and may propose one candidate project-state delta. Its approval language means ready for downstream review, not merged or written. `R10`, `R18`.

**Selected design:** a prominent `Candidate only` notice precedes the candidate delta. Downstream destinations and proposed next step remain advisory.

### Finding 13: J8 is contextual learning, not a benchmark

Usage quality is a lightweight observation for a comparable task, not a universal model ranking. Exactly one accepted route signal is selected, and current cost or quota claims require a source. `R11`.

**Selected design:** planned versus actual, evidence status, contextual quality, one route signal, and a short future hint. No usage ledger or quota dashboard appears.

### Finding 14: J9 approval must leave room for actual write evidence

The merge design includes approval states but Round 6 makes `merged` conditional on durable confirmation. `R13`, `R04`.

**Selected design:** the operator decision is captured first. A separate `Durable write confirmation` section stays `Not yet confirmed` until a J10 result reference exists.

### Finding 15: J10 must expose the write result, not just the intent

The KB update card is the durable-write boundary. Prepared, awaiting confirmation, executed, partially executed, skipped, and blocked are materially different. `R14`, `R19`.

**Selected design:** the template separates approved input, prepared update, write execution, actual durable result, effective change, freshness, and result reference. Only confirmed executed results are marked ready for J11.

### Finding 16: J11 is a projection of accepted truth, not a state editor

The live ProjectStatus contract uses project -> task -> subtask, ranked by manual override, deadline, priority, and urgency. The accepted presentation excludes a workstream layer and candidate acceptance. `R15`, `R20`.

**Selected design:** repeatable project cards plus a compact ranked task list and freshness. Entries that are stale or unconfirmed become review flags, not silent new truth.

### Finding 17: J12 should route by stable surface class

The live routing contract treats exact model availability, limits, and pricing as volatile. Round 6 requires current verification for an exact model claim. `R16`, `R21`.

**Selected design:** the default recommendation is a stable surface or tool class with alternatives. An optional exact-model line requires verification source, date, and validity window. The operator decision is captured separately.

### Finding 18: Template metadata is necessary but must stay secondary

The Step 4 handoff asks each implementation to identify source design, overlay intent, contract references, and overlay status. `R17`.

**Selected design:** static authority YAML closes each file. It is not front matter and does not compete with operator value.

### Finding 19: Missing context should degrade, not fabricate

Repository principles say partial context lowers confidence and creates a visible review flag but should not prevent a useful degraded output when safe interpretation remains possible. `R01`, `R02`.

**Selected design:** `None`, `Unknown`, `Not verified`, and exact missing evidence are valid visible values. Empty placeholders are not treated as certainty.

### Finding 20: Examples must be clearly non-authoritative

The Master of Arts workflow source provides useful varied work content but contains older Hermes, Kanban, cron, and orchestration assumptions that are not current APEX authority. `P09`.

**Selected design:** examples live in one separate document, every section is marked illustrative, and fragments demonstrate template use rather than adding fields or states.

## 5. Step 2 user-story findings

The user stories reveal the practical problems behind the architecture:

- The operator should not have to re-read entire project histories before planning. `U01`, `U02`.
- Weekly and daily artifacts must expose decisions and constraints before background. `U01`, `U02`.
- Execution needs one primary workspace and direct prompt access, not several competing packs. `U03`.
- Evidence collection must preserve messy reality without becoming interpretation. `U03`.
- Candidate changes must remain reviewable and reversible before durable writing. `U04`.
- Usage learning should be light enough to capture consistently and advisory enough to avoid automation drift. `U04`.
- The operator must see exactly what changed, what to do, and what remains uncertain. `U01`-`U05`.

**System-level implication:** the templates prioritize decisions and resumption over completeness theater. A section is valuable only if it improves the current operator job or the next handoff.

## 6. Named project-source findings

### 6.1 Earlier output attempts became table-first and schema-heavy

The prior PreCap template handover demonstrates the failure mode of machine structure becoming the primary interface. The orchestration source indexes explicitly warn against wide tables, schema dumps, path inventories, fake examples, implied execution, and treating PreCap as a database. `P03`, `P06`, `P07`.

**Design response:** tables are limited to the decision matrix, J5 prompt mapping, and genuinely comparable compact lists. Human cards and labeled bullets dominate templates.

### 6.2 Three parallel schemas create drift

The skill and prompt-flow handovers warn against duplicating concepts across prose requirements, examples, validation checklists, and manifests. `P04`, `P05`.

**Design response:** each template contains one human projection and one minimal handoff. Authority blocks reference contracts instead of reproducing them. Examples live separately.

### 6.3 Older lifecycle diagrams collapsed authority

The weekly routine and earlier orchestration material provide useful operating rhythm but sometimes compress recap, acceptance, and state writing into one step. `P06`, `P08`.

**Design response:** the durable-state strip is repeated in the README, overview, and the relevant templates. Repetition here protects a critical boundary rather than duplicating content.

### 6.4 Real workflows vary greatly in shape

The Master of Arts examples include portfolio prioritization, single-note transformation, workshop design, slide compression, embodied protocols, product-use-case translation, legal setup, and agent handover. `P09`.

**Design response:** templates use repeatable blocks and links rather than fixed project counts. Example fragments test both short transformation flows and high-risk multi-dependency work.

## 7. Current web research and concrete implications

### 7.1 GPT-5.6 and reasoning-model prompting

Current OpenAI guidance favors lean, direct prompts with context, hard constraints, approval boundaries, and success criteria stated once. It recommends straightforward instructions, delimiters, examples when needed, and iterative evaluation rather than asking the model to reveal chain-of-thought. `W01`-`W04`.

**Template implications:**

- prompt files separate role/context, task, constraints, inputs, required return, and stop/review conditions;
- operator templates state approval boundaries explicitly;
- long repeated doctrine is excluded;
- J5 uses one prompt per file so prompts can be tested and versioned without duplicating J4;
- template instructions are sparse and structural rather than essay-like.

### 7.2 Human-AI decision interfaces

Microsoft's HAX guidance emphasizes making capabilities and performance limits clear, showing contextually relevant information, supporting efficient invocation, dismissal, and correction, scoping when uncertain, explaining behavior, adapting cautiously, and conveying consequences. `W05`.

**Template implications:**

- every result card states what the artifact can support now and what requires review;
- valid correction actions are visible;
- uncertainty narrows or degrades the output instead of triggering an invented answer;
- J9, J10, and J12 show the consequences and limits of operator actions;
- candidate and advisory states are visibly scoped.

### 7.3 Uncertainty, provenance, and human oversight

NIST's Generative AI Profile highlights confabulation, information integrity, human-AI configuration, documented knowledge limits, provenance, human oversight, and tracing outputs and modifications to sources. `W13`.

**Template implications:**

- source references and freshness sit near consequential decisions;
- evidence gaps and conflicts remain explicit;
- J6 preserves source lineage before interpretation;
- J10 records a durable result reference;
- exact volatile route claims require verification;
- machine handoffs carry review status and confidence when material.

### 7.4 Progressive disclosure

GOV.UK guidance says optional details can make a page easier to scan, but content needed by most users should not be hidden. `W09`.

**Template implications:**

- decision, action, and review remain expanded and first;
- provenance, full source inventory, and technical validation move later;
- optional sections are labeled and removable rather than used to hide critical content;
- the package does not depend on HTML disclosure widgets to remain portable.

### 7.5 Cards versus tables

USWDS recommends cards for modular collections and warns against using cards as table rows or for continuous text. It recommends tables for genuinely tabular, consistently structured, brief data and advises minimizing columns. GOV.UK similarly distinguishes key-value summaries from tabular data. `W08`, `W11`, `W12`.

**Template implications:**

- project, flow, result, and route items are modular cards or headings;
- prompt mappings use a narrow table because rows are comparable;
- long narrative never sits inside table cells;
- the requested design decision matrix is intentionally wide because comparison is its dominant job, not because tables are a family default.

### 7.6 Accessible Markdown hierarchy

WCAG guidance says descriptive headings and labels help people orient and find content; link purpose should be understandable from context. CommonMark and GitHub documentation support a small portable Markdown subset. `W06`, `W07`, `W14`, `W15`.

**Template implications:**

- one H1 per artifact, then logical H2/H3 progression;
- no skipped levels in the blank templates;
- links use action-oriented labels such as `Open J4 flow card`, not `click here`;
- visible file paths serve as fallback;
- meaning is not conveyed by color or icon alone;
- plain blockquotes, lists, links, tables, and fenced YAML maximize renderer compatibility.

### 7.7 Material warnings should be exceptional and explicit

GOV.UK reserves warning text for important consequences. `W10`.

**Template implications:** warning callouts appear only when they change the next action, such as unconfirmed durable writing, insufficient evidence, a legal/professional gate, or an unverified exact model claim. Routine metadata is not styled as a warning.

### 7.8 Reusable template systems should remain testable

OpenAI prompt guidance supports versioned prompts and evaluations; GOV.UK emphasizes evidence for new patterns; the project handovers warn against manifests becoming second schemas. `W03`, `W04`, `W16`, `P04`, `P05`.

**Template implications:** the family uses stable filenames, separate examples, a lightweight manifest, parseable YAML blocks, and automated structural checks. The manifest inventories files and boundaries but does not redefine contract fields.

## 8. Source conflicts and resolutions

### Conflict A: J5 canonical name

The canonical lifecycle map still uses `Flow_Prompt_Pack`, while the package manifest and the accepted J5 design use `Prompt_Files_and_Index` and explicitly reject the large operator-facing pack.

**Resolution:** use `Prompt Files and Index` in the template family. Treat the live flow-prompt-pack contract as domain input projected into one prompt per file plus a lightweight index. `R00`, `R05`, `R08`.

### Conflict B: Round 6 patch application state

The package manifest and closeout record disagree about whether source designs were uniformly unmodified and whether patch artifacts were present. The Step 4 handoff instructs implementations to use files 20-22 and the recorded overlay intent without applying patches or assuming uniform application. `R00`, `R17`.

**Resolution:** templates state `intended_guidance_not_applied_by_this_package`. No repository source is described as patched by this run.

### Conflict C: Older batching restriction

The Step 4 handoff proposed implementing J3/J4 first and said later batches required separate authorization. It also says that sequence is guidance only and has no authorization effect. The current operator request explicitly authorizes all J1-J12 templates in one continuous run.

**Resolution:** create the complete family while preserving the J3/J4 validation priority. No repository mutation or runtime scope is expanded.

### Source gap D: Weekly plan output contract

The live `PrecapWeek` skill points to a weekly-plan output contract that was not retrievable from `main`.

**Resolution:** J2 uses the verified Step 3 design and live skill behavior. Its machine handoff is deliberately minimal and does not claim the missing schema.

### Source gap E: J1 and Prompt Engineering entrypoints

Repository search did not verify a dedicated J1 owner entrypoint or the expected Prompt Engineering skill entrypoint.

**Resolution:** J1 and J5 cite the accepted Step 3 designs plus adjacent live contracts. Required fields are not invented to fill the gap.

## 9. Consequential assumptions

1. The operator's current request authorizes the complete presentation package despite the earlier suggested batch sequence.
2. Round 6 files 20-22 and the overlay intents named in file 23 represent the intended presentation target, even where patches were not uniformly available.
3. A compact YAML presentation handoff is useful for downstream AI consumption but is not itself a domain packet.
4. Static template authority blocks are implementation metadata and should remain after filling; optional author guidance may be removed.
5. Example fragments may use realistic but fictionalized outcomes derived from the workflow database, provided they are never presented as current project truth.

## 10. Evidence register

### Live repository sources

- `R00` - `apex-meta/operator-output-design/step3-output-design-system/00-package-manifest.okf.yaml`
- `R01` - `01-operator-output-design-principles.okf.yaml`
- `R02` - `02-shared-card-and-brief-anatomy.okf.yaml`
- `R03` - `03-planning-artifact-designs.okf.yaml`
- `R04` - `20-round6-cross-cutting-consistency-resolution.okf.yaml`
- `R05` - `21-canonical-artifact-family-and-lifecycle-map.okf.yaml`
- `R06` - `22-round6-decision-and-verification-record.okf.yaml`
- `R07` - `04-flow-execution-card-design.okf.yaml`
- `R08` - `05-prompt-file-and-index-design.okf.yaml`
- `R09` - `06-execution-evidence-handoff-design.okf.yaml`
- `R10` - `07-skip-marker-low-priority-design.okf.yaml`
- `R11` - `11-usage-learning-card-design.okf.yaml`
- `R12` - `08-round3-cross-artifact-relationship.okf.yaml`
- `R13` - `14-status-merge-decision-card-design.okf.yaml`
- `R14` - `15-project-kb-update-card-design.okf.yaml`
- `R15` - `16-project-status-overview-design.okf.yaml`
- `R16` - `17-ai-routing-card-design.okf.yaml`
- `R17` - `23-step4-template-implementation-handoff.okf.md`
- `R18` - `10-flow-recap-result-card-design.okf.yaml`
- `R19` - `.claude/skills/project-kb-manager/SKILL.md` and `references/write-rules.md`
- `R20` - `.claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md` and `project-status-overview-contract_v2_fixed.md`
- `R21` - `.claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md` and `routing-recommendation-packet-contract.md`
- Additional domain authorities: PrecapWeek, PrecapNextDay, raw-flow-dump-normalize, flow-recap, model-usage-log, and status-merge skills and contracts under `.claude/skills/`.

### Step 2 user stories

- `U01` - `02-macro-loop-and-value-frame.okf.yaml`
- `U02` - `03-planning-side-user-stories.okf.yaml`
- `U03` - `04-execution-recap-user-stories.okf.yaml`
- `U04` - `05-status-learning-user-stories.okf.yaml`
- `U05` - `06-output-jobs-and-artifact-family.okf.yaml`

### Named project sources

- `P01` - `deep-research-report (11)(2).md`
- `P02` - `deep-research-report (12).md`
- `P03` - `APEX_PreCapNextDay_OutputTemplates_Handover.md`
- `P04` - `Claude_Skill_Package_BestPractice_Handover.md`
- `P05` - `Claude_Skill_PromptFlow_Design_Guidance_v1.md`
- `P06` - `WeeklyRoutine_Overview_Marco&Meso.md`
- `P07` - `weekly-orchestration-source-index-v0.1.md`
- `P08` - `weekly-orchestration-skills-source-index-v0.2.md`
- `P09` - `Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md`

### Current web sources

- `W01` - OpenAI, [Model guidance: Using GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model)
- `W02` - OpenAI, [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- `W03` - OpenAI, [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- `W04` - OpenAI, [GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)
- `W05` - Microsoft HAX Toolkit, [18 Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/library/)
- `W06` - W3C WAI, [Understanding Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)
- `W07` - W3C WAI, [Understanding Link Purpose in Context](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)
- `W08` - GOV.UK Design System, [Summary list](https://design-system.service.gov.uk/components/summary-list/)
- `W09` - GOV.UK Design System, [Details](https://design-system.service.gov.uk/components/details/)
- `W10` - GOV.UK Design System, [Warning text](https://design-system.service.gov.uk/components/warning-text/)
- `W11` - U.S. Web Design System, [Card](https://designsystem.digital.gov/components/card/)
- `W12` - U.S. Web Design System, [Table](https://designsystem.digital.gov/components/table/)
- `W13` - NIST, [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- `W14` - CommonMark, [Markdown Reference](https://commonmark.org/help/)
- `W15` - GitHub Docs, [Organizing information with tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)
- `W16` - GOV.UK Service Manual, [Making your service look like GOV.UK](https://www.gov.uk/service-manual/design/making-your-service-look-like-govuk)
