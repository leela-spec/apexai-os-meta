All three spec files fully read. Here is the complete implementation plan, derived entirely from. 
***

# Apex KB + SQLite FTS5/BM25 — Implementation Plan

***

## Part 0 — Thinking Paper

### Decision 1: Implementation Path

**Option A — Minimal Delta**
Add only the 10 action items from the gap analysis. No existing KB content is touched except the surgical front-matter append pass.

| | Option A | Option B |
|---|---|---|
| **Scope** | 10 targeted additions | Full KB restructure + 10 additions |
| **Risk** | Low — existing pages unchanged except 4 added fields | High — full rewrite risks silent content corruption |
| **Effort** | ~3–4h | ~8–12h |
| **Reversibility** | High — surgical script is diff-friendly | Low — mass rewrite is hard to audit |
| **When to choose** | Current KB structure is directionally correct | Current KB has structural debt requiring cleanup |

**Recommendation: Option A.** The gap analysis in `Claude_Apex KB_SQLiteFTS5BM25.md §4.5` explicitly states "No restructuring of existing folders required" — the delta is exactly 10 items.  Option B introduces significant rewrite risk for zero architectural benefit at this stage. Choose Option B only if the pre-flight audit reveals >40% of pages have corrupted or inconsistent structure beyond the 4 missing fields. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)

**Assumption:** If >50% of wiki pages have additional structural deviations not covered by the 4 known missing fields, re-evaluate before running the script.

***

### Decision 2: `search.sqlite` — Per-KB vs. Shared

| | Per-KB (`apex-meta/kb/<slug>/search.sqlite`) | Shared (`apex-meta/registry/search.sqlite`) |
|---|---|---|
| Query scoping | Native — no `WHERE kb =` needed | Requires `AND ft.kb = ?` filter on every query |
| Cross-KB queries | Impossible | Possible |
| Index rebuild isolation | Per-KB rebuild doesn't touch others | One rebuild touches all |
| Spec alignment | Contradicts spec canonical path | Matches spec exactly |

**Recommendation: Shared at `apex-meta/registry/search.sqlite`.** The spec's Python `search_kb()` function already includes `AND ft.kb = ?` as a required parameter — per-KB scoping is handled in SQL, not by file separation.  A shared file also enables future cross-KB queries without architectural change. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)

***

### Decision 3: Sequencing Risk

**What breaks if indexer runs before front-matter update:**
- Pages missing `id` → indexer inserts `NULL` primary key → FTS5 `id` column is empty → result rows have no path reference → Claude receives ranked results with no file path to open
- Pages missing `kb` → `WHERE ft.kb = ?` returns zero rows for every query → system appears broken
- Pages missing `status` → `WHERE ft.status = 'current'` returns zero rows (same failure)
- Pages missing `summary` → summary column is `NULL` → snippet pre-filtering is degraded but non-fatal

**Safe sequence:**
1. Pre-flight audit → count missing fields
2. Front-matter surgical update → all pages get `id`, `kb`, `status`, `summary`
3. Manifest update → add `status`, `lastmodified`
4. Create `apex-meta/registry/`
5. Write scripts
6. First index build
7. First search test
8. Write skill/rules/CLAUDE.md additions
9. End-to-end Claude test

***

## Part 1 — Pre-Flight Audit Checklist

Run these one-liners from repo root before any implementation step. Output: one line each, count or YES/NO.

```bash
# Missing `id` in front-matter
grep -rL "^id:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l

# Missing `kb` in front-matter
grep -rL "^kb:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l

# Missing `status` in front-matter
grep -rL "^status:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l

# Missing `summary` in front-matter
grep -rL "^summary:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l

# Manifest entries missing `status` field
python3 -c "
import json, glob, sys
total=0
for f in glob.glob('apex-meta/kb/*/manifests/source-manifest.json'):
    entries=json.load(open(f)) if isinstance(json.load(open(f)),list) else [json.load(open(f))]
    total+=sum(1 for e in entries if 'status' not in e)
print(total)
"

# Manifest entries missing `lastmodified` field
python3 -c "
import json, glob
total=0
for f in glob.glob('apex-meta/kb/*/manifests/source-manifest.json'):
    d=json.load(open(f))
    entries=d if isinstance(d,list) else d.get('sources',[d])
    total+=sum(1 for e in entries if 'last_modified' not in e and 'lastmodified' not in e)
print(total)
"

# registry/ exists?
[ -d apex-meta/registry ] && echo YES || echo NO

# scripts/apex-index.py exists?
[ -f scripts/apex-index.py ] && echo YES || echo NO

# scripts/apex-search.py exists?
[ -f scripts/apex-search.py ] && echo YES || echo NO

# .claude/skills/apex-search.md exists?
[ -f .claude/skills/apex-search.md ] && echo YES || echo NO

# UTF-8 encoding check (prints non-UTF-8 files; empty = all clean)
file --mime-encoding apex-meta/kb/*/wiki/**/*.md 2>/dev/null | grep -v "utf-8" | grep -v "us-ascii"
```

