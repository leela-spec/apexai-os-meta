I would split this into **nine separate research tracks** rather than one large prompt. That prevents exactly the failure mode we have seen before: one agent tries to solve research, architecture, portfolio tracking, KB design, automation, and trading logic at once and ends up inventing a new platform.

The repo supports this decomposition. IPOS already has the deterministic warehouse/scoring/reporting stack and a real portfolio-vs-stance implementation, while the master architecture explicitly prioritizes free/local, deterministic computation and thin integration. The older plan's critical constraints remain useful—especially **code computes, LLM narrates**, free-first, artifacts over services, and no silent architecture expansion.

I interpret **“Gospel portfolio” = Ghostfolio**, **“activities” = Activepieces**, and **“iPATS” = the current IPOS project**.

---

# Research sequence

|ID|Research|Output|
|---|---|---|
|**R1**|Karakeep → IPOS integration|Exact value + integration design + POC|
|**R2**|Can IPOS become 100% free-data?|Complete source/gap matrix|
|**R3**|Financial Evidence Knowledge Base|Best architecture + downloadable corpora + skills|
|**R4**|Karakeep vs Zotero|Role decision and interoperability test|
|**R5**|Activepieces|Actual local implementation/test of ingestion workflows|
|**R6**|Ghostfolio + alternatives|Actual Ghostfolio POC + ranked competitors|
|**R7**|Deterministic Trading Advisor|Script architecture derived from current Playbook|
|**R8**|Evidence KB ↔ Operational KB bridge|Provenance/promotion/governance architecture|
|**R9**|Final thin-glue implementation plan|File-level implementation plan consuming R1–R8|

**Important:** R1–R8 are independent evidence-gathering tracks. **R9 happens last.**

---

# R1 — Karakeep → IPOS integration

```
<system_instruction>
You are an independent systems-integration researcher.

Your task is NOT to design a new research platform.

Your task is to determine exactly whether and how the existing open-source
Karakeep system should be integrated with the existing IPOS Investment Process OS,
what concrete value it adds that IPOS does not already possess, and the smallest
battle-proven implementation path.

Prefer reuse over invention.
Prefer deterministic interfaces over AI.
Do not implement production integration until the architecture has been evaluated.
</system_instruction>

<repository_context>
Repository: leela-spec/Investment
Branch of record: main

Before reasoning:
1. Inspect current HEAD and recent commits.
2. Read current implementation, not merely historical planning prose.
3. Read at minimum:
   - PROJECT_STATE.md
   - 05_blueprint/00_MASTER_PLAN.md
   - 05_blueprint/01_DECISION_ANALYSIS.md
   - 05_blueprint/03_PORTFOLIO_MODULE.md
   - 04_playbook/modules/*
   - 03_extract/*
   - configs/*
   - ipos/etl/*
   - ipos/export/*
   - ipos/report/*
   - ipos/ai/*
4. Identify stale/conflicting documents instead of treating every Markdown file as authority.

Known architecture principles to preserve unless evidence justifies a formal change:
- Windows/local-first
- free-first
- deterministic numeric computation
- LLM only as optional last-mile narrator
- append-only/versioned evidence where possible
- fail-degraded, never fail-silent
- no autonomous trading
- do not replace working IPOS subsystems unnecessarily
</repository_context>

<objective>
Determine whether Karakeep should become the IPOS research/evidence intake system.

Answer four questions:

1. What exact IPOS problem does Karakeep solve?
2. Which Karakeep capabilities should IPOS consume?
3. Which capabilities should NOT be duplicated inside IPOS?
4. What is the smallest reliable integration that gives most of the value?
</objective>

<required_research>
Research the current Karakeep product and repository from primary sources.

Verify, not assume:
- license
- local/self-host deployment
- Windows/Docker feasibility
- storage architecture
- API
- CLI
- official skill support
- RSS ingestion
- web-page archiving
- PDF/media handling
- notes
- highlights
- tags
- smart lists/search
- full-text search
- webhooks
- automation/rules
- export
- backup/restore
- deduplication
- identifiers
- metadata preservation
- content update/version behavior
- authentication
- failure behavior
- current maintenance/release activity

Inspect the actual API/CLI schemas where available.
Do not rely on marketing summaries alone.
</required_research>

<fit_analysis>
Map Karakeep capability-by-capability onto the CURRENT IPOS architecture.

For every Karakeep capability classify it:

- ADOPT
- ADOPT_AS_OPTIONAL
- IPOS_ALREADY_HAS_THIS
- NOT_NEEDED
- CONFLICTS_WITH_IPOS
- REQUIRES_OPERATOR_DECISION

Explicitly answer whether Karakeep should be:

A. the canonical raw research/evidence store,
B. only a human-facing research dashboard,
C. only an ingestion inbox,
D. a combination of the above.

Do not use vague phrases such as "integrate via API".
Specify exact data crossing each boundary.
</fit_analysis>

<poc>
Build a disposable non-production proof of concept if the environment permits.

Use representative evidence types:
1. web article
2. PDF
3. YouTube URL/transcript artifact
4. research note
5. RSS item
6. duplicated URL

Test:
- ingest
- metadata capture
- content retrieval
- tag/list assignment
- search
- duplicate behavior
- API/CLI retrieval
- export
- backup/recovery

Do not modify the production IPOS scoring path.

Record every command/configuration required so a second operator can reproduce the test.
If installation cannot be executed, provide the exact blocked dependency and a deterministic test plan instead.
</poc>

<mcda>
Score Karakeep and the "do nothing / current repo only" baseline 0-100.

Weights:
- IPOS functional value: 20
- deterministic/auditable interfaces: 15
- provenance preservation: 15
- portability/exportability: 10
- maturity/maintenance: 10
- local/free licensing fit: 10
- integration simplicity: 10
- failure/recovery characteristics: 5
- agent/CLI/API support: 5

Show raw evidence behind every score.
</mcda>

<deliverables>
Produce:

1. EXECUTIVE_VERDICT.md
2. CURRENT_IPOS_GAP_MAP.md
3. KARAKEEP_CAPABILITY_MAP.md
4. POC_RESULTS.md
5. PROPOSED_INTEGRATION.md
6. MCDA.json
7. MACHINE_READABLE_DECISION.json

PROPOSED_INTEGRATION.md must contain:

Input → process → output for every interface.

For example:

external source
→ Karakeep
→ canonical Karakeep identifier
→ IPOS research-event adapter
→ IPOS evidence view

Specify:
- exact identifiers
- schemas
- timestamps
- content hashes if appropriate
- source URLs
- artifact locations
- retry/idempotency behavior
- failure behavior
- backup path
- what remains human-controlled
</deliverables>

<anti_drift>
Do not:
- redesign IPOS;
- replace DuckDB without evidence;
- replace the existing report;
- build a custom bookmark manager;
- create a new RAG stack by default;
- assume Karakeep research should influence numeric scores;
- allow newly ingested prose to silently alter Playbook rules.
</anti_drift>

<definition_of_done>
Done only when an operator can answer:

"Exactly what new value do I gain from Karakeep,
what does it replace,
what remains in IPOS,
and exactly how would one source move through the complete system?"
</definition_of_done>
```

