# -*- coding: utf-8 -*-
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['baiwale.com', 'www.baiwale.com']

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'baiwale-dev',
        'USER': 'root',
        'PASSWORD': 'Agood123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}