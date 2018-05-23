from .base import *

import_secrets()

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.dev.application'

# Static
DEFAULT_FILE_STORAGE = 'config.storages.DefaultFileStorage'
STATICFILES_STORAGE = 'config.storages.StaticFilesStorage'
COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_URL = 'https://lhy-lecture.s3.amazonaws.com/'
