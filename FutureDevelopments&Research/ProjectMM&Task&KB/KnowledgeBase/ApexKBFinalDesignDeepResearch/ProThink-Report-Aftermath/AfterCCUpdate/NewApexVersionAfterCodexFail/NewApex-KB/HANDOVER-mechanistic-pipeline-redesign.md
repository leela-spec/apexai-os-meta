# Handover: Redesign apex-kb Toward a Mechanistic, No-Reasoning Pipeline

**To the session picking this up:** this is a research-and-design handover, not a build ticket.
Do not start writing code or prose doctrine on day one. Read Sections 1-4 first, run the Section 7
research agenda, and only then design Section 5. The single biggest way to fail this handover is
to skip straight to "add more guardrails" — that is the exact mistake this document exists to
correct.

---

## 1. Failure acknowledgment — what was misunderstood, stated plainly

The operator asked, across several sessions, for a **mechanistic, script-and-command execution
pipeline** where an AI has no choices to make: a fixed welcome message, a fixed Q&A, fixed
templates, fixed next-command derivation — "the AI does not think, it just executes."

What actually got built, across this session and the one before it, was a **real deterministic
control plane** (`apex_kb_control.py` — canonical run state, legal-transition enforcement, exact
next-command derivation, file-based semantic handoff packets, a mandatory acceptance gate, a
read-only Git classifier, a package self-check) plus a **growing body of prose doctrine**
(`SKILL.md` and its reference docs) instructing an AI to use that control plane correctly.

That is not the same thing as what was asked for, and the operator caught this directly: after a
live run still went wrong, they stated explicitly that "nothing of what I wanted... is actually
realized," and that the accumulating prose doctrine may be making the skill *less* reliable, not
more. **Both of those are correct, and the previous sessions (including this one) did not clock
it until asked directly.** The precise error was this: every prior fix treated the deterministic
control plane's existence as sufficient — but a deterministic engine that an AI must *choose* to
invoke, by first reading and correctly following a 371-line `SKILL.md`, is still fundamentally a
"read a lot of prose and comply" system. It is a much better one than before (see Section 4 for
what genuinely improved), but it is not the "AI cannot choose anything" system that was requested,
and no prior session said so directly until this one.

A second, more specific error also happened in this same session and should be named directly: an
externally-authored patch (module M2, applied at commit `87883945`) correctly fixed one bug
("non-text files were silently dropped from custody visibility") by removing a file-extension
filter from `cmd_source_intake`'s recursive `--source-root` branch. That fix was verified against
its own stated scope — exact-match blocks matched byte-for-byte, its own test suite passed. What
was not checked was how that change *interacted* with a second, unrelated, pre-existing defect in
the same code block (hardcoded `copy_into_kb`, ignoring the caller's requested storage mode — see
Section 2). Each change was individually correct and individually verified; the two together
produced a real-world incident (1,736 files / 176MB copied against an explicit pointer-only
instruction). The lesson: **verifying a patch against its own stated scope is not the same as
verifying the combined behavior of every code path it touches.** This should inform how the next
session reviews any change to this codebase, not just this one bug.

---

## 2. Evidence

### 2a. What the live transcript actually shows (source: `NewApex-KB/Untitled/Untitled.md`)

