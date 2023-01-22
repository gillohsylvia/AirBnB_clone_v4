#!/usr/bin/python3
from api.vi.views import app.views
from flask import*
@app-views.route('/status')
def index_status():
    return jsonify({"status":"ok"})
