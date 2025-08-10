class Account:
    def __init__(self, owner:str, balance:float=0):
        assert isinstance(owner, str)
        assert isinstance(balance, (int,float))

        self._owner = owner
        self._balance = balance 
        self._transactions = []  # Transaction history
    
    def deposit(self, amount:float):
        assert isinstance(amount, (int,float))

        if amount > 0:
            self._balance += amount
            self._transactions.append(f'Deposited ${amount}')
            return True
        return False
    
    def withdraw(self, amount:float):
        assert isinstance(amount, (int,float))

        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f'Withdrew ${amount}')
            return True
        return False
    
    def __repr__(self):
        return f'{self._owner} : {self._balance}'
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def owner(self):
        return self._owner