import unittest
from main import *


class MyTestCase(unittest.TestCase):

    def test_paycheck_is_a_multiple_of_50(self):
        self.assertTrue(is_paycheck_amount_correct(50))
        self.assertTrue(is_paycheck_amount_correct(100))
        self.assertTrue(is_paycheck_amount_correct(200))
        self.assertTrue(is_paycheck_amount_correct(550))
        self.assertTrue(is_paycheck_amount_correct(850))
        self.assertTrue(is_paycheck_amount_correct(1000))

    def test_paycheck_is_not_multiple_of_50(self):
        self.assertFalse(is_paycheck_amount_correct(0))
        self.assertFalse(is_paycheck_amount_correct(4))
        self.assertFalse(is_paycheck_amount_correct(9))
        self.assertFalse(is_paycheck_amount_correct(43))
        self.assertFalse(is_paycheck_amount_correct(49))
        self.assertFalse(is_paycheck_amount_correct(51))
        self.assertFalse(is_paycheck_amount_correct(101))
        self.assertFalse(is_paycheck_amount_correct(199))
        self.assertFalse(is_paycheck_amount_correct(248))
        self.assertFalse(is_paycheck_amount_correct(803))

    def test_money_on_the_clients_account_less_than_paycheck(self):
        paycheck = 50
        accountBalance = 70
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance))
        paycheck = 550
        accountBalance = 551
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance))

    def test_money_on_the_clients_account_equal_paycheck(self):
        paycheck = 50
        accountBalance = 50
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance))
        paycheck = 700
        accountBalance = 700
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance))

    def test_paycheck_is_higher_than_money_in_clients_account(self):
        paycheck = 200
        accountBalance = 199
        self.assertFalse(money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance))
        paycheck = 450
        accountBalance = 300
        self.assertFalse(money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance))

    def test_money_on_the_atm_state_higher_than_paycheck(self):
        paycheck = 150
        atmState = 200
        self.assertTrue(money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmState))

    def test_money_on_the_atm_equal_paycheck(self):
        paycheck = 350
        atmState = 350
        self.assertTrue(money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmState))

    def test_money_on_the_atm_state_less_than_paycheck(self):
        paycheck = 500
        atmState = 499
        self.assertFalse(money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmState))

    def test_banknotes_to_be_given_to_clients(self):
        paycheck = 200
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck), (1, 0, 0))
        paycheck = 400
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck), (2, 0, 0))
        paycheck = 850
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck), (4, 0, 1))
        paycheck = 350
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck), (1, 1, 1))
        paycheck = 500
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck), (2, 1, 0))
        paycheck = 50
        self.assertTrue(banknotes_to_be_given_to_clients(paycheck), (0, 0, 1))








