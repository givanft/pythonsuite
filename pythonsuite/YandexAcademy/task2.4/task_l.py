# -*- coding: cp1251 -*-

n: int = int(input())
m: int = int(input())

num: int = n * m
tmp: int = num

len_num: int = 0
while (tmp > 0):
    tmp //= 10
    len_num += 1

for i in range(1, num + 1):
    print(f"{str(i).rjust(len_num, ' ')} ", end="")
    
    if i % m == 0:
        print()


