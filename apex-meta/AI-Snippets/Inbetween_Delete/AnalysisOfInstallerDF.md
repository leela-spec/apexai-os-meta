I’ll use the QMD and OpenMausBot operations guidance to compare the package with Lila’s documented architecture, then map each component’s role, overlap, dependencies, and integration order. This is analysis only; I won’t install or change anything.

9:09 PM

Leela already gives OpenProject ownership of current work and Git ownership of code and specifications. I also verified that the existing OpenProject is reachable. A key distinction emerged: the Archon revision named by this package is a workflow execution engine, while Apache AGE is only the graph database—it needs an ingestion process before it can answer questions about Leela’s code.

9:10 PM

**Dark Software Factory should supplement Leela component by component. The complete installer is unsuitable for that integration because it provisions services Leela already has and does not establish the connections Leela needs.**

I checked Leela’s indexed architecture, its current repository instructions, the package, and upstream documentation today. I also verified the existing OpenProject: version **17.8.0**, with the Leela project and its feature subprojects reachable. Everything remained read-only.

**The existing architecture determines where each component belongs.**

Leela already separates three responsibilities:

- **OpenProject:** selected work, ownership, priorities, and dependencies.
- **Git, specifications, and materialization ledgers:** implementation, product intent, decisions, and build state.
- **Tests and repository gates:** evidence that the implementation works.

Those distinctions are explicit in the live Leela instructions. Earlier orchestration research contains proposed architectures and historical work queues; I did not treat those as current configuration.

| Component                    | What it contributes                                                               | Fit with Leela                                                              |
| ---------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Archon**                   | Executes workflows containing agents, scripts, checks, loops, and human decisions | A candidate execution engine; overlaps with OpenMausBot’s coordination role |
| **OpenProject**              | Tracks and organizes work                                                         | Reuse the existing instance                                                 |
| **Apache AGE / “CodeGraph”** | Stores and queries relationships                                                  | Optional derived code/dependency index                                      |
| **QMD**                      | Retrieves relevant documents and source passages                                  | Retain the existing retrieval system                                        |
| **Langfuse**                 | Records and analyzes AI execution traces                                          | Optional observability                                                      |
| **Local Git storage**        | Supplies repositories for execution and delivery                                  | Reuse the existing repository; avoid a competing canonical repository       |

**Archon is the orchestration candidate—not another task database.**

