from django.test import TestCase
from django.test.client import Client
from authapp.models import User
from django.core.management import call_command


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')

        self.user = User.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')

    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title'], 'главная')
        self.assertNotContains(response, 'Пользователь', status_code=200)

        self.client.login(username='tarantino', password='geekbrains')

        response = self.client.get('/authapp/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        response = self.client.get('/')
        self.assertContains(response, 'Пользователь', status_code=200)
        self.assertEqual(response.context['user'], self.user)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp')
