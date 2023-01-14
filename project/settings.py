import os

from environs import Env


env = Env()
env.read_env()
django_db_engine = env.str("DJANGO_DB_ENGINE")
django_db_host = env.str("DJANGO_DB_HOST")
django_db_port = env.str("DJANGO_DB_PORT")
django_db_name = env.str("DJANGO_DB_NAME")
django_db_user = env.str("DJANGO_DB_USER")
django_db_password = env.str("DJANGO_DB_PASSWORD")
django_db_secretkey = env.str("DJANGO_DB_SECRET_KEY")
django_db_debug = env.bool("DJANGO_DB_DEBUG")
DATABASES = {
    'default': {
        'ENGINE': django_db_engine,
        'HOST': django_db_host,
        'PORT': django_db_port,
        'NAME': django_db_name,
        'USER': django_db_user,
        'PASSWORD': django_db_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = django_db_secretkey

DEBUG = django_db_debug

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
