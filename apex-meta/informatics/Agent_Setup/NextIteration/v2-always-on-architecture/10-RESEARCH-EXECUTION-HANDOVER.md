---
type: ExecutionHandover
id: V2-RESEARCH-EXECUTION-HANDOVER-v1.0
title: Research Execution Handover — Nine Packets, Iterative
description: Self-contained handover instructing a high-reasoning AI to execute nine research packets iteratively against the Apex Informatics always-on contract architecture, writing one result file per packet.
status: current
tags: [handover, research-execution, iterative, prompt-packets]
---

# Research Execution Handover — Nine Research Packets

**You are executing research, not implementing changes.** Nothing you produce modifies the contract
block or any live file. You write nine result files and one synthesis. That is the whole job.

---

## 1. Repository and starting point

```
repository : https://github.com/leela-spec/apexai-os-meta
branch     : main — pull latest; do not pin to a commit
work root  : apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/
```

Every path in this document is **relative to the repository root**. Clone, `git pull`, then work
from the repo root so the paths resolve directly.

---

## 2. What this project is — read this before anything else

A specification suite governs how AI agents author knowledge files in this repository. It currently
lives in five files that agents load on demand. The work in progress moves the universal rules into
a **single always-loaded contract block** that would be embedded in the repository's root agent
instruction file, with conditional pointers to the detail files.

The candidate block is **1,622 tokens** and carries ~20 rules. Several of its design decisions rest
on assumptions nobody has verified. **Your nine packets are those assumptions.**

The three that could invalidate or reshape the architecture:

- **Does conditional gating work at all?** Every `when="…"` attribute assumes an agent honours the
  condition rather than reading everything anyway. (Packet `RP-01`)
- **Is static hand-authored routing the right mechanism**, or has semantic retrieval superseded it?
  (Packet `RP-02`)
- **Does the token count even matter the way the author assumes?** If prompt caching makes an
  always-loaded block effectively free after the first request, a large part of this effort
  optimized the wrong variable. (Packet `RP-09`, question 1)

Treat all three as genuinely open. The architecture's author — a previous AI session — has a stake
in them being true. You do not.

### A known weakness in the author's own reasoning

The author concluded that **~1,476 tokens is the floor** after an aggressive rewording pass
recovered only 47 tokens (3%). That conclusion may be wrong: the same author also measured a
wholesale table reformat at ~190 tokens (12%) and initially dismissed the format question on the
strength of a narrower 39-token measurement before correcting themselves.

**`RP-09` exists specifically to challenge the floor claim.** Do not take 1,476 as given.

---

## 3. Input & Priority Ledger

Load these **in order, one stage at a time**. Do not bulk-read the repository.

| Priority | File | What to take from it | Load when |
|---|---|---|---|
| **1** | `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/05-research-prompt-packets.md` | **The nine prompts you will execute.** This is your primary input | Start |
| **2** | `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md` | The current block, its measured token decomposition, and the open items | Start |
| **3** | `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/01-decision-register.md` | What is settled, what was superseded, falsification conditions. **Part B and Part F matter most** | Start |
| 4 | `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/08-discussion-and-open-threads.md` | Why each open question exists, in the operator's own words | Before `RP-04`–`RP-08` |
| 5 | `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/04-empirical-test-protocol.md` | The local experiment that will test the same assumptions empirically | Before `RP-01` only |
| 6 | `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/index.md` | Navigation if you need a file not listed here | As needed |
| 7 | `apex-meta/informatics/writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md` | The live rules the contract compresses. **Only if a packet needs the original wording** | Rarely |
| 8 | `apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/` | The earlier, partly superseded pass. **Consult only if a packet explicitly needs its history** | Rarely |

**Ignore** everything else in the repository. `ki-basis/`, `apex-meta/orchestration/`,
`source-knowledge/` and the rest are unrelated to this work.

---

## 4. Process — iterative, one packet at a time

**You must work iteratively. Do not attempt all nine in one pass, and do not hold all nine in
context simultaneously.** The loop per packet:

1. **Load** the packet from file `05-…` — that packet only.
2. **Execute** its copy-paste prompt as written. The prompt is the research task; do not rewrite or
   soften it. Where a prompt instructs you to look for disconfirming evidence first, do that first.
3. **Write** the result to its own file (§5) before moving on.
4. **Drop** that packet's raw sources from working context. The result file is now the artifact; do
   not re-read sources you have already distilled.