**Assumption:** `source-manifest.json` is either a JSON array or a JSON object with a `sources` key. If your manifest uses a different top-level structure, the Python one-liners need adjustment before running.

***

## Part 2 — Execution Plan

***

### Step 1 — Pre-flight audit
**What:** Run all 11 checks from Part 1 and log baseline counts.
**Artifact:** `apex-meta/registry/preflight-audit-<date>.txt`
**Claude's action:**
```bash
mkdir -p apex-meta/registry
# Run each check above, pipe to log:
(echo "=== Pre-flight Audit $(date) ===" && \
 echo "missing id:     $(grep -rL '^id:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" && \
 echo "missing kb:     $(grep -rL '^kb:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" && \
 echo "missing status: $(grep -rL '^status:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" && \
 echo "missing summary:$(grep -rL '^summary:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" && \
 echo "registry_dir:   $([ -d apex-meta/registry ] && echo YES || echo NO)" && \
 echo "apex-index.py:  $([ -f scripts/apex-index.py ] && echo YES || echo NO)" && \
 echo "apex-search.py: $([ -f scripts/apex-search.py ] && echo YES || echo NO)" && \
 echo "apex-search.md: $([ -f .claude/skills/apex-search.md ] && echo YES || echo NO)") \
 | tee apex-meta/registry/preflight-audit-$(date +%Y-%m-%d).txt
```
**Validation gate:** Log file exists and all counts are numeric values (no errors).
**Estimated time:** 5 min
**Blocking dependency:** None

***

### Step 2 — Decide Option A vs. Option B
**What:** Operator reviews preflight log and decides implementation path.
**Artifact:** Decision noted in `apex-meta/registry/preflight-audit-<date>.txt`
**Claude's action:** Read preflight log, present summary table to operator. Await explicit confirmation of Option A before proceeding.
**Decision rule:**
- If structural deviations are limited to the 4 known missing fields → **Option A** (default)
- If >50% of pages have additional structural problems (missing `title`, `tags`, corrupted YAML) → **Option B** (operator must explicitly confirm)
**Validation gate:** Operator says "proceed with Option A" or "proceed with Option B."
**Estimated time:** 5 min
**Blocking dependency:** Step 1

***

### Step 3 — Front-matter surgical update
**What:** Add `id`, `kb`, `status`, `summary` to all wiki pages that are missing them — no existing content rewritten.
**Artifact:** Modified `wiki/**/*.md` files across all KB slugs
**Claude's action:** Write and run `scripts/fix-frontmatter.py`:

```python
# scripts/fix-frontmatter.py
# CLI: python scripts/fix-frontmatter.py --kb <slug>
# For each wiki page: read front-matter, append ONLY missing fields, write back.
# Never rewrites existing fields. Preserves body unchanged.
# Derives `id` from filename stem (lowercased, hyphens). 
# Derives `kb` from parent kb-slug directory name.
# Sets `status: current` if missing.
# Sets `summary: ""` with TODO marker if missing (operator fills in).
```

**Function signatures:**
```python
def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Returns (frontmatter_dict, body_str). Handles --- delimiters."""

def write_frontmatter(path: Path, fm: dict, body: str) -> None:
    """Writes front-matter back as YAML block + body. Preserves body exactly."""

def patch_page(path: Path, kb_slug: str) -> bool:
    """Returns True if page was modified. Only writes if change needed."""

def main(kb_slug: str, wiki_dir: Path, dry_run: bool = False) -> None:
    """Iterates all .md under wiki_dir, patches each, prints count."""
```

**CLI spec:**
```
python scripts/fix-frontmatter.py --kb <slug> [--dry-run]
--kb       required: kb slug string (e.g. prompt-engineer-research-base)
--dry-run  optional: print what would change, don't write
```

