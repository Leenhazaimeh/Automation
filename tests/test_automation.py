from logging import raiseExceptions
from automation import __version__
import re
from automation.automation import*

def test_version():
    assert __version__ == '0.1.0'


def test_phones_and_emails():
    pass


# def test_phone():
#     actual =phone_regex
#     excepted = open("email.txt", "r").read()
#     assert actual == excepted

# def test_email():
#     actual = email_regex
#     excepted = open("email.txt", "r").read()
#     assert actual == excepted