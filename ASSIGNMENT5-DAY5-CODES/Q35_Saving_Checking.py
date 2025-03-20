# 35. Write a class Person with methods to 
# deposit(), withdraw(), and check the balance. 
# Create subclasses for SavingAccount and CheckingAccount, 
# where the SavingAccount has an interest rate and the CheckingAccount has overdraft protection.
class Person:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
    
    def check_balance(self):
        print(f"Balance: {self.balance}")

class SavingAccount(Person):
    def __init__(self, name, interest_rate):
        super().__init__(name)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f"Interest applied. New Balance: {self.balance}")

class CheckingAccount(Person):
    def __init__(self, name, overdraft_limit):
        super().__init__(name)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")

obj1 = SavingAccount("John", 0.05)
obj1.deposit(1000)
obj1.apply_interest()
obj1.check_balance()

obj2 = CheckingAccount("Jane", 500)
obj2.deposit(1000)
obj2.withdraw(1200)
obj2.check_balance()