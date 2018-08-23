"""
Useful functions across the board
"""
import datetime as dt

def academic_year_calc(date_obj):
    """Takes a date or datetime object and returns a string of the
    academic year it belongs to. 
    
    The academic year is defined as starting from July.

    Args:
        date: a datetime object e.g. datetime(2017, 5, 3)

    Returns:
        str: the academic year that the date belongs to e.g. 2017/18
    """
    if date_obj.month < 7:
        return '{}/{}'.format(
            dt.datetime.strftime(date_obj - dt.timedelta(days=365), '%Y'),
            dt.datetime.strftime(date_obj, '%y'),
        )
    else:
        return '{}/{}'.format(
            dt.datetime.strftime(date_obj, '%Y'),
            dt.datetime.strftime(date_obj + dt.timedelta(days=365), '%y'),
        )


def format_date(date_obj):
    """Takes a date object and returns a readable string representation of the date in the format e.g Mon 17 Sep 18"""
    return dt.datetime.strftime(date_obj, '%a %d %b %y')


def format_time(time_obj):
    """Takes a time object and returns a time in the 24 h format '19:30'"""
    return dt.time.strftime(time_obj, '%H:%M')



# show image preview in Admin
# NOT correct, currently
def image_tag(self):
    return '<img src={} />'.format(self.url)
# image_tag.short_description = 'Image'
# image_tag.allow_tags = True
