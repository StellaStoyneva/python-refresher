import unittest
from unittest import TestCase

from sorter import *


class TestSorter(TestCase):
    def test_return_ordered_list_of_bank_accounts_data_in_decending_order_by_balance_and_last_transaction_date(self):
        initial_data = bank_data
        sorter = BancAccountDataSorter(initial_data)
        sorter.get_sorted_data()
        actual = sorter.get_bank_data()
        expected = [{'Peter': {'account': {'balance': 10400, 'last_transaction': '2020-12-15 14:30:00', 'timezone': 'Asia/Singapore'}}}, {'Kevin': {'account': {'balance': 10000, 'last_transaction': '2020-12-13 12:00:00', 'timezone': 'Europe/Vienna'}}}, {'Dave': {'account': {'balance': 1300, 'last_transaction': '2020-12-12 12:00:05', 'timezone': 'UTC'}}}, {'Dohn': {'account': {'balance': 1300, 'last_transaction': '2020-12-12 12:00:00', 'timezone': 'UTC'}}}]
        self.assertDictEqual(actual[0], expected[0])
        self.assertDictEqual(actual[1], expected[1])
        self.assertDictEqual(actual[2], expected[2])
        self.assertDictEqual(actual[3], expected[3])
    def test_raise_exception_on_invalid_initial_data(self):
        initial_data = [{
            'balance': 10000,
            'last_transaction': '2020-12-13 12:00:00',
            'timezone': 'Europe/Vienna'
            },{
                'Peter': {
                    'account': {
                        'balance': 10400,
                        'last_transaction': '2020-12-15 14:30:00',
                        'timezone': 'Asia/Singapore'
                        }
                    }
                },
            ]
        sorter = BancAccountDataSorter(initial_data)
        
        with self.assertRaises(Exception):
            sorter.get_sorted_data()
   

if __name__ == "__main__":
    unittest.main()
    