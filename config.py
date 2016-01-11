# -*- coding=utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
]

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 30025
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['dingchengjie@aztechx.com']
