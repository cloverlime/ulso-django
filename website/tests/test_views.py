import datetime as dt
from django.test import TestCase, Client
from django.urls import reverse

from status.models import Status
from ulsosite.models.concerts import Concert
from ulsosite.models.people import CommitteeMember

from website.models import Page

class WebsiteViewsTestCase(TestCase):
    """Tests that all expected pages load with 200"""

    def setUp(self):
        """
        Sets up required database calls for the webpages.
        Also sets up the test client.
        """
        self.client = Client()
        
        self.season = '2017/18'

        Status.objects.create(
            auditions_open=True,
            concerto_open=True,
            season=self.season
        )

        Page.objects.create(title='About', body='')
        Page.objects.create(title='Rehearsals', body='')
        Page.objects.create(title='Contact Us', body='')
        Page.objects.create(title='Concerto Competition', body='')
        Page.objects.create(title='How to Join', body='')
        Page.objects.create(title='Join', body='')

        Concert.objects.create(
            current=True,
            season=self.season,
            project_term='Autumn 1',
            start_time=dt.time(hour=19, minute=00),
            date=dt.date(year=2017, month=11, day=17),
            conductor=None,
            soloist='',
            soloist_website='',
            concert_venue='St Stephen\'s',
        )

        CommitteeMember.objects.create(
            first_name='Stephen',
            last_name='Yates',
            email='chair@ulso.co.uk',
            phone='07398 345286',
            instrument='Violin', 
            uni='GSDM', 
            role='Chair', 
            season=self.season, 
            description='Hi I\'m Chair!',
        )
                
    def test_wrong_url(self):
        response = self.client.get('/iamwrong')
        self.assertEqual(response.status_code, 404)    

    def test_index(self):
        # A static page
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_rehearsals(self):
        response = self.client.get(reverse('rehearsals'))
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_concerto(self):
        response = self.client.get(reverse('concerto'))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_join(self):
        response = self.client.get(reverse('join'))
        self.assertEqual(response.status_code, 200)

    def test_audition_signup(self):
        response = self.client.get(reverse('audition_signup'))
        self.assertEqual(response.status_code, 200)

    def test_concerto_signup(self):
        response = self.client.get(reverse('concerto_signup'))
        self.assertEqual(response.status_code, 200)

    def test_absence_form(self):
        response = self.client.get(reverse('absence_form'))
        self.assertEqual(response.status_code, 200)

    def test_project_signup(self):
        response = self.client.get(reverse('project_signup'))
        self.assertEqual(response.status_code, 200)