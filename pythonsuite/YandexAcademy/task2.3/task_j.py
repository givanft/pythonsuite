# -*- coding: cp1251 -*-

path: str = ""
step: int = 0

point_x = 0
point_y = 0

while ((path := input()) != "СТОП"):
    step = int(input())

    if path == "СЕВЕР":
        point_y += step
    elif path == "ВОСТОК":
        point_x += step
    elif path == "ЮГ":
        point_y -= step
    elif path == "ЗАПАД":
        point_x -= step

print(f"{point_y}")
print(f"{point_x}")

