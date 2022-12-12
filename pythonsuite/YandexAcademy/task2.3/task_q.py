# -*- coding: cp1251 -*-

n: int = int(input())
last: int = 0

while (n > 0):
    rem: int = n % 10
    n //= 10

    if rem % 2 == 0:
        continue
    
    last += rem

    if n != 0:
        last *= 10

n = last
last = 0

while (n > 0):
    rem: int = n % 10
    n //= 10

    if rem % 2 == 0:
        continue
    
    last += rem

    if n != 0:
        last *= 10

print(f"{last}")
