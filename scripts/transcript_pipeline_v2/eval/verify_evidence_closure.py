"""
Deterministic Evidence Closure Validator for V2.1 Trial 1.
Enforces raw-result-first evidence, observed execution receipts, hash integrity,
non-simulation verification, and hard gate satisfaction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CORRECTIVE_ROOT = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "corrective-run"
CANONICAL_ROOT = REPO_ROOT / "artifacts" / "transcript_pipeline_v2"

ALLOWED_TRIAL1_TRANSPORTS = {
    "claude_code",
    "claude_subscription_cli",
    "codex_cli",
    "codex_chatgpt_plan_cli",
    "antigravity_cli",
    "claude",
    "codex",
    "antigravity",
}

FORBIDDEN_TRANSPORTS = {
    "api_key_billing",
    "pay_as_you_go",
    "direct_anthropic_api",
    "direct_openai_api",
    "direct_gemini_api",
    "vertex_ai",
    "hosted_model_api",
    "browser_ai",
    "gemini_cli",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


class EvidenceClosureValidator:
    def __init__(self, run_root: Optional[Path] = None):
        self.run_root = run_root or CORRECTIVE_ROOT
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def log_error(self, msg: str):
        self.errors.append(msg)

    def log_warning(self, msg: str):
        self.warnings.append(msg)

    def validate_identity_receipt(self, receipt_path: Path, expected_component: str) -> bool:
        if not receipt_path.exists():
            self.log_error(f"Missing identity receipt for component '{expected_component}': {receipt_path}")
            return False

        try:
            with open(receipt_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            self.log_error(f"Malformed identity receipt {receipt_path}: {e}")
            return False

        if data.get("test_mode") == "mock" or data.get("is_simulation") is True:
            self.log_error(f"Identity receipt {receipt_path} is marked as simulation/mock; ineligible for real evidence")
            return False

        if data.get("component_id") != expected_component and data.get("id") != expected_component:
            self.log_error(f"Identity receipt {receipt_path} component mismatch: expected {expected_component}, got {data.get('component_id') or data.get('id')}")
            return False

        status = data.get("status") or data.get("smoke_status")
        if status not in {"PASS", "BLOCKED", "BLOCKED_DEPENDENCY", "BLOCKED_CREDENTIAL", "BLOCKED_FOR_TRIAL1", "NOT_INSTALLED", "UNMEASURED"}:
            self.log_error(f"Identity receipt {receipt_path} has invalid status '{status}'")
            return False

        return True

    def validate_semantic_receipt(self, receipt_path: Path) -> bool:
        if not receipt_path.exists():
            self.log_error(f"Missing semantic invocation receipt: {receipt_path}")
            return False

        try:
            with open(receipt_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            self.log_error(f"Malformed semantic receipt {receipt_path}: {e}")
            return False

        if data.get("test_mode") == "mock" or data.get("mock") is True:
            self.log_error(f"Semantic receipt {receipt_path} was executed in mock mode; ineligible for HG01")
            return False

        transport = (data.get("transport_class") or data.get("transport") or "").lower()
        if transport in FORBIDDEN_TRANSPORTS:
            self.log_error(f"Semantic receipt {receipt_path} uses forbidden Trial-1 transport: '{transport}'")
            return False

        if data.get("exit_code") != 0:
            self.log_error(f"Semantic receipt {receipt_path} recorded nonzero exit code {data.get('exit_code')}")
            return False

        if data.get("ttk_validation_status") == "FAIL":
            self.log_error(f"Semantic receipt {receipt_path} recorded TTK validation failure")
            return False

        output_file = data.get("output_file")
        if output_file:
            out_p = Path(output_file)
            if not out_p.is_absolute():
                out_p = REPO_ROOT / out_p
            if not out_p.exists():
                self.log_error(f"Semantic receipt {receipt_path} references missing output file {out_p}")
                return False
            output_sha = sha256_file(out_p)
            if data.get("output_sha256") and data["output_sha256"] != output_sha:
                self.log_error(f"Semantic receipt {receipt_path} output hash mismatch: recorded {data['output_sha256']}, actual {output_sha}")
                return False

        return True

    def validate_scorecard(self, scorecard_path: Path) -> bool:
        if not scorecard_path.exists():
            self.log_error(f"Scorecard does not exist: {scorecard_path}")
            return False

        try:
            with open(scorecard_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            self.log_error(f"Malformed scorecard YAML {scorecard_path}: {e}")
            return False

        if not isinstance(data, dict):
            self.log_error(f"Scorecard root must be a mapping: {scorecard_path}")
            return False

        def check_metrics(obj: Any, path_prefix: str):
            if isinstance(obj, dict):
                if "value" in obj and ("evidence_refs" not in obj and obj.get("value") != "UNMEASURED"):
                    if isinstance(obj["value"], (int, float)):
                        self.log_error(f"Scorecard {scorecard_path} metric at '{path_prefix}' has numeric value {obj['value']} without 'evidence_refs'")
                if "evidence_refs" in obj:
                    refs = obj["evidence_refs"]
                    if not isinstance(refs, list) or len(refs) == 0:
                        self.log_error(f"Scorecard {scorecard_path} at '{path_prefix}' has empty or invalid evidence_refs")
                    else:
                        for ref in refs:
                            ref_path = Path(ref)
                            if not ref_path.is_absolute():
                                ref_path = REPO_ROOT / ref_path
                            if not ref_path.exists():
                                self.log_error(f"Scorecard {scorecard_path} evidence_ref does not exist: {ref}")
                for k, v in obj.items():
                    check_metrics(v, f"{path_prefix}.{k}" if path_prefix else k)
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    check_metrics(item, f"{path_prefix}[{idx}]")

        check_metrics(data, "")
        return True

    def validate_four_source_regression(self, report_path: Path) -> bool:
        if not report_path.exists():
            self.log_error(f"Four source regression report missing: {report_path}")
            return False

        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            self.log_error(f"Malformed four source report {report_path}: {e}")
            return False

        required_sources = ["P-h5WSQG1Sw", "CygwqaNg2PY", "vFTuLylvYnA", "oZIsMX6WgFs"]
        sources = data.get("sources", {})
        for src in required_sources:
            if src not in sources:
                self.log_error(f"P20 Four-source regression missing source '{src}'")
                continue
            src_data = sources[src]
            if src_data.get("status") != "PASS":
                self.log_error(f"P20 source '{src}' status is '{src_data.get('status')}', expected 'PASS'")
            receipts = src_data.get("semantic_receipts", [])
            if not receipts:
                self.log_error(f"P20 source '{src}' has no semantic invocation receipts recorded")
            for r in receipts:
                r_p = Path(r)
                if not r_p.is_absolute():
                    r_p = REPO_ROOT / r_p
                self.validate_semantic_receipt(r_p)

        return True

    def validate_fresh_e2e(self, report_path: Path) -> bool:
        if not report_path.exists():
            self.log_error(f"Fresh E2E report missing: {report_path}")
            return False

        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            self.log_error(f"Malformed fresh E2E report {report_path}: {e}")
            return False

        for lang, expected_src in [("en", "CygwqaNg2PY"), ("de", "vFTuLylvYnA")]:
            runs = data.get("runs", {})
            if expected_src not in runs:
                self.log_error(f"P21 Fresh E2E missing required run for '{expected_src}' ({lang})")
                continue
            run_data = runs[expected_src]
            if run_data.get("status") != "PASS":
                self.log_error(f"P21 fresh run '{expected_src}' status is '{run_data.get('status')}', expected 'PASS'")
            if not run_data.get("fresh_audio_sha256"):
                self.log_error(f"P21 fresh run '{expected_src}' has no fresh audio SHA256 recorded")
            if not run_data.get("fresh_transcript_sha256"):
                self.log_error(f"P21 fresh run '{expected_src}' has no fresh transcript SHA256 recorded")
            if run_data.get("reused_old_transcript") is True:
                self.log_error(f"P21 fresh run '{expected_src}' reused old transcript, violating fresh E2E requirement")

        return True

    def validate_closure(self) -> bool:
        scorecards_dir = self.run_root / "scorecards"
        if scorecards_dir.exists():
            for sc in scorecards_dir.glob("*.yaml"):
                self.validate_scorecard(sc)

        p20_report = scorecards_dir / "four-source-regression.yaml"
        if p20_report.exists():
            self.validate_four_source_regression(p20_report)

        p21_report = scorecards_dir / "fresh-e2e-report.yaml"
        if p21_report.exists():
            self.validate_fresh_e2e(p21_report)

        manifest_path = self.run_root / "evidence-manifest.yaml"
        if manifest_path.exists():
            try:
                with open(manifest_path, "r", encoding="utf-8") as f:
                    manifest = yaml.safe_load(f)
                files = manifest.get("files", {})
                for rel_path, expected_sha in files.items():
                    f_p = REPO_ROOT / rel_path
                    if not f_p.exists():
                        self.log_error(f"Manifest file missing from disk: {rel_path}")
                    else:
                        actual_sha = sha256_file(f_p)
                        if actual_sha != expected_sha:
                            self.log_error(f"Manifest hash mismatch for '{rel_path}': expected {expected_sha}, got {actual_sha}")
            except Exception as e:
                self.log_error(f"Malformed manifest {manifest_path}: {e}")

        final_report_path = self.run_root / "corrective-final-report.yaml"
        if not final_report_path.exists():
            final_report_path = CANONICAL_ROOT / "FINAL-REPORT.yaml"

        if final_report_path.exists():
            try:
                with open(final_report_path, "r", encoding="utf-8") as f:
                    final_rep = yaml.safe_load(f)
                if final_rep.get("verdict") == "PASS":
                    if self.errors:
                        self.log_error(f"FINAL-REPORT claims PASS but evidence closure validator found {len(self.errors)} error(s)")
            except Exception as e:
                self.log_error(f"Malformed final report {final_report_path}: {e}")

        return len(self.errors) == 0


def main():
    parser = argparse.ArgumentParser(description="Validate evidence closure for V2.1 Trial 1")
    parser.add_argument("--root", type=str, default=None, help="Root path of corrective run")
    args = parser.parse_args()

    root = Path(args.root) if args.root else None
    validator = EvidenceClosureValidator(root)
    passed = validator.validate_closure()

    if validator.warnings:
        print(f"[WARNINGS] ({len(validator.warnings)}):")
        for w in validator.warnings:
            print(f"  - {w}")

    if not passed:
        print(f"[FAIL] Evidence closure validation failed with {len(validator.errors)} error(s):")
        for err in validator.errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("[PASS] Evidence closure validated successfully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
