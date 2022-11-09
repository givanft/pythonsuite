from project import is_alphabet, get_string_by_number, get_cipher_key, prepare_cipher_alphabet


def test_is_alphabet():
    assert is_alphabet("Ivan") == True
    assert is_alphabet("1234") == False
    assert is_alphabet("A B") == True
    assert is_alphabet("A.") == False


def test_get_string_by_number():
    assert get_string_by_number(0) == "nil"
    assert get_string_by_number(12) == "twelve"
    assert get_string_by_number(18) == "eighteen"
    assert get_string_by_number(59) == "fiftynine"


def test_get_cipher_key():
    assert get_cipher_key("01/01/2022, 00:00:00") == "nilnilnilonesaturdayjanuary"
    assert get_cipher_key("31/12/2022, 23:59:59") == "fiftyninefiftyninetwentythreethirtyonesaturdaydecember"


def test_prepare_cipher_alphabet():
    assert prepare_cipher_alphabet("01/01/2022, 00:00:00") == "niloesaturdyjbcfghkmpqvwxz"
    assert prepare_cipher_alphabet("31/12/2022, 23:59:59") == "fitynewhrosaudcmbgjklpqvxz"