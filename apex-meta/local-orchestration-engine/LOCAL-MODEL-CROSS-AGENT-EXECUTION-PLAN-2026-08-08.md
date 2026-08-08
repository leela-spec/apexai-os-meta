---
title: "Local Model Research — Cross-Agent Execution Plan"
doc_type: execution_plan
initiative: local-orchestration-engine
created: 2026-08-08
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
source_commit: 212ba9d5
repo: leela-spec/apexai-os-meta
branch_policy: "WORK DIRECTLY ON main ONLY. Do not create branches unless the operator explicitly asks for one."
status: "calibration round (Prompt A x 3 agents) complete; results and comparison staged for operator review; Round 2 (prompts B-E) gated on operator decision re: Gemini configuration per comparison doc Section 6"
---

# Cross-Agent Execution Plan — Local Model Research Prompts

## 1. What this plan is

Commit `212ba9d5` produced six research prompts plus the authority documents they
depend on. Those prompts have never been executed. This plan defines how they get
executed across three subscription reasoning agents — ChatGPT, Gemini and
Perplexity — so that the results are comparable to each other rather than merely
three separate opinions.

The object under study is deliberately dual. The stated goal is to answer the
research questions about local models. The equally important goal is to learn
**which subscription agent is worth spending a research prompt on**, which is
itself a Layer-4 routing decision for APEX. A run that produces a weak answer is
not a wasted run; it is evidence about the agent.

This plan does not select a local model, a runtime, or an agent. It defines the
procedure that produces the evidence.

## 2. What was recovered from the commit

The correction commit `212ba9d5` sits in the direct history of current `main`
(`1fb992f7`). Nothing was lost. The relevant material is:

**Authority documents** — these are inputs to every run, not things to be researched:

| File | Size | Role |
|---|---|---|
| `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` | 16.3 KB | LM-1..LM-30 locked decisions, the 7–8B correction, planner-routing architecture, machine profile |
| `LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md` | 10.8 KB | CODE/WEEKLY/MA/INJECT/COEX fixtures, hard gates, scoring dimensions, repeat protocol |

**Research prompts** — these are the payloads to be executed:

| ID | File | Size | Target |
|---|---|---|---|
| A | `LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08.md` | 6.4 KB | Current 7–8B-centred candidate landscape with smaller controls and larger challengers |
| B | `LOCAL-MODEL-RESEARCH-CODING-2026-08-08.md` | 5.4 KB | Bounded coding execution candidates; CODE-01..05 fixture hypotheses |
| C | `LOCAL-MODEL-RESEARCH-WEEKLY-MULTIAGENT-2026-08-08.md` | 6.2 KB | Non-coding execution: Weekly browser/state/recovery and Multi-Agent worker support |
| D | `LOCAL-MODEL-RESEARCH-WINDOWS-INTEL-RUNTIME-2026-08-08.md` | 6.3 KB | Runtime decision packet for Core Ultra 7 258V / Arc 140V / Windows 11 |
| E | `LOCAL-MODEL-RESEARCH-BENCHMARK-HARNESS-2026-08-08.md` | 7.0 KB | Reproducible harness design turning user stories into executable fixtures |
| F | `LOCAL-MODEL-RESEARCH-SYNTHESIS-2026-08-08.md` | 9.1 KB | Decision packet reconciling A–E; verdict on the 7–8B hypothesis |

A through E are mutually independent and can run in any order or in parallel.
F consumes the outputs of A through E and must run last.

## 3. Operator decisions locked for this campaign

Four choices were made before planning and they constrain everything below.

**Calibration before scale.** The first round is Prompt A only, executed once in
each of the three agents. Three runs, not fifteen. The campaign only expands after
the calibration round proves the harness, the capture path and the scoring rubric.
Committing fifteen browser-driven runs before knowing whether capture works cleanly
is how a session ends with six good results and nine ambiguous ones.

**Per-agent synthesis.** When the campaign reaches Prompt F, each agent synthesizes
only its own A–E outputs. This preserves three independent end-to-end research
chains and makes the comparison meaningful. Cross-feeding one agent's landscape
research into another agent's synthesis would destroy the very independence that
makes the comparison worth running.

**Standard reasoning mode with web search enabled.** Not Deep Research. This is a
deliberate trade and it has a consequence that must be recorded in every result
file: these prompts explicitly demand current primary sources, and standard mode
will source more shallowly than Deep Research would. The calibration round is
therefore also a test of whether standard mode is adequate for this prompt class.
If all three agents source poorly, that finding — not the model landscape — is the
round's real output, and the campaign should re-run at depth.

**Results land in the repo.** One result file per agent per prompt, under
`research-results/`, following the existing `PLATFORM-RESEARCH-*-RESULT.md`
convention. Prepared as a commit on `main`, handed to the operator for review
before any push.

## 4. The comparability problem and how it is solved

Three agents produce comparable output only if every variable except the agent
itself is held constant. Four things threaten that.

### 4.1 The prompts reference repo files the agents cannot read

Every prompt names its authority documents by repo path. An external agent has no
repo checkout. Left unhandled, each agent would invent its own idea of what the
decision lock says, and the three outputs would be incomparable.

