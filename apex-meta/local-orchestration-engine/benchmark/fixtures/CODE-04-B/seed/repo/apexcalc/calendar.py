import datetime


def week_start(d):
    """Return the Monday (ISO week start) on or before `d`."""
    return d - datetime.timedelta(days=d.weekday())


def billing_week_start(d):
    """Return the Sunday on or before `d` -- the provider's billing week origin."""
    days_since_sunday = (d.weekday() + 1) % 7
    return d - datetime.timedelta(days=days_since_sunday)
