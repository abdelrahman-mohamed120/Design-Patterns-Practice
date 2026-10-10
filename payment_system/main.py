from strategies.stripe_payment import StripePayment
from strategies.paypal_payment import PaypalPayment
from checkout import Checkout

stripe_gateway = StripePayment(api_key="sk_live_12345")
paypal_gateway = PaypalPayment(email="user@example.com", password="securepassword")


my_cart = Checkout(payment_strategy=stripe_gateway)
result1 = my_cart.process_checkout(amount=150.00)
print(result1)

print("-" * 30)
my_cart.set_payment_strategy(paypal_gateway)
result2 = my_cart.process_checkout(amount=150.00)
print(result2)
