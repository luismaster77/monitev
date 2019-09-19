"""
Django settings for monivet project.

Generated by 'django-admin startproject' using Django 1.11.24.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cn(+iwpi%-(jaofmo=!7hj$a&2@lz48kb$z81u8qmo@@lxo4+o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gestionmonitev@gmail.com'
EMAIL_HOST_PASSWORD = 'lu13edu4rd0'
EMAIL_PORT = 465

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_adminlte',
    'django_adminlte_theme',
    'registration',
    'crispy_forms',
    'gestionMonitev'
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

ROOT_URLCONF = 'monivet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'monivet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'monitev',
        'USER': 'develop1',
        'PASSWORD':'lu13edu4rd0',
        'HOST':'127.1.0.0',
        'POST':5432,
        'CHARSET':'UTF8',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-Co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATIC_URL = '/static/'
    # MEDIA_URL = '/media/'
    # STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    # MEDIA_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static", "media")

    # STATICFILES_DIRS = (
    #     os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
    # )
    # TEMPLATE_DIRS = (
    #     os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
    # )
# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates'),
# )
# STATICFILES_DIRS = (
#      os.path.join(BASE_DIR, 'static'),
# )
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
if not DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/home/pi/monitev/monivet/static'
    MEDIA_ROOT =  '/home/pi/monitev/monivet/static/media'

    STATICFILES_DIRS = (
        '/home/pi/monitev/monivet/static/static',
        )
    TEMPLATE_DIRS = (
        '/home/pi/monitev/monivet/static/templates',
    )
ACCOUNT_ACTIVATION_DAYS = 7

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = '/login'

LOGIN_REDIRECT_URL = '/monitev/welcome/'