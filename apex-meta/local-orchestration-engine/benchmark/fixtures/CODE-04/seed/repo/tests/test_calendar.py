import datetime
import unittest

from apexcalc.calendar import week_start


class TestWeekStart(unittest.TestCase):
    def test_week_start_is_monday(self):
        # 2026-08-05 is a Wednesday; the ISO week start is Monday 2026-08-03.
        d = datetime.date(2026, 8, 5)
        self.assertEqual(week_start(d), datetime.date(2026, 8, 3))
        self.assertEqual(week_start(d).weekday(), 0)
