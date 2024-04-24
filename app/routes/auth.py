from app import app, db
from flask import jsonify, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta, timezone
from authlib.integrations.flask_client import OAuth
from functools import wraps
import jwt
import os
from app.models import User, Token



# Initialize OAuth for Google sign-in
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id= os.environ.get('CLIENT_ID'),
    client_secret= os.environ.get('CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    refresh_token_params=None,
    redirect_uri='http://localhost:5000/auth/google',
    client_kwargs={'scope': 'openid profile email'}
)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if username, email, and password are provided
    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if the email is already in use
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already in use'}), 409

    # Hash the password
    password_hash = generate_password_hash(password)

    # Create a new user with hashed password
    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 201



@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not isinstance(password, str) or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate JWT token
    payload = {
        'user_id': user.user_id,
        'is_admin': user.is_admin if hasattr(user, 'is_admin') else False,  # Check if 'is_admin' attribute exists
        'exp': datetime.now(timezone.utc) + timedelta(days=1)  # Token expires in 1 day
    }
    token = jwt.encode(payload, app.secret_key, algorithm='HS256')

    # Store token in database
    new_token = Token(token=token, user_id=user.user_id)  # Remove .decode('utf-8')
    db.session.add(new_token)
    db.session.commit()

    return jsonify({'token': token, 'is_admin': user.is_admin}), 200



@app.route('/auth/google')
def google_login():
    return google.authorize_redirect(redirect_uri=url_for('google_auth_callback', _external=True))

@app.route('/auth/google/callback')
def google_auth_callback():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # Here, you can create or retrieve a user account based on user_info
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        # Create new user if not exists
        user = User(
            email=user_info['email'],
            username=user_info['name']
        )
        db.session.add(user)
        db.session.commit()

    # Generate JWT token
    payload = {
        'user_id': user.user_id,
        'is_admin': False,  # Assuming Google sign-in users are not admins by default
        'exp': datetime.now(timezone.utc) + timedelta(days=1)  # Token expires in 1 day
    }
    token = jwt.encode(payload, app.secret_key, algorithm='HS256')

    # Store token in database
    new_token = Token(token=token.decode('utf-8'), user_id=user.user_id)
    db.session.add(new_token)
    db.session.commit()

    return redirect(url_for('redirect_uri', token=token.decode('utf-8')))



def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        user_id = get_user_from_token(token)
        if not user_id:
            return jsonify({'message': 'Invalid token'}), 401

        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        request.user = user  # Set request.user for later use
        return f(*args, **kwargs)

    return decorated_function


@app.route('/dashboard')
@token_required
def dashboard():
    user = request.user  # Assuming token_required decorator sets request.user
    return jsonify({'message': f'Welcome, {user.username}!'}), 200

def get_user_from_token(token):
    try:
        data = jwt.decode(token, app.secret_key, algorithms=['HS256'])
        return data.get('user_id')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None