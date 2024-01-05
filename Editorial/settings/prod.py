from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'editorial.omardanielesquivel.com',
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'https://editorial.omardanielesquivel.com',
]
CORS_ALLOWED_ORIGINS = [
    'https://editorial.omardanielesquivel.com',
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME_PROD'),
        'USER': get_secret('DB_USER_PROD'),
        'PASSWORD': get_secret('DB_PASSWORD_PROD'),
        'HOST': get_secret('DB_HOST_PROD'),
        'PORT': get_secret('DB_PORT_PROD'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / STATIC_URL]
STATIC_ROOT = BASE_DIR / 'staticfiles/'


# Media Config
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / MEDIA_URL
