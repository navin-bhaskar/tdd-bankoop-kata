from account import Account

class Bank:
    def __init__(self, bank_name: str):
        self._name = bank_name
        self._accounts = dict()

    def add_account(self, account_id: str):
        self._accounts[account_id] = Account()
        