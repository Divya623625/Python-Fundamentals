# Concept - Classes and Objects
# Create a BankAccount class with attributes account_number, owner_name, and balance.
# Add methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.balance)


# Creating object
acc1 = BankAccount(101, "Divya", 5000)

acc1.deposit(1000)
acc1.withdraw(2000)
acc1.check_balance()


