import unittest
from main import *
from customer import *


class MyTestCase(unittest.TestCase):

    def test_find_customer(self):
        idEntered = 10
        customer01 = Customer(10, 5236, 1500)
        customer02 = Customer(20, 1234, 150)
        customersList = [customer01, customer02]
        self.assertTrue(find_customer(idEntered, customersList))
        idEntered = 20
        self.assertTrue(find_customer(idEntered, customersList))
        idEntered = 50
        self.assertFalse(find_customer(idEntered, customersList))
        idEntered = 0
        self.assertFalse(find_customer(idEntered, customersList))

    def test_withdrawal_amount_is_correct(self):
        self.assertTrue(is_withdrawal_amount_correct(50))
        self.assertTrue(is_withdrawal_amount_correct(100))
        self.assertTrue(is_withdrawal_amount_correct(200))
        self.assertTrue(is_withdrawal_amount_correct(550))
        self.assertTrue(is_withdrawal_amount_correct(850))
        self.assertTrue(is_withdrawal_amount_correct(1000))

    def test_withdrawal_amount_is_not_correct(self):
        self.assertFalse(is_withdrawal_amount_correct(0))
        self.assertFalse(is_withdrawal_amount_correct(4))
        self.assertFalse(is_withdrawal_amount_correct(9))
        self.assertFalse(is_withdrawal_amount_correct(43))
        self.assertFalse(is_withdrawal_amount_correct(49))
        self.assertFalse(is_withdrawal_amount_correct(51))
        self.assertFalse(is_withdrawal_amount_correct(101))
        self.assertFalse(is_withdrawal_amount_correct(199))
        self.assertFalse(is_withdrawal_amount_correct(248))
        self.assertFalse(is_withdrawal_amount_correct(803))

    def test_money_on_the_clients_account_less_than_withdrawal(self):
        withdrawal = 50
        accountBalance = 70
        self.assertTrue(money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, accountBalance))
        withdrawal = 550
        accountBalance = 551
        self.assertTrue(money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, accountBalance))

    def test_money_on_the_clients_account_equal_withdrawal(self):
        withdrawal = 50
        accountBalance = 50
        self.assertTrue(money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, accountBalance))
        withdrawal = 700
        accountBalance = 700
        self.assertTrue(money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, accountBalance))

    def test_withdrawal_is_higher_than_money_in_clients_account(self):
        withdrawal = 200
        accountBalance = 199
        self.assertFalse(money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, accountBalance))
        withdrawal = 450
        accountBalance = 300
        self.assertFalse(money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, accountBalance))

    def test_money_on_the_atm_state_higher_than_withdrawal(self):
        withdrawal = 150
        atmBalance = 200
        self.assertTrue(money_on_the_atm_state_higher_equal_than_withdrawal(withdrawal, atmBalance))

    def test_money_on_the_atm_equal_withdrawal(self):
        withdrawal = 350
        atmBalance = 350
        self.assertTrue(money_on_the_atm_state_higher_equal_than_withdrawal(withdrawal, atmBalance))

    def test_money_on_the_atm_state_less_than_withdrawal(self):
        withdrawal = 500
        atmBalance = 499
        self.assertFalse(money_on_the_atm_state_higher_equal_than_withdrawal(withdrawal, atmBalance))

    def test_banknotes_to_be_given_to_clients(self):
        withdrawal = 200
        self.assertEqual(banknotes_to_be_given_to_clients(withdrawal), (1, 0, 0))
        withdrawal = 400
        self.assertEqual(banknotes_to_be_given_to_clients(withdrawal), (2, 0, 0))
        withdrawal = 850
        self.assertEqual(banknotes_to_be_given_to_clients(withdrawal), (4, 0, 1))
        withdrawal = 350
        self.assertEqual(banknotes_to_be_given_to_clients(withdrawal), (1, 1, 1))
        withdrawal = 500
        self.assertEqual(banknotes_to_be_given_to_clients(withdrawal), (2, 1, 0))
        withdrawal = 50
        self.assertEqual(banknotes_to_be_given_to_clients(withdrawal), (0, 0, 1))








