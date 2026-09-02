---
type: Plan
title: PATCH-02 — OKF Validator Correctness
description: Corrective patch pack for upstream-vs-Apex diagnostic ownership, real YAML parsing, nested-index traversal, reserved-file validation, and regression tests.
tags: [patch, okf, validator, tests, yaml]
generated: { by: openai/gpt-5.6-sol, at: 2026-09-02T07:02:00Z }
status: proposed_not_applied
---

# Intent

The current validator is not yet a valid implementation of the standard it claims to enforce.

This patch fixes four classes of error:

```text
false upstream failures
false negatives below nested index.md files
fake YAML parsing
missing reserved-file validation
```

Apply after or together with `PATCH-01-informatics-scope-and-standard.md`.

# Dependency decision

OKF requires **parseable YAML**, including producer-defined nested structures. A colon-splitting parser cannot prove that requirement. Use a real YAML parser.

Create:

<file>apex-meta/scripts/requirements-okf-validator.txt</file>
<new>PyYAML>=6.0,<7
</new>

Execution environment must install this dependency before running the validator or its tests:

```bash
python -m pip install -r apex-meta/scripts/requirements-okf-validator.txt
```

# Block 1 — import the real YAML parser

<file>apex-meta/scripts/okf_validator.py</file>
<old>import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple</old>
<new>import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml</new>

# Block 2 — replace the hand-written frontmatter parser

<file>apex-meta/scripts/okf_validator.py</file>
<old>def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str, Optional[str]]:
    """
    Parses frontmatter from Markdown text.
    Returns (frontmatter_dict, body_text, error_message).
    """
    if not content.startswith("---"):
        return None, content, "No YAML frontmatter header ('---') found at start of file"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content, "Unterminated YAML frontmatter ('---' closing delimiter missing)"

    fm_raw = parts[1]
    body = parts[2]

    # Lightweight deterministic YAML parser for flat/nested maps without external PyYAML dependency
    fm_dict: Dict[str, Any] = {}
    for line_num, line in enumerate(fm_raw.splitlines(), start=2):
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        if ":" not in line_clean:
            return None, content, f"Malformed frontmatter on line {line_num}: missing ':'"

        key, val = line_clean.split(":", 1)
        key = key.strip()
        val = val.strip()

        # Handle simple quotes
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        elif val.startswith("[") and val.endswith("]"):
            # Simple list
            items = [item.strip().strip("'\"") for item in val[1:-1].split(",") if item.strip()]
            val = items

        fm_dict[key] = val

    return fm_dict, body, None</old>
<new>def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str, Optional[str]]:
    """Parse a Markdown YAML frontmatter block with a real YAML parser."""
    if not content.startswith("---\n"):
        return None, content, "No YAML frontmatter header ('---') found at start of file"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content, "Unterminated YAML frontmatter ('---' closing delimiter missing)"

    fm_raw = parts[1]
    body = parts[2]

    try:
        parsed = yaml.safe_load(fm_raw)
    except yaml.YAMLError as exc:
        return None, content, f"YAML parse error: {exc}"

    if parsed is None:
        parsed = {}
    if not isinstance(parsed, dict):
        return None, content, "YAML frontmatter must parse to a mapping"

    return parsed, body, None</new>

# Block 3 — add reserved-file validators

Insert immediately after `extract_links` and before `check_writing_style`.

