from account import Account

class Bank:
    def __init__(self, bank_name: str):
        self._name = bank_name
        self._accounts = dict()

    def add_account(self, account_id: str):
        if account_id in self._accounts:
            raise ValueError(f"Account '{account_id}' already in records")
        self._accounts[account_id] = Account()
        