import logging
import sys

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.settings')

db = SQLAlchemy(app)
admin = Admin(app, name='Lakenlink', template_mode='bootstrap3')

heroku = Heroku(app)

from app import views, models

# Add views to the admin page that let us modify database entries.
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Link, db.session))
admin.add_view(ModelView(models.Panther, db.session))

# Fix Heroku logging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
