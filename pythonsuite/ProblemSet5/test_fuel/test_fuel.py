import pytest
from fuel import convert, gauge

#--------------------------------------------------
def test_convert_1():
    assert convert("1/4") == 25

def test_convert_2():
    with pytest.raises(ValueError):
        convert("5/2")

def test_convert_3():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
#--------------------------------------------------

def test_gauge_1():
    assert gauge(99) == "F"

def test_gauge_2():
    assert gauge(1) == "E"

def test_gauge_3():
    assert gauge(50) == "50%"