<file>apex-meta/scripts/okf_validator.py</file>
<old>def check_writing_style(path: str, body_text: str) -> List[Finding]:</old>
<new>def validate_index_file(file_path: Path, rel_path: str, target_path: Path) -> List[Finding]:
    """Validate an OKF reserved index.md and Apex routing-profile additions."""
    findings: List[Finding] = []
    content = file_path.read_text(encoding="utf-8", errors="replace")
    is_root = rel_path == "index.md"

    if is_root:
        if content.startswith("---"):
            fm, _body, err = parse_frontmatter(content)
            if err:
                findings.append(Finding("OKF_ERROR", rel_path, "OKF-INDEX-STRUCTURE", err))
            else:
                assert fm is not None
                extra_keys = set(fm) - {"okf_version"}
                if extra_keys:
                    findings.append(
                        Finding(
                            "APEX_PROFILE_ERROR",
                            rel_path,
                            "APEX-ROOT-INDEX-FRONTMATTER",
                            f"Apex root index frontmatter should contain only okf_version; extra keys: {sorted(extra_keys)}",
                        )
                    )
                if str(fm.get("okf_version", "")) != "0.2":
                    findings.append(
                        Finding(
                            "APEX_PROFILE_ERROR",
                            rel_path,
                            "APEX-OKF-VERSION-DECLARATION",
                            "Governed Apex bundle root index.md must declare okf_version: '0.2'",
                        )
                    )
        else:
            findings.append(
                Finding(
                    "APEX_PROFILE_ERROR",
                    rel_path,
                    "APEX-OKF-VERSION-DECLARATION",
                    "Governed Apex bundle root index.md must declare okf_version: '0.2'",
                )
            )
    elif content.startswith("---"):
        findings.append(
            Finding(
                "OKF_ERROR",
                rel_path,
                "OKF-NESTED-INDEX-FRONTMATTER",
                "Only the bundle-root index.md may contain frontmatter",
            )
        )

    for link in extract_links(content):
        resolved = (file_path.parent / link).resolve()
        if not resolved.exists():
            findings.append(
                Finding(
                    "APEX_PROFILE_ERROR",
                    rel_path,
                    "APEX-LINK-INTEGRITY",
                    f"Governed index link does not resolve to target file: '{link}'",
                )
            )

    return findings


def validate_log_file(file_path: Path, rel_path: str) -> List[Finding]:
    """Validate the OKF reserved log.md date-grouped structure."""
    findings: List[Finding] = []
    content = file_path.read_text(encoding="utf-8", errors="replace")

    if content.startswith("---"):
        findings.append(
            Finding(
                "OKF_ERROR",
                rel_path,
                "OKF-LOG-FRONTMATTER",
                "Reserved log.md must not contain YAML frontmatter",
            )
        )

    level_two_headings = re.findall(r"^##\s+(.+?)\s*$", content, flags=re.MULTILINE)
    for heading in level_two_headings:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", heading):
            findings.append(
                Finding(
                    "OKF_ERROR",
                    rel_path,
                    "OKF-LOG-DATE-HEADING",
                    f"log.md level-two heading must be ISO date YYYY-MM-DD: '{heading}'",
                )
            )

    return findings


def check_writing_style(path: str, body_text: str) -> List[Finding]:</new>

# Block 4 — reclassify a missing root index as an Apex profile failure

<file>apex-meta/scripts/okf_validator.py</file>
<old>    # 1. Root index.md validation
    if not root_index.is_file():
        findings.append(
            Finding(
                severity="OKF_ERROR",
                path="index.md",
                rule="OKF-ROOT-INDEX-EXISTS",
                message="Bundle root index.md does not exist",
            )
        )
    else:
        content = root_index.read_text(encoding="utf-8", errors="replace")
        fm, body, err = parse_frontmatter(content)
        if err:
            findings.append(
                Finding(
                    severity="OKF_ERROR",
                    path="index.md",
                    rule="OKF-INDEX-FRONTMATTER",
                    message=f"Invalid root index.md frontmatter: {err}",
                )
            )
        elif not fm or fm.get("okf_version") != "0.2":
            findings.append(
                Finding(
                    severity="OKF_ERROR",
                    path="index.md",
                    rule="OKF-VERSION-DECLARATION",
                    message="Root index.md must declare okf_version: '0.2'",
                )
            )

        # Apex profile check: verify links in root index resolve to existing files
        links = extract_links(content)
        for link in links:
            resolved = (target_path / link).resolve()
            if not resolved.exists():
                findings.append(
                    Finding(
                        severity="APEX_PROFILE_ERROR",
                        path="index.md",
                        rule="APEX-LINK-INTEGRITY",
                        message=f"Governed index link does not resolve to target file: '{link}'",
                    )
                )</old>
<new>    # 1. Apex governed-bundle root routing requirement.
    # Upstream OKF permits a bundle without index.md; therefore missing root index is not OKF_ERROR.
    if not root_index.is_file():
        findings.append(
            Finding(
                severity="APEX_PROFILE_ERROR",
                path="index.md",
                rule="APEX-ROOT-INDEX-EXISTS",
                message="Governed Apex bundle root index.md does not exist",
            )
        )</new>

