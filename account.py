class Account:

    def __init__(self, account_id: str):
        self._account_id =account_id
        self._balance = 0
        # Future use
        self.history = []

    def get_account_id(self):
        return self._account_id
    
    def credit_amount(self, amt: int):
        self._balance += amt

    def get_balance(self):
        return self._balance
    