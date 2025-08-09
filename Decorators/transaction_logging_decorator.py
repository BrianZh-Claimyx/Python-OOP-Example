def transaction_logging_decorator(func):
    def wrapper(*args, **kwargs):
        pre_transaction_balance = args[0].balance
        result = func(*args, **kwargs)
        print(f'{args[0].owner}\'s account - Action: {func.__name__}'
               f' - Previous Balance: {pre_transaction_balance}'
               f' - New Balance: {args[0].balance}')
        return result
    return wrapper

def attach_logging_decorator(cls, method):
    wrapped = transaction_logging_decorator(method)
    setattr(cls, method.__name__, wrapped)