
n: int = int(input())
nod: int = 0

for i in range(n):
    x: int = int(input())

    if nod == 0:
        nod = x
        continue

    while (x != nod):
        if x > nod:
            x -= nod
        else:
            nod -= x

print(f"{nod}")