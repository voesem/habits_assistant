from django.conf import settings
from telebot import TeleBot
from config.celery import app
from habits.models import Habit


@app.task
def send_telegram_message(habit_id):
    """ Задача на отправку напоминаний через телеграм-бота """

    habit = Habit.objects.get(pk=habit_id)
    bot = TeleBot(settings.TELEGRAM_BOT_TOKEN)
    message = f'Напоминание о выполнении привычки {habit.action} в {habit.time} в {habit.place}'
    bot.send_message(habit.user.chat_id, message)
