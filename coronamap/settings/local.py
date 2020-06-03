import os
import dj_database_url
from .base import *  # NOQA

DEBUG = True
SHELL_PLUS = "ipython"
DATABASE_URL = os.getenv(
    'DATABASE_URL', 'postgres://coronamap_user:coronamap123@localhost:5432/coronamap_db'
)
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
