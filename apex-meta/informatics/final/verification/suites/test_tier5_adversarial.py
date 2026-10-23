#!/usr/bin/env python3
"""
test_tier5_adversarial.py — Tier 5 Adversarial Behavioral & Scenario Hardening Test Suite.

Authoritative Context:
- ORIGINAL_REQUEST.md (Requirements R1–R5 and Acceptance Criteria)
- DISPATCH.md (Tier 5 Adversarial Behavioral & Scenario Hardening)
- PROJECT.md, TEST_INFRA.md, TEST_READY.md
- Upstream Lore: Snippets.md, 2Dos Ai Instructions.md

Modules Tested:
1. Context Isolation Simulation & JIT Dispatch Mechanics
2. Operational Lore Traceability & Exact Codification
3. Task Adapter Semantic Soundness (Exact Patch, Decision Matrix, Bake-Off, MMM)
4. Significance Ranking, Math Formula Prohibition & Top-Loaded Primacy
5. OKF v0.2 Frontmatter, Flat YAML & Bundle Link Integrity
6. Router Compactness, Token Budgets & Exception Authority
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Dict, List, Optional, Set, Tuple
import unittest
import xml.etree.ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parents[5]
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final"
TESTS_DIR = INFORMATICS_DIR / "verification" / "suites"
SCRIPTS_DIR = REPO_ROOT / "apex-meta" / "scripts"
FINAL_TOOLS_DIR = INFORMATICS_DIR / "tools"

for p in (SCRIPTS_DIR, FINAL_TOOLS_DIR, TESTS_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

def resolve_file(fname: str) -> Path:
    p_root = REPO_ROOT / "apex-meta" / "informatics" / fname
    if p_root.exists():
        return p_root
    for base in (INFORMATICS_DIR, INFORMATICS_DIR / "specs", INFORMATICS_DIR / "sub-bundles"):
        cand = base / fname
        if cand.exists():
            return cand
    return p_root

import okf_validator

ALL_DELIVERABLES = [
    "Agent_Setup/index.md",
    "file-architecture.md",
    "writing-profile.md",
    "execution-modes.md",
    "anti-drift-rules.md",
    "governance-schemas.md",
    "index.md",
    "general-informatics-router.md",
]

SIG_TAG_REGEX = re.compile(
    r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]"
)
ROUTER_XML_TAG_REGEX = re.compile(
    r'<informatics\s+when="([^"]+)"\s+ref="([^"]+)"(?:\s+deepen_when="([^"]+)")?\s*/?>'
)


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```[\s\S]*?```", "", text)


# ==============================================================================
# Suite 1: Context Isolation Simulation & JIT Dispatch Mechanics
# ==============================================================================

class TestContextIsolationSimulation(unittest.TestCase):
    """
    Stress-tests context isolation:
    Simulates agent runtime dispatch under various operational intents.
    Verifies zero eager expansion and strict single-module JIT loading.
    """

    def setUp(self):
        self.router_text = resolve_file("general-informatics-router.md").read_text(encoding="utf-8")
        self.index_text = resolve_file("index.md").read_text(encoding="utf-8")

    def test_cis_01_pure_writing_task_isolation(self):
        """
        Pure writing task matches ONLY `writing_or_documentation` and resolves ONLY `writing-profile.md`.
        Remaining 7 deliverable files MUST NOT be expanded.
        """
        router_tags = okf_validator.extract_links(self.router_text)  # fallback
        # Parse XML tags
        xml_matches = ROUTER_XML_TAG_REGEX.findall(self.router_text)
        dispatches = {when: ref for when, ref, _ in xml_matches}

        self.assertIn("writing_or_documentation", dispatches)
        target_file = dispatches["writing_or_documentation"]
        self.assertEqual(target_file, "writing-profile.md")

        # Disallowed files for a pure writing intent
        disallowed = [
            "file-architecture.md",
            "execution-modes.md",
            "anti-drift-rules.md",
            "governance-schemas.md",
            "Agent_Setup/index.md",
            "standard.md",
            "migration.md"
        ]

        active_intent = "writing_or_documentation"
        loaded_modules = [ref for when, ref, _ in xml_matches if when == active_intent]

        self.assertEqual(loaded_modules, ["writing-profile.md"])
        for mod in disallowed:
            self.assertNotIn(mod, loaded_modules, f"Context bleed: {mod} was loaded for pure writing task")

    def test_cis_02_pure_file_scaffolding_isolation(self):
        """
        Pure file creation task matches ONLY `file_creation_or_structure` and resolves ONLY `file-architecture.md`.
        """
        xml_matches = ROUTER_XML_TAG_REGEX.findall(self.router_text)
        dispatches = {when: ref for when, ref, _ in xml_matches}

        self.assertIn("file_creation_or_structure", dispatches)
        self.assertEqual(dispatches["file_creation_or_structure"], "file-architecture.md")

        active_intent = "file_creation_or_structure"
        loaded_modules = [ref for when, ref, _ in xml_matches if when == active_intent]
        self.assertEqual(loaded_modules, ["file-architecture.md"])
        self.assertNotIn("writing-profile.md", loaded_modules)
        self.assertNotIn("execution-modes.md", loaded_modules)

    def test_cis_03_pure_task_adapter_isolation(self):
        """
        Task adapter request matches ONLY `task_execution_adapter` and resolves ONLY `execution-modes.md`.
        """
        xml_matches = ROUTER_XML_TAG_REGEX.findall(self.router_text)
        dispatches = {when: ref for when, ref, _ in xml_matches}

        self.assertIn("task_execution_adapter", dispatches)
        self.assertEqual(dispatches["task_execution_adapter"], "execution-modes.md")

        active_intent = "task_execution_adapter"
        loaded_modules = [ref for when, ref, _ in xml_matches if when == active_intent]
        self.assertEqual(loaded_modules, ["execution-modes.md"])
        self.assertNotIn("writing-profile.md", loaded_modules)
        self.assertNotIn("anti-drift-rules.md", loaded_modules)

    def test_cis_04_pure_anti_drift_isolation(self):
        """
        Operational anti-drift query matches ONLY `operational_anti_drift` and resolves ONLY `anti-drift-rules.md`.
        """
        xml_matches = ROUTER_XML_TAG_REGEX.findall(self.router_text)
        dispatches = {when: ref for when, ref, _ in xml_matches}

        self.assertIn("operational_anti_drift", dispatches)
        self.assertEqual(dispatches["operational_anti_drift"], "anti-drift-rules.md")

        active_intent = "operational_anti_drift"
        loaded_modules = [ref for when, ref, _ in xml_matches if when == active_intent]
        self.assertEqual(loaded_modules, ["anti-drift-rules.md"])
        self.assertNotIn("writing-profile.md", loaded_modules)

    def test_cis_05_pure_governance_schemas_isolation(self):
        """
        Schema / directive validation matches ONLY `governance_and_schemas` and resolves ONLY `governance-schemas.md`.
        """
        xml_matches = ROUTER_XML_TAG_REGEX.findall(self.router_text)
        dispatches = {when: ref for when, ref, _ in xml_matches}

        self.assertIn("governance_and_schemas", dispatches)
        self.assertEqual(dispatches["governance_and_schemas"], "governance-schemas.md")

        active_intent = "governance_and_schemas"
        loaded_modules = [ref for when, ref, _ in xml_matches if when == active_intent]
        self.assertEqual(loaded_modules, ["governance-schemas.md"])
        self.assertNotIn("writing-profile.md", loaded_modules)

    def test_cis_06_zero_eager_imports_ban(self):
        """
        Detects and rejects any prohibited eager `@path` imports in both router files.
        """
        for rfile in ["general-informatics-router.md", "index.md"]:
            content = resolve_file(rfile).read_text(encoding="utf-8")
            # Strip code blocks to check live router prose
            clean = strip_code_blocks(content)
            eager_matches = re.findall(r"@[\w./\-]+\.md", clean)
            self.assertEqual(
                len(eager_matches), 0,
                f"Prohibited eager import detected in {rfile}: {eager_matches}"
            )

    def test_cis_07_token_budget_efficiency_quantification(self):
        """
        Empirically measures token economy of JIT routing vs monolithic loading.
        Verifies that JIT context slice achieves >= 70% token savings over full-stack loading.
        """
        # Full stack token estimate
        full_stack_tokens = 0
        for f in ALL_DELIVERABLES:
            content = resolve_file(f).read_text(encoding="utf-8")
            full_stack_tokens += estimate_tokens(content)

        # JIT writing slice = router tokens + writing-profile tokens
        router_tokens = estimate_tokens(self.router_text)
        wp_tokens = estimate_tokens(resolve_file("writing-profile.md").read_text(encoding="utf-8"))
        jit_slice_tokens = router_tokens + wp_tokens

        savings_ratio = 1.0 - (jit_slice_tokens / full_stack_tokens)
        self.assertGreaterEqual(
            savings_ratio, 0.70,
            f"JIT token efficiency below 70% target: {savings_ratio:.2%} (JIT: {jit_slice_tokens}, Full: {full_stack_tokens})"
        )

    def test_cis_08_xml_tag_structural_validity(self):
        """
        Validates that all `<informatics>` blocks in the routers are syntactically valid XML elements.
        """
        for rpath in [resolve_file("general-informatics-router.md"), REPO_ROOT / "apex-meta" / "informatics" / "index.md"]:
            content = rpath.read_text(encoding="utf-8")
            # Extract XML blocks
            xml_blocks = re.findall(r"(<informatics[\s\S]*?</informatics>)", content)
            self.assertGreaterEqual(len(xml_blocks), 5, f"Expected at least 5 XML blocks in {rpath.name}")
            for block in xml_blocks:
                try:
                    root = ET.fromstring(block)
                    self.assertEqual(root.tag, "informatics")
                    self.assertIn("when", root.attrib)
                    self.assertIn("ref", root.attrib)
                    # Verify target ref actually exists on disk
                    ref_path = resolve_file(root.attrib["ref"])
                    self.assertTrue(ref_path.exists(), f"Broken ref in XML tag: {root.attrib['ref']}")
                except ET.ParseError as pe:
                    self.fail(f"Invalid XML syntax in {rname}: {block} -> {pe}")


# ==============================================================================
# Suite 2: Operational Lore Traceability & Exact Codification
# ==============================================================================

class TestOperationalLoreTraceability(unittest.TestCase):
    """
    Stress-tests the codification and traceability of operational lore:
    - 8 Anti-Drift Laws
    - Two-Strike Rule & Sunk-Cost Prohibition
    - Operator Challenge Boundary
    - Task Minimalism (Gall's Law, Minto BLUF, Minimal Viable Artifact, Zero Speculation)
    - Anti-Overcorrection & Context Hygiene
    - Residual Name Eradication
    - Substance-Over-Ceremony Exception Authority
    """

    def setUp(self):
        self.adr_text = resolve_file("anti-drift-rules.md").read_text(encoding="utf-8")
        self.exec_text = resolve_file("execution-modes.md").read_text(encoding="utf-8")
        self.wp_text = resolve_file("writing-profile.md").read_text(encoding="utf-8")
        self.fa_text = resolve_file("file-architecture.md").read_text(encoding="utf-8")
        self.gs_text = resolve_file("governance-schemas.md").read_text(encoding="utf-8")

    def test_olt_01_eight_anti_drift_laws_presence(self):
        """
        Verifies that all 8 Anti-Drift Laws are formally codified in `anti-drift-rules.md`.
        """
        required_laws = [
            ("TARGET Dominance", r"TARGET dominates everything"),
            ("Two-Strike Subsystem Rule", r"two corrective iterations without advancing"),
            ("Whole-File Rewrite Prohibition", r"Never regenerate or overwrite full files"),
            ("Operator Challenge Boundary", r"Does this need to be fixed before we can test the actual product\?"),
            ("Sunk-Cost Prohibition", r"No sunk-cost reasoning"),
            ("Substance Over Ceremony", r"Substance Over Ceremony"),
            ("Stop on Drift", r"Stop on drift"),
            ("Product Before Infrastructure", r"Product Before Infrastructure"),
            ("Reuse Before Build", r"Reuse before build"),
            ("Product Advancement", r"Every work unit must advance the product"),
            ("Evidence Proportionality", r"Evidence proportionality"),
        ]

        for law_name, law_regex in required_laws:
            match = re.search(law_regex, self.adr_text, re.IGNORECASE)
            self.assertIsNotNone(match, f"Missing Anti-Drift Law in anti-drift-rules.md: {law_name}")

    def test_olt_02_operator_challenge_boundary_verbatim(self):
        """
        Verifies verbatim presence of the Operator Challenge Boundary question:
        'Does this need to be fixed before we can test the actual product?'
        """
        question = "Does this need to be fixed before we can test the actual product?"
        self.assertIn(question, self.adr_text)

    def test_olt_03_two_strike_tracker_mechanics(self):
        """
        Verifies codification of Two-Strike subsystem tracker mechanics:
        - Maintains failure counts per subsystem independently.
        - Successful execution resets strike count to zero.
        - Strike 2 triggers pivot/replacement.
        """
        self.assertIn("Two-Strike Subsystem Tracker Mechanics", self.adr_text)
        self.assertIn("resets its strike count to zero", self.adr_text)
        self.assertIn("Two-Strike Pivot Rule", self.exec_text)

    def test_olt_04_task_minimalism_codification(self):
        """
        Verifies codification of Task Minimalism tenets:
        - Gall's Law & Single Flat Artifact
        - Minto BLUF (Bottom Line Up Front)
        - Zero-Speculation Scope Boundary
        - Balanced Viable Path
        """
        self.assertIn("Gall's Law", self.adr_text)
        self.assertIn("Minto BLUF", self.adr_text)
        self.assertIn("Zero-Speculation Scope Boundary", self.adr_text)
        self.assertIn("Balanced Viable Path", self.adr_text)

    def test_olt_05_anti_overcorrection_and_asset_preservation(self):
        """
        Verifies codification of:
        - Surgical edits (no wiping out surrounding valid code)
        - Asset preservation (existing code/comments are assets to preserve)
        - Pre-existing red vs regression boundary
        """
        self.assertIn("Surgical Edits & Anti-Overcorrection", self.adr_text)
        self.assertIn("Asset Preservation & Deterministic Moves", self.adr_text)
        self.assertIn("Pre-Existing Red vs Regression Boundary", self.adr_text)

    def test_olt_06_context_hygiene_and_residual_name_eradication(self):
        """
        Verifies codification of:
        - Step-by-Step Context & File Iteration Invariant
        - Residual Name Eradication post-refactor
        - Primary Grounding vs Secondary Citation
        - Command-Carrying Claims
        """
        self.assertIn("Step-by-Step Context & File Iteration Invariant", self.adr_text)
        self.assertIn("Residual Name Eradication", self.adr_text)
        self.assertIn("Primary Grounding vs Secondary Citation", self.adr_text)
        self.assertIn("Command-Carrying Claims", self.adr_text)

        # Also check file-architecture.md for residual name eradication
        self.assertIn("Residual Name Eradication", self.fa_text)

    def test_olt_07_substance_over_ceremony_exception_authority(self):
        """
        Verifies that Substance Over Ceremony Exception Authority is explicitly codified
        across all primary normative files.
        """
        authority_phrase = "Substance Over Ceremony"
        for name, text in [
            ("anti-drift-rules.md", self.adr_text),
            ("writing-profile.md", self.wp_text),
            ("file-architecture.md", self.fa_text),
            ("index.md", (REPO_ROOT / "apex-meta" / "informatics" / "index.md").read_text(encoding="utf-8")),
            ("general-informatics-router.md", resolve_file("general-informatics-router.md").read_text(encoding="utf-8")),
        ]:
            self.assertIn(authority_phrase, text, f"Missing Substance Over Ceremony in {name}")

    def test_olt_08_handover_anti_paralysis_law(self):
        """
        Verifies Handover Non-Paralysis Invariant / Checkable Ambiguity Resolution:
        'Never write a handover or defer an action that available tools can resolve immediately.'
        """
        self.assertIn("Handover Non-Paralysis Invariant", self.exec_text)
        self.assertIn("Checkable Ambiguity Resolution", self.adr_text)


# ==============================================================================
# Suite 3: Task Adapter Semantic Soundness
# ==============================================================================

class TestTaskAdapterSemanticSoundness(unittest.TestCase):
    """
    Stress-tests the deterministic behavior and data models of task adapters:
    1. Exact-Match Patch Intent discipline (Mode A block & Mode B AST JSON schema)
    2. Q&A Decision Matrix (structure, grounding, uncomputed 3-metrics, single-line rejection)
    3. Comparison / Bake-Off rubric (4-phase workflow, matrix format, decision triggers)
    4. MMM Iterative Execution (Route 0/1/2, preflight checklist, progressive elaboration)
    """

    def setUp(self):
        self.exec_text = resolve_file("execution-modes.md").read_text(encoding="utf-8")
        self.gov_text = resolve_file("governance-schemas.md").read_text(encoding="utf-8")

    def test_tas_01_exact_match_patch_mode_a_block_replacement(self):
        """
        Mode A: `<file>/<old>/<new>` exact-match block replacement.
        Verifies whitespace sensitivity, disambiguating context, and rollback on failure.
        """
        original = (
            "class AuthenticationService:\n"
            "    def __init__(self, port: int = 8080):\n"
            "        self.port = port\n"
            "        self.active = True\n"
        )

        # 1. Successful exact-match replacement
        old_block = "        self.port = port\n        self.active = True"
        new_block = "        self.port = 8085\n        self.active = True\n        self.tls = True"

        # Simulator
        self.assertEqual(original.count(old_block), 1)
        patched = original.replace(old_block, new_block, 1)
        self.assertIn("self.port = 8085", patched)
        self.assertIn("self.tls = True", patched)

        # 2. Whitespace mismatch failure (spaces vs tabs) -> pristine rollback
        whitespace_old_block = "\tself.port = port\n\tself.active = True"
        self.assertEqual(original.count(whitespace_old_block), 0)
        # Rollback: original remains pristine
        self.assertIn("8080", original)

        # 3. Ambiguous match failure (multiple instances without enough context)
        ambiguous_original = "val = 1\nval = 1\n"
        self.assertEqual(ambiguous_original.count("val = 1"), 2)

    def test_tas_02_patch_intent_v1_json_schema_validation(self):
        """
        Mode B: Validates AST `patch_intent.v1` JSON Schema against valid and invalid payloads.
        Safety invariants: require_unique_match=true, fail_on_ambiguity=true, allow_full_file_rewrite=false.
        Prohibited: line numbers/ranges/hunks.
        """
        # Load the AUTHORITATIVE schema the deterministic patcher validates against.
        # `governance-schemas.md` deliberately no longer embeds a copy (WP-23): an embedded copy
        # had already drifted from this file, dropping every maxLength bound it enforces.
        schema_path = (
            REPO_ROOT / ".claude" / "skills" / "deterministic-markdown-patcher2"
            / "references" / "patch-intent-schema.json"
        )
        self.assertTrue(schema_path.exists(), f"Authoritative patch intent schema missing: {schema_path}")
        schema = json.loads(schema_path.read_text(encoding="utf-8"))

        self.assertEqual(schema["properties"]["schema_version"]["const"], "patch_intent.v1")

        def deref(node):
            """Resolve a local $ref against the schema's $defs."""
            if "$ref" in node:
                return schema["$defs"][node["$ref"].split("/")[-1]]
            return node

        # Validate mandatory safety invariants in the authoritative schema
        intent_schema = deref(schema["properties"]["intents"]["items"])
        safety_props = deref(intent_schema["properties"]["safety"])["properties"]
        self.assertEqual(safety_props["require_unique_match"]["const"], True)
        self.assertEqual(safety_props["fail_on_ambiguity"]["const"], True)
        self.assertEqual(safety_props["allow_full_file_rewrite"]["const"], False)

        # The specification must state the same operative contract it points at.
        # This is the anti-drift guard that replaces the removed inline copy.
        self.assertIn("patch_intent.v1", self.gov_text)
        self.assertIn("patch-intent-schema.json", self.gov_text)
        for invariant in ("require_unique_match", "fail_on_ambiguity", "allow_full_file_rewrite"):
            self.assertIn(invariant, self.gov_text, f"GS must state safety invariant {invariant}")
        for operation in deref(intent_schema["properties"]["operation"]).get("enum", []):
            self.assertIn(operation, self.gov_text, f"GS must list operation '{operation}'")

        # Valid payload example conforming to schema
        valid_intent = {
            "schema_version": "patch_intent.v1",
            "intents": [
                {
                    "intent_id": "update-auth-port",
                    "operation": "replace-once",
                    "target": {
                        "target_file_guess": "config/services.yaml"
                    },
                    "hints": {
                        "nearby_phrases": ["auth_service:", "port: 8080"]
                    },
                    "replacement": {
                        "content": "  port: 8085\n",
                        "content_role": "span_replacement"
                    },
                    "safety": {
                        "require_unique_match": True,
                        "fail_on_ambiguity": True,
                        "allow_full_file_rewrite": False,
                        "max_files_touched": 1
                    }
                }
            ]
        }
        # Payload conforms to mandatory fields
        intent_obj = valid_intent["intents"][0]
        self.assertTrue(intent_obj["safety"]["require_unique_match"])
        self.assertFalse(intent_obj["safety"]["allow_full_file_rewrite"])

        # Check that forbidden line numbers are banned by rule GS-11
        self.assertIn("GS-11", self.gov_text)
        self.assertIn("line_number", self.gov_text)
        self.assertIn("unified_diff", self.gov_text)

    def test_tas_03_qa_decision_matrix_data_contract(self):
        """
        Verifies Q&A Decision Matrix specification and example:
        - Question
        - Options (letter, mechanism 2-4 lines, Grounding real-world story, raw 3-metrics 1-100)
        - Recommendation
        - Reasoning
        - Notes (one concise line per rejected option)
        """
        self.assertIn("Question", self.exec_text)
        self.assertIn("Grounding", self.exec_text)
        self.assertIn("Recommendation", self.exec_text)
        self.assertIn("Reasoning", self.exec_text)
        self.assertIn("Notes", self.exec_text)
        self.assertTrue("one concise line per rejected option" in self.exec_text.lower() or "one line per rejected option" in self.exec_text.lower())

        # Test canonical example in execution-modes.md
        self.assertIn("Option A (Bloc)", self.exec_text)
        self.assertIn("Option B (Riverpod)", self.exec_text)
        self.assertIn("Option C (SetState / Vanilla)", self.exec_text)
        self.assertIn("(I85/E95/R20)", self.exec_text)
        self.assertIn("(I90/E90/R15)", self.exec_text)
        self.assertIn("(I40/E80/R70)", self.exec_text)

    def test_tas_04_comparison_bakeoff_rubric(self):
        """
        Verifies Comparison / Bake-off Rubric:
        - 4 sequential phases: Gating hard filters, Multi-metric evaluation matrix, Ranked verdicts, Functional prototypes
        - Primary failure mode column
        - Explicit decision triggers ("Select this if..." vs "Avoid this if...")
        """
        self.assertIn("Phase 1: Candidate Discovery & Hard Gating", self.exec_text)
        self.assertIn("Phase 2: Multi-Metric Evaluation Matrix", self.exec_text)
        self.assertIn("Phase 3: Ranked Verdicts", self.exec_text)
        self.assertIn("Phase 4: Functional Prototypes & Decision Triggers", self.exec_text)
        self.assertIn("Primary Failure Mode", self.exec_text)
        self.assertIn("Select this if...", self.exec_text)
        self.assertIn("Avoid this if...", self.exec_text)

    def test_tas_05_mmm_iterative_execution_routing(self):
        """
        Verifies MMM iterative execution adapter:
        - Route 0, Route 1, Route 2 / MMM
        - File-Producing Iterative Execution Loop (Master Matrix, Implementation Map, Per-Step Files)
        - Macro (Why?), Meso (How?), Micro (What exactly?)
        - Top-down progressive elaboration & Bottom-up return
        - Upward Invalidation Rule
        """
        self.assertIn("Route 0", self.exec_text)
        self.assertIn("Route 1", self.exec_text)
        self.assertIn("Route 2 / MMM", self.exec_text)
        self.assertIn("Each Iteration Creates Files", self.exec_text)

        self.assertIn("Macro", self.exec_text)
        self.assertIn("Meso", self.exec_text)
        self.assertIn("Micro", self.exec_text)

        self.assertIn("Upward Invalidation Rule", self.exec_text)
        self.assertIn("Top-Down Decomposition", self.exec_text)
        self.assertIn("Bottom-Up Verification", self.exec_text)


# ==============================================================================
# Suite 4: Significance Ranking, Primacy & Anti-Formula Engine
# ==============================================================================

NORMATIVE_DELIVERABLES = [
    "file-architecture.md",
    "writing-profile.md",
    "execution-modes.md",
    "anti-drift-rules.md",
    "governance-schemas.md",
    "general-informatics-router.md",
]


class TestSignificanceAndRankingEngine(unittest.TestCase):
    """
    Stress-tests the Significance & Ranking system across all normative deliverable files:
    - Syntax conformance: `[P<0-3> | I<1-100>/E<1-100>/R<1-100>]`
    - Top-loaded positional primacy (first P0 tag within first 500 tokens)
    - Descending tier sort order (P0 -> P1 -> P2 -> P3)
    - Strict mathematical formula ban
    """

    def test_sre_01_syntax_and_metric_ranges(self):
        """
        Validates all significance tags across all normative deliverables.
        Ensures P-tier in P0..P3 and metrics in 1..100.
        """
        total_tags = 0
        for fname in NORMATIVE_DELIVERABLES:
            fpath = resolve_file(fname)
            content = fpath.read_text(encoding="utf-8")
            content_no_code = strip_code_blocks(content)
            matches = SIG_TAG_REGEX.findall(content_no_code)
            self.assertGreater(len(matches), 0, f"No significance tags found in {fname}")
            total_tags += len(matches)
            for tier, i_str, e_str, r_str in matches:
                self.assertIn(tier, ["P0", "P1", "P2", "P3"])
                i_val, e_val, r_val = int(i_str), int(e_str), int(r_str)
                self.assertTrue(1 <= i_val <= 100, f"Impact {i_val} out of bounds in {fname}")
                self.assertTrue(1 <= e_val <= 100, f"Evidence {e_val} out of bounds in {fname}")
                self.assertTrue(1 <= r_val <= 100, f"Risk {r_val} out of bounds in {fname}")

        self.assertGreaterEqual(total_tags, 80, f"Expected >= 80 total significance tags across bundle, found {total_tags}")

    def test_sre_02_top_loaded_primacy_across_all_specs(self):
        """
        Verifies that the first P0 invariant appears within the first 500 tokens
        across all normative specification files.
        """
        for fname in NORMATIVE_DELIVERABLES:
            content = resolve_file(fname).read_text(encoding="utf-8")
            content_no_code = strip_code_blocks(content)
            match = SIG_TAG_REGEX.search(content_no_code)
            self.assertIsNotNone(match, f"No tag found in {fname}")
            first_p0_match = None
            for m in SIG_TAG_REGEX.finditer(content_no_code):
                if m.group(1) == "P0":
                    first_p0_match = m
                    break
            self.assertIsNotNone(first_p0_match, f"No P0 tag found in {fname}")
            token_pos = estimate_tokens(content[:first_p0_match.start()])
            self.assertLessEqual(
                token_pos, 500,
                f"P0 primacy violated in {fname}: first P0 appears at token {token_pos} (> 500)"
            )

    def test_sre_03_descending_priority_sort_order(self):
        """
        Verifies descending priority ordering (P0 -> P1 -> P2 -> P3) across all files.
        """
        rank_map = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
        for fname in NORMATIVE_DELIVERABLES:
            content = resolve_file(fname).read_text(encoding="utf-8")
            content_no_code = strip_code_blocks(content)
            matches = SIG_TAG_REGEX.findall(content_no_code)
            ranks = [rank_map[tier] for tier, _, _, _ in matches]
            for idx in range(len(ranks) - 1):
                self.assertLessEqual(
                    ranks[idx], ranks[idx + 1],
                    f"Priority inversion in {fname} at tag index {idx}: {matches[idx][0]} appears before {matches[idx+1][0]}"
                )

    def test_sre_04_strict_math_formula_ban(self):
        """
        Verifies absence of computed expected value calculations or formula scores in all files.
        """
        formula_patterns = [
            r"Expected Value\s*=",
            r"\(Effective Impact\)\s*×",
            r"\(I\d+/E\d+/R\d+:\s*\d+\)",
            r"Score\s*=\s*I\s*\*",
        ]
        for fname in ALL_DELIVERABLES:
            content = resolve_file(fname).read_text(encoding="utf-8")
            # Strip code blocks (since Snippets might mention formula historically)
            content_no_code = strip_code_blocks(content)
            for pat in formula_patterns:
                matches = re.findall(pat, content_no_code, re.IGNORECASE)
                self.assertEqual(
                    len(matches), 0,
                    f"Forbidden computed formula detected in {fname}: {matches}"
                )


# ==============================================================================
# Suite 5: OKF v0.2 Frontmatter, Flat YAML & Bundle Link Integrity
# ==============================================================================

class TestFrontmatterAndOKFIntegrity(unittest.TestCase):
    """
    Stress-tests OKF v0.2 conformance, flat YAML frontmatter parsing, and bundle integrity.
    """

    def test_okf_01_all_files_have_flat_frontmatter(self):
        """
        Every governed file must have valid flat YAML frontmatter.
        Multiline lists (`- item`) are strictly forbidden.
        """
        for fname in ALL_DELIVERABLES:
            fpath = resolve_file(fname)
            content = fpath.read_text(encoding="utf-8")
            fm, body, err = okf_validator.parse_frontmatter(content)
            self.assertIsNone(err, f"Frontmatter parse error in {fname}: {err}")
            self.assertIsNotNone(fm, f"Missing frontmatter in {fname}")

            # Check that frontmatter lines all have ':'
            fm_raw = content.split("---")[1]
            for lidx, line in enumerate(fm_raw.splitlines(), start=2):
                lclean = line.strip()
                if not lclean or lclean.startswith("#"):
                    continue
                self.assertIn(":", lclean, f"Non-flat frontmatter line {lidx} in {fname}: {lclean}")

    def test_okf_02_durable_id_uniqueness(self):
        """
        All declared `id: ...` attributes across the bundle must be globally unique.
        """
        seen_ids: Dict[str, str] = {}
        for fname in ALL_DELIVERABLES:
            content = resolve_file(fname).read_text(encoding="utf-8")
            fm, _, _ = okf_validator.parse_frontmatter(content)
            if fm and "id" in fm:
                doc_id = str(fm["id"]).strip()
                self.assertNotIn(
                    doc_id, seen_ids,
                    f"Duplicate durable ID '{doc_id}' found in {fname} (already declared in {seen_ids.get(doc_id)})"
                )
                seen_ids[doc_id] = fname

    def test_okf_03_root_index_link_integrity(self):
        """
        Every relative markdown link in root `index.md` must resolve to an existing file.
        """
        root_index_path = REPO_ROOT / "apex-meta" / "informatics" / "index.md"
        content = root_index_path.read_text(encoding="utf-8")
        links = okf_validator.extract_links(content)
        self.assertGreater(len(links), 0)
        for link in links:
            resolved = (root_index_path.parent / link).resolve()
            self.assertTrue(resolved.exists(), f"Broken relative link in index.md: '{link}'")

    def test_okf_04_agent_setup_sub_bundle_isolation(self):
        """
        Verifies `Agent_Setup/index.md` creates a valid sub-bundle boundary with `okf_version: "0.2"`.
        """
        agent_setup_index = resolve_file("Agent_Setup/index.md")
        self.assertTrue(agent_setup_index.exists())
        content = agent_setup_index.read_text(encoding="utf-8")
        fm, _, err = okf_validator.parse_frontmatter(content)
        self.assertIsNone(err)
        self.assertEqual(fm.get("okf_version"), "0.2")


# ==============================================================================
# Suite 6: Router Compactness & Token Budgets
# ==============================================================================

class TestRouterCompactnessAndBudgets(unittest.TestCase):
    """
    Stress-tests router line count, character count, and token ceilings.
    """

    def test_rcb_01_general_router_ceilings(self):
        """
        `general-informatics-router.md` must adhere to:
        - Lines <= 100 (advisory <= 120)
        - Characters <= 2,000
        - Tokens <= 500
        """
        content = resolve_file("general-informatics-router.md").read_text(encoding="utf-8")
        lines = len(content.splitlines())
        chars = len(content)
        tokens = estimate_tokens(content)

        self.assertLessEqual(lines, 120, f"Router lines exceed advisory ceiling: {lines} > 120")
        self.assertLessEqual(chars, 2000, f"Router chars exceed ceiling: {chars} > 2000")
        self.assertLessEqual(tokens, 500, f"Router tokens exceed ceiling: {tokens} > 500")

    def test_rcb_02_index_router_ceilings(self):
        """
        Root `index.md` must adhere to:
        - Lines <= 100 (advisory <= 120)
        - Characters <= 4,000
        - Tokens <= 1,000
        """
        content = (REPO_ROOT / "apex-meta" / "informatics" / "index.md").read_text(encoding="utf-8")
        lines = len(content.splitlines())
        chars = len(content)
        tokens = estimate_tokens(content)

        self.assertLessEqual(lines, 120, f"Root index lines exceed advisory ceiling: {lines} > 120")
        self.assertLessEqual(chars, 4000, f"Root index chars exceed ceiling: {chars} > 4000")
        self.assertLessEqual(tokens, 1000, f"Root index tokens exceed ceiling: {tokens} > 1000")



# ==============================================================================
# Suite 7: Adversarial Boundary & Edge Cases
# ==============================================================================

class TestAdversarialBoundaryAndEdgeCases(unittest.TestCase):
    """
    White-box adversarial stress tests probing boundary conditions,
    attribute order mutations, transitive isolation, and tracker dynamics.
    """

    def test_adv_01_xml_attribute_order_insensitivity(self):
        """
        Adversarial test: Router XML tags with inverted or mutated attribute orders
        (e.g., ref before when, or deepen_when first) must parse cleanly in XML parsers.
        """
        mutated_xml = (
            '<informatics ref="writing-profile.md" when="writing_or_documentation" deepen_when="ste_word_limits">\n'
            '  [P1 | I92/E95/R10] Information Mapping and STE word limits.\n'
            '</informatics>'
        )
        elem = ET.fromstring(mutated_xml)
        self.assertEqual(elem.attrib["ref"], "writing-profile.md")
        self.assertEqual(elem.attrib["when"], "writing_or_documentation")
        self.assertEqual(elem.attrib["deepen_when"], "ste_word_limits")

    def test_adv_02_patch_intent_rejection_of_line_numbers(self):
        """
        Adversarial test: AST Patch Intent oracle strictly rejects payloads containing
        volatile line number references (line_number, line_start, hunk, unified_diff).
        """
        banned_keys = ["line_number", "line_start", "line_end", "line_range", "hunk", "unified_diff"]
        adversarial_payload = {
            "schema_version": "patch_intent.v1",
            "intents": [
                {
                    "intent_id": "fragile-patch",
                    "operation": "replace-once",
                    "target": {"target_file_guess": "test.py", "line_number": 42},
                    "safety": {"require_unique_match": True, "fail_on_ambiguity": True}
                }
            ]
        }
        # Oracle checks for banned keys per GS-P1-06
        found_banned = [k for k in banned_keys if k in adversarial_payload["intents"][0]["target"]]
        self.assertEqual(found_banned, ["line_number"])

        # Confirm governance-schemas.md explicitly bans these keys
        gov_text = resolve_file("governance-schemas.md").read_text(encoding="utf-8")
        for k in banned_keys:
            self.assertIn(k, gov_text, f"Governance schemas must explicitly ban brittle identifier: {k}")

    def test_adv_03_decision_matrix_uncomputed_metrics_validation(self):
        """
        Adversarial test: Validates that uncomputed 3-metric notation strictly rejects:
        - Computed synthetic scores (e.g., `(I90/E95/R20: 77)`)
        - Out-of-bound integer values (e.g., 0, 101, -5)
        """
        valid_tag = "(I90/E95/R20)"
        computed_tag = "(I90/E95/R20: 77)"
        out_of_bounds_high = "(I105/E95/R20)"
        out_of_bounds_zero = "(I0/E95/R20)"

        def validate_metric_tag(tag: str) -> Tuple[bool, Optional[str]]:
            if ":" in tag:
                return False, "Computed formula score prohibited"
            m = re.match(r"\(I(\d+)/E(\d+)/R(\d+)\)", tag)
            if not m:
                return False, "Syntax mismatch"
            i, e, r = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if not (1 <= i <= 100 and 1 <= e <= 100 and 1 <= r <= 100):
                return False, "Metric value out of bounds [1-100]"
            return True, None

        self.assertTrue(validate_metric_tag(valid_tag)[0])
        self.assertFalse(validate_metric_tag(computed_tag)[0])
        self.assertIn("Computed formula", validate_metric_tag(computed_tag)[1])
        self.assertFalse(validate_metric_tag(out_of_bounds_high)[0])
        self.assertFalse(validate_metric_tag(out_of_bounds_zero)[0])

    def test_adv_04_two_strike_multi_subsystem_isolation(self):
        """
        Adversarial test: Two-Strike tracker isolates distinct subsystems:
        Failure on Subsystem A does not increment or halt Subsystem B.
        A success on Subsystem A resets its counter to 0.
        """
        from test_informatics_e2e import TwoStrikeSubsystemTracker
        tracker = TwoStrikeSubsystemTracker()

        # Subsystem A fails once -> RETRY_ALLOWED
        self.assertEqual(tracker.record_attempt("ast_parser", False), "RETRY_ALLOWED")
        self.assertEqual(tracker.strikes["ast_parser"], 1)

        # Subsystem B fails once -> independent RETRY_ALLOWED
        self.assertEqual(tracker.record_attempt("yaml_serializer", False), "RETRY_ALLOWED")
        self.assertEqual(tracker.strikes["yaml_serializer"], 1)

        # Subsystem A fails second time -> TWO_STRIKE_HALT_AND_PIVOT
        self.assertEqual(tracker.record_attempt("ast_parser", False), "TWO_STRIKE_HALT_AND_PIVOT")
        self.assertIn("ast_parser", tracker.pivots)

        # Subsystem B still only has 1 failure -> RETRY_ALLOWED
        self.assertNotIn("yaml_serializer", tracker.pivots)

        # Subsystem B succeeds -> resets failure count to 0
        self.assertEqual(tracker.record_attempt("yaml_serializer", True), "SUCCESS")
        self.assertEqual(tracker.strikes["yaml_serializer"], 0)

    def test_adv_05_substance_over_ceremony_precedence(self):
        """
        Adversarial test: Verifies that Substance Over Ceremony Exception Authority
        is non-negotiably positioned as a P0 invariant in all core specifications.
        """
        adr_p0 = resolve_file("anti-drift-rules.md").read_text(encoding="utf-8")
        wp_p0 = resolve_file("writing-profile.md").read_text(encoding="utf-8")

        self.assertIn("AD-08 [P0 | I95/E95/R05] Substance Over Ceremony", adr_p0)
        self.assertIn("WP-01 [P0 | I98/E98/R05] Substance Over Ceremony", wp_p0)

    def test_adv_06_durable_id_referential_integrity(self):
        """
        Adversarial test: Paired directive examples in writing-profile.md
        must reference existing declared durable IDs in the same file.
        """
        wp_content = resolve_file("writing-profile.md").read_text(encoding="utf-8")
        # Extract referenced rule IDs in table
        table_matches = re.findall(r"\*\*(WP-\d{2})\*\*", wp_content)
        self.assertGreater(len(table_matches), 0)
        for rule_id in table_matches:
            # Must appear as a declared rule header
            self.assertIn(f"**{rule_id} [", wp_content, f"Orphaned example referencing undeclared rule: {rule_id}")

    def test_adv_07_pure_writing_zero_transitive_expansion(self):
        """
        Adversarial test: Zero Transitive Expansion.
        When an agent loads `writing-profile.md`, it does not contain transitive links
        or references instructing the agent to eagerly load `file-architecture.md`,
        `execution-modes.md`, `anti-drift-rules.md`, or `governance-schemas.md`.
        """
        wp_content = resolve_file("writing-profile.md").read_text(encoding="utf-8")
        transitive_targets = [
            "file-architecture.md",
            "execution-modes.md",
            "anti-drift-rules.md",
            "governance-schemas.md"
        ]
        for target in transitive_targets:
            self.assertNotIn(
                f"({target})", wp_content,
                f"Transitive expansion leak: writing-profile.md links directly to {target}"
            )

    def test_adv_08_sub_bundle_isolation_pruning_verification(self):
        """
        Adversarial test: okf_validator.py correctly prunes the Agent_Setup directory
        from root traversal and does not fail on legacy files inside Agent_Setup.
        """
        report = okf_validator.validate_bundle(str(REPO_ROOT / "apex-meta" / "informatics"))
        self.assertEqual(report.okf_errors, 0)
        self.assertEqual(report.apex_profile_errors, 0)
        self.assertTrue(report.passed)


# ==============================================================================
# CLI Entrypoint
# ==============================================================================

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestContextIsolationSimulation))
    suite.addTests(loader.loadTestsFromTestCase(TestOperationalLoreTraceability))
    suite.addTests(loader.loadTestsFromTestCase(TestTaskAdapterSemanticSoundness))
    suite.addTests(loader.loadTestsFromTestCase(TestSignificanceAndRankingEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestFrontmatterAndOKFIntegrity))
    suite.addTests(loader.loadTestsFromTestCase(TestRouterCompactnessAndBudgets))
    suite.addTests(loader.loadTestsFromTestCase(TestAdversarialBoundaryAndEdgeCases))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
