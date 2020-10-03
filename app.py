from flask import Flask
import os
from gevent.pywsgi import WSGIServer
from routes import cth_routes

#App instance
app = Flask("CTH")

#Routes
app.add_url_rule('/', view_func=cth_routes.dummy, methods=['GET'])

#Run
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.debug = False
    wsgi_app = app.wsgi_app
    http_server = WSGIServer(('', port), wsgi_app)
    http_server.serve_forever()
