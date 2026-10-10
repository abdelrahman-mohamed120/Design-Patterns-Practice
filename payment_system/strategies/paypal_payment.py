from strategies.payment_strategy import PaymentStrategy


class PaypalPayment(PaymentStrategy):

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def pay(self, amount: float) -> dict:

        print(
            f"Processing payment of ${amount} through PayPal with email: {self.email}"
        )
        # Simulate a successful payment response
        return {"status": "success", "amount": amount, "gateway": "PayPal"}
