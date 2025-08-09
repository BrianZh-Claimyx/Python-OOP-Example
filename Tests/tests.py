from Accounts.account import Account
from Accounts.savingsaccount import SavingsAccount
from Accounts.checkingaccount import CheckingAccount
from Decorators.transaction_logging_decorator import *
from Notification.create_notifier import attach_notifier

def run_tests():
    test_notifier()

def test_account_decorator():
    attach_logging_decorator(Account, Account.withdraw)
    account = Account("Brian", 500)
    account.withdraw(200)

def test_notifier():
    class someobserver:
        def update(self, notifier):
            print(f'{notifier} fired an event')
    observer = someobserver()

    notifyingaccount = Account("NotifyingAccount", 500)
    attach_notifier(notifyingaccount, [Account.withdraw, Account.deposit])
    notifyingaccount.attach(observer)
    notifyingaccount.withdraw(100)
    

