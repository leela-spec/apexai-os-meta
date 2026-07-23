This is a thorough primary-source research question. Here is the full independent architecture assessment.

---

# Apex KB Execution Model — Independent Architecture Assessment

Apex KB is fundamentally a **stateful, single-operator, local lifecycle manager** whose core problem is enforcing exact sequencing and exact template fidelity. Its primary execution authority must be **deterministic code**, not an AI. The AI is a bounded semantic worker invoked at specific, machine-defined moments.

---

## 1. Decisive Verdict

Apex KB is a **manifest-driven local application** that collects a fixed configuration from a human operator, governs a finite sequence of deterministic and semantic phases, and imports AI-produced artifacts under structural validation. It is not a chat workflow, not an agent orchestrator, and not a Skill-driven system. The observed failure pattern — the AI improvising templates, interpreting paths, certifying its own completion — is the direct consequence of placing lifecycle authority inside a system (a Skill or agent prompt) whose operational guarantee is _best-effort instruction following_, not _exact deterministic execution_. The correct boundary: a CLI application owns the lifecycle; an AI Skill or prompt is called as a worker and returns a validated artifact.

---

## 2. Option Matrix

Primary research established the following about Skills: they load SKILL.md instructions probabilistically based on description matching; Claude "decides whether to consult a skill based on that description" and only reliably triggers on complex multi-step queries. Scripts inside Skills run deterministically, but the _invocation_ of the Skill and which files it reads remain model choices. This makes any Skill the wrong primary lifecycle engine for an exact stateful workflow.[[platform.claude](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

|#|Option|Template Reliability|Deterministic Seq.|Resume/Recovery|Testability|Windows|Cross-model|Path Flexibility|Semantic Isolation|Operator Clarity|Impl. Cost|Maint.|Dep. Burden|AI Drift Risk|Arch. Duplication|Evolvability|**Total**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|A|Large Skill as primary engine|20|15|20|25|40|80|55|30|50|70|40|85|10|30|45|**615**|
|B|Skill containing+invoking scripts|45|50|45|55|50|75|65|55|60|65|55|70|35|50|60|**835**|
|C|One monolithic script|80|85|70|65|75|90|75|75|70|75|65|75|90|85|60|**1160**|
|**D**|**Modular CLI application**|**95**|**95**|**90**|**90**|**85**|**95**|**90**|**90**|**90**|**80**|**70**|**80**|**95**|**95**|**90**|**1360**|
|E|CLI + thin manually invoked Skill|90|90|88|85|83|92|88|92|85|82|72|78|90|88|88|**1321**|
|F|Terminal UI over CLI core|85|90|85|80|70|88|85|88|80|90|55|65|92|90|80|**1243**|
|G|Desktop/web app|80|85|80|65|60|70|70|80|70|85|30|40|90|88|55|**1048**|
|H|External workflow engine|60|90|88|70|50|65|65|88|65|50|35|35|85|85|60|**991**|
|I|Autonomous agent orchestrator|15|10|20|20|45|60|50|25|30|45|50|30|5|10|40|**455**|
|J|Manifest-driven pipeline + thin Skill|92|93|91|88|84|93|90|93|87|83|68|76|93|93|90|**1338**|

**Selected: Option D — Modular CLI Application**, with an optional thin Skill for semantic task delivery (Option E posture). This is the smallest architecture that satisfies every product requirement without introducing AI drift into lifecycle control.

_Scoring note: all scores are architectural judgment. No external benchmark calibrates these numbers._

---

## 3. Minimal Architecture

text

`OPERATOR    │   ▼ apexkb init            ← renders canonical setup template; writes run.config.json    │   ▼ run.config.json        ← human-editable; JSON Schema validated on every load    │   ▼ apexkb validate        ← confirms source/dest paths exist; writes run.manifest.json    │   ▼ run.manifest.json      ← canonical run state; stage + substage + legal-next    │   ▼ apexkb inventory       ← deterministic corpus scan; writes inventory.json    │   ▼ apexkb brief           ← generates semantic task packet; writes task.packet.json    │   ▼ [AI invoked externally] ← operator pastes/calls AI with task.packet.json    │                       AI writes: analysis.json + wiki drafts   ▼ apexkb import          ← structural validation; writes import.result.json    │   ▼ apexkb accept          ← operator reviews AI output; unlocks next stage    │   ▼ apexkb retrieve        ← deterministic retrieval; writes retrieval.evidence.json    │   ▼ apexkb complete        ← checks all evidence present; writes completion.json`

**Information flow rule:** every stage reads exactly one upstream artifact and writes exactly one downstream artifact. The manifest is rewritten on every transition. No stage reads AI output without first passing `apexkb import` structural validation.

---

## 4. Skill Decision

**Status: Optional, thin semantic guidance package.**

A Skill is not the primary engine and must not sequence, select templates, or decide file paths. Its legitimate role: package the AI's semantic instructions (analysis heuristics, wiki writing rules, contradiction logic) as a SKILL.md that the operator invokes when submitting `task.packet.json` to the AI. The Skill's scripts are zero — it contains only a structured prompt resource. The CLI generates the task packet; the Skill shapes the AI's response style. This is consistent with the documented behavior that Skills reliably trigger on complex multi-step specialized queries and run scripts only deterministically.[[github](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)]

**If cross-model portability is required:** the Skill is replaced by a static `semantic-guidance.md` file referenced by the task packet. The open Agent Skills specification (adopted by OpenAI Codex CLI, Gemini CLI, Cursor, and others as of late 2025) means a SKILL.md is portable, but it is still not lifecycle-authoritative.[[rywalker](https://rywalker.com/research/anthropic-skills)]

---

## 5. CLI Contract

Minimum public commands:

|Command|Input|Output|Guarantee|
|---|---|---|---|
|`apexkb init`|None (interactive prompts)|`run.config.json`|Renders canonical template exactly; every field present and labelled|
|`apexkb validate`|`run.config.json`|`run.manifest.json`|Paths confirmed real; JSON Schema validated; no inference|
|`apexkb inventory`|`run.manifest.json`|`inventory.json`|Deterministic file count + hash; idempotent|
|`apexkb brief`|`inventory.json`|`task.packet.json`|Bounded semantic scope assigned; operator sees what AI will receive|
|`apexkb import <file>`|`analysis.json` + wiki files|`import.result.json`|Schema validation before any file touches run directory|
|`apexkb accept`|`import.result.json` + operator keystroke|Manifest stage advance|Human gate; cannot be automated without explicit `--force`|
|`apexkb retrieve`|Manifest|`retrieval.evidence.json`|Deterministic; no AI involvement|
|`apexkb complete`|All evidence files|`completion.json`|Checks all evidence present; exit code 0 only if complete|
|`apexkb status`|Manifest|Stdout|Shows current stage, legal next actions, blocking conditions|
|`apexkb resume`|Manifest|Stdout|Reads manifest; prints exact next command to run|

**Global flags:** `--config <path>`, `--run-dir <path>`, `--json` (machine output to stdout), `--dry-run`, `--no-color`. Errors to stderr only. Exit codes: 0 success, 1 expected failure, 2 usage/validation error.[[github](https://github.com/steipete/agent-scripts/blob/main/skills/create-cli/SKILL.md)]

---

## 6. Semantic Boundary

**AI owns (semantic judgment):**

- Meaning and authority of each source document
    
- Contradiction detection and resolution reasoning
    
- Synthesis and narrative construction
    
- Macro / Meso / Micro wiki writing
    
- Source scope interpretation _within the bounded packet the CLI issued_
    
- Quality and confidence of its own analysis
    

**CLI/deterministic code owns (structural authority):**

- Which sources are in scope (set in `run.config.json`, confirmed by `apexkb validate`)
    
- Which stage the run is in (manifest, never AI-readable as writable)
    
- What the legal next action is (`apexkb resume` outputs it; no AI reads manifest)
    
- Whether AI output passes structural validation (`apexkb import`)
    
- Whether the run is complete (`apexkb complete`)
    
- File paths and locations (set once at `init`, validated, never re-derived)
    
- Template rendering (hardcoded in `init`, not prompt-generated)
    

**The critical cut:** the AI never sees the manifest as an object it may modify. It receives a task packet, produces an artifact, and the CLI decides whether the artifact is structurally acceptable. Semantic acceptance is a separate human `apexkb accept` gate.

---

## 7. Canonical Artifacts

Only artifacts with a proven producer and consumer are listed. _Judgment: "proven" means the producer is deterministic code, not AI prose._

|Artifact|Producer|Consumer|Content|
|---|---|---|---|
|`run.config.json`|`apexkb init`|Every subsequent command|Operator choices, verbatim|
|`run.manifest.json`|`apexkb validate` (created); every command (updated)|`apexkb status`, `apexkb resume`, all stage commands|Current stage, legal transitions, timestamps|
|`inventory.json`|`apexkb inventory`|`apexkb brief`|File paths, hashes, counts|
|`task.packet.json`|`apexkb brief`|AI (read-only), `apexkb import` (reference)|Bounded semantic scope + instructions|
|`analysis.json`|AI|`apexkb import`|AI's structured source analysis|
|`wiki/` (files)|AI|`apexkb import`|Macro/Meso/Micro drafts|
|`import.result.json`|`apexkb import`|`apexkb accept`|Validation pass/fail + file list|
|`retrieval.evidence.json`|`apexkb retrieve`|`apexkb complete`|Deterministic retrieval proof|
|`completion.json`|`apexkb complete`|Operator / downstream|Final evidence record|

**Removed as decorative:** routing documents, guardrail files, recovery instructions, handover templates, Skill patch notes, migration guides. None of these have a deterministic producer or a structural consumer.

---

## 8. Test Strategy

Product-level acceptance tests. Each test must pass without human interpretation of output.

**T1 — Exact template rendering**  
Run `apexkb init` with scripted input (all fields answered). Diff `run.config.json` against the canonical schema. Every required field must be present, correctly keyed, and contain the operator's literal input. Zero inferred or defaulted values for required fields. _Failure = any field absent, renamed, or reworded._

**T2 — Real path topology**  
Run `apexkb validate` with a known source directory and known destination. Assert `run.manifest.json` contains resolved absolute paths matching filesystem reality. Run again with a nonexistent path; assert exit code 1 and stderr message. _Failure = path accepted without existence check, or relative path stored._

**T3 — Resume after interruption**  
Run through `apexkb inventory`, kill process, restart machine state. Run `apexkb resume`. Assert output is the exact command string for the next legal stage. Assert no data loss in manifest. _Failure = resume suggests a wrong stage, or re-runs a completed stage._

**T4 — Semantic packet generation**  
Run `apexkb brief`. Assert `task.packet.json` contains: source scope exactly matching `inventory.json`, semantic instruction block matching the canonical guidance text verbatim, no file paths outside the validated source directory. _Failure = scope expanded, contracted, or reworded._

**T5 — AI lifecycle control absence**  
Inject a mock `analysis.json` where AI has written a field named `next_stage` or `manifest_update`. Run `apexkb import`. Assert the field is ignored; manifest is not modified; import result only records structural pass/fail. _Failure = any manifest field changed by imported AI content._

**T6 — Structural import validation**  
Run `apexkb import` with a malformed `analysis.json` (missing required fields per schema). Assert exit code 1, stderr error identifying missing fields, no files written to run directory. _Failure = partial write, silent pass, or error on stdout._

**T7 — Completion evidence**  
Run all stages to completion with valid inputs. Run `apexkb complete`. Assert exit code 0 and `completion.json` present and schema-valid. Remove one evidence file; re-run; assert exit code 1. _Failure = completion certified with missing evidence._

---

## 9. Build Sequence

**M1 — Schema and manifest core** _(~1 week)_  
Define JSON Schema for `run.config.json`, `run.manifest.json`, `task.packet.json`, `analysis.json`. Implement schema validator. No CLI yet. T1/T2 harnesses written first.

**M2 — `init` and `validate` commands** _(~1 week)_  
Interactive prompt engine rendering canonical template exactly. Path validation. Manifest creation. T1 and T2 pass.

**M3 — `inventory`, `brief`, `status`, `resume`** _(~1 week)_  
Deterministic corpus scan. Task packet generation. Status display. Resume logic. T3 and T4 pass.

**M4 — `import` and `accept`** _(~1 week)_  
Structural validation of AI output. Human gate. Manifest advance. T5 and T6 pass.

**M5 — `retrieve` and `complete`** _(~1 week)_  
Deterministic retrieval evidence. Completion check. T7 passes. All commands integrated. Full happy-path run end-to-end.

**M6 — Optional Skill and hardening** _(~1 week)_  
If desired: package `semantic-guidance.md` as a minimal SKILL.md. Cross-platform path testing (Windows). `--json` output on all commands. Exit code audit.

---

## 10. Kill List

Remove or make optional immediately:

- **Large Skill as lifecycle engine** — primary source of all observed failures; incompatible with exact stateful sequencing[[platform.claude](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]
    
- **Routing and guardrail documents** — no structural consumer; replaced by CLI state machine
    
- **Handover and recovery instruction files** — replaced by `apexkb resume` reading the manifest
    
- **Design files treated as installed behavior** — the CLI _is_ the installed behavior; design docs are input to M1, then archived
    
- **Template variants** — one canonical template, hardcoded in `apexkb init`; no variants until core is proven
    
- **AI-authored next-stage or path fields** — structurally excluded at `apexkb import`
    
- **Migration program** — no migration; new architecture starts from M1 clean
    
- **Duplicate lifecycle implementations** — if any Skill currently duplicates init/validate logic, delete it
    

**Make optional:**

- Terminal UI (add post-M5 if operator usability testing shows need)
    
- Desktop/web app (add only if multi-operator or remote use cases emerge)
    
- External workflow engine (Temporal, etc.) — not warranted for single-operator local workflow[[community.temporal](https://community.temporal.io/t/implement-finite-state-machine-transitioning-in-the-workflow/8143)]
    

---

## 11. Uncertainties

**Established by primary sources:**

- Skills invoke SKILL.md probabilistically based on description match; invocation is not guaranteed for exact stateful workflows[[github](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)]
    
- Script execution inside a Skill is deterministic once invoked; only the _invocation decision_ is AI-controlled[[platform.claude](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]
    
- Agent Skills specification is cross-platform (Claude Code, claude.ai, API, OpenAI Codex CLI, Gemini CLI, Cursor) as of late 2025[[rywalker](https://rywalker.com/research/anthropic-skills)]
    
- CLI best practice: flags > env > config file > default precedence; errors to stderr; `--json` for machine output; exit codes 0/1/2[[github](https://github.com/steipete/agent-scripts/blob/main/skills/create-cli/SKILL.md)]
    
- JSON Schema validation via CLI tooling is production-ready[[github](https://github.com/sourcemeta/jsonschema)]
    

**Architectural judgment (not sourced):**

- The 15-dimension scoring matrix is a relative ranking tool, not a calibrated measurement
    
- "Modular CLI application" is recommended over "one monolithic script" primarily for testability and evolvability; a single well-structured Python/Node script satisfying T1–T7 would also be acceptable for M1–M5
    
- The exact schema design for `task.packet.json` and `analysis.json` requires one design session with a domain expert before M1
    

**Unresolved choices requiring one operator decision:**

- Runtime language for the CLI (Python with `click`/`typer`, Go single binary, Node): choice affects Windows distribution and dependency burden; no architecture decision is blocked, but M1 should not start without this choice made
    
- Whether `apexkb accept` requires a passphrase/reason or a bare keystroke: affects audit trail design in the manifest