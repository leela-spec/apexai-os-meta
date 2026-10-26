# Adversarial Challenge Report: Router Ceilings & Parsing Stress Testing (Milestone M2)

**Author**: `challenger_m2_1` (Empirical Challenger: Critic & Specialist)  
**Target Milestone**: M2 — Governance, Anti-Drift & Consolidated Router  
**Authored Scope**:
- `apex-meta/informatics/anti-drift-rules.md`
- `apex-meta/informatics/governance-schemas.md`
- `apex-meta/informatics/index.md`
- `apex-meta/informatics/general-informatics-router.md`
**Test Harness**: `apex-meta/informatics/tests/stress_test_m2_challenger.py`  
**Execution Timestamp**: 2026-10-19T17:17:00Z  
**Verdict**: **APPROVE** (All hard constraints and regression gates verified; low-risk headroom sensitivities documented)

---

## Challenge Summary

**Overall risk assessment**: **LOW**  
All four M2 deliverables strictly fulfill architectural contracts, token/line/character ceilings, XML tag schema requirements, frontmatter parsing constraints, and zero-formula significance ranking. Automated validators and test runners pass with 100% compliance. Two boundary sensitivities were surfaced through stress-testing and documented below.

---

## Empirical Verification Matrix

| Metric / Dimension | Requirement / Boundary | Measured Value | Empirical Result | Status |
|---|---|---|---|:---:|
| **Router Line Count** | Target ~100 lines (Ceiling <= 120) | 46 lines | Verified via `len(content.splitlines())` | **PASS** |
| **Router Char Count** | Ceiling <= 2,000 characters | 1,994 characters | Verified via `len(content)` (headroom: 6 chars) | **PASS** |
| **Router Token Count** | Target ~400 (Ceiling <= 500) | 498 tokens (`chars//4`), ~301 tokens (word-based) | Verified via `estimate_tokens` heuristic | **PASS** |
| **XML Tag Pairing** | Balanced `<informatics ...>` / `</informatics>` | 5 pairs in router, 5 pairs in `index.md` | `xml.etree.ElementTree` validation | **PASS** |
| **XML Attributes** | `when` (mandatory), `ref` (valid path), `deepen_when` | 100% valid attributes, all target files exist | Resolves to existing markdown files | **PASS** |
| **XML Body Purity** | Clean Markdown, zero `@path` eager imports | 0 eager imports detected | Regex scan across all tag bodies | **PASS** |
| **YAML Frontmatter** | Flat key-values/inline lists, no multiline `- ` | 0 missing colons, 0 multiline lists | Parsed cleanly by `okf_validator.py` | **PASS** |
| **Zero Math Formulas** | No computed EV/Score, no arithmetic combinations | 0 formulas found | Negative regex pattern scan | **PASS** |
| **Significance Tags** | `[P<0-3> \| I/E/R]`, 1–100 integer bounds | 76 tags across M2 files, 0 inversions | Strictly descending priority sort (P0->P3) | **PASS** |
| **Top-Loaded Primacy** | First P0 invariant within first 500 tokens | Router: 50, Index: 102, Gov: 205, Anti-Drift: 217 | All <= 500 tokens | **PASS** |
| **OKF Validator** | `okf_validator.py --target apex-meta/informatics` | 0 OKF Errors, 0 Apex Errors, 0 Advisories | Verified via CLI execution | **PASS** |
| **E2E Test Suite** | `test_informatics_e2e.py` | 146 passed, 0 skipped, 0 failed, 0 errors | 100% Spec Conformance | **PASS** |

---

## Challenges & Sensitivity Findings

### [Low] Challenge 1: Router Character & Token Ceiling Headroom Margin

- **Assumption Challenged**: The consolidated general router (`general-informatics-router.md`) operates safely below the 2,000 character and 500 token ceilings.
- **Attack Scenario**: Author adds minor descriptive text or formatting; or git line-ending conversion modifies LF (`\n`) to CRLF (`\r\n`).
- **Empirical Measurement**:
  - Measured character length: **1,994 characters** (headroom: 6 characters, or 0.3% margin).
  - Measured token estimate (`chars // 4`): **498 tokens** (headroom: 2 tokens, or 0.4% margin).
  - If converted to CRLF on Windows, raw file size expands from 1,994 bytes to **2,040 bytes** (+46 bytes from `\r`).
  - Worker's handoff originally cited ~1,514 characters and ~378 tokens (an earlier draft estimate), which concealed how close the final artifact is to the 2,000 character limit.
- **Blast Radius**: If any downstream contributor adds even a 7-character string without trimming, mechanical tools with strict `< 2000` ceilings will trigger.
- **Mitigation / Defense**:
  1. The file currently satisfies all ceiling constraints strictly (1,994 <= 2,000; 498 <= 500; 46 <= 100).
  2. Requirement R2 explicitly provides **Substance Over Ceremony Exception Authority**: *"An agent or author is explicitly permitted to exceed an approximate ceiling or relax a stylistic constraint whenever strict adherence would harm technical accuracy, omit load-bearing context, create artificial distortions, or produce unnatural prose. Substantive realization of the target always overrides mechanical metric compliance."*
  3. Ensure repository `.gitattributes` maintains `eol=lf` for markdown to prevent CRLF byte inflation.

