x: int = int(input())
y: int = int(input())

n: int = x
m: int = y

while (x != y):
    if x > y:
        x -= y
    else:
        y -= x

print(f"{int((m * n)/x)}")