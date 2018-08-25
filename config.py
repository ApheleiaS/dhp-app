import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = 'thisisdfjdshkddfjchanged'
CSRF_SESSION_KEY = 'ad190242b1dd440584ab5324688526dshb'
