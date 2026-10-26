# Handoff Report — Milestone 1 (Rules 02–08) Adversarial Challenge & Verification

**Agent**: Challenger 2 (`challenger_m1_2`)
**Role**: Critic, Specialist (Empirical Challenger)
**Recipient / Parent**: Orchestrator (`a1918f04-9801-41c9-a8a4-6cebbbfab6ed`)
**Target Deliverables**: `apex-meta/informatics/final/research/06-layered-rule-kb/` (`rule-02-product-first.md` through `rule-08-context.md`)
**Verdict**: **`REQUEST_CHANGES`** (pending surgical repair of 30 broken relative links)

---

## 1. Observation

### Obs 1: Relative Markdown Link Resolution (30 Broken Links)
Direct execution of link resolution auditing across `rule-02-product-first.md` through `rule-08-context.md` identified **30 broken relative links** pointing to non-existent disk targets:
- **`rule-02-product-first.md`**:
  - `[A01-substance-over-ceremony.md](../../research/01-universal-instruction-research/module-deepening/A01-substance-over-ceremony.md)` (Line 12) $\rightarrow$ Non-existent
  - `[A07-hierarchical-realization.md](../../research/01-universal-instruction-research/module-deepening/A07-hierarchical-realization.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent
- **`rule-03-scope.md`**:
  - `[A02-scope-and-non-goals.md](../../research/01-universal-instruction-research/module-deepening/A02-scope-and-non-goals.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent
- **`rule-04-communication.md`**:
  - `[A12-communication-economy.md](../../research/01-universal-instruction-research/module-deepening/A12-communication-economy.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent
- **`rule-05-hold-position.md`**:
  - `[A05-intent-alignment.md](../../research/01-universal-instruction-research/module-deepening/A05-intent-alignment.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent
- **`rule-06-ground.md`**:
  - `[A08-evidence-integrity.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity.md)` (Line 12) $\rightarrow$ Non-existent
  - `[A13-external-grounding.md](../../research/01-universal-instruction-research/module-deepening/A13-external-grounding.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent
- **`rule-07-reuse.md`**:
  - `[A03-reuse-before-invention.md](../../research/01-universal-instruction-research/module-deepening/A03-reuse-before-invention.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent
- **`rule-08-context.md`**:
  - `[A06-context-engineering.md](../../research/01-universal-instruction-research/module-deepening/A06-context-engineering.md)` (Line 12) $\rightarrow$ Non-existent
  - `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)` (Line 14) $\rightarrow$ Non-existent
  - `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)` (Line 14) $\rightarrow$ Non-existent
  - `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)` (Line 14) $\rightarrow$ Non-existent

### Obs 2: Zero Live Mutation Boundary
- `git diff AGENTS.md CLAUDE.md GEMINI.md`:
  - `GEMINI.md`: 0 diff lines (unmodified).
  - `AGENTS.md` and `CLAUDE.md`: diffs contain only `ki-basis/docs/INFRASTRUCTURE.md` pointer added on `2026-10-08T15:10:55Z` (pre-existing, prior to M1).
  - Live carrier files were untouched during Milestone 1 authoring (`2026-10-22`).

### Obs 3: Research Preservation Boundary
- `apex-meta/informatics/final/research/01-universal-instruction-research`: 70 files, latest mtime `2026-09-29T15:29:09Z`. Zero mutations.
- `apex-meta/informatics/final/research/03-research-of-file-10`: 14 files, latest mtime `2026-10-21T14:36:44Z`. Zero mutations.

### Obs 4: Pytest Suite Execution
- Command: `python -m pytest apex-meta/informatics/tests/ -q`
- Output: `196 passed, 98 subtests passed in 0.52s`. Exit code 0.

### Obs 5: Byte-Level Fidelity and BPE Precision
- Section 1.1 quotes `<apex_contract v="1.0">` candidate tags from `13-candidate-3A-xml.md` with 100% byte-for-byte exactness across all 7 rules.
- Live `tiktoken` (`cl100k_base`) calculation confirmed 100% accuracy for all claimed BPE counts in Section 1.1, Section 1.2 semantic blocks, and Section 3 rollup tables across all 7 rules:
  - `rule-02`: Baseline 62 BPE, Option B 46 BPE (−25.8%), Option C 32 BPE (−48.4%).
  - `rule-03`: Baseline 43 BPE, Option B 38 BPE (−11.6%), Option C 30 BPE (−30.2%).
  - `rule-04`: Baseline 73 BPE, Option B 64 BPE (−12.3%), Option C 53 BPE (−27.4%).
  - `rule-05`: Baseline 55 BPE, Option B 47 BPE (−14.5%), Option C 38 BPE (−30.9%).
  - `rule-06`: Baseline 81 BPE, Option B 70 BPE (−13.6%), Option C 50 BPE (−38.3%).
  - `rule-07`: Baseline 56 BPE, Option B 40 BPE (−28.6%), Option C 36 BPE (−35.7%).
  - `rule-08`: Baseline 42 BPE, Option B 42 BPE (0.0%), Option C 36 BPE (−14.3%).

---

## 2. Logic Chain

1. **Premise 1 (R1 & Dispatch Mandate)**: The task mandate explicitly requires: *"Inspect relative markdown links in rule-02 through rule-08 to verify link resolution"* and R1 §4 requires *"Complete Bidirectional Research & Provenance Links"*.
2. **Premise 2 (Obs 1)**: Auditing every relative markdown link in `rule-02` through `rule-08` proved empirically that 30 links fail to resolve to any file on disk.
3. **Premise 3 (Traceability Risk)**: When an agent or human operator loads these files, navigation to upstream contract lineage and research corpora breaks, violating self-contained bidirectional provenance.
4. **Premise 4 (Readiness of Solution)**: All 12 missing target paths were located on disk, verified, and mapped into an exact 1:1 replacement table.
5. **Conclusion**: While all structural, metric, invariant, and ecosystem boundaries pass with distinction (Obs 2–5), the 30 broken links represent an unambiguous defect that must be corrected before final approval.

---

## 3. Caveats

- **Prototype `rule-01-target.md`**: `rule-01-target.md` was not authored in Milestone 1 (it is the pre-existing prototype from 2026-10-21). It also contains broken links from pre-consolidation paths, but was not in the M1 authoring scope. It should be swept for link normalization during the index/rollup milestone.
- **Root `index.md` in `06-layered-rule-kb/`**: `okf_validator.py` reports `OKF-ROOT-INDEX-EXISTS` error on the `06-layered-rule-kb` directory because `index.md` has not been authored yet. Per the project prompt, `index.md` is a Milestone 4 deliverable and was not expected in Milestone 1.

---

## 4. Conclusion & Actionable Verdict

**Structured Verdict**: **`REQUEST_CHANGES`**

Worker M1 is requested to apply the following surgical link corrections across `rule-02` through `rule-08`:

### Exact Replacement Mapping

1. **Lineage Links (Lines 14 of rules 02–08)**:
   - Replace: `../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md`
   - With: `../../candidates/02-informatics-contract-block.md`
   - Replace: `../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md`
   - With: `../../candidates/07-contract-block-v0.4.md`
   - Replace: `../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md`
   - With: `../../candidates/09-contract-block-v0.5.md`

2. **Module Deepening Links (Line 12 of rules 02–08)**:
   - In `rule-02`: Replace `A01-substance-over-ceremony.md` with `A01-target-outcome-alignment/README.md`
   - In `rule-02`: Replace `A07-hierarchical-realization.md` with `A07-hierarchical-realization-verification-validation/README.md`
   - In `rule-03`: Replace `A02-scope-and-non-goals.md` with `A02-scope-non-goals/README.md`
   - In `rule-04`: Replace `A12-communication-economy.md` with `A12-communication-economy-actionable-visibility/README.md`
   - In `rule-05`: Replace `A05-intent-alignment.md` with `A05-intent-alignment-clarification-threshold/README.md`
   - In `rule-06`: Replace `A08-evidence-integrity.md` with `A08-evidence-integrity-uncertainty-calibration/README.md`
   - In `rule-06`: Replace `A13-external-grounding.md` with `A13-external-grounding-real-world-verification/README.md`
   - In `rule-07`: Replace `A03-reuse-before-invention.md` with `A03-reuse-before-invention/README.md`
   - In `rule-08`: Replace `A06-context-engineering.md` with `A06-context-engineering-progressive-disclosure/README.md`

Once Worker M1 applies these surgical replacements, the milestone will achieve 100% link resolution and can be immediately APPROVED.

---

## 5. Verification Method

To independently reproduce the broken link findings and verify resolution after the worker patches them, run the following PowerShell command:

```powershell
@'
import os, re, urllib.parse

rule_dir = "apex-meta/informatics/final/research/06-layered-rule-kb"
rules = [f"rule-{i:02d}-{n}.md" for i, n in [
    (2, "product-first"), (3, "scope"), (4, "communication"),
    (5, "hold-position"), (6, "ground"), (7, "reuse"), (8, "context")
]]

pat = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
broken = []

for r in rules:
    content = open(os.path.join(rule_dir, r), encoding="utf-8").read()
    for text, url in pat.findall(content):
        u = url.strip()
        if u.startswith(("http:", "https:", "mailto:", "#")):
            continue
        p = urllib.parse.unquote(u.split("#")[0])
        if not p:
            continue
        res = os.path.normpath(os.path.join(rule_dir, p))
        if not os.path.exists(res):
            broken.append((r, text, url))

print(f"Broken relative links count: {len(broken)}")
for r, t, u in broken:
    print(f"[{r}] [{t}]({u})")
'@ | python
```

**Invalidation Condition**: If `Broken relative links count` returns `0`, the issue is fully resolved.
