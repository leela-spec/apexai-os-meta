"""
test_challenger_2_adversarial.py - Exhaustive Empirical Adversarial Challenge Suite
Challenger 2: Independent verification of all 4 defect cures from Iteration 1.

Targets:
1. ki-basis/scripts/hermes_telegram_intake.py: Zero private ports (:8010, :8082), community fallback.
2. ki-basis/compose.yaml: Exactly 10 volumes, all external: true, teardown destruction immunity.
3. ki-basis/docs/OPERATOR_RUNBOOKS_AND_TEMPLATES.md: Split Nginx templates, real service polling in start.ps1.
4. Cross-domain isolation & credential divergence invariance.
"""

import ast
import importlib.util
import json
import os
import re
import subprocess
from pathlib import Path
import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
KI_BASIS_DIR = REPO_ROOT / "ki-basis"
DOCS_DIR = KI_BASIS_DIR / "docs"

INTAKE_SCRIPT = KI_BASIS_DIR / "scripts" / "hermes_telegram_intake.py"
COMPOSE_FILE = KI_BASIS_DIR / "compose.yaml"
ENV_PRIVATE_FILE = KI_BASIS_DIR / ".env.private"
ENV_COMMUNITY_FILE = KI_BASIS_DIR / ".env.community"
RUNBOOK_DOC = DOCS_DIR / "OPERATOR_RUNBOOKS_AND_TEMPLATES.md"
ARCH_DOC = DOCS_DIR / "WORKSPACE_ISOLATION_ARCHITECTURE.md"
PRESERV_DOC = DOCS_DIR / "DOCKER_VOLUME_PRESERVATION_PLAN.md"


# =============================================================================
# 1. Target 1: Hermes Telegram Intake Deep Adversarial Stress
# =============================================================================
class TestTarget1IntakeScriptDeepAdversarial:
    """Adversarially probe hermes_telegram_intake.py for any lingering private ports or routing leaks."""

    def test_zero_occurrences_of_private_ports_in_entire_file(self):
        """Audit the raw text of hermes_telegram_intake.py: absolutely zero occurrences of 8010 or 8082."""
        content = INTAKE_SCRIPT.read_text(encoding="utf-8")
        assert "8010" not in content, "VULNERABILITY: Found private port 8010 in hermes_telegram_intake.py"
        assert "8082" not in content, "VULNERABILITY: Found private port 8082 in hermes_telegram_intake.py"
        assert "http://127.0.0.1:8010" not in content
        assert "http://127.0.0.1:8082" not in content

    def test_ast_inspection_get_base_urls_and_headers(self):
        """Parse Python AST to verify fallback constants and environment variable lookups."""
        tree = ast.parse(INTAKE_SCRIPT.read_text(encoding="utf-8"))
        
        string_constants = [
            node.value for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        ]
        
        # Check that no string contains private ports
        for s in string_constants:
            assert "8010" not in s, f"AST constant leaked port 8010: {s}"
            assert "8082" not in s, f"AST constant leaked port 8082: {s}"

        # Verify community defaults exist in constants
        assert "http://127.0.0.1:9010" in string_constants
        assert "http://127.0.0.1:9082" in string_constants
        assert "127.0.0.1:9082" in string_constants
        assert "COMMUNITY_PAPERLESS_URL" in string_constants
        assert "COMMUNITY_OPENPROJECT_URL" in string_constants
        assert "OPENPROJECT_HOST_HEADER" in string_constants

    def test_runtime_permutation_matrix(self, monkeypatch):
        """
        Execute get_base_urls() under all four environment permutations:
        1. Fully unconfigured & unreachable (must default to community ports 9010 & 9082)
        2. Container hostnames reachable (must return container hostnames)
        3. Standard PAPERLESS_URL / OPENPROJECT_URL set (must respect explicit vars)
        4. Custom COMMUNITY_* overrides set (must respect community overrides)
        """
        spec = importlib.util.spec_from_file_location("hermes_telegram_intake", str(INTAKE_SCRIPT))
        intake_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(intake_mod)

        # Permutation 1: Completely clean, host unreachable
        monkeypatch.delenv("PAPERLESS_URL", raising=False)
        monkeypatch.delenv("OPENPROJECT_URL", raising=False)
        monkeypatch.delenv("COMMUNITY_PAPERLESS_URL", raising=False)
        monkeypatch.delenv("COMMUNITY_OPENPROJECT_URL", raising=False)
        monkeypatch.setattr(intake_mod, "check_reachable", lambda h, p, timeout=1: False)

        p_url, op_url = intake_mod.get_base_urls()
        assert p_url == "http://127.0.0.1:9010", f"Unexpected paperless fallback: {p_url}"
        assert op_url == "http://127.0.0.1:9082", f"Unexpected openproject fallback: {op_url}"

        # Permutation 2: Containers reachable
        monkeypatch.setattr(intake_mod, "check_reachable", lambda h, p, timeout=1: True)
        p_url, op_url = intake_mod.get_base_urls()
        assert p_url == "http://paperless:8000"
        assert op_url == "http://openproject:80"

        # Permutation 3: Standard env vars set
        monkeypatch.setenv("PAPERLESS_URL", "http://custom-paperless:8000")
        monkeypatch.setenv("OPENPROJECT_URL", "http://custom-openproject:80")
        p_url, op_url = intake_mod.get_base_urls()
        assert p_url == "http://custom-paperless:8000"
        assert op_url == "http://custom-openproject:80"

        # Permutation 4: Custom COMMUNITY overrides when standard not set
        monkeypatch.delenv("PAPERLESS_URL", raising=False)
        monkeypatch.delenv("OPENPROJECT_URL", raising=False)
        monkeypatch.setenv("COMMUNITY_PAPERLESS_URL", "http://community-gateway:9010")
        monkeypatch.setenv("COMMUNITY_OPENPROJECT_URL", "http://community-gateway:9082")
        monkeypatch.setattr(intake_mod, "check_reachable", lambda h, p, timeout=1: False)
        p_url, op_url = intake_mod.get_base_urls()
        assert p_url == "http://community-gateway:9010"
        assert op_url == "http://community-gateway:9082"


