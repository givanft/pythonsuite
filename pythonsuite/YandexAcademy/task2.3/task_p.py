# -*- coding: cp1251 -*-
m: int = int(input())
last: int = 0

n = m
while (n > 0):
    rem: int = n % 10
    n //= 10
    last += rem

    if n != 0:
        last *= 10

if last == m:
    print("YES")
else:
    print("NO")
