# Apex KB + SQLite FTS5/BM25 — Implementation Plan v2

## Multi-source verified | June 2026

---

## Part 0 — Thinking Paper

## Decision 1: Implementation Path

**Option A — Minimal Delta** | Add only the 10 gap-analysis items. Existing KB untouched except surgical front-matter append.

**Option B — Clean Rebuild** | Full KB restructure + 10 additions in one pass.

|Dimension|Option A|Option B|
|---|---|---|
|**Scope**|10 targeted additions|Full rewrite + 10 additions|
|**Risk**|Low — surgical script, diff-friendly|High — mass rewrite, hard to audit|
|**Effort (hrs)**|3–4|8–12|
|**Reversibility**|High — git diff shows exact change|Low — original pages overwritten|
|**When correct**|KB structure is directionally sound|KB has structural debt beyond 4 known fields|

**Recommendation: Option A.** The spec confirms "no restructuring of existing folders required" and the gap is precisely 10 items. Option B only if pre-flight audit reveals >50% of pages have corruption beyond the 4 known missing fields. **Assumption:** If your wiki pages have non-standard YAML delimiters (e.g., `+++` instead of `---`), the surgical script needs a parser adjustment before running.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)

---

## Decision 2: `search.sqlite` — Per-KB vs. Shared

||Per-KB|Shared (`apex-meta/registry/`)|
|---|---|---|
|Scoping|Native, no filter needed|`AND ft.kb = ?` required|
|Cross-KB queries|Impossible without file merge|Native via single query|
|Rebuild isolation|Per-slug rebuild safe|One stale page touches all KBs|
|Spec alignment|Contradicts spec §1.3|Matches spec exactly|

**Recommendation: Shared.** The spec's `search_kb()` function already requires `kb` as a mandatory parameter — per-KB scoping is enforced in SQL, not by file separation. Shared enables future cross-KB queries at zero additional cost.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)

---

## Decision 3: Sequencing Risk

**What breaks if indexer runs before front-matter update:**

- Missing `id` → FTS5 rows have NULL primary key → ranked results contain no file path → Claude cannot open any page
    
- Missing `kb` → `WHERE ft.kb = ?` returns 0 rows → system appears non-functional for every query
    
- Missing `status` → `WHERE ft.status = 'current'` returns 0 rows → identical failure
    
- Missing `summary` → NULL column → snippet pre-filtering degraded but non-fatal
    

**Safe sequence:** pre-flight → front-matter patch → manifest patch → create registry dir → write scripts → first build → validate → write skill/rules/CLAUDE.md → end-to-end test.

---

## Part 1 — Pre-Flight Audit

Run from repo root. Output: one line per check.

bash

``# 1. Missing `id` grep -rL "^id:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l # 2. Missing `kb` grep -rL "^kb:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l # 3. Missing `status` grep -rL "^status:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l # 4. Missing `summary` grep -rL "^summary:" apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l # 5. Manifest entries missing `status` python3 -c " import json, glob t=0 for f in glob.glob('apex-meta/kb/*/manifests/source-manifest.json'):     d=json.load(open(f))    e=d if isinstance(d,list) else d.get('sources',[d])    t+=sum(1 for x in e if 'status' not in x) print(t) " # 6. Manifest entries missing `last_modified` python3 -c " import json, glob t=0 for f in glob.glob('apex-meta/kb/*/manifests/source-manifest.json'):     d=json.load(open(f))    e=d if isinstance(d,list) else d.get('sources',[d])    t+=sum(1 for x in e if 'last_modified' not in x and 'lastmodified' not in x) print(t) " # 7. registry/ dir exists? [ -d apex-meta/registry ] && echo YES || echo NO # 8. scripts/apex-index.py exists? [ -f scripts/apex-index.py ] && echo YES || echo NO # 9. scripts/apex-search.py exists? [ -f scripts/apex-search.py ] && echo YES || echo NO # 10. .claude/skills/apex-search.md exists? [ -f .claude/skills/apex-search.md ] && echo YES || echo NO # 11. UTF-8 encoding check (non-UTF-8 files listed; empty = clean) file --mime-encoding apex-meta/kb/*/wiki/**/*.md 2>/dev/null \   | grep -v "utf-8" | grep -v "us-ascii"``

**Assumption:** `source-manifest.json` is either a JSON array or object with `sources` key. If your manifest uses a different top-level shape, the Python one-liners need adjustment.

---

## Part 2 — Execution Plan

---

## Step 1 — Pre-flight audit + log

**What:** Run all 11 checks, persist baseline to file.  
**Artifact:** `apex-meta/registry/preflight-<date>.txt`  
**Claude's action:**

bash