| Time | What happened | Assessment |
|---|---|---|
| 1:26-1:29 | Codex "installs" the skill (39 files, `.codex/skills/apex-kb`); asks the execution-route question correctly; explains the 3-step sequence (identify scope → readback+confirm → scaffold/intake/analyze/compile/validate) reasonably accurately when pressed. | Doctrine *did* activate and was followed at a high level. |
| 1:29-1:43 | Operator gives scope (Leela app, priority folders, topics). AI initially conflates "priority source folders" with "topics" — a real comprehension error, corrected only after the operator caught it and demanded a verification table. | Genuine misunderstanding, but of natural-language scope, not of the process itself. |
| 1:43-2:00 | AI produces a scope-decision table; generates KB scaffold, topic registry, and an "operator readback" (this is the real `intent_lock` stage artifact — the mechanism engaged correctly here). Asks for confirmation via a **custom phrase** ("Reply: 'I confirm the Leela KB run.'") rather than surfacing the documented `control confirm --confirmation-quote` command. | Mechanism engaged; confirmation *step* correct, exact *command surface* not shown to the operator (Class D, below). |
| 1:46 | AI reports being **blocked**: `apex_kb.py` is not present under the target repo (`leela`) and "is not included in the installed apex-kb skill package." | **Confirmed real packaging gap** (Class A, below) — not an AI error. |
| 2:00-2:04 | Operator redirects the AI to read from the *original* `apexai-os-meta` skill folder. AI proceeds; correctly reports it has **not** run Phase 1/2 itself and will hand off bounded packets to another AI instead — this is exactly the intended division of labor. | Doctrine correctly followed once the AI had real script access. |
| 2:04-8:54 | Operator instructs "run the deterministic phase." AI runs confirm → preflight → source_intake → phase0 in sequence (visible as "Ran commands"), survives a machine shutdown mid-Phase-0 with a clean recovery, and correctly renders (but does not execute) a Phase 1 packet for the "Epic" topic. | **This is the control plane working exactly as designed**, including resume-from-files behavior. |
| 9:06 | Operator asks what went wrong. AI **self-diagnoses correctly**: `--source-root` recursive intake ignored the requested storage mode and defaulted to `copy_into_kb`, copying 1,736 files (176,773,752 bytes) — including PDFs, images, and old KB folders — into `raw/`. | **Confirmed, reproducible code bug** (Class B, below) — fixed in this handover's companion commit. |

**Read this trace carefully: most of it is the mechanism working.** The failure was not "the AI
ignored the process." It was one packaging gap and one code bug, both concrete and fixable, plus
one UX inconsistency (Class D). Do not let "the whole thing is unreliable" become the operating
assumption for the next session — it is not supported by this evidence.

### 2b. The bug, exact diff

`apex-meta/scripts/apex_kb.py`, `cmd_source_intake`, the `if args.source_root:` recursive branch:

```diff
         existing = {k: v for k, v in existing.items() if not belongs_to_source_root(v)}
         results = []
+        root_storage_mode = args.storage_mode
+        root_source_type = args.source_type
         eligible = sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.as_posix().lower())
         for path in eligible:
             rel = path.relative_to(root).as_posix()
             source_id = "source-" + hashlib.sha256(rel.encode("utf-8")).hexdigest()[:16]
-            dest = kb_root / "raw" / "other" / Path(rel)
-            copy_result = copy_file(path, dest, kb_root, args.allow_write, dry_run)
+            copy_result = None
+            if root_storage_mode in {"copy_into_kb", "snapshot_copy"}:
+                dest = kb_root / "raw" / "other" / Path(rel)
+                copy_result = copy_file(path, dest, kb_root, args.allow_write, dry_run)
+                entry_source_path = relpath(kb_root, dest)
+            else:
+                entry_source_path = str(path)
             entry = {
                 "source_id": source_id,
                 "title": rel,
-                "source_type": "other",
-                "source_storage_mode": "copy_into_kb",
-                "source_path": relpath(kb_root, dest),
+                "source_type": root_source_type,
+                "source_storage_mode": root_storage_mode,
+                "source_path": entry_source_path,
                 "original_source_path": str(path),
```

Already fixed and tested (3 new tests, `apex-meta/scripts/tests/test_apex_kb_source_intake.py`;
full suite 75/75 green) as part of this handover's companion commit. The next session does not
need to redo this — it is evidence of *what class of bug to watch for*, not an open task.

### 2c. Doctrine size, measured (not assumed)

