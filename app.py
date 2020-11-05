from flask import Flask
import os
from gevent.pywsgi import WSGIServer
from API.routes import cth_routes
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

#App instance
app = Flask("CTH")
app.config['SECRET_KEY'] = '34f17fc6c2d3dbc65842162b549486f6764c9c1462317f5607bd36f93c8d3986'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ewlsfolgbjbyin:34f17fc6c2d3dbc65842162b549486f6764c9c1462317f5607bd36f93c8d3986@ec2-34-235-62-201.compute-1.amazonaws.com:5432/d662524kgh9iqj'

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Institution = Base.classes.institutions
Operator = Base.classes.operator
Citizen = Base.classes.citizen
Test = Base.classes.tests
Infected = Base.classes.infected
Recovered = Base.classes.recovered
Illness = Base.classes.illness

@app.route('/test')
def index():
    # new_institution = Institution(instname='Hospital del Maestro',instlocation='San Juan, 00927', insttype="Hospital")
    # db.session.add(new_institution)
    # db.session.commit()
    results = db.session.query(Institution).all()
    for r in results:
        print(r.instname)
    return ''

#Routes
app.add_url_rule('/results-global', view_func=cth_routes.get_global_results, methods=['GET'])

app.add_url_rule('/results-age/<min_age>&<max_age>/<illness>', view_func=cth_routes.get_results_by_age, methods=['GET'])
app.add_url_rule('/results-age/<min_age>&<max_age>', view_func=cth_routes.get_results_by_age, methods=['GET'], defaults={'illness': None})

app.add_url_rule('/results-municipality/<municipality>/<illness>', view_func=cth_routes.get_results_by_municipality, methods=['GET'])
app.add_url_rule('/results-municipality/<municipality>', view_func=cth_routes.get_results_by_municipality, methods=['GET'], defaults={'illness': None})

app.add_url_rule('/results-sex/<sex>/<illness>', view_func=cth_routes.get_results_by_sex, methods=['GET'])
app.add_url_rule('/results-sex/<sex>', view_func=cth_routes.get_results_by_sex, methods=['GET'], defaults={'illness': None})


#Run
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.debug = False
    wsgi_app = app.wsgi_app
    http_server = WSGIServer(('', port), wsgi_app)
    http_server.serve_forever()
