# -*- coding: cp1251 -*-

x: float = -10#float(input())
y: float = 1#float(input())

alarm: int = 0

if x**2 + y**2 > 100:
    alarm = 2
elif x >= 0 and y >= 0:
    if x**2 + y**2 < 25:
        alarm = 1
elif x <= 0 and y >= 0:
    if x >= -4 and y <= 5:
        alarm = 1
    elif x >= -7 and y <= (1.667 * x + 11.666):
        alarm = 1
elif y < 0:
    y1: float = x**2 / 4 + x / 2 - 8.75
    if y1 < 0:
        if y >= y1:
            alarm = 1

if alarm == 2:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif alarm == 1:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")