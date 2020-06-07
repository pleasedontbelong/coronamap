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

LOGGING = {
    'disable_existing_loggers': False,
    'formatters': {
        'complete': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s'
                      ':%(lineno)d->%(funcName)s()] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            "formatter": 'complete',
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
        'command': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
    'version': 1,
}
