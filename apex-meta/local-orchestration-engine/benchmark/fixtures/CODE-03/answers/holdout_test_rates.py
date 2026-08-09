import unittest

from apexcalc.rates import prorate


class TestProrateHoldout(unittest.TestCase):
    def test_holdout_cases(self):
        cases = [
            ((1, 1, 2), 1),
            ((3, 1, 2), 2),
            ((250, 3, 8), 94),
            ((1000, 7, 3), 1000),
            ((1000, -2, 3), 0),
            ((0, 5, 7), 0),
            ((999, 500, 999), 500),
            ((5, 1, 4), 1),
            ((7, 1, 3), 2),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual(prorate(*args), expected)


if __name__ == "__main__":
    unittest.main()
