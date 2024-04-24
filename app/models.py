from . import db
from datetime import datetime, timezone, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import os
import secrets

class Apartment(db.Model):
    apartment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rent_amount = db.Column(db.Integer, nullable=False)
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaint.complaint_id'))
    complaint = db.relationship('Complaint', backref='apartments')
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    request = db.relationship('Request', backref='apartments')
    apartment_details_id = db.Column(db.Integer, db.ForeignKey('apartment_details.apartment_details_id'))
    apartment_details = db.relationship('ApartmentDetails', backref='apartments')


    def create_apartment(self, name, description, rent_amount, complaint_id=None, request_id=None, apartment_details_id=None):
        new_apartment = Apartment(name=name, description=description, rent_amount=rent_amount, complaint_id=complaint_id, request_id=request_id, apartment_details_id=apartment_details_id)
        db.session.add(new_apartment)
        db.session.commit()
        return new_apartment

    def update_apartment(self, apartment_id, **kwargs):
        apartment = Apartment.query.get(apartment_id)
        if apartment:
            for key, value in kwargs.items():
                setattr(apartment, key, value)
            db.session.commit()
            return apartment
        return None

    def delete_apartment(self, apartment_id):
        apartment = Apartment.query.get(apartment_id)
        if apartment:
            db.session.delete(apartment)
            db.session.commit()
            return True
        return False

    def get_apartment_by_id(self, apartment_id):
        return Apartment.query.get(apartment_id)
    
    def serialize(self):
        return {
            'apartment_id': self.apartment_id,
            'name': self.name,
            'description': self.description,
            'rent_amount': self.rent_amount,
            'complaint_id': self.complaint_id,
            'request_id': self.request_id,
            'apartment_details_id': self.apartment_details_id
        }


class ApartmentDetails(db.Model):
    apartment_details_id = db.Column(db.Integer, primary_key=True)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    amenities = db.Column(db.String(250))


    def create_apartment_details(self, bedrooms, bathrooms, amenities):
        new_details = ApartmentDetails(bedrooms=bedrooms, bathrooms=bathrooms, amenities=amenities)
        db.session.add(new_details)
        db.session.commit()
        return new_details

    def update_apartment_details(self, details_id, **kwargs):
        details = ApartmentDetails.query.get(details_id)
        if details:
            for key, value in kwargs.items():
                setattr(details, key, value)
            db.session.commit()
            return details
        return None

    def delete_apartment_details(self, details_id):
        details = ApartmentDetails.query.get(details_id)
        if details:
            db.session.delete(details)
            db.session.commit()
            return True
        return False

    def get_apartment_details_by_id(self, details_id):
        return ApartmentDetails.query.get(details_id)
    
    def serialize(self):
        return {
            'apartment_details_id': self.apartment_details_id,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'amenities': self.amenities
        }



class Tenant(db.Model):
    tenant_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(40), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='tenants')
    reminder_id = db.Column(db.Integer, db.ForeignKey('reminder.reminder_id'))
    reminder = db.relationship('Reminder', backref='tenants')
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.apartment_id'))
    apartment = db.relationship('Apartment', backref='tenants')


    def create_tenant(self, first_name, last_name, phone_number, apartment_id, user_id=None, reminder_id=None):
        new_tenant = Tenant(first_name=first_name, last_name=last_name, phone_number=phone_number, user_id=user_id, reminder_id=reminder_id, apartment_id=apartment_id)
        db.session.add(new_tenant)
        db.session.commit()
        return new_tenant

    def update_tenant(self, tenant_id, **kwargs):
        tenant = Tenant.query.get(tenant_id)
        if tenant:
            for key, value in kwargs.items():
                setattr(tenant, key, value)
            db.session.commit()
            return tenant
        return None

    def delete_tenant(self, tenant_id):
        tenant = Tenant.query.get(tenant_id)
        if tenant:
            db.session.delete(tenant)
            db.session.commit()
            return True
        return False

    def get_tenant_by_id(self, tenant_id):
        return Tenant.query.get(tenant_id)
    
    def serialize(self):
        return {
            'tenant_id': self.tenant_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'apatment_id': self.apartment_id,
            'user_id': self.user_id,
            'reminder_id': self.reminder_id
        }


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def promote_to_admin(self):
        self.is_admin = True
        db.session.commit()

    def demote_from_admin(self):
        self.is_admin = False
        db.session.commit()

    def create_user(self, username, password, email, date_created):
        new_user = User(username=username, email=email, date_created=date_created)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user


    def find_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()
    

    def serialize(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username': self.username,
            'password_hash': self.password_hash,
            'is_admin': self.is_admin,
            'date_created': self.date_created.strftime('%Y-%m-%d %H:%M:%S')
        }


