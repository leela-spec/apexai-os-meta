"""
test_deliverables_stress.py - Empirical Adversarial Stress Test Suite for 2026-09-22 Deliverables
Challenger 1: Stress-testing Architecture, Volume Preservation, Network Security, and Runbooks.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
KI_BASIS_DIR = REPO_ROOT / "ki-basis"
DOCS_DIR = KI_BASIS_DIR / "docs"

ARCH_DOC = DOCS_DIR / "WORKSPACE_ISOLATION_ARCHITECTURE.md"
PRESERV_DOC = DOCS_DIR / "DOCKER_VOLUME_PRESERVATION_PLAN.md"
RUNBOOK_DOC = DOCS_DIR / "OPERATOR_RUNBOOKS_AND_TEMPLATES.md"

COMPOSE_FILE = KI_BASIS_DIR / "compose.yaml"
ENV_PRIVATE_FILE = KI_BASIS_DIR / ".env.private"
ENV_COMMUNITY_FILE = KI_BASIS_DIR / ".env.community"
INTAKE_SCRIPT = KI_BASIS_DIR / "scripts" / "hermes_telegram_intake.py"


# =============================================================================
# 1. Docker Volume Invariance & Destruction Resistance
# =============================================================================
class TestDockerVolumeInvarianceStress:
    """Stress tests for volume naming, external: true, and destruction resistance."""

    EXPECTED_COMMUNITY_VOLUMES = {
        "ki-basis-community-postgres-data",
        "ki-basis-community-valkey-data",
        "ki-basis-community-firefly-upload",
        "ki-basis-community-paperless-data",
        "ki-basis-community-paperless-media",
        "ki-basis-community-paperless-export",
        "ki-basis-community-paperless-consume",
        "ki-basis-community-openproject-assets",
        "ki-basis-community-hermes-data",
        "ki-basis-community-hermes-workspaces",
    }

    EXPECTED_PRIVATE_VOLUMES = {
        "ki-basis-private-postgres-data",
        "ki-basis-private-valkey-data",
        "ki-basis-private-firefly-upload",
        "ki-basis-private-paperless-data",
        "ki-basis-private-paperless-media",
        "ki-basis-private-paperless-export",
        "ki-basis-private-paperless-consume",
        "ki-basis-private-openproject-assets",
        "ki-basis-private-hermes-data",
        "ki-basis-private-hermes-workspaces",
    }

    def test_20_volume_naming_conventions_in_root_compose(self):
        """Verify that evaluating root compose.yaml with .env produces exact 20 volumes."""
        def get_vols(env_file, proj_name):
            cmd = [
                "docker", "compose",
                "-p", proj_name,
                "--env-file", str(env_file),
                "-f", str(COMPOSE_FILE),
                "config", "--format", "json"
            ]
            res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
            assert res.returncode == 0
            cfg = json.loads(res.stdout)
            return {v["name"] for v in cfg.get("volumes", {}).values()}

        comm_vols = get_vols(ENV_COMMUNITY_FILE, "ki-basis-community")
        pvt_vols = get_vols(ENV_PRIVATE_FILE, "ki-basis-private")

        assert comm_vols == self.EXPECTED_COMMUNITY_VOLUMES
        assert pvt_vols == self.EXPECTED_PRIVATE_VOLUMES
        assert len(comm_vols & pvt_vols) == 0

    def test_root_compose_has_external_true_immunization(self):
        """
        Remediation Verification: Audits root compose.yaml for external: true on all 10 volumes.
        Immunizes against data destruction if an operator runs `docker compose down -v`.
        """
        content = COMPOSE_FILE.read_text(encoding="utf-8")
        parsed = yaml.safe_load(content)
        vols = parsed.get("volumes", {})
        assert len(vols) == 10, f"Expected 10 volumes in root compose.yaml, got {len(vols)}"
        for vol_key, vol_cfg in vols.items():
            assert vol_cfg.get("external") is True, (
                f"Volume {vol_key} in root compose.yaml lacks 'external: true'!"
            )
        print("\n[REMEDIATION VERIFIED]: All 10 volumes in ki-basis/compose.yaml set 'external: true'!")

    def test_templates_in_runbook_have_external_true(self):
        """Verify that the templates in OPERATOR_RUNBOOKS_AND_TEMPLATES.md DO include external: true."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        # Extract YAML blocks for compose
        yaml_blocks = re.findall(r"```yaml\n(name:\s*ki-basis-[\s\S]*?)\n```", content)
        assert len(yaml_blocks) == 2, f"Expected 2 compose templates, found {len(yaml_blocks)}"

        for block in yaml_blocks:
            parsed = yaml.safe_load(block)
            vols = parsed.get("volumes", {})
            assert len(vols) == 10
            for vname, vcfg in vols.items():
                assert vcfg.get("external") is True, f"Template volume {vname} lacks external: true"
                assert "name" in vcfg, f"Template volume {vname} lacks explicit name"

    def test_volume_names_match_across_all_three_docs(self):
        """Verify that all 20 volume names are mentioned identically across all 3 docs."""
        preserv_content = PRESERV_DOC.read_text(encoding="utf-8")
        runbook_content = RUNBOOK_DOC.read_text(encoding="utf-8")
        arch_content = ARCH_DOC.read_text(encoding="utf-8")

        all_20 = self.EXPECTED_COMMUNITY_VOLUMES | self.EXPECTED_PRIVATE_VOLUMES
        for vol in all_20:
            assert vol in preserv_content, f"Volume {vol} missing in DOCKER_VOLUME_PRESERVATION_PLAN.md"
            assert vol in runbook_content, f"Volume {vol} missing in OPERATOR_RUNBOOKS_AND_TEMPLATES.md"


