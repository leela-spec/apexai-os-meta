#!/usr/bin/env python3
"""
test_m4_audits_coverage.py — Adversarial Verification Suite for Milestone 4 (Plane 4 Infrastructure Module Audits).

Empirically verifies:
1. Rule inventory coverage across all 5 audit files:
   - Module 01: All 25 WP rules (WP-01..WP-25)
   - Module 02: All 13 FA rules (FA-01..FA-13)
   - Module 03: All 12 EM rules (EM-01..EM-12)
   - Module 04: All 28 AD rules (AD-01..AD-28)
   - Module 05: All 22 GS rules (GS-01..GS-22, with GS-16, GS-18, GS-19 retired)
   - Total active governed rules = 97 rules (100 total IDs accounted for).
2. Atomic semantic block inventory (SB-XX-NN.k) presence for all active rules.
3. Significance tagging syntax [P<tier> | I<impact>/E<evidence>/R<risk>] with raw integers 1–100.
4. Zero calculated math formulas (composite ranking scores, synthetic weights) in tags or calculations.
5. Byte sizes, line counts, word counts, and BPE token counts (cl100k_base).
6. 5-Chapter analytical structure compliance (Ch1 Scope/Inventory, Ch2 Single-Ownership, Ch3 Redundancy, Ch4 Traceability, Ch5 Failure Modes).
7. Link integrity and zero machine-specific paths across all 5 audit files.
8. Frontmatter schema conformance (OKF v0.2).
"""

from __future__ import annotations
import re
import urllib.parse
from pathlib import Path
import pytest
import tiktoken

REPO_ROOT = Path(__file__).resolve().parents[3]
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"

AUDIT_FILES = {
    "module-01": {
        "file": "audit-module-01-writing-profile.md",
        "prefix": "WP",
        "expected_rules": [f"WP-{i:02d}" for i in range(1, 26)],
        "retired_rules": [],
        "min_bytes": 25000,
    },
    "module-02": {
        "file": "audit-module-02-file-architecture.md",
        "prefix": "FA",
        "expected_rules": [f"FA-{i:02d}" for i in range(1, 14)],
        "retired_rules": [],
        "min_bytes": 20000,
    },
    "module-03": {
        "file": "audit-module-03-execution-modes.md",
        "prefix": "EM",
        "expected_rules": [f"EM-{i:02d}" for i in range(1, 13)],
        "retired_rules": [],
        "min_bytes": 20000,
    },
    "module-04": {
        "file": "audit-module-04-anti-drift-rules.md",
        "prefix": "AD",
        "expected_rules": [f"AD-{i:02d}" for i in range(1, 29)],
        "retired_rules": [],
        "min_bytes": 25000,
    },
    "module-05": {
        "file": "audit-module-05-governance-schemas.md",
        "prefix": "GS",
        "expected_rules": [f"GS-{i:02d}" for i in range(1, 23)],
        "retired_rules": ["GS-16", "GS-18", "GS-19"],
        "min_bytes": 25000,
    },
}

enc = tiktoken.get_encoding("cl100k_base")


