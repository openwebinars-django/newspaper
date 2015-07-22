from datetime import datetime

from django.test import TestCase
from django.test.client import Client

from newspaper.news.models import News


class NewsTestCase(TestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def test_newslist(self):
        news = News.objects.create(title='Mi noticia test',
                                   description='Mi descripcion test',
                                   publish_date=datetime.now())
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(news.title, response.content)
        self.assertIn(news.description, response.content)
        self.assertNotIn('ESTA CADENA NO SE ENCUENTRA EN EL RESPONSE',
                         response.content)
