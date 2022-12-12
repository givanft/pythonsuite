# -*- coding: cp1251 -*-

n: int = int(input())
maxn: int = 0

while (n != 0):
    rem: int = n % 10
    if rem > maxn:
        maxn = rem
    n //= 10

print(f"{maxn}")


#n: int = int(input())
#summ: int = 0

#while (n != 0):
#    rem: int = n % 10
#    summ += rem
#    n //= 10

#print(f"{summ}")
