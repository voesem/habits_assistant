from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    """
    Модель Привычки

    Поля:
    user: создатель привычки (через внешний ключ на пользователя).
    place: место, в котором необходимо выполнять привычку.
    time: время, когда необходимо выполнять привычку.
    action: действие, которое представляет собой привычка.
    is_pleasant: привычка, которую можно привязать к выполнению полезной привычки.
    related_habit: привычка, связанная с другой привычкой.
    periodicity: периодичность выполнения привычки для напоминания в днях (по умолчанию 1 - ежедневная).
    reward: чем пользователь должен себя вознаградить после выполнения.
    to_complete: время, которое предположительно потратит пользователь на выполнение привычки.
    is_public: признак публичности привычки для общего доступа.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')
    place = models.CharField(max_length=150, verbose_name='место выполнения')
    time = models.TimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    to_complete = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        """
        :return: описание привычки в виде строки.
        """
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
