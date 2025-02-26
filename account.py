class Account:

    def __init__(self, account_id: str):
        self._account_id =account_id
        self._balance = 0
        # Future use
        self.history = []

    def get_account_id(self):
        return self._account_id
    