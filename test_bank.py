from unittest import TestCase

from bank import Bank


class TestBan(TestCase):
    def test__add_account_to_bank__bank_account_added(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')

    def test__adding_duplicate_account__raises_exception(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')
        with self.assertRaises(ValueError) as em:
            new_bank.add_account('1234')

        self.assertEqual(str(em.exception), "Account '1234' already in records") 
        

