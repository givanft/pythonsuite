# -*- coding: cp1251 -*-
n: int = int(input())
count_bunny: int = 0

while ((n := n - 1) > -1):
    s: str = input()
    if "зайка" in s:
        count_bunny += 1

print(f"{count_bunny}")