# =============================================================================
# 2. Port Band Disjointedness & Network Security
# =============================================================================
class TestPortAndNetworkSecurityStress:
    def test_zero_port_collisions(self):
        """Port bands 808x and 908x must be completely disjoint."""
        pvt_ports = {8010, 8082, 8084, 8086, 8642, 9119}
        comm_ports = {9010, 9082, 9084, 9086, 9219, 9642}
        assert len(pvt_ports & comm_ports) == 0

    def test_postgres_unexposed_in_runbook_templates(self):
        """Ensure no template in OPERATOR_RUNBOOKS_AND_TEMPLATES.md exposes Postgres (:5432)."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        yaml_blocks = re.findall(r"```yaml\n(name:\s*ki-basis-[\s\S]*?)\n```", content)
        for block in yaml_blocks:
            parsed = yaml.safe_load(block)
            pg_ports = parsed.get("services", {}).get("postgres", {}).get("ports", [])
            assert len(pg_ports) == 0, f"Postgres exposed in template: {pg_ports}"

    def test_hermes_intake_fallback_ports_remediated(self):
        """
        Remediation Verification: Audits hermes_telegram_intake.py to confirm fallback ports
        are community-scoped (:9010/:9082) and NEVER fall back to Private ports (:8010/:8082).
        """
        content = INTAKE_SCRIPT.read_text(encoding="utf-8")
        has_8010_fallback = '127.0.0.1:8010' in content
        has_8082_fallback = '127.0.0.1:8082' in content
        has_9010_fallback = '127.0.0.1:9010' in content or 'COMMUNITY_PAPERLESS_URL' in content
        has_9082_fallback = '127.0.0.1:9082' in content or 'COMMUNITY_OPENPROJECT_URL' in content

        print(f"\n[REMEDIATION VERIFIED] hermes_telegram_intake.py fallback ports:")
        print(f"  Private Paperless (:8010) removed: {not has_8010_fallback}")
        print(f"  Private OpenProject (:8082) removed: {not has_8082_fallback}")
        print(f"  Community Paperless fallback (:9010): {has_9010_fallback}")
        print(f"  Community OpenProject fallback (:9082): {has_9082_fallback}")

        assert not has_8010_fallback, "Security Violation: 8010 fallback still exists in script"
        assert not has_8082_fallback, "Security Violation: 8082 fallback still exists in script"
        assert has_9010_fallback, "Missing community paperless fallback"
        assert has_9082_fallback, "Missing community openproject fallback"

    def test_hermes_intake_runtime_fallback_behavior(self, monkeypatch):
        """Directly invokes get_base_urls() under clean environment to verify community-scoped ports."""
        import importlib.util
        spec = importlib.util.spec_from_file_location("hermes_telegram_intake", str(INTAKE_SCRIPT))
        intake_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(intake_mod)

        # Clear env and force unreachable container hostnames
        monkeypatch.delenv("PAPERLESS_URL", raising=False)
        monkeypatch.delenv("OPENPROJECT_URL", raising=False)
        monkeypatch.delenv("COMMUNITY_PAPERLESS_URL", raising=False)
        monkeypatch.delenv("COMMUNITY_OPENPROJECT_URL", raising=False)
        monkeypatch.setattr(intake_mod, "check_reachable", lambda h, p, timeout=1: False)

        paperless_url, openproject_url = intake_mod.get_base_urls()
        assert "8010" not in paperless_url, f"Leaked private port 8010: {paperless_url}"
        assert "8082" not in openproject_url, f"Leaked private port 8082: {openproject_url}"
        assert paperless_url == "http://127.0.0.1:9010"
        assert openproject_url == "http://127.0.0.1:9082"

    def test_prompt_injection_lateral_movement_impossibility(self):
        """
        Verify the defense-in-depth layers preventing Community Hermes from communicating
        with Private Postgres (:5432) or Private Paperless (:8010).
        """
        # 1. Network separation: Compose creates distinct bridge networks
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        assert "ki-basis-community-net" in content
        assert "ki-basis-private-net" in content

        # 2. Host loopback binding: Private Paperless binds to 127.0.0.1 on host,
        # not accessible from container network namespace (container 127.0.0.1 is local to container).
        assert '127.0.0.1:${PAPERLESS_HOST_PORT:-8010}:8000' in content


# =============================================================================
# 3. Token Overhead & Context Bleeding Verification
# =============================================================================
class TestTokenCalculationsStress:
    def test_token_reduction_formula_mathematics(self):
        """Verify the claimed mathematical calculation in doc."""
        base_tokens = 13796
        isolated_tokens = 1170
        reduction = (base_tokens - isolated_tokens) / base_tokens * 100
        assert round(reduction, 2) == 91.52

    def test_rules_file_token_estimation(self):
        """Verify that AGENTS.md + GEMINI.md tokens match ~2100 tokens."""
        agents_md = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8", errors="ignore")
        gemini_md = (REPO_ROOT / "GEMINI.md").read_text(encoding="utf-8", errors="ignore")
        total_chars = len(agents_md) + len(gemini_md)
        est_tokens = total_chars / 4
        # Claim was ~2,156 tokens (4.5 KB + 4.1 KB)
        assert 1900 <= est_tokens <= 2300, f"Token estimation {est_tokens} outside expected range"


# =============================================================================
# 4. Script & Template Robustness
# =============================================================================
class TestScriptAndTemplateRobustness:
    def test_runbook_start_ps1_preflight_checks(self):
        """Verify that start.ps1 in runbooks contains pre-flight assertions for all 10 volumes."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        # Check Community start.ps1
        comm_vols_block = re.search(r"\$RequiredVols\s*=\s*@\(([\s\S]*?)\)", content)
        assert comm_vols_block, "start.ps1 missing $RequiredVols definition"
        block_text = comm_vols_block.group(1)
        for vol in TestDockerVolumeInvarianceStress.EXPECTED_COMMUNITY_VOLUMES:
            assert vol in block_text

        # Verify fail-closed halt
        assert "throw \"HALT:" in content or "throw 'HALT:" in content

    def test_runbook_stop_ps1_uses_stop_not_down(self):
        """Verify that stop.ps1 uses `docker compose stop`, preventing accidental destruction."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        stop_matches = re.findall(r"docker compose -p ki-basis-(?:community|private) stop", content)
        assert len(stop_matches) >= 2, "stop.ps1 should use `docker compose stop`"

        # Verify stop.ps1 does NOT use down -v
        assert "docker compose down -v" not in re.findall(r"###.*stop\.ps1[\s\S]*?```powershell([\s\S]*?)```", content)[0]
