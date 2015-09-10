import logging
import sys

from flask import Flask
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
# Import the custom flask_sslify that supports an includes list.
from flask_sslify2 import SSLify

app = Flask(__name__)
app.config.from_object('app.config')

# Force SSL redirect on the roster and map. Note that we have to use the
# lakenheath.herokuapp website, to avoid paying for an SSL cert etc.
sslify = SSLify(app, includes=['roster', 'map'])

db = SQLAlchemy(app)
admin = Admin(app, name='Lakenlink', base_template='my_master.html',
              template_mode='bootstrap3')

heroku = Heroku(app)

from app import views, models


admin.add_view(views.AdminModelView(models.Role, db.session))
admin.add_view(views.AdminModelView(models.User, db.session))
admin.add_view(views.AdminModelView(models.Link, db.session))
admin.add_view(views.AdminModelView(models.Panther, db.session))
admin.add_view(views.AdminModelView(models.Location, db.session))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)


# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )

# Fix Heroku logging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
