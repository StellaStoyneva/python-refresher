import unittest
from unittest import TestCase

from phone_number_finder import PhoneNumberFinder
from data import *


class TestProcessRegexMixIn(TestCase):
    '''
    def test_return_first_valid_phone_number_when_two_valid_phone_numbers(self):
        initial_data = phonebook_data
        phonebook = PhoneNumberFinder(initial_data)
        actual = phonebook.get_result(pattern)
        expected = ['John Doe - 0888463789', 'Corey Lee - 052 62-47-72', 'Reece Russell - +359 32 267453', 'James Thomas - (032) 21 18 28']
        self.assertListEqual(actual, expected)s
    '''
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
        phonebook = PhoneNumberFinder(initial_data)
        actual = phonebook.get_result(pattern)
        self.assertEqual(actual, 'Invalid data format')


if __name__ == "__main__":
    unittest.main()