# Scope: Milestone 5 — Candidate 16-ultra Compilation, Indices, & Full Verification

## Architecture & Inputs
- Source files: `apex-meta/informatics/final/research/06-layered-rule-kb/rule-01-target.md` through `rule-22-pointers.md`
- Audit files: `apex-meta/informatics/final/research/06-layered-rule-kb/audit-module-01-writing-profile.md` through `audit-module-05-governance-schemas.md`
- Reference Baseline: `apex-meta/informatics/final/candidates/13-candidate-3A-xml.md`

## Deliverables
1. `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`:
   - Assembled from 22 Option B blocks from Layered Rule KB
   - Root tag `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">`
   - Exact 22 semantic tags
   - Metrics: lines, words, chars, repo tokens, cl100k_base BPE tokens (~900–980 BPE, target ~950 BPE)
   - Rule-by-rule delta table against 13-candidate-3A-xml.md
2. `apex-meta/informatics/final/research/06-layered-rule-kb/index.md`:
   - Comprehensive navigation linking all 22 rules, 5 module audits, and the synthesis/rollup
3. `apex-meta/informatics/final/index.md`:
   - Updated with references to Layered Rule KB and 16-candidate-3A-ultra.md

## Verification Gates
1. OKF Conformance: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (0 errors)
2. Pytest Suite: `python -m pytest apex-meta/informatics/tests/ -q` (100% pass)
3. Immutability Check: zero modifications to root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`
4. Research Preservation: zero byte modifications to `01-universal-instruction-research/` and `03-research-of-file-10/`
