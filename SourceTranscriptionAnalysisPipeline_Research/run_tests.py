import sys
from pathlib import Path

# Add directory to path
research_dir = Path(__file__).parent
sys.path.insert(0, str(research_dir))

import test_transcript_engine as t
import tempfile

def run_all():
    tests = [
        ("test_timestamp_roundtrip", t.test_timestamp_roundtrip),
        ("test_timestamp_invalid_raises", t.test_timestamp_invalid_raises),
        ("test_micro_claim_validates_timestamp", t.test_micro_claim_validates_timestamp),
        ("test_micro_claim_validates_verdict", t.test_micro_claim_validates_verdict),
        ("test_macro_markdown_contains_wikilinks", t.test_macro_markdown_contains_wikilinks),
        ("test_meso_module_renders_timestamp_range", t.test_meso_module_renders_timestamp_range),
        ("test_micro_claim_default_verdict_is_unverified", t.test_micro_claim_default_verdict_is_unverified),
        ("test_verification_hook_injects_sources_without_network", t.test_verification_hook_injects_sources_without_network),
        ("test_engine_end_to_end_renders_full_wiki_markdown", lambda: t.test_engine_end_to_end_renders_full_wiki_markdown(Path(tempfile.mkdtemp()))),
        ("test_engine_json_serializable_roundtrip", t.test_engine_json_serializable_roundtrip),
    ]

    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  [PASS] {name}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {name}: {e}")

    print(f"\nResult: {passed}/{len(tests)} tests passed.")
    if passed == len(tests):
        print("All 10 unit tests verified successfully!")

if __name__ == "__main__":
    run_all()
