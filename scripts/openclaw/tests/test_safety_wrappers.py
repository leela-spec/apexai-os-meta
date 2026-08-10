from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
POWERSHELL = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
SCRIPT_WRAPPER = REPO_ROOT / "scripts" / "openclaw" / "run-script-safe.ps1"
GIT_WRAPPER = REPO_ROOT / "scripts" / "openclaw" / "git-safe.ps1"
COMMAND_WRAPPER = REPO_ROOT / "scripts" / "openclaw" / "run-command-safe.ps1"
GUARD_INSTALLER = REPO_ROOT / "scripts" / "openclaw" / "install-guards.ps1"
RUNTIME_INSTALLER = REPO_ROOT / "scripts" / "openclaw" / "install-openclaw-runtime.ps1"


class SafetyWrapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name).resolve()
        self.trusted = self.root / "trusted"
        self.work = self.root / "work"
        self.trusted.mkdir()
        self.work.mkdir()
        self.prompt = self.trusted / "prompt.md"
        self.prompt.write_text("prompt", encoding="utf-8")
        self.output = self.work / "script-output.txt"
        self.worker = self.trusted / "worker.ps1"
        self.worker.write_text(
            "param([string]$OutputPath, [string]$Value)\n"
            "Set-Content -LiteralPath $OutputPath -Value $Value -NoNewline\n",
            encoding="utf-8",
        )
        self.git_repo = self.work / "repo"
        self.git_repo.mkdir()
        subprocess.run(["git", "init", "-b", "main", str(self.git_repo)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.git_repo), "config", "user.email", "test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(self.git_repo), "config", "user.name", "APEX Test"], check=True)
        tracked = self.git_repo / "tracked.txt"
        tracked.write_text("initial\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.git_repo), "add", "tracked.txt"], check=True)
        subprocess.run(["git", "-C", str(self.git_repo), "commit", "-m", "initial"], check=True, capture_output=True)
        self.git_remote = self.root / "origin.git"
        subprocess.run(["git", "init", "--bare", "--initial-branch=main", str(self.git_remote)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.git_repo), "remote", "add", "origin", str(self.git_remote)], check=True)
        subprocess.run(["git", "-C", str(self.git_repo), "push", "-u", "origin", "main"], check=True, capture_output=True)
        self.request_path = self.root / "request.json"
        self.write_request()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def request(self) -> dict:
        return {
            "schema_version": "apex.execution-request/v2",
            "execution_id": "exec-wrapper-001",
            "idempotency_key": "wrapper-fixture-001",
            "origin": {"repo": str(self.git_repo), "workflow": "fixture", "step": "safe-wrapper"},
            "instruction": "apex-flow-executor",
            "provider": "none",
            "provider_settings": {
                "browser_profile": "none",
                "hostname": "none",
                "mode": "none",
                "model": "none",
                "reasoning_mode": "off",
                "session_policy": "none",
            },
            "prompt_ref": {
                "path": str(self.prompt),
                "sha256": hashlib.sha256(self.prompt.read_bytes()).hexdigest(),
            },
            "roots": [
                {"path": str(self.trusted), "mode": "read"},
                {"path": str(self.work), "mode": "read_write"},
            ],
            "grants": {
                "tools": ["exec"],
                "scripts": [{
                    "id": "worker",
                    "executable": POWERSHELL,
                    "executable_sha256": hashlib.sha256(Path(POWERSHELL).read_bytes()).hexdigest(),
                    "path": str(self.worker),
                    "sha256": hashlib.sha256(self.worker.read_bytes()).hexdigest(),
                    "argv": [str(self.output), "EXACT_ARG_OK"],
                }],
                "commands": [],
                "git": {
                    "repo": str(self.git_repo),
                    "remote": "origin",
                    "remote_url": str(self.git_remote),
                    "branch": "main",
                    "operations": ["status", "diff", "add", "commit", "push"],
                    "add_paths": [str(self.git_repo / "tracked.txt")],
                    "commit_message": "bounded update",
                },
            },
            "success_criteria": ["fixture succeeds"],
            "stop_conditions": ["authority mismatch"],
            "result_path": str(self.work / "evidence" / "result.md"),
            "evidence_dir": str(self.work / "evidence"),
        }

    def write_request(self, request: dict | None = None) -> None:
        self.request_path.write_text(json.dumps(request or self.request()), encoding="utf-8")

    def powershell(
        self, script: Path, *arguments: str, env_overrides: dict[str, str] | None = None
    ) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        if env_overrides:
            environment.update(env_overrides)
        return subprocess.run(
            [POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", str(script), *arguments],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=environment,
        )

    def test_declared_script_runs_with_exact_argv(self) -> None:
        result = self.powershell(SCRIPT_WRAPPER, "-RequestPath", str(self.request_path), "-ScriptId", "worker")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.output.read_text(encoding="utf-8"), "EXACT_ARG_OK")

    def test_undeclared_script_id_fails_closed(self) -> None:
        result = self.powershell(SCRIPT_WRAPPER, "-RequestPath", str(self.request_path), "-ScriptId", "other")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_script_identity_change_after_request_is_rejected(self) -> None:
        self.worker.write_text("Write-Output 'changed'\n", encoding="utf-8")
        result = self.powershell(SCRIPT_WRAPPER, "-RequestPath", str(self.request_path), "-ScriptId", "worker")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_validator_blocks_inline_execution_before_wrapper_runs(self) -> None:
        request = self.request()
        request["grants"]["scripts"][0]["argv"] = ["-Command", "Remove-Item anything"]
        self.write_request(request)
        result = self.powershell(SCRIPT_WRAPPER, "-RequestPath", str(self.request_path), "-ScriptId", "worker")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_declared_exact_argv_command_runs_by_id(self) -> None:
        where_exe = Path(r"C:\Windows\System32\where.exe")
        request = self.request()
        request["grants"]["commands"] = [{
            "id": "locate-powershell",
            "executable": str(where_exe),
            "executable_sha256": hashlib.sha256(where_exe.read_bytes()).hexdigest(),
            "argv": ["powershell.exe"],
        }]
        self.write_request(request)
        result = self.powershell(
            COMMAND_WRAPPER, "-RequestPath", str(self.request_path),
            "-CommandId", "locate-powershell",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("powershell.exe", result.stdout.lower())

    def test_undeclared_command_id_fails_closed(self) -> None:
        result = self.powershell(
            COMMAND_WRAPPER, "-RequestPath", str(self.request_path), "-CommandId", "other"
        )
        self.assertNotEqual(result.returncode, 0)

    def test_git_status_and_diff_are_bounded(self) -> None:
        (self.git_repo / "tracked.txt").write_text("changed\n", encoding="utf-8")
        status = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "status")
        diff = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "diff")
        self.assertEqual(status.returncode, 0, status.stdout + status.stderr)
        self.assertIn("tracked.txt", status.stdout)
        self.assertEqual(diff.returncode, 0, diff.stdout + diff.stderr)
        self.assertIn("changed", diff.stdout)

    def test_git_add_and_commit_use_only_declared_path_and_message(self) -> None:
        (self.git_repo / "tracked.txt").write_text("changed\n", encoding="utf-8")
        add = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "add",
            "-Path", str(self.git_repo / "tracked.txt"),
        )
        commit = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "commit",
            "-Message", "bounded update",
        )
        self.assertEqual(add.returncode, 0, add.stdout + add.stderr)
        self.assertEqual(commit.returncode, 0, commit.stdout + commit.stderr)
        subject = subprocess.run(
            ["git", "-C", str(self.git_repo), "log", "-1", "--format=%s"],
            text=True, capture_output=True, check=True,
        ).stdout.strip()
        self.assertEqual(subject, "bounded update")

    def test_git_rejects_prohibited_operation_path_and_message(self) -> None:
        for operation in (
            "reset", "rebase", "filter-branch", "branch", "remote", "checkout", "switch",
            "push --force", "push --force-with-lease",
        ):
            rejected = self.powershell(
                GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", operation
            )
            self.assertNotEqual(rejected.returncode, 0, operation)
        outside = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "add",
            "-Path", str(self.root / "prompt.md"),
        )
        wrong_message = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "commit",
            "-Message", "widened",
        )
        self.assertNotEqual(outside.returncode, 0)
        self.assertNotEqual(wrong_message.returncode, 0)

    def test_git_push_is_fixed_to_origin_main(self) -> None:
        (self.git_repo / "tracked.txt").write_text("push fixture\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.git_repo), "add", "tracked.txt"], check=True)
        subprocess.run(["git", "-C", str(self.git_repo), "commit", "-m", "push fixture"], check=True, capture_output=True)
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "push")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        remote_subject = subprocess.run(
            ["git", "--git-dir", str(self.git_remote), "log", "-1", "--format=%s"],
            text=True, capture_output=True, check=True,
        ).stdout.strip()
        self.assertEqual(remote_subject, "push fixture")

    def test_git_commit_rejects_pre_staged_undeclared_path(self) -> None:
        undeclared = self.git_repo / "undeclared.txt"
        undeclared.write_text("must not commit\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.git_repo), "add", "undeclared.txt"], check=True)
        result = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "commit",
            "-Message", "bounded update",
        )
        self.assertNotEqual(result.returncode, 0)
        staged = subprocess.run(
            ["git", "-C", str(self.git_repo), "diff", "--cached", "--name-only"],
            text=True, capture_output=True, check=True,
        ).stdout
        self.assertIn("undeclared.txt", staged)

    def test_git_commit_rejects_rename_from_undeclared_source(self) -> None:
        secret = self.git_repo / "secret.txt"
        secret.write_text("secret\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.git_repo), "add", "secret.txt"], check=True)
        subprocess.run(["git", "-C", str(self.git_repo), "commit", "-m", "secret fixture"], check=True, capture_output=True)
        allowed_destination = self.git_repo / "allowed-new.txt"
        subprocess.run(
            ["git", "-C", str(self.git_repo), "mv", "secret.txt", allowed_destination.name], check=True
        )
        request = self.request()
        request["grants"]["git"]["add_paths"] = [str(allowed_destination)]
        self.write_request(request)
        result = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "commit",
            "-Message", "bounded update",
        )
        self.assertNotEqual(result.returncode, 0)

    def test_git_commit_disables_repository_hooks(self) -> None:
        marker = self.work / "hook-ran.txt"
        hook = self.git_repo / ".git" / "hooks" / "pre-commit"
        hook.write_text(f"#!/bin/sh\nprintf ran > '{marker.as_posix()}'\n", encoding="utf-8")
        (self.git_repo / "tracked.txt").write_text("hook fixture\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.git_repo), "add", "tracked.txt"], check=True)
        result = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "commit",
            "-Message", "bounded update",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(marker.exists())

    def test_git_push_disables_pre_push_hook(self) -> None:
        marker = self.work / "pre-push-ran.txt"
        hook = self.git_repo / ".git" / "hooks" / "pre-push"
        hook.write_text(f"#!/bin/sh\nprintf ran > '{marker.as_posix()}'\n", encoding="utf-8")
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "push")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(marker.exists())

    def test_git_rejects_executable_local_configuration(self) -> None:
        marker = self.work / "fsmonitor-ran.txt"
        monitor = self.work / "monitor.sh"
        monitor.write_text(f"#!/bin/sh\nprintf ran > '{marker.as_posix()}'\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(self.git_repo), "config", "core.fsmonitor", str(monitor)], check=True
        )
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "status")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(marker.exists())

    def test_git_rejects_url_rewrite_configuration(self) -> None:
        replacement = self.work / "rewrite.git"
        subprocess.run(["git", "init", "--bare", str(replacement)], check=True, capture_output=True)
        subprocess.run(
            ["git", "-C", str(self.git_repo), "config", f"url.{replacement}.insteadOf", str(self.git_remote)],
            check=True,
        )
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "push")
        self.assertNotEqual(result.returncode, 0)

    def test_git_clears_inherited_command_scope_configuration(self) -> None:
        marker = self.work / "injected-fsmonitor-ran.txt"
        monitor = self.work / "injected-monitor.sh"
        monitor.write_text(f"#!/bin/sh\nprintf ran > '{marker.as_posix()}'\n", encoding="utf-8")
        result = self.powershell(
            GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "status",
            env_overrides={
                "GIT_CONFIG_COUNT": "1",
                "GIT_CONFIG_KEY_0": "core.fsmonitor",
                "GIT_CONFIG_VALUE_0": str(monitor),
                "GIT_EXEC_PATH": str(self.work / "fake-git-exec"),
                "GIT_ASKPASS": str(monitor),
                "SSH_ASKPASS": str(monitor),
            },
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(marker.exists())

    def test_git_push_rejects_changed_remote_identity(self) -> None:
        replacement = self.work / "replacement.git"
        subprocess.run(["git", "init", "--bare", str(replacement)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.git_repo), "remote", "set-url", "origin", str(replacement)], check=True)
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "push")
        self.assertNotEqual(result.returncode, 0)

    def test_git_push_rejects_separate_pushurl(self) -> None:
        replacement = self.work / "pushurl-replacement.git"
        subprocess.run(["git", "init", "--bare", str(replacement)], check=True, capture_output=True)
        subprocess.run(
            ["git", "-C", str(self.git_repo), "remote", "set-url", "--add", "--push", "origin", str(replacement)],
            check=True,
        )
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "push")
        self.assertNotEqual(result.returncode, 0)

    def test_git_rejects_subdirectory_instead_of_worktree_root(self) -> None:
        subdir = self.git_repo / "subdir"
        subdir.mkdir()
        request = self.request()
        request["grants"]["git"]["repo"] = str(subdir)
        self.write_request(request)
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "status")
        self.assertNotEqual(result.returncode, 0)

    def test_git_rejects_non_main_branch(self) -> None:
        subprocess.run(["git", "-C", str(self.git_repo), "switch", "-c", "other"], check=True, capture_output=True)
        result = self.powershell(GIT_WRAPPER, "-RequestPath", str(self.request_path), "-Operation", "status")
        self.assertNotEqual(result.returncode, 0)


