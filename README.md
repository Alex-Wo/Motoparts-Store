# MotoParts - Store

Интернет-магазин для быстрого поиска и заказа запасных частей мотоциклов KTM, Husqvarna, GasGas.

## Функциональность:

- Данная платформа предоставляет клиентам возможность просматривать товары и добавлять их в корзину для последующего быстрого заказа;
- Реализована купонная система скидок, подразумевающая использование имеющегося промокода;
- Спроектирован интуитивно понятный процесс оформления платежа с дружелюбным интерфейсом;
- Подключён платёжный шлюз, позволяющий совершать оплату банковской картой;
- В случае успешной/неуспешной оплаты заказа клиенту на e-mail высылается счёт-фактура в формате PDF с подробностями транзакции;
- Внедрён рекомендательный механизм товаров, позволяющий клиенту совершать дополнительные покупки;
- Кеширование запросов, результатов поиска и прорисовки содержимого в результатах запросов.

## Стек:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Celery](https://pypi.org/project/celery/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/downloads/)
- [Stripe](https://stripe.com/)

### Установка и настройка:

• Клонируйте репозиторий с помощью команды:
```python
git clone https://github.com/Alex-Wo/Motoparts-Store.git
```
• Перейдите в каталог проекта:
```python
cd myshop
```
• Создайте виртуальную среду и активируйте её:
```python
python3.11 -m venv env/myshop
source env/myshop/bin/activate (для Linux и MacOS)
.\env\myshop\Scripts\activate (для Windows)
```
• Обновите pip и установите зависимости:
```python
pip install --upgrade pip
pip install -r requirements.txt
```
• Установите зависимости [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) для вашей операционной системы. Это необходимо для генерации pdf чеков, которые генерируются из html шаблона.

• Примените миграции базы данных:
```python
python manage.py makemigrations
python manage.py migrate
```
• Создайте суперпользователя:
```python
python manage.py createsuperuser
```
• Для функционала оплаты проведите ключи платежной системы Stripe. Создайте файл .env и добавьте
```python
STRIPE_PUBLISHABLE_KEY = 'pk_test_your_key'
STRIPE_SECRET_KEY = 'sk_test_your_key'
STRIPE_API_VERSION = 'your_stripe_aoi_version'
STRIPE_WEBHOOK_SECRET = 'whsec_yourWebhookKey'
```
• В контейнере Docker запустите службы RabbitMQ и Redis:
```python
docker pull rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

docker pull redis
docker run -it --rm --name redis -p 6379:6379 redis
```
• Запустите celery worker:
```python
celery -A myshop worker -l info
```
• Если у вас Windows OS, то для корректной работы установите пакет eventlet:
```python
pip install eventlet
```
• Запустите celery worker командой:
```python
celery -A myshop worker -l info -P eventlet
```
• Мониторинг Celery при помощи Flower:
```python
celery -A myshop flower
```
• Для просмотра активных работников Celery и статистики асинхронных заданий перейдите по адресу:

http://localhost:5555/dashboard

• Запустите прослушивание событий вебхуков:
```python
stripe listen --forward-to localhost:8000/payment/webhook/
```
• Запустите сервер разработки:
```python
python manage.py runserver
```
• Теперь вы можете открыть приложение в браузере по адресу:

http://localhost:8000

#### Примечание:

По умолчанию, проект настроен на использование консольного бэкенда отправки почты. Для использования функционала отправки электронной почты, установите соответствующие параметры в файле settings.py

## Contributing:

Если вы обнаружили ошибки или у вас есть предложения по улучшению проекта, пожалуйста, создайте новый Issue или отправьте Pull Request.

## Скриншоты:

![image_2024-08-03_15-05-47](https://github.com/user-attachments/assets/ce304804-a3d2-4866-9a9b-79aae17fe98b)

## Лицензия:

Этот проект лицензирован в соответствии с лицензией MIT. Подробности можно найти в файле LICENSE.
