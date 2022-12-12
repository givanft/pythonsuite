# -*- coding: cp1251 -*-

year: int = int(input())
answ: str = "NO"

if year % 4 == 0:
    if year % 100 != 0:
        answ = "YES"

print(answ)