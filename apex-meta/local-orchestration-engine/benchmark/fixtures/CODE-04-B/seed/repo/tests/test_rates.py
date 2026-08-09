import unittest

from apexcalc.rates import prorate


class TestProrate(unittest.TestCase):
    def test_prorate_full_period(self):
        self.assertEqual(prorate(1000, 3, 3), 1000)

    def test_prorate_zero_days(self):
        self.assertEqual(prorate(1000, 0, 3), 0)

    def test_prorate_clamps_negative_days(self):
        self.assertEqual(prorate(1000, -2, 3), 0)

    def test_prorate_clamps_excess_days(self):
        self.assertEqual(prorate(1000, 7, 3), 1000)

    def test_prorate_rejects_nonpositive_period(self):
        with self.assertRaises(ValueError):
            prorate(1000, 1, 0)

    def test_prorate_rounds_half_up(self):
        self.assertEqual(prorate(1000, 1, 3), 333)
        self.assertEqual(prorate(1000, 2, 3), 667)
        self.assertEqual(prorate(101, 1, 2), 51)
