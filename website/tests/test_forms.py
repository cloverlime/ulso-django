import datetime as dt
import unittest
from django.test import TestCase, Client, tag
from django.urls import reverse
from django.core import mail

# TODO Tidy up names - make consistent
from website.forms.absence import AbsenceForm
from website.forms.audition_signup import AuditionSignUpForm
from website.forms.concerto_signup_form import ConcertoForm
from website.forms.contact import ContactForm
from website.forms.project_signup_form import ProjectSignUp

from status.models import Status
from ulsosite.models.people import Musician, ConcertoApplicant
from ulsosite.models.concerts import (
    Concert, Rehearsal, Absence
)


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

    @tag('integration')
    def test_valid_form_saves_to_database(self):
        self.client.post('/auditions/signup/',data=self.data)

        entry_exists = Musician.objects.filter(
            first_name= self.data['first_name'],
            last_name= self.data['last_name'],
            instrument= self.data['instrument'],
            ).exists()

        self.assertTrue(entry_exists)    

    @tag('integration')
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


class ConcertoSignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.season = '2017/18'
        
        Status.objects.create(
            auditions_open=True,
            concerto_open=True,
            season=self.season
        )

        self.data = {
            'first_name': 'Max',
            'last_name': 'Bagel',
            'email': 'bread@donut.com',
            'instrument': 'Cello',
            'phone': '07623 982627',
            'piece': 'Dvorak Cello Concerto',
            'years_ulso_member': '2012-17',
            'notes': '',
        }

    def test_valid_data(self):
        form = ConcertoForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        self.data['first_name'] = ''
        form = ConcertoForm(data=self.data)
        self.assertFalse(form.is_valid())

    @tag('integration')
    def test_valid_form_saves_to_database(self):
        self.client.post('/concerto/signup/',data=self.data)

        entry_exists = ConcertoApplicant.objects.filter(
            first_name= self.data['first_name'],
            last_name= self.data['last_name'],
            instrument= self.data['instrument'],
            email=self.data['email'],
            ).exists()

        self.assertTrue(entry_exists)    

    @tag('integration')
    def test_invalid_form_does_not_save_to_database(self):
        self.data['first_name'] = ''
        self.client.post('/auditions/signup/',data=self.data)
        entry_exists = ConcertoApplicant.objects.filter(
            first_name= self.data['first_name'],
            last_name= self.data['last_name'],
            instrument= self.data['instrument'],
            email=self.data['email'],
            ).exists()

        self.assertFalse(entry_exists)    


    # def test_redirects_after_POST(self):
    #     response = self.client.post('/', data={'item_text': 'A new list item'})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/')


class ContactFormTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.data = {
            'name': 'Moo Baa',
            'email': 'moomoo@baa.com',
            'topic': 'Website',
            'subject': 'TEST!',
            'message': 'TEST TEST TEST',
            'send_self': False,
        }

    def test_valid_data(self):
        form = ContactForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        self.data['name'] = ''
        form = ContactForm(data=self.data)
        self.assertFalse(form.is_valid())

    # TODO Split up?
    @tag('integration')
    def test_valid_form_sends_email(self):
        self.client.post('/contact/',data=self.data)
        
        # Sends one message
        self.assertEqual(len(mail.outbox), 1)
        
        # From sender's email
        self.assertEqual(mail.outbox[0].from_email, self.data['email'])
        
        # Check length of recipients is 2 (if subject is website)
        self.assertEqual(len(mail.outbox[0].to), 2)
        
        # Check length of reciplients includes chair
        self.assertTrue('chair@ulso.co.uk' in mail.outbox[0].to)
       
        # Check subject
        self.assertEqual(mail.outbox[0].subject, 'WEBSITE: ' + self.data['subject'])

    @tag('integration')
    def test_self_sends_more_emails(self):
        self.data['send_self'] = True
        self.client.post('/contact/',data=self.data)
        self.assertEqual(mail.outbox[0].cc, [self.data['email']])       

    @tag('integration')
    def test_invalid_form_does_not_send_email(self):
        self.data['name'] = ''
        self.client.post('/auditions/signup/',data=self.data)
        self.assertEqual(len(mail.outbox), 0)            


class AbsenceFormTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.concert = Concert.objects.create(
            current=True,
            season='2018/19',
            project_term='Autumn 1',
            start_time=dt.time(hour=19, minute=00),
            date=dt.date(year=2017, month=11, day=17),
            conductor=None,
            soloist='',
            soloist_website='',
            concert_venue='St Stephen\'s',
        )
        
        self.rehearsal = Rehearsal.objects.create(
            concert=self.concert,
            date=dt.date(year=2018, month=10, day=23),
            start_time=dt.time(hour=19, minute=00),
            end_time=dt.time(hour=22, minute=00),
            rehearsal_venue='St Stephen\'s',
            notes='',
        )

        self.data = {
            'rehearsal': self.rehearsal.id,
            'first_name': 'Nyancat',
            'last_name': 'Poptart',
            'email': 'nyan@meow.com',
            'instrument': 'Harp',
            'dep_name': 'Grumpy Cat',
            'dep_email': 'sadkitty@cat.com',
            'dep_phone': '02345 826438',
            'reasons': 'I am too sad today.',
        }

    # TODO FIX THIS
    @unittest.skip
    def test_valid_data(self):
        # print(f"id: {self.rehearsal.id}")
        print(self.data['rehearsal'])
        form = AbsenceForm(data=self.data)
        form.is_valid()
        print(form.errors)
        self.assertTrue(form.is_valid())

    # TODO FIX THIS
    @unittest.skip
    def test_invalid_data(self):
        self.data['rehearsal'] = None
        form = AbsenceForm(data=self.data)
        self.assertFalse(form.is_valid())

    @tag('integration')
    def test_valid_form_saves_to_database(self):
        pass    

    @tag('integration')
    def test_invalid_form_does_not_save_to_database(self):
        pass   


class ProjectSignUpTestCase(TestCase):
    def setUp(self):
        pass

    def test_valid_data(self):
        pass

    def test_invalid_data(self):
        pass

    @tag('integration')
    def test_valid_form_saves_to_database(self):
        pass   

    @tag('integration')
    def test_invalid_form_does_not_save_to_database(self):
        pass
