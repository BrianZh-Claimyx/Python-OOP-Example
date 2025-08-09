from Accounts.account import Account
from Accounts.savingsaccount import SavingsAccount
from Accounts.checkingaccount import CheckingAccount
from Decorators.transaction_logging_decorator import *
from Tests.tests import run_tests

run_tests()

# attach_logging_decorator(Account, Account.withdraw)
# attach_logging_decorator(Account, Account.deposit)
# attach_logging_decorator(CheckingAccount, CheckingAccount.withdraw)

# brian_account = Account("Brian", 500)
# ido_savings_account = SavingsAccount("Ido", 500)
# sharon_checking_account = CheckingAccount("Sharon", 500)

# brian_account.deposit(200)
# brian_account.withdraw(300)
# ido_savings_account.withdraw(300)
# ido_savings_account.apply_interest()
# sharon_checking_account.withdraw(100)