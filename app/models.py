from flask.ext.security import UserMixin, RoleMixin

from app import db


roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return "<User {}".format(self.email)


class Panther(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    callsign = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    # Phone number without country code.
    phone = db.Column(db.String(64), unique=True)
    # 'A flight', 'B flight' etc, or 'Intel', 'AFE'. Needs to be searchable,
    # so 'A' won't do.
    flight = db.Column(db.String(64))

    def full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def phone_formatted(self):
        return ' '.join([self.phone[:5], self.phone[5:8], self.phone[8:]])

    def __repr__(self):
        return self.full_name()


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120))
    # lat and lon are in degrees.
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return self.label


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    # category  include 'ops_resources', 'personal', 'base_services' etc.
    category = db.Column(db.String(64))
    # Order is for display order
    order = db.Column(db.Integer)
    cac_required = db.Column(db.Boolean())
    login_required = db.Column(db.Boolean())
    gov_only = db.Column(db.Boolean())
