from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class CustomUserManager(BaseUserManager):
    """ Кастомный менеджер для создания пользователей. """

    def create_user(self, email, password, **extra_fields):
        """ Создает и сохраняет пользователя с указанным адресом электронной почты и паролем. """

        if not email:
            raise ValueError('Поле email должно быть заполнено')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """
    Модель пользователя

    Поля:
    email: адрес электронной почты.
    name: имя.
    is_active: признак активности.

    """
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True, verbose_name='признак активности')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        :return: Строковое представление пользователя по адресу электронной почты.
        """
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
