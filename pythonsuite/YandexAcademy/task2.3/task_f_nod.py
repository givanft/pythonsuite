x: int = int(input())
y: int = int(input())

while (x != y):
    if x > y:
        x -= y
    else:
        y -= x

print(f"{x}")
