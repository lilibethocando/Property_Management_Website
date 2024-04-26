from flask import request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS, cross_origin
from app import app
import os

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lilibethocando@hotmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('HOTMAIL')

mail = Mail(app)

def forward_email(sender, subject, body):
    msg = Message(subject, sender=sender, recipients=['lilibethocando@hotmail.com'])
    msg.body = body
    mail.send(msg)

@app.route('/receiveemail', methods=['POST'])
def receive_email():
    sender = request.form.get('sender')
    subject = request.form.get('subject')
    body = request.form.get('body')
    
    forward_email(sender, subject, body)
    
    return jsonify({'message': 'Email received and forwarded successfully'})

@app.route('/sendemail', methods=['POST'])
@cross_origin(supports_credentials=True)
def send_email():
    data = request.json
    user_email = data['email']
    message = data['message']

    # Send email to owner
    owner_msg = Message('New Inquiry from User', sender='lilibethocando@hotmail.com', recipients=['lilibethocando@hotmail.com'])
    owner_msg.body = f"Message from {user_email}: {message}"
    mail.send(owner_msg)

    # Send confirmation email to user
    confirmation_msg = Message('Inquiry Confirmation', sender='lilibethocando@hotmail.com', recipients=[user_email])
    confirmation_msg.body = "Thank you for reaching out to Smart Property Planning LLC. We appreciate your inquiry and will be in contact with you shortly."
    mail.send(confirmation_msg)

    return 'Email sent successfully', 200