### [Low] Challenge 2: Asymmetric Attribute Ordering in Router Tag Regex

- **Assumption Challenged**: Downstream agent parsers and validator regexes reliably extract `<informatics>` dispatch tags regardless of attribute ordering.
- **Attack Scenario**: An author or automated tool emits `<informatics ref="writing-profile.md" when="writing_or_documentation">` (inverting `when` and `ref`).
- **Empirical Measurement**:
  - `ROUTER_XML_TAG_REGEX = re.compile(r'<informatics\s+when="([^"]+)"\s+ref="([^"]+)"(?:\s+deepen_when="([^"]+)")?\s*/?>')`.
  - Passing `<informatics ref="..." when="...">` returns `len(parsed) == 0`.
  - While standard XML parsers (`xml.etree.ElementTree`) parse arbitrary attribute order correctly, regex-based line parsers fail on inverted attributes.
- **Blast Radius**: Any future tool generating tags with non-canonical attribute ordering will fail regex detection in `test_informatics_e2e.py`.
- **Current Mitigation**: All authored files (`general-informatics-router.md` and `index.md`) strictly follow canonical attribute order (`when="..." ref="..." deepen_when="..."`). The canonical ordering is documented in `governance-schemas.md` and enforced by tests.

### [Low] Challenge 3: Numbered Heading Period Splitting in STE Advisory Linter

- **Assumption Challenged**: Markdown numbered headings (e.g., `## 1. Title`) do not interfere with prose sentence splitting.
- **Attack Scenario**: Worker encountered `STE-SENTENCE-LENGTH` advisory on `## 5. Traceability & Reference Grounding` in `governance-schemas.md` because `re.split(r"(?<=[.!?])\s+", text_no_tables)` split after `5.`, leaving the remainder of the line without `#`, where it was concatenated with subsequent unpunctuated bullets.
- **Empirical Measurement**:
  - Adversarial scan identified 27 headings across M2 files formatted as `## N. Title`.
  - All 27 headings currently pass with 0 advisories because their following paragraphs have periods within 30 words, preventing accumulator overflow.
- **Blast Radius**: Adding unpunctuated bullet lists directly under a numbered heading containing a period can re-trigger false-positive STE sentence length advisories.
- **Mitigation**: Using colon syntax (e.g. `## 5: Title`) or ensuring initial sentences under headings have terminating periods prevents false-positive splitting.

---

## Stress Test Results

| Test Scenario | Expected Behavior | Actual Behavior | Result |
|---|---|---|:---:|
| Character Ceiling Boundary (`chars <= 2000`) | Measured chars <= 2000 | 1,994 characters | **PASS** |
| Line Ceiling Boundary (`lines <= 100`) | Measured lines <= 100 | 46 lines | **PASS** |
| Token Ceiling Boundary (`tokens <= 500`) | Estimated tokens <= 500 | 498 tokens (chars/4), 301 tokens (words*1.33) | **PASS** |
| Primacy Token Placement (`first P0 <= 500`) | First P0 rule at token <= 500 | Router: 50, Index: 102, Gov: 205, Anti-Drift: 217 | **PASS** |
| XML Tag Well-Formedness | 100% parseable by `ET.fromstring` | 10/10 tags parsed without XMLSyntaxError | **PASS** |
| Eager Import Detection | 0 matches for `@path/\w+\.md` | 0 eager imports found | **PASS** |
| Frontmatter Line Colon Check | 100% non-comment lines have `:` | All lines contain `:`, no multiline lists | **PASS** |
| Arithmetic Formula Detection | 0 computed scores or equations | 0 formulas found; raw 3-metric tags verified | **PASS** |
| Priority Tier Monotonicity | Sort order P0 -> P1 -> P2 -> P3 | 76 tags sorted strictly descending, 0 inversions | **PASS** |
| Link Target Verification | 100% relative links resolve on disk | 13/13 relative links resolve to existing files | **PASS** |
| Upstream OKF Validator | 0 OKF Errors, 0 Apex Errors, 0 Advisories | 0 Errors, 0 Warnings across entire bundle | **PASS** |
| E2E Test Suite Run | 146 passed, 0 failures, 0 skipped | 146/146 tests passed (0.169s) | **PASS** |

---

## Unchallenged Areas

- **Downstream Agent Execution Dynamics**: The live integration of `general-informatics-router.md` into external agent system prompts (e.g. `AGENTS.md`) will be tested during Milestone M3 integration and runtime evaluation.

---

## Final Verdict

**APPROVE** — Milestone M2 deliverables are robust, strictly compliant with specifications, and empirically verified with zero failures across all automated stress harnesses.
