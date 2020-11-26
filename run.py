from cth import app
import os
from gevent.pywsgi import WSGIServer
from cth.API.routes import cth_routes
# @app.route('/test')
# def index():
#     # new_institution = Institution(instname='Hospital del Maestro',instlocation='San Juan, 00927', insttype="Hospital")
#     # db.session.add(new_institution)
#     # db.session.commit()
#     results = db.session.query(Institution).all()
#     for r in results:
#         print(r.instname)
#     return ''

# Routes
app.add_url_rule('/operator-login', view_func=cth_routes.operator_login, methods=['POST'])
app.add_url_rule('/results-global', view_func=cth_routes.get_global_results, methods=['GET'])
app.add_url_rule('/input-form', view_func=cth_routes.input_form, methods=['GET', 'POST'])


app.add_url_rule('/results-age/<min_age>&<max_age>/<illness>', view_func=cth_routes.get_results_by_age, methods=['GET'])
app.add_url_rule('/results-age/<min_age>&<max_age>', view_func=cth_routes.get_results_by_age, methods=['GET'], defaults={'illness': None})

app.add_url_rule('/results-municipality/<municipality>/<illness>', view_func=cth_routes.get_results_by_municipality, methods=['GET'])
app.add_url_rule('/results-municipality/<municipality>', view_func=cth_routes.get_results_by_municipality, methods=['GET'], defaults={'illness': None})

app.add_url_rule('/results-sex/<sex>/<illness>', view_func=cth_routes.get_results_by_sex, methods=['GET'])
app.add_url_rule('/results-sex/<sex>', view_func=cth_routes.get_results_by_sex, methods=['GET'], defaults={'illness': None})


# Run
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    wsgi_app = app.wsgi_app
    http_server = WSGIServer(('', port), wsgi_app)
    http_server.serve_forever()
