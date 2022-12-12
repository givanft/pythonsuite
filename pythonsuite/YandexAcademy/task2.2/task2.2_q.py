from math import sqrt

a: float = 1#float(input())
b: float = 2#float(input())
c: float = 0#float(input())

d: float = b**2 - (4 * a * c)
y: float = 2 * a
x1: float = 0.0
x2: float = 0.0

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        if c == 0:
            print("0.00")
        else:
            x1 = -c / b
            print(f"{x1.real:.2f}")
else:
    if b == 0:
        if c == 0:
            print("0.00")
        else:
            ca: float = -c / a
            if ca > 0:
                x1 = -sqrt(ca)
                x2 = sqrt(ca)
                if x2 < x1:
                    print(f"{x2.real:.2f} {x1.real:.2f}")
                else:
                    print(f"{x1.real:.2f} {x2.real:.2f}")
            else:
                print("No solution")
    else:
        if c == 0:
            ba: float = -b / a
            if 0 < ba:
                print(f"{0.00} {ba.real:.2f}")
            else:
                print(f"{ba.real:.2f} {0.00}")
        else:
            if d > 0:
                x1 = (-b - sqrt(d)) / y
                x2 = (-b + sqrt(d)) / y
                if x2 < x1:
                    print(f"{x2.real:.2f} {x1.real:.2f}")
                else:
                    print(f"{x1.real:.2f} {x2.real:.2f}")
            elif d == 0:
                x1 = -b / y
                print(f"{x1.real:.2f}")
            else:
                print("No solution")