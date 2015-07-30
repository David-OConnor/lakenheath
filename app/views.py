from collections import namedtuple

from flask import render_template
from app import app


Link = namedtuple('Link', ['title', 'url'])
Label = namedtuple('Label', ['text', 'lat', 'lon'])


@app.route('/')
@app.route('/index')
def index():
    # todo consider making this a dict, to prevent repeating code
    # todo in the template. Only if the format stays the same for all/most cats.
    ops_resources = [
        Link("OGV home page*",
             'https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/48OGStan'
             'Eval/SitePages/Home.aspx'),
        Link("OGV pubs library*",
             'https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/48OGStan'
             'Eval/FCIF%20(Pubs)%20Library/SitePages/Home.aspx'),
        Link("OGV Master Question  Files*",
             'https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/'
             '48OGStanEval/MQF/F15E/Forms/AllItems.aspx'),
        # Sub links on the main page to pubs checkers, ifg etc?
        Link("Lowfly Notams and Target imagery", 'http://flight-plan.herokuapp.com/'),
        # Link("Ops useful contacts", '/contacts'),
    ]

    personal = [
        #Link("Pass policy", '/pass'),
        Link("Form 6s (Foreign travel)*", ''),
        Link("Leave", 'https://www.my.af.mil/leavewebprod/profile'),
        Link("Pay", 'https://mypay.dfas.mil/mypay.aspx')
    ]

    base_services = [
        Link("Base map", '/map'),
        Link("Official useful contacts",
             'http://www.lakenheath.af.mil/news/usefulcontacts.asp'),
        Link("Base dining menus and hours", 'http://www.lakenheathfss.com/dining/')
    ]

    queep = [
        Link("CBTs", 'https://golearn.adls.af.mil/'),
        Link("PT Scores", 
             'https://www.my.af.mil/afpc2affms/affms/ui/reportWrapper.jsp?Jsp='
             'callreport&AppName=launch&ReportTitle=Fitness%20Tracker&viewer=HTML'),
        Link("Surf's up, Dude!", ''),
        Link("Webmail", 'https://lakenheath.mail.us.af.mil/owa'),
        Link("DTS travel vouchers", 
             'http://www.defensetravel.osd.mil/dts/site/index.jsp')
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

    return render_template('contacts.html', contacts=contacts)


@app.route('/map')
def base_map():

    # lat, lon. List instead of tuple for JS compatibility.
    center = [52.397283, 0.551360]

    labels = [
        Label("SEC", 52.399423, 0.561185),
        Label("Sims", 52.398394, 0.563266),
        Label("Hangar 6", 52.402678, 0.560025),
        Label("MOPP training", 52.399567, 0.565717),
        # Label("SERE", 52.400139, 0.567896),
        Label("Gold", 52.410059, 0.578290),
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
