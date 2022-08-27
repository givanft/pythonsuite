from bank import value

def test_hi():
    assert value("hi") == 20

def test_hello():
    assert value("hello") == 0

def test_hello_upper():
    assert value("HELLO") == 0

def test_whatsup():
    assert value("What's up") == 100