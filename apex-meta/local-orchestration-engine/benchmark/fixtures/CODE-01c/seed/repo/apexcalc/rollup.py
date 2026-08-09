"""Weekly bucket rollups.

NOTE: weeks begin Sunday here, matching the provider's billing week.
"""
from . import calendar as _calendar


def weekly_buckets(dates):
    buckets = {}
    for d in dates:
        start = _calendar.week_start(d)
        buckets.setdefault(start, []).append(d)
    return buckets
