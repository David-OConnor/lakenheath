from flask import Flask
# from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.settings')
db = SQLAlchemy(app)

# heroku = Heroku(app)

from app import views, models