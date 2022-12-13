# -*- coding: cp1251 -*-

n: int = int(input())
out: str = ""

for i in range(n):
    max_n: int = 0
    user_n: int = int(input())

    k: int = 0
    tmp = user_n
    while (tmp > 0):
        k = tmp % 10
        if k > max_n:
            max_n = k
        tmp //= 10

    out += str(max_n)

print(f"{out}")