The repository is publicly readable, which was verified without credentials, so
raw GitHub URLs are a viable delivery path. That path is nevertheless rejected as
the primary mechanism, because whether an agent actually fetches a URL — and how
much of it it retains — varies per agent and per run. That variance would land
squarely on the axis being measured.

**Resolution:** every run receives one frozen text bundle containing the full
authority documents inline. The URLs are included as a secondary reference only.
The bundle is byte-identical across all three agents.

### 4.2 Bundle assembly

Each run's payload is assembled in this fixed order:

```text
[1] Standing preamble
      - role and task framing
      - explicit statement that the two documents below replace repo access
      - output contract: single markdown packet, all numbered deliverables,
        YAML block last and complete
      - source discipline: label every claim measured / documented / inferred / unknown
      - the run must not ask clarifying questions; it must state assumptions and proceed

[2] OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md   (verbatim, full)

[3] LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md          (verbatim, full)

[4] The research prompt itself                             (verbatim, full)

[5] Reference URLs at commit 212ba9d5
```

For Prompt A this totals roughly 33,500 characters, comfortably inside every
platform's input limit.

The no-clarifying-questions clause matters more than it looks. All three chat UIs
will happily return a question instead of an answer, which produces a null run and
forces a retry that is no longer a clean first response.

### 4.3 Input injection must not fire prematurely

Typing 33 KB into a chat box character-by-character is slow, and every newline in
the payload risks submitting the message early — these UIs send on Enter. A
partially submitted prompt is a contaminated run.

**Resolution:** set the composer's value directly through the page's own input
handling and dispatch the events the framework listens for, then submit once,
deliberately. Before submitting, the composer content is verified to match the
intended payload length. This makes injection near-instant and eliminates the
premature-submit failure mode entirely.

### 4.4 Account state contaminates the run

All three accounts carry projects with custom instructions and, in ChatGPT's and
Gemini's case, cross-chat memory. ChatGPT shows projects including `FusionAi2`,
`Mental-6`, `Master of Arts`; Perplexity shows `AIHow2_2`, `health`, `AI How to`.
A run executed inside any of them inherits instructions that the other two agents
never saw.

**Resolution:** every run starts in a fresh chat at the account root, outside all
projects and Gems. Any persistent-memory or personalization setting that is on
gets recorded in the result file's frontmatter as a known uncontrolled variable,
since it cannot be neutralized per-run without changing account settings.

### 4.5 Interface language

All three accounts render in German. This affects only my navigation, not the
payload — the bundle is English throughout, and each run is instructed to answer
in English so the three outputs are directly comparable and match repo convention.

## 5. Run matrix

### Calibration round — approved

| Run | Agent | Prompt | Mode | Chat context |
|---|---|---|---|---|
| R1 | ChatGPT | A — Landscape | Standard reasoning, web search on | Fresh chat, no project |
| R2 | Gemini | A — Landscape | Standard model, web search on | Fresh chat, no Gem |
| R3 | Perplexity | A — Landscape | Search mode, standard model | Fresh thread, no Space |

Prompt A is the right calibration probe because it is the most falsifiable of the
six. It demands exact model versions, release dates, licences and quantization
availability — claims that can be checked against primary sources afterwards.
Fabrication shows up immediately. A prompt like E, which asks for a harness
design, would produce three plausible essays that are far harder to score.

### Expansion rounds — pending calibration outcome

| Round | Prompts | Runs | Gate |
|---|---|---|---|
| 2 | B, C, D | 9 | Calibration capture clean and rubric discriminates between agents |
| 3 | E | 3 | Round 2 complete |
| 4 | F per agent | 3 | That agent's own A–E complete |

Full campaign at completion: 18 runs. The gates exist so the campaign can be
abandoned or redesigned after three runs instead of after fifteen.

## 6. Per-run execution procedure

Every run follows the same eleven steps. Deviation gets recorded in the result
file rather than silently absorbed.

```text
 1. Open a fresh tab; navigate to the agent at its account root
 2. Confirm no project / Gem / Space is active
 3. Set mode: standard reasoning, web search enabled
 4. Record the exact model label the UI displays          <- goes in frontmatter
 5. Inject the frozen bundle into the composer
 6. Verify composer length matches the intended payload
 7. Submit once; record submit time
 8. Poll until generation completes and the stop control disappears
 9. Extract the full response as text, expanding any collapsed reasoning or source panels
10. Capture the permanent chat URL and a screenshot of the final state
11. Record wall-clock duration, retry count and any interruption
```

**Interruption handling.** If a run hits a CAPTCHA, a login prompt, or a
rate/usage limit, it stops and returns to the operator. I do not solve CAPTCHAs
and I do not enter credentials. A run that was interrupted and resumed is marked
as such, because a resumed run is not a clean single-response measurement.

**Retry policy.** At most one retry per run, and only for a mechanical failure —
truncated injection, network error, empty response. A retry for a *disappointing
but complete* answer is forbidden. Retrying until an agent looks good is exactly
how a comparison stops being a comparison.

## 7. Capture and result file convention

Each run produces one file:

