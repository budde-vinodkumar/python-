# Parent class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # Encapsulation
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)




# Creating object
acc = SavingsAccount("Amit", 20000)

acc.display()
acc.deposit(5000)
acc.withdraw(12000)
acc.withdraw(8000)
acc.display()
