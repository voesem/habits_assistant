from django_celery_beat.models import CrontabSchedule, PeriodicTask


def create_habit_schedule(habit):
    """ Периодическая задача на отправку напоминаний в телеграме """

    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_month=f'*/{habit.periodicity}',
        month_of_year='*',
        day_of_week='*',
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit Task - {habit.action}',
        task='habits.tasks.send_telegram_message',
        args=[habit.pk],
    )
