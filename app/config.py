import os
import pathlib

# Development key
SECRET_KEY = '\x83=\xeeKWp\x8eEo\x01\x05\xf5 \xbf\x8e\x124m\x1f\x01\x05H%\x9b'

# todo convert this os link below to pathlib.
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL', 'postgresql://david:test@localhost:5432/lakenheath')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# Code below taken from flask-admin/sqlsecurity example

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False