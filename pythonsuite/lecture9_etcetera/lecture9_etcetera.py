#### MAP ######################################################
# MAP allows you to map a function to a sequence of values.
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words) # < First, it takes a function we want applied to every element of a list. Second, it takes that list itself, to which we'll apply the aforementioned function. 
    print(*uppercased)

if __name__ == "__main__":
    main()


#### ARGS AND KWARGS ######################################################
#def f(*args, **kwargs):
#    print("Named:", kwargs)
#
#f(galleons=100, sickles=50, knuts=25)

#### UNPACK ######################################################
#def total(galleons, sickles, knuts):
#    return (galleons * 17 + sickles) * 29 + knuts
#
#
#coins = {"galleons": 100, "sickles": 50, "knuts": 25}
#
#print(total(**coins), "Knuts")
## --------------------------------------------------------
#def main():
#    yell("This", "is", "CS50")


#def yell(*words):
#    uppercased = []
#    for word in words:
#        uppercased.append(word.upper())
#    print(*uppercased)


#if __name__ == "__main__":
#    main()

### ARGPARSE ######################################################
#import argparse

#parser = argparse.ArgumentParser(description="Meow like a cat")
#parser.add_argument("-n", default=1, help="number of times to meow", type=int)
#args = parser.parse_args()

#for _ in range(args.n):
#    print("meow")

###  CONSTANT | TYPE HINTS | DOCSTRINGS ######################################################
#MEOWS: int = 3
#
#def getmeows(n: int) -> str:
#    """
#    Meow n times.
#    
#    :param n: Number of times to meow
#    :type n: int
#    :raise TypeError: If n is not an int
#    :return: A string of n meows, one per line
#    :rtype: str
#    """
#    return "MEOWS" * n
#
#def main():
#    for _ in range(MEOWS):
#        print(getmeows(MEOWS))
#
#if __name__ == "__main__":
#    main()


###  GLOBAL IN CLASS ######################################################
#class Account:
#    def __init__(self, n = 0):
#        self.balance = n
#
#    @property
#    def balance(self):
#        return self._balance
#
#    @balance.setter
#    def balance(self, n):
#        self._balance = n
#
#    def deposit(self, n):
#        self.balance += n
#
#    def withdraw(self, n):
#        self.balance -= n
#
#    def __del__(self):
#        pass
#
#
#def main():
#    account = Account(50)
#    print("Balance: ", account.balance)
#    account.deposit(100)
#    account.withdraw(50)
#    print("Balance: ", account.balance)
#
#
#if __name__ == "__main__":
#    main()

###  GLOBAL ######################################################
#balance = 0
#
#
#def main():
#    print("Balance:", balance)
#    deposit(100)
#    withdraw(50)
#    print("Balance:", balance)
#    pass
#
#
#def deposit(n):
#    global balance
#    balance += n
#
#
#def withdraw(n):
#    global balance
#    balance -= n
#
#
#if __name__ == "__main__":
#    main()

###  SET ######################################################
## a set of numbers without duplicates
#
#students = [
#    {"name":"ivan", "house":"shymkent"},
#    {"name":"anastasia", "house":"shymkent"},
#    {"name":"sergei", "house":"odincovo"}
#    ]
#
#houses = set()
#for student in students:
#    houses.add(student["house"])
#
#for house in sorted(houses):
#    print(f"{house}")
