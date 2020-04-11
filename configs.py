# -*- encoding:utf-8 -*-
# -*- python:3.8     -*-
# -*- author:LiuBX   -*-

import os

WEB_HOST = 'http://127.0.0.1:5000/'
ADMIN_USER_ID = 'SALAMANDER'
DEBUG = True
SECRET_KEY = os.urandom(24)
DB_USERNAME = 'root'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'upload'
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO= False
