# -*- coding: cp1251 -*-

path: str = ""
step: int = 0

point_x = 0
point_y = 0

while ((path := input()) != "����"):
    step = int(input())

    if path == "�����":
        point_y += step
    elif path == "������":
        point_x += step
    elif path == "��":
        point_y -= step
    elif path == "�����":
        point_x -= step

print(f"{point_y}")
print(f"{point_x}")

