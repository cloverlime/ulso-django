import datetime as dt
from django.test import TestCase, Client
from django.urls import reverse

# TODO Tidy up names - make consistent
from website.forms.absence import AbsenceForm
from website.forms.audition_signup import AuditionSignUpForm
from website.forms.concerto_signup_form import ConcertoForm
from website.forms.contact import ContactForm
from website.forms.project_signup_form import ProjectSignUp

from status.models import Status
from ulsosite.models.people import Musician

class AuditionSignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.season = '2017/18'
        
        Status.objects.create(
            auditions_open=True,
            concerto_open=True,
            season=self.season
        )

        self.data = {
            'first_name': 'Jennifer',
            'last_name': 'Frost',
            'email': 'jellybelly@frost.com',
            'phone': '04728 395827',
            'uni': 'RAM',
            'other_uni': '',
            'year': '3',
            'returning_member': False,
            'instrument': 'Flute',
            'doubling': 'Piccolo, alto flute',
            'experience': 'RAM orchestras, Arch Sinfonia, 3 years NYO',
            'depping_policy': True,
            'privacy_policy': True,
            'notes': 'Available for audition in Oct',
            'season': self.season,
        }

    def test_valid_data(self):
        form = AuditionSignUpForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_wrong_instrument(self):
        self.data['instrument'] = 'Zither'
        form = AuditionSignUpForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_disagrees_with_privacy_policy(self):
        self.data['privacy_policy'] = False
        form = AuditionSignUpForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_disagrees_with_depping_policy(self):
        self.data['depping_policy'] = False
        form = AuditionSignUpForm(data=self.data)
        self.assertFalse(form.is_valid())    

    # Not a unit test...?
    def test_valid_form_saves_to_database(self):
        self.client.post('/auditions/signup/',data=self.data)

        entry_exists = Musician.objects.filter(
            first_name= self.data['first_name'],
            last_name= self.data['last_name'],
            instrument= self.data['instrument'],
            ).exists()

        self.assertTrue(entry_exists)    

    def test_invalid_form_does_not_save_to_database(self):
        self.data['instrument'] = 'Zither'
        self.client.post('/auditions/signup/',data=self.data)
        entry_exists = Musician.objects.filter(
            first_name= self.data['first_name'],
            last_name= self.data['last_name'],
            instrument= self.data['instrument'],
            ).exists()

        self.assertFalse(entry_exists)    

    # def test_redirects_after_POST(self):
    #     response = self.client.post('/', data={'item_text': 'A new list item'})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/')





class Forms(TestCase):
    def setUp(self):
        pass

    def test_concert_form(self):
        pass
    
    def test_contact_form(self):
        pass

    def test_absence_form(self):
        pass   

    def test_project_form(self):
        pass   
