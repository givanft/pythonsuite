e = 7
d = e
fi = 8

r = 0
while r != 1:
    d += 1
    r = (d * e) % fi

print(f"{d}")