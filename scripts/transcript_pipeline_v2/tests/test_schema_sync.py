"""Unit test to ensure JSON Schemas stay synchronized with TTK contract constants."""
import json
import sys
import unittest
from pathlib import Path

# Add TTK scripts directory to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TTK_SCRIPTS_DIR = REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"
sys.path.insert(0, str(TTK_SCRIPTS_DIR))

import ttk_base


class TestSchemaSync(unittest.TestCase):

    def setUp(self):
        self.schemas_dir = REPO_ROOT / "scripts" / "transcript_pipeline_v2" / "schemas"

    def test_map_result_schema_sync(self):
        schema_path = self.schemas_dir / "map-result.schema.json"
        self.assertTrue(schema_path.exists())
        with open(schema_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertEqual(data["properties"]["schema"]["const"], ttk_base.MAP_RESULT_SCHEMA)
        
        # Verify claim_kinds match TTK CLAIM_KINDS
        kinds = set(data["properties"]["candidate_claims"]["items"]["properties"]["claim_kind"]["enum"])
        self.assertEqual(kinds, ttk_base.CLAIM_KINDS)
        
        # Verify checkworthiness matches TTK CHECKWORTHINESS
        cw = set(data["properties"]["candidate_claims"]["items"]["properties"]["checkworthiness"]["enum"])
        self.assertEqual(cw, ttk_base.CHECKWORTHINESS)

    def test_reduce_result_schema_sync(self):
        schema_path = self.schemas_dir / "reduce-result.schema.json"
        self.assertTrue(schema_path.exists())
        with open(schema_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertEqual(data["properties"]["schema"]["const"], ttk_base.REDUCE_RESULT_SCHEMA)
        
        # Verify claim_kinds match TTK CLAIM_KINDS
        kinds = set(data["properties"]["micro"]["items"]["properties"]["claim_kind"]["enum"])
        self.assertEqual(kinds, ttk_base.CLAIM_KINDS)
        
        # Verify source_support matches TTK SOURCE_SUPPORT
        ss = set(data["properties"]["micro"]["items"]["properties"]["source_support"]["enum"])
        self.assertEqual(ss, ttk_base.SOURCE_SUPPORT)

    def test_verify_result_schema_sync(self):
        schema_path = self.schemas_dir / "verify-result.schema.json"
        self.assertTrue(schema_path.exists())
        with open(schema_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertEqual(data["properties"]["schema"]["const"], ttk_base.VERIFY_RESULT_SCHEMA)
        
        # Verify status matches TTK EXTERNAL_STATUS
        status = set(data["properties"]["results"]["items"]["properties"]["status"]["enum"])
        self.assertEqual(status, ttk_base.EXTERNAL_STATUS)
        
        # Verify stance matches TTK EVIDENCE_STANCE
        stance = set(data["properties"]["results"]["items"]["properties"]["evidence"]["items"]["properties"]["stance"]["enum"])
        self.assertEqual(stance, ttk_base.EVIDENCE_STANCE)


if __name__ == "__main__":
    unittest.main()
