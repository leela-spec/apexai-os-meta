def prorate(amount_cents: int, used_days: int, period_days: int) -> int:
    """Prorate `amount_cents` over `used_days` of a `period_days` period.

    Rounds half-up to the nearest cent. `used_days` is clamped to
    [0, period_days]. Raises ValueError when `period_days` <= 0.
    """
    if period_days <= 0:
        raise ValueError("period_days must be positive")
    if used_days < 0:
        used_days = 0
    if used_days > period_days:
        used_days = period_days
    return (amount_cents * used_days + period_days // 2) // period_days
