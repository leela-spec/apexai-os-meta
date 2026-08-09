import unittest

from apexcalc.report import format_money


class TestMoneyFormat(unittest.TestCase):
    def test_two_decimal_places(self):
        self.assertEqual(format_money(1250), "EUR 12.50")
