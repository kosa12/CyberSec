

class BankAccount:
    
    def __init__(self, owner, account_number, initial_balance = 0):
        self.owner = owner
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def is_overdrawn(self):
        return self.balance < 0
    
    def __str__(self):
        return f"Balance of {self.owner} (account number: {self.account_number}) is: {self.balance}"


account = BankAccount("Dagobert Duck", (12345678,87654321,00000000), 15)
account.withdraw(5)
print(account)