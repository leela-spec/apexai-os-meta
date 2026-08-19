# S04 — TTK Canonical Custody

**Execute only S04, then stop.**  
**Input:** canonical transcript candidate from S03  
**Next:** S05

## Outcome

Bring the transcript into the existing TTK deterministic evidence/state system: immutable source identity, stable segment IDs, timestamps, packet/run state, and source SHA custody.

## Context to load

- this file;
- S03 handoff + exact transcript artifact;
- `.claude/skills/transcript-to-knowledge/SKILL.md` sections on initialization/custody;
- TTK source/init code directly invoked by `ttk.py`;
- relevant TTK tests.

Do not load Map prompt/research yet.

## Tool

Existing TTK. Do not replace it with LangExtract, a database, vector store, or new state framework.

## Work

1. Verify input transcript hash matches S03 handoff.
2. Initialize the run's TTK directory, preferably `<run>/ttk/`.
3. Preserve original source/transcript artifact; normalization may create canonical data but must not silently mutate the original evidence.
4. Ensure stable segment IDs, timestamps where available, source SHA, and state metadata are created by the owning TTK code.
5. Record the relationship between S02/S03 transcript hash and TTK canonical source hash.

Typical command pattern:

```powershell
python .claude/skills/transcript-to-knowledge/scripts/ttk.py init <transcript> --output <run>\ttk
python .claude/skills/transcript-to-knowledge/scripts/ttk.py status <run>\ttk --json-output
```

Use actual supported syntax from current code.

## Tests

- TTK unit tests relevant to source parsing/custody pass;
- canonical source SHA is reproducible from the input artifact;
- every canonical segment has a stable unique ID;
- timestamps are preserved when source provides them;
- original transcript remains unchanged;
- rerun/init behavior does not silently create a different source identity for unchanged input;
- `ttk status` reports truthful pending state, not semantic completion.

## Outputs

TTK canonical source/state under `<run>/ttk/`, plus S04 handoff.

Handoff must name TTK run directory, canonical source hash, segment count, input transcript hash, and exact command/version/code SHA used.

## Acceptance

PASS means downstream windowing can derive its packets entirely from TTK state without rereading chat history.

Commit/push relevant code/test changes, return handoff, **STOP.**