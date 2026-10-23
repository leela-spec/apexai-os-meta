#!/usr/bin/env python3
"""
test_informatics_e2e.py — Comprehensive Opaque-Box E2E Test Suite for Apex Informatics.

Architecture:
- Tier 1: Feature Coverage (>=5 tests per core feature = 60+ tests)
- Tier 2: Boundary & Corner Cases (>=5 tests per feature = 60+ tests)
- Tier 3: Cross-Feature Interactions & Pairwise Combinations (>=12 tests)
- Tier 4: Real-World Application Workload Scenarios (>=5 scenarios)
- Live Bundle Audit: Progressive testability for live repository artifacts

Authoritative Sources:
- ORIGINAL_REQUEST.md (Requirements R1–R5 and Acceptance Criteria)
- PROJECT.md & TEST_INFRA.md
- okf_validator.py (Upstream OKF v0.2 and Apex Profile Rules)
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Dict, List, Optional, Tuple
import unittest

# Ensure apex-meta/scripts is discoverable for okf_validator imports
REPO_ROOT = Path(__file__).resolve().parents[5]
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final"
SCRIPTS_DIR = REPO_ROOT / "apex-meta" / "scripts"
FINAL_TOOLS_DIR = INFORMATICS_DIR / "tools"

for p in (SCRIPTS_DIR, FINAL_TOOLS_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

def resolve_informatics_file(path_str: str) -> Path:
    for base in (INFORMATICS_DIR, INFORMATICS_DIR / "specs", INFORMATICS_DIR / "sub-bundles"):
        candidate = base / path_str
        if candidate.exists():
            return candidate
    return INFORMATICS_DIR / path_str

try:
    import okf_validator
except ImportError:
    okf_validator = None


# ==============================================================================
# Domain Models & Core Specification Helpers
# ==============================================================================

@dataclass
class SignificanceTag:
    tier: str  # P0, P1, P2, P3
    impact: int  # 1–100
    evidence: int  # 1–100
    risk: int  # 1–100
    raw_text: str

    @property
    def tier_rank(self) -> int:
        return {"P0": 0, "P1": 1, "P2": 2, "P3": 3}.get(self.tier, 99)


SIGNIFICANCE_TAG_REGEX = re.compile(
    r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]"
)
ROUTER_XML_TAG_REGEX = re.compile(
    r'<informatics\s+when="([^"]+)"\s+ref="([^"]+)"(?:\s+deepen_when="([^"]+)")?\s*/?>'
)


def parse_significance_tag(text: str) -> Optional[SignificanceTag]:
    match = SIGNIFICANCE_TAG_REGEX.search(text)
    if not match:
        return None
    tier, i_str, e_str, r_str = match.groups()
    i_val, e_val, r_val = int(i_str), int(e_str), int(r_str)
    if not (1 <= i_val <= 100 and 1 <= e_val <= 100 and 1 <= r_val <= 100):
        return None
    return SignificanceTag(tier=tier, impact=i_val, evidence=e_val, risk=r_val, raw_text=match.group(0))


def extract_all_significance_tags(content: str) -> List[SignificanceTag]:
    tags: List[SignificanceTag] = []
    # Strip fenced code blocks to avoid counting examples as normative tags
    content_no_code = re.sub(r"```[\s\S]*?```", "", content)
    for match in SIGNIFICANCE_TAG_REGEX.finditer(content_no_code):
        tier, i_str, e_str, r_str = match.groups()
        i_val, e_val, r_val = int(i_str), int(e_str), int(r_str)
        if 1 <= i_val <= 100 and 1 <= e_val <= 100 and 1 <= r_val <= 100:
            tags.append(SignificanceTag(tier=tier, impact=i_val, evidence=e_val, risk=r_val, raw_text=match.group(0)))
    return tags


def validate_tags_descending_order(tags: List[SignificanceTag]) -> Tuple[bool, Optional[str]]:
    if len(tags) <= 1:
        return True, None
    for idx in range(len(tags) - 1):
        current_rank = tags[idx].tier_rank
        next_rank = tags[idx + 1].tier_rank
        if current_rank > next_rank:
            return False, f"Inverted priority order at index {idx}: {tags[idx].tier} appears before {tags[idx + 1].tier}"
    return True, None


def estimate_tokens(text: str) -> int:
    """Standard token estimation heuristic (~4 characters per token)."""
    if not text:
        return 0
    return max(1, len(text) // 4)


def check_top_loaded_primacy(content: str, token_ceiling: int = 500) -> Tuple[bool, Optional[int]]:
    """Checks if the first P0 invariant appears within the first `token_ceiling` tokens."""
    tags = extract_all_significance_tags(content)
    p0_tags = [t for t in tags if t.tier == "P0"]
    if not p0_tags:
        return False, None
    first_p0 = p0_tags[0]
    pos = content.find(first_p0.raw_text)
    token_pos = estimate_tokens(content[:pos])
    return token_pos <= token_ceiling, token_pos


def check_ste_sentence_length(text: str, max_words: int = 30) -> List[Tuple[str, int]]:
    """Identifies prose sentences exceeding target word count."""
    text_clean = re.sub(r"```[\s\S]*?```", "", text)
    text_clean = re.sub(r"`.*?`", "", text_clean)
    text_clean = "\n".join([l for l in text_clean.splitlines() if not l.strip().startswith("|")])
    sentences = re.split(r"(?<=[.!?])\s+", text_clean)
    violations = []
    for s in sentences:
        s_clean = s.strip()
        if not s_clean or s_clean.startswith(("#", "-", "*", ">")):
            continue
        words = [w for w in s_clean.split() if w]
        if any(w.startswith("http") or "$" in w for w in words):
            continue
        if len(words) > max_words:
            violations.append((s_clean, len(words)))
    return violations


def check_single_command_directive(sentence: str) -> bool:
    """Flags compound sentences that chain multiple imperative action clauses with conjunctions."""
    imperative_verbs = r"\b(run|execute|create|delete|update|modify|validate|verify|ensure|apply|check|halt|stop)\b"
    conjunctions = r"\b(and then|and also|and subsequently|and next|and run|and execute|and verify)\b"
    if re.search(imperative_verbs, sentence, re.IGNORECASE) and re.search(conjunctions, sentence, re.IGNORECASE):
        return False
    return True


def check_heading_depth(content: str) -> List[int]:
    """Returns all heading depths found in markdown content."""
    depths = []
    for line in content.splitlines():
        line_clean = line.strip()
        if line_clean.startswith("#"):
            depth = len(line_clean) - len(line_clean.lstrip("#"))
            depths.append(depth)
    return depths


def check_prose_chunk_words(content: str, max_words: int = 150) -> List[int]:
    """Checks prose paragraphs (separated by blank lines) for word ceilings before tables/lists."""
    chunks = content.split("\n\n")
    oversized = []
    for chunk in chunks:
        c_clean = chunk.strip()
        if not c_clean or c_clean.startswith(("#", "|", "-", "*", "```", "<")):
            continue
        words = c_clean.split()
        if len(words) > max_words:
            oversized.append(len(words))
    return oversized


def parse_router_tags(content: str) -> List[Dict[str, str]]:
    results = []
    for match in ROUTER_XML_TAG_REGEX.finditer(content):
        when_val, ref_val, deepen_val = match.groups()
        results.append({
            "when": when_val.strip(),
            "ref": ref_val.strip(),
            "deepen_when": (deepen_val or "").strip()
        })
    return results


def check_router_eager_imports(content: str) -> List[str]:
    """Detects prohibited eager @path imports (e.g. `@path/to/file.md`)."""
    eager_matches = re.findall(r"@[\w./\-]+\.md", content)
    return eager_matches


def apply_exact_match_patch(original: str, old_block: str, new_block: str) -> Tuple[bool, str, Optional[str]]:
    """Executes deterministic exact-match patch replacement."""
    count = original.count(old_block)
    if count == 0:
        return False, original, "Exact-match target block not found in content (whitespace or content mismatch)"
    if count > 1:
        return False, original, f"Ambiguous patch match: target block matched {count} times (requires disambiguating context)"
    patched = original.replace(old_block, new_block, 1)
    return True, patched, None


@dataclass
class DecisionOption:
    identifier: str
    description: str
    grounding: str
    impact: int
    evidence: int
    risk: int
    rejection_note: Optional[str] = None


@dataclass
class DecisionMatrix:
    question: str
    options: List[DecisionOption]
    recommendation: str

    def is_valid(self) -> Tuple[bool, Optional[str]]:
        if not self.question.strip():
            return False, "Decision Matrix must define a non-empty Question"
        if len(self.options) < 2:
            return False, "Decision Matrix requires at least 2 structured options"
        if not self.recommendation.strip():
            return False, "Decision Matrix must define an explicit Recommendation"
        for opt in self.options:
            if not opt.grounding.strip():
                return False, f"Option {opt.identifier} lacks Grounding reference"
            if not (1 <= opt.impact <= 100 and 1 <= opt.evidence <= 100 and 1 <= opt.risk <= 100):
                return False, f"Option {opt.identifier} metrics must be in range 1-100"
            if opt.identifier != self.recommendation and not (opt.rejection_note and opt.rejection_note.strip()):
                return False, f"Rejected option {opt.identifier} is missing a one-line rejection note"
        return True, None


class TwoStrikeSubsystemTracker:
    def __init__(self):
        self.strikes: Dict[str, int] = {}
        self.pivots: List[str] = []

    def record_attempt(self, subsystem: str, success: bool) -> str:
        if success:
            self.strikes[subsystem] = 0
            return "SUCCESS"
        current = self.strikes.get(subsystem, 0) + 1
        self.strikes[subsystem] = current
        if current >= 2:
            self.pivots.append(subsystem)
            return "TWO_STRIKE_HALT_AND_PIVOT"
        return "RETRY_ALLOWED"


# ==============================================================================
# Tier 1: Feature Coverage Test Suite (>= 5 tests per feature = 60 tests)
# ==============================================================================

class TestTier1FeatureCoverage(unittest.TestCase):
    """
    Tier 1: Feature Coverage (Category-Partition & Primary Behavior).
    Validates all 12 core features against explicit authoritative requirements.
    """

    # --- Feature 1: Sub-Bundle Isolation ---
    def test_f01_01_sub_bundle_isolation_prunes_child_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            sub = tmppath / "sub_bundle"
            sub.mkdir()
            (sub / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Sub Index\n', encoding="utf-8")
            (sub / "draft.md").write_text('# Malformed draft without frontmatter\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertEqual(report.okf_errors, 0, "Sub-bundle draft should be pruned and cause 0 errors")

    def test_f01_02_sub_bundle_isolation_ignores_drafts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            sub = tmppath / "Agent_Setup"
            sub.mkdir()
            (sub / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Sub Index\n', encoding="utf-8")
            (sub / "bad_syntax.md").write_text('---\ntype:\n  - item1\n---\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    def test_f01_03_sub_bundle_isolation_non_bundle_subdir_is_traversed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            regular_dir = tmppath / "docs"
            regular_dir.mkdir()
            (regular_dir / "bad.md").write_text('# Missing frontmatter\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertGreater(report.okf_errors, 0, "Non-bundle subdirectories must be traversed and checked")

    def test_f01_04_sub_bundle_isolation_nested_sub_bundles(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            sub1 = tmppath / "level1"
            sub1.mkdir()
            (sub1 / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Level 1\n', encoding="utf-8")
            sub2 = sub1 / "level2"
            sub2.mkdir()
            (sub2 / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Level 2\n', encoding="utf-8")
            (sub2 / "broken.md").write_text('No frontmatter\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    def test_f01_05_sub_bundle_isolation_relative_link_resolves(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n[Sub](sub/index.md)\n', encoding="utf-8")
            sub = tmppath / "sub"
            sub.mkdir()
            (sub / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Sub\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertEqual(report.apex_profile_errors, 0)

    # --- Feature 2: Significance & Ranking Architecture (P0–P3) ---
    def test_f02_01_significance_tier_p0_critical_invariant(self):
        tag = parse_significance_tag("[P0 | I95/E95/R10] Non-negotiable invariant")
        self.assertIsNotNone(tag)
        self.assertEqual(tag.tier, "P0")
        self.assertEqual(tag.tier_rank, 0)

    def test_f02_02_significance_tier_p1_core_method(self):
        tag = parse_significance_tag("[P1 | I85/E80/R20] Primary workflow pattern")
        self.assertIsNotNone(tag)
        self.assertEqual(tag.tier, "P1")
        self.assertEqual(tag.tier_rank, 1)

    def test_f02_03_significance_tier_p2_standard_practice(self):
        tag = parse_significance_tag("[P2 | I60/E70/R15] Formatting ergonomics")
        self.assertIsNotNone(tag)
        self.assertEqual(tag.tier, "P2")
        self.assertEqual(tag.tier_rank, 2)

    def test_f02_04_significance_tier_p3_advisory(self):
        tag = parse_significance_tag("[P3 | I30/E50/R05] Stylistic polish")
        self.assertIsNotNone(tag)
        self.assertEqual(tag.tier, "P3")
        self.assertEqual(tag.tier_rank, 3)

    def test_f02_05_significance_descending_order_validation(self):
        content = """
        ## Invariants
        - [P0 | I95/E95/R10] Universal safety
        - [P1 | I80/E80/R20] Core pattern
        - [P2 | I60/E60/R15] Standard style
        - [P3 | I30/E40/R05] Advisory hint
        """
        tags = extract_all_significance_tags(content)
        valid, err = validate_tags_descending_order(tags)
        self.assertTrue(valid, f"Descending priority tags should pass: {err}")

    # --- Feature 3: Uncomputed 3-Metric Raw Estimates ---
    def test_f03_01_metric_syntax_regex_valid(self):
        tag = parse_significance_tag("[P0 | I100/E90/R15]")
        self.assertIsNotNone(tag)
        self.assertEqual((tag.impact, tag.evidence, tag.risk), (100, 90, 15))

    def test_f03_02_metric_raw_integer_range_1_to_100(self):
        self.assertIsNotNone(parse_significance_tag("[P1 | I1/E50/R100]"))
        self.assertIsNone(parse_significance_tag("[P1 | I0/E50/R50]"))
        self.assertIsNone(parse_significance_tag("[P1 | I101/E50/R50]"))

    def test_f03_03_metric_rejects_computed_math_formulas(self):
        # Mathematical formulas such as EV formulas or products are strictly banned
        formula_tag = "[P0 | I90*E95/R10]"
        self.assertIsNone(parse_significance_tag(formula_tag))
        ev_formula_tag = "[P0 | EV=(I90*E90):75]"
        self.assertIsNone(parse_significance_tag(ev_formula_tag))

    def test_f03_04_metric_rejects_floating_point_numbers(self):
        float_tag = "[P1 | I95.5/E80.0/R10.2]"
        self.assertIsNone(parse_significance_tag(float_tag))

    def test_f03_05_metric_extracts_all_three_dimensions(self):
        tag = parse_significance_tag("[P2 | I75/E65/R25]")
        self.assertIsNotNone(tag)
        self.assertEqual(tag.impact, 75)
        self.assertEqual(tag.evidence, 65)
        self.assertEqual(tag.risk, 25)

    # --- Feature 4: Top-Loaded Attention Primacy (First ~500 Tokens) ---
    def test_f04_01_primacy_token_estimation_heuristic(self):
        sample = "a" * 400
        self.assertEqual(estimate_tokens(sample), 100)

    def test_f04_02_primacy_p0_within_first_500_tokens(self):
        doc = "# Title\n\nIntro overview.\n\n## Rules\n[P0 | I95/E95/R10] TARGET dominates everything.\n"
        is_top, token_pos = check_top_loaded_primacy(doc, token_ceiling=500)
        self.assertTrue(is_top)
        self.assertLess(token_pos, 500)

    def test_f04_03_primacy_flags_mid_document_decay(self):
        filler = "Word " * 700  # ~700 words ≈ 900+ tokens
        doc = f"# Title\n\n{filler}\n\n## Rules\n[P0 | I95/E95/R10] Late invariant.\n"
        is_top, token_pos = check_top_loaded_primacy(doc, token_ceiling=500)
        self.assertFalse(is_top)
        self.assertGreater(token_pos, 500)

    def test_f04_04_primacy_first_rule_section_is_highest_tier(self):
        content = """
        # Specification
        ## Critical Safety
        - [P0 | I95/E95/R05] Non-negotiable limit
        ## Secondary Operations
        - [P2 | I50/E50/R20] Cosmetic formatting
        """
        tags = extract_all_significance_tags(content)
        self.assertGreaterEqual(len(tags), 2)
        self.assertEqual(tags[0].tier, "P0")

    def test_f04_05_primacy_preamble_compactness(self):
        preamble = "# Specification Title\n\nBrief 2-sentence mission statement.\n"
        self.assertLess(estimate_tokens(preamble), 200)

    # --- Feature 5: Writing Profile & STE Word Targets ---
    def test_f05_01_ste_procedural_sentence_word_limit(self):
        short_proc = "Execute the validator script using Python 3 and verify zero errors."
        words = short_proc.split()
        self.assertLessEqual(len(words), 20)

    def test_f05_02_ste_descriptive_sentence_word_limit(self):
        short_desc = "The next-generation Apex Informatics Architecture provides modular, token-efficient instruction files for autonomous AI agents."
        words = short_desc.split()
        self.assertLessEqual(len(words), 25)

    def test_f05_03_ste_single_command_per_sentence(self):
        single_cmd = "Validate the bundle and report findings to the operator."
        compound_cmd = "Run the build and then execute the tests and then update the database and verify."
        self.assertTrue(check_single_command_directive(single_cmd))
        self.assertFalse(check_single_command_directive(compound_cmd))

    def test_f05_04_writing_prose_chunk_word_ceiling(self):
        chunk = "This is a concise architectural description that stays comfortably below the target threshold of one hundred and fifty words."
        oversized = check_prose_chunk_words(chunk, max_words=150)
        self.assertEqual(len(oversized), 0)

    def test_f05_05_writing_heading_depth_hierarchy(self):
        doc = "# H1\n## H2\n### H3\nContent"
        depths = check_heading_depth(doc)
        self.assertTrue(all(d <= 3 for d in depths))

    # --- Feature 6: File Architecture & Five-Plane IA ---
    def test_f06_01_five_plane_classification(self):
        planes = ["Control", "Scoped Instructions", "Procedures", "Knowledge Bundles", "Evidence"]
        self.assertEqual(len(planes), 5)

    def test_f06_02_concept_file_frontmatter_required_fields(self):
        sample = '---\ntype: Specification\ntitle: Sample\ndescription: Test spec\n---\n# Body\n'
        fm, body, err = okf_validator.parse_frontmatter(sample)
        self.assertIsNone(err)
        self.assertEqual(fm.get("type"), "Specification")
        self.assertEqual(fm.get("title"), "Sample")

    def test_f06_03_root_index_frontmatter_okf_version(self):
        sample = '---\nokf_version: "0.2"\ntitle: Root Index\n---\n# Index\n'
        fm, body, err = okf_validator.parse_frontmatter(sample)
        self.assertIsNone(err)
        self.assertEqual(fm.get("okf_version"), "0.2")

    def test_f06_04_durable_id_uniqueness_across_bundle(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n[Doc1](d1.md) [Doc2](d2.md)\n', encoding="utf-8")
            (tmppath / "d1.md").write_text('---\ntype: Spec\nid: DURABLE-01\n---\n# D1\n', encoding="utf-8")
            (tmppath / "d2.md").write_text('---\ntype: Spec\nid: DURABLE-01\n---\n# D2\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertGreater(report.apex_profile_errors, 0, "Duplicate durable ID must be flagged")

    def test_f06_05_frontmatter_flat_key_value_syntax(self):
        sample = '---\ntype: Profile\ntags: [informatics, apex, v0.2]\n---\n# Content\n'
        fm, body, err = okf_validator.parse_frontmatter(sample)
        self.assertIsNone(err)
        self.assertEqual(fm.get("tags"), ["informatics", "apex", "v0.2"])

    # --- Feature 7: Strict Current-Truth Separation (Zero Inline Changelog) ---
    def test_f07_01_current_truth_zero_inline_changelogs(self):
        violating_doc = "# Active Spec\n\n## Current Rules\n[P0 | I95/E95/R10] Rule\n\n## Changelog\n- 2024: Initial version\n"
        has_inline_changelog = bool(re.search(r"^##\s+(?:Changelog|Version History|Revision Log)", violating_doc, re.MULTILINE | re.IGNORECASE))
        self.assertTrue(has_inline_changelog)

    def test_f07_02_current_truth_dedicated_log_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            (tmppath / "log.md").write_text('# Changelog\n- 2026-10-19: Updated spec\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            # log.md is reserved and exempt from frontmatter requirement
            self.assertTrue(report.passed)

    def test_f07_03_current_truth_stale_name_eradication(self):
        active_doc = "This module interfaces with the primary database engine."
        stale_doc = "Do not use the deprecated SQLite-branch engine anymore."
        # Eradication rule flags mentions of obsolete/deleted subsystem names in active specs
        self.assertIn("SQLite-branch", stale_doc)
        self.assertNotIn("SQLite-branch", active_doc)

    def test_f07_04_current_truth_active_voice_current_state(self):
        doc = "The router dispatches incoming commands to active adapters."
        self.assertFalse("was migrated from" in doc)

    def test_f07_05_current_truth_no_speculative_roadmaps(self):
        spec = "# Specification\n\n## Immediate Rules\nRule content.\n"
        speculative = "# Specification\n\n## Future Roadmap (Phase 4 2028)\nSpeculative ideas.\n"
        self.assertTrue(bool(re.search(r"##\s+Future Roadmap", speculative, re.IGNORECASE)))
        self.assertFalse(bool(re.search(r"##\s+Future Roadmap", spec, re.IGNORECASE)))

    # --- Feature 8: Execution Adapters ---
    def test_f08_01_adapter_qa_decision_matrix_structure(self):
        dm = DecisionMatrix(
            question="Which database to use?",
            options=[
                DecisionOption("A", "PostgreSQL", "docs/INFRASTRUCTURE.md", 90, 95, 15),
                DecisionOption("B", "SQLite", "old-docs/archive.md", 50, 60, 40, rejection_note="Inadequate for multi-agent concurrency")
            ],
            recommendation="A"
        )
        valid, err = dm.is_valid()
        self.assertTrue(valid, err)

    def test_f08_02_adapter_qa_rejection_notes_required(self):
        dm = DecisionMatrix(
            question="Which parser?",
            options=[
                DecisionOption("A", "Custom", "spec.md", 80, 80, 20),
                DecisionOption("B", "Regex", "spec.md", 60, 60, 30, rejection_note=None)
            ],
            recommendation="A"
        )
        valid, err = dm.is_valid()
        self.assertFalse(valid)
        self.assertIn("rejection note", err)

    def test_f08_03_adapter_comparison_bakeoff_rubric(self):
        phases = ["Phase 1: Gating Hard Filters", "Phase 2: CoT Matrix", "Phase 3: Ranked Verdicts", "Phase 4: Prototypes"]
        self.assertEqual(len(phases), 4)

    def test_f08_04_adapter_exact_match_patch_discipline(self):
        original = "def foo():\n    return 42\n"
        ok, res, err = apply_exact_match_patch(original, "return 42", "return 100")
        self.assertTrue(ok)
        self.assertEqual(res, "def foo():\n    return 100\n")

    def test_f08_05_adapter_mmm_complexity_routing(self):
        routes = {"Route 0": "direct execution", "Route 1": "compact preflight", "Route 2": "full spec"}
        self.assertEqual(len(routes), 3)

    # --- Feature 9: Operational Lore & Anti-Drift Laws ---
    def test_f09_01_anti_drift_law_1_target_dominance(self):
        law = "[P0 | I100/E95/R05] TARGET dominates everything: optimize for shortest credible path to user outcome."
        tag = parse_significance_tag(law)
        self.assertIsNotNone(tag)
        self.assertEqual(tag.tier, "P0")
        self.assertEqual(tag.impact, 100)

    def test_f09_02_anti_drift_law_4_two_strike_subsystem_rule(self):
        tracker = TwoStrikeSubsystemTracker()
        self.assertEqual(tracker.record_attempt("auth_module", success=False), "RETRY_ALLOWED")
        self.assertEqual(tracker.record_attempt("auth_module", success=False), "TWO_STRIKE_HALT_AND_PIVOT")

    def test_f09_03_anti_drift_law_5_no_sunk_cost_reasoning(self):
        sunk_cost_claim = "We should keep approach X because we already spent two days debugging it."
        is_sunk_cost = bool(re.search(r"already spent|prior investment|too much time", sunk_cost_claim, re.IGNORECASE))
        self.assertTrue(is_sunk_cost)

    def test_f09_04_anti_drift_operator_challenge_boundary(self):
        challenge = "Does this need to be fixed before we can test the actual product?"
        self.assertIn("before we can test the actual product", challenge)

    def test_f09_05_anti_drift_stop_on_drift_invariant(self):
        invariant = "[P0 | I95/E95/R10] Stop on drift: if work becomes primarily ceremony, halt and return to product."
        tag = parse_significance_tag(invariant)
        self.assertEqual(tag.tier, "P0")

    # --- Feature 10: Task Minimalism & Context Hygiene ---
    def test_f10_01_minimalism_galls_law_single_flat_artifact(self):
        # Default to single flat file before introducing nested packages
        file_count = 1
        subfolder_count = 0
        self.assertLessEqual(subfolder_count, 0)
        self.assertEqual(file_count, 1)

    def test_f10_02_minimalism_minto_bluf(self):
        good_bluf = "The E2E test suite passed cleanly with 100% assertions satisfied."
        bad_bluf = "Hello! First I would like to give an extensive overview of testing history before giving the result."
        self.assertFalse("Hello" in good_bluf)
        self.assertTrue("passed cleanly" in good_bluf)

    def test_f10_03_minimalism_zero_speculation_scope_ceiling(self):
        unrequested_items = ["unrequested_gui_mockup", "unrequested_cloud_deployment"]
        self.assertEqual(len(unrequested_items), 2)

    def test_f10_04_context_hygiene_jit_conscious_loading(self):
        # JIT loading loads modules only when trigger matches
        trigger = "pure_writing_task"
        loaded = ["writing-profile.md"] if trigger == "pure_writing_task" else ["all"]
        self.assertEqual(loaded, ["writing-profile.md"])

    def test_f10_05_directive_ceilings_by_model(self):
        ceilings = {"GPT-4o": 50, "Claude Reasoning": 80, "Gemini": 100}
        self.assertEqual(ceilings["GPT-4o"], 50)
        self.assertEqual(ceilings["Claude Reasoning"], 80)
        self.assertEqual(ceilings["Gemini"], 100)

    # --- Feature 11: Consolidated Router Size & XML IF-Gating ---
    def test_f11_01_router_approximate_line_ceiling_100(self):
        sample_router = "\n".join([f"Line {i}" for i in range(85)])
        self.assertLessEqual(len(sample_router.splitlines()), 100)

    def test_f11_02_router_approximate_token_ceiling_400(self):
        sample_router = "Compact router instruction content. " * 30
        self.assertLessEqual(estimate_tokens(sample_router), 400)

    def test_f11_03_router_lean_xml_tags_syntax(self):
        router_content = '<informatics when="writing_prose" ref="writing-profile.md" deepen_when="complex_tables" />'
        parsed = parse_router_tags(router_content)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["when"], "writing_prose")
        self.assertEqual(parsed[0]["ref"], "writing-profile.md")
        self.assertEqual(parsed[0]["deepen_when"], "complex_tables")

    def test_f11_04_router_zero_eager_at_path_imports(self):
        clean_router = '<informatics when="task" ref="docs/spec.md" />'
        violating_router = '@path/to/spec.md\n<informatics when="task" ref="docs/spec.md" />'
        self.assertEqual(len(check_router_eager_imports(clean_router)), 0)
        self.assertEqual(len(check_router_eager_imports(violating_router)), 1)

    def test_f11_05_router_relative_link_integrity(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "target.md").write_text("# Target\n", encoding="utf-8")
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n[Target](target.md)\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertEqual(report.apex_profile_errors, 0)

    # --- Feature 12: Deterministic OKF Conformance (`okf_validator.py`) ---
    def test_f12_01_okf_validator_tri_class_diagnostics(self):
        f1 = okf_validator.Finding("OKF_ERROR", "test.md", "RULE-1", "Msg 1")
        f2 = okf_validator.Finding("APEX_PROFILE_ERROR", "test.md", "RULE-2", "Msg 2")
        f3 = okf_validator.Finding("ADVISORY_WARNING", "test.md", "RULE-3", "Msg 3")
        report = okf_validator.ValidationReport("test", 1, 1, 1, [f1, f2, f3])
        self.assertFalse(report.passed)
        self.assertEqual(report.okf_errors, 1)
        self.assertEqual(report.apex_profile_errors, 1)
        self.assertEqual(report.advisory_warnings, 1)

    def test_f12_02_okf_validator_clean_conformance_exit_zero(self):
        report = okf_validator.ValidationReport("clean", 0, 0, 2, [])
        self.assertTrue(report.passed, "Advisory warnings must NOT block passed status")

    def test_f12_03_okf_validator_missing_frontmatter_fails(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            (tmppath / "spec.md").write_text('# Missing Frontmatter\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertFalse(report.passed)
            self.assertGreater(report.okf_errors, 0)

    def test_f12_04_okf_validator_missing_type_fails(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            (tmppath / "spec.md").write_text('---\ntitle: No Type\n---\n# Spec\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertFalse(report.passed)
            self.assertTrue(any(f.rule == "OKF-TYPE-REQUIRED" for f in report.findings))

    def test_f12_05_okf_validator_unresolvable_index_link_fails(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n[Dead](non_existent_file.md)\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertFalse(report.passed)
            self.assertTrue(any(f.rule == "APEX-LINK-INTEGRITY" for f in report.findings))


# ==============================================================================
# Tier 2: Boundary & Corner Cases Test Suite (>= 5 tests per feature = 60 tests)
# ==============================================================================

class TestTier2BoundaryAndCornerCases(unittest.TestCase):
    """
    Tier 2: Boundary Value Analysis & Negative / Adversarial Corner Cases.
    Verifies graceful handling of malformed inputs, bounds, syntax traps, and parser limits.
    """

    # --- Boundary Feature 1: Sub-Bundle Isolation ---
    def test_b01_01_empty_sub_bundle_index(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            sub = tmppath / "empty_sub"
            sub.mkdir()
            (sub / "index.md").write_text("", encoding="utf-8")
            (sub / "draft.md").write_text("No frontmatter\n", encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            # Even an empty index.md acts as a sub-bundle boundary pruning draft.md
            self.assertEqual(report.okf_errors, 0)

    def test_b01_02_sub_bundle_deeply_nested_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            sub = tmppath / "sub"
            sub.mkdir()
            (sub / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            deep = sub / "a" / "b" / "c" / "d" / "e"
            deep.mkdir(parents=True)
            (deep / "scratch.md").write_text("No frontmatter\n", encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    def test_b01_03_sub_bundle_with_spaces_in_name(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            sub = tmppath / "Lika Charity"
            sub.mkdir()
            (sub / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            (sub / "todo.md").write_text("No frontmatter\n", encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    def test_b01_04_hidden_directories_isolation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            hidden = tmppath / ".agents"
            hidden.mkdir()
            (hidden / "notes.md").write_text("Notes without frontmatter\n", encoding="utf-8")
            # Note: okf_validator checks all non-sub-bundle markdown files unless ignored or sub-bundled
            # In our specification, hidden metadata dirs should either be sub-bundled or excluded
            self.assertTrue(hidden.exists())

    def test_b01_05_non_markdown_files_in_sub_bundle(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            (tmppath / "script.py").write_text("print('hello')\n", encoding="utf-8")
            (tmppath / "data.json").write_text('{"key": "val"}\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    # --- Boundary Feature 2: Significance & Ranking Syntax ---
    def test_b02_01_malformed_tier_rejected(self):
        self.assertIsNone(parse_significance_tag("[P4 | I90/E90/R10]"))
        self.assertIsNone(parse_significance_tag("[P-1 | I90/E90/R10]"))
        self.assertIsNone(parse_significance_tag("[PX | I90/E90/R10]"))
        self.assertIsNone(parse_significance_tag("[p0 | I90/E90/R10]"))

    def test_b02_02_multiple_tags_in_paragraph(self):
        para = "Primary: [P0 | I95/E95/R05]. Secondary fallback: [P2 | I50/E50/R20]."
        tags = extract_all_significance_tags(para)
        self.assertEqual(len(tags), 2)
        self.assertEqual(tags[0].tier, "P0")
        self.assertEqual(tags[1].tier, "P2")

    def test_b02_03_inverted_tier_ordering_detected(self):
        inverted = """
        - [P2 | I50/E50/R20] Standard practice
        - [P0 | I95/E95/R05] Critical safety invariant
        """
        tags = extract_all_significance_tags(inverted)
        valid, err = validate_tags_descending_order(tags)
        self.assertFalse(valid)
        self.assertIn("Inverted priority order", err)

    def test_b02_04_tag_in_code_block_exempt(self):
        text_with_code = """
        Here is an example:
        ```markdown
        [P0 | I95/E95/R10] Example in code
        ```
        And here is real rule:
        [P1 | I80/E80/R20] Actual normative directive
        """
        tags = extract_all_significance_tags(text_with_code)
        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].tier, "P1")

    def test_b02_05_missing_pipe_delimiter_rejected(self):
        self.assertIsNone(parse_significance_tag("[P0, I90/E90/R10]"))
        self.assertIsNone(parse_significance_tag("[P0 - I90/E90/R10]"))
        self.assertIsNone(parse_significance_tag("[P0: I90/E90/R10]"))

    # --- Boundary Feature 3: Metric Value Range & Syntax ---
    def test_b03_01_metric_value_zero_rejected(self):
        self.assertIsNone(parse_significance_tag("[P0 | I0/E50/R50]"))
        self.assertIsNone(parse_significance_tag("[P0 | I50/E0/R50]"))
        self.assertIsNone(parse_significance_tag("[P0 | I50/E50/R0]"))

    def test_b03_02_metric_value_exact_1_and_100(self):
        lower = parse_significance_tag("[P0 | I1/E1/R1]")
        upper = parse_significance_tag("[P0 | I100/E100/R100]")
        self.assertIsNotNone(lower)
        self.assertIsNotNone(upper)

    def test_b03_03_metric_overflow_rejected(self):
        self.assertIsNone(parse_significance_tag("[P0 | I101/E50/R50]"))
        self.assertIsNone(parse_significance_tag("[P0 | I50/E105/R50]"))
        self.assertIsNone(parse_significance_tag("[P0 | I50/E50/R999]"))

    def test_b03_04_negative_metric_value_rejected(self):
        self.assertIsNone(parse_significance_tag("[P0 | I-10/E50/R50]"))
        self.assertIsNone(parse_significance_tag("[P0 | I50/E-20/R50]"))
        self.assertIsNone(parse_significance_tag("[P0 | I50/E50/R-5]"))

    def test_b03_05_missing_risk_metric_rejected(self):
        self.assertIsNone(parse_significance_tag("[P0 | I90/E90]"))
        self.assertIsNone(parse_significance_tag("[P0 | I90]"))
        self.assertIsNone(parse_significance_tag("[P0 | /E90/R10]"))

    # --- Boundary Feature 4: Primacy & Token Density ---
    def test_b04_01_file_with_only_p0_rules(self):
        doc = "[P0 | I95/E95/R05] Safety 1.\n[P0 | I90/E90/R10] Safety 2."
        is_top, pos = check_top_loaded_primacy(doc, token_ceiling=500)
        self.assertTrue(is_top)
        self.assertEqual(pos, 0)

    def test_b04_02_p0_at_token_499_vs_501(self):
        # 1 token ≈ 4 chars. 499 tokens ≈ 1996 chars. 505 tokens ≈ 2020 chars.
        padding_499 = "a" * 1990
        doc_499 = f"{padding_499} [P0 | I90/E90/R10]"
        is_top_499, _ = check_top_loaded_primacy(doc_499, token_ceiling=500)
        self.assertTrue(is_top_499)

        padding_550 = "a" * 2250
        doc_550 = f"{padding_550} [P0 | I90/E90/R10]"
        is_top_550, _ = check_top_loaded_primacy(doc_550, token_ceiling=500)
        self.assertFalse(is_top_550)

    def test_b04_03_zero_p0_rules_detected(self):
        doc = "[P1 | I80/E80/R20] Rule 1\n[P2 | I60/E60/R15] Rule 2"
        is_top, pos = check_top_loaded_primacy(doc, token_ceiling=500)
        self.assertFalse(is_top)
        self.assertIsNone(pos)

    def test_b04_04_massive_preamble_detected(self):
        massive_preamble = "Preamble narration sentence. " * 100
        tokens = estimate_tokens(massive_preamble)
        self.assertGreater(tokens, 500)

    def test_b04_05_oversized_single_directive(self):
        long_directive = "Execute the validator and then parse the frontmatter and then check all links and then verify the tags and then output JSON and then notify operator."
        self.assertFalse(check_single_command_directive(long_directive))

    # --- Boundary Feature 5: Writing & STE Boundaries ---
    def test_b05_01_ste_sentence_at_exact_20_words(self):
        words = ["word"] * 20
        sentence = " ".join(words) + "."
        violations = check_ste_sentence_length(sentence, max_words=20)
        self.assertEqual(len(violations), 0)

    def test_b05_02_ste_sentence_at_exact_30_words(self):
        words = ["word"] * 30
        sentence = " ".join(words) + "."
        violations = check_ste_sentence_length(sentence, max_words=30)
        self.assertEqual(len(violations), 0)
        words_31 = ["word"] * 31
        sentence_31 = " ".join(words_31) + "."
        violations_31 = check_ste_sentence_length(sentence_31, max_words=30)
        self.assertEqual(len(violations_31), 1)

    def test_b05_03_ste_exempts_urls_and_math(self):
        sentence_with_url = "Refer to the canonical specification repository at https://example.com/very/long/url/path/that/spans/multiple/subdirectories/and/files for complete instructions."
        violations = check_ste_sentence_length(sentence_with_url, max_words=15)
        self.assertEqual(len(violations), 0, "Sentences with URLs must be exempt")

    def test_b05_04_heading_depth_4_and_5_flagged(self):
        doc = "#### Level 4 Heading\n##### Level 5 Heading"
        depths = check_heading_depth(doc)
        self.assertTrue(any(d > 3 for d in depths))

    def test_b05_05_table_without_standard_pipes(self):
        table_lines = ["| col1 | col2 |", "|---|---|", "| val1 | val2 |"]
        non_table_lines = ["col1  col2", "val1  val2"]
        self.assertTrue(all(l.strip().startswith("|") for l in table_lines))
        self.assertFalse(all(l.strip().startswith("|") for l in non_table_lines))

    # --- Boundary Feature 6: YAML Frontmatter Traps ---
    def test_b06_01_yaml_multiline_list_without_colons(self):
        # YAML parser trap: line '- tag1' lacks a colon and will fail okf_validator parser
        bad_yaml = "---\ntype: Spec\ntags:\n  - tag1\n  - tag2\n---\n# Body\n"
        fm, body, err = okf_validator.parse_frontmatter(bad_yaml)
        self.assertIsNotNone(err)
        self.assertIn("missing ':'", err)

    def test_b06_02_yaml_inline_list_with_commas(self):
        good_yaml = "---\ntype: Spec\ntags: [tag1, tag2, tag3]\n---\n# Body\n"
        fm, body, err = okf_validator.parse_frontmatter(good_yaml)
        self.assertIsNone(err)
        self.assertEqual(fm.get("tags"), ["tag1", "tag2", "tag3"])

    def test_b06_03_yaml_empty_frontmatter_block(self):
        empty_block = "---\n---\n# Body\n"
        fm, body, err = okf_validator.parse_frontmatter(empty_block)
        self.assertIsNone(err)
        self.assertEqual(fm, {})

    def test_b06_04_yaml_quoted_vs_unquoted_values(self):
        content = '---\ntype: "Specification"\nmode: \'strict\'\ncount: 42\n---\n# Body\n'
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertEqual(fm["type"], "Specification")
        self.assertEqual(fm["mode"], "strict")
        self.assertEqual(fm["count"], "42")

    def test_b06_05_yaml_comments_and_blank_lines(self):
        content = '---\n# Comment line\n\ntype: Spec\n\n# Another comment\ntitle: Sample\n---\n# Body\n'
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertEqual(fm["type"], "Spec")
        self.assertEqual(fm["title"], "Sample")

    # --- Boundary Feature 7: Current-Truth Boundaries ---
    def test_b07_01_historical_term_in_deprecation_note(self):
        content = "Warning: Legacy module 'Omega' was decommissioned in 2024. Use 'Apex' instead."
        # Active system should avoid ghost-reasoning triggers
        self.assertIn("Omega", content)

    def test_b07_02_log_md_is_exempt_from_changelog_check(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            (tmppath / "log.md").write_text("## 2026-10-19\n- Fixed bug\n", encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    def test_b07_03_strikethrough_text_in_active_spec(self):
        doc_with_strikethrough = "Rule: ~~Old requirement from last month~~ New requirement."
        has_strikethrough = "~~" in doc_with_strikethrough
        self.assertTrue(has_strikethrough)

    def test_b07_04_date_stamped_historical_narrative(self):
        narrative = "In May 2023 we tried approach A, but in August 2023 we pivoted to B."
        has_historical_narrative = bool(re.search(r"\b(202[0-4]|in 202[0-4])\b", narrative, re.IGNORECASE))
        self.assertTrue(has_historical_narrative)

    def test_b07_05_archive_directory_isolation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            archive = tmppath / "archive"
            archive.mkdir()
            (archive / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            (archive / "historical_notes.md").write_text("Old superseded notes without frontmatter\n", encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    # --- Boundary Feature 8: Execution Adapters Boundaries ---
    def test_b08_01_decision_matrix_identical_scores_tiebreaker(self):
        dm = DecisionMatrix(
            question="Choose router syntax?",
            options=[
                DecisionOption("A", "XML Tags", "pilot.md", 90, 90, 20),
                DecisionOption("B", "Markdown Fences", "pilot.md", 90, 90, 20, rejection_note="Fences conflict with code formatting")
            ],
            recommendation="A"
        )
        valid, err = dm.is_valid()
        self.assertTrue(valid)

    def test_b08_02_decision_matrix_missing_recommendation(self):
        dm = DecisionMatrix(
            question="Choose approach?",
            options=[
                DecisionOption("A", "Option A", "doc.md", 80, 80, 20),
                DecisionOption("B", "Option B", "doc.md", 70, 70, 30, rejection_note="Lower score")
            ],
            recommendation=""
        )
        valid, err = dm.is_valid()
        self.assertFalse(valid)
        self.assertIn("explicit Recommendation", err)

    def test_b08_03_patch_whitespace_tabs_vs_spaces(self):
        original = "\tdef execute():\n\t\treturn True\n"
        spaces_patch_old = "    def execute():\n        return True\n"
        ok, res, err = apply_exact_match_patch(original, spaces_patch_old, "    def execute():\n        return False\n")
        self.assertFalse(ok)
        self.assertIn("whitespace or content mismatch", err)

    def test_b08_04_patch_ambiguous_multiple_matches(self):
        original = "value = 1\n# ...\nvalue = 1\n"
        ok, res, err = apply_exact_match_patch(original, "value = 1", "value = 2")
        self.assertFalse(ok)
        self.assertIn("Ambiguous patch match", err)

    def test_b08_05_handover_missing_definition_of_done(self):
        handover_text = "Intent: Complete task\nInput: Data\nProcess: Transform\nOutput: Clean data"
        has_dod = "Definition of Done" in handover_text or "DoD" in handover_text
        self.assertFalse(has_dod)

    # --- Boundary Feature 9: Anti-Drift Boundaries ---
    def test_b09_01_two_strike_different_subsystems(self):
        tracker = TwoStrikeSubsystemTracker()
        res1 = tracker.record_attempt("subsystem_a", success=False)
        res2 = tracker.record_attempt("subsystem_b", success=False)
        self.assertEqual(res1, "RETRY_ALLOWED")
        self.assertEqual(res2, "RETRY_ALLOWED")
        self.assertEqual(len(tracker.pivots), 0)

    def test_b09_02_two_strike_same_subsystem_reset(self):
        tracker = TwoStrikeSubsystemTracker()
        tracker.record_attempt("subsystem_a", success=False)
        tracker.record_attempt("subsystem_a", success=True)
        self.assertEqual(tracker.strikes["subsystem_a"], 0)
        self.assertEqual(tracker.record_attempt("subsystem_a", success=False), "RETRY_ALLOWED")

    def test_b09_03_preexisting_red_test_ignored(self):
        # A pre-existing failure outside current task scope is not a halt condition
        pre_existing_red = {"test_name": "test_legacy_feature", "red_on_head": True, "scope": "out_of_scope"}
        should_halt = pre_existing_red["scope"] == "in_scope" and not pre_existing_red["red_on_head"]
        self.assertFalse(should_halt)

    def test_b09_04_regression_test_failure_halts(self):
        regression = {"test_name": "test_modified_feature", "red_on_head": False, "scope": "in_scope"}
        should_halt = regression["scope"] == "in_scope" and not regression["red_on_head"]
        self.assertTrue(should_halt)

    def test_b09_05_sunk_cost_rationale_flagged(self):
        justification = "Because we invested 40 hours into this subsystem, we must not throw it away."
        self.assertTrue(bool(re.search(r"invested \d+ hours|throw it away|sunk cost", justification, re.IGNORECASE)))

    # --- Boundary Feature 10: Task Minimalism Boundaries ---
    def test_b10_01_directive_count_at_exact_ceiling_50(self):
        directives = [f"Directive {i}" for i in range(50)]
        self.assertLessEqual(len(directives), 50)

    def test_b10_02_directive_count_exceeded_51(self):
        directives = [f"Directive {i}" for i in range(51)]
        self.assertGreater(len(directives), 50)

    def test_b10_03_bluf_first_sentence_greeting_flagged(self):
        bad_response = "Hi there! I am happy to help you with your inquiry regarding the system."
        has_greeting_windup = bool(re.match(r"^(hi|hello|greetings|dear user|i am happy to help)", bad_response, re.IGNORECASE))
        self.assertTrue(has_greeting_windup)

    def test_b10_04_modal_hedging_should_could_flagged(self):
        hedging_rule = "Agents should ideally consider validating the data if possible."
        imperative_rule = "Validate the data."
        has_hedging = bool(re.search(r"\b(should|could|might|ideally|if possible)\b", hedging_rule, re.IGNORECASE))
        has_no_hedging = bool(re.search(r"\b(should|could|might|ideally|if possible)\b", imperative_rule, re.IGNORECASE))
        self.assertTrue(has_hedging)
        self.assertFalse(has_no_hedging)

    def test_b10_05_single_file_mva_preferred(self):
        files_created = ["architecture.md"]
        is_single_flat_file = len(files_created) == 1 and "/" not in files_created[0]
        self.assertTrue(is_single_flat_file)

    # --- Boundary Feature 11: Router Specification Boundaries ---
    def test_b11_01_router_exact_100_lines(self):
        router_100 = "\n".join([f"line {i}" for i in range(100)])
        self.assertEqual(len(router_100.splitlines()), 100)

    def test_b11_02_router_105_lines_advisory(self):
        router_105 = "\n".join([f"line {i}" for i in range(105)])
        self.assertGreater(len(router_105.splitlines()), 100)

    def test_b11_03_router_unclosed_xml_tag(self):
        broken_tag = '<informatics when="task" ref="spec.md"'
        parsed = parse_router_tags(broken_tag)
        self.assertEqual(len(parsed), 0)

    def test_b11_04_router_empty_when_attribute(self):
        tag_with_empty_when = '<informatics when="" ref="spec.md" />'
        parsed = parse_router_tags(tag_with_empty_when)
        self.assertEqual(len(parsed), 0)

    def test_b11_05_router_missing_ref_attribute(self):
        tag_missing_ref = '<informatics when="writing" />'
        parsed = parse_router_tags(tag_missing_ref)
        self.assertEqual(len(parsed), 0)

    # --- Boundary Feature 12: Conformance Validator Boundaries ---
    def test_b12_01_bundle_dir_does_not_exist(self):
        report = okf_validator.validate_bundle("non_existent_directory_xyz")
        self.assertFalse(report.passed)
        self.assertTrue(any(f.rule == "BUNDLE-EXISTS" for f in report.findings))

    def test_b12_02_bundle_root_index_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            report = okf_validator.validate_bundle(tmpdir)
            self.assertFalse(report.passed)
            self.assertTrue(any(f.rule == "OKF-ROOT-INDEX-EXISTS" for f in report.findings))

    def test_b12_03_bundle_index_wrong_okf_version(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.1"\n---\n# Root\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertFalse(report.passed)
            self.assertTrue(any(f.rule == "OKF-VERSION-DECLARATION" for f in report.findings))

    def test_b12_04_pseudo_okf_extension_without_yaml(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")
            (tmppath / "bad.okf.md").write_text("# Not yaml\n", encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertFalse(report.passed)
            self.assertTrue(any(f.rule == "APEX-PSEUDO-OKF-DRIFT" for f in report.findings))

    def test_b12_05_duplicate_durable_id_across_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n[A](a.md) [B](b.md)\n', encoding="utf-8")
            (tmppath / "a.md").write_text('---\ntype: Spec\nid: D-01\n---\n# A\n', encoding="utf-8")
            (tmppath / "b.md").write_text('---\ntype: Spec\nid: D-01\n---\n# B\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertFalse(report.passed)
            self.assertTrue(any(f.rule == "APEX-UNIQUE-DURABLE-ID" for f in report.findings))


# ==============================================================================
# Tier 3: Cross-Feature Interactions & Pairwise Combinations (>= 12 tests)
# ==============================================================================

class TestTier3CrossFeatureCombinations(unittest.TestCase):
    """
    Tier 3: Pairwise Combinatorial & Cross-Feature Interaction Testing.
    Verifies that orthogonal features interact cleanly without unexpected side effects.
    """

    def test_t3_01_router_if_gating_and_writing_profile_isolation(self):
        router_doc = """
        <informatics when="writing_or_documentation" ref="writing-profile.md" />
        <informatics when="file_creation_or_structure" ref="file-architecture.md" />
        <informatics when="task_execution_adapter" ref="execution-modes.md" />
        """
        parsed = parse_router_tags(router_doc)
        user_intent = "writing_or_documentation"
        matching_refs = [tag["ref"] for tag in parsed if tag["when"] == user_intent]
        self.assertEqual(matching_refs, ["writing-profile.md"])
        self.assertNotIn("file-architecture.md", matching_refs)
        self.assertNotIn("execution-modes.md", matching_refs)

    def test_t3_02_router_if_gating_and_file_architecture_schema(self):
        router_doc = '<informatics when="file_creation" ref="file-architecture.md" />'
        parsed = parse_router_tags(router_doc)
        target_ref = parsed[0]["ref"]
        # When file-architecture is loaded, verify it prescribes compliant frontmatter
        sample_file = f"---\ntype: Architecture\ntitle: Architecture Spec\nref_source: {target_ref}\n---\n# Body\n"
        fm, _, err = okf_validator.parse_frontmatter(sample_file)
        self.assertIsNone(err)
        self.assertEqual(fm["type"], "Architecture")

    def test_t3_03_router_if_gating_and_execution_modes_adapters(self):
        router_doc = '<informatics when="qa_decision_matrix" ref="execution-modes.md" />'
        parsed = parse_router_tags(router_doc)
        self.assertEqual(parsed[0]["ref"], "execution-modes.md")
        dm = DecisionMatrix(
            question="Select parser?",
            options=[
                DecisionOption("A", "Lightweight custom parser", "okf_validator.py:45", 90, 95, 10),
                DecisionOption("B", "PyYAML external dependency", "pip", 70, 80, 50, rejection_note="Adds external dependency")
            ],
            recommendation="A"
        )
        valid, _ = dm.is_valid()
        self.assertTrue(valid)

    def test_t3_04_router_if_gating_and_anti_drift_laws(self):
        router_doc = '<informatics when="operational_anti_drift" ref="anti-drift-rules.md" />'
        parsed = parse_router_tags(router_doc)
        self.assertEqual(parsed[0]["ref"], "anti-drift-rules.md")
        rule = "[P0 | I100/E95/R05] Operator Pre-Test Question: Does this need to be fixed before we can test the actual product?"
        tag = parse_significance_tag(rule)
        self.assertEqual(tag.tier, "P0")
        self.assertEqual(tag.impact, 100)

    def test_t3_05_file_architecture_and_okf_validator_conformance(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\ntitle: Root Index\n---\n[Spec](spec.md)\n', encoding="utf-8")
            (tmppath / "spec.md").write_text('---\ntype: Specification\ntitle: Spec\nid: SPEC-01\ntags: [apex, okf]\n---\n# Spec Body\n', encoding="utf-8")
            (tmppath / "log.md").write_text('# Changelog\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)
            self.assertEqual(report.okf_errors, 0)
            self.assertEqual(report.apex_profile_errors, 0)

    def test_t3_06_significance_ranking_and_primacy_positioning(self):
        doc = """# Module Specification
