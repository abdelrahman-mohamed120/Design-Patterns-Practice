from abc import abstractmethod


class PaymentStrategy:

    # Define an abstract method for paying an amount
    @abstractmethod
    def pay(self, amount: float) -> dict:

        pass
