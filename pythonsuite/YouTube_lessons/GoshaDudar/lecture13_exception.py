try:
    a = int(input("x? "))
    b = 0
    c = a/b
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("exception")
finally:
    print(c)
