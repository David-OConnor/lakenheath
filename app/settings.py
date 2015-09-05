import os
import pathlib

# Development key
SECRET_KEY = '\x83=\xeeKWp\x8eEo\x01\x05\xf5 \xbf\x8e\x124m\x1f\x01\x05H%\x9b'


# todo convert this os link below to pathlib.
basedir = os.path.abspath(os.path.dirname(__file__))


# todo make this work with heroku
SQLALCHEMY_DATABASE_URI = 'postgresql://david:test@localhost:5432/lakenheath'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
