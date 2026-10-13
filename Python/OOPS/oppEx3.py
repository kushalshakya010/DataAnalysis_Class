"""
Create a class BankAccount with owner and balance (default starting balance 0).

deposit(amount) adds to the balance
withdraw(amount) subtracts, but if the amount is more than the balance, print “Insufficient funds” and don’t change the balance
__str__ returns something like Kushal's balance: 500

Test: create an account, deposit 1000, withdraw 300, try to withdraw 5000, then print the account.

Hint for the default balance: def __init__(self, owner, balance=0).
"""

class Bankstatement:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
         self.balance+=amount

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient fund"
        elif amount <= self.balance: 
             self.balance-=amount

    def __str__(self):
        return f"{self.owner}'s balance: {self.balance}"



p1 = Bankstatement("ram")
p1.deposit(5000)
p1.withdraw(2000)
print(p1)