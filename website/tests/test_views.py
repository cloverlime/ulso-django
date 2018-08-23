import unittest

from django.test import TestCase, Client
from django.urls import reverse

from ulsosite.models.concerts import Concert

class WebsiteViewsTestCase(TestCase):
    """Tests that all expected pages load with 200"""

    def setUp(self):
        """
        Sets up required database calls for the webpages.
        Also sets up the test client.
        """
        self.client = Client()

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

    # def test_contact(self):
    #     response = self.client.get(reverse('contact'))
    #     self.assertEqual(response.status_code, 200)

    # def test_concerto(self):
    #     response = self.client.get(reverse('concerto'))
    #     self.assertEqual(response.status_code, 200)

    # def test_about(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertEqual(response.status_code, 200)

    # def test_join(self):
    #     response = self.client.get(reverse('join'))
    #     self.assertEqual(response.status_code, 200)

    # def test_audition_signup(self):
    #     response = self.client.get(reverse('audition_signup'))
    #     self.assertEqual(response.status_code, 200)

    # def test_concerto_signup(self):
    #     response = self.client.get(reverse('concerto_signup'))
    #     self.assertEqual(response.status_code, 200)

    # def test_absence_form(self):
    #     response = self.client.get(reverse('absence_form'))
    #     self.assertEqual(response.status_code, 200)

    # def test_project_signup(self):
    #     response = self.client.get(reverse('project_signup'))
    #     self.assertEqual(response.status_code, 200)