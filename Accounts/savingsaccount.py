from Accounts.account import Account

class SavingsAccount(Account):
    def __init__(self, owner:str, balance:float=0, interest_rate:float=0.02):
        assert isinstance(owner, str)
        assert isinstance(balance, (int,float))
        assert isinstance(interest_rate, (int,float))

        super().__init__(owner, balance)
        self._interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self.deposit(interest)
        return interest