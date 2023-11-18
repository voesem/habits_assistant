import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from config.settings import BASE_DIR
from users.models import User

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    """ Кастомная команда для создания обычного пользователя """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('REGULAR_USER_EMAIL'),
            name=os.getenv('REGULAR_USER_NAME'),
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        user.set_password('REGULAR_USER_PASSWORD')
        user.save()