`mkdir -p apex-meta/registry (echo "=== Pre-flight $(date +%Y-%m-%d) ===" \  && echo "id_missing:      $(grep -rL '^id:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" \ && echo "kb_missing:      $(grep -rL '^kb:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" \ && echo "status_missing:  $(grep -rL '^status:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" \ && echo "summary_missing: $(grep -rL '^summary:' apex-meta/kb/*/wiki/**/*.md 2>/dev/null | wc -l)" \ && echo "registry_dir:    $([ -d apex-meta/registry ] && echo YES || echo NO)" \ && echo "apex-index.py:   $([ -f scripts/apex-index.py ] && echo YES || echo NO)" \ && echo "apex-search.py:  $([ -f scripts/apex-search.py ] && echo YES || echo NO)" \ && echo "apex-search.md:  $([ -f .claude/skills/apex-search.md ] && echo YES || echo NO)") \ | tee apex-meta/registry/preflight-$(date +%Y-%m-%d).txt`

**Validation gate:** Log file exists; all values are numeric or YES/NO (no shell errors).  
**Estimated time:** 5 min | **Blocking dependency:** None

---

## Step 2 — Operator decision: Option A vs. B

**What:** Operator reviews preflight log, confirms path.  
**Artifact:** Decision appended to preflight log.  
**Decision rule:** If all non-zero counts are limited to the 4 known missing fields (`id`, `kb`, `status`, `summary`) → Option A. If additional structural anomalies detected → discuss before proceeding.  
**Claude's action:** Present preflight summary table. Await operator confirmation.  
**Estimated time:** 5 min | **Blocking dependency:** Step 1

---

## Step 3 — Front-matter surgical update

**What:** Append `id`, `kb`, `status`, `summary` to pages missing them. Never rewrites existing content.  
**Artifact:** Modified `wiki/**/*.md` across all KB slugs.  
**Claude writes:** `scripts/fix-frontmatter.py`

**Function signatures (Option A — surgical append only):**

python

`def parse_frontmatter(path: Path) -> tuple[dict, str]:     """Read YAML front-matter between --- delimiters. Returns (fm_dict, body_str).""" def write_frontmatter(path: Path, fm: dict, body: str) -> None:     """Write YAML front-matter block + body. Preserves body byte-for-byte.""" def patch_page(path: Path, kb_slug: str) -> bool:     """Add only missing fields. Returns True if modified. Never touches existing fields."""    # id  → derived from path.stem (lowercase, hyphens)    # kb  → kb_slug argument    # status → "current"    # summary → "TODO: add one-sentence summary" def main(kb_slug: str, wiki_dir: Path, dry_run: bool) -> None:     """Iterate wiki_dir/**/*.md, patch each, report count."""`

**CLI spec:**

text

`python scripts/fix-frontmatter.py --kb <slug> [--dry-run] --kb        required: KB slug string --dry-run   print what would change, no writes`

**Validation gate:**

bash

`grep -rL "^id:" apex-meta/kb/<slug>/wiki/**/*.md | wc -l   # → 0 grep -rL "^kb:" apex-meta/kb/<slug>/wiki/**/*.md | wc -l   # → 0 grep -rL "^status:" apex-meta/kb/<slug>/wiki/**/*.md | wc -l  # → 0`

**Estimated time:** 20 min | **Blocking dependency:** Step 2

---

## Step 4 — Manifest update

**What:** Add `"status": "compiled"` and `"last_modified": "<today>"` to manifest entries missing them.  
**Artifact:** Updated `apex-meta/kb/*/manifests/source-manifest.json`  
**Claude writes:** `scripts/fix-manifest.py`

**Function signatures:**

python

`def patch_manifest(manifest_path: Path, default_date: str) -> int:     """Add status + last_modified to entries missing them. Returns patch count.""" def main(kb_slug: str) -> None:     """Locate manifest, patch, write formatted JSON, print count."""`

**CLI spec:**

text

`python scripts/fix-manifest.py --kb <slug>`

**Validation gate:**

bash

`python3 -c " import json d=json.load(open('apex-meta/kb/<slug>/manifests/source-manifest.json')) e=d if isinstance(d,list) else d.get('sources',[]) print(sum(1 for x in e if 'status' not in x or 'last_modified' not in x)) " # Expected: 0`

**Estimated time:** 15 min | **Blocking dependency:** Step 3

---

## Step 5 — Create `apex-meta/registry/`

**What:** Create canonical home for `search.sqlite` and cross-KB index.  
**Artifact:** `apex-meta/registry/.gitkeep`  
**Claude's action:**

bash

`mkdir -p apex-meta/registry touch apex-meta/registry/.gitkeep`

**Validation gate:** `[ -d apex-meta/registry ] && echo OK`  
**Estimated time:** 2 min | **Blocking dependency:** Step 1 (idempotent)

