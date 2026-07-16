# N1 - Phase 1 source-coverage gate exact-match replacements

Adds a deterministic floor on how many of a topic's work-pack-concentrated candidate sources
must actually be analyzed (produce a `### <source_id> - authority:` record) before the topic's
Phase 1 stage may complete. This is the mechanical fix for the confirmed incident pattern of a
build reporting topics "complete" while only 4 of 405 ranked sources were ever opened.

Every `<old>` block was copied from the live baseline at commit `878839459ff8430c8bbfd3e8c52a4753794f1c56` (see
`package-manifest.json`).

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\run-intent.schema.json</file>
<old>
    "corpus_breadth": {"enum": ["narrow", "broad"]},
    "broad_breadth_reason": {"type": ["string", "null"]},
    "topic_slugs": {
</old>
<new>
    "corpus_breadth": {"enum": ["narrow", "broad"]},
    "broad_breadth_reason": {"type": ["string", "null"]},
    "phase1_min_coverage": {"type": ["number", "null"], "minimum": 0, "maximum": 1},
    "topic_slugs": {
</new>

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\run-state.schema.json</file>
<old>
    "output_tier": {
      "enum": [
        "source_only",
        "analysis_only",
        "compiled_minimal",
        "compiled_full",
        "query_ready"
      ]
    },
    "operator_confirmation": {"$ref": "#/$defs/operator_confirmation"},
</old>
<new>
    "output_tier": {
      "enum": [
        "source_only",
        "analysis_only",
        "compiled_minimal",
        "compiled_full",
        "query_ready"
      ]
    },
    "phase1_min_coverage": {"type": ["number", "null"], "minimum": 0, "maximum": 1},
    "operator_confirmation": {"$ref": "#/$defs/operator_confirmation"},
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
    init.add_argument("--corpus-breadth", choices=["narrow", "broad"], default="narrow")
    init.add_argument("--broad-breadth-reason")
    init.add_argument("--topic-slug", action="append", default=[])
</old>
<new>
    init.add_argument("--corpus-breadth", choices=["narrow", "broad"], default="narrow")
    init.add_argument("--broad-breadth-reason")
    init.add_argument(
        "--phase1-min-coverage",
        type=float,
        default=0.6,
        help="Minimum ratio (0-1) of a topic's work-pack concentrated-candidate sources that "
        "must have a per-source analysis record before that topic's phase1 stage completes",
    )
    init.add_argument("--topic-slug", action="append", default=[])
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
        "corpus_breadth": args.corpus_breadth,
        "broad_breadth_reason": args.broad_breadth_reason,
        "topic_slugs": topic_slugs,
</old>
<new>
        "corpus_breadth": args.corpus_breadth,
        "broad_breadth_reason": args.broad_breadth_reason,
        "phase1_min_coverage": args.phase1_min_coverage,
        "topic_slugs": topic_slugs,
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
        "topics": topics,
        "output_tier": intent["output_tier"],
        "operator_confirmation": {"confirmed": False, "quote": "", "confirmed_at": None},
</old>
<new>
        "topics": topics,
        "output_tier": intent["output_tier"],
        "phase1_min_coverage": intent.get("phase1_min_coverage", 0.6),
        "operator_confirmation": {"confirmed": False, "quote": "", "confirmed_at": None},
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_control.py</file>
<old>
    finding_func = core.get("candidate_disposition_findings")
    if callable(finding_func):
        findings = finding_func(kb_root)
        rel_output = output.relative_to(kb_root).as_posix()
        if any(item.get("path") == rel_output for item in findings if isinstance(item, dict)):
            return ControlError("candidate_disposition_missing", "Phase 1 candidate disposition is incomplete", paths=[rel_output])
    workpack_json, workpack_md = _workpack_paths(slug)
    record_fingerprint(state, kb_root, kb_root / workpack_json, f"phase1:{slug}")
</old>
<new>
    finding_func = core.get("candidate_disposition_findings")
    if callable(finding_func):
        findings = finding_func(kb_root)
        rel_output = output.relative_to(kb_root).as_posix()
        if any(item.get("path") == rel_output for item in findings if isinstance(item, dict)):
            return ControlError("candidate_disposition_missing", "Phase 1 candidate disposition is incomplete", paths=[rel_output])
    ranked = len(_candidate_inputs(kb_root, slug))
    opened = len(set(re.findall(r"(?m)^### (\S+) - authority:", text)))
    floor = float(state.get("phase1_min_coverage") or 0.6)
    coverage = (opened / ranked) if ranked else 1.0
    if ranked and coverage < floor:
        return ControlError(
            "phase1_source_coverage_below_floor",
            f"{opened}/{ranked} work-pack concentrated-candidate sources analyzed "
            f"(coverage {coverage:.2f}, floor {floor:.2f}); open more ranked sources or "
            f"record them as rejected in the Source Inventory before completing this topic",
            paths=[rel_or_abs(kb_root, output)],
        )
    workpack_json, workpack_md = _workpack_paths(slug)
    record_fingerprint(state, kb_root, kb_root / workpack_json, f"phase1:{slug}")
</new>
