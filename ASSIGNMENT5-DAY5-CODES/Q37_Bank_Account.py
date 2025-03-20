# 37. Create a class BankAccount with a method withdraw() t
# hat prints "Withdrawal from a generic bank account." 
# Create subclasses SavingsAccount
# and CheckingAccount that override the withdraw() 
# method to print "Withdrawal from a savings account" and "Withdrawal from a checking account", respectively.


class BankAccount:
    def withdraw(self):
        print("Withdrawal from a generic bank account.")

class SavingsAccount(BankAccount):
    def withdraw(self):
        print("Withdrawal from a savings account.")

class CheckingAccount(BankAccount):
    def withdraw(self):
        print("Withdrawal from a checking account.")

obj1 = BankAccount()
obj1.withdraw()

obj2 = SavingsAccount()
obj2.withdraw()

obj3 = CheckingAccount()
obj3.withdraw()