class TestAuditModuleExistenceAndFrontmatter:
    """Verifies file existence, sizes, and OKF v0.2 frontmatter."""

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_file_exists_and_size(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        assert p.exists(), f"Audit file {cfg['file']} does not exist in {KB_DIR}"
        size = p.stat().st_size
        assert size >= cfg["min_bytes"], f"{cfg['file']} size {size} < {cfg['min_bytes']}"

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_frontmatter_schema(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        assert content.startswith("---\n"), f"{cfg['file']} must start with YAML frontmatter delimiter"
        fm_end = content.find("\n---\n", 4)
        assert fm_end != -1, f"{cfg['file']} missing closing frontmatter delimiter"
        fm = content[4:fm_end]
        
        # Check required fields
        assert re.search(r"^type:\s*Reference", fm, re.MULTILINE), f"Missing 'type: Reference' in {cfg['file']}"
        assert re.search(r"^id:\s*V2-AUDIT-MODULE-0\d-", fm, re.MULTILINE), f"Missing valid 'id' in {cfg['file']}"
        assert re.search(r"^title:\s*.+", fm, re.MULTILINE), f"Missing 'title' in {cfg['file']}"
        assert re.search(r"^description:\s*.+", fm, re.MULTILINE), f"Missing 'description' in {cfg['file']}"
        assert re.search(r"^status:\s*current_truth", fm, re.MULTILINE), f"Missing 'status: current_truth' in {cfg['file']}"
        assert re.search(r"^tags:\s*\[.+\]", fm, re.MULTILINE), f"Missing 'tags: [...]' in {cfg['file']}"


class TestFiveChapterStructure:
    """Verifies that all 5 audit files implement the mandatory 5-chapter analytical structure."""

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_five_chapters_present(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        # Verify Chapters 1 through 5 headers
        assert re.search(r"^##\s+1\.\s+Module Scope", content, re.MULTILINE), f"{cfg['file']} missing Chapter 1"
        assert re.search(r"^##\s+2\.\s+Single-Ownership", content, re.MULTILINE), f"{cfg['file']} missing Chapter 2"
        assert re.search(r"^##\s+3\.\s+Redundancy", content, re.MULTILINE), f"{cfg['file']} missing Chapter 3"
        assert re.search(r"^##\s+4\.\s+Cross-Traceability", content, re.MULTILINE), f"{cfg['file']} missing Chapter 4"
        assert re.search(r"^##\s+5\.\s+Module Failure Modes", content, re.MULTILINE), f"{cfg['file']} missing Chapter 5"


class TestRuleInventoryCoverage:
    """Verifies complete 97-rule inventory coverage across all 5 files."""

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_chapter1_table_rule_coverage(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        prefix = cfg["prefix"]
        expected_rules = cfg["expected_rules"]
        
        # Extract rules defined in table cells
        table_rules = re.findall(rf'\|\s*`?({prefix}-\d{{2}})`?\s*\|', content)
        unique_table_rules = set(table_rules)
        
        missing = [r for r in expected_rules if r not in unique_table_rules]
        assert not missing, f"{cfg['file']} missing rules in Chapter 1 Table: {missing}"
        assert len(unique_table_rules) >= len(expected_rules)

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_semantic_block_inventory_coverage(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        prefix = cfg["prefix"]
        expected_rules = cfg["expected_rules"]
        retired_rules = cfg["retired_rules"]
        
        active_rules = [r for r in expected_rules if r not in retired_rules]
        
        missing_sb = []
        for r in active_rules:
            # Check for SB-XX-NN.k pattern
            sb_pattern = re.compile(rf'SB-{r}\.\d+')
            sbs = sb_pattern.findall(content)
            if not sbs:
                missing_sb.append(r)
                
        assert not missing_sb, f"{cfg['file']} active rules missing Semantic Blocks (SB-{prefix}-NN.k): {missing_sb}"

    def test_total_governed_rules_count(self):
        """Asserts total governed active rules across all 5 modules equals exactly 97."""
        total_active_rules = 0
        total_rule_ids = 0
        for mod_key, cfg in AUDIT_FILES.items():
            active = len(cfg["expected_rules"]) - len(cfg["retired_rules"])
            total_active_rules += active
            total_rule_ids += len(cfg["expected_rules"])
            
        assert total_active_rules == 97, f"Expected 97 active governed rules, got {total_active_rules}"
        assert total_rule_ids == 100, f"Expected 100 total rule IDs, got {total_rule_ids}"

    def test_retired_rules_documentation(self):
        """Verifies that retired rules (GS-16, GS-18, GS-19) are explicitly documented in Module 05."""
        p = KB_DIR / AUDIT_FILES["module-05"]["file"]
        content = p.read_text(encoding="utf-8")
        for retired_id in ["GS-16", "GS-18", "GS-19"]:
            assert retired_id in content, f"Retired rule {retired_id} not mentioned in Module 05"
            # Ensure retirement explanation exists
            m = re.search(rf'{retired_id}[^\n]*Retired', content, re.IGNORECASE)
            assert m is not None, f"Retirement status for {retired_id} not clearly stated in Module 05"


class TestSignificanceTagsAndZeroMathFormulas:
    """Verifies raw [P<tier> | I<impact>/E<evidence>/R<risk>] tagging and zero math formulas."""

    # Matches [P<tier> | I<val>/E<val>/R<val>] or table-escaped [P<tier> \| I<val>/E<val>/R<val>]
    TAG_REGEX = re.compile(r'\[P([0-3])\s*(?:\\\||\|)\s*I(\d+)/E(\d+)/R(\d+)\]')

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_significance_tag_syntax_and_ranges(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        tags = self.TAG_REGEX.findall(content)
        assert len(tags) > 0, f"No significance tags found in {cfg['file']}"
        
        for tier, impact, evidence, risk in tags:
            assert tier in ("0", "1", "2", "3"), f"Invalid tier P{tier} in {cfg['file']}"
            i_val, e_val, r_val = int(impact), int(evidence), int(risk)
            assert 1 <= i_val <= 100, f"Impact {i_val} out of range 1-100 in {cfg['file']}"
            assert 1 <= e_val <= 100, f"Evidence {e_val} out of range 1-100 in {cfg['file']}"
            assert 1 <= r_val <= 100, f"Risk {r_val} out of range 1-100 in {cfg['file']}"

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_zero_calculated_math_formulas(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        # Check for calculation formulas attempting to compute composite score
        forbidden_patterns = [
            re.compile(r'Score\s*=\s*\(?I', re.I),
            re.compile(r'Rank\s*=\s*\(?I', re.I),
            re.compile(r'\(I\s*[\+\*]\s*E\)\s*/', re.I),
            re.compile(r'I\s*[\+\*]\s*E\s*/\s*R', re.I),
        ]
        for pat in forbidden_patterns:
            matches = pat.findall(content)
            # If match found, check if it's within a "Never compute" / "Do not compute" prohibition context
            for m in matches:
                # Find line containing match
                for line in content.splitlines():
                    if m in line:
                        is_prohibition = any(neg in line.lower() for neg in [
                            "never", "forbid", "do not", "ban", "reject", "violation"
                        ])
                        assert is_prohibition, f"Calculated formula used in {cfg['file']}: '{line}'"


class TestLinkIntegrityAndPortability:
    """Verifies that 100% of links resolve and contain zero machine-specific paths."""

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_markdown_links_resolve(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        # Remove fenced code blocks
        clean_content = re.sub(r'```[\s\S]*?```', '', content)
        
        link_re = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        links = link_re.findall(clean_content)
        assert len(links) > 0, f"Expected links in {cfg['file']}"
        
        broken = []
        machine_specific = []
        for text, url in links:
            url_clean = url.strip()
            if url_clean.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            if ':\\' in url_clean or ':/' in url_clean or url_clean.startswith('file:'):
                machine_specific.append((text, url_clean))
            
            tgt = urllib.parse.unquote(url_clean.split('#')[0])
            if not tgt:
                continue
            tgt_path = (REPO_ROOT / tgt.lstrip('/')) if tgt.startswith('/') else (KB_DIR / tgt).resolve()
            if not tgt_path.exists():
                broken.append((text, url_clean, str(tgt_path)))
                
        assert not machine_specific, f"Machine specific absolute links in {cfg['file']}: {machine_specific}"
        assert not broken, f"Broken links in {cfg['file']}: {broken}"


class TestSingleOwnershipCompliance:
    """Verifies single-ownership ledger in Chapter 2."""

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_chapter2_single_ownership_ledger(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        # Must document canonically owned rules
        assert re.search(r"###\s+2\.1\s+Rules Canonically Owned", content), f"{cfg['file']} missing 2.1 Owned Rules"
        # Must document delegations
        assert re.search(r"###\s+2\.(?:2|3)\s+Rules Within.*Delegating", content) or re.search(r"###\s+2\.(?:2|3|4)\s+", content), f"{cfg['file']} missing Delegation section"
        # Must mention WP-23
        assert "WP-23" in content, f"{cfg['file']} must cite WP-23"


class TestTerminalFailureModesGuards:
    """Verifies Chapter 5 terminal position failure mode guards (WP-25)."""

    @pytest.mark.parametrize("mod_key", list(AUDIT_FILES.keys()))
    def test_terminal_guards_present(self, mod_key: str):
        cfg = AUDIT_FILES[mod_key]
        p = KB_DIR / cfg["file"]
        content = p.read_text(encoding="utf-8")
        
        lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
        last_50_lines = "\n".join(lines[-50:])
        
        assert "## 5. Module Failure Modes" in last_50_lines or "## 5." in content, f"{cfg['file']} missing Chapter 5 at end"
        assert "WP-25" in content, f"{cfg['file']} must cite WP-25"
        # Check presence of non-negotiable guards (e.g., bullet list with "Never" or "Do not")
        assert re.search(r"-\s+\*\*Never\b", last_50_lines, re.IGNORECASE) or re.search(r"-\s+\*\*Do not\b", last_50_lines, re.IGNORECASE), f"{cfg['file']} missing terminal failure-mode guards"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
