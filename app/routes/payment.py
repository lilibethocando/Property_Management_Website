from flask import request, jsonify
from app import app, db
from app.models import Payment, PaymentStatus, Tenant
import stripe
import os

# Set your Stripe API key
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')



@app.route('/payments', methods=['POST'])
def create_payment():
    # Get payment data from request
    data = request.json
    tenant_id = data.get('tenant_id')
    amount = data.get('amount')
    currency = data.get('currency', 'usd')  # Default to USD if currency is not provided
    payment_method = data.get('payment_method', 'pm_card_visa')  # Default to a test Visa card token
    description = data.get('description')

    try:
        # Create a payment with Stripe
        stripe.PaymentIntent.create(
            amount=amount,  # Amount in cents
            currency=currency,
            payment_method_types=["card"],
            payment_method=payment_method,
            confirm=True,
            description=description
        )

        # Save payment information to the database
        payment = Payment(
            tenant_id=tenant_id,
            amount=amount,
            status='Paid',  # Assuming payment is successful
            payment_type='Stripe',
            description=description
        )
        db.session.add(payment)
        db.session.commit()

        # Create a payment status
        payment_status = PaymentStatus(
            tenant_id=tenant_id,
            status='Paid'  # Assuming payment is successful
        )
        db.session.add(payment_status)
        db.session.commit()

        # Return success response
        return jsonify({'message': 'Payment successful', 'payment_id': payment.payment_id}), 200
    except stripe.error.CardError as e:
        # Return error response if payment fails
        return jsonify({'error': str(e)}), 400
    

@app.route('/payments', methods=['GET'])
def get_payments():
    # Get all payments from the database
    payments = Payment.query.all()

    # Serialize payments data
    payments_data = []
    for payment in payments:
        payments_data.append({
            'payment_id': payment.payment_id,
            'tenant_id': payment.tenant_id,
            'amount': payment.amount,
            'status': payment.status,
            'payment_type': payment.payment_type,
            'description': payment.description
        })

    return jsonify(payments_data), 200


@app.route('/payments/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    # Get payment by payment_id
    payment = Payment.query.filter_by(payment_id=payment_id).first()

    if payment:
        # Serialize payment data
        payment_data = {
            'payment_id': payment.payment_id,
            'tenant_id': payment.tenant_id,
            'amount': payment.amount,
            'status': payment.status,
            'payment_type': payment.payment_type,
            'description': payment.description
        }

        return jsonify(payment_data), 200
    else:
        return jsonify({'error': 'Payment not found'}), 404