---

# R2 — Can all required IPOS data be free?

This should be a **source audit**, not another architecture exercise.

```
<system_instruction>
You are a financial-data sourcing auditor.

Determine whether the complete intended IPOS data universe can be operated using
free data sources without materially reducing decision quality.

Do not invent data.
Do not substitute a different indicator merely because the intended series is difficult.
Do not accept a source until the actual endpoint/download mechanism has been verified.
</system_instruction>

<repo>
Repository: leela-spec/Investment
Branch: main

Read:
- PROJECT_STATE.md
- configs/registry.yaml
- configs/modules.yaml
- configs/scoring_defaults.yaml
- 03_extract/indicators.jsonl
- 04_playbook/modules/*
- 05_blueprint/00_MASTER_PLAN.md
- 05_blueprint/meso/C2_ingestion_connectors.md
- current ipos/etl/*
- tests/test_connectors.py
- current source-health notes in 05_blueprint/01_DECISION_ANALYSIS.md

Important:
The currently implemented registry is narrower than the intended 60→120 indicator architecture.
Audit both:
A. current implemented requirements;
B. target requirements implied by Playbook/blueprint.
</repo>

<objective>
Answer:

Can IPOS obtain every economically meaningful required input for €0?

If no:
- exactly which inputs cannot;
- why;
- what free proxy alternatives exist;
- what quality is lost;
- whether the item should be dropped, deferred, manually supplied, or paid later.
</objective>

<data_domains>
Audit separately:

1. Equity prices/OHLC/volume
2. Equity breadth
3. Rates
4. Yield curves
5. Credit spreads
6. Funding/liquidity
7. FX
8. Commodities
9. Volatility
10. Macro growth
11. Inflation
12. Labour
13. Sentiment surveys
14. Positioning
15. Options sentiment
16. Corporate buybacks
17. Corporate fundamentals
18. Earnings
19. valuation
20. ETF/instrument metadata
21. liquidity/tradability data
22. portfolio security pricing
23. economic calendars
24. revisions/vintages
25. historical data sufficient for percentile/z-score calculations
</data_domains>

<source_requirements>
For every candidate source determine:

- organization
- exact API/download URL mechanism
- official vs unofficial
- free/keyless/free-key/paid
- authentication
- license/TOS
- personal-use rights
- refresh frequency
- revision behavior
- history depth
- geography
- asset coverage
- rate limits
- survivorship risk
- Windows compatibility
- machine-readability
- current availability
- fallback options

Actually probe representative endpoints where permissible.

Do not call a source "available" solely because an old blog says so.
</source_requirements>

<output_matrix>
Create one row for EVERY required series or data family:

requirement_id
IPOS module
indicator
importance
currently implemented?
primary source
fallback source
free?
history
frequency
verified endpoint?
licensing
quality risk
failure mode
recommended action
confidence
</output_matrix>

<mcda>
For competing sources score:
- correctness 25
- provenance/officiality 15
- historical depth 15
- reliability 15
- free/licensing fit 10
- deterministic access 10
- maintenance burden 5
- fallback compatibility 5
</mcda>

<deliverables>
1. FREE_DATA_COVERAGE.md
2. SERIES_SOURCE_MATRIX.csv
3. SOURCE_MCDA.json
4. UNRESOLVED_GAPS.md
5. FREE_ONLY_ARCHITECTURE.md
6. MACHINE_READABLE_SOURCE_REGISTRY_CANDIDATES.json

Report:
- % of CURRENT IPOS requirements fully covered for free
- % of TARGET 60-indicator requirements covered
- % of likely 120-indicator expansion covered
- weighted % by decision importance
</deliverables>

<critical_rule>
"No free source found" is a legitimate result.

Never create synthetic or fabricated replacement data to reach 100%.
</critical_rule>
```

