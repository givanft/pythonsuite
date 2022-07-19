def Main():
    x = int(input("What is x? "))
    print(f"x squared is {Square(x)}")

def Square(n):
    return pow(n, 2)

Main()
#print(name)