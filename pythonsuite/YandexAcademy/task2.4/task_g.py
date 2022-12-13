# -*- coding: cp1251 -*-

START_SEC = 3

n: int = int(input())
start_from: int = START_SEC

for i in range(n):

    while (start_from > 0):
        print(f"До старта {start_from} секунд(ы)")
        start_from -= 1

    print(f"Старт {i + 1}!!!")

    start_from = START_SEC + (i + 1)

