import pytest
from working import convert

#--------------------------------------------------
def test_convert_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert_3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_convert_4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

#--------------------------------------------------

def test_convert_6():
    with pytest.raises(ValueError):
        convert("13 AM to 17 PM")

def test_convert_5():
    with pytest.raises(ValueError):
        convert("11:60 AM to 17 PM")

def test_convert_7():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_convert_8():
    with pytest.raises(ValueError):
        convert("09:00 - 17:00")

def test_convert_9():
    with pytest.raises(ValueError):
        convert("9: AM to 9 PM")