**Validation gate:**
```bash
# After run, count should be 0:
grep -rL "^id:" apex-meta/kb/<slug>/wiki/**/*.md | wc -l
grep -rL "^kb:" apex-meta/kb/<slug>/wiki/**/*.md | wc -l
grep -rL "^status:" apex-meta/kb/<slug>/wiki/**/*.md | wc -l
```
**Estimated time:** 20 min (write script 15 min + run + verify 5 min)
**Blocking dependency:** Step 2

***

### Step 4 — Manifest update
**What:** Add `"status": "compiled"` and `"last_modified": "<date>"` to all manifest entries missing them.
**Artifact:** Updated `apex-meta/kb/*/manifests/source-manifest.json`
**Claude's action:** Write and run `scripts/fix-manifest.py`:

```python
# scripts/fix-manifest.py
# CLI: python scripts/fix-manifest.py --kb <slug>
# For each entry in source-manifest.json: add status="compiled" and last_modified=today if missing.
# Never removes or rewrites existing fields. Writes back as formatted JSON.
```

**Function signatures:**
```python
def patch_manifest(manifest_path: Path, default_date: str) -> int:
    """Returns count of entries patched. default_date = today ISO."""

def main(kb_slug: str) -> None:
    """Locates manifest, patches, writes back, prints summary."""
```

**CLI spec:**
```
python scripts/fix-manifest.py --kb <slug>
```

**Validation gate:**
```bash
python3 -c "
import json
d=json.load(open('apex-meta/kb/<slug>/manifests/source-manifest.json'))
entries=d if isinstance(d,list) else d.get('sources',[])
missing=[e for e in entries if 'status' not in e or 'last_modified' not in e]
print(len(missing))
"
# Expected: 0
```
**Estimated time:** 15 min
**Blocking dependency:** Step 3

***

### Step 5 — Create `apex-meta/registry/` directory
**What:** Create canonical home for `search.sqlite` and cross-KB registry files.
**Artifact:** `apex-meta/registry/` directory with `.gitkeep`
**Claude's action:**
```bash
mkdir -p apex-meta/registry
touch apex-meta/registry/.gitkeep
```
**Validation gate:** `[ -d apex-meta/registry ] && echo OK`
**Estimated time:** 2 min
**Blocking dependency:** Step 1 (directory may already exist after Step 1 creates it — idempotent)

***

### Step 6 — Write `scripts/apex-index.py`
**What:** Create the SQLite FTS5 indexer that reads all wiki pages and builds `search.sqlite`.
**Artifact:** `scripts/apex-index.py`
**Reference:** Spec file §2.3 (`CREATE VIRTUAL TABLE` statement), §4.5 item 4. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)

**Function signatures:**
```python
def get_wiki_pages(kb_dir: Path) -> list[Path]:
    """Returns all .md files under <kb_dir>/wiki/ recursively."""

def parse_page(path: Path, kb_slug: str, repo_root: Path) -> dict | None:
    """Parses front-matter + body. Returns dict with all FTS5 fields.
    Returns None if page is missing required fields (logs warning)."""

def build_index(pages: list[dict], db_path: Path) -> int:
    """Drops and recreates FTS5 table + wiki_meta table.
    Inserts all pages with status='current'.
    Returns count of rows inserted."""

def check_stale(db_path: Path, wiki_dir: Path) -> tuple[bool, str]:
    """Returns (is_stale, reason). Reason is human-readable string."""

def main() -> None:
    """CLI entry point. Handles --rebuild, --check-stale, --kb, --db flags."""
```

**CLI spec:**
```
python scripts/apex-index.py --rebuild --kb <slug>
python scripts/apex-index.py --check-stale --kb <slug>

--kb          required: kb slug
--rebuild     full drop-recreate-insert cycle
--check-stale outputs OK or STALE: <reason>, exit 0 either way
--db          optional: override db path (default: apex-meta/registry/search.sqlite)
--repo-root   optional: override repo root (default: cwd)
```

**Validation gate:**
```bash
python scripts/apex-index.py --rebuild --kb <slug>
# Expected output: "Indexed N pages → apex-meta/registry/search.sqlite"
# Verify: sqlite3 apex-meta/registry/search.sqlite "SELECT count(*) FROM ft;"
# Count must match: find apex-meta/kb/<slug>/wiki -name "*.md" | wc -l
```
**Estimated time:** 30 min
**Blocking dependency:** Steps 3, 4, 5

