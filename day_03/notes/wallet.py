class Wallet:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

food_wallet = Wallet(700)
food_wallet.amount += 2_000

print("Food Budget:", food_wallet.amount)