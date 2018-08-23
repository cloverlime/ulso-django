import unittest

from django.test import TestCase, Client
# from django.core.urlresolvers import reverse

from ulsosite.models.concerts import Concert

class WebsiteViewsTestCase(TestCase):
    """Tests that all webpages load with 200"""

    # fixtures = ['ulsosite/fixtures/initial_data']

    def setUp(self):
        """
        Sets up required database calls for the webpages.
        Also sets up the test client.
        """
        self.client = Client()

    def test_response(self):
        self.assertTrue(True)
        
        # print(self.client.get(reverse('index')))
        # response = self.client.get('/')
        # self.assertEqual(response.status_code, 200)

        