class Complaint(db.Model):
    complaint_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    description = db.Column(db.String)
    severity = db.Column(db.String)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    notification_id = db.Column(db.Integer, db.ForeignKey('notification.notification_id'))
    notification_rel = db.relationship('Notification', backref='complaints', foreign_keys=[notification_id])

    def create_complaint(self, type, description, severity, created_at):
        new_complaint = Complaint(type=type, description=description, severity=severity, created_at=created_at)
        db.session.add(new_complaint)
        db.session.commit()
        return new_complaint

    def find_by_id(self, complaint_id):
        return Complaint.query.get(complaint_id)

    def get_all_complaints(self):
        return Complaint.query.all()

    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()

    def serialize(self):
        created_at_formatted = self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None
        return {
            'complaint_id': self.complaint_id,
            'type': self.type,
            'description': self.description,
            'severity': self.severity,
            'status': self.status,
            'created_at': created_at_formatted,
            'notification_id': self.notification_id
        }


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    description = db.Column(db.String)
    severity = db.Column(db.String)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    @classmethod
    def create_request(cls, type, description, severity, status='Pending', created_at=datetime.now(timezone.utc)):
        new_request = cls(type=type, description=description, severity=severity, status=status, created_at=created_at)
        db.session.add(new_request)
        db.session.commit()
        return new_request

    @classmethod
    def find_by_id(cls, request_id):
        return cls.query.get(request_id)

    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'description': self.description,
            'severity': self.severity,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'notification_id': self.notification_id
        }

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.tenant_id'))
    tenant = db.relationship('Tenant', backref='payments')
    amount = db.Column(db.Integer)
    description = db.Column(db.String(255))
    date_paid = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String)
    payment_type = db.Column(db.String)
    notification_id = db.Column(db.Integer, db.ForeignKey('notification.notification_id'))
    notification = db.relationship('Notification', backref='payments')

    def create_payment(self, tenant_id, amount, status, payment_type):
        new_payment = Payment(tenant_id=tenant_id, amount=amount, status=status, payment_type=payment_type)
        db.session.add(new_payment)
        db.session.commit()
        return new_payment
    
    def find_by_id(self, payment_id):
        return Payment.query.get(payment_id)


    def get_all_payments(self):
        return Payment.query.all()
    
    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()

    def serialize(self):
        return {
            'payment_id': self.payment_id,
            'tenant_id': self.tenant_id,
            'amount': self.amount,
            'date_paid': self.date_paid.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status,
            'payment_type': self.payment_type,
            'notification_id': self.notification_id
        }

class PaymentStatus(db.Model):
    payment_status_id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.tenant_id'))
    tenant = db.relationship('Tenant', backref='payment_statuses')
    payment_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String(30))

    def create_payment_status(self, tenant_id, status):
        new_payment_status = PaymentStatus(tenant_id=tenant_id, status=status)
        db.session.add(new_payment_status)
        db.session.commit()
        return new_payment_status
    
    def find_by_id(self, payment_status_id):
        return PaymentStatus.query.get(payment_status_id)
    
    def get_all_payment_statuses(self):
        return PaymentStatus.query.all()
    
    def serialize(self):
        return {
            'payment_status_id': self.payment_status_id,
            'tenant_id': self.tenant_id,
            'payment_date': self.payment_date.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status
        }

class Reminder(db.Model):
    reminder_id = db.Column(db.Integer, primary_key=True)
    reminder_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String(30))

    def create_reminder(self, status):
        new_reminder = Reminder(status=status)
        db.session.add(new_reminder)
        db.session.commit()
        return new_reminder
    

    def find_by_id(self, reminder_id):
        return Reminder.query.get(reminder_id)
    

    def get_all_reminders(self):
        return Reminder.query.all()
    
    def serialize(self):
        return {
            'reminder_id': self.reminder_id,
            'reminder_date': self.reminder_date.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status
        }

class Notification(db.Model):
    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='notifications')
    notification_type = db.Column(db.String(30))
    details = db.Column(db.String)
    created_at = db.Column(db.TIMESTAMP(timezone=True))
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    request = db.relationship('Request', backref='notification')
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaint.complaint_id'))
    complaint_rel = db.relationship('Complaint', backref='notifications', foreign_keys=[complaint_id])


    def create_notification(self, user_id, notification_type, details):
        new_notification = Notification(user_id=user_id, notification_type=notification_type, details=details)
        db.session.add(new_notification)
        db.session.commit()
        return new_notification
    
    def find_by_id(self, notification_id):
        return Notification.query.get(notification_id)
    
    def get_all_notifications(self):
        return Notification.query.all()

    def serialize(self):
        return {
            'notification_id': self.notification_id,
            'user_id': self.user_id,
            'notification_type': self.notification_type,
            'details': self.details,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'request_id': self.request_id,
            'complaint_id': self.complaint_id
        }
    


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))