from flask import render_template, redirect, abort, url_for, request, \
    make_response, send_from_directory, send_file
from flask_admin.contrib import sqla
from flask_security import current_user, login_required

from app import app
from app.models import Panther, Link, Location


@app.route('/')
@app.route('/index')
def index():
    ops_resources = Link.query.filter_by(category='ops_resources').order_by(Link.order)
    personal = Link.query.filter_by(category='personal').order_by(Link.order)
    base_services = Link.query.filter_by(category='base_services').order_by(Link.order)
    queep = Link.query.filter_by(category='queep').order_by(Link.order)

    return render_template('index.html',
                           title='Lakenheath Ops Info',
                           ops_resources=ops_resources,
                           personal=personal,
                           base_services=base_services,
                           queep=queep,)


# @app.route('/contacts')
# def phone_numbers():
#
#     contacts = [
#         # V
#         #
#
#     ]
#
#     return render_template('contacts.html', contacts=contacts)


@app.route('/pass')
@login_required
def pass_guidance():
    return send_file('static/pass_guidance.pdf', as_attachment=False)


@app.route('/map')
@login_required
def base_map():
    center = [52.397283, 0.551360]
    locations = Location.query.all()

    # Pass the template a dictionary representing the database entries in the
    # map, like in the roster. view
    locations_js = [{'label': loc.label,
                     'lat': loc.lat,
                     'lon': loc.lon} for loc in locations]

    return render_template('map.html',
                           title="Lakenheath Map",
                           center=center,
                           # Set map type in map.js due to limitations.
                           # map_type='SATELLITE',
                           zoom=16,
                           locations_js=locations_js)


@app.route('/housing')
def housing():
    return render_template('housing.html',
                           title="Housing near Lakenheath")


@app.route('/roster')
@login_required
def roster():
    if not current_user.confirmed_at:
        return render_template('not_confirmed.html')
    panthers = Panther.query.order_by(Panther.callsign)

    # Pass the template a dictionary representing the database entries in the
    # roster instead of a Python model object... The dict will be converted
    # to a JS object by the template engine.
    panthers_js = [{'first_name': panther.first_name,
                    'last_name': panther.last_name,
                    'callsign': panther.callsign,
                    'email': panther.email,
                    'phone': panther.phone,
                    'flight': panther.flight,
                    'full_name': panther.full_name(),
                    'phone_formatted': panther.phone_formatted()
                    } for panther in panthers if panther.active]

    # This prevents None values from raising javascript errors, preventing the
    # roster from displaying.
    for panther in panthers_js:
        for key in panther:
            if panther[key] is None:
                panther[key] = ''

    return render_template('roster.html',
                           title="Squadron roster",
                           # panthers=panthers,
                           panthers_js=panthers_js
                           )


# Create customized model view class
class AdminModelView(sqla.ModelView):
    def is_accessible(self):
        if not current_user.is_active() or not current_user.is_authenticated():
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is
        not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated():
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
