"""
Useful functions across the board
"""
import datetime

def academic_year_calc(date_obj):
    """Takes a datetime object and returns a string of the
    academic year it belongs to.

    Args:
        date: a datetime object e.g. datetime(2017, 5, 3)

    Returns:
        str: the academic year that the date belongs to e.g. 2017/18
    """
    if date_obj.month < 7:
        return '{}/{}'.format(str(date_obj.year-1), str(date_obj.year-2000))

    else:
        return '{}/{}'.format(str(date_obj.year), str(date_obj.year-1999))

def format_date(date_obj):
    """Takes a date object and returns a readable string representation of the date in the format e.g Mon 17 Sep 18"""
    return datetime.datetime.strftime(date_obj, '%a %d %b %y')

def format_time(time_obj):
    """Takes a time object and returns a time in the format '7:30 pm'"""
    return datetime.time.strftime(time_obj, '%H:%M')



# show image preview in Admin
# NOT correct, currently
def image_tag(self):
    return '<img src={} />'.format(self.url)
# image_tag.short_description = 'Image'
# image_tag.allow_tags = True
