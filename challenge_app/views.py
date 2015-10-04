from django import forms
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


class HomeForm(forms.Form):
    input_number = forms.CharField(
        label='Integer number',
        widget = forms.TextInput(attrs={
            'placeholder': "Please enter an integer between 1 and 3999",
            'size': 50,
        })
    )

    def clean_input_number(self):
        """
        Make sure the input number is a number between 1 and 3999.
        """
        input_number = self.cleaned_data.get("input_number", "")
        if (
            input_number.isdigit()
            and int(input_number) > 0
            and int(input_number) < 4000
        ):
            return input_number
        raise forms.ValidationError(
            "Please enter an integer between 1 and 3999."
        )


class HomeView(generic.FormView):
    """
    This view presents a form to the user with an input box for entering an
    integer between 1 and 3999 and a button to convert the number into roman
    numerals and display that result.
    """
    template_name = 'challenge_app/home.html'
    form_class = HomeForm

    def form_valid(self, form):
        """
        In order for the user to be able to continue to use the converter
        after successfully filling in the form with valid input, call
        form_invalid to avoid the redirect to success_url.
        """
        return self.form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        """
        If the form is passed, get the input_number from its cleaned_data and
        convert it to roman numerals, putting the result into context_data
        under the key, 'roman', for the template to use in displaying the
        answer.
        """
        context_data = super(HomeView, self).get_context_data(*args, **kwargs)
        cleaned_data = getattr(kwargs['form'], 'cleaned_data', {})
        input_number = cleaned_data.get('input_number', '')
        if input_number:
            context_data['roman'] = convert_integer_to_roman_numerals(
                int(input_number)
            )
        else:
            context_data['roman'] = ''
        return context_data
