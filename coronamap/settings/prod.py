# https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
import dj_database_url
from .base import *  # NOQA

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE


PARENT_HOST = 'cv19map.herokuapp.com'
ALLOWED_HOSTS = ['.%s' % PARENT_HOST]
SESSION_COOKIE_DOMAIN = ALLOWED_HOSTS[0]
SESSION_COOKIE_NAME = 'coronamap_sid'
STATIC_ROOT = ROOT
