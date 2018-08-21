from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ulsosite.models.concerts import Concert

class WebsiteViewsTestCase(TestCase):
    """Tests that all webpages load with 200"""

    fixtures = ['ulsosite/fixtures/test_fixture']

    def setUp(self):
        """
        Sets up required database calls for the webpages.
        Also sets up the test client.
        """
        self.client = Client()

        # conductor = Conductor.objects.create(
        #     first_name='Daniel',
        #     last_name='Capps,
        #     email='danielcapps@gmail.com',
        #     phone='01234 567890',
        #     website='danielcapps.com',
        # )

        # concert = Concert.objects.create(
        #     current=True,
        #     season="2018/19",
        #     project_term="Autumn",
        #     start_time="19:00:00",
        #     date=""
        #     conductor=
        #     concert_venue="St Stephen's Church"
        # )

    def test_response(self):
        print(self.client.get(reverse('index')))

        # response = self.client.get('/')
        # self.assertEqual(response.status_code, 200)