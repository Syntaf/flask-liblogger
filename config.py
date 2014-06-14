import os

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'Gmercer015@gmail.com'
MAIL_PASSWORD = None

ADMINS = ['gmercer@gmail.com']

basedir = os.path.abspath(os.path.dirname(__file__))

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS=50

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'gmoney'

OPENID_PROVIDERS = [
		{ 'name': 'Google', 'url': 'https://www.google.com/account/o8/id'},
		{ 'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
		{ 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
		{ 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
