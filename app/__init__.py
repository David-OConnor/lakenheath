from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.settings')

db = SQLAlchemy(app)
admin = Admin(app, name='Lakenlink', template_mode='bootstrap3')

# import the models here to prevent chicken-egg import problems.
from app.models import User, Panther
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Panther, db.session))

heroku = Heroku(app)

from app import views, models