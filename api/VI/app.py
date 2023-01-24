#!/usr/binpython3
from models import storage
from api.vi.views import app_views
from flask import*
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_view)
@app.teardown_appcontext
def tear_down(exeption):
    storage.close()


if __name__ = __main__
host = getenv('HBNB_API_HOST') or 0.0.0.0
port = getenv('HBNB_API_PORT') or 5050
app.run(host=host. port=port. threaded=True)
