# Base class
class ATM:
    def __init__(self, balance):
        self.balance = balance    # Encapsulation

    def check_balance(self):
        print("Available Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


# Child class (Inheritance)
class UserATM(ATM):
    def withdraw(self, amount):    # Polymorphism
        if amount > 10000:
            print("Withdrawal limit exceeded")
        else:
            super().withdraw(amount)


# Object creation
user = UserATM(20000)

# ATM operations
user.check_balance()
user.deposit(5000)
user.withdraw(15000)
user.withdraw(8000)
user.check_balance()