# Block 5 — traverse the complete bundle tree and validate reserved files at every level

<file>apex-meta/scripts/okf_validator.py</file>
<old>    # 2. Iterate through concept files inside the bundle (excluding .git and sub-bundles)
    durable_ids: Dict[str, str] = {}

    for root, dirs, files in os.walk(target_path):
        # Exclude subdirectories that are separate bundles (have their own index.md)
        current_dir = Path(root)
        if current_dir != target_path and (current_dir / "index.md").exists():
            dirs.clear()  # Do not recurse into separate sub-bundle
            continue

        for f in files:
            if not f.endswith(".md"):
                continue

            file_path = current_dir / f
            rel_path = file_path.relative_to(target_path).as_posix()

            # Reserved files
            if rel_path == "index.md":
                continue
            if rel_path == "log.md":
                # Reserved changelog
                continue

            content = file_path.read_text(encoding="utf-8", errors="replace")</old>
<new>    # 2. Iterate through every Markdown file in the bundle tree.
    # A nested index.md is progressive disclosure inside the same OKF bundle; it does not create an implicit sub-bundle boundary.
    durable_ids: Dict[str, str] = {}

    for root, dirs, files in os.walk(target_path):
        dirs[:] = [d for d in dirs if d != ".git"]
        current_dir = Path(root)

        for f in files:
            if not f.endswith(".md"):
                continue

            file_path = current_dir / f
            rel_path = file_path.relative_to(target_path).as_posix()

            if f == "index.md":
                findings.extend(validate_index_file(file_path, rel_path, target_path))
                continue
            if f == "log.md":
                findings.extend(validate_log_file(file_path, rel_path))
                continue

            content = file_path.read_text(encoding="utf-8", errors="replace")</new>

# Block 6 — enforce Apex routing metadata separately from upstream type

Insert immediately after the existing `OKF-TYPE-REQUIRED` check.

<file>apex-meta/scripts/okf_validator.py</file>
<old>            # Apex profile check: unique durable ID
            if "id" in fm:</old>
<new>            # Apex governed-bundle routing metadata. These are local profile requirements, not upstream OKF requirements.
            for local_key in ("title", "description"):
                local_value = fm.get(local_key)
                if not local_value or not str(local_value).strip():
                    findings.append(
                        Finding(
                            severity="APEX_PROFILE_ERROR",
                            path=rel_path,
                            rule=f"APEX-{local_key.upper()}-REQUIRED",
                            message=f"Governed Apex concept must contain non-empty '{local_key}' metadata",
                        )
                    )

            # Apex profile check: unique durable ID
            if "id" in fm:</new>

# Test corrections

## Block 7 — update the test-suite scope comment

<file>apex-meta/scripts/tests/test_okf_validator.py</file>
<old>Covers:
- RED tests (must fail): malformed YAML, missing type, missing index, broken index link, duplicate durable ID, pseudo-OKF drift.
- GREEN tests (must pass): valid OKF bundles, custom local types (Research, Plan, Standard), omitted optional metadata, long code lines.</old>
<new>Covers:
- OKF RED tests: malformed YAML, missing type, invalid reserved index/log structure.
- APEX_PROFILE RED tests: missing governed root index/version, missing local routing metadata, broken governed index link, duplicate durable ID, pseudo-OKF drift.
- GREEN tests: upstream OKF without an index, custom local types, nested indexed directories, valid nested YAML, and code-line advisory exemptions.</new>

## Block 8 — replace the wrong missing-index test

