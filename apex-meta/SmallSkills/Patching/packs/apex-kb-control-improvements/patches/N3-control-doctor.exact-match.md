# N3 - control doctor self-check exact-match replacements

Adds `control doctor`: a read-only self-check of the apex-kb *skill package itself* (not a
specific KB instance) - every schema parses, every template's referenced schema file exists,
`canonical_paths` agrees between `SKILL.md` and `kb-contract.md`, the documented control-test
discovery path resolves to real files, `apex_kb_control.py` compiles, and every parser action has
a dispatch branch. This module also fixes one real inconsistency `doctor` immediately surfaces:
`kb-contract.md`'s canonical list includes `log/runs/<run-id>/stage-results/`, which `SKILL.md`'s
list was missing.

Every `<old>` block was copied from the live baseline at commit `878839459ff8430c8bbfd3e8c52a4753794f1c56` (see
`package-manifest.json`).

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\SKILL.md</file>
<old>
  - log/
  - log/runs/<run-id>/packets/
</old>
<new>
  - log/
  - log/runs/<run-id>/packets/
  - log/runs/<run-id>/stage-results/
</new>

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\script-command-contract.md</file>
<old>
| `git-state` | no | classify branch, HEAD, upstream, ahead/behind, dirty/untracked/conflicted counts, and in-progress operations without mutation |

The compact result for every action conforms to `apex.kb.stage-result.v1`. A controlled KB has `manifests/run-state.json`; direct low-level mutation commands are blocked for that KB so state cannot drift. Legacy KBs without run state keep their existing low-level command behavior.
</old>
<new>
| `git-state` | no | classify branch, HEAD, upstream, ahead/behind, dirty/untracked/conflicted counts, and in-progress operations without mutation |
| `doctor` | no | validate the apex-kb skill package's own internal consistency (schemas parse, template schema references exist, `SKILL.md`/`kb-contract.md` canonical paths agree, control test files are discoverable, `apex_kb_control.py` compiles, every parser action has a dispatch branch) - independent of any specific KB |

The compact result for every action conforms to `apex.kb.stage-result.v1`. A controlled KB has `manifests/run-state.json`; direct low-level mutation commands are blocked for that KB so state cannot drift. Legacy KBs without run state keep their existing low-level command behavior.
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
    git_state = actions.add_parser("git-state", help="Classify Git/worktree state without mutating it")
    git_state.add_argument("--repo-root")
</old>
<new>
    git_state = actions.add_parser("git-state", help="Classify Git/worktree state without mutating it")
    git_state.add_argument("--repo-root")

    actions.add_parser("doctor", help="Validate skill-package internal consistency (independent of any specific KB)")
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
        if action == "git-state":
            return control_git_state(args)
        raise ControlError("unknown_control_action", f"Unknown control action: {action}")
</old>
<new>
        if action == "git-state":
            return control_git_state(args)
        if action == "doctor":
            return cmd_doctor(args)
        raise ControlError("unknown_control_action", f"Unknown control action: {action}")
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
# ---------------------------------------------------------------------------
# Parser integration, dispatch, and direct-command guard
# ---------------------------------------------------------------------------


