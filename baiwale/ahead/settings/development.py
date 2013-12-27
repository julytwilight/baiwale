# -*- coding: utf-8 -*-
from .base import *

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'baiwale-dev',
        'USER': 'root',
        'PASSWORD': 'good123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}