class GuardInstallerTests(unittest.TestCase):
    def test_installers_rescan_staging_before_hashing_or_promotion(self) -> None:
        guard_source = GUARD_INSTALLER.read_text(encoding="utf-8")
        self.assertLess(
            guard_source.index("Assert-NoReparseEntry -Path $copiedPath"),
            guard_source.index("Get-FileHash -Algorithm SHA256 -LiteralPath $copiedPath"),
        )

        runtime_source = RUNTIME_INSTALLER.read_text(encoding="utf-8")
        staged_scan = runtime_source.index("Assert-NoReparseTree -Path (Join-Path $staging 'node_modules')")
        self.assertLess(staged_scan, runtime_source.index("$stagedPackage =", staged_scan))
        self.assertLess(staged_scan, runtime_source.index("$fileHashes = Get-RuntimeHashes", staged_scan))

    def test_runtime_installer_rejects_reparse_node_source(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            real_node = root / "real-node.exe"
            real_node.write_bytes(b"fixture-node")
            linked_node = root / "node.exe"
            try:
                linked_node.symlink_to(real_node)
            except OSError as exc:
                self.skipTest(f"symbolic links unavailable: {exc}")
            modules = root / "node_modules"
            openclaw = modules / "openclaw"
            openclaw.mkdir(parents=True)
            (openclaw / "openclaw.mjs").write_text("fixture", encoding="utf-8")
            (openclaw / "package.json").write_text(
                json.dumps({"name": "openclaw", "version": "2026.7.1-2"}), encoding="utf-8"
            )
            result = subprocess.run(
                [
                    POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                    "-File", str(RUNTIME_INSTALLER), "-NodePath", str(linked_node),
                    "-ModulesPath", str(modules), "-TargetPath", str(root / "runtime"), "-SkipAcl",
                ],
                cwd=REPO_ROOT, text=True, capture_output=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            combined = (result.stdout + result.stderr).lower()
            self.assertIn("reparse point", combined)
            self.assertIn(str(linked_node).lower(), combined.replace("\n", ""))

    def test_installs_versioned_hash_manifest_without_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            target = Path(tempdir) / "guards"
            result = subprocess.run(
                [
                    POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                    "-File", str(GUARD_INSTALLER), "-TargetPath", str(target), "-SkipAcl",
                ],
                cwd=REPO_ROOT, text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(result.stdout)
            installed = Path(payload["installed_path"])
            self.assertTrue(installed.is_dir())
            manifest = json.loads((installed / "guard-manifest.json").read_text(encoding="utf-8"))
            for name, expected_hash in manifest["files"].items():
                actual_hash = hashlib.sha256((installed / name).read_bytes()).hexdigest()
                self.assertEqual(actual_hash, expected_hash)

            second = subprocess.run(
                [
                    POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                    "-File", str(GUARD_INSTALLER), "-TargetPath", str(target), "-SkipAcl",
                ],
                cwd=REPO_ROOT, text=True, capture_output=True, check=False,
            )
            self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
            second_payload = json.loads(second.stdout)
            self.assertEqual(second_payload["installed_path"], payload["installed_path"])
            self.assertTrue(second_payload["already_existed"])

    def test_installs_complete_versioned_runtime_manifest_without_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            node = root / "source" / "node.exe"
            modules = root / "source" / "node_modules"
            openclaw = modules / "openclaw"
            dependency = modules / "fixture-dependency"
            openclaw.mkdir(parents=True)
            dependency.mkdir()
            node.write_bytes(b"fixture-node")
            (openclaw / "openclaw.mjs").write_text("fixture", encoding="utf-8")
            (openclaw / "package.json").write_text(
                json.dumps({"name": "openclaw", "version": "2026.7.1-2"}), encoding="utf-8"
            )
            (dependency / "index.js").write_text("dependency", encoding="utf-8")
            long_dependency = dependency / ("a" * 50) / ("b" * 50)
            long_dependency.mkdir(parents=True)
            (long_dependency / (("c" * 30) + ".map")).write_text("long-path", encoding="utf-8")
            target = root / "runtime"
            command = [
                POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                "-File", str(RUNTIME_INSTALLER), "-NodePath", str(node),
                "-ModulesPath", str(modules), "-TargetPath", str(target), "-SkipAcl",
            ]
            first = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            payload = json.loads(first.stdout)
            installed = Path(payload["installed_path"])
            manifest = json.loads((installed / "runtime-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["openclaw_version"], "2026.7.1-2")
            self.assertIn("node_modules/fixture-dependency/index.js", manifest["files"])
            for relative, expected_hash in manifest["files"].items():
                actual = hashlib.sha256((installed / Path(relative)).read_bytes()).hexdigest()
                self.assertEqual(actual, expected_hash)
            second = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
            self.assertTrue(json.loads(second.stdout)["already_existed"])
            (installed / "node_modules" / "injected.js").write_text("unmanifested", encoding="utf-8")
            third = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
            self.assertNotEqual(third.returncode, 0)
            self.assertIn("file set mismatch", (third.stdout + third.stderr).lower())


if __name__ == "__main__":
    unittest.main()