```
SKILL.md                                     371 lines   2,817 words
references/acceptance-tests.md               352 lines   1,961 words
references/browser-git-connector-...          45 lines     682 words
references/ingest-query-lint-audit-rules.md  125 lines   1,001 words
references/kb-contract.md                    184 lines   1,365 words
references/knowledge-promotion-rules.md       76 lines     243 words
references/old-apex-knowledge-bank-doctrine    44 lines     521 words
references/retrieval-contract.md              67 lines     279 words
references/script-command-contract.md        189 lines   1,466 words
references/semantic-value-contract.md        166 lines   1,969 words
templates/*.md (7 files)                     849 lines   3,165 words
examples/*.md (2 files)                      104 lines     827 words
------------------------------------------------------------------
TOTAL (39 files)                           2,785 lines  18,150 words  (~24,000 tokens if read in full)
```

This is real and worth reducing (Section 6). It is **not proven** to be the cause of any specific
failure in the transcript above — every failure there had a precise, different cause. Do not
conflate the two; Section 3 exists specifically to stop that conflation.

---

## 3. Four distinct failure classes — keep these separate

The single biggest risk in redoing this work is collapsing everything back into one vague "the AI
didn't follow the process" bucket. It didn't happen that way. Four different things happened:

- **Class A — Packaging / cross-repo gap.** The executable scripts (`apex_kb.py`,
  `apex_kb_control.py`, `apex_kb_retrieval.py`) live in `apex-meta/scripts/` inside
  `apexai-os-meta`; the "installable" skill package (`.claude/skills/apex-kb/`, 39 files) does
  **not** include them. An AI given only the installed skill package (as Codex's own install
  mechanism does) has the doctrine and templates but not the engine. This is an architecture/
  packaging problem, not an AI-behavior problem.
