import pytest
from numb3rs import validate

#--------------------------------------------------
def test_validate_1():
    assert validate(".10.13.255") == False

def test_validate_2():
    assert validate("127.0.0.1") == True

def test_validate_3():
    assert validate("cat") == False

def test_validate_4():
    assert validate("275.10.10.255") == False
