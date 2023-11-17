from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.paginators import HabitPaginator


class HabitCreateView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """ При создании привычки устанавливается связь с текущим пользователем. """
        serializer.save(user=self.request.user)


class HabitListView(generics.ListAPIView):
    """ Список привычек """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator


class HabitRetrieveView(generics.RetrieveAPIView):
    """ Просмотр привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(generics.UpdateAPIView):
    """ Редактирование привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()
