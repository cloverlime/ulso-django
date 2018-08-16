from django.test import TestCase, Client

class HomepageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response(self):
        print(self.client.get('/'))