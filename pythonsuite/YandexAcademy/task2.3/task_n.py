# -*- coding: cp1251 -*-
from math import sqrt

n: int = int(input())


maxn = int(sqrt(n))
output: str = "YES"

for i in range(maxn, 1, -1):
    if n % i == 0:
        output = "NO"
        break

if n == 1:
    output = "NO"

print(f"{output}")