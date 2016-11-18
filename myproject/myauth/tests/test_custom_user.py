from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings


class FunctionalCustomUserTest(TestCase):

    def setUp(self):
        self.user_data = {
            # 'username': None,
            'email': 'regis.santos.100@gmail.com',
            'password': '12345678'
        }
        self.User = get_user_model()

    def test_auth_user_model(self):
        self.assertEqual(settings.AUTH_USER_MODEL, 'myauth.User')

    def test_create_user(self):
        fields = ('email', 'password')
        create_data = {k: v for k, v in self.user_data.items() if k in fields}
        self.assertEqual(0, self.User.objects.count())
        self.User.objects.create(**self.user_data)
        self.assertEqual(1, self.User.objects.count())

    def test_login_with_email(self):
        login_data = {
            'email': self.user_data.get('email'),
            'password': self.user_data.get('password')
        }
        self.assertTrue(self.client.login(**login_data))