---

# R3 — General Financial Evidence Knowledge Base

This is deliberately broader than Karakeep.

```
<system_instruction>
You are researching the best evidence architecture for a serious personal
financial research system.

The goal is NOT "chat with PDFs".

The goal is a downloadable, auditable, source-preserving financial evidence base
that can support human research, deterministic IPOS processes and optional AI
analysis without making the AI the source of truth.
</system_instruction>

<repo_context>
Inspect leela-spec/Investment main.

Understand the distinction between:

1. IPOS operational knowledge:
   03_extract/*.jsonl
   04_playbook/modules/*
   configs/*
   scoring/rules/governors

and

2. external evidence:
   filings, macro releases, PDFs, articles, transcripts, newsletters,
   posts, alerts, official documentation and datasets.

Do not collapse these two layers.
</repo_context>

<objective>
Determine the best FREE architecture for a general financial evidence KB.

Research three separate things:

A. storage/indexing software;
B. extraction/processing skills/tools;
C. downloadable financial corpora/knowledge sources.
</objective>

<software_landscape>
Research mature existing systems including, but not limited to relevant candidates:

- Karakeep
- Zotero
- Paperless-ngx
- Obsidian/local Markdown approaches
- SQLite/DuckDB FTS
- Tantivy/Meilisearch/Typesense where appropriate
- Docling
- GROBID
- Apache Tika
- OCR/document parsers only if actually needed
- existing MCP/agent skills
- existing OpenClaw/Codex/Claude Code/Gemini skills

Do not reward a tool because it contains the word "AI".
</software_landscape>

<skill_requirements>
Search specifically for existing battle-tested:

- document parsing skills
- PDF extraction
- web archiving
- metadata extraction
- citation extraction
- entity/ticker extraction
- deduplication
- source classification
- research ingestion
- summarization
- claim extraction
- contradiction checking
- provenance/citation management

For each AI/agent skill verify:
- public implementation exists;
- recent maintenance;
- actual code;
- supported agents;
- tests or demonstrated use;
- license;
- whether AI is required;
- whether deterministic components can run without AI.

Reject vaporware and toy skill repositories.
</skill_requirements>

<downloadable_knowledge>
Research legally downloadable or programmatically obtainable financial evidence corpora.

Examples of categories to investigate:
- company filings
- regulatory filings
- central-bank research/publications
- national statistics
- macro databases
- international institutions
- earnings documents/transcripts where legally available
- corporate investor-relations releases
- academic finance research
- economic working papers
- legislation/regulations relevant to markets
- financial dictionaries/taxonomies/ontologies
- security/instrument reference data
- public historical datasets

Determine for each:
- full-download possibility;
- API/bulk mechanism;
- licensing;
- update mechanism;
- approximate size;
- machine readability;
- provenance quality;
- practical IPOS relevance.

Separate:
FULLY DOWNLOADABLE
INCREMENTALLY ARCHIVABLE
API-ONLY
NOT LEGALLY/PRACTICALLY ARCHIVABLE
</downloadable_knowledge>

<architecture_options>
Compare at least:

A. Karakeep-centric evidence library
B. Zotero-centric evidence library
C. Karakeep + Zotero
D. filesystem/Markdown + deterministic search
E. hybrid evidence store + local search index

Do not assume embeddings/RAG are necessary.

Compare:
- FTS/BM25
- metadata filtering
- deterministic tag/entity lookup
- embeddings only as an optional additional retrieval method
</architecture_options>

<mcda>
Weights:
- evidence provenance: 20
- source preservation/export: 15
- retrieval quality: 15
- local/free: 10
- deterministic operation: 10
- breadth of supported evidence: 10
- automation interfaces: 10
- maturity: 5
- maintenance simplicity: 5
</mcda>

<deliverables>
1. EVIDENCE_KB_REQUIREMENTS.md
2. TOOL_LANDSCAPE.md
3. BATTLE_TESTED_SKILLS.md
4. DOWNLOADABLE_FINANCIAL_CORPORA.md
5. KB_ARCHITECTURE_OPTIONS.md
6. MCDA.json
7. RECOMMENDATION.md
8. INSTALLATION_COMPONENT_MAP.json

The recommendation must identify:
- what to reuse;
- what to download;
- what to archive incrementally;
- what NOT to store;
- what IPOS-specific glue is still actually necessary.
</deliverables>
```

