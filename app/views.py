from collections import namedtuple

from flask import render_template
from app import app
from app.models import Panther, Link

Label = namedtuple('Label', ['text', 'lat', 'lon'])


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
                           queep=queep,
                           )


@app.route('/contacts')
def phone_numbers():

    contacts = [
        # V
        #

    ]

    return render_template('contacts.html', contacts=contacts)


@app.route('/map')
def base_map():

    # lat, lon. List instead of tuple for JS compatibility.
    center = [52.397283, 0.551360]

    labels = [
        # Label("SEC", 52.399423, 0.561185),
        # Label("Sims", 52.398394, 0.563266),
        # Label("Hangar 6", 52.402678, 0.560025),
        # Label("MOPP training", 52.399567, 0.565717),
        # Label("SERE", 52.400139, 0.567896),
        # Label("Gold", 52.410059, 0.578290),
        Label("Post office", 52.397489, 0.541705),
        Label("Golf course, Breckland Pines", 52.398476, 0.569096),
        Label("Gym", 52.392908, 0.540615),
        Label("MPF", 52.395588, 0.547411),
        Label("Comm", 52.399222, 0.548833),
        Label("Flight medicine", 52.394161, 0.544522),
        Label("Lodging", 52.393930, 0.548817),
        Label("BX", 52.392778, 0.547357),
        Label("Uniform store", 52.391725, 0.544996),
        Label("Commissary", 52.396789, 0.550654),
        Label("Auto hobby", 52.398453, 0.544610),
        Label("Auto mechanic", 52.396730, 0.542175),
        Label("Liquor store, Subway", 52.390869, 0.544623),
        Label("Rugby's, Pinkerton's", 52.390250, 0.544795),
        Label("Pizza", 52.390568, 0.545648),
        Label("Fast food", 52.396392, 0.545290),
        Label("Gas station, Taco Bell", 52.397190, 0.554822),
        Label("In-processing", 52.394469, 0.547057)
    ]

    labels_jssafe = [[label.text, label.lat, label.lon] for label in labels]

    return render_template('map.html',
                           title="Lakenheath Map",
                           center=center,
                           # Set map type in map.js due to limitations.
                           # map_type='SATELLITE',
                           zoom=16,
                           labels=labels_jssafe)


@app.route('/housing')
def housing():
    return render_template('housing.html',
                           title="Housing near Lakenheath")


@app.route('/roster')
def roster():
    panthers = Panther.query.order_by(Panther.last_name)
    return render_template('roster.html',
                           title="Squadron roster",
                           panthers=panthers)
