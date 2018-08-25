import unittest
import datetime as dt

from django.test import TestCase

from ulsosite.utils import (
    academic_year_calc,
    format_date,
    format_time
)

class AcademicYearCalcTestCase(TestCase):
    """Tests the function academic_year_calc(date) with a range of dates"""
    def test_before_1000(self):
        date = dt.date(year=980, month=3, day=15)
        season = academic_year_calc(date)
        self.assertEqual(season, '979/80')

    def test_millennium(self):
        date = dt.date(year=999, month=7, day=15)
        season = academic_year_calc(date)
        self.assertEqual(season, '999/00')

    def test_before_jul(self):
        date = dt.date(year=2018, month=3, day=15)
        season = academic_year_calc(date)
        self.assertEqual(season, '2017/18')

    def test_after_jul(self):
        date = dt.date(year=2018, month=8, day=15)
        season = academic_year_calc(date)
        self.assertEqual(season, '2018/19')


class DateFormatTestCase(TestCase):
    def test_format_date(self):
        date = dt.date(year=2018, month=8, day=23)
        formatted = format_date(date)
        self.assertEqual(formatted, 'Thu 23 Aug 18')

    def test_format_time(self):
        time = dt.time(hour=13, minute=30)
        formatted = format_time(time)
        self.assertEqual(formatted, '13:30')