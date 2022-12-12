# -*- coding: cp1251 -*-

n: int = int(input())
min_name: str = "яяяяяяяяяяяяяяяяяяяяяяяяя"

while ((n := n - 1) > -1):
    name: str = input()
    min_name = min(min_name, name)

print(f"{min_name}")