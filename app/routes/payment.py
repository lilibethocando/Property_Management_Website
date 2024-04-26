from flask import request, jsonify
from app import app, db
from flask_cors import CORS, cross_origin
from app.models import Payment, PaymentStatus, Tenant
import stripe
import os

# route to fetch the Stripe API key
@app.route('/api/get-stripe-key', methods=['GET'])
@cross_origin()
def get_stripe_key():
    stripe_api_key = os.environ.get('STRIPE_PUBLIC_KEY')  # Replace with your actual Stripe public key
    return jsonify({'stripe_public_key': stripe_api_key})


stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')



def calculate_balance(tenant_id):
    # Calculate balance for a given tenant
    payments = Payment.query.filter_by(tenant_id=tenant_id, status='Paid').all()
    balance = sum(payment.amount for payment in payments)
    return balance


@app.route('/payments/getbalance/<int:tenant_id>', methods=['GET'])
@cross_origin()
def get_balance(tenant_id):
    # Get balance for the given tenant
    balance = calculate_balance(tenant_id)
    return jsonify({'balance': balance}), 200



@app.route('/payments/makepayment', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def make_payment():
    # Get payment data from request
    data = request.json
    tenant_id = data.get('tenant_id')
    amount = data.get('amount')
    payment_method = data.get('payment_method')
    description = data.get('description')

    if not all([tenant_id, amount, payment_method]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Validate amount type
        amount = int(amount)
    except ValueError:
        return jsonify({'error': 'Invalid amount format'}), 400

    try:
        # Handle payment method
        if payment_method == 'Stripe':
            # Create a payment with Stripe (assuming payment_method_types and payment_method are dynamic)
            response = stripe.PaymentIntent.create(
                amount=amount * 100,  # Amount in cents
                currency='usd',
                payment_method_types=["card"],  # Use payment_method from request
                payment_method="pm_card_visa",  # Use payment_method_id from request
                confirm=True,
                description=description
            )

            # Print Stripe response for debugging (optional)
            print(response)

            # Save payment information to the database
            payment_status = 'Paid' if response.status == 'succeeded' else 'Failed'
        else:
            # Handle other payment methods
            # Assuming payment_status is determined based on the success of the payment processing
            payment_status = 'Paid'  # Update this according to your logic for other payment methods

        # Save payment information to the database
        payment = Payment(
            tenant_id=tenant_id,
            amount=amount,
            status=payment_status,
            payment_type=payment_method,
            description=description
        )
        db.session.add(payment)
        db.session.commit()

        # Create a payment status
        payment_status = PaymentStatus(
            tenant_id=tenant_id,
            status=payment_status
        )
        db.session.add(payment_status)
        db.session.commit()

        return jsonify({'message': 'Payment successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


        return jsonify({
            'payment_id': payment.payment_id,
            'message': 'Payment successful!',
            'stripe_response': response  # Include sanitized Stripe response (optional)
        }), 200
    except stripe.error.CardError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/payments', methods=['GET'])
@cross_origin()
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


@app.route('/payments/<int:payment_id>', methods=['GET'])
@cross_origin()
def get_payment(payment_id):
    # Get payment by payment_id
    payment = Payment.query.get(payment_id)

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


@app.route('/payments/updatebalance', methods=['POST'])
@cross_origin()
def update_balance():
    # Get data from request
    data = request.json
    tenant_id = data.get('tenant_id')
    amount = data.get('amount')

    if not all([tenant_id, amount]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Calculate new balance
        balance = calculate_balance(tenant_id)
        new_balance = balance - amount

        # Update balance in the database
        # This assumes there is a Tenant model with a balance field
        tenant = Tenant.query.get(tenant_id)
        tenant.balance = new_balance
        db.session.commit()

        return jsonify({'new_balance': new_balance}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500