***

### Step 7 — Write `scripts/apex-search.py`
**What:** Create the CLI query interface over `search.sqlite`.
**Artifact:** `scripts/apex-search.py`
**Reference:** Spec file §2.3 (`search_kb()` function, BM25 weight vector, output format). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)

**Function signatures:**
```python
def search_kb(query: str, kb: str, db_path: str, limit: int, status_filter: str) -> list[dict]:
    """Exact function from spec §2.3. Returns list of result dicts."""

def format_results(results: list[dict], query: str, kb: str) -> str:
    """Formats results in the spec §2.3 output format with rank, path, title,
    updated, sources, score, snippet."""

def main() -> None:
    """CLI entry point."""
```

**CLI spec:**
```
python scripts/apex-search.py --kb <slug> --q "<query>" [--limit 8] [--db <path>]
python scripts/apex-search.py --check-stale --kb <slug>

--kb           required
--q            required for search: query string
--limit        optional: default 8, max 20
--check-stale  outputs OK or STALE: <reason>
--db           optional: override db path
--format       optional: text (default) | json
```

**Validation gate:**
```bash
python scripts/apex-search.py --kb <slug> --q "test query" --limit 3
# Expected: formatted result block with rank, path, title, snippet
# Must not crash; must return ≥1 result if KB is non-empty
```
**Estimated time:** 20 min
**Blocking dependency:** Step 6

***

### Step 8 — First index build
**What:** Run the indexer against the actual KB and verify row count.
**Artifact:** `apex-meta/registry/search.sqlite` (populated)
**Claude's action:**
```bash
python scripts/apex-index.py --rebuild --kb <slug>
# Then verify:
sqlite3 apex-meta/registry/search.sqlite "SELECT count(*) FROM ft;"
find apex-meta/kb/<slug>/wiki -name "*.md" | wc -l
```
**Validation gate:** SQLite row count equals wiki page count (excluding `index.md` if it is not indexed). If count is 0, check that Step 3 completed — missing `status` field causes all pages to be excluded.
**Estimated time:** 10 min
**Blocking dependency:** Steps 6, 7

***

### Step 9 — First search test
**What:** Run 3 test queries and confirm ranked output with snippets.
**Artifact:** None (console verification)
**Claude's action:** Run 3 queries representative of the KB's actual content:
```bash
python scripts/apex-search.py --kb <slug> --q "<topic-1>" --limit 5
python scripts/apex-search.py --kb <slug> --q "<topic-2>" --limit 5
python scripts/apex-search.py --kb <slug> --q "<topic-3>" --limit 5
```
**Validation gate (pass criteria per query):**
- At least 1 result returned
- Result includes: path, title, score (negative float), snippet with `>>>` markers
- Top result is intuitively correct for the query
- Snippet contains at least one query term wrapped in `>>>...<<<`

**If zero results:** Check that `status: current` was correctly written in Step 3.
**Estimated time:** 10 min
**Blocking dependency:** Step 8

***

### Step 10 — Write `.claude/skills/apex-search.md`
**What:** Create the skill file that triggers the search workflow in Claude Code.
**Artifact:** `.claude/skills/apex-search.md`
**Reference:** Spec file §3.2 (exact skill file content). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)
**Claude's action:**
```bash
mkdir -p .claude/skills
# Write exact content from spec §3.2 to .claude/skills/apex-search.md
```
**Validation gate:**
```bash
[ -f .claude/skills/apex-search.md ] && head -5 .claude/skills/apex-search.md
# Must show: name: apex-search, triggers section present
```
**Estimated time:** 10 min
**Blocking dependency:** Step 9

***

### Step 11 — Update `CLAUDE.md`
**What:** Add KB retrieval block so Claude loads retrieval behavior at session start.
**Artifact:** `CLAUDE.md` (modified — append only)
**Reference:** Spec file §3.3 (exact CLAUDE.md block). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)
**Claude's action:**
```bash
# Read current CLAUDE.md, check if KB Retrieval section exists
grep -n "KB Retrieval" CLAUDE.md
# If not present: append exact block from spec §3.3
# If present: do NOT overwrite — report to operator
```
**Two valid approaches:**
- A: Append to end of CLAUDE.md — simpler, may create ordering issues
- B: Insert after the first major section break — cleaner but requires manual placement