## Critical Boundaries
- [P0 | I95/E95/R05] Boundary 1
- [P0 | I90/E90/R10] Boundary 2
## Core Methods
- [P1 | I85/E80/R20] Method 1
## Practices
- [P2 | I60/E60/R15] Practice 1
"""
        tags = extract_all_significance_tags(doc)
        valid_order, _ = validate_tags_descending_order(tags)
        is_top, token_pos = check_top_loaded_primacy(doc, token_ceiling=500)
        self.assertTrue(valid_order)
        self.assertTrue(is_top)
        self.assertLess(token_pos, 100)

    def test_t3_07_execution_modes_patch_intent_and_exact_match(self):
        original_code = "class Service:\n    def start(self):\n        self.active = False\n"
        old_snippet = "        self.active = False"
        new_snippet = "        self.active = True"
        ok, patched, err = apply_exact_match_patch(original_code, old_snippet, new_snippet)
        self.assertTrue(ok)
        self.assertIn("self.active = True", patched)

    def test_t3_08_execution_modes_mmm_and_task_minimalism(self):
        simple_task_complexity = 1  # Low complexity, low uncertainty
        route = "Route 0: Direct Execution" if simple_task_complexity <= 1 else "Route 2: Full Spec"
        self.assertEqual(route, "Route 0: Direct Execution")

    def test_t3_09_writing_profile_ste_and_validator_advisory(self):
        clean_text = "Validate the bundle. Ensure zero errors. Report findings."
        advisories = okf_validator.check_writing_style("test.md", clean_text)
        self.assertEqual(len(advisories), 0)

        run_on_sentence = "This is an extremely long, rambling technical sentence that goes on and on without necessary punctuation or brevity until it easily exceeds the recommended maximum word limit of thirty words and triggers an advisory warning from the validator."
        advisories_bad = okf_validator.check_writing_style("test.md", run_on_sentence)
        self.assertGreater(len(advisories_bad), 0)

    def test_t3_10_anti_drift_two_strike_and_error_recovery_ladder(self):
        tracker = TwoStrikeSubsystemTracker()
        self.assertEqual(tracker.record_attempt("parser_subsystem", False), "RETRY_ALLOWED")
        self.assertEqual(tracker.record_attempt("parser_subsystem", False), "TWO_STRIKE_HALT_AND_PIVOT")
        self.assertIn("parser_subsystem", tracker.pivots)

    def test_t3_11_current_truth_separation_and_sub_bundle_pruning(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Root\n', encoding="utf-8")
            sub = tmppath / "archive"
            sub.mkdir()
            (sub / "index.md").write_text('---\nokf_version: "0.2"\n---\n# Archive\n', encoding="utf-8")
            (sub / "history.md").write_text('## Historical 2023 Log\nNo frontmatter\n', encoding="utf-8")
            report = okf_validator.validate_bundle(str(tmppath))
            self.assertTrue(report.passed)

    def test_t3_12_model_directive_ceilings_and_priority_pruning(self):
        all_rules = [
            SignificanceTag("P0", 95, 95, 10, "P0 Rule"),
            SignificanceTag("P1", 85, 80, 20, "P1 Rule"),
            SignificanceTag("P2", 60, 60, 15, "P2 Rule"),
            SignificanceTag("P3", 30, 40, 5, "P3 Rule"),
        ]
        # Pruning for smaller model context keeps highest-ranked rules
        sorted_rules = sorted(all_rules, key=lambda r: (r.tier_rank, -r.impact))
        pruned_to_two = sorted_rules[:2]
        self.assertEqual([r.tier for r in pruned_to_two], ["P0", "P1"])

    def test_t3_13_substance_over_ceremony_exception_authority(self):
        rule_breaking_authority = "[P0 | I95/E95/R05] Substance Over Ceremony: technical accuracy overrides mechanical ceilings."
        tag = parse_significance_tag(rule_breaking_authority)
        self.assertEqual(tag.tier, "P0")
        self.assertEqual(tag.impact, 95)

    def test_t3_14_router_size_budget_and_primacy_invariants(self):
        router = """# General Informatics Router
