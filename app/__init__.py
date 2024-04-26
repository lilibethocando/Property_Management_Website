from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os


app = Flask(__name__)
CORS(app, support_credentials=True)


app.config.from_object(Config)

app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from . import models
from app.routes import home, apartment, request_by, tenant, user, complaint, payment, reminder, notification, auth, email

@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request received'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        return response, 200


if __name__ == '__main__':
    app.run(debug=True)