The package’s named revision, `1f4d265e`, describes a workflow engine that runs coding assistants, deterministic commands, loops, and approval steps. The older Archon knowledge/RAG product is a separate archived version. [Archon at the package’s named revision](https://raw.githubusercontent.com/coleam00/Archon/1f4d265e/README.md)

Its potential value is making an agreed development process executable and resumable: retrieve the task, gather context, implement, validate, review, and report evidence.

For Leela, I propose this division:

- OpenMausBot remains your point of contact.
- OpenProject supplies the authorized task.
- Archon, **if a pilot proves useful**, executes that bounded task.
- Existing Leela instructions, acceptance criteria, and gates govern the result.

OpenMausBot and Archon should not independently schedule, retry, or approve the same work. One must own execution for each run. A working connection between them has not been demonstrated.

**OpenProject needs a workflow connection, not another installation.**

Your existing OpenProject should remain the operational owner. “Priming” it would mean agreeing how an executor recognizes eligible work and records results: project, work-package ID, scope, dependencies, status transitions, and evidence links.

Initially, that connection should only read a selected work package. Later, an authorized execution could return a run reference, commit reference, validation results, and any blocker. It should use the existing supported client rather than modify the database.

The package instead provisions another OpenProject on port `18084`; it does not configure a connection to your existing one on `8083`.

**“CodeGraph” is supplementary to QMD, but the package supplies only its storage foundation.**

Apache AGE adds nodes, edges, and graph traversal to PostgreSQL. It does not automatically parse a repository or discover dependencies. [Apache AGE documentation](https://age.apache.org/)

The package’s initialization file enables AGE and creates `code_graph`. That establishes a graph container; it does not populate a code graph.

|Question|Existing QMD|Proposed code graph|
|---|---|---|
|“Why did we choose this architecture?”|Retrieves decisions and explanations|Useful only if those relationships are explicitly modeled|
|“Which functions transitively depend on this symbol?”|Can find mentions; does not establish complete dependencies|Useful with a reliable parser and dependency extractor|
|Setup and maintenance|Already available|Requires extraction, schema, updates, and query access|
|Main failure|Missing or outdated indexed content|Missing, incorrect, or stale relationships|
|Grounding|Open the retrieved originating source|Resolve graph results to their source and indexed commit|

Leela already has explicit rule-to-artifact mappings and deterministic `--rule` / `--target` lookup mechanisms. A graph should add relationships those mechanisms cannot answer efficiently, rather than recreate them.

The first unresolved requirement is **accurate Dart support**. Neither an AGE database nor the package’s bootstrap proves that. Any graph must remain rebuildable from authoritative sources, record its indexed revision, and expose stale results clearly.

**Langfuse observes execution; installing it does not create instrumentation.**

Langfuse captures traces such as model calls, tool activity, latency, token usage, and evaluation results. It can help answer, “Which step failed or consumed the budget?” [Langfuse observability documentation](https://langfuse.com/docs/observability/overview)

Its integration would require the executor to emit correlated traces. A shared run reference could link an OpenProject task, execution, and resulting commit. That connection is not demonstrated by this package.

Self-hosting also adds operational dependencies: the package includes web and worker services, PostgreSQL, ClickHouse, Redis, and object storage. I would defer it until existing execution records fail to answer a concrete debugging or measurement question.

**Existing Git storage should remain canonical.**

The package’s repository setup creates another bare repository and directories. That alone does not connect Leela’s history, its remote, review process, or delivery permissions.

An executor needs an explicitly selected checkout and branch strategy. Archon’s default worktree behavior needs reconciliation with Leela’s current rules, which permit harness-created worktrees but restrict manual ones. Leela Git rules

**The installer also contains an additional database integration hazard.**

Archon receives the same `.env` file that defines OpenProject’s `DATABASE_URL`. Archon interprets that variable as its own database configuration. Consequently, the package can direct both applications into the OpenProject database. This is a configuration risk identified by inspection, not an observed database change. Package configuration, [Archon database behavior](https://archon.diy/reference/database/)

Archon’s execution state would need separate storage. Reusing an OpenProject **service through its API** does not mean reusing its application database.

**I propose this modular integration sequence. Each stage must work before connecting the next.**

|Stage|Proposed scope|Evidence required before proceeding|
|---|---|---|
|**1. Establish the baseline**|Identify the existing task, repository, retrieval paths, execution owner, and acceptance checks|One real task can be traced through existing owners|
|**2. Test the OpenProject boundary**|Read one selected task through the existing client|Correct scope, dependencies, and originating artifacts; no writes|
|**3. Evaluate Archon alone**|Exact reviewed version, separate state, disposable repository, manually started workflow|Start, pause, resume, failure, and cancellation behave correctly|
|**4. Connect context retrieval**|Give that workflow access to relevant Leela sources|It finds current decisions and distinguishes historical proposals|
|**5. Complete one bounded development task**|One execution owner; existing Leela validation and delivery rules|Reviewable change, actual validation evidence, accurate reporting|
|**6. Evaluate the graph separately**|One Dart module and a few independently checked dependency questions|Correct relationships and a demonstrated advantage over existing lookup|
|**7. Add observability if justified**|Instrument the proven workflow|A trace explains a real execution problem|
|**8. Test interdependencies**|Restart, retry, duplicate submission, stale context, unavailable optional services|No duplicate work, lost approvals, or competing task state|

QMD and code-graph retrieval would be parallel context sources. Langfuse would observe execution. Neither should become a prerequisite for selecting work in OpenProject or preserving code in Git.

My recommendation is **reuse the existing foundation, then evaluate Archon with one bounded workflow**. Relative judgment estimates—not benchmark results—are:

|Approach|Impact / Evidence / Risk, 0–100|
|---|---|
|Reuse existing owners and adopt useful mechanisms incrementally|**85 / 90 / 15**|
|Pilot Archon as an optional executor|**80 / 60 / 45**|
|Install the complete package into the existing environment|**40 / 85 / 90**|

The complete package duplicates infrastructure and couples databases before proving the workflow. The immediate deliverable should therefore be a tested execution boundary for one task, with the package preserved unchanged.