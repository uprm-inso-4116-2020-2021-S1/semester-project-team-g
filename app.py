from flask import Flask
import os
from gevent.pywsgi import WSGIServer
from API.routes import cth_routes

#App instance
app = Flask("CTH")

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