---

## Step 6 — Write `scripts/apex-index.py`

**What:** SQLite FTS5 indexer — reads wiki pages, builds `search.sqlite`.  
**Reference:** Spec §2.3 — `CREATE VIRTUAL TABLE` statement, schema, staleness function.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)  
**Artifact:** `scripts/apex-index.py`

**Function signatures:**

python

`def get_wiki_pages(kb_dir: Path) -> list[Path]:     """Return all .md under <kb_dir>/wiki/ recursively. Excludes index.md.""" def parse_page(path: Path, kb_slug: str, repo_root: Path) -> dict | None:     """Parse front-matter + body. Returns FTS5 field dict.    Returns None + logs warning if required fields missing.""" def build_index(pages: list[dict], db_path: Path) -> int:     """DROP + CREATE VIRTUAL TABLE ft (spec §2.3 schema).    CREATE TABLE wiki_meta (id, path, updated, status, kb).    INSERT all pages with status='current'. Returns row count.""" def check_stale(db_path: Path, wiki_dir: Path) -> tuple[bool, str]:     """Return (is_stale, reason_str). Checks db existence + mtime vs page mtimes.""" def main() -> None:     """argparse entry point. --rebuild | --check-stale | --kb | --db | --repo-root"""`

**CLI spec:**

text

`python scripts/apex-index.py --rebuild --kb <slug> python scripts/apex-index.py --check-stale --kb <slug> --kb           required --rebuild      drop + recreate + insert --check-stale  stdout: "OK" or "STALE: <reason>", exit 0 always --db           optional, default: apex-meta/registry/search.sqlite --repo-root    optional, default: cwd`

**Two valid approaches for NULL-field handling:**

- A: Skip page entirely, log warning (safe, conservative)
    
- B: Insert with NULL, exclude via `WHERE status='current'` (more permissive)
    

**Recommendation: Option A.** A page with missing `id` or `kb` is invalid for FTS5 use — skipping it prevents silent corruption of the result set.

**Validation gate:**

bash

`python scripts/apex-index.py --rebuild --kb <slug> sqlite3 apex-meta/registry/search.sqlite "SELECT count(*) FROM ft;" find apex-meta/kb/<slug>/wiki -name "*.md" ! -name "index.md" | wc -l # Both counts must match (±0 if no index.md; ±1 if index.md excluded)`

**Estimated time:** 30 min | **Blocking dependency:** Steps 3, 4, 5

---

## Step 7 — Write `scripts/apex-search.py`

**What:** CLI query interface over `search.sqlite`.  
**Reference:** Spec §2.3 — `search_kb()` function, BM25 weight vector `(0,0,0,5,3,2,0,0,0,1)`, output format.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)  
**Artifact:** `scripts/apex-search.py`

**Function signatures:**

python

`def search_kb(query: str, kb: str, db_path: str,               limit: int = 8, status_filter: str = "current") -> list[dict]:    """Exact implementation from spec §2.3. Uses bm25(ft,0,0,0,5,3,2,0,0,0,1).""" def format_results(results: list[dict], query: str, kb: str) -> str:     """Spec §2.3 output: rank, path, title, updated, sources, score, snippet with >>><<<.""" def main() -> None:     """argparse entry point."""`

**CLI spec:**

text

`python scripts/apex-search.py --kb <slug> --q "<query>" [--limit 8] [--db <path>] [--format text|json] python scripts/apex-search.py --check-stale --kb <slug>`

**Validation gate:**

bash

`python scripts/apex-search.py --kb <slug> --q "test" --limit 3 # Must return: ≥1 result, negative float score, snippet with >>>markers<<< # Must NOT crash on empty result set`

**Estimated time:** 20 min | **Blocking dependency:** Step 6

---

## Step 8 — First index build

**What:** Run indexer against actual KB, verify row count.  
**Artifact:** `apex-meta/registry/search.sqlite` (populated)  
**Claude's action:**

bash

`python scripts/apex-index.py --rebuild --kb <slug> echo "SQLite rows: $(sqlite3 apex-meta/registry/search.sqlite 'SELECT count(*) FROM ft;')" echo "Wiki pages:  $(find apex-meta/kb/<slug>/wiki -name '*.md' ! -name 'index.md' | wc -l)"`

**Validation gate:** Row count = wiki page count. If 0: check Step 3 completed — missing `status` field causes all pages to be excluded by `WHERE status='current'`.  
**Estimated time:** 10 min | **Blocking dependency:** Steps 6, 7

---

## Step 9 — First search test (3 queries)

**What:** Confirm ranked output with snippets on real content.  
**Artifact:** None (console verification)  
**Claude's action:**

bash

