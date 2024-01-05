from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME_LOCAL'),
        'USER': get_secret('DB_USER_LOCAL'),
        'PASSWORD': get_secret('DB_PASSWORD_LOCAL'),
        'HOST': get_secret('DB_HOST_LOCAL'),
        'PORT': get_secret('DB_PORT_LOCAL'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static/']
STATIC_ROOT = BASE_DIR / 'staticfiles/'


# Media Config
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:4200',
    'http://localhost:5500',
    'http://localhost:5173',
    'http://localhost:5174',
    'http://localhost:5175',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:8888',
]