5. **Update** `RESULTS-00-progress.md` with one line: packet, status, headline finding.
6. **Move** to the next packet.

**Execution order — this matters.** Packets that can invalidate the architecture run first, so their
results inform the rest:

```
RP-01 → RP-02 → RP-09 → RP-03 → RP-08 → RP-06 → RP-05 → RP-07 → RP-04 → synthesis
```

| # | Packet ID | Question | Why this position |
|---|---|---|---|
| 1 | `RP-01` | Does conditional instruction gating actually work? | Can invalidate every `when=` in the design |
| 2 | `RP-02` | Could vector retrieval replace static dispatch? | Can replace the architecture outright |
| 3 | **`RP-09`** | **Every remaining token-efficiency lever; is ~1,000 achievable?** | **Its caching question can make the whole optimization premise moot. Run before the narrower format packets** |
| 4 | `RP-03` | What is this design's reasoning missing or stale about? | Reframes everything downstream |
| 5 | `RP-08` | How does `deepen_when` actually work? | Narrow case of `RP-01`; worth 99 tokens |
| 6 | `RP-06` | Full serialization comparison — XML vs bullets vs table vs other | Depends on `RP-01`, `RP-08` and `RP-09` |
| 7 | `RP-05` | Stopping self-authored acceptance criteria | Independent |
| 8 | `RP-07` | What reduces over-building | Independent |
| 9 | `RP-04` | The communication register term | Smallest; last |

**Two carry-forward rules:**

- **If `RP-01` concludes gating does not work, do not stop.** Record it and carry it into `RP-06`
  and `RP-08`, both of which assume gating functions. That finding changes their answers.
- **If `RP-09` concludes caching makes always-on token cost largely irrelevant, say so loudly and
  carry it into `RP-06`.** A format change that saves 12% of a cost that does not matter is not
  worth the comprehension risk.

---

## 5. Output contract

One file per packet, in the work root:

```
apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/
├── RESULTS-00-progress.md          ← running log, updated after every packet
├── RESULTS-01-gating-efficacy.md
├── RESULTS-02-vector-retrieval.md
├── RESULTS-03-currency-check.md
├── RESULTS-04-register-terminology.md
├── RESULTS-05-self-authored-criteria.md
├── RESULTS-06-condition-syntax.md
├── RESULTS-07-over-building.md
├── RESULTS-08-deepen-when-mechanics.md
├── RESULTS-09-efficiency-audit.md
└── RESULTS-10-synthesis.md         ← written last
```

### Every result file must contain

```markdown
---
type: Reference
id: RESULTS-<NN>-<slug>
title: <packet title> — Findings
description: <one sentence>
status: current
tags: [research-result, <topic>]
---

# <Packet title> — Findings

**Verdict:** <one paragraph. The answer, and your confidence: high / medium / low.>

## Evidence
<table: claim | source link | evidence type (controlled study / production report /
 vendor doc / anecdote) | supports or undermines>

## Strongest case against the verdict
<argue it properly>

## What I could not find
<explicit list. "No evidence exists" is a finding, not a failure.>

## Consequence for the contract
<which decision ID, rule, or token count this changes, and how>
```

**Do not modify any existing file** except `RESULTS-00-progress.md`, which you create and maintain.
In particular: do not edit `01-decision-register.md`, `09-contract-block-v0.5.md`, or anything in
`apex-meta/informatics/*.md`. The operator merges findings; you do not.

### The synthesis file

Written after all nine. It must state:

1. **Which recorded decisions survive and which are falsified**, by ID — `DEC-16`, `DEC-17`,
   `DEC-18`, `DEC-19`, `DEC-20`, `DEC-M1`…`DEC-M6`. The falsification conditions are pre-registered
   in `01-decision-register.md` Part F — check your findings against them literally.
2. **The token consequence, as a single arithmetic table.** The block is 1,622 tokens. List every
   saving your findings support, with its token figure and its risk, and give a recommended total.
   State whether ~1,000 is reachable and what the realistic floor is.
3. **A verdict on whether token count is the right variable at all** — `RP-09`'s caching question.
   If it is not, say so first, because it reframes items 1 and 2.
4. **Contradictions between packets**, if any. Do not smooth them over. `RP-06` and `RP-09` may
   disagree about format; `RP-01` and `RP-08` may disagree about whether conditions are honoured.