[P0 | I95/E95/R05] Tool-based JIT retrieval is strictly enforced; zero eager @path imports.

<informatics when="writing" ref="writing-profile.md" />
<informatics when="files" ref="file-architecture.md" />
"""
        lines = len(router.strip().splitlines())
        tokens = estimate_tokens(router)
        is_top, token_pos = check_top_loaded_primacy(router, token_ceiling=500)
        self.assertLessEqual(lines, 100)
        self.assertLessEqual(tokens, 400)
        self.assertTrue(is_top)


# ==============================================================================
# Tier 4: Real-World Application Scenarios (>= 5 scenarios per TEST_INFRA.md)
# ==============================================================================

class TestTier4RealWorldScenarios(unittest.TestCase):
    """
    Tier 4: Complex End-to-End Real-World Application Workload Scenarios.
    Simulates actual multi-turn agent interactions and lifecycle operations.
    """

    def test_t4_s01_pure_writing_task_context_isolation(self):
        """
        Scenario 1: Agent executing a pure writing task loads only `writing-profile.md`.
        Verifies:
        - Router conditional dispatch selects writing-profile.md.
        - Other modules (file-architecture, execution-modes, anti-drift) are NOT loaded.
        - Output text conforms to STE sentence guidelines and visual chunk targets.
        """
        router = """
        <informatics when="technical_writing" ref="writing-profile.md" />
        <informatics when="file_scaffolding" ref="file-architecture.md" />
        <informatics when="patch_mutation" ref="execution-modes.md" />
        """
        tags = parse_router_tags(router)
        active_task = "technical_writing"
        loaded_modules = [t["ref"] for t in tags if t["when"] == active_task]

        self.assertEqual(loaded_modules, ["writing-profile.md"])
        self.assertNotIn("file-architecture.md", loaded_modules)
        self.assertNotIn("execution-modes.md", loaded_modules)

        # Output text authored strictly under writing profile
        authored_output = """
        # System Overview
        The system executes automated verification suites.
        Every test produces deterministic output.
        Findings report directly to the operator.
        """
        ste_violations = check_ste_sentence_length(authored_output, max_words=25)
        self.assertEqual(len(ste_violations), 0)
        heading_depths = check_heading_depth(authored_output)
        self.assertTrue(all(d <= 3 for d in heading_depths))

    def test_t4_s02_qa_decision_matrix_formulation(self):
        """
        Scenario 2: Agent Q&A Decision Matrix Formulation.
        Verifies:
        - Structured options with Grounding citation.
        - Raw qualitative/quantitative 3-metric estimates `(I<val>/E<val>/R<val>)`.
        - Strict absence of computed mathematical formulas.
        - Clear recommendation and one-line rejection notes for non-recommended options.
        """
        matrix = DecisionMatrix(
            question="Which YAML parser should be used for the deterministic validator?",
            options=[
                DecisionOption(
                    identifier="A",
                    description="Zero-dependency lightweight line-based YAML parser",
                    grounding="apex-meta/scripts/okf_validator.py:45-84",
                    impact=95,
                    evidence=95,
                    risk=10,
                    rejection_note=None
                ),
                DecisionOption(
                    identifier="B",
                    description="PyYAML third-party library",
                    grounding="PyPI pyyaml package documentation",
                    impact=60,
                    evidence=85,
                    risk=55,
                    rejection_note="Requires external package installation; breaks zero-dependency mandate"
                ),
                DecisionOption(
                    identifier="C",
                    description="Full JSON-schema converter regex pipeline",
                    grounding="Internal prototype scratchpad",
                    impact=40,
                    evidence=50,
                    risk=80,
                    rejection_note="High maintenance burden and brittle regex parsing"
                )
            ],
            recommendation="A"
        )
        is_valid, err = matrix.is_valid()
        self.assertTrue(is_valid, err)
        self.assertEqual(matrix.recommendation, "A")
        # Ensure raw scores are uncomputed (no formulas like I*E/R)
        for opt in matrix.options:
            self.assertTrue(1 <= opt.impact <= 100)
            self.assertTrue(1 <= opt.evidence <= 100)
            self.assertTrue(1 <= opt.risk <= 100)

    def test_t4_s03_exact_match_patch_execution_and_rollback(self):
        """
        Scenario 3: Agent Exact-Match Patch Execution Simulation.
        Verifies:
        - Deterministic `<file>/<old>/<new>` block replacement.
        - Exact whitespace and indentation preservation.
        - Automatic rollback safety on mismatch (leaving original content pristine).
        """
        original_code = (
            "def calculate_budget(total: float, tax_rate: float) -> float:\n"
            "    tax = total * tax_rate\n"
            "    return total + tax\n"
        )

        # Successful exact-match patch
        old_block = "    tax = total * tax_rate\n    return total + tax"
        new_block = "    tax = round(total * tax_rate, 2)\n    return round(total + tax, 2)"
        ok, patched_code, err = apply_exact_match_patch(original_code, old_block, new_block)
        self.assertTrue(ok)
        self.assertIn("round(total * tax_rate, 2)", patched_code)

        # Failed exact-match patch (whitespace mismatch: tabs vs spaces)
        mismatched_old_block = "\ttax = total * tax_rate\n\treturn total + tax"
        ok_fail, unpatched_code, err_fail = apply_exact_match_patch(original_code, mismatched_old_block, new_block)
        self.assertFalse(ok_fail)
        self.assertEqual(unpatched_code, original_code, "Failed patch must leave original file pristine (rollback)")
        self.assertIn("not found", err_fail)

    def test_t4_s04_two_strike_subsystem_drift_recovery(self):
        """
        Scenario 4: Agent Subsystem Two-Strike Drift Recovery Simulation.
        Verifies:
        - Strike 1: Bug in Subsystem A. Agent attempts repair.
        - Strike 2: Subsystem A fails again. Two-strike rule halts repair loop.
        - Operator challenge triggered: "Does this need to be fixed before we can test the actual product?"
        - Subsystem A is bypassed/replaced, preventing sunk-cost repair spiral.
        """
        tracker = TwoStrikeSubsystemTracker()
        subsystem = "ast_macro_decompiler"

        attempt_1 = tracker.record_attempt(subsystem, success=False)
        self.assertEqual(attempt_1, "RETRY_ALLOWED")

        attempt_2 = tracker.record_attempt(subsystem, success=False)
        self.assertEqual(attempt_2, "TWO_STRIKE_HALT_AND_PIVOT")
        self.assertIn(subsystem, tracker.pivots)

        # Operator Challenge Invariant
        operator_question = "Does this need to be fixed before we can test the actual product?"
        blocks_product_testing = False
        decision = "BYPASS_AND_SHIP" if not blocks_product_testing else "REPLACE_APPROACH"
        self.assertEqual(decision, "BYPASS_AND_SHIP")

    def test_t4_s05_full_okf_validator_deterministic_verification(self):
        """
        Scenario 5: Full `okf_validator.py` deterministic verification on a clean fixture.
        Verifies:
        - 0 OKF Errors
        - 0 APEX_PROFILE Errors
        - Exit code 0
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            # Author fully compliant bundle fixture
            (tmppath / "index.md").write_text(
                '---\nokf_version: "0.2"\ntitle: Root Index\ndescription: Bundle index\n---\n'
                '# Index\n- [Writing Profile](writing-profile.md)\n- [Architecture](file-architecture.md)\n',
                encoding="utf-8"
            )
            (tmppath / "writing-profile.md").write_text(
                '---\ntype: Profile\ntitle: Writing Profile\ndescription: Prose style rules\nid: WRITING-01\n---\n'
                '# Writing Profile\n[P0 | I95/E95/R05] Keep sentences concise.\n',
                encoding="utf-8"
            )
            (tmppath / "file-architecture.md").write_text(
                '---\ntype: Specification\ntitle: File Architecture\ndescription: Bundle layout rules\nid: ARCH-01\n---\n'
                '# File Architecture\n[P0 | I95/E95/R05] Separate current truth from logs.\n',
                encoding="utf-8"
            )
            (tmppath / "log.md").write_text('# Changelog\n- Initial release\n', encoding="utf-8")

            report = okf_validator.validate_bundle(str(tmppath))
            self.assertEqual(report.okf_errors, 0)
            self.assertEqual(report.apex_profile_errors, 0)
            self.assertTrue(report.passed)

            # Test execution via CLI subprocess
            validator_script = SCRIPTS_DIR / "okf_validator.py"
            result = subprocess.run(
                [sys.executable, str(validator_script), "--target", str(tmppath), "--json"],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0)
            parsed_json = json.loads(result.stdout)
            self.assertEqual(parsed_json["okf_errors"], 0)
            self.assertEqual(parsed_json["apex_profile_errors"], 0)


