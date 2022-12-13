# -*- coding: cp1251 -*-

n: int = int(input())
max_n: int = 0
his_name: str = ""

for i in range(n):
    user_name: str = input()
    user_num: int = int(input())

    sum_n = 0
    tmp_n = user_num

    while (tmp_n > 0):
        sum_n += tmp_n % 10
        tmp_n //= 10

    if sum_n >= max_n:
        max_n = sum_n
        his_name = user_name

print(f"{his_name}")
