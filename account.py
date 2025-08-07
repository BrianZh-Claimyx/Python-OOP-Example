class Account:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance  # Protected attribute
        self.__transactions = []  # Transaction history
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f'Deposited ${amount}')
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f'Withdrew ${amount}')
            return True
        return False
    
    @property
    def balance(self):
        return self.__balance
    @property
    def owner(self):
        return self.__owner