from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from newspaper.news.models import News


class NewsTestCase(TestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def authentication(self):
        user, is_created = User.objects.get_or_create(username='admin')
        if is_created:
            user.is_superuser = True
            user.set_password('admin')
            user.save()
        self.client.login(username='admin', password='admin')

    def test_newslist(self):
        news = News.objects.create(title='Mi noticia test',
                                   description='Mi descripcion test',
                                   publish_date=datetime.now())
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(news.title, response.content)
        self.assertIn(news.description, response.content)
        self.assertNotIn('ESTA CADENA NO SE ENCUENTRA EN EL RESPONSE',
                         response.content)

    def test_news_add(self):
        self.authentication()
        response1 = self.client.get(reverse('news_add'))
        self.assertEqual(response1.status_code, 200)
        self.assertIn('TEXTO DE AYUDA', response1.content)

        news_title = 'Mi noticia test 2'
        news_description = 'Mi descripcion test 2'
        data = {'title': news_title,
                'description': news_description,
                'publish_date': datetime.now()}
        response2 = self.client.post(reverse('news_add'),
                                     data=data)
        self.assertEqual(response2.status_code, 302)

        response3 = self.client.get(reverse('news_list'))
        self.assertIn(news_title, response3.content)
        self.assertIn(news_description, response3.content)