---

# R4 — Karakeep vs Zotero

R3 asks **what a KB should be**. R4 answers the much narrower question: **do we need one or both?**

```
<system_instruction>
Perform a head-to-head integration evaluation of Karakeep and Zotero for IPOS.

Do not conduct a generic product review.

The output must decide:
KARAKEEP_ONLY
ZOTERO_ONLY
BOTH_WITH_CLEAR_ROLE_BOUNDARIES
NEITHER
</system_instruction>

<target_workloads>
Test/evaluate these exact IPOS workloads:

1. YouTube research
2. financial web articles
3. PDFs/research reports
4. academic papers
5. central-bank papers
6. corporate filings
7. newsletter/email research
8. highlighted quotations
9. personal notes
10. source provenance
11. citation/reference management
12. machine retrieval by an agent/script
13. offline/archive recovery
14. automated intake
</target_workloads>

<research>
For each product verify current:

- license
- self-host/local characteristics
- APIs
- CLI
- MCP/skill integrations
- import/export
- attachment storage
- web snapshots
- PDF annotation
- notes/highlights
- metadata
- DOI/citation support
- duplicate handling
- RSS
- webhooks
- automation
- search
- full text
- collections/lists/tags
- backup/restore
- interoperability
</research>

<interop_test>
Determine whether BOTH can coexist without duplicate canonical truth.

If both:
define exactly which owns:

SOURCE RECORD
WEB ARCHIVE
PDF
BIBLIOGRAPHIC METADATA
HIGHLIGHTS
NOTES
TAGS
RESEARCH STATUS
CITATION DATA
FULL TEXT
IPOS SOURCE ID

Investigate existing synchronizers/connectors before proposing custom code.
</interop_test>

<poc>
If feasible, create a disposable test corpus containing:

- 2 web articles
- 2 PDFs, one with DOI
- 1 YouTube-related transcript artifact
- 1 personal note
- 1 duplicate resource

Attempt the same workflows in both systems.

Record:
setup time
manual actions
machine actions
data retained
data lost
export quality
searchability
API accessibility
failure points
</poc>

<mcda>
Weights:
IPOS workload fit 20
provenance 15
web evidence 10
academic/PDF evidence 10
automation/API 10
export/portability 10
determinism 10
local/free 5
maturity 5
operator friction 5
</mcda>

<deliverables>
1. KARAKEEP_VS_ZOTERO.md
2. WORKLOAD_TEST_RESULTS.md
3. ROLE_BOUNDARY_IF_BOTH.md
4. MCDA.json
5. FINAL_DECISION.json
</deliverables>

<rule>
"BOTH" is only acceptable if each system has a clearly different responsibility.
Two databases holding overlapping canonical copies without ownership rules is a rejection.
</rule>
```

---

# R5 — Activepieces: actual ingestion POC

This track specifically tests whether introducing a workflow engine is actually justified.

```
<system_instruction>
Evaluate Activepieces as a deterministic research-ingestion sidecar for IPOS.

This is a research + proof-of-concept task.

The current IPOS architecture deliberately rejected an orchestrator for its weekly
core pipeline. Therefore Activepieces must NOT be silently inserted into that core.

Test it as a separate intake automation layer and determine whether the added value
justifies formally changing or refining the existing architecture decision.
</system_instruction>

<objective>
Test this target flow:

YouTube channel
Email/newsletter
RSS/web publication
alert/webhook
        ↓
Activepieces
        ↓
source metadata + artifact
        ↓
Karakeep and/or deterministic research inbox
        ↓
existing transcription/extraction system where applicable
        ↓
IPOS research_event candidate

No investment scoring occurs here.
</objective>

<research>
Verify:
- current license
- community/self-host limitations
- Windows/Docker compatibility
- local deployment
- Gmail connector
- IMAP alternative
- RSS
- webhook
- HTTP
- filesystem/data outputs
- scheduling
- retries
- idempotency
- deduplication
- secrets
- logging
- backup/export
- flow portability
- failure notifications
- API/MCP characteristics
</research>

<alternatives>
Benchmark against:
- n8n
- Node-RED
- plain Python + Windows Task Scheduler
- PowerShell + Task Scheduler
- Huginn if still relevant

Do not compare feature counts alone.
</alternatives>

<poc>
Actually implement a disposable proof of concept.

Flow A — YouTube:
YouTube channel RSS/Atom
→ detect unseen video
→ structured metadata
→ hand off URL to transcription inbox or mock
→ create research_event fixture.

Flow B — email:
test mailbox/fixture
→ detect labelled research email
→ save metadata/body/attachment reference
→ research_event.

Flow C — RSS:
feed item
→ dedupe
→ Karakeep or local evidence-inbox entry
→ research_event.

Test:
- first event
- duplicate event
- malformed event
- source unavailable
- destination unavailable
- restart/retry
- secret not available
- rerun/idempotency

Do not commit credentials.
Use fixtures where live credentials are unavailable.
</poc>

<mcda>
determinism/resilience 20
IPOS fit 20
local/free 15
connector maturity 10
observability 10
failure recovery 10
operator simplicity 10
portability 5
</mcda>

<deliverables>
1. ACTIVEPIECES_RESEARCH.md
2. ALTERNATIVES_MCDA.md
3. POC_RUNBOOK.md
4. POC_RESULTS.md
5. FLOW_EXPORTS/ if legally/technically exportable
6. ADOPTION_DECISION.md

ADOPTION_DECISION must explicitly say one of:
- ADOPT_SIDE_CAR
- STAY_TASK_SCHEDULER_ONLY
- ADOPT_N8N_INSTEAD
- ADOPT_NODE_RED_INSTEAD
- OTHER

If ADOPT_SIDE_CAR:
state which existing IPOS architecture decision must be amended and why.
</deliverables>
```

