<<<<<<< HEAD
# Modify the withdraw method of BankAccount so that the bank
# account can not have a negative balance.
#
# If a person tries to withdraw more than what is in the
# balance, then the method should raise a ValueError.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(160)
=======
# Modify the withdraw method of BankAccount so that the bank
# account can not have a negative balance.
#
# If a person tries to withdraw more than what is in the
# balance, then the method should raise a ValueError.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(160)
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