5. **What should now be tested locally** rather than researched further.

---

## 6. Standing rules for this work

These are the repository's own operating rules. Follow them.

- **Ground every claim.** Cite a source link or a file path and line. Never cite your own earlier
  result file as evidence for a new claim — it is the thing under construction.
- **Separate measured from plausible.** A controlled study and a blog assertion are not the same
  evidence. Label which is which, every time.
- **"No evidence exists" is a valid, valuable answer.** Do not assemble weak sources into a false
  verdict to appear productive.
- **Do not be agreeable.** The architecture under study was designed by a previous AI session that
  had a stake in its assumptions holding. Several prompts instruct you to argue against it. Do that
  genuinely.
- **Do not implement.** No changes to the contract block, the live suite, or the decision register.
- **Do not add machinery.** No scripts, no validators, no tooling. Nine result files and a
  synthesis.
- **Do not expand scope.** If you find an unrelated problem, note it in the synthesis under "out of
  scope" and move on.
- **Search widely, claim narrowly.** There is no limit on where you look for answers — `RP-09` in
  particular should range far outside AI and prompt engineering, into any field that has solved
  dense instruction under a hard budget. But a technique only reaches a recommendation if it has a
  real standard, a published measurement, or documented production use behind it. Your own ideas go
  in a clearly-marked Speculative section and nowhere else. **Creativity governs where you search;
  evidence governs what you recommend.**
- **Stop and ask** only if a packet is genuinely unexecutable. Everything else: make a reasonable
  call, record it, continue.

---

## 7. Definition of Done

- [ ] Ten files exist in the work root: nine `RESULTS-NN-*.md` plus `RESULTS-10-synthesis.md`.
- [ ] `RESULTS-00-progress.md` has one line per packet.
- [ ] Every result file has a **Verdict** with an explicit confidence level.
- [ ] Every quantitative claim carries a source link.
- [ ] Every result file has a **What I could not find** section that is not empty unless genuinely so.
- [ ] The synthesis checks findings against **every** pre-registered falsification condition in
      `01-decision-register.md` Part F, by ID.
- [ ] The synthesis contains a single arithmetic table of every supported saving, with a recommended
      total and a realistic floor figure.
- [ ] The synthesis answers whether token count is the right variable at all.
- [ ] `RESULTS-09` contains a "Not on the author's list" section with at least one genuinely new
      lever, or an explicit statement that the author's list is complete.
- [ ] `RESULTS-09` draws on **at least three fields outside AI and prompt engineering**, and every
      lever is labelled Proven / Plausible / Speculative with Speculative kept in its own section.
- [ ] `RESULTS-09` names specific rules that a current model likely follows by default and therefore
      cost tokens for nothing — or states that none do.
- [ ] No file outside the work root has been modified. Verify with `git status`.
- [ ] `RP-01`, `RP-02` and `RP-09` each contain a genuine "strongest case against" section, not a
      token one.

---

## 8. What success looks like

The operator can read `RESULTS-10-synthesis.md` and know:

- whether the conditional-gating architecture is sound, needs modification, or should be abandoned;
- whether a fundamentally different mechanism supersedes it;
- **whether optimizing token count is worth doing at all**, given caching;
- **how small the block can realistically get, and by which specific levers** — the operator has
  pushed on this repeatedly and deserves a defensible floor figure rather than another estimate;
- what the contract block should say where its wording is currently provisional;
- what remains genuinely unknown and must be settled by local measurement instead.

**A result that says "three of your assumptions are wrong" is a success.** A result that confirms
everything is a warning sign — check whether you looked hard enough for disconfirming evidence.

---

## 9. Context you will not find in the files

- The contract block is a **candidate**. Nothing is installed. There is no deadline pressure and no
  sunk cost to protect.
- The operator is not a prompt-engineering specialist and has asked for plain explanations,
  particularly in packet 8. Jargon that only a specialist can parse fails that packet.
- Earlier in this project, an inline copy of a JSON schema silently drifted from its authoritative
  source and weakened a published contract without any gate noticing. That is the class of failure
  this architecture exists to prevent, and it is why "state it once, point to the owner" runs through
  every decision.
- A previous session twice justified a design by appealing to authority — "this is the operator's own
  prior design" — without verifying authorship. Both claims were wrong. **Verify provenance before
  treating any repository file as authoritative.**