**Recommendation: Option A (append).** Operator can manually reorder later; appending is safe and auditable.

**Validation gate:**
```bash
grep -A 10 "KB Retrieval" CLAUDE.md
# Must show: apex-meta/kb path, apex-search skill reference, known KBs list
```
**Estimated time:** 10 min
**Blocking dependency:** Step 10

***

### Step 12 — Write `.claude/rules/apex-meta.md`
**What:** Create path-scoped rule file that restricts Claude behavior inside `apex-meta/`.
**Artifact:** `.claude/rules/apex-meta.md`
**Reference:** Spec file §3.3 (path-scoped rules block). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200)
**Claude's action:**
```bash
mkdir -p .claude/rules
# Write exact content from spec §3.3 to .claude/rules/apex-meta.md
```
**Validation gate:**
```bash
[ -f .claude/rules/apex-meta.md ] && cat .claude/rules/apex-meta.md
# Must contain: no silent wiki/ writes, no raw/ deletes, audit-log append-only
```
**Estimated time:** 5 min
**Blocking dependency:** Step 11

***

### Step 13 — End-to-end Claude test
**What:** Give Claude a KB question and verify the full loop executes correctly.
**Artifact:** Optional saved query at `outputs/queries/<date>-<topic>.md`
**Test prompt to Claude:** `"What does the KB say about [topic central to your KB]?"`

**Verification checklist:**
- [ ] Claude does NOT open `wiki/index.md` first
- [ ] Claude triggers `apex-search` skill (visible in tool calls)
- [ ] Claude runs `python scripts/apex-search.py --check-stale` first
- [ ] Claude runs `python scripts/apex-search.py --kb <slug> --q "..." --limit 8`
- [ ] Claude reads ≤4 wiki pages
- [ ] Answer includes inline source pointer in format `[wiki/path.md §Section]`
- [ ] No hallucinated sources

**Validation gate:** All 7 checklist items pass. If Claude reads `index.md` first, the CLAUDE.md retrieval block from Step 11 needs strengthening with more explicit ordering instruction.
**Estimated time:** 15 min
**Blocking dependency:** Steps 10, 11, 12

***

### Step 14 — Add `search.sqlite` to `.gitignore`
**What:** Prevent the derived index artifact from being committed to version control.
**Artifact:** `.gitignore` (modified)
**Claude's action:**
```bash
grep -q "search.sqlite" .gitignore || echo "apex-meta/registry/search.sqlite" >> .gitignore
```
**Validation gate:** `grep search.sqlite .gitignore` — must return the line.
**Estimated time:** 2 min
**Blocking dependency:** Step 5

***

### Step 15 — Document implementation in `apex-meta/registry/index.md`
**What:** Write the cross-KB registry index documenting the implemented system.
**Artifact:** `apex-meta/registry/index.md`
**Claude's action:** Write a short structured document with:
```markdown
# Apex Registry

## Active KBs
| slug | wiki_pages | index_rows | last_rebuilt | status |
|---|---|---|---|---|
| <slug> | N | N | YYYY-MM-DD | OK |

## Retrieval Engine
- Engine: SQLite FTS5/BM25
- Index path: apex-meta/registry/search.sqlite
- Index script: scripts/apex-index.py
- Search script: scripts/apex-search.py
- Skill: .claude/skills/apex-search.md

## Rebuild command
python scripts/apex-index.py --rebuild --kb <slug>
```
**Validation gate:** File exists, table row count matches actual KB slugs.
**Estimated time:** 10 min
**Blocking dependency:** Step 13

***

## Part 3 — Validation Protocol

### Test 1 — Index Integrity
```bash
# Row count matches page count:
PAGES=$(find apex-meta/kb/<slug>/wiki -name "*.md" | wc -l)
ROWS=$(sqlite3 apex-meta/registry/search.sqlite "SELECT count(*) FROM ft WHERE kb='<slug>';")
[ "$PAGES" = "$ROWS" ] && echo PASS || echo "FAIL: pages=$PAGES rows=$ROWS"

# No stale/flagged pages in index:
STALE=$(sqlite3 apex-meta/registry/search.sqlite "SELECT count(*) FROM ft WHERE status != 'current';")
[ "$STALE" = "0" ] && echo PASS || echo "FAIL: stale_rows=$STALE"
```
**Pass criteria:** Both checks return PASS.

***

