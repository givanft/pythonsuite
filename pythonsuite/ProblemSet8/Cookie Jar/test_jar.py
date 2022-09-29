import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(2)
    assert jar2.capacity == 2
    with pytest.raises(ValueError):
        jar.deposit(50)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    jar.deposit(5)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(50)

def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(50)