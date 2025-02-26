from unittest import TestCase

from bank import Bank


class TestBan(TestCase):
    def test__add_account_to_bank__bank_account_added(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')
        account = new_bank.get_account('1234')
        self.assertEqual(account.get_account_id(), '1234')

    def test__adding_duplicate_account__raises_exception(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')
        with self.assertRaises(ValueError) as em:
            new_bank.add_account('1234')

        self.assertEqual(str(em.exception), "Account '1234' already in records") 

    def test_getting_non_existent_account__raises_exception(self):
        new_bank = Bank('Laxmi Chit Fund')
        with self.assertRaises(ValueError) as em:
            new_bank.get_account('1234')

        self.assertEqual(str(em.exception), "No such account: '1234'")

    def test_crediting_amount_to_account__amount_is_credited_to_account(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')

        new_bank.credit_amount('1234', 100)

        act = new_bank.get_account('1234')
        self.assertEqual(act.get_balance(), 100)

    def test_debiting_amount_to_account__amount_is_debited_from_account(self):
        new_bank = Bank('Laxmi Chit Fund')
        new_bank.add_account('1234')

        new_bank.credit_amount('1234', 100)

        act = new_bank.get_account('1234')
        self.assertEqual(act.get_balance(), 100)

        new_bank.debit_amount('1234', 50)
        


        

