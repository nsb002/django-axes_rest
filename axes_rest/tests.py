from django.test import TestCase, RequestFactory

from django.contrib.auth.models import User
from django.test.client import Client

from django.apps import apps

userpswd = 'a_very_cryptic_password'
username = 'testuser'

# tests go here
class LoginTests(TestCase):
    def test_accessLog(self):
        """
        Create a super user and check if the access is logged.
        """
        u = User.objects.create_superuser(username=username, email='user@test.com', password=userpswd)
        u.save()

        factory = RequestFactory()
        
        self.client.login(username=username, password=userpswd, request=factory.request())
        
        model = apps.get_model('axes', 'AccessLog')
        accessLog_list = model.objects.all()
        
        self.assertTrue(accessLog_list[0].username, username)
    
    def test_accessAttempt(self):
        """
        Try to log in with a fake user and check if the attempt is logged.
        """
        fake_username = 'bob'
        fake_userpswd = 'not_the_real_pswd'

        factory = RequestFactory()
        
        self.client.login(username=fake_username, password=fake_userpswd, request=factory.request())
        
        model = apps.get_model('axes', 'AccessAttempt')
        accessAttempt_list = model.objects.all()
        
        self.assertEqual(accessAttempt_list[0].username, fake_username)