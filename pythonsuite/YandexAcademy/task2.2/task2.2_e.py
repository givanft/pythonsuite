# -*- coding: cp1251 -*-

petr: int = int(input())
vasya: int = int(input())
tolya: int = int(input())

if vasya < petr > tolya:
    print("1. Петя")
    if vasya > tolya:
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася")

elif petr < vasya > tolya:
    print("1. Вася")
    if petr > tolya:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")

elif petr < tolya > vasya:
    print("1. Толя")
    if petr > vasya:
        print("2. Петя")
        print("3. Вася")
    else:
        print("2. Вася")
        print("3. Петя")


