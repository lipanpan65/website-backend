# -*- coding: utf-8 -*-
# @Time    : 2021/7/31 11:09 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : dev.py


from .common import *

DEV = True

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website_dev',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '39.105.100.168',
        'PORT': '3306',
    }
}
