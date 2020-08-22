from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('NAMEDBPG'),
        'USER': config('USERDBPG'),
        'PASSWORD': config('PASSWORDDBPG'),
        'HOST': 'localhost',
        'PORT': '25432'
       },
   }
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
