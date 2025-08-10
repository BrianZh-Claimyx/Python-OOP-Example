from Accounts.account import Account

def access_log(method):
    def wrapper(self, *args, **kwargs):
        if len(args) > 0:
            access_string = f'Performing action {method.__name__} on {args[0]}'
        else:
            access_string = f'Performing action {method.__name__}'

        self._accesslog.append(access_string)
        return method(self, *args, **kwargs)
    return wrapper

class Bank:
    global_interest = 0.04
    def __init__(self, balance:float, accounts:list = [], bank_interest:float = 0.06):
        assert isinstance(balance, (int,float))
        assert isinstance(bank_interest, (int,float))
        assert isinstance(accounts, list)
        for account in accounts:
            assert isinstance(account, Account)

        self._accounts = accounts
        self._accesslog = []
        self._balance = balance # The bank's own balance
        self._bank_interest = bank_interest

    @access_log
    def add_account(self, account : Account):
        assert isinstance(account, Account)
        self._accounts.append(account)

    @access_log
    def remove_account(self, account: Account):
        assert isinstance(account, Account)
        self._accounts.remove(account)
    
    @access_log
    def apply_interest(self):
        rate = self._bank_interest + self.global_interest
        for account in self._accounts:
            account.withdraw(account.balance * rate)

    @property
    @access_log
    def accounts(self):
        return self._accounts
    @property
    @access_log
    def balance(self):
        return self.balance
    @property
    @access_log
    def accesslog(self):
        return self._accesslog