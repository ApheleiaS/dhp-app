import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = 'this-really-needs-to-be-changed'
