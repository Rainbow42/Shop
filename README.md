# Shop

## Инструкция по развертыванию:
1. Установить Python 3.8.3
2. Создать вирутальное окружение: `python3 -m venv env`
3. Активировать виртуальное окружение `source env/bin/activate`
4. Устаовить зависимости: `pip install -r requirements.txt`
5. Создать базу данных:
    1. Создаем пользователя и насоаевам пароль `create user user_name with password 'password';`
    2. Подключиться к БД через psql: `psql -U postgres`
    3. Создать БД: `create database shop owner user_name;
7. Установить переменные окружения:
    1. DOT_ENV_FILE=абсолютный_путь_до_locals.env.envs
8. Накатить миграции: `python manage.py migrate`

