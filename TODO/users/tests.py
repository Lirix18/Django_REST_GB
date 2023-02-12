from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import MyUserViewSet
from .models import MyUser
from mixer.backend.django import mixer


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = MyUser.objects.create_superuser(username='Anna', password='123123')
        self.author = MyUser.objects.create(first_name="Админ", last_name="Админович", birthday_year=1980,
                                            email="admin1@admin1.ru")

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = MyUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = MyUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class UserClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = MyUser.objects.create_superuser(username='Anna', password='123123')
        self.author = MyUser.objects.create(first_name="Админ", last_name="Админович", birthday_year=1980,
                                            email="admin1@admin1.ru")

    def test_get_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_1(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
