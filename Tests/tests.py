from Accounts.account import Account
from Accounts.savingsaccount import SavingsAccount
from Accounts.checkingaccount import CheckingAccount
from Decorators.transaction_logging_decorator import *
from Notification.create_notifier import attach_notifier
from Accounts.bank import Bank

def run_tests():
    print("### TESTING DECORATOR ###")
    test_account_decorator()
    print("### TESTING NOTIFIER ###")
    test_notifier()
    print("### TESTING BANK ###")
    test_bank()


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
    
def test_bank():
    bank = Bank(1000, [Account("Brian", 500), 
                       CheckingAccount("Ido", 500, 100),
                       SavingsAccount("Sharon", 500)])
    
    someaccount = Account("Some", 5000)
    bank.add_account(someaccount)
    bank.apply_interest()
    print(str(bank.accounts))
    print(str(bank.accesslog))
    bank.remove_account(someaccount)
