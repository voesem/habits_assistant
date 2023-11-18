# Курсовая 7. DRF
## Трекер полезных привычек

### Виртуальное окружение
В проекте используется менеджер зависимостей Poetry.
1. Для активации виртуального окружения выполнить команду:
`poetry shell`
2. Установить зависимости проекта командой:
`poetry install`

### Переменные окружения
Для активации используемых в проекте переменных окружения 
файл .env_sample необходимо переименовать в .env и заполнить его необходимыми данными:
1. DJANGO_SECRET_KEY - секретный ключ Django.
2. DATABASE_NAME - название базы данных.
3. DATABASE_USER - пользователь postgres.
4. DATABASE_PASSWORD - пароль пользователя postgres.

### Кастомные команды создания пользователей
#### Создание суперпользователя:
1. Открыть файл .env.
2. В переменной SUPER_USER_EMAIL указать электронную почту, в SUPER_USER_NAME - имя (необязательно), в SUPER_USER_PASSWORD - пароль.
3. В терминале выполнить команду:
`python manage.py csu`

#### Создание обычного пользователя:
1. Открыть файл .env.
2. В переменной REGULAR_USER_EMAIL указать электронную почту, в REGULAR_USER_NAME - имя (необязательно), в REGULAR_USER_PASSWORD - пароль.
3. В терминале выполнить команду:
`python manage.py cu`

### Запуск менеджера задач Celery (для Windows)
`celery -A config worker --loglevel=info -P eventlet`
`celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`