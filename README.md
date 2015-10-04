# coding_challenge
Coding Challenge for Celerity

This repository contains a django site that can be used as a integer to
roman numeral calculator as specified in Celerity's coding challenge page
found at:

www.evernote.com/shard/s268/sh/7e54b25f-79a6-4274-ba38-00dbf0bcd8e0/115a6d3091231709

It has one page that presents a form for the calculator with the input field
receiving the focus and the entire text selected to make it convenient to
quickly test many numbers in a row without needing to use the mouse.  There are
unit tests for the function that does the conversion calculation as well as
user interface tests to test the behaviour of the form when invalid or valid
input is entered by the user.

The following are the instructions for cloning the repo and getting it to
run on any unix system (assuming virtualenv-2.7 is installed):

git clone git@github.com:aelkner/coding_challenge.git
cd coding_challenge
virtualenv-2.7 --distribute venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py test challenge_app
    (all tests pass)
python manage.py migrate
    (not needed as this app has no need for a database, but to avoid the
     red warning message when running the server)
python manage.py runserver
    (visit http://localhost:8000/ in the browser)
