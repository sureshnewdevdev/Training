from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    def payment_details(self):
        print("Payment details are confidential.")

class CreditCard(Payment):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}")
        
cr=CreditCard("1234-5678-9876-5432", "John Doe")
cr.process_payment(1000)