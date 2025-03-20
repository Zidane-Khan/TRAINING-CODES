# 36. Design a simple bank system using classes in Python. 
# Create a BankAccount class with methods to deposit(), withdraw(), 
# and check the balance. Add logic to prevent withdrawals from an account if there are insufficient funds.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current Balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Current Balance: {self.balance}")
        else:
            print("Insufficient funds.")
    
    def check_balance(self):
        print(f"Current Balance: {self.balance}")

obj = BankAccount("Zidane", 1000)
obj.deposit(500)
obj.withdraw(1200)
obj.check_balance()