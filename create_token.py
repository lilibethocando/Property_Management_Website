import stripe
import os

# Set your Stripe API key
stripe.api_key = "sk_test_51OCsCqCb8MXdJtc6GplIKp1r5ecaHUpKeTImWvUKE2SqMz12KlFvlTBBGTbYLjW8DVysEvTHStGhihDsPrprbrcz00I0KPZcF5"

try:
    # Create a payment with a test token
    stripe.PaymentIntent.create(
        amount=2000,  # Amount in cents
        currency="usd",
        payment_method_types=["card"],
        payment_method="pm_card_visa",  # Test card token
        confirm=True,
    )

    # Payment was successful
    print("Payment successful")
except stripe.error.CardError as e:
    # Payment failed
    print(f"Payment failed: {e.error.message}")
