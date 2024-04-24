from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os


app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from . import models
from app.routes import home, apartment, tenant, user, complaint, request, payment, reminder, notification, auth

if __name__ == '__main__':
    app.run(debug=True)
