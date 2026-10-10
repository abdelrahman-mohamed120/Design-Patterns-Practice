from strategies.payment_strategy import PaymentStrategy


class StripePayment(PaymentStrategy):

    def __init__(self, api_key: str):
        self.api_key = api_key

    def pay(self, amount: float) -> dict:

        print(
            f"Processing payment of ${amount} through Stripe with API key: {self.api_key}"
        )
        # Simulate a successful payment response
        return {"status": "success", "amount": amount, "gateway": "Stripe"}
