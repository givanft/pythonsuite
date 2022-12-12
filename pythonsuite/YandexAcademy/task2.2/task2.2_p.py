# -*- coding: cp1251 -*-


p: int = int(input())
v: int = int(input())
t: int = int(input())

line_const_len: int = 8

if p >= v and p >= t:
    print(f"{' '.center(line_const_len, ' ')}{'Петя'.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}")
    if v >= t:
        print(f"{'Вася'.center(line_const_len, ' ')}")
        print(f"{' '.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}{'Толя'.center(line_const_len, ' ')}")
    else:
        print(f"{'Толя'.center(line_const_len, ' ')}")
        print(f"{' '.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}{'Вася'.center(line_const_len, ' ')}")

if v >= p and v >= t:
    print(f"{' '.center(line_const_len, ' ')}{'Вася'.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}")
    if p > t:
        print(f"{'Петя'.center(line_const_len, ' ')}")
        print(f"{' '.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}{'Толя'.center(line_const_len, ' ')}")
    else:
        print(f"{'Толя'.center(line_const_len, ' ')}")
        print(f"{' '.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}{'Петя'.center(line_const_len, ' ')}")

if t >= p and t >= v:
    print(f"{' '.center(line_const_len, ' ')}{'Толя'.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}")
    if p >= v:
        print(f"{'Петя'.center(line_const_len, ' ')}")
        print(f"{' '.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}{'Вася'.center(line_const_len, ' ')}")
    else:
        print(f"{'Вася'.center(line_const_len, ' ')}")
        print(f"{' '.center(line_const_len, ' ')}{' '.center(line_const_len, ' ')}{'Петя'.center(line_const_len, ' ')}")

print(f"{'II'.center(line_const_len, ' ')}{'I'.center(line_const_len, ' ')}{'III'.center(line_const_len, ' ')}")