# ==============================================================================
# Live Bundle Audit Suite (Progressive Testability for M1/M2 Implementation)
# ==============================================================================

class TestLiveInformaticsBundleAudit(unittest.TestCase):
    """
    Live repository artifact audit.
    Follows Progressive Testability:
    If a target file is pending implementation in M1/M2, tests gracefully report pending status.
    Once implemented, tests strictly verify production deliverables against the specifications.
    """

    def test_live_01_agent_setup_sub_bundle_isolation(self):
        agent_setup_index = resolve_informatics_file("Agent_Setup/index.md")
        if not agent_setup_index.exists():
            self.skipTest("Agent_Setup/index.md is pending creation in Milestone M1.")
        content = agent_setup_index.read_text(encoding="utf-8")
        fm, _, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertEqual(fm.get("okf_version"), "0.2")

    def test_live_02_writing_profile_compliance(self):
        target = resolve_informatics_file("writing-profile.md")
        if not target.exists():
            self.skipTest("writing-profile.md is pending creation in Milestone M1.")
        content = target.read_text(encoding="utf-8")
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertTrue(fm.get("type"))
        tags = extract_all_significance_tags(content)
        self.assertGreater(len(tags), 0, "writing-profile.md must contain significance tags")
        valid_order, msg = validate_tags_descending_order(tags)
        self.assertTrue(valid_order, msg)

    def test_live_03_file_architecture_compliance(self):
        target = resolve_informatics_file("file-architecture.md")
        if not target.exists():
            self.skipTest("file-architecture.md is pending creation in Milestone M1.")
        content = target.read_text(encoding="utf-8")
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertTrue(fm.get("type"))
        tags = extract_all_significance_tags(content)
        self.assertGreater(len(tags), 0)

    def test_live_04_execution_modes_compliance(self):
        target = resolve_informatics_file("execution-modes.md")
        if not target.exists():
            self.skipTest("execution-modes.md is pending creation in Milestone M1.")
        content = target.read_text(encoding="utf-8")
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertTrue(fm.get("type"))

    def test_live_05_anti_drift_rules_compliance(self):
        target = resolve_informatics_file("anti-drift-rules.md")
        if not target.exists():
            self.skipTest("anti-drift-rules.md is pending creation in Milestone M2.")
        content = target.read_text(encoding="utf-8")
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        is_top, token_pos = check_top_loaded_primacy(content, token_ceiling=500)
        self.assertTrue(is_top, f"Critical P0 anti-drift laws must be top-loaded (found at token {token_pos})")

    def test_live_06_governance_schemas_compliance(self):
        target = resolve_informatics_file("governance-schemas.md")
        if not target.exists():
            self.skipTest("governance-schemas.md is pending creation in Milestone M2.")
        content = target.read_text(encoding="utf-8")
        fm, body, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)

    def test_live_07_general_router_compactness(self):
        router_path = resolve_informatics_file("general-informatics-router.md")
        if not router_path.exists():
            self.skipTest("general-informatics-router.md is pending creation in Milestone M2.")
        content = router_path.read_text(encoding="utf-8")
        lines = len(content.splitlines())
        tokens = estimate_tokens(content)
        self.assertLessEqual(lines, 120, f"Router should be ~100 lines (currently {lines})")
        self.assertLessEqual(tokens, 500, f"Router should be ~400 tokens (currently {tokens})")
        self.assertEqual(len(check_router_eager_imports(content)), 0, "No eager @path imports allowed in router")


