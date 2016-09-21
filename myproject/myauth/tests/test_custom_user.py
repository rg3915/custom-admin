from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.auth import get_user_model


@override_settings(AUTH_USER_MODEL='myauth.User')
class FunctionalCustomUserTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        u = UserModel(email='regis.santos.100@gmail.com')
        u.set_password('1234')
        u.save()

    def test_login_with_email(self):
        self.assertTrue(self.client.login(
            email='regis.santos.100@gmail.com',
            password='1234'))
