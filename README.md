# Shop
Медведева Антонида Викторовна
## Цель:
Реализовать сервис, который принимает и отвечает на HTTP запросы.
## Функционал:
1. В случае успешной обработки сервис должен отвечать статусом 200, в
случае любой ошибки — статус 400.
2. Сохранение всех объектов в базе данных.
3. Запросы:
    1. GET /city/ — получение всех городов из базы;
    2. GET /city//street/ — получение всех улиц города; (city_id —
    идентификатор города)
    3. POST /shop/ — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи.
    4. GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
    5. Метод принимает параметры для фильтрации. Параметры не обязательны. В случае отсутствия параметров выводятся все магазины, если хоть один параметр есть , то по нему выполняется фильтрация.
    5.1 Важно!: в объекте каждого магазина выводится название города и улицы, а не id записей.
    5.2 Параметр open: 0 - закрыт, 1 - открыт. Данный статус определяется исходя из параметров «Время открытия», «Время закрытия» и текущего времени сервера.

### Объекты:
    Магазин:
        Название
        Город
        Улица
        Дом
        Время открытия
        Время закрытия
    Город:
        Название
    Улица:
        Название
        Город

## Инструкция по развертыванию:
1. Установить Python 3.8.3
2. Создать вирутальное окружение: `python3 -m venv env`
3. Активировать виртуальное окружение `source env/bin/activate`
4. Устаовить зависимости: `pip install -r requirements.txt`
5. Создать базу данных PostgreSQL 12:
    1. Подключиться к БД через psql: `sudo -u postgres psql postgres`
    2. Создаем пользователя и настраеваем пароль `create user user_name with password 'PASSWORD';`
    3. Создать БД: `create database shop owner user_name;`
7. Установить переменные окружения:
    1. DOT_ENV_FILE=абсолютный_путь_до_locals.env.envs
8. Накатить миграции: `python manage.py migrate`
9. Запустить сервер `python manage.py runserver`

##Информация о доступах (логины/пароли и т.д.) *

1. Создать суперпользователя `python manage.py createsuperuser`
