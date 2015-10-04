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
