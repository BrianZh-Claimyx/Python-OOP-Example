from account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.__balance * self.interest_rate
        self.deposit(interest)
        return interest

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and amount <= (self.__balance + self.overdraft_limit):
            self._balance -= amount
            self.__transactions.append(f'Withdrew ${amount}')
            return True
        return False