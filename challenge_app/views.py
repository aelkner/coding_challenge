from django.views import generic


# This table is used in convert_integer_to_roman_numerals below.
conversion_table = [
    (None,  'M',    1000),
    ('D',   'C',    100),
    ('L',   'X',    10),
    ('V',   'I',    1),
]


def convert_integer_to_roman_numerals(input_number):
    """
    This function takes an integer number (assumed to be between 1 and 3999)
    and returns a string containing the roman numeral equivalent.  It uses
    the conversion_table above to determine what range the number is in,
    and within that range computes the output for 1-3, 4, 5-8 and 9.  The
    function is then called recursively, passing the remainder, to generate
    the entire result.
    """
    last_one_letter = None
    for five_letter, one_letter, one_value in conversion_table:
        # If we are in the range of the current conversion_table entry
        # then determine the result for that entry and recursively call with
        # the remainder.
        if input_number >= one_value:
            count = input_number / one_value
            remainder = input_number % one_value
            if count == 9:
                roman = '{0}{1}'.format(one_letter, last_one_letter)
            elif count >= 5:
                roman = '{0}{1}'.format(five_letter, one_letter * (count - 5))
            elif count == 4:
                roman = '{0}{1}'.format(one_letter, five_letter)
            else:
                roman = one_letter * count

            # Return the combination of this result with the return value
            # from recursively passing the remainder.
            return '{0}{1}'.format(
                roman, convert_integer_to_roman_numerals(remainder)
            )

        # The current one letter could be used by the next iteration of the
        # loop to build the 9 result.
        last_one_letter = one_letter

    # The recursion ends with an empty result.
    return ''


class HomeView(generic.TemplateView):
    template_name = 'challenge_app/home.html'
