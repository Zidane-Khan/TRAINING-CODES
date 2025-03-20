#  Write a Python class Account with a private attribute _balance and a private 
# method _check_balance() to ensure the account balance is checked before 
# withdrawal.

class Account:
    def __init__(self, balance):
     
        self._balance = balance

    def _check_balance(self):
        if self._balance < 0:
            print("Balance is insufficient!")
            return False
        return True

    def withdraw(self, amount):

        if self._check_balance():
            if amount <= self._balance:
                self._balance = amount-amount
                print(f"Withdrawal successful. New balance: ${self._balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Balance check failed. Withdrawal not allowed.")
    def get_balance(self):
        return self._balance


account = Account(2000)
account.withdraw(350) 
account.withdraw(600)  
print("Current Balance:", account.get_balance())

