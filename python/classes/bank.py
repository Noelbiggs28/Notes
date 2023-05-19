# each user can only access their own info due to self
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
    
    bank_account_one = BankAccount(12345, 300)
    print(bank_account_one)  # returns location in memory of variable