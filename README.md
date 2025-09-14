# MotoParts - Store

![Python](https://img.shields.io/badge/python-3670A0?style=style-flat&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=style-flat&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=style-flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=style-flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=style-flat&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=style-flat&logo=celery&logoColor=ddf4a4)
![Stripe](https://img.shields.io/badge/Stripe-5469d4?style=style-flat&logo=stripe&logoColor=ffffff)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=style-flat&logo=bootstrap&logoColor=white)

Интернет-магазин для быстрого поиска и заказа запасных частей мотоциклов KTM, Husqvarna, GasGas.

## Функциональность:

- Просмотр товаров и корзина для заказов;
- Купонная система со скидками по промокодам;
- Дружественный интерфейс оформления платежей;
- Платёжный шлюз для оплаты картой;
- Автоматическая отправка PDF-счёта на email;
- Система рекомендаций товаров;
- Кеширование запросов и результатов поиска.

## Стек:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/downloads/)
- [Celery](https://pypi.org/project/celery/)
- [Stripe](https://stripe.com/)
- [Bootstrap](https://getbootstrap.com/)

### Установка и настройка:

1. Клонируйте репозиторий с помощью команды:
```python
git clone https://github.com/Alex-Wo/Motoparts-Store.git
```
2. Перейдите в каталог проекта:
```python
cd myshop
```
3. Создайте виртуальную среду и активируйте её:
```python
python3.11 -m venv env/myshop
source env/myshop/bin/activate (для Linux и MacOS)
.\env\myshop\Scripts\activate (для Windows)
```
4. Обновите pip и установите зависимости:
```python
pip install --upgrade pip
pip install -r requirements.txt
```
5. Установите зависимости [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) для вашей операционной системы. Это необходимо для генерации pdf чеков, которые генерируются из html шаблона.

6. Примените миграции базы данных:
```python
python manage.py makemigrations
python manage.py migrate
```
7. Создайте суперпользователя:
```python
python manage.py createsuperuser
```
8. Для функционала оплаты проведите ключи платежной системы Stripe. Создайте файл .env и добавьте
```python
STRIPE_PUBLISHABLE_KEY = 'pk_test_your_key'
STRIPE_SECRET_KEY = 'sk_test_your_key'
STRIPE_API_VERSION = 'your_stripe_aoi_version'
STRIPE_WEBHOOK_SECRET = 'whsec_yourWebhookKey'
```
9. В контейнере Docker запустите службы RabbitMQ и Redis:
```python
docker pull rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

docker pull redis
docker run -it --rm --name redis -p 6379:6379 redis
```
10. Запустите celery worker:
```python
celery -A myshop worker -l info
```
> Если у вас Windows OS, то для корректной работы установите пакет [Eventlet](https://pypi.org/project/eventlet/):
```python
pip install eventlet
```
11. Запустите celery worker командой:
```python
celery -A myshop worker -l info -P eventlet
```
12. Мониторинг Celery при помощи Flower:
```python
celery -A myshop flower
```
13. Для просмотра активных работников Celery и статистики асинхронных заданий перейдите по адресу:

http://localhost:5555/dashboard

14. Запустите прослушивание событий вебхуков:
```python
stripe listen --forward-to localhost:8000/payment/webhook/
```
15. Запустите сервер разработки:
```python
python manage.py runserver
```
16. Теперь вы можете открыть приложение в браузере по адресу:

http://localhost:8000

#### Примечание:

По умолчанию, проект настроен на использование консольного бэкенда отправки почты. Для использования функционала отправки электронной почты, установите соответствующие параметры в файле settings.py

## Contributing:

Если вы обнаружили ошибки или у вас есть предложения по улучшению проекта, пожалуйста, создайте новый Issue или отправьте Pull Request.

## Скриншоты:

![127 0 0 1_8000_](https://github.com/user-attachments/assets/29fa7d20-7295-4ab7-8fce-75a456bd772e)
•••
![image_2025-04-28_19-56-56](https://github.com/user-attachments/assets/83079272-abf6-42c4-9f6a-f166e824c3e9)
•••
![image_2025-04-28_19-59-10](https://github.com/user-attachments/assets/b9f7edab-73b6-40e4-a00c-d794b1e93d6e)
•••
![image_2025-04-28_19-59-49](https://github.com/user-attachments/assets/a6b7bd94-a739-454b-b3c8-d0e81fd3bab7)
•••
![image_2025-04-28_20-01-27](https://github.com/user-attachments/assets/2573d2c0-9f6d-4d13-aafc-07e5c70bf1bd)
•••
![image_2025-04-28_20-36-59](https://github.com/user-attachments/assets/3e364978-a4dc-487e-ab26-44b9cf57220e)
•••
![image_2025-04-28_21-17-16](https://github.com/user-attachments/assets/e5869e37-0668-4dd3-b5fe-7d61931f5d1a)

## Лицензия:

Этот проект лицензирован в соответствии с лицензией ISC. Подробности можно найти в файле [LICENSE](https://github.com/Alex-Wo/Motoparts-Store/blob/master/LICENSE)