# =============================================================================
# 2. Target 2: Root compose.yaml Volume Externalization & Teardown Immunity
# =============================================================================
class TestTarget2ComposeVolumesExternalDeepAdversarial:
    """Stress-test compose.yaml for complete data loss immunity under docker compose down -v."""

    EXPECTED_10_VOLUMES = [
        "postgres_data",
        "valkey_data",
        "firefly_upload",
        "paperless_data",
        "paperless_media",
        "paperless_export",
        "paperless_consume",
        "openproject_assets",
        "hermes_data",
        "hermes_workspaces",
    ]

    def test_root_compose_volume_count_and_external_attribute(self):
        """Verify root compose.yaml defines exactly 10 volumes, each marked external: true."""
        parsed = yaml.safe_load(COMPOSE_FILE.read_text(encoding="utf-8"))
        volumes = parsed.get("volumes", {})
        
        assert len(volumes) == 10, f"Expected exactly 10 volumes, found {len(volumes)}"
        assert sorted(list(volumes.keys())) == sorted(self.EXPECTED_10_VOLUMES)

        for name, cfg in volumes.items():
            assert cfg is not None, f"Volume {name} config is None"
            assert cfg.get("external") is True, f"Volume {name} missing 'external: true'"
            expected_vol_name = "${COMPOSE_PROJECT_NAME:-ki-basis}-" + name.replace("_", "-")
            assert cfg["name"] == expected_vol_name

    def test_docker_compose_config_validates_both_profiles(self):
        """Invoke `docker compose config` on compose.yaml with both .env files."""
        for env_file, proj_name in [(ENV_COMMUNITY_FILE, "ki-basis-community"), (ENV_PRIVATE_FILE, "ki-basis-private")]:
            res = subprocess.run(
                [
                    "docker", "compose",
                    "-p", proj_name,
                    "--env-file", str(env_file),
                    "-f", str(COMPOSE_FILE),
                    "config", "--format", "json"
                ],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT)
            )
            assert res.returncode == 0, f"docker compose config failed for {proj_name}: {res.stderr}"
            cfg = json.loads(res.stdout)
            
            # Confirm all 10 volumes are flagged as external in compose output
            compose_vols = cfg.get("volumes", {})
            assert len(compose_vols) == 10
            for vname, vmeta in compose_vols.items():
                assert vmeta.get("external") is True, f"Resolved volume {vname} not external in {proj_name}"
                assert vmeta.get("name").startswith(f"{proj_name}-")

    def test_service_volume_mounts_strictly_bound_to_external_volumes(self):
        """Verify that every service's volume mounts use named external volumes or read-only configs."""
        parsed = yaml.safe_load(COMPOSE_FILE.read_text(encoding="utf-8"))
        external_vol_names = set(parsed.get("volumes", {}).keys())
        
        for sname, scfg in parsed.get("services", {}).items():
            for m in scfg.get("volumes", []):
                if isinstance(m, str):
                    host_part, _, opts = m.partition(":")
                    if host_part in external_vol_names:
                        # Valid named external volume
                        continue
                    elif host_part.startswith("./"):
                        # Host path: must be read-only configuration
                        assert ":ro" in m or opts == "ro", f"Service {sname} mounts host path writeable: {m}"
                    else:
                        pytest.fail(f"Service {sname} has unexpected volume mount: {m}")


