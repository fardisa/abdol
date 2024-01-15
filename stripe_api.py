import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_API_KEY')

SUBSCRIPTION_COST = 2900  # $29.00 in cents
BOOKING_FEE_PERCENTAGE = 0.10

def create_customer(email, payment_method):
    customer = stripe.Customer.create(
        email=email,
        payment_method=payment_method,
        invoice_settings={
            'default_payment_method': payment_method,
        },
    )
    return customer

def create_subscription(customer_id):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[
            {"price": SUBSCRIPTION_COST},
        ],
        expand=["latest_invoice.payment_intent"],
    )
    return subscription

def calculate_payout_amount(booking_cost):
    return int(booking_cost * (1 - BOOKING_FEE_PERCENTAGE))

def create_payout(provider_account_id, booking_cost):
    payout_amount = calculate_payout_amount(booking_cost)
    payout = stripe.Payout.create(
        amount=payout_amount,
        currency="usd",
        destination=provider_account_id,
    )
    return payout

def retrieve_customer(customer_id):
    return stripe.Customer.retrieve(customer_id)

def retrieve_subscription(subscription_id):
    return stripe.Subscription.retrieve(subscription_id)

def cancel_subscription(subscription_id):
    return stripe.Subscription.delete(subscription_id)

def update_customer_payment_method(customer_id, new_payment_method):
    customer = stripe.Customer.modify(
        customer_id,
        invoice_settings={
            'default_payment_method': new_payment_method,
        },
    )
    return customer

def retrieve_payout(payout_id):
    return stripe.Payout.retrieve(payout_id)