### Test 2 — Query Determinism
```bash
for i in 1 2 3; do
  python scripts/apex-search.py --kb <slug> --q "test query" --limit 5 --format json
done | md5sum
# All 3 outputs must produce identical hash
```
**Pass criteria:** All three `md5sum` values identical.

***

### Test 3 — Snippet Quality
Run 3 test queries. For each result:
- Snippet must contain at least one `>>>term<<<` match marker
- Snippet token count ≤30 (count words in snippet text excluding markers)

```bash
python scripts/apex-search.py --kb <slug> --q "<query>" --limit 3
# Visually inspect each snippet: contains query term? ≤30 words?
```
**Pass criteria:** ≥1 match marker per snippet; all snippets ≤30 tokens.

***

### Test 4 — Skill Trigger Test
Give Claude: `"Using the KB, explain <concept>."`
**Pass criteria:**
- Skill `apex-search` fires (visible in Claude Code tool call log)
- `python scripts/apex-search.py` invoked before any `Read` calls
- ≤4 wiki pages opened
- No `wiki/index.md` opened

***

### Test 5 — Staleness Detection
```bash
# Modify a wiki page:
echo "" >> apex-meta/kb/<slug>/wiki/summaries/some-page.md

# Check stale:
python scripts/apex-search.py --check-stale --kb <slug>
# Expected: "STALE: <page>.md newer than index"

# Rebuild:
python scripts/apex-index.py --rebuild --kb <slug>

# Check again:
python scripts/apex-search.py --check-stale --kb <slug>
# Expected: "OK"
```
**Pass criteria:** First check returns STALE, second returns OK.

***

### Test 6 — Failure Mode Test
```bash
# Delete index:
rm apex-meta/registry/search.sqlite

# Ask Claude a KB question — Claude must auto-rebuild:
# Expected: Claude runs --rebuild, then --q, returns results without operator prompt

# Zero-results test:
python scripts/apex-search.py --kb <slug> --q "xyzzy-nonexistent-term-abc" --limit 5
# Expected: empty result list + fallback message "No FTS5 results; falling back to index scan"
```
**Pass criteria:** Auto-rebuild completes without operator intervention; zero-result query prints explicit fallback message, does not silently return no output.

***

## Part 4 — Maintenance Procedures

| Trigger | Action | Command | Frequency |
|---|---|---|---|
| New wiki page added | Rebuild index | `python scripts/apex-index.py --rebuild --kb <slug>` | End of KB update session |
| Wiki page edited | Rebuild index | same | End of KB update session |
| New KB slug created | Create folder structure, run fix-frontmatter, rebuild | `mkdir -p apex-meta/kb/<slug>/{raw,manifests,wiki/{summaries,concepts,entities,synthesis},outputs/queries,audit,logs}` → `python scripts/apex-index.py --rebuild --kb <slug>` | On slug creation |
| Manifest entry added | Run fix-manifest, rebuild index | `python scripts/fix-manifest.py --kb <slug>` → rebuild | Per-session after manifest update |
| Query reused 3+ times | Save to `outputs/queries/` | Write `outputs/queries/<date>-<topic>.md` with `query:`, `retrieved_pages:`, `answer:` fields | When pattern recognized |
| Front-matter audit | Check all pages for missing/invalid fields | `grep -rL "^id:" apex-meta/kb/*/wiki/**/*.md` (repeat for kb/status/summary) | Monthly |
| UTF-8 check | Verify encoding before index rebuild | `file --mime-encoding apex-meta/kb/*/wiki/**/*.md \| grep -v utf-8` | Before any mass front-matter update |

***

## Part 5 — v1 Boundary: What Is Not in Scope

