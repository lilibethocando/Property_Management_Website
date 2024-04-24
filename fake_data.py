from app import app, db
from app.models import Apartment, Tenant, User, Complaint, Request, Payment, PaymentStatus, Reminder, Notification
from faker import Faker
from random import randint

fake = Faker()

def create_fake_data():
    with app.app_context():
        # Create Apartments
        for _ in range(10):
            apartment = Apartment().create_apartment(
                name=fake.word(),
                description=fake.sentence(),
                rent_amount=randint(500, 3000)
            )
            db.session.add(apartment)

        # Create Tenants
        for _ in range(10):
            tenant = Tenant().create_tenant(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=fake.phone_number()
            )
            db.session.add(tenant)

        # Create Users
        admin_user = User().create_user(
            email='tpetrou@example.com',
            username='capno',
            password='tatipassword',
            date_created=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        )
        db.session.add(admin_user)

        # Create Complaints
        for _ in range(5):
            complaint = Complaint().create_complaint(
                type=fake.word(),
                description=fake.sentence(),
                severity=fake.random_element(elements=('Low', 'Medium', 'High')),
                created_at=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            )
            db.session.add(complaint)

        # Create Requests
        for _ in range(5):
            request = Request().create_request(
                type=fake.word(),
                description=fake.sentence(),
                severity=fake.random_element(elements=('Low', 'Medium', 'High')),
                status=fake.random_element(elements=('Pending', 'Completed')),
                created_at=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            )
            db.session.add(request)

        # Create Payments
        for _ in range(5):
            payment = Payment().create_payment(
                tenant_id=randint(1, 10),
                amount=randint(500, 3000),
                status=fake.random_element(elements=('Paid', 'Pending', 'Late')),
                payment_type=fake.word(),
                date_paid=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            )
            db.session.add(payment)

        # Create Payment Statuses
        for _ in range(5):
            payment_status = PaymentStatus().create_payment_status(
                tenant_id=randint(1, 10),
                status=fake.random_element(elements=('Paid', 'Pending', 'Late')),
                date_created=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            )
            db.session.add(payment_status)

        # Create Reminders
        for _ in range(5):
            reminder = Reminder().create_reminder(
                status=fake.random_element(elements=('Pending', 'Completed')),
                date_created=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            )
            db.session.add(reminder)

        # Create Notifications
        for _ in range(5):
            notification = Notification().create_notification(
                user_id=1,  # Assuming the admin user has user_id 1
                notification_type=fake.random_element(elements=('Alert', 'Info')),
                details=fake.sentence(),
                date_created=fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            )
            db.session.add(notification)

        db.session.commit()
        print("Fake data created successfully!")

if __name__ == '__main__':
    create_fake_data()