---

# R6 — Ghostfolio POC + alternatives

This explicitly requires a **real test installation**, not just online comparison.

```
<system_instruction>
Research portfolio-management sidecars for IPOS and perform a disposable
proof-of-concept implementation of Ghostfolio.

The existing IPOS portfolio-vs-stance module is already operational and must
not be replaced without evidence.

The question is whether a portfolio ledger/performance system adds enough
value to justify running alongside IPOS.
</system_instruction>

<repo_grounding>
Read:
- PROJECT_STATE.md
- 05_blueprint/03_PORTFOLIO_MODULE.md
- ipos/etl/portfolio_csv.py
- ipos/aggregate/portfolio.py
- configs/portfolio_mapping.yaml
- portfolio warehouse migration(s)
- report rendering
- portfolio tests

Understand exactly what IPOS already does before evaluating another system.
</repo_grounding>

<objective>
Answer:

1. What useful portfolio capabilities are missing from IPOS?
2. Does Ghostfolio solve them?
3. Can Ghostfolio feed holdings/transactions into IPOS deterministically?
4. Is another existing product better?
5. Should IPOS retain its current CSV path even if Ghostfolio is added?
</objective>

<alternatives>
Research at least:

- Ghostfolio
- Portfolio Performance
- Wealthfolio if mature enough
- Rotki where relevant
- Maybe Finance if relevant
- other actively maintained open-source portfolio trackers that meet the requirements

Only include alternatives with verifiable active implementations.

Do not include generic budgeting apps unless they genuinely support investment portfolios.
</alternatives>

<requirements>
Evaluate:
- self-host/local
- Windows
- free/open-source licensing
- security
- portfolio holdings
- transactions
- cash
- dividends
- realized/unrealized P&L
- TWR/MWR
- performance history
- allocation
- multi-currency
- instrument metadata
- import
- export
- API
- deterministic machine access
- backup
- current maintenance
- broker compatibility
- finanzen.net Zero
- Smartbroker where feasible
</requirements>

<ghostfolio_poc>
Actually install Ghostfolio in a disposable environment.

Do NOT use the operator's production financial data.

Create a representative synthetic portfolio mirroring the shapes IPOS must handle:
- ETF
- stock
- commodity ETC
- EUR instrument
- USD instrument
- multiple transactions
- dividend/cash event

Test:

1. import path
2. holdings retrieval
3. transactions retrieval
4. API access
5. portfolio valuation
6. export
7. multi-currency behavior
8. restart persistence
9. backup/restore if practical

Then build ONLY A TEMPORARY TEST ADAPTER:

Ghostfolio output/API
→ normalized representation compatible with the existing IPOS portfolio model.

Compare its normalized output against what
ipos/etl/portfolio_csv.py + ipos/aggregate/portfolio.py expect.

Do not merge into production.
</ghostfolio_poc>

<comparison_test>
Run the same synthetic portfolio through:
A. current IPOS CSV path
B. Ghostfolio → test adapter → IPOS-compatible structure

Compare:
- holdings
- currency values
- totals
- weights
- unmapped handling
- missing information
- reproducibility
</comparison_test>

<mcda>
IPOS value added 20
data integrity 15
API/export 15
local/free 10
maturity 10
portfolio analytics 10
operator effort 10
resilience/backup 5
security 5
</mcda>

<deliverables>
1. CURRENT_IPOS_PORTFOLIO_GAPS.md
2. PORTFOLIO_TOOL_LANDSCAPE.md
3. GHOSTFOLIO_POC_RUNBOOK.md
4. GHOSTFOLIO_POC_RESULTS.md
5. TEST_ADAPTER_SPEC.md
6. MCDA.json
7. PORTFOLIO_ARCHITECTURE_DECISION.md

Final choices:
- KEEP_IPOS_ONLY
- IPOS_PLUS_GHOSTFOLIO
- IPOS_PLUS_OTHER
</deliverables>
```

---

# R7 — Build the Trading Advisor from existing IPOS knowledge

This is the one I would make **especially strict**, because otherwise an AI will invent a trading strategy.

