import unittest
from unittest import TestCase

from process_regex_mixin import ProcessRegexMixIn
from data import *


class TestProcessRegexMixIn(TestCase):
    def test_return_first_valid_phone_number_when_two_valid_phone_numbers(self):
        input_data = '0888463789 / /032/ 26 74 27'
        actual = ProcessRegexMixIn.find_first_match(input_data, pattern)
        expected = '0888463789'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
    