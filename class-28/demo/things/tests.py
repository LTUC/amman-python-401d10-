from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Thing
from django.contrib.auth import get_user_model


class ThingsTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('things')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('things')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'things.html')
        self.assertTemplateUsed(response, 'base.html')

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )

        self.thing = Thing.objects.create(
            name='test',
            rating=1,
            desc="test info",
            reviewer = self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.thing),"test")

    def test_detail_view(self):
        url = reverse('thing_detail', args=[self.thing.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'thing_details.html')

    def test_create_view(self):
        obj={
            'name':"test2",
            'rating':5,
            'desc': "info...",
            'reviewer': self.user.id
        }

        url = reverse('thing_create')
        response = self.client.post(path=url,data=obj,follow=True)
        # self.assertEqual(len(Thing.objects.all()),2)
        self.assertRedirects(response, reverse('thing_detail', args=[2]))


    

    
