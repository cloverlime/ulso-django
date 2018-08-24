import datetime as dt

from django.test import TestCase

from ulsosite.models.auditions import (
    AuditionDate,
    AuditionSlot
)

from ulsosite.models.people import Musician

class AuditionsTestCase(TestCase):
    def setUp(self):
        # Create audition day
        self.audition_date = AuditionDate.objects.create(
            date=dt.date(year=2018, month=9, day=23),
            panel1='Ling Ling',
            panel2='',
            panel3='',
            panel4='',
            location='Strand Campus, King\'s College London, Strand, WC2R 2LS',
            season='',
            notes='',
        )
        # Create empty slot
        self.slot = AuditionSlot.objects.create(
            date=self.audition_date,
            time=dt.time(hour=10, minute=15),
            musician=None, 
            first_name='',
            last_name='',
            instrument='',
            verdict='',
            notes='',
        )
        # Create a musician
        self.musician = Musician.objects.create(
            first_name='Stacey',
            last_name='Lewis',
            alias='Lacey',
            email='stacey@lewis.net',
            phone='06879 034246',
            instrument='Bassoon',
            doubling='Contrabassoon',
            uni='RCM',
            other_uni='',
            status='Candidate',
            year='5',
            experience='NYO, RCM orchestras, London Mahler Orchestra, ULSO 2 years',
            returning_member=True,
            subs_paid=False,
            depping_policy=True,
            privacy_policy=True,
            season='',
            notes='Available for all audition dates',
        )

    def test_audition_date_creates_season(self):
        self.assertIsNotNone(self.audition_date.season)

    def test_find_musician_from_name_and_instrument(self):
        # arrange
        self.slot.first_name='Stacey'
        self.slot.last_name='Lewis'
        self.slot.instrument='Bassoon'

        # act
        self.slot.save()

        # assert 
        self.assertEqual(self.slot.musician, self.musician)

    def test_fill_in_names_from_musician_model(self):
        # arrange
        self.slot.musician = self.musician

        # act
        self.slot.save()

        # assert
        self.assertEqual(self.slot.first_name, 'Stacey')
        self.assertEqual(self.slot.last_name, 'Lewis')
        self.assertEqual(self.slot.instrument, 'Bassoon')

    def test_change_verdict_to_member_changes_musician_status(self):
        self.slot.musician = self.musician
        self.slot.verdict = 'Member'
        self.slot.save()

        self.assertEqual(self.musician.status, 'Member')

    def test_change_verdict_to_rejected_changes_musician_status(self):
        self.slot.musician = self.musician
        self.slot.verdict = 'Rejected'
        self.slot.save()

        self.assertEqual(self.musician.status, 'Rejected')
    
    def test_change_verdict_to_reserve_changes_musician_status(self):
        self.slot.musician = self.musician
        self.slot.verdict = 'Reserve'
        self.slot.save()

        self.assertEqual(self.musician.status, 'Reserve')