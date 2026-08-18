#!/usr/bin/env python3
"""Standalone CLI entrypoint for transcript-to-knowledge v2."""
from ttk_compile import *
def doctor() -> dict[str, Any]:
    return {
        "schema": "ttk.doctor.v2",
        "python": sys.version.split()[0],
        "python_ok": sys.version_info >= (3, 10),
        "stdlib_only": True,
        "network_calls_in_cli": False,
        "llm_calls_in_cli": False,
        "supported_inputs": [".json", ".jsonl", ".ndjson", ".srt", ".vtt", ".txt", ".md", ".markdown"],
    }


def print_output(value: Any, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True))
    elif isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                print(f"{key}: {json.dumps(item, ensure_ascii=False, sort_keys=True)}")
            else:
                print(f"{key}: {item}")
    else:
        print(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Standalone deterministic control plane for transcript-to-knowledge runs")
    parser.add_argument("--json-output", action="store_true", help="Emit machine-readable JSON")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_init(name: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name, help="Normalize a transcript and create semantic work packets")
        p.add_argument("input", type=Path)
        p.add_argument("--output", "-o", type=Path, required=True)
        p.add_argument("--target-words", type=int, default=1100)
        p.add_argument("--min-words", type=int, default=700)
        p.add_argument("--max-words", type=int, default=1500)
        p.add_argument("--block-segments", type=int, default=4)
        p.add_argument("--pause-weight", type=float, default=0.15)
        p.add_argument("--context-segments", type=int, default=1)
        return p

    add_init("init")
    add_init("prepare")
    for name in ("status", "next", "validate", "make-reduce", "make-verify", "compile"):
        p = sub.add_parser(name)
        p.add_argument("run_dir", type=Path)
        if name == "validate":
            p.add_argument("--complete", action="store_true", help="Fail unless the run is fully compiled and current")
        if name == "make-verify":
            p.add_argument("--min-checkworthiness", choices=["high", "medium", "low"], default="medium")
        if name == "compile":
            p.add_argument("--allow-unsupported", action="store_true")
    sub.add_parser("doctor")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    actual = list(sys.argv[1:] if argv is None else argv)
    if "--json-output" in actual:
        actual = [item for item in actual if item != "--json-output"]
        actual.insert(0, "--json-output")
    args = parser.parse_args(actual)
    try:
        if args.command in {"init", "prepare"}:
            result = init_run(args.input, args.output, args.target_words, args.min_words, args.max_words,
                              args.block_segments, args.pause_weight, args.context_segments)
        elif args.command == "status":
            result = status(args.run_dir)
        elif args.command == "next":
            result = next_action(args.run_dir)
        elif args.command == "validate":
            result = validate_run(args.run_dir)
        elif args.command == "make-reduce":
            result = make_reduce_packet(args.run_dir)
        elif args.command == "make-verify":
            result = make_verify_queue(args.run_dir, args.min_checkworthiness)
        elif args.command == "compile":
            result = compile_wiki(args.run_dir, strict=not args.allow_unsupported)
        elif args.command == "doctor":
            result = doctor()
        else:
            parser.error("unknown command")
            return 2
        print_output(result, args.json_output)
        if args.command == "validate" and (not result.get("ok") or (args.complete and not result.get("complete"))):
            return 1
        return 0
    except (TTKError, OSError, json.JSONDecodeError) as exc:
        if args.json_output:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
