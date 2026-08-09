import datetime
import unittest

from apexcalc.report import format_money, render_week_label


class TestMoneyFormat(unittest.TestCase):
    def test_two_decimal_places(self):
        self.assertEqual(format_money(1250), "EUR 12.50")


class TestWeekLabel(unittest.TestCase):
    def test_week_label_matches_billing_week(self):
        # 2026-08-02 is a Sunday. The ISO (Monday-start) week label is "W31";
        # the provider's billing week (Sunday-start) label is "BW-2026-32".
        # This is the date on which the two conventions genuinely disagree.
        d = datetime.date(2026, 8, 2)
        self.assertEqual(render_week_label(d), "BW-2026-32")