<file>apex-meta/scripts/tests/test_okf_validator.py</file>
<old>    def test_red_missing_root_index(self):
        """Bundle missing root index.md fails OKF conformance."""
        bundle_dir = os.path.join(self.test_dir, "missing_index_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "concept.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\n---\n# Concept\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertGreaterEqual(report.okf_errors, 1)
        self.assertTrue(any(f.rule == "OKF-ROOT-INDEX-EXISTS" for f in report.findings))</old>
<new>    def test_red_missing_root_index_is_apex_profile_only(self):
        """Upstream OKF permits missing index.md; the Apex governed profile may reject it separately."""
        bundle_dir = os.path.join(self.test_dir, "missing_index_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "concept.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\ntitle: Concept\ndescription: Test concept.\n---\n# Concept\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertEqual(report.okf_errors, 0)
        self.assertTrue(any(f.rule == "APEX-ROOT-INDEX-EXISTS" for f in report.findings))</new>

## Block 9 — add nested-tree and real-YAML regressions

Insert before `if __name__ == "__main__":`.

<file>apex-meta/scripts/tests/test_okf_validator.py</file>
<old>

if __name__ == "__main__":
    unittest.main()</old>
<new>
    def test_green_nested_index_does_not_hide_concepts(self):
        """Nested index.md is progressive disclosure, not an implicit separate-bundle boundary."""
        bundle_dir = os.path.join(self.test_dir, "nested_bundle")
        sub_dir = os.path.join(bundle_dir, "sub")
        os.makedirs(sub_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Sub](sub/)\n')
        with open(os.path.join(sub_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('# Sub\n- [Concept](concept.md)\n')
        with open(os.path.join(sub_dir, "concept.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\ntitle: Nested\ndescription: Nested concept.\n---\n# Nested\n')

        report = validate_bundle(bundle_dir)
        self.assertTrue(report.passed)

    def test_red_nested_concept_missing_type_is_not_skipped(self):
        bundle_dir = os.path.join(self.test_dir, "nested_bad_bundle")
        sub_dir = os.path.join(bundle_dir, "sub")
        os.makedirs(sub_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Sub](sub/)\n')
        with open(os.path.join(sub_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('# Sub\n- [Concept](concept.md)\n')
        with open(os.path.join(sub_dir, "concept.md"), "w", encoding="utf-8") as f:
            f.write('---\ntitle: Nested\ndescription: Missing type.\n---\n# Nested\n')

        report = validate_bundle(bundle_dir)
        self.assertTrue(any(f.rule == "OKF-TYPE-REQUIRED" for f in report.findings))

    def test_green_real_nested_yaml_frontmatter(self):
        bundle_dir = os.path.join(self.test_dir, "nested_yaml_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Concept](concept.md)\n')
        with open(os.path.join(bundle_dir, "concept.md"), "w", encoding="utf-8") as f:
            f.write(
                '---\n'
                'type: Reference\n'
                'title: Nested YAML\n'
                'description: Valid nested YAML.\n'
                'sources:\n'
                '  - id: source-a\n'
                '    resource: https://example.com/a\n'
                'verified:\n'
                '  - by: tester\n'
                '    at: 2026-09-02T00:00:00Z\n'
                '---\n# Concept\n'
            )

        report = validate_bundle(bundle_dir)
        self.assertTrue(report.passed)

    def test_red_log_non_iso_level_two_heading(self):
        bundle_dir = os.path.join(self.test_dir, "bad_log_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n')
        with open(os.path.join(bundle_dir, "log.md"), "w", encoding="utf-8") as f:
            f.write('# Log\n\n## September 2, 2026\n- Updated\n')

        report = validate_bundle(bundle_dir)
        self.assertTrue(any(f.rule == "OKF-LOG-DATE-HEADING" for f in report.findings))


if __name__ == "__main__":
    unittest.main()</new>

# Important test-fixture consequence

After Block 6, every test concept intended to be `APEX_PROFILE`-clean must include `title` and `description`. Update existing GREEN fixtures accordingly. Do **not** add those fields to tests whose purpose is specifically to prove upstream OKF tolerates missing optional fields; those tests should assert `okf_errors == 0` while allowing the local `APEX_PROFILE` result to be inspected separately.

# Acceptance gate

```bash
python -m pip install -r apex-meta/scripts/requirements-okf-validator.txt
python apex-meta/scripts/tests/test_okf_validator.py
python apex-meta/scripts/okf_validator.py --target apex-meta/informatics/
python apex-meta/scripts/okf_validator.py --target apex-meta/SmallSkills/OKF_Format/
```

Pass only when:

```text
- malformed real YAML is rejected
- nested indexed concepts are traversed
- missing root index is not labeled upstream OKF failure
- optional upstream fields are not labeled upstream OKF failure
- reserved log/index structure is checked when present
- Apex routing requirements remain visibly separate
```
