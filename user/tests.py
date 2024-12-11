from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from user.models import User
from takimlar.models import Takim

class KullaniciGirisTest(TestCase):
    def setUp(self):
        self.takim = Takim.objects.create(isim="Test Takımı", takim_tipi="MONTAJ")
        self.kullanici = User.objects.create(username="testkullanici", password=make_password("sifre123"), takim=self.takim)


    def test_login_view_post_gecerli(self):
        response = self.client.post(reverse('login'), {'username': 'testkullanici', 'password': 'sifre123'})
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_view_post_gecersiz_kullanici_adi(self):
        response = self.client.post(reverse('login'), {'username': 'yanliskullanici', 'password': 'sifre123'})
        self.assertContains(response, 'User does not exist')

    def test_login_view_post_gecersiz_sifre(self):
        response = self.client.post(reverse('login'), {'username': 'testkullanici', 'password': 'yanlissifre'})
        self.assertContains(response, 'Invalid username or password')


class DashboardTest(TestCase):
    def setUp(self):
        self.takim = Takim.objects.create(isim="Test Takımı", takim_tipi="MONTAJ")
        self.kullanici = User.objects.create(username="testkullanici", password=make_password("sifre123"), takim=self.takim)
        self.client.login(username="testkullanici", password="sifre123")


class LogoutTest(TestCase):
    def setUp(self):
        self.takim = Takim.objects.create(isim="Test Takımı", takim_tipi="MONTAJ")
        self.kullanici = User.objects.create(username="testkullanici", password=make_password("sifre123"), takim=self.takim)
        self.client.login(username="testkullanici", password="sifre123")

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
