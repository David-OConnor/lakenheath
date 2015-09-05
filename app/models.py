from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return "<User {}".format(self.username)


class Panther(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    callsign = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(64), unique=True)


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    # category  include 'ops_resources', 'personal', 'base_services' etc.
    category = db.Column(db.String(64))

    def __repr__(self):
        return self.name
