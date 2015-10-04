from bs4 import BeautifulSoup

from django.test import TestCase

import views

# Create your tests here.
class UnitTest(TestCase):
    def test_convert_integer_to_roman_numerals(self):
        """
        Tests for various values passed to convert_integer_to_roman_numerals.
        """
        def assert_convert_integer_to_roman_numerals(integer, roman):
            self.assertEqual(
                views.convert_integer_to_roman_numerals(integer), roman
            )

        assert_convert_integer_to_roman_numerals(6,     'VI')
        assert_convert_integer_to_roman_numerals(9,     'IX')
        assert_convert_integer_to_roman_numerals(18,    'XVIII')
        assert_convert_integer_to_roman_numerals(19,    'XIX')
        assert_convert_integer_to_roman_numerals(38,    'XXXVIII')
        assert_convert_integer_to_roman_numerals(39,    'XXXIX')
        assert_convert_integer_to_roman_numerals(40,    'XL')
        assert_convert_integer_to_roman_numerals(98,    'XCVIII')
        assert_convert_integer_to_roman_numerals(388,   'CCCLXXXVIII')
        assert_convert_integer_to_roman_numerals(499,   'CDXCIX')
        assert_convert_integer_to_roman_numerals(867,   'DCCCLXVII')
        assert_convert_integer_to_roman_numerals(1998,  'MCMXCVIII')
        assert_convert_integer_to_roman_numerals(3999,  'MMMCMXCIX')


class ClientTest(TestCase):
    def test_convert_integer_to_roman_numerals(self):
        INVALID_ERROR = 'Please enter an integer between 1 and 3999.'

        # Doing a get on the view yields a form with a blank input_number
        # field and no results.
        self.response = self.client.get('/')
        soup = BeautifulSoup(self.response.content)
        self.assertIsNone(soup.find(id='id_input_number').get('value'))
        self.assertIsNone(soup.find(id='id_roman_numerals'))

        # Posting no input_number yields the missing field error.
        self.response = self.client.post('/', {})
        soup = BeautifulSoup(self.response.content)
        self.assertEqual(
            soup.select('.errorlist li')[0].string,
            'This field is required.'
        )
        self.assertIsNone(soup.find(id='id_roman_numerals'))

        # Posting a non-integer yields the invalid field error.
        self.response = self.client.post('/', {'input_number': 'foo'})
        soup = BeautifulSoup(self.response.content)
        self.assertEqual(
            soup.select('.errorlist li')[0].string, INVALID_ERROR
        )
        self.assertIsNone(soup.find(id='id_roman_numerals'))

        # Posting an integer < 1 yields the invalid field error.
        self.response = self.client.post('/', {'input_number': '0'})
        soup = BeautifulSoup(self.response.content)
        self.assertEqual(
            soup.select('.errorlist li')[0].string, INVALID_ERROR
        )
        self.assertIsNone(soup.find(id='id_roman_numerals'))

        # Posting an integer > 3999 yields the invalid field error.
        self.response = self.client.post('/', {'input_number': '4000'})
        soup = BeautifulSoup(self.response.content)
        self.assertEqual(
            soup.select('.errorlist li')[0].string, INVALID_ERROR
        )
        self.assertIsNone(soup.find(id='id_roman_numerals'))

        # Posting a valid number yields no errors but rather a
        # successfully converted result.
        self.response = self.client.post('/', {'input_number': '1'})
        soup = BeautifulSoup(self.response.content)
        self.assertFalse(soup.select('.errorlist li'))
        self.assertEqual(
            soup.find(id='id_roman_numerals').string.strip(),
            'I'
        )

        # Posting another valid number yields success again.
        self.response = self.client.post('/', {'input_number': '3999'})
        soup = BeautifulSoup(self.response.content)
        self.assertFalse(soup.select('.errorlist li'))
        self.assertEqual(
            soup.find(id='id_roman_numerals').string.strip(),
            'MMMCMXCIX'
        )
