# -*- coding: cp1251 -*-

a: int = int(input())
b: int = int(input())
c: int = int(input())

a = a**2
b = b**2
c = c**2

t: int = c

if a >= b and a >= c:
    c = a
    a = t

if b >= a and b >= c:
    c = b
    b = t

dx: int = a + b

if c == dx:
    print("100%")
elif c > dx:
    print("велика")
else:
    print("крайне мала")
