# encoding: utf-8
from settings import *

DEBUG = TEMPLATE_DEBUG = False

DEFAULT_FILE_STORAGE = 'common.storage.GoogleCloudStorage'
STATICFILE_STORAGE = 'common.storage.GoogleCloudStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/[]:[]',
        'NAME': '[]',
        'USER': 'root',
    }
}
BUCKET_NAME = 'bucket_name'

EMAIL_HOST_PASSWORD = ''

EMAIL_BACKEND = 'common.mail.EmailBackend'
