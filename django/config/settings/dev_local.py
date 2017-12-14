from .base import *

DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
WSGI_APPLICATION = 'config.wsgi.dev_local.application'

# Static
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')