def configure_parser(parser: argparse.ArgumentParser) -> None:
</old>
<new>
def cmd_doctor(args: argparse.Namespace) -> Dict[str, Any]:
    """Read-only self-check of the apex-kb skill package's own internal consistency - not a
    specific KB instance. Never touches --kb-root; catches the class of bug where the skill
    package itself ships internally inconsistent documentation or code."""
    root = repository_root()
    skill = skill_root()
    checks: List[Dict[str, Any]] = []

    def add_check(name: str, ok: bool, detail: str = "") -> None:
        checks.append({"check": name, "status": "ok" if ok else "fail", "detail": detail})

    schema_dir = skill / "references"
    schema_files = sorted(schema_dir.glob("*.schema.json")) if schema_dir.exists() else []
    for schema_file in schema_files:
        try:
            value = json.loads(schema_file.read_text(encoding="utf-8-sig"))
            add_check(f"schema_parses:{schema_file.name}", isinstance(value, dict), "" if isinstance(value, dict) else "schema root is not an object")
        except json.JSONDecodeError as exc:
            add_check(f"schema_parses:{schema_file.name}", False, str(exc))

    template_dir = skill / "templates"
    schema_names = {schema_file.name for schema_file in schema_files}
    template_files = sorted(template_dir.glob("*.md")) if template_dir.exists() else []
    referenced_missing: List[str] = []
    for template_file in template_files:
        text = template_file.read_text(encoding="utf-8-sig")
        for match in re.finditer(r"([\w.-]+\.schema\.json)", text):
            name = match.group(1)
            if name not in schema_names:
                referenced_missing.append(f"{template_file.name} -> {name}")
    add_check("template_schema_refs_exist", not referenced_missing, "; ".join(referenced_missing))

    def _canonical_block(text: str, key: str) -> Optional[List[str]]:
        match = re.search(rf"{key}:\n((?:  - .+\n)+)", text)
        if not match:
            return None
        return [line.strip("- ").strip() for line in match.group(1).splitlines() if line.strip()]

    skill_md_text = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
    kb_contract_text = (skill / "references" / "kb-contract.md").read_text(encoding="utf-8-sig")
    skill_paths = _canonical_block(skill_md_text, "canonical_paths")
    contract_paths = _canonical_block(kb_contract_text, "canonical")
    if skill_paths is None or contract_paths is None:
        add_check("canonical_paths_match", False, "could not locate a canonical_paths block in SKILL.md and/or kb-contract.md")
    else:
        missing_from_contract = sorted(set(skill_paths) - set(contract_paths))
        missing_from_skill = sorted(set(contract_paths) - set(skill_paths))
        detail_parts = []
        if missing_from_contract:
            detail_parts.append(f"in SKILL.md only: {missing_from_contract}")
        if missing_from_skill:
            detail_parts.append(f"in kb-contract.md only: {missing_from_skill}")
        add_check("canonical_paths_match", not detail_parts, "; ".join(detail_parts))

    test_dir = root / "apex-meta" / "scripts" / "tests"
    control_tests = sorted(test_dir.glob("test_apex_kb_control*.py")) if test_dir.exists() else []
    add_check("control_test_discovery_path_resolves", len(control_tests) >= 2, f"found {len(control_tests)} at {test_dir}")

    control_path = Path(__file__).resolve()
    try:
        compile(control_path.read_text(encoding="utf-8-sig"), str(control_path), "exec")
        add_check("control_module_compiles", True)
    except SyntaxError as exc:
        add_check("control_module_compiles", False, str(exc))

    parser_for_check = argparse.ArgumentParser()
    configure_parser(parser_for_check)
    actions_choices: List[str] = []
    for action in parser_for_check._actions:
        if isinstance(action, argparse._SubParsersAction):
            actions_choices = sorted(action.choices.keys())
            break
    dispatch_source = control_path.read_text(encoding="utf-8-sig")
    missing_dispatch = [name for name in actions_choices if f'action == "{name}"' not in dispatch_source]
    add_check("every_control_action_has_dispatch_branch", not missing_dispatch, f"missing: {missing_dispatch}" if missing_dispatch else "")

    all_ok = all(item["status"] == "ok" for item in checks)
    return stage_result(
        "doctor",
        "doctor",
        "ok" if all_ok else "failed",
        reason_code=None if all_ok else "doctor_check_failed",
        artifact={"checks": checks},
        next_stage=None,
        operator_action=None if all_ok else "Fix the failing skill-package consistency check(s) listed in artifact.checks",
    )


# ---------------------------------------------------------------------------
# Parser integration, dispatch, and direct-command guard
# ---------------------------------------------------------------------------


def configure_parser(parser: argparse.ArgumentParser) -> None:
</new>
