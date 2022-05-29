import unittest
import main
from main import *





class MyTestCase(unittest.TestCase):

    def test_paycheck_is_a_multipe_of_50(self):
        self.assertTrue(paycheck_is_a_multipe_of_50(50))
        self.assertTrue(paycheck_is_a_multipe_of_50(100))
        self.assertTrue(paycheck_is_a_multipe_of_50(200))
        self.assertTrue(paycheck_is_a_multipe_of_50(550))
        self.assertTrue(paycheck_is_a_multipe_of_50(850))
        self.assertTrue(paycheck_is_a_multipe_of_50(1000))

    def test_paycheck_is_not_multipe_of_50(self):
        self.assertFalse(paycheck_is_a_multipe_of_50(0))
        self.assertFalse(paycheck_is_a_multipe_of_50(4))
        self.assertFalse(paycheck_is_a_multipe_of_50(9))
        self.assertFalse(paycheck_is_a_multipe_of_50(43))
        self.assertFalse(paycheck_is_a_multipe_of_50(49))
        self.assertFalse(paycheck_is_a_multipe_of_50(51))
        self.assertFalse(paycheck_is_a_multipe_of_50(101))
        self.assertFalse(paycheck_is_a_multipe_of_50(199))
        self.assertFalse(paycheck_is_a_multipe_of_50(248))
        self.assertFalse(paycheck_is_a_multipe_of_50(803))

    def test_money_on_the_clients_account_less_than_paycheck(self):
        paycheck = 50
        accountBalans= 70
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck,accountBalans))
        paycheck = 550
        accountBalans = 551
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck,accountBalans))

    def test_money_on_the_clients_account_equal_paycheck(self):
        paycheck = 50
        accountBalans = 50
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck,accountBalans))
        paycheck = 700
        accountBalans = 700
        self.assertTrue(money_on_the_clients_account_less_equal_than_paycheck(paycheck,accountBalans))

    def test_paycheck_is_higher_than_money_in_clients_account(self):
        paycheck = 200
        accountBalans = 199
        self.assertFalse(money_on_the_clients_account_less_equal_than_paycheck(paycheck,accountBalans))
        paycheck = 450
        accountBalans = 300
        self.assertFalse(money_on_the_clients_account_less_equal_than_paycheck(paycheck,accountBalans))

    def test_money_on_the_atm_state_higher_than_paycheck(self):
        paycheck = 150
        atmState = 200
        self.assertTrue(money_on_the_atm_state_higher_equal_than_paycheck(paycheck,atmState))

    def test_money_on_the_atm_equal_paycheck(self):
        paycheck = 350
        atmState = 350
        self.assertTrue(money_on_the_atm_state_higher_equal_than_paycheck(paycheck,atmState))

    def test_money_on_the_atm_state_less_than_paycheck(self):
        paycheck = 500
        atmState = 499
        self.assertFalse(money_on_the_atm_state_higher_equal_than_paycheck(paycheck,atmState))

    def test_banknotes_to_be_given_to_clients(self):
        paycheck = 200
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck),(1,0,0))
        paycheck = 400
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck),(2,0,0))
        paycheck = 850
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck),(4,0,1))
        paycheck = 350
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck),(1,1,1))
        paycheck = 500
        self.assertEqual(banknotes_to_be_given_to_clients(paycheck),(2,1,0))
        paycheck = 50
        self.assertTrue(banknotes_to_be_given_to_clients(paycheck),(0,0,1))







if __name__ == '__main__':
    unittest.main()
