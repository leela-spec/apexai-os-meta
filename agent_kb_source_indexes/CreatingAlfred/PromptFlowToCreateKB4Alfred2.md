## Recommendation

Do **not** continue the current “one browser chat builds many KB folders” plan. It is too fragile.

Use this replacement flow:

1. **Source-pack chat:** read Master Of Arts only and produce a compact extraction bundle.
    
2. **One-agent build chat:** build exactly one agent KB from that bundle.
    
3. **One-file write turns:** write exactly one Apex target file per turn.
    
4. **Verify after each file:** fetch the file back, compare intent, then proceed.
    
5. **Final audit turn:** repo-mixing drift check + source coverage check.
    

This reduces connector payload size, stale-SHA collisions, UI timeout risk, and source/write mixing.

---

## Why the current prompt fails

|Failure mode|Cause|Fix|
|---|---|---|
|UI “Something went wrong”|Long tool calls with large Markdown bodies|one file per turn, shorter body|
|Repeated stopped thinking|many connector calls + large context|split source extraction from writing|
|GitHub `409` stale SHA|update uses old file SHA after retry/interruption|fetch current SHA immediately before each write|
|Token-loss artifacts|source reading + synthesis + writes in same context|source bundle first, write pass second|
|Repo-mixing risk|both repos active during write phase|no Master Of Arts reads during write phase|

---

## Updated prompt flow

### Phase 0 — Source Bundle Prompt

Use this first, before any Apex writing:

```md
# Apex AI KB Source Bundle Builder

You are preparing a source bundle only. Do not write to any repo.

Source repo:
- leela-spec/MasterOfArts

Target repo for later:
- leela-spec/apexai-os-meta

Task:
Read the relevant Master Of Arts source index and all accessible repo sources for exactly one agent/head.

Agent/head:
- [PASTE_AGENT_ID]

Source index:
- [PASTE_INDEX_PATH]

Output:
Create a compact source bundle in Markdown with these sections:

1. SOURCE_INDEX_SUMMARY
   - every source listed in the index
   - role: primary/supporting/evidence/duplicate
   - read mode
   - accessible: yes/no
   - actual read status: fully_read / skimmed / not_accessible / not_needed
   - reason

2. EXTRACTION_LEDGER
   - stable claims extracted
   - source refs
   - confidence
   - contradiction/gap notes
   - candidate output file informed

3. DOCTRINE_DRAFT
   - identity and boundaries
   - owns / does not own
   - workflows
   - routing rules
   - failure modes
   - templates needed

4. SOURCE_GAP_REGISTER
   - inaccessible local/manual files
   - why they matter
   - what must be treated as inferred or index-derived

5. WRITE_PLAN
   - target Apex files
   - one-sentence purpose per file
   - file priority order

Rules:
- Master Of Arts is read-only.
- Do not write to Apex in this phase.
- Do not paste raw source dumps.
- Mark inferred claims explicitly.
- Preserve contradictions; do not resolve them silently.
```

---

### Phase 1 — One-Agent KB Build Prompt

Use the source bundle as input:

```md
# Apex AI KB Builder — One Agent Only

You are building the KB base for exactly one agent/head.

Agent/head:
- [PASTE_AGENT_ID]

Target repo:
- leela-spec/apexai-os-meta

Allowed write root:
- managed/agent_kb/[AGENT_ID]/

Source basis:
- Use the attached SOURCE_BUNDLE only.
- Do not read Master Of Arts in this phase unless an explicit source gap blocks the file being written.
- If a source is missing, record it in SOURCE_MANIFEST.md and COVERAGE_AUDIT.md.

Apex write rule:
- Apex AI is the only write target.
- Before every write, state:
  "Writing only to leela-spec/apexai-os-meta: [path]"
- Write exactly one file per turn.
- Before updating an existing file, fetch its current SHA.
- After writing, fetch the file back and verify.
- Do not proceed to the next file until verification is complete.

Target files:
1. AGENT_CARD.md
2. ESSENCE.md
3. BEST_PRACTICES.md
4. MISTAKES.md or MISTAKES_FAILURES.md
5. TEMPLATES.md
6. LEARNING_QUEUE.md
7. SOURCE_MANIFEST.md
8. COVERAGE_AUDIT.md

Convention rule:
- If Apex already uses a stronger existing convention, preserve it.
- If Apex uses `MISTAKES.md`, do not rename it to `MISTAKES_FAILURES.md`; mention alias compatibility in SOURCE_MANIFEST.md.
- Add missing extension files without breaking existing scaffold.

Quality bar:
- dense, operational, specific
- no generic AI advice
- source-grounded synthesis
- inferred details marked
- contradictions preserved in COVERAGE_AUDIT.md
```

---

### Phase 2 — Single-File Write Prompt

Use this for each file:

```md
# Apex AI KB Single-File Write

Write exactly one file.

Repo:
- leela-spec/apexai-os-meta

Path:
- managed/agent_kb/[AGENT_ID]/[FILE_NAME].md

Source basis:
- attached SOURCE_BUNDLE
- existing Apex KB conventions
- prior verified files in this agent KB folder

Rules:
1. Fetch current file first.
2. If it exists, use current SHA.
3. If it does not exist, create it.
4. Write only this one path.
5. Keep the body compact enough for one safe connector call.
6. After writing, fetch the file back.
7. Report:
   - path written
   - commit SHA
   - verification result
   - next recommended file
8. Do not write the next file in the same turn.
```

---

## Revised target-file convention

For Apex, use this safer convention:

```text
managed/agent_kb/<agent>/
  AGENT_CARD.md              # extension, if absent
  ESSENCE.md                 # existing accepted scaffold
  BEST_PRACTICES.md          # existing accepted scaffold
  MISTAKES.md                # keep existing Apex name
  TEMPLATES.md               # existing accepted scaffold
  LEARNING_QUEUE.md          # existing accepted scaffold
  SOURCE_MANIFEST.md         # extension, required by KB build flow
  COVERAGE_AUDIT.md          # extension, required by KB build flow
```

Do **not** force `MISTAKES_FAILURES.md` if Apex already uses `MISTAKES.md`.

---

## What I would do next for Alfred

Use one turn per file in this order:

```text
1. Verify LEARNING_QUEUE.md write status
2. Create SOURCE_MANIFEST.md
3. Create COVERAGE_AUDIT.md
4. Fetch all Alfred KB files
5. Run final repo-mixing drift check
```

For the next message, the safest instruction is:

```text
Continue with Alfred only. First verify whether managed/agent_kb/alfred/LEARNING_QUEUE.md was updated. Do not write anything else in that turn. Report current status and next file.
```