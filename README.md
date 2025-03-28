# Motoparts-Store

Интернет-магазин запасных частей для мотоциклов KTM, Husqvarna, GasGas

## Функциональность:

## Стек:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/downloads/)

## Скриншоты:

## Запуск локально:

Все действия следует выполнять из исходного каталога проекта и только после установки всех требований.

1. Сначала создайте и активируйте новую виртуальную среду:

```
python3.9 -m venv ../venv
source ../venv/bin/activate
```
2. Обновите pip и установите пакеты:

```
pip install --upgrade pip
pip install -r requirements.txt
```
3. Запуск зависимостей проекта, миграций, заполнение базы данных данными фикстур и т. д.:

```
./manage.py migrate
./manage.py loaddata <path_to_fixture_files>
./manage.py runserver
```
4. Запустите сервер Redis:

```
redis-server
```
5. Запустите Celery:

```
celery -A store worker --loglevel=INFO
```

