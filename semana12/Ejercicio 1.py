class AvailableBalance(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
class SavingAccount(BankAccount):
    def __init__(self, balance=0,min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):

        if self.balance - amount < self.min_balance:
            raise AvailableBalance('Sorry, minimum balance must be maintained.')
        
        else:
            self.balance = super().withdraw(amount)
            return self.balance
        
try:
    my_account = SavingAccount(100,10)
    print(my_account.withdraw(90))
    print(my_account.deposit(30))
    print(my_account.withdraw(20))
    print(my_account.withdraw(20))

except AvailableBalance as e:
    print(e)