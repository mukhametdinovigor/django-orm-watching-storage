import os
from environs import Env

env = Env()
env.read_env()

database_host = env('DATABASE_HOST')
database_port = env.int('DATABASE_PORT')
database_name = env('DATABASE_NAME')
database_user = env('DATABASE_USER')
database_password = env('DATABASE_PASSWORD')
secret_key = env('SECRET_KEY')
debug = env.bool('DEBUG')
allowed_hosts = env('ALLOWED_HOSTS')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': database_host,
        'PORT': database_port,
        'NAME': database_name,
        'USER': database_user,
        'PASSWORD': database_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = debug

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = [allowed_hosts]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