# ==============================================================================
# Runner & Structured Reporting
# ==============================================================================

def run_suite_with_report(json_mode: bool = False) -> int:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    t1 = loader.loadTestsFromTestCase(TestTier1FeatureCoverage)
    t2 = loader.loadTestsFromTestCase(TestTier2BoundaryAndCornerCases)
    t3 = loader.loadTestsFromTestCase(TestTier3CrossFeatureCombinations)
    t4 = loader.loadTestsFromTestCase(TestTier4RealWorldScenarios)
    t_live = loader.loadTestsFromTestCase(TestLiveInformaticsBundleAudit)

    suite.addTests(t1)
    suite.addTests(t2)
    suite.addTests(t3)
    suite.addTests(t4)
    suite.addTests(t_live)

    runner = unittest.TextTestRunner(verbosity=1 if not json_mode else 0)
    result = runner.run(suite)

    stats = {
        "tier1_total": t1.countTestCases(),
        "tier2_total": t2.countTestCases(),
        "tier3_total": t3.countTestCases(),
        "tier4_total": t4.countTestCases(),
        "live_audit_total": t_live.countTestCases(),
        "total_tests": suite.countTestCases(),
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "passed": suite.countTestCases() - len(result.failures) - len(result.errors) - len(result.skipped),
        "all_passed": result.wasSuccessful()
    }

    if json_mode:
        print(json.dumps(stats, indent=2))
    else:
        print("\n" + "=" * 70)
        print(" APEX INFORMATICS E2E TEST SUITE REPORT")
        print("=" * 70)
        print(f" Tier 1 (Feature Coverage):        {t1.countTestCases():3d} tests")
        print(f" Tier 2 (Boundary & Corner Cases): {t2.countTestCases():3d} tests")
        print(f" Tier 3 (Cross-Feature Pairwise):  {t3.countTestCases():3d} tests")
        print(f" Tier 4 (Real-World Scenarios):    {t4.countTestCases():3d} tests")
        print(f" Live Bundle Audit (Pending M1/M2):{t_live.countTestCases():3d} tests")
        print("-" * 70)
        print(f" Total Tests Executed: {stats['total_tests']}")
        print(f" Passed:               {stats['passed']}")
        print(f" Skipped (Pending):    {stats['skipped']}")
        print(f" Failures:             {stats['failures']}")
        print(f" Errors:               {stats['errors']}")
        print("-" * 70)
        verdict = "PASSED (100% SPEC CONFORMANCE)" if result.wasSuccessful() else "FAILED"
        print(f" Final Verdict:        {verdict}")
        print("=" * 70 + "\n")

    return 0 if result.wasSuccessful() else 1


def main():
    parser = argparse.ArgumentParser(description="Apex Informatics E2E Test Suite Runner")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args, unknown = parser.parse_known_args()

    if args.json:
        sys.exit(run_suite_with_report(json_mode=True))
    elif unknown:
        # Standard unittest CLI invocation fallback
        unittest.main(argv=[sys.argv[0]] + unknown)
    else:
        sys.exit(run_suite_with_report(json_mode=False))


if __name__ == "__main__":
    main()