```
<system_instruction>
You are a quantitative systems researcher.

Design a deterministic, read-only trading-advisory engine derived from the
existing IPOS Playbook.

You are NOT allowed to invent a new trading strategy.

You are NOT allowed to execute trades.

Your job is:

existing IPOS knowledge
+ existing market data
+ proven deterministic technical libraries
→ explainable entry / stop / target / CRV / sizing advice.
</system_instruction>

<repo_grounding>
Fully inspect:

04_playbook/modules/
especially:
- MARKET_CONDITIONS
- TREND_BREAKS_TRANSITIONS
- TECH_MOVING_AVERAGES
- TECH_VOLUME_CONFIRMATION
- TECH_OSCILLATORS
- EXPECTANCY_CRV
- EXECUTION_LIQUIDITY_FILTERS
- DRAW_DOWN_AND_RECOVERY_GOVERNOR
- TRAILING_STOP_POLICIES if present

Also inspect:
- 03_extract/rules.jsonl
- 03_extract/process.jsonl
- configs/*
- ipos/aggregate/regime.py
- stance/risk-budget code
- portfolio module
- current OHLC pipeline
- existing forecast/self-scoring code

Every proposed advisory rule must cite an existing IPOS rule or explicitly label itself NEW/EXTERNAL.
</repo_grounding>

<objective>
Determine the smallest deterministic engine capable of producing:

- NO_ACTION
- WATCH
- ENTRY_CANDIDATE
- ADD_CANDIDATE
- REDUCE_RISK
- TIGHTEN_STOP
- EXIT_CONDITION

plus:
- entry zone/trigger
- initial stop
- trailing policy
- target or reward assumption
- CRV/R multiple
- liquidity gate
- position-risk cap
- confidence
- invalidation condition
- provenance/reason codes

Advice only.
No order placement.
</objective>

<library_research>
Compare battle-tested libraries/processes:

- TA-Lib
- OpenAlgo TA
- pandas-ta only if currently viable
- Stock Indicators
- vectorbt
- Backtrader if relevant
- established swing/pivot implementations
- existing agent skills such as vectorbt-backtesting-skills

Distinguish:

PRODUCTION_CALCULATION_LIBRARY
BACKTEST_VALIDATION_LIBRARY
AGENT_HELPER_SKILL

Do not confuse these roles.
</library_research>

<rule_mapping>
Create a complete map:

IPOS rule
→ required market data
→ deterministic calculation
→ advisory effect
→ precedence/governor
→ conflict handling

Example conceptually:

regime = MOMENTUM
+ bullish structure
+ liquidity passes
+ CRV >= required floor
→ entry may be considered
→ stop methodology comes from regime policy

Do not add arbitrary numeric thresholds merely to make code easy.

Any number not already authorized by IPOS must be:
- externally justified;
- configurable;
- marked as NEW;
- excluded from production recommendation until approved.
</rule_mapping>

<precedence>
Research and define governor order.

At minimum examine:

portfolio drawdown/capital governor
→ liquidity/tradability gate
→ market regime
→ primary trend
→ secondary/tertiary structure
→ volume confirmation
→ oscillators
→ entry trigger
→ stop
→ CRV gate
→ advisory action

Determine the correct ordering from current Playbook evidence rather than assuming this exact sequence.
</precedence>

<output_contract>
Design a machine-readable advisory object containing at least:

as_of
instrument
data_timestamp
action
entry_method
entry_trigger
entry_zone
initial_stop
stop_method
trailing_policy
reward_assumption
risk_R
reward_R
crv
crv_pass
liquidity_gate
regime
trend_state
confidence
risk_cap
invalidation
reason_codes[]
playbook_refs[]
warnings[]
calculation_version

Every numeric recommendation must be reconstructible without an LLM.
</output_contract>

<validation>
Research best-practice validation:

- no lookahead
- transaction costs
- slippage
- walk-forward testing
- parameter sensitivity
- regime-conditioned evaluation
- benchmark comparison
- adverse-case testing
- false-breakout tests
- data-quality failures

Use vectorbt or another established engine for validation rather than building a backtester if possible.

Separate:
1. whether code reproduces the Playbook correctly;
2. whether the Playbook produces useful historical advice.

Do not confuse implementation correctness with alpha validation.
</validation>

<test_cases>
Design at least:
- clean uptrend
- clean downtrend
- choppy market
- momentum breakout
- false breakout
- low-liquidity instrument
- CRV failure
- drawdown governor override
- conflicting indicators
- stale/missing market data
</test_cases>

<deliverables>
1. PLAYBOOK_TO_CODE_MAPPING.md
2. LIBRARY_MCDA.md
3. ADVISORY_STATE_MACHINE.md
4. ADVISORY_SCHEMA.json
5. GOVERNOR_PRECEDENCE.md
6. VALIDATION_PLAN.md
7. TEST_MATRIX.md
8. IMPLEMENTATION_RECOMMENDATION.md

Do not implement production code in this research stage.
</deliverables>
```

---

# R8 — Merge Karakeep evidence with the existing operational KB

This is **not** the same question as R1.

R1 asks how Karakeep connects technically.  
R8 asks **when evidence is allowed to become “what IPOS believes.”**

