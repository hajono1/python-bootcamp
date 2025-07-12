class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0

class Coupon:
    def __init__(self, amount, expired):
        self.amount = amount
        self.expired = expired

    def valid(self):
        return not self.expired and self.amount > 0

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def valid(self):
        return len(str(self.card_number)) == 16 and super().valid()

class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def valid(self):
        return self.email.endswith("@gmail.com") and super().valid()

email1 = OnlinePayment(20000, "hajimeono@gmail.com")
print (email1.valid())
