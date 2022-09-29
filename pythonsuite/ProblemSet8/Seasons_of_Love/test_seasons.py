import pytest
from seasons import get_birth_date
from datetime import date

#--------------------------------------------------
def test_correct_date():
    assert get_birth_date("1983-07-12") == date(1983, 7, 12)

#--------------------------------------------------
def test_incorrect_date():

    with pytest.raises(SystemExit):
        get_birth_date("198-07-12")

    with pytest.raises(SystemExit):
        get_birth_date("January 1, 1980")

    with pytest.raises(SystemExit):
        get_birth_date("1983-30-01")

    with pytest.raises(SystemExit):
        get_birth_date("1983-01-32")

