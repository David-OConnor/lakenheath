from collections import namedtuple

from flask import render_template
from app import app


Link = namedtuple('Link', ['title', 'url'])


@app.route('/')
@app.route('/index')
def index():
    # todo consider making this a dict, to prevent repeating code
    # todo in the template. Only if the format stays the same for all/most cats.
    ops_resources = [
        Link("OGV home page (Gov computer only)",
             'https://ice.usafe.af.mil/sites/48OG/OGV/default.aspx'),
        Link("OGV pubs library (Gov computer only)", 'http://google.com'),
        # Sub links on the main page to pubs checkers, ifg etc?
        Link("Lowfly Notams and Target imagery", 'http://flight-plan.herokuapp.com/'),
        Link("Ops useful contacts", '/contacts'),
    ]

    personal = [
        Link("Pass policy", '/pass'),
        Link("Form 6s (Foreign travel)", ''),
        Link("Leave", 'https://www.my.af.mil/leavewebprod/profile'),
    ]

    base_services = [
        Link("Base map", '/map'),
        Link("Official useful contacts",
             'http://www.lakenheath.af.mil/news/usefulcontacts.asp'),
    ]

    queep = [
        Link("CBTs", 'https://golearn.adls.af.mil/'),
        Link("PT Scores", ''),
        Link("Surf's up, Dude!", ''),
        Link("Webmail", 'https://lakenheath.mail.us.af.mil/owa'),
        Link("DTS travel vouchers", 'http://www.defensetravel.osd.mil/dts/site/index.jsp')
    ]

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

    return render_template('contacts.html',
                           contacts=contacts)
