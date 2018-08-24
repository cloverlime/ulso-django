import datetime

from django.test import TestCase

from ulsosite.models.people import (
    Musician,
    CommitteeMember,
    ConcertoApplicant,
    ConcertoWinner,
    Conductor,
    UsefulContact
)

class MusicianTestCase(TestCase):
    def setUp(self):
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

    def test_string_representation(self):
        string = self.musician.__str__()
        self.assertEquals(string, 'Stacey Lewis')

    def test_has_attributes(self):
        """Tests that all the attributes are as expected"""
        pass

    def test_has_creation_date(self):
        self.assertIsNotNone(self.musician.created)

    def test_has_modification_date(self):
        self.assertIsNotNone(self.musician.modified)

    def test_has_season(self):
        # Was initialised without a season but one should be auto-saved
        self.assertIsNotNone(self.musician.season)


def MusicianFromDictTestCase(TestCase):
    DICT = []

    def setUp(self):
        pass

    # Run all the same tests as above but with the newly created one    