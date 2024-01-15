```python
import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_API_KEY')

SUBSCRIPTION_COST = 2900  # $29.00 in cents
BOOKING_FEE_PERCENTAGE = 0.10  # 10%

def create_subscription(customer_id):
    """
    Create a monthly subscription for a service provider.
    """
    stripe.Subscription.create(
        customer=customer_id,
        items=[
            {"price": SUBSCRIPTION_COST},
        ],
        expand=["latest_invoice.payment_intent"],
    )

def charge_booking_fee(amount, customer_id):
    """
    Charge a 10% booking fee to the service provider.
    """
    fee = int(amount * BOOKING_FEE_PERCENTAGE)
    stripe.Charge.create(
        amount=fee,
        currency="usd",
        customer=customer_id,
    )

def payout_provider(amount, provider_account_id):
    """
    Payout 90% of the booking fee to the service provider.
    """
    payout_amount = int(amount * (1 - BOOKING_FEE_PERCENTAGE))
    stripe.Payout.create(
        amount=payout_amount,
        currency="usd",
        destination=provider_account_id,
    )
```