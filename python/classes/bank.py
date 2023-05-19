class BankAccount:

    def __init__(self, account_ID, balance):
        self._account_ID = account_ID
        self._balance = balance
    
    def get_account_ID(self): 
        return self._account_ID
    
    def set_account_ID(self, new_ID):
        self._account_ID = new_ID

    def get_balance(self):
        return self._balance