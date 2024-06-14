from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os


app = Flask(__name__, static_folder='/property-management-frontend/build', static_url_path='')

CORS(app, resources={r"/*": {"origins": ['http://localhost:5173', 'https://property-management-website.onrender.com']}}, supports_credentials=True)


app.config.from_object(Config)

app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return app.send_static_file('index.html')

from . import models
from app.routes import home, apartment, request_by, tenant, user, complaint, payment, reminder, notification, auth, email

@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = request.headers.get('Access-Control-Request-Headers', '')
        response.headers.add('Access-Control-Allow-Headers', headers)
        response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin', ''))
        return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
