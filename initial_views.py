# Script to set up (and back up) the links set up in an early version of the site.

from app import db
from app.models import Link

ops_resources = [
    Link(title="Roster", url='/roster', category='ops_resources', order=1),
    Link(title="OGV ICE home page*",
         url='https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/SitePages/Home.aspx',
         category='ops_resources', order=2),
    Link(title="Pubs library*",
         url='https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/48OGStan'
         'Eval/FCIF%20(Pubs)%20Library/SitePages/Home.aspx',
         category='ops_resources', order=3),
    Link(title="Pubs checker*",
         url='https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/'
         '48OGStanEval/Sample%20Pubs%20Checkers/F15E%20Pubs%20Checkers/'
         'Forms/AllItems.aspx',
         category='ops_resources', order=4),
    Link(title="Master Question Files*",
         url='https://ice.usafe.af.mil/sites/48FW/48thOperationsGroup/'
         '48OGStanEval/MQF/F15E/Forms/AllItems.aspx', category='ops_resources',
         order=5),
    # Sub links on the main page to pubs checkers, ifg etc?
    Link(title="Lowfly notams and target imagery", url='https://flight-plan.herokuapp.com/',
         category='ops_resources', order=6),
    # Link(title="Ops useful contacts", url='/contacts', category='ops_resources',
    # , order=7),
]

personal = [
    #Link(title="Pass policy", '/pass'),
    Link(title="Form 6s (Foreign travel)*",
         url='https://ice.usafe.af.mil/sites/48FW/WSA/48thFWAdvancedPrograms/'
         'test/CVN%20Foreign%20Travel.aspx?PageView=Shared',
         category='personal', order=1),
    Link(title="Leave", url='https://www.my.af.mil/leavewebprod/profile',
         category='personal', order=2),
    Link(title="Pay", url='https://mypay.dfas.mil/mypay.aspx',
         category='personal', order=3),
    # Link(title="Housing information", '/housing', category='personal', order=4)
]

base_services = [
    # Link(title="Base map", url='/map', category='base_services', order=1),
    Link(title="Useful contacts",
         url='http://www.lakenheath.af.mil/news/usefulcontacts.asp',
         category='base_services', order=2),
    Link(title="Base dining menus and hours",
         url='http://www.lakenheathfss.com/dining/',
         category='base_services', order=3)
]

queep = [
    Link(title="CBTs", url='https://golearn.adls.af.mil/', category='queep', order=1),
    Link(title="PT Scores",
         url='https://www.my.af.mil/afpc2affms/affms/ui/reportWrapper.jsp?Jsp='
         'callreport&AppName=launch&ReportTitle=Fitness%20Tracker&viewer=HTML',
         category='queep', order=2),
    Link(title="Surf's up, Dude!**",
         url='https://w45.afpc.randolph.af.mil/AFPCSecureNet40/PKI/MainMenu1.aspx',
         category='queep', order=3),
    Link(title="Webmail", url='https://lakenheath.mail.us.af.mil/owa',
         category='queep', order=4),
    Link(title="DTS travel vouchers",
         url='http://www.defensetravel.osd.mil/dts/site/index.jsp',
         category='queep', order=5)
]


for category in [ops_resources, personal, base_services, queep]:
    for link in category:
        db.session.add(link)
        db.session.commit()
