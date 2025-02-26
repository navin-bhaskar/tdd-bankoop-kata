from account import Account

class Bank:
    def __init__(self, bank_name: str):
        self._name = bank_name
        self._accounts = dict()

    def add_account(self, account_id: str):
        if account_id in self._accounts:
            raise ValueError(f"Account '{account_id}' already in records")
        # TODO: Add a builder pattern in future
        self._accounts[account_id] = Account(account_id)
        
    def get_account(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise ValueError(f"No such account: '{account_id}'")
        return self._accounts[account_id]
    
    def credit_amount(self, account_id: str, amount: int):
        account = self.get_account(account_id)
        