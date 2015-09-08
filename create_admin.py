# Create an admin profile. Useful for setting up the first admin when deployed
# on Heroku.

from flask_security.utils import encrypt_password
from flask_security import SQLAlchemyUserDatastore

from app import app
from app import db

from app.models import Role, User


user_datastore = SQLAlchemyUserDatastore(db, User, Role)

with app.app_context():
    super_user_role = Role(name='superuser')
    user_role = Role(name='user')

    db.session.add(super_user_role)
    db.session.add(user_role)
    db.session.commit()

    first_admin = user_datastore.create_user(
        email='admin',
        password=encrypt_password('admin'),
        roles=[user_role, super_user_role]
    )
    
db.session.add(first_admin)
db.session.commit()
