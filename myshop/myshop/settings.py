from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG'))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': (os.getenv('ENGINE')),
        'NAME': (os.getenv('NAME')),
        'USER': (os.getenv('USER')),
        'PASSWORD': (os.getenv('PASSWORD')),
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = (os.getenv('LANGUAGE_CODE'))

TIME_ZONE = (os.getenv('TIME_ZONE'))  # UTC -3

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = (os.getenv('STATIC_URL'))

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = (os.getenv('MEDIA_URL'))
MEDIA_ROOT = (os.getenv('MEDIA_ROOT'))

CART_SESSION_ID = (os.getenv('CART_SESSION_ID'))

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Параметры настройки Stripe
STRIPE_PUBLISHABLE_KEY = (os.getenv('STRIPE_PUBLISHABLE_KEY'))  # Публикуемый ключ
STRIPE_SECRET_KEY = (os.getenv('STRIPE_SECRET_KEY'))  # Секретный ключ
STRIPE_API_VERSION = (os.getenv('STRIPE_API_VERSION'))
STRIPE_WEBHOOK_SECRET = (os.getenv('STRIPE_WEBHOOK_SECRET'))  # Подпись веб-перехватчика

STATIC_ROOT = (os.getenv('STATIC_ROOT'))

# Параметры настройки Redis
REDIS_HOST = (os.getenv('REDIS_HOST'))
REDIS_PORT = (os.getenv('REDIS_PORT'))
REDIS_DB = (os.getenv('REDIS_DB'))
