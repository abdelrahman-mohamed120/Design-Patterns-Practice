from strategies.payment_strategy import PaymentStrategy
from strategies.paypal_payment import PaypalPayment
from strategies.stripe_payment import StripePayment


class Checkout:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_checkout(self, amount: float) -> dict:

        return self.payment_strategy.pay(amount)
