# -*- coding: cp1251 -*-

n: int = int(input())
count_bunny: int = 0
bunny_is_here = False

for i in range(n):
    bunny_is_here: bool = False
    while ((st := input()) != "ВСЁ"):
        if st == "зайка":
            bunny_is_here = True
    
    if bunny_is_here is True:
        count_bunny += 1

print(f"{count_bunny}")