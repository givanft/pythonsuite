# -*- coding: cp1251 -*-

petr: int = int(input())
vasya: int = int(input())
tolya: int = int(input())

if vasya < petr > tolya:
    print("1. ����")
    if vasya > tolya:
        print("2. ����")
        print("3. ����")
    else:
        print("2. ����")
        print("3. ����")

elif petr < vasya > tolya:
    print("1. ����")
    if petr > tolya:
        print("2. ����")
        print("3. ����")
    else:
        print("2. ����")
        print("3. ����")

elif petr < tolya > vasya:
    print("1. ����")
    if petr > vasya:
        print("2. ����")
        print("3. ����")
    else:
        print("2. ����")
        print("3. ����")


