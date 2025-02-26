from unittest import TestCase

from bank import Bank


class TestBan(TestCase):
    def test__add_account_to_bank__bank_acount_added(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')
        

