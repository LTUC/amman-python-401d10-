from django.test import TestCase,SimpleTestCase
from django.urls import reverse

# Create your tests here.

class ThingsTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