`python scripts/apex-search.py --kb <slug> --q "<core-topic-1>" --limit 5 python scripts/apex-search.py --kb <slug> --q "<core-topic-2>" --limit 5 python scripts/apex-search.py --kb <slug> --q "<core-topic-3>" --limit 5`

**Validation gate per query:**

- ≥1 result returned
    
- Score is a negative float
    
- Snippet contains `>>>term<<<` markers
    
- Top result is intuitively correct for the query
    

**Estimated time:** 10 min | **Blocking dependency:** Step 8

---

## Step 10 — Write `.claude/skills/apex-search.md`

**What:** Create skill file that triggers the retrieval loop in Claude Code.  
**Reference:** Spec §3.2 — exact skill file content.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)  
**Artifact:** `.claude/skills/apex-search.md`  
**Claude's action:**

bash

`mkdir -p .claude/skills # Write exact content from spec §3.2`

**Validation gate:**

bash

`head -8 .claude/skills/apex-search.md # Must show: name: apex-search, triggers: block present`

**Estimated time:** 10 min | **Blocking dependency:** Step 9

---

## Step 11 — Update `CLAUDE.md`

**What:** Append KB retrieval block so Claude loads retrieval behavior at boot.  
**Reference:** Spec §3.3 — exact CLAUDE.md block.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)  
**Claude's action:**

bash

``grep -q "KB Retrieval" CLAUDE.md \   && echo "ALREADY EXISTS — do not overwrite" \  || cat >> CLAUDE.md << 'EOF' ## KB Retrieval - Canonical KB: `apex-meta/kb/<kb-slug>/` - Do not read raw sources unless resolving flagged contradiction - Before answering any KB-dependent question:   1. Check `outputs/queries/` for matching saved answer  2. If none, trigger skill `apex-search`  3. Read wiki pages only after reviewing search results - Index: `apex-meta/registry/search.sqlite` - Check staleness before every query after KB update sessions - All KB citations must include: page path + section pointer ## Known KBs - `<slug>` — [one-line description] EOF``

**Validation gate:** `grep -A 12 "KB Retrieval" CLAUDE.md` — shows complete block.  
**Estimated time:** 10 min | **Blocking dependency:** Step 10

---

## Step 12 — Write `.claude/rules/apex-meta.md`

**What:** Path-scoped rule file restricting Claude behavior inside `apex-meta/`.  
**Reference:** Spec §3.3 — path-scoped rules block.[Claude_Apex-KB_SQLiteFTS5BM25.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/061f11b3-7cff-4e87-8cd0-160ab496374a/Claude_Apex-KB_SQLiteFTS5BM25.md?AWSAccessKeyId=ASIA2F3EMEYEXJYS2VVT&Signature=Ouct2Xi6sstILkkgQ96zAmyIr8M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIALPC9lEFcx4Icwn7PE2CLjUw83WCKaPqyH9jAch3zHTAiAHoC5iydfW13SZrNmonXq187AklBxekjGAoKwqgiBqDCrzBAhREAEaDDY5OTc1MzMwOTcwNSIMX4cNAtq3Eub%2FI%2B8WKtAEUVnX6I6hcMKKILz4FEOtjtAwtvRR%2B%2B6Vkwi73xQK1P7Dg%2BNSWspM8XdbMZVMKuR8cDGRhpNVLM5b%2BvYw%2FLrFHhSxh6mLpauME5GqitNMqh68MlXeoKCJ06E8IgH0J6kNpjRK%2Bwsy1J0gz87pG6ID%2FKyaEN1w349y4Xbe8CqlhfPmYuzN1pqt8jnFJt%2BS4erVUbPa6xLwm5tn7eFiaBGpAT8veB1WH6jii68iyeseT1I2SZoxeOgbotXNsoW7OWF2TGD3ucFaWBt9cSp20POw3rB5eCH5HRzz8uFj5z9LlIKmVFbqhenavC9AgeBYlIv2QinUCAcBy5SIUPJbS8Dmv7RdmGZNJvjBwW%2FZB3UooBALFDMLuQpVC71SMoqYN4zfF9SKBCACg890a2lpK3OAO9jeKTN88pkotkRqmaLPXO0%2FLopmpPoxCNL1p1%2FDXgyv0ur0sY2EGa37Q4crQqViNYIw3SsTVeuuHRI9qEVNYNUhZPJp3dXhxX15YR2x3YdAaZAKnv2ALlrV97I1tQ0N7kT%2FrO2dgrT138I5oAHhssG4lDNXoYkw0pU%2B3ks9LzZ%2ByUzbichhRehkbPX3uv26yYNN1pbH%2Fk6SmDrvyRkm37e0ds%2BQzEu7QBRR5F2stMU9rUbcm5F9ka9ICn7y0MUwvsfAxDZCYpVwxBGyUpgoi7YYmXLYc44jGTrplwowPhdzzkKp7n22J49GCw6%2B6fSD%2F2NqS4ycq1HQtIBadmw37%2BDNJbdgxv8V8vOk5zTBdZKgVVE7QHp8Z2Lrtbrw9MN2rjDbqvXRBjqZAbZuJ70tZ3HOYVx0%2FEkbI3vJU39jAgl%2FOTrLyF87FmJ4awKg0QPXDCa%2F7bevoA%2Bwr%2BsRi%2FYcXDVyogt21VAsWxsDuG0aePXSks8ZzhBtTWOCNjSSf3qRqUOrVgksCV0rgOo52N5AWskJQoy66mrU46xRNIDwOvJ6qebpIKQwXmchOMtpJ0wQKvF6liHMFBEvuEJ42hkJELU4Dw%3D%3D&Expires=1782407982)  
**Claude's action:**

