from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(models.Model):
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
