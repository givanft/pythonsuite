# -*- coding: cp1251 -*-

START_SEC = 3

n: int = int(input())
start_from: int = START_SEC

for i in range(n):

    while (start_from > 0):
        print(f"�� ������ {start_from} ������(�)")
        start_from -= 1

    print(f"����� {i + 1}!!!")

    start_from = START_SEC + (i + 1)

