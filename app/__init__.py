from flask import Flask
# from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config.from_object('app.settings')

# heroku = Heroku(app)

from app import views