```text
apex-meta/local-orchestration-engine/research-results/
  LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-CHATGPT-RESULT.md
  LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-GEMINI-RESULT.md
  LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-PERPLEXITY-RESULT.md
```

Frontmatter extends the existing result convention with the run metadata that
makes cross-agent comparison auditable:

```yaml
---
title: "Local Model Research Result — Landscape — ChatGPT"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08.md
prompt_id: A
agent: chatgpt
agent_model_label: null          # exactly as the UI displayed it
agent_mode: "standard reasoning + web search"
account_tier: null
run_id: R1
run_started: null
run_duration_seconds: null
evidence_date: 2026-08-08
chat_url: null
bundle_sha256: null              # identical across R1/R2/R3 or the run is void
retries: 0
interruptions: []
uncontrolled_variables: []       # e.g. cross-chat memory enabled
status: "raw agent output; unverified; no APEX authority"
---
```

The `bundle_sha256` field is the integrity check for the whole campaign. If the
three runs of a prompt do not share one hash, they were not given the same input
and the comparison is void.

**Authority note carried in every result file:** this output is raw external
research. Per the R3 lock it is data, not APEX authority, and it creates no
authority regardless of how confident it sounds.

## 8. Scoring rubric

Agents are scored on the same axes the prompts themselves impose, not on
readability. Each axis is scored 0–5 with a written justification.

### 8.1 Boundary compliance — pass/fail per boundary

Prompt A carries seven explicit boundaries. These are checked first because a
violation invalidates the content regardless of quality:

- did not select a production model;
- treated 7–8B as hypothesis, not proven;
- did not silently substitute a largest-model or maximum-reasoning objective;
- did not equate public benchmark strength with APEX execution reliability;
- did not infer dedicated VRAM from integrated-GPU reporting;
- separated measured / documented / inferred / unknown;
- preferred current primary sources.

The third and fifth are the sharpest discriminators. The 7–8B correction is
precisely the trap the commit was created to fix, and an agent that drifts back
toward "just use the biggest model that fits" has failed the run's central test.
The VRAM point is a specific, checkable technical claim about Arc 140V shared
memory that a careless agent will get wrong.

### 8.2 Deliverable completeness

Prompt A specifies sixteen numbered deliverables and a YAML block with eighteen
keys. Scored as fraction present and substantive. A YAML block that parses but is
padded with nulls scores lower than a shorter, honest one.

### 8.3 Evidence quality

- proportion of claims traceable to a primary source (model card, repo, release notes, technical report) versus secondary aggregators;
- whether cited versions and dates actually exist — spot-checked independently;
- whether the freshness map is real or decorative;
- **fabrication count**, tracked separately and weighted heavily. One invented model version is worse than five missing deliverables.

### 8.4 APEX fit

Whether the answer engages the actual bounded-executor role — tool reliability,
structured output, escalation behaviour, coexistence on a 31.6 GB machine — or
retreats into generic model-comparison content that would be identical for any
questioner.

### 8.5 Cross-agent contradiction table

Built after all three runs. Every factual disagreement between the agents becomes
a row: the claim, each agent's position, and which is verifiable. Contradictions
are preserved rather than averaged away, per the synthesis prompt's explicit
instruction. Agreement between all three on a checkable fact raises confidence;
unanimous agreement on an *unverifiable* claim raises suspicion of shared training
bias, which is itself a finding worth recording.

## 9. Deliverables from the calibration round

1. Three result files, raw agent output preserved verbatim, in the repo convention above.
2. `LOCAL-MODEL-CROSS-AGENT-COMPARISON-A-2026-08-08.md` — rubric scores, boundary-compliance matrix, contradiction table, fabrication log.
3. A routing recommendation: which agent to spend which of the remaining prompts on, with reasoning. This is the operationally valuable output.
4. A verdict on whether standard mode was sufficient, or whether the campaign must re-run at Deep Research depth.
5. A staged commit on `main`, presented for operator review before push.

## 10. Known risks

**Standard mode may be insufficient.** Accepted deliberately; the calibration
round measures it. If all three agents source shallowly, the finding is about the
mode, not the models, and Round 2 should not proceed until that is resolved.

**Usage limits.** Three long-context runs across three subscriptions in one
session may hit caps, particularly on Gemini. A run blocked by a cap stops and
returns to the operator rather than silently degrading to a weaker model.

**UI drift.** All three interfaces change frequently. Selectors are re-derived per
run from the live page rather than assumed, and the composer content is verified
before every submit.

**Single-sample noise.** Three runs is one sample per agent. The rubric scores
are indicative, not statistically meaningful, and the comparison document must say
so. The benchmark portfolio's repeat protocol exists for the local models; it is
not being applied to the agents here, and no claim should be made as though it were.

**The measurement is dated.** Agent capability changes weekly. Every conclusion is
stamped with `evidence_date` and is a snapshot, not a standing verdict.

## 11. Success condition

The calibration round succeeds when the operator can see, from evidence rather
than impression, how the three subscription agents differ on a real APEX research
prompt — specifically which ones respected the 7–8B correction, which ones cited
sources that actually exist, and which are worth spending the remaining fifteen
runs on.
