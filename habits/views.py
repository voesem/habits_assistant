from rest_framework import generics

from habits.models import Habit
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer, PublicHabitSerializer
from habits.paginators import HabitPaginator
from habits.services import create_habit_schedule


class HabitCreateView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """
        При создании привычки устанавливается связь с текущим пользователем
        и создается задача на отправку уведомлений в телеграме.
        """
        serializer.save(user=self.request.user)
        habit = serializer.save()
        create_habit_schedule(habit)


class HabitListView(generics.ListAPIView):
    """ Список привычек """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            # Стаффу и суперпользователю доступен весь список привычек.
            return Habit.objects.all()
        else:
            # Обычным пользователям доступны только созданные ими привычки.
            return Habit.objects.filter(user=user.pk)


class PublicHabitListView(generics.ListAPIView):
    """ Список привычек, имеющих признак публичных """

    serializer_class = PublicHabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator


class HabitRetrieveView(generics.RetrieveAPIView):
    """ Просмотр привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class HabitUpdateView(generics.UpdateAPIView):
    """ Редактирование привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class HabitDestroyView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
