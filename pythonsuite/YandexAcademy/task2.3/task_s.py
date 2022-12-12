# -* - coding: cp1251 -*-
up: int = 1001
dw: int = 1
md: int = (up + dw) // 2

print(f"{md}")

while ((msg := input()) != "Угадал!"):
    if msg == "Больше":
        dw = md
        md = (up + md) // 2
    else:
        up = md
        md = (up + dw) // 2
    
    print(f"{md}")


