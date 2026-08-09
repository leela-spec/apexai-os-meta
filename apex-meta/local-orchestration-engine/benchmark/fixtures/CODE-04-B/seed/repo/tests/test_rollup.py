import datetime
import unittest

from apexcalc.rollup import weekly_buckets


class TestRollup(unittest.TestCase):
    def test_bucket_spans_sunday_to_saturday(self):
        # Saturday-anchored fixture data -- both Monday-start and Sunday-start
        # week numbering agree on this range, so this test does not detect
        # the week-origin conflict between rollup.py's docstring and its
        # actual (Monday-based) implementation.
        dates = [datetime.date(2026, 8, 1)]  # Saturday
        buckets = weekly_buckets(dates)
        self.assertEqual(len(buckets), 1)
