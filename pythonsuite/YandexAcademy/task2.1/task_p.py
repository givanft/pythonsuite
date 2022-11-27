a: int = 1
b: int = 100
c: int = 30

dx: int = b - a
out: float = float(dx) / float(c)

print(f"{format(out, '.2f')}")