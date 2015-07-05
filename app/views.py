from collections import namedtuple

from flask import render_template
from app import app


Link = namedtuple('Link', ['title', 'url'])

@app.route('/')
@app.route('/index')
def index():
    # user = {'nickname': 'Dave!'}

    links = [
        Link("OGV home page (Gov computer only)", 'http://google.com'),
        Link("OGV pubs library (Gov computer only)", 'http://google.com'),
        Link("Official useful contacts",
             'http://www.lakenheath.af.mil/news/usefulcontacts.asp'),
        Link("ADLS (CBTs)", 'https://golearn.csd.disa.mil/'),
        Link("Ops useful contacts", '/contacts'),



        # {
            #'title': 'OGV Home page',
            #'url': 'http://'
        # },
        # {
        #     'title': 'OGV Pubs library',
        #     'url': 'http://'
        # },
        # {
        #     'title': 'Official Useful Contacts',
        #     'url': 'http://www.lakenheath.af.mil/news/usefulcontacts.asp'
        # }



    ]

    return render_template('index.html',
                           title='Lakenheath Ops Info',
                           links=links,
                           )

@app.route('/contacts')
def phone_numbers():

    contacts = [


    ]

    return render_template('contacts.html',
                           contacts=contacts)
