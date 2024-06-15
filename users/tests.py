from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

USERNAME = 'testuser'
PASSWORD = 'Secret.x86'

class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': USERNAME,
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        self.assertEqual(response.status_code, 302)  # Redirect dopo la registrazione
        self.assertTrue(get_user_model().objects.filter(username=USERNAME).exists()) # L'utente qua deve esistere


class UserLoginTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username=USERNAME, password=PASSWORD)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200) # HTTP Ok status dopo richiesta pagina
        self.assertTemplateUsed(response, 'users/login.html') # controllo del template usato

    def test_login(self):
        login = self.client.login(username=USERNAME, password=PASSWORD) # login vera e propria
        self.assertTrue(login)
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200) # HTTP Ok status dopo login

    def test_logout(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        response = self.client.post(reverse('logout')) # Richiesta HTTP per logout
        self.assertRedirects(response, reverse('login')) # Risposta di redirect dopo logout