from rest_framework.serializers import ValidationError
from datetime import time


def habit_validator(value):
    # Валидация одновременного выбора связанной привычки и указания вознаграждения.
    if value.get('related_habit') and value.get('reward'):
        raise ValidationError('Исключён одновременный выбор связанной привычки и указания вознаграждения.')

    # Валидация связанной привычки.
    if value.get('related_habit') is None:
        pass
    elif not value.get('related_habit').is_pleasant:
        raise ValidationError('Можно связать только с приятной привычкой.')

    # Валидация приятной привычки.
    if (value.get('reward') or value.get('related_habit')) is None:
        pass
    elif value.get('is_pleasant') is True and (value.get('reward') or value.get('related_habit')):
        raise ValidationError('Приятная привычка не может иметь вознаграждения или связанной привычки.')

    # Валидация частоты выполнения привычки.
    if value.get('periodicity') is None:
        pass
    elif value.get('periodicity') < 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

    # Валидация времени, требуемого для выполнения привычки.
    if value.get('to_complete') is None:
        pass
    elif value.get('to_complete') > time(00, 2):
        raise ValidationError('Время выполнения должно быть не больше 120 секунд.')
