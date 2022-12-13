# -*- coding: cp1251 -*-

n: int = int(input())
rem: int = 0

print(f"А Б В")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        rem = n - (i + j)
        if rem <= 0:
            continue
        print(f"{i} {j} {rem}")