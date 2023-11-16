import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from config.settings import BASE_DIR
from users.models import User

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    """ Кастомная команда для создания суперпользователя """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('SUPER_USER_EMAIL'),
            name=os.getenv('SUPER_USER_NAME'),
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('SUPER_USER_PASSWORD'))
        user.save()
