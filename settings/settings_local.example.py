# encoding: utf-8
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER':  'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
EMAIL_HOST_PASSWORD = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG = TEMPLATE_DEBUG = True