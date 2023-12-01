from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from users.models import User


class SuperuserTestCase(APITestCase):
    """Тесты суперюзера"""
    def setUp(self) -> None:
        """Подготовка данных перед тестом"""
        self.user = User.objects.create(
                        email='test@user.com',
                    )
        self.user.set_password('123')
        self.user.save()
        # response = self.client.post('/api/token/', {"email": "test@user.com", "password": "123"})
        # self.access_token = response.json().get('access')
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_authorization(self):
        """Тест суперюзера"""
        # response = self.client.get('/users/')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'email': self.user.email,
            'password': self.user.password,
        }

        response = self.client.post(
            reverse('users:token_obtain_pair'),
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