- **Class B — Code defects.** The storage_mode bug (Section 2b) is the concrete instance: a real
  software bug that *looked* like AI misbehavior from the outside ("it copied everything despite
  being told not to") but was actually a hardcoded value in a function nobody had re-audited after
  an adjacent, individually-correct fix changed the surrounding code.
- **Class C — Doctrine bloat.** Measured (Section 2c), real, but not proven to be the cause of any
  specific incident observed so far. Worth fixing on its own merits and because the deterministic
  control plane now makes it *safe* to cut prose that used to be the only enforcement (Section 6).
- **Class D — UX/consistency gap.** The AI translated the mechanistic confirmation step into its
  own natural-language wrapper ("Reply: 'I confirm the Leela KB run.'") instead of surfacing the
  literal `control confirm --confirmation-quote "<...>"` command the engine actually expects. This
  is a small thing, but it is exactly the kind of improvisation the operator does not want — every
  step should show the operator the real command, not a paraphrase of it.

When the next session finds a new failure, force it into exactly one of these four buckets before
proposing a fix. If it doesn't fit any of them, that's a fifth class worth naming precisely — not
an excuse to reach for "add another guardrail."

---

## 4. The honest answer to "can an AI be made to not think at all"

**No — not literally.** The executor is a large language model; it does not have a mode where it
executes text without any interpretation. Any system built on an LLM retains some non-zero
probability of misreading an instruction, improvising, or choosing wrong.

**What *is* achievable, and has real precedent** (see this repo's own prior research, Section 7):
shrinking the *surface area* where judgment is exercised to as close to zero as the host tooling
allows, by making the very first and only required action a **single fixed command whose own
output is the complete next instruction** — never a document the AI must read and interpret to
decide what to do. This is exactly what `control next` / `control run` already do at the mechanical
layer (Section 2a's trace proves it works when reached). The actual gap is narrower than "the whole
skill needs rethinking": **nothing currently forces an AI to reach for `control` at all**, or to
keep using it instead of improvising once it has (Class D). Closing that specific gap is a much
smaller, much more tractable problem than redesigning the whole pipeline from scratch.

---

## 5. A concrete design to build and test (not to copy verbatim)

Design, build, and test a **compact activation seed**: a fixed entry-point text of roughly 15-20
lines — not a rewritten `SKILL.md` — whose entire content is approximately:

> Do not read any other apex-kb file first. Run exactly:
> `python apex-meta/scripts/apex_kb.py --kb-root <target> control next`
> (or `control init ...` if no run exists yet — its own `--help` lists every required flag).
> Do only what the `operator_action` field says, verbatim. Never construct your own command. Never
> paraphrase a confirmation prompt — show the operator the exact command from `operator_action`.
> Never fall back to a legacy command (`scaffold`, `source-intake`, `phase0`, etc. called directly).
> If blocked, paste the exact `reason_code` and `operator_action` back to the operator and stop.

This document does not prescribe the final wording — that is the next session's design work. It
prescribes the **constraints**: tiny, fixed, points at exactly one command, explicitly forbids the
four improvisations observed in Section 2a/3 (constructing a command, paraphrasing a confirmation,
falling back to legacy commands, silently retrying past a block).

**A design question to resolve with evidence, not assumption** (part of Section 7's agenda): a
fixed activation seed only helps if something reaches for it *first*. Right now, nothing does —
`guard_direct_command` in `apex_kb_control.py` only blocks legacy commands **after**
`manifests/run-state.json` already exists (i.e., after `control init` has already run once). For a
brand-new KB, an AI can still skip straight to `scaffold`/`source-intake`/etc. and nothing stops
it. Whether to close that gap by making legacy commands refuse to run *at all* without a run-state
present (even for a KB that has never been initialized) is a real design decision with a real
cost — it would require every genuinely-legacy, pre-control KB workflow to explicitly opt out, and
that tradeoff needs to be evaluated deliberately, not assumed away.

---

## 6. Doctrine-shrink mandate

Authorized and expected as part of this work, not optional: identify every section of `SKILL.md`
and its reference docs that exists purely to *explain* something the control plane now enforces
*mechanically* (a reason code, a schema requirement, a `control doctor` check) — and cut it. The
target is a specific, measured reduction (e.g., halving the current ~18,150 words), not "trim a
little where convenient." Where a control-plane error message already tells an AI exactly what
went wrong and exactly what to run next, a paragraph of SKILL.md prose restating that same rule is
pure surface area for the AI to misread, skip, or contradict — it earns its place only if it
conveys something the code cannot.

---

## 7. Research agenda — run this before building anything

1. **Q&A with the operator, first.** Draft questions before assuming answers, e.g.: What exactly
   counts as success — zero operator corrections on a first-time KB run? A hard word/token budget
   for what an AI must read before its first action? Should the activation seed be a physical file
   the AI is told to read, a Claude-Code-style slash command, or something else — tool-agnostic
   was confirmed as a requirement (Codex ran the failing session, not Claude Code), so the answer
   cannot depend on a host-specific plugin mechanism.
2. **Reuse this repo's own prior research — do not re-derive it.** `apex-meta/kb/
   claude-code-orchestration-design` already has directly relevant, cited findings:
   - `wiki/concepts/compact-activation-seed.md`
   - `wiki/concepts/progressive-disclosure-for-agent-kbs.md`
   - `wiki/concepts/stop-condition-as-context-saver.md`
   - `wiki/summaries/token-efficient-information-design.md`
   Read these fully before proposing a new pattern.
3. **Test the activation-seed hypothesis directly**, rather than assuming it: does a tiny fixed
   entry point actually survive being embedded in an arbitrary, noisy operator conversation (as
   opposed to a clean session), or does it need the reinforcement described in Section 5 (the
   engine itself refusing to proceed without having been invoked first)?
4. **Resolve Class A (packaging) as its own workstream.** Whatever pipeline design is chosen, it is
   worthless to a Codex session if the engine scripts aren't reachable from wherever the "installed
   skill" actually lives. This may be a Codex-specific packaging fix, a repository-layout change, or
   a documented cross-repo pointer convention — decide based on how Codex's own skill-install
   mechanism actually resolves paths, not assumption.
5. **Close with an explicit feasibility/value verdict.** Given that Classes A and B may already
   explain most of the observed pain independently of doctrine size or activation-seed design, is
   the full redesign effort justified before those two are fixed and re-tested in isolation? State
   the answer plainly, with the reasoning, rather than proceeding on momentum.
