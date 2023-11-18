from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class PublicHabitSerializer(serializers.ModelSerializer):
    """ Сериализатор списка привычек, имеющих признак публичных """

    class Meta:
        model = Habit
        fields = '__all__'