| Feature | Why Deferred |
|---|---|
| **Vector search** (Chroma, Qdrant, FAISS, LanceDB) | Requires embedding model (CPU/GPU inference), Docker or pip dependencies, and non-deterministic results. The corpus at v1 is lexically well-specified — exact terms, source paths, artifact names are the primary query surface. Lexical retrieval is sufficient.  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=xmxfcjjSkMSdumJ05kvj28BBrpc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200) |
| **Hybrid BM25 + vector** | Inherits all vector complexity plus adds re-ranking logic. Improvement is marginal over pure BM25 for a corpus of <500 pages with precise terminology.  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/ca1b3c94-f02e-485d-81d1-49ccdd3a5e90/KB-Researchv3_gpt_FB_claude.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=rX1C2RNgZqikNzX75ubvsep1P0s%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200) |
| **MCP connectors** | MCP is an adapter layer for external system integration, not a KB engine. v1 has no external system dependency. MCP adds tool-description overhead (~67% more execution steps per 2026 empirical study) without retrieval quality gain at this scale.  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/9a030661-6791-4ceb-8779-395ffb51e3e0/KB-Researchv3_gpt.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=yRqmLmm76ZARV0fXQDXytYM7Irc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200) |
| **Personal orchestration memory domain** (`apex-meta/orchestration/`) | Separate first-class memory domain for weekly/daily routines, model routing, flow recaps. Architecturally correct to separate from project KB, but not required for SQLite retrieval to function. Implement as a follow-on after v1 retrieval is stable.  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/9a030661-6791-4ceb-8779-395ffb51e3e0/KB-Researchv3_gpt.md?AWSAccessKeyId=ASIA2F3EMEYE2WTJWTZM&Signature=yRqmLmm76ZARV0fXQDXytYM7Irc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQz9g14IfahMzC93hfS0M6xrT8GxEt%2FSxiTp2JPo3adQIhALFiAKBc3KsLeEoVCOChQvdsb%2B3zcOX13z5yYmd0UbAJKvMECFEQARoMNjk5NzUzMzA5NzA1IgzLfphJ4NUgv5e7XtUq0AQE3Z6UPp2pp2ty4nhcNPJJm4Ybi%2BX6Rwxyq3xZIekrKJ7lKMX8umhribucmHHH4HaRM6e%2BDyWx83QyYt5A3XVW3hdoPavPaG0L7lShvcc4vhXQ5KulL3iTKzwLw231fIfRRx%2BXROcQeqy2gyH%2FUx6XthmG0lMqz2jzoRqcj3fHw9m9IzKNrYwtnGyGeWICwXcqrsidgrqqbKueGGv82z9YBigwUSnbjwAsNHh3XA30N8LzQ3R7D%2B7%2BrR04erF3FLlo4Uz2kAhhWMYx%2FuAljwnxrf7S%2FJAAbXkJJ0aevADnLsN42b6V97e5i8xLzGm4fpF2KQf24GqEy%2FCOz%2BUca8ReHq072qaSUS7ePFtsCQ73iNEwrpntYgr7ed3tP3rZ6kwwQaVuQBm7idiTyz3YIYCuMEq7xwN%2FN%2BkjD45FUgV9fHGS0tB1qap2pai5BzB46ydsgAwAgNEdojT%2BCalPdBbUfuq4c32vSY9g5Ctkghs4rKeMytZgzyHy8Ntti00iQMJg6uPFfyNDymxQvCHiJYIa88qbaUKquxKmFCNdJkDyhT73OJDfRo9zr9Qdfny2cGkI7rKMFyxU20a2cTjruDgpjx5P13WZ08dnL5vn%2BV05TBPNl3r4A6D6lx9ThOlJsB8VSF5bUsC6OEnusj5ioQfaoMTHpNUgPaACWz1i0a687llWT%2F4lf7IkwwZDDCuHyrALBy3jKEU963iMlvN22vXGT1Era62LjmN%2BsrwwuEi2zPu%2FqjaBQsQ2%2FfcYrf69JfbYjMwgGh4Ook9lS4K9vtLkMM2k9dEGOpcBldmlpNKPwPnGeXTS245mEmVZLOvjO92kVsIyN%2B1uuZFXOq7JRC6deYkctA7G1P4J7Xw3joZhsGiUUQTZ4aoxZiKIaKOvlZ2edxdzHFf0sG99U9RU50O7vFHXxC8VhKJosNmgl7Fi2ZbvFaJYr0qI2VOb2RHpzcUuYg%2BRntfpZiDKobp4%2F0v5HnQZHKQ5MJCddFVZYwTfbA%3D%3D&Expires=1782407200) |
| **Automatic manifest ingestion pipeline** | Would require hashing, change detection, and auto-compilation triggers. This is a full ingestion automation layer. v1 operator ingests manually. Automation introduces state mutation risk before the base pipeline is validated. |

***

**Total implementation estimate: 3–4 hours in a single focused session.** All scripts use Python stdlib only (`sqlite3`, `pathlib`, `json`, `re`, `argparse`). Zero new dependencies. Zero new directories beyond `apex-meta/registry/` and `.claude/skills/` + `.claude/rules/`. 