# Motoparts-Store

Интернет-магазин запасных частей для мотоциклов KTM, Husqvarna, GasGas

## Функциональность:

## Стек:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Celery](https://pypi.org/project/celery/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/downloads/)
- [Stripe](https://stripe.com/)

## Скриншоты:

## Запуск локально:

Все действия следует выполнять из исходного каталога проекта и только после установки всех требований.

1. Сначала создайте и активируйте новую виртуальную среду:

```python
python3.11 -m venv ../venv
source ../venv/bin/activate
```
2. Обновите pip и установите пакеты:

```python
pip install --upgrade pip
pip install -r requirements.txt
```
3. Запуск зависимостей проекта, миграций, заполнение базы данных данными фикстур и т. д.:

```python
./manage.py migrate
./manage.py loaddata <path_to_fixture_files>
./manage.py runserver
```
4. Запустите сервер Redis:

```python
redis-server
```
5. Запустите Celery:

```python
celery -A store worker --loglevel=INFO
```

