from Accounts.account import Account

class CheckingAccount(Account):
    def __init__(self, owner:str, balance:float=0, overdraft_limit:float=100):
        assert isinstance(owner, str)
        assert isinstance(balance, (int,float))
        assert isinstance(overdraft_limit, (int,float))

        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount:float):
        assert isinstance(amount, (int,float))

        if amount > 0 and amount <= (self._balance + self.overdraft_limit):
            self._balance -= amount
            self._transactions.append(f'Withdrew ${amount}')
            return True
        return False