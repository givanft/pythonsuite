from plates import is_valid

def test_1():
    assert is_valid("A222") == False

def test_2():
    assert is_valid("A") == False

def test_3():
    assert is_valid("ABCDEFJ") == False

def test_4():
    assert is_valid("AB12FJ") == False

def test_5():
    assert is_valid("AB1256") == True

def test_6():
    assert is_valid("AB056") == False

#def test_7():
#    assert is_valid("AB 56") == False

def test_8():
    assert is_valid("AB.56") == False
