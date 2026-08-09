import unittest

from apexcalc.cache import load_index


class TestCacheIndex(unittest.TestCase):
    def test_index_loads_at_current_schema(self):
        data = load_index(".apexcalc_cache")
        self.assertEqual(data["schema"], 2)
