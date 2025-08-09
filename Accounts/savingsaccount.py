from Accounts.account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self.deposit(interest)
        return interest