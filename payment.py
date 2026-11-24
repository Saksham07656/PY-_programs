# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# Concrete Strategy 2
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Context
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Client
credit_card = CreditCardPayment()
processor = PaymentProcessor(credit_card)
processor.process_payment(1000)

upi = UPIPayment()
processor = PaymentProcessor(upi)
processor.process_payment(500)s