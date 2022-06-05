from .base import *

#  debug mode
DEBUG = True

ALLOWED_HOSTS = []

# Database Config
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Installed Application
INSTALLED_APPS += [
    'apps.dashboard'
]
