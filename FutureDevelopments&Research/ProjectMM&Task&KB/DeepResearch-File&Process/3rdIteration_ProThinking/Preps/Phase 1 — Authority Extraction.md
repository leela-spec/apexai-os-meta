# Phase 1 Complete — Authority Extraction

## 0. Scope executed

**Phase 1 goal:** Extract the binding authority layer only.

I did **not** generate package files, write repo files, or perform full mechanism extraction. This phase extracted:

- authority hierarchy
- H1–H7 lock decisions
- ProThinking source ledger
- evidence categories
- all 20 process best-source selections
- cluster assignments
- explicit gaps/custom-build requirements

---

## 1. Authority hierarchy extracted

|Tier|Authority|Binding meaning|
|---|---|---|
|**1**|`ProThinkingGPT_Harmonization_v1.md`|Primary source for the source ledger, evidence matrix, 20 process options, best options, copy types, needs-script decisions, and priority ranks. It contains the source ledger beginning with S1a–S9b.|
|**2**|`APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md`|Lockfile for H1–H7 and local-path expectations. It states ProThinking is binding and that source evidence must be read locally rather than fetched externally.|
|**3**|Repo content|Implementation target and local mirrored source corpus.|

**Binding interpretation:** ProThinking defines the **selection and rationale**, but later phases must still read actual local files before treating mechanisms as validated.

---

## 2. H1–H7 lock decisions extracted

|Lock|Decision|Generation constraint|
|---|---|---|
|**H1**|Status enum = `open`, `in-progress`, `blocked`, `done`, `deferred`|All Apex task/status files and generated skills must use this exact enum.|
|**H2**|Base path = `apex-meta/` with `harmonization/`, `epics/`, `handoff/`, `registry/`; scripts under `scripts/`; skills under `.claude/skills/`|No generated package may invent a different state root.|
|**H3**|Dependency field = `depends_on`, type int array|Actionability requires all `depends_on` IDs to have `status=done`.|
|**H4**|Script language = Python only|No Bash/TypeScript scripts in Apex final implementation.|
|**H5**|Clusters: A_PLAN, B_SYNC, C_SESSION|`apex-plan`, `apex-sync`, `apex-session` must map to those process groups.|
|**H6**|Handoff files = `task_plan.md`, `findings.md`, `progress.md`, `next-session.md` under `apex-meta/handoff/`|`next-session.md` must include Current Step, Open Items, Risks, Decisions Made, Next Actions.|
|**H7**|Priority = `high/medium/low`; urgency = ISO8601 `due_date`, scored by days-until-due with `None=999`|Ranking/scoring must adapt to this, not invent a separate scale.|

---

## 3. Source ledger extracted from ProThinking

|Source ID|Source label|Used for|ProThinking copy posture|
|---|---|---|---|
|**S1a**|CCPM `SKILL.md`|PM2, PM3, PM4, PM5, PM6, PM8, PD4|ADAPT / lifecycle and script-first pattern|
|**S1b**|CCPM `structure.md`|PM2, PM3, PM4, PM5, PM8, PD3|ADAPT / decomposition and dependency structure|
|**S1c**|CCPM `track.md`|PM4, PM5, PM6, PM8, KB5, PD4|ADAPT / status, next, blocked, validate pattern|
|**S2a**|Backlog example task|PM1, PM6, PM8, PD5|ADAPT / Markdown task contract|
|**S2b**|Backlog `types/index.ts`|PM1, PM6, PM8, KB2, PD5|ADAPT / canonical task fields|
|**S2c**|Backlog parser|PM1, PM6, KB2, PD5|ADAPT / frontmatter/body extraction|
|**S3a–S3c**|Task Master schema + next-task algorithm|PM3, PM4, PM5, PD1, PD3, PD4|ADAPT / dependency and ranking algorithm|
|**S4a–S4b**|planning-with-files|PM7, KB1, KB2, KB5, KB6, PD6|FULL / ADAPT / CONCEPT depending process|
|**S5a–S5c**|Kanban skill + scripts|PM3, PM5, PM6, PM7, PD2|FULL or ADAPT depending script|
|**S6a–S6b**|llm-wiki skill + update-index|KB3, KB4, KB5, PM8|ADAPT / FULL for index pattern|
|**S7a**|OpenClaw taskflow|PM7, KB6, PD6|CONCEPT / persisted state|
|**S8a–S8b**|CrewAI skills|KB2, PD4, PD5, PD6|ADAPT / expected output, human gate, output file|
|**S9a–S9b**|Hermes skill hub/guard|PD5 governance|Governance support only|

The first source ledger explicitly records these IDs, source URLs, evidence extracted, limitations, and process use.

---

## 4. Evidence categories extracted

|Evidence category|Binding source pattern|Script boundary|
|---|---|---|
|Markdown/YAML task contract|Backlog + Kanban|Script optional for typed parsing / bulk updates|
|Dependency graph|CCPM + Task Master + Backlog|**Script required** for exact traversal|
|Blocker detection|Kanban + CCPM|**Script required** for exact multi-file detection|
|Next-action computation|Task Master + CCPM|**Script required**|
|Status update|Backlog + Kanban + CCPM|Single-file update may be instruction-only; batch propagation may need script|
|Stall detection|planning-with-files + OpenClaw|**Script required** for stale-state detection|
|Work registry/index|CCPM + Kanban + llm-wiki|**Script required**|
|Session progress capture|planning-with-files|No script required|
|State delta extraction|planning-with-files + CrewAI|No script required|
|Entity file maintenance|llm-wiki|Maybe script for multi-file validation|
|Index rebuild|llm-wiki `update-index.py`|**Script required**|
|Drift detection|planning-with-files + llm-wiki + Hermes guard|**Script required**|
|Human validation gate|CrewAI + Hermes guard|No script for operator gate; optional guard script|

