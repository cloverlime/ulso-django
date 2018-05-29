"""
Useful functons across the board
"""
import datetime

def academic_year_calc(date):
    """Takes a datetime object and returns a string of the
    academic year it belongs to.

    Args:
        date: a datetime object e.g. datetime(2017, 5, 3)

    Returns:
        str: the academic year that the date belongs to e.g. 2017/18
    """
    if date.month < 7:
        return '{}/{}'.format(str(date.year-1), str(date.year-2000))

    else:
        return '{}/{}'.format(str(date.year), str(date.year-1999))
