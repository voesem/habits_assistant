from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateView, HabitListView, HabitRetrieveView, HabitUpdateView, HabitDestroyView, \
    PublicHabitListView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateView.as_view(), name='create_habit'),
    path('habits/', HabitListView.as_view(), name='habits_list'),
    path('habits/public/', PublicHabitListView.as_view(), name='public_habits_list'),
    path('habits/<int:pk>/', HabitRetrieveView.as_view(), name='view_habit'),
    path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='update_habit'),
    path('habits/delete/<int:pk>/', HabitDestroyView.as_view(), name='delete_habit'),
]
