import datetime
from ulsosite.utils import academic_year_calc

CURRENT_SEASON = academic_year_calc(datetime.datetime.now())