bash

`mkdir -p .claude/rules # Write exact content from spec §3.3`

**Validation gate:** `cat .claude/rules/apex-meta.md` — shows all 4 rules (no silent wiki writes, no raw deletes, manifest append-only, audit-log append-only).  
**Estimated time:** 5 min | **Blocking dependency:** Step 11

---

## Step 13 — End-to-end Claude test

**What:** Confirm full loop fires correctly for a real KB question.  
**Test prompt:** `"What does the KB say about [central topic]?"`

**Verification checklist:**

- Claude does NOT open `wiki/index.md` first
    
- `apex-search` skill fires (visible in tool calls)
    
- `--check-stale` runs before `--q`
    
- `apex-search.py --kb <slug> --q "..." --limit 8` executes
    
- ≤4 wiki pages opened
    
- Answer includes `[wiki/path.md §Section]` pointer
    
- No fabricated source citations
    

**If Claude opens `index.md` first:** Strengthen CLAUDE.md block with explicit ordering: `"Step 1: check outputs/queries/. Step 2: run apex-search skill. Do NOT read index.md before running search."`  
**Estimated time:** 15 min | **Blocking dependency:** Steps 10, 11, 12

---

## Step 14 — Add `search.sqlite` to `.gitignore`

**What:** Exclude derived artifact from version control.  
**Claude's action:**

bash

`grep -q "search.sqlite" .gitignore \   || echo "apex-meta/registry/search.sqlite" >> .gitignore`

**Validation gate:** `grep search.sqlite .gitignore` — returns the line.  
**Estimated time:** 2 min | **Blocking dependency:** Step 5

---

## Step 15 — Document in `apex-meta/registry/index.md`

**What:** Write cross-KB registry index documenting the implemented system.  
**Artifact:** `apex-meta/registry/index.md`  
**Claude's action:** Write structured markdown with:

text

`# Apex Registry Index ## Active KBs | slug | wiki_pages | index_rows | last_rebuilt | status | |---|---|---|---|---| | <slug> | N | N | YYYY-MM-DD | OK | ## Retrieval Engine - Engine: SQLite FTS5/BM25 | stdlib sqlite3 - Index: apex-meta/registry/search.sqlite - Indexer: scripts/apex-index.py - Search: scripts/apex-search.py - Skill: .claude/skills/apex-search.md ## Rebuild python scripts/apex-index.py --rebuild --kb <slug>`

**Validation gate:** File exists; table row count matches active KB slugs.  
**Estimated time:** 10 min | **Blocking dependency:** Step 13

---

## Part 3 — Validation Protocol

## Test 1 — Index Integrity

bash

`PAGES=$(find apex-meta/kb/<slug>/wiki -name "*.md" ! -name "index.md" | wc -l) ROWS=$(sqlite3 apex-meta/registry/search.sqlite \   "SELECT count(*) FROM ft WHERE kb='<slug>';") [ "$PAGES" = "$ROWS" ] && echo "PASS: $ROWS rows" || echo "FAIL: pages=$PAGES rows=$ROWS" STALE=$(sqlite3 apex-meta/registry/search.sqlite \   "SELECT count(*) FROM ft WHERE status != 'current';") [ "$STALE" = "0" ] && echo "PASS: no stale rows" || echo "FAIL: stale=$STALE"`

**Pass:** Both return PASS.

---

## Test 2 — Query Determinism

bash

`for i in 1 2 3; do   python scripts/apex-search.py --kb <slug> --q "test query" \    --limit 5 --format json done | md5sum`

