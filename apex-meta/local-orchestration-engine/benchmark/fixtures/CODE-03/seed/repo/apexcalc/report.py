def render_week_label(d):
    """Render the ISO week label, e.g. 'W31'."""
    _, week, _ = d.isocalendar()
    return f"W{week:02d}"


def format_money(cents):
    """Format integer cents as 'EUR X.YY'."""
    return f"EUR {cents / 100:.2f}"