These evidence categories are explicitly listed in the ProThinking evidence matrix.

---

## 5. Process source selections extracted

|Process|Best source|Mechanism|Needs script|Copy type|Priority|
|---|---|---|---|---|---|
|**PM1 Capture project**|Backlog `types/index.ts`|Markdown/frontmatter project-task capture contract|No|ADAPT|27|
|**PM2 Decompose project**|CCPM `structure.md`|Epic-to-task decomposition with task files and split/parallel metadata|No|ADAPT|9|
|**PM3 Assign dependencies**|CCPM `structure.md`|`depends_on`, `parallel`, `conflicts_with` plus validation|Yes|ADAPT|5|
|**PM4 Compute next action**|Task Master `find-next-task.js`|Dependency-satisfied eligible-task ranking|Yes|ADAPT|1|
|**PM5 Detect blockers**|Kanban `show_blocked.sh`|Scan Markdown cards for nonempty `blocked_by`|Yes|FULL|2|
|**PM6 Update status**|Backlog `types/index.ts`|`TaskUpdateInput` + structured status/frontmatter fields|Maybe|ADAPT|6|
|**PM7 Detect stall**|planning-with-files `SKILL.md`|Session artifact comparison; custom stale detector needed|Yes|CONCEPT|15|
|**PM8 Generate work registry**|llm-wiki `update-index.py`|Scan Markdown frontmatter and regenerate compact index|Yes|ADAPT|3|
|**KB1 Write session progress**|planning-with-files `SKILL.md`|Write `progress.md` with actions/errors/outcomes|No|FULL|7|
|**KB2 Extract state deltas**|planning-with-files quickstart|Convert narrative into findings/progress/delta sections|No|ADAPT|18|
|**KB3 Maintain entity files**|llm-wiki `SKILL.md`|Maintain LLM-owned entity/concept/source Markdown while preserving raw input|Maybe|ADAPT|10|
|**KB4 Rebuild index**|llm-wiki `update-index.py`|Recursively scan pages and regenerate `index.md`|Yes|FULL|4|
|**KB5 Detect drift**|llm-wiki `update-index.py`|Regenerate state/index and compare snapshot|Yes|CONCEPT|14|
|**KB6 Produce next-session context**|planning-with-files quickstart|Read plan/findings/progress and write handoff context|No|FULL|8|
|**PD1 Score priority**|Task Master `find-next-task.js`|Adapt high/medium/low priority weights|Yes|ADAPT|17|
|**PD2 Score urgency**|Kanban `SKILL.md`|Use due date as urgency substrate; numeric rule local|Yes|CONCEPT|19|
|**PD3 Compute unlock depth**|Task Master `find-next-task.js`|Reverse dependency traversal|Yes|CONCEPT|16|
|**PD4 Synthesize focus recommendation**|Task Master `find-next-task.js`|Deterministic ranking plus rationale|Yes|ADAPT|11|
|**PD5 Validate with operator**|CrewAI `design-task/SKILL.md`|Human review gate before mutation|No|ADAPT|12|
|**PD6 Feed planning layer**|planning-with-files `SKILL.md`|Handoff ranked context through planning files|No|FULL|13|

The final summary table in ProThinking explicitly records these best sources, mechanisms, script requirements, copy types, and priority ranks.

---

## 6. Cluster assignment extracted

|Cluster|Processes|Implementation type|Source base|
|---|---|---|---|
|**A_PLAN**|PM1, PM2, PM3, PD1, PD2, PD4|Pure SKILL.md / operator-gated planning; no scripts in the cluster itself per H5|Backlog, CCPM, Task Master, Kanban, CrewAI|
|**B_SYNC**|PM4, PM5, PM7, PM8, KB4, KB5|SKILL.md + read-only Python scripts|Task Master, Kanban, llm-wiki, planning-with-files|
|**C_SESSION**|PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6|SKILL.md + write-gated mutation procedures|Backlog, planning-with-files, llm-wiki, CrewAI|

The lockfile gives the binding H5 cluster split. ProThinking also gives natural clusters such as Intake/task contract, Decomposition/dependency engine, Session memory/handoff, Knowledge entity maintenance, Product scoring/recommendation, and Governance/validation.

---

## 7. Explicit gaps extracted

|Process|Gap|Phase 2/3 implication|
|---|---|---|
|**PM7**|No exact Apex stale detector exists in fetched sources|Must build custom snapshot/session comparator|
|**KB5**|No exact Apex current-state vs last-session drift comparator|Must build drift script from index dry-run/hash concepts|
|**PD1**|Numeric Apex priority scoring not directly implemented|Must adapt enum priority to H7 weights|
|**PD2**|No separate numeric urgency scorer|Must build date-to-urgency scoring from `due_date`|
|**PD3**|No source computes reverse unlock depth exactly|Must build reverse dependency traversal|

These gaps are explicitly listed in ProThinking’s Q3 gap table.

---

## 8. Phase 1 readiness verdict

**PHASE_1_PASS_AUTHORITY_EXTRACTED**

The authority layer is now sufficiently extracted to begin **Phase 2 — URL / label → local mirrored path map**.

### Carry-forward rules for Phase 2

1. **Do not use public GitHub or web.**
2. **Treat public URLs only as source identities.**
3. **Resolve every selected source to local repo paths under `source-knowledge/ProjectRepos/`.**
4. **Record path drift explicitly.**
5. **Do not validate a mechanism until the local file is opened and inspected.**
6. **PM2 must remain the control sample: CCPM + Backlog + CrewAI must all be resolved/read or explicitly substituted with evidence.**