**Pass:** All three `md5sum` values identical. Verified basis: SQLite FTS5 BM25 is a pure deterministic mathematical ranking function — same data, same query, same result every invocation.[sqlite](https://sqlite.org/src/info/d85f4f27f58adcc7)

---

## Test 3 — Snippet Quality

bash

`python scripts/apex-search.py --kb <slug> --q "<topic>" --limit 3`

Per result: snippet contains `>>>term<<<`; word count ≤30.  
**Pass:** ≥1 match marker per snippet; all snippets ≤30 tokens.

---

## Test 4 — Skill Trigger Test

Prompt Claude: `"Using the KB, explain <concept>."`  
**Pass:**

- `apex-search` skill fires before any Read call
    
- `apex-search.py` invoked before any file open
    
- ≤4 pages opened
    
- `wiki/index.md` NOT opened
    

---

## Test 5 — Staleness Detection

bash

`echo "" >> apex-meta/kb/<slug>/wiki/summaries/any-page.md python scripts/apex-search.py --check-stale --kb <slug> # → STALE: <page>.md newer than index python scripts/apex-index.py --rebuild --kb <slug> python scripts/apex-search.py --check-stale --kb <slug> # → OK`

**Pass:** First check = STALE, second = OK.

---

## Test 6 — Failure Mode Tests

bash

`# Test A: missing index → auto-rebuild rm apex-meta/registry/search.sqlite # Give Claude a KB question # Pass: Claude runs --rebuild silently, then returns results # Test B: zero-results fallback python scripts/apex-search.py --kb <slug> \   --q "xyzzy-impossible-nonexistent-term" --limit 5 # Pass: explicit message "No FTS5 results; falling back to index scan" # Fail: empty stdout with no message; or Claude answers from general knowledge`

---

## Part 4 — Maintenance Procedures

|Trigger|Action|Command|Frequency|
|---|---|---|---|
|New wiki page added|Rebuild index|`python scripts/apex-index.py --rebuild --kb <slug>`|End of KB session|
|Wiki page edited|Rebuild index|same|End of KB session|
|New KB slug created|Init dirs + fix-frontmatter + rebuild|`mkdir -p apex-meta/kb/<slug>/{raw,manifests,wiki/{summaries,concepts,entities,synthesis},outputs/queries,audit,logs}` → `python scripts/apex-index.py --rebuild --kb <slug>`|On slug creation|
|Manifest entry added|Fix-manifest + rebuild|`python scripts/fix-manifest.py --kb <slug>` → rebuild|Per-session|
|Query reused 3+ times|Save output|Write `outputs/queries/<date>-<topic>.md`|When pattern recognized|
|Front-matter audit|Check missing fields|`grep -rL "^id:" apex-meta/kb/*/wiki/**/*.md` (repeat for kb/status/summary)|Monthly|
|UTF-8 check|Before mass update|`file --mime-encoding apex-meta/kb/*/wiki/**/*.md \\| grep -v utf-8`|Before mass front-matter runs|

---

## Part 5 — v1 Boundary: Not In Scope

|Feature|Evidence for deferral|
|---|---|
|**Vector search** (Chroma, Qdrant, FAISS, LanceDB)|Real benchmark (303 files, 6 weeks, 30 human-scored queries): FTS-only scores **85%** on exact-term queries — the primary query type for a structured technical KB. [dev](https://dev.to/tomleelive/fts-vs-hybrid-memory-search-a-real-world-benchmark-54ka) Vectors add +25pp on paraphrased/contextual queries but require embedding model + additional infrastructure. Defer until query failures actually require it.|
|**Hybrid BM25 + vector**|Hybrid earns its keep on indirect/semantic queries. For a KB with controlled vocabulary (exact slug names, source IDs, procedure names), exact-term queries dominate. [tianpan](https://tianpan.co/blog/2026-04-12-hybrid-search-production-bm25-dense-embeddings) [dev](https://dev.to/gabrielanhaia/rag-without-embeddings-when-bm25-beats-your-020-per-1k-vector-index-2140) Per benchmark [dev](https://dev.to/tomleelive/fts-vs-hybrid-memory-search-a-real-world-benchmark-54ka): FTS-only = 85% on exact, hybrid = 85% on exact — no gain for the dominant query type. Build it when you measure the gap.|
|**MCP connectors**|MCP is an adapter for external systems, not a KB engine. Adds tool-description overhead; a 2026 study found augmented MCP descriptions increased execution steps ~67%. [KB-Researchv3_gpt.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/9a030661-6791-4ceb-8779-395ffb51e3e0/KB-Researchv3_gpt.md?AWSAccessKeyId=ASIA2F3EMEYEVRY2SEPX&Signature=d9bFql4EoF01KnTkOgBsubeCILE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHoRg6Qhs55wbLi19Pp1gV%2BjaPtHJYpPdukaSDES2RkcAiEAgItbFEyTWSkYHtW57IONYUjpFvo93obxMENpQm6cbmoq8wQIUhABGgw2OTk3NTMzMDk3MDUiDPdctKk%2B01ap4t1NOSrQBCsMox1AI8gArrz%2FAY3Lx1fJGJVRGeadJaeB9vel8rpl9XdAUhHSC02nUpOI8%2F24KlU7PKSFZhhTkNANcmXQ6c0ennHTgbG%2FBaW80Dqtmddr44ptinz7NlALx8u1QKvnM1Q9q45lI1xE9Hb5GNDuJQYktovHUST1yqEDmT3LrfvXS2XC23X8Z%2BCP3xyqxYjdNiXEIVU%2BTDszChVNzUGe2jimFGwmwNNR6dfYTbvsFvapoTkRV6hXJ2Zp72VhQ%2B6dldtuax5t%2BNnpKlMSFi2BqYdTv2yf3ciVRtYtZypC%2B3w1D84P6ip%2BBnVLG3QK%2BqI4whJ11%2Fkd3dH5rkynfozijnhKfB8S%2FCna7VfRqZnA%2Fd3OyFB6qc9rXmRXGomvd6c5P51GqGUhu6E0RC59Jv0yaO0hgLXOUp8iOKIHlsJVkFfFtRNjKkNPgbc4SxAHwARhOeb3RN4eKSF2yyzEjvcavPHjui6iF%2FHF8w%2F7m71UNL%2Fbs6F%2Biy1vo5rYK%2BBdb4lkbW6Q36Zq1%2F3tKvITSWHqEm4KO%2Fz6WknsFFStmIRTl8y19FJQ6xVjfw76e5XPXrXKCe%2BS2tQ9IkdZpfODg9uGtngE7NsPMXYB%2B247HzNYYSABdaJXKz2GKUchKB%2FVG%2B0vPwF8NvBO%2Bwf%2FmJ7Rd%2FLHXElojENIsWQf0y7HIuKSuph2OAIWFamHlQb2eLiinUi6T31Z2wcbZ4%2B5yPwxjzYgcAymsuE81jUbdBuxTaTL%2FScYJHkhU1pqN03kcZkTI6U6AlUb9r7w1vovaZ88c1iriF8w57%2F10QY6mAGMxai%2FxaGIXqI34xccuvJXAjrtAnoXnqQMlcqZ1KyF6EcR0MgM%2Bc0%2Bd%2BgFphPLJEdVak7mTNJTglD4K90rnyPFrz1ISl5uVRE8z0y8JVdW1iA5aUs7Yckxr0UId9VLgG7UVzBStI5wMYs3dxVVpRtNzjxgRpnUB6On97whgolmOxq4QdzXIkm3i7VVa%2FQDXFAx9qydse%2Bd7A%3D%3D&Expires=1782410682) No external system dependency in v1.|
|**Personal orchestration memory** (`apex-meta/orchestration/`)|Separate first-class domain for weekly/daily routines, model routing, flow history. Architecturally correct to isolate [KB-Researchv3_gpt.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/9a030661-6791-4ceb-8779-395ffb51e3e0/KB-Researchv3_gpt.md?AWSAccessKeyId=ASIA2F3EMEYEVRY2SEPX&Signature=d9bFql4EoF01KnTkOgBsubeCILE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHoRg6Qhs55wbLi19Pp1gV%2BjaPtHJYpPdukaSDES2RkcAiEAgItbFEyTWSkYHtW57IONYUjpFvo93obxMENpQm6cbmoq8wQIUhABGgw2OTk3NTMzMDk3MDUiDPdctKk%2B01ap4t1NOSrQBCsMox1AI8gArrz%2FAY3Lx1fJGJVRGeadJaeB9vel8rpl9XdAUhHSC02nUpOI8%2F24KlU7PKSFZhhTkNANcmXQ6c0ennHTgbG%2FBaW80Dqtmddr44ptinz7NlALx8u1QKvnM1Q9q45lI1xE9Hb5GNDuJQYktovHUST1yqEDmT3LrfvXS2XC23X8Z%2BCP3xyqxYjdNiXEIVU%2BTDszChVNzUGe2jimFGwmwNNR6dfYTbvsFvapoTkRV6hXJ2Zp72VhQ%2B6dldtuax5t%2BNnpKlMSFi2BqYdTv2yf3ciVRtYtZypC%2B3w1D84P6ip%2BBnVLG3QK%2BqI4whJ11%2Fkd3dH5rkynfozijnhKfB8S%2FCna7VfRqZnA%2Fd3OyFB6qc9rXmRXGomvd6c5P51GqGUhu6E0RC59Jv0yaO0hgLXOUp8iOKIHlsJVkFfFtRNjKkNPgbc4SxAHwARhOeb3RN4eKSF2yyzEjvcavPHjui6iF%2FHF8w%2F7m71UNL%2Fbs6F%2Biy1vo5rYK%2BBdb4lkbW6Q36Zq1%2F3tKvITSWHqEm4KO%2Fz6WknsFFStmIRTl8y19FJQ6xVjfw76e5XPXrXKCe%2BS2tQ9IkdZpfODg9uGtngE7NsPMXYB%2B247HzNYYSABdaJXKz2GKUchKB%2FVG%2B0vPwF8NvBO%2Bwf%2FmJ7Rd%2FLHXElojENIsWQf0y7HIuKSuph2OAIWFamHlQb2eLiinUi6T31Z2wcbZ4%2B5yPwxjzYgcAymsuE81jUbdBuxTaTL%2FScYJHkhU1pqN03kcZkTI6U6AlUb9r7w1vovaZ88c1iriF8w57%2F10QY6mAGMxai%2FxaGIXqI34xccuvJXAjrtAnoXnqQMlcqZ1KyF6EcR0MgM%2Bc0%2Bd%2BgFphPLJEdVak7mTNJTglD4K90rnyPFrz1ISl5uVRE8z0y8JVdW1iA5aUs7Yckxr0UId9VLgG7UVzBStI5wMYs3dxVVpRtNzjxgRpnUB6On97whgolmOxq4QdzXIkm3i7VVa%2FQDXFAx9qydse%2Bd7A%3D%3D&Expires=1782410682) but not a prerequisite for SQLite retrieval to function. Implement after v1 retrieval is validated.|
|**Automatic manifest ingestion pipeline**|Requires hashing, change detection, auto-compilation triggers — a full ingestion automation layer. Manual ingestion in v1 keeps state mutations operator-gated. Automate after base pipeline is stable.|

---

## APPENDIX — Verifier Prompt for Claude Sonnet Extended Thinking

Copy this verbatim into a new Claude.ai window with Extended Thinking enabled:

---

text

`You are a TECHNICAL VERIFIER, not an implementer. Your only job is to verify  whether a given implementation plan is correct, complete, and safe to execute. You will be given: an implementation plan for Apex KB + SQLite FTS5/BM25  integration with Claude Code. Your role: 1. VERIFY every technical claim against:    - The official SQLite FTS5 documentation (https://sqlite.org/fts5.html)   - Real published implementations (GitHub repos, production blog posts, benchmarks)   - Claude Code official documentation (skills, CLAUDE.md, path-scoped rules)   - Python stdlib sqlite3 module documentation   Do NOT accept AI-generated claims as evidence. Cite actual sources. 2. For each plan component, score on these metrics (0–100):    IMPACT     — How much does this step improve retrieval quality or token efficiency?                0 = no measurable impact, 100 = eliminates the core problem       EVIDENCE   — How well is this approach validated by external, non-AI sources?                0 = AI speculation only, 100 = production deployments + benchmarks       RISK       — What is the failure risk of this step as specified?                0 = catastrophic/irreversible, 100 = fully safe/reversible       EFFORT     — Is the effort estimate realistic?                0 = wildly underestimated, 100 = accurate or conservative 3. For each step scored below 60 on any metric, explain:    - What specifically is wrong or unverified   - What the correct approach is, with a real source   - Whether the step should be modified, replaced, or removed 4. Flag any of these critical failure patterns:    - Steps that run indexer before front-matter is patched   - BM25 weight vector that doesn't match column order in CREATE VIRTUAL TABLE   - Script that opens wiki pages at index time instead of reading front-matter only   - CLAUDE.md block that is too long (>500 tokens loaded at every session start)   - Missing UTF-8 verification before first index build   - Any step that silently overwrites existing wiki page content 5. Output format:    For each step: [Step N] | IMPACT: X | EVIDENCE: X | RISK: X | EFFORT: X | VERDICT: PASS/FLAG   Flags: explain in 2–3 sentences with a real source citation.   End with: overall plan verdict (EXECUTE / EXECUTE WITH CHANGES / DO NOT EXECUTE)   and a 3-sentence summary of the highest-priority changes required. The plan to verify is attached as: ApexKBSQLiteFTS5BM25 implementation plan`

---

**Total verified implementation estimate: 3–4 hours, single session, zero dependencies beyond Python stdlib `sqlite3`.** Evidence basis: SQLite Cloud documented sub-6ms query times on a markdown documentation corpus using FTS5; production hybrid RAG in 200 lines using FTS5 + sqlite-vec confirmed working May 2026; BM25 dominance on exact-identifier queries confirmed across BEIR benchmark and 2026 production measurements; FTS-only 85% accuracy on exact-term agent memory queries confirmed by real benchmark with human scoring.