# =============================================================================
# 3. Target 3: Dedicated Nginx Templates & start.ps1 Real Backend Polling
# =============================================================================
class TestTarget3OperatorRunbooksAndNginxDeepAdversarial:
    """Stress-test runbook templates for strict reverse-proxy isolation and real healthcheck polling."""

    def test_community_nginx_template_isolation(self):
        """Verify lika-community/docker/nginx/default.conf contains only Band 908x ports."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        # Extract Section 2.5 Nginx block
        match = re.search(
            r"### 2\.5 Edge Proxy Specification: `lika-community/docker/nginx/default\.conf`[\s\S]*?```nginx([\s\S]*?)```",
            content
        )
        assert match, "Section 2.5 Nginx block not found in runbook"
        nginx_conf = match.group(1)

        # Must contain community ports
        for p in ["9082", "9010", "9086", "9219", "9642"]:
            assert p in nginx_conf, f"Community Nginx config missing community port {p}"

        # Must NOT contain any private ports
        for p in ["8082", "8010", "8086", "9119", "8642"]:
            assert p not in nginx_conf, f"VULNERABILITY: Community Nginx config contains private port {p}"

    def test_private_nginx_template_isolation(self):
        """Verify private-business/docker/nginx/default.conf contains only Band 808x ports."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        # Extract Section 3.6 Nginx block
        match = re.search(
            r"### 3\.6 Edge Proxy Specification: `private-business/docker/nginx/default\.conf`[\s\S]*?```nginx([\s\S]*?)```",
            content
        )
        assert match, "Section 3.6 Nginx block not found in runbook"
        nginx_conf = match.group(1)

        # Must contain private ports
        for p in ["8082", "8010", "8086", "9119", "8642"]:
            assert p in nginx_conf, f"Private Nginx config missing private port {p}"

        # Must NOT contain any community ports
        for p in ["9082", "9010", "9086", "9219", "9642"]:
            assert p not in nginx_conf, f"VULNERABILITY: Private Nginx config contains community port {p}"

    def test_community_start_ps1_service_polling_logic(self):
        """Verify Community start.ps1 polls real applications (Paperless & OpenProject)."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        match = re.search(
            r"### 2\.3 1-Click Startup Runbook: `lika-community/scripts/start\.ps1`[\s\S]*?```powershell([\s\S]*?)```",
            content
        )
        assert match, "Community start.ps1 block not found in runbook"
        script = match.group(1)

        # Must poll real services
        assert "http://127.0.0.1:9010" in script, "start.ps1 does not poll Paperless on 9010"
        assert "http://127.0.0.1:9082" in script, "start.ps1 does not poll OpenProject on 9082"
        assert "http://127.0.0.1:9084/healthz" in script, "start.ps1 does not poll Nginx edge proxy"

        # Must verify status codes
        assert "StatusCode -in 200, 301, 302" in script
        assert "Start-Sleep -Seconds 3" in script

    def test_private_start_ps1_service_polling_logic(self):
        """Verify Private start.ps1 polls real applications (Paperless & OpenProject)."""
        content = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        match = re.search(
            r"### 3\.4 1-Click Startup Runbook: `private-business/scripts/start\.ps1`[\s\S]*?```powershell([\s\S]*?)```",
            content
        )
        assert match, "Private start.ps1 block not found in runbook"
        script = match.group(1)

        # Must poll real services
        assert "http://127.0.0.1:8010" in script, "start.ps1 does not poll Paperless on 8010"
        assert "http://127.0.0.1:8082" in script, "start.ps1 does not poll OpenProject on 8082"
        assert "http://127.0.0.1:8084/healthz" in script, "start.ps1 does not poll Nginx edge proxy"

        # Must verify status codes
        assert "StatusCode -in 200, 301, 302" in script
        assert "Start-Sleep -Seconds 3" in script


# =============================================================================
# 4. Cross-Domain Isolation & Cryptographic Invariance
# =============================================================================
class TestCrossDomainIsolationStress:
    """Stress-test environment configs for complete credential divergence and Telegram fences."""

    def test_credentials_entropy_and_complete_disjointedness(self):
        """Ensure no secrets or database credentials are shared between Private and Community."""
        def load_env(env_path):
            env_vars = {}
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()
            return env_vars

        pvt = load_env(ENV_PRIVATE_FILE)
        comm = load_env(ENV_COMMUNITY_FILE)

        sensitive_keys = [
            "POSTGRES_PASSWORD",
            "FIREFLY_DB_PASSWORD",
            "FIREFLY_APP_KEY",
            "PAPERLESS_DB_PASSWORD",
            "PAPERLESS_SECRET_KEY",
            "PAPERLESS_ADMIN_PASSWORD",
            "OPENPROJECT_DB_PASSWORD",
            "OPENPROJECT_SECRET_KEY_BASE",
            "HERMES_DASHBOARD_BASIC_AUTH_PASSWORD",
            "HERMES_API_SERVER_KEY"
        ]

        for k in sensitive_keys:
            assert k in pvt, f"Missing key {k} in .env.private"
            assert k in comm, f"Missing key {k} in .env.community"
            assert pvt[k] != comm[k], f"SECURITY CRITICAL: Shared secret between environments for {k}!"
            assert len(pvt[k]) >= 16, f"Secret {k} too short in private (<16 chars)"
            assert len(comm[k]) >= 16, f"Secret {k} too short in community (<16 chars)"

    def test_telegram_policy_enforcement(self):
        """Private must have Telegram disabled; Community must have Telegram configured."""
        runbook = RUNBOOK_DOC.read_text(encoding="utf-8")
        
        # Private compose template must disable telegram
        pvt_compose = re.search(r"### 3\.3 Docker Compose Specification: `private-business/compose\.yaml`[\s\S]*?```yaml([\s\S]*?)```", runbook).group(1)
        assert 'TELEGRAM_BOT_TOKEN: ""' in pvt_compose or "TELEGRAM_BOT_TOKEN: ''" in pvt_compose

        # Community compose template must expose telegram config
        comm_compose = re.search(r"### 2\.2 Docker Compose Specification: `lika-community/compose\.yaml`[\s\S]*?```yaml([\s\S]*?)```", runbook).group(1)
        assert 'TELEGRAM_BOT_TOKEN: ${TELEGRAM_BOT_TOKEN:-}' in comm_compose
        assert 'TELEGRAM_GROUP_ALLOWED_CHATS: "${TELEGRAM_GROUP_ALLOWED_CHATS:--1004343753692}"' in comm_compose
