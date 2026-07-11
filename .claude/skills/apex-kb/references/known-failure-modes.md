# Apex KB Known Failure Modes

```yaml
artifact_name: apex_kb_known_failure_modes
package_path: .claude/skills/apex-kb/references/known-failure-modes.md
source_doctrine:
  - apex-meta/kb/apex-plan-sync-session-workflow-v2/
purpose: >
  Capture concrete, previously-observed apex-kb failure modes and their
  actionable pre-checks so a future KB run catches them before execution
  instead of mid-run, avoiding full rerun cycles.
```

## Failure mode 1: source-intake destination collision

**Mechanism:** `apex-meta/scripts/apex_kb.py`'s `source-intake --source-root` mode
computes each destination path from the file's basename alone, with no
per-source-root prefix. When two or more source roots contain files with
the same basename (for example, three skill packages each shipping their
own `SKILL.md` and `package-manifest.md`), intaking them in sequence causes
each later source to silently overwrite the stored content from an earlier
one at the same destination path. There is no error or warning — the
collision is only visible by noticing that a stored file's hash doesn't
match its claimed source, or that two logically distinct sources ended up
identical.

**Actionable pre-check:** Before running the first `source-intake` for a
multi-source-root ingest, scan every planned `--source-root` for repeated
basenames across roots. If any collide, assign each source root its own
destination bucket (e.g. `raw/plan/`, `raw/sync/`, `raw/session/`) instead
of intaking all roots into the same destination directory.

## Failure mode 2: topic-registry schema drift

**Mechanism:** `rank_topic_sources()` in `apex_kb.py` (around line 1038)
requires each entry in `manifests/topic-registry.json` to carry `slug` and
`name` fields. A registry hand-authored with `topic_id`/`title` instead of
`slug`/`name` passes no validation step — every such topic silently
collapses into a single `"unnamed"` ranking bucket during Phase 0, and
topic separation is defeated with no error raised.

**Actionable pre-check:** Before running `phase0`, validate that every
entry in `topic-registry.json` has both a non-empty `slug` and a non-empty
`name`. Fix any entry missing either field before proceeding.

## Pre-run checklist

Run both checks before calling `source-intake` or `phase0`.

**1. Basename collision scan across planned source roots (shell):**

```bash
for root in "$@"; do
  find "$root" -type f -printf '%f\n'
done | sort | uniq -d
```

If this prints any filenames, do not intake all roots into one destination
directory — assign each root a distinct destination bucket first.

**2. Topic-registry schema validation (python):**

```python
import json, sys

path = "manifests/topic-registry.json"
with open(path) as f:
    registry = json.load(f)

topics = registry.get("topics", registry) if isinstance(registry, dict) else registry
bad = [
    t for t in topics
    if not (isinstance(t, dict) and t.get("slug") and t.get("name"))
]
if bad:
    print(f"{len(bad)} topic entries missing slug/name:", bad)
    sys.exit(1)
print("topic-registry.json: all entries have slug and name")
```

Fix any flagged entries before running `phase0`.
