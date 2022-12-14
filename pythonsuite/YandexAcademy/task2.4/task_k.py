# -*- coding: cp1251 -*-
from math import sqrt

n: int = int(input())
count_prime: int = 0

for i in range(n):
    num: int = int(input())
    if num == 2:
        continue
    prime: bool = False
    for j in range(int(sqrt(num)), 1, -1):
        if num % j == 0:
            prime = True
    
    if prime is False:
        count_prime += 1

print(f"{count_prime}")
