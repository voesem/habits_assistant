from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    """ Тестирование модели Habit """

    def setUp(self) -> None:
        """ Первичные данные для тестов """

        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='123')
        self.client.force_authenticate(user=self.user)

        self.habit_1 = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='07:00:00',
            action='Сделать зарядку',
            periodicity=3,
            to_complete='00:01:00',
            is_public=True
        )

        self.habit_2 = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='07:10:00',
            action='Почистить зубы',
            periodicity=3,
            to_complete='00:01:00',
            related_habit=self.habit_1
        )

        self.habit_3 = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='07:15:00',
            action='Сделать 50 отжиманий',
            periodicity=3,
            to_complete='00:03:00',
        )

        self.habit_4 = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='07:20:00',
            action='Полежать',
            periodicity=4,
            to_complete='00:01:00',
            is_pleasant=True,
            reward='Еще полежать'
        )

    def test_habit_create(self):
        """ Тест создания привычки """

        data_1 = {
            'user': self.user.pk,
            'place': self.habit_1.place,
            'time': self.habit_1.time,
            'action': self.habit_1.action,
            'periodicity': self.habit_1.periodicity,
            'to_complete': self.habit_1.to_complete,
            'is_public': True
        }

        data_2 = {
            'user': self.user.pk,
            'place': self.habit_2.place,
            'time': self.habit_2.time,
            'action': self.habit_2.action,
            'periodicity': self.habit_2.periodicity,
            'to_complete': self.habit_2.to_complete,
            'related_habit': self.habit_1.pk
        }

        data_3 = {
            'user': self.user.pk,
            'place': self.habit_3.place,
            'time': self.habit_3.time,
            'action': self.habit_3.action,
            'periodicity': self.habit_3.periodicity,
            'to_complete': self.habit_3.to_complete,
        }

        data_4 = {
            'user': self.user.pk,
            'place': self.habit_4.place,
            'time': self.habit_4.time,
            'action': self.habit_4.action,
            'periodicity': self.habit_4.periodicity,
            'to_complete': self.habit_4.to_complete,
            'is_pleasant': self.habit_4.is_pleasant,
            'reward': self.habit_4.reward
        }

        response_1 = self.client.post(
            reverse('habits:create_habit'),
            data=data_1
        )

        response_2 = self.client.post(
            reverse('habits:create_habit'),
            data=data_2
        )

        response_3 = self.client.post(
            reverse('habits:create_habit'),
            data=data_3
        )

        response_4 = self.client.post(
            reverse('habits:create_habit'),
            data=data_4
        )

        self.assertEqual(
            response_1.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response_2.status_code,
            status.HTTP_400_BAD_REQUEST  # Срабатывает валидатор (связанная привычка может быть только приятной)
        )

        self.assertEqual(
            response_3.status_code,
            status.HTTP_400_BAD_REQUEST  # Срабатывает валидатор (по времени выполнения привычки)
        )

        self.assertEqual(
            response_4.status_code,
            status.HTTP_400_BAD_REQUEST  # Срабатывает валидатор (приятная привычка не может иметь вознаграждения)
        )

    def test_habits_list(self):
        """ Тест списка привычек """

        response = self.client.get(
            reverse('habits:habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 4,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.habit_1.pk,
                        'user': self.user.pk,
                        'place': self.habit_1.place,
                        'time': self.habit_1.time,
                        'action': self.habit_1.action,
                        'is_pleasant': False,
                        'related_habit': None,
                        'periodicity': self.habit_1.periodicity,
                        'reward': None,
                        'to_complete': self.habit_1.to_complete,
                        'is_public': True
                    },
                    {
                        'id': self.habit_2.pk,
                        'user': self.user.pk,
                        'place': self.habit_2.place,
                        'time': self.habit_2.time,
                        'action': self.habit_2.action,
                        'is_pleasant': False,
                        'related_habit': self.habit_1.pk,
                        'periodicity': self.habit_2.periodicity,
                        'reward': None,
                        'to_complete': self.habit_2.to_complete,
                        'is_public': False
                    },
                    {
                        'id': self.habit_3.pk,
                        'user': self.user.pk,
                        'place': self.habit_3.place,
                        'time': self.habit_3.time,
                        'action': self.habit_3.action,
                        'is_pleasant': False,
                        'related_habit': None,
                        'periodicity': self.habit_3.periodicity,
                        'reward': None,
                        'to_complete': self.habit_3.to_complete,
                        'is_public': False
                    },
                    {
                        'id': self.habit_4.pk,
                        'user': self.user.pk,
                        'place': self.habit_4.place,
                        'time': self.habit_4.time,
                        'action': self.habit_4.action,
                        'is_pleasant': True,
                        'related_habit': None,
                        'periodicity': self.habit_4.periodicity,
                        'reward': self.habit_4.reward,
                        'to_complete': self.habit_4.to_complete,
                        'is_public': False
                    }
                ]
            }
        )

    def test_view_habit(self):
        """ Тест просмотра привычки """

        response = self.client.get(
            reverse('habits:view_habit', kwargs={'pk': self.habit_1.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.habit_1.pk,
                'user': self.user.pk,
                'place': self.habit_1.place,
                'time': self.habit_1.time,
                'action': self.habit_1.action,
                'is_pleasant': False,
                'related_habit': None,
                'periodicity': self.habit_1.periodicity,
                'reward': None,
                'to_complete': self.habit_1.to_complete,
                'is_public': True
            }
        )

    def test_public_habits_list(self):
        """ Тест списка привычек, имеющих признак публичных """

        response = self.client.get(
            reverse('habits:public_habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.habit_1.pk,
                        'user': self.user.pk,
                        'place': self.habit_1.place,
                        'time': self.habit_1.time,
                        'action': self.habit_1.action,
                        'is_pleasant': False,
                        'related_habit': None,
                        'periodicity': self.habit_1.periodicity,
                        'reward': None,
                        'to_complete': self.habit_1.to_complete,
                        'is_public': True
                    }
                ]
            }
        )
