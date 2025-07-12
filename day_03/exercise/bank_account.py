class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def print_balance(self):
        print(self._balance)

account1 = BankAccount(500)
account1.deposit(250)
account1.print_balance()