```
<system_instruction>
Design the evidence-to-operational-knowledge bridge for IPOS.

The core safety principle is:

EXTERNAL EVIDENCE IS NOT AUTOMATICALLY AN IPOS RULE.

Karakeep may preserve and organize evidence.
The existing IPOS Playbook/configuration controls operational behavior.
Your task is to design the bridge between those layers.
</system_instruction>

<input_layers>
Layer A — raw evidence:
articles
papers
videos/transcripts
emails
filings
official releases
data-source documentation

Layer B — candidate knowledge:
claims
mechanisms
indicator proposals
contradictions
rule proposals
source updates

Layer C — operational IPOS knowledge:
03_extract
04_playbook
configs
scoring
governors
contradiction rules

Layer C is authoritative for runtime.
</input_layers>

<objective>
Design a provenance-preserving lifecycle:

source
→ evidence object
→ extracted candidate claim
→ corroboration/contradiction
→ review
→ accepted/rejected/deferred
→ optional operational promotion
→ versioned IPOS change

Determine what should be deterministic and what may use AI.
</objective>

<research>
Investigate existing proven patterns/software for:

- provenance graphs
- evidence ledgers
- claim/evidence stores
- citation graphs
- research review queues
- data lineage
- content-addressed storage
- Git-based review
- knowledge promotion workflows
- Zotero/Karakeep IDs
- W3C PROV or similar standards where useful
- JSON-LD only if it materially helps
- simple relational alternatives

Prefer simpler proven schemas over ontology engineering.
</research>

<data_contracts>
Design:

1. research_event
2. evidence_source
3. candidate_claim
4. claim_evidence_link
5. review_decision
6. operational_promotion

Each needs:
- stable ID
- source system ID
- canonical URL where applicable
- retrieved_at
- published_at
- content hash/version if useful
- provenance
- status
- confidence where appropriate
- citations
- supersession/retraction handling
</data_contracts>

<state_machine>
Research and propose states such as:

INGESTED
PARSED
CANDIDATE
CORROBORATED
CONTRADICTED
REVIEW_REQUIRED
ACCEPTED_AS_RESEARCH
REJECTED
PROMOTED_TO_OPERATIONAL
SUPERSEDED

Do not assume these exact labels are optimal.
</state_machine>

<governance>
Explicitly define what happens when:

- two sources contradict;
- a source changes;
- an article is corrected;
- duplicate evidence arrives;
- an AI extracts a false claim;
- a research claim is later invalidated;
- an existing Playbook rule conflicts with new evidence;
- an operational numeric threshold changes.

Any operational scoring-behavior change must respect current IPOS versioning/golden-test governance.
</governance>

<retrieval>
Determine whether IPOS needs:

- deterministic metadata/tag retrieval
- full-text/BM25
- optional semantic retrieval
- no retrieval integration at all for weekly scoring

Do not introduce RAG merely because a research KB exists.
</retrieval>

<deliverables>
1. KNOWLEDGE_LAYER_BOUNDARIES.md
2. EVIDENCE_TO_RULE_LIFECYCLE.md
3. DATA_CONTRACTS.json
4. PROVENANCE_MODEL.md
5. GOVERNANCE.md
6. FAILURE_CASES.md
7. MINIMUM_BRIDGE_RECOMMENDATION.md
</deliverables>

<definition_of_done>
An operator must be able to point at any future IPOS rule and answer:

- Where did this rule come from?
- Which evidence supported it?
- Who/what promoted it?
- When did it become operational?
- What changed from the prior version?
</definition_of_done>
```

---

# R9 — Final implementation plan for the thin custom IPOS layer

Your screenshot actually contains **four** custom items. Because you now explicitly require Karakeep and the operational KB to be merged safely, I would add the missing **evidence-promotion bridge** and make the implementation plan cover **five** custom pieces:

1. `research_event` contract
2. research-event renderer
3. evidence → operational knowledge promotion bridge
4. instrument advisory adapter
5. optional Ghostfolio adapter

Everything else should remain an existing product/library wherever possible.

```
<system_instruction>
You are the final systems-integration architect.

Do NOT conduct another broad landscape study.

Consume the completed research outputs R1-R8 and convert their evidence into one
implementation-ready, repository-specific plan for the minimum custom IPOS glue.

The fundamental rule is:

USE EXISTING PRODUCTS FOR CAPABILITIES.
BUILD ONLY THE CONTRACTS REQUIRED TO COMPOSE THEM.
</system_instruction>

<prerequisites>
Do not begin until the outputs of these tracks exist:

R1 Karakeep/IPOS
R2 free-data completeness
R3 evidence KB
R4 Karakeep vs Zotero
R5 Activepieces
R6 Ghostfolio alternatives + POC
R7 deterministic trading advisor
R8 evidence↔operational KB bridge

Re-ground conclusions against current leela-spec/Investment main before planning.

If earlier research contradicts current repo state:
current executable code + tests + explicit current decisions win,
and the contradiction must be documented.
</prerequisites>

<target_architecture>
Produce a plan for exactly five possible custom IPOS components:

C1. research_event contract
C2. research-event renderer
C3. evidence/promotion bridge
C4. instrument advisory adapter
C5. Ghostfolio adapter, only if R6 says it is justified

Do not automatically build C5.

Any Activepieces/Karakeep/Zotero installation is external infrastructure configuration,
not custom IPOS software unless a thin adapter is actually required.
</target_architecture>

<required_detail>
For EACH component specify:

WHY
- user value
- existing gap
- evidence from R1-R8
- why existing software cannot already perform it

INPUTS
- exact upstream system
- exact data format
- schema
- required/optional fields
- provenance

PROCESS
- deterministic steps
- validation
- dedupe/idempotency
- error handling
- retries
- versioning

OUTPUTS
- exact downstream consumer
- format
- storage
- human-visible representation

FILES
- exact existing files touched
- exact proposed files created
- dependencies
- migrations
- config changes

TESTS
- unit
- integration
- fixture
- golden/regression
- failure/degraded tests
- isolation tests

FAILURE MODES
- upstream unavailable
- malformed data
- duplicate
- stale data
- schema mismatch
- unauthorized operational promotion
- numerical advice failure

ROLLBACK
- how to remove component
- how existing IPOS continues without it

DEFINITION OF DONE
- observable operator outcome
</required_detail>

<implementation_principles>
Preserve unless explicitly approved otherwise:

- Windows/local-first
- main branch only
- deterministic numeric calculations
- DuckDB where it remains appropriate
- static report remains primary IPOS decision artifact
- append-only/versioned facts where useful
- fail-degraded
- explicit configs
- no hidden auto-classification
- no credentials committed
- no autonomous trading
- no LLM authority over numerical advice
- no new always-on service inside the IPOS core merely because an external sidecar exists
</implementation_principles>

<architecture_boundaries>
Explicitly draw:

EXTERNAL RESEARCH SOURCES
↓
AUTOMATION LAYER, if adopted
↓
EVIDENCE SYSTEM: Karakeep / Zotero per research decision
↓
C1 research_event
↓
IPOS evidence storage/view
↓
C2 report renderer

Separately:

evidence
↓
C3 candidate-knowledge/promotion gate
↓
existing Playbook/configs

Separately:

market data + Playbook + portfolio + governors
↓
C4 deterministic advisory engine
↓
read-only advice
↓
LLM explanation optional

Separately if justified:

broker/import
↓
Ghostfolio
↓
C5 adapter
↓
existing IPOS portfolio model
</architecture_boundaries>

<sequencing>
Rank implementation using:

VALUE
DEPENDENCIES
RISK
EFFORT
REVERSIBILITY

Prefer vertical slices.

Every stage must produce independently testable value.

Do not propose one giant "integrate everything" implementation.
</sequencing>

<required_outputs>
Create:

1. FINAL_ARCHITECTURE.md
2. IMPLEMENTATION_SEQUENCE.md
3. COMPONENT_C1_RESEARCH_EVENT.md
4. COMPONENT_C2_RENDERER.md
5. COMPONENT_C3_PROMOTION_BRIDGE.md
6. COMPONENT_C4_TRADING_ADVISOR.md
7. COMPONENT_C5_GHOSTFOLIO_ADAPTER.md or REJECT_C5.md
8. FILE_CHANGE_MATRIX.csv
9. TEST_PLAN.md
10. MIGRATION_AND_ROLLBACK.md
11. DEPENDENCY_GRAPH.mmd
12. DECISIONS_REQUIRED_FROM_OPERATOR.md
13. IMPLEMENTATION_HANDOVER.md

Also provide one machine-readable plan:

implementation_plan.json

with:
component_id
priority
status
dependencies
inputs
outputs
files_create
files_modify
tests
risks
rollback
definition_of_done
operator_decision_required
</required_outputs>

<anti_overengineering_gate>
For every proposed new file/component ask:

"Can Karakeep, Zotero, Activepieces, Ghostfolio, TA-Lib, VectorBT,
DuckDB, or current IPOS already do this?"

If yes:
do not build the feature.

Only build the minimum adapter or schema necessary to connect existing systems.
</anti_overengineering_gate>

<final_gate>
The final recommendation must distinguish:

ADOPT NOW
TEST FURTHER
DEFER
REJECT

No implementation may be recommended merely because it is technically possible.
</final_gate>
```

---

## Why this decomposition is important

The existing portfolio subsystem is a good model for what we want: it didn't create a new portfolio-management platform; it created a narrow ingestion/aggregation boundary around real broker data, kept missing inputs explicit, preserved fail-degraded operation, and later verified the initially assumed CSV schema against an actual German broker export.

The same principle should govern this entire expansion:

> **Karakeep owns evidence capture. Zotero only joins if it has a distinct job. Activepieces only owns transport/triggering if its POC proves worthwhile. Ghostfolio only owns portfolio ledger functions if they add value beyond current IPOS. TA-Lib/vectorbt own established quantitative mechanics. IPOS owns the investment process, governors, provenance, and final advice logic.**

And **R9 is forbidden from inventing the architecture until R1–R8 have produced evidence**. That is the main safeguard against ending up with another large custom